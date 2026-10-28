"""The checks of the technical requirements: one per requirement of the reference, by its id.

A check applies the method of its requirement (reference/requirements/) to one case: a page of the
audit (particular view) or the site (general view), and returns its state (D-131): satisfecho, no
satisfecho, NA (with why it does not apply) or NE (with the incident), with the evidence the
requirement asks for. When the method needs a judgement that code cannot make (whether a page is
a soft 404, whether a name is a person's) or the visible content of the page, the check returns
`pendiente` with the question, and an agent decides it over the extracted facts (the skill
/web-audit); the code then validates what the agent wrote.

The registry must cover every requirement of the reference: `missing()` lists the ones without a
check, and the tests fail on them.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

SAT, UNSAT, NA, NE, PENDING = "satisfecho", "no satisfecho", "NA", "NE", "pendiente"
STATES = (SAT, UNSAT, NA, NE)
MAX_EVIDENCE = 25


@dataclass
class Result:
    state: str
    evidence: object = None
    reason: str | None = None   # why NA or NE; for `pendiente`, the question for the agent


@dataclass
class Case:
    """What a check examines: the site and, in the particular view, one page."""
    site: object
    page: object | None
    req: dict
    memo: dict = field(default_factory=dict)

    @property
    def graph(self):
        return self.page.graph if self.page is not None else self.site.graph


REGISTRY: dict[str, Callable[[Case], Result]] = {}


def check(*ids: str):
    def register(fn):
        for i in ids:
            if i in REGISTRY:
                raise ValueError(f"comprobación repetida: {i}")
            REGISTRY[i] = fn
        return fn
    return register


def bind(req_id: str, fn: Callable[[Case], Result]) -> None:
    check(req_id)(fn)


def capped(items: list) -> list:
    items = list(items)
    if len(items) > MAX_EVIDENCE:
        return items[:MAX_EVIDENCE] + [f"… {len(items) - MAX_EVIDENCE} más"]
    return items


def load_all() -> dict:
    from . import consumer, serialization, vocabulary, web  # noqa: F401  (they register)
    return REGISTRY


def missing(requirement_ids) -> list[str]:
    load_all()
    return sorted(set(requirement_ids) - set(REGISTRY))
