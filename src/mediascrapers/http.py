from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field

import httpx

log = logging.getLogger(__name__)

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
)


@dataclass
class HttpConfig:
    user_agent: str = DEFAULT_USER_AGENT
    timeout: float = 20.0
    delay: float = 2.5
    concurrency: int = 3
    accept_language: str = "fr-FR,fr;q=0.9,en;q=0.8"
    extra_headers: dict[str, str] = field(default_factory=dict)
    # test hook: an httpx transport replacing the network
    transport: httpx.AsyncBaseTransport | None = None

    def headers(self, accept: str = "*/*") -> dict[str, str]:
        return {
            "User-Agent": self.user_agent,
            "Accept": accept,
            "Accept-Language": self.accept_language,
            **self.extra_headers,
        }


class RateLimit:
    """Tracks ``x-rate-limit-*`` headers and sleeps until the window resets."""

    def __init__(self) -> None:
        self.remaining: int | None = None
        self.reset_at: float | None = None

    def read(self, headers: httpx.Headers) -> None:
        try:
            if (rem := headers.get("x-rate-limit-remaining")) is not None:
                self.remaining = int(rem)
            if (rst := headers.get("x-rate-limit-reset")) is not None:
                self.reset_at = float(rst)
        except (TypeError, ValueError):
            pass

    def seconds_to_reset(self) -> float:
        if not self.reset_at:
            return 0.0
        return max(0.0, self.reset_at - time.time() + 1.0)

    async def wait_if_exhausted(self) -> None:
        if self.remaining is not None and self.remaining <= 0:
            wait = self.seconds_to_reset()
            if wait > 0:
                log.info("rate limit exhausted, sleeping %.0fs", wait)
                await asyncio.sleep(wait)
            self.remaining = None


def is_cloudflare_challenge(body: str) -> bool:
    head = (body or "")[:14].lower()
    return head.startswith("<!doctype html") and "cloudflare" in (body or "").lower()


def client(config: HttpConfig, accept: str = "*/*", timeout: float | None = None) -> httpx.AsyncClient:
    return httpx.AsyncClient(
        timeout=timeout or config.timeout,
        headers=config.headers(accept),
        follow_redirects=True,
        transport=config.transport,
    )
