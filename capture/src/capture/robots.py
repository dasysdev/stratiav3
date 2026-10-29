"""robots.txt as RFC 9309 reads it.

Python's urllib.robotparser is not used: it applies the first matching rule (not the most
specific) and ignores the `*` and `$` wildcards that shops use a lot.

- Groups: consecutive user-agent lines share the rules that follow them. The engine obeys the
  groups of its own token (`stratia-cic`) and, if none names it, the `*` groups (merged).
- Matching: the longest matching pattern wins; on a tie, Allow wins. /robots.txt is always
  allowed. Crawl-delay (not in the RFC) is read from the chosen groups.
- Unavailable (4xx): everything allowed. Unreachable (5xx, 429 or no answer): nothing allowed.
"""
from __future__ import annotations

import re
import urllib.parse
from dataclasses import dataclass, field

TOKEN = "stratia-cic"

# Crawlers of AI services: a Disallow for them is reported to the user, not obeyed by us
AI_AGENTS = (
    "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User", "Claude-SearchBot",
    "Claude-Web", "anthropic-ai", "CCBot", "Google-Extended", "Applebot-Extended",
    "PerplexityBot", "Perplexity-User", "Bytespider", "Meta-ExternalAgent", "FacebookBot",
    "cohere-ai", "Amazonbot", "Diffbot", "MistralAI-User", "DuckAssistBot", "YouBot",
)


@dataclass
class Group:
    agents: list[str] = field(default_factory=list)
    rules: list[tuple[bool, str]] = field(default_factory=list)  # (allow, pattern)
    crawl_delay: float | None = None


def _normalize(path: str) -> str:
    # Percent-encode what is not printable ASCII and uppercase existing escapes
    path = urllib.parse.quote(path, safe="".join(chr(c) for c in range(33, 127)))
    return re.sub(r"%[0-9a-f]{2}", lambda m: m.group(0).upper(), path)


def _pattern(pattern: str) -> re.Pattern:
    anchored = pattern.endswith("$")
    body = _normalize(pattern[:-1] if anchored else pattern)
    regex = "".join(".*" if ch == "*" else re.escape(ch) for ch in body)
    return re.compile(regex + ("$" if anchored else ""))


def matches(pattern: str, path: str) -> bool:
    return _pattern(pattern).match(_normalize(path)) is not None


def parse(text: str) -> tuple[list[Group], list[str]]:
    groups: list[Group] = []
    sitemaps: list[str] = []
    current: Group | None = None
    in_agents = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        key = key.lower()
        if key == "user-agent":
            if not in_agents:
                current = Group()
                groups.append(current)
                in_agents = True
            current.agents.append(value.split("/")[0].split()[0].lower() if value else "")
        elif key in ("allow", "disallow"):
            in_agents = False
            if current is not None and value:
                current.rules.append((key == "allow", value))
        elif key == "crawl-delay":
            in_agents = False
            if current is not None:
                try:
                    current.crawl_delay = float(value)
                except ValueError:
                    pass
        elif key == "sitemap":
            if value:
                sitemaps.append(value)
    return groups, sitemaps


class Robots:
    def __init__(self, text: str | None, status: int | None) -> None:
        self.status = status
        self.groups, self.sitemaps = parse(text or "")
        if status is None or status == 429 or status >= 500:
            self.mode = "unreachable"
        elif 400 <= status < 500:
            self.mode = "unavailable"
        else:
            self.mode = "rules"

    def _chosen(self, token: str) -> list[Group]:
        token = token.lower()
        own = [g for g in self.groups if token in g.agents]
        return own or [g for g in self.groups if "*" in g.agents]

    def allowed(self, url: str, token: str = TOKEN) -> bool:
        return self.decision(url, token)[0]

    def decision(self, url: str, token: str = TOKEN) -> tuple[bool, str | None]:
        """Whether `token` may fetch `url` and the rule that decides it ("Disallow: /x"), or None
        when no rule matches or the file does not apply (unavailable, unreachable)."""
        parts = urllib.parse.urlsplit(url)
        path = (parts.path or "/") + (f"?{parts.query}" if parts.query else "")
        if parts.path == "/robots.txt" or self.mode == "unavailable":
            return True, None
        if self.mode == "unreachable":
            return False, None
        best_len, best = -1, (True, None)
        for group in self._chosen(token):
            for allow, pattern in group.rules:
                if matches(pattern, path):
                    length = len(_normalize(pattern))
                    if length > best_len or (length == best_len and allow):
                        best_len, best = length, (allow, f"{'Allow' if allow else 'Disallow'}: {pattern}")
        return best

    def crawl_delay(self, token: str = TOKEN) -> float | None:
        delays = [g.crawl_delay for g in self._chosen(token) if g.crawl_delay is not None]
        return max(delays) if delays else None

    def blocked_agents(self, agents=AI_AGENTS) -> list[str]:
        """Agents of `agents` that have their own group and may not fetch the root."""
        return [a for a in agents
                if any(a.lower() in g.agents for g in self.groups) and not self.allowed("/", a)]

    def by_bot(self, url: str, bots) -> dict:
        """For each bot: the groups it obeys (its own, `*` or none) and whether it may fetch
        `url` and the root of its site. A fact recorded for the audit, not a rule for us."""
        root = urllib.parse.urlsplit(url)._replace(path="/", query="", fragment="").geturl()
        out = {}
        for bot in bots:
            own = any(bot.lower() in g.agents for g in self.groups)
            group = "own" if own else ("*" if any("*" in g.agents for g in self.groups) else None)
            out[bot] = {"group": group, "url": self.allowed(url, bot), "root": self.allowed(root, bot)}
        return out
