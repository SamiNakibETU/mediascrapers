"""Command line entry point: ``mediascrapers x timeline J_Bardella``."""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from collections.abc import Iterable

from mediascrapers.http import HttpConfig
from mediascrapers.press import Extractor, FeedCollector, load_sources
from mediascrapers.x import Backfill, SyndicationClient


def _emit(items: Iterable, out) -> None:
    for item in items:
        out.write(json.dumps(item.to_dict(), ensure_ascii=False) + "\n")


async def _x_timeline(args) -> None:
    client = SyndicationClient(HttpConfig(delay=args.delay))
    for handle in args.handles:
        posts = await client.collect(handle)
        if posts is None:
            logging.getLogger("mediascrapers").warning("%s: no answer", handle)
            continue
        _emit(posts, sys.stdout)


async def _x_backfill(args) -> None:
    backfill = Backfill(HttpConfig(delay=args.delay))
    for handle in args.handles:
        posts = await backfill.run(handle, since_year=args.since, limit=args.limit)
        _emit(posts, sys.stdout)


async def _press_collect(args) -> None:
    sources = load_sources(args.sources)
    if args.only:
        wanted = set(args.only)
        sources = [s for s in sources if s.id in wanted]
    collector = FeedCollector(Extractor(), HttpConfig(concurrency=args.concurrency))
    articles = await collector.collect_all(sources)
    _emit(articles, sys.stdout)


async def _press_extract(args) -> None:
    extractor = Extractor()
    for url in args.urls:
        ext = await extractor.extract(url)
        sys.stdout.write(json.dumps(
            {"url": url, "method": ext.method, "is_full": ext.is_full,
             "paywalled": ext.paywalled, "text": ext.text},
            ensure_ascii=False,
        ) + "\n")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="mediascrapers", description="Collect X timelines and press articles as JSON lines."
    )
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="command", required=True)

    x = sub.add_parser("x", help="X / Twitter").add_subparsers(dest="action", required=True)
    t = x.add_parser("timeline", help="recent tweets of one or more handles")
    t.add_argument("handles", nargs="+")
    t.add_argument("--delay", type=float, default=2.5)
    t.set_defaults(run=_x_timeline)
    b = x.add_parser("backfill", help="archived tweets since a given year")
    b.add_argument("handles", nargs="+")
    b.add_argument("--since", type=int, default=2022)
    b.add_argument("--limit", type=int, default=300)
    b.add_argument("--delay", type=float, default=1.0)
    b.set_defaults(run=_x_backfill)

    press = sub.add_parser("press", help="online press").add_subparsers(dest="action", required=True)
    c = press.add_parser("collect", help="poll RSS feeds from a source file")
    c.add_argument("sources", help="path to a JSON source list, or a bundled name such as press_fr")
    c.add_argument("--only", nargs="*", help="restrict to these source ids")
    c.add_argument("--concurrency", type=int, default=3)
    c.set_defaults(run=_press_collect)
    e = press.add_parser("extract", help="full text of one or more article URLs")
    e.add_argument("urls", nargs="+")
    e.set_defaults(run=_press_extract)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )
    asyncio.run(args.run(args))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
