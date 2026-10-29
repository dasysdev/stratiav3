"""Capture of the pages of an audit of a site (D-167), all under the audit profile (audit-es).

One audit is one directory, var/audits/<audit>/, never replaced, with everything in it:

  audit.json          the manifest: every page with its type (product, home, policy, category),
                      what was located and what was not, and whether each product page is in
                      the sitemaps
  sites/<host>/       robots.txt and tdmrep.json of each origin visited
  sitemaps/           the sitemaps as they came (indexes and gzip included), numbered
  pages/<page>/<at>/  the snapshot of each page (capture.visit)

The pages: the product pages of the engagement (the list given); the home page; the shipping,
returns, contact and legal notice pages, located from the links of the home page (its footer
first); and the immediate category of each product page, by its breadcrumbs. A policy that is
not located, or a product page without breadcrumbs, is recorded as such and never replaced by
another page. Two product pages that share their category capture it once.

The sitemaps are those declared in robots.txt or, if none, /sitemap.xml, read up to a budget.
Whether a product page is in them, by its URL, its final URL or the canonical URL it declares,
is yes, no, or undetermined when sitemaps were left unread or failed: an absence needs the whole
coverage.

Each page gets a fresh window and context of its own (audit-es), with a short pause between
pages (or the Crawl-delay, if larger). A block stops the audit; the rest is recorded as pending.

A TDM reservation stops it too (D-171). Before capturing anything the audit reads the tdmrep.json
of the site: any entry that reserves stops it with nothing captured. The home page is the first
page visited, and its header and meta are the rest of that check. A reservation that appears
later (a page, or the tdmrep.json of another origin) stops it there: that page is not kept, the
pages before it are. The manifest records the stop and its evidence (`reservation`).
Reading an audit and the links of its pages needs neither Chrome nor websockets (on the host).
"""
from __future__ import annotations

import base64
import gzip
import json
import random
import re
import time
import unicodedata
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlsplit

from . import ROOT, profile, profiles, tdm
from .files import now, read_json, sha256, unique_dir, write_json
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
    data = read_json(AUDITS / audit_id / "audit.json")
    if data is None:
        raise AuditError(f"no hay auditoría {audit_id}")
    return data


def read(audit_id: str, page_id: str) -> str:
    """The document of a captured page of an audit (the HTTP response, in UTF-8)."""
    page = next((p for p in manifest(audit_id)["pages"] if p["id"] == page_id), None)
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
    """The links of a document, each with its text, whether it is in the footer and the
    breadcrumb trail it belongs to (if any)."""

    def __init__(self, base: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base = base
        self.stack: list[tuple[str, bool, int | None]] = []   # (tag, footer, trail)
        self.links: list[dict] = []
        self.trails = 0
        self._open: dict | None = None

    def _state(self) -> tuple[bool, int | None]:
        return self.stack[-1][1:] if self.stack else (False, None)

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
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
                          "footer": footer, "trail": trail}
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
                  pause_s=PAUSE_S) -> dict:
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
        entry.update({"file": f"sitemaps/{name}", "bytes": len(data), "sha256": sha256(data),
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


def in_sitemaps(sitemaps: dict, url: str, url_final: str | None, canonical=()) -> dict:
    """Whether a product page is in the sitemaps by its URL as requested, its final URL or the
    canonical URL it declares, in that order; `by` says which one matched."""
    candidates = [("url", url), ("url_final", url_final)] + [("canonical", c) for c in canonical]
    for by, candidate in candidates:
        if candidate and _clean(candidate) in sitemaps["urls"]:
            return {"value": "yes", "match": _clean(candidate), "by": by}
    return {"value": "no" if sitemaps["complete"] else "undetermined"}


# ------------------------------------------------------------------ the audit
def check_new(audit_id: str) -> Path:
    if not ID.fullmatch(audit_id):
        raise AuditError(f"ID no válido: {audit_id!r} (minúsculas, dígitos y guiones)")
    folder = AUDITS / audit_id
    if folder.exists():
        raise AuditError(f"la auditoría {audit_id} ya existe y no se sustituye; la nueva lleva otro ID")
    return folder


def run(audit_id: str, products: list[str], browser=None, pause_s=PAUSE_S,
        sitemap_files: int = SITEMAP_FILES, sitemap_mb: int = SITEMAP_MB, out=print) -> dict:
    """Capture the pages of an audit of the site of `products` (its product pages) and return
    its manifest, written in var/audits/<audit>/audit.json."""
    from .browser import Browser
    from .once import _refused
    from .visit import visit

    folder = check_new(audit_id)
    if not products:
        raise AuditError("sin fichas del encargo")
    origins = {"{0.scheme}://{0.netloc}".format(urlsplit(u)) for u in products}
    if len(origins) != 1:
        raise AuditError(f"las fichas de una auditoría son de un solo sitio: {', '.join(sorted(origins))}")
    base = origins.pop()
    folder.mkdir(parents=True)
    chosen = profiles.AUDIT_ES
    record = {"audit": audit_id, "site": base, "profile": chosen.name, "started_at": now(),
              "products": [{"url": u} for u in products], "pages": []}
    own = browser is None
    if own:
        browser = Browser(profile())
        browser.start()
    tool = browser.new_window(chosen)
    sites = _Sites(folder / "sites")
    by_url: dict[str, dict] = {}
    state = {"stopped": None, "visited": 0, "reservation": None}

    def stop_reserved(where: str, url: str, evidence: dict) -> None:
        """A TDM reservation stops the audit (D-171): what is left stays pending."""
        nothing = not any(p.get("outcome") == "captured" for p in record["pages"])
        state["reservation"] = {"where": where, "url": url, **evidence}
        state["stopped"] = (f"auditoría parada: reserva TDM en {where} ({evidence['source']}); "
                            + ("no se captura nada" if nothing else "lo pendiente no se captura"))

    def origin_file(url: str) -> str:
        return str((sites.folder / urlsplit(url).netloc.replace(":", "_") / "tdmrep.json").relative_to(folder))

    def capture(page_id: str, kind: str, url: str) -> dict:
        key = _clean(url)
        if key in by_url:
            return by_url[key]
        entry = {"id": page_id, "type": kind, "url": url}
        record["pages"].append(entry)
        by_url[key] = entry
        if state["stopped"]:
            entry.update({"outcome": "pending", "detail": state["stopped"]})
            return entry
        robots, entries, summary = sites.of(tool, url)
        snap = unique_dir(folder / "pages" / page_id)
        meta = {"profile": chosen.name, "legitimacy": summary, "audit": audit_id, "page_type": kind,
                "robots_bots": robots.by_bot(url, profiles.BOTS)}
        if state["visited"]:
            time.sleep(max(random.uniform(*pause_s), robots.crawl_delay() or 0))
        state["visited"] += 1
        if tdm.reserving(entries):   # the tdmrep.json of another origin
            result = _refused(snap, url, meta, "reserved", "reserva TDM (tdmrep.json): no se conserva el contenido")
        elif not robots.allowed(url):
            result = _refused(snap, url, meta, "disallowed",
                              "robots.txt inaccesible" if robots.mode == "unreachable" else "robots.txt")
        else:
            window = browser.new_window(chosen)
            try:
                result = visit(window, url, snap, None, entries, browser.info, meta=meta)
            finally:
                browser.close_window(window)
        m = result["meta"]
        entry.update({"outcome": result["outcome"], "detail": result["detail"],
                      "snapshot": str(snap.relative_to(folder)), "url_final": m.get("url_final"),
                      "http_status": (m.get("http") or {}).get("status")})
        out(f"{page_id}: {result['outcome']} ({result['detail']})")
        if result["outcome"] == "blocked":
            state["stopped"] = f"auditoría parada: bloqueo en {page_id}"
        elif result["outcome"] == "reserved":
            if tdm.reserving(entries):
                evidence = {"source": "tdmrep.json", "file": origin_file(url), "entries": tdm.reserving(entries)}
            else:
                found = tdm.signals((m.get("http") or {}).get("headers"), m.get("page_meta"))
                source = "cabecera tdm-reservation" if found["header"] == "1" else "meta tdm-reservation"
                evidence = {"source": source, **found}
            stop_reserved(page_id, url, {**evidence, "snapshot": entry["snapshot"]})
        return entry

    def document(entry: dict) -> str | None:
        if entry.get("outcome") != "captured":
            return None
        snap = folder / entry["snapshot"]
        return _response_text(snap, read_json(snap / "meta.json")).decode("utf-8")

    try:
        # The check before capturing (D-171): tdmrep.json, then the header and meta of the home
        # page, which is the first page visited
        robots, entries, summary = sites.of(tool, base)
        record["legitimacy"] = summary
        if robots.mode == "unreachable":
            state["stopped"] = "robots.txt inaccesible: no se captura nada"
        elif tdm.reserving(entries):
            stop_reserved("tdmrep.json", base + "/.well-known/tdmrep.json",
                          {"source": "tdmrep.json", "file": origin_file(base), "entries": tdm.reserving(entries)})
        home = capture("home", "home", base + "/")
        home_doc = document(home)

        if not state["stopped"]:
            tool.idle(random.uniform(*pause_s))
            sitemaps = read_sitemaps(tool, sites, base, folder / "sitemaps",
                                     sitemap_files, sitemap_mb * 1_000_000, pause_s)
            record["sitemaps"] = {k: v for k, v in sitemaps.items() if k not in ("urls", "reserved")}
            record["sitemaps"]["urls"] = len(sitemaps["urls"])
            out(f"sitemaps: {len(sitemaps['read'])} leídos, {len(sitemaps['pending'])} pendientes, "
                f"{len(sitemaps['urls'])} URL")
            if sitemaps["reserved"]:
                stop_reserved("sitemaps", sitemaps["reserved"]["url"],
                              {"source": "tdmrep.json", "file": origin_file(sitemaps["reserved"]["url"]),
                               "entries": sitemaps["reserved"]["entries"]})
        policies = locate_policies(home_doc, home.get("url_final") or base + "/") if home_doc else \
            {k: {"status": "home_not_captured"} for k in POLICIES}

        for n, product in enumerate(record["products"], 1):
            entry = capture(f"product-{n:02d}", "product", product["url"])
            product["page"] = entry["id"]
            doc = document(entry)
            if doc:
                product["canonical"] = canonicals(doc, entry.get("url_final") or product["url"])
            if "sitemaps" in record:
                product["in_sitemaps"] = in_sitemaps(sitemaps, product["url"], entry.get("url_final"),
                                                     product.get("canonical") or ())
            product["breadcrumbs"] = breadcrumbs(doc, product["url"], entry.get("url_final")) if doc \
                else {"status": "not_captured"}

        for kind, policy in policies.items():
            if policy["status"] == "located":
                policy["page"] = capture(f"policy-{kind}", "policy", policy["url"])["id"]
        record["policies"] = policies

        categories = 0
        for product in record["products"]:
            category = product["breadcrumbs"].get("category")
            if category:
                if _clean(category) not in by_url:
                    categories += 1
                product["category_page"] = capture(f"category-{categories:02d}", "category", category)["id"]
    finally:
        browser.close_window(tool)
        if own:
            browser.stop()
        record["stopped"] = state["stopped"]
        record["reservation"] = state["reservation"]
        record["finished_at"] = now()
        write_json(folder / "audit.json", record)
    return record


def load_list(path: Path) -> list[str]:
    """The product pages of an engagement: one URL per line; blank lines and # comments skipped."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise PageError(f"no se puede leer {path}: {exc}") from None
    return [l.strip() for l in lines if l.strip() and not l.lstrip().startswith("#")]
