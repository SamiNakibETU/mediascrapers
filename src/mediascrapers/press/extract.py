"""Full-text extraction with a fallback chain.

Order: subscriber cookies, direct fetch and trafilatura, Jina Reader, Wayback
snapshot. The chain stops at the first clean result (long enough and without
a paywall marker); otherwise it returns the longest clean candidate, or the
longest candidate at all.
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

import httpx

from mediascrapers.archive.wayback import closest_snapshot
from mediascrapers.http import HttpConfig, client
from mediascrapers.models import Extraction

log = logging.getLogger(__name__)

try:
    import trafilatura
except ImportError:  # pragma: no cover
    trafilatura = None

MIN_LENGTH = 350

_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_PAYWALL_RE = re.compile(
    r"il vous reste\s+\d+|article réservé|réservé aux abonné|pour lire la suite|"
    r"abonnez-vous|déjà abonné|%\s+à lire|s['’]abonner pour lire|"
    r"soutenir.{0,30}journalisme|connectez-vous pour lire|"
    r"subscribe to continue|subscribers only|to continue reading|already a subscriber",
    re.IGNORECASE,
)


@dataclass
class ExtractorConfig:
    http: HttpConfig = field(default_factory=HttpConfig)
    jina_enabled: bool = True
    jina_url: str = "https://r.jina.ai"
    wayback_enabled: bool = True
    # domain -> Cookie header value, for sources you subscribe to
    cookies: dict[str, str] = field(default_factory=dict)

    @classmethod
    def with_cookies_json(cls, raw: str, **kw) -> ExtractorConfig:
        cookies = {k.lower(): v for k, v in json.loads(raw).items()} if raw.strip() else {}
        return cls(cookies=cookies, **kw)


def is_paywalled(text: str | None) -> bool:
    return bool(text) and bool(_PAYWALL_RE.search(text[:4000]))


def build_extraction(text: str | None, method: str, *, is_full: bool | None = None) -> Extraction | None:
    if not text:
        return None
    paywalled = is_paywalled(text)
    if is_full is None:
        is_full = not paywalled and len(text) >= MIN_LENGTH
    return Extraction(text=text, method=method, is_full=is_full, paywalled=paywalled)


def _trafilatura(html: str, *, recall: bool) -> str | None:
    if "<html" not in html[:2000].lower():
        html = f"<html><body>{html}</body></html>"  # RSS bodies are fragments
    return trafilatura.extract(
        html,
        include_comments=False,
        include_tables=False,
        favor_recall=recall,
        favor_precision=not recall,
        deduplicate=True,
        output_format="txt",
    )


async def extract_html(html: str | None) -> str | None:
    """Article text from HTML already in hand (e.g. RSS ``content:encoded``)."""
    if trafilatura is None or not html:
        return None
    best: str | None = None
    for recall in (True, False):
        try:
            txt = await asyncio.to_thread(_trafilatura, html, recall=recall)
        except Exception:  # noqa: BLE001
            txt = None
        if txt and len(txt) > len(best or ""):
            best = txt
        if best and len(best) >= MIN_LENGTH:
            break
    return best


class Extractor:
    def __init__(self, config: ExtractorConfig | None = None) -> None:
        self.config = config or ExtractorConfig()

    async def _get(
        self, url: str, *, headers: dict[str, str] | None = None, timeout: float | None = None
    ) -> str | None:
        accept = "text/html,application/xhtml+xml"
        try:
            async with client(self.config.http, accept=accept, timeout=timeout) as http:
                r = await http.get(url, headers=headers)
        except httpx.HTTPError as exc:
            log.debug("fetch %s: %s", url, exc)
            return None
        return r.text if r.status_code == 200 else None

    def _cookie_for(self, url: str) -> str | None:
        host = urlparse(url).hostname or ""
        return next((c for d, c in self.config.cookies.items() if d in host), None)

    async def via_cookies(self, url: str) -> str | None:
        cookie = self._cookie_for(url)
        if not cookie or trafilatura is None:
            return None
        html = await self._get(url, headers={"Cookie": cookie}, timeout=self.config.http.timeout * 2)
        return await asyncio.to_thread(_trafilatura, html, recall=True) if html else None

    async def via_fetch(self, url: str) -> str | None:
        """trafilatura's own fetch, then a browser-like fetch if the site refused it."""
        if trafilatura is None:
            return None
        best: str | None = None
        try:
            downloaded = await asyncio.to_thread(trafilatura.fetch_url, url)
        except Exception:  # noqa: BLE001
            downloaded = None
        if downloaded:
            best = await extract_html(downloaded)
            if best and len(best) >= MIN_LENGTH:
                return best
        html = await self._get(url, timeout=30)
        if html and len(html) > 500:
            txt = await asyncio.to_thread(_trafilatura, html, recall=True)
            if txt and len(txt) > len(best or ""):
                best = txt
        return best

    async def via_jina(self, url: str) -> str | None:
        """Jina Reader: JS-rendered pages fetched from Jina's IPs, returned as markdown."""
        base = self.config.jina_url.rstrip("/")
        try:
            async with httpx.AsyncClient(
                timeout=self.config.http.timeout * 2,
                headers={"Accept": "text/plain"},
                transport=self.config.http.transport,
            ) as http:
                r = await http.get(f"{base}/{url}")
        except httpx.HTTPError:
            return None
        if r.status_code != 200:
            return None
        md = r.text
        if "Markdown Content:" in md:
            md = md.split("Markdown Content:", 1)[1]
        md = _MD_LINK_RE.sub(r"\1", md)
        return re.sub(r"\n{3,}", "\n\n", md).strip() or None

    async def via_wayback(self, url: str) -> str | None:
        """Closest Wayback snapshot, often predating a paywall or a 403."""
        if trafilatura is None:
            return None
        snap = await closest_snapshot(url)
        if not snap:
            return None
        html = await self._get(snap, timeout=self.config.http.timeout * 2)
        return await asyncio.to_thread(_trafilatura, html, recall=True) if html else None

    async def extract(self, url: str) -> Extraction:
        best_clean: Extraction | None = None
        best_any: Extraction | None = None

        def consider(ext: Extraction | None) -> bool:
            nonlocal best_clean, best_any
            if not ext or not ext.text:
                return False
            if best_any is None or len(ext.text) > len(best_any.text or ""):
                best_any = ext
            if not ext.paywalled and (best_clean is None or len(ext.text) > len(best_clean.text or "")):
                best_clean = ext
            return bool(best_clean and len(best_clean.text or "") >= MIN_LENGTH)

        steps = [("cookies", self.via_cookies), ("fetch", self.via_fetch)]
        if self.config.jina_enabled:
            steps.append(("jina", self.via_jina))
        if self.config.wayback_enabled:
            steps.append(("wayback", self.via_wayback))

        for method, step in steps:
            if consider(build_extraction(await step(url), method)):
                return best_clean  # type: ignore[return-value]
        return best_clean or best_any or Extraction()
