"""RSS polling and article materialisation.

For every feed entry, the body is resolved in this order: the feed's own
``content:encoded`` when it is clearly a full article, otherwise the
extraction chain, otherwise the longest of the RSS text, summary and title.
"""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable, Iterable
from datetime import UTC, datetime
from time import mktime

import feedparser
import httpx

from mediascrapers.http import HttpConfig, client
from mediascrapers.models import Article, Extraction, Source, sha256
from mediascrapers.press.clean import clean_article_text, clean_html
from mediascrapers.press.extract import Extractor, build_extraction, extract_html

log = logging.getLogger(__name__)

RSS_FULLTEXT_MIN = 1200
RSS_ACCEPT = "application/rss+xml, application/xml, text/xml, */*"

Filter = Callable[[str, str], bool]


def feed_datetime(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        st = getattr(entry, key, None)
        if st:
            try:
                return datetime.fromtimestamp(mktime(st), tz=UTC)
            except (OverflowError, ValueError):
                continue
    return None


def _rss_full_html(entry) -> str:
    content = getattr(entry, "content", None)
    if content:
        try:
            return content[0].get("value", "") or ""
        except (AttributeError, IndexError, TypeError):
            return ""
    return ""


class FeedCollector:
    """Polls RSS feeds and yields :class:`Article` objects.

    ``seen`` is a set of URL hashes already stored; those entries are skipped
    before any extraction happens. ``prefilter(title, summary)`` lets the
    caller discard entries cheaply before fetching the body.
    """

    def __init__(
        self,
        extractor: Extractor | None = None,
        config: HttpConfig | None = None,
        *,
        max_entries: int = 60,
        prefilter: Filter | None = None,
    ) -> None:
        self.config = config or HttpConfig()
        self.extractor = extractor or Extractor()
        self.max_entries = max_entries
        self.prefilter = prefilter
        self._sem = asyncio.Semaphore(self.config.concurrency)

    async def fetch_feed(self, source: Source) -> feedparser.FeedParserDict | None:
        try:
            async with client(self.config, accept=RSS_ACCEPT) as http:
                r = await http.get(source.rss_url)
        except httpx.HTTPError as exc:
            log.warning("%s: %s", source.id, exc)
            return None
        if r.status_code != 200:
            log.info("%s: http %d", source.id, r.status_code)
            return None
        feed = feedparser.parse(r.text)
        if feed.bozo and not feed.entries:
            log.info("%s: unparsable feed", source.id)
            return None
        return feed

    async def resolve_body(self, entry, url: str, title: str, summary: str) -> Extraction:
        rss_html = _rss_full_html(entry)
        rss_text = await extract_html(rss_html)
        if rss_text and len(rss_text) >= RSS_FULLTEXT_MIN:
            return build_extraction(rss_text, "rss_full", is_full=True)  # type: ignore[return-value]

        scraped = await self.extractor.extract(url)
        fallbacks = [
            (rss_text or "", "rss_text"),
            (clean_html(rss_html) if rss_html else "", "rss_raw"),
            (summary, "summary"),
            (title, "title"),
        ]
        fb_text, fb_method = max(
            ((t, m) for t, m in fallbacks if t), key=lambda tm: len(tm[0]), default=("", "summary")
        )
        if scraped.text and len(scraped.text) >= len(fb_text):
            return scraped
        return build_extraction(fb_text, fb_method) or scraped

    async def collect(self, source: Source, *, seen: set[str] | None = None) -> list[Article]:
        seen = seen or set()
        async with self._sem:
            feed = await self.fetch_feed(source)
        if feed is None:
            return []

        out: list[Article] = []
        for entry in feed.entries[: self.max_entries]:
            url = getattr(entry, "link", None)
            if not url:
                continue
            h = sha256(url)
            if h in seen:
                continue
            title = clean_html(getattr(entry, "title", ""))
            summary = clean_html(getattr(entry, "summary", ""))
            if self.prefilter and not self.prefilter(title, summary):
                continue

            extraction = await self.resolve_body(entry, url, title, summary)
            text = clean_article_text(extraction.text or summary or title)
            published = feed_datetime(entry)
            out.append(Article(
                url=url,
                url_hash=h,
                source_id=source.id,
                title=title,
                text=text,
                published_at=published or datetime.now(UTC),
                published_estimated=published is None,
                summary=summary,
                language=source.language,
                extraction_method=extraction.method,
                is_full=extraction.is_full,
                paywalled=extraction.paywalled,
                word_count=len(text.split()),
            ))
            seen.add(h)
        log.info("%s: %d new articles", source.id, len(out))
        return out

    async def collect_all(self, sources: Iterable[Source], *, seen: set[str] | None = None) -> list[Article]:
        seen = seen if seen is not None else set()
        results = await asyncio.gather(*(self.collect(s, seen=seen) for s in sources))
        return [a for batch in results for a in batch]
