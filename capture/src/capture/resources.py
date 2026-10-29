"""Access to the resources of an audit by a list of URLs (the images of the markup, which
web-audit extracts): each URL asked for once with GET, its responses cut after the headers.
capture does not read the markup: the list is the caller's.

  resources.jsonl            the journal: a line per run, per host and per URL
  resources.json             the manifest: the runs, the robots.txt of each host and the record
                             of each URL (written at the end of each run)
  resources/sites/<host>/    robots.txt and tdmrep.json of each host the audit did not hold yet

The record of a URL: its outcome, the status and headers of the last response, the redirects
(status and headers of each) and the final URL. No byte of a body is kept, nor read: Chrome
aborts the last response after its headers (Page.heads). Outcomes:
  answered     a response, of any status (a 404 or a 403 is a fact for web-audit)
  failed       no response (network error, timeout)
  disallowed   robots.txt does not allow it to our bot (or is unreachable): not asked for; the
               record carries the rule
  reserved     a TDM reservation of its host (tdmrep.json) or in the headers of its response
  blocked      a 429: the run stops; a later run asks for it again
  invalid      not an http(s) URL: not asked for

robots.txt of each host: the one the crawl kept (sites/ of its runs), with the status the crawl
recorded, if the crawl was on that host; else it is fetched and kept in resources/sites/<host>/.
A TDM reservation, of a host or in a response, stops the run and the audit (D-171): no later
run is made. A URL already recorded is not asked for again (a blocked one is).

Under audit-es: a fresh window and browser context per URL, es-ES, no JavaScript. Pace: at most
one request per second to a host, or its Crawl-delay if larger. The origin of the requests
(RIPEstat) is consulted once per run.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from urllib.parse import urldefrag, urlsplit

from . import profile, profiles, tdm
from .audit import AUDITS, AuditError, Reserved
from .files import now, read_json, write_json
from .robots import Robots

JOURNAL = "resources.jsonl"
MANIFEST = "resources.json"
MIN_INTERVAL_S = 1.0


def _crawl_robots(folder: Path, crawl: dict) -> dict:
    """The robots.txt the crawl kept, by host, with the status it recorded: that of the site
    (crawl.json, or audit.json in an audit made before the spider) and that of each host a page
    of the crawl is on (the page's meta.json)."""
    status = {urlsplit(crawl["site"]).netloc: (crawl.get("legitimacy") or {}).get("robots") or {}}
    for page in crawl.get("pages", []):
        host = urlsplit(page["url"]).netloc
        if host in status or not page.get("snapshot"):
            continue
        meta = read_json(folder / page["snapshot"] / "meta.json") or {}
        robots = (meta.get("legitimacy") or {}).get("robots")
        if robots:
            status[host] = robots
    dirs = [r["sites"] for r in crawl.get("runs", []) if r.get("sites")] or ["sites"]
    known = {}
    for host, summary in status.items():
        if "status" not in summary:
            continue
        name = host.replace(":", "_")
        file = next((f"{d}/{name}/robots.txt" for d in dirs if (folder / d / name / "robots.txt").is_file()), None)
        known[host] = {"status": summary["status"], "mode": summary.get("mode"), "file": file, "source": "crawl"}
    return known


def _load(folder: Path) -> tuple[list, dict, dict]:
    """Runs, hosts and records of the journal (the last record of a URL wins)."""
    runs, hosts, records = [], {}, {}
    path = folder / JOURNAL
    if path.is_file():
        for raw in path.read_text(encoding="utf-8").splitlines():
            try:
                line = json.loads(raw)
            except ValueError:   # a line cut short by a hard stop
                continue
            if "run" in line:
                runs.append(line["run"])
            elif "run_end" in line:
                runs[-1].update(line["run_end"])
            elif "host" in line:
                hosts[line["host"]["host"]] = line["host"]
            elif "resource" in line:
                records[line["resource"]["url"]] = line["resource"]
    return runs, hosts, records


def run(audit_id: str, urls: list[str], browser=None, min_interval_s: float = MIN_INTERVAL_S, out=print) -> dict:
    """Ask for each URL of `urls` not recorded yet in the audit and return the manifest, written
    in resources.json."""
    from .browser import Browser
    from .legitimacy import access

    folder = AUDITS / audit_id
    if not (folder / "audit.json").is_file():
        raise AuditError(f"no hay auditoría {audit_id} con sus páginas elegidas: primero, pages audit {audit_id}")
    crawl = read_json(folder / "crawl.json") or read_json(folder / "audit.json")
    if crawl.get("reservation"):
        raise Reserved(crawl["reservation"])
    runs, hosts, records = _load(folder)
    reservation = next((r["reservation"] for r in reversed(runs) if r.get("reservation")), None)
    if reservation:
        raise Reserved(reservation)
    known = _crawl_robots(folder, crawl)
    wanted = list(dict.fromkeys(urldefrag(u.strip())[0] for u in urls if u.strip()))
    asked = [u for u in wanted if u not in records or records[u]["outcome"] == "blocked"]

    this_run = {"run": len(runs) + 1, "started_at": now(), "profile": profiles.AUDIT_ES.name,
                "given": len(wanted), "asked": len(asked), "origin": profiles.origin() if asked else None}
    journal = open(folder / JOURNAL, "a", encoding="utf-8")

    def write(line: dict) -> None:
        journal.write(json.dumps(line, ensure_ascii=False) + "\n")
        journal.flush()

    write({"run": this_run})
    runs.append(this_run)
    stop = {"stopped": None, "reservation": None, "interrupted": False}
    rules: dict[str, tuple] = {}   # host → (Robots, TDMRep entries)
    last: dict[str, float] = {}
    own = browser is None and bool(asked)
    if own:
        browser = Browser(profile())
        browser.start()

    def site(url: str) -> tuple:
        parts = urlsplit(url)
        host = parts.netloc
        if host in rules:
            return rules[host]
        if host in known or host in hosts:   # kept by the crawl or by an earlier run
            entry = known.get(host) or hosts[host]["robots"]
            text = (folder / entry["file"]).read_text(encoding="utf-8", errors="replace") if entry["file"] else None
            entries = ((hosts.get(host) or {}).get("tdmrep") or {}).get("entries") or []
            rules[host] = (Robots(text, entry["status"]), entries)
            return rules[host]
        where = folder / "resources/sites" / host.replace(":", "_")
        where.mkdir(parents=True, exist_ok=True)
        window = browser.new_window(profiles.AUDIT_ES)
        try:
            robots, entries, summary = access(window, f"{parts.scheme}://{host}", where)
        finally:
            browser.close_window(window)
        file = where / "robots.txt"
        entry = {"host": host, "robots": {**summary["robots"], "file": str(file.relative_to(folder)) if file.is_file() else None,
                                          "source": "resources"},
                 "tdmrep": summary.get("tdmrep")}
        hosts[host] = entry
        write({"host": entry})
        rules[host] = (robots, entries)
        return rules[host]

    try:
        for url in asked:
            record = {"url": url, "run": this_run["run"], "host": urlsplit(url).netloc}
            parts = urlsplit(url)
            if parts.scheme not in ("http", "https") or not parts.netloc:
                record.update({"outcome": "invalid", "detail": "no es una URL http(s)"})
            else:
                robots, entries = site(url)
                allowed, rule = robots.decision(url)
                if tdm.reserving(entries):
                    record.update({"outcome": "reserved", "detail": "reserva TDM (tdmrep.json del host)"})
                    stop["reservation"] = {"where": record["host"], "url": url, "source": "tdmrep.json",
                                           "file": f"resources/sites/{record['host'].replace(':', '_')}/tdmrep.json",
                                           "entries": tdm.reserving(entries)}
                elif not allowed:
                    record.update({"outcome": "disallowed", "rule": rule,
                                   "detail": "robots.txt inaccesible" if robots.mode == "unreachable" else "robots.txt"})
                else:
                    record.update(_ask(browser, url, max(min_interval_s, robots.crawl_delay() or 0), last))
                    if record["outcome"] == "answered" and tdm.reserved_by_response(record["headers"], None):
                        record.update({"outcome": "reserved", "detail": "cabecera tdm-reservation"})
                        stop["reservation"] = {"where": url, "url": url, "source": "cabecera tdm-reservation",
                                               **tdm.signals(record["headers"], None)}
                    elif record["outcome"] == "answered" and record["status"] == 429:
                        record["outcome"] = "blocked"
                        stop["stopped"] = f"parado: 429 en {url}"
            records[url] = record
            write({"resource": record})
            out(f"{record['outcome']} {record.get('status') or '-'} {url}")
            if stop["reservation"]:
                stop["stopped"] = f"parado: reserva TDM ({stop['reservation']['source']}); lo pendiente no se pide"
                break
            if stop["stopped"]:
                break
    except KeyboardInterrupt:
        stop["interrupted"] = True
        out("interrumpido: lo pendiente se pide en otra ejecución")
    finally:
        if own:
            browser.stop()
        end = {"finished_at": now(), "stopped": stop["stopped"], "reservation": stop["reservation"],
               "interrupted": stop["interrupted"]}
        this_run.update(end)
        write({"run_end": end})
        journal.close()
        for host in {r["host"] for r in records.values() if r.get("host") in known}:
            hosts.setdefault(host, {"host": host, "robots": known[host]})
        manifest = {"audit": audit_id, "profile": profiles.AUDIT_ES.name, "runs": runs,
                  "hosts": dict(sorted(hosts.items())),
                  "outcomes": {k: sum(r["outcome"] == k for r in records.values())
                               for k in sorted({r["outcome"] for r in records.values()})},
                  "resources": list(records.values()),
                  "stopped": stop["stopped"], "reservation": stop["reservation"]}
        write_json(folder / MANIFEST, manifest)
    return manifest


def _ask(browser, url: str, interval: float, last: dict) -> dict:
    """GET `url` in a fresh window, at most once per `interval` seconds to its host."""
    host = urlsplit(url).netloc
    wait = interval - (time.monotonic() - last.get(host, float("-inf")))
    if wait > 0:
        time.sleep(wait)
    last[host] = time.monotonic()
    requested = now()
    window = browser.new_window(profiles.AUDIT_ES)
    try:
        got = window.heads(url)
    finally:
        browser.close_window(window)
    chain = got["chain"]
    if got["error"]:
        return {"outcome": "failed", "detail": got["error"], "requested_at": requested,
                "redirects": chain}
    final = chain[-1]
    return {"outcome": "answered", "status": final["status"], "url_final": final["url"],
            "headers": final["headers"], "redirects": chain[:-1], "requested_at": requested}
