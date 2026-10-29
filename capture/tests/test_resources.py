import argparse
import json
import threading
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture import audit, cli, pages, profiles, resources
from capture.audit import AuditError
from capture.robots import Robots

JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 500_000   # a body large enough to be cut


class Host:
    """A local host: what each path answers (`routes`) and how often it was asked."""

    def __init__(self, routes: dict) -> None:
        self.asked: Counter = Counter()
        self.routes = routes
        host = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                host.asked[self.path] += 1
                status, body, headers = host.routes.get(self.path, (404, b"no", [("Content-Type", "text/plain")]))
                self.send_response(status)
                for name, value in [("Content-Length", str(len(body))), *headers]:
                    self.send_header(name, value)
                self.end_headers()
                try:
                    self.wfile.write(body)
                except OSError:   # Chrome aborted the response
                    pass

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.base = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        self.netloc = self.base.split("/")[2]
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()


def image(*headers) -> tuple:
    return 200, JPEG, [("Content-Type", "image/jpeg"), *headers]


def test_robots_gives_the_rule_that_decides():
    robots = Robots("User-agent: *\nDisallow: /privado/\nAllow: /privado/libre\n", 200)
    assert robots.decision("https://x.es/privado/a.jpg") == (False, "Disallow: /privado/")
    assert robots.decision("https://x.es/privado/libre.jpg") == (True, "Allow: /privado/libre")
    assert robots.decision("https://x.es/a.jpg") == (True, None)
    assert Robots(None, 503).decision("https://x.es/a.jpg") == (False, None)


def make_audit(folder, shop: Host) -> None:
    """An audit whose crawl was on the shop: its robots.txt in sites/, its status in crawl.json."""
    site = folder / "sites" / shop.netloc.replace(":", "_")
    site.mkdir(parents=True)
    (site / "robots.txt").write_text("User-agent: *\nDisallow: /img/privado/\n", encoding="utf-8")
    crawl = {"audit": folder.name, "site": shop.base, "legitimacy": {"robots": {"status": 200, "mode": "rules"}},
             "runs": [{"run": 1, "sites": "sites"}], "pages": [], "reservation": None}
    (folder / "crawl.json").write_text(json.dumps(crawl), encoding="utf-8")
    (folder / "audit.json").write_text(json.dumps({"audit": folder.name, "site": shop.base, "pages": []}), encoding="utf-8")


@pytest.fixture(scope="module")
def engine(tmp_path_factory):
    from capture.browser import Browser

    browser = Browser(tmp_path_factory.mktemp("chrome") / "chrome-profile", port=9297)
    browser.start()
    yield browser
    browser.stop()


@pytest.fixture
def hosts(engine, tmp_path, monkeypatch):
    shop = Host({
        "/robots.txt": (200, b"User-agent: *\nAllow: /\n", [("Content-Type", "text/plain")]),
        "/img/ok.jpg": image(),
        "/img/prohibida.jpg": (403, b"no", [("Content-Type", "text/plain")]),
        "/img/vieja.jpg": (301, b"", [("Location", "/img/nueva.jpg"), ("X-Cache", "HIT")]),
        "/img/nueva.jpg": image(),
        "/img/noindex.jpg": image(("X-Robots-Tag", "noindex"), ("X-Robots-Tag", "googlebot-image: noimageindex")),
        "/img/privado/x.jpg": image(),
    })
    cdn = Host({
        "/robots.txt": (200, b"User-agent: *\nDisallow: /secreto/\n", [("Content-Type", "text/plain")]),
        "/a.jpg": image(("Cache-Control", "max-age=60")),
        "/secreto/b.jpg": image(),
    })
    monkeypatch.setattr(audit, "AUDITS", tmp_path / "audits")
    monkeypatch.setattr(resources, "AUDITS", tmp_path / "audits")
    monkeypatch.setattr(profiles, "origin", lambda: {"ip": "192.0.2.1", "source": "RIPEstat"})
    folder = tmp_path / "audits/recursos"
    make_audit(folder, shop)
    run = lambda urls: resources.run("recursos", urls, browser=engine, min_interval_s=0, out=lambda *_: None)  # noqa: E731
    yield shop, cdn, folder, run
    shop.httpd.shutdown()
    cdn.httpd.shutdown()


chrome = pytest.mark.skipif(not pages.engine_available(), reason="sin Chrome ni websockets (se ejecuta en el contenedor)")


@pytest.mark.chrome
@chrome
def test_resources_are_asked_for_with_their_headers_and_no_body(hosts):
    shop, cdn, folder, run = hosts
    s, c = shop.base, cdn.base
    urls = [f"{s}/img/ok.jpg", f"{s}/img/falta.jpg", f"{s}/img/prohibida.jpg", f"{s}/img/vieja.jpg",
            f"{s}/img/noindex.jpg", f"{s}/img/privado/x.jpg#frag", f"{c}/a.jpg", f"{c}/secreto/b.jpg",
            "data:image/png;base64,AAAA"]
    record = run(urls)
    assert json.loads((folder / "resources.json").read_text(encoding="utf-8")) == json.loads(json.dumps(record))
    got = {r["url"]: r for r in record["resources"]}
    assert {u.replace(s, "S").replace(c, "C"): (r["outcome"], r.get("status")) for u, r in got.items()} == {
        "S/img/ok.jpg": ("answered", 200), "S/img/falta.jpg": ("answered", 404),
        "S/img/prohibida.jpg": ("answered", 403), "S/img/vieja.jpg": ("answered", 200),
        "S/img/noindex.jpg": ("answered", 200), "S/img/privado/x.jpg": ("disallowed", None),
        "C/a.jpg": ("answered", 200), "C/secreto/b.jpg": ("disallowed", None),
        "data:image/png;base64,AAAA": ("invalid", None)}
    assert got[f"{s}/img/ok.jpg"]["headers"]["Content-Type"] == "image/jpeg"
    moved = got[f"{s}/img/vieja.jpg"]
    assert moved["url_final"] == f"{s}/img/nueva.jpg"
    assert [(r["status"], r["headers"]["Location"], r["headers"]["X-Cache"]) for r in moved["redirects"]] == \
        [(301, "/img/nueva.jpg", "HIT")]
    assert got[f"{s}/img/noindex.jpg"]["headers"]["X-Robots-Tag"] == "noindex\ngooglebot-image: noimageindex"
    assert got[f"{c}/a.jpg"]["headers"]["Cache-Control"] == "max-age=60"
    assert got[f"{s}/img/privado/x.jpg"]["rule"] == "Disallow: /img/privado/"
    assert got[f"{c}/secreto/b.jpg"]["rule"] == "Disallow: /secreto/"

    # Nothing of a body is kept; robots.txt of the shop comes from the crawl, that of the CDN is kept
    assert "/robots.txt" not in shop.asked and "/img/privado/x.jpg" not in shop.asked
    assert cdn.asked["/robots.txt"] == 1 and "/secreto/b.jpg" not in cdn.asked
    cdn_dir = f"resources/sites/{cdn.netloc.replace(':', '_')}"
    assert (folder / cdn_dir / "robots.txt").read_bytes() == b"User-agent: *\nDisallow: /secreto/\n"
    kept = sorted(str(p.relative_to(folder)) for p in folder.rglob("*") if p.is_file())
    assert kept == sorted(["audit.json", "crawl.json", f"sites/{shop.netloc.replace(':', '_')}/robots.txt",
                           f"{cdn_dir}/robots.txt", "resources.json", "resources.jsonl"])
    assert record["hosts"][cdn.netloc]["robots"]["source"] == "resources"
    assert record["hosts"][cdn.netloc]["robots"]["file"] == f"{cdn_dir}/robots.txt"
    assert record["hosts"][shop.netloc]["robots"] == {"status": 200, "mode": "rules", "source": "crawl",
                                                      "file": f"sites/{shop.netloc.replace(':', '_')}/robots.txt"}

    # A URL already recorded is not asked for again
    before = shop.asked + cdn.asked
    again = run([f"{s}/img/ok.jpg", f"{c}/a.jpg", f"{c}/otra.jpg"])
    assert (shop.asked + cdn.asked) - before == Counter({"/otra.jpg": 1})
    assert len(again["resources"]) == 10 and [r["run"] for r in again["runs"]] == [1, 2]
    assert again["runs"][1]["asked"] == 1


@pytest.mark.chrome
@chrome
def test_a_429_stops_the_run_and_is_asked_again(hosts):
    shop, _, _, run = hosts
    s = shop.base
    shop.routes["/img/lenta.jpg"] = (429, b"", [("Retry-After", "60")])
    record = run([f"{s}/img/lenta.jpg", f"{s}/img/ok.jpg"])
    assert [r["outcome"] for r in record["resources"]] == ["blocked"] and record["stopped"].startswith("parado: 429")
    shop.routes["/img/lenta.jpg"] = image()
    record = run([f"{s}/img/lenta.jpg", f"{s}/img/ok.jpg"])
    assert {r["url"]: r["outcome"] for r in record["resources"]} == {f"{s}/img/lenta.jpg": "answered",
                                                                     f"{s}/img/ok.jpg": "answered"}


@pytest.mark.chrome
@chrome
def test_a_tdm_reservation_stops_the_audit(hosts):
    shop, cdn, _, run = hosts
    cdn.routes["/.well-known/tdmrep.json"] = (200, b'[{"location": "/", "tdm-reservation": 1}]',
                                              [("Content-Type", "application/json")])
    shop.routes["/img/reservada.jpg"] = image(("tdm-reservation", "1"))
    record = run([f"{cdn.base}/a.jpg", f"{shop.base}/img/ok.jpg"])
    assert [r["outcome"] for r in record["resources"]] == ["reserved"] and "/a.jpg" not in cdn.asked
    assert record["reservation"]["source"] == "tdmrep.json"
    with pytest.raises(audit.Reserved):
        run([f"{shop.base}/img/ok.jpg"])


@pytest.mark.chrome
@chrome
def test_a_reservation_in_the_headers_of_a_response(hosts):
    shop, _, _, run = hosts
    shop.routes["/img/reservada.jpg"] = image(("tdm-reservation", "1"))
    record = run([f"{shop.base}/img/reservada.jpg", f"{shop.base}/img/ok.jpg"])
    assert [r["outcome"] for r in record["resources"]] == ["reserved"]
    assert record["reservation"]["source"] == "cabecera tdm-reservation" and "/img/ok.jpg" not in shop.asked


def test_the_resources_command(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(audit, "AUDITS", tmp_path)
    monkeypatch.setattr(resources, "AUDITS", tmp_path)
    monkeypatch.setattr(pages, "engine_available", lambda: True)
    with pytest.raises(AuditError, match="sin URL"):
        cli.cmd_resources(argparse.Namespace(audit="a", urls=[], from_file=None))
    with pytest.raises(AuditError, match="pages audit a"):
        cli.cmd_resources(argparse.Namespace(audit="a", urls=["https://x.es/a.jpg"], from_file=None))
    seen = {}

    def fake(audit_id, urls):
        seen["urls"] = urls
        return {"resources": [{}, {}], "outcomes": {"answered": 1, "disallowed": 1}, "stopped": None,
                "reservation": None}

    monkeypatch.setattr(resources, "run", fake)
    monkeypatch.setattr("sys.stdin", __import__("io").StringIO("https://x.es/b.jpg\n# nota\n\nhttps://x.es/c.jpg\n"))
    cli.cmd_resources(argparse.Namespace(audit="a", urls=["https://x.es/a.jpg"], from_file="-"))
    assert seen["urls"] == ["https://x.es/a.jpg", "https://x.es/b.jpg", "https://x.es/c.jpg"]
    assert "2 URL registradas (1 answered, 1 disallowed)" in capsys.readouterr().out
    monkeypatch.setattr(resources, "run", lambda *a: {"resources": [{}], "outcomes": {"reserved": 1},
                                                      "stopped": "parado", "reservation": {
                                                          "where": "x.es", "source": "tdmrep.json", "url": "https://x.es/a.jpg"}})
    with pytest.raises(SystemExit) as stop:
        cli.cmd_resources(argparse.Namespace(audit="a", urls=["https://x.es/a.jpg"], from_file=None))
    assert stop.value.code == cli.RESERVED and "reserva la minería" in capsys.readouterr().err
