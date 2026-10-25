"""External reference material for the product taxonomy, frozen by version under demand-engine/var/refs/.

Each source keeps immutable versions in refs/<source>/<version>/: the files as
published plus a MANIFEST.json (origin, size, sha256, fetch date). A new version
never overwrites an existing one, and a fetch whose content equals the latest
version is discarded. The version the project works with is pinned in
refs/pins.json; only `refs pin` changes it, because a new pin obliges a review of
the mappings built on the previous one. The first version of a source is pinned
automatically. Everything here is disposable (var/): what matters is recorded where it
is used, in the training results and in each demand model (the versions they used).

Sources:
  shopify      Shopify Standard Product Taxonomy, Spanish release assets (GitHub)
  shopify-google  Shopify's official mapping to the Google taxonomy, same release (English only)
  google       Google Product Taxonomy es-ES with IDs
  amazon-btg   Amazon.es browse tree (SP-API report GET_XML_BROWSE_TREE_DATA)
  amazon-ptd   Amazon.es Product Type Definitions es_ES: index, definitions, schemas

Usage:
  refs [status]                      versions per source and the pinned one
  refs check [SOURCE...]             is there something newer upstream? (stores nothing)
  refs fetch [SOURCE...] [--version TAG]
  refs diff SOURCE [OLD [NEW]] [--all]
                                     added, removed, renamed and moved nodes
                                     (default: pinned → latest)
  refs pin SOURCE VERSION            set the version the project works with

SP-API credentials come from .env: SPAPI_LWA_ID, SPAPI_LWA_SECRET, SPAPI_REFRESH_TOKEN.
REFS_DIR overrides the refs directory (tests).

The module is also the read access to the pinned versions (section «Reading»), shared
by taxo, blocks and the demand engine.
"""
import argparse
import base64
import functools
import gzip
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path

from . import ROOT

REFS = Path(os.environ.get("REFS_DIR") or ROOT / "var/refs")
PINS = REFS / "pins.json"
ENV_FILE = ROOT / ".env"

USER_AGENT = "stratia-refs/1.0"
SHOPIFY_API = "https://api.github.com/repos/Shopify/product-taxonomy/releases"
SHOPIFY_ASSET_RE = re.compile(r"\.es\.(json|txt)\.gz$")   # Spanish release assets only
SHOPIFY_GOOGLE_RE = re.compile(r"^integrations\.google\.shopify_.+\.en\.json\.gz$")
GOOGLE_URL = "https://www.google.com/basepages/producttype/taxonomy-with-ids.es-ES.txt"
GOOGLE_FILE = "taxonomy-with-ids.es-ES.txt"
GOOGLE_VERSION_RE = re.compile(rb"^# Google_Product_Taxonomy_Version: (\S+)")
LWA_URL = "https://api.amazon.com/auth/o2/token"
SPAPI_HOST = "https://sellingpartnerapi-eu.amazon.com"
MARKETPLACE_ES = "A1RKKUPIHCS9HS"
PTD_LOCALE = "es_ES"
PTD_INTERVAL = 0.25     # seconds between getDefinitionsProductType calls (rate 5/s)
REPORT_POLL = 15        # seconds between report status polls
REPORT_TIMEOUT = 1800
BTG_FILE = "browse_tree.es.xml.gz"
DIFF_LIMIT = 30         # lines per section unless --all
RETRY_CODES = (429, 500, 502, 503, 504)


def fail(msg: str) -> None:
    print(f"refs: {msg}", file=sys.stderr)
    sys.exit(1)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dumps(obj) -> bytes:
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True).encode("utf-8")


def today() -> str:
    return date.today().isoformat()


# --- HTTP -------------------------------------------------------------------

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


def get_bytes(url: str, headers: dict = None) -> bytes:
    with request(url, headers=headers) as r:
        return r.read()


def get_json(url: str, headers: dict = None):
    return json.loads(get_bytes(url, headers))


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
            fail(f"faltan credenciales SP-API en .env: {', '.join(missing)}")
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


# --- Snapshots ----------------------------------------------------------------

def versions(source: str) -> list:
    folder = REFS / source
    if not folder.exists():
        return []
    return sorted(p.name for p in folder.iterdir() if (p / "MANIFEST.json").exists())


def manifest(source: str, version: str) -> dict:
    return json.loads((REFS / source / version / "MANIFEST.json").read_text(encoding="utf-8"))


def latest_manifest(source: str):
    found = versions(source)
    return manifest(source, found[-1]) if found else None


def pins() -> dict:
    return json.loads(PINS.read_text(encoding="utf-8")) if PINS.exists() else {}


def save_pins(data: dict) -> None:
    PINS.parent.mkdir(parents=True, exist_ok=True)
    PINS.write_bytes(dumps(data) + b"\n")


def fingerprint(files: list) -> list:
    """What counts as content: the inflated bytes of a .gz, else the bytes."""
    return sorted((f["path"], f.get("content_sha256") or f["sha256"]) for f in files)


class Snapshot:
    """A version being written: files land in a partial folder renamed on commit."""

    def __init__(self, source: str, version: str, origin: dict):
        if version in versions(source):
            fail(f"{source} {version} ya existe; las versiones no se sobrescriben")
        self.source, self.version, self.origin = source, version, origin
        self.final = REFS / source / version
        self.tmp = REFS / source / f".partial-{version}"
        shutil.rmtree(self.tmp, ignore_errors=True)
        self.tmp.mkdir(parents=True)
        self.files, self.errors = [], []

    def add(self, path: str, data: bytes, origin: str, **extra) -> dict:
        target = self.tmp / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        entry = {"path": path, "origin": origin, "size": len(data), "sha256": sha256(data)}
        if path.endswith(".gz"):
            entry["content_sha256"] = sha256(gzip.decompress(data))
        entry.update(extra)
        self.files.append(entry)
        return entry

    def commit(self) -> None:
        previous = latest_manifest(self.source)
        if previous and fingerprint(previous["files"]) == fingerprint(self.files) \
                and previous.get("errors", []) == sorted(self.errors):
            shutil.rmtree(self.tmp)
            print(f"{self.source}: sin cambios respecto a {previous['version']}; no se crea versión")
            return
        data = {
            "source": self.source,
            "version": self.version,
            "fetched_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "origin": self.origin,
            "files": sorted(self.files, key=lambda f: f["path"]),
        }
        if self.errors:
            data["errors"] = sorted(self.errors)   # compared on the next fetch, like the files
        (self.tmp / "MANIFEST.json").write_bytes(dumps(data) + b"\n")
        self.tmp.rename(self.final)
        size = sum(f["size"] for f in self.files) / 1e6
        print(f"{self.source}: {self.version} descargada ({len(self.files)} ficheros, {size:.1f} MB)")
        for error in self.errors:
            print(f"  error: {error}")
        current = pins()
        if self.source not in current:
            current[self.source] = self.version
            save_pins(current)
            print(f"{self.source}: fijada {self.version} (primera versión)")

    def discard(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)


# --- Reading ------------------------------------------------------------------

class RefsError(LookupError):
    pass


def pinned(source: str) -> Path:
    """Folder of the version of `source` the project works with."""
    current = pins()
    if source not in current:
        raise RefsError(f"{source} no está fijada; ejecuta demand-engine/bin/refs status")
    folder = REFS / source / current[source]
    if not folder.exists():
        raise RefsError(f"{source} {current[source]} está fijada pero no está en var/refs; "
                        f"descárgala con demand-engine/bin/refs fetch {source}")
    return folder


def load_gz(path: Path):
    return json.loads(gzip.decompress(path.read_bytes()))


def short(gid: str) -> str:
    return gid.rsplit("/", 1)[-1] if gid else gid


def shopify_categories_in(folder: Path) -> dict:
    return {short(c["id"]): c for v in load_gz(folder / "categories.es.json.gz")["verticals"] for c in v["categories"]}


def google_rules_in(folder: Path) -> dict:
    """Shopify category → (English full name, [(Google id, Google full name)]) of a shopify-google version."""
    out = {}
    for path in sorted(folder.glob("integrations.google.*.json.gz")):
        for mapping in load_gz(path)["mappings"]:
            for rule in mapping["rules"]:
                out[short(rule["input"]["category"]["id"])] = (
                    rule["input"]["category"]["full_name"],
                    [(o["id"], o["full_name"]) for o in rule["output"]["category"]],
                )
    return out


@functools.cache
def shopify_categories() -> dict:
    """Shopify categories of the pinned version, by short id."""
    return shopify_categories_in(pinned("shopify"))


@functools.cache
def shopify_attributes() -> dict:
    return {a["handle"]: a for a in load_gz(pinned("shopify") / "attributes.es.json.gz")["attributes"]}


@functools.cache
def google_mapping() -> dict:
    """Shopify's official mapping to Google, pinned version."""
    return google_rules_in(pinned("shopify-google"))


@functools.cache
def google_names() -> dict:
    lines = (pinned("google") / GOOGLE_FILE).read_text(encoding="utf-8").splitlines()
    return dict(l.split(" - ", 1) for l in lines if " - " in l and not l.startswith("#"))


def ptd(product_type: str) -> tuple:
    """(properties of the JSON schema, definition) of an Amazon PTD, pinned version."""
    base = pinned("amazon-ptd")
    path = base / f"schemas/{product_type}.schema.json.gz"
    if not path.exists():
        raise RefsError(f"no existe el PTD {product_type}")
    definition = json.loads((base / f"definitions/{product_type}.json").read_text(encoding="utf-8"))
    return load_gz(path)["properties"], definition


def enum_values(node, out=None) -> list:
    """Every value of the enums in a JSON schema node (their display names when present)."""
    out = [] if out is None else out
    if isinstance(node, dict):
        if isinstance(node.get("enum"), list):
            out.extend(node.get("enumNames") or node["enum"])
        for v in node.values():
            enum_values(v, out)
    elif isinstance(node, list):
        for v in node:
            enum_values(v, out)
    return out


def dated_version(source: str) -> str:
    version = today()
    if version in versions(source):
        fail(f"{source}: ya hay una extracción de hoy ({version})")
    return version


# --- Shopify ------------------------------------------------------------------

def shopify_release(tag: str = None) -> dict:
    return get_json(f"{SHOPIFY_API}/tags/{tag}" if tag else f"{SHOPIFY_API}/latest")


def check_release(source: str) -> str:
    tag = shopify_release()["tag_name"]
    return f"al día ({tag})" if tag in versions(source) else f"nueva versión publicada: {tag}"


def fetch_release(source: str, asset_re, assets: str, args) -> None:
    """A Shopify release as a version of `source`: the assets matching asset_re, checked against the digest."""
    release = shopify_release(args.version)
    tag = release["tag_name"]
    if tag in versions(source):
        print(f"{source}: {tag} ya descargada")
        return
    snap = Snapshot(source, tag, {
        "repository": "Shopify/product-taxonomy",
        "release": release["html_url"],
        "published_at": release["published_at"],
        "assets": assets,
    })
    for asset in sorted(release["assets"], key=lambda a: a["name"]):
        if not asset_re.search(asset["name"]):
            continue
        entry = snap.add(asset["name"], get_bytes(asset["browser_download_url"]), asset["browser_download_url"])
        digest = asset.get("digest")
        if entry["size"] != asset["size"] or (digest and digest != "sha256:" + entry["sha256"]):
            snap.discard()
            fail(f"{source}: {asset['name']} no coincide con el tamaño o el sha256 publicados")
    if not snap.files:
        snap.discard()
        fail(f"{source}: la release {tag} no tiene ficheros que coincidan con {assets}")
    snap.commit()


def check_shopify() -> str:
    return check_release("shopify")


def fetch_shopify(args) -> None:
    fetch_release("shopify", SHOPIFY_ASSET_RE, "*.es.json.gz, *.es.txt.gz", args)


def nodes_shopify(folder: Path) -> list:
    categories = {k: (c["name"], (short(c.get("parent_id")),) if c.get("parent_id") else ())
                  for k, c in shopify_categories_in(folder).items()}
    attributes = {short(a["id"]): (a["name"], ()) for a in load_gz(folder / "attributes.es.json.gz")["attributes"]}
    return [("categorías", categories, "renombrados"), ("atributos", attributes, "renombrados")]


def check_shopify_google() -> str:
    return check_release("shopify-google")


def fetch_shopify_google(args) -> None:
    fetch_release("shopify-google", SHOPIFY_GOOGLE_RE, "integrations.google.shopify_*.en.json.gz", args)


def nodes_shopify_google(folder: Path) -> list:
    """Each mapped Shopify category, named by the Google categories it maps to."""
    rules = {k: (",".join(g for g, _ in outputs), ()) for k, (_, outputs) in google_rules_in(folder).items()}
    return [("mapeos", rules, "cambiados")]


# --- Google -------------------------------------------------------------------

def google_download():
    data = get_bytes(GOOGLE_URL)
    match = GOOGLE_VERSION_RE.match(data)
    if not match:
        fail("google: no se reconoce la cabecera de versión del fichero")
    return match.group(1).decode(), data


def check_google() -> str:
    version, data = google_download()
    latest = latest_manifest("google")
    if latest and latest["files"][0]["sha256"] == sha256(data):
        return f"al día ({latest['version']})"
    if latest and latest["origin"]["taxonomy_version"] == version:
        return f"contenido distinto con la misma cabecera ({version})"
    return f"nueva versión publicada: {version}"


def fetch_google(args) -> None:
    version, data = google_download()
    name = version if version not in versions("google") else f"{version}+{today()}"
    snap = Snapshot("google", name, {"url": GOOGLE_URL, "taxonomy_version": version, "locale": "es-ES"})
    snap.add(GOOGLE_FILE, data, GOOGLE_URL)
    snap.commit()


def nodes_google(folder: Path) -> list:
    by_path = {}
    for line in (folder / GOOGLE_FILE).read_text(encoding="utf-8").splitlines():
        if not line.startswith("#") and " - " in line:
            gid, path = line.split(" - ", 1)
            by_path[path] = gid
    nodes = {}
    for path, gid in by_path.items():
        parts = path.split(" > ")
        parent = by_path.get(" > ".join(parts[:-1]))
        nodes[gid] = (parts[-1], (parent,) if parent else ())
    return [("categorías", nodes, "renombrados")]


# --- Amazon -------------------------------------------------------------------

def check_amazon_btg() -> str:
    latest = latest_manifest("amazon-btg")
    if not latest:
        return "sin extracciones"
    age = (date.today() - date.fromisoformat(latest["version"][:10])).days
    return f"sin versión publicada; última extracción {latest['version']} (hace {age} días). Para comprobarla, refs fetch amazon-btg"


def fetch_amazon_btg(args) -> None:
    version = dated_version("amazon-btg")
    api = SPAPI()
    report = api.call("POST", "/reports/2021-06-30/reports",
                      {"reportType": "GET_XML_BROWSE_TREE_DATA", "marketplaceIds": [MARKETPLACE_ES]})
    print(f"amazon-btg: informe {report['reportId']} solicitado; esperando…", flush=True)
    deadline = time.time() + REPORT_TIMEOUT
    while True:
        time.sleep(REPORT_POLL)
        status = api.call("GET", f"/reports/2021-06-30/reports/{report['reportId']}")
        if status["processingStatus"] == "DONE":
            break
        if status["processingStatus"] in ("CANCELLED", "FATAL") or time.time() > deadline:
            fail(f"amazon-btg: el informe terminó en {status['processingStatus']}")
    document = api.call("GET", f"/reports/2021-06-30/documents/{status['reportDocumentId']}")
    data = get_bytes(document["url"])   # presigned URL: temporary credentials, never stored
    if document.get("compressionAlgorithm") != "GZIP":
        data = gzip.compress(data, mtime=0)
    snap = Snapshot("amazon-btg", version, {
        "marketplace": "Amazon.es",
        "marketplace_id": MARKETPLACE_ES,
        "report_type": "GET_XML_BROWSE_TREE_DATA",
        "report_id": report["reportId"],
        "data_end_time": status.get("dataEndTime"),
    })
    snap.add(BTG_FILE, data, f"SP-API report document {status['reportDocumentId']}")
    snap.commit()


def nodes_amazon_btg(folder: Path) -> list:
    """A browse node may hang from several paths: its parents are a set."""
    names, parents = {}, {}
    with gzip.open(folder / BTG_FILE) as f:
        for _, el in ET.iterparse(f):
            if el.tag == "Node":
                node = el.findtext("browseNodeId")
                path = (el.findtext("browsePathById") or "").split(",")
                names.setdefault(node, el.findtext("browseNodeName"))
                parents.setdefault(node, set()).update(path[-2:-1])
                el.clear()
    return [("nodos", {n: (names[n], tuple(sorted(parents[n]))) for n in names}, "renombrados")]


def ptd_index(api: SPAPI) -> dict:
    return api.call("GET", "/definitions/2020-09-01/productTypes", marketplaceIds=MARKETPLACE_ES, locale=PTD_LOCALE)


def check_amazon_ptd() -> str:
    index = ptd_index(SPAPI())
    latest = latest_manifest("amazon-ptd")
    if not latest:
        return f"sin extracciones; publicados {len(index['productTypes'])} tipos"
    if latest["origin"]["product_type_version"] == index.get("productTypeVersion") \
            and latest["origin"]["product_types"] == len(index["productTypes"]):
        return f"al día ({latest['version']})"
    return f"cambios publicados desde {latest['version']}: {len(index['productTypes'])} tipos, versión {index.get('productTypeVersion')}"


def fetch_amazon_ptd(args) -> None:
    version = dated_version("amazon-ptd")
    api = SPAPI()
    index = ptd_index(api)
    names = sorted(p["name"] for p in index["productTypes"])
    snap = Snapshot("amazon-ptd", version, {
        "marketplace": "Amazon.es",
        "marketplace_id": MARKETPLACE_ES,
        "locale": PTD_LOCALE,
        "requirements": "LISTING",
        "product_type_version": index.get("productTypeVersion"),
        "product_types": len(names),
    })
    snap.add("index.json", dumps(index), "GET /definitions/2020-09-01/productTypes")

    def download(path, url, checksum):
        try:
            data = get_bytes(url)
        except urllib.error.URLError as e:
            snap.errors.append(f"{path}: {e}")
            return
        if checksum and base64.b64encode(hashlib.md5(data).digest()).decode() != checksum:
            snap.errors.append(f"{path}: el MD5 no coincide con el checksum publicado")
            return
        snap.add(path, gzip.compress(data, mtime=0), "presigned schema link", checksum_md5=checksum)

    try:
        with ThreadPoolExecutor(max_workers=4) as pool:
            jobs = []
            for i, name in enumerate(names, 1):
                time.sleep(PTD_INTERVAL)
                path = f"/definitions/2020-09-01/productTypes/{name}"
                try:
                    definition = api.call("GET", path, marketplaceIds=MARKETPLACE_ES,
                                          locale=PTD_LOCALE, requirements="LISTING")
                except urllib.error.HTTPError as e:
                    snap.errors.append(f"{name}: HTTP {e.code}")
                    continue
                links = {key: definition[key]["link"].pop("resource") for key in ("schema", "metaSchema")}
                snap.add(f"definitions/{name}.json", dumps(definition), f"GET {path}")
                jobs.append(pool.submit(download, f"schemas/{name}.schema.json.gz",
                                        links["schema"], definition["schema"].get("checksum")))
                if i == 1:
                    jobs.append(pool.submit(download, "meta-schema.json.gz",
                                            links["metaSchema"], definition["metaSchema"].get("checksum")))
                if i % 100 == 0:
                    print(f"amazon-ptd: {i}/{len(names)}", flush=True)
            for job in jobs:
                job.result()
    except BaseException:
        snap.discard()
        raise
    snap.commit()


def nodes_amazon_ptd(folder: Path) -> list:
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    types = {p["name"]: (p.get("displayName"), ()) for p in index["productTypes"]}
    files = json.loads((folder / "MANIFEST.json").read_text(encoding="utf-8"))["files"]
    schemas = {f["path"].split("/")[-1].split(".")[0]: (f["content_sha256"], ())
               for f in files if f["path"].startswith("schemas/")}
    return [("tipos de producto", types, "renombrados"), ("esquemas", schemas, "modificados")]


# --- Commands -----------------------------------------------------------------

SOURCES = {
    "shopify": (check_shopify, fetch_shopify, nodes_shopify),
    "shopify-google": (check_shopify_google, fetch_shopify_google, nodes_shopify_google),
    "google": (check_google, fetch_google, nodes_google),
    "amazon-btg": (check_amazon_btg, fetch_amazon_btg, nodes_amazon_btg),
    "amazon-ptd": (check_amazon_ptd, fetch_amazon_ptd, nodes_amazon_ptd),
}


def selected(names: list) -> list:
    unknown = [n for n in names if n not in SOURCES]
    if unknown:
        fail(f"fuente desconocida: {', '.join(unknown)} (fuentes: {', '.join(SOURCES)})")
    return names or list(SOURCES)


def cmd_status(args) -> None:
    current = pins()
    for name in SOURCES:
        found = versions(name)
        if not found:
            print(f"{name:<14} sin descargar")
            continue
        pinned = current.get(name, "—")
        latest = manifest(name, found[-1])
        newer = " · hay una versión posterior a la fijada" if found[-1] != pinned else ""
        print(f"{name:<14} fijada {pinned} · última {found[-1]} ({latest['fetched_at'][:10]}) · "
              f"{len(found)} versión(es){newer}")


def cmd_check(args) -> None:
    for name in selected(args.sources):
        try:
            print(f"{name:<14} {SOURCES[name][0]()}", flush=True)
        except urllib.error.URLError as e:
            print(f"{name:<14} no se pudo comprobar: {e}")


def cmd_fetch(args) -> None:
    if args.version and (not args.sources or set(args.sources) - {"shopify", "shopify-google"}):
        fail("--version solo se aplica a: refs fetch shopify|shopify-google --version TAG")
    for name in selected(args.sources):
        SOURCES[name][1](args)


def show(label: str, lines: list, limit: int) -> None:
    if not lines:
        return
    print(f"  {label} ({len(lines)}):")
    for line in lines[:limit]:
        print(f"    {line}")
    if len(lines) > limit:
        print(f"    … +{len(lines) - limit} más (--all)")


def cmd_diff(args) -> None:
    found = versions(args.source)
    old = args.old or pins().get(args.source)
    new = args.new or (found[-1] if found else None)
    for version in (old, new):
        if version not in found:
            fail(f"{args.source}: no existe la versión {version} (hay: {', '.join(found) or 'ninguna'})")
    if old == new:
        print(f"{args.source}: {old} es a la vez la fijada y la última; nada que comparar")
        return
    limit = sys.maxsize if args.all else DIFF_LIMIT
    nodes = SOURCES[args.source][2]
    print(f"{args.source}: {old} → {new}")
    for (title, before, label), (_, after, _) in zip(nodes(REFS / args.source / old), nodes(REFS / args.source / new)):
        common = before.keys() & after.keys()
        added = sorted(after.keys() - before.keys())
        removed = sorted(before.keys() - after.keys())
        changed = sorted(k for k in common if before[k][0] != after[k][0])
        moved = sorted(k for k in common if before[k][1] != after[k][1])
        print(f"{title}: {len(before)} → {len(after)} · +{len(added)} −{len(removed)} · "
              f"{label} {len(changed)} · movidos {len(moved)}")
        show("añadidos", [f"{k}  {after[k][0]}" for k in added], limit)
        show("eliminados", [f"{k}  {before[k][0]}" for k in removed], limit)
        show(label, [f"{k}  {before[k][0]} → {after[k][0]}" for k in changed], limit)
        show("movidos", [f"{k}  {after[k][0]}: {','.join(before[k][1]) or '—'} → {','.join(after[k][1]) or '—'}"
                         for k in moved], limit)


def cmd_pin(args) -> None:
    if args.version not in versions(args.source):
        fail(f"{args.source}: no existe la versión {args.version}")
    current = pins()
    previous = current.get(args.source)
    current[args.source] = args.version
    save_pins(current)
    print(f"{args.source}: fijada {args.version}" + (f" (antes {previous})" if previous else ""))
    if previous and previous != args.version:
        print(f"Revisa los mapeos construidos sobre {previous}: bin/refs diff {args.source} {previous} {args.version}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="refs", description="Material de referencia externo (refs/).")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("status", help="versiones por fuente y la fijada").set_defaults(func=cmd_status)
    p = sub.add_parser("check", help="¿hay algo nuevo en origen? (no guarda nada)")
    p.add_argument("sources", nargs="*", metavar="SOURCE")
    p.set_defaults(func=cmd_check)
    p = sub.add_parser("fetch", help="descargar una versión nueva")
    p.add_argument("sources", nargs="*", metavar="SOURCE")
    p.add_argument("--version", help="tag de Shopify (por defecto, la última estable)")
    p.set_defaults(func=cmd_fetch)
    p = sub.add_parser("diff", help="cambios de nodos entre dos versiones")
    p.add_argument("source", choices=list(SOURCES))
    p.add_argument("old", nargs="?")
    p.add_argument("new", nargs="?")
    p.add_argument("--all", action="store_true", help="sin límite de líneas")
    p.set_defaults(func=cmd_diff)
    p = sub.add_parser("pin", help="fijar la versión de trabajo")
    p.add_argument("source", choices=list(SOURCES))
    p.add_argument("version")
    p.set_defaults(func=cmd_pin)
    args = parser.parse_args()
    (getattr(args, "func", None) or cmd_status)(args)


if __name__ == "__main__":
    main()
