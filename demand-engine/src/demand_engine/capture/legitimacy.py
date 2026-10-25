"""Legitimacy of the access to a site, checked before capturing and kept as evidence.

1. robots.txt (RFC 9309, capture.robots): status, Crawl-delay, sitemaps, whether the root is
   allowed and which AI crawlers it excludes (reported for review; they are not us).
2. TDM reservations (capture.tdm): /.well-known/tdmrep.json, header and meta of the home page.
3. Home page, only if robots.txt allows it: challenge, anti-bot vendors, meta robots `noai`.

`access` does 1 and the tdmrep.json of 2 (what any capture needs); `check_site` does all of
it and gives a verdict: ok · reserved (TDM reservation for the site) · blocked (challenge or
403/429) · unreachable (robots.txt 5xx/429 or no answer: RFC 9309 means nothing may be fetched).
"""
from __future__ import annotations

import json
import random
from pathlib import Path

from . import detect, tdm
from .browser import Page
from .files import write_evidence
from .robots import Robots
from .visit import META, load

FETCH = """(async url => {
  try {
    const r = await fetch(url, {credentials: 'include'});
    const text = await r.text();
    return {status: r.status, type: r.headers.get('content-type'), text: text.slice(0, 2000000)};
  } catch (e) { return {status: null, error: String(e)}; }
})(%s)"""


def fetch_text(page: Page, url: str) -> dict:
    """Fetch from the page's own origin (same browser, cookies and fingerprint)."""
    return page.eval(FETCH % json.dumps(url), timeout=60, await_promise=True) or {}


def robots_of(page: Page, base: str) -> tuple[Robots, bytes]:
    nav = page.navigate(base + "/robots.txt")
    if nav.get("errorText"):
        return Robots(None, None), b""
    page.wait_ready(timeout=30)
    event = page.main_response()
    if event is None:
        return Robots(None, None), b""
    body = page.response_body(event["requestId"])
    return Robots(body.decode("utf-8", "replace"), event["response"].get("status")), body


def access(page: Page, base: str, folder: Path) -> tuple[Robots, list, dict]:
    """robots.txt and tdmrep.json of a site, with their evidence in `folder`.
    Returns (robots, TDMRep entries, summary for the record)."""
    robots, raw = robots_of(page, base)
    if raw:
        write_evidence(folder, "robots.txt", raw, compress=False)
    summary = {"robots": {
        "status": robots.status, "mode": robots.mode, "groups": len(robots.groups),
        "crawl_delay": robots.crawl_delay(), "sitemaps": robots.sitemaps,
        "root_allowed": robots.allowed(base + "/"), "ai_blocked": robots.blocked_agents(),
    }}
    if robots.mode == "unreachable":
        return robots, [], summary
    tdmrep = fetch_text(page, base + "/.well-known/tdmrep.json")
    entries = tdm.entries(tdmrep.get("text"), tdmrep.get("status"))
    if tdmrep.get("status") == 200 and tdmrep.get("text"):
        write_evidence(folder, "tdmrep.json", tdmrep["text"].encode("utf-8"), compress=False)
    summary["tdmrep"] = {"status": tdmrep.get("status"), "entries": entries}
    return robots, entries, summary


def check_site(page: Page, base: str, folder: Path, challenge_wait: float, rng: random.Random) -> dict:
    """The full check of a site: {'flags', 'robots', 'tdmrep', 'home', 'verdict'}."""
    base = base.rstrip("/")
    check = {"flags": []}
    robots, entries, summary = access(page, base, folder)
    check.update(summary)
    if robots.mode == "unreachable":
        check["verdict"] = "unreachable"
        check["flags"].append(f"robots.txt inaccesible (HTTP {robots.status}): no se puede capturar nada")
        return check

    home = {}
    if summary["robots"]["root_allowed"]:
        page.idle(rng.uniform(3, 8))
        loaded = load(page, base + "/", challenge_wait)
        if "error" in loaded:
            home = {"error": loaded["error"]}
        else:
            response = loaded["event"]["response"]
            signals = page.eval(META) or {}
            home = {
                "status": response.get("status"), "url_final": response.get("url"),
                "title": detect.title(loaded["html"]), "challenge": loaded["challenge"],
                "antibot": detect.vendors_in(response.get("headers"), page.cookie_names(base + "/"),
                                             loaded["html"]),
                "tdm_header": {k.lower(): v for k, v in (response.get("headers") or {}).items()}.get("tdm-reservation"),
                "meta": signals,
            }
    check["home"] = home

    reserved = tdm.reserved_by_entries(entries, base + "/") or \
        (home and tdm.reserved_by_response({"tdm-reservation": home.get("tdm_header") or ""}, home.get("meta")))
    if reserved:
        check["verdict"] = "reserved"
    elif home.get("challenge"):
        check["verdict"] = "blocked"
    else:
        check["verdict"] = "ok"

    flags = check["flags"]
    if not summary["robots"]["root_allowed"]:
        flags.append("robots.txt excluye la raíz: solo se capturarán las URL que permita")
    if summary["robots"]["ai_blocked"]:
        flags.append("robots.txt excluye a bots de IA (" + ", ".join(summary["robots"]["ai_blocked"])
                     + "): no nos aplica, pero revisa si expresa una reserva")
    if "noai" in str((home.get("meta") or {}).get("robots") or "").lower():
        flags.append("meta robots «noai»: revisa si expresa una reserva")
    if home.get("antibot"):
        flags.append("antibot presente: " + ", ".join(home["antibot"]))
    if home.get("error"):
        flags.append(f"portada no recuperada: {home['error']}")
    return check
