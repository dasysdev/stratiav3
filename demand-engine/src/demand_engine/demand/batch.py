"""Classification of the training catalog in batches with Claude Code agents (T-026, D-054).

The agents are launched from a Claude Code session (skill classify-batch); this module keeps the
batch: which captured pages go in it and in which phase, the state of each case, the tokens each
agent used and the assembly. Phase 1 is one case per type: it generates the blocks that are
missing, so that the agents of phase 2, in parallel, find them in the catalog.

The plan (RUN/batch.json) fixes the cases of the run; usage.jsonl keeps the usage of each agent
(the last record of a case is the one that counts, so a case run again replaces it).
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .catalog import read_json, write_json
from .collect import log_path, read_log
from .model import check, cmd_assemble
from .selection import shown

STATES = ("pendiente", "con problemas", "comprobada", "ensamblada")


def captured_cases(selection: dict, selection_file: Path, pilot_only: bool, only: list) -> list:
    """Captured pages of the selection, in its order (pages first, then the reserves used)."""
    last = {}
    for r in read_log(log_path(selection, selection_file)):
        last[r["id"]] = r["outcome"]
    cases = []
    for c in selection["categories"]:
        if pilot_only and not c["pilot"]:
            continue
        for p in c["pages"] + c["reserves"]:
            if last.get(p["id"]) == "captured" and (not only or p["id"] in only):
                cases.append({"id": p["id"], "url": p["url"], "category": c["category"]})
    return cases


def phased(cases: list) -> list:
    """Phase 1: the first case of each type; phase 2: the rest."""
    seen = set()
    for c in cases:
        c["phase"] = 2 if c["category"] in seen else 1
        seen.add(c["category"])
    return sorted(cases, key=lambda c: c["phase"])


def plan(selection_file: Path, run_dir: Path, pilot_only: bool = False, only: list | None = None) -> dict:
    path = run_dir / "batch.json"
    if path.exists():
        return read_json(path)
    selection = read_json(selection_file)
    cases = phased(captured_cases(selection, selection_file, pilot_only, only or []))
    missing = sorted(set(only or []) - {c["id"] for c in cases})
    if missing:
        raise SystemExit(f"train: sin captura en la selección: {' '.join(missing)}")
    if not cases:
        raise SystemExit("train: ninguna ficha capturada en la selección")
    data = {"selection": shown(selection_file), "created": datetime.now().isoformat(timespec="seconds"),
            "pilot": pilot_only, "cases": cases}
    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(path, data)
    return data


def usage(run_dir: Path) -> dict:
    path = run_dir / "usage.jsonl"
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] \
        if path.exists() else []
    return {r["case"]: r for r in records}


USAGE_FIELDS = ("input", "cache_write", "cache_read", "output")


def transcript_usage(transcript: Path) -> dict:
    """Tokens an agent used, summed over its requests (a request repeats in the transcript, once per block)."""
    requests, tools, times = {}, set(), []
    for line in transcript.read_text(encoding="utf-8").splitlines():
        try:
            entry = json.loads(line)
        except ValueError:
            continue
        if entry.get("timestamp"):
            times.append(datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00")))
        m = entry.get("message")
        if not isinstance(m, dict) or m.get("role") != "assistant":
            continue
        if m.get("usage"):
            requests[m.get("id")] = m["usage"]
        tools |= {c["id"] for c in m.get("content") or [] if isinstance(c, dict) and c.get("type") == "tool_use"}
    if not requests:
        raise SystemExit(f"train: {transcript} no tiene peticiones con consumo")
    keys = dict(zip(USAGE_FIELDS, ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens",
                                   "output_tokens")))
    used = {f: sum(u.get(k) or 0 for u in requests.values()) for f, k in keys.items()}
    return {**used, "tokens": sum(used.values()), "requests": len(requests), "tool_uses": len(tools),
            "duration_ms": int((max(times) - min(times)).total_seconds() * 1000)}


def record_usage(run_dir: Path, case: str, transcript: Path) -> dict:
    cases = {c["id"] for c in read_json(run_dir / "batch.json")["cases"]}
    if case not in cases:
        raise SystemExit(f"train: {case} no está en el lote de {run_dir}")
    record = {"case": case, **transcript_usage(transcript), "at": datetime.now().isoformat(timespec="seconds")}
    with open(run_dir / "usage.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    return record


def state(run_dir: Path, case: str) -> tuple:
    """(state, problems) of a case: no output, output that does not check, checked, or assembled."""
    out, model = run_dir / f"{case}.json", run_dir / f"{case}.model.json"
    if not out.exists():
        return "pendiente", []
    try:
        _, problems = check(out)
    except (ValueError, KeyError, TypeError) as e:
        return "con problemas", [f"salida ilegible: {e}"]
    if problems:
        return "con problemas", problems
    if model.exists() and model.stat().st_mtime >= out.stat().st_mtime:
        return "ensamblada", []
    return "comprobada", []


def status(run_dir: Path) -> dict:
    data = read_json(run_dir / "batch.json")
    used = usage(run_dir)
    rows = []
    for c in data["cases"]:
        st, problems = state(run_dir, c["id"])
        rows.append({**c, "state": st, "problems": problems, "usage": used.get(c["id"])})
    measured = [r["usage"] for r in rows if r["usage"]]
    total = {k: sum(u[k] for u in measured) for k in ("tokens", *USAGE_FIELDS, "requests", "tool_uses", "duration_ms")}
    by_phase = {p: sum(r["usage"]["tokens"] for r in rows if r["usage"] and r["phase"] == p) for p in (1, 2)}
    return {"rows": rows, "measured": len(measured), "total": total, "by_phase": by_phase}


def show(run_dir: Path, out=print) -> None:
    s = status(run_dir)
    for phase in (1, 2):
        rows = [r for r in s["rows"] if r["phase"] == phase]
        if not rows:
            continue
        out(f"Fase {phase} ({'un caso por tipo: genera los bloques que falten' if phase == 1 else 'el resto, en paralelo'})")
        for r in rows:
            u = r["usage"]
            spent = (f" · {u['tokens']:,} tokens ({u['output']:,} de salida), {u['requests']} peticiones, "
                     f"{u['tool_uses']} herramientas, {u['duration_ms'] / 1000:.0f} s") if u else ""
            out(f"  {r['id']} [{r['category']}] {r['state']}{spent}")
            for p in r["problems"][:3]:
                out(f"      {p}")
    counts = {st: sum(r["state"] == st for r in s["rows"]) for st in STATES}
    out("\n" + " · ".join(f"{n} {st}" for st, n in counts.items()))
    if s["measured"]:
        t = s["total"]
        out(f"consumo: {t['tokens']:,} tokens en {s['measured']} casos ({t['tokens'] // s['measured']:,} por caso; "
            f"fase 1: {s['by_phase'][1]:,}, fase 2: {s['by_phase'][2]:,})")
        out(f"  entrada {t['input']:,} · escritura de caché {t['cache_write']:,} · lectura de caché {t['cache_read']:,} · "
            f"salida {t['output']:,}; {t['requests']} peticiones, {t['tool_uses']} herramientas, "
            f"{t['duration_ms'] / 60000:.1f} min de agente")
    pending = [r["id"] for r in s["rows"] if r["state"] in ("pendiente", "con problemas")]
    first = [r for r in s["rows"] if r["phase"] == 1 and r["id"] in pending]
    if first:
        out(f"siguiente: fase 1 — {' '.join(r['id'] for r in first)}")
    elif pending:
        out(f"siguiente: fase 2 — {' '.join(pending)}")
    elif counts["comprobada"]:
        out("siguiente: train batch assemble")


def assemble_all(run_dir: Path, out=print) -> int:
    """Assemble, one after another (they share the queue), the checked cases not yet assembled."""
    n = 0
    for r in status(run_dir)["rows"]:
        if r["state"] == "comprobada":
            cmd_assemble(run_dir / f"{r['id']}.json")
            n += 1
    out(f"{n} modelos ensamblados")
    return n


def main(args: list) -> None:
    from .train import __doc__ as usage_doc
    if args[:1] == ["plan"] and len(args) >= 3:
        rest = args[3:]
        pilot = "--pilot" in rest
        only = rest[rest.index("--only") + 1:] if "--only" in rest else []
        run_dir = Path(args[2])
        plan(Path(args[1]), run_dir, pilot, only)
        show(run_dir)
    elif args[:1] == ["status"] and len(args) == 2:
        show(Path(args[1]))
    elif args[:1] == ["usage"] and len(args) == 4:
        u = record_usage(Path(args[1]), args[2], Path(args[3]))
        print(f"{args[2]}: {u['tokens']:,} tokens ({u['output']:,} de salida), {u['requests']} peticiones")
    elif args[:1] == ["assemble"] and len(args) == 2:
        assemble_all(Path(args[1]))
    else:
        raise SystemExit(usage_doc)
