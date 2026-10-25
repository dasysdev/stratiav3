"""Compare classification runs with the expected cases, or two runs with each other.

Usage:
  compare RUN_DIR [CASE_ID ...]          run against the expected cases
  compare --pair RUN_A RUN_B [CASE_ID ...]
                                         stability between two runs of the same cases

Handles rulebook v0 outputs (class composition and specializations) and v1 outputs
(blocks, application, denomination). For v1 the comparison is made on what the
model asks, not on labels: an expected key question counts as covered if some
requirement of the model shares most of its significant words. Word matching is
approximate; the report is a starting point for manual review.
"""
import json
import re
import sys
from pathlib import Path

from . import ROOT
from .demand.text import covers, match_names, stem, words

CASES = ROOT / "cases"


def requirements(out: dict) -> list:
    return [(b, r) for b in out.get("blocks", []) for r in b.get("requirements", []) if isinstance(r, dict)]


def shopify_refs(block: dict) -> set:
    return {m.group(1) for ref in block.get("refs", []) for m in [re.match(r"shopify:([^@]+)@", ref)] if m}


def composition(out: dict) -> tuple:
    cats = out.get("composition", {}).get("categories", [])
    return ({c.get("shopify") for c in cats if not c.get("alias")}, {c.get("shopify") for c in cats if c.get("alias")})


def esp_blocks(out: dict) -> list:
    return [b for b in out.get("blocks", []) if b.get("type") == "especialización" or str(b.get("id", "")).startswith("esp.")]


def esp_label(b: dict) -> str:
    return f"{b.get('id', '')} {b.get('name', '')} {b.get('trigger', '')}".replace(".", " ").replace("-", " ")


def active(out: dict) -> set:
    return {a.get("block") if isinstance(a, dict) else a for a in out.get("application", {}).get("active", [])}


def expected_questions(case: dict) -> list:
    exp = case["expected"]
    qs = [q for s in exp["specializations"] for q in s.get("questions", [])]
    qs += [q for f in exp.get("features", []) for q in f.get("questions", []) if f.get("role", "").startswith(("valor que condiciona", "requisito", "cuestión", "respuesta"))]
    return qs


def compare_v1(case: dict, out: dict, totals: dict) -> None:
    exp = case["expected_v1"]
    cats, alias = composition(out)
    ok_cats = cats == set(exp["categories"]) and alias == set(exp["alias"])
    totals["composition"] += ok_cats
    print(f"  composición: {'igual' if ok_cats else 'distinta'} · obtenida {sorted(cats)} alias {sorted(alias)}"
          + ("" if ok_cats else f" · esperada {exp['categories']} alias {exp['alias']}"))
    pairs, extra = match_names([s["name"] for s in exp["specializations"]], [esp_label(b) for b in esp_blocks(out)])
    ok_esp = all(o for _, o in pairs) and not extra
    totals["specializations"] += ok_esp
    print(f"  especializaciones: {'coinciden' if ok_esp else 'difieren'}")
    for e, o in pairs:
        print(f"    {e:<32} ↔ {o or '— (falta)'}")
    for o in extra:
        print(f"    {'— (no esperada)':<32} ↔ {o}")
    reqs = requirements(out)
    qs = expected_questions(case)
    hit = [q for q in qs if any(covers(q, r.get("question", "")) for _, r in reqs)]
    totals["questions"] += len(hit)
    totals["questions_all"] += len(qs)
    if qs:
        print(f"  cuestiones clave cubiertas en el modelo: {len(hit)}/{len(qs)}"
              + (f" · faltan {[q for q in qs if q not in hit]}" if len(hit) < len(qs) else ""))
    if exp.get("application") is not None:
        want, got = set(exp["application"]), active(out)
        ok_app = want <= got
        totals["application"] += ok_app
        totals["application_all"] += 1
        print(f"  aplicación: {'contiene lo esperado' if ok_app else 'incompleta'} · activa {sorted(got)}"
              + ("" if ok_app else f" · faltan {sorted(want - got)}"))
    groups = exp.get("inferred_any_of") or []
    if groups:
        inferred = [r.get("question", "") for _, r in reqs if r.get("origin") == "inferida"]
        ok_inf = any(all(stem(w) in {stem(x) for x in words(q)} for w in g) for g in groups for q in inferred)
        totals["inferred"] += ok_inf
        totals["inferred_all"] += 1
        print(f"  cuestión inferida esperada: {'presente' if ok_inf else 'ausente'}")
    imp = {}
    for _, r in reqs:
        imp[r.get("importance")] = imp.get(r.get("importance"), 0) + 1
    n_inf = sum(1 for _, r in reqs if r.get("origin") == "inferida")
    print(f"  requisitos propios del modelo: {len(reqs)} · importancia {imp} · inferidos {n_inf} · "
          f"revisiones de la capa general {len(out.get('general_overrides', []))}")
    print(f"  nombre: {out.get('denomination', {}).get('name')}")


def compare_v0(case: dict, out: dict, totals: dict) -> None:
    exp = case["expected"]
    want = {c["shopify"] for c in exp["components"]}
    got = {c.get("shopify") for c in out.get("components", [])}
    totals["composition"] += want == got
    print(f"  componentes: {'iguales' if want == got else 'distintos'}")
    pairs, extra = match_names([s["name"] for s in exp["specializations"]], [s.get("name", "") for s in out.get("specializations", [])])
    totals["specializations"] += all(o for _, o in pairs) and not extra


def against_expected(run: Path, ids: list) -> None:
    totals = dict.fromkeys(["cases", "composition", "specializations", "questions", "questions_all",
                            "application", "application_all", "inferred", "inferred_all", "missing"], 0)
    for case_id in ids:
        case = json.loads((CASES / f"{case_id}.json").read_text(encoding="utf-8"))
        path = run / f"{case_id}.json"
        print(f"\n=== {case_id} ({case['vertical']})")
        if not path.exists():
            print("  sin resultado")
            totals["missing"] += 1
            continue
        out = json.loads(path.read_text(encoding="utf-8"))
        totals["cases"] += 1
        (compare_v1 if out.get("rulebook") == "v1" else compare_v0)(case, out, totals)
        for d in out.get("doubts", [])[:3]:
            print(f"  duda: {str(d)[:200]}")
    n = totals["cases"]
    print(f"\nCasos: {n} · composición igual {totals['composition']}/{n} · especializaciones {totals['specializations']}/{n} · "
          f"cuestiones clave {totals['questions']}/{totals['questions_all']} · aplicación {totals['application']}/{totals['application_all']} · "
          f"inferidas esperadas {totals['inferred']}/{totals['inferred_all']} · sin resultado {totals['missing']}")


def model_key(out: dict) -> tuple:
    cats = set()
    for b in out.get("blocks", []):
        if b.get("type") == "categoría" or str(b.get("id", "")).startswith("cat."):
            cats |= shopify_refs(b)
    return cats, [esp_label(b) for b in esp_blocks(out)]


def req_key(block: dict, req: dict):
    attrs = [s for s in req.get("sources", []) if s.startswith("shopify-attr:")]
    refs = sorted(shopify_refs(block))
    return (refs[0] if refs else block.get("id"), attrs[0]) if attrs else None


def pair(run_a: Path, run_b: Path, ids: list) -> None:
    agg = dict.fromkeys(["cases", "cats", "esp", "app", "attr_a", "attr_b", "attr_both", "imp_same", "free_a", "free_b", "free_both"], 0)
    for case_id in ids:
        pa, pb = run_a / f"{case_id}.json", run_b / f"{case_id}.json"
        if not (pa.exists() and pb.exists()):
            print(f"\n=== {case_id}: falta una de las ejecuciones")
            continue
        a, b = json.loads(pa.read_text(encoding="utf-8")), json.loads(pb.read_text(encoding="utf-8"))
        agg["cases"] += 1
        (ca, ea), (cb, eb) = model_key(a), model_key(b)
        pairs, extra = match_names(ea, eb)
        same_esp = all(o for _, o in pairs) and not extra
        same_app = active(a) == active(b)
        agg["cats"] += ca == cb
        agg["esp"] += same_esp
        agg["app"] += same_app
        ka = {req_key(bl, r): r for bl, r in requirements(a) if req_key(bl, r)}
        kb = {req_key(bl, r): r for bl, r in requirements(b) if req_key(bl, r)}
        both = ka.keys() & kb.keys()
        same_imp = sum(1 for k in both if ka[k].get("importance") == kb[k].get("importance"))
        fa = [r.get("question", "") for bl, r in requirements(a) if not req_key(bl, r)]
        fb = [r.get("question", "") for bl, r in requirements(b) if not req_key(bl, r)]
        fpairs, _ = match_names(fa, fb)
        fboth = sum(1 for _, o in fpairs if o)
        for k, v in (("attr_a", len(ka)), ("attr_b", len(kb)), ("attr_both", len(both)), ("imp_same", same_imp),
                     ("free_a", len(fa)), ("free_b", len(fb)), ("free_both", fboth)):
            agg[k] += v
        print(f"\n=== {case_id}")
        print(f"  categorías {'=' if ca == cb else '≠'} · especializaciones {'=' if same_esp else '≠'} · aplicación {'=' if same_app else '≠'}")
        print(f"  nombre A: {a.get('denomination', {}).get('name')}")
        print(f"  nombre B: {b.get('denomination', {}).get('name')}")
        print(f"  requisitos de atributos: A {len(ka)} · B {len(kb)} · comunes {len(both)} · misma importancia {same_imp}/{len(both)}")
        print(f"  otros requisitos (inferidos y de especialización): A {len(fa)} · B {len(fb)} · emparejados {fboth}")
    n = agg["cases"]
    print(f"\nCasos: {n} · categorías iguales {agg['cats']}/{n} · especializaciones iguales {agg['esp']}/{n} · aplicación igual {agg['app']}/{n}")
    print(f"Requisitos de atributos comunes: {agg['attr_both']} de {agg['attr_a']} (A) y {agg['attr_b']} (B) · "
          f"misma importancia {agg['imp_same']}/{agg['attr_both']}")
    print(f"Otros requisitos emparejados: {agg['free_both']} de {agg['free_a']} (A) y {agg['free_b']} (B)")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--pair":
        if len(args) < 3:
            sys.exit(__doc__)
        ids = args[3:] or sorted(p.stem for p in CASES.glob("*.json"))
        pair(Path(args[1]), Path(args[2]), ids)
    else:
        ids = args[1:] or sorted(p.stem for p in CASES.glob("*.json"))
        against_expected(Path(args[0]), ids)


if __name__ == "__main__":
    main()
