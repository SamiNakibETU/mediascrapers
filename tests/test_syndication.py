import json

from mediascrapers.x.syndication import parse_profile, parse_timeline, timeline_state

USER = {"screen_name": "J_Bardella", "id_str": "42", "followers_count": 1000}


def page(entries: list[dict]) -> str:
    payload = {"props": {"pageProps": {"timeline": {"entries": entries}}}}
    return f'<html><script id="__NEXT_DATA__" type="application/json">{json.dumps(payload)}</script></html>'


def entry(**tweet) -> dict:
    base = {
        "id_str": "2091800582042333264",
        "created_at": "Mon Aug 24 08:11:37 +0000 2026",
        "full_text": "Texte du tweet https://t.co/abc",
        "entities": {"urls": [{"url": "https://t.co/abc", "expanded_url": "https://example.org/a"}]},
        "favorite_count": 1239, "retweet_count": 220, "reply_count": 40, "quote_count": 12,
        "lang": "fr", "user": USER,
    }
    base.update(tweet)
    return {"content": {"tweet": base}}


def test_original_tweet():
    (p,) = parse_timeline(page([entry()]), "J_Bardella")
    assert p.url == "https://x.com/J_Bardella/status/2091800582042333264"
    assert p.post_type == "original" and not p.is_retweet and not p.is_reply
    assert p.text == "Texte du tweet https://example.org/a"
    assert p.published_at.isoformat() == "2026-08-24T08:11:37+00:00"
    assert (p.likes, p.retweets, p.replies, p.quotes) == (1239, 220, 40, 12)
    assert p.collected_via == "syndication"


def test_retweet_carries_original_text_and_author():
    rt = entry(
        full_text="RT @K_Pfeffer: Le sérieux…",
        retweeted_status={"id_str": "1", "full_text": "Le sérieux du Canard est en cause.",
                          "entities": {}, "user": {"screen_name": "K_Pfeffer"}},
    )
    (p,) = parse_timeline(page([rt]), "J_Bardella")
    assert p.post_type == "retweet"
    assert p.text == "Le sérieux du Canard est en cause."
    assert p.quoted_handle == "K_Pfeffer"
    assert p.quoted_url == "https://x.com/K_Pfeffer/status/1"
    assert p.quoted_text is None


def test_quote_keeps_quoted_text():
    q = entry(quoted_status={"id_str": "9", "full_text": "Propos cité", "entities": {},
                             "user": {"screen_name": "someone"}})
    (p,) = parse_timeline(page([q]), "J_Bardella")
    assert p.post_type == "quote"
    assert p.quoted_text == "Propos cité"


def test_reply_strips_leading_mentions():
    r = entry(full_text="@a @b Réponse", display_text_range=[6, 13],
              in_reply_to_screen_name="a", in_reply_to_status_id_str="7")
    (p,) = parse_timeline(page([r]), "J_Bardella")
    assert p.post_type == "reply"
    assert p.text == "Réponse"
    assert p.reply_to_url == "https://x.com/a/status/7"


def test_truncated_tweet_flagged_and_link_stub_removed():
    text = "x" * 275 + " https://t.c"
    (p,) = parse_timeline(page([entry(full_text=text, entities={})]), "J_Bardella")
    assert p.text_truncated is True
    assert p.text == "x" * 275


def test_video_media_picks_best_mp4():
    media = {"type": "video", "media_url_https": "thumb.jpg", "video_info": {"variants": [
        {"content_type": "video/mp4", "bitrate": 200, "url": "low.mp4"},
        {"content_type": "video/mp4", "bitrate": 900, "url": "high.mp4"},
        {"content_type": "application/x-mpegURL", "url": "x.m3u8"},
    ]}}
    (p,) = parse_timeline(page([entry(extended_entities={"media": [media]})]), "J_Bardella")
    assert p.media_url == "high.mp4"


def test_profile_and_state():
    html = page([entry()])
    prof = parse_profile(html, "j_bardella")
    assert prof.user_id == "42" and prof.followers == 1000
    assert timeline_state(html) == "ok"
    assert timeline_state(page([])) == "empty"
    assert parse_timeline("<html></html>", "x") == []
