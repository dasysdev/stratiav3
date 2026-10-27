"""Seed sets and what the engine keeps of them.

What defines a search goes in git, in demand-engine/paa/ (PAA_SETS overrides it, in tests):
  paa/<set>.json                     the seed set: class, model, rule, market, clicks, seeds

What the engine produces is disposable, in demand-engine/var/paa/sets/<set>/ (PAA_VAR):
  state.json                         status of every seed
  searches/<seed>/<at>/              one search: record.json and dom.html.gz
  questions.json · related.json      consolidated, with their provenance
  log.jsonl                          one line per search and per change
and, for the whole engine (Google blocks the IP, not a set), var/paa/engine.json: the blocks.
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

from .. import ROOT
from ..capture.files import now, read_json, unique_dir, write_evidence, write_json
from .text import norm

DEFAULTS = {
    "market": {"base": "https://www.google.es", "hl": "es", "gl": "es"},
    "clicks": 8,
    "patience": 2,
    "pacing": {
        "pause_s": [5, 5],          # between two searches (decided 2026-10-27)
        "dwell_s": [1.5, 4],        # reading the results before opening the first question
        "long_every": None,         # searches between long pauses, e.g. [12, 18] (None: none).
        "long_pause_s": None,       # e.g. [60, 180]. The first thing to add if Google blocks (README)
        "daily_cap": None,          # searches per day, all sets together (None: no cap)
        "hours": None,              # local hours allowed, [start, end) (None: any hour)
        "timezone": "Europe/Madrid",
    },
    "block_backoff": {              # after an HTTP 429, before giving up (decided 2026-10-27)
        "first_s": 60,              # first wait, if Google does not say how long (Retry-After)
        "factor": 1.5,              # each wait, 50 % longer than the previous one
        "retries": 5,
        "max_wait_s": 3600,         # a longer Retry-After is not waited for: it becomes the block
    },
    "block_retry_hours": 6,
}
STATUS = ("pending", "captured", "blocked", "failed")


class StoreError(Exception):
    pass


def sets_dir() -> Path:
    return Path(os.environ.get("PAA_SETS") or ROOT / "paa")


def var_root() -> Path:
    return Path(os.environ.get("PAA_VAR") or ROOT / "var/paa")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", norm(text)).strip("-") or "consulta"


def merged(base: dict, extra: dict) -> dict:
    out = dict(base)
    for k, v in (extra or {}).items():
        out[k] = merged(base[k], v) if isinstance(v, dict) and isinstance(base.get(k), dict) else v
    return out


class SeedSet:
    def __init__(self, set_id: str) -> None:
        self.id = set_id
        self.file = sets_dir() / f"{set_id}.json"
        self.dir = var_root() / "sets" / set_id
        if not self.file.exists():
            raise StoreError(f"no existe el conjunto {set_id} ({self.file})")

    @staticmethod
    def ids() -> list[str]:
        return sorted(p.stem for p in sets_dir().glob("*.json"))

    # ------------------------------------------------------------ definition
    def definition(self) -> dict:
        data = merged(DEFAULTS, json.loads(self.file.read_text(encoding="utf-8")))
        seeds = data.get("seeds") or []
        keys = [norm(s.get("q", "")) for s in seeds]
        if not seeds or not all(keys):
            raise StoreError(f"{self.file}: cada semilla necesita «q»")
        if len(set(keys)) != len(keys):
            raise StoreError(f"{self.file}: hay semillas repetidas")
        return data

    def seeds(self) -> list[dict]:
        return self.definition()["seeds"]

    # ------------------------------------------------------------ state
    def state(self) -> dict:
        return read_json(self.dir / "state.json", {"seeds": {}})

    def write_state(self, state: dict) -> None:
        write_json(self.dir / "state.json", state)

    def status_of(self, seed: dict, state: dict | None = None) -> str:
        return ((state or self.state())["seeds"].get(norm(seed["q"])) or {}).get("status", "pending")

    def pending(self) -> list[dict]:
        state = self.state()
        return [s for s in self.seeds() if self.status_of(s, state) != "captured"]

    # ------------------------------------------------------------ searches
    def save(self, seed: dict, record: dict, html: str) -> Path:
        folder = unique_dir(self.dir / "searches" / slug(seed["q"]))
        record = {"set": self.id, "group": seed.get("group"), **record, "at": record.get("at") or now()}
        if html:
            record["files"] = {"dom": write_evidence(folder, "dom.html", html.encode("utf-8"))}
        write_json(folder / "record.json", record)
        state = self.state()
        state["seeds"][norm(seed["q"])] = {"status": record["outcome"], "at": record["at"],
                                           "record": str(folder.relative_to(self.dir))}
        self.write_state(state)
        self.log({"event": "search", "query": seed["q"], "outcome": record["outcome"],
                  "questions": len(record.get("questions", [])), "elapsed_s": record.get("elapsed_s")})
        return folder

    def log(self, entry: dict) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        with open(self.dir / "log.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"at": now(), **entry}, ensure_ascii=False) + "\n")

    def records(self) -> list[dict]:
        """The last captured search of every seed, in the order of the set."""
        state, out = self.state(), []
        for seed in self.seeds():
            entry = state["seeds"].get(norm(seed["q"])) or {}
            if entry.get("status") == "captured":
                out.append(read_json(self.dir / entry["record"] / "record.json"))
        return out

    def consolidate(self) -> dict:
        """questions.json and related.json: each text once, with every search that showed it."""
        questions, related = {}, {}
        for r in self.records():
            for q in r.get("questions", []):
                entry = questions.setdefault(norm(q["q"]), {"q": q["q"], "seeds": []})
                entry["seeds"].append({"query": r["query"], "group": r.get("group"), "position": q["position"],
                                       "via": q["via"], "at": r["at"]})
            for i, t in enumerate(r.get("related", []), 1):
                related.setdefault(norm(t), {"text": t, "seeds": []})["seeds"].append(
                    {"query": r["query"], "position": i, "at": r["at"]})
        out = {"set": self.id, "at": now(), "searches": len(self.records()),
               "questions": list(questions.values()), "related": list(related.values())}
        write_json(self.dir / "questions.json", {k: out[k] for k in ("set", "at", "searches", "questions")})
        write_json(self.dir / "related.json", {k: out[k] for k in ("set", "at", "searches", "related")})
        return out

    def searches_since(self, since: datetime) -> int:
        path = self.dir / "log.jsonl"
        if not path.exists():
            return 0
        count = 0
        for line in path.read_text(encoding="utf-8").splitlines():
            entry = json.loads(line)
            if entry.get("event") == "search" and datetime.fromisoformat(entry["at"]) >= since:
                count += 1
        return count


# ---------------------------------------------------------------- blocks (whole engine)
def engine_state() -> dict:
    return read_json(var_root() / "engine.json", {"blocks": [], "blocked_until": None, "stopped": False})


def blocked_now(at: datetime | None = None) -> str | None:
    """Why the engine cannot search now, or None. A block stops every set: Google blocks the IP."""
    state = engine_state()
    if state.get("stopped"):
        return "parado tras dos bloqueos: revisa y ejecuta «paa unblock»"
    until = state.get("blocked_until")
    if until and (at or datetime.now().astimezone()) < datetime.fromisoformat(until):
        return f"bloqueado hasta {until}"
    return None


def block(set_id: str, detail, hours: float) -> None:
    state = engine_state()
    state["blocks"].append({"at": now(), "set": set_id, "detail": detail})
    state["blocked_until"] = (datetime.now().astimezone() + timedelta(hours=hours)).isoformat(timespec="seconds")
    state["stopped"] = len(state["blocks"]) >= 2
    write_json(var_root() / "engine.json", state)


def unblock() -> None:
    write_json(var_root() / "engine.json", {"blocks": [], "blocked_until": None, "stopped": False})


def searches_today(tz) -> int:
    """Searches of every set since midnight (the daily cap is for the whole engine: one IP)."""
    midnight = datetime.now(tz).replace(hour=0, minute=0, second=0, microsecond=0)
    total = 0
    for set_id in SeedSet.ids():
        total += SeedSet(set_id).searches_since(midnight)
    return total
