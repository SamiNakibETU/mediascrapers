"""Recent timeline of an X account through the public syndication endpoint.

``syndication.twitter.com/srv/timeline-profile/screen-name/<handle>`` is the
service behind embedded timelines. It returns a Next.js page whose
``__NEXT_DATA__`` block holds the last 20 to 100 tweets with full text, dates,
engagement counts and retweet/quote/reply structure. No account, cookie or
proxy is required.

Known limits: no pagination, and long "note tweets" arrive cut at 280
characters (see ``Post.text_truncated``; ``backfill.fetch_tweet`` returns the
full text by id).
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
from datetime import UTC, datetime

import httpx

from mediascrapers.http import HttpConfig, RateLimit, client, is_cloudflare_challenge
from mediascrapers.models import Post, PostType, Profile, post_guid

log = logging.getLogger(__name__)

SYNDICATION_URL = "https://syndication.twitter.com/srv/timeline-profile/screen-name/{handle}"
COLLECTED_VIA = "syndication"
TRUNCATION_HINT = 270

_NEXT_DATA_RE = re.compile(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S)
_DATE_FMT = "%a %b %d %H:%M:%S %z %Y"
_URL_STUBS = tuple("https://t.co/"[:n] for n in range(len("https://t.co/"), 0, -1))


def _parse_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    try:
        return datetime.strptime(raw, _DATE_FMT).astimezone(UTC)
    except ValueError:
        return None


def _expand_urls(text: str, entities: dict | None) -> str:
    for u in (entities or {}).get("urls") or []:
        short, full = u.get("url"), u.get("expanded_url")
        if short and full:
            text = text.replace(short, full)
    return text


def _trim_cut_link(text: str, *, truncated: bool) -> str:
    """Drop the dangling ``htt`` / ``https://t.c`` left when a tweet is cut mid-link."""
    if not truncated:
        return text
    head, sep, tail = text.rstrip().rpartition(" ")
    if sep and tail in _URL_STUBS:
        return head.rstrip()
    return text


def _media_url(tweet: dict) -> str | None:
    """First media item; for videos, the highest-bitrate mp4 variant."""
    ext = tweet.get("extended_entities") or tweet.get("entities") or {}
    for m in ext.get("media") or []:
        if m.get("type") in ("video", "animated_gif"):
            variants = [
                v for v in (m.get("video_info") or {}).get("variants") or []
                if v.get("content_type") == "video/mp4" and v.get("url")
            ]
            if variants:
                return max(variants, key=lambda v: v.get("bitrate") or 0)["url"]
        return m.get("media_url_https") or m.get("media_url")
    return None


def _entries(html: str) -> list[dict]:
    m = _NEXT_DATA_RE.search(html or "")
    if not m:
        return []
    try:
        return json.loads(m.group(1))["props"]["pageProps"]["timeline"]["entries"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return []


def _to_post(tweet: dict, handle: str) -> Post | None:
    tid = tweet.get("id_str")
    if not tid:
        return None
    author = (tweet.get("user") or {}).get("screen_name") or handle
    retweeted = tweet.get("retweeted_status")
    quoted = tweet.get("quoted_status")
    reply_to = tweet.get("in_reply_to_screen_name")

    body = retweeted or tweet
    raw = body.get("full_text") or body.get("text") or ""
    # display_text_range bounds the displayed text, in code points: it strips
    # leading @mentions of a reply and the trailing media link.
    rng = body.get("display_text_range") or [0, len(raw)]
    try:
        start, end = int(rng[0]), int(rng[1])
        runes = list(raw)
        shown = "".join(runes[start:end]) if 0 <= start <= end <= len(runes) else raw
    except (TypeError, ValueError):
        shown, start, end = raw, 0, len(raw)
    text = _expand_urls(shown, body.get("entities")).strip()
    if not text:
        return None
    truncated = (end - start) >= TRUNCATION_HINT
    text = _trim_cut_link(text, truncated=truncated)

    post_type: PostType = (
        "retweet" if retweeted is not None
        else "quote" if quoted is not None
        else "reply" if reply_to
        else "original"
    )
    url = f"https://x.com/{author}/status/{tid}"
    post = Post(
        guid=post_guid(handle, url),
        handle=handle,
        url=url,
        text=text,
        published_at=_parse_date(tweet.get("created_at")),
        post_type=post_type,
        lang=(tweet.get("lang") or "fr")[:8],
        reply_to_handle=reply_to,
        reply_to_url=(
            f"https://x.com/{reply_to}/status/{tweet['in_reply_to_status_id_str']}"
            if reply_to and tweet.get("in_reply_to_status_id_str") else None
        ),
        media_url=_media_url(body),
        likes=tweet.get("favorite_count"),
        retweets=tweet.get("retweet_count"),
        replies=tweet.get("reply_count"),
        quotes=tweet.get("quote_count"),
        text_truncated=truncated,
        collected_via=COLLECTED_VIA,
    )

    # The carried tweet (quoted or retweeted) is the amplification target.
    carried = quoted if quoted is not None else retweeted
    if carried is not None:
        c_user = (carried.get("user") or {}).get("screen_name")
        c_id = carried.get("id_str")
        post.quoted_handle = c_user
        post.quoted_url = f"https://x.com/{c_user}/status/{c_id}" if c_user and c_id else None
        if quoted is not None:
            post.quoted_text = _expand_urls(
                quoted.get("full_text") or quoted.get("text") or "", quoted.get("entities")
            )[:2000] or None
    return post


def parse_timeline(html: str, handle: str) -> list[Post]:
    out: list[Post] = []
    for e in _entries(html):
        tweet = (e.get("content") or {}).get("tweet")
        if tweet and (p := _to_post(tweet, handle)):
            out.append(p)
    return out


def parse_profile(html: str, handle: str) -> Profile | None:
    for e in _entries(html):
        u = ((e.get("content") or {}).get("tweet") or {}).get("user") or {}
        if (u.get("screen_name") or "").lower() == handle.lower():
            return Profile(
                handle=handle,
                user_id=u.get("id_str"),
                followers=u.get("followers_count"),
                statuses=u.get("statuses_count"),
                protected=bool(u.get("protected", False)),
            )
    return None


def timeline_state(html: str) -> str:
    """``ok`` when the page holds tweets, ``empty`` otherwise (protected, suspended, silent)."""
    return "ok" if any((e.get("content") or {}).get("tweet") for e in _entries(html)) else "empty"


class SyndicationClient:
    """Serial, rate-limit-aware client. One request at a time: the endpoint
    answers 429 to bursts, and a 113-handle pass takes about six minutes
    at the default delay."""

    def __init__(self, config: HttpConfig | None = None, backoff: tuple[int, ...] = (10, 30, 90)) -> None:
        self.config = config or HttpConfig()
        self.backoff = backoff
        self.rate = RateLimit()
        self.last_profile: Profile | None = None
        self._lock = asyncio.Lock()

    async def fetch_timeline(self, handle: str) -> str | None:
        url = SYNDICATION_URL.format(handle=handle)
        async with self._lock, client(self.config, accept="text/html,application/xhtml+xml") as http:
            for attempt, pause in enumerate(self.backoff, start=1):
                await self.rate.wait_if_exhausted()
                try:
                    r = await http.get(url)
                except httpx.HTTPError as exc:
                    log.warning("%s: http error on attempt %d: %s", handle, attempt, exc)
                    await asyncio.sleep(pause)
                    continue
                self.rate.read(r.headers)
                if r.status_code == 200 and "__NEXT_DATA__" in r.text:
                    await asyncio.sleep(self.config.delay)
                    return r.text
                if r.status_code == 404 and not r.text.strip():
                    await asyncio.sleep(pause)  # transient empty 404
                    continue
                if is_cloudflare_challenge(r.text):
                    log.warning("%s: cloudflare challenge (status %d)", handle, r.status_code)
                    await asyncio.sleep(pause)
                    continue
                if r.status_code == 429:
                    await asyncio.sleep(self.rate.seconds_to_reset() or pause)
                    continue
                log.info("%s: unavailable (status %d)", handle, r.status_code)
                return None
        return None

    async def collect(self, handle: str) -> list[Post] | None:
        """Normalised posts, or ``None`` when the endpoint did not answer."""
        html = await self.fetch_timeline(handle)
        if html is None:
            self.last_profile = None
            return None
        self.last_profile = parse_profile(html, handle)
        posts = parse_timeline(html, handle)
        log.info("%s: %d posts", handle, len(posts))
        return posts

    async def collect_many(self, handles: list[str]) -> dict[str, list[Post] | None]:
        return {h: await self.collect(h) for h in handles}
