"""Files of the snapshots: unique folders, evidence written once, JSON and MHTML reading."""
from __future__ import annotations

import email
import email.policy
import gzip
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def stamp() -> str:
    return datetime.now().astimezone().strftime("%Y%m%dT%H%M%S")


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def unique_dir(base: Path) -> Path:
    """A new folder under `base` named by the current time; never reuses an existing one."""
    name = stamp()
    for i in range(100):
        path = base / (name if i == 0 else f"{name}-{i}")
        try:
            path.mkdir(parents=True, exist_ok=False)
            return path
        except FileExistsError:
            continue
    raise FileExistsError(f"no se pudo crear un directorio nuevo en {base}")


def write_evidence(folder: Path, name: str, data: bytes, compress: bool = True) -> dict:
    """Write a file that must not exist yet; return its sha256 and size (of the content)."""
    path = folder / (name + ".gz" if compress else name)
    with open(path, "xb") as f:
        f.write(gzip.compress(data, mtime=0) if compress else data)
    return {"file": path.name, "sha256": sha256(data), "bytes": len(data)}


def html_part(mhtml: bytes) -> bytes | None:
    """The main document of an MHTML file (its first text/html part)."""
    msg = email.message_from_bytes(mhtml, policy=email.policy.default)
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            return part.get_content().encode("utf-8")
    return None
