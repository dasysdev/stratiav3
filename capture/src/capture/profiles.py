"""Capture profiles: how a page is read, chosen by whoever asks for the capture.

  reader     the default: the persistent profile with JavaScript, the page scrolled through
             (PAA, the training catalog, the MPIR and any single page that names no profile)
  audit-es   the consumption profile of the informative audit of Contenido and Marcado (D-156,
             D-157, D-220): a real Chrome that runs no JavaScript, a fresh browser context per page
             (no cookies, storage or cache of any site, never a consent given), the first load
             without scrolling; it keeps the original bytes of the response and the headers of
             each redirect, and records Accept-Language, the origin (IP, country, ASN) and what
             robots.txt allows each AI and search bot

Every profile is the same Chrome: its user agent, es-ES and no automation flags (D-042, D-046).
A challenge that needs JavaScript is not passed without it: under audit-es it is an incident
(blocked), not an absence (OQ-80).
"""
from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass

from .files import now


@dataclass(frozen=True)
class Profile:
    name: str
    javascript: bool = True       # False: the page's scripts never run (Emulation)
    fresh_context: bool = False   # a new browser context per page, disposed afterwards
    scroll: bool = True           # a single page is scrolled through; False keeps the first load
    evidence: bool = False        # original bytes, Accept-Language, origin and robots.txt by bot


READER = Profile("reader")
AUDIT_ES = Profile("audit-es", javascript=False, fresh_context=True, scroll=False, evidence=True)
PROFILES = {p.name: p for p in (READER, AUDIT_ES)}
DEFAULT = READER.name


def get(name: str | Profile | None) -> Profile:
    if isinstance(name, Profile):
        return name
    if name is None:
        return READER
    try:
        return PROFILES[name]
    except KeyError:
        raise ValueError(f"perfil de captura desconocido: {name!r} ({', '.join(PROFILES)})") from None


# The bots of D-157 whose robots.txt rules are recorded. Meta's and Amazon's are not yet among
# the sources of references/: these are their documented user-agent tokens.
BOTS = ("GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "PerplexityBot",
        "Googlebot", "Google-Extended", "Bingbot", "Meta-ExternalAgent", "Meta-ExternalFetcher",
        "FacebookBot", "Amazonbot")

RIPESTAT = "https://stat.ripe.net/data/{}/data.json"


def _ripestat(call: str, resource: str = "") -> dict:
    url = RIPESTAT.format(call) + (f"?resource={resource}" if resource else "")
    with urllib.request.urlopen(url, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))["data"]


def origin() -> dict:
    """The public IP this machine goes out with, its country and its ASN (RIPEstat). Recorded,
    never checked: a failure is written down and the capture goes on."""
    try:
        ip = _ripestat("whats-my-ip")["ip"]
        network = _ripestat("network-info", ip)
        asn = network["asns"][0] if network.get("asns") else None
        geo = _ripestat("maxmind-geo-lite", ip)
        countries = sorted({loc.get("country") for res in geo.get("located_resources", [])
                            for loc in res.get("locations", []) if loc.get("country")})
        holder = _ripestat("as-overview", f"AS{asn}").get("holder") if asn else None
        return {"ip": ip, "prefix": network.get("prefix"), "asn": int(asn) if asn else None,
                "as_holder": holder, "country": countries[0] if len(countries) == 1 else countries or None,
                "source": "RIPEstat", "checked_at": now()}
    except (OSError, ValueError, KeyError, IndexError) as exc:
        return {"error": f"{type(exc).__name__}: {exc}", "source": "RIPEstat", "checked_at": now()}
