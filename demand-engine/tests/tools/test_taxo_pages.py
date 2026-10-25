import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from demand_engine import pages, taxo

PAGE = """<html><head><title>Sábanas Coralina</title>
<script type="application/ld+json">{"@graph": [{"@type": "Product", "name": "Sábanas Coralina", "material": "Franela"},
 {"@type": "BreadcrumbList", "itemListElement": [{"name": "Hogar"}, {"name": "Sábanas"}]}]}</script>
<script>var oculto = 1;</script></head>
<body><h2>Composición</h2><p>100 % algodón</p></body></html>"""


def run(monkeypatch, *argv) -> None:
    monkeypatch.setattr(sys, "argv", ["taxo", *argv])
    taxo.main()


def test_category(fake_refs, monkeypatch, capsys):
    run(monkeypatch, "category", "zz-1-2")
    out = capsys.readouterr().out
    assert "zz-1-2 | Hogar > Ropa de cama > Sábanas" in out
    assert "Google (mapeo oficial): 2541 Casa > Ropa de cama > Sábanas" in out
    assert "madres: zz Hogar > zz-1 Ropa de cama" in out
    assert "- Tejido (fabric) [propio]: ['Franela']" in out


def test_ptd_and_errors(fake_refs, monkeypatch, capsys):
    run(monkeypatch, "ptd", "SHEET")
    assert "[product_details] thread_count | Número de hilos | ['200', '400']" in capsys.readouterr().out
    with pytest.raises(SystemExit, match="taxo: no existe la categoría nope"):
        run(monkeypatch, "category", "nope")
    with pytest.raises(SystemExit, match="taxo: no existe el PTD NOPE"):
        run(monkeypatch, "ptd", "NOPE")


def test_page_text_and_json_ld():
    lines = pages.text_lines(PAGE)
    assert "100 % algodón" in lines and not any("oculto" in l for l in lines)
    kinds = [n.get("@type") for data in pages.json_ld(PAGE) for n in pages.walk(data)]
    assert [k for k in kinds if k] == ["Product", "BreadcrumbList"]   # graph root and crumbs have no type


def test_page_facts(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(pages, "PAGES", tmp_path)
    (tmp_path / "caso.html").write_text(PAGE, encoding="utf-8")
    run(monkeypatch, "page", "facts", "caso", "composición")
    out = capsys.readouterr().out
    assert "PRODUCT: {'name': 'Sábanas Coralina', 'material': 'Franela'}" in out
    assert "BREADCRUMB: Hogar > Sábanas" in out and "[composición] Composición | 100 % algodón" in out
    with pytest.raises(SystemExit, match="taxo: no hay página congelada para otro"):
        run(monkeypatch, "page", "grep", "otro", "x")


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_page_fetch_with_the_capture_engine(tmp_path, monkeypatch, capsys):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            if self.path == "/robots.txt":
                status, body = 200, b"User-agent: *\nDisallow: /privado\n"
            elif self.path.startswith("/ficha"):
                status, body = 200, PAGE.encode("utf-8")
            else:
                status, body = 404, b"no"
            self.send_response(status)
            self.send_header("Content-Type", "text/plain" if self.path == "/robots.txt" else "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}"
    monkeypatch.setattr(pages, "PAGES", tmp_path)
    monkeypatch.setenv("CAPTURE_PROFILE", str(tmp_path / "chrome-profile"))
    monkeypatch.setenv("CAPTURE_CDP_PORT", "9297")
    try:
        run(monkeypatch, "page", "fetch", "caso", f"{base}/ficha#medidas")
        with pytest.raises(SystemExit, match="taxo: otro: excluida por robots.txt"):
            run(monkeypatch, "page", "fetch", "otro", f"{base}/privado/x")
    finally:
        httpd.shutdown()
    assert "caso: " in capsys.readouterr().out
    meta = json.loads((tmp_path / "caso.json").read_text(encoding="utf-8"))
    assert meta["method"] == "chrome-cdp" and meta["http_status"] == 200 and "Headless" not in meta["user_agent"]
    assert "100 % algodón" in (tmp_path / "caso.html").read_text(encoding="utf-8")   # the rendered DOM
    snapshot = json.loads((tmp_path / meta["snapshot"].split("/", 2)[2] / "meta.json").read_text(encoding="utf-8"))
    assert snapshot["outcome"] == "captured" and "actions" in snapshot and snapshot["legitimacy"]["robots"]["status"] == 200
    assert not (tmp_path / "otro.html").exists()
    refused = next((tmp_path / "otro").iterdir())
    assert json.loads((refused / "meta.json").read_text(encoding="utf-8"))["outcome"] == "disallowed"
    assert (refused / "robots.txt").exists()
