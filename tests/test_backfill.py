import httpx
import pytest

from mediascrapers.models import post_guid
from mediascrapers.x import backfill
from mediascrapers.x.backfill import (
    id_prefixes,
    list_archived_ids,
    parse_fxtwitter,
    snowflake_floor,
    spread_quota,
)


def test_snowflake_floor_is_monotonic():
    assert snowflake_floor(2022) < snowflake_floor(2023) < snowflake_floor(2026)


def test_id_prefixes_cover_period():
    prefixes = id_prefixes(2022)
    assert prefixes[0] == str(snowflake_floor(2022))[:2]
    assert len(prefixes) >= 2


def test_spread_quota_is_shared_across_slices():
    old = {snowflake_floor(2022) + i for i in range(100)}
    new = {snowflake_floor(2025) + i for i in range(100)}
    ids = spread_quota([old, new], 10)
    assert len(ids) == 10
    assert sum(int(i) < snowflake_floor(2025) for i in ids) == 5


async def test_cdx_queries_both_domains_and_filters_by_year():
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.params["url"])
        recent = snowflake_floor(2025) + 5
        old = snowflake_floor(2019) + 5
        return httpx.Response(200, text=f"x.com/h/status/{recent}\nx.com/h/status/{old}\n")

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        ids = await list_archived_ids(http, "h", since_year=2022, limit=50, pause=0)
    assert all(int(i) >= snowflake_floor(2022) for i in ids)
    assert any(c.startswith("x.com/") for c in calls) and any(c.startswith("twitter.com/") for c in calls)


async def test_cdx_failure_yields_empty():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(504)

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        assert await list_archived_ids(http, "h", since_year=2022, limit=10, pause=0) == []


FX = {"tweet": {
    "id": "2091800582042333264", "url": "https://x.com/J_Bardella/status/2091800582042333264",
    "text": "Texte complet", "created_at": "Mon Aug 24 08:11:37 +0000 2026",
    "author": {"screen_name": "J_Bardella"}, "likes": 10, "retweets": 2, "replies": 1, "views": 500,
    "lang": "fr",
}}


def test_fxtwitter_normalisation_and_shared_guid():
    p = parse_fxtwitter(FX, "J_Bardella")
    assert p.text == "Texte complet" and p.views == 500 and p.post_type == "original"
    assert p.published_at.isoformat() == "2026-08-24T08:11:37+00:00"
    assert p.guid == post_guid("J_Bardella", p.url)
    assert p.guid == post_guid("j_bardella", "https://twitter.com/J_Bardella/status/2091800582042333264")


def test_fxtwitter_other_author_is_retweet():
    data = {"tweet": {**FX["tweet"], "author": {"screen_name": "someone"}}}
    p = parse_fxtwitter(data, "J_Bardella")
    assert p.post_type == "retweet" and p.quoted_handle == "someone"


def test_fxtwitter_empty_is_none():
    assert parse_fxtwitter({"tweet": {"id": "1", "text": ""}}, "h") is None


@pytest.mark.parametrize("status", [404, 500])
async def test_fetch_tweet_unavailable(status):
    async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(status))) as http:
        assert await backfill.fetch_tweet(http, "h", "1") is None


def test_fxtwitter_graph_fields():
    data = {"tweet": {
        **FX["tweet"],
        "text": "Réponse à @MeteoFrance sur #DANA https://example.org/x https://t.co/zz",
        "author": {"screen_name": "J_Bardella", "id": "42"},
        "replying_to": "MeteoFrance", "replying_to_status": "7", "source": "Twitter Web App",
        "quote": {"url": "https://x.com/q/status/9", "text": "cité",
                  "author": {"screen_name": "q", "id": "9"}},
    }}
    p = parse_fxtwitter(data, "J_Bardella")
    assert p.tweet_id == "2091800582042333264" and p.author_id == "42"
    assert p.reply_to_url == "https://x.com/MeteoFrance/status/7"
    assert p.source == "Twitter Web App"
    assert p.mentions == ["MeteoFrance"] and p.hashtags == ["DANA"]
    assert p.urls == ["https://example.org/x"]
    assert p.quoted_user_id == "9"
