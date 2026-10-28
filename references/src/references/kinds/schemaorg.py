"""The Schema.org vocabulary in machine format, by release (GitHub schemaorg/schemaorg)."""
import hashlib
import json
from pathlib import Path

from .. import net
from ..read import VOCABULARY, ids, literal
from ..store import RefsError, Version, refs_dir, versions
from .common import show

SCHEMAORG_API = "https://api.github.com/repos/schemaorg/schemaorg"
SCHEMAORG_FILES = (
    VOCABULARY,                                   # the vocabulary
    "schemaorg-all-https.jsonld",                 # plus the retired terms (attic)
    "schemaorg-current-https-types.csv",
    "schemaorg-current-https-properties.csv",
    "schemaorgcontext.jsonld",                    # JSON-LD context of the release
)
RELATIONS = (("rdfs:subClassOf", "superclase"), ("schema:domainIncludes", "dominio"),
             ("schema:rangeIncludes", "rango"), ("schema:isPartOf", "sección"),
             ("schema:supersededBy", "sustituido por"))


def git_sha(data: bytes) -> str:
    """The sha GitHub gives for a file: its git blob id."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def release(version: str = None) -> dict:
    return net.get_json(f"{SCHEMAORG_API}/releases/" + (f"tags/v{version}" if version else "latest"))


def check(sid: str, source: dict) -> str:
    version = release()["tag_name"].removeprefix("v")
    return f"al día ({version})" if version in versions(sid) else f"nueva versión publicada: {version}"


def fetch(sid: str, source: dict, tag: str) -> None:
    published = release(tag)
    tag = published["tag_name"]
    version = tag.removeprefix("v")
    if version in versions(sid):
        print(f"{sid}: {version} ya descargada")
        return
    folder = f"data/releases/{version}"
    listing = {f["name"]: f for f in net.get_json(f"{SCHEMAORG_API}/contents/{folder}?ref={tag}")}
    files = []
    for name in SCHEMAORG_FILES:
        if name not in listing:
            raise RefsError(f"{sid}: la release {version} no tiene {folder}/{name}")
        meta = listing[name]
        data = net.get_bytes(meta["download_url"])
        if len(data) != meta["size"] or git_sha(data) != meta["sha"]:
            raise RefsError(f"{sid}: {name} no coincide con el tamaño o el sha de GitHub")
        files.append((name, data, meta))
    snap = Version(sid, version, {
        "repository": "schemaorg/schemaorg",
        "release": published["html_url"],
        "published_at": published["published_at"],
        "folder": folder,
    })
    for name, data, meta in files:
        snap.add(name, data, meta["download_url"], git_sha=meta["sha"])
    snap.commit()


def terms(folder: Path) -> list:
    """Types, properties and enumeration members: id → (definition, relations)."""
    graph = json.loads((folder / VOCABULARY).read_text(encoding="utf-8"))["@graph"]
    groups = {"tipos": {}, "propiedades": {}, "valores de enumeración": {}}
    for node in graph:
        types = ids(node.get("@type"))
        relations = {f"{label}:{i}" for key, label in RELATIONS for i in ids(node.get(key))}
        if "rdfs:Class" in types:
            group = "tipos"
        elif "rdf:Property" in types:
            group = "propiedades"
        else:
            group = "valores de enumeración"
            relations |= {f"de:{t}" for t in types}
        groups[group][node["@id"]] = (literal(node.get("rdfs:comment", "")), frozenset(relations))
    return list(groups.items())


def diff(sid: str, old: str, new: str, limit: int) -> None:
    for (title, before), (_, after) in zip(terms(refs_dir() / sid / old), terms(refs_dir() / sid / new)):
        common = before.keys() & after.keys()
        added = sorted(after.keys() - before.keys())
        removed = sorted(before.keys() - after.keys())
        changed = sorted(k for k in common if before[k][0] != after[k][0])
        related = sorted(k for k in common if before[k][1] != after[k][1])
        print(f"{title}: {len(before)} → {len(after)} · +{len(added)} −{len(removed)} · "
              f"definición cambiada {len(changed)} · relaciones cambiadas {len(related)}")
        show("añadidos", [f"{k}  {after[k][0][:90]}" for k in added], limit)
        show("eliminados", [f"{k}  {before[k][0][:90]}" for k in removed], limit)
        show("definición cambiada", changed, limit)
        show("relaciones cambiadas", [
            f"{k}  " + " ".join([f"+{r}" for r in sorted(after[k][1] - before[k][1])]
                                + [f"−{r}" for r in sorted(before[k][1] - after[k][1])])
            for k in related], limit)
