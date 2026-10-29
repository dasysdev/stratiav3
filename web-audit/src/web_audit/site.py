"""The pages of an audit as capture froze them (capture.audit, D-167), read for the technical audit.

An audit is capture/var/audits/<audit>/: its manifest (audit.json), the snapshot of each page
(meta.json, the response document and its original bytes), robots.txt of each origin (sites/),
the sitemaps as they came (sitemaps/) and the responses to the images of the markup, without
their bodies, with robots.txt of each host the audit did not hold (resources.json, resources/). This module reads them without Chrome and derives what the
checks need: the document tree, the markup of each syntax as one graph, robots.txt and the URLs of
the sitemaps in any of their formats (XML, RSS or Atom, text). The interpretation is web-audit's.

Under the profile (D-156) the document examined is the HTTP response, without JavaScript: capture
with audit-es keeps no rendered DOM (its dom.html is the DOM of the first load without scripts).
"""
from __future__ import annotations

import functools
import gzip
import io
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urldefrag, urlsplit

from capture import audit as capture_audit
from capture.robots import Robots

from . import html, jsonld, microdata, rdfa
from .graph import Entity, Graph

# Page types of capture.audit and of the canon (D-161)
PAGE_TYPES = {"product": "ficha de producto", "category": "categoría o listado",
              "policy": "políticas y contenido", "home": "portada"}
LD_JSON = "application/ld+json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


@dataclass
class Page:
    id: str
    type: str                    # product, home, policy, category
    url: str
    outcome: str
    folder: Path | None = None
    meta: dict | None = None
    record: dict = field(default_factory=dict)

    @property
    def page_type(self) -> str:
        return PAGE_TYPES[self.type]

    @property
    def captured(self) -> bool:
        return self.outcome == "captured" and self.folder is not None

    @property
    def http(self) -> dict:
        return (self.meta or {}).get("http") or {}

    @property
    def status(self) -> int | None:
        return self.http.get("status")

    @property
    def headers(self) -> dict:
        return {k.lower(): v for k, v in (self.http.get("headers") or {}).items()}

    @property
    def url_final(self) -> str:
        return (self.meta or {}).get("url_final") or self.record.get("url_final") or self.url

    @functools.cached_property
    def raw(self) -> bytes | None:
        """The original bytes of the body (response.html.gz), BOM included."""
        if self.folder is None or not (self.folder / "response.html.gz").exists():
            return None
        return gzip.decompress((self.folder / "response.html.gz").read_bytes())

    @property
    def original_bytes(self) -> bool:
        return (self.meta or {}).get("response_body") == "original"

    @functools.cached_property
    def text(self) -> str | None:
        """The response document in UTF-8, decoded as the browser did."""
        if self.raw is None:
            return None
        return capture_audit._response_text(self.folder, self.meta).decode("utf-8")

    @functools.cached_property
    def doc(self) -> html.Document | None:
        return html.parse(self.text) if self.text is not None else None

    @property
    def mime(self) -> str:
        ctype = self.headers.get("content-type")
        if ctype:
            return ctype.split(";")[0].strip().lower()
        return (self.http.get("mime") or "").lower()

    @property
    def is_html(self) -> bool:
        return self.mime in ("text/html", "application/xhtml+xml") or (
            not self.headers.get("content-type") and self.http.get("mime") == "text/html")

    # --- markup
    @functools.cached_property
    def blocks(self) -> list[jsonld.Block]:
        if self.doc is None:
            return []
        out = []
        for el in self.doc.all("script"):
            if (el.get("type") or "").strip().lower() == LD_JSON:
                text = el.text()
                data, error = jsonld.parse(text)
                out.append(jsonld.Block(len(out) + 1, el.line, text, data, error))
        return out

    @functools.cached_property
    def jsonld(self) -> jsonld.Report:
        return jsonld.analyze(self.blocks)

    @functools.cached_property
    def items(self) -> list:
        return microdata.items(self.doc) if self.doc is not None else []

    def nodes(self) -> list[Entity]:
        """The nodes of the markup, freshly extracted (linking a graph changes them)."""
        if self.doc is None:
            return []
        return (jsonld.entities(self.blocks, self.url_final, self.id)
                + microdata.entities(self.doc, self.url_final, self.id)
                + rdfa.entities(self.doc, self.url_final, self.id))

    @functools.cached_property
    def graph(self) -> Graph:
        return Graph.link(self.nodes())

    @functools.cached_property
    def syntaxes(self) -> dict:
        """Markup with Schema.org in the document: JSON-LD blocks, Microdata items, RDFa."""
        if self.doc is None:
            return {}
        out = {}
        if any(b.text.strip() for b in self.blocks):
            out["json-ld"] = [f"bloque {b.index} (línea {b.line})" for b in self.blocks if b.text.strip()]
        md = [el for el in self.doc.all() if el.has("itemscope") and el.has("itemtype")]
        if md:
            out["microdata"] = [el.where() for el in md[:10]] + ([f"… {len(md)} en total"] if len(md) > 10 else [])
        if rdfa.schema_org(self.doc):
            out["rdfa"] = ["typeof o property de Schema.org"]
        return out


SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
UNESCAPED = re.compile(rb"&(?!(#\d+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);)|<(?![A-Za-z_/!?])")
CDATA_OR_COMMENT = re.compile(rb"<!\[CDATA\[.*?\]\]>|<!--.*?-->", re.S)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


@dataclass
class Sitemap:
    """A sitemap as capture kept it. It is read once, streaming, into `summary`: neither its body
    nor its XML tree is kept (a site may publish hundreds of MB of sitemaps)."""
    url: str
    status: int | None
    data: bytes | None = None
    error: str | None = None
    gzip: bool = False

    @property
    def obtained(self) -> bool:
        return self.data is not None

    @property
    def missing(self) -> bool:
        """It does not exist: a 4xx other than 429, without body kept."""
        return self.data is None and self.error is None and self.status is not None and 400 <= self.status < 500

    def _body(self) -> bytes | None:
        if self.data is not None and self.data[:2] == b"\x1f\x8b":
            try:
                return gzip.decompress(self.data)
            except (OSError, EOFError):
                return None
        return self.data

    @functools.cached_property
    def summary(self) -> dict:
        """format (xml, feed, text), root (its tag with namespace), parse_error, entries
        [(position, tag, [loc…])], size (bytes uncompressed), utf8_error (byte offset),
        declared_encoding, unescaped (positions of & or < unescaped) and urls (pages listed)."""
        body = self._body()
        out = {"format": "unknown", "root": None, "parse_error": None, "entries": [], "size": 0,
               "utf8_error": None, "declared_encoding": None, "unescaped": [], "urls": []}
        if body is None:
            out["parse_error"] = "no se puede descomprimir"
            return out
        out["size"] = len(body)
        try:
            body.decode("utf-8", errors="strict")
        except UnicodeDecodeError as e:
            out["utf8_error"] = e.start
        m = re.match(rb"\s*<\?xml[^>]*encoding=[\"']([^\"']+)", body)
        out["declared_encoding"] = m.group(1).decode("ascii", "replace") if m else None
        if not body.lstrip().startswith(b"<"):
            out["format"] = "text"
            text = body.decode("utf-8", errors="replace")
            out["urls"] = [line.strip() for line in text.splitlines() if line.strip()]
            return out
        out["unescaped"] = [m.start() for m in UNESCAPED.finditer(CDATA_OR_COMMENT.sub(b"", body))][:20]
        depth, entry, links = 0, None, []
        try:
            for event, el in ET.iterparse(io.BytesIO(body), events=("start", "end")):
                if event == "start":
                    depth += 1
                    if depth == 1:
                        out["root"] = el.tag
                    elif depth == 2 and _local(el.tag) in ("url", "sitemap"):
                        entry = (len(out["entries"]), _local(el.tag), [])
                    continue
                if depth == 3 and entry is not None and _local(el.tag) == "loc":
                    entry[2].append((el.text or "").strip())
                if _local(el.tag) == "link":
                    links.append(el.get("href") or (el.text or "").strip())
                if depth == 2:
                    if entry is not None:
                        out["entries"].append(entry)
                        entry = None
                    el.clear()
                depth -= 1
        except ET.ParseError as e:
            out["parse_error"] = str(e)
        root = _local(out["root"] or "")
        out["format"] = "feed" if root in ("rss", "feed") else "xml"
        if root == "urlset":
            out["urls"] = [loc for _, tag, locs in out["entries"] if tag == "url" for loc in locs if loc]
        elif root in ("rss", "feed"):
            out["urls"] = [u for u in links if u]
        return out

    @property
    def format(self) -> str:
        return self.summary["format"]

    @property
    def index(self) -> bool:
        return _local(self.summary["root"] or "") == "sitemapindex"

    def urls(self) -> list[str]:
        """The pages it lists, in any format (an index lists sitemaps, not pages)."""
        return self.summary["urls"]


class Site:
    """An audit of capture: its pages, robots.txt and sitemaps."""

    def __init__(self, audit_id: str, folder: Path | None = None) -> None:
        self.id = audit_id
        self.folder = folder or capture_audit.AUDITS / audit_id
        self.manifest = read_json(self.folder / "audit.json")
        if self.manifest is None:
            raise capture_audit.AuditError(f"no hay auditoría {audit_id} en {self.folder}")
        self.url = self.manifest["site"]
        self._robots: dict[str, tuple] = {}
        self.memo: dict = {}  # what the checks derive once per site
        self.pages = []
        for rec in self.manifest.get("pages", []):
            folder = self.folder / rec["snapshot"] if rec.get("snapshot") else None
            meta = read_json(folder / "meta.json") if folder else None
            self.pages.append(Page(rec["id"], rec["type"], rec["url"], rec.get("outcome", "pending"), folder, meta, rec))

    def page(self, page_id: str) -> Page:
        return next(p for p in self.pages if p.id == page_id)

    # --- resources (capture.resources, T-086)
    @functools.cached_property
    def resources_manifest(self) -> dict:
        return read_json(self.folder / "resources.json") or {}

    @functools.cached_property
    def resources(self) -> dict[str, dict]:
        """The record of each resource URL capture asked for (by URL without fragment)."""
        return {r["url"]: r for r in self.resources_manifest.get("resources", [])}

    def resource(self, url: str) -> dict | None:
        return self.resources.get(urldefrag(url)[0])

    # --- robots.txt
    def robots(self, url: str) -> tuple[int | None, str | None, str]:
        """(status, text, origin) of the robots.txt of the origin of `url`: the status as capture
        recorded it (the manifest for the site, the snapshot of a page), the text kept in sites/."""
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        if origin not in self._robots:
            self._robots[origin] = self._read_robots(parts, origin)
        return self._robots[origin]

    def _read_robots(self, parts, origin: str) -> tuple:
        path = self.folder / "sites" / parts.netloc.replace(":", "_") / "robots.txt"
        text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else None
        kept = ((self.resources_manifest.get("hosts") or {}).get(parts.netloc) or {}).get("robots")
        if text is None and kept and kept.get("source") == "resources":  # a host only the resources reached (a CDN)
            file = self.folder / kept["file"] if kept.get("file") else None
            text = file.read_text(encoding="utf-8", errors="replace") if file and file.exists() else None
            return kept.get("status"), text, origin
        status = None
        if origin == self.url.rstrip("/"):
            status = ((self.manifest.get("legitimacy") or {}).get("robots") or {}).get("status")
        if status is None:
            for page in self.pages:
                if page.meta and urlsplit(page.url).netloc == parts.netloc:
                    status = (((page.meta.get("legitimacy") or {}).get("robots")) or {}).get("status")
                    if status is not None:
                        break
        return status, text, origin

    def declared_sitemaps(self, url: str) -> frozenset:
        """The sitemaps that the robots.txt of the origin of `url` declares (when it answers 2xx)."""
        status, text, origin = self.robots(url)
        key = ("declared", origin)
        if key not in self.memo:
            ok = text is not None and status is not None and 200 <= status < 300
            self.memo[key] = frozenset(
                line.split(":", 1)[1].strip() for line in (text or "").splitlines()
                if ok and line.split("#", 1)[0].strip().lower().startswith("sitemap:"))
        return self.memo[key]

    def robots_rules(self, url: str) -> Robots | None:
        status, text, _ = self.robots(url)
        if status is None and text is None:
            return None
        return Robots(text if status is not None and 200 <= status < 300 else "", status)

    # --- sitemaps
    @functools.cached_property
    def sitemaps(self) -> list[Sitemap]:
        out = []
        for entry in (self.manifest.get("sitemaps") or {}).get("read", []):
            data = None
            if entry.get("file"):
                path = self.folder / entry["file"]
                data = path.read_bytes() if path.exists() else None
            error = entry.get("error")
            if error and error.startswith("no se puede leer") and data is not None:
                error = None  # kept: web-audit reads it in its format
            out.append(Sitemap(entry["url"], entry.get("status"), data, error, bool(entry.get("gzip"))))
        return out

    @property
    def sitemaps_pending(self) -> list[str]:
        return list((self.manifest.get("sitemaps") or {}).get("pending", []))

    @property
    def sitemaps_complete(self) -> bool:
        """Every sitemap was obtained (or does not exist) and none is left unread."""
        return not self.sitemaps_pending and all(s.obtained or s.missing for s in self.sitemaps)

    @functools.cached_property
    def graph(self) -> Graph:
        """The entities of all the pages, one per identifier across pages (general view)."""
        nodes: list[Entity] = []
        for page in self.pages:
            if page.captured and page.doc is not None:
                nodes += page.nodes()
        return Graph.link(nodes)


def clean(url: str) -> str:
    return urldefrag(url)[0]


WWW = re.compile(r"^www\.", re.I)


def same_host(a: str, b: str) -> bool:
    ha, hb = urlsplit(a).hostname or "", urlsplit(b).hostname or ""
    return bool(ha) and WWW.sub("", ha.lower()) == WWW.sub("", hb.lower())
