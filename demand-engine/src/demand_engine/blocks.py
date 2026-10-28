"""Deterministic skeleton of the category blocks (cat.) of the catalog (D-038 to D-040).

Usage:
  blocks plan CATEGORY_ID [...] [--ptd CATEGORY_ID=PTD[:NODE] ...]
                                  the blocks of the given Shopify categories and all their
                                  ancestors, as JSON on stdout; --ptd maps a category that
                                  catalog/amazon-map.json lacks to its Amazon PTD (runtime)

Each block holds the Shopify attributes that its category lists and none of its
ancestors lists: a repeated attribute goes to the most general category that lists
it, so a block has the same content whatever the product (D-040). The properties of
an Amazon PTD (product_details group, the descriptive compliance_* properties and
fabric weight of the safety_and_compliance group, and the values of special_feature) are proposed
as candidates for the most general category of the chain that catalog/amazon-map.json
maps to that PTD (D-039); generic or administrative properties, and those that
repeat a Shopify attribute of the chain, are left out. Deciding which candidates are
relevant and writing the questions, their trait and the vote is the drafting step
(catalog/DRAFTING.md); importance comes from the compiled rules (D-045).
"""
import json
import sys

from references.read import enum_values, google_mapping, ptd, shopify_attributes, shopify_categories, short
from references.store import RefsError, pins

from . import ROOT

SKIP_PTD = {
    "product_description", "bullet_point", "generic_keyword", "item_name", "brand", "part_number", "model_number",
    "model_name", "manufacturer", "unit_count", "item_package_quantity", "number_of_items", "number_of_packs",
    "product_site_launch_date", "league_name", "team_name", "athlete", "subject_character", "language", "edition",
    "configuration", "customer_package_type", "handmade_classification", "theme", "animal_theme", "personalization_font",
    "recommended_browse_nodes", "externally_assigned_product_identifier", "merchant_suggested_asin", "item_display_dimensions",
    "supplier_declared_has_product_identifier_exemption", "package_level", "package_contains_sku", "set_name",
    "title_differentiation", "item_type_name", "flavor", "scent", "style", "embellishment_feature", "occasion",
    "orientation", "is_fragile", "item_shape", "special_feature", "shape_variant_name", "fit_to_size_sentiment",
}
COMPLIANCE_KEEP = {"fabric_weight", "fur", "safety_warning"}  # descriptive properties outside product_details
COMPLIANCE_SKIP = {"compliance_media", "compliance_is_handmade", "compliance_age_range"}
SAME_AS_SHOPIFY = {  # PTD property -> Shopify handles that already cover the dimension
    "color": {"color"}, "pattern": {"pattern"}, "pattern_type": {"pattern"}, "material": {"material", "fabric"},
    "care_instructions": {"care-instructions"}, "size": {"bedding-size", "shoe-size", "size"},
    "age_range_description": {"age-group"}, "target_gender": {"target-gender"}, "fill_material": {"filler-material"},
    "seasons": {"season"}, "closure": {"closure-type", "cover-closure-design"}, "fit_type": {"shoe-fit"},
}


def ptd_candidates(product_type: str, covered: set) -> list:
    props, definition = ptd(product_type)
    out = []
    names = list(definition["propertyGroups"].get("product_details", {}).get("propertyNames", []))
    names += [n for n in definition["propertyGroups"].get("safety_and_compliance", {}).get("propertyNames", [])
              if (n.startswith("compliance_") and n not in COMPLIANCE_SKIP) or n in COMPLIANCE_KEEP]
    for name in names:
        if name in SKIP_PTD or SAME_AS_SHOPIFY.get(name, set()) & covered:
            continue
        values = enum_values(props[name])
        out.append({"source": f"amazon-ptd-prop:{product_type}.{name}", "title": props[name].get("title", ""),
                    "values": values[:20] if len(values) < 400 else []})
    if "special_feature" in props:
        for v in enum_values(props["special_feature"]):
            out.append({"source": f"amazon-ptd-prop:{product_type}.special_feature={v}", "title": f"Característica especial: {v}"})
    return out


def plan(ids: list, extra_map: dict = None) -> dict:
    cats, attrs = shopify_categories(), shopify_attributes()
    english = {k: (en, [g for g, _ in outputs]) for k, (en, outputs) in google_mapping().items()}
    amazon = json.loads((ROOT / "catalog/amazon-map.json").read_text(encoding="utf-8"))["map"]
    amazon.update(extra_map or {})
    versions = pins("demand-engine")
    blocks = {}
    for cid in ids:
        if cid not in cats:
            sys.exit(f"blocks: no existe la categoría {cid}")
        chain = [short(a["id"]) for a in reversed(cats[cid].get("ancestors", []))] + [cid]  # root first
        chain_handles = set()
        for i, c in enumerate(chain):
            above = set()
            for a in chain[:i]:
                above |= {x["handle"] for x in cats[a]["attributes"]}
            own = [x["handle"] for x in cats[c]["attributes"] if x["handle"] not in above]
            chain_handles |= {x["handle"] for x in cats[c]["attributes"]}
            if c in blocks:
                continue
            en, google = english.get(c, ("", []))
            blocks[c] = {
                "shopify": c, "name": cats[c]["name"], "full_name": cats[c]["full_name"], "english": en,
                "parent": chain[i - 1] if i else None, "children_in_plan": [],
                "refs": [f"shopify:{c}@{versions['shopify']}"] + [f"google:{g}@{versions['google']}" for g in google],
                "attributes": [{"source": f"shopify-attr:{h}", "name": attrs.get(h, {}).get("name", h),
                                "description": attrs.get(h, {}).get("description", ""),
                                "values": [v["name"] for v in attrs.get(h, {}).get("values", [])][:25]} for h in own],
                "amazon": [],
            }
        for i, c in enumerate(chain[1:], 1):
            if c not in blocks[chain[i - 1]]["children_in_plan"]:
                blocks[chain[i - 1]]["children_in_plan"].append(c)
        mapped = next((c for c in chain if c in amazon), None)
        if mapped and not blocks[mapped]["amazon"]:
            m = amazon[mapped]
            blocks[mapped]["refs"].append(f"amazon-ptd:{m['ptd']}@{versions['amazon-ptd']}")
            if m.get("node"):
                blocks[mapped]["refs"].append(f"amazon-btg:{m['node']}@{versions['amazon-btg']}")
            blocks[mapped]["amazon"] = ptd_candidates(m["ptd"], chain_handles)
    return {"rule": "D-040: cada atributo, en la categoría más general que lo lista; candidatos de Amazon, D-039",
            "blocks": list(blocks.values())}


def main() -> None:
    if len(sys.argv) < 3 or sys.argv[1] != "plan":
        sys.exit(__doc__)
    ids, extra, args = [], {}, sys.argv[2:]
    while args:
        a = args.pop(0)
        if a == "--ptd" and args:
            cat, _, target = args.pop(0).partition("=")
            ptd, _, node = target.partition(":")
            extra[cat] = {"ptd": ptd, "node": node or None, "relation": "ejecución"}
        else:
            ids.append(a)
    try:
        print(json.dumps(plan(ids, extra), ensure_ascii=False, indent=2))
    except RefsError as exc:
        sys.exit(f"blocks: {exc}")


if __name__ == "__main__":
    main()
