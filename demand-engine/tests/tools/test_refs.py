import argparse
import shutil

import pytest

from demand_engine import refs


def test_reading_the_pinned_versions(fake_refs):
    assert list(refs.shopify_categories()) == ["zz", "zz-1", "zz-1-2"]
    assert refs.shopify_attributes()["fabric"]["name"] == "Tejido"
    assert refs.google_mapping()["zz-1-2"] == ("Home > Bedding > Sheets", [("2541", "Home > Linens > Sheets")])
    assert refs.google_names() == {"2541": "Casa > Ropa de cama > Sábanas"}
    props, definition = refs.ptd("SHEET")
    assert definition["displayName"] == "Sábana"
    assert refs.enum_values(props["thread_count"]) == ["200", "400"]


def test_missing_pins_and_ptd_are_reported(fake_refs):
    with pytest.raises(refs.RefsError, match="no existe el PTD NOPE"):
        refs.ptd("NOPE")
    refs.PINS.write_text("{}", encoding="utf-8")
    with pytest.raises(refs.RefsError, match="shopify no está fijada"):
        refs.pinned("shopify")


@pytest.fixture
def empty_refs(tmp_path, monkeypatch):
    monkeypatch.setattr(refs, "REFS", tmp_path)
    monkeypatch.setattr(refs, "PINS", tmp_path / "pins.json")
    return tmp_path


def snapshot(version: str, content: bytes) -> None:
    snap = refs.Snapshot("google", version, {"url": "x"})
    snap.add(refs.GOOGLE_FILE, content, "x")
    snap.commit()


def test_versions_are_immutable_and_the_first_one_is_pinned(empty_refs, capsys):
    snapshot("v1", b"2541 - Casa\n")
    assert refs.versions("google") == ["v1"] and refs.pins() == {"google": "v1"}
    with pytest.raises(SystemExit):
        refs.Snapshot("google", "v1", {})
    snapshot("v2", b"2541 - Casa\n")          # same content: discarded
    assert refs.versions("google") == ["v1"]
    snapshot("v3", b"2541 - Casa\n1 - Hogar\n")
    assert refs.versions("google") == ["v1", "v3"] and refs.pins() == {"google": "v1"}
    assert "sin cambios" in capsys.readouterr().out


def test_pin_and_diff(empty_refs, capsys):
    snapshot("v1", b"2541 - Casa\n")
    snapshot("v2", "2541 - Casa\n2542 - Casa > Sábanas\n".encode("utf-8"))
    refs.cmd_diff(argparse.Namespace(source="google", old=None, new=None, all=False))
    assert "+1 −0" in capsys.readouterr().out
    refs.cmd_pin(argparse.Namespace(source="google", version="v2"))
    assert refs.pins() == {"google": "v2"}
    assert "Revisa los mapeos" in capsys.readouterr().out


def test_a_pinned_version_missing_locally_is_reported(empty_refs):
    snapshot("v1", b"2541 - Casa\n")
    shutil.rmtree(empty_refs / "google/v1")
    with pytest.raises(refs.RefsError, match="fijada pero no está en var/refs"):
        refs.pinned("google")
