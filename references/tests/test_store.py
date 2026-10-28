import argparse
import json
import shutil

import pytest

from references import cli, store
from references.read import GOOGLE_FILE


def snapshot(version: str, content: bytes, source: str = "google") -> bool:
    snap = store.Version(source, version, {"url": "x"})
    snap.add(GOOGLE_FILE, content, "x")
    return snap.commit()


def test_versions_are_immutable_and_the_first_one_is_pinned(refs_dir, capsys):
    assert snapshot("v1", b"2541 - Casa\n")
    assert store.versions("google") == ["v1"] and store.pins() == {"google": "v1"}
    assert not snapshot("v2", b"2541 - Casa\n")             # same content: discarded
    assert store.versions("google") == ["v1"] and "sin cambios" in capsys.readouterr().out
    with pytest.raises(store.RefsError, match="ya hay una versión v1 con otro contenido"):
        snapshot("v1", b"2541 - Hogar\n")
    assert snapshot("v3", b"2541 - Casa\n1 - Hogar\n")
    assert store.versions("google") == ["v1", "v3"] and store.pins() == {"google": "v1"}
    assert not list((refs_dir / "google").glob(".partial-*"))


def test_a_gz_counts_by_its_content(refs_dir):
    import gzip
    snap = store.Version("shopify", "v1", {})
    snap.add("categories.es.json.gz", gzip.compress(b"{}", mtime=1), "x")
    assert snap.commit()
    snap = store.Version("shopify", "v2", {})               # other gzip header, same content
    snap.add("categories.es.json.gz", gzip.compress(b"{}", mtime=2), "x")
    assert not snap.commit()


def test_errors_of_a_partial_download_count_as_content(refs_dir):
    snap = store.Version("amazon-ptd", "2026-10-24", {})
    snap.add("index.json", b"{}", "x")
    snap.errors.append("SHEET: HTTP 500")
    assert snap.commit()
    assert store.manifest("amazon-ptd", "2026-10-24")["errors"] == ["SHEET: HTTP 500"]
    snap = store.Version("amazon-ptd", "2026-10-25", {})
    snap.add("index.json", b"{}", "x")
    assert snap.commit()                                     # same files, no errors: a new version


def test_natural_order_of_versions(refs_dir):
    for version, content in (("30.1", b"a"), ("9.0", b"b"), ("2026-10-27", b"c"), ("2026-11-02", b"d")):
        snapshot(version, content)
    assert store.versions("google") == ["9.0", "30.1", "2026-10-27", "2026-11-02"]


def test_registry_is_checked(refs_dir):
    path = store.sources_file()
    data = json.loads(path.read_text(encoding="utf-8"))
    data["sources"] += [
        {"id": "guide", "kind": "document", "title": "Again", "url": "x", "uses": ["web-audit"]},
        {"id": "Bad_Id", "kind": "page", "title": "X", "uses": ["nobody"]},
    ]
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(store.RefsError) as e:
        store.sources()
    err = str(e.value)
    assert "guide: id repetido" in err and "Bad_Id: el id ha de ser kebab-case" in err
    assert "kind «page» desconocido" in err and "Bad_Id: falta url" in err
    assert "Bad_Id: uses nombra un sistema no declarado: nobody" in err


def test_pins_of_a_system(refs_dir):
    store.save_pins({"shopify": "v1", "schemaorg": "30.1", "guide": "2026-10-27", "unregistered": "x"})
    assert store.pins("demand-engine") == {"shopify": "v1", "guide": "2026-10-27"}
    assert store.pins("web-audit") == {"schemaorg": "30.1", "guide": "2026-10-27"}


def test_a_pinned_version_missing_is_reported(refs_dir):
    with pytest.raises(store.RefsError, match="guide no está fijada"):
        store.pinned("guide")
    snapshot("v1", b"2541 - Casa\n")
    shutil.rmtree(refs_dir / "google/v1")
    with pytest.raises(store.RefsError, match="fijada pero no está en references/var"):
        store.pinned("google")


def test_pin_lists_the_systems_that_review_it(refs_dir, capsys):
    snapshot("v1", b"2541 - Casa\n")
    snapshot("v2", "2541 - Casa\n2542 - Casa > Sábanas\n".encode("utf-8"))
    cli.cmd_diff(argparse.Namespace(source="google", old=None, new=None, all=False))
    out = capsys.readouterr().out
    assert "google: v1 → v2" in out and "categorías: 1 → 2 · +1 −0" in out and "2542  Sábanas" in out
    cli.cmd_pin(argparse.Namespace(source="google", version="v2"))
    out = capsys.readouterr().out
    assert store.pins() == {"google": "v2"}
    assert "fijada v2 (antes v1)" in out and "  demand-engine: entrenamiento" in out and "web-audit" not in out
    with pytest.raises(SystemExit):
        cli.cmd_pin(argparse.Namespace(source="google", version="v9"))


def test_status_names_who_uses_each_source(refs_dir, capsys):
    snapshot("v1", b"2541 - Casa\n")
    cli.cmd_status(argparse.Namespace())
    lines = capsys.readouterr().out.splitlines()
    assert any(l.startswith("google ") and "fijada v1 · última v1" in l and l.endswith("· demand-engine") for l in lines)
    assert any(l.startswith("guide ") and "sin descargar · web-audit, demand-engine" in l for l in lines)
