import argparse
import gzip
import json
import threading
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture import audit, cli, pages, profiles, spider
from capture.audit import AuditError

HTML = "text/html; charset=utf-8"


def page(title: str, *hrefs: str, extra: str = "") -> bytes:
    body = "".join(h if h.startswith("<") else f'<a href="{h}">{h}</a>' for h in hrefs)
    return f"<!doctype html><html><head><meta charset=utf-8><title>{title}</title></head><body>{body}{extra}</body></html>".encode()


def test_links_carry_nofollow_and_follow_base_href():
    doc = ('<head><base href="/tienda/"></head><a href="p/uno" rel="nofollow noopener">Uno</a>'
           '<base href="/otra/"><a href="https://x.es/dos">Dos</a>')
    found = audit.links(doc, "https://x.es/inicio")
    assert [(l["url"], l["nofollow"]) for l in found] == [("https://x.es/tienda/p/uno", True), ("https://x.es/dos", False)]


def test_what_the_spider_follows():
    assert spider.normal("HTTPS://X.es?a=1#top") == "https://x.es/"
    assert spider.normal("https://x.es/c/sabanas#m") == "https://x.es/c/sabanas"
    hosts = {"x.es", "www.x.es"}
    assert spider.skip_reason("https://www.x.es/c/sabanas", hosts) is None
    assert spider.skip_reason("http://x.es/p/uno.html", hosts) is None
    assert spider.skip_reason("https://otra.es/", hosts) == "external"
    assert spider.skip_reason("https://cdn.x.es/a", hosts) == "external"
    assert spider.skip_reason("https://x.es/c?page=2", hosts) is None          # pagination (D-204)
    assert spider.skip_reason("https://x.es/c?pagina=3#top", hosts) is None
    assert spider.skip_reason("https://x.es/c?page=2&color=rojo", hosts) == "query"
    assert spider.skip_reason("https://x.es/c?page=dos", hosts) == "query"
    assert spider.skip_reason("https://x.es/c?q=Cama+90", hosts) == "query"     # facets
    assert spider.skip_reason("https://x.es/catalogo.PDF", hosts) == "resource"
    assert spider.skip_reason("whatsapp://send?text=x", hosts) == "other"
    assert spider.normal("https://X.es/c?page=2#top") == "https://x.es/c?page=2"


def test_the_shape_of_a_url():
    assert spider.shape("https://x.es/cojines-con-relleno-018-azul-p-5777-92767.html") == "/W-p-N.html"
    assert spider.shape("https://x.es/fundas-camas-180-200-cm-c-526") == "/W-c-N"
    assert spider.shape("https://x.es/sabanas-c-487?page=2") == "/W-c-N?page"
    assert spider.shape("https://x.es/products/funda-azul") == "/products/W"
    assert spider.shape("https://x.es/collections/sabanas") == "/collections/W"
    assert spider.shape("https://x.es/es/ropa-de-cama/12345") == "/es/W/N"
    assert spider.shape("https://x.es/") == "/"
    assert spider.shape("https://x.es/info-a") == spider.shape("https://x.es/contacto") == "/W"   # a marker needs numbers


def test_the_signals_of_a_product_page():
    ld = '<script type="application/ld+json">%s</script>'
    assert spider.product_signals('<meta property="og:type" content="product">'
                                  + ld % '{"@context": "https://schema.org", "@type": "Product", "name": "x"}') == ["og:type", "json-ld"]
    assert spider.product_signals(ld % '{"@graph": [{"@type": "WebPage"}, {"@type": ["Product"]}]}') == ["json-ld"]
    assert spider.product_signals('<div itemscope itemtype="https://schema.org/Product"><span itemprop="name">x</span></div>') == ["microdata"]
    listing = (ld % '{"@type": "ItemList", "itemListElement": [{"@type": "Product"}, {"@type": "Product"}]}'
               + '<ul itemscope itemtype="https://schema.org/ItemList"><li itemprop="itemListElement" itemscope'
               ' itemtype="https://schema.org/Product"></li></ul>')
    assert spider.product_signals(listing) == []                               # the products of a listing
    assert spider.product_signals(ld % '[{"@type": "Product"}, {"@type": "Product"}, {"@type": "Product"}]') == []
    assert spider.product_signals('<meta property="og:type" content="website">') == []


def test_product_pages_go_first():
    state, x = spider._State(), "https://x.es"
    state.replay({"run": {"run": 1, "start": f"{x}/"}})

    def visit(why, url, product=False, found=()):
        assert state.next() == (url, why)
        entry = {"id": f"page-{len(state.entries) + 1:05d}", "url": url, "depth": 0, "outcome": "captured",
                 "shape": spider.shape(url), "chosen_as": why, "snapshot": url,
                 **({"product_signals": ["og:type"]} if product else {})}
        state.replay({"page": entry, "found": [[f"{x}{f}", False] for f in found]})

    visit("probe", f"{x}/", found=["/a-c-1", "/b-c-2", "/uno-p-1.html", "/info"])
    visit("probe", f"{x}/a-c-1", found=["/dos-p-2.html", "/tres-p-3.html", "/a-c-1?page=2"])
    visit("probe", f"{x}/uno-p-1.html", product=True)
    visit("product", f"{x}/dos-p-2.html", product=True)
    visit("product", f"{x}/tres-p-3.html", product=True)
    visit("probe", f"{x}/info")                      # a shape not seen yet, once
    visit("probe", f"{x}/a-c-1?page=2", found=["/cuatro-p-4.html"])
    visit("product", f"{x}/cuatro-p-4.html", product=True)
    assert state.next() == (f"{x}/b-c-2", "other")
    state.put_back(f"{x}/b-c-2", "other")
    entry = state.entries["page-00008"]
    assert state.target(f"{x}/b-c-2", {"category_of": "page-00008"}, entry)          # a page of D-167
    assert not state.target(f"{x}/b-c-2", {"category_of": "page-00009"}, entry)      # once
    assert state.target("https://ayuda.x.es/envios", {"policy": "shipping", "skip": "external"}, entry)
    assert state.next() == (f"{x}/b-c-2", "category")
    # category by category: its pagination, then its product pages (D-204, T-093)
    visit("category", f"{x}/b-c-2", found=["/cinco-p-5.html", "/b-c-2?page=2", "/c-c-3"])
    assert state.group == f"{x}/b-c-2"
    visit("pagination", f"{x}/b-c-2?page=2", found=["/seis-p-6.html", "/b-c-2?page=3"])
    visit("pagination", f"{x}/b-c-2?page=3")                   # lists no product page: the pagination ends
    visit("listed", f"{x}/cinco-p-5.html", product=True)
    visit("listed", f"{x}/seis-p-6.html", product=True)
    assert state.next() == (f"{x}/c-c-3", "category")           # then the next category, by its shape
    state.put_back(f"{x}/c-c-3", "category")
    state.target(f"{x}/a-c-1", {"category_of": "page-00014"}, entry)   # captured before it was known as one
    assert state.next() == (f"{x}/c-c-3", "category")          # a-c-1 was gone through first: nothing was left
    assert state.events == [f"{x}/a-c-1"] and f"{x}/a-c-1" in state.grouped
    assert {k: v for k, v in state.shapes["/W-p-N.html"].items() if k != "links"} == {"captured": 6, "products": 6}
    assert state.product_links("/W-c-N", {"/W-p-N.html"}) == 1.5        # /a-c-1 found two product pages, /b-c-2 one
    assert state.product_like("/W-p-N.html") and not state.product_like("/W-c-N")


def test_the_journal_rebuilds_what_is_pending():
    state = spider._State()
    state.replay({"run": {"run": 1, "start": "https://x.es/"}})
    state.replay({"page": {"id": "page-00001", "url": "https://x.es/", "depth": 0, "outcome": "captured",
                           "url_final": "https://x.es/", "snapshot": "s1"},
                  "found": [["https://x.es/a", False], ["https://x.es/b", True], ["https://x.es/c", False]]})
    state.replay({"page": {"id": "page-00002", "url": "https://x.es/a", "depth": 1, "outcome": "captured",
                           "url_final": "https://x.es/c", "snapshot": "s2"}, "found": []})
    state.replay({"page": {"id": "page-00003", "url": "https://x.es/b", "depth": 1, "outcome": "blocked",
                           "snapshot": "s3"}, "found": []})
    state.replay({"run_end": {"run": 1, "finished_at": "t"}})
    assert state.discovered["https://x.es/b"] == {"n": 2, "depth": 1, "from": "page-00001", "nofollow": True}
    assert state.pending() == ["https://x.es/b"]           # the blocked page first; /c was reached by a redirect
    assert state.next() == ("https://x.es/b", "retry") and state.next() is None
    assert state.runs == [{"run": 1, "start": "https://x.es/", "finished_at": "t"}]


def test_the_universe_and_its_types():
    state, x = spider._State(), "https://x.es"
    state.hosts = {"x.es"}
    state.replay({"run": {"run": 1, "start": f"{x}/", "started_at": "t"}})

    def visit(n, url, found=(), targets=(), why="probe", **extra):
        assert state.next() == (url, why)
        entry = {"id": f"page-{n:05d}", "url": url, "depth": None if why == "sitemap" else min(n - 1, 1),
                 "outcome": "captured", "url_final": url, "shape": spider.shape(url), "chosen_as": why,
                 "snapshot": f"s{n}", **extra}
        state.replay({"page": entry, "found": [[f"{x}{f}", False] for f in found], "targets": list(targets)})

    visit(1, f"{x}/", found=["/envios", "/uno-p-1.html", "/info"], targets=[[f"{x}/envios", {"policy": "shipping"}]])
    visit(2, f"{x}/envios", why="audit")
    visit(3, f"{x}/uno-p-1.html", found=["/raro-p-9.html", "/cat-c-1"], product_signals=["og:type"],
          canonical=[f"{x}/uno"], targets=[[f"{x}/cat-c-1", {"category_of": "page-00003"}]])
    visit(4, f"{x}/cat-c-1", found=["/dos-p-2.html"], why="category")
    visit(5, f"{x}/dos-p-2.html", product_signals=["json-ld"], why="listed")
    visit(6, f"{x}/raro-p-9.html", why="product")         # a product shape, no product signals
    visit(7, f"{x}/info", why="other")                   # the shape of /envios
    assert state.next() is None                           # the sitemaps are not read yet
    state.replay({"sitemaps": {"declared": True, "read": [], "pending": [], "complete": True,
                               "urls": [f"{x}/uno", f"{x}/dos-p-2.html", f"{x}/solo-p-4.html",
                                        f"{x}/cat-c-1?orden=precio", "https://otra.es/y"]}})
    visit(8, f"{x}/solo-p-4.html", why="sitemap", source="sitemaps", product_signals=["og:type"])
    assert state.next() == (f"{x}/cat-c-1?orden=precio", "sitemap")    # any query, from the sitemaps
    state.put_back(f"{x}/cat-c-1?orden=precio", "sitemap")
    assert state.shapes["/W-p-N.html"]["captured"] == 3                 # the page of the sitemaps teaches nothing

    record = spider._manifest("a", x, state, state.hosts, 100, {"stopped": None, "reservation": None,
                                                                 "interrupted": False, "limit": False}, 1)
    rows = {r["url"].removeprefix(x): {k: v for k, v in r.items() if k != "url"} for r in record["universe"]}
    assert rows == {
        "/": {"page": "page-00001", "outcome": "captured", "reached": "yes", "in_sitemaps": "no", "type": "home"},
        "/envios": {"page": "page-00002", "outcome": "captured", "reached": "yes", "in_sitemaps": "no", "type": "policy"},
        "/uno-p-1.html": {"page": "page-00003", "outcome": "captured", "reached": "yes", "in_sitemaps": "yes",
                          "sitemaps_by": "canonical", "type": "product"},
        "/cat-c-1": {"page": "page-00004", "outcome": "captured", "reached": "yes", "in_sitemaps": "no", "type": "category"},
        "/dos-p-2.html": {"page": "page-00005", "outcome": "captured", "reached": "yes", "in_sitemaps": "yes", "type": "product"},
        "/raro-p-9.html": {"page": "page-00006", "outcome": "captured", "reached": "yes", "in_sitemaps": "no", "type": None},
        "/info": {"page": "page-00007", "outcome": "captured", "reached": "yes", "in_sitemaps": "no", "type": "other"},
        "/solo-p-4.html": {"page": "page-00008", "outcome": "captured", "reached": "no", "in_sitemaps": "yes", "type": "product"},
        "/cat-c-1?orden=precio": {"page": None, "outcome": "pending", "reached": "no", "in_sitemaps": "yes", "type": None},
        "https://otra.es/y": {"page": None, "outcome": "skipped", "reached": "no", "in_sitemaps": "yes", "type": None,
                              "skip": "external"}}
    coverage = record["crawl"]["coverage"]
    assert coverage["crawl_complete"] and not coverage["complete"] and coverage["pending"] == 1
    assert record["crawl"]["pending"] == [f"{x}/cat-c-1?orden=precio"]
    assert record["crawl"]["universe"]["reached"] == {"yes": 7, "no": 3}

    state.replay({"page": {"id": "page-00009", "url": f"{x}/nueva", "depth": 1, "outcome": "failed", "snapshot": "s9"}})
    state.discover(f"{x}/otra", 2, "page-00009", False)
    rows = {r["url"]: r for r in spider.universe(state, {"/W-p-N.html"}, crawl_complete=False)}
    assert rows[f"{x}/solo-p-4.html"]["reached"] == "undetermined"      # an absence needs the whole crawl
    assert rows[f"{x}/otra"] == {"url": f"{x}/otra", "page": None, "outcome": "pending", "reached": "yes",
                                 "in_sitemaps": "no", "type": None}


class Shop:
    """A local shop for the spider: what each path answers (`routes`) and how often it was asked."""

    def __init__(self) -> None:
        self.asked: Counter = Counter()
        self.routes: dict[str, tuple] = {}
        shop = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                shop.asked[self.path] += 1
                if self.headers.get("Host", "").startswith("localhost") and self.path == "/":
                    status, body, headers = 301, b"", {"Location": shop.base + "/"}   # x.es → www.x.es
                else:
                    status, body, headers = shop.answer(self.path)
                self.send_response(status)
                for name, value in {"Content-Type": HTML, "Content-Length": str(len(body)), **headers}.items():
                    self.send_header(name, value)
                self.end_headers()
                self.wfile.write(body)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.base = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def answer(self, path: str) -> tuple:
        if path in self.routes:
            return self.routes[path]
        if path.startswith("/f/"):   # facets without end, in the path: each page links to the next
            n = int(path.rsplit("/", 1)[1])
            return 200, page(f"Faceta {n}", f"/f/{n + 1}"), {}
        return 404, b"no", {}

    def visits(self) -> Counter:
        return Counter({p: n for p, n in self.asked.items()
                        if p not in ("/robots.txt", "/.well-known/tdmrep.json", "/favicon.ico")})


def shop_routes(shop: Shop) -> dict:
    js_link = "<script>const a = document.createElement('a'); a.href = '/solo-js'; document.body.append(a)</script>"
    return {
        "/robots.txt": (200, b"User-agent: *\nDisallow: /privado\n", {"Content-Type": "text/plain"}),
        "/": (200, page("Inicio", "/a", '<a href="/b" rel="nofollow">B</a>', "/privado/x", "/viejo", "/c", "/a#medidas",
                        "https://otra.es/x", "/catalogo.pdf", "mailto:hola@x.es", extra=js_link), {}),
        "/a": (200, page("A", "/", "/d", f"{shop.base}/e"), {}),
        "/b": (200, page("B", "/e"), {}),
        "/c": (200, page("Categoría", "/c?page=2", "/c?color=rojo"), {}),
        "/c?page=2": (200, page("Categoría, página 2", "/c", "/c?page=1&color=rojo"), {}),
        "/viejo": (301, b"", {"Location": "/d"}),
        "/d": (200, page("D"), {}),
        "/e": (200, page("E", "/f/1"), {}),
    }


@pytest.fixture(scope="module")
def engine(tmp_path_factory):
    from capture.browser import Browser

    browser = Browser(tmp_path_factory.mktemp("chrome") / "chrome-profile", port=9295)
    browser.start()
    yield browser
    browser.stop()


@pytest.fixture
def shop(engine, tmp_path, monkeypatch):
    shop = Shop()
    shop.routes.update(shop_routes(shop))
    shop.origins = []
    monkeypatch.setattr(audit, "AUDITS", tmp_path / "audits")
    monkeypatch.setattr(spider, "AUDITS", tmp_path / "audits")

    def origin():
        shop.origins.append(1)
        return {"ip": "192.0.2.1", "source": "RIPEstat"}

    monkeypatch.setattr(profiles, "origin", origin)
    shop.crawl = lambda audit_id, **kw: spider.run(audit_id, kw.pop("start", shop.base + "/"), browser=engine,
                                                   min_interval_s=0, out=kw.pop("out", lambda *_: None), **kw)
    yield shop
    shop.httpd.shutdown()


def by_path(record, base) -> dict:
    return {p["url"].removeprefix(base): p for p in record["pages"]}


chrome = pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")


@pytest.mark.chrome
@chrome
def test_the_spider_crawls_and_captures_a_site(shop, tmp_path):
    shop.routes["/e"] = (200, page("E"), {})   # a finite site
    record, base = shop.crawl("arana"), shop.base
    folder = tmp_path / "audits/arana"
    assert json.loads((folder / "crawl.json").read_text(encoding="utf-8")) == json.loads(json.dumps(record))
    found = by_path(record, base)
    assert {path: p["outcome"] for path, p in found.items()} == {
        "/": "captured", "/a": "captured", "/b": "captured", "/privado/x": "disallowed", "/viejo": "captured",
        "/c": "captured", "/c?page=2": "captured", "/e": "captured"}
    assert found["/viejo"]["url_final"] == f"{base}/d"           # /d, reached by the redirect, is not asked again
    assert found["/b"]["found_by_nofollow"] and found["/b"]["found_from"] == found["/"]["id"]
    assert found["/e"]["depth"] == 2
    visits = shop.visits()
    assert set(visits.values()) == {1}                          # each page once
    assert "/solo-js" not in visits and "/privado/x" not in visits and "/catalogo.pdf" not in visits
    assert [p for p in visits if "?" in p] == ["/c?page=2"]     # pagination, no facets (D-204)

    crawl = record["crawl"]
    assert crawl["coverage"] == {"complete": True, "reasons": [], "pending": 0, "crawl_complete": True}
    assert crawl["pending"] == [] and record["sitemaps"]["complete"] and record["sitemaps"]["urls"] == 0
    assert crawl["skipped_links"] == {"external": 1, "resource": 1, "query": 2}   # ?color=rojo, ?page=1&color=rojo
    assert crawl["hosts"] == [base.split("//")[1]] and record["stopped"] is None and record["reservation"] is None

    home = folder / found["/"]["snapshot"]
    rows = json.loads(gzip.decompress((home / "links.json.gz").read_bytes()))
    assert [r["url"].removeprefix(base) for r in rows if r["nofollow"]] == ["/b"]
    assert {r["url"]: r["skip"] for r in rows if r["skip"]} == {
        "https://otra.es/x": "external", f"{base}/catalogo.pdf": "resource"}
    assert found["/"]["links"] == {"total": 8, "nofollow": 1, "new": 5, "skipped": {"external": 1, "resource": 1}}

    assert len(shop.origins) == 1                                # the origin, once per run
    meta = json.loads((home / "meta.json").read_text(encoding="utf-8"))
    assert meta["profile"] == "audit-es" and meta["request_context"]["origin"] == {"ip": "192.0.2.1", "source": "RIPEstat"}
    assert set(meta["files"]) == {"response.html", "dom.html"}
    assert record["runs"][0]["origin"]["ip"] == "192.0.2.1"
    assert "Inicio" in audit.read("arana", found["/"]["id"])     # an audit like any other

    with pytest.raises(AuditError, match="no queda nada"):
        shop.crawl("arana", start=None, resume=True)


@pytest.mark.chrome
@chrome
def test_facets_without_end_stop_at_the_limit(shop):
    record = shop.crawl("tope", limit=8)
    crawl = record["crawl"]
    assert crawl["processed"] == 8 and not crawl["coverage"]["complete"]
    assert crawl["coverage"]["reasons"] == [{"reason": "limit", "detail": "tope de 8 URL"}]
    assert crawl["pending"] == [f"{shop.base}/f/1"] and crawl["coverage"]["pending"] == 1

    more = shop.crawl("tope", start=None, resume=True, limit=10)   # the limit raised, it goes on
    assert more["crawl"]["processed"] == 10 and more["crawl"]["pending"] == [f"{shop.base}/f/3"]
    assert more["crawl"]["discovered"] == record["crawl"]["discovered"] + 2   # /f/3 and /f/4
    assert set(shop.visits().values()) == {1} and len(more["runs"]) == 2


@pytest.mark.chrome
@chrome
def test_the_host_of_the_home_page_after_its_redirect(shop):
    shop.routes["/e"] = (200, page("E"), {})
    start = shop.base.replace("127.0.0.1", "localhost") + "/"
    record = shop.crawl("redirige", start=start)
    assert record["pages"][0]["url_final"] == shop.base + "/"
    assert record["crawl"]["hosts"] == sorted([start.split("/")[2], shop.base.split("/")[2]])
    assert record["crawl"]["processed"] == 8 and record["crawl"]["coverage"]["complete"]


def test_the_crawl_command(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(audit, "AUDITS", tmp_path)
    monkeypatch.setattr(pages, "engine_available", lambda: True)
    budget = {"sitemap_files": 1, "sitemap_mb": 1}
    args = argparse.Namespace(audit="nueva", url=None, resume=False, max_urls=None, **budget)
    with pytest.raises(AuditError, match="--resume"):
        cli.cmd_crawl(args)
    (tmp_path / "hecha").mkdir()
    with pytest.raises(AuditError, match="ya existe"):
        cli.cmd_crawl(argparse.Namespace(audit="hecha", url="https://x.es/", resume=False, max_urls=None, **budget))
    stopped = {"crawl": {"processed": 1, "discovered": 3, "outcomes": {"reserved": 1},
                         "coverage": {"complete": False, "reasons": [{"reason": "reserved"}], "pending": 2}},
               "reservation": {"where": "page-00001", "source": "meta tdm-reservation", "url": "https://x.es/"}}
    monkeypatch.setattr(spider, "run", lambda *a, **k: stopped)
    with pytest.raises(SystemExit) as stop:
        cli.cmd_crawl(argparse.Namespace(audit="nueva", url="https://x.es/", resume=False, max_urls=None, **budget))
    assert stop.value.code == cli.RESERVED
    printed = capsys.readouterr()
    assert "cobertura incompleta (reserved; 2 pendientes)" in printed.out and "reserva la minería" in printed.err


@pytest.mark.chrome
@chrome
def test_an_interrupted_crawl_is_resumed_without_asking_again(shop, tmp_path):
    shop.routes["/e"] = (200, page("E"), {})
    seen = []

    def stop_after_three(line):
        if line.startswith("page-"):
            seen.append(line)
            if len(seen) == 3:
                raise KeyboardInterrupt

    first = shop.crawl("reanuda", out=stop_after_three)
    assert first["crawl"]["processed"] == 3 and first["runs"][0]["interrupted"]
    assert {"reason": "interrupted", "detail": "interrumpido; se reanuda con --resume"} in first["crawl"]["coverage"]["reasons"]

    # A hard stop: the journal line of the third page is cut short, its snapshot is there
    folder = tmp_path / "audits/reanuda"
    lines = (folder / "crawl.jsonl").read_text(encoding="utf-8").splitlines()
    third = next(i for i, l in enumerate(lines) if '"page-00003"' in l and l.startswith('{"page"'))
    cut = "\n".join(lines[:third]) + "\n" + lines[third][:40]
    (folder / "crawl.jsonl").write_text(cut, encoding="utf-8")

    record = shop.crawl("reanuda", start=None, resume=True)
    assert record["crawl"]["coverage"]["complete"] and record["crawl"]["processed"] == 8
    assert set(shop.visits().values()) == {1}                 # nothing asked twice
    third_page = next(p for p in record["pages"] if p["id"] == "page-00003")
    assert third_page["recovered"] and third_page["outcome"] == first["pages"][2]["outcome"]
    assert len(shop.origins) == 2 and [r["sites"] for r in record["runs"]] == ["sites", "resumes/02"]
    assert (folder / "resumes/02").is_dir()


@pytest.mark.chrome
@chrome
def test_a_reservation_stops_the_crawl_and_it_is_not_resumed(shop):
    shop.routes["/b"] = (200, page("B", "/e"), {"tdm-reservation": "1"})
    record = shop.crawl("reserva")
    found = by_path(record, shop.base)
    assert found["/b"]["outcome"] == "reserved" and record["reservation"]["where"] == found["/b"]["id"]
    assert record["reservation"]["source"] == "cabecera tdm-reservation"
    assert record["stopped"].endswith("lo pendiente no se captura")
    assert [r["reason"] for r in record["crawl"]["coverage"]["reasons"]] == ["reserved"]
    with pytest.raises(AuditError, match="reserva TDM"):
        shop.crawl("reserva", start=None, resume=True)


def store_routes() -> dict:
    """A shop where breadth first meets the categories and the other pages long before the product
    pages: policies in the footer, categories with a second page, and product pages (og:type) with
    breadcrumbs that link a product page of the next category."""
    home = page("Inicio", *[f"/cat-{c}-c-{c}" for c in (1, 2, 3)], *[f"/info-{i}" for i in "abcdef"], "/ofertas-c-9",
                "/cat-1-c-1", "/textil-c-7",
                extra='<footer><a href="/envios">Envíos</a><a href="/devoluciones">Devoluciones</a>'
                      '<a href="/contacto">Contacto</a><a href="/aviso-legal">Aviso legal</a></footer>')
    routes = {"/robots.txt": (200, b"User-agent: *\nAllow: /\n", {"Content-Type": "text/plain"}), "/": (200, home, {})}
    for c in (1, 2, 3):
        routes[f"/cat-{c}-c-{c}"] = (200, page(f"Cat {c}", f"/ficha-{c}1-p-{c}1-1.html", f"/ficha-{c}2-p-{c}2-1.html",
                                               f"/cat-{c}-c-{c}?page=2", f"/cat-{c}-c-{c}?orden=precio"), {})
        routes[f"/cat-{c}-c-{c}?page=2"] = (200, page(f"Cat {c}, 2", f"/ficha-{c}3-p-{c}3-1.html"), {})
        for k in (1, 2, 3):
            other = c % 3 + 1
            crumbs = (f'<nav class="breadcrumb"><a href="/">Inicio</a><a href="/textil-c-7">Textil</a>'
                      f'<a href="/cat-{c}-c-{c}">Cat {c}</a></nav>')
            routes[f"/ficha-{c}{k}-p-{c}{k}-1.html"] = (200, page(f"Ficha {c}{k}", f"/ficha-{other}{k}-p-{other}{k}-1.html",
                                                                  extra=crumbs + '<meta property="og:type" content="product">'), {})
    routes["/textil-c-7"] = (200, page("Textil", *[f"/cat-{c}-c-{c}" for c in (1, 2, 3)]), {})
    routes["/ofertas-c-9"] = (200, page("Ofertas"), {})          # a category in no breadcrumbs
    for path in [f"/info-{i}" for i in "abcdef"] + ["/envios", "/devoluciones", "/contacto", "/aviso-legal"]:
        routes[path] = (200, page(path), {})
    return routes


@pytest.mark.chrome
@chrome
def test_product_pages_are_captured_first(shop):
    shop.routes = store_routes()
    record = shop.crawl("fichas", limit=22)
    order = [(p["url"].removeprefix(shop.base), p["chosen_as"]) for p in record["pages"]]
    products = [p for p in record["pages"] if p.get("product_signals")]
    assert order[:5] == [("/", "probe"), ("/envios", "audit"), ("/devoluciones", "audit"), ("/contacto", "audit"),
                         ("/aviso-legal", "audit")]                       # the policies of D-167 first
    assert len(products) == 9                                   # breadth first would capture none in 22
    assert order[5:] == [                                       # category by category: pagination, then its products
        ("/cat-1-c-1", "probe"), ("/ficha-11-p-11-1.html", "probe"),    # known as a category by these breadcrumbs
        ("/cat-1-c-1?page=2", "pagination"), ("/ficha-12-p-12-1.html", "listed"), ("/ficha-13-p-13-1.html", "listed"),
        ("/textil-c-7", "category"),
        ("/cat-2-c-2", "category"), ("/cat-2-c-2?page=2", "pagination"), ("/ficha-21-p-21-1.html", "listed"),
        ("/ficha-22-p-22-1.html", "listed"), ("/ficha-23-p-23-1.html", "listed"),
        ("/cat-3-c-3", "category"), ("/cat-3-c-3?page=2", "pagination"), ("/ficha-31-p-31-1.html", "listed"),
        ("/ficha-32-p-32-1.html", "listed"), ("/ficha-33-p-33-1.html", "listed"),
        ("/ofertas-c-9", "category")]
    assert record["crawl"]["category_shapes"] == {"/W-c-N": 4}            # categories found in breadcrumbs
    assert not [o for o in order if o[0] in ("/info-b", "/info-c", "/info-d")]   # the other pages wait
    targets = {t["url"].removeprefix(shop.base): t for t in record["crawl"]["audit_pages"]}
    assert targets["/envios"] == {"url": f"{shop.base}/envios", "policy": "shipping", "page": "page-00002"}
    assert targets["/textil-c-7"]["category_of"] == targets["/cat-1-c-1"]["category_of"] and targets["/textil-c-7"]["page"]
    shapes = {s["shape"]: s for s in record["crawl"]["shapes"]}
    assert shapes["/W-p-N.html"]["product_like"] and shapes["/W-p-N.html"]["products"] == 9
    assert record["crawl"]["product_pages"] == 9
    assert set(shop.visits().values()) == {1}

    rest = shop.crawl("fichas", start=None, resume=True, limit=200)   # the order is rebuilt from the journal
    assert rest["crawl"]["coverage"]["complete"] and rest["crawl"]["product_pages"] == 9
    assert rest["crawl"]["audit_pages"] == record["crawl"]["audit_pages"]
    assert set(shop.visits().values()) == {1} and "/cat-1-c-1?orden=precio" not in shop.visits()


@pytest.mark.chrome
@chrome
def test_a_crawl_resumed_in_a_category_goes_on_with_it(shop):
    shop.routes = store_routes()
    first = shop.crawl("en-categoria", limit=13)
    assert [(p["url"].removeprefix(shop.base), p["chosen_as"]) for p in first["pages"][-2:]] == \
        [("/cat-2-c-2", "category"), ("/cat-2-c-2?page=2", "pagination")]
    more = shop.crawl("en-categoria", start=None, resume=True, limit=16)
    assert [(p["url"].removeprefix(shop.base), p["chosen_as"]) for p in more["pages"][13:]] == \
        [("/ficha-21-p-21-1.html", "listed"), ("/ficha-22-p-22-1.html", "listed"), ("/ficha-23-p-23-1.html", "listed")]
    assert set(shop.visits().values()) == {1}
