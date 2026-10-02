"""Route a request to the backends that can answer it, fall back on failure.

The router holds an ordered list of backends. For a given capability it tries
each backend that declares it, in order, and returns the first real answer. A
backend returning ``None`` (route unreachable) is skipped; a backend raising
:class:`~mediascrapers.x.base.BackendError` is recorded unhealthy and skipped.
Order encodes preference: put the cheapest, lowest-risk route first (the public
syndication endpoint), the operator's authenticated route last.

This is the single object the rest of the pipeline talks to. Whether a given
capability is available depends only on which backends were registered, so the
same code runs whether or not an authenticated backend is present.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from mediascrapers.models import Post, Profile
from mediascrapers.x.base import Backend, BackendError, Capability

log = logging.getLogger(__name__)


@dataclass
class BackendHealth:
    ok: int = 0
    failed: int = 0
    last_error: str | None = None

    @property
    def healthy(self) -> bool:
        # A backend is shelved only after repeated failures with no success,
        # so one transient error does not disable a working route.
        return not (self.failed >= 3 and self.ok == 0)


class Router:
    def __init__(self, backends: list[Backend]) -> None:
        self._backends = list(backends)
        self._health: dict[str, BackendHealth] = {b.name: BackendHealth() for b in backends}

    def supports(self, cap: Capability) -> bool:
        return any(cap in b.capabilities for b in self._eligible(cap))

    def health(self) -> dict[str, BackendHealth]:
        return dict(self._health)

    def _eligible(self, cap: Capability) -> list[Backend]:
        return [
            b for b in self._backends
            if cap in b.capabilities and self._health[b.name].healthy
        ]

    async def _try(self, cap: Capability, method: str, *args, **kwargs):
        """Call ``method`` on each eligible backend until one gives a real answer."""
        last_exc: Exception | None = None
        for backend in self._eligible(cap):
            fn = getattr(backend, method, None)
            if fn is None:
                continue
            h = self._health[backend.name]
            try:
                result = await fn(*args, **kwargs)
            except BackendError as exc:
                h.failed += 1
                h.last_error = str(exc)[:200]
                log.warning("%s.%s failed: %s", backend.name, method, exc)
                last_exc = exc
                continue
            if result is None:
                log.info("%s.%s: no answer, trying next", backend.name, method)
                continue
            h.ok += 1
            log.debug("%s.%s: answered", backend.name, method)
            return result
        if last_exc is not None:
            raise last_exc
        return None

    # --- capability-typed entry points -------------------------------------

    async def timeline(self, handle: str) -> list[Post] | None:
        return await self._try(Capability.TIMELINE, "timeline", handle)

    async def profile(self, handle: str) -> Profile | None:
        return await self._try(Capability.PROFILE, "profile", handle)

    async def neighbours(self, handle: str) -> dict[str, Profile] | None:
        return await self._try(Capability.NEIGHBOURS, "neighbours", handle)

    async def hydrate(self, handle: str, tid: str) -> Post | None:
        return await self._try(Capability.HYDRATE, "hydrate", handle, tid)

    async def conversation(self, handle: str, tid: str, **kw) -> list[Post] | None:
        return await self._try(Capability.HYDRATE, "conversation", handle, tid, **kw)

    async def backfill(self, handle: str, **kw) -> list[Post] | None:
        return await self._try(Capability.BACKFILL, "backfill", handle, **kw)

    async def search(self, query: str, **kw) -> list[Post] | None:
        return await self._try(Capability.SEARCH, "search", query, **kw)

    async def replies(self, tid: str, **kw) -> list[Post] | None:
        return await self._try(Capability.REPLIES, "replies", tid, **kw)

    async def followers(self, user_id: str, **kw) -> list[Profile] | None:
        return await self._try(Capability.FOLLOWERS, "followers", user_id, **kw)


def build_router(
    extra: list[Backend] | None = None, *, config=None
) -> Router:
    """A router over the no-account backends, plus any extra backends.

    Extra backends (an authenticated adapter, a private-instance client) go
    last so the public routes are always preferred.
    """
    from mediascrapers.x.backends import default_backends

    return Router(default_backends(config) + list(extra or []))
