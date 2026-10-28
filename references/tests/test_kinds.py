import argparse
import gzip
import hashlib
import json

import pytest

from references import cli, html, net, store
from references.kinds import document, schemaorg

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
    assert html.page_text(PAGE) == TEXT
    assert html.page_text("<p>No body, <b>still</b> text</p>") == "No body, still text\n"
    assert html.published(PAGE) == "Last updated 2026-09-08"


def page(body: str, nonce: str = "a") -> tuple:
    text = f'<html><body><script nonce="{nonce}">t()</script><main>{body}</main></body></html>'
    return text.encode("utf-8"), {"content-type": "text/html; charset=utf-8"}


def fetch(*names, version=None):
    cli.cmd_fetch(argparse.Namespace(sources=list(names), version=version))


def test_a_page_counts_by_its_text(web, monkeypatch, capsys):
    source = store.sources()["guide"]
    web["https://example.org/guide"] = page("<h1>Guide</h1><p>Rule one.</p>")
    monkeypatch.setattr(store, "today", lambda: "2026-10-27")
    monkeypatch.setattr(document, "today", lambda: "2026-10-27")
    fetch("guide")
    folder = store.refs_dir() / "guide/2026-10-27"
    assert (folder / "text.md").read_text(encoding="utf-8") == "# Guide\n\nRule one.\n"
    files = {f["path"]: f for f in store.manifest("guide", "2026-10-27")["files"]}
    assert files["page.html"]["counted_by"] == "text.md" and store.pins() == {"guide": "2026-10-27"}

    web["https://example.org/guide"] = page("<h1>Guide</h1><p>Rule one.</p>", nonce="b")
    fetch("guide")                                      # markup only: no new version
    assert store.versions("guide") == ["2026-10-27"] and "sin cambios" in capsys.readouterr().out
    assert document.check("guide", source).startswith("al día")

    web["https://example.org/guide"] = page("<h1>Guide</h1><p>Rule one.</p><p>Rule two.</p>")
    assert document.check("guide", source) == "cambió desde 2026-10-27: refs fetch guide"
    with pytest.raises(SystemExit):                     # the same day: versions are not overwritten
        fetch("guide")
    assert "ya hay una versión 2026-10-27" in capsys.readouterr().err
    monkeypatch.setattr(document, "today", lambda: "2026-11-02")
    fetch("guide")
    assert store.versions("guide") == ["2026-10-27", "2026-11-02"] and store.pins() == {"guide": "2026-10-27"}

    cli.cmd_diff(argparse.Namespace(source="guide", old=None, new=None, all=False))
    out = capsys.readouterr().out
    assert "guide: 2026-10-27 → 2026-11-02" in out and "text.md: +2 −0 líneas" in out and "+Rule two." in out
    cli.cmd_pin(argparse.Namespace(source="guide", version="2026-11-02"))
    out = capsys.readouterr().out
    assert store.pins() == {"guide": "2026-11-02"}
    assert "  web-audit: web-audit/bin/reqs check" in out and "  demand-engine: entrenamiento" in out


def test_other_documents_are_kept_as_published(web):
    web["https://example.org/spec/"] = (b"%PDF-1.4 one", {"content-type": "application/pdf"})
    fetch("spec-pdf")
    version = store.versions("spec-pdf")[0]
    assert [f["path"] for f in store.manifest("spec-pdf", version)["files"]] == ["document.pdf"]
    found, _ = document.files("https://example.org/spec/")
    assert store.fingerprint([e for _, _, e in found]) == store.fingerprint(store.manifest("spec-pdf", version)["files"])
    web["https://example.org/voc.jsonld"] = (b"{}", {"content-type": "application/ld+json"})
    assert document.files("https://example.org/voc.jsonld")[0][0][0] == "voc.jsonld"


def test_a_failed_source_does_not_stop_the_others(web, capsys):
    web["https://example.org/spec/"] = (b"%PDF-1.4", {"content-type": "application/pdf"})
    web["https://example.org/guide"] = (b"\x00", {"content-type": "application/octet-stream"})
    with pytest.raises(SystemExit):
        fetch("guide", "spec-pdf")
    assert store.versions("spec-pdf") and not store.versions("guide")
    assert "sin descargar: guide" in capsys.readouterr().err


def test_version_only_for_release_sources(web, capsys):
    with pytest.raises(SystemExit):
        fetch("guide", version="1.0")
    assert "--version solo se aplica" in capsys.readouterr().err


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
    monkeypatch.setattr(net, "request", lambda url, headers=None: Response(gzip.compress(b"<p>x</p>"), {"content-encoding": "gzip"}))
    assert net.download("https://example.org/") == (b"<p>x</p>", {"content-encoding": "gzip"}, "https://example.org/final")
    monkeypatch.setattr(net, "request", lambda url, headers=None: Response(b"x", {"content-encoding": "br"}))
    with pytest.raises(store.RefsError, match="content-encoding br"):
        net.download("https://example.org/")


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


def release(web, version: str, vocab: bytes, corrupt: str = None) -> None:
    api = schemaorg.SCHEMAORG_API
    web[f"{api}/releases/tags/v{version}"] = (json.dumps({
        "tag_name": f"v{version}", "html_url": f"https://github.com/r/v{version}",
        "published_at": "2026-09-15T20:22:24Z"}).encode(), {})
    listing = []
    for name in schemaorg.SCHEMAORG_FILES:
        data = vocab if name == schemaorg.VOCABULARY else name.encode()
        url = f"https://raw.example/{version}/{name}"
        web[url] = (data + (b"!" if name == corrupt else b""), {})
        listing.append({"name": name, "size": len(data), "sha": schemaorg.git_sha(data), "download_url": url})
    web[f"{api}/contents/data/releases/{version}?ref=v{version}"] = (json.dumps(listing).encode(), {})


def test_schemaorg_release_checked_against_github(web, capsys):
    release(web, "30.1", V1, corrupt="schemaorgcontext.jsonld")
    with pytest.raises(SystemExit):
        fetch("schemaorg", version="30.1")
    assert "no coincide con el tamaño o el sha" in capsys.readouterr().err
    assert not (store.refs_dir() / "schemaorg").exists()

    release(web, "30.1", V1)
    fetch("schemaorg", version="30.1")
    files = store.manifest("schemaorg", "30.1")["files"]
    assert sorted(f["path"] for f in files) == sorted(schemaorg.SCHEMAORG_FILES) and all(f["git_sha"] for f in files)
    assert store.pins() == {"schemaorg": "30.1"}
    fetch("schemaorg", version="30.1")
    assert "30.1 ya descargada" in capsys.readouterr().out


def test_schemaorg_diff_by_term(web, capsys):
    release(web, "30.1", V1)
    release(web, "9.0", V2)                               # sorted naturally: 9.0 before 30.1
    fetch("schemaorg", version="30.1")
    fetch("schemaorg", version="9.0")
    assert store.versions("schemaorg") == ["9.0", "30.1"]
    capsys.readouterr()
    cli.cmd_diff(argparse.Namespace(source="schemaorg", old="9.0", new="30.1", all=False))
    out = capsys.readouterr().out
    assert "tipos: 2 → 1 · +0 −1 · definición cambiada 1 · relaciones cambiadas 0" in out
    assert "propiedades: 1 → 1 · +0 −0 · definición cambiada 0 · relaciones cambiadas 1" in out
    assert "schema:gtin  −dominio:schema:Offer" in out
    assert "valores de enumeración: 0 → 1 · +1 −0" in out and "schema:InStock  In stock." in out


def shopify_release(web, tag: str, assets: dict, bad: str = None) -> None:
    listing = []
    for name, data in assets.items():
        url = f"https://github.com/dl/{tag}/{name}"
        web[url] = (data, {})
        digest = "sha256:" + hashlib.sha256(data + (b"!" if name == bad else b"")).hexdigest()
        listing.append({"name": name, "size": len(data), "digest": digest, "browser_download_url": url})
    body = json.dumps({"tag_name": tag, "html_url": f"https://github.com/r/{tag}",
                       "published_at": "2026-08-01T00:00:00Z", "assets": listing}).encode()
    web[f"https://api.github.com/repos/Shopify/product-taxonomy/releases/tags/{tag}"] = (body, {})


G = "gid://shopify/TaxonomyCategory/"


def taxonomy(*categories) -> dict:
    return {
        "categories.es.json.gz": gzip.compress(json.dumps({"verticals": [{"categories": [
            {"id": G + cid, "name": name, "parent_id": G + parent if parent else None}
            for cid, name, parent in categories]}]}).encode(), mtime=0),
        "attributes.es.json.gz": gzip.compress(json.dumps({"attributes": []}).encode(), mtime=0),
        "categories.es.txt.gz": gzip.compress(b"x", mtime=0),
        "integrations.google.shopify_x.en.json.gz": gzip.compress(b"{}", mtime=0),   # the other source's asset
    }


def test_shopify_release_keeps_its_assets_checked_against_the_digest(web, capsys):
    shopify_release(web, "v1", taxonomy(("zz", "Hogar", None)), bad="categories.es.txt.gz")
    with pytest.raises(SystemExit):
        fetch("shopify", version="v1")
    assert "no coincide con el tamaño o el sha256" in capsys.readouterr().err and not store.versions("shopify")

    shopify_release(web, "v1", taxonomy(("zz", "Hogar", None)))
    fetch("shopify", version="v1")
    assert [f["path"] for f in store.manifest("shopify", "v1")["files"]] == [
        "attributes.es.json.gz", "categories.es.json.gz", "categories.es.txt.gz"]
    shopify_release(web, "v2", taxonomy(("zz", "Casa", None), ("zz-1", "Ropa de cama", "zz")))
    fetch("shopify", version="v2")
    capsys.readouterr()
    cli.cmd_diff(argparse.Namespace(source="shopify", old=None, new=None, all=False))
    out = capsys.readouterr().out
    assert "categorías: 1 → 2 · +1 −0 · renombrados 1 · movidos 0" in out and "zz  Hogar → Casa" in out


def test_google_taxonomy_by_its_header(web, capsys):
    url = store.sources()["google"]["url"]
    web[url] = (b"# Google_Product_Taxonomy_Version: 2021-09-21\n1 - Casa\n", {})
    fetch("google")
    assert store.versions("google") == ["2021-09-21"]
    assert store.manifest("google", "2021-09-21")["origin"]["taxonomy_version"] == "2021-09-21"
    web[url] = (b"Not a taxonomy\n", {})
    with pytest.raises(SystemExit):
        fetch("google")
    assert "cabecera de versión" in capsys.readouterr().err
