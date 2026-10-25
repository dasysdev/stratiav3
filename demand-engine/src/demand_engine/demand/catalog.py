"""Catalog of requirement blocks, Shopify tree, importance and relevance rules (D-038 to D-052).

The importance of a requirement comes from its trait (what the question resolves) and
the class of the product, through rules induced by the training along the Shopify tree:
a rule lives in a class and climbs to the parent only if all the children with data
share it. The critical level is global, the general layer is fixed and the measure
criteria of D-043 always apply (the framework). Without a rule, the agent's vote is
used as provisional. Relevance comes first (D-050): a requirement leaves the model of a
class only if a compiled rule excludes it there; doubt does not exclude.
"""
import json
from collections import Counter
from pathlib import Path

from .. import ROOT
from ..refs import shopify_categories

CATALOG = ROOT / "catalog"
CAT_DIR = CATALOG / "cat"
RUNTIME_DIR = CATALOG / "runtime"
RULES = CATALOG / "rules" / "importance.json"
TRAITS = CATALOG / "traits.json"
EMPTY = CATALOG / "empty.json"
GEN = CATALOG / "gen.json"
QUEUE = ROOT / "var" / "queue.jsonl"

LEVELS = ("complementario", "principal", "crítico")
COMPILED, UNCOMPILED = "compilado", "no compilado"
CRITICAL_TRAITS = ("identidad", "contenido")  # whether they are critical is decided by a global rule
FIXED = {  # framework: D-043, criterion 1
    "medida-que-fija": ("crítico", "marco:D-043.1/medida-que-fija"),
    "medida": ("principal", "marco:D-043.1/medida-descriptiva"),
}
TEXTILE_LAW = "ley:UE-1007/2011"  # framework: D-043, criterion 6
TEXTILE_RULE = ("principal", "marco:D-043.6/composicion-textil")
ESP_ORDER = ("juego", "uso", "material", "función")
NO_RULE = "sin-regla:voto"
NOT_RELEVANT = "no relevante"  # relevance vote (D-050); not an importance level
VOTES = LEVELS + (NOT_RELEVANT,)
DOUBTFUL = "relevancia dudosa"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rank(level) -> int:
    return LEVELS.index(level) if level in LEVELS else -1


def majority(weights: Counter) -> str:
    """Most weighted level; a tie goes to the higher level, because doubt does not lower importance (D-035)."""
    top = max(weights.values())
    return max((level for level, w in weights.items() if abs(w - top) < 1e-9), key=rank)


# Shopify tree: ids encode the path (hg-15-1-4 → hg-15-1 → hg-15 → hg); verticals are the roots.

def parent(node: str):
    return node.rsplit("-", 1)[0] if node and "-" in node else None


def chain(node: str) -> list:
    """Ancestors and the node itself, root first."""
    out = []
    while node:
        out.append(node)
        node = parent(node)
    return out[::-1]


def depth(node: str) -> int:
    return node.count("-")


def under(node: str, ancestor: str) -> bool:
    return node == ancestor or node.startswith(ancestor + "-")


def category_name(node: str) -> str:
    return shopify_categories().get(node, {}).get("name", node)


# Catalog

def load_blocks() -> dict:
    """Category blocks of the catalog (compiled or not) and those generated at runtime, by id."""
    blocks = {}
    for where, folder in (("catálogo", CAT_DIR), ("ejecución", RUNTIME_DIR)):
        for path in sorted(folder.glob("*.json")):
            if path.name.startswith("_"):
                continue
            block = read_json(path)
            block["_path"], block["_where"] = str(path), where
            blocks.setdefault(block["id"], block)
    return blocks


def blocks_by_node(blocks: dict) -> dict:
    return {b["shopify"]: b for b in blocks.values() if b.get("shopify")}


def load_empty() -> dict:
    """Categories known to have no block of their own: {node: 'catálogo' | 'ejecución'}."""
    if not EMPTY.exists():
        return {}
    data = read_json(EMPTY)
    return {n: where for where, nodes in (("catálogo", data.get("catalog", [])), ("ejecución", data.get("runtime", [])))
            for n in nodes}


def load_gen() -> dict:
    return read_json(GEN)


def load_traits() -> dict:
    return read_json(TRAITS)


def load_rules() -> dict:
    if RULES.exists():
        return read_json(RULES)
    return {"version": "0", "global": {}, "tree": {}, "rules": []}


def save_block(block: dict) -> None:
    write_json(Path(block["_path"]), {k: v for k, v in block.items() if not k.startswith("_")})


def requirement_trait(req: dict, source_traits: dict) -> tuple:
    """Trait of a requirement: the one of its sources when they agree, else its own tag (D-045)."""
    found = {source_traits[s] for s in req.get("sources", []) if s in source_traits}
    if len(found) == 1:
        return found.pop(), "fuente"
    return req.get("trait"), "requisito"


def resolve(trait: str, nodes: list, rules: dict, sources=()) -> tuple:
    """Importance of a requirement with this trait in a model whose classes are `nodes`.

    Framework first; then the global critical rule; then, from each class up the tree,
    the most specific rule of the trait (the highest level across classes). Returns
    (level, rule id), or (None, None) if no rule applies.
    """
    if any(s.startswith(TEXTILE_LAW) for s in sources):
        return TEXTILE_RULE
    if trait in FIXED:
        return FIXED[trait]
    if trait in CRITICAL_TRAITS and rules.get("global", {}).get(trait) == "crítico":
        return "crítico", f"imp:{trait}@*"
    best = (None, None)
    for node in nodes:
        n = node
        while n:
            level = rules.get("tree", {}).get(f"{trait}@{n}")
            if level:
                if rank(level) > rank(best[0]):
                    best = (level, f"imp:{trait}@{n}")
                break
            n = parent(n)
    return best


def protected(trait, origin, sources=()) -> bool:
    """Framework: the measure that fixes what is sold and normative requirements are never excluded (D-050)."""
    return trait == "medida-que-fija" or origin == "normativa" or any(s.startswith("ley:") for s in sources)


def relevance(req_id: str, nodes: list, rules: dict) -> tuple:
    """(excluded, rule id): excluded only if, from every class of the model it applies to, the most
    specific relevance rule of the requirement excludes it. Without a rule it stays (D-050)."""
    found = []
    for node in nodes:
        n, hit = node, None
        while n:
            value = rules.get("relevance", {}).get(f"{req_id}@{n}")
            if value:
                hit = (value == "excluido", f"rel:{req_id}@{n}")
                break
            n = parent(n)
        found.append(hit or (False, None))
    if found and all(excluded for excluded, _ in found):
        return True, found[0][1]
    return False, None


def class_nodes_for(block_node, classes: list) -> list:
    """Classes of the model to which a block applies: those under the block's category (all, for esp. and inferred)."""
    if not block_node:
        return list(classes)
    return [c for c in classes if under(c, block_node)] or [block_node]
