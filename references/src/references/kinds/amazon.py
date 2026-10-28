"""Amazon.es through the Selling Partner API: the browse tree and the Product Type Definitions."""
import base64
import gzip
import hashlib
import json
import time
import urllib.error
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

from .. import net
from ..read import BTG_FILE
from ..store import RefsError, Version, dumps, latest_manifest
from .common import dated_version, diff_nodes

MARKETPLACE_ES = "A1RKKUPIHCS9HS"
PTD_LOCALE = "es_ES"
PTD_INTERVAL = 0.25     # seconds between getDefinitionsProductType calls (rate 5/s)
REPORT_POLL = 15        # seconds between report status polls
REPORT_TIMEOUT = 1800


# --- Browse tree --------------------------------------------------------------

def check_btg(sid: str, source: dict) -> str:
    latest = latest_manifest(sid)
    if not latest:
        return "sin extracciones"
    age = (date.today() - date.fromisoformat(latest["version"][:10])).days
    return f"sin versión publicada; última extracción {latest['version']} (hace {age} días). Para comprobarla, refs fetch {sid}"


def fetch_btg(sid: str, source: dict, tag: str) -> None:
    version = dated_version(sid)
    api = net.SPAPI()
    report = api.call("POST", "/reports/2021-06-30/reports",
                      {"reportType": "GET_XML_BROWSE_TREE_DATA", "marketplaceIds": [MARKETPLACE_ES]})
    print(f"{sid}: informe {report['reportId']} solicitado; esperando…", flush=True)
    deadline = time.time() + REPORT_TIMEOUT
    while True:
        time.sleep(REPORT_POLL)
        status = api.call("GET", f"/reports/2021-06-30/reports/{report['reportId']}")
        if status["processingStatus"] == "DONE":
            break
        if status["processingStatus"] in ("CANCELLED", "FATAL") or time.time() > deadline:
            raise RefsError(f"{sid}: el informe terminó en {status['processingStatus']}")
    document = api.call("GET", f"/reports/2021-06-30/documents/{status['reportDocumentId']}")
    data = net.get_bytes(document["url"])   # presigned URL: temporary credentials, never stored
    if document.get("compressionAlgorithm") != "GZIP":
        data = gzip.compress(data, mtime=0)
    snap = Version(sid, version, {
        "marketplace": "Amazon.es",
        "marketplace_id": MARKETPLACE_ES,
        "report_type": "GET_XML_BROWSE_TREE_DATA",
        "report_id": report["reportId"],
        "data_end_time": status.get("dataEndTime"),
    })
    snap.add(BTG_FILE, data, f"SP-API report document {status['reportDocumentId']}")
    snap.commit()


def nodes_btg(folder: Path) -> list:
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


def diff_btg(sid: str, old: str, new: str, limit: int) -> None:
    diff_nodes(nodes_btg, sid, old, new, limit)


# --- Product Type Definitions -------------------------------------------------

def ptd_index(api) -> dict:
    return api.call("GET", "/definitions/2020-09-01/productTypes", marketplaceIds=MARKETPLACE_ES, locale=PTD_LOCALE)


def check_ptd(sid: str, source: dict) -> str:
    index = ptd_index(net.SPAPI())
    latest = latest_manifest(sid)
    if not latest:
        return f"sin extracciones; publicados {len(index['productTypes'])} tipos"
    if latest["origin"]["product_type_version"] == index.get("productTypeVersion") \
            and latest["origin"]["product_types"] == len(index["productTypes"]):
        return f"al día ({latest['version']})"
    return f"cambios publicados desde {latest['version']}: {len(index['productTypes'])} tipos, versión {index.get('productTypeVersion')}"


def fetch_ptd(sid: str, source: dict, tag: str) -> None:
    version = dated_version(sid)
    api = net.SPAPI()
    index = ptd_index(api)
    names = sorted(p["name"] for p in index["productTypes"])
    snap = Version(sid, version, {
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
            data = net.get_bytes(url)
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
                    print(f"{sid}: {i}/{len(names)}", flush=True)
            for job in jobs:
                job.result()
    except BaseException:
        snap.discard()
        raise
    snap.commit()


def nodes_ptd(folder: Path) -> list:
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    types = {p["name"]: (p.get("displayName"), ()) for p in index["productTypes"]}
    files = json.loads((folder / "MANIFEST.json").read_text(encoding="utf-8"))["files"]
    schemas = {f["path"].split("/")[-1].split(".")[0]: (f["content_sha256"], ())
               for f in files if f["path"].startswith("schemas/")}
    return [("tipos de producto", types, "renombrados"), ("esquemas", schemas, "modificados")]


def diff_ptd(sid: str, old: str, new: str, limit: int) -> None:
    diff_nodes(nodes_ptd, sid, old, new, limit)
