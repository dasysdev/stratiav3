"""Approximate matching of questions by their significant words (shared by compare and train)."""
import re

STOP = {"de", "del", "la", "el", "los", "las", "y", "o", "en", "con", "uso", "tejido", "distinto", "que", "qué",
        "se", "su", "sus", "un", "una", "es", "al", "por", "para", "cada", "como", "cómo", "si", "tiene", "hay"}


def words(text: str) -> set:
    return {w for w in re.findall(r"\w+", (text or "").lower()) if len(w) > 2 and w not in STOP}


def stem(w: str) -> str:
    return w[:6]


def stems(text: str) -> set:
    return {stem(w) for w in words(text)}


def covers(phrase: str, question: str) -> bool:
    """True if the question shares at least half of the significant words of the phrase."""
    want, have = stems(phrase), stems(question)
    return bool(want) and len(want & have) >= max(1, (len(want) + 1) // 2)


def match_names(expected: list, obtained: list) -> tuple:
    """Pair each expected name with the obtained name that shares most words; returns (pairs, unmatched obtained)."""
    pairs, left = [], list(obtained)
    for e in expected:
        best = max(left, key=lambda o: len(stems(e) & stems(o)), default=None)
        if best is not None and stems(e) & stems(best):
            pairs.append((e, best))
            left.remove(best)
        else:
            pairs.append((e, None))
    return pairs, left
