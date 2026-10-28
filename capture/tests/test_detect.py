from capture.detect import challenge, title, vendors_in

NORMAL_CF = """<html><head><title>Sábanas Coralina</title>
<script>(function(){var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js'})()</script>
</head><body><form><iframe src="https://www.google.com/recaptcha/api2/anchor"></iframe></form></body></html>"""


def test_ordinary_pages_are_not_challenges():
    assert challenge(200, {"server": "cloudflare", "cf-ray": "1"}, NORMAL_CF) is None


def test_cloudflare_interstitial():
    html = "<html><head><title>Just a moment...</title></head><body>cf-chl-widget</body></html>"
    assert challenge(403, {}, html)["vendor"] == "cloudflare"
    assert challenge(200, {"cf-mitigated": "challenge"}, "")["vendor"] == "cloudflare"


def test_vendor_specific_pages():
    dd = '<iframe src="https://geo.captcha-delivery.com/captcha/?initialCid=x"></iframe>'
    assert challenge(403, {}, dd)["vendor"] == "datadome"
    px = '<div id="px-captcha"></div>'
    assert challenge(403, {}, px)["vendor"] == "perimeterx"
    ak = "<html><head><title>Access Denied</title></head><body>Reference #18.6a2d1</body></html>"
    assert challenge(403, {}, ak)["vendor"] == "akamai"
    assert challenge(200, {}, "Incapsula incident ID: 123")["vendor"] == "imperva"


def test_plain_blocks():
    assert challenge(429, {}, "")["evidence"] == "HTTP 429"
    assert challenge(403, {"server": "AkamaiGHost"}, "<p>no</p>")["vendor"] == "akamai"
    assert challenge(503, {}, NORMAL_CF)["evidence"] == "HTTP 503"   # error + CAPTCHA widget
    assert challenge(500, {}, "<p>error</p>") is None                 # an error, not a block


def test_vendors_in():
    assert vendors_in({"cf-ray": "x"}, ["_abck", "datadome"], "") == ["akamai", "cloudflare", "datadome"]
    assert vendors_in({}, [], '<script src="https://js.datadome.co/tags.js">') == ["datadome"]
    assert vendors_in({}, ["TS01a2b3c4d5"], "") == ["f5"]


def test_title():
    assert title("<title>\n Funda   nórdica </title>") == "Funda nórdica"
