"""End to end with the real Chrome against a local server (runs in the container)."""
import gzip
import json
import os
import random
import shutil
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

from capture import sitemaps
from capture.browser import Browser
from capture.files import write_json
from demand_engine.mpir import scheduler
from demand_engine.mpir.store import Study

SITE = Path(__file__).parent / "site"
CHROME = os.environ.get("CAPTURE_CHROME", "google-chrome")
pytestmark = [pytest.mark.chrome,
              pytest.mark.skipif(not shutil.which(CHROME), reason="sin Chrome (se ejecuta en el contenedor)")]

CHALLENGE = b"<!doctype html><html><head><title>Just a moment...</title></head><body>cf-chl-widget</body></html>"


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def _send(self, status: int, body: bytes, ctype: str = "text/html; charset=utf-8") -> None:
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        port = self.server.server_address[1]
        if self.path == "/robots.txt":
            body = (f"User-agent: *\nDisallow: /private\n\nUser-agent: GPTBot\nDisallow: /\n\n"
                    f"Sitemap: http://127.0.0.1:{port}/sitemap.xml\n").encode()
            return self._send(200, body, "text/plain")
        if self.path == "/sitemap.xml":
            urls = "".join(f"<url><loc>http://127.0.0.1:{port}/{p}</loc></url>" for p in ("product.html", "index.html"))
            body = f'<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
            return self._send(200, body.encode(), "application/xml")
        if self.path == "/blocked.html":
            return self._send(403, CHALLENGE)
        return super().do_GET()


@pytest.fixture(scope="module")
def server():
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), partial(Handler, directory=str(SITE)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield httpd.server_address[1]
    httpd.shutdown()


@pytest.fixture
def browser(tmp_path):
    b = Browser(tmp_path / "chrome-profile", port=9299, chrome=CHROME)
    b.start()
    yield b
    b.stop()


def read_gz(path: Path) -> str:
    return gzip.decompress(path.read_bytes()).decode("utf-8")


def test_check_discover_and_capture(server, browser):
    study = Study.create("e2e", "Ropa de cama")
    plan = study.plan()
    plan["pacing"].update({"dwell_s": [6, 6], "pause_s": [0.2, 0.3], "long_every": [99, 99],
                           "hours": [0, 24], "challenge_wait_s": 2})
    write_json(study.home / "plan.json", plan)
    local, other = f"http://127.0.0.1:{server}", f"http://localhost:{server}"
    for sid, base in (("local", local), ("otro", other)):
        study.save_site({"id": sid, "base_url": base, "type": "especialista", "reason": "prueba",
                         "terms_reviewed": True, "checks": [], "blocks": []})
    out = []
    stop = threading.Event()

    scheduler.run_checks(study, ["local", "otro"], browser, out.append, stop)
    check = study.site("local")["checks"][-1]
    assert check["verdict"] == "ok", out
    assert check["robots"]["ai_blocked"] == ["GPTBot"]
    assert check["tdmrep"]["status"] == 404
    assert check["home"]["title"] == "Tienda de prueba"
    assert (study.dir / check["evidence"] / "robots.txt").exists()

    page = browser.new_window()
    try:
        found = sitemaps.discover(page, local, check["robots"]["sitemaps"], r"product", None, 10,
                                  random.Random(1))
    finally:
        browser.close_window(page)
    assert [u["loc"] for u in found["urls"]] == [f"{local}/product.html"]

    study.add_resources("local", [f"{local}/product.html", f"{local}/private/x.html",
                                  f"{local}/reserved.html", f"{local}/missing.html"], "product")
    study.add_resources("otro", [f"{other}/blocked.html", f"{other}/product.html"], "product")
    scheduler.run_capture(study, ["local", "otro"], browser, out.append, stop)

    status = {r["id"]: r["status"] for r in study.resources()}
    assert status == {"local-001": "captured", "local-002": "disallowed", "local-003": "reserved",
                      "local-004": "gone", "otro-001": "blocked", "otro-002": "pending"}, out

    res = {r["id"]: r for r in study.resources()}
    folder = study.dir / res["local-001"]["snapshots"][0]
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
    assert meta["outcome"] == "captured" and meta["http"]["status"] == 200
    assert "Headless" not in meta["browser"]["user_agent"]
    assert gzip.decompress((folder / "response.html.gz").read_bytes()) == (SITE / "product.html").read_bytes()
    dom = read_gz(folder / "dom.html.gz")
    assert "Contenido diferido cargado" in dom          # scrolling loaded the lazy block
    assert dom.count('data-capture-hidden="1"') == 3       # details, display:none, collapsed accordion
    assert meta["dom"]["hidden_roots"] == 3
    assert 'style="display: contents" data-capture-hidden' not in dom
    assert not (folder / "page.mhtml.gz").exists()                 # no MHTML (D-172)

    reserved = study.dir / res["local-003"]["snapshots"][0]
    assert sorted(p.name for p in reserved.iterdir()) == ["meta.json"]   # nothing kept
    blocked = json.loads((study.dir / res["otro-001"]["snapshots"][0] / "meta.json").read_text())
    assert blocked["challenge"]["vendor"] == "cloudflare"
    assert len(study.site("otro")["blocks"]) == 1
    assert "bloqueado" in scheduler.capturable(study, study.site("otro"))
