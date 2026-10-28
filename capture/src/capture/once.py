"""Capture of a single page (pages.fetch): the legitimacy of its site, one visit without a
reader's pace and its snapshot. The refusals (robots.txt, TDM reservation) also leave meta.json.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

from . import profile
from .browser import Browser
from .files import now
from .legitimacy import access
from .tdm import reserved_by_entries
from .visit import visit


def capture_once(url: str, folder: Path, browser: Browser | None = None) -> dict:
    """Snapshot of `url` in `folder`: {'outcome', 'detail', 'meta'} (and 'elapsed_s' if visited).
    Uses the Chrome already running in the container, or launches one."""
    own = browser is None
    if own:
        browser = Browser(profile())
        browser.start()
    page = browser.new_window()
    try:
        parts = urlsplit(url)
        base = f"{parts.scheme}://{parts.netloc}"
        robots, entries, summary = access(page, base, folder)
        meta = {"legitimacy": summary}
        if not robots.allowed(url):
            detail = "robots.txt inaccesible" if robots.mode == "unreachable" else "robots.txt"
            return _refused(folder, url, meta, "disallowed", detail)
        if reserved_by_entries(entries, url):
            return _refused(folder, url, meta, "reserved", "reserva TDM (tdmrep.json): no se conserva el contenido")
        return visit(page, url, folder, None, entries, browser.info, meta=meta)
    finally:
        browser.close_window(page)
        if own:
            browser.stop()


def _refused(folder: Path, url: str, meta: dict, outcome: str, detail: str) -> dict:
    meta = {**meta, "url_requested": url, "outcome": outcome, "detail": detail, "files": {}, "finished_at": now()}
    (folder / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"outcome": outcome, "detail": detail, "meta": meta}
