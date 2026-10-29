"""Visit of one page and its snapshot.

Every visit leaves meta.json in the snapshot folder it is given, whatever the outcome. Content
is kept only when the page is not a challenge, an error or under a TDM reservation:

  response.html.gz   body of the main document as the server sent it (decoded to UTF-8 by
                     Chrome; its original bytes under a profile that keeps evidence)
  dom.html.gz        rendered DOM after reading the page (shadow roots serialised); the roots
                     of hidden subtrees (closed details, collapsed accordions, display:none)
                     carry data-capture-hidden="1"

No MHTML (D-172) and no screenshots (D-042): nothing reads the page's resources.

With a pacer (batch captures) the page is read at a reader's pace; without one (a single
page) it is only scrolled through, so that lazy content loads. A pacing without scroll keeps
the first load: no scrolling and no dwell (the training catalog, D-053), and so does a profile
without scroll (audit-es).

The window's capture profile (capture.profiles) is recorded in meta.json. Without JavaScript a
challenge cannot resolve by itself, so it is not waited for. A profile that keeps evidence also
records the request context: Accept-Language as sent and the origin (IP, country, ASN). A caller
that visits many pages consults the origin once per run and gives it (`origin`); without it,
each visit consults it.
"""
from __future__ import annotations

import json
import random
import threading
import time
from pathlib import Path

from . import detect, profiles, tdm
from .browser import Page
from .cdp import CdpError
from .files import now, write_evidence
from .pacing import DEFAULTS, Pacer

SINGLE_SCROLL_S = 8  # scrolling budget of a single page, without a reader's pace

OUTER_HTML = "document.documentElement ? document.documentElement.outerHTML : ''"

META = """(() => {
  const m = n => { const e = document.querySelector(`meta[name="${n}" i]`); return e ? e.getAttribute('content') : null; };
  return {tdm: m('tdm-reservation'), tdm_policy: m('tdm-policy'), robots: m('robots')};
})()"""

# Marks the root of every hidden subtree that has content. Elements with display:contents
# have no box but are not hidden. The list stays in the isolated world for UNMARK.
MARK_HIDDEN = """(() => {
  const SKIP = new Set(['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE', 'META', 'LINK', 'BR']);
  const marked = [];
  const hidden = el => {
    const style = getComputedStyle(el);
    if (style.display === 'contents') return false;
    if (!el.checkVisibility({opacityProperty: true, visibilityProperty: true})) return true;
    const r = el.getBoundingClientRect();
    return r.height < 1 && el.scrollHeight > 1 && (style.overflowY === 'hidden' || style.overflowY === 'clip');
  };
  const walk = node => {
    for (const el of node.children) {
      if (SKIP.has(el.tagName)) continue;
      if (hidden(el)) {
        if (el.textContent.trim() || el.querySelector('img')) { el.setAttribute('data-capture-hidden', '1'); marked.push(el); }
        continue;
      }
      walk(el);
      if (el.shadowRoot) walk(el.shadowRoot);
    }
  };
  if (document.body) walk(document.body);
  window.__captureMarked = marked;
  return marked.length;
})()"""

UNMARK_HIDDEN = """(() => {
  for (const el of window.__captureMarked || []) el.removeAttribute('data-capture-hidden');
  window.__captureMarked = [];
  return true;
})()"""

# documentElement.getHTML() serialises open shadow roots (declarative shadow DOM)
SERIALIZE = """(() => {
  const roots = [];
  const collect = node => { for (const el of node.querySelectorAll('*')) if (el.shadowRoot) { roots.push(el.shadowRoot); collect(el.shadowRoot); } };
  collect(document);
  const root = document.documentElement;
  const doctype = document.doctype ? new XMLSerializer().serializeToString(document.doctype) + '\\n' : '';
  const attrs = [...root.attributes].map(a => ` ${a.name}="${a.value.replace(/&/g, '&amp;').replace(/"/g, '&quot;')}"`).join('');
  const inner = root.getHTML ? root.getHTML({serializableShadowRoots: true, shadowRoots: roots}) : root.innerHTML;
  return {html: `${doctype}<html${attrs}>${inner}</html>`, elements: document.getElementsByTagName('*').length,
          shadow_roots: roots.length, title: document.title, charset: document.characterSet};
})()"""


def _html(page: Page) -> str:
    try:
        return page.eval(OUTER_HTML, timeout=30) or ""
    except CdpError:
        return ""


def load(page: Page, url: str, challenge_wait: float) -> dict:
    """Navigate and wait for the document. A non-interactive challenge (Cloudflare's «Just a
    moment») may resolve by itself in a real browser: it is given `challenge_wait` seconds,
    without touching it. Nothing else is done against a challenge."""
    nav = page.navigate(url)
    if nav.get("errorText"):
        return {"error": nav["errorText"]}
    ready = page.wait_ready()
    event = page.main_response()
    if event is None:
        return {"error": page.main_failure() or "sin respuesta del documento principal"}
    html = _html(page)
    found = detect.challenge(event["response"].get("status"), event["response"].get("headers"), html)
    deadline = time.monotonic() + (challenge_wait if found else 0)
    while found and time.monotonic() < deadline:
        page.idle(2)
        latest = page.main_response()
        if latest and latest["requestId"] != event["requestId"]:
            page.wait_ready(timeout=max(1, deadline - time.monotonic()))
            event = page.main_response()
        html = _html(page)
        found = detect.challenge(event["response"].get("status"), event["response"].get("headers"), html)
    return {"event": event, "html": html, "challenge": found, "ready": ready, "redirects": page.redirects()}


def visit(page: Page, url: str, folder: Path, pacer: Pacer | None = None, tdm_entries=(),
          browser_info: dict | None = None, stop: threading.Event | None = None, meta: dict | None = None,
          origin: dict | None = None) -> dict:
    """Visit `url`, write its snapshot in `folder` and return {'outcome', 'detail', 'elapsed_s', 'meta'}.
    `meta` holds the caller's fields, written first in meta.json; `origin`, the origin of the run."""
    started, t0 = now(), time.monotonic()
    meta = {**(meta or {}), "url_requested": url, "method": "chrome-cdp", "profile": page.profile.name,
            "browser": browser_info or {}, "started_at": started}
    files = {}
    try:
        outcome, detail = _visit(page, url, pacer, tdm_entries, stop, meta, folder, files, t0, origin)
    except CdpError as exc:
        outcome, detail = "failed", f"error CDP: {exc}"
    meta.update({"outcome": outcome, "detail": detail, "files": files, "finished_at": now()})
    with open(folder / "meta.json", "x", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    return {"outcome": outcome, "detail": detail, "elapsed_s": round(time.monotonic() - t0, 1), "meta": meta}


def _body(page: Page, request_id: str, meta: dict) -> bytes:
    """The body of the main document: its original bytes if the profile keeps them."""
    raw = page.raw_body(request_id) if page.profile.evidence else None
    if page.profile.evidence:
        meta["response_body"] = "original" if raw is not None else "decodificado por Chrome (sin los bytes originales)"
    return raw if raw is not None else page.response_body(request_id)


def _visit(page, url, pacer, tdm_entries, stop, meta, folder, files, t0, origin) -> tuple[str, str]:
    wait = pacer.pacing.challenge_wait_s if pacer else DEFAULTS["challenge_wait_s"]
    loaded = load(page, url, wait if page.profile.javascript else 0)
    if "error" in loaded:
        outcome, detail = "failed", loaded["error"]
    else:
        event = loaded["event"]
        response = event["response"]
        status = response.get("status")
        meta.update({
            "url_final": response.get("url"), "redirects": loaded["redirects"],
            "load_complete": loaded["ready"],
            "http": {"status": status, "headers": response.get("headers"),
                     "protocol": response.get("protocol"), "mime": response.get("mimeType"),
                     "remote_ip": response.get("remoteIPAddress"),
                     "from_cache": bool(response.get("fromDiskCache") or response.get("fromServiceWorker"))},
        })
        if page.profile.evidence:
            sent = {k.lower(): v for k, v in page.request_headers(event["requestId"]).items()}
            meta["request_context"] = {"accept_language": sent.get("accept-language"),
                                       "user_agent": sent.get("user-agent"),
                                       "origin": origin if origin is not None else profiles.origin()}
        signals = page.eval(META) or {}
        meta["page_meta"] = signals
        if loaded["challenge"]:
            outcome, detail = "blocked", f"{loaded['challenge']['vendor']}: {loaded['challenge']['evidence']}"
            meta["challenge"] = loaded["challenge"]
            files["response.html"] = write_evidence(folder, "response.html", _body(page, event["requestId"], meta))
        elif status in (404, 410):
            outcome, detail = "gone", f"HTTP {status}"
        elif status and status >= 400:
            outcome, detail = "failed", f"HTTP {status}"
        elif tdm.reserved_by_response(response.get("headers"), signals) \
                or tdm.reserved_by_entries(tdm_entries, response.get("url") or url):
            outcome, detail = "reserved", "reserva TDM (cabecera, meta o tdmrep.json): no se conserva el contenido"
        else:
            page.wait_stable()
            if not page.profile.scroll or (pacer and not pacer.pacing.scroll):
                actions = [{"action": "first_load", "seconds": round(time.monotonic() - t0, 1)}]
            else:
                dwell = pacer.dwell() if pacer else 0.0
                steps = page.scroll_through(budget=dwell * 0.8 if pacer else SINGLE_SCROLL_S,
                                            rng=pacer.rng if pacer else random.Random(), stop=stop)
                page.wait_stable()
                if pacer:
                    page.idle(max(0.0, dwell - (time.monotonic() - t0)), stop)
                actions = [{"action": "scroll", "wheel_steps": steps},
                           {"action": "dwell", "seconds": round(time.monotonic() - t0, 1)}]
            hidden = page.eval(MARK_HIDDEN, timeout=60)
            try:
                dom = page.eval(SERIALIZE, timeout=90)
            finally:
                page.eval(UNMARK_HIDDEN)
            files["response.html"] = write_evidence(folder, "response.html", _body(page, event["requestId"], meta))
            files["dom.html"] = write_evidence(folder, "dom.html", dom["html"].encode("utf-8"))
            meta["dom"] = {"title": dom["title"], "charset": dom["charset"], "elements": dom["elements"],
                           "shadow_roots": dom["shadow_roots"], "hidden_roots": hidden}
            meta["actions"] = actions
            outcome, detail = "captured", dom["title"][:80]
    return outcome, detail
