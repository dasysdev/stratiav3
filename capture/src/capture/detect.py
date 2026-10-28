"""Challenge pages and anti-bot vendors.

A challenge is recognised only by markers specific to block or challenge pages: the scripts
that vendors inject into ordinary pages (Cloudflare's /cdn-cgi/challenge-platform/, DataDome's
tags.js, a reCAPTCHA in a newsletter form) are not challenges. A plain 403 or 429 is a block.
"""
from __future__ import annotations

import re

TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)

# (vendor, regex over the HTML) — markers of challenge or block pages only
CHALLENGE_MARKERS = (
    ("cloudflare", re.compile(r"<title[^>]*>\s*(Just a moment|Un momento|Attention Required!? \| Cloudflare)", re.I)),
    ("cloudflare", re.compile(r"cf-chl-(widget|bypass|opt)|window\._cf_chl_opt", re.I)),
    ("datadome", re.compile(r"(geo|interstitial)\.captcha-delivery\.com|captcha-delivery\.com/(captcha|interstitial)", re.I)),
    ("perimeterx", re.compile(r"id=[\"']px-captcha|_pxCaptcha|Press &amp; Hold|Press & Hold", re.I)),
    ("imperva", re.compile(r"Incapsula incident ID|_Incapsula_Resource\?SWUDNSAI", re.I)),
    ("akamai", re.compile(r"<title[^>]*>\s*Access Denied\s*</title>[\s\S]*Reference\s*(&#32;)?(#|&#35;)", re.I)),
)
# Generic CAPTCHA widgets: a challenge only when the response is an error
CAPTCHA = re.compile(r"<iframe[^>]+(recaptcha|hcaptcha|challenges\.cloudflare\.com)", re.I)

# Vendor fingerprints in headers, cookies and script URLs of ordinary pages
HEADER_VENDORS = (
    ("cloudflare", "cf-ray", None), ("cloudflare", "server", "cloudflare"),
    ("akamai", "server", "akamaighost"), ("akamai", "akamai-grn", None),
    ("datadome", "x-datadome", None), ("datadome", "x-dd-b", None),
    ("imperva", "x-iinfo", None), ("imperva", "x-cdn", "incapsula"),
    ("kasada", "x-kpsdk-ct", None),
)
COOKIE_VENDORS = (
    ("cloudflare", re.compile(r"^(__cf_bm|cf_clearance|__cflb)$")),
    ("akamai", re.compile(r"^(_abck|bm_sz|ak_bmsc|bm_sv|bm_mi)$")),
    ("datadome", re.compile(r"^datadome$")),
    ("perimeterx", re.compile(r"^_px(2|3|hd|vid|de)?$")),
    ("imperva", re.compile(r"^(incap_ses_|visid_incap_|nlbi_)")),
    ("f5", re.compile(r"^TS01[0-9a-f]{6,}$")),
    ("aws-waf", re.compile(r"^aws-waf-token$")),
)
SCRIPT_VENDORS = (
    ("cloudflare", re.compile(r"/cdn-cgi/challenge-platform/")),
    ("datadome", re.compile(r"js\.datadome\.co")),
    ("perimeterx", re.compile(r"client\.(perimeterx\.net|px-cloud\.net)|/px/client/main\.min\.js")),
    ("akamai", re.compile(r"/akam/\d+/")),
)


def title(html: str) -> str:
    m = TITLE.search(html[:100_000])
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def challenge(status: int | None, headers: dict, html: str) -> dict | None:
    """{'vendor', 'evidence'} if the response is a challenge or a block, else None."""
    h = {k.lower(): str(v).lower() for k, v in (headers or {}).items()}
    head = html[:300_000]
    if h.get("cf-mitigated") == "challenge":
        return {"vendor": "cloudflare", "evidence": "cabecera cf-mitigated: challenge"}
    for vendor, marker in CHALLENGE_MARKERS:
        m = marker.search(head)
        if m:
            return {"vendor": vendor, "evidence": f"HTTP {status}; marca «{m.group(0)[:80]}»"}
    if status in (403, 429) or (status and status >= 400 and CAPTCHA.search(head)):
        vendors = vendors_in(headers, [], head)
        return {"vendor": vendors[0] if vendors else "desconocido", "evidence": f"HTTP {status}"}
    return None


def vendors_in(headers: dict, cookie_names: list[str], html: str) -> list[str]:
    """Anti-bot vendors whose fingerprints appear in an ordinary response."""
    h = {k.lower(): str(v).lower() for k, v in (headers or {}).items()}
    found = []
    for vendor, name, value in HEADER_VENDORS:
        if name in h and (value is None or value in h[name]):
            found.append(vendor)
    for vendor, pattern in COOKIE_VENDORS:
        if any(pattern.search(c) for c in cookie_names):
            found.append(vendor)
    for vendor, pattern in SCRIPT_VENDORS:
        if pattern.search(html[:500_000]):
            found.append(vendor)
    return sorted(set(found))
