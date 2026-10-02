"""Historical tweets without an account: Wayback CDX for ids, fxtwitter for content.

The syndication endpoint only serves recent tweets. For history, two free
services complement each other:

* the Wayback CDX index lists every ``x.com/<handle>/status/*`` URL the
  Internet Archive has captured. The captures themselves are empty (X renders
  in JavaScript), but the ids are what we need;
* ``api.fxtwitter.com/<handle>/status/<id>`` returns the full tweet for an id.

fxtwitter is a third-party service: requests are serial and paced.
"""

from __future__ import annotations

import asyncio
import logging
import re
from collections.abc import Iterable
from datetime import UTC, datetime

import httpx

from mediascrapers.http import HttpConfig, client
from mediascrapers.models import Post, PostType, post_guid

log = logging.getLogger(__name__)

CDX_URL = "https://web.archive.org/cdx/search/cdx"
FX_URL = "https://api.fxtwitter.com/{handle}/status/{tid}"
COLLECTED_VIA = "fxtwitter"
CDX_PAUSE_SECONDS = 1.0

_STATUS_RE = re.compile(r"/status/(\d{15,20})")
_HANDLE_RE = re.compile(r"(?<![\w@])@([A-Za-z0-9_]{1,15})")
_HASHTAG_RE = re.compile(r"(?<![\w#])#([\w\u00C0-\u024F]+)")
_URL_RE = re.compile(r"https?://[^\s<>\"')\]]+")


def _handles_in(text: str) -> list[str]:
    return list(dict.fromkeys(_HANDLE_RE.findall(text or "")))


def _hashtags_in(text: str) -> list[str]:
    return list(dict.fromkeys(_HASHTAG_RE.findall(text or "")))


_FX_DATE_FMT = "%a %b %d %H:%M:%S %z %Y"
_TWITTER_EPOCH_MS = 1288834974657


def snowflake_floor(year: int) -> int:
    """Smallest id a tweet published on or after 1 January ``year`` can have.

    Snowflake ids encode the publication time (``id >> 22`` is milliseconds
    since the Twitter epoch), so filtering on the id filters on publication
    date; CDX's own ``from=`` parameter filters on capture date instead.
    """
    ms = int(datetime(year, 1, 1, tzinfo=UTC).timestamp() * 1000) - _TWITTER_EPOCH_MS
    return max(0, ms) << 22


def id_prefixes(since_year: int) -> list[str]:
    """Two-digit id prefixes covering [1 January ``since_year``, now].

    Querying CDX by prefix splits a request that times out on a large account
    into a handful of small ones, each a time slice.
    """
    lo = str(snowflake_floor(since_year))
    now_ms = int(datetime.now(UTC).timestamp() * 1000) - _TWITTER_EPOCH_MS
    hi = str(now_ms << 22)
    if len(lo) != len(hi):
        return [str(d) for d in range(int(lo[:1]), 10)] + [str(d) for d in range(1, int(hi[:1]) + 1)]
    return [str(v) for v in range(int(lo[:2]), int(hi[:2]) + 1)]


async def _cdx_ids(http: httpx.AsyncClient, url_pattern: str, floor: int) -> set[int]:
    params = {"url": url_pattern, "fl": "original", "limit": "3000"}
    try:
        r = await http.get(CDX_URL, params=params, timeout=90)
    except httpx.HTTPError as exc:
        log.warning("cdx %s: %s", url_pattern, exc)
        return set()
    if r.status_code != 200:
        return set()
    return {int(m.group(1)) for m in _STATUS_RE.finditer(r.text) if int(m.group(1)) >= floor}


def spread_quota(slices: Iterable[set[int]], limit: int) -> list[str]:
    """Pick up to ``limit`` ids, newest first within each slice, shared evenly
    across slices so that older years are represented, not only the latest."""
    pending = [sorted(s, reverse=True) for s in slices if s]
    picked: list[int] = []
    remaining = limit
    while remaining > 0 and pending:
        share = max(1, remaining // len(pending))
        taken: list[int] = []
        for s in pending:
            taken.extend(s[:share])
            del s[:share]
        if not taken:
            break
        picked.extend(taken)
        remaining -= len(taken)
        pending = [s for s in pending if s]
    return [str(t) for t in sorted(set(picked), reverse=True)[:limit]]


async def list_archived_ids(
    http: httpx.AsyncClient,
    handle: str,
    *,
    since_year: int = 2022,
    limit: int = 300,
    pause: float = CDX_PAUSE_SECONDS,
) -> list[str]:
    """Status ids captured by the Wayback Machine, published since ``since_year``.

    Both ``x.com`` and ``twitter.com`` are queried: captures predating the
    rebranding live under the old domain.
    """
    floor = snowflake_floor(since_year)
    slices: list[set[int]] = []
    for prefix in id_prefixes(since_year):
        found: set[int] = set()
        for domain in ("x.com", "twitter.com"):
            found |= await _cdx_ids(http, f"{domain}/{handle}/status/{prefix}*", floor)
            if pause:
                await asyncio.sleep(pause)
        slices.append(found)
    ids = spread_quota(slices, limit)
    log.info("%s: %d archived ids (%d found)", handle, len(ids), sum(len(s) for s in slices))
    return ids


def parse_fxtwitter(data: dict, handle: str) -> Post | None:
    t = data.get("tweet") or {}
    tid, text = t.get("id"), (t.get("text") or "").strip()
    if not tid or not text:
        return None
    author_obj = t.get("author") or {}
    author = author_obj.get("screen_name") or handle
    is_retweet = author.lower() != handle.lower()
    quote = t.get("quote")
    reply_to = t.get("replying_to")
    reply_to_status = t.get("replying_to_status")
    try:
        published = datetime.strptime(t["created_at"], _FX_DATE_FMT).astimezone(UTC)
    except (KeyError, ValueError):
        ts = t.get("created_timestamp")
        published = datetime.fromtimestamp(ts, tz=UTC) if ts else None
    url = t.get("url") or f"https://x.com/{author}/status/{tid}"
    media = ((t.get("media") or {}).get("all") or [{}])[0].get("url")
    post_type: PostType = (
        "retweet" if is_retweet else "quote" if quote else "reply" if reply_to else "original"
    )
    post = Post(
        guid=post_guid(handle, url),
        handle=handle,
        url=url,
        text=text,
        published_at=published,
        post_type=post_type,
        lang=(t.get("lang") or "fr")[:8],
        reply_to_handle=reply_to,
        reply_to_url=(
            f"https://x.com/{reply_to}/status/{reply_to_status}" if reply_to and reply_to_status else None
        ),
        media_url=media,
        likes=t.get("likes"),
        retweets=t.get("retweets"),
        replies=t.get("replies"),
        views=t.get("views"),
        collected_via=COLLECTED_VIA,
        tweet_id=str(tid),
        author_id=author_obj.get("id"),
        source=t.get("source") or None,
        mentions=_handles_in(text),
        hashtags=_hashtags_in(text),
        urls=[u for u in _URL_RE.findall(text) if not u.startswith("https://t.co/")],
    )
    if quote:
        post.quoted_handle = (quote.get("author") or {}).get("screen_name")
        post.quoted_user_id = (quote.get("author") or {}).get("id")
        post.quoted_url = quote.get("url")
        post.quoted_text = (quote.get("text") or "")[:2000] or None
    elif is_retweet:
        post.quoted_handle = author
        post.quoted_user_id = author_obj.get("id")
        post.quoted_url = url
    return post


async def fetch_tweet(http: httpx.AsyncClient, handle: str, tid: str) -> Post | None:
    """One tweet by id, or ``None`` if deleted, private or unreachable."""
    try:
        r = await http.get(FX_URL.format(handle=handle, tid=tid))
    except httpx.HTTPError:
        return None
    if r.status_code != 200:
        return None
    try:
        return parse_fxtwitter(r.json(), handle)
    except ValueError:
        return None


class Backfill:
    def __init__(self, config: HttpConfig | None = None) -> None:
        self.config = config or HttpConfig()

    async def run(
        self,
        handle: str,
        *,
        since_year: int = 2022,
        limit: int = 300,
        known_ids: set[str] | None = None,
        max_fetch: int | None = None,
    ) -> list[Post]:
        """Fetch archived tweets of ``handle``, skipping ``known_ids``."""
        known = set(known_ids or ())
        out: list[Post] = []
        async with client(self.config, accept="application/json") as http:
            ids = await list_archived_ids(http, handle, since_year=since_year, limit=limit)
            for tid in (i for i in ids if i not in known):
                if max_fetch is not None and len(out) >= max_fetch:
                    break
                if post := await fetch_tweet(http, handle, tid):
                    out.append(post)
                await asyncio.sleep(self.config.delay)
        return out

    async def expand_truncated(self, posts: list[Post]) -> list[Post]:
        """Replace the text of truncated posts with the full version from fxtwitter."""
        async with client(self.config, accept="application/json") as http:
            for p in posts:
                if not p.text_truncated:
                    continue
                tid = _STATUS_RE.search(p.url)
                if not tid:
                    continue
                full = await fetch_tweet(http, p.handle, tid.group(1))
                if full and len(full.text) > len(p.text):
                    p.text = full.text
                    p.text_truncated = False
                await asyncio.sleep(self.config.delay)
        return posts
