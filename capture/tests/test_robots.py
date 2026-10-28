from capture.robots import Robots

ROBOTS = """
# comentario
User-agent: *
Disallow: /checkout
Allow: /checkout/ayuda
Disallow: /*?filter=
Disallow: /*.pdf$
Crawl-delay: 5

User-agent: GPTBot
User-agent: CCBot
Disallow: /

Sitemap: https://x.es/sitemap.xml
"""

B = "https://x.es"


def test_longest_match_wins():
    r = Robots(ROBOTS, 200)
    assert not r.allowed(B + "/checkout/pago")
    assert r.allowed(B + "/checkout/ayuda/envios")
    assert r.allowed(B + "/sabanas")


def test_wildcards_and_end_anchor():
    r = Robots(ROBOTS, 200)
    assert not r.allowed(B + "/sabanas?filter=azul")
    assert r.allowed(B + "/sabanas?page=2")
    assert not r.allowed(B + "/ficha.pdf")
    assert r.allowed(B + "/ficha.pdf?v=1")


def test_allow_wins_a_tie():
    assert Robots("User-agent: *\nDisallow: /a\nAllow: /a\n", 200).allowed(B + "/a")


def test_own_token_group_replaces_star():
    text = "User-agent: *\nDisallow: /\n\nUser-agent: stratia-cic\nDisallow: /privado\n"
    r = Robots(text, 200)
    assert r.allowed(B + "/sabanas")
    assert not r.allowed(B + "/privado/x")


def test_star_groups_are_merged():
    r = Robots("User-agent: *\nDisallow: /a\n\nUser-agent: *\nDisallow: /b\n", 200)
    assert not r.allowed(B + "/a") and not r.allowed(B + "/b")


def test_crawl_delay_sitemaps_and_ai_agents():
    r = Robots(ROBOTS, 200)
    assert r.crawl_delay() == 5
    assert r.sitemaps == ["https://x.es/sitemap.xml"]
    assert r.blocked_agents() == ["GPTBot", "CCBot"]


def test_status_modes():
    assert Robots(None, 404).allowed(B + "/checkout")          # unavailable: all allowed
    assert not Robots("User-agent: *\n", 503).allowed(B + "/")  # unreachable: nothing
    assert not Robots(None, None).allowed(B + "/")
    assert not Robots(None, 429).allowed(B + "/")


def test_robots_txt_always_allowed():
    assert Robots("User-agent: *\nDisallow: /\n", 200).allowed(B + "/robots.txt")


def test_case_comments_empty_rules_and_non_ascii():
    r = Robots("USER-AGENT: *  # todos\nDISALLOW: /x\nDisallow:\nDisallow: /sábanas\n", 200)
    assert not r.allowed(B + "/x/1")
    assert r.allowed(B + "/y")
    assert not r.allowed(B + "/s%C3%A1banas/coralina")


def test_user_agent_version_is_ignored():
    r = Robots("User-agent: stratia-cic/1.0\nDisallow: /a\n", 200)
    assert not r.allowed(B + "/a")
