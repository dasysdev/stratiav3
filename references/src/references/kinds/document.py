"""One published document (HTML page, PDF or data file), versioned by fetch date. An HTML page
is kept as published (page.html, which counts by its text) plus its text (text.md)."""
import difflib
import json
import urllib.parse
from pathlib import Path

from .. import net
from ..html import charset, page_text, published
from ..store import RefsError, Version, entry, fingerprint, latest_manifest, refs_dir, sha256, today

EXTENSIONS = {"application/pdf": ".pdf", "application/ld+json": ".jsonld", "application/json": ".json",
              "text/turtle": ".ttl", "text/plain": ".txt", "text/csv": ".csv", "application/xml": ".xml"}
INTERVAL = 1.0      # seconds between two document downloads


def files(url: str) -> tuple:
    """Download a document: ([(path, data, manifest entry)], origin)."""
    data, headers, final = net.download(url)
    content_type = (headers.get("content-type") or "").split(";")[0].strip().lower()
    origin = {"url": url, "final_url": final, "content_type": content_type}
    if headers.get("last-modified"):
        origin["last_modified"] = headers["last-modified"]
    if content_type in ("text/html", "application/xhtml+xml"):
        html = data.decode(charset(data, headers.get("content-type")), errors="replace")
        text = page_text(html).encode("utf-8")
        marker = published(html)
        if marker:
            origin["published"] = marker
        return [("page.html", data, entry("page.html", data, final, counted_by="text.md")),
                ("text.md", text, entry("text.md", text, "page.html"))], origin
    path = Path(urllib.parse.urlsplit(final).path)
    name = path.name if path.suffix else "document" + EXTENSIONS.get(content_type, "")
    if not Path(name).suffix:
        raise RefsError(f"{url}: tipo {content_type or 'desconocido'} sin extensión conocida")
    return [(name, data, entry(name, data, final))], origin


def check(sid: str, source: dict) -> str:
    latest = latest_manifest(sid)
    if not latest:
        return "sin descargar"
    found, _ = files(source["url"])
    if fingerprint(latest["files"]) == fingerprint([e for _, _, e in found]):
        return f"al día ({latest['version']})"
    return f"cambió desde {latest['version']}: refs fetch {sid}"


def fetch(sid: str, source: dict, tag: str) -> None:
    found, origin = files(source["url"])
    snap = Version(sid, today(), origin)
    for path, data, item in found:
        snap.put(path, data, item)
    snap.commit()


def content_file(folder: Path):
    """The file a document diff reads: its text, or its only file."""
    names = [f["path"] for f in json.loads((folder / "MANIFEST.json").read_text(encoding="utf-8"))["files"]]
    return folder / ("text.md" if "text.md" in names else names[0])


def diff(sid: str, old: str, new: str, limit: int) -> None:
    before, after = content_file(refs_dir() / sid / old), content_file(refs_dir() / sid / new)
    try:
        a = before.read_text(encoding="utf-8").splitlines()
        b = after.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        print(f"{after.name}: contenido binario; sha256 {sha256(before.read_bytes())[:12]} → "
              f"{sha256(after.read_bytes())[:12]}")
        return
    lines = list(difflib.unified_diff(a, b, f"{old}/{before.name}", f"{new}/{after.name}", n=1, lineterm=""))
    added = sum(1 for l in lines if l.startswith("+") and not l.startswith("+++"))
    removed = sum(1 for l in lines if l.startswith("-") and not l.startswith("---"))
    print(f"{after.name}: +{added} −{removed} líneas")
    for line in lines[:limit]:
        print(f"  {line}")
    if len(lines) > limit:
        print(f"  … +{len(lines) - limit} líneas más (--all)")
