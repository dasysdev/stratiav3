import argparse
import gzip
import json
import shutil
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture import audit, cli, pages, profiles, spider
from capture.audit import AuditError

OG = '<meta property="og:type" content="product">'

HOME = """<!doctype html><html><head><meta charset=utf-8><title>Tienda</title></head><body>
<header><a href="/promo-envios">Envíos gratis</a><a href="/c/cojines">Cojines</a></header>
<main><a href="/p/uno">Uno</a></main>
<footer><ul><li><a href="/ayuda/envios">Envíos</a></li><li><a href="/ayuda/cambios">Cambios y devoluciones</a></li>
<li><a href="/contacto"><span>Contacto</span></a></li><li><a href="mailto:x@x.es">Escríbenos</a></li></ul></footer>
</body></html>"""

PRODUCT_HTML = """<!doctype html><html><head><meta charset=utf-8><title>Uno</title>%s</head><body>
<nav aria-label="Breadcrumb"><ol><li><a href="/">Inicio</a></li><li><a href="/c/cojines">Cojines</a></li>
<li><a href="/p/uno">Cojín uno</a></li></ol></nav><p>Composición: 100 %% algodón</p></body></html>""" % OG

PRODUCT_LD = """<!doctype html><html><head><meta charset=utf-8><title>Dos</title>
<link rel="canonical" href="/p/dos-c#x"><meta property="og:type" content="product">
<script type="application/ld+json">{"@context": "https://schema.org", "@graph": [{"@type": "BreadcrumbList",
"itemListElement": [{"@type": "ListItem", "position": 3, "name": "Cojín dos"},
{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "/"},
{"@type": "ListItem", "position": 2, "name": "Cojines", "item": {"@id": "/c/cojines#top"}}]}]}</script>
</head><body><p>Dos</p></body></html>"""

PRODUCT_BARE = "<!doctype html><html><head><title>Tres</title></head><body><p>Tres</p></body></html>"


def urlset(*urls) -> bytes:
    return ('<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + "".join(f"<url><loc>{u}</loc></url>" for u in urls) + "</urlset>").encode()


def test_policies_are_located_from_the_home_page():
    found = audit.locate_policies(HOME, "https://x.es/")
    assert found["shipping"]["url"] == "https://x.es/ayuda/envios"          # the footer first
    assert found["shipping"]["footer"] and found["shipping"]["candidates"][0]["url"] == "https://x.es/promo-envios"
    assert found["returns"] == {"status": "located", "url": "https://x.es/ayuda/cambios", "text": "Cambios y devoluciones",
                                "footer": True, "by": "text", "candidates": []}
    assert found["contact"]["url"] == "https://x.es/contacto"
    assert found["legal"] == {"status": "not_located"}                      # never replaced by another page
    other = audit.locate_policies('<a href="https://otra.es/aviso-legal">Legal</a>'
                                  '<a href="https://ayuda.x.es/aviso-legal">Información</a>', "https://www.x.es/")
    assert other["legal"]["url"] == "https://ayuda.x.es/aviso-legal" and other["legal"]["by"] == "url"


def test_breadcrumbs_and_the_immediate_category():
    html = audit.breadcrumbs(PRODUCT_HTML, "https://x.es/p/uno", None)
    assert html["status"] == "found" and html["source"] == "html" and html["category"] == "https://x.es/c/cojines"
    assert [c["name"] for c in html["trail"]] == ["Inicio", "Cojines", "Cojín uno"]
    ld = audit.breadcrumbs(PRODUCT_LD, "https://x.es/p/dos", "https://x.es/p/dos")
    assert ld["source"] == "json-ld" and ld["category"] == "https://x.es/c/cojines"
    assert [c["name"] for c in ld["trail"]] == ["Inicio", "Cojines", "Cojín dos"]
    assert audit.breadcrumbs(PRODUCT_BARE, "https://x.es/p/tres", None) == {"status": "none"}
    home_only = '<div class="breadcrumbs"><a href="/">Inicio</a><a href="/p/cuatro">Cuatro</a></div>'
    assert audit.breadcrumbs(home_only, "https://x.es/p/cuatro", None)["status"] == "no_category"


def test_sitemaps_and_coverage():
    parsed = audit._parse_sitemap(gzip.compress(urlset("https://x.es/p/uno")))
    assert parsed == {"kind": "urlset", "urls": ["https://x.es/p/uno"]}
    index = b'<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc> https://x.es/a.xml </loc></sitemap></sitemapindex>'
    assert audit._parse_sitemap(index) == {"kind": "index", "sitemaps": ["https://x.es/a.xml"]}
    assert audit.canonicals(PRODUCT_LD, "https://x.es/p/dos") == ["https://x.es/p/dos-c"]
    assert audit.canonicals(PRODUCT_BARE, "https://x.es/p/tres") == []


def test_the_audit_is_chosen_on_its_crawl(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "AUDITS", tmp_path)
    with pytest.raises(AuditError, match="primero, pages crawl"):
        audit.run("nueva", ["https://x.es/p/uno"])
    (tmp_path / "hecha").mkdir()
    crawl = {"site": "https://x.es", "profile": "audit-es", "runs": [{}], "pages": [], "reservation": None,
             "crawl": {"hosts": ["x.es"], "coverage": {"crawl_complete": True}}}
    (tmp_path / "hecha/crawl.json").write_text(json.dumps(crawl))
    with pytest.raises(AuditError, match="de otro sitio"):
        audit.run("hecha", ["https://y.es/p/dos"])
    (tmp_path / "hecha/audit.json").write_text("{}")
    with pytest.raises(AuditError, match="no se sustituye"):
        audit.run("hecha", ["https://x.es/p/uno"])


class Site:
    """A local shop: the routes of the audit test, and what each test changes (`extra`: path →
    (body, content type, headers))."""

    def __init__(self) -> None:
        self.sent: dict[str, bytes] = {}
        self.extra: dict[str, tuple] = {}
        site = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                routes = site.routes()
                body, kind, headers = routes.get(self.path, (b"no", "text/plain", {}))
                site.sent[self.path] = body
                self.send_response(200 if self.path in routes else 404)
                self.send_header("Content-Type", kind)
                self.send_header("Content-Length", str(len(body)))
                for name, value in headers.items():
                    self.send_header(name, value)
                self.end_headers()
                self.wfile.write(body)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.base = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        self.host = f"127.0.0.1_{self.httpd.server_address[1]}"
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def routes(self) -> dict:
        base, kind = self.base, "text/html; charset=utf-8"
        routes = {
            "/robots.txt": (f"User-agent: *\nDisallow: /privado\nSitemap: {base}/sitemap_index.xml\n".encode(), "text/plain"),
            "/sitemap_index.xml": (f'<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                   f'<sitemap><loc>{base}/sitemap-p.xml.gz</loc></sitemap>'
                                   f'<sitemap><loc>{base}/sitemap-gone.xml</loc></sitemap></sitemapindex>'.encode(),
                                   "application/xml"),
            "/sitemap-p.xml.gz": (gzip.compress(urlset(f"{base}/p/uno", f"{base}/p/dos-c", f"{base}/p/cuatro",
                                                       f"{base}/c/cojines?orden=precio", "https://otra.es/p/x")),
                                  "application/gzip"),
            "/": (HOME.encode(), kind), "/p/uno": (PRODUCT_HTML.encode(), kind),
            "/p/dos": (PRODUCT_LD.encode(), kind), "/p/tres": (PRODUCT_BARE.encode(), kind),
            "/p/cuatro": (PRODUCT_HTML.replace("Uno", "Cuatro").replace("/p/uno", "/p/cuatro").encode(), kind),
            "/c/cojines": ('<!doctype html><title>Cojines</title><a href="/p/uno">Uno</a><a href="/p/dos">Dos</a>'.encode(), kind),
        }
        for path in ("/c/cojines?orden=precio", "/ayuda/envios", "/ayuda/cambios", "/contacto"):
            routes[path] = (f"<!doctype html><title>{path}</title><p>{path}</p>".encode(), kind)
        routes = {path: (*route, {}) for path, route in routes.items()}
        return {**routes, **self.extra}

    def products(self) -> list[str]:
        return [f"{self.base}/p/uno", f"{self.base}/p/dos", f"{self.base}/p/tres"]

    def crawl(self, audit_id: str, engine) -> dict:
        return spider.run(audit_id, self.base + "/", browser=engine, min_interval_s=0, out=lambda *_: None)


@pytest.fixture(scope="module")
def engine(tmp_path_factory):
    from capture.browser import Browser

    browser = Browser(tmp_path_factory.mktemp("chrome") / "chrome-profile", port=9296)
    browser.start()
    yield browser
    browser.stop()


@pytest.fixture
def site(engine, tmp_path, monkeypatch):
    shop = Site()
    monkeypatch.setattr(audit, "AUDITS", tmp_path / "audits")
    monkeypatch.setattr(spider, "AUDITS", tmp_path / "audits")
    monkeypatch.setattr(profiles, "origin", lambda: {"ip": "192.0.2.1", "source": "RIPEstat"})
    shop.run = lambda audit_id: shop.crawl(audit_id, engine)
    yield shop
    shop.httpd.shutdown()


chrome = pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")


@pytest.mark.chrome
@chrome
def test_audit_on_the_crawl(site, tmp_path):
    crawled, base, sent = site.run("prueba"), site.base, site.sent
    folder = tmp_path / "audits/prueba"
    asked = dict(sent)
    record = audit.run("prueba")                                    # every product page of the universe
    assert sent == asked                                            # nothing asked for
    assert json.loads((folder / "audit.json").read_text(encoding="utf-8")) == json.loads(json.dumps(record))
    url = {p["id"]: p["url"].removeprefix(base) for p in crawled["pages"]}
    kinds = {url[p["id"]]: p["type"] for p in record["pages"]}
    assert kinds == {"/": "home", "/ayuda/envios": "policy", "/ayuda/cambios": "policy", "/contacto": "policy",
                     "/p/uno": "product", "/p/dos": "product", "/p/cuatro": "product", "/c/cojines": "category"}
    assert all(p["outcome"] == "captured" for p in record["pages"])
    assert record["policies"]["legal"] == {"status": "not_located"}
    assert record["policies"]["shipping"]["url"] == f"{base}/ayuda/envios"
    one, two, four = record["products"]
    assert one["category_page"] == two["category_page"] == four["category_page"]          # a shared category, once
    assert (one["breadcrumbs"]["source"], two["breadcrumbs"]["source"]) == ("html", "json-ld")
    assert [p["in_sitemaps"] for p in record["products"]] == [
        {"value": "yes", "by": "url"}, {"value": "yes", "by": "canonical"}, {"value": "yes", "by": "url"}]
    assert two["canonical"] == [f"{base}/p/dos-c"]
    assert record["sitemaps"]["complete"] and record["sitemaps"]["urls"] == 5
    gz = next(e for e in record["sitemaps"]["read"] if e["url"].endswith(".gz"))
    assert gz["gzip"] and (folder / gz["file"]).read_bytes() == sent["/sitemap-p.xml.gz"]   # as it came
    assert next(e for e in record["sitemaps"]["read"] if e["url"].endswith("gone.xml"))["status"] == 404
    assert (folder / "sites" / site.host / "robots.txt").read_text().startswith("User-agent: *")
    assert "100 % algodón" in audit.read("prueba", one["page"])
    meta = json.loads((folder / one_snapshot(record, one["page"]) / "meta.json").read_text(encoding="utf-8"))
    assert meta["profile"] == "audit-es" and meta["response_body"] == "original"
    assert set(meta["files"]) == {"response.html", "dom.html"}                # no MHTML (D-172)
    with pytest.raises(AuditError, match="no se reanuda"):
        spider.run("prueba", resume=True)

    shutil.copytree(folder, tmp_path / "audits/encargo", ignore=shutil.ignore_patterns("audit.json"))
    given = audit.run("encargo", site.products())                    # the product pages of the engagement
    assert [(p["url"].removeprefix(base), p.get("page") and url[p["page"]], p.get("in_universe"))
            for p in given["products"]] == [("/p/uno", "/p/uno", None), ("/p/dos", "/p/dos", None),
                                            ("/p/tres", None, "no")]                # not reached: not audited
    assert sorted(kinds.get(url[p["id"]]) for p in given["pages"]) == sorted(
        ["home", "policy", "policy", "policy", "product", "product", "category"])


def test_a_reservation_ends_the_command_with_an_error(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(audit, "AUDITS", tmp_path)
    reservation = {"where": "tdmrep.json", "source": "tdmrep.json", "url": "https://x.es/.well-known/tdmrep.json"}
    (tmp_path / "parada").mkdir()
    (tmp_path / "parada/crawl.json").write_text(json.dumps({"reservation": reservation}))
    with pytest.raises(SystemExit) as stop:
        cli.cmd_audit(argparse.Namespace(audit="parada", urls=[], from_file=None))
    assert stop.value.code == cli.RESERVED
    err = capsys.readouterr().err
    assert "reserva la minería de textos y datos" in err and "https://x.es/.well-known/tdmrep.json" in err
    assert not (tmp_path / "parada/audit.json").exists()


@pytest.mark.chrome
@chrome
def test_a_reservation_in_tdmrep_stops_the_crawl_before_capturing(site, tmp_path):
    site.extra["/.well-known/tdmrep.json"] = (b'[{"location": "/blog/*", "tdm-reservation": 1}]', "application/json", {})
    record = site.run("tdmrep")
    folder = tmp_path / "audits/tdmrep"
    assert record["pages"] == [] and not (folder / "pages").exists() and not (folder / "sitemaps").exists()
    assert not set(site.sent) - {"/robots.txt", "/.well-known/tdmrep.json", "/favicon.ico"}   # nothing else asked
    assert record["reservation"] == {
        "where": "tdmrep.json", "url": f"{site.base}/.well-known/tdmrep.json", "source": "tdmrep.json",
        "file": f"sites/{site.host}/tdmrep.json", "entries": [{"location": "/blog/*", "reservation": 1, "policy": None}]}
    assert record["stopped"].endswith("no se captura nada")
    with pytest.raises(audit.Reserved):
        audit.run("tdmrep")


@pytest.mark.chrome
@chrome
def test_a_reservation_in_the_home_page_stops_the_crawl(site, tmp_path):
    site.extra["/"] = (HOME.encode(), "text/html; charset=utf-8",
                       {"tdm-reservation": "1", "tdm-policy": "https://x.es/tdm-policy.json"})
    record = site.run("portada")
    home, = record["pages"]
    assert home["outcome"] == "reserved"
    snap = tmp_path / "audits/portada" / home["snapshot"]
    assert [f.name for f in snap.iterdir()] == ["meta.json"]          # the visit is recorded, its content is not kept
    assert "/sitemap_index.xml" not in site.sent and record["sitemaps"] is None
    assert record["reservation"] == {"where": home["id"], "url": f"{site.base}/", "source": "cabecera tdm-reservation",
                                     "header": "1", "meta": None, "policy": "https://x.es/tdm-policy.json",
                                     "snapshot": home["snapshot"]}
    assert record["stopped"].endswith("no se captura nada")


@pytest.mark.chrome
@chrome
def test_a_reservation_in_an_inner_page_stops_the_crawl_there(site, tmp_path):
    reserved = PRODUCT_LD.replace("<title>", '<meta name="tdm-reservation" content="1"><title>')
    site.extra["/p/dos"] = (reserved.encode(), "text/html; charset=utf-8", {})
    record = site.run("interior")
    two = next(p for p in record["pages"] if p["url"].endswith("/p/dos"))
    assert two["outcome"] == "reserved" and record["pages"][-1] is two
    assert [f.name for f in (tmp_path / "audits/interior" / two["snapshot"]).iterdir()] == ["meta.json"]
    assert record["reservation"] == {"where": two["id"], "url": f"{site.base}/p/dos", "source": "meta tdm-reservation",
                                     "header": None, "meta": "1", "policy": None, "snapshot": two["snapshot"]}
    assert record["sitemaps"]["complete"] and record["stopped"].endswith("lo pendiente no se captura")


def one_snapshot(record, page_id):
    return next(p["snapshot"] for p in record["pages"] if p["id"] == page_id)
