"""HTTP access of the fetches: retries, inflation of what a server compressed and the SP-API
client of the Amazon sources (credentials in references/.env or the environment)."""
import gzip
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

from . import ROOT
from .store import RefsError

USER_AGENT = "stratia-refs/1.0"
RETRY_CODES = (429, 500, 502, 503, 504)
ENV_FILE = ROOT / ".env"
LWA_URL = "https://api.amazon.com/auth/o2/token"
SPAPI_HOST = "https://sellingpartnerapi-eu.amazon.com"


def request(url: str, data: bytes = None, headers: dict = None, method: str = None, retries: int = 4):
    """Open a URL, retrying on throttling, server errors and network failures."""
    hdrs = {"user-agent": USER_AGENT, **(headers or {})}
    for attempt in range(retries + 1):
        try:
            return urllib.request.urlopen(
                urllib.request.Request(url, data=data, headers=hdrs, method=method), timeout=120)
        except urllib.error.HTTPError as e:
            if e.code not in RETRY_CODES or attempt == retries:
                raise
        except urllib.error.URLError:
            if attempt == retries:
                raise
        time.sleep(2 ** attempt)


def download(url: str, headers: dict = None) -> tuple:
    """(body, response headers, final URL). Some servers compress without being asked."""
    with request(url, headers=headers) as r:
        data, headers, final = r.read(), r.headers, r.geturl()
    encoding = (headers.get("content-encoding") or "identity").lower()
    if encoding == "gzip":
        data = gzip.decompress(data)
    elif encoding != "identity":
        raise RefsError(f"{url}: content-encoding {encoding} no admitido")
    return data, headers, final


def get_bytes(url: str) -> bytes:
    return download(url)[0]


def get_json(url: str):
    return json.loads(get_bytes(url))


def load_env() -> dict:
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip().strip("\"'")
    env.update({k: v for k, v in os.environ.items() if k.startswith("SPAPI_")})
    return env


class SPAPI:
    """Minimal Selling Partner API client (LWA refresh token, EU endpoint)."""

    KEYS = ("SPAPI_LWA_ID", "SPAPI_LWA_SECRET", "SPAPI_REFRESH_TOKEN")

    def __init__(self):
        env = load_env()
        missing = [k for k in self.KEYS if not env.get(k)]
        if missing:
            raise RefsError(f"faltan credenciales SP-API en {ENV_FILE}: {', '.join(missing)}")
        self.env, self.token, self.expires = env, None, 0.0

    def access_token(self) -> str:
        if time.time() > self.expires - 60:
            data = urllib.parse.urlencode({
                "grant_type": "refresh_token",
                "refresh_token": self.env["SPAPI_REFRESH_TOKEN"],
                "client_id": self.env["SPAPI_LWA_ID"],
                "client_secret": self.env["SPAPI_LWA_SECRET"],
            }).encode()
            with request(LWA_URL, data=data) as r:
                body = json.load(r)
            self.token, self.expires = body["access_token"], time.time() + body["expires_in"]
        return self.token

    def call(self, method: str, path: str, body=None, **params):
        url = SPAPI_HOST + path + ("?" + urllib.parse.urlencode(params) if params else "")
        data = json.dumps(body).encode() if body is not None else None
        headers = {"x-amz-access-token": self.access_token(), "content-type": "application/json"}
        with request(url, data=data, headers=headers, method=method) as r:
            return json.load(r)
