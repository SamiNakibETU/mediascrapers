import json

import httpx

from mediascrapers.http import HttpConfig
from mediascrapers.models import Source, sha256
from mediascrapers.press.clean import clean_article_text, clean_html
from mediascrapers.press.extract import Extractor, ExtractorConfig, build_extraction, is_paywalled
from mediascrapers.press.feed import FeedCollector
from mediascrapers.press.sources import load_sources


def test_clean_removes_teasers_links_and_duplicates():
    raw = (
        "Le ministre a déclaré que [la réforme](https://x.y) serait votée.\n"
        "Lire aussi : un autre article\n"
        "Partager sur Facebook\n"
        "Même phrase.\nMême phrase.\n"
        "Contact : redaction@example.org et https://example.org/page\n"
        "3 min de lecture\n"
    )
    out = clean_article_text(raw)
    assert "la réforme serait votée" in out
    assert "Lire aussi" not in out and "Facebook" not in out
    assert out.count("Même phrase.") == 1
    assert "@" not in out and "https" not in out
    assert "min de lecture" not in out


def test_clean_keeps_long_paragraph_mentioning_a_marker():
    para = (
        "Il faut partager sur Facebook les résultats, a dit le maire, "
        "car la newsletter municipale ne suffit plus à informer."
    )
    assert clean_article_text(para) == para


def test_clean_html_decodes_entities():
    assert clean_html("<p>L&#39;&eacute;t&eacute; &amp; l'hiver</p>") == "L'été & l'hiver"


def test_paywall_detection():
    assert is_paywalled("Chapô. Il vous reste 85% de cet article à lire.")
    assert not is_paywalled("Un article complet sans marqueur.")
    ext = build_extraction("x" * 400, "fetch")
    assert ext.is_full is True and ext.paywalled is False


def test_load_bundled_sources():
    fr = load_sources("press_fr")
    assert fr and all(isinstance(s, Source) for s in fr)
    assert all(s.is_active for s in fr)
    mena = load_sources("press_mena")
    assert {s.country for s in mena} >= {"LB", "IL"}


def test_load_sources_from_file(tmp_path):
    p = tmp_path / "s.json"
    p.write_text(json.dumps([{"id": "a", "name": "A", "rss_url": "https://a/feed", "unknown_key": 1}]))
    (s,) = load_sources(p)
    assert s.id == "a" and s.language == "fr"


RSS = """<?xml version="1.0"?><rss version="2.0"><channel><title>T</title>
<item><title>Un &amp; deux</title><link>https://example.org/a1</link>
<description>Résumé</description><pubDate>Mon, 24 Aug 2026 08:00:00 GMT</pubDate>
<content:encoded xmlns:content="http://purl.org/rss/1.0/modules/content/"><![CDATA[%s]]></content:encoded></item>
<item><title>Déjà vu</title><link>https://example.org/seen</link></item>
</channel></rss>"""


async def test_feed_uses_full_rss_body_without_fetching_article():
    body = "<p>" + "Phrase complète de l'article. " * 60 + "</p>"
    fetched: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        fetched.append(str(request.url))
        return httpx.Response(200, text=RSS % body)

    http = HttpConfig(transport=httpx.MockTransport(handler))
    extractor = Extractor(ExtractorConfig(http=http, jina_enabled=False, wayback_enabled=False))
    collector = FeedCollector(extractor, http)
    seen = {sha256("https://example.org/seen")}
    source = Source(id="ex", name="Ex", rss_url="https://example.org/feed")
    articles = await collector.collect(source, seen=seen)

    assert len(articles) == 1
    a = articles[0]
    assert a.title == "Un & deux"
    assert a.extraction_method == "rss_full" and a.is_full is True
    assert a.published_at.isoformat() == "2026-08-24T08:00:00+00:00"
    assert a.word_count > 200
    assert fetched == ["https://example.org/feed"]
    assert sha256("https://example.org/a1") in seen
