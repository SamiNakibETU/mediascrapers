"""Keyword discovery of X posts through routes that are not X.

The public routes cannot search X by keyword. But tweets are indexed and
re-posted elsewhere, so a keyword can still surface tweet URLs without any
account:

* web search engines index ``x.com`` status pages (``site:x.com <terms>``);
* the project's own press and Telegram collectors carry tweet links in the
  text they gather.

This module extracts status ids from arbitrary text/HTML, so any such source
can feed the hydrate route. The engine queries themselves are left to the
operator's chosen search provider; :func:`extract_status_urls` is the common,
dependency-free core.
"""

from __future__ import annotations

import re

from mediascrapers.models import status_id

_STATUS_URL_RE = re.compile(
    r"https?://(?:x|twitter|mobile\.twitter|nitter[^/]*)\.[a-z.]+/([A-Za-z0-9_]{1,15})/status/(\d{15,20})"
)


def extract_status_urls(text: str) -> list[tuple[str, str]]:
    """Every ``(handle, status_id)`` pair found in ``text``, deduplicated.

    Accepts x.com, twitter.com, mobile and nitter-style hosts, so the output of
    a search engine, a press article or a Telegram message all parse the same
    way. Feed each pair to the router's ``hydrate`` to get the full post.
    """
    seen: dict[tuple[str, str], None] = {}
    for m in _STATUS_URL_RE.finditer(text or ""):
        seen.setdefault((m.group(1), m.group(2)), None)
    return list(seen)


def status_ids(text: str) -> list[str]:
    """Just the status ids in ``text`` (any url shape), order-preserving."""
    out: dict[str, None] = {}
    for url in re.findall(r"\S+/status/\d{15,20}", text or ""):
        if sid := status_id(url):
            out.setdefault(sid, None)
    return list(out)


def site_query(terms: str) -> str:
    """A ``site:x.com`` search-engine query string for the given terms."""
    return f"site:x.com {terms.strip()}"
