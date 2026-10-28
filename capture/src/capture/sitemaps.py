"""Discovery of candidate resources in a site's sitemaps (MPIR: «Descubrimiento y clasificación
de recursos»). The sitemaps are fetched and parsed inside the site's window (same browser),
and only the URLs that match come back. Indexes are followed up to a budget.
"""
from __future__ import annotations

import json
import random
import re

from .browser import Page

PARSE = """(async (url, pattern, limit) => {
  let r;
  try { r = await fetch(url, {credentials: 'include'}); } catch (e) { return {error: String(e)}; }
  if (!r.ok) return {status: r.status};
  let buf = await r.arrayBuffer();
  const head = new Uint8Array(buf.slice(0, 2));
  if (head[0] === 0x1f && head[1] === 0x8b) {
    const stream = new Blob([buf]).stream().pipeThrough(new DecompressionStream('gzip'));
    buf = await new Response(stream).arrayBuffer();
  }
  const doc = new DOMParser().parseFromString(new TextDecoder().decode(buf), 'application/xml');
  if (doc.getElementsByTagName('parsererror').length) return {status: r.status, error: 'XML no válido'};
  const loc = el => { const l = el.getElementsByTagNameNS('*', 'loc')[0]; return l ? l.textContent.trim() : ''; };
  const children = [...doc.getElementsByTagNameNS('*', 'sitemap')].map(loc).filter(Boolean);
  if (children.length) return {status: r.status, kind: 'index', sitemaps: children};
  const re = pattern ? new RegExp(pattern) : null;
  const urls = []; let total = 0;
  for (const el of doc.getElementsByTagNameNS('*', 'url')) {
    const u = loc(el); if (!u) continue; total++;
    if ((!re || re.test(u)) && urls.length < limit) {
      const lm = el.getElementsByTagNameNS('*', 'lastmod')[0];
      urls.push({loc: u, lastmod: lm ? lm.textContent.trim() : null});
    }
  }
  return {status: r.status, kind: 'urlset', total, urls};
})(%s, %s, %d)"""


def discover(page: Page, base: str, sitemaps: list[str], match: str | None, follow: str | None,
             limit: int, rng: random.Random, budget: int = 30) -> dict:
    """URLs of the sitemaps that match `match`; child sitemaps are followed if they match
    `follow`. Pauses of a few seconds between fetches."""
    page.navigate(base + "/robots.txt")  # a document of the site's origin to fetch from
    page.wait_ready(timeout=30)
    queue = list(sitemaps) or [base + "/sitemap.xml"]
    seen, urls, report = set(), [], []
    while queue and len(seen) < budget and len(urls) < limit:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        result = page.eval(PARSE % (json.dumps(url), json.dumps(match or ""), limit - len(urls)),
                           timeout=120, await_promise=True) or {}
        report.append({"sitemap": url, "status": result.get("status"), "kind": result.get("kind"),
                       "total": result.get("total"), "error": result.get("error")})
        if result.get("kind") == "index":
            queue.extend(s for s in result["sitemaps"] if not follow or re.search(follow, s))
        elif result.get("kind") == "urlset":
            urls.extend(result["urls"])
        page.idle(rng.uniform(2, 6))
    return {"sitemaps": report, "urls": urls, "pending_sitemaps": queue}
