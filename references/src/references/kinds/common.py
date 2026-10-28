"""What the kinds share: the dated version of an extraction and the printing of a diff."""
from ..store import RefsError, refs_dir, today, versions


def dated_version(source: str) -> str:
    version = today()
    if version in versions(source):
        raise RefsError(f"{source}: ya hay una extracción de hoy ({version})")
    return version


def show(label: str, lines: list, limit: int) -> None:
    if not lines:
        return
    print(f"  {label} ({len(lines)}):")
    for line in lines[:limit]:
        print(f"    {line}")
    if len(lines) > limit:
        print(f"    … +{len(lines) - limit} más (--all)")


def diff_nodes(nodes, sid: str, old: str, new: str, limit: int) -> None:
    """Added, removed, renamed and moved nodes. `nodes(folder)` gives [(title, {id: (name,
    parents)}, label of a change of name)]."""
    before_groups, after_groups = nodes(refs_dir() / sid / old), nodes(refs_dir() / sid / new)
    for (title, before, label), (_, after, _) in zip(before_groups, after_groups):
        common = before.keys() & after.keys()
        added = sorted(after.keys() - before.keys())
        removed = sorted(before.keys() - after.keys())
        changed = sorted(k for k in common if before[k][0] != after[k][0])
        moved = sorted(k for k in common if before[k][1] != after[k][1])
        print(f"{title}: {len(before)} → {len(after)} · +{len(added)} −{len(removed)} · "
              f"{label} {len(changed)} · movidos {len(moved)}")
        show("añadidos", [f"{k}  {after[k][0]}" for k in added], limit)
        show("eliminados", [f"{k}  {before[k][0]}" for k in removed], limit)
        show(label, [f"{k}  {before[k][0]} → {after[k][0]}" for k in changed], limit)
        show("movidos", [f"{k}  {after[k][0]}: {','.join(before[k][1]) or '—'} → {','.join(after[k][1]) or '—'}"
                         for k in moved], limit)
