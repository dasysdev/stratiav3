"""The store of frozen pages shared by every system (D-150): var/pages/<id>.html (the rendered
DOM) and <id>.json, and the readers of a page (text lines, JSON-LD).

`fetch` captures with the engine: legitimacy of the site, a real Chrome, no reader's pace for a
single page, and the full snapshot of every fetch in var/pages/<id>/<at>/ (meta.json, response,
DOM, MHTML, robots.txt). It needs Chrome and websockets, so on the host bin/pages runs it in
the container. Reading needs neither. The capture profile (capture.profiles) is the caller's:
`reader` by default (the rendered DOM becomes the page); under `audit-es` the page is the
document of the HTTP response without JavaScript (D-156), decoded with the charset the browser
used, and its record adds the request context and robots.txt by bot. A page frozen before
profiles existed is a `reader` one.

A frozen page is never replaced: `fetch` and `freeze` refuse an ID that already has one, and a
new capture of the same product takes another ID. A refused or blocked fetch leaves only its
snapshot, so its ID stays free.
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
ID = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


class PageError(LookupError):
    pass


def page_path(case_id: str) -> Path:
    path = PAGES / f"{case_id}.html"
    if not path.exists():
        raise PageError(f"no hay página congelada para {case_id}; usa: capture/bin/pages fetch {case_id} URL")
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


def _response_text(folder: Path, meta: dict) -> bytes:
    """The document of the HTTP response in UTF-8, decoded as the browser decoded it (its
    charset, a BOM first); a charset Python does not know falls back to UTF-8."""
    raw = gzip.decompress((folder / "response.html.gz").read_bytes())
    charset = ((meta.get("dom") or {}).get("charset") or "utf-8").lower()
    for bom, codec in ((b"\xef\xbb\xbf", "utf-8"), (b"\xff\xfe", "utf-16-le"), (b"\xfe\xff", "utf-16-be")):
        if raw.startswith(bom):
            raw, charset = raw[len(bom):], codec
            break
    try:
        text = raw.decode(charset, errors="replace")
    except LookupError:
        text = raw.decode("utf-8", errors="replace")
    return text.encode("utf-8")


def engine_available() -> bool:
    """The capture engine needs websockets and Chrome: there in the container, not on the host."""
    return importlib.util.find_spec("websockets") is not None \
        and shutil.which(os.environ.get("CAPTURE_CHROME", "google-chrome")) is not None


def check_new(case_id: str) -> None:
    """A valid ID (kebab-case) with no frozen page yet; otherwise PageError."""
    if not ID.fullmatch(case_id):
        raise PageError(f"ID no válido: {case_id!r} (minúsculas, dígitos y guiones)")
    if (PAGES / f"{case_id}.html").exists() or (PAGES / f"{case_id}.json").exists():
        raise PageError(f"{case_id} ya tiene página congelada y no se sustituye; la captura nueva lleva otro ID")


def fetch(case_id: str, url: str, browser=None, profile: str | None = None) -> dict:
    """Freeze a page with the capture engine under a new ID (an existing one is refused before
    visiting). Returns the metadata written in <id>.json; a refusal or a block raises PageError."""
    check_new(case_id)
    from . import OUTCOMES, profiles
    from .files import unique_dir
    from .once import capture_once

    chosen = profiles.get(profile)   # an unknown profile is refused before visiting
    folder = unique_dir(PAGES / case_id)
    result = capture_once(url, folder, browser, chosen)
    where = f"var/pages/{case_id}/{folder.name}"
    if result["outcome"] != "captured":
        raise PageError(f"{case_id}: {OUTCOMES[result['outcome']]} — {result['detail']}; evidencia en {where}")
    return freeze(case_id, url, folder, result["meta"])


def freeze(case_id: str, url: str, folder: Path, meta: dict, extra: dict | None = None) -> dict:
    """The DOM of a captured snapshot becomes the page of `case_id` (<id>.html and <id>.json),
    which must not exist yet."""
    check_new(case_id)
    from . import profiles

    name = meta.get("profile") or profiles.READER.name
    if not profiles.get(name).javascript:   # without JavaScript the page is the response (D-156)
        doc, content = _response_text(folder, meta), "respuesta HTTP sin JavaScript"
    else:
        doc = gzip.decompress((folder / "dom.html.gz").read_bytes())
        first_load = any(a.get("action") == "first_load" for a in meta.get("actions") or [])
        content = "DOM de la primera carga" if first_load else "DOM renderizado"
    info = {"id": case_id, "url": url, "fetched_at": meta["finished_at"], "size": len(doc),
            "sha256": hashlib.sha256(doc).hexdigest(), "method": "chrome-cdp", "profile": name,
            "content": content,
            "url_final": meta.get("url_final"), "http_status": (meta.get("http") or {}).get("status"),
            "user_agent": (meta.get("browser") or {}).get("user_agent"),
            "snapshot": f"var/pages/{case_id}/{folder.name}"}
    if "request_context" in meta:
        info["request_context"] = meta["request_context"]
    if "robots_bots" in meta:
        info["robots_bots"] = meta["robots_bots"]
    info.update(extra or {})
    with open(PAGES / f"{case_id}.html", "xb") as f:
        f.write(doc)
    with open(PAGES / f"{case_id}.json", "x", encoding="utf-8") as f:
        f.write(json.dumps(info, ensure_ascii=False, indent=2) + "\n")
    return info
