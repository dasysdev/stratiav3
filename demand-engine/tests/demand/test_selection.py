"""Selection of the training catalog (T-024): one page per product, types by department, fixed seed."""
import gzip
import json

from demand_engine.demand.selection import product_type, select

BASE = "https://shop.test"
SPEC = {
    "store": "t", "base_url": BASE, "sitemap": BASE + "/sitemap.xml", "follow_products": "products",
    "product": r"^https://shop\.test/(?P<dept>[a-z-]+)/(?P<id>A\d+)(?:-[^/]*?)?-pr-(?P<slug>[^/]+)/$",
    "exclude_departments": ["entradas"], "title_departments": ["libros"], "stopwords": ["juego", "de"],
    "seed": 7, "categories": 4, "per_category": 2, "reserves": 1, "pilot": 2, "min_products": 3,
}


def url(dept, pid, slug, variant=""):
    return f"{BASE}/{dept}/A{pid}{'-' + variant if variant else ''}-pr-{slug}/"


def discovery(tmp_path, urls, robots="User-agent: *\nDisallow: /privado/\n"):
    (tmp_path / "robots.txt").write_text(robots)
    (tmp_path / "products.json.gz").write_bytes(gzip.compress(json.dumps(urls).encode()))
    (tmp_path / "categories.json.gz").write_bytes(gzip.compress(json.dumps(
        [f"{BASE}/hogar/mesa/sartenes/", f"{BASE}/hogar/cocina/menaje/sartenes-y-cazos/"]).encode()))
    (tmp_path / "discovery.json").write_text(json.dumps({"at": "2026-10-25", "flags": []}))
    return tmp_path


def catalog():
    urls = []
    for n in range(4):
        urls += [url("hogar", 100 + n, f"sarten-{n}-tefal"), url("hogar", 200 + n, f"juego-de-2-vasos-{n}")]
        urls += [url("moda", 300 + n, f"vestido-{n}", "rojo"), url("moda", 300 + n, f"vestido-{n}", "azul")]
        urls += [url("libros", 400 + n, f"el-quijote-{n}"), url("entradas", 500 + n, f"concierto-{n}")]
        urls += [url("privado", 600 + n, f"sarten-{n}")]
    urls += [url("moda", 700, "falda-unica")]  # too few products of its type
    return urls


def test_product_type_skips_the_stoplist():
    assert product_type("juego-de-2-vasos-de-vino", {"juego", "de"}) == "vaso"
    assert product_type("calcetines-cortos", set()) == "calcetin"
    assert product_type("10-x", set()) is None


def test_one_page_per_product_and_scope(tmp_path):
    result = select(SPEC, discovery(tmp_path, catalog()))
    c = result["counts"]
    assert c["variant"] == 4 and c["excluded_department"] == 4 and c["disallowed"] == 4
    types = {cat["category"] for cat in result["categories"]}
    assert types <= {"hogar/sarten", "hogar/vaso", "moda/vestido", "libros/libros"}
    assert "moda/falda" not in types
    for cat in result["categories"]:
        assert len(cat["pages"]) == 2 and len(cat["reserves"]) == 1
        assert len({p["product"] for p in cat["pages"] + cat["reserves"]}) == 3


def test_seed_is_deterministic_and_pilot_spans_departments(tmp_path):
    folder = discovery(tmp_path, catalog())
    a, b = select(SPEC, folder), select(SPEC, folder)
    assert a["categories"] == b["categories"]
    pilot = [cat for cat in a["categories"] if cat["pilot"]]
    assert len(pilot) == 2 and len({cat["department"] for cat in pilot}) == 2
    assert a["counts"]["selected_departments"] == 3


def test_store_category_names_the_type(tmp_path):
    result = select(SPEC, discovery(tmp_path, catalog()))
    sarten = next(cat for cat in result["categories"] if cat["category"] == "hogar/sarten")
    assert sarten["store_category"] == f"{BASE}/hogar/mesa/sartenes/"


def test_types_can_be_required_to_have_a_store_category(tmp_path):
    result = select({**SPEC, "require_store_category": True}, discovery(tmp_path, catalog()))
    assert [cat["category"] for cat in result["categories"]] == ["hogar/sarten"]
