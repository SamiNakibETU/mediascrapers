"""Article text cleaning: strip navigation, teasers and links, keep the prose intact.

Sentences are never rewritten. Only lines that are clearly outside the article
body (share buttons, "read also" teasers, credits, reading time) are removed,
markdown links are replaced by their anchor text, and whitespace is normalised.
"""

from __future__ import annotations

import html
import re
import unicodedata

_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_URL_RE = re.compile(r"https?://\S+|www\.\S+")
_EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
_TAG_RE = re.compile(r"<[^>]+>")
_SPACES_RE = re.compile(r"[ \t ]+")
_BLANK_LINES_RE = re.compile(r"\n{3,}")
_READING_TIME_RE = re.compile(r"^\s*\d+\s*min(utes)?\b")

# A line starting with one of these (accents stripped, lowercased) is dropped.
DROP_PREFIXES = (
    "lire aussi", "a lire aussi", "a lire egalement", "a lire", "voir aussi",
    "sur le meme sujet", "le meme sujet", "a decouvrir", "a voir aussi",
    "ceci peut vous interesser", "vous aimerez aussi", "ces articles peuvent",
    "dans la meme rubrique", "pour aller plus loin", "en savoir plus",
    "publie le", "mis a jour le", "modifie le", "credit photo", "credits photo",
    "photo :", "illustration :", "source afp", "avec afp", "abonnez-vous",
    "s'abonner", "newsletter", "inscrivez-vous", "recevez", "suivez-nous",
    "suivez l'actualite", "suivez toute l'actualite", "partager",
    "partagez", "tweeter", "commenter", "reagir", "0 commentaire",
    "la suite apres cette publicite", "publicite", "lecture :", "temps de lecture",
    "cet article est reserve", "video :", "regardez :", "en images",
    "read also", "read more", "related articles", "share this", "subscribe",
    "advertisement", "photo credit",
)

# A short line (nine words or fewer) containing one of these is dropped.
DROP_IF_SHORT = (
    "partager sur", "partager l'article", "sur facebook", "sur twitter",
    "sur whatsapp", "sur linkedin", "copier le lien", "min de lecture",
    "minutes de lecture", "accepter les cookies", "gerer les cookies",
    "afficher les commentaires", "laisser un commentaire", "tous droits reserves",
    "mots-cles", "voir les commentaires", "ajouter aux favoris",
    "share on", "copy link", "all rights reserved", "min read",
)


def strip_accents(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)
    ).lower()


def clean_html(raw: str | None) -> str:
    """Remove tags, decode entities, collapse whitespace."""
    text = _TAG_RE.sub(" ", raw or "")
    text = html.unescape(text)
    return _SPACES_RE.sub(" ", text).strip()


def _is_boilerplate(line: str) -> bool:
    norm = strip_accents(line).strip()
    if not norm:
        return False
    if norm.startswith(DROP_PREFIXES):
        return True
    words = len(norm.split())
    if _READING_TIME_RE.match(norm) and words <= 6:
        return True
    return words <= 9 and any(marker in norm for marker in DROP_IF_SHORT)


def clean_article_text(text: str | None) -> str:
    if not text:
        return ""
    t = _TAG_RE.sub(" ", text)
    t = _MD_LINK_RE.sub(r"\1", t)
    t = _URL_RE.sub("", t)
    t = _EMAIL_RE.sub("", t)

    kept: list[str] = []
    prev: str | None = None
    for raw in t.splitlines():
        line = _SPACES_RE.sub(" ", raw).strip()
        if _is_boilerplate(line):
            continue
        if line and line == prev:
            continue
        kept.append(line)
        prev = line or prev
    return _BLANK_LINES_RE.sub("\n\n", "\n".join(kept)).strip()
