"""Manual capture: a page that a person saved with their own browser (MHTML or HTML) enters
the corpus as a snapshot with method «manual». Used when the engine was blocked or the page
needs interaction. The DOM of a manual snapshot carries no visibility marks.
"""
from __future__ import annotations

import json
from pathlib import Path

from capture.files import html_part, now, write_evidence

from .store import Study, StoreError


def ingest(study: Study, site_id: str, url: str, path: Path, profile: str) -> dict:
    site = study.site(site_id)
    checks = site.get("checks") or []
    if checks and checks[-1]["verdict"] == "reserved":
        raise StoreError(f"{site_id} tiene una reserva TDM: no se conserva su contenido")
    suffix = path.suffix.lower()
    if suffix not in (".mhtml", ".mht", ".html", ".htm"):
        raise StoreError("formato no admitido: .mhtml, .mht, .html o .htm")
    data = path.read_bytes()
    study.add_resources(site_id, [url], profile, reason="incorporada a mano")
    resource = next(r for r in study.resources() if r["url"] == url)
    folder = study.new_dir("snapshots", site_id, resource["id"])
    files = {}
    if suffix in (".mhtml", ".mht"):
        files["page.mhtml"] = write_evidence(folder, "page.mhtml", data)
        html = html_part(data)
        if html is not None:
            files["dom.html"] = write_evidence(folder, "dom.html", html)
    else:
        files["dom.html"] = write_evidence(folder, "dom.html", data)
    meta = {"study": study.id, "site": site_id, "resource": resource["id"], "profile": resource["profile"],
            "url_requested": url, "method": "manual", "source_file": path.name, "started_at": now(),
            "outcome": "captured", "detail": "guardada a mano en un navegador", "files": files,
            "note": "Guardada por una persona; el DOM no lleva marcas de visibilidad", "finished_at": now()}
    with open(folder / "meta.json", "x", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    snapshot = str(folder.relative_to(study.dir))
    study.update_resource(resource["id"], status="captured", snapshot=snapshot,
                          last={"at": now(), "outcome": "captured", "detail": "manual"})
    study.log("ingest", site=site_id, resource=resource["id"], snapshot=snapshot, source=path.name)
    return {"resource": resource["id"], "snapshot": snapshot}
