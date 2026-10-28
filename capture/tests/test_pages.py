import gzip
import hashlib
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture import cli, pages
from capture.pages import PageError

PAGE = """<html><head><title>Sábanas Coralina</title>
<script type="application/ld+json">{"@graph": [{"@type": "Product", "name": "Sábanas Coralina", "material": "Franela"},
 {"@type": "BreadcrumbList", "itemListElement": [{"name": "Hogar"}, {"name": "Sábanas"}]}]}</script>
<script>var oculto = 1;</script></head>
<body><h2>Composición</h2><p>100 % algodón</p></body></html>"""


@pytest.fixture
def store(tmp_path, monkeypatch):
    monkeypatch.setattr(pages, "PAGES", tmp_path)
    return tmp_path


def snapshot(store, case_id, name="20261028T100000", dom=PAGE):
    """A captured snapshot as the engine leaves it (only what freeze reads)."""
    folder = store / case_id / name
    folder.mkdir(parents=True)
    (folder / "dom.html.gz").write_bytes(gzip.compress(dom.encode("utf-8")))
    meta = {"finished_at": "2026-10-28T10:00:05+01:00", "url_final": "https://x.es/ficha",
            "http": {"status": 200}, "browser": {"user_agent": "Mozilla/5.0 Chrome/141"},
            "actions": [{"action": "first_load"}]}
    return folder, meta


def run(monkeypatch, *argv) -> None:
    monkeypatch.setattr(sys, "argv", ["pages", *argv])
    cli.main()


def test_readers():
    lines = pages.text_lines(PAGE)
    assert "100 % algodón" in lines and not any("oculto" in l for l in lines)
    kinds = [n.get("@type") for data in pages.json_ld(PAGE) for n in pages.walk(data)]
    assert [k for k in kinds if k] == ["Product", "BreadcrumbList"]   # graph root and crumbs have no type


def test_freeze_and_read(store):
    folder, meta = snapshot(store, "caso")
    info = pages.freeze("caso", "https://x.es/ficha", folder, meta, {"selection": "s.json"})
    assert info["snapshot"] == "var/pages/caso/20261028T100000"   # relative to capture/
    assert info["content"] == "DOM de la primera carga" and info["http_status"] == 200 and info["selection"] == "s.json"
    assert info["sha256"] == hashlib.sha256(PAGE.encode("utf-8")).hexdigest()
    assert json.loads((store / "caso.json").read_text(encoding="utf-8")) == info
    assert pages.read("caso") == PAGE and pages.page_path("caso") == store / "caso.html"
    with pytest.raises(PageError, match="no hay página congelada para otro; usa: capture/bin/pages fetch otro URL"):
        pages.read("otro")


def test_a_frozen_page_is_never_replaced(store):
    folder, meta = snapshot(store, "caso")
    pages.freeze("caso", "https://x.es/ficha", folder, meta)
    before = {p.name: p.read_bytes() for p in store.glob("caso.*")}
    again, meta2 = snapshot(store, "caso", "20261028T110000", dom="<html>otra</html>")
    with pytest.raises(PageError, match="caso ya tiene página congelada y no se sustituye"):
        pages.freeze("caso", "https://x.es/ficha", again, meta2)
    assert {p.name: p.read_bytes() for p in store.glob("caso.*")} == before
    # The ID counts as taken with either file
    (store / "solo.json").write_text("{}", encoding="utf-8")
    folder, meta = snapshot(store, "solo")
    with pytest.raises(PageError, match="solo ya tiene página congelada"):
        pages.freeze("solo", "https://x.es/ficha", folder, meta)
    assert not (store / "solo.html").exists()


def test_fetch_refuses_an_existing_id_before_visiting(store, monkeypatch):
    folder, meta = snapshot(store, "caso")
    pages.freeze("caso", "https://x.es/ficha", folder, meta)

    class Browser:   # any use of the browser would be a visit
        def __getattr__(self, name):
            raise AssertionError("no debe visitar")
    with pytest.raises(PageError, match="caso ya tiene página congelada"):
        pages.fetch("caso", "https://x.es/ficha", Browser())
    assert [p.name for p in (store / "caso").iterdir()] == ["20261028T100000"]   # no new snapshot
    with pytest.raises(SystemExit, match="pages: caso ya tiene página congelada"):
        run(monkeypatch, "fetch", "caso", "https://x.es/ficha")   # refused on the host too, before delegating


@pytest.mark.parametrize("bad", ["Caso", "caso_1", "../caso", "caso/x", "-caso", "caso-", ""])
def test_ids_are_kebab_case(store, bad):
    with pytest.raises(PageError, match="ID no válido"):
        pages.check_new(bad)


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_fetch_with_the_capture_engine(store, monkeypatch, capsys):
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
    monkeypatch.setenv("CAPTURE_PROFILE", str(store / "chrome-profile"))
    monkeypatch.setenv("CAPTURE_CDP_PORT", "9298")
    try:
        run(monkeypatch, "fetch", "caso", f"{base}/ficha#medidas")
        with pytest.raises(SystemExit, match="pages: otro: excluida por robots.txt"):
            run(monkeypatch, "fetch", "otro", f"{base}/privado/x")
        with pytest.raises(SystemExit, match="pages: caso ya tiene página congelada"):
            run(monkeypatch, "fetch", "caso", f"{base}/ficha")
    finally:
        httpd.shutdown()
    assert "caso: " in capsys.readouterr().out
    meta = json.loads((store / "caso.json").read_text(encoding="utf-8"))
    assert meta["method"] == "chrome-cdp" and meta["http_status"] == 200 and "Headless" not in meta["user_agent"]
    assert "100 % algodón" in pages.read("caso")   # the rendered DOM
    assert len(list((store / "caso").iterdir())) == 1   # the refused second fetch left no snapshot
    snap = json.loads((store / meta["snapshot"].split("/", 2)[2] / "meta.json").read_text(encoding="utf-8"))
    assert snap["outcome"] == "captured" and "actions" in snap and snap["legitimacy"]["robots"]["status"] == 200
    # A refusal leaves its evidence but no page: the ID stays free
    assert not (store / "otro.html").exists() and not (store / "otro.json").exists()
    refused = next((store / "otro").iterdir())
    assert json.loads((refused / "meta.json").read_text(encoding="utf-8"))["outcome"] == "disallowed"
    assert (refused / "robots.txt").exists()
    pages.check_new("otro")
