import gzip
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture import pages, profiles
from capture.browser import Browser
from capture.pages import PageError
from capture.robots import Robots

# windows-1252, no BOM: Chrome would hand the body over decoded to UTF-8. The script inserts
# INSERTED right after itself
PAGE = ("<!doctype html><html><head><meta charset=windows-1252><title>Café</title></head>"
        "<body><p>Composición: 100 % algodón · 25 €</p>"
        "<script>document.cookie = 'js=1'; document.body.insertAdjacentHTML('beforeend', '<p>solo-con-js</p>')</script>"
        "<noscript><p>sin-js</p></noscript></body></html>").encode("cp1252")
INSERTED = "</script><p>solo-con-js</p>"
ROBOTS = b"User-agent: GPTBot\nDisallow: /\n\nUser-agent: *\nDisallow: /privado\n"
ORIGIN = {"ip": "192.0.2.1", "prefix": "192.0.2.0/24", "asn": 64500, "as_holder": "PRUEBA",
          "country": "ES", "source": "RIPEstat", "checked_at": "2026-10-28T10:00:00+01:00"}


@pytest.fixture
def store(tmp_path, monkeypatch):
    monkeypatch.setattr(pages, "PAGES", tmp_path)
    return tmp_path


def test_profiles():
    assert profiles.get(None) is profiles.READER and profiles.DEFAULT == "reader"
    audit = profiles.get("audit-es")
    assert (audit.javascript, audit.fresh_context, audit.scroll, audit.evidence) == (False, True, False, True)
    with pytest.raises(ValueError, match="perfil de captura desconocido: 'otro'"):
        profiles.get("otro")


def test_robots_by_bot():
    bots = Robots(ROBOTS.decode(), 200).by_bot("https://x.es/privado/a?b=1", ["GPTBot", "ClaudeBot"])
    assert bots == {"GPTBot": {"group": "own", "url": False, "root": False},
                    "ClaudeBot": {"group": "*", "url": False, "root": True}}
    assert Robots(None, 404).by_bot("https://x.es/a", ["GPTBot"]) == {"GPTBot": {"group": None, "url": True, "root": True}}


def test_audit_page_is_the_response_decoded_as_the_browser_did(store):
    folder = store / "caso" / "20261028T100000"
    folder.mkdir(parents=True)
    (folder / "response.html.gz").write_bytes(gzip.compress(b"\xef\xbb\xbf" + "<p>Café</p>".encode("utf-8")))
    meta = {"finished_at": "2026-10-28T10:00:05+01:00", "profile": "audit-es", "dom": {"charset": "windows-1252"},
            "request_context": {"accept_language": "es-ES,es;q=0.9", "origin": ORIGIN},
            "robots_bots": {"GPTBot": {"group": "own", "url": False, "root": False}}}
    info = pages.freeze("caso", "https://x.es/ficha", folder, meta)
    assert pages.read("caso") == "<p>Café</p>"   # the BOM wins over the charset, and is not kept
    assert info["profile"] == "audit-es" and info["content"] == "respuesta HTTP sin JavaScript"
    assert info["request_context"]["origin"]["asn"] == 64500 and info["robots_bots"]["GPTBot"]["url"] is False


def test_fetch_refuses_an_unknown_profile_before_visiting(store):
    with pytest.raises(ValueError, match="perfil de captura desconocido"):
        pages.fetch("caso", "https://x.es/ficha", object(), profile="otro")
    assert not (store / "caso").exists()


@pytest.mark.chrome
@pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")
def test_audit_profile_against_the_reader_one(store, monkeypatch):
    seen = []   # (path, Cookie, Accept-Language) of every document request

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            headers = {}
            if self.path == "/robots.txt":
                status, body, kind = 200, ROBOTS, "text/plain"
            elif self.path == "/salto":
                status, body, kind = 301, b"", "text/html"
                headers = {"Location": "/ficha", "X-Salto": "1"}
            elif self.path == "/ficha":
                seen.append((self.path, self.headers.get("Cookie"), self.headers.get("Accept-Language")))
                status, body, kind = 200, PAGE, "text/html"
                headers = {"Set-Cookie": "visto=1; Path=/"}
            else:
                status, body, kind = 404, b"no", "text/plain"
            self.send_response(status)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(body)))
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body)

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}"
    monkeypatch.setattr(profiles, "origin", lambda: ORIGIN)
    browser = Browser(store / "chrome-profile", port=9297)
    browser.start()
    try:
        pages.fetch("lector", f"{base}/ficha", browser)                          # the domain, already captured
        audit = pages.fetch("auditoria", f"{base}/salto", browser, profile="audit-es")
        pages.fetch("lector-2", f"{base}/ficha", browser)
        with pytest.raises(PageError, match="excluida por robots.txt"):
            pages.fetch("privado", f"{base}/privado/x", browser, profile="audit-es")
    finally:
        browser.stop()
        httpd.shutdown()

    # Clean state: the reader profile keeps its cookies, the audit one starts without any
    cookies = [c for _, c, _ in seen]
    assert cookies[0] is None and cookies[1] is None and "visto=1" in cookies[2] and "js=1" in cookies[2]
    assert all(lang.startswith("es-ES") for _, _, lang in seen)

    reader = json.loads((store / "lector.json").read_text(encoding="utf-8"))
    assert reader["profile"] == "reader" and reader["content"] == "DOM renderizado"
    assert "request_context" not in reader and "robots_bots" not in reader
    assert INSERTED in pages.read("lector")                                     # its JavaScript ran

    assert audit["profile"] == "audit-es" and audit["content"] == "respuesta HTTP sin JavaScript"
    assert audit["request_context"]["accept_language"].startswith("es-ES")
    assert audit["request_context"]["origin"] == ORIGIN
    assert audit["robots_bots"]["GPTBot"] == {"group": "own", "url": False, "root": False}
    assert audit["robots_bots"]["ClaudeBot"] == {"group": "*", "url": True, "root": True}
    assert set(audit["robots_bots"]) == set(profiles.BOTS)
    text = pages.read("auditoria")
    assert "Composición: 100 % algodón · 25 €" in text and "<noscript>" in text

    snap = store / audit["snapshot"].split("/", 2)[2]
    meta = json.loads((snap / "meta.json").read_text(encoding="utf-8"))
    assert meta["profile"] == "audit-es" and meta["response_body"] == "original"
    assert gzip.decompress((snap / "response.html.gz").read_bytes()) == PAGE      # the original bytes
    assert meta["redirects"][0]["status"] == 301 and meta["redirects"][0]["headers"]["X-Salto"] == "1"
    assert meta["actions"][0]["action"] == "first_load" and meta["dom"]["charset"] == "windows-1252"
    assert meta["legitimacy"]["tdmrep"]["status"] == 404                        # read without the page's JavaScript
    dom = gzip.decompress((snap / "dom.html.gz").read_bytes()).decode("utf-8")
    assert INSERTED not in dom and "<p>sin-js</p>" in dom                    # no script ran; noscript is markup
