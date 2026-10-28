"""Kinds of source (`kind` in sources.json): how each one is checked upstream, fetched as a new
version and compared between two versions.

  shopify-taxonomy   Shopify Standard Product Taxonomy, Spanish release assets (GitHub)
  shopify-google     Shopify's official mapping to the Google taxonomy, same release (English only)
  google-taxonomy    Google Product Taxonomy es-ES with IDs
  amazon-browse-tree Amazon.es browse tree (SP-API report GET_XML_BROWSE_TREE_DATA)
  amazon-ptd         Amazon.es Product Type Definitions es_ES: index, definitions, schemas
  schemaorg          Schema.org vocabulary in machine format, by release (GitHub schemaorg/schemaorg,
                     data/releases/<version>/), checked against the git sha of each file
  document           one published document (HTML page, PDF or data file), versioned by fetch
                     date. An HTML page counts by its text: a change of markup alone is no new version
  law                a law by its official consolidated text (BOE, or EUR-Lex through Cellar),
                     versioned by the date the official source names the text by
  eu-authority       an authority table of EU Vocabularies (country), by its release
"""
from typing import Callable, NamedTuple

from . import amazon, document, euvoc, law, schemaorg, taxonomy


class Kind(NamedTuple):
    check: Callable     # (sid, source) -> str
    fetch: Callable     # (sid, source, version) -> None; version: a release tag, or None
    diff: Callable      # (sid, old, new, limit) -> None
    release: bool       # versioned by an upstream release (fetch --version)
    fields: tuple = ()  # what a source of the kind declares besides the common keys; "a|b": one of them


KINDS = {
    "shopify-taxonomy": Kind(taxonomy.check_release, taxonomy.fetch_shopify, taxonomy.diff_shopify, True),
    "shopify-google": Kind(taxonomy.check_release, taxonomy.fetch_shopify_google, taxonomy.diff_shopify_google, True),
    "google-taxonomy": Kind(taxonomy.check_google, taxonomy.fetch_google, taxonomy.diff_google, False),
    "amazon-browse-tree": Kind(amazon.check_btg, amazon.fetch_btg, amazon.diff_btg, False),
    "amazon-ptd": Kind(amazon.check_ptd, amazon.fetch_ptd, amazon.diff_ptd, False),
    "schemaorg": Kind(schemaorg.check, schemaorg.fetch, schemaorg.diff, True),
    "document": Kind(document.check, document.fetch, document.diff, False),
    "law": Kind(law.check, law.fetch, document.diff, True, ("cite", "boe|celex")),
    "eu-authority": Kind(euvoc.check, euvoc.fetch, euvoc.diff, True, ("authority", "file")),
}
