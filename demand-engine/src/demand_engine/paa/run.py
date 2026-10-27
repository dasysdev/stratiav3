"""Run the pending seeds of a set, one search at a time, at a person's pace.

One window, one Google session: searches never go in parallel (one IP). The run closes any
other tab its Chrome still has (a run cut short leaves its tab behind), opens the home page,
as a person does, and rejects consent. Between searches there is a pause; a long pause every so
often, hours and a daily cap apply only if the set sets them. A challenge (/sorry/, CAPTCHA,
403/429) stops the whole engine (Google blocks the IP, not a set): it is retried after
`block_retry_hours`, and after a second block it waits for «paa unblock».

A page that stops answering (an evaluation without reply) is `failed`, not a block: it was the
AI answers' rendering in a Chrome without GPU (2026-10-27), now blocked (serp.Answers). The
run stops and the seed stays pending.
"""
from __future__ import annotations

import random
from datetime import datetime
from zoneinfo import ZoneInfo

from ..capture.browser import Browser
from ..capture.cdp import CdpError
from ..capture.pacing import draw
from . import serp, store
from .store import SeedSet, searches_today

UNRESPONSIVE = "la página dejó de responder (hilo principal ocupado)"


def run(seedset: SeedSet, browser: Browser, max_searches: int | None = None, ignore_hours: bool = False,
        rng: random.Random | None = None, say=print) -> dict:
    rng = rng or random.Random()
    spec = seedset.definition()
    pacing, market = spec["pacing"], spec["market"]
    tz = ZoneInfo(pacing["timezone"])
    summary = {"captured": 0, "blocked": 0, "failed": 0, "stopped": None}
    reason = store.blocked_now()
    if reason:
        summary["stopped"] = reason
        return summary
    pending = seedset.pending()[:max_searches] if max_searches else seedset.pending()
    if not pending:
        summary["stopped"] = "no quedan semillas pendientes"
        return summary

    page = browser.new_window()
    closed = browser.close_other_tabs(page)
    if closed:
        seedset.log({"event": "tabs", "closed": closed})
    answers = serp.Answers()
    try:
        try:
            page.navigate(f"{market['base']}/?hl={market['hl']}")
            page.wait_ready()
            if serp.reject_consent(page, rng):
                seedset.log({"event": "consent", "action": "Rechazar todo"})
            page.idle(rng.uniform(2, 5))
        except CdpError as exc:
            summary.update(failed=1, stopped=f"portada: {UNRESPONSIVE} ({exc})")
            return summary
        long_every = pacing.get("long_every")
        next_long = rng.randint(*long_every) if long_every else None
        for i, seed in enumerate(pending):
            hours = pacing.get("hours")
            if hours and not ignore_hours and not (hours[0] <= datetime.now(tz).hour < hours[1]):
                summary["stopped"] = f"fuera de horario ({hours[0]}–{hours[1]} h)"
                break
            if pacing.get("daily_cap") and searches_today(tz) >= pacing["daily_cap"]:
                summary["stopped"] = f"tope diario alcanzado ({pacing['daily_cap']} búsquedas)"
                break
            try:
                record, html = serp.search(page, market["base"], seed["q"], market["hl"], market["gl"],
                                           spec["clicks"], rng, pacing["dwell_s"], spec["patience"], answers)
            except CdpError as exc:
                record, html = {"query": seed["q"], "outcome": "failed", "elapsed_s": None,
                                "detail": f"{UNRESPONSIVE} ({exc})"}, ""
            record["browser"] = browser.info
            seedset.save(seed, record, html)
            summary[record["outcome"]] += 1
            say(f"  {seed['q']}: {record['outcome']}, {len(record.get('questions', []))} preguntas, "
                f"{record.get('clicks', 0)} clics, {record.get('elapsed_s')} s")
            if record["outcome"] == "blocked":
                store.block(seedset.id, record["detail"], spec["block_retry_hours"])
                seedset.log({"event": "block", "detail": record["detail"]})
                summary["stopped"] = f"bloqueo: {record['detail']}"
                break
            if record["outcome"] == "failed" and str(record.get("detail", "")).startswith(UNRESPONSIVE):
                summary["stopped"] = record["detail"]
                break
            if i < len(pending) - 1:
                pause = draw(rng, pacing["pause_s"])
                if next_long is not None and i + 1 >= next_long:
                    pause += draw(rng, pacing["long_pause_s"])
                    next_long = i + 1 + rng.randint(*long_every)
                page.idle(pause)
    finally:
        browser.close_window(page)
        seedset.consolidate()
    return summary
