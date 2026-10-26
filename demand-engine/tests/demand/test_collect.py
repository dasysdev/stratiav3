"""Capture of the training catalog (T-025): pending pages, reserves and the batch with Chrome."""
import json
import os
import shutil
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from demand_engine import pages
from demand_engine.demand import collect

CHROME = os.environ.get("CAPTURE_CHROME", "google-chrome")


def page(pid):
    return {"id": f"t-{pid}", "url": f"/p/{pid}.html", "product": pid}


def selection(base=""):
    def fix(p):
        return {**p, "url": base + p["url"]}
    return {"store": "t", "spec": "x", "categories": [
        {"category": "hogar/sarten", "pilot": True, "pages": [fix(page("a")), fix(page("gone"))],
         "reserves": [fix(page("c"))]},
        {"category": "moda/vestido", "pilot": False, "pages": [fix(page("d"))], "reserves": []}]}


def test_batch_skips_what_is_done_and_keeps_reserves():
    batch = collect.Batch(selection(), [], pilot_only=True)
    assert [i["id"] for i in batch.items] == ["t-a", "t-gone"]
    assert batch.replace(batch.items[1])["id"] == "t-c"
    log = [{"id": "t-a", "outcome": "captured"}, {"id": "t-gone", "outcome": "gone"}, {"id": "t-c", "outcome": "blocked"}]
    batch = collect.Batch(selection(), log, pilot_only=False)
    assert [i["id"] for i in batch.items] == ["t-c", "t-d"]  # a block is retried; the gone page is not


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path == "/robots.txt":
            body, status, ctype = b"User-agent: *\nAllow: /\n", 200, "text/plain"
        elif self.path == "/p/gone.html":
            body, status, ctype = b"<html><title>404</title></html>", 404, "text/html"
        else:
            name = self.path.rsplit("/", 1)[-1]
            body, status, ctype = f"<html><head><title>Ficha {name}</title></head><body><h1>{name}</h1></body></html>".encode(), 200, "text/html"
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


@pytest.mark.chrome
@pytest.mark.skipif(not shutil.which(CHROME), reason="sin Chrome (se ejecuta en el contenedor)")
def test_capture_first_load_and_reserve(tmp_path, monkeypatch):
    from demand_engine.capture.browser import Browser

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}"
    monkeypatch.setattr(pages, "PAGES", tmp_path / "pages")
    monkeypatch.setattr(collect, "DISCOVERIES", tmp_path / "training")
    sel_file = tmp_path / "t-sel.json"
    sel_file.write_text(json.dumps(selection(base)))
    spec = {"base_url": base, "pacing": {"pause_s": [0.1, 0.2], "long_every": [99, 99], "hours": [0, 24],
                                         "challenge_wait_s": 1, "scroll": False}}
    browser = Browser(tmp_path / "chrome-profile", port=9298, chrome=CHROME)
    browser.start()
    try:
        records = collect.capture(spec, sel_file, pilot_only=True, out=lambda m: None, browser=browser)
    finally:
        browser.stop()
        httpd.shutdown()
    assert [(r["id"], r["outcome"]) for r in records] == [("t-a", "captured"), ("t-gone", "gone"), ("t-c", "captured")]
    info = json.loads((tmp_path / "pages" / "t-a.json").read_text())
    assert info["content"] == "DOM de la primera carga" and info["category"] == "hogar/sarten"
    assert "<h1>a.html</h1>" in (tmp_path / "pages" / "t-a.html").read_text()
    meta = json.loads((tmp_path / "pages" / "t-a" / info["snapshot"].rsplit("/", 1)[1] / "meta.json").read_text())
    assert meta["actions"][0]["action"] == "first_load"
    st = collect.status(selection(base), sel_file, pilot_only=True)
    assert st["captured"] == 2 and st["target"] == 2
    assert collect.capture(spec, sel_file, pilot_only=True, out=lambda m: None, browser=None) == []  # nothing pending
