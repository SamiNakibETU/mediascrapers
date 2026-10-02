"""Backend interface, authenticated adapter and router fallback."""

from datetime import datetime

import pytest

from mediascrapers.models import Post
from mediascrapers.x.backends import AuthenticatedBackend, default_backends
from mediascrapers.x.base import AuthRequired, Capability
from mediascrapers.x.router import Router, build_router


def _post(text="x", handle="h"):
    return Post(guid="g" + text, handle=handle, url=f"https://x.com/{handle}/status/1",
                text=text, published_at=None)


class FakeBackend:
    """A configurable backend for exercising the router."""

    def __init__(self, name, capabilities, *, answers=None, raises=False, none=False):
        self.name = name
        self.capabilities = capabilities
        self._answers = answers or []
        self._raises = raises
        self._none = none
        self.calls = 0

    async def timeline(self, handle):
        self.calls += 1
        if self._raises:
            from mediascrapers.x.base import BackendError
            raise BackendError("boom")
        if self._none:
            return None
        return list(self._answers)


def test_default_backends_capabilities():
    caps = Capability.NONE
    for b in default_backends():
        caps |= b.capabilities
    assert Capability.TIMELINE in caps
    assert Capability.HYDRATE in caps
    assert Capability.BACKFILL in caps
    assert Capability.NEIGHBOURS in caps
    # Search and replies are NOT available from the no-account routes.
    assert Capability.SEARCH not in caps
    assert Capability.REPLIES not in caps


async def test_router_falls_back_from_none_to_next():
    a = FakeBackend("a", Capability.TIMELINE, none=True)
    b = FakeBackend("b", Capability.TIMELINE, answers=[_post("hit")])
    r = Router([a, b])
    posts = await r.timeline("h")
    assert [p.text for p in posts] == ["hit"]
    assert a.calls == 1 and b.calls == 1


async def test_router_falls_back_from_error_and_records_health():
    a = FakeBackend("a", Capability.TIMELINE, raises=True)
    b = FakeBackend("b", Capability.TIMELINE, answers=[_post("ok")])
    r = Router([a, b])
    assert (await r.timeline("h"))[0].text == "ok"
    assert r.health()["a"].failed == 1 and r.health()["b"].ok == 1


async def test_router_shelves_backend_after_repeated_failures():
    a = FakeBackend("a", Capability.TIMELINE, raises=True)
    b = FakeBackend("b", Capability.TIMELINE, answers=[_post("ok")])
    r = Router([a, b])
    for _ in range(3):
        await r.timeline("h")
    assert not r.health()["a"].healthy
    a.calls = 0
    await r.timeline("h")
    assert a.calls == 0  # shelved, no longer tried


async def test_router_returns_none_when_no_backend_supports():
    r = Router([FakeBackend("a", Capability.TIMELINE)])
    assert not r.supports(Capability.SEARCH)
    assert await r.search("climat") is None


def test_authenticated_backend_requires_reader():
    with pytest.raises(AuthRequired):
        AuthenticatedBackend(None)


class FakeTweet:
    def __init__(self, tid, text, user):
        self.id = tid
        self.rawContent = text
        self.url = f"https://x.com/{user.username}/status/{tid}"
        self.user = user
        self.date = datetime(2026, 1, 2, 3, 4, 5)
        self.likeCount, self.retweetCount, self.replyCount = 5, 2, 1
        self.viewCount, self.conversationId, self.lang = 99, tid, "fr"
        self.retweetedTweet = self.quotedTweet = self.inReplyToUser = None
        self.inReplyToTweetId = None
        self.mentionedUsers, self.hashtags, self.links = [], ["DANA"], []
        self.sourceLabel = "Twitter Web App"


class FakeUser:
    def __init__(self, uid, username):
        self.id = uid
        self.username = username
        self.displayname = username.title()
        self.followersCount = 1000
        self.rawDescription = " bio "
        self.verified = False
        self.blue = True


async def _agen(items):
    for i in items:
        yield i


async def test_authenticated_backend_search_normalises():
    u = FakeUser(42, "MeteoFrance")

    class Reader:
        def search(self, query, limit=200):
            return _agen([FakeTweet(1, "alerte #DANA", u)])

    be = AuthenticatedBackend(Reader())
    assert Capability.SEARCH in be.capabilities
    posts = await be.search("DANA")
    assert len(posts) == 1
    p = posts[0]
    assert p.text == "alerte #DANA" and p.handle == "MeteoFrance"
    assert p.author_id == "42" and p.tweet_id == "1" and p.views == 99
    assert p.hashtags == ["DANA"] and p.collected_via == "auth"
    assert p.published_at.isoformat() == "2026-01-02T03:04:05+00:00"


async def test_build_router_puts_extra_backends_last():
    class Reader:
        def search(self, query, limit=200):
            return _agen([])

    r = build_router(extra=[AuthenticatedBackend(Reader())])
    assert r.supports(Capability.SEARCH)   # unlocked by the extra backend
    assert r.supports(Capability.TIMELINE)  # still from syndication
    names = [b.name for b in r._backends]
    assert names[-1] == "authenticated" and names[0] == "syndication"


def test_extract_status_urls_across_hosts():
    from mediascrapers.x.discover import extract_status_urls, site_query, status_ids
    text = (
        "voir https://x.com/MeteoFrance/status/1900000000000000001 et "
        "https://twitter.com/prefet/status/1900000000000000002 , doublon "
        "https://x.com/MeteoFrance/status/1900000000000000001 et "
        "https://nitter.net/autre/status/1900000000000000003"
    )
    pairs = extract_status_urls(text)
    assert ("MeteoFrance", "1900000000000000001") in pairs
    assert ("prefet", "1900000000000000002") in pairs
    assert ("autre", "1900000000000000003") in pairs
    assert len(pairs) == 3  # deduplicated
    assert status_ids(text) == [
        "1900000000000000001", "1900000000000000002", "1900000000000000003"
    ]
    assert site_query("  inondations Valence ") == "site:x.com inondations Valence"
