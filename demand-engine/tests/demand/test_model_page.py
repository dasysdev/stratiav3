"""The assembled model records the frozen page of its case and its capture profile (T-104)."""
import json

from demand_engine.demand import model as engine


def assembled(tmp_path, monkeypatch, case, pages=None):
    store = tmp_path / "pages"
    store.mkdir()
    for page_id, record in (pages or {}).items():
        (store / f"{page_id}.html").write_text("<html></html>", encoding="utf-8")
        (store / f"{page_id}.json").write_text(json.dumps(record), encoding="utf-8")
    monkeypatch.setattr(engine.pages, "PAGES", store)
    out = {"case": case, "rulebook": "v5", "url": "https://tienda.example/p-1", "declared": [], "application": [],
           "inferred": [], "composition": {"categories": []}, "specializations": [], "votes": {}, "trait_votes": {}}
    path = tmp_path / f"{case}.json"
    path.write_text(json.dumps(out), encoding="utf-8")
    return engine.assemble(path)


def test_the_model_records_the_page_of_its_case_and_its_capture_profile(tmp_path, monkeypatch):
    m = assembled(tmp_path, monkeypatch, "audit-x-1", {"audit-x-1": {"id": "audit-x-1", "profile": "audit-es"},
                                                       "x-1": {"id": "x-1", "profile": "reader"}})
    assert m["page"] == {"id": "audit-x-1", "profile": "audit-es"}
    assert "- Ficha: `audit-x-1` · perfil de captura `audit-es`" in engine.render(m).splitlines()


def test_a_page_frozen_before_the_profiles_is_a_reader_one(tmp_path, monkeypatch):
    m = assembled(tmp_path, monkeypatch, "x-1", {"x-1": {"id": "x-1", "url": "https://tienda.example/p-1"}})
    assert m["page"] == {"id": "x-1", "profile": "reader"}


def test_without_a_page_in_the_store_the_model_records_none(tmp_path, monkeypatch):
    m = assembled(tmp_path, monkeypatch, "sin-ficha")
    assert m["page"] is None
    assert not any(line.startswith("- Ficha:") for line in engine.render(m).splitlines())
