import argparse
import gzip
import json

import pytest

from web_audit import refs

PAGE = """<html><head><title>T</title><script>var x = 1;</script></head><body>
<header>Site menu</header><nav><a href="/">Home</a></nav>
<main>
 <h1 id="top">Merchant listing</h1>
 <p>You must include the <code>required</code>
    properties.</p>
 <section id="rules"><div><h2 id="x1-rules">1. Rules</h2></div>
  <ul><li>First<ul><li>Nested</li></ul></li><li><p>Second</p></li></ul>
  <h3 id="own">Own anchor</h3>
  <table><tr><th>Property</th><th>Type</th></tr>
   <tr><td><code>name</code></td><td><p>Text</p><p>The name.</p></td></tr>
   <tr><th>sku<td>Text<td>Omitted end tags.
   <tr><td>gtin</td></table>
  <pre>{
  "@type": "Product"
}</pre>
 </section>
 <h2><a id="help_anchor" name="help_anchor"></a>Help heading</h2>
 <button>Send feedback</button><footer>Last updated 2026-09-08 UTC.</footer>
</main>
<div>Outside main</div>
</body></html>"""

TEXT = """# Merchant listing {#top}

You must include the required properties.

## 1. Rules {#rules}

- First
  - Nested
- Second

### Own anchor {#own}

| Property | Type |
| name | Text The name. |
| sku | Text | Omitted end tags. |
| gtin |

```
{
  "@type": "Product"
}
```

## Help heading {#help_anchor}
"""


def test_page_text():
    assert refs.page_text(PAGE) == TEXT
    assert refs.page_text("<p>No body, <b>still</b> text</p>") == "No body, still text\n"
    assert refs.published(PAGE) == "Last updated 2026-09-08"


SOURCES = [
    {"id": "schemaorg", "kind": "schemaorg", "title": "Vocabulary", "url": "https://github.com/x"},
    {"id": "guide", "kind": "document", "title": "Guide", "url": "https://example.org/guide"},
    {"id": "spec-pdf", "kind": "document", "title": "Spec", "url": "https://example.org/spec/"},
]


@pytest.fixture
def store(tmp_path, monkeypatch):
    """Empty refs directory, a registry and a fake web (url → (body, headers))."""
    monkeypatch.setattr(refs, "REFS", tmp_path / "refs")
    monkeypatch.setattr(refs, "PINS", tmp_path / "refs/pins.json")
    monkeypatch.setattr(refs, "SOURCES_FILE", tmp_path / "sources.json")
    monkeypatch.setattr(refs, "DOCUMENT_INTERVAL", 0)
    (tmp_path / "sources.json").write_text(json.dumps({"sources": SOURCES}), encoding="utf-8")
    web = {}
    monkeypatch.setattr(refs, "download", lambda url: (*web[url], url))
    return web


def html(body: str, nonce: str = "a") -> tuple:
    page = f'<html><body><script nonce="{nonce}">t()</script><main>{body}</main></body></html>'
    return page.encode("utf-8"), {"content-type": "text/html; charset=utf-8"}


def fetch(*names, version=None):
    refs.cmd_fetch(argparse.Namespace(sources=list(names), version=version))


def test_registry_is_checked(store, capsys):
    refs.SOURCES_FILE.write_text(json.dumps({"sources": SOURCES + [
        {"id": "guide", "kind": "document", "title": "Again", "url": "x"},
        {"id": "Bad_Id", "kind": "page", "title": "X"},
    ]}), encoding="utf-8")
    with pytest.raises(SystemExit):
        refs.sources()
    err = capsys.readouterr().err
    assert "guide: id repetido" in err and "Bad_Id: el id ha de ser kebab-case" in err
    assert "kind «page» desconocido" in err and "Bad_Id: falta url" in err


def test_a_page_counts_by_its_text(store, monkeypatch, capsys):
    store["https://example.org/guide"] = html("<h1>Guide</h1><p>Rule one.</p>")
    monkeypatch.setattr(refs, "today", lambda: "2026-10-27")
    fetch("guide")
    folder = refs.REFS / "guide/2026-10-27"
    assert (folder / "text.md").read_text(encoding="utf-8") == "# Guide\n\nRule one.\n"
    files = {f["path"]: f for f in refs.manifest("guide", "2026-10-27")["files"]}
    assert files["page.html"]["counted_by"] == "text.md" and refs.pins() == {"guide": "2026-10-27"}

    store["https://example.org/guide"] = html("<h1>Guide</h1><p>Rule one.</p>", nonce="b")
    fetch("guide")                                      # markup only: no new version
    assert refs.versions("guide") == ["2026-10-27"] and "sin cambios" in capsys.readouterr().out
    assert refs.check_document("guide", SOURCES[1]).startswith("al día")

    store["https://example.org/guide"] = html("<h1>Guide</h1><p>Rule one.</p><p>Rule two.</p>")
    assert refs.check_document("guide", SOURCES[1]) == "cambió desde 2026-10-27: refs fetch guide"
    with pytest.raises(SystemExit):                     # the same day: versions are not overwritten
        fetch("guide")
    assert "ya hay una versión 2026-10-27" in capsys.readouterr().err
    monkeypatch.setattr(refs, "today", lambda: "2026-11-02")
    fetch("guide")
    assert refs.versions("guide") == ["2026-10-27", "2026-11-02"] and refs.pins() == {"guide": "2026-10-27"}

    refs.cmd_diff(argparse.Namespace(source="guide", old=None, new=None, all=False))
    out = capsys.readouterr().out
    assert "guide: 2026-10-27 → 2026-11-02" in out and "text.md: +2 −0 líneas" in out and "+Rule two." in out
    refs.cmd_pin(argparse.Namespace(source="guide", version="2026-11-02"))
    assert refs.pins() == {"guide": "2026-11-02"} and "Revisa las fichas" in capsys.readouterr().out


def test_other_documents_are_kept_as_published(store, capsys):
    store["https://example.org/spec/"] = (b"%PDF-1.4 one", {"content-type": "application/pdf"})
    fetch("spec-pdf")
    version = refs.versions("spec-pdf")[0]
    assert [f["path"] for f in refs.manifest("spec-pdf", version)["files"]] == ["document.pdf"]
    files, _ = refs.document_files("https://example.org/spec/")
    assert refs.fingerprint([e for _, _, e in files]) == refs.fingerprint(refs.manifest("spec-pdf", version)["files"])
    store["https://example.org/voc.jsonld"] = (b"{}", {"content-type": "application/ld+json"})
    assert refs.document_files("https://example.org/voc.jsonld")[0][0][0] == "voc.jsonld"


def test_a_failed_source_does_not_stop_the_others(store, capsys):
    store["https://example.org/spec/"] = (b"%PDF-1.4", {"content-type": "application/pdf"})
    store["https://example.org/guide"] = (b"\x00", {"content-type": "application/octet-stream"})
    with pytest.raises(SystemExit):
        fetch("guide", "spec-pdf")
    assert refs.versions("spec-pdf") and not refs.versions("guide")
    assert "sin descargar: guide" in capsys.readouterr().err


class Response:
    def __init__(self, data, headers):
        self.data, self.headers = data, headers

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self):
        return self.data

    def geturl(self):
        return "https://example.org/final"


def test_download_inflates_what_the_server_compressed(monkeypatch):
    monkeypatch.setattr(refs, "request", lambda url: Response(gzip.compress(b"<p>x</p>"), {"content-encoding": "gzip"}))
    assert refs.download("https://example.org/") == (b"<p>x</p>", {"content-encoding": "gzip"}, "https://example.org/final")
    monkeypatch.setattr(refs, "request", lambda url: Response(b"x", {"content-encoding": "br"}))
    with pytest.raises(refs.RefsError, match="content-encoding br"):
        refs.download("https://example.org/")


def vocabulary(*nodes) -> bytes:
    return json.dumps({"@context": {}, "@graph": list(nodes)}).encode("utf-8")


V1 = vocabulary(
    {"@id": "schema:Product", "@type": "rdfs:Class", "rdfs:comment": "Any offered product.",
     "rdfs:subClassOf": {"@id": "schema:Thing"}},
    {"@id": "schema:gtin", "@type": "rdf:Property", "rdfs:comment": "A GTIN.",
     "schema:domainIncludes": [{"@id": "schema:Product"}], "schema:rangeIncludes": {"@id": "schema:Text"}},
    {"@id": "schema:InStock", "@type": "schema:ItemAvailability", "rdfs:comment": "In stock."},
)
V2 = vocabulary(
    {"@id": "schema:Product", "@type": "rdfs:Class", "rdfs:comment": "Any offered product or service.",
     "rdfs:subClassOf": {"@id": "schema:Thing"}},
    {"@id": "schema:gtin", "@type": "rdf:Property", "rdfs:comment": "A GTIN.",
     "schema:domainIncludes": [{"@id": "schema:Product"}, {"@id": "schema:Offer"}],
     "schema:rangeIncludes": {"@id": "schema:Text"}},
    {"@id": "schema:ProductGroup", "@type": "rdfs:Class", "rdfs:comment": "A group of products.",
     "rdfs:subClassOf": {"@id": "schema:Product"}},
)


def release(store, version: str, vocab: bytes, corrupt: str = None) -> None:
    api = refs.SCHEMAORG_API
    store[f"{api}/releases/tags/v{version}"] = (json.dumps({
        "tag_name": f"v{version}", "html_url": f"https://github.com/r/v{version}",
        "published_at": "2026-09-15T20:22:24Z"}).encode(), {})
    listing = []
    for name in refs.SCHEMAORG_FILES:
        data = vocab if name == refs.VOCABULARY else name.encode()
        url = f"https://raw.example/{version}/{name}"
        store[url] = (data + (b"!" if name == corrupt else b""), {})
        listing.append({"name": name, "size": len(data), "sha": refs.git_sha(data), "download_url": url})
    store[f"{api}/contents/data/releases/{version}?ref=v{version}"] = (json.dumps(listing).encode(), {})


def test_schemaorg_release_checked_against_github(store, capsys):
    release(store, "30.1", V1, corrupt="schemaorgcontext.jsonld")
    with pytest.raises(SystemExit):
        fetch("schemaorg", version="30.1")
    assert "no coincide con el tamaño o el sha" in capsys.readouterr().err
    assert not (refs.REFS / "schemaorg").exists()

    release(store, "30.1", V1)
    fetch("schemaorg", version="30.1")
    files = refs.manifest("schemaorg", "30.1")["files"]
    assert sorted(f["path"] for f in files) == sorted(refs.SCHEMAORG_FILES) and all(f["git_sha"] for f in files)
    assert refs.pins() == {"schemaorg": "30.1"}
    fetch("schemaorg", version="30.1")
    assert "30.1 ya descargada" in capsys.readouterr().out


def test_schemaorg_diff_by_term(store, capsys):
    release(store, "30.1", V1)
    release(store, "9.0", V2)                               # sorted naturally: 9.0 before 30.1
    fetch("schemaorg", version="30.1")
    fetch("schemaorg", version="9.0")
    assert refs.versions("schemaorg") == ["9.0", "30.1"]
    capsys.readouterr()
    refs.cmd_diff(argparse.Namespace(source="schemaorg", old="9.0", new="30.1", all=False))
    out = capsys.readouterr().out
    assert "tipos: 2 → 1 · +0 −1 · definición cambiada 1 · relaciones cambiadas 0" in out
    assert "propiedades: 1 → 1 · +0 −0 · definición cambiada 0 · relaciones cambiadas 1" in out
    assert "schema:gtin  −dominio:schema:Offer" in out
    assert "valores de enumeración: 0 → 1 · +1 −0" in out and "schema:InStock  In stock." in out


def test_pinned_version_missing_is_reported(store):
    with pytest.raises(refs.RefsError, match="guide no está fijada"):
        refs.pinned("guide")
    refs.save_pins({"guide": "2026-10-27"})
    with pytest.raises(refs.RefsError, match="está fijada pero no está en var/refs"):
        refs.pinned("guide")
