"""Sources of the technical reference, frozen by version under web-audit/var/refs/.

The sources are declared in reference/sources.json. Each one keeps immutable versions in
refs/<source>/<version>/: the files as published, the text of each HTML page (text.md, what a
citation quotes) and a MANIFEST.json (origin, size, sha256, fetch date). A new version never
overwrites an existing one, and a fetch whose content equals the latest version is discarded.
The version the reference cites is pinned in refs/pins.json; only `refs pin` changes it,
because a new pin obliges a review of the source cards and requirements that cite the previous
one. The first version of a source is pinned automatically. Everything here is disposable
(var/): what matters is the version each citation names.

Kinds of source (`kind` in sources.json):
  schemaorg   Schema.org vocabulary in machine format, by release (GitHub schemaorg/schemaorg,
              data/releases/<version>/), checked against the git sha of each file
  document    one published document (HTML page, PDF or data file), versioned by fetch date.
              An HTML page counts by its text: a change of markup alone is no new version

Usage:
  refs [status]                      versions per source and the pinned one
  refs check [SOURCE...]             has the source changed upstream? (stores nothing)
  refs fetch [SOURCE...] [--version V]
                                     download a new version (--version: Schema.org release)
  refs diff SOURCE [OLD [NEW]] [--all]
                                     text changes of a document; added, removed and changed
                                     terms of the vocabulary (default: pinned → latest)
  refs pin SOURCE VERSION            set the version the reference cites

REFS_DIR overrides the refs directory and SOURCES_FILE the registry (tests).
"""
import argparse
import codecs
import difflib
import gzip
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path

from . import ROOT

REFS = Path(os.environ.get("REFS_DIR") or ROOT / "var/refs")
PINS = REFS / "pins.json"
SOURCES_FILE = Path(os.environ.get("SOURCES_FILE") or ROOT / "reference/sources.json")

USER_AGENT = "stratia-refs/1.0"
KINDS = ("schemaorg", "document")
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SCHEMAORG_API = "https://api.github.com/repos/schemaorg/schemaorg"
SCHEMAORG_FILES = (
    "schemaorg-current-https.jsonld",             # the vocabulary
    "schemaorg-all-https.jsonld",                 # plus the retired terms (attic)
    "schemaorg-current-https-types.csv",
    "schemaorg-current-https-properties.csv",
    "schemaorgcontext.jsonld",                    # JSON-LD context of the release
)
VOCABULARY = SCHEMAORG_FILES[0]
DOCUMENT_INTERVAL = 1.0     # seconds between two document downloads
DIFF_LIMIT = 40             # lines per section unless --all
RETRY_CODES = (429, 500, 502, 503, 504)
EXTENSIONS = {"application/pdf": ".pdf", "application/ld+json": ".jsonld", "application/json": ".json",
              "text/turtle": ".ttl", "text/plain": ".txt", "text/csv": ".csv", "application/xml": ".xml"}
PUBLISHED = (               # the publisher's own version marker, kept in the manifest
    (re.compile(r"Last updated (\d{4}-\d{2}-\d{2}) UTC"), "Last updated {0}"),        # Google developers
    (re.compile(r'id="versioninfo".{0,300}?V([\d.]+).{0,100}?(\d{4}-\d{2}-\d{2})', re.S), "Schema.org V{0} ({1})"),
    (re.compile(r"This version:.{0,300}?href=\"([^\"]+)\"", re.S), "This version: {0}"),  # W3C
)


class RefsError(LookupError):
    pass


def fail(msg: str) -> None:
    print(f"refs: {msg}", file=sys.stderr)
    sys.exit(1)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_sha(data: bytes) -> str:
    """The sha GitHub gives for a file: its git blob id."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def dumps(obj) -> bytes:
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True).encode("utf-8")


def today() -> str:
    return date.today().isoformat()


def natural(name: str) -> list:
    """Sort key: 9.0 before 30.1, 2026-10-27 before 2026-11-02."""
    return [(0, int(p), "") if p.isdigit() else (1, 0, p) for p in re.split(r"(\d+)", name)]


# --- Registry -----------------------------------------------------------------

def sources() -> dict:
    """reference/sources.json by id, checked: kebab-case unique ids, a known kind, title and URL."""
    entries = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))["sources"]
    out, errors = {}, []
    for i, entry in enumerate(entries, 1):
        sid = entry.get("id") or f"#{i}"
        if not ID_RE.match(sid):
            errors.append(f"{sid}: el id ha de ser kebab-case")
        elif sid in out:
            errors.append(f"{sid}: id repetido")
        if entry.get("kind") not in KINDS:
            errors.append(f"{sid}: kind «{entry.get('kind')}» desconocido ({', '.join(KINDS)})")
        errors += [f"{sid}: falta {key}" for key in ("title", "url") if not entry.get(key)]
        out[sid] = entry
    if errors:
        fail(f"{SOURCES_FILE.name}:\n  " + "\n  ".join(errors))
    return out


# --- HTTP ---------------------------------------------------------------------

def request(url: str, headers: dict = None, retries: int = 4):
    """Open a URL, retrying on throttling, server errors and network failures."""
    hdrs = {"user-agent": USER_AGENT, **(headers or {})}
    for attempt in range(retries + 1):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=hdrs), timeout=120)
        except urllib.error.HTTPError as e:
            if e.code not in RETRY_CODES or attempt == retries:
                raise
        except urllib.error.URLError:
            if attempt == retries:
                raise
        time.sleep(2 ** attempt)


def download(url: str) -> tuple:
    """(body, response headers, final URL). Some servers compress without being asked."""
    with request(url) as r:
        data, headers, final = r.read(), r.headers, r.geturl()
    encoding = (headers.get("content-encoding") or "identity").lower()
    if encoding == "gzip":
        data = gzip.decompress(data)
    elif encoding != "identity":
        raise RefsError(f"{url}: content-encoding {encoding} no admitido")
    return data, headers, final


def get_json(url: str):
    return json.loads(download(url)[0])


# --- Snapshots ----------------------------------------------------------------

def versions(source: str) -> list:
    folder = REFS / source
    if not folder.exists():
        return []
    return sorted((p.name for p in folder.iterdir() if (p / "MANIFEST.json").exists()), key=natural)


def manifest(source: str, version: str) -> dict:
    return json.loads((REFS / source / version / "MANIFEST.json").read_text(encoding="utf-8"))


def latest_manifest(source: str):
    found = versions(source)
    return manifest(source, found[-1]) if found else None


def pins() -> dict:
    return json.loads(PINS.read_text(encoding="utf-8")) if PINS.exists() else {}


def save_pins(data: dict) -> None:
    PINS.parent.mkdir(parents=True, exist_ok=True)
    PINS.write_bytes(dumps(data) + b"\n")


def entry(path: str, data: bytes, origin: str, **extra) -> dict:
    return {"path": path, "origin": origin, "size": len(data), "sha256": sha256(data), **extra}


def fingerprint(files: list) -> list:
    """What counts as content: every file but the HTML pages, which count by their text."""
    return sorted((f["path"], f["sha256"]) for f in files if "counted_by" not in f)


def store(source: str, version: str, origin: dict, files: list) -> bool:
    """Write a version from [(path, data, entry)]. False, writing nothing, if the content
    equals the latest version."""
    entries = [e for _, _, e in files]
    previous = latest_manifest(source)
    if previous and fingerprint(previous["files"]) == fingerprint(entries):
        print(f"{source}: sin cambios respecto a {previous['version']}; no se crea versión")
        return False
    if version in versions(source):
        raise RefsError(f"{source}: ya hay una versión {version} con otro contenido; "
                        "las versiones no se sobrescriben")
    final = REFS / source / version
    tmp = REFS / source / f".partial-{version}"
    shutil.rmtree(tmp, ignore_errors=True)
    for path, data, _ in files:
        (tmp / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp / path).write_bytes(data)
    (tmp / "MANIFEST.json").write_bytes(dumps({
        "source": source,
        "version": version,
        "fetched_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "origin": origin,
        "files": sorted(entries, key=lambda f: f["path"]),
    }) + b"\n")
    tmp.rename(final)
    size = sum(e["size"] for e in entries) / 1e6
    print(f"{source}: {version} descargada ({len(entries)} ficheros, {size:.1f} MB)")
    current = pins()
    if source not in current:
        current[source] = version
        save_pins(current)
        print(f"{source}: fijada {version} (primera versión)")
    return True


# --- Reading ------------------------------------------------------------------

def pinned(source: str) -> Path:
    """Folder of the version of `source` the reference cites."""
    current = pins()
    if source not in current:
        raise RefsError(f"{source} no está fijada; ejecuta web-audit/bin/refs status")
    folder = REFS / source / current[source]
    if not folder.exists():
        raise RefsError(f"{source} {current[source]} está fijada pero no está en var/refs; "
                        f"descárgala con web-audit/bin/refs fetch {source}")
    return folder


# --- HTML text ----------------------------------------------------------------

SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "nav", "header", "footer", "aside",
             "form", "button", "select", "iframe"}
BLOCK_TAGS = {"address", "article", "blockquote", "body", "caption", "dd", "details", "div", "dl",
              "dt", "figcaption", "figure", "hr", "main", "ol", "p", "section", "summary", "table",
              "tbody", "tfoot", "thead", "ul"}
HEADINGS = {f"h{n}": n for n in range(1, 7)}


class TextExtractor(HTMLParser):
    """The text of a page as light Markdown: headings with their anchor ({#id}), list items,
    one line per table row and code blocks. Only the content root counts (main, else article,
    else body); navigation, headers, footers, forms and scripts are left out."""

    def __init__(self, root: str, inside: bool):
        super().__init__(convert_charrefs=True)
        self.root, self.inside = root, int(inside)
        self.skipping = []      # open skipped elements
        self.lines, self.inline = [], []
        self.bullet = ""        # list mark waiting for the first line of its item
        self.lists = 0
        self.heading = None     # [level, anchor] of the open heading
        self.sections = []      # [id, its heading seen] of the open <section> elements
        self.row = None         # cells of the open table row
        self.cell = False       # a cell is open (its end tag may be omitted)
        self.pre = 0

    def flush(self, head: str = "", tail: str = "") -> None:
        text = re.sub(r"[ \t]+", " ", "".join(self.inline)).strip()
        self.inline = []
        if text:
            self.lines.append(self.bullet + head + text + tail)
            self.bullet = ""

    def end_cell(self) -> None:
        if self.cell:
            self.row.append(re.sub(r"\s+", " ", "".join(self.inline)).strip())
            self.inline, self.cell = [], False

    def end_row(self) -> None:
        self.end_cell()
        if any(self.row):
            self.lines.append("| " + " | ".join(self.row) + " |")
        self.row = None

    def handle_starttag(self, tag, attrs):
        if tag == self.root:
            self.inside += 1
        if self.skipping or tag in SKIP_TAGS:
            if tag in SKIP_TAGS:
                self.skipping.append(tag)
            return
        if not self.inside:
            return
        attrs = dict(attrs)
        if tag == "section":
            self.sections.append([attrs.get("id"), False])
        if self.heading and not self.heading[1] and tag == "a":
            self.heading[1] = attrs.get("id") or attrs.get("name")
        if self.row is not None:
            if tag in ("td", "th"):
                self.end_cell()
                self.cell = True
            elif tag == "tr":
                self.end_row()
                self.row = []
            elif tag in BLOCK_TAGS or tag in HEADINGS or tag in ("br", "li", "pre"):
                self.inline.append(" ")
            return
        if tag == "tr":
            self.flush()
            self.row = []
        elif tag in HEADINGS:
            # The anchor a citation names: that of the section the heading opens (W3C), else its
            # own id, else that of an <a id|name> inside it (Google Help)
            self.flush()
            section = self.sections[-1] if self.sections else [None, True]
            self.heading = [HEADINGS[tag], section[0] if not section[1] else attrs.get("id")]
            self.heading[1] = self.heading[1] or attrs.get("id")
            section[1] = True
        elif tag == "li":
            self.flush()
            self.bullet = "  " * max(self.lists - 1, 0) + "- "
        elif tag == "pre":
            self.flush()
            self.pre += 1
        elif tag == "br":
            self.inline.append("\n" if self.pre else " ")
            if not self.pre:
                self.flush()
        elif tag in BLOCK_TAGS:
            self.flush()
            if tag in ("ul", "ol"):
                self.lists += 1

    def handle_endtag(self, tag):
        if tag == self.root and self.inside:
            self.inside -= 1
        if self.skipping:
            if tag in self.skipping:
                while self.skipping.pop() != tag:
                    pass
            return
        if not self.inside and tag != self.root:
            return
        if tag == "section" and self.sections:
            self.sections.pop()
        if self.row is not None:
            if tag in ("td", "th"):
                self.end_cell()
            elif tag in ("tr", "table"):
                self.end_row()
            return
        if tag in HEADINGS and self.heading:
            level, anchor = self.heading
            self.lines.append("")
            self.flush("#" * level + " ", f" {{#{anchor}}}" if anchor else "")
            self.lines.append("")
            self.heading = None
        elif tag == "pre" and self.pre:
            self.pre -= 1
            code = "".join(self.inline).strip("\n")
            self.inline = []
            if code.strip():
                self.lines += ["", "```", code, "```", ""]
        elif tag in BLOCK_TAGS or tag == "li":
            self.flush()
            if tag in ("ul", "ol") and self.lists:
                self.lists -= 1
            if tag == "p":
                self.lines.append("")

    def handle_data(self, data):
        if self.skipping or not self.inside:
            return
        self.inline.append(data if self.pre else re.sub(r"\s+", " ", data))

    def text(self) -> str:
        self.flush()
        out = "\n".join(self.lines)
        return re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"


def charset(html: bytes, content_type: str) -> str:
    match = re.search(r"charset=([\w-]+)", content_type or "") \
        or re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", html[:4096], re.I)
    name = match.group(1) if match else "utf-8"
    name = name.decode("ascii") if isinstance(name, bytes) else name
    try:
        return codecs.lookup(name).name
    except LookupError:
        return "utf-8"


def page_text(html: str) -> str:
    """Text of an HTML page (see TextExtractor)."""
    root = next((t for t in ("main", "article") if re.search(rf"<{t}[\s>]", html, re.I)), "body")
    parser = TextExtractor(root, inside=not re.search(rf"<{root}[\s>]", html, re.I))
    parser.feed(html)
    parser.close()
    return parser.text()


def published(html: str):
    for pattern, label in PUBLISHED:
        match = pattern.search(html)
        if match:
            return label.format(*match.groups())
    return None


# --- Documents ----------------------------------------------------------------

def document_files(url: str) -> tuple:
    """Download a document: ([(path, data, entry)], origin). An HTML page is kept as published
    (page.html, which counts by its text) plus its text (text.md)."""
    data, headers, final = download(url)
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


def check_document(sid: str, source: dict) -> str:
    latest = latest_manifest(sid)
    if not latest:
        return "sin descargar"
    files, _ = document_files(source["url"])
    if fingerprint(latest["files"]) == fingerprint([e for _, _, e in files]):
        return f"al día ({latest['version']})"
    return f"cambió desde {latest['version']}: refs fetch {sid}"


def fetch_document(sid: str, source: dict, args) -> None:
    files, origin = document_files(source["url"])
    store(sid, today(), origin, files)


def content_file(folder: Path):
    """The file a document diff reads: its text, or its only file."""
    names = [f["path"] for f in json.loads((folder / "MANIFEST.json").read_text(encoding="utf-8"))["files"]]
    return folder / ("text.md" if "text.md" in names else names[0])


def diff_document(sid: str, old: str, new: str, limit: int) -> None:
    before, after = content_file(REFS / sid / old), content_file(REFS / sid / new)
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


# --- Schema.org vocabulary ----------------------------------------------------

def schemaorg_release(version: str = None) -> dict:
    return get_json(f"{SCHEMAORG_API}/releases/" + (f"tags/v{version}" if version else "latest"))


def check_schemaorg(sid: str, source: dict) -> str:
    version = schemaorg_release()["tag_name"].removeprefix("v")
    return f"al día ({version})" if version in versions(sid) else f"nueva versión publicada: {version}"


def fetch_schemaorg(sid: str, source: dict, args) -> None:
    release = schemaorg_release(args.version)
    tag = release["tag_name"]
    version = tag.removeprefix("v")
    if version in versions(sid):
        print(f"{sid}: {version} ya descargada")
        return
    folder = f"data/releases/{version}"
    listing = {f["name"]: f for f in get_json(f"{SCHEMAORG_API}/contents/{folder}?ref={tag}")}
    files = []
    for name in SCHEMAORG_FILES:
        if name not in listing:
            raise RefsError(f"{sid}: la release {version} no tiene {folder}/{name}")
        meta = listing[name]
        data = download(meta["download_url"])[0]
        if len(data) != meta["size"] or git_sha(data) != meta["sha"]:
            raise RefsError(f"{sid}: {name} no coincide con el tamaño o el sha de GitHub")
        files.append((name, data, entry(name, data, meta["download_url"], git_sha=meta["sha"])))
    store(sid, version, {
        "repository": "schemaorg/schemaorg",
        "release": release["html_url"],
        "published_at": release["published_at"],
        "folder": folder,
    }, files)


def literal(value) -> str:
    if isinstance(value, list):
        return " ".join(literal(v) for v in value)
    return value.get("@value", "") if isinstance(value, dict) else str(value)


def ids(value) -> list:
    values = value if isinstance(value, list) else [value] if value else []
    return [v["@id"] if isinstance(v, dict) else v for v in values]


RELATIONS = (("rdfs:subClassOf", "superclase"), ("schema:domainIncludes", "dominio"),
             ("schema:rangeIncludes", "rango"), ("schema:isPartOf", "sección"),
             ("schema:supersededBy", "sustituido por"))


def terms(folder: Path) -> list:
    """Types, properties and enumeration members: id → (definition, relations)."""
    graph = json.loads((folder / VOCABULARY).read_text(encoding="utf-8"))["@graph"]
    groups = {"tipos": {}, "propiedades": {}, "valores de enumeración": {}}
    for node in graph:
        types = ids(node.get("@type"))
        relations = {f"{label}:{i}" for key, label in RELATIONS for i in ids(node.get(key))}
        if "rdfs:Class" in types:
            group = "tipos"
        elif "rdf:Property" in types:
            group = "propiedades"
        else:
            group = "valores de enumeración"
            relations |= {f"de:{t}" for t in types}
        groups[group][node["@id"]] = (literal(node.get("rdfs:comment", "")), frozenset(relations))
    return list(groups.items())


def diff_schemaorg(sid: str, old: str, new: str, limit: int) -> None:
    for (title, before), (_, after) in zip(terms(REFS / sid / old), terms(REFS / sid / new)):
        common = before.keys() & after.keys()
        added = sorted(after.keys() - before.keys())
        removed = sorted(before.keys() - after.keys())
        changed = sorted(k for k in common if before[k][0] != after[k][0])
        related = sorted(k for k in common if before[k][1] != after[k][1])
        print(f"{title}: {len(before)} → {len(after)} · +{len(added)} −{len(removed)} · "
              f"definición cambiada {len(changed)} · relaciones cambiadas {len(related)}")
        show("añadidos", [f"{k}  {after[k][0][:90]}" for k in added], limit)
        show("eliminados", [f"{k}  {before[k][0][:90]}" for k in removed], limit)
        show("definición cambiada", changed, limit)
        show("relaciones cambiadas", [
            f"{k}  " + " ".join([f"+{r}" for r in sorted(after[k][1] - before[k][1])]
                                + [f"−{r}" for r in sorted(before[k][1] - after[k][1])])
            for k in related], limit)


# --- Commands -----------------------------------------------------------------

KIND_OPS = {
    "schemaorg": (check_schemaorg, fetch_schemaorg, diff_schemaorg),
    "document": (check_document, fetch_document, diff_document),
}


def selected(registry: dict, names: list) -> list:
    unknown = [n for n in names if n not in registry]
    if unknown:
        fail(f"fuente desconocida: {', '.join(unknown)} (ver {SOURCES_FILE.name} o refs status)")
    return names or list(registry)


def show(label: str, lines: list, limit: int) -> None:
    if not lines:
        return
    print(f"  {label} ({len(lines)}):")
    for line in lines[:limit]:
        print(f"    {line}")
    if len(lines) > limit:
        print(f"    … +{len(lines) - limit} más (--all)")


def cmd_status(args) -> None:
    current = pins()
    registry = sources()
    width = max(map(len, registry))
    for sid in registry:
        found = versions(sid)
        if not found:
            print(f"{sid:<{width}}  sin descargar")
            continue
        pin = current.get(sid, "—")
        latest = manifest(sid, found[-1])
        newer = " · hay una versión posterior a la fijada" if found[-1] != pin else ""
        print(f"{sid:<{width}}  fijada {pin} · última {found[-1]} ({latest['fetched_at'][:10]}) · "
              f"{len(found)} versión(es){newer}")


def cmd_check(args) -> None:
    registry = sources()
    names = selected(registry, args.sources)
    width = max(map(len, names))
    for sid in names:
        source = registry[sid]
        try:
            print(f"{sid:<{width}}  {KIND_OPS[source['kind']][0](sid, source)}", flush=True)
        except (urllib.error.URLError, RefsError) as e:
            print(f"{sid:<{width}}  no se pudo comprobar: {e}")
        if source["kind"] == "document":
            time.sleep(DOCUMENT_INTERVAL)


def cmd_fetch(args) -> None:
    registry = sources()
    names = selected(registry, args.sources)
    if args.version and any(registry[n]["kind"] != "schemaorg" for n in names):
        fail("--version solo se aplica a las fuentes de tipo schemaorg: refs fetch schemaorg --version 30.1")
    failed = []
    for sid in names:
        source = registry[sid]
        try:
            KIND_OPS[source["kind"]][1](sid, source, args)
        except (urllib.error.URLError, RefsError) as e:
            print(f"{sid}: no se pudo descargar: {e}", file=sys.stderr)
            failed.append(sid)
        if source["kind"] == "document" and sid != names[-1]:
            time.sleep(DOCUMENT_INTERVAL)
    if failed:
        fail(f"sin descargar: {', '.join(failed)}")


def cmd_diff(args) -> None:
    registry = sources()
    selected(registry, [args.source])
    found = versions(args.source)
    old = args.old or pins().get(args.source)
    new = args.new or (found[-1] if found else None)
    for version in (old, new):
        if version not in found:
            fail(f"{args.source}: no existe la versión {version} (hay: {', '.join(found) or 'ninguna'})")
    if old == new:
        print(f"{args.source}: {old} es a la vez la fijada y la última; nada que comparar")
        return
    print(f"{args.source}: {old} → {new}")
    KIND_OPS[registry[args.source]["kind"]][2](args.source, old, new, sys.maxsize if args.all else DIFF_LIMIT)


def cmd_pin(args) -> None:
    selected(sources(), [args.source])
    if args.version not in versions(args.source):
        fail(f"{args.source}: no existe la versión {args.version}")
    current = pins()
    previous = current.get(args.source)
    current[args.source] = args.version
    save_pins(current)
    print(f"{args.source}: fijada {args.version}" + (f" (antes {previous})" if previous else ""))
    if previous and previous != args.version:
        print(f"Revisa las fichas y los requisitos técnicos que citan {args.source} {previous}: "
              f"web-audit/bin/refs diff {args.source} {previous} {args.version}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="refs", description="Fuentes de la referencia técnica (var/refs/).")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("status", help="versiones por fuente y la fijada").set_defaults(func=cmd_status)
    p = sub.add_parser("check", help="¿ha cambiado la fuente en origen? (no guarda nada)")
    p.add_argument("sources", nargs="*", metavar="SOURCE")
    p.set_defaults(func=cmd_check)
    p = sub.add_parser("fetch", help="descargar una versión nueva")
    p.add_argument("sources", nargs="*", metavar="SOURCE")
    p.add_argument("--version", help="release de Schema.org (por defecto, la última)")
    p.set_defaults(func=cmd_fetch)
    p = sub.add_parser("diff", help="cambios entre dos versiones")
    p.add_argument("source")
    p.add_argument("old", nargs="?")
    p.add_argument("new", nargs="?")
    p.add_argument("--all", action="store_true", help="sin límite de líneas")
    p.set_defaults(func=cmd_diff)
    p = sub.add_parser("pin", help="fijar la versión que cita la referencia")
    p.add_argument("source")
    p.add_argument("version")
    p.set_defaults(func=cmd_pin)
    args = parser.parse_args()
    (getattr(args, "func", None) or cmd_status)(args)


if __name__ == "__main__":
    main()
