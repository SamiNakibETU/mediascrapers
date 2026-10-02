"""Internet Archive helpers: look up an existing capture, or request a new one."""

from __future__ import annotations

import httpx

AVAILABLE_URL = "https://archive.org/wayback/available"
SAVE_URL = "https://web.archive.org/save/"
USER_AGENT = "mediascrapers/0.1 (archive lookup; research)"


def parse_availability(data: object) -> str | None:
    if not isinstance(data, dict):
        return None
    closest = (data.get("archived_snapshots") or {}).get("closest")
    if not isinstance(closest, dict):
        return None
    if closest.get("available") is True or str(closest.get("status", "")).startswith("2"):
        return closest.get("url")
    return None


async def closest_snapshot(url: str, *, timeout: float = 12.0) -> str | None:
    """URL of the closest existing capture, or ``None``."""
    try:
        async with httpx.AsyncClient(timeout=timeout, headers={"User-Agent": USER_AGENT}) as http:
            r = await http.get(AVAILABLE_URL, params={"url": url})
            if r.status_code != 200:
                return None
            return parse_availability(r.json())
    except (httpx.HTTPError, ValueError):
        return None


async def save_page_now(url: str, *, timeout: float = 60.0) -> str | None:
    """Request a capture and return its archive URL. Slow and rate limited:
    call it in small batches."""
    try:
        headers = {"User-Agent": USER_AGENT}
        async with httpx.AsyncClient(timeout=timeout, headers=headers, follow_redirects=True) as http:
            r = await http.get(f"{SAVE_URL}{url}")
    except httpx.HTTPError:
        return None
    if r.status_code not in (200, 301, 302):
        return None
    location = r.headers.get("Content-Location")
    if location and location.startswith("/web/"):
        return f"https://web.archive.org{location}"
    final = str(r.url)
    return final if "/web/" in final else None
