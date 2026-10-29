import argparse
import gzip
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture import audit, cli, pages, profiles
from capture.audit import AuditError

HOME = """<!doctype html><html><head><meta charset=utf-8><title>Tienda</title></head><body>
<header><a href="/promo-envios">Envíos gratis</a><a href="/c/cojines">Cojines</a></header>
<main><a href="/p/uno">Uno</a></main>
<footer><ul><li><a href="/ayuda/envios">Envíos</a></li><li><a href="/ayuda/cambios">Cambios y devoluciones</a></li>
<li><a href="/contacto"><span>Contacto</span></a></li><li><a href="mailto:x@x.es">Escríbenos</a></li></ul></footer>
</body></html>"""

PRODUCT_HTML = """<!doctype html><html><head><meta charset=utf-8><title>Uno</title></head><body>
<nav aria-label="Breadcrumb"><ol><li><a href="/">Inicio</a></li><li><a href="/c/cojines">Cojines</a></li>
<li><a href="/p/uno">Cojín uno</a></li></ol></nav><p>Composición: 100 % algodón</p></body></html>"""

PRODUCT_LD = """<!doctype html><html><head><meta charset=utf-8><title>Dos</title>
<link rel="canonical" href="/p/dos-c#x">
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
    complete = {"urls": {"https://x.es/p/uno"}, "complete": True}
    assert audit.in_sitemaps(complete, "https://x.es/p/uno#medidas", None) == \
        {"value": "yes", "match": "https://x.es/p/uno", "by": "url"}
    assert audit.in_sitemaps(complete, "https://x.es/p/x", "https://x.es/p/uno")["by"] == "url_final"
    assert audit.in_sitemaps(complete, "https://x.es/p/x-1", None, ["https://x.es/p/uno"])["by"] == "canonical"
    assert audit.canonicals(PRODUCT_LD, "https://x.es/p/dos") == ["https://x.es/p/dos-c"]
    assert audit.canonicals(PRODUCT_BARE, "https://x.es/p/tres") == []
    assert audit.in_sitemaps(complete, "https://x.es/p/dos", None) == {"value": "no"}
    assert audit.in_sitemaps({**complete, "complete": False}, "https://x.es/p/dos", None) == {"value": "undetermined"}


def test_an_audit_is_never_replaced(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "AUDITS", tmp_path)
    (tmp_path / "hecha").mkdir()
    with pytest.raises(AuditError, match="ya existe y no se sustituye"):
        audit.run("hecha", ["https://x.es/p/uno"], object())
    with pytest.raises(AuditError, match="de un solo sitio"):
        audit.run("nueva", ["https://x.es/p/uno", "https://y.es/p/dos"], object())
    assert not (tmp_path / "nueva").exists()


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
            "/sitemap-p.xml.gz": (gzip.compress(urlset(f"{base}/p/uno", f"{base}/p/dos-c")), "application/gzip"),
            "/": (HOME.encode(), kind), "/p/uno": (PRODUCT_HTML.encode(), kind),
            "/p/dos": (PRODUCT_LD.encode(), kind), "/p/tres": (PRODUCT_BARE.encode(), kind),
        }
        for path in ("/c/cojines", "/ayuda/envios", "/ayuda/cambios", "/contacto"):
            routes[path] = (f"<!doctype html><title>{path}</title><p>{path}</p>".encode(), kind)
        routes = {path: (*route, {}) for path, route in routes.items()}
        return {**routes, **self.extra}

    def products(self) -> list[str]:
        return [f"{self.base}/p/uno", f"{self.base}/p/dos", f"{self.base}/p/tres"]


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
    monkeypatch.setattr(profiles, "origin", lambda: {"ip": "192.0.2.1", "source": "RIPEstat"})
    shop.run = lambda audit_id: audit.run(audit_id, shop.products(), engine, pause_s=(0, 0), out=lambda *_: None)
    yield shop
    shop.httpd.shutdown()


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_audit_with_the_capture_engine(site, tmp_path):
    record, base, sent = site.run("prueba"), site.base, site.sent
    folder = tmp_path / "audits/prueba"
    assert json.loads((folder / "audit.json").read_text(encoding="utf-8")) == json.loads(json.dumps(record))
    kinds = {p["id"]: (p["type"], p["outcome"]) for p in record["pages"]}
    assert kinds == {"home": ("home", "captured"), "product-01": ("product", "captured"),
                     "product-02": ("product", "captured"), "product-03": ("product", "captured"),
                     "policy-shipping": ("policy", "captured"), "policy-returns": ("policy", "captured"),
                     "policy-contact": ("policy", "captured"), "category-01": ("category", "captured")}
    assert record["policies"]["legal"] == {"status": "not_located"}
    assert record["stopped"] is None and record["reservation"] is None
    assert record["policies"]["shipping"]["url"] == f"{base}/ayuda/envios"
    one, two, three = record["products"]
    assert one["category_page"] == two["category_page"] == "category-01"      # a shared category, once
    assert (one["breadcrumbs"]["source"], two["breadcrumbs"]["source"]) == ("html", "json-ld")
    assert three["breadcrumbs"] == {"status": "none"} and "category_page" not in three
    assert [p["in_sitemaps"].get("by", p["in_sitemaps"]["value"]) for p in record["products"]] == \
        ["url", "canonical", "no"]                                         # /p/dos is listed by its canonical
    assert two["canonical"] == [f"{base}/p/dos-c"] and three["canonical"] == []

    sitemaps = record["sitemaps"]
    assert sitemaps["declared"] and sitemaps["complete"] and sitemaps["urls"] == 2 and not sitemaps["pending"]
    gz = next(e for e in sitemaps["read"] if e["url"].endswith(".gz"))
    assert gz["gzip"] and (folder / gz["file"]).read_bytes() == sent["/sitemap-p.xml.gz"]   # as it came
    assert next(e for e in sitemaps["read"] if e["url"].endswith("gone.xml"))["status"] == 404
    host = site.host
    assert (folder / "sites" / host / "robots.txt").read_text().startswith("User-agent: *")

    assert "100 % algodón" in audit.read("prueba", "product-01")
    meta = json.loads((folder / one_snapshot(record, "product-01") / "meta.json").read_text(encoding="utf-8"))
    assert meta["profile"] == "audit-es" and meta["page_type"] == "product" and meta["response_body"] == "original"
    assert set(meta["robots_bots"]) == set(profiles.BOTS)


def test_a_reservation_ends_the_command_with_an_error(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(audit, "AUDITS", tmp_path)
    monkeypatch.setattr(pages, "engine_available", lambda: True)
    stopped = {"pages": [{"outcome": "pending"}], "policies": {}, "stopped": "auditoría parada: reserva TDM",
               "reservation": {"where": "tdmrep.json", "source": "tdmrep.json", "url": "https://x.es/.well-known/tdmrep.json"}}
    monkeypatch.setattr(audit, "run", lambda *a, **k: stopped)
    args = argparse.Namespace(audit="nueva", urls=["https://x.es/p/uno"], from_file=None, sitemap_files=1, sitemap_mb=1)
    with pytest.raises(SystemExit) as stop:
        cli.cmd_audit(args)
    assert stop.value.code == cli.RESERVED
    err = capsys.readouterr().err
    assert "reserva la minería de textos y datos" in err and "https://x.es/.well-known/tdmrep.json" in err


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_a_reservation_in_tdmrep_stops_the_audit_before_capturing(site, tmp_path):
    site.extra["/.well-known/tdmrep.json"] = (b'[{"location": "/blog/*", "tdm-reservation": 1}]', "application/json", {})
    record = site.run("tdmrep")
    folder = tmp_path / "audits/tdmrep"
    assert [(p["id"], p["outcome"]) for p in record["pages"]] == \
        [("home", "pending"), ("product-01", "pending"), ("product-02", "pending"), ("product-03", "pending")]
    assert not (folder / "pages").exists() and not (folder / "sitemaps").exists() and "sitemaps" not in record
    assert not set(site.sent) - {"/robots.txt", "/.well-known/tdmrep.json", "/favicon.ico"}   # nothing else asked
    assert record["reservation"] == {
        "where": "tdmrep.json", "url": f"{site.base}/.well-known/tdmrep.json", "source": "tdmrep.json",
        "file": f"sites/{site.host}/tdmrep.json", "entries": [{"location": "/blog/*", "reservation": 1, "policy": None}]}
    assert (folder / record["reservation"]["file"]).is_file()
    assert record["stopped"].endswith("no se captura nada")
    assert json.loads((folder / "audit.json").read_text(encoding="utf-8"))["reservation"]["where"] == "tdmrep.json"


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_a_reservation_in_the_home_page_stops_the_audit(site, tmp_path):
    site.extra["/"] = (HOME.encode(), "text/html; charset=utf-8",
                       {"tdm-reservation": "1", "tdm-policy": "https://x.es/tdm-policy.json"})
    record = site.run("portada")
    home = record["pages"][0]
    assert (home["id"], home["outcome"]) == ("home", "reserved")
    assert [p["outcome"] for p in record["pages"][1:]] == ["pending"] * 3
    snap = tmp_path / "audits/portada" / home["snapshot"]
    assert [f.name for f in snap.iterdir()] == ["meta.json"]          # the visit is recorded, its content is not kept
    assert "/sitemap_index.xml" not in site.sent and "sitemaps" not in record
    assert record["reservation"] == {"where": "home", "url": f"{site.base}/", "source": "cabecera tdm-reservation",
                                     "header": "1", "meta": None, "policy": "https://x.es/tdm-policy.json",
                                     "snapshot": home["snapshot"]}
    assert record["stopped"].endswith("no se captura nada")


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_a_reservation_in_an_inner_page_stops_the_audit_there(site, tmp_path):
    reserved = PRODUCT_LD.replace("<title>", '<meta name="tdm-reservation" content="1"><title>')
    site.extra["/p/dos"] = (reserved.encode(), "text/html; charset=utf-8", {})
    record = site.run("interior")
    assert {p["id"]: p["outcome"] for p in record["pages"]} == {
        "home": "captured", "product-01": "captured", "product-02": "reserved", "product-03": "pending",
        "policy-shipping": "pending", "policy-returns": "pending", "policy-contact": "pending",
        "category-01": "pending"}
    assert "100 % algodón" in audit.read("interior", "product-01")   # what came before is kept
    two = next(p for p in record["pages"] if p["id"] == "product-02")
    assert [f.name for f in (tmp_path / "audits/interior" / two["snapshot"]).iterdir()] == ["meta.json"]
    assert record["reservation"] == {"where": "product-02", "url": f"{site.base}/p/dos", "source": "meta tdm-reservation",
                                     "header": None, "meta": "1", "policy": None, "snapshot": two["snapshot"]}
    assert record["sitemaps"]["complete"] and record["stopped"].endswith("lo pendiente no se captura")


def one_snapshot(record, page_id):
    return next(p["snapshot"] for p in record["pages"] if p["id"] == page_id)
