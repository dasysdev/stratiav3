"""The spider of an audit (D-170): from the home page, the pages of a site discovered by the
<a href> links of the response document without JavaScript, each page captured once under
audit-es in the same visit that reads its links.

  crawl.json          the manifest: the crawl (start, hosts, limit, coverage), every URL
                      processed, with its outcome and snapshot, and the universe of the audit
  crawl.jsonl         the journal: a line per run, per URL processed and for the sitemaps read
  sites/<host>/       robots.txt and tdmrep.json of each origin (a resumed run: resumes/NN/<host>/)
  sitemaps/           the sitemaps as they came, read after the home page (capture.audit)
  pages/<page>/<at>/  the snapshot of each page (capture.visit) and links.json.gz: every <a href>
                      of its document, with its text, nofollow and why it was not followed

What is followed: http(s) links of the host of the start URL (or of the final URL of the home
page), without query (no facets: D-173) except a single numeric pagination parameter (D-204),
and not a known resource that is not a page (by its extension); the fragment is dropped.
nofollow links are followed and recorded. The links only discover: nothing about them is judged.

Order (D-204, D-215): learnt during the crawl, with no setting per site.
  - A product page is a captured page whose document says so (og:type, a Product at the top of
    the JSON-LD or the microdata). A category is a link of the breadcrumbs of a product page, at
    any level, and any URL of the shape of those. Each URL has a shape: its path with slugs and
    numbers abstracted (W-p-N.html, W-c-N, W-c-N?page).
  - First the policies of the audit (D-167), located in the links of the home page (its footer
    first, as capture.audit locates them).
  - Then category by category: a category, all its pagination (a page that lists no product
    ends it), then the product pages its pages list; then the next category (those of the
    breadcrumbs first, then by shape). A category captured before it was known as one is gone
    through the same way, without asking for it again.
  - Then the product pages found elsewhere; a shape not captured yet, once (probe); and the rest,
    the shapes whose pages found most product URLs first (other).
  - Before the first product page, product pages and probes lead and this is breadth first. The
    order only matters when the crawl is cut short: a complete crawl reaches the same pages.

The sitemaps (D-170): read after the home page, as capture.audit reads them. When the crawl has
nothing left, each URL of the sitemaps it did not reach is captured once (chosen as `sitemap`):
its links are not read, so it adds nothing to the crawl. A URL of the sitemaps that is the URL, the
final URL or the canonical URL of a page of the crawl is that page.

The universe (universe; crawl.universe sums it up): every URL of the crawl and of the sitemaps, once, with its page,
whether the crawl reached it, whether it is in the sitemaps and its type. Reached and in the
sitemaps are yes, no, or undetermined when the crawl or the reading of the sitemaps is not
complete: an absence needs the whole coverage. The type takes several signals, not the markup
alone, and what is doubtful is left without one (None):
  - home: the start URL; policy: a policy of D-167 located in the home page;
  - product: product signals in its document and a URL of a product shape;
  - category: in the breadcrumbs of a product page or of their shape (its pagination too), it
    lists URLs of a product shape and has no product signal;
  - other: none of those signals; a page not captured, not HTML or of another host has no type.

Pace: at most one page per second, or the Crawl-delay if larger; a fresh window and context per
page. Limit: 50 000 URLs processed.

Legitimacy and stops, as in capture.audit: robots.txt and tdmrep.json of each origin, the home
page first; a TDM reservation stops the crawl (D-171) and so does a block. The origin of the
requests (RIPEstat) is consulted once per run and recorded in every page.

Coverage: complete when nothing is left to process, the links of every page were read and the
sitemaps were read whole; if not, the manifest says why (limit, block, reservation,
interruption, pages that failed, sitemaps) and what is pending. crawl_complete says whether the
crawl itself, the URLs of the sitemaps aside, is complete. A crawl whose pages the audit chose
(audit.json) is not resumed. A crawl that is interrupted or stopped by a block or the limit is resumed from
its journal: nothing already processed is asked for again; a blocked page is retried first.
"""
from __future__ import annotations

import gzip
import json
import re
import time
from collections import Counter, deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit, urlunsplit

from . import profile, profiles, tdm
from .audit import (AUDITS, SITEMAP_FILES, SITEMAP_MB, AuditError, _Sites, breadcrumbs, canonicals, check_new,
                    links, locate_policies, read_sitemaps)
from .files import now, read_json, unique_dir, write_evidence, write_json
from .pages import _response_text, json_ld

LIMIT = 50_000
MIN_INTERVAL_S = 1.0
JOURNAL = "crawl.jsonl"
MANIFEST = "crawl.json"
HTML = ("text/html", "application/xhtml+xml")

# Extensions of resources that are not pages: their links are not followed
RESOURCES = frozenset("""pdf jpg jpeg png gif webp avif svg ico bmp tif tiff heic mp4 webm mov avi
    m4v mp3 wav ogg m4a zip rar 7z gz tgz tar doc docx xls xlsx ppt pptx odt ods csv txt xml json
    css js mjs map woff woff2 ttf otf eot exe dmg apk""".split())

PAGINATION = frozenset({"page", "p", "pag", "pagina", "pg"})   # D-204
PRODUCT_TYPES = {"product", "productgroup"}
OG_PRODUCT = {"product", "og:product", "product.item", "product.group"}
PRODUCT_RATE = 0.5   # share of the captured pages of a shape that are product pages


def pagination(query: str) -> str | None:
    """The query as kept when it is a single numeric pagination parameter (`page=2`), else None."""
    pairs = parse_qsl(query, keep_blank_values=True)
    if len(pairs) == 1 and pairs[0][0].lower() in PAGINATION and pairs[0][1].isdigit():
        return f"{pairs[0][0]}={pairs[0][1]}"
    return None


def _base(url: str) -> str:
    """A URL without its query: the category a pagination URL belongs to."""
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def normal(url: str) -> str:
    """A URL as the spider keys it: scheme and host in lowercase, `/` for an empty path, no
    fragment and no query but a pagination one."""
    parts = urlsplit(url)
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path or "/",
                       pagination(parts.query) or "", ""))


def url_key(url: str) -> str:
    """A URL as the universe keys it: as `normal`, but with its whole query (a URL of the sitemaps
    may have one)."""
    parts = urlsplit(url)
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path or "/", parts.query, ""))


def _tail(segment: str) -> str:
    """The shape of a slug by its end: numbers (N), then a short marker before them (p, c), the
    rest W."""
    tokens = [t for t in re.split(r"[-_]+", segment) if t]
    tail = []
    while tokens and tokens[-1].isdigit():
        tokens.pop()
        if not tail:
            tail.append("N")
    if tail and tokens and len(tokens[-1]) <= 2 and tokens[-1].isalpha():
        tail.append(tokens.pop().lower())
    if tokens:
        tail.append("W")
    return "-".join(reversed(tail))


def shape(url: str) -> str:
    """The shape of a URL: an inner segment that is one plain word is kept (products,
    collections, es), the rest abstracted; the last segment by its end and its extension; a
    pagination parameter by its name. /a-b-c-p-12-34.html → W-p-N.html."""
    parts = urlsplit(url)
    segments = [s for s in parts.path.split("/") if s]
    out = []
    for i, segment in enumerate(segments):
        if i < len(segments) - 1:
            out.append(segment.lower() if segment.isalpha() and len(segment) <= 20 else _tail(segment))
        else:
            stem, dot, ext = segment.rpartition(".")
            out.append(_tail(stem) + "." + ext.lower() if dot and stem and ext.isalnum() else _tail(segment))
    query = pagination(parts.query)
    return "/" + "/".join(out) + ("?" + query.split("=")[0].lower() if query else "")


class _Signals(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.og: str | None = None
        self.microdata = 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "meta" and a.get("property", "").lower() == "og:type" and self.og is None:
            self.og = a.get("content", "").strip().lower()
        if "itemscope" in a and "itemprop" not in a:   # a top-level item
            if {t.rstrip("/").rsplit("/", 1)[-1].lower() for t in a.get("itemtype", "").split()} & PRODUCT_TYPES:
                self.microdata += 1


def product_signals(doc: str) -> list[str]:
    """The signals of a product page in a document: og:type product, or one product (a Product
    and its ProductGroup at most) at the top of the JSON-LD or the microdata. The products of a
    listing (inside an ItemList) are not at the top."""
    parser = _Signals()
    parser.feed(doc)
    parser.close()
    found = []
    if parser.og in OG_PRODUCT:
        found.append("og:type")
    top = []
    for block in json_ld(doc):
        for node in block if isinstance(block, list) else [block]:
            if isinstance(node, dict):
                top += [node, *(node.get("@graph") or []), node.get("mainEntity")]
    count = 0
    for node in top:
        types = node.get("@type") if isinstance(node, dict) else None
        types = types if isinstance(types, list) else [types]
        count += any(str(t).lower() in PRODUCT_TYPES for t in types)
    if 1 <= count <= 2:
        found.append("json-ld")
    if 1 <= parser.microdata <= 2:
        found.append("microdata")
    return found


def skip_reason(url: str, hosts, query: bool = False) -> str | None:
    """Why a link is not followed (other scheme, external, query, resource), or None; with
    `query`, a URL with any query is (a URL of the sitemaps)."""
    parts = urlsplit(url)
    if parts.scheme.lower() not in ("http", "https"):
        return "other"
    if parts.netloc.lower() not in hosts:
        return "external"
    if parts.query and not query and not pagination(parts.query):
        return "query"
    last = parts.path.rsplit("/", 1)[-1]
    if "." in last and last.rsplit(".", 1)[1].lower() in RESOURCES:
        return "resource"
    return None


class _State:
    """What the journal holds: the URLs discovered (in order), the entries processed, the runs
    and, from them, what the crawl learnt of each shape and what to visit next."""

    def __init__(self, folder: Path | None = None) -> None:
        self.folder = folder                      # the audit: the links of its pages
        self.runs: list[dict] = []
        self.discovered: dict[str, dict] = {}     # normal URL → {n, depth, from, nofollow}
        self.entries: dict[str, dict] = {}        # page ID → entry
        self.by_url: dict[str, str] = {}          # normal URL requested → page ID
        self.finals: dict[str, str] = {}          # normal final URL of a page visited → page ID
        self.shapes: dict[str, dict] = {}         # shape → {captured, products, links: shapes of the URLs it found}
        self.waiting: dict[str, deque] = {}       # shape → its URLs not visited, in order of discovery
        self.retry: deque = deque()               # blocked pages, retried first
        self.targets: dict[str, dict] = {}        # normal URL → the page of D-167 it is for
        self.audit: deque = deque()               # the policies not visited, in order
        self.crumbs: deque = deque()              # the categories of breadcrumbs not visited, in order
        self.category_shapes: Counter = Counter() # shape → categories found in breadcrumbs
        self.children: dict[str, list] = {}       # page ID → the URLs it found first
        self.pages_of: dict[str, list] = {}       # URL without query → its pagination URLs
        self.group: str | None = None             # the category being gone through
        self.grouped: set[str] = set()            # the categories gone through (or going)
        self.ungrouped: deque = deque()           # categories captured, not gone through yet
        self.events: list[str] = []               # groups opened by `next`, for the journal
        self._links: dict[str, list] = {}         # page ID → its followed links (the group's pages)
        self.hosts: set[str] = set()              # the hosts of the crawl
        self.sitemaps: dict | None = None         # what was read of the sitemaps; None: not read yet
        self.listed: list[str] = []               # the URLs of the sitemaps (key), in order
        self.in_listed: set[str] = set()          # the same, to look up
        self.covered: set[str] = set()            # the URLs, final URLs and canonical URLs of the crawl
        self.extra: deque | None = None           # the URLs of the sitemaps to capture, once the crawl is done

    def discover(self, url: str, depth: int, parent: str | None, nofollow: bool) -> bool:
        if url in self.discovered or url in self.finals:
            return False
        self.discovered[url] = {"n": len(self.discovered), "depth": depth, "from": parent, "nofollow": nofollow}
        self.waiting.setdefault(shape(url), deque()).append(url)
        if parent:
            self.children.setdefault(parent, []).append(url)
        if urlsplit(url).query:   # a followed query is a pagination one
            self.pages_of.setdefault(_base(url), []).append(url)
        return True

    def target(self, url: str, purpose: dict, entry: dict) -> bool:
        """Mark a URL as a page of the audit (D-167): a policy goes first; a category is gone through."""
        if url in self.targets:
            return False
        self.targets[url] = purpose
        if "category_of" in purpose:
            key = shape(url)
            self.category_shapes[key] += 1
            if self.category_shapes[key] == 1:   # a new shape of categories: those already captured
                for e in self.entries.values():
                    if e["outcome"] == "captured" and (e.get("shape") or shape(e["url"])) == key:
                        self._ungrouped(e["url"])
        if "skip" not in purpose:
            self.discover(url, entry["depth"] + 1, entry["id"], False)
            if self.done(url):
                if "category_of" in purpose:
                    self._ungrouped(url)
            else:
                (self.crumbs if "category_of" in purpose else self.audit).append(url)
        return True

    def _ungrouped(self, url: str) -> None:
        if _base(url) not in self.grouped and _base(url) not in self.ungrouped:
            self.ungrouped.append(_base(url))

    def open_group(self, key: str) -> None:
        self.group = key
        self.grouped.add(key)
        self._links.clear()

    def links_of(self, page_id: str) -> list:
        """Every followed link of a captured page (its links.json.gz), or the URLs it found first."""
        if page_id not in self._links:
            entry = self.entries[page_id]
            path = self.folder / entry["snapshot"] / "links.json.gz" if self.folder and entry.get("snapshot") else None
            if path and path.is_file():
                rows = json.loads(gzip.decompress(path.read_bytes()))
                urls = [normal(r["url"]) for r in rows if not r["skip"]]
            else:
                urls = self.children.get(page_id, [])
            self._links[page_id] = list(dict.fromkeys(urls))
        return self._links[page_id]

    def done(self, url: str) -> bool:
        return url in self.by_url or url in self.finals

    def unreached(self) -> list:
        """The URLs of the sitemaps that no page of the crawl is, that the crawl did not discover
        and that can be captured: what is captured once the crawl is done."""
        return [u for u in self.listed if u not in self.covered and u not in self.discovered
                and not skip_reason(u, self.hosts, query=True)]

    def page_of(self, url: str) -> str | None:
        return self.by_url.get(url) or self.finals.get(url)

    def product_like(self, key: str) -> bool:
        stats = self.shapes.get(key)
        return bool(stats and stats["products"] and stats["products"] >= PRODUCT_RATE * stats["captured"])

    def processed(self, entry: dict) -> None:
        previous = self.entries.get(entry["id"])
        new = previous is None or previous["outcome"] == "blocked"
        self.entries[entry["id"]] = entry
        sitemap = entry.get("source") == "sitemaps"
        self.by_url[(url_key if sitemap else normal)(entry["url"])] = entry["id"]
        if entry.get("url_final"):
            self.finals.setdefault((url_key if sitemap else normal)(entry["url_final"]), entry["id"])
        if not sitemap:
            self.covered.update(url_key(u) for u in [entry["url"], entry.get("url_final"), *entry.get("canonical", [])] if u)
        if entry["outcome"] == "blocked":
            self.retry.append(entry["url"])
        elif sitemap:   # captured once: it teaches the crawl nothing
            return
        elif new and entry["outcome"] == "captured":
            stats = self.shapes.setdefault(entry.get("shape") or shape(entry["url"]),
                                           {"captured": 0, "products": 0, "links": Counter()})
            stats["captured"] += 1
            stats["products"] += bool(entry.get("product_signals"))
            if entry.get("chosen_as") == "category":
                self.open_group(_base(entry["url"]))
            elif (entry.get("shape") or shape(entry["url"])) in self.category_shapes \
                    and not urlsplit(entry["url"]).query:
                self._ungrouped(entry["url"])

    def found(self, entry: dict, urls) -> None:
        """Count the shapes of the URLs a captured page found first: what a listing yields."""
        if entry["outcome"] == "captured" and entry.get("source") != "sitemaps":
            self.shapes[entry.get("shape") or shape(entry["url"])]["links"].update(shape(u) for u in urls)

    def product_links(self, key: str, products: set) -> float:
        """The URLs of product shapes that a page of this shape found, on average."""
        stats = self.shapes[key]
        return sum(n for k, n in stats["links"].items() if k in products) / stats["captured"]

    def replay(self, line: dict) -> None:
        if "run" in line:
            self.runs.append(line["run"])
            self.discover(line["run"]["start"], 0, None, False)   # the start URL, discovered first
        elif "run_end" in line:
            self.runs[line["run_end"]["run"] - 1].update(line["run_end"])
        elif "group" in line:
            self.open_group(line["group"])
        elif "sitemaps" in line:
            self.read(line["sitemaps"])
        elif "page" in line:
            entry = line["page"]
            if entry["url"] in self.retry:
                self.retry.remove(entry["url"])
            self.processed(entry)
            for url, nofollow in line.get("found", []):
                self.discover(url, entry["depth"] + 1, entry["id"], nofollow)
            self.found(entry, [url for url, _ in line.get("found", [])])
            for url, purpose in line.get("targets", []):
                self.target(url, purpose, entry)

    def read(self, sitemaps: dict) -> None:
        """What was read of the sitemaps: their summary and their URLs."""
        self.listed = list(dict.fromkeys(sitemaps["urls"]))
        self.sitemaps = {**sitemaps, "urls": len(self.listed)}
        self.in_listed = set(self.listed)

    def _in_group(self, products: set) -> tuple[str, str] | None:
        """The next URL of the category being gone through: its pagination, from the pages that
        list product pages, then the product pages its pages list."""
        key = self.group
        pages = [p for p in [self.page_of(key)] + [self.page_of(u) for u in self.pages_of.get(key, [])] if p]
        for page_id in pages:
            links = self.links_of(page_id)
            if any(shape(u) in products for u in links):
                for url in links:
                    if _base(url) == key and urlsplit(url).query and not self.done(url):
                        return url, "pagination"
        for page_id in pages:
            for url in self.links_of(page_id):
                if shape(url) in products and not self.done(url):
                    return url, "listed"
        return None

    def next(self) -> tuple[str, str] | None:
        """The next URL and why (retry, audit, pagination, listed, category, product, probe,
        other); None when nothing is left."""
        if self.retry:
            return self.retry.popleft(), "retry"
        while self.audit and self.done(self.audit[0]):
            self.audit.popleft()
        if self.audit:
            return self.audit.popleft(), "audit"
        products = {key for key in self.shapes if self.product_like(key)}
        while self.group:
            chosen = self._in_group(products)
            if chosen:
                return chosen
            self.group = None
            while self.ungrouped and self.ungrouped[0] in self.grouped:
                self.ungrouped.popleft()
            if self.ungrouped:   # a category captured before it was known as one
                self.open_group(self.ungrouped.popleft())
                self.events.append(self.group)
        while self.ungrouped and self.ungrouped[0] in self.grouped:
            self.ungrouped.popleft()
        if self.ungrouped:
            self.open_group(self.ungrouped.popleft())
            self.events.append(self.group)
            return self.next()
        while self.crumbs and self.done(self.crumbs[0]):
            self.crumbs.popleft()
        if self.crumbs:
            return self.crumbs.popleft(), "category"
        best, empty = {}, []
        for key, urls in self.waiting.items():
            while urls and self.done(urls[0]):
                urls.popleft()
            if not urls:
                empty.append(key)
                continue
            stats = self.shapes.get(key)
            first = self.discovered[urls[0]]["n"]
            if key in self.category_shapes and key not in products:
                rank = (0, 0, first)
            elif key in products:
                rank = (1, -stats["products"] / stats["captured"], first)
            elif stats is None:
                rank = (2, 0, first)
            else:
                rank = (3, -self.product_links(key, products), first)
            if rank[0] not in best or rank < best[rank[0]][0]:
                best[rank[0]] = (rank, key)
        for key in empty:
            del self.waiting[key]
        if not best:
            if self.sitemaps is None:
                return None
            if self.extra is None:
                self.extra = deque(self.unreached())
            while self.extra and self.done(self.extra[0]):
                self.extra.popleft()
            return (self.extra.popleft(), "sitemap") if self.extra else None
        tier = min(best)
        return self.waiting[best[tier][1]].popleft(), ("category", "product", "probe", "other")[tier]

    def put_back(self, url: str, why: str) -> None:
        if why in ("pagination", "listed"):   # never taken out of their queues
            return
        if why == "sitemap":
            self.extra.appendleft(url)
            return
        crumb = why == "category" and "category_of" in self.targets.get(url, {})
        queue = self.crumbs if crumb else {"retry": self.retry, "audit": self.audit}.get(why) \
            or self.waiting.setdefault(shape(url), deque())
        queue.appendleft(url)

    def pending(self) -> list:
        """What is left: the blocked pages, then the rest in the order of discovery, then the URLs
        of the sitemaps the crawl did not reach."""
        rest = [u for u in self.unreached() if not self.done(u)]
        return list(self.retry) + [u for u in self.discovered if not self.done(u)] + rest

    def crawl_pending(self) -> list:
        """What is left of the crawl itself: the URLs of the sitemaps aside."""
        return [u for u in self.retry if u not in self.by_url or not self._sitemap(self.by_url[u])] \
            + [u for u in self.discovered if not self.done(u)]

    def _sitemap(self, page_id: str) -> bool:
        return self.entries[page_id].get("source") == "sitemaps"


def _load(folder: Path) -> _State:
    state = _State(folder)
    with open(folder / JOURNAL, encoding="utf-8") as f:
        for raw in f:
            if raw.strip():
                try:
                    state.replay(json.loads(raw))
                except ValueError:   # a line cut short by a hard stop: that URL is processed again
                    continue
    return state


def _recover(folder: Path, page_id: str, url: str, known: set) -> tuple[Path, dict] | None:
    """A snapshot of `url` that a hard stop left out of the journal: its visit is not repeated."""
    for meta_path in sorted((folder / "pages" / page_id).glob("*/meta.json")):
        snap = meta_path.parent
        meta = read_json(meta_path)
        if str(snap.relative_to(folder)) not in known and meta.get("url_requested") == url:
            return snap, meta
    return None


def run(audit_id: str, start: str | None = None, resume: bool = False, limit: int | None = None,
        browser=None, min_interval_s: float = MIN_INTERVAL_S, sitemap_files: int = SITEMAP_FILES,
        sitemap_mb: int = SITEMAP_MB, out=print) -> dict:
    """Crawl and capture the site of `start` (its home page) in var/audits/<audit>/, or resume
    that crawl, and return its manifest, written in crawl.json."""
    from .browser import Browser
    from .once import _refused
    from .visit import visit

    if resume:
        folder = AUDITS / audit_id
        if not (folder / JOURNAL).is_file():
            raise AuditError(f"no hay rastreo {audit_id} que reanudar")
        if (folder / "audit.json").exists():
            raise AuditError(f"{audit_id}: la auditoría ya eligió sus páginas (audit.json); el rastreo no se reanuda")
        record = read_json(folder / MANIFEST) or {}
        state = _load(folder)
        if record.get("reservation") or any(e["outcome"] == "reserved" for e in state.entries.values()):
            raise AuditError(f"{audit_id}: rastreo parado por una reserva TDM (D-171); no se reanuda")
        start, limit = state.runs[0]["start"], limit or state.runs[-1]["limit"]
        if not state.pending() and state.sitemaps is not None:
            raise AuditError(f"{audit_id}: no queda nada que rastrear")
    else:
        folder = check_new(audit_id)
        parts = urlsplit(start or "")
        if parts.scheme not in ("http", "https") or not parts.netloc:
            raise AuditError(f"URL de inicio no válida: {start!r}")
        start, limit, state = normal(start), limit or LIMIT, _State(folder)
        state.discover(start, 0, None, False)
        folder.mkdir(parents=True)

    base = "{0.scheme}://{0.netloc}".format(urlsplit(start))
    hosts = {urlsplit(start).netloc}
    for entry in state.entries.values():
        if entry["depth"] == 0 and entry.get("url_final"):
            hosts.add(urlsplit(normal(entry["url_final"])).netloc)
    state.hosts = hosts
    chosen = profiles.AUDIT_ES
    number = len(state.runs) + 1
    sites_dir = folder / "sites" if number == 1 else folder / "resumes" / f"{number:02d}"
    this_run = {"run": number, "started_at": now(), "start": start, "limit": limit,
                "sitemap_budget": {"files": sitemap_files, "mb": sitemap_mb},
                "sites": str(sites_dir.relative_to(folder)), "origin": profiles.origin()}   # once per run
    cut = False
    if (folder / JOURNAL).is_file() and (folder / JOURNAL).stat().st_size:
        with open(folder / JOURNAL, "rb") as f:   # a line cut short by a hard stop ends here
            f.seek(-1, 2)
            cut = f.read(1) != b"\n"
    journal = open(folder / JOURNAL, "a", encoding="utf-8")
    if cut:
        journal.write("\n")

    def write(line: dict) -> None:
        journal.write(json.dumps(line, ensure_ascii=False) + "\n")
        journal.flush()

    write({"run": this_run})
    state.runs.append(this_run)
    stop = {"stopped": None, "reservation": None, "interrupted": False, "limit": False}
    own = browser is None
    if own:
        browser = Browser(profile())
        browser.start()
    tool = browser.new_window(chosen)
    sites = _Sites(sites_dir)
    last_request = 0.0

    def origin_file(url: str) -> str:
        return str((sites.folder / urlsplit(url).netloc.replace(":", "_") / "tdmrep.json").relative_to(folder))

    def reserved(where: str, url: str, evidence: dict) -> None:
        stop["reservation"] = {"where": where, "url": url, **evidence}
        nothing = not any(e["outcome"] == "captured" for e in state.entries.values())
        stop["stopped"] = (f"rastreo parado: reserva TDM en {where} ({evidence['source']}); "
                           + ("no se captura nada" if nothing else "lo pendiente no se captura"))

    def read_links(snap: Path, meta: dict, entry: dict, follow: bool) -> list:
        """The links of a captured page: links.json.gz in its snapshot and, if it is followed, the
        URLs new to the crawl."""
        final = meta.get("url_final") or entry["url"]
        if urlsplit(final).netloc.lower() not in hosts:
            entry["offsite"] = True
            return []
        if (meta.get("http") or {}).get("mime") not in HTML:
            entry["not_html"] = True
            return []
        found, rows, skipped = [], [], Counter()
        for link in links(_response_text(snap, meta).decode("utf-8"), final):
            reason = skip_reason(link["url"], hosts)
            rows.append({"url": link["url"], "text": link["text"][:120], "nofollow": link["nofollow"],
                         "skip": reason})
            if reason:
                skipped[reason] += 1
            elif follow and state.discover(normal(link["url"]), entry["depth"] + 1, entry["id"], link["nofollow"]):
                found.append([normal(link["url"]), link["nofollow"]])
        if not (snap / "links.json.gz").exists():
            write_evidence(snap, "links.json", json.dumps(rows, ensure_ascii=False).encode("utf-8"))
        entry["links"] = {"total": len(rows), "nofollow": sum(r["nofollow"] for r in rows),
                          "new": len(found), "skipped": dict(skipped)}
        return found

    def audit_pages(doc: str, entry: dict) -> list:
        """The pages of the audit (D-167) a captured page points to: the policies, from the home
        page; every category of its breadcrumbs, from a product page."""
        final = entry["url_final"] or entry["url"]
        out = []
        if entry["depth"] == 0:
            for kind, policy in locate_policies(doc, final).items():
                if policy["status"] == "located":
                    out.append((policy["url"], {"policy": kind}))
        if entry.get("product_signals"):
            own = {normal(entry["url"]), normal(final)}
            for crumb in breadcrumbs(doc, entry["url"], entry["url_final"]).get("trail") or []:
                if crumb["url"] and normal(crumb["url"]) not in own and urlsplit(crumb["url"]).path not in ("", "/"):
                    out.append((crumb["url"], {"category_of": entry["id"]}))
        targets = []
        for url, purpose in out:
            reason = skip_reason(url, hosts)
            targets.append([url if reason else normal(url), {**purpose, "skip": reason} if reason else purpose])
        return targets

    try:
        robots, entries, summary = sites.of(tool, base)
        this_run["legitimacy"] = summary
        if robots.mode == "unreachable":
            stop["stopped"] = "robots.txt inaccesible: no se captura nada"
        elif tdm.reserving(entries):
            reserved("tdmrep.json", base + "/.well-known/tdmrep.json",
                     {"source": "tdmrep.json", "file": origin_file(base), "entries": tdm.reserving(entries)})

        while not stop["stopped"]:
            if state.sitemaps is None and state.entries:   # after the home page (D-171), once
                read = read_sitemaps(tool, sites, base, folder / "sitemaps" if number == 1 else sites_dir / "sitemaps",
                                     sitemap_files, sitemap_mb * 1_000_000, (min_interval_s, min_interval_s),
                                     root=folder)
                summary = {k: v for k, v in read.items() if k not in ("urls", "reserved")}
                write({"sitemaps": {**summary, "urls": sorted(url_key(u) for u in read["urls"])}})
                state.read({**summary, "urls": sorted(url_key(u) for u in read["urls"])})
                out(f"sitemaps: {len(read['read'])} leídos, {len(read['pending'])} pendientes, "
                    f"{len(read['urls'])} URL")
                if read["reserved"]:
                    reserved("sitemaps", read["reserved"]["url"],
                             {"source": "tdmrep.json", "file": origin_file(read["reserved"]["url"]),
                              "entries": read["reserved"]["entries"]})
                    break
            chosen_next = state.next()
            if chosen_next is None:
                break
            url, why = chosen_next
            for key in state.events:   # a category captured before it was known as one
                write({"group": key})
            state.events.clear()
            page_id = state.by_url.get(url)
            if page_id is None and len(state.entries) >= limit:
                state.put_back(url, why)
                stop["limit"] = True
                break
            previous = state.entries.get(page_id)
            page_id = page_id or f"page-{len(state.entries) + 1:05d}"
            sitemap = why == "sitemap" or bool(previous and previous.get("source") == "sitemaps")
            found_by = state.discovered.get(url, {"depth": None if sitemap else 0, "from": None, "nofollow": False})
            entry = {"id": page_id, "url": url, "depth": found_by["depth"], "found_from": found_by["from"],
                     "shape": shape(url), "chosen_as": why}
            if sitemap:
                entry["source"] = "sitemaps"
            if url in state.targets:
                entry["audit_page"] = state.targets[url]
            if found_by["nofollow"]:
                entry["found_by_nofollow"] = True
            if previous:
                entry["attempts"] = previous.get("attempts", []) + [previous["snapshot"]]
            robots, entries, summary = sites.of(tool, url)
            meta = {"profile": chosen.name, "legitimacy": summary, "audit": audit_id,
                    "robots_bots": robots.by_bot(url, profiles.BOTS)}
            recovered = None
            if (folder / "pages" / page_id).exists():
                known = {e.get("snapshot") for e in state.entries.values()} | set(entry.get("attempts", []))
                recovered = _recover(folder, page_id, url, known)
            if recovered:
                snap, m = recovered
                result = {"outcome": m["outcome"], "detail": m["detail"], "meta": m}
                entry["recovered"] = True
            else:
                snap = unique_dir(folder / "pages" / page_id)
                if tdm.reserving(entries):   # the tdmrep.json of another origin
                    result = _refused(snap, url, meta, "reserved", "reserva TDM (tdmrep.json): no se conserva el contenido")
                elif not robots.allowed(url):
                    result = _refused(snap, url, meta, "disallowed",
                                      "robots.txt inaccesible" if robots.mode == "unreachable" else "robots.txt")
                else:
                    wait = max(min_interval_s, robots.crawl_delay() or 0) - (time.monotonic() - last_request)
                    if wait > 0:
                        time.sleep(wait)
                    last_request = time.monotonic()
                    window = browser.new_window(chosen)
                    try:
                        result = visit(window, url, snap, None, entries, browser.info, meta=meta,
                                       origin=this_run["origin"])
                    finally:
                        browser.close_window(window)
            m = result["meta"]
            entry.update({"outcome": result["outcome"], "detail": result["detail"],
                          "snapshot": str(snap.relative_to(folder)), "url_final": m.get("url_final"),
                          "http_status": (m.get("http") or {}).get("status"), "elapsed_s": result.get("elapsed_s")})
            if entry["depth"] == 0 and entry["url_final"]:
                hosts.add(urlsplit(normal(entry["url_final"])).netloc)
            same = entry["url_final"] and (state.by_url.get(normal(entry["url_final"]))
                                           or state.finals.get(normal(entry["url_final"])))
            if same and same != page_id:   # a redirect to a page already captured
                entry["same_as"] = same
            doc = None
            if result["outcome"] == "captured" and (m.get("http") or {}).get("mime") in HTML:
                doc = _response_text(snap, m).decode("utf-8")
                signals = product_signals(doc)
                if signals:
                    entry["product_signals"] = signals
                canonical = canonicals(doc, entry["url_final"] or url)
                if canonical:
                    entry["canonical"] = canonical
            state.processed(entry)   # what the page teaches comes before its links are weighed
            found = read_links(snap, m, entry, not sitemap) if result["outcome"] == "captured" else []
            state.found(entry, [u for u, _ in found])
            targets = audit_pages(doc, entry) if doc and not entry.get("offsite") and not sitemap else []
            targets = [[u, purpose] for u, purpose in targets if state.target(u, purpose, entry)]
            write({"page": entry, "found": found, "targets": targets})
            out(f"{page_id} {entry['outcome']} {entry['http_status'] or '-'} {why}"
                f"{' ficha' if entry.get('product_signals') else ''} {url}")
            if result["outcome"] == "blocked":
                stop["stopped"] = f"rastreo parado: bloqueo en {page_id}"
            elif result["outcome"] == "reserved":
                if tdm.reserving(entries):
                    evidence = {"source": "tdmrep.json", "file": origin_file(url), "entries": tdm.reserving(entries)}
                else:
                    found_tdm = tdm.signals((m.get("http") or {}).get("headers"), m.get("page_meta"))
                    source = "cabecera tdm-reservation" if found_tdm["header"] == "1" else "meta tdm-reservation"
                    evidence = {"source": source, **found_tdm}
                reserved(page_id, url, {**evidence, "snapshot": entry["snapshot"]})
    except KeyboardInterrupt:
        stop["interrupted"] = True
        out("rastreo interrumpido: se reanuda con --resume")
    finally:
        browser.close_window(tool)
        if own:
            browser.stop()
        end = {"run": number, "finished_at": now(), "legitimacy": this_run.get("legitimacy"),
               "interrupted": stop["interrupted"]}
        this_run.update(end)
        write({"run_end": end})
        journal.close()
        record = _manifest(audit_id, base, state, hosts, limit, stop, min_interval_s)
        write_json(folder / MANIFEST, record)
    return record


def in_sitemaps(state: _State, entry: dict) -> dict:
    """Whether a page is in the sitemaps by its URL, its final URL or the canonical URL it
    declares, in that order (`by`); no only when the reading of the sitemaps is complete."""
    listed = state.in_listed
    for by, url in [("url", entry["url"]), ("url_final", entry.get("url_final"))] \
            + [("canonical", c) for c in entry.get("canonical", [])]:
        if url and url_key(url) in listed:
            return {"value": "yes", "match": url_key(url), "by": by}
    return {"value": "no" if state.sitemaps and state.sitemaps["complete"] else "undetermined"}


def page_type(state: _State, entry: dict, products: set) -> str | None:
    """The type of a page of the universe from several signals; None when they do not agree or
    the page was not captured as HTML of the site."""
    if entry["outcome"] != "captured" or entry.get("offsite") or entry.get("not_html"):
        return None
    if entry["depth"] == 0:
        return "home"
    urls = {normal(entry["url"]), normal(entry.get("url_final") or entry["url"])}
    if any("policy" in state.targets.get(u, {}) and "skip" not in state.targets[u] for u in urls):
        return "policy"
    markup = bool(entry.get("product_signals"))
    product_shape = (entry.get("shape") or shape(entry["url"])) in products
    crumb = any("category_of" in state.targets.get(_base(u), {}) or shape(_base(u)) in state.category_shapes
                for u in urls)
    if markup and product_shape and not crumb:
        return "product"
    if crumb and not markup and not product_shape and any(shape(u) in products for u in state.links_of(entry["id"])):
        return "category"
    if not (markup or product_shape or crumb):
        return "other"
    return None


def universe(state: _State, products: set, crawl_complete: bool) -> list[dict]:
    """Every URL of the crawl and of the sitemaps, once: its page, whether the crawl reached it,
    whether it is in the sitemaps and its type."""
    unreached = "no" if crawl_complete else "undetermined"
    absent = "no" if state.sitemaps and state.sitemaps["complete"] else "undetermined"
    listed = state.in_listed
    rows: dict[str, dict] = {}
    for e in sorted(state.entries.values(), key=lambda e: e["id"]):
        found = in_sitemaps(state, e)
        row = {"url": url_key(e["url"]), "page": e["id"], "outcome": e["outcome"],
               "reached": unreached if e.get("source") == "sitemaps" else "yes",
               "in_sitemaps": found["value"], "type": page_type(state, e, products)}
        if found["value"] == "yes" and found["by"] != "url":
            row["sitemaps_by"] = found["by"]
        if e.get("same_as"):
            row["same_as"] = e["same_as"]
        rows.setdefault(row["url"], row)
    for url in state.discovered:
        if url not in rows and not state.done(url):
            rows[url] = {"url": url, "page": None, "outcome": "pending", "reached": "yes",
                         "in_sitemaps": "yes" if url in listed else absent, "type": None}
    for url in state.listed:
        if url not in rows and url not in state.covered:
            reason = skip_reason(url, state.hosts, query=True)
            rows[url] = {"url": url, "page": None, "outcome": "skipped" if reason else "pending",
                         "reached": unreached, "in_sitemaps": "yes", "type": None,
                         **({"skip": reason} if reason else {})}
    return list(rows.values())


def _manifest(audit_id, base, state, hosts, limit, stop, min_interval_s) -> dict:
    pages = sorted(state.entries.values(), key=lambda e: e["id"])
    pending = state.pending()
    products = {key for key in state.shapes if state.product_like(key)}
    waiting = Counter(shape(u) for u in pending)
    failed = [e["id"] for e in pages if e["outcome"] == "failed"]
    reasons = []
    if stop["limit"]:
        reasons.append({"reason": "limit", "detail": f"tope de {limit} URL"})
    if stop["reservation"]:
        reasons.append({"reason": "reserved", "detail": stop["stopped"]})
    elif stop["stopped"]:
        reasons.append({"reason": "blocked" if "bloqueo" in stop["stopped"] else "stopped", "detail": stop["stopped"]})
    if stop["interrupted"]:
        reasons.append({"reason": "interrupted", "detail": "interrumpido; se reanuda con --resume"})
    if failed:
        reasons.append({"reason": "failed", "detail": "páginas sin leer sus enlaces (error)", "pages": failed})
    if state.sitemaps is None:
        reasons.append({"reason": "sitemaps", "detail": "sitemaps sin leer"})
    elif not state.sitemaps["complete"]:
        reasons.append({"reason": "sitemaps", "detail": "sitemaps pendientes o fallidos"})
    skipped = Counter()
    for e in pages:
        if e.get("source") != "sitemaps":
            skipped.update((e.get("links") or {}).get("skipped", {}))
    crawl_complete = bool(pages) and not state.crawl_pending() \
        and not any(e["outcome"] == "failed" and e.get("source") != "sitemaps" for e in pages)
    rows = universe(state, products, crawl_complete)
    first = state.runs[0]
    return {
        "audit": audit_id, "site": base, "profile": profiles.AUDIT_ES.name, "started_at": first["started_at"],
        "legitimacy": first.get("legitimacy"), "runs": state.runs,
        "crawl": {
            "start": first["start"], "hosts": sorted(hosts), "limit": limit, "min_interval_s": min_interval_s,
            "discovered": len(state.discovered), "processed": len(pages),
            "outcomes": dict(Counter(e["outcome"] for e in pages)), "skipped_links": dict(skipped),
            "order": "políticas (D-167); después, categoría a categoría: su paginación y sus fichas (D-215)",
            "category_shapes": dict(state.category_shapes),
            "audit_pages": [{"url": url, **purpose,
                             "page": state.by_url.get(url) or state.finals.get(url)}
                            for url, purpose in state.targets.items()],
            "product_pages": sum(bool(e.get("product_signals")) for e in pages),
            "shapes": [{"shape": key, "captured": stats["captured"], "products": stats["products"],
                        "product_like": key in products,
                        "product_links": round(state.product_links(key, products), 2),
                        "pending": waiting[key]}
                       for key, stats in sorted(state.shapes.items(), key=lambda kv: -kv[1]["captured"])],
            "coverage": {"complete": not reasons and not pending, "reasons": reasons, "pending": len(pending),
                         "crawl_complete": crawl_complete},
            "pending": pending,
            "universe": {"urls": len(rows), "reached": dict(Counter(r["reached"] for r in rows)),
                         "in_sitemaps": dict(Counter(r["in_sitemaps"] for r in rows)),
                         "types": dict(Counter(r["type"] or "unclassified" for r in rows))},
        },
        "sitemaps": state.sitemaps, "universe": rows,
        "pages": pages, "stopped": stop["stopped"], "reservation": stop["reservation"],
        "finished_at": state.runs[-1].get("finished_at"),
    }
