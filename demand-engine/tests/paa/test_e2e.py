"""End to end with the real Chrome against a local imitation of the results page (runs in the
container): consent, the echo of the query, expansion by clicks, the answer calls learned and
blocked, early stop, a leftover tab, a 429 that lifts on retry, a block and a page that stops
answering."""
import collections
import html
import json
import os
import random
import shutil
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from capture.browser import Browser
from demand_engine.paa import store
from demand_engine.paa.run import run
from demand_engine.paa.store import SeedSet

CHROME = os.environ.get("CAPTURE_CHROME", "google-chrome")
pytestmark = [pytest.mark.chrome,
              pytest.mark.skipif(not shutil.which(CHROME), reason="sin Chrome (se ejecuta en el contenedor)")]

CONSENT = """<div id="consent"><h2>Antes de ir a Google</h2>
<button onclick="document.cookie='consent=no; path=/'; document.getElementById('consent').remove()">Rechazar todo</button>
<button>Aceptar todo</button></div>"""

RESULTS = """<!doctype html><html><head><meta charset="utf-8"><title>{q} - Buscar</title></head><body>
{consent}
<form><input name="q" value="{q}"><div data-q="{q}" style="display:none"></div></form>
<h2>Vista creada con IA</h2><p>Respuesta generada.</p>
<h2>Más preguntas</h2><div id="box"></div>
<h2>Otras personas también buscan</h2><div><a href="#">{q} 90</a> <a href="#">{q} 135</a> <a href="#">{q} 150</a></div>
<script>
// As Google: opening a question asks callback:1 for the new questions and callback:2 (twice)
// for the AI answer
const Q = {jq};
let n = 0;
const box = document.getElementById('box');
function add(text) {{
  n += 1;
  const d = document.createElement('div'); d.className = 'rq'; d.dataset.q = text;
  const b = document.createElement('div'); b.setAttribute('role', 'button'); b.setAttribute('aria-expanded', 'false');
  b.style.cssText = 'padding:12px;border:1px solid #ccc;width:600px'; b.textContent = text;
  d.appendChild(b); box.appendChild(d);
}}
for (let i = 0; i < 4; i++) add('¿' + Q + ' pregunta ' + (n + 1) + '?');
box.addEventListener('click', e => {{
  const b = e.target.closest('[role=button]');
  if (!b || b.getAttribute('aria-expanded') === 'true') return;
  b.setAttribute('aria-expanded', 'true');
  fetch('/async/callback:2?a=' + n).catch(() => {{}});
  fetch('/async/callback:2?b=' + n).catch(() => {{}});
  fetch('/async/callback:1?q=' + encodeURIComponent(Q) + '&n=' + n).then(r => r.text()).then(html => {{
    const tmp = document.createElement('div'); tmp.innerHTML = html;
    tmp.querySelectorAll('[data-q]').forEach(x => add(x.getAttribute('data-q')));
  }});
}});
</script></body></html>"""

SORRY = b"""<!doctype html><html><body><form id="captcha-form" action="/sorry/index">
<iframe src="https://www.google.com/recaptcha/api2/anchor"></iframe></form></body></html>"""


class Handler(BaseHTTPRequestHandler):
    hits = collections.Counter()  # requests per async callback id

    def log_message(self, *args):
        pass

    def _send(self, status, body: bytes, headers: dict | None = None):
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urllib.parse.urlsplit(self.path)
        consent = "" if "consent=no" in (self.headers.get("Cookie") or "") else CONSENT
        if url.path == "/":
            return self._send(200, f"<!doctype html><html><body>{consent}<p>Google</p></body></html>".encode())
        args = urllib.parse.parse_qs(url.query)
        q = args.get("q", [""])[0]
        if url.path.startswith("/async/callback:"):
            cid = url.path.rsplit(":", 1)[1]
            Handler.hits[cid] += 1
            if cid == "2":  # the AI answer: no question
                return self._send(200, ("<div>Respuesta de IA</div>" * 50).encode())
            n, limit = int(args.get("n", ["0"])[0]), 4 if q == "corta" else 10
            new = "".join(f'<div data-q="¿{html.escape(q)} pregunta {i}?"></div>' for i in range(n + 1, min(n + 2, limit) + 1))
            return self._send(200, (new or "<div></div>").encode("utf-8"))
        if q == "bloqueo":
            return self._send(429, SORRY)
        if q == "pasajero":  # a 429 that lifts: the first asks to wait 0 s, the second says nothing
            Handler.hits[q] += 1
            if Handler.hits[q] <= 2:
                return self._send(429, SORRY, {"Retry-After": "0"} if Handler.hits[q] == 1 else None)
        if q == "colgada":  # main thread busy for good, as Google's results page on 2026-10-26
            return self._send(200, b"<!doctype html><html><body><script>setTimeout(() => { for (;;) {} }, 0)</script></body></html>")
        body = RESULTS.format(q=html.escape(q), jq=json.dumps(q), consent=consent)
        return self._send(200, body.encode("utf-8"))


@pytest.fixture(scope="module")
def server():
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield httpd.server_address[1]
    httpd.shutdown()


@pytest.fixture
def browser(tmp_path):
    b = Browser(tmp_path / "chrome-profile", port=9298, chrome=CHROME)
    b.start()
    yield b
    b.stop()


def test_run_set(server, browser, paa_dirs):
    spec = {"class": "Ropa de cama", "clicks": 3, "market": {"base": f"http://127.0.0.1:{server}"},
            "pacing": {"pause_s": [0.1, 0.2], "dwell_s": [0.1, 0.2], "hours": [0, 24], "long_every": [99, 99]},
            "block_backoff": {"first_s": 0.2, "retries": 5},
            "seeds": [{"q": "sábanas", "group": "núcleo"}, {"q": "corta"}, {"q": "pasajero"}, {"q": "bloqueo"},
                      {"q": "después"}]}
    (paa_dirs / "sets" / "e2e.json").write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
    s = SeedSet("e2e")
    leftover = browser.new_window()                                   # a tab left by a run cut short
    Handler.hits.clear()
    summary = run(s, browser, rng=random.Random(1), say=lambda *a: None)
    assert leftover.target_id not in [t["id"] for t in browser._json("/json")]

    assert summary["captured"] == 3 and summary["blocked"] == 1 and summary["stopped"].startswith("bloqueo")
    assert summary["retries"] == 2 + 5                                # pasajero: 2; bloqueo: los 5
    recs = {r["query"]: r for r in s.records()}
    full = recs["sábanas"]
    qs = [q["q"] for q in full["questions"]]
    assert len(qs) == 10 and "sábanas" not in qs                      # 4 + 3 clics × 2, sin el eco
    assert full["questions"][4]["via"] == qs[0] and full["questions"][0]["via"] is None
    assert full["related"] == ["sábanas 90", "sábanas 135", "sábanas 150"]
    assert full["paa_box"] and full["ai_overview"] and full["clicks"] == 3
    assert full["blocked_callbacks"] == ["2"]                         # aprendido en el primer clic
    assert Handler.hits["2"] == 2 and Handler.hits["1"] >= 5          # después, ninguna respuesta más
    assert recs["corta"]["clicks"] == 2 and len(recs["corta"]["questions"]) == 4   # dos clics sin nada: para
    assert [x["q"] for x in s.pending()] == ["bloqueo", "después"]
    assert store.blocked_now() and len(store.engine_state()["blocks"]) == 1   # los reintentos no son bloqueos
    log = [json.loads(x) for x in (s.dir / "log.jsonl").read_text(encoding="utf-8").splitlines()]
    events = {e["event"] for e in log}
    assert {"consent", "block", "tabs", "retry"} <= events
    retries = [e for e in log if e["event"] == "retry"]
    assert retries[0]["query"] == "pasajero" and retries[0]["retry_after_s"] == 0 and retries[0]["wait_s"] == 0
    assert retries[1]["retry_after_s"] is None and retries[1]["wait_s"] == 0.3            # sin Retry-After: 0,2 × 1,5
    assert [e["wait_s"] for e in retries[2:]] == [0.2, 0.3, 0.5, 0.7, 1.0]                # +50 % cada vez
    attempts = sorted((s.dir / "searches" / "bloqueo").iterdir())
    assert len(attempts) == 6                                         # cada intento, con su registro
    last = json.loads((attempts[-1] / "record.json").read_text(encoding="utf-8"))
    assert last["status"] == 429 and last["detail"]["vendor"] == "google" and last["retry_after_s"] is None
    assert "content-type" in {k.lower() for k in last["headers"]} and last["files"]["dom"]
    data = json.loads((s.dir / "questions.json").read_text(encoding="utf-8"))
    assert data["searches"] == 3 and len(data["questions"]) == 14 + 10

    assert run(s, browser, say=lambda *a: None)["stopped"].startswith("bloqueado hasta")
    (paa_dirs / "sets" / "otro.json").write_text(json.dumps({**spec, "seeds": [{"q": "x"}]}), encoding="utf-8")
    assert run(SeedSet("otro"), browser, say=lambda *a: None)["stopped"].startswith("bloqueado hasta")  # global


def test_unresponsive_page_stops_the_run_without_blocking(server, browser, paa_dirs):
    spec = {"class": "Ropa de cama", "clicks": 2, "market": {"base": f"http://127.0.0.1:{server}"},
            "pacing": {"pause_s": [0.1, 0.2], "dwell_s": [0.1, 0.2]},
            "seeds": [{"q": "colgada"}, {"q": "después"}]}
    (paa_dirs / "sets" / "hang.json").write_text(json.dumps(spec), encoding="utf-8")
    s = SeedSet("hang")
    summary = run(s, browser, rng=random.Random(1), say=lambda *a: None)
    assert summary["failed"] == 1 and "dejó de responder" in summary["stopped"]
    assert s.status_of({"q": "colgada"}) == "failed" and store.blocked_now() is None
    assert [x["q"] for x in s.pending()] == ["colgada", "después"]
