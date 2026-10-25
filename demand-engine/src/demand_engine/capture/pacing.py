"""A reader's pace for one site: time on each page, pauses, long pauses, daily cap and hours.

Durations are drawn between the bounds with a skew towards the lower one (Beta(2, 3)), so
most pauses are short and a few are long. Crawl-delay raises the pause when it is larger.
"""
from __future__ import annotations

import random
from dataclasses import asdict, dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

DEFAULTS = {
    "dwell_s": [8, 30],          # time on a page, scrolling included
    "pause_s": [20, 60],         # between two pages of the same site
    "long_every": [15, 25],      # pages between long pauses
    "long_pause_s": [120, 300],
    "daily_cap": 150,            # visits per site and day
    "hours": [9, 21],            # local hours allowed: [start, end)
    "timezone": "Europe/Madrid",
    "challenge_wait_s": 20,      # time for a non-interactive challenge to resolve by itself
}


@dataclass
class Pacing:
    dwell_s: list
    pause_s: list
    long_every: list
    long_pause_s: list
    daily_cap: int
    hours: list
    timezone: str
    challenge_wait_s: float

    @classmethod
    def from_plan(cls, plan: dict) -> "Pacing":
        return cls(**{**DEFAULTS, **(plan.get("pacing") or {})})

    def as_dict(self) -> dict:
        return asdict(self)

    def within_hours(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(ZoneInfo(self.timezone))
        start, end = self.hours
        return start <= now.hour < end


def draw(rng: random.Random, bounds) -> float:
    lo, hi = bounds
    return lo + (hi - lo) * rng.betavariate(2, 3)


class Pacer:
    def __init__(self, pacing: Pacing, rng: random.Random | None = None,
                 crawl_delay: float | None = None) -> None:
        self.pacing = pacing
        self.rng = rng or random.Random()
        self.crawl_delay = crawl_delay or 0
        self._since_long = 0
        self._next_long = self.rng.randint(*pacing.long_every)

    def dwell(self) -> float:
        return draw(self.rng, self.pacing.dwell_s)

    def pause(self) -> float:
        seconds = max(draw(self.rng, self.pacing.pause_s), self.crawl_delay)
        self._since_long += 1
        if self._since_long >= self._next_long:
            self._since_long = 0
            self._next_long = self.rng.randint(*self.pacing.long_every)
            seconds += draw(self.rng, self.pacing.long_pause_s)
        return seconds
