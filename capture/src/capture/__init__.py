"""capture: the capture engine (D-046) and the store of frozen pages shared by every system
(D-150). Pages of ecommerce read with a real Chrome over CDP, after checking legitimacy
(robots.txt, TDM reservations), stopping at any challenge. Batch captures go at a reader's pace
(crawl); a single page does not (once). The store (pages) keeps the frozen pages that every
system evaluates. Usage and principles: capture/README.md.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # capture/

# Outcome of a visit → label for reports
OUTCOMES = {
    "captured": "capturada",
    "blocked": "bloqueada (desafío o 403/429)",
    "failed": "no recuperada (error)",
    "gone": "no existe (404/410)",
    "disallowed": "excluida por robots.txt",
    "reserved": "reserva TDM: no se conserva",
}


def profile() -> Path:
    """The one Chrome profile of the container (CAPTURE_PROFILE overrides it, in tests)."""
    return Path(os.environ.get("CAPTURE_PROFILE") or ROOT / "var/chrome-profile")
