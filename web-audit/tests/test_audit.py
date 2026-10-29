import gzip
import json

import pytest

from references.store import RefsError
from web_audit import audit, html, jsonld, microdata, vocab
from web_audit.checks import NA, NE, PENDING, SAT, UNSAT, Case, load_all, missing
from web_audit.checks.markup import has
from web_audit.graph import Entity, Graph, Lit, Ref
from web_audit.site import Site

try:
    vocab.load()
    HAS_VOCAB = True
except (RefsError, FileNotFoundError, StopIteration):
    HAS_VOCAB = False
needs_vocab = pytest.mark.skipif(not HAS_VOCAB, reason="sin Schema.org 30.1 en references/var")

SITE = "https://shop.example"


# --- A synthetic audit of capture -----------------------------------------------------------------

def make_audit(root, pages, robots="User-agent: *\nDisallow: /private\nSitemap: https://shop.example/sitemap.xml\n",
               robots_status=200, sitemaps=None):
    """pages: id → (type, url, html, extra meta). sitemaps: [(url, status, bytes or None)]."""
    folder = root / "aud"
    (folder / "sites" / "shop.example").mkdir(parents=True)
    (folder / "sites" / "shop.example" / "robots.txt").write_text(robots)
    if sitemaps is None:
        sitemaps = [(f"{SITE}/sitemap.xml", 200, (
            '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + "".join(f"<url><loc>{p[1]}</loc></url>" for p in pages.values()) + "</urlset>").encode())]
    read = []
    (folder / "sitemaps").mkdir()
    for i, (url, status, data) in enumerate(sitemaps, 1):
        entry = {"url": url, "status": status}
        if data is not None:
            name = f"sitemaps/{i:03d}-sitemap.xml"
            (folder / name).write_bytes(data)
            entry.update({"file": name, "gzip": data[:2] == b"\x1f\x8b"})
        elif status and status >= 500:
            entry["error"] = f"HTTP {status}"
        read.append(entry)
    records = []
    for pid, (kind, url, doc, extra) in pages.items():
        snap = folder / "pages" / pid / "20261028T000000"
        snap.mkdir(parents=True)
        status = (extra or {}).get("status", 200)
        meta = {"profile": "audit-es", "url_requested": url, "url_final": url, "redirects": [],
                "legitimacy": {"robots": {"status": robots_status}}, "response_body": "original",
                "http": {"status": status, "headers": {"content-type": "text/html; charset=utf-8"}, "mime": "text/html"},
                "dom": {"charset": "UTF-8"}, "outcome": "captured"}
        meta.update(extra or {})
        (snap / "meta.json").write_text(json.dumps(meta))
        (snap / "response.html.gz").write_bytes(gzip.compress(doc.encode("utf-8")))
        records.append({"id": pid, "type": kind, "url": url, "outcome": meta["outcome"],
                        "snapshot": f"pages/{pid}/20261028T000000", "url_final": url, "http_status": status})
    manifest = {"audit": "aud", "site": SITE, "profile": "audit-es", "pages": records, "products": [],
                "legitimacy": {"robots": {"status": robots_status}},
                "sitemaps": {"read": read, "pending": [], "complete": True}, "policies": {}}
    (folder / "audit.json").write_text(json.dumps(manifest))
    return Site("aud", folder)


PRODUCT = """<!doctype html><html><head><meta charset="utf-8"><title>Cojín azul</title>
<link rel="canonical" href="https://shop.example/cojin">
<meta property="og:title" content="Cojín"><meta property="og:type" content="product">
<meta property="og:image" content="https://shop.example/c.jpg"><meta property="og:url" content="https://shop.example/cojin">
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Product", "@id": "https://shop.example/cojin#p",
 "name": "Cojín azul", "sku": "CJ 01", "image": ["https://shop.example/c.jpg", "https://shop.example/private/d.jpg"],
 "offers": {"@type": "Offer", "price": "19.90", "priceCurrency": "EUR", "availability": "https://schema.org/InStock",
            "url": "https://shop.example/cojin"}}</script>
</head><body><h1>Cojín azul</h1><p>Un cojín.</p></body></html>"""


def case(site, page_id, req_id):
    req = next(r for r in audit.requirements() if r["id"] == req_id)
    return Case(site, site.page(page_id) if page_id else None, req)


# --- Registry -----------------------------------------------------------------------------------------

def test_every_requirement_has_a_check():
    ids = [r["id"] for r in audit.requirements()]
    assert missing(ids) == []
    assert set(load_all()) == set(ids)


# --- Parsers ------------------------------------------------------------------------------------------

def test_head_closes_at_body_content():
    doc = html.parse("<html><head><title>x</title><div>a</div><link rel=canonical href=/b></head><body></body></html>")
    link = doc.all("link")[0]
    assert not doc.in_head(link)
    assert doc.in_head(doc.all("title")[0])


def test_visible_text_skips_hidden_and_scripts():
    doc = html.parse('<body><p>uno</p><script>x</script><div hidden>no</div><span style="display: none">no</span>'
                     '<noscript>dos</noscript></body>')
    assert doc.visible_text(doc.body()) == "uno dos"


@pytest.mark.parametrize("text, ok", [('{"a": 1}', True), ('{"a": 1,}', False), ('{"a": NaN}', False),
                                      ("", False), ("{'a': 1}", False), ('{"a": "x\ny"}', False)])
def test_strict_json(text, ok):
    assert (jsonld.parse(text)[1] is None) == ok


def test_duplicate_keys_and_aliases():
    data, _ = jsonld.parse('{"@context": "https://schema.org", "type": "Product", "name": "a", "name": "b"}')
    report = jsonld.analyze([jsonld.Block(1, 1, "", data)])
    assert report.problems["duplicates"]
    if HAS_VOCAB:  # `type` is an alias of @type in the Schema.org context
        assert report.seen.get("type") == 1


def test_value_objects_and_base():
    text = '{"@context": {"@vocab": "https://schema.org/"}, "@id": "#p", "name": {"@value": "x", "@type": "xsd:string", "@language": "es"}}'
    data, _ = jsonld.parse(text)
    report = jsonld.analyze([jsonld.Block(1, 1, text, data)])
    assert report.problems["value-type-language"]
    assert report.problems["base"]  # a relative @id without @base


def test_microdata_itemref_error_and_loose_itemprop():
    doc = html.parse('<div itemscope itemtype="https://schema.org/Product" id="a" itemref="a"><span itemprop="name">x</span></div>'
                     '<span itemprop="sku">1</span>')
    items = microdata.items(doc)
    assert items[0].errors
    assert [el.get("itemprop") for el in microdata.loose(doc)] == ["sku"]


@needs_vocab
def test_graph_merges_by_id_and_keeps_unresolved_refs():
    a = Entity(["Product"], "json-ld", "a", "https://x/#p", True, {"name": [Lit("n", "json-string")]})
    b = Entity(["Product"], "json-ld", "b", "https://x/#p", True, {"name": [Lit("n", "json-string")],
                                                                    "offers": [Ref("https://x/#o")]})
    g = Graph.link([a, b])
    assert len(g.of("Product")) == 1
    assert len(g.of("Product")[0].values("name")) == 1  # the same triple once
    result = has("Product>offers", "price")(Case(None, type("P", (), {"graph": g})(), {}))
    assert result.state == NE


# --- Checks over a synthetic audit ------------------------------------------------------------------

@needs_vocab
def test_product_page(tmp_path):
    site = make_audit(tmp_path, {"product-01": ("product", f"{SITE}/cojin", PRODUCT, None)})
    assert case(site, "product-01", "ws-consumer/001")
    states = {r: (lambda c: load_all()[r](c).state)(case(site, "product-01", r)) for r in
              ("ws-consumer/001", "ws-consumer/042", "ws-consumer/045", "ws-consumer/055", "ws-consumer/057",
               "ws-consumer/004", "w-document/008", "w-document/014", "w-consumer/014", "w-consumer/015",
               "ws-serialization/001", "ws-vocabulary/001", "ws-consumer/066", "ws-consumer/032")}
    assert states["ws-consumer/001"] == SAT
    assert states["ws-consumer/045"] == UNSAT          # the sku has a space
    assert states["ws-consumer/055"] == SAT
    assert states["ws-consumer/057"] == SAT
    assert states["ws-consumer/004"] == UNSAT          # an image under /private is disallowed
    assert states["w-document/014"] == SAT
    assert states["w-consumer/014"] == SAT
    assert states["ws-consumer/032"] == PENDING        # variants: what the page shows decides


@needs_vocab
def test_product_without_markup_is_not_satisfied(tmp_path):
    site = make_audit(tmp_path, {"product-01": ("product", f"{SITE}/x", "<html><head><title>x</title></head><body>x</body></html>", None)})
    assert load_all()["ws-consumer/001"](case(site, "product-01", "ws-consumer/001")).state == UNSAT
    assert load_all()["ws-consumer/066"](case(site, "product-01", "ws-consumer/066")).state == NA
    assert load_all()["w-consumer/006"](case(site, "product-01", "w-consumer/006")).state == UNSAT


@pytest.mark.parametrize("status, google, rfc", [(200, SAT, SAT), (404, SAT, SAT), (429, NE, SAT), (503, NE, UNSAT)])
def test_robots_readers(tmp_path, status, google, rfc):
    site = make_audit(tmp_path, {"home": ("home", f"{SITE}/", "<title>x</title>", None)}, robots_status=status)
    assert load_all()["w-consumer/009"](case(site, "home", "w-consumer/009")).state == google
    assert load_all()["w-consumer/011"](case(site, "home", "w-consumer/011")).state == rfc


def test_robots_disallow_for_a_bot(tmp_path):
    site = make_audit(tmp_path, {"home": ("home", f"{SITE}/a", "<title>x</title>", None)},
                      robots="User-agent: OAI-SearchBot\nDisallow: /\n\nUser-agent: *\nAllow: /\n")
    assert load_all()["w-consumer/011"](case(site, "home", "w-consumer/011")).state == UNSAT
    assert load_all()["w-consumer/012"](case(site, "home", "w-consumer/012")).state == SAT


def test_sitemap_not_obtained_is_ne(tmp_path):
    site = make_audit(tmp_path, {"home": ("home", f"{SITE}/", "<title>x</title>", None)},
                      sitemaps=[(f"{SITE}/sitemap.xml", 503, None)])
    assert load_all()["w-consumer/014"](case(site, "home", "w-consumer/014")).state == NE
    assert load_all()["w-protocol/004"](case(site, None, "w-protocol/004")).state == NE


def test_no_sitemap_means_not_in_it(tmp_path):
    site = make_audit(tmp_path, {"home": ("home", f"{SITE}/", "<title>x</title>", None)},
                      sitemaps=[(f"{SITE}/sitemap.xml", 404, None)])
    assert load_all()["w-consumer/014"](case(site, "home", "w-consumer/014")).state == UNSAT
    assert load_all()["w-protocol/004"](case(site, None, "w-protocol/004")).state == NA


def test_noindex_and_status(tmp_path):
    doc = '<html><head><meta name="robots" content="noindex"><title>x</title></head><body>x</body></html>'
    site = make_audit(tmp_path, {"p": ("policy", f"{SITE}/p", doc, None),
                                 "q": ("policy", f"{SITE}/q", "<title>x</title>", {"status": 403, "outcome": "failed"})})
    assert load_all()["w-consumer/010"](case(site, "p", "w-consumer/010")).state == UNSAT
    assert load_all()["w-consumer/002"](case(site, "q", "w-consumer/002")).state == NE


# --- Rate and judgements -----------------------------------------------------------------------------

def test_counts_follow_d166_d169():
    cases = [{"state": s, "nature": "obligatoria"} for s in (SAT, SAT, UNSAT, NA, NE)]
    c = audit.counts(cases)
    assert (c["pertinentes"], c["evaluados"], c["satisfechos"]) == (5, 3, 2)
    assert c["tasa"] == round(2 / 3, 4)
    assert c["cobertura"] == round(3 / 4, 4)
    only_na = audit.counts([{"state": NA, "nature": "obligatoria"}])
    assert only_na["tasa"] is None and only_na["cobertura"] is None


def test_validate_judgments():
    pending = [{"req": "w-consumer/003", "page": "home"}]
    assert audit.validate(pending, [{"req": "w-consumer/003", "page": "home", "state": SAT, "evidence": "ok"}]) == []
    errors = audit.validate(pending, [{"req": "w-consumer/003", "page": "home", "state": NE, "evidence": "x"},
                                      {"req": "x", "page": None, "state": "bien", "evidence": ""}])
    assert any("motivo" in e for e in errors) and any("no es un caso pendiente" in e for e in errors)
    assert audit.validate(pending, []) == ["falta el juicio de w-consumer/003 en home"]


@needs_vocab
def test_end_to_end(tmp_path, monkeypatch):
    site = make_audit(tmp_path, {"product-01": ("product", f"{SITE}/cojin", PRODUCT, None),
                                 "home": ("home", f"{SITE}/", "<html><head><title>Tienda</title></head><body>Hola</body></html>", None)})
    monkeypatch.setattr(audit, "OUT", tmp_path / "out")
    monkeypatch.setattr(audit, "Site", lambda audit_id: site)
    cases, pending = audit.run("aud")
    assert {c["state"] for c in cases} <= {SAT, UNSAT, NA, NE, PENDING}
    judgments = [{"req": p["req"], "page": p["page"], "state": NA, "evidence": "La página no lo muestra.",
                  "reason": "No se da la aplicabilidad."} for p in pending]
    (tmp_path / "out" / "aud" / "judgments.json").write_text(json.dumps(judgments))
    dossier = audit.finish("aud")
    product = dossier["rate"]["Web Schema.org"]["particular"]["ficha de producto"]["total"]
    assert product["evaluados"] == product["pertinentes"] - product["NA"] - product["NE"]
    assert (tmp_path / "out" / "aud" / "report.md").read_text().startswith("# Expediente técnico")


def test_crawl_audit_evaluates_sitemap_on_every_page(tmp_path, monkeypatch):
    """An audit of the spider (D-170, D-217): audit.json beside crawl.json, with pages found only by
    the crawl. The method does not change: w-consumer/014 is evaluated on each audited page."""
    xml = (b'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           b'<url><loc>https://shop.example/</loc></url><url><loc>https://shop.example/cojin</loc></url></urlset>')
    home = "<html><head><title>Tienda</title></head><body>Hola</body></html>"
    site = make_audit(tmp_path, {"page-00001": ("home", f"{SITE}/", home, None),
                                 "page-00002": ("product", f"{SITE}/cojin", PRODUCT, None),
                                 "page-00003": ("product", f"{SITE}/manta", PRODUCT.replace("cojin", "manta"), None)},
                      sitemaps=[(f"{SITE}/sitemap.xml", 200, xml)])
    manifest = json.loads((site.folder / "audit.json").read_text())
    manifest["crawl"] = {"manifest": "crawl.json", "coverage": {"complete": True}}
    for depth, rec in enumerate(manifest["pages"]):
        rec.update({"depth": depth, "found_from": None if depth == 0 else "page-00001"})
    (site.folder / "audit.json").write_text(json.dumps(manifest))
    (site.folder / "crawl.json").write_text(json.dumps({"universe": [
        {"url": f"{SITE}/", "page": "page-00001", "reached": "yes", "in_sitemaps": "yes", "type": "home"},
        {"url": f"{SITE}/cojin", "page": "page-00002", "reached": "yes", "in_sitemaps": "yes", "type": "product"},
        {"url": f"{SITE}/manta", "page": "page-00003", "reached": "yes", "in_sitemaps": "no", "type": "product"}]}))
    site = Site("aud", site.folder)
    monkeypatch.setattr(audit, "OUT", tmp_path / "out")
    monkeypatch.setattr(audit, "Site", lambda audit_id: site)
    cases, _ = audit.run("aud")
    states = {c["page"]: c["state"] for c in cases if c["req"] == "w-consumer/014"}
    assert states == {"page-00001": SAT, "page-00002": SAT, "page-00003": UNSAT}


def test_sitemap_in_subdirectory_counts_for_its_host(tmp_path):
    """Google's reading (method common to Web, point 5): a submitted sitemap is valid for its whole
    host; the protocol's strict location is w-protocol/009."""
    xml = (b'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           b'<url><loc>https://shop.example/cojin</loc></url></urlset>')
    site = make_audit(tmp_path, {"product-01": ("product", f"{SITE}/cojin", PRODUCT, None)},
                      sitemaps=[(f"{SITE}/sitemaps/es/products.xml", 200, xml)])
    assert load_all()["w-consumer/014"](case(site, "product-01", "w-consumer/014")).state == SAT
    assert load_all()["w-protocol/009"](case(site, None, "w-protocol/009")).state == UNSAT
