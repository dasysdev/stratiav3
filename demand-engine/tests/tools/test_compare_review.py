import json
import sys

from demand_engine import catalog_review, compare

CASE = {"vertical": "Hogar", "expected": {"specializations": [], "features": [
    {"role": "requisito", "questions": ["¿Qué medidas tiene la sábana?"]}]},
    "expected_v1": {"categories": ["zz-1-2"], "alias": [], "specializations": [], "application": ["cat.sabanas"]}}
OUT = {"rulebook": "v1", "composition": {"categories": [{"shopify": "zz-1-2"}]},
       "blocks": [{"id": "cat.sabanas", "type": "categoría", "refs": ["shopify:zz-1-2@v1"], "requirements": [
           {"question": "¿Qué medidas tiene la sábana?", "importance": "principal", "origin": "referencias",
            "sources": ["shopify-attr:bedding-size"]}]}],
       "application": {"active": ["cat.sabanas"]}, "denomination": {"name": "Sábanas"}}


def write(path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")


def test_compare_against_expected_and_pair(tmp_path, monkeypatch, capsys):
    write(tmp_path / "cases/caso.json", CASE)
    write(tmp_path / "run-a/caso.json", OUT)
    write(tmp_path / "run-b/caso.json", OUT)
    monkeypatch.setattr(compare, "CASES", tmp_path / "cases")
    compare.against_expected(tmp_path / "run-a", ["caso"])
    out = capsys.readouterr().out
    assert "cuestiones clave cubiertas en el modelo: 1/1" in out
    assert "Casos: 1 · composición igual 1/1 · especializaciones 1/1 · cuestiones clave 1/1 · aplicación 1/1" in out
    monkeypatch.setattr(sys, "argv", ["compare", "--pair", str(tmp_path / "run-a"), str(tmp_path / "run-b")])
    compare.main()
    assert "categorías iguales 1/1 · especializaciones iguales 1/1 · aplicación igual 1/1" in capsys.readouterr().out


def test_catalog_review(tmp_path, monkeypatch, capsys):
    block = {"id": "cat.ropa-de-cama", "name": "Ropa de cama", "shopify": "zz-1", "parent": None, "refs": ["shopify:zz-1@v1"],
             "requirements": [{"id": "cat.ropa-de-cama/1", "question": "¿Qué medidas tiene?", "importance": "crítico",
                               "entity": "producto", "sources": ["shopify-attr:bedding-size"]}]}
    child = {"id": "cat.sabanas", "name": "Sábanas", "shopify": "zz-1-2", "parent": "cat.ropa-de-cama", "refs": [],
             "requirements": [], "excluded": [{"source": "amazon-ptd-prop:SHEET.brand", "reason": "administrativa"}]}
    write(tmp_path / "catalog/cat/ropa-de-cama.json", block)
    write(tmp_path / "catalog/cat/sabanas.json", child)
    write(tmp_path / "catalog/skeleton.json", {"blocks": [{"shopify": "zz-1", "name": "Ropa de cama"},
                                                          {"shopify": "zz", "name": "Hogar"}]})
    monkeypatch.setattr(catalog_review, "ROOT", tmp_path)
    monkeypatch.setattr(catalog_review, "CAT", tmp_path / "catalog/cat")
    monkeypatch.setattr(sys, "argv", ["catalog-review", str(tmp_path / "REVIEW.md")])
    catalog_review.main()
    review = (tmp_path / "REVIEW.md").read_text(encoding="utf-8")
    assert "- `cat.ropa-de-cama/1` — ¿Qué medidas tiene?" in review
    assert "- zz Hogar" in review                               # empty category of the skeleton
    assert review.index("### `cat.ropa-de-cama`") < review.index("#### `cat.sabanas`")
    assert "2 bloques, 1 requisitos, 1 críticos, 1 categorías vacías" in capsys.readouterr().out
