"""Capture of the training catalog (T-025, D-053): the pages of a selection in one batch of the
capture engine (crawl), at the pace of the store's spec. Each captured page becomes
var/pages/ID.html, like taxo page fetch; a page that no longer exists, or that the store
excludes, is replaced by a reserve of its type.

The log of each selection (var/training/<store>/capture-<selection>.jsonl) makes the batch
resumable: what was captured or ruled out is not visited again, and a block or a failure is
retried in the next run. It also counts the visits of the day for the daily cap.
"""
from __future__ import annotations

import json
import threading
from collections import Counter
from datetime import date
from pathlib import Path

from .. import pages
from .selection import DISCOVERIES, SelectionError, shown

FINAL = ("captured", "gone", "disallowed", "reserved")  # not visited again


def log_path(selection: dict, selection_file: Path) -> Path:
    return DISCOVERIES / selection["store"] / f"capture-{Path(selection_file).stem}.jsonl"


def read_log(path: Path) -> list:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def categories_of(selection: dict, pilot_only: bool) -> list:
    return [c for c in selection["categories"] if c["pilot"] or not pilot_only]


class Batch:
    """The pages still to visit, a few per type, and the reserves left for each type."""

    def __init__(self, selection: dict, log: list, pilot_only: bool) -> None:
        final = {r["id"] for r in log if r["outcome"] in FINAL}
        captured = {r["id"] for r in log if r["outcome"] == "captured"}
        self.items, self.spare = [], {}
        for c in categories_of(selection, pilot_only):
            candidates = [{**p, "category": c["category"]} for p in c["pages"] + c["reserves"]]
            need = max(0, len(c["pages"]) - sum(p["id"] in captured for p in candidates))
            left = [p for p in candidates if p["id"] not in final]
            self.items += left[:need]
            self.spare[c["category"]] = left[need:]

    def replace(self, item: dict) -> dict | None:
        spare = self.spare.get(item["category"]) or []
        return spare.pop(0) if spare else None


def capture(spec: dict, selection_file: Path, pilot_only: bool = False, max_visits: int | None = None,
            ignore_hours: bool = False, out=print, browser=None) -> list:
    """Visit what is pending of the selection; returns the records of this run."""
    from ..capture import profile
    from ..capture.browser import Browser
    from ..capture.crawl import SiteRun, crawl
    from ..capture.files import now, stamp, unique_dir, write_json
    from ..capture.legitimacy import access
    from ..capture.pacing import Pacing

    selection = json.loads(Path(selection_file).read_text(encoding="utf-8"))
    log = log_path(selection, selection_file)
    batch = Batch(selection, read_log(log), pilot_only)
    if not batch.items:
        out("nada pendiente en la selección")
        return []
    pacing = Pacing.from_plan(spec)
    own = browser is None
    if own:
        browser = Browser(profile())
        browser.start()
    records, lock = [], threading.Lock()
    try:
        evidence = DISCOVERIES / selection["store"] / f"access-{stamp()}"
        evidence.mkdir(parents=True)
        page = browser.new_window()
        try:
            robots, entries, summary = access(page, spec["base_url"], evidence)
        finally:
            browser.close_window(page)
        write_json(evidence / "access.json", summary)
        if robots.mode == "unreachable":
            raise SelectionError(f"robots.txt de {spec['base_url']} inaccesible: no se captura nada")

        def visits_today() -> int:
            today = date.today().isoformat()
            return sum(r["at"].startswith(today) and r["outcome"] != "disallowed" for r in read_log(log))

        def on_result(item: dict, result: dict) -> None:
            record = {"id": item["id"], "url": item["url"], "category": item["category"],
                      "outcome": result["outcome"], "detail": result["detail"], "at": now(),
                      "elapsed_s": result.get("elapsed_s"),
                      "snapshot": shown(result["folder"]) if result.get("folder") else None}
            if result["outcome"] == "captured":
                pages.freeze(item["id"], item["url"], result["folder"], result["meta"],
                             {"selection": shown(selection_file), "category": item["category"]})
            elif result["outcome"] in ("gone", "disallowed", "reserved"):
                spare = batch.replace(item)
                if spare:
                    run.items.append(spare)
                    record["replaced_by"] = spare["id"]
            with lock:
                with open(log, "a", encoding="utf-8") as f:
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
                records.append(record)
            out(f"{item['id']}: {result['outcome']} — {result['detail']}")

        run = SiteRun(key=selection["store"], robots=robots, tdm_entries=entries, items=batch.items,
                      folder_for=lambda item: unique_dir(pages.PAGES / item["id"]), on_result=on_result,
                      meta_for=lambda item: {"training": {"selection": shown(selection_file),
                                                          "category": item["category"]}},
                      visits_today=visits_today)
        crawl([run], browser, pacing, out, threading.Event(), max_visits, ignore_hours)
    finally:
        if own:
            browser.stop()
    return records


def status(selection: dict, selection_file: Path, pilot_only: bool = False) -> dict:
    """Last result of each page and pages captured by type, against what each type needs."""
    last = {}
    for r in read_log(log_path(selection, selection_file)):
        last[r["id"]] = r
    by_type = {}
    for c in categories_of(selection, pilot_only):
        ids = [p["id"] for p in c["pages"] + c["reserves"]]
        by_type[c["category"]] = (sum(last.get(i, {}).get("outcome") == "captured" for i in ids), len(c["pages"]))
    return {"outcomes": dict(Counter(r["outcome"] for r in last.values())), "types": by_type,
            "captured": sum(n for n, _ in by_type.values()), "target": sum(t for _, t in by_type.values())}
