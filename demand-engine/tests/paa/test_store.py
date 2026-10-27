"""Seed sets, state, blocks and consolidation (no browser)."""
import json
from datetime import datetime, timedelta, timezone

import pytest

from demand_engine.paa import store
from demand_engine.paa.serp import norm, retry_after, search_url
from demand_engine.paa.store import SeedSet, StoreError, slug


def make_set(paa_dirs, seeds, set_id="s", **extra):
    (paa_dirs / "sets" / f"{set_id}.json").write_text(json.dumps({"class": "C", "seeds": seeds, **extra}), encoding="utf-8")
    return SeedSet(set_id)


def record(query, questions, related=(), outcome="captured"):
    return {"query": query, "outcome": outcome, "elapsed_s": 1.0, "related": list(related),
            "questions": [{"q": q, "position": i + 1, "via": via} for i, (q, via) in enumerate(questions)]}


def test_norm_and_slug():
    assert norm("¿Qué es mejor, el  Satén o el PERCAL?") == "que es mejor, el saten o el percal"
    assert norm("sábana bajera") == norm("sabana bajera")
    assert slug("¿Sábanas de 300 hilos?") == "sabanas-de-300-hilos"
    assert search_url("https://www.google.es", "sábanas coralina", "es", "es") == \
        "https://www.google.es/search?q=s%C3%A1banas+coralina&hl=es&gl=es"


def test_definition_defaults_and_validation(paa_dirs):
    s = make_set(paa_dirs, [{"q": "sábanas"}], clicks=3, pacing={"pause_s": [1, 2]})
    spec = s.definition()
    assert spec["clicks"] == 3 and spec["pacing"]["pause_s"] == [1, 2]
    assert spec["pacing"]["daily_cap"] is None and spec["pacing"]["hours"] is None and spec["market"]["gl"] == "es"
    with pytest.raises(StoreError):
        make_set(paa_dirs, [{"q": "Sábanas"}, {"q": "sabanas"}], set_id="dup").definition()
    with pytest.raises(StoreError):
        SeedSet("no-existe")


def test_resume_and_consolidate(paa_dirs):
    s = make_set(paa_dirs, [{"q": "a", "group": "núcleo"}, {"q": "b", "group": "material"}, {"q": "c"}])
    s.save(s.seeds()[0], record("a", [("¿Uno?", None), ("¿Dos?", "¿Uno?")], ["a 90"]), "<html></html>")
    s.save(s.seeds()[1], record("b", [("¿uno?", None)], ["a 90", "b 150"]), "")
    s.save(s.seeds()[2], {"query": "c", "outcome": "failed", "detail": "x", "elapsed_s": 0}, "")
    assert [x["q"] for x in s.pending()] == ["c"]
    out = s.consolidate()
    assert out["searches"] == 2
    uno = out["questions"][0]
    assert uno["q"] == "¿Uno?" and [x["query"] for x in uno["seeds"]] == ["a", "b"]
    assert out["questions"][1]["seeds"][0]["via"] == "¿Uno?"
    assert [r["text"] for r in out["related"]] == ["a 90", "b 150"]
    folder = s.dir / s.state()["seeds"]["a"]["record"]
    assert (folder / "dom.html.gz").exists() and json.loads((folder / "record.json").read_text())["group"] == "núcleo"
    since = datetime.now().astimezone() - timedelta(minutes=1)
    assert s.searches_since(since) == 3


def test_block_policy(paa_dirs):
    """A block is of the whole engine: Google blocks the IP, not a set."""
    store.block("a", {"vendor": "google"}, hours=6)
    assert "bloqueado hasta" in store.blocked_now()
    assert store.blocked_now(datetime.now().astimezone() + timedelta(hours=7)) is None
    store.block("b", {"vendor": "google"}, hours=6)
    assert "dos bloqueos" in store.blocked_now(datetime.now().astimezone() + timedelta(hours=7))
    assert [b["set"] for b in store.engine_state()["blocks"]] == ["a", "b"]
    store.unblock()
    assert store.blocked_now() is None


def test_retry_after():
    """Retry-After in seconds or as an HTTP date; anything else is no instruction."""
    at = datetime(2026, 10, 27, 14, 50, tzinfo=timezone.utc)
    assert retry_after({"Retry-After": "120"}) == 120
    assert retry_after({"retry-after": "Tue, 27 Oct 2026 14:55:00 GMT"}, at) == 300
    assert retry_after({"Retry-After": "Tue, 27 Oct 2026 14:00:00 GMT"}, at) == 0
    assert retry_after({"Retry-After": "pronto"}) is None and retry_after({}) is None and retry_after(None) is None
