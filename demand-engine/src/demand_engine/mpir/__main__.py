"""Capture engine of the MPIR (layer A). Run inside the container: demand-engine/bin/mpir <command>.

Usage:
  mpir study new ID --class TEXT [--note TEXT]   create an observation plan
  mpir study list
  mpir site add ID BASE_URL --type TYPE --reason TEXT [--group TEXT]
                                    add a reference site (selection card)
  mpir site list
  mpir site check [ID ...]          legitimacy: robots.txt, TDM reservations, home page
  mpir site unblock ID              clear the blocks of a site after reviewing them
  mpir discover ID [--match RE] [--follow RE] [--limit N]
                                    candidate URLs from the sitemaps (saved, not added)
  mpir add ID URL... --profile P [--segment S] [--reason R] [--from FILE]
                                    add resources to the inventory
  mpir capture [--site ID ...] [--max N] [--ignore-hours]
                                    visit pending resources, sites in parallel
  mpir ingest ID URL FILE [--profile P]
                                    add a page saved by hand (.mhtml or .html)
  mpir status [--site ID]           coverage by status, verdicts and blocks
  mpir browser                      user agent and signals of the engine's Chrome

The study is -s ID, MPIR_STUDY or the only one that exists. Profiles: product, category,
comparison, guide, faq, selector, conditions. Types: especialista, multimarca, fabricante,
generalista.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import threading
from pathlib import Path
from urllib.parse import urlsplit

from ..capture import profile, sitemaps
from ..capture.browser import Browser, signals
from ..capture.files import now, stamp, write_json
from . import scheduler
from .ingest import ingest
from .store import PROFILES, SITE_TYPES, STATUS, Study, StoreError

def fail(msg: str) -> None:
    sys.exit(f"mpir: {msg}")


def shown(path: Path) -> Path:
    """A path as the user sees it: relative to the project (the container's /work)."""
    try:
        return path.resolve().relative_to(Path.cwd())
    except ValueError:
        return path


def study_of(args) -> Study:
    sid = args.study or os.environ.get("MPIR_STUDY")
    if not sid:
        ids = Study.ids()
        if len(ids) != 1:
            fail("indica el estudio con -s ID (" + (", ".join(ids) or "no hay ninguno: mpir study new") + ")")
        sid = ids[0]
    return Study(sid)


def with_browser(fn):
    browser = Browser(profile())
    browser.start()
    try:
        return fn(browser)
    finally:
        browser.stop()


# ---------------------------------------------------------------- study
def cmd_study_new(args) -> None:
    study = Study.create(args.id, args.class_name, args.note or "")
    print(f"estudio {study.id} creado: {shown(study.home / 'plan.json')}")
    print("completa en el plan los segmentos, la taxonomía de referencia y la matriz de cobertura")


def cmd_study_list(args) -> None:
    for sid in Study.ids():
        plan = Study(sid).plan()
        print(f"{sid}  {plan.get('class')}")


# ---------------------------------------------------------------- sites
def cmd_site_add(args) -> None:
    study = study_of(args)
    if study.site_path(args.id).exists():
        fail(f"el referente {args.id} ya existe")
    parts = urlsplit(args.base_url)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        fail("BASE_URL debe ser como https://www.ejemplo.es")
    study.save_site({"id": args.id, "base_url": f"{parts.scheme}://{parts.netloc}", "type": args.type,
                     "reason": args.reason, "editorial_group": args.group or "", "biases": "",
                     "terms_reviewed": False, "added": now(), "checks": [], "blocks": []})
    study.log("site-add", site=args.id)
    print(f"referente {args.id} añadido; siguiente paso: mpir site check {args.id}")


def cmd_site_list(args) -> None:
    study = study_of(args)
    for sid, site in study.sites().items():
        last = (site.get("checks") or [{}])[-1]
        print(f"{sid:20} {site['base_url']:40} {site['type']:12} {last.get('verdict', 'sin comprobar')}")


def cmd_site_check(args) -> None:
    study = study_of(args)
    ids = args.ids or list(study.sites())
    for sid in ids:
        study.site(sid)
    with_browser(lambda b: scheduler.run_checks(study, ids, b, scheduler.clock, threading.Event()))


def cmd_site_unblock(args) -> None:
    study = study_of(args)

    def clear(site):
        site.setdefault("blocks_history", []).extend(site.get("blocks") or [])
        site["blocks"] = []
    study.update_site(args.id, clear)
    study.log("site-unblock", site=args.id)
    print(f"{args.id}: bloqueos retirados (quedan en blocks_history)")


# ---------------------------------------------------------------- resources
def cmd_discover(args) -> None:
    study = study_of(args)
    site = study.site(args.id)
    checks = site.get("checks") or []
    if not checks or checks[-1]["verdict"] != "ok":
        fail(f"{args.id} necesita una comprobación con veredicto ok: mpir site check {args.id}")
    robots_sitemaps = checks[-1]["robots"]["sitemaps"]

    def run(browser):
        page = browser.new_window()
        try:
            return sitemaps.discover(page, site["base_url"], robots_sitemaps, args.match, args.follow,
                                     args.limit, random.Random())
        finally:
            browser.close_window(page)
    result = with_browser(run)
    out = study.dir / "discovery" / f"{args.id}-{stamp()}.json"
    write_json(out, {"site": args.id, "at": now(), "match": args.match, "follow": args.follow, **result})
    for s in result["sitemaps"]:
        print(f"  {s['sitemap']}: {s['kind'] or s['error'] or s['status']} {s['total'] or ''}")
    print(f"{len(result['urls'])} URL candidatas en {shown(out)}")
    for u in result["urls"][:20]:
        print(f"  {u['loc']}")


def cmd_add(args) -> None:
    study = study_of(args)
    study.site(args.id)
    urls = list(args.urls)
    if args.from_file:
        urls += [line.strip() for line in Path(args.from_file).read_text(encoding="utf-8").splitlines()
                 if line.strip() and not line.startswith("#")]
    base = study.site(args.id)["base_url"]
    foreign = [u for u in urls if urlsplit(u)[:2] != urlsplit(base)[:2]]
    if foreign:
        fail(f"URL fuera de {base}: {foreign[0]}")
    added, present = study.add_resources(args.id, urls, args.profile, args.segment or "", args.reason or "")
    study.log("add", site=args.id, resources=[r["id"] for r in added])
    print(f"{len(added)} recursos añadidos, {len(present)} ya estaban")


def cmd_capture(args) -> None:
    study = study_of(args)
    ids = args.sites or list(study.sites())
    with_browser(lambda b: scheduler.run_capture(study, ids, b, scheduler.clock, threading.Event(),
                                                  args.max, args.ignore_hours))


def cmd_ingest(args) -> None:
    study = study_of(args)
    result = ingest(study, args.id, args.url, Path(args.file), args.profile)
    print(f"{result['resource']}: instantánea manual en {result['snapshot']}")


def cmd_status(args) -> None:
    study = study_of(args)
    plan = study.plan()
    print(f"Estudio {study.id} — {plan.get('class')}")
    resources = study.resources()
    for sid, site in study.sites().items():
        if args.site and sid != args.site:
            continue
        last = (site.get("checks") or [{}])[-1]
        mine = [r for r in resources if r["site"] == sid]
        counts = {s: sum(1 for r in mine if r["status"] == s) for s in STATUS}
        reason = scheduler.capturable(study, site)
        print(f"\n{sid} ({site['base_url']}) · veredicto {last.get('verdict', 'sin comprobar')}"
              f" {('del ' + last['at'][:16]) if last.get('at') else ''} · bloqueos {len(site.get('blocks') or [])}")
        if reason:
            print(f"  no capturable: {reason}")
        for flag in last.get("flags", []):
            print(f"  · {flag}")
        for status, label in STATUS.items():
            if counts[status]:
                print(f"  {counts[status]:4} {label}")
    print(f"\nTotal: {len(resources)} recursos")


def cmd_browser(args) -> None:
    print(json.dumps(with_browser(signals), ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser(prog="mpir", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-s", "--study")
    sub = ap.add_subparsers(dest="cmd", required=True)

    study = sub.add_parser("study").add_subparsers(dest="sub", required=True)
    p = study.add_parser("new"); p.add_argument("id"); p.add_argument("--class", dest="class_name", required=True)
    p.add_argument("--note"); p.set_defaults(func=cmd_study_new)
    study.add_parser("list").set_defaults(func=cmd_study_list)

    site = sub.add_parser("site").add_subparsers(dest="sub", required=True)
    p = site.add_parser("add"); p.add_argument("id"); p.add_argument("base_url")
    p.add_argument("--type", choices=SITE_TYPES, required=True); p.add_argument("--reason", required=True)
    p.add_argument("--group"); p.set_defaults(func=cmd_site_add)
    site.add_parser("list").set_defaults(func=cmd_site_list)
    p = site.add_parser("check"); p.add_argument("ids", nargs="*"); p.set_defaults(func=cmd_site_check)
    p = site.add_parser("unblock"); p.add_argument("id"); p.set_defaults(func=cmd_site_unblock)

    p = sub.add_parser("discover"); p.add_argument("id"); p.add_argument("--match"); p.add_argument("--follow")
    p.add_argument("--limit", type=int, default=500); p.set_defaults(func=cmd_discover)
    p = sub.add_parser("add"); p.add_argument("id"); p.add_argument("urls", nargs="*")
    p.add_argument("--profile", choices=PROFILES, required=True); p.add_argument("--segment")
    p.add_argument("--reason"); p.add_argument("--from", dest="from_file"); p.set_defaults(func=cmd_add)
    p = sub.add_parser("capture"); p.add_argument("--site", dest="sites", action="append")
    p.add_argument("--max", type=int); p.add_argument("--ignore-hours", action="store_true")
    p.set_defaults(func=cmd_capture)
    p = sub.add_parser("ingest"); p.add_argument("id"); p.add_argument("url"); p.add_argument("file")
    p.add_argument("--profile", choices=PROFILES, default="product"); p.set_defaults(func=cmd_ingest)
    p = sub.add_parser("status"); p.add_argument("--site"); p.set_defaults(func=cmd_status)
    sub.add_parser("browser").set_defaults(func=cmd_browser)

    args = ap.parse_args()
    try:
        args.func(args)
    except StoreError as exc:
        fail(str(exc))


if __name__ == "__main__":
    main()
