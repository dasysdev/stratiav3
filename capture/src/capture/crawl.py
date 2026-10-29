"""Batch capture: one thread and one window per site, sites in parallel, at a reader's pace.

Each site sees one reader at a time; the total speeds up with the number of sites. The caller
(the MPIR, the training of the demand model) owns the inventory: it gives the items of each
site, where each snapshot goes and what to do with each result. The capture profile is the
caller's (`reader` by default); one with a fresh context opens a window per page, so that no
page inherits the state of the one before. One that keeps evidence consults the origin of the
requests once per run.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from . import profiles
from .browser import Browser
from .pacing import Pacer, Pacing
from .profiles import Profile
from .robots import Robots
from .visit import visit


@dataclass
class SiteRun:
    key: str                                   # name of the site in messages
    robots: Robots
    tdm_entries: list
    items: list                                # dicts with a "url"
    folder_for: Callable[[dict], Path]         # snapshot folder of an item
    on_result: Callable[[dict, dict], None]    # result: outcome, detail, elapsed_s, meta, folder
    meta_for: Callable[[dict], dict] = field(default=lambda item: {})
    visits_today: Callable[[], int] = field(default=lambda: 0)


def run_parallel(jobs: dict, stop: threading.Event) -> None:
    """Run `jobs` ({name: callable}) in threads; Ctrl+C asks them to stop."""
    threads = [threading.Thread(target=fn, name=name, daemon=True) for name, fn in jobs.items()]
    for t in threads:
        t.start()
    try:
        while any(t.is_alive() for t in threads):
            for t in threads:
                t.join(timeout=0.5)
    except KeyboardInterrupt:
        stop.set()
        for t in threads:
            t.join(timeout=30)


def crawl(runs: list[SiteRun], browser: Browser, pacing: Pacing, out, stop: threading.Event,
          max_per_site: int | None = None, ignore_hours: bool = False, profile: str | Profile | None = None) -> None:
    chosen = profiles.get(profile)
    origin = profiles.origin() if chosen.evidence else None
    run_parallel({run.key: _job(run, browser, pacing, out, stop, max_per_site, ignore_hours, chosen, origin)
                  for run in runs}, stop)


def _job(run: SiteRun, browser, pacing, out, stop, max_per_site, ignore_hours, profile, origin):
    def work():
        pacer = Pacer(pacing, crawl_delay=run.robots.crawl_delay())
        page = browser.new_window(profile)
        done = 0
        try:
            for i, item in enumerate(run.items):
                if stop.is_set():
                    break
                if not ignore_hours and not pacing.within_hours():
                    out(f"{run.key}: fuera del horario {pacing.hours[0]}-{pacing.hours[1]} h; se para")
                    break
                if run.visits_today() >= pacing.daily_cap:
                    out(f"{run.key}: tope diario de {pacing.daily_cap} visitas; se para")
                    break
                if max_per_site is not None and done >= max_per_site:
                    break
                if not run.robots.allowed(item["url"]):
                    run.on_result(item, {"outcome": "disallowed", "detail": "robots.txt", "folder": None})
                    continue
                folder = run.folder_for(item)
                meta = run.meta_for(item)
                if profile.evidence:
                    meta = {**meta, "robots_bots": run.robots.by_bot(item["url"], profiles.BOTS)}
                if profile.fresh_context and done:
                    browser.close_window(page)
                    page = browser.new_window(profile)
                result = visit(page, item["url"], folder, pacer, run.tdm_entries, browser.info, stop, meta, origin)
                done += 1
                run.on_result(item, {**result, "folder": folder})
                if result["outcome"] == "blocked":
                    out(f"{run.key}: bloqueo; se para este sitio")
                    break
                if i < len(run.items) - 1:
                    page.idle(pacer.pause(), stop)
        except Exception as exc:  # noqa: BLE001 - one site must not stop the others
            out(f"{run.key}: error: {exc}")
        finally:
            browser.close_window(page)
            out(f"{run.key}: {done} visitas en esta ejecución")

    return work
