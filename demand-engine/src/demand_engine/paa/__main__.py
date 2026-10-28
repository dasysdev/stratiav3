"""PAA engine: People Also Ask questions of google.es. Run inside the container: demand-engine/bin/paa <command>.

Usage:
  paa list                          seed sets and their progress
  paa run SET [--max N] [--ignore-hours]
                                    search the pending seeds, one at a time
  paa status SET                    status of every seed, blocks and totals
  paa questions SET [--json]        consolidated questions (with the seeds that showed them)
  paa unblock                       clear the blocks of the engine after reviewing them
  paa classify prepare SET          input of the agent that classifies the questions (classifier/paa.md)
  paa classify check SET            what is missing or wrong in its output, until «correcto»
  paa classify report SET [--compare CLASSIFIED.json] [--previous CLASSIFIED.json]
                                    classified.json and report.md, optionally against a manual classification
                                    and against an earlier one of the set
  paa classify usage SET TRANSCRIPT tokens of the agent (its output file), in classify/usage.json and the report
  paa control [SET ...]             the classification of each set against its control case (cases/paa; all of
                                    them by default), by content; report in var/paa/control/<date>/
  (classify and control run on the host: standard library only)

Seed sets are demand-engine/paa/<SET>.json; manual: src/demand_engine/paa/README.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from ..capture.files import read_json, write_json
from . import classify, control, store
from .store import STATUS, SeedSet, StoreError, var_root
from .text import norm


def fail(msg: str) -> None:
    sys.exit(f"paa: {msg}")


def shown(path: Path) -> Path:
    try:
        return path.resolve().relative_to(Path.cwd())
    except ValueError:
        return path


def browser():
    """The engine's own Chrome: separate profile and port from the capture engine's."""
    from ..capture.browser import Browser  # websockets: only in the container
    profile = Path(os.environ.get("PAA_PROFILE") or var_root() / "chrome-profile")
    return Browser(profile, port=int(os.environ.get("PAA_CDP_PORT", "9224")))


def counts(seedset: SeedSet) -> dict:
    state = seedset.state()
    out = {s: 0 for s in STATUS}
    for seed in seedset.seeds():
        out[seedset.status_of(seed, state)] += 1
    return out


def cmd_list(args) -> None:
    for set_id in SeedSet.ids():
        s = SeedSet(set_id)
        c = counts(s)
        print(f"{set_id}  {s.definition().get('class', '')}  ·  " +
              ", ".join(f"{k} {v}" for k, v in c.items() if v))


def cmd_run(args) -> None:
    from .run import run
    seedset = SeedSet(args.set)
    b = browser()
    b.start()
    try:
        summary = run(seedset, b, args.max, args.ignore_hours)
    finally:
        b.stop()
    done = ", ".join(f"{k} {v}" for k, v in summary.items() if k != "stopped" and v)
    print(f"{seedset.id}: {done or 'ninguna búsqueda'}" + (f" · {summary['stopped']}" if summary["stopped"] else ""))
    data = read_json(seedset.dir / "questions.json", {})
    print(f"{len(data.get('questions', []))} preguntas únicas en {shown(seedset.dir / 'questions.json')}")


def cmd_status(args) -> None:
    seedset = SeedSet(args.set)
    state = seedset.state()
    for seed in seedset.seeds():
        entry = state["seeds"].get(norm(seed["q"])) or {}
        print(f"  {entry.get('status', 'pending'):<9} {seed.get('group', ''):<10} {seed['q']}  {entry.get('at', '')}")
    reason, blocks = store.blocked_now(), store.engine_state()["blocks"]
    if reason or blocks:
        print(f"bloqueos del motor: {len(blocks)}" + (f" · {reason}" if reason else ""))
    data = read_json(seedset.dir / "questions.json", {})
    print(", ".join(f"{k} {v}" for k, v in counts(seedset).items() if v) +
          f" · {len(data.get('questions', []))} preguntas únicas")


def cmd_questions(args) -> None:
    seedset = SeedSet(args.set)
    data = seedset.consolidate()
    if args.json:
        print(json.dumps(data["questions"], ensure_ascii=False, indent=2))
        return
    for q in data["questions"]:
        print(f"{q['q']}  ·  {len(q['seeds'])}")


def cmd_unblock(args) -> None:
    store.unblock()
    print("bloqueos del motor borrados")


def cmd_classify(args) -> None:
    seedset = SeedSet(args.set)
    if args.step == "prepare":
        out = classify.prepare(seedset)
        spec = read_json(out / "input.json")
        print(f"{seedset.id}: {len(spec['questions'])} preguntas y {len(spec['catalog'])} requisitos en "
              f"{shown(out / 'input.md')}")
    elif args.step == "check":
        problems = classify.check(*classify.load(seedset))
        print("\n".join(problems) if problems else "correcto")
        if problems:
            sys.exit(1)
    elif args.step == "usage":
        if not args.transcript:
            fail("usage necesita la transcripción del agente")
        from ..demand.batch import transcript_usage
        used = {**transcript_usage(Path(args.transcript)), "at": classify.now()}
        write_json(classify.folder(seedset) / "usage.json", used)
        print(f"{seedset.id}: {used['tokens']} tokens en {used['requests']} peticiones")
    else:
        result = classify.finish(seedset, Path(args.compare) if args.compare else None,
                                 Path(args.previous) if args.previous else None)
        verdicts = {}
        for c in result["criteria"]:
            verdicts[c["verdict"]] = verdicts.get(c["verdict"], 0) + 1
        print(f"{seedset.id}: {len(result['questions'])} preguntas · {len(result['criteria'])} criterios (" +
              ", ".join(f"{k} {v}" for k, v in verdicts.items()) + f") · {len(result['candidates'])} candidatos · "
              f"{shown(seedset.dir / 'report.md')}")


def cmd_control(args) -> None:
    out, data = control.run(args.sets or control.case_ids())
    t = data["total"]
    print(f"fuera {t['out_found']}/{t['out_expected']} · " + " · ".join(
        f"{control.NAMES[k].lower()} {t[k]['found']}/{t[k]['expected']} (coinciden {t[k]['agree']}, "
        f"regresiones {t[k]['regressions']}, nuevos {t[k]['new']})" for k in control.SECTIONS))
    print(f"informe: {shown(out / 'report.md')}")


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(prog="paa", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    p = sub.add_parser("run"); p.add_argument("set"); p.add_argument("--max", type=int)
    p.add_argument("--ignore-hours", action="store_true"); p.set_defaults(func=cmd_run)
    p = sub.add_parser("status"); p.add_argument("set"); p.set_defaults(func=cmd_status)
    p = sub.add_parser("questions"); p.add_argument("set"); p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_questions)
    sub.add_parser("unblock").set_defaults(func=cmd_unblock)
    p = sub.add_parser("classify"); p.add_argument("step", choices=("prepare", "check", "report", "usage")); p.add_argument("set")
    p.add_argument("transcript", nargs="?")
    p.add_argument("--compare", help="manual classification ([{q, code}]) for the contrast")
    p.add_argument("--previous", help="an earlier classified.json of the set"); p.set_defaults(func=cmd_classify)
    p = sub.add_parser("control"); p.add_argument("sets", nargs="*"); p.set_defaults(func=cmd_control)
    args = ap.parse_args(argv)
    try:
        args.func(args)
    except StoreError as exc:
        fail(str(exc))


if __name__ == "__main__":
    main()
