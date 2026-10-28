import gzip
import json
import os
from email.message import EmailMessage

import pytest

from capture.files import html_part, write_evidence
from demand_engine.mpir.ingest import ingest
from demand_engine.mpir.store import Study, StoreError


def make_study():
    study = Study.create("prueba", "Ropa de cama")
    study.save_site({"id": "tienda", "base_url": "https://tienda.es", "type": "especialista",
                     "reason": "r", "checks": [], "blocks": []})
    return study


def test_inventory_ids_and_duplicates():
    study = make_study()
    added, present = study.add_resources("tienda", ["https://tienda.es/a", "https://tienda.es/b"], "product")
    assert [r["id"] for r in added] == ["tienda-001", "tienda-002"] and present == []
    added, present = study.add_resources("tienda", ["https://tienda.es/b", "https://tienda.es/c"], "guide")
    assert [r["id"] for r in added] == ["tienda-003"] and present == ["https://tienda.es/b"]
    res = study.update_resource("tienda-001", status="captured", snapshot="snapshots/x")
    assert res["status"] == "captured" and res["snapshots"] == ["snapshots/x"]


def test_snapshots_are_never_overwritten():
    study = make_study()
    a = study.new_dir("snapshots", "tienda", "tienda-001")
    b = study.new_dir("snapshots", "tienda", "tienda-001")
    assert a != b
    info = write_evidence(a, "dom.html", b"<html></html>")
    assert gzip.decompress((a / "dom.html.gz").read_bytes()) == b"<html></html>"
    assert info["bytes"] == 13
    with pytest.raises(FileExistsError):
        write_evidence(a, "dom.html", b"otra")


def test_visits_today():
    study = make_study()
    study.log("visit", site="tienda", resource="tienda-001", outcome="captured")
    study.log("visit", site="otra", resource="otra-001", outcome="captured")
    assert study.visits_today("tienda") == 1


def mhtml() -> bytes:
    msg = EmailMessage()
    msg["Subject"] = "Sábanas"
    msg.make_related()
    msg.add_related("<html><body><p>Composición: 100 % algodón</p></body></html>", subtype="html",
                    cte="quoted-printable")
    msg.add_related(b"\x89PNG", maintype="image", subtype="png")
    return msg.as_bytes()


def test_html_part_of_mhtml():
    assert "100 % algodón" in html_part(mhtml()).decode("utf-8")


def test_ingest_manual_page(tmp_path):
    study = make_study()
    path = tmp_path / "pagina.mhtml"
    path.write_bytes(mhtml())
    result = ingest(study, "tienda", "https://tienda.es/sabanas", path, "product")
    folder = study.dir / result["snapshot"]
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
    assert meta["method"] == "manual" and set(meta["files"]) == {"page.mhtml", "dom.html"}
    assert study.resources()[0]["status"] == "captured"


def test_ingest_refuses_a_reserved_site(tmp_path):
    study = make_study()
    study.update_site("tienda", lambda s: s["checks"].append({"verdict": "reserved", "at": "x"}))
    path = tmp_path / "p.html"
    path.write_text("<html></html>")
    with pytest.raises(StoreError):
        ingest(study, "tienda", "https://tienda.es/x", path, "product")


def test_what_is_defined_is_apart_from_what_is_produced():
    study = make_study()
    study.add_resources("tienda", ["https://tienda.es/a"], "product", reason="ficha tipo")
    study.update_resource("tienda-001", status="captured", snapshot="snapshots/x", last={"outcome": "captured"})
    study.update_site("tienda", lambda s: s["checks"].append({"verdict": "ok", "at": "x"}))
    card = json.loads(study.site_path("tienda").read_text(encoding="utf-8"))
    assert "checks" not in card and card["reason"] == "r"
    inventory = json.loads((study.home / "resources.json").read_text(encoding="utf-8"))["resources"]
    assert "status" not in inventory[0] and inventory[0]["reason"] == "ficha tipo"
    assert study.resources()[0]["status"] == "captured" and study.site("tienda")["checks"][0]["verdict"] == "ok"
    assert study.home != study.dir and str(study.dir).startswith(os.environ["MPIR_VAR"])

