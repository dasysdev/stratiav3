"""Files of the MPIR (no database). What a person defines is versioned, under MPIR_STUDIES
(default demand-engine/studies/); what the engine produces is disposable, under MPIR_VAR
(default demand-engine/var/mpir/). The Chrome profile is the capture engine's
(capture/var/chrome-profile).

  studies/<study>/plan.json               observation plan (class, segments, pacing…)
  studies/<study>/sites/<site>.json       reference site: selection card
  studies/<study>/resources.json          inventory: what is captured and why

  var/mpir/studies/<study>/site-state/<site>.json
                                          checks and blocks of the site
  var/mpir/studies/<study>/resource-state.json
                                          status, snapshots and last visit of each resource
  var/mpir/studies/<study>/checks/<site>/<at>/       evidence of a check (robots.txt, tdmrep.json)
  var/mpir/studies/<study>/snapshots/<site>/<resource>/<at>/   snapshot of a visit
  var/mpir/studies/<study>/discovery/<site>-<at>.json
  var/mpir/studies/<study>/log.jsonl      one line per visit, check and change

The API joins both halves: a site or a resource is read and written whole.
A snapshot directory is never overwritten: each capture creates a new one.
"""
from __future__ import annotations

import json
import os
import threading
from datetime import datetime
from pathlib import Path

from capture import OUTCOMES
from capture.files import now, read_json, unique_dir, write_json
from capture.pacing import DEFAULTS

from .. import ROOT

_LOCK = threading.RLock()

# Resource status → label for reports (MPIR: sampling-capture, «Qué se conserva»)
STATUS = {"pending": "no inspeccionada", **OUTCOMES}
PROFILES = ("product", "category", "comparison", "guide", "faq", "selector", "conditions")
SITE_TYPES = ("especialista", "multimarca", "fabricante", "generalista")


# Fields produced by the engine, kept in var/ (the rest of a site or resource is versioned)
SITE_STATE = ("checks", "blocks", "blocks_history")
RESOURCE_STATE = ("status", "snapshots", "last")


def var_root() -> Path:
    return Path(os.environ.get("MPIR_VAR") or ROOT / "var/mpir")


def studies_root() -> Path:
    return Path(os.environ.get("MPIR_STUDIES") or ROOT / "studies")


class StoreError(RuntimeError):
    pass


class Study:
    def __init__(self, study_id: str) -> None:
        self.id = study_id
        self.home = studies_root() / study_id        # versioned definition
        self.dir = var_root() / "studies" / study_id  # state and evidence (disposable)
        if not (self.home / "plan.json").exists():
            raise StoreError(f"no existe el estudio {study_id}; créalo con: mpir study new {study_id}")

    @staticmethod
    def ids() -> list[str]:
        root = studies_root()
        return sorted(p.name for p in root.iterdir() if (p / "plan.json").exists()) if root.exists() else []

    @staticmethod
    def create(study_id: str, class_name: str, note: str = "") -> "Study":
        path = studies_root() / study_id / "plan.json"
        if path.exists():
            raise StoreError(f"el estudio {study_id} ya existe")
        write_json(path, {
            "id": study_id, "created": now(), "class": class_name, "note": note,
            "taxonomy": [], "segments": [], "market": "ES", "language": "es",
            "profiles": list(PROFILES), "coverage_matrix": {},
            "pacing": dict(DEFAULTS), "check_max_age_days": 7, "block_retry_hours": 6,
        })
        return Study(study_id)

    # ------------------------------------------------------------ plan and sites
    def plan(self) -> dict:
        return read_json(self.home / "plan.json")

    def site_path(self, site_id: str) -> Path:
        return self.home / "sites" / f"{site_id}.json"

    def _site_state_path(self, site_id: str) -> Path:
        return self.dir / "site-state" / f"{site_id}.json"

    def sites(self) -> dict[str, dict]:
        folder = self.home / "sites"
        return {p.stem: self.site(p.stem) for p in sorted(folder.glob("*.json"))} if folder.exists() else {}

    def site(self, site_id: str) -> dict:
        card = read_json(self.site_path(site_id))
        if card is None:
            raise StoreError(f"no existe el referente {site_id} en {self.id}")
        return {**card, "checks": [], "blocks": [], **read_json(self._site_state_path(site_id), {})}

    def save_site(self, site: dict) -> None:
        with _LOCK:
            write_json(self.site_path(site["id"]), {k: v for k, v in site.items() if k not in SITE_STATE})
            write_json(self._site_state_path(site["id"]), {k: site[k] for k in SITE_STATE if k in site})

    def update_site(self, site_id: str, fn) -> dict:
        with _LOCK:
            site = self.site(site_id)
            fn(site)
            self.save_site(site)
            return site

    # ------------------------------------------------------------ resources
    def resources(self) -> list[dict]:
        inventory = read_json(self.home / "resources.json", {"resources": []})["resources"]
        state = read_json(self.dir / "resource-state.json", {})
        return [{**r, "status": "pending", "snapshots": [], "last": None, **state.get(r["id"], {})} for r in inventory]

    def _save_resources(self, resources: list[dict]) -> None:
        write_json(self.home / "resources.json",
                   {"resources": [{k: v for k, v in r.items() if k not in RESOURCE_STATE} for r in resources]})
        write_json(self.dir / "resource-state.json",
                   {r["id"]: {k: r[k] for k in RESOURCE_STATE if k in r} for r in resources})

    def add_resources(self, site_id: str, urls: list[str], profile: str, segment: str = "",
                      reason: str = "") -> tuple[list[dict], list[str]]:
        """Add new URLs to the inventory; return (added, already present)."""
        with _LOCK:
            resources = self.resources()
            known = {r["url"] for r in resources}
            numbers = [int(r["id"].rsplit("-", 1)[1]) for r in resources if r["site"] == site_id]
            n = max(numbers, default=0)
            added, present = [], []
            for url in urls:
                if url in known:
                    present.append(url)
                    continue
                n += 1
                known.add(url)
                res = {"id": f"{site_id}-{n:03d}", "site": site_id, "url": url, "profile": profile,
                       "segment": segment, "reason": reason, "added": now(), "status": "pending",
                       "snapshots": [], "last": None}
                resources.append(res)
                added.append(res)
            self._save_resources(resources)
            return added, present

    def update_resource(self, resource_id: str, **fields) -> dict:
        with _LOCK:
            resources = self.resources()
            for res in resources:
                if res["id"] == resource_id:
                    snapshot = fields.pop("snapshot", None)
                    if snapshot:
                        res["snapshots"].append(snapshot)
                    res.update(fields)
                    self._save_resources(resources)
                    return res
        raise StoreError(f"no existe el recurso {resource_id}")

    # ------------------------------------------------------------ evidence
    def new_dir(self, *parts: str) -> Path:
        """A new directory named by the current time; never reuses an existing one."""
        return unique_dir(self.dir.joinpath(*parts))

    def log(self, event: str, **fields) -> None:
        with _LOCK:
            self.dir.mkdir(parents=True, exist_ok=True)
            with open(self.dir / "log.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps({"at": now(), "event": event, **fields}, ensure_ascii=False) + "\n")

    def visits_today(self, site_id: str) -> int:
        path = self.dir / "log.jsonl"
        if not path.exists():
            return 0
        today = datetime.now().astimezone().date().isoformat()
        count = 0
        with open(path, encoding="utf-8") as f:
            for line in f:
                ev = json.loads(line)
                if ev.get("event") == "visit" and ev.get("site") == site_id and ev["at"].startswith(today):
                    count += 1
        return count
