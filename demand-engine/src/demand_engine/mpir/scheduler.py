"""Runs of the MPIR on the capture engine: checks of the reference sites and capture of the
pending resources of the inventory (capture.crawl: one window per site, sites in parallel).
"""
from __future__ import annotations

import random
import threading
import time
from datetime import datetime, timedelta

from ..capture.browser import Browser
from ..capture.crawl import SiteRun, crawl, run_parallel
from ..capture.legitimacy import check_site
from ..capture.pacing import Pacing
from ..capture.robots import Robots
from .store import STATUS, Study, now


def capturable(study: Study, site: dict) -> str:
    """'' if the site may be captured now, else the reason."""
    plan = study.plan()
    checks = site.get("checks") or []
    if not checks:
        return "sin comprobación de legitimidad: mpir site check " + site["id"]
    last = checks[-1]
    age = datetime.now().astimezone() - datetime.fromisoformat(last["at"])
    if age > timedelta(days=plan.get("check_max_age_days", 7)):
        return f"comprobación de hace {age.days} días: repite mpir site check {site['id']}"
    if last["verdict"] != "ok":
        return f"veredicto «{last['verdict']}» en la última comprobación"
    blocks = site.get("blocks") or []
    if len(blocks) >= 2:
        return "bloqueado dos veces: revisa y usa mpir site unblock " + site["id"]
    if blocks:
        retry = datetime.fromisoformat(blocks[-1]) + timedelta(hours=plan.get("block_retry_hours", 6))
        if datetime.now().astimezone() < retry:
            return f"bloqueado; un reintento a partir de {retry.strftime('%d/%m %H:%M')}"
    return ""


def run_checks(study: Study, site_ids: list[str], browser: Browser, out, stop: threading.Event) -> None:
    pacing = Pacing.from_plan(study.plan())

    def job(site_id: str):
        def work():
            page = browser.new_window()
            try:
                site = study.site(site_id)
                folder = study.new_dir("checks", site_id)
                check = {"at": now(), "evidence": str(folder.relative_to(study.dir)),
                         **check_site(page, site["base_url"], folder, pacing.challenge_wait_s, random.Random())}
                if not site.get("terms_reviewed"):
                    check["flags"].append("condiciones de uso sin revisar (terms_reviewed en la ficha)")
                study.update_site(site_id, lambda s: s.setdefault("checks", []).append(check))
                study.log("check", site=site_id, verdict=check["verdict"], evidence=check["evidence"])
                out(f"{site_id}: veredicto {check['verdict']}")
                for flag in check["flags"]:
                    out(f"{site_id}:   · {flag}")
            except Exception as exc:  # noqa: BLE001 - one site must not stop the others
                out(f"{site_id}: error en la comprobación: {exc}")
            finally:
                browser.close_window(page)
        return work

    run_parallel({sid: job(sid) for sid in site_ids}, stop)


def run_capture(study: Study, site_ids: list[str], browser: Browser, out, stop: threading.Event,
                max_per_site: int | None = None, ignore_hours: bool = False) -> None:
    runs = []
    for site_id in site_ids:
        site = study.site(site_id)
        reason = capturable(study, site)
        retry = bool(site.get("blocks"))
        todo = [r for r in study.resources() if r["site"] == site_id
                and (r["status"] == "pending" or (retry and r["status"] == "blocked"))]
        if reason:
            out(f"{site_id}: no se captura — {reason}")
        elif not todo:
            out(f"{site_id}: nada pendiente")
        else:
            runs.append(_site_run(study, site, todo, out))
    if runs:
        crawl(runs, browser, Pacing.from_plan(study.plan()), out, stop, max_per_site, ignore_hours)


def _site_run(study: Study, site: dict, todo: list, out) -> SiteRun:
    site_id = site["id"]
    check = site["checks"][-1]
    robots_file = study.dir / check["evidence"] / "robots.txt"
    robots = Robots(robots_file.read_text(encoding="utf-8", errors="replace") if robots_file.exists() else "",
                    check["robots"]["status"])

    def on_result(res: dict, result: dict) -> None:
        outcome = result["outcome"]
        last = {"at": now(), "outcome": outcome, "detail": result["detail"]}
        if result["folder"] is None:  # not visited: excluded by robots.txt
            study.update_resource(res["id"], status=outcome, last=last)
            study.log("skip", site=site_id, resource=res["id"], outcome=outcome)
            out(f"{site_id} {res['id']}: {STATUS[outcome]}")
            return
        snapshot = str(result["folder"].relative_to(study.dir))
        study.update_resource(res["id"], status=outcome, snapshot=snapshot, last=last)
        study.log("visit", site=site_id, resource=res["id"], outcome=outcome, snapshot=snapshot,
                  elapsed_s=result["elapsed_s"])
        out(f"{site_id} {res['id']}: {STATUS[outcome]} — {result['detail']} ({result['elapsed_s']} s)")
        if outcome == "blocked":
            study.update_site(site_id, lambda s: s.setdefault("blocks", []).append(now()))

    return SiteRun(
        key=site_id, robots=robots, tdm_entries=(check.get("tdmrep") or {}).get("entries") or [], items=todo,
        folder_for=lambda res: study.new_dir("snapshots", res["site"], res["id"]),
        on_result=on_result,
        meta_for=lambda res: {"study": study.id, "site": res["site"], "resource": res["id"], "profile": res["profile"]},
        visits_today=lambda: study.visits_today(site_id),
    )


def clock(msg: str) -> None:
    print(f"{time.strftime('%H:%M:%S')} {msg}", flush=True)
