from __future__ import annotations

import json
from pathlib import Path

from mediascrapers.models import Source

_BUNDLED = Path(__file__).resolve().parents[3] / "sources"


def load_sources(path: str | Path, *, active_only: bool = True) -> list[Source]:
    """Read a source list from JSON.

    Accepts either a bare list of source objects or ``{"sources": [...]}``.
    A name without a slash (``press_fr``) resolves to the bundled ``sources/``
    directory.
    """
    p = Path(path)
    if not p.suffix and "/" not in str(path):
        p = _BUNDLED / f"{path}.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    items = data["sources"] if isinstance(data, dict) else data
    sources = [Source.from_dict(d) for d in items]
    if active_only:
        sources = [s for s in sources if s.is_active]
    return sources
