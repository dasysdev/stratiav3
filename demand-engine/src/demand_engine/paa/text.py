"""Text normalisation shared by the engine and the classification (standard library only: it runs on the host)."""
from __future__ import annotations

import re
import unicodedata


def norm(text: str) -> str:
    """The same normalisation as the page scripts: lower case, no accents, no ¿?¡!, one space."""
    text = "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[¿?¡!]", "", text)).strip()
