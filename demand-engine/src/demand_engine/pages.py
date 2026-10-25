"""Product pages frozen for the cases: var/pages/<id>.html (the rendered DOM) and <id>.json.

`fetch` captures with the shared capture engine (D-046): legitimacy of the site, a real
Chrome, no reader's pace for a single page, and the full snapshot of every fetch in
var/pages/<id>/<at>/ (meta.json, response, DOM, MHTML, robots.txt). It needs Chrome and
websockets, so on the host taxo runs it in the container. Reading needs neither.
"""
import gzip
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
from pathlib import Path

from . import ROOT

PAGES = ROOT / "var/pages"


class PageError(LookupError):
    pass


def page_path(case_id: str) -> Path:
    path = PAGES / f"{case_id}.html"
    if not path.exists():
        raise PageError(f"no hay página congelada para {case_id}; usa: taxo page fetch {case_id} URL")
    return path


def read(case_id: str) -> str:
    return page_path(case_id).read_text(encoding="utf-8", errors="replace")


def text_lines(raw: str) -> list:
    text = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", raw)
    return [l.strip() for l in html.unescape(re.sub(r"(?s)<[^>]+>", "\n", text)).splitlines() if l.strip()]


def walk(node):
    """The nodes of a JSON-LD document, following graphs, entities, lists and variants."""
    if isinstance(node, list):
        for x in node:
            yield from walk(x)
    elif isinstance(node, dict):
        yield node
        for key in ("@graph", "mainEntity", "itemListElement", "hasVariant"):
            if key in node:
                yield from walk(node[key])


def json_ld(raw: str):
    """The JSON-LD blocks of a page that parse."""
    for m in re.finditer(r"<script[^>]+application/ld\+json[^>]*>(.*?)</script>", raw, re.S):
        try:
            yield json.loads(m.group(1).strip())
        except ValueError:
            continue


def engine_available() -> bool:
    """The capture engine needs websockets and Chrome: there in the container, not on the host."""
    return importlib.util.find_spec("websockets") is not None \
        and shutil.which(os.environ.get("CAPTURE_CHROME", "google-chrome")) is not None


def fetch(case_id: str, url: str, browser=None) -> dict:
    """Freeze a page with the capture engine (it replaces <id>.html; snapshots are kept).
    Returns the metadata written in <id>.json; a refusal or a block raises PageError."""
    from .capture import OUTCOMES
    from .capture.files import unique_dir
    from .capture.once import capture_once

    folder = unique_dir(PAGES / case_id)
    result = capture_once(url, folder, browser)
    where = f"var/pages/{case_id}/{folder.name}"
    if result["outcome"] != "captured":
        raise PageError(f"{case_id}: {OUTCOMES[result['outcome']]} — {result['detail']}; evidencia en {where}")
    meta = result["meta"]
    dom = gzip.decompress((folder / "dom.html.gz").read_bytes())
    (PAGES / f"{case_id}.html").write_bytes(dom)
    info = {"id": case_id, "url": url, "fetched_at": meta["finished_at"], "size": len(dom),
            "sha256": hashlib.sha256(dom).hexdigest(), "method": "chrome-cdp", "content": "DOM renderizado",
            "url_final": meta.get("url_final"), "http_status": (meta.get("http") or {}).get("status"),
            "user_agent": (meta.get("browser") or {}).get("user_agent"), "snapshot": where}
    (PAGES / f"{case_id}.json").write_text(json.dumps(info, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return info
