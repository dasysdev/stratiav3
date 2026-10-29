"""Specializations induced by the training (D-190): blocks of the catalog with a citable rule.

Up to rulebook v3 the classifier drafted each specialization inline in each run, so the same one could
take two names (esp.a-bateria, esp.bateria) and its requirements never had a stable id. The training
now turns what the runs propose into blocks of catalog/esp/:

- Synonyms: two ids of the same vertical whose significant words (name and id, without accents) share at
  least half of the words of both are one specialization. Its id is the one already compiled; otherwise
  the most observed; a tie goes to the first in alphabetical order.
- Anchor: along the Shopify tree, as the importance rules (D-045): it lives in the classes where it is
  observed and climbs to the parent when at least two children have it and all the children with data
  share it; never above the verticals. The anchors of a registered block are kept (no data go against them).
- Requirements: the seed is the first block registered (catalog, then runtime) or, for the runs of
  rulebook v3, the first admissible proposal in the order of the runs; a requirement that another proposal adds enters
  as a proposal to the block, as D-088 does with the inferred ones, unless the block covers it: the block
  has half of its significant words, or it has all of those of a question of the block.
- Admission: no threshold of cases. The family passes the gate of the metrics (no metric worse, one
  better); each specialization must respect the framework: support in the references (D-024), an order of
  the rulebook and requirements with question, trait and resolving information (D-063). A proposal to the
  block without resolving information does not enter.

The rule of a specialization is esp:<id>@<node>, one per anchor.
"""
import datetime
import unicodedata
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from .catalog import (COMPILED, ESP_DIR, ESP_ORDER, ESP_RUNTIME_DIR, LEVELS, NO_RULE, chain, depth, parent, read_json,
                      requirement_trait, resolve, vertical, write_json)
from .text import covers, stems

SYNONYM = 0.5  # share of the significant words two ids of a vertical must share to be one specialization
REQUIREMENT_FIELDS = ("id", "question", "dimension", "entity", "trait", "origin", "sources", "applicability", "rationale",
                      "seed_importance", "resolving_info", "hints")


def plain(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", text or "") if unicodedata.category(c) != "Mn")


def words(spec_id: str, names) -> set:
    """Significant words of a specialization: its names and its id, without accents."""
    text = " ".join(list(names) + [spec_id.removeprefix("esp.").replace("-", " ")])
    return stems(plain(text))


def drafted(run: str, case: str, spec_id: str) -> list:
    """The requirements the classifier drafted inline for a specialization (rulebook v3), from its output."""
    path = Path(run) / f"{case}.json"
    if not path.exists():
        return []
    out = read_json(path)
    for e in out.get("specializations", []):
        if e.get("id") == spec_id:
            return [dict(r, id=r.get("id") or f"{spec_id}/{i:02d}") for i, r in enumerate(e.get("requirements", []), 1)]
    return []


def observations(models: dict) -> list:
    """Each specialization of each assembled model, in the order of the runs and the cases: id, name, order,
    trigger, support, classes and store; the requirements drafted inline when the model drafted it (no anchors)."""
    out = []
    for run, cases in models.items():
        for case, m in cases.items():
            for b in m["blocks"]:
                if b["type"] != "especialización":
                    continue
                inline = "anchors" not in b
                out.append({"id": b["id"], "name": b.get("name") or "", "order": b.get("order"),
                            "trigger": b.get("trigger"), "support": b.get("support", []),
                            "classes": m["composition"]["classes"], "store": store(m.get("url")),
                            "run": run, "case": case,
                            "requirements": drafted(run, case, b["id"]) if inline else []})
    return out


def store(url) -> str:
    host = (url or "").split("//", 1)[-1].split("/", 1)[0]
    return host.removeprefix("www.")


def synonyms(obs: list, specs: dict) -> dict:
    """{id: canonical id}: ids of one vertical that share at least half of their significant words are one
    specialization; the compiled id wins, else the most observed, else the first in alphabetical order."""
    names, verts, count = defaultdict(set), defaultdict(set), Counter()
    for o in obs:
        names[o["id"]].add(o["name"])
        verts[o["id"]] |= {vertical(c) for c in o["classes"]}
        count[o["id"]] += 1
    for sid, s in specs.items():
        names[sid].add(s.get("name") or "")
        verts[sid] |= {vertical(a) for a in s.get("anchors", [])}
        for a in s.get("aliases", []):
            names[sid].add(a.removeprefix("esp.").replace("-", " "))
    group = {sid: sid for sid in names}

    def root(x):
        while group[x] != x:
            x = group[x]
        return x

    for a, b in combinations(sorted(names), 2):
        wa, wb = words(a, names[a]), words(b, names[b])
        if verts[a] & verts[b] and wa and wb and len(wa & wb) >= SYNONYM * max(len(wa), len(wb)):
            group[root(b)] = root(a)
    members = defaultdict(list)
    for sid in names:
        members[root(sid)].append(sid)
    out = {}
    for ids in members.values():
        compiled = [i for i in ids if specs.get(i, {}).get("_where") == "catálogo"]
        canonical = min(compiled or ids, key=lambda i: (-count[i], i))
        out.update({i: canonical for i in ids})
    for s in specs.values():  # synonyms merged in earlier cycles
        out.update({a: out[s["id"]] for a in s.get("aliases", [])})
    return out


def anchors(classes, kept=()) -> list:
    """Where a specialization lives (D-045, D-190): the classes where it is observed and the registered anchors; a parent
    when at least two children have it and every child with data does; never above the verticals."""
    has = set(classes) | set(kept)
    nodes = {n for c in has for n in chain(c)}
    for n in sorted(nodes, key=depth, reverse=True):
        kids = [c for c in nodes if parent(c) == n]
        if n not in has and len(kids) >= 2 and all(k in has for k in kids):
            has.add(n)
    return sorted(n for n in has if not any(a in has for a in chain(n)[:-1]))


def catalog_requirement(r: dict) -> dict:
    """The fields of a drafted requirement that the catalog keeps; its vote becomes the starting label."""
    out = {k: r[k] for k in REQUIREMENT_FIELDS if r.get(k) is not None}
    out.setdefault("seed_importance", r.get("vote") if r.get("vote") in LEVELS else "complementario")
    out.setdefault("origin", "referencias" if r.get("sources") else "inferida")
    out.setdefault("applicability", "universal")
    out["resolving_info"] = [{k: v for k, v in c.items() if k != "stores"} for c in r.get("resolving_info", [])]
    return out


def framework_problems(block: dict) -> list:
    """What the framework does not admit in a specialization (D-024, rulebook step 4)."""
    problems = []
    if not block.get("support"):
        problems.append("sin apoyo en las referencias (D-024)")
    if block.get("order") not in ESP_ORDER:
        problems.append(f"orden «{block.get('order')}» fuera del reglamento")
    if not block.get("requirements"):
        problems.append("sin requisitos")
    problems += [f"{r.get('id')}: sin pregunta o sin rasgo" for r in block.get("requirements", [])
                 if not r.get("question") or not r.get("trait")]
    problems += [f"{r.get('id')}: sin información resolutiva (D-063)" for r in block.get("requirements", [])
                 if not r.get("resolving_info")]
    return problems


def induce(models: dict, specs: dict) -> dict:
    """The specializations the runs propose, as blocks (D-190): {"table", "rules", "blocks", "rejected"}.
    table: {id: {anchors, aliases, cases, stores}}; blocks: the block of each id, seed and proposals."""
    obs = observations(models)
    canon = synonyms(obs, specs)
    by_spec = defaultdict(list)
    for o in obs:
        by_spec[canon[o["id"]]].append(o)
    table, rules, blocks, rejected = {}, [], {}, []
    for sid in sorted(set(by_spec) | {canon[s] for s in specs}):
        seen = by_spec.get(sid, [])
        group = sorted({i for i, c in canon.items() if c == sid})
        block = seed_block(sid, group, seen, specs)
        if block is None:
            continue
        observed = sorted({c for o in seen for c in o["classes"]})
        kept = sorted({a for i in group for a in specs.get(i, {}).get("anchors", [])})
        block["anchors"] = anchors(observed, kept)
        block["aliases"] = [i for i in group if i != sid]
        problems = framework_problems(block)
        if problems:
            rejected.append({"id": sid, "problems": problems, "cases": len(seen)})
            continue
        blocks[sid] = block
        table[sid] = {"anchors": block["anchors"], "aliases": block["aliases"], "cases": len({o["case"] for o in seen}),
                      "observations": len(seen), "stores": sorted({o["store"] for o in seen if o["store"]})}
        for n in block["anchors"]:
            rules.append({"id": f"esp:{sid}@{n}", "kind": "especialización", "specialization": sid, "node": n,
                          "climbed": n not in observed and n not in kept,
                          "cases": len({o["case"] for o in seen if any(c == n or c.startswith(n + "-") for c in o["classes"])})})
    return {"table": table, "rules": rules, "blocks": blocks, "rejected": rejected}


def seed_block(sid: str, group: list, seen: list, specs: dict):
    """The block of a specialization: its registered block (catalog first) or the first inline proposal, plus the
    requirements other proposals add that no requirement of the block covers (proposals to the block, D-088)."""
    registered = specs.get(sid) or next((specs[i] for i in group if i in specs), None)
    drafts = [o for o in seen if o["requirements"]]
    if registered is not None:
        block = {k: v for k, v in registered.items() if not k.startswith("_")}
        block["id"] = sid
        block["requirements"] = [catalog_requirement(r) for r in registered["requirements"]]
    elif drafts:
        # the first admissible proposal, its own id first: one drafted before D-063 has no resolving information
        complete = [o for o in drafts if all(r.get("resolving_info") for r in o["requirements"])] or drafts
        first = next((o for o in complete if o["id"] == sid), complete[0])
        block = {"id": sid, "type": "especialización", "name": first["name"], "order": first["order"],
                 "trigger": first["name"], "support": first["support"],  # the inline trigger is the evidence of a page
                 "generated": datetime.date.today().isoformat(), "seed": f"{first['case']} ({Path(first['run']).name})",
                 "requirements": [catalog_requirement(r) for r in first["requirements"]]}
        drafts = [o for o in drafts if o is not first]
    else:
        return None
    for r in block["requirements"]:
        r["id"] = renumber(r["id"], sid)
    for o in drafts:
        for r in o["requirements"]:
            if not r.get("resolving_info"):  # drafted before D-063: the catalog does not admit it
                continue
            text = f"{r.get('dimension') or ''} {r.get('question')}"
            asked = [f"{q.get('dimension') or ''} {q['question']}" for q in block["requirements"]]
            if covers(text, " ".join(asked)) or any(stems(q) and stems(q) <= stems(text) for q in asked):
                continue
            used = [int(x["id"].rsplit("/", 1)[1]) for x in block["requirements"]]
            entry = catalog_requirement(r)
            entry["id"] = f"{sid}/{max(used, default=0) + 1:02d}"
            entry["rationale"] = (f"{entry.get('rationale') or ''} Propuesta al bloque (D-190, como D-088) desde "
                                  f"{o['case']} ({Path(o['run']).name}).").strip()
            block["requirements"].append(entry)
    return block


def renumber(rid: str, sid: str) -> str:
    """A requirement of a merged synonym takes the id of the specialization it joins."""
    return f"{sid}/{rid.rsplit('/', 1)[1]}" if "/" in rid else rid


def compile_blocks(induced: dict, table: dict, specs: dict, rules: dict, src_traits: dict, voted: dict) -> list:
    """Write the specializations of the accepted table to catalog/esp/ (D-190): importance from the rules over the
    anchors, status «compilado», a new version when the content changes; the runtime blocks they replace and the
    compiled synonyms they absorb are removed. Returns the ids with a new version."""
    changed = []
    for sid, entry in sorted(table.items()):
        block = induced["blocks"].get(sid) or {k: v for k, v in specs.get(sid, {}).items() if not k.startswith("_")}
        if not block:
            continue
        block["anchors"], block["aliases"] = entry["anchors"], entry["aliases"]
        for r in block["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            level, rule = resolve(trait, block["anchors"], rules, r.get("sources", []), r["id"])
            r["trait"], r["importance"], r["rule"] = trait, level or r.get("seed_importance"), rule or NO_RULE
        block["rules"] = [f"esp:{sid}@{n}" for n in block["anchors"]]
        previous = specs.get(sid) if specs.get(sid, {}).get("_where") == "catálogo" else None
        content = lambda b: [b.get("requirements"), b.get("anchors"), b.get("aliases"), b.get("status")]
        block["status"] = COMPILED
        if previous is None or content(previous) != content(block):
            block["version"] = str(int(float((previous or {}).get("version", "0"))) + 1)
            changed.append(sid)
        else:
            block["version"] = previous["version"]
        block["compiled_by"] = f"reglas {rules.get('version')}"
        write_json(ESP_DIR / f"{sid.removeprefix('esp.')}.json", block)
        for i in [sid] + entry["aliases"]:
            (ESP_RUNTIME_DIR / f"{i.removeprefix('esp.')}.json").unlink(missing_ok=True)
            if i != sid:
                (ESP_DIR / f"{i.removeprefix('esp.')}.json").unlink(missing_ok=True)
    return changed


def canonical(rules: dict) -> dict:
    """{alias: id} of the specializations of a rule set, to compare runs assembled before a merge."""
    return {a: sid for sid, e in (rules.get("specializations") or {}).items() for a in e.get("aliases", [])}
