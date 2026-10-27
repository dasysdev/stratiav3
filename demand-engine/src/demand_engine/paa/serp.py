"""The Google results page as the PAA engine reads it.

- Consent («Antes de ir a Google»): always «Rechazar todo».
- The «Más preguntas» box: every question carries its text in `data-q`. The echo of the query
  also carries it and is skipped.
- Expansion: a real mouse click on the first question not yet opened. Google adds two or three
  questions; the engine waits for the box to grow, not a fixed time.
- AI answers are not loaded. Opening a question makes two kinds of async call: one brings the
  new questions (`data-q`), the others bring the AI answer, whose scripts keep a frame loop
  running that a Chrome without GPU paints in software: two or three open answers saturate the
  page until it stops responding (2026-10-26/27). `Answers` learns which calls never bring a
  question and blocks them (`Network.setBlockedURLs`), as a content blocker would.
- Challenge (/sorry/, CAPTCHA, 429): the search is `blocked` and nothing else is done.

The answers («Vista creada con IA») are not read: only the questions are evidence.
"""
from __future__ import annotations

import json
import random
import re
import time
import urllib.parse

from ..capture import detect
from ..capture.browser import Page
from ..capture.cdp import CdpError
from ..capture.visit import OUTER_HTML
from .text import norm

NORM_JS = r"""s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
  .replace(/[¿?¡!]/g, '').replace(/\s+/g, ' ').trim()"""

READ = r"""((query) => {
  const norm = %s;
  const txt = el => (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim();
  const heads = [...document.querySelectorAll('h1,h2,h3,[role=heading]')].map(h => [h, txt(h)]);
  const q0 = norm(query), questions = [], seen = new Set();
  for (const e of document.querySelectorAll('[data-q]')) {
    const q = (e.getAttribute('data-q') || '').trim(), k = norm(q);
    if (q && k !== q0 && !seen.has(k)) { seen.add(k); questions.push(q); }
  }
  const related = [];
  heads.filter(([, t]) => /búsquedas relacionadas|otras búsquedas|también buscan/i.test(t)).forEach(([h]) => {
    let c = h.parentElement;
    for (let i = 0; i < 5 && c && c.querySelectorAll('a').length < 3; i++) c = c.parentElement;
    if (c) c.querySelectorAll('a').forEach(a => { const t = txt(a); if (t && t.length < 120 && !related.includes(t)) related.push(t); });
  });
  return {url: location.href, questions, related,
          paa_box: heads.some(([, t]) => /^más preguntas$|people also ask/i.test(t)),
          ai_overview: heads.some(([, t]) => /creada con ia|modo ia|ai overview/i.test(t) && t.length < 80),
          consent: !!document.querySelector('form[action*="consent"]') || /^consent\./.test(location.host),
          sorry: /\/sorry\//.test(location.pathname) || !!document.querySelector('#captcha-form')};
})(%s)"""

COUNT = "document.querySelectorAll('[data-q]').length"

# The first question not yet opened, scrolled into view: its text and where to click
TARGET = r"""((opened) => {
  const norm = %s;
  const done = new Set(opened);
  const el = [...document.querySelectorAll('[data-q]')].find(e => !done.has(norm(e.getAttribute('data-q') || '')));
  if (!el) return null;
  const b = el.querySelector('[aria-expanded],[role=button]') || el;
  b.scrollIntoView({block: 'center'});
  const r = b.getBoundingClientRect();
  if (!r.width || !r.height) return {q: el.getAttribute('data-q'), x: null, y: null};
  return {q: el.getAttribute('data-q'), x: r.left + Math.min(r.width / 2, 200), y: r.top + r.height / 2};
})(%s)"""

CONSENT = r"""(() => {
  const b = [...document.querySelectorAll('button, [role=button], input[type=submit]')]
    .find(e => /^rechazar todo$/i.test((e.innerText || e.value || '').trim()));
  if (!b) return null;
  b.scrollIntoView({block: 'center'});
  const r = b.getBoundingClientRect();
  return {x: r.left + r.width / 2, y: r.top + r.height / 2};
})()"""


CALLBACK = re.compile(r"/async/callback:(\d+)")


class Answers:
    """The async calls that bring AI answers, learned during a run and blocked from then on.

    A call id (`/async/callback:<id>`) is an answer when at least two of its responses carried no
    question and none ever did; an id that once brought questions is never blocked. The ids are
    Google's and may change: they are learned again in every run."""

    def __init__(self) -> None:
        self.questions: set[str] = set()
        self.blocked: set[str] = set()
        self.misses: dict[str, int] = {}
        self._checked: set[str] = set()

    def learn(self, page: Page) -> set[str]:
        """Read the finished async responses of the page; block the new answer ids."""
        urls, finished = {}, set()
        for ev in page.cdp.events:
            p = ev.get("params", {})
            if ev.get("method") == "Network.responseReceived":
                m = CALLBACK.search(p["response"]["url"])
                if m:
                    urls[p["requestId"]] = m.group(1)
            elif ev.get("method") == "Network.loadingFinished":
                finished.add(p["requestId"])
        for rid, cid in urls.items():
            if rid in self._checked or rid not in finished:
                continue
            self._checked.add(rid)
            try:
                body = page.cdp.send("Network.getResponseBody", {"requestId": rid}, timeout=10)
            except CdpError:
                continue
            if "data-q" in body.get("body", ""):  # a base64 body is binary: not questions
                self.questions.add(cid)
            else:
                self.misses[cid] = self.misses.get(cid, 0) + 1
        new = {c for c, n in self.misses.items() if n >= 2 and c not in self.questions} - self.blocked
        if new:
            self.blocked |= new
            page.cdp.send("Network.setBlockedURLs", {"urls": [f"*/async/callback:{c}*" for c in sorted(self.blocked)]})
        return new


def search_url(base: str, query: str, hl: str, gl: str) -> str:
    return f"{base}/search?" + urllib.parse.urlencode({"q": query, "hl": hl, "gl": gl})


def click(page: Page, x: float, y: float, rng: random.Random) -> None:
    page.cdp.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})
    page.cdp.pump(rng.uniform(0.15, 0.4))
    for kind in ("mousePressed", "mouseReleased"):
        page.cdp.send("Input.dispatchMouseEvent", {"type": kind, "x": x, "y": y, "button": "left", "clickCount": 1})
        page.cdp.pump(rng.uniform(0.05, 0.15))


def read(page: Page, query: str) -> dict:
    return page.eval(READ % (NORM_JS, json.dumps(query, ensure_ascii=False))) or {}


def wait_for(page: Page, condition: str, timeout: float) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            if page.eval(condition):
                return True
        except CdpError:
            pass
        page.cdp.pump(0.25)
    return False


def reject_consent(page: Page, rng: random.Random) -> bool:
    target = page.eval(CONSENT)
    if not target:
        return False
    click(page, target["x"], target["y"], rng)
    page.idle(rng.uniform(1.5, 3))
    return True


def load(page: Page, url: str) -> dict:
    """Navigate and wait for the document and for the box (or a challenge) to appear."""
    nav = page.navigate(url)
    if nav.get("errorText"):
        return {"error": nav["errorText"]}
    page.wait_ready()
    event = page.main_response()
    if event is None:
        return {"error": page.main_failure() or "sin respuesta del documento principal"}
    wait_for(page, f"{COUNT} > 1 || /\\/sorry\\//.test(location.pathname)", timeout=4)
    return {"event": event}


def blocked(page: Page, event: dict, state: dict) -> dict | None:
    status = event["response"].get("status")
    try:
        html = page.eval(OUTER_HTML) or ""
    except CdpError:
        html = ""
    found = detect.challenge(status, event["response"].get("headers"), html)
    if state.get("sorry") and not found:
        found = {"vendor": "google", "evidence": f"HTTP {status}; página /sorry/ o formulario de CAPTCHA"}
    return found


def search(page: Page, base: str, query: str, hl: str, gl: str, clicks: int, rng: random.Random,
           dwell_s=(1.5, 4.0), patience: int = 2, answers: Answers | None = None) -> tuple[dict, str]:
    """One search: open the results, read the box and open up to `clicks` questions, one at a
    time. Expansion stops early after `patience` clicks that add nothing. `answers` is shared by
    the searches of a run. Returns the record and the final DOM ('' unless captured)."""
    answers = answers if answers is not None else Answers()
    t0 = time.monotonic()
    url = search_url(base, query, hl, gl)
    record = {"query": query, "url": url, "hl": hl, "gl": gl, "actions": []}
    timings, mark = {}, [time.monotonic()]

    def lap(step: str) -> None:  # seconds spent in each step, added up over the clicks
        t = time.monotonic()
        timings[step] = round(timings.get(step, 0) + t - mark[0], 2)
        mark[0] = t

    loaded = load(page, url)
    lap("load")
    if "error" in loaded:
        return {**record, "outcome": "failed", "detail": loaded["error"], "elapsed_s": round(time.monotonic() - t0, 1)}, ""
    if reject_consent(page, rng):
        record["actions"].append("consentimiento: Rechazar todo")
        loaded = load(page, url)
        if "error" in loaded:
            return {**record, "outcome": "failed", "detail": loaded["error"], "elapsed_s": round(time.monotonic() - t0, 1)}, ""
        lap("consent")
    event = loaded["event"]
    first = read(page, query)
    record.update({"final_url": first.get("url"), "status": event["response"].get("status")})
    found = blocked(page, event, first)
    lap("read")
    if found:
        return {**record, "outcome": "blocked", "detail": found, "elapsed_s": round(time.monotonic() - t0, 1)}, ""
    if record["status"] and record["status"] >= 400:
        return {**record, "outcome": "failed", "detail": f"HTTP {record['status']}", "elapsed_s": round(time.monotonic() - t0, 1)}, ""

    questions = [{"q": q, "position": i + 1, "via": None} for i, q in enumerate(first.get("questions", []))]
    seen = {norm(q["q"]) for q in questions}
    opened, idle_clicks = [norm(query)], 0
    page.idle(rng.uniform(*dwell_s))
    lap("dwell")
    for _ in range(clicks):
        target = page.eval(TARGET % (NORM_JS, json.dumps(opened, ensure_ascii=False)))
        lap("target")
        if not target:
            break
        opened.append(norm(target["q"]))
        if target["x"] is None:
            continue
        before = page.eval(COUNT) or 0
        click(page, target["x"], target["y"], rng)
        record["actions"].append(f"clic: {target['q']}")
        lap("click")
        wait_for(page, f"{COUNT} > {before}", timeout=5)
        lap("wait_growth")
        page.idle(rng.uniform(0.8, 2.0))
        lap("idle")
        added = [q for q in read(page, query).get("questions", []) if norm(q) not in seen]
        lap("read")
        for cid in sorted(answers.learn(page)):
            record["actions"].append(f"bloqueo de respuestas: callback {cid}")
        lap("learn")
        for q in added:
            seen.add(norm(q))
            questions.append({"q": q, "position": len(questions) + 1, "via": target["q"]})
        idle_clicks = 0 if added else idle_clicks + 1
        if idle_clicks >= patience:
            break
    final = read(page, query)
    try:
        html = page.eval(OUTER_HTML, timeout=30) or ""
    except CdpError:
        html = ""
    lap("final")
    record.update({"outcome": "captured", "timings": timings, "blocked_callbacks": sorted(answers.blocked),
                   "questions": questions, "related": final.get("related", []),
                   "paa_box": final.get("paa_box", False), "ai_overview": final.get("ai_overview", False),
                   "clicks": sum(a.startswith("clic: ") for a in record["actions"]),
                   "elapsed_s": round(time.monotonic() - t0, 1)})
    return record, html
