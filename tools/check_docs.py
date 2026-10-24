#!/usr/bin/env python3
"""Validate the integrity of the documentation under docs/.

Checks:
  - frontmatter present with required keys and valid enum values
  - unique `id` across docs/
  - `sources` keys belong to the v0 source keys; `INTAKE <stem>` exists in docs/archive/intake/
  - relative markdown links resolve (file and GitHub-style heading anchor)
  - property IDs referenced are within P06–P18
  - glossary terms are not duplicated

Usage: python3 tools/check_docs.py [--quiet]
Exit code 1 if any error is found.
"""

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ARCHIVE = DOCS / "archive"
INTAKE = DOCS / "intake"                 # raw update artifacts, not canon: not checked
INTAKE_ARCHIVE = ARCHIVE / "intake"      # processed artifacts, cited as `INTAKE <stem>`
EXEMPT = {DOCS / "CLAUDE.md"}
EXTRA_LINKED = [ROOT / "CLAUDE.md"]  # checked for links, not frontmatter

REQUIRED = ["id", "title", "layer", "status", "version", "updated", "sources"]
LAYERS = {"context", "model", "method", "governance", "meta"}
STATUSES = {"vigente", "propuesta", "pendiente", "historico"}
SOURCE_KEYS = {"CTX", "BASE", "FUND", "TAX", "MPIR", "GSC0", "INTAKE"}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
CODE_FENCE_RE = re.compile(r"^\s*(```|~~~)")
PROP_RE = re.compile(r"\bP(\d{2})\b")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans (links inside them are not links)."""
    out, in_fence = [], False
    for line in text.splitlines():
        if CODE_FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else re.sub(r"`[^`]*`", "", line))
    return "\n".join(out)


def slugify(heading: str) -> str:
    """Approximate GitHub's heading anchor algorithm."""
    text = re.sub(r"`([^`]*)`", r"\1", heading)          # inline code keeps its text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links keep their label
    text = re.sub(r"<[^>]+>", "", text)                   # html tags
    text = text.strip().lower()
    text = "".join(ch for ch in text if ch == "-" or ch == " " or ch == "_"
                   or unicodedata.category(ch)[0] in ("L", "N", "M"))
    return text.replace(" ", "-")


def anchors_of(path: Path, cache: dict) -> set:
    if path not in cache:
        seen, result, in_fence = {}, set(), False
        for line in path.read_text(encoding="utf-8").splitlines():
            if CODE_FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            m = None if in_fence else HEADING_RE.match(line)
            if m:
                slug = slugify(m.group(2))
                n = seen.get(slug, 0)
                result.add(slug if n == 0 else f"{slug}-{n}")
                seen[slug] = n + 1
        cache[path] = result
    return cache[path]


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.split(" #")[0].strip()
    return fm


def main() -> int:
    quiet = "--quiet" in sys.argv
    errors, warnings = [], []
    ids, anchor_cache = {}, {}

    files = sorted(p for p in DOCS.rglob("*.md")
                   if ARCHIVE not in p.parents and INTAKE not in p.parents)

    for path in files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")

        if path not in EXEMPT:
            fm = parse_frontmatter(text)
            if fm is None:
                errors.append(f"{rel}: missing frontmatter")
            else:
                for key in REQUIRED:
                    if key not in fm:
                        errors.append(f"{rel}: frontmatter missing '{key}'")
                if fm.get("layer") and fm["layer"] not in LAYERS:
                    errors.append(f"{rel}: invalid layer '{fm['layer']}'")
                if fm.get("status") and fm["status"] not in STATUSES:
                    errors.append(f"{rel}: invalid status '{fm['status']}'")
                if fm.get("id"):
                    if fm["id"] in ids:
                        errors.append(f"{rel}: duplicate id '{fm['id']}' (also {ids[fm['id']]})")
                    ids[fm["id"]] = rel
                src = fm.get("sources", "").strip("[] ")
                for item in filter(None, (s.strip() for s in src.split(","))):
                    key = item.split()[0]
                    if key not in SOURCE_KEYS:
                        errors.append(f"{rel}: unknown source key '{key}' in '{item}'")
                    elif key == "INTAKE":
                        stem = item[len("INTAKE"):].strip().split()[0] if item.strip() != "INTAKE" else ""
                        if not stem or not list(INTAKE_ARCHIVE.glob(f"{stem}.*")):
                            errors.append(f"{rel}: source '{item}' not found in docs/archive/intake/")

        # governance records may discuss retired IDs (e.g. I-05 on P01–P05)
        props = [] if "30-governance" in path.parts else PROP_RE.findall(strip_code(text))
        for num in props:
            if not 6 <= int(num) <= 18:
                warnings.append(f"{rel}: property P{num} outside P06–P18")

    for path in files + [p for p in EXTRA_LINKED if p.exists()]:
        rel = path.relative_to(ROOT)
        for target in LINK_RE.findall(strip_code(path.read_text(encoding="utf-8"))):
            if re.match(r"^[a-z]+:", target):  # http:, mailto:, ...
                continue
            file_part, _, anchor = target.partition("#")
            dest = path if not file_part else (path.parent / file_part).resolve()
            if not dest.exists():
                errors.append(f"{rel}: broken link '{target}'")
                continue
            if anchor and dest.suffix == ".md" and anchor.lower() not in anchors_of(dest, anchor_cache):
                errors.append(f"{rel}: broken anchor '{target}'")

    glossary = DOCS / "glossary.md"
    if glossary.exists():
        terms = {}
        for line in glossary.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*\*\*(.+?)\*\*", line)
            if m:
                term = m.group(1).strip().lower()
                if term in terms:
                    errors.append(f"docs/glossary.md: duplicate term '{m.group(1)}'")
                terms[term] = True

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if not quiet or errors:
        print(f"\n{len(files)} files checked · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
