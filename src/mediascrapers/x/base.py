"""Common interface for every way of reading X.

The project reaches X through several unrelated routes: the public syndication
endpoint, the fxtwitter hydration service, the Wayback archive, and — on the
caller's own machine, with the caller's own authenticated session — a
pluggable backend. Each route answers a different subset of questions and
fails in its own way. This module is the contract they all share so the
router (``x.router``) can treat them uniformly and fall back from one to the
next.

A backend never raises for an expected "no answer"; it returns ``None`` (route
unavailable right now) or an empty list (route answered, nothing there). It
raises only for programming errors.
"""

from __future__ import annotations

import enum
from typing import Protocol, runtime_checkable

from mediascrapers.models import Post, Profile


class Capability(enum.Flag):
    """What a backend can answer. A router matches a request to the backends
    that declare the needed capability, in preference order."""

    TIMELINE = enum.auto()      # recent posts of one account
    PROFILE = enum.auto()       # bio and counters of one account
    NEIGHBOURS = enum.auto()    # profiles a timeline relays / answers (first circle)
    HYDRATE = enum.auto()       # one post (and its parent) by id or url
    BACKFILL = enum.auto()      # historical posts of one account
    SEARCH = enum.auto()        # posts matching a query (keyword / hashtag)
    REPLIES = enum.auto()       # replies under a given post (cascades)
    FOLLOWERS = enum.auto()     # accounts following / followed by one account

    NONE = 0


@runtime_checkable
class Backend(Protocol):
    """One route to X. Methods a backend does not support are simply absent;
    the router consults ``capabilities`` before calling, so no method ever
    needs to exist just to raise ``NotImplementedError``.

    Every method returns ``None`` when the route is momentarily unreachable
    (so the router moves to the next backend) and a value — possibly empty —
    when the route answered.
    """

    name: str
    capabilities: Capability


class BackendError(RuntimeError):
    """A backend failed in a way the router should record but not crash on."""


class AuthRequired(BackendError):
    """Raised at construction when an authenticated backend has no session.

    Carried, not swallowed: a misconfigured credentialed backend is a setup
    mistake the operator must see, not a transient outage to fall back from.
    """


# Narrow structural aliases documenting what each optional method returns.
# A backend implements the subset matching its declared capabilities.
TimelineResult = list[Post] | None
ProfileResult = Profile | None
ProfilesResult = dict[str, Profile] | None
PostResult = Post | None
PostsResult = list[Post] | None
