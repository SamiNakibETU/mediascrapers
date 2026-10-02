# mediascrapers

Collectors for X timelines and online press, packaged as a library so they can
be dropped into other projects. Extracted from ED Mediawatch, where they have
run in production since August 2026; the database layer and project-specific
filtering were left behind.

Three building blocks:

| Module | What it does | Cost |
|---|---|---|
| `mediascrapers.x` | Recent tweets of any public account through X's own syndication endpoint; historical tweets through Wayback CDX and fxtwitter | free, no account |
| `mediascrapers.press` | RSS polling, full-text extraction with a fallback chain (direct fetch, Jina Reader, Wayback), boilerplate removal | free |
| `mediascrapers.archive` | Wayback lookup and Save Page Now | free |

Everything returns plain dataclasses (`Post`, `Article`, `Source`). Storage is
the caller's business.

## Install

```bash
pip install git+ssh://git@github.com/SamiNakibETU/mediascrapers.git
# or, for development
git clone git@github.com:SamiNakibETU/mediascrapers.git && cd mediascrapers
pip install -e ".[dev]"
```

Python 3.11 or later.

## Command line

```bash
# last 20-100 tweets of one or more handles, one JSON object per line
mediascrapers x timeline J_Bardella MLP_officiel > tweets.jsonl

# archived tweets since 2022 (Wayback ids, fxtwitter content)
mediascrapers x backfill J_Bardella --since 2022 --limit 300 > history.jsonl

# poll a source list (bundled: press_fr, press_mena) and extract full text
mediascrapers press collect press_fr > articles.jsonl
mediascrapers press collect sources/press_mena.json --only lorient_le_jour

# full text of arbitrary URLs
mediascrapers press extract https://www.lemonde.fr/...
```

## Library

```python
import asyncio
from mediascrapers.x import SyndicationClient, Backfill
from mediascrapers.press import FeedCollector, Extractor, load_sources

async def main():
    x = SyndicationClient()
    posts = await x.collect("J_Bardella")          # list[Post] or None if unreachable
    print(x.last_profile.followers)

    history = await Backfill().run("J_Bardella", since_year=2023, limit=200)

    sources = load_sources("press_mena")
    seen: set[str] = set()                          # url hashes already stored
    articles = await FeedCollector(Extractor()).collect_all(sources, seen=seen)

asyncio.run(main())
```

### Filtering before extraction

Fetching an article body is the expensive step. `FeedCollector` takes a
`prefilter(title, summary) -> bool` so the caller can discard entries first:

```python
names = ("bardella", "le pen", "zemmour")
collector = FeedCollector(prefilter=lambda t, s: any(n in f"{t} {s}".lower() for n in names))
```

### Paywalled sources you subscribe to

Pass per-domain cookie headers; they are tried first:

```python
from mediascrapers.press import Extractor, ExtractorConfig
extractor = Extractor(ExtractorConfig(cookies={"lemonde.fr": "lmd_a_s=...; lmd_sso=..."}))
```

### Truncated tweets

The syndication endpoint cuts long tweets at 280 characters. Posts touching the
limit carry `text_truncated=True`; `Backfill().expand_truncated(posts)` fetches
the full text by id.

## Source lists

`sources/press_fr.json` holds 60 French outlets. `sources/press_mena.json` is a
starting point for Middle East coverage. The format:

```json
{"id": "lorient_le_jour", "name": "L'Orient-Le Jour", "rss_url": "https://www.lorientlejour.com/rss",
 "homepage": "https://www.lorientlejour.com", "language": "fr", "country": "LB", "category": "daily"}
```

Optional fields: `leaning`, `tags`, `is_active` (default true; set false to
keep a dead feed on record without polling it).

## Behaviour and limits

* X requests are serial and paced (2.5 s by default). The endpoint publishes
  `x-rate-limit-*` headers; the client reads them and sleeps until the reset
  rather than retrying blindly. A full pass over 110 handles takes about six
  minutes.
* fxtwitter and Jina Reader are third-party services. Keep request rates low;
  if either disappears, the primary paths (syndication, RSS, direct fetch) do
  not depend on them.
* Retweets carry the original author's text. `Post.is_retweet` is set so the
  consumer never attributes relayed words to the account that relayed them.
* Extraction prefers a shorter clean text over a longer one carrying a
  paywall marker: a paywall page is long but is not the article.

## Development

```bash
pytest
ruff check src tests
```
