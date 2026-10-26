"""Classification in batches with agents (T-026): phases, usage and the guard against duplicated blocks."""
import json

import pytest

from demand_engine.demand import batch, catalog, model


def selection():
    def pages(prefix, n):
        return [{"id": f"t-{prefix}{i}", "url": f"https://t/{prefix}{i}"} for i in range(n)]
    return {"store": "t", "categories": [
        {"category": "hogar/sarten", "pilot": True, "pages": pages("s", 3), "reserves": pages("r", 1)},
        {"category": "moda/vestido", "pilot": False, "pages": pages("v", 2), "reserves": []}]}


@pytest.fixture
def selection_file(tmp_path, monkeypatch):
    path = tmp_path / "t-2026-10-25.json"
    path.write_text(json.dumps(selection()), encoding="utf-8")
    log = tmp_path / "capture.jsonl"
    outcomes = {"t-s0": "captured", "t-s1": "gone", "t-s2": "captured", "t-r0": "captured", "t-v0": "captured",
                "t-v1": "blocked"}
    log.write_text("".join(json.dumps({"id": i, "outcome": o}) + "\n" for i, o in outcomes.items()), encoding="utf-8")
    monkeypatch.setattr(batch, "log_path", lambda sel, f: log)
    return path


def test_phase_one_is_one_captured_case_per_type(selection_file, tmp_path):
    data = batch.plan(selection_file, tmp_path / "run")
    assert [(c["id"], c["phase"]) for c in data["cases"]] == [
        ("t-s0", 1), ("t-v0", 1), ("t-s2", 2), ("t-r0", 2)]  # gone and blocked pages are left out
    pilot = batch.plan(selection_file, tmp_path / "pilot", pilot_only=True)
    assert [c["id"] for c in pilot["cases"]] == ["t-s0", "t-s2", "t-r0"]


def test_plan_is_fixed_once_written(selection_file, tmp_path):
    batch.plan(selection_file, tmp_path / "run", only=["t-s2", "t-v0"])
    again = batch.plan(selection_file, tmp_path / "run")
    assert [(c["id"], c["phase"]) for c in again["cases"]] == [("t-s2", 1), ("t-v0", 1)]
    with pytest.raises(SystemExit):
        batch.plan(selection_file, tmp_path / "other", only=["t-v1"])  # not captured


def transcript(tmp_path, name, requests):
    """An agent transcript: each request repeats once per content block, with the same usage."""
    lines, t = [], 0
    for rid, (inp, write, read, out) in requests.items():
        usage = {"input_tokens": inp, "cache_creation_input_tokens": write, "cache_read_input_tokens": read,
                 "output_tokens": out}
        for block in ({"type": "text", "text": "…"}, {"type": "tool_use", "id": f"tu-{rid}", "name": "Bash"}):
            t += 1
            lines.append({"timestamp": f"2026-10-25T22:00:{t:02d}.000Z",
                          "message": {"id": rid, "role": "assistant", "usage": usage, "content": [block]}})
    lines.append({"timestamp": f"2026-10-25T22:00:{t + 10:02d}.000Z", "message": {"role": "user", "content": "ok"}})
    path = tmp_path / f"{name}.jsonl"
    path.write_text("".join(json.dumps(x) + "\n" for x in lines) + "no es json\n", encoding="utf-8")
    return path


def test_usage_is_summed_over_the_requests_of_the_transcript(selection_file, tmp_path):
    run = tmp_path / "run"
    batch.plan(selection_file, run)
    first = transcript(tmp_path, "a", {"m1": (5, 100, 0, 10), "m2": (1, 20, 100, 30)})
    assert batch.transcript_usage(first) == {"input": 6, "cache_write": 120, "cache_read": 100, "output": 40,
                                             "tokens": 266, "requests": 2, "tool_uses": 2, "duration_ms": 13000}
    batch.record_usage(run, "t-s0", transcript(tmp_path, "b", {"m1": (1, 1, 1, 1)}))
    batch.record_usage(run, "t-s0", first)  # run again: the last record counts
    batch.record_usage(run, "t-s2", transcript(tmp_path, "c", {"m1": (0, 0, 0, 34)}))
    with pytest.raises(SystemExit):
        batch.record_usage(run, "t-x", first)
    s = batch.status(run)
    assert (s["total"]["tokens"], s["total"]["output"], s["total"]["requests"]) == (300, 74, 3)
    assert s["by_phase"] == {1: 266, 2: 34}
    assert {r["id"]: r["state"] for r in s["rows"]} == {"t-s0": "pendiente", "t-v0": "pendiente",
                                                         "t-s2": "pendiente", "t-r0": "pendiente"}


@pytest.fixture
def runtime(tmp_path, monkeypatch):
    for name in ("CAT_DIR", "RUNTIME_DIR", "EMPTY"):
        target = tmp_path / name.lower()
        if name != "EMPTY":
            target.mkdir()
        monkeypatch.setattr(catalog, name, target)
        monkeypatch.setattr(model, name, target)
    monkeypatch.setattr(model, "ROOT", tmp_path)
    return tmp_path


def block(tmp_path, bid, node="hg-1"):
    path = tmp_path / f"{bid}.json"
    path.write_text(json.dumps({"id": bid, "shopify": node, "requirements": [
        {"question": "¿De qué material es?", "trait": "material", "vote": "principal"}]}), encoding="utf-8")
    return str(path)


def test_a_runtime_block_is_not_registered_twice(runtime):
    model.cmd_register([block(runtime, "cat.sarten")])
    assert (runtime / "runtime_dir" / "sarten.json").exists()
    with pytest.raises(SystemExit, match="otro caso del lote"):
        model.cmd_register([block(runtime, "cat.sarten")])
    with pytest.raises(SystemExit, match="ya tiene el bloque cat.sarten"):
        model.cmd_register([block(runtime, "cat.sartenes")])
    model.cmd_register([block(runtime, "cat.sarten"), "--replace"])  # correcting your own block
    with pytest.raises(SystemExit, match="ya tiene el bloque"):
        model.cmd_register(["--empty", "hg-1"])
    model.cmd_register(["--empty", "hg-2"])
    with pytest.raises(SystemExit, match="sin requisitos propios"):
        model.cmd_register([block(runtime, "cat.olla", "hg-2")])
