"""Capture engine shared by the MPIR and the demand model (D-046): pages of reference ecommerce
read with a real Chrome over CDP, after checking legitimacy (robots.txt, TDM reservations),
stopping at any challenge. Batch captures go at a reader's pace (crawl); a single page does
not (once). Usage and principles: README.md in this package.
"""
import os
from pathlib import Path

from .. import ROOT

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
    return Path(os.environ.get("CAPTURE_PROFILE") or ROOT / "var/capture/chrome-profile")
