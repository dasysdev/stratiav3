"""The pages of an audit of a site (D-167), chosen on its crawl (capture.spider, D-170).

One audit is one directory, var/audits/<audit>/, never replaced. The crawl captures every page
under the audit profile (audit-es) and writes crawl.json, with the universe of the audit. The
audit only chooses among what the crawl captured, with the snapshot of the crawl's visit, and
asks for nothing (D-170):

  audit.json          the manifest: every page chosen with its type (product, home, policy,
                      category), what was located and what was not, and whether each product
                      page is in the sitemaps

The pages: the product pages of the engagement (the list given) or, with no list, every product
page of the universe; the home page; the shipping, returns, contact and legal notice pages,
located from the links of the home page (its footer first); and the categories: every category
of the universe and the immediate category of each product page, by its breadcrumbs (D-215). A
policy that is not located, a page the crawl did not capture or a product page without
breadcrumbs is recorded as such and never replaced by another page. A product page of the list
that is not in the universe is not audited: it is recorded, as not reached only if the crawl was
complete. A crawl stopped by a TDM reservation (D-171) is not audited.

This module also holds what the crawl shares: the links and breadcrumbs of a document, the
policies of a home page, robots.txt and tdmrep.json of each origin and the reading of the
sitemaps (those declared in robots.txt or, if none, /sitemap.xml, up to a budget).
Reading an audit and the links of its pages needs neither Chrome nor websockets (on the host).
"""
from __future__ import annotations

import base64
import gzip
import json
import random
import re
import unicodedata
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlsplit

from . import ROOT, tdm
from .files import now, read_json, sha256, write_json
from .pages import ID, PageError, _response_text, json_ld, walk

AUDITS = ROOT / "var/audits"
PAUSE_S = (3, 8)
SITEMAP_FILES = 50
SITEMAP_MB = 200

# Link text or address (accents removed, lowercase) of each policy page of D-167
POLICIES = {
    "shipping": r"\b(envios?|gastos de envio|entregas?|shipping|delivery)\b",
    "returns": r"\b(devolucion|devoluciones|desistimiento|returns?|refunds?)\b",
    "contact": r"\b(contacto|contacta|contactar|contactanos|contact|atencion al cliente)\b",
    "legal": r"\b(aviso legal|legal notice|informacion legal)\b",
}

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

FETCH_BYTES = """(async url => {
  try {
    const r = await fetch(url, {credentials: 'omit'});
    const buf = new Uint8Array(await r.arrayBuffer());
    let s = '';
    for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
    return {status: r.status, url: r.url, type: r.headers.get('content-type'), body: btoa(s)};
  } catch (e) { return {status: null, error: String(e)}; }
})(%s)"""


class AuditError(LookupError):
    pass


# ------------------------------------------------------------------ reading an audit
def manifest(audit_id: str) -> dict:
    """The manifest of an audit (audit.json) or, until its pages are chosen, of its crawl."""
    data = read_json(AUDITS / audit_id / "audit.json") or read_json(AUDITS / audit_id / "crawl.json")
    if data is None:
        raise AuditError(f"no hay auditoría {audit_id}")
    return data


def read(audit_id: str, page_id: str) -> str:
    """The document of a captured page of an audit or of its crawl (the HTTP response, in UTF-8)."""
    folder = AUDITS / audit_id
    data = read_json(folder / "crawl.json") or manifest(audit_id)
    page = next((p for p in data["pages"] if p["id"] == page_id), None)
    if page is None or page.get("outcome") != "captured":
        raise AuditError(f"{audit_id}: no hay página capturada {page_id}")
    folder = AUDITS / audit_id / page["snapshot"]
    return _response_text(folder, read_json(folder / "meta.json")).decode("utf-8")


# ------------------------------------------------------------------ links and breadcrumbs
def _plain(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", re.sub(r"[-_/.]+", " ", text.lower())).strip()


def _clean(url: str) -> str:
    return urldefrag(url)[0]


class _Links(HTMLParser):
    """The links of a document, each with its text, whether it is in the footer, the
    breadcrumb trail it belongs to (if any) and whether it is nofollow. The first <base href>
    sets the base of relative links."""

    def __init__(self, base: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base = base
        self.stack: list[tuple[str, bool, int | None]] = []   # (tag, footer, trail)
        self.links: list[dict] = []
        self.trails = 0
        self._open: dict | None = None
        self._based = False

    def _state(self) -> tuple[bool, int | None]:
        return self.stack[-1][1:] if self.stack else (False, None)

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
        if tag == "base" and a.get("href", "").strip() and not self._based:
            self.base, self._based = urljoin(self.base, a["href"].strip()), True
        footer, trail = self._state()
        footer = footer or tag == "footer" or a.get("role") == "contentinfo"
        marks = " ".join((a.get("class", ""), a.get("id", ""), a.get("aria-label", ""))).lower()
        if trail is None and ("breadcrumb" in marks or "migas" in marks
                              or "breadcrumblist" in a.get("itemtype", "").lower()):
            self.trails += 1
            trail = self.trails
        if tag == "a" and self._open:
            self._close()
        if tag == "a" and a.get("href"):
            self._open = {"href": a["href"], "text": " ".join(filter(None, (a.get("title"), a.get("aria-label")))),
                          "footer": footer, "trail": trail, "nofollow": "nofollow" in a.get("rel", "").lower().split()}
        if tag not in VOID:
            self.stack.append((tag, footer, trail))

    def handle_endtag(self, tag):
        if tag == "a" and self._open:
            self._close()
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self._open is not None:
            self._open["text"] += " " + data

    def _close(self):
        link, self._open = self._open, None
        href = link["href"].strip()
        if href.startswith(("#", "mailto:", "tel:", "javascript:")):
            return
        link["url"] = _clean(urljoin(self.base, href))
        link["text"] = re.sub(r"\s+", " ", link["text"]).strip()
        self.links.append(link)


def links(doc: str, base: str) -> list[dict]:
    parser = _Links(base)
    parser.feed(doc)
    parser.close()
    if parser._open:
        parser._close()
    return parser.links


def _same_site(url: str, base: str) -> bool:
    host, own = urlsplit(url).hostname or "", urlsplit(base).hostname or ""
    domain = ".".join(own.split(".")[-2:]) if not re.fullmatch(r"[\d.]+", own) else own
    return host == own or host.endswith("." + domain)


def locate_policies(doc: str, base: str) -> dict:
    """For each policy of D-167, the link of the home page that names it, its footer first and
    its text before its address; {'status': 'not_located'} if none does."""
    found = [l for l in links(doc, base) if _same_site(l["url"], base) and urlsplit(l["url"]).scheme.startswith("http")]
    out = {}
    for kind, pattern in POLICIES.items():
        candidates = []
        for l in found:
            by_text = bool(re.search(pattern, _plain(l["text"])))
            by_url = bool(re.search(pattern, _plain(urlsplit(l["url"]).path)))
            if by_text or by_url:
                candidates.append({"url": l["url"], "text": l["text"][:120], "footer": l["footer"],
                                   "by": "text" if by_text else "url", "_rank": (l["footer"], by_text, by_url)})
        candidates.sort(key=lambda c: c.pop("_rank"), reverse=True)   # stable: document order within a rank
        unique = list({c["url"]: c for c in reversed(candidates)}.values())[::-1]
        if unique:
            out[kind] = {"status": "located", **unique[0], "candidates": unique[1:10]}
        else:
            out[kind] = {"status": "not_located"}
    return out


def breadcrumbs(doc: str, url: str, url_final: str | None) -> dict:
    """The breadcrumb trail of a product page (its markup first, then JSON-LD) and its
    immediate category: the last link of the trail that is neither the page nor the root."""
    own = {_clean(url), _clean(url_final or url)}
    trails: dict[int, list] = {}
    for l in links(doc, url_final or url):
        if l["trail"] is not None:
            trails.setdefault(l["trail"], []).append({"name": l["text"], "url": l["url"]})
    source, trail = None, next((t for t in trails.values() if t), None)
    if trail:
        source = "html"
    else:
        for block in json_ld(doc):
            for node in walk(block):
                types = node.get("@type")
                if "BreadcrumbList" in (types if isinstance(types, list) else [types]):
                    items = sorted((i for i in node.get("itemListElement") or [] if isinstance(i, dict)),
                                   key=lambda i: float(i.get("position") or 0))
                    trail = []
                    for i in items:
                        item = i.get("item")
                        item = item if isinstance(item, (str, dict)) else None
                        target = item.get("@id") or item.get("url") if isinstance(item, dict) else item
                        name = i.get("name") or (item.get("name") if isinstance(item, dict) else None)
                        trail.append({"name": name, "url": _clean(urljoin(url, target)) if target else None})
                    source = "json-ld"
                    break
            if source:
                break
    if not trail:
        return {"status": "none"}
    category = next((c["url"] for c in reversed(trail)
                     if c["url"] and c["url"] not in own and urlsplit(c["url"]).path not in ("", "/")), None)
    return {"status": "found" if category else "no_category", "source": source, "trail": trail,
            "category": category}


# ------------------------------------------------------------------ sitemaps
def _parse_sitemap(data: bytes) -> dict:
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    root = ET.fromstring(data)
    local = lambda el: el.tag.rsplit("}", 1)[-1]  # noqa: E731
    locs = lambda tag: [(el.text or "").strip() for child in root if local(child) == tag  # noqa: E731
                        for el in child if local(el) == "loc" and (el.text or "").strip()]
    if local(root) == "sitemapindex":
        return {"kind": "index", "sitemaps": locs("sitemap")}
    if local(root) == "urlset":
        return {"kind": "urlset", "urls": locs("url")}
    raise ValueError(f"raíz desconocida: {local(root)}")


class _Sites:
    """robots.txt and tdmrep.json of each origin, read once and kept in sites/<host>/."""

    def __init__(self, folder: Path) -> None:
        self.folder = folder
        self.known: dict[str, tuple] = {}

    def of(self, page, url: str):
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        if origin not in self.known:
            folder = self.folder / parts.netloc.replace(":", "_")
            folder.mkdir(parents=True, exist_ok=True)
            from .legitimacy import access
            self.known[origin] = access(page, origin, folder)
        return self.known[origin]


def read_sitemaps(page, sites: _Sites, base: str, folder: Path, files: int, max_bytes: int,
                  pause_s=PAUSE_S, root: Path | None = None) -> dict:
    """The sitemaps of the site, kept as they came in `folder`; each file named relative to
    `root` (the audit; by default the parent of `folder`)."""
    from .legitimacy import robots_of

    robots = sites.of(page, base)[0]
    queue = list(dict.fromkeys(robots.sitemaps)) or [base + "/sitemap.xml"]
    declared = bool(robots.sitemaps)
    folder.mkdir(parents=True, exist_ok=True)
    report, urls, seen, used, at, reserved = [], set(), set(), 0, None, None
    while queue and len(seen) < files and used < max_bytes:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        entry = {"url": url}
        report.append(entry)
        site, entries, _ = sites.of(page, url)
        if tdm.reserving(entries):   # a sitemap on another origin with a reservation stops the audit
            entry["error"] = "reserva TDM (tdmrep.json): no se lee"
            reserved = {"url": url, "entries": tdm.reserving(entries)}
            break
        if not site.allowed(url):
            entry["error"] = "excluido por robots.txt"
            continue
        origin = "{0.scheme}://{0.netloc}".format(urlsplit(url))
        if at != origin:   # fetch from a document of the sitemap's own origin
            robots_of(page, origin)
            at = origin
        got = page.eval(FETCH_BYTES % json.dumps(url), timeout=300, await_promise=True) or {}
        entry["status"] = got.get("status")
        if got.get("error") or not got.get("status"):
            entry["error"] = got.get("error") or "sin respuesta"
            continue
        if got["status"] >= 400:
            if got["status"] == 429 or got["status"] >= 500:
                entry["error"] = f"HTTP {got['status']}"
            continue
        data = base64.b64decode(got["body"])
        used += len(data)
        name = f"{len(report):03d}-" + (re.sub(r"[^A-Za-z0-9._-]+", "_", urlsplit(url).path.rsplit("/", 1)[-1])
                                        or "sitemap")
        (folder / name).write_bytes(data)
        entry.update({"file": str((folder / name).relative_to(root or folder.parent)), "bytes": len(data), "sha256": sha256(data),
                      "content_type": got.get("type"), "gzip": data[:2] == b"\x1f\x8b"})
        try:
            parsed = _parse_sitemap(data)
        except (ValueError, OSError, EOFError, ET.ParseError) as exc:
            entry["error"] = f"no se puede leer: {exc}"
            continue
        entry["kind"] = parsed["kind"]
        if parsed["kind"] == "index":
            entry["sitemaps"] = len(parsed["sitemaps"])
            queue.extend(s for s in parsed["sitemaps"] if s not in seen)
        else:
            entry["urls"] = len(parsed["urls"])
            urls.update(_clean(u) for u in parsed["urls"])
        page.idle(random.uniform(*pause_s))
    complete = not queue and not any("error" in e for e in report)
    return {"declared": declared, "budget": {"files": files, "mb": max_bytes // 1_000_000},
            "read": report, "pending": queue, "complete": complete, "urls": urls, "reserved": reserved}


class _Canonicals(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.found: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
        if tag == "link" and "canonical" in a.get("rel", "").lower().split() and a.get("href", "").strip():
            self.found.append(a["href"].strip())


def canonicals(doc: str, base: str) -> list[str]:
    """The canonical URLs a page declares (link rel=canonical), absolute and in order."""
    parser = _Canonicals()
    parser.feed(doc)
    parser.close()
    return list(dict.fromkeys(_clean(urljoin(base, href)) for href in parser.found))


# ------------------------------------------------------------------ the audit
class Reserved(AuditError):
    """A crawl stopped by a TDM reservation (D-171): nothing of it is audited."""

    def __init__(self, reservation: dict) -> None:
        super().__init__("rastreo parado por una reserva TDM (D-171): no se audita")
        self.reservation = reservation


def check_new(audit_id: str) -> Path:
    if not ID.fullmatch(audit_id):
        raise AuditError(f"ID no válido: {audit_id!r} (minúsculas, dígitos y guiones)")
    folder = AUDITS / audit_id
    if folder.exists():
        raise AuditError(f"la auditoría {audit_id} ya existe y no se sustituye; la nueva lleva otro ID")
    return folder


def run(audit_id: str, products: list[str] | None = None) -> dict:
    """Choose the pages of the audit (D-167) on the crawl of var/audits/<audit>/ (capture.spider)
    and return its manifest, written in audit.json: the product pages given, or every product
    page of the universe; the home page, the policies and the categories. Nothing is asked for:
    a page the crawl did not capture is recorded, not audited."""
    from .spider import MANIFEST, url_key

    folder = AUDITS / audit_id
    crawl = read_json(folder / MANIFEST)
    if crawl is None:
        raise AuditError(f"no hay rastreo {audit_id}: primero, pages crawl {audit_id} URL")
    if (folder / "audit.json").exists():
        raise AuditError(f"la auditoría {audit_id} ya eligió sus páginas y no se sustituye")
    if crawl.get("reservation"):
        raise Reserved(crawl["reservation"])
    hosts = set(crawl["crawl"]["hosts"])
    others = sorted({urlsplit(u).netloc for u in products or []} - hosts)
    if others:
        raise AuditError(f"fichas de otro sitio que el rastreo ({', '.join(hosts)}): {', '.join(others)}")
    entries = {e["id"]: e for e in crawl["pages"]}
    rows = {r["url"]: r for r in crawl.get("universe", [])}
    alias: dict[str, str] = {}   # URL, final URL and canonical URL of a page → the page
    for e in sorted(entries.values(), key=lambda e: (e.get("source") == "sitemaps", e["id"])):
        if e.get("same_as"):
            continue
        for u in [e["url"], e.get("url_final"), *e.get("canonical", [])]:
            if u:
                alias.setdefault(url_key(u), e["id"])

    def document(entry: dict) -> str | None:
        if entry.get("outcome") != "captured" or entry.get("not_html"):
            return None
        snap = folder / entry["snapshot"]
        return _response_text(snap, read_json(snap / "meta.json")).decode("utf-8")

    chosen: dict[str, str] = {}   # page ID → type, in the order of D-167

    def choose(page_id: str, kind: str) -> str:
        chosen.setdefault(page_id, kind)
        return page_id

    home = next((e for e in entries.values() if e["depth"] == 0), None)
    home_doc = document(home) if home else None
    if home:
        choose(home["id"], "home")
    policies = locate_policies(home_doc, home.get("url_final") or home["url"]) if home_doc else \
        {k: {"status": "home_not_captured"} for k in POLICIES}
    for policy in policies.values():
        if policy["status"] == "located":
            page = alias.get(url_key(policy["url"]))
            if page:
                policy["page"] = choose(page, "policy")
            else:
                policy["status"] = "not_captured"

    complete = crawl["crawl"]["coverage"].get("crawl_complete", False)
    if products:
        given = []
        for url in products:
            page = alias.get(url_key(url))
            row = rows.get(url_key(url))
            given.append({"url": url, "page": page} if page else
                         {"url": url, "in_universe": "yes" if row else "no" if complete else "undetermined"})
    else:
        given = [{"url": r["url"], "page": r["page"]} for r in rows.values()
                 if r["type"] == "product" and r["page"] and not r.get("same_as")]
    categories = []
    for product in given:
        if not product.get("page"):
            continue
        entry = entries[product["page"]]
        row = rows.get(url_key(entry["url"]), {})
        product["type_in_universe"] = row.get("type")
        product["canonical"] = entry.get("canonical", [])
        found = row.get("in_sitemaps", "undetermined")
        product["in_sitemaps"] = {"value": found, **({"by": row.get("sitemaps_by", "url")} if found == "yes" else {})}
        doc = document(entry)
        product["breadcrumbs"] = breadcrumbs(doc, entry["url"], entry.get("url_final")) if doc else {"status": "not_captured"}
        choose(entry["id"], "product")
        category = product["breadcrumbs"].get("category")
        if category:
            product["category_page"] = alias.get(url_key(category))
            if product["category_page"]:
                categories.append(product["category_page"])
    categories += [r["page"] for r in rows.values() if r["type"] == "category" and r["page"]
                   and not urlsplit(r["url"]).query and not r.get("same_as")]
    for page in categories:
        choose(page, "category")

    fields = ("outcome", "detail", "snapshot", "url_final", "http_status")
    first = crawl["runs"][0]
    record = {"audit": audit_id, "site": crawl["site"], "profile": crawl["profile"], "started_at": now(),
              "origin": first.get("origin"), "legitimacy": crawl.get("legitimacy"),
              "crawl": {"manifest": MANIFEST, "coverage": crawl["crawl"]["coverage"],
                        "universe": crawl["crawl"].get("universe")},
              "sitemaps": crawl.get("sitemaps"), "products": given, "policies": policies,
              "pages": [{"id": page, "type": kind, "url": entries[page]["url"],
                         **{k: entries[page].get(k) for k in fields}} for page, kind in chosen.items()],
              "stopped": None, "reservation": None, "finished_at": now()}
    write_json(folder / "audit.json", record)
    return record


def load_list(path: Path) -> list[str]:
    """The product pages of an engagement: one URL per line; blank lines and # comments skipped."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise PageError(f"no se puede leer {path}: {exc}") from None
    return [l.strip() for l in lines if l.strip() and not l.lstrip().startswith("#")]
