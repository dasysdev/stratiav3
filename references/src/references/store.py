"""Custody of the frozen sources: the registry, the versions and the pinned one (D-149).

The sources are declared in references/sources.json, each with the systems that use it
(`uses`). Each one keeps immutable versions in var/<source>/<version>/: the files as
published plus a MANIFEST.json (origin, size, sha256, fetch date). A new version never
overwrites an existing one, and a fetch whose content equals the latest version is discarded:
a .gz counts by its inflated content and an HTML page by its text. The version every system
works with is pinned in var/pins.json; only `refs pin` changes it, because a new pin obliges
each system of `uses` to review what it built on the previous one. The first version of a
source is pinned automatically. Everything in var/ is disposable: what matters is the version
each citation, model or rule names.

REFS_DIR overrides the directory of the versions and SOURCES_FILE the registry (tests).
"""
import gzip
import hashlib
import json
import os
import re
import shutil
from datetime import date, datetime
from pathlib import Path

from . import ROOT

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class RefsError(LookupError):
    pass


def refs_dir() -> Path:
    return Path(os.environ.get("REFS_DIR") or ROOT / "var")


def sources_file() -> Path:
    return Path(os.environ.get("SOURCES_FILE") or ROOT / "sources.json")


def pins_file() -> Path:
    return refs_dir() / "pins.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dumps(obj) -> bytes:
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True).encode("utf-8")


def today() -> str:
    return date.today().isoformat()


def natural(name: str) -> list:
    """Sort key: 9.0 before 30.1, 2026-10-27 before 2026-11-02."""
    return [(0, int(p), "") if p.isdigit() else (1, 0, p) for p in re.split(r"(\d+)", name)]


# --- Registry -----------------------------------------------------------------

def registry() -> dict:
    """sources.json, checked: {"systems": {name: {"review"}}, "sources": {id: entry}}. Ids are
    kebab-case and unique; every source has a known kind, a title, a URL and the systems that
    use it, each one declared with how it reviews a new pin."""
    from .kinds import KINDS
    data = json.loads(sources_file().read_text(encoding="utf-8"))
    systems = data.get("systems") or {}
    out, errors = {}, []
    errors += [f"sistema {name}: falta review" for name, s in systems.items() if not s.get("review")]
    for i, entry in enumerate(data.get("sources") or [], 1):
        sid = entry.get("id") or f"#{i}"
        if not ID_RE.match(sid):
            errors.append(f"{sid}: el id ha de ser kebab-case")
        elif sid in out:
            errors.append(f"{sid}: id repetido")
        if entry.get("kind") not in KINDS:
            errors.append(f"{sid}: kind «{entry.get('kind')}» desconocido ({', '.join(KINDS)})")
        else:
            for field in KINDS[entry["kind"]].fields:
                given = sum(bool(entry.get(f)) for f in field.split("|"))
                if given != 1:
                    errors.append(f"{sid}: " + (f"falta {field.replace('|', ' o ')}" if not given
                                                else f"solo uno de {field.replace('|', ', ')}"))
        errors += [f"{sid}: falta {key}" for key in ("title", "url", "uses") if not entry.get(key)]
        errors += [f"{sid}: uses nombra un sistema no declarado: {name}"
                   for name in entry.get("uses") or [] if name not in systems]
        out[sid] = entry
    if errors:
        raise RefsError(f"{sources_file().name}:\n  " + "\n  ".join(errors))
    return {"systems": systems, "sources": out}


def sources() -> dict:
    return registry()["sources"]


def used_by(system: str) -> set:
    return {sid for sid, s in sources().items() if system in s["uses"]}


# --- Versions -----------------------------------------------------------------

def versions(source: str) -> list:
    folder = refs_dir() / source
    if not folder.exists():
        return []
    return sorted((p.name for p in folder.iterdir() if (p / "MANIFEST.json").exists()), key=natural)


def manifest(source: str, version: str) -> dict:
    return json.loads((refs_dir() / source / version / "MANIFEST.json").read_text(encoding="utf-8"))


def latest_manifest(source: str):
    found = versions(source)
    return manifest(source, found[-1]) if found else None


def pins(system: str = None) -> dict:
    """Pinned version of each source; with `system`, only of the sources it uses."""
    path = pins_file()
    current = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if system is None:
        return current
    mine = used_by(system)
    return {sid: v for sid, v in current.items() if sid in mine}


def save_pins(data: dict) -> None:
    pins_file().parent.mkdir(parents=True, exist_ok=True)
    pins_file().write_bytes(dumps(data) + b"\n")


def pinned(source: str) -> Path:
    """Folder of the pinned version of `source`."""
    current = pins()
    if source not in current:
        raise RefsError(f"{source} no está fijada; ejecuta references/bin/refs status")
    folder = refs_dir() / source / current[source]
    if not folder.exists():
        raise RefsError(f"{source} {current[source]} está fijada pero no está en references/var; "
                        f"descárgala con references/bin/refs fetch {source}")
    return folder


def entry(path: str, data: bytes, origin: str, **extra) -> dict:
    """Manifest entry of a file. A .gz also counts by its inflated content (content_sha256)."""
    out = {"path": path, "origin": origin, "size": len(data), "sha256": sha256(data)}
    if path.endswith(".gz"):
        out["content_sha256"] = sha256(gzip.decompress(data))
    return {**out, **extra}


def fingerprint(files: list) -> list:
    """What counts as content: the inflated bytes of a .gz, else the bytes; an HTML page counts
    by its text (counted_by), not by its markup."""
    return sorted((f["path"], f.get("content_sha256") or f["sha256"]) for f in files if "counted_by" not in f)


class Version:
    """A version being written: files land in a partial folder renamed on commit. Errors of a
    partial download (`errors`) are kept in the manifest and compared like the files."""

    def __init__(self, source: str, version: str, origin: dict):
        self.source, self.version, self.origin = source, version, origin
        self.tmp = refs_dir() / source / f".partial-{version}"
        shutil.rmtree(self.tmp, ignore_errors=True)
        self.tmp.mkdir(parents=True)
        self.files, self.errors = [], []

    def add(self, path: str, data: bytes, origin: str, **extra) -> dict:
        return self.put(path, data, entry(path, data, origin, **extra))

    def put(self, path: str, data: bytes, item: dict) -> dict:
        """Write a file whose manifest entry is already made (see entry)."""
        target = self.tmp / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        self.files.append(item)
        return item

    def commit(self) -> bool:
        """Write the version. False, writing nothing, if its content equals the latest one."""
        previous = latest_manifest(self.source)
        if previous and fingerprint(previous["files"]) == fingerprint(self.files) \
                and previous.get("errors", []) == sorted(self.errors):
            self.discard()
            print(f"{self.source}: sin cambios respecto a {previous['version']}; no se crea versión")
            return False
        if self.version in versions(self.source):
            self.discard()
            raise RefsError(f"{self.source}: ya hay una versión {self.version} con otro contenido; "
                            "las versiones no se sobrescriben")
        data = {
            "source": self.source,
            "version": self.version,
            "fetched_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "origin": self.origin,
            "files": sorted(self.files, key=lambda f: f["path"]),
        }
        if self.errors:
            data["errors"] = sorted(self.errors)
        (self.tmp / "MANIFEST.json").write_bytes(dumps(data) + b"\n")
        self.tmp.rename(refs_dir() / self.source / self.version)
        size = sum(f["size"] for f in self.files) / 1e6
        print(f"{self.source}: {self.version} descargada ({len(self.files)} ficheros, {size:.1f} MB)")
        for error in self.errors:
            print(f"  error: {error}")
        current = pins()
        if self.source not in current:
            current[self.source] = self.version
            save_pins(current)
            print(f"{self.source}: fijada {self.version} (primera versión)")
        return True

    def discard(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

