import argparse
import json

import pytest

from web_audit import refs, reqs

TEXT = """# Merchant listing {#top}

## Structured data type definitions {#definitions}

You must include the required properties to be eligible.

### Product {#product-properties}

| Required properties |
| offers | Offer A nested Offer to sell the product. |
| Recommended properties |
| sku | Text The merchant-specific identifier for the product. |

```
# not a heading
```

#### Identifiers

We recommend that the sku value only contain ASCII characters.

## Examples {#examples}

### Example

First.

### Example

An example.
"""

VOCABULARY = {"@context": {}, "@graph": [
    {"@id": "schema:gtin", "@type": "rdf:Property",
     "rdfs:comment": "A Global Trade Item Number.\n\nA correct [[gtin]] value should be a valid GTIN."},
]}

SOURCES = [
    {"id": "guide", "kind": "document", "title": "Guide", "url": "https://example.org/guide"},
    {"id": "schemaorg", "kind": "schemaorg", "title": "Vocabulary", "url": "https://github.com/x"},
    {"id": "spec-pdf", "kind": "document", "title": "Spec", "url": "https://example.org/spec/"},
    {"id": "principles", "kind": "document", "title": "Principles", "url": "https://example.org/p"},
]


def freeze(source: str, version: str, files: dict) -> None:
    folder = refs.REFS / source / version
    folder.mkdir(parents=True)
    for name, data in files.items():
        (folder / name).write_bytes(data)
    (folder / "MANIFEST.json").write_text(json.dumps({"files": [{"path": n} for n in files]}), encoding="utf-8")


@pytest.fixture
def reference(tmp_path, monkeypatch):
    """Frozen sources (a page, the vocabulary, a PDF), pinned, and an empty reference."""
    monkeypatch.setattr(refs, "REFS", tmp_path / "refs")
    monkeypatch.setattr(refs, "PINS", tmp_path / "refs/pins.json")
    monkeypatch.setattr(refs, "SOURCES_FILE", tmp_path / "sources.json")
    monkeypatch.setattr(reqs, "REFERENCE", tmp_path / "reference")
    (tmp_path / "sources.json").write_text(json.dumps({"sources": SOURCES}), encoding="utf-8")
    freeze("guide", "2026-10-27", {"page.html": b"<html></html>", "text.md": TEXT.encode()})
    freeze("guide", "2026-11-02", {"page.html": b"<html></html>", "text.md": b"# Merchant listing {#top}\n"})
    freeze("schemaorg", "30.1", {refs.VOCABULARY: json.dumps(VOCABULARY).encode()})
    freeze("spec-pdf", "2026-10-27", {"document.pdf": b"%PDF-1.4"})
    freeze("principles", "2026-10-27", {"text.md": b"# Principles {#p}\n\nData should be reusable.\n"})
    refs.save_pins({"guide": "2026-10-27", "schemaorg": "30.1", "spec-pdf": "2026-10-27", "principles": "2026-10-27"})
    reqs.vocabulary.cache_clear()
    return tmp_path / "reference"


def card(source="guide", version="2026-10-27", cls="especificación aplicable", level="consumidor", quotes=(), **extra):
    data = {"source": source, "version": version, "class": cls, "summary": "What it fixes.",
            "quotes": [{"id": f"q{i:02d}", "section": s, "text": t} for i, (s, t) in enumerate(quotes, 1)], **extra}
    if level:
        data["level"] = level
    return data


GUIDE = card(quotes=[("#definitions", "You must include the required properties"),
                     ("#product-properties", "Required properties"),
                     ("#product-properties", "offers | Offer A nested Offer to sell the product."),
                     ("Identifiers", "We recommend that the sku value only contain ASCII characters.")])


def requirement(n=1, **fields):
    return {"id": f"ws-consumer/{n:03d}", "scope": "Web Schema.org", "spec": "guide",
            "condition": "Cada entidad Product del marcado tiene la propiedad offers.", "nature": "obligatoria",
            "quotes": ["guide#q02", "guide#q03"], "method": "Extraer los Product y buscar offers.",
            "evidence": "Cada Product y sus offers.", "applicability": "universal", "not_evaluable": [], **fields}


def write(reference, cards=(), requirements=None, level="consumidor", stem="consumer"):
    (reference / "cards").mkdir(parents=True, exist_ok=True)
    for c in cards:
        (reference / "cards" / f"{c['source']}.json").write_text(json.dumps(c), encoding="utf-8")
    if requirements is not None:
        (reference / "requirements").mkdir(parents=True, exist_ok=True)
        (reference / "requirements" / f"{stem}.json").write_text(
            json.dumps({"level": level, "requirements": requirements}), encoding="utf-8")


def errors(reference) -> str:
    return "\n".join(reqs.check()[0])


def test_a_valid_reference(reference):
    vocab = card("schemaorg", "30.1", level="vocabulario", quotes=[("schema:gtin", "should be a valid GTIN.")])
    write(reference, [GUIDE, vocab, card("principles", cls="principios generales", level=None)],
          [requirement(), requirement(2, nature="recomendada", quotes=["guide#q04"],
                                      condition="El valor de sku solo contiene caracteres ASCII.")])
    (reference / "requirements" / "vocabulary.json").write_text(json.dumps({"level": "vocabulario", "requirements": [
        {**requirement(), "id": "ws-vocabulary/001", "spec": "schemaorg", "nature": "recomendada",
         "quotes": ["schemaorg#q01"], "condition": "El valor de gtin es un GTIN válido."}]}), encoding="utf-8")
    found, summary = reqs.check()
    assert found == []
    assert summary == ["3 fichas (2 de especificaciones aplicables), 5 citas, 3 requisitos "
                       "(1 obligatorias, 2 recomendadas)", "sin ficha (1): spec-pdf"]


def test_sections(reference):
    section = reqs.section_text("guide", "document", "#product-properties")
    assert section.startswith("### Product") and "We recommend" in section     # with its subsections
    assert "## Examples" not in section and "# not a heading" in section        # code is no heading
    assert reqs.section_text("guide", "document", "#examples").endswith("An example.")
    assert reqs.section_text("guide", "document", "Identifiers").startswith("#### Identifiers\n")
    with pytest.raises(reqs.ReqsError, match="hay 2 encabezados «Example»"):
        reqs.section_text("guide", "document", "Example")
    with pytest.raises(reqs.ReqsError, match="no existe la sección #nope"):
        reqs.section_text("guide", "document", "#nope")
    assert reqs.section_text("schemaorg", "schemaorg", "schema:gtin").endswith("should be a valid GTIN.")
    with pytest.raises(reqs.ReqsError, match="no tiene texto citable"):
        reqs.section_text("spec-pdf", "document", "#x")


def test_card_errors(reference):
    write(reference, [
        {**card(quotes=[("#product-properties", "offers | Offer A nested\n  Offer to sell the product."),
                        ("#examples", "offers | Offer"), ("#product-properties", "Required properties")]),
         "score": 1},
        card("principles", cls="norma", level=None),
        card("spec-pdf", level=None, quotes=[("#x", "anything"), (7, "")]),
        card("schemaorg", "30.0", cls="principios generales", quotes=[("schema:nope", "x")]),
    ])
    (reference / "cards" / "other.json").write_text(json.dumps(card("guide")), encoding="utf-8")
    found = errors(reference)
    assert "cards/guide.json: campo no admitido «score»" in found
    assert "guide.json q01" not in found                    # whitespace does not count
    assert "guide.json q02: la cita no está en #examples de guide 2026-10-27" in found
    assert "principles.json: class «norma» no es una clase del canon" in found
    assert "spec-pdf.json: una especificación aplicable lleva level" in found
    assert "spec-pdf.json q01: spec-pdf: document.pdf no tiene texto citable" in found
    assert "spec-pdf.json q02: section ha de ser un texto no vacío" in found
    assert "spec-pdf.json q02: text ha de ser un texto no vacío" in found
    assert "schemaorg.json: level solo corresponde a una especificación aplicable" in found
    assert "schemaorg.json: cita la versión 30.0 y la fijada es 30.1" in found
    assert "schemaorg.json q01: no existe el término schema:nope" in found
    assert "other.json: source «guide» no coincide con el nombre del fichero" in found


def test_a_new_pin_shows_the_quotes_to_review(reference):
    write(reference, [GUIDE])
    refs.save_pins({**refs.pins(), "guide": "2026-11-02"})
    found = errors(reference)
    assert "cita la versión 2026-10-27 y la fijada es 2026-11-02; revisa las citas (refs diff guide" in found
    assert "q03: la cita no está en #product-properties" not in found     # the section is gone first
    assert "q03: no existe la sección #product-properties" in found


def test_requirement_errors(reference):
    write(reference, [GUIDE, card("principles", cls="principios generales", level=None,
                                  quotes=[("#p", "Data should be reusable.")])], [
        requirement(weight=2),
        requirement(2, condition="Tiene offers. Y también name."),
        requirement(3, condition="Tiene offers; tiene name."),
        requirement(4, scope="Web", nature="crítica", not_evaluable="no"),
        requirement(5, spec="principles", quotes=["principles#q01"]),
        requirement(6, quotes=["guide#q09", "guide-q01", "principles#q01"]),
        requirement(7, nature="recomendada"),
        requirement(7),
        {**requirement(), "id": "ws-vocabulary/001"},
    ])
    found = errors(reference)
    assert "ws-consumer/001: campo no admitido «weight»" in found
    assert "ws-consumer/002: condition ha de ser una sola frase" in found
    assert "ws-consumer/003: condition ha de ser una sola frase" in found
    assert "ws-consumer/004: scope «Web» sin perfil de implementación en el canon" in found
    assert "ws-consumer/004: nature «crítica» no es del canon" in found
    assert "ws-consumer/004: not_evaluable ha de ser una lista" in found
    assert "ws-consumer/005: principles no es una especificación aplicable (D-132)" in found
    assert "ws-consumer/006: la cita guide#q09 no existe" in found
    assert "ws-consumer/006: la cita «guide-q01» ha de tener la forma fuente#q01" in found
    assert "ws-consumer/006: principles#q01 no es de una especificación aplicable" in found
    assert "ws-consumer/006: ninguna cita es de su especificación (guide)" in found
    assert "ws-consumer/007: ninguna cita de guide contiene el término que fija la naturaleza recomendada" in found
    assert "ws-consumer/007: id repetido" in found
    assert "ws-vocabulary/001: el id ha de ser ws-consumer/001" in found


def test_requirements_by_level(reference):
    write(reference, [GUIDE], [requirement(1, id="ws-vocabulary/001")], level="vocabulario", stem="vocabulary")
    write(reference, requirements=[requirement()], level="vocabulario", stem="consumer")
    write(reference, requirements=[], stem="extra")
    found = errors(reference)
    assert "vocabulary.json ws-vocabulary/001: guide es de nivel consumidor, no vocabulario" in found
    assert "consumer.json: level «vocabulario» no coincide con el fichero (consumidor)" in found
    assert "extra.json: el fichero ha de ser el de un nivel" in found


def test_cli(reference, capsys):
    reqs.cmd_section(argparse.Namespace(source="guide", section=None))
    out = capsys.readouterr().out
    assert "  #definitions  Structured data type definitions\n    #product-properties  Product\n" in out
    assert "      Identifiers\n" in out
    reqs.cmd_section(argparse.Namespace(source="schemaorg", section=None))
    assert "1 términos; indica uno" in capsys.readouterr().out
    with pytest.raises(SystemExit):
        reqs.cmd_section(argparse.Namespace(source="nope", section=None))
    assert "reqs: fuente desconocida: nope" in capsys.readouterr().err

    write(reference, [GUIDE], [requirement(nature="nada")])
    with pytest.raises(SystemExit):
        reqs.cmd_check(argparse.Namespace())
    assert capsys.readouterr().out.splitlines()[-2].startswith("incorrecto: 1 problema(s) · 1 fichas")
