from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Literal

PostType = Literal["original", "reply", "quote", "retweet"]

_STATUS_RE = re.compile(r"/status/(\d{15,20})")


def sha256(text: str) -> str:
    return hashlib.sha256(text.strip().encode()).hexdigest()


def status_id(url: str) -> str | None:
    m = _STATUS_RE.search(url or "")
    return m.group(1) if m else None


def post_guid(handle: str, url: str) -> str:
    """Stable dedup key for a tweet: hash of ``handle/status/<id>``.

    Identical whichever collector produced the post, so a syndication fetch
    and a backfill of the same tweet collapse to one key.
    """
    sid = status_id(url)
    key = f"{handle.lower()}/status/{sid}" if sid else (url or "").strip()
    return sha256(key)


@dataclass(slots=True)
class Post:
    guid: str
    handle: str
    url: str
    text: str
    published_at: datetime | None
    post_type: PostType = "original"
    lang: str = "fr"
    reply_to_handle: str | None = None
    reply_to_url: str | None = None
    quoted_handle: str | None = None
    quoted_url: str | None = None
    quoted_text: str | None = None
    media_url: str | None = None
    likes: int | None = None
    retweets: int | None = None
    replies: int | None = None
    quotes: int | None = None
    views: int | None = None
    text_truncated: bool = False
    collected_via: str = ""
    # Graph fields: what network analysis needs beyond the text.
    tweet_id: str | None = None
    conversation_id: str | None = None
    author_id: str | None = None
    reply_to_user_id: str | None = None
    quoted_user_id: str | None = None
    mentions: list[str] = field(default_factory=list)
    hashtags: list[str] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)
    source: str | None = None

    @property
    def is_retweet(self) -> bool:
        return self.post_type == "retweet"

    @property
    def is_reply(self) -> bool:
        return self.post_type == "reply"

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        if self.published_at:
            d["published_at"] = self.published_at.isoformat()
        return d


@dataclass(slots=True)
class Profile:
    handle: str
    user_id: str | None = None
    followers: int | None = None
    statuses: int | None = None
    protected: bool = False
    name: str | None = None
    description: str | None = None
    location: str | None = None
    website: str | None = None
    created_at: datetime | None = None
    verified: bool = False
    blue_verified: bool = False
    following: int | None = None
    likes_given: int | None = None
    listed: int | None = None
    media_count: int | None = None
    profile_image_url: str | None = None
    collected_at: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        for k in ("created_at", "collected_at"):
            if d.get(k):
                d[k] = d[k].isoformat()
        return d


@dataclass(slots=True)
class Source:
    """A press source polled through its RSS feed."""

    id: str
    name: str
    rss_url: str
    homepage: str | None = None
    language: str = "fr"
    country: str | None = None
    category: str | None = None
    leaning: str | None = None
    is_active: bool = True
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Source:
        known = {f for f in cls.__dataclass_fields__}  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass(slots=True)
class Extraction:
    """Full text of an article plus how it was obtained and how complete it looks."""

    text: str | None = None
    method: str = "empty"
    is_full: bool | None = None
    paywalled: bool | None = None

    @property
    def ok(self) -> bool:
        return bool(self.text)


@dataclass(slots=True)
class Article:
    url: str
    url_hash: str
    source_id: str
    title: str
    text: str
    published_at: datetime | None
    published_estimated: bool = False
    summary: str = ""
    language: str = "fr"
    extraction_method: str = "empty"
    is_full: bool | None = None
    paywalled: bool | None = None
    word_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        if self.published_at:
            d["published_at"] = self.published_at.isoformat()
        return d
