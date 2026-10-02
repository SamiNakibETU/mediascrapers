"""Concrete backends over the existing collectors, plus the adapter seam for an
authenticated route.

Three of these need no account and are ready now:

* :class:`SyndicationBackend` — recent timeline, profile and first-circle
  profiles, through the public widget endpoint;
* :class:`HydrateBackend` — one post by id/url, and the chain up to the root of
  its conversation, through fxtwitter;
* :class:`BackfillBackend` — historical posts, through Wayback ids + fxtwitter.

The fourth, :class:`AuthenticatedBackend`, is an *adapter*, not a scraper: it
holds no credentials and ships no login, session-rotation or
detection-avoidance logic. It takes any object that already knows how to read
X from an authenticated session on the operator's own machine (for example a
configured ``twscrape.API`` or a private Nitter instance client) and maps its
results into the project's :class:`~mediascrapers.models.Post` /
:class:`~mediascrapers.models.Profile`. What that session is, how it was
created and whether its use is appropriate are the operator's responsibility,
decided outside this code.
"""

from __future__ import annotations

import logging
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime

from mediascrapers.http import HttpConfig, client
from mediascrapers.models import Post, Profile, post_guid, status_id
from mediascrapers.x.backfill import Backfill, fetch_tweet
from mediascrapers.x.base import (
    AuthRequired,
    Backend,
    Capability,
)
from mediascrapers.x.syndication import SyndicationClient

log = logging.getLogger(__name__)


class SyndicationBackend:
    """Public syndication endpoint. No account. Primary route for the live
    timeline, the account's profile and its first circle of amplified
    accounts."""

    name = "syndication"
    capabilities = Capability.TIMELINE | Capability.PROFILE | Capability.NEIGHBOURS

    def __init__(self, config: HttpConfig | None = None) -> None:
        self._client = SyndicationClient(config)

    async def timeline(self, handle: str) -> list[Post] | None:
        return await self._client.collect(handle)

    async def profile(self, handle: str) -> Profile | None:
        if await self._client.collect(handle) is None:
            return None
        return self._client.last_profile

    async def neighbours(self, handle: str) -> dict[str, Profile] | None:
        if await self._client.collect(handle) is None:
            return None
        return dict(self._client.last_profiles)


class HydrateBackend:
    """fxtwitter. No account. Turns a known id or url into a full post, and
    walks the reply chain up to the root of the conversation."""

    name = "fxtwitter"
    capabilities = Capability.HYDRATE

    def __init__(self, config: HttpConfig | None = None) -> None:
        self.config = config or HttpConfig()

    async def hydrate(self, handle: str, tid: str) -> Post | None:
        async with client(self.config, accept="application/json") as http:
            return await fetch_tweet(http, handle, tid)

    async def conversation(self, handle: str, tid: str, *, max_depth: int = 40) -> list[Post]:
        """The chain of posts from ``tid`` up to the root of its thread.

        Walks ``reply_to`` links upward. This yields the ancestors of a post
        (the thread it answers), not the replies beneath it; the latter needs
        an authenticated route and lives on :class:`AuthenticatedBackend`.
        """
        chain: list[Post] = []
        seen: set[str] = set()
        cur_handle, cur_id = handle, tid
        async with client(self.config, accept="application/json") as http:
            for _ in range(max_depth):
                if not cur_id or cur_id in seen:
                    break
                seen.add(cur_id)
                post = await fetch_tweet(http, cur_handle, cur_id)
                if post is None:
                    break
                chain.append(post)
                if not post.reply_to_url:
                    break
                cur_id = status_id(post.reply_to_url) or ""
                cur_handle = post.reply_to_handle or cur_handle
        chain.reverse()
        return chain


class BackfillBackend:
    """Wayback ids + fxtwitter. No account. Historical posts of an account."""

    name = "backfill"
    capabilities = Capability.BACKFILL

    def __init__(self, config: HttpConfig | None = None) -> None:
        self._backfill = Backfill(config)

    async def backfill(
        self, handle: str, *, since_year: int = 2022, limit: int = 300,
        known_ids: set[str] | None = None,
    ) -> list[Post] | None:
        return await self._backfill.run(
            handle, since_year=since_year, limit=limit, known_ids=known_ids
        )


# A session reader is any object the operator wires on their own machine that
# exposes these coroutine methods. Shapes are kept loose on purpose: an adapter
# normalises whatever each returns. None of these are implemented here.
SessionReader = object


class AuthenticatedBackend:
    """Adapter around an operator-supplied authenticated session reader.

    This class contains no credentials, no login flow, and nothing that
    disguises automated reading as human. It is a translator: it forwards
    requests to ``reader`` — the object the operator configured on their own
    machine — and maps whatever comes back into the project's dataclasses.
    It unlocks the capabilities the public routes cannot offer (search, the
    replies beneath a post, follower lists) *when* such a reader is provided.

    ``to_post`` / ``to_profile`` convert the reader's native objects. Defaults
    assume twscrape-shaped objects; pass your own converters for another
    reader (e.g. a private Nitter client).
    """

    name = "authenticated"
    capabilities = (
        Capability.SEARCH | Capability.REPLIES | Capability.FOLLOWERS
        | Capability.TIMELINE | Capability.PROFILE
    )

    def __init__(
        self,
        reader: SessionReader | None,
        *,
        to_post: Callable[[object, str], Post] | None = None,
        to_profile: Callable[[object], Profile] | None = None,
    ) -> None:
        if reader is None:
            raise AuthRequired(
                "AuthenticatedBackend needs a configured session reader; "
                "none was supplied. Wire one on the collecting machine."
            )
        self._reader = reader
        self._to_post = to_post or _twscrape_post
        self._to_profile = to_profile or _twscrape_profile

    async def _collect(self, agen: Awaitable | object, query_handle: str) -> list[Post]:
        out: list[Post] = []
        async for item in agen:  # type: ignore[union-attr]
            try:
                out.append(self._to_post(item, query_handle))
            except Exception as exc:  # noqa: BLE001
                log.debug("authenticated: skipped one item: %s", exc)
        return out

    async def search(self, query: str, *, limit: int = 200) -> list[Post]:
        return await self._collect(self._reader.search(query, limit=limit), query)

    async def replies(self, tid: str, *, limit: int = 200) -> list[Post]:
        return await self._collect(self._reader.tweet_replies(int(tid), limit=limit), "")

    async def followers(self, user_id: str, *, limit: int = 1000) -> list[Profile]:
        out: list[Profile] = []
        async for item in self._reader.followers(int(user_id), limit=limit):
            try:
                out.append(self._to_profile(item))
            except Exception as exc:  # noqa: BLE001
                log.debug("authenticated: skipped one follower: %s", exc)
        return out


def _twscrape_post(tw, query_handle: str) -> Post:
    """Map a twscrape ``Tweet`` to :class:`~mediascrapers.models.Post`."""
    handle = getattr(getattr(tw, "user", None), "username", None) or query_handle
    url = getattr(tw, "url", None) or f"https://x.com/{handle}/status/{tw.id}"
    rt = getattr(tw, "retweetedTweet", None)
    qt = getattr(tw, "quotedTweet", None)
    post_type = "retweet" if rt else "quote" if qt else (
        "reply" if getattr(tw, "inReplyToTweetId", None) else "original"
    )
    body = rt or tw
    published = getattr(tw, "date", None)
    if published and published.tzinfo is None:
        published = published.replace(tzinfo=UTC)
    post = Post(
        guid=post_guid(handle, url),
        handle=handle,
        url=url,
        text=getattr(body, "rawContent", None) or getattr(body, "content", "") or "",
        published_at=published,
        post_type=post_type,
        lang=(getattr(tw, "lang", None) or "fr")[:8],
        likes=getattr(tw, "likeCount", None),
        retweets=getattr(tw, "retweetCount", None),
        replies=getattr(tw, "replyCount", None),
        quotes=getattr(tw, "quoteCount", None),
        views=getattr(tw, "viewCount", None),
        collected_via="auth",
        tweet_id=str(tw.id),
        conversation_id=str(getattr(tw, "conversationId", "") or tw.id),
        author_id=str(getattr(getattr(tw, "user", None), "id", "") or "") or None,
        reply_to_user_id=_str_or_none(getattr(tw, "inReplyToUser", None) and tw.inReplyToUser.id),
        mentions=[m.username for m in getattr(tw, "mentionedUsers", []) or []],
        hashtags=list(getattr(tw, "hashtags", []) or []),
        urls=[u.expandedUrl if hasattr(u, "expandedUrl") else str(u)
              for u in getattr(tw, "links", []) or []],
        source=getattr(tw, "source", None) or getattr(tw, "sourceLabel", None),
    )
    carried = qt or rt
    if carried is not None:
        c_user = getattr(getattr(carried, "user", None), "username", None)
        post.quoted_handle = c_user
        post.quoted_user_id = _str_or_none(getattr(getattr(carried, "user", None), "id", None))
        post.quoted_url = getattr(carried, "url", None)
        if qt is not None:
            post.quoted_text = (getattr(qt, "rawContent", None) or "")[:2000] or None
    return post


def _twscrape_profile(u) -> Profile:
    """Map a twscrape ``User`` to :class:`~mediascrapers.models.Profile`."""
    created = getattr(u, "created", None)
    if created and created.tzinfo is None:
        created = created.replace(tzinfo=UTC)
    return Profile(
        handle=getattr(u, "username", ""),
        user_id=_str_or_none(getattr(u, "id", None)),
        followers=getattr(u, "followersCount", None),
        statuses=getattr(u, "statusesCount", None),
        protected=bool(getattr(u, "protected", False)),
        name=getattr(u, "displayname", None),
        description=(getattr(u, "rawDescription", None) or "").strip() or None,
        location=(getattr(u, "location", None) or "").strip() or None,
        website=getattr(u, "url", None),
        created_at=created,
        verified=bool(getattr(u, "verified", False)),
        blue_verified=bool(getattr(u, "blue", False)),
        following=getattr(u, "friendsCount", None),
        likes_given=getattr(u, "favouritesCount", None),
        listed=getattr(u, "listedCount", None),
        media_count=getattr(u, "mediaCount", None),
        profile_image_url=getattr(u, "profileImageUrl", None),
        collected_at=datetime.now(UTC),
    )


def _str_or_none(v) -> str | None:
    return str(v) if v is not None else None


def default_backends(config: HttpConfig | None = None) -> list[Backend]:
    """The no-account routes, ready to use without any configuration."""
    return [SyndicationBackend(config), HydrateBackend(config), BackfillBackend(config)]
