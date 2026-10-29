"""Text and data mining reservations (art. 67.3 TRLPI, RDL 24/2021; TDMRep).

The TDM exception does not apply when the rightholder has reserved the use by machine-readable
means. The engine reads three of them: /.well-known/tdmrep.json (entries with a `location`
path pattern), the `tdm-reservation` response header and <meta name="tdm-reservation">.
A reservation means that no copy of the content is kept.
"""
from __future__ import annotations

import json
import urllib.parse

from .robots import _normalize, matches


def entries(text: str | None, status: int | None) -> list[dict]:
    if status != 200 or not text:
        return []
    try:
        data = json.loads(text)
    except ValueError:
        return []
    out = []
    for item in data if isinstance(data, list) else []:
        if isinstance(item, dict) and "location" in item:
            out.append({"location": str(item["location"]),
                        "reservation": int(item.get("tdm-reservation", 0) or 0),
                        "policy": item.get("tdm-policy")})
    return out


def reserved_by_entries(items: list[dict], url: str) -> bool:
    """The most specific matching location decides."""
    parts = urllib.parse.urlsplit(url)
    path = (parts.path or "/") + (f"?{parts.query}" if parts.query else "")
    best = (-1, 0)
    for item in items:
        location = item["location"] or "/"
        if matches(location, path) and len(_normalize(location)) > best[0]:
            best = (len(_normalize(location)), item["reservation"])
    return best[1] == 1


def reserving(items: list[dict]) -> list[dict]:
    """The entries of a tdmrep.json that reserve some location. In an audit any of them is a
    reservation of the site (D-171)."""
    return [item for item in items if item["reservation"] == 1]


def signals(headers: dict, meta: dict | None) -> dict:
    """The reservation signals of a response: header and meta tdm-reservation, and tdm-policy."""
    h = {k.lower(): str(v).strip() for k, v in (headers or {}).items()}
    meta = meta or {}
    return {"header": h.get("tdm-reservation"), "meta": meta.get("tdm"),
            "policy": h.get("tdm-policy") or meta.get("tdm_policy")}


def reserved_by_response(headers: dict, meta: dict | None) -> bool:
    found = signals(headers, meta)
    return found["header"] == "1" or str(found["meta"] or "").strip() == "1"
