"""An authority table of EU Vocabularies (EU Publications Office), such as the country table
with its ISO 3166-1 codes. `authority` names the table (country) and `file` its SKOS file
(countries-skos.rdf). A version is the table's own release (owl:versionInfo, 20260923-0); the
file of a release comes from the download handler of the Publications Office."""
import re
import urllib.parse
import xml.etree.ElementTree as ET

from .. import net
from ..store import RefsError, Version, latest_manifest, refs_dir, versions
from .common import show

SCHEME = "https://publications.europa.eu/resource/authority/{}"
DISTRIBUTION = "http://publications.europa.eu/resource/distribution/{}/{}/rdf/skos_core/{}"
DOWNLOAD = "https://op.europa.eu/o/opportal-service/euvoc-download-handler?"
SKOS = "{http://www.w3.org/2004/02/skos/core#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def release(source: dict) -> str:
    """The current release of the table: owl:versionInfo of its scheme."""
    data, _, _ = net.download(SCHEME.format(source["authority"]), {"accept": "application/rdf+xml"})
    m = re.search(rb"<owl:versionInfo>\s*([^<\s]+)", data)
    if not m:
        raise RefsError(f"{source['authority']}: el esquema no declara owl:versionInfo")
    return m[1].decode()


def check(sid: str, source: dict) -> str:
    latest = latest_manifest(sid)
    upstream = release(source)
    if not latest:
        return f"sin descargar (en origen: {upstream})"
    if upstream in versions(sid):
        return f"al día ({upstream})"
    return f"hay una versión {upstream} (la última descargada es {latest['version']}): refs fetch {sid}"


def fetch(sid: str, source: dict, tag: str) -> None:
    version = tag or release(source)
    cellar = DISTRIBUTION.format(source["authority"], version, source["file"])
    url = DOWNLOAD + urllib.parse.urlencode({"cellarURI": cellar, "fileName": source["file"]})
    data, _, final = net.download(url)
    if b"skos" not in data[:2000].lower():
        raise RefsError(f"{sid}: {source['file']} {version} no es un fichero SKOS")
    snap = Version(sid, version, {"url": url, "cellar": cellar})
    snap.add(source["file"], data, cellar)
    snap.commit()


def concepts(path) -> dict:
    """URI → (notations, deprecated) of each concept of a SKOS file."""
    out = {}
    for c in ET.parse(path).getroot().iter(SKOS + "Concept"):
        notations = sorted(f"{n.get(RDF + 'datatype', '').rsplit('#', 1)[-1]}={n.text}" for n in c.findall(SKOS + "notation"))
        deprecated = any(x.tag.endswith("}deprecated") and x.text == "true" for x in c)
        out[c.get(RDF + "about")] = (notations, deprecated)
    return out


def diff(sid: str, old: str, new: str, limit: int) -> None:
    before, after = ({k.rsplit("/", 1)[-1]: v for k, v in concepts(next((refs_dir() / sid / v).glob("*.rdf"))).items()}
                     for v in (old, new))
    common = before.keys() & after.keys()
    print(f"conceptos: {len(before)} → {len(after)}")
    show("añadidos", sorted(after.keys() - before.keys()), limit)
    show("eliminados", sorted(before.keys() - after.keys()), limit)
    show("retirados", sorted(k for k in common if after[k][1] and not before[k][1]), limit)
    show("notaciones cambiadas", [f"{k}: {sorted(set(before[k][0]) ^ set(after[k][0]))}"
                                  for k in sorted(common) if before[k][0] != after[k][0]], limit)
