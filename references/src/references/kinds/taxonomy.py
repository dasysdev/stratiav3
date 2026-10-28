"""Product taxonomies: Shopify (Spanish release assets and its mapping to Google) and Google."""
import re
from pathlib import Path

from .. import net
from ..read import GOOGLE_FILE, SHOPIFY_ATTRIBUTES, google_rules_in, load_gz, shopify_categories_in, short
from ..store import RefsError, Version, latest_manifest, sha256, today, versions
from .common import diff_nodes

SHOPIFY_API = "https://api.github.com/repos/Shopify/product-taxonomy/releases"
ASSETS = {      # the release assets each Shopify source keeps
    "shopify-taxonomy": (re.compile(r"\.es\.(json|txt)\.gz$"), "*.es.json.gz, *.es.txt.gz"),
    "shopify-google": (re.compile(r"^integrations\.google\.shopify_.+\.en\.json\.gz$"),
                       "integrations.google.shopify_*.en.json.gz"),
}
GOOGLE_VERSION_RE = re.compile(rb"^# Google_Product_Taxonomy_Version: (\S+)")


# --- Shopify ------------------------------------------------------------------

def shopify_release(tag: str = None) -> dict:
    return net.get_json(f"{SHOPIFY_API}/tags/{tag}" if tag else f"{SHOPIFY_API}/latest")


def check_release(sid: str, source: dict) -> str:
    tag = shopify_release()["tag_name"]
    return f"al día ({tag})" if tag in versions(sid) else f"nueva versión publicada: {tag}"


def fetch_release(sid: str, kind: str, tag: str) -> None:
    """A Shopify release as a version of `sid`: the assets of its kind, checked against the digest."""
    asset_re, assets = ASSETS[kind]
    release = shopify_release(tag)
    tag = release["tag_name"]
    if tag in versions(sid):
        print(f"{sid}: {tag} ya descargada")
        return
    snap = Version(sid, tag, {
        "repository": "Shopify/product-taxonomy",
        "release": release["html_url"],
        "published_at": release["published_at"],
        "assets": assets,
    })
    for asset in sorted(release["assets"], key=lambda a: a["name"]):
        if not asset_re.search(asset["name"]):
            continue
        item = snap.add(asset["name"], net.get_bytes(asset["browser_download_url"]), asset["browser_download_url"])
        digest = asset.get("digest")
        if item["size"] != asset["size"] or (digest and digest != "sha256:" + item["sha256"]):
            snap.discard()
            raise RefsError(f"{sid}: {asset['name']} no coincide con el tamaño o el sha256 publicados")
    if not snap.files:
        snap.discard()
        raise RefsError(f"{sid}: la release {tag} no tiene ficheros que coincidan con {assets}")
    snap.commit()


def fetch_shopify(sid: str, source: dict, tag: str) -> None:
    fetch_release(sid, "shopify-taxonomy", tag)


def fetch_shopify_google(sid: str, source: dict, tag: str) -> None:
    fetch_release(sid, "shopify-google", tag)


def nodes_shopify(folder: Path) -> list:
    categories = {k: (c["name"], (short(c.get("parent_id")),) if c.get("parent_id") else ())
                  for k, c in shopify_categories_in(folder).items()}
    attributes = {short(a["id"]): (a["name"], ()) for a in load_gz(folder / SHOPIFY_ATTRIBUTES)["attributes"]}
    return [("categorías", categories, "renombrados"), ("atributos", attributes, "renombrados")]


def nodes_shopify_google(folder: Path) -> list:
    """Each mapped Shopify category, named by the Google categories it maps to."""
    rules = {k: (",".join(g for g, _ in outputs), ()) for k, (_, outputs) in google_rules_in(folder).items()}
    return [("mapeos", rules, "cambiados")]


def diff_shopify(sid: str, old: str, new: str, limit: int) -> None:
    diff_nodes(nodes_shopify, sid, old, new, limit)


def diff_shopify_google(sid: str, old: str, new: str, limit: int) -> None:
    diff_nodes(nodes_shopify_google, sid, old, new, limit)


# --- Google -------------------------------------------------------------------

def google_download(source: dict):
    data = net.get_bytes(source["url"])
    match = GOOGLE_VERSION_RE.match(data)
    if not match:
        raise RefsError("google: no se reconoce la cabecera de versión del fichero")
    return match.group(1).decode(), data


def check_google(sid: str, source: dict) -> str:
    version, data = google_download(source)
    latest = latest_manifest(sid)
    if latest and latest["files"][0]["sha256"] == sha256(data):
        return f"al día ({latest['version']})"
    if latest and latest["origin"]["taxonomy_version"] == version:
        return f"contenido distinto con la misma cabecera ({version})"
    return f"nueva versión publicada: {version}"


def fetch_google(sid: str, source: dict, tag: str) -> None:
    version, data = google_download(source)
    name = version if version not in versions(sid) else f"{version}+{today()}"
    snap = Version(sid, name, {"url": source["url"], "taxonomy_version": version, "locale": "es-ES"})
    snap.add(GOOGLE_FILE, data, source["url"])
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


def diff_google(sid: str, old: str, new: str, limit: int) -> None:
    diff_nodes(nodes_google, sid, old, new, limit)
