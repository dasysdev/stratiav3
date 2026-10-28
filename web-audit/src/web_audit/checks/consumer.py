"""Checks of the consumer level of Web Schema.org (reference/requirements/consumer.json).

Each requirement is bound by its id. Most are a primitive of `markup` over a path of the graph;
those whose method is more than that have a function of their own. The general view (the
organization and its policies, ws-consumer/208 onwards) runs over the graph of the whole site.
"""
from __future__ import annotations

import re
import unicodedata
from urllib.parse import parse_qsl, urldefrag, urlsplit

from .. import vocab
from ..graph import Entity, Lit, Ref, is_type
from . import NA, NE, PENDING, SAT, UNSAT, Case, Result, bind, capped, check
from .markup import (at_most_one, country, currency, enum, enum_name, has, iso_date_or_datetime,
                     iso_datetime_with_zone, iso_time, label, non_negative_integer, none_has, not_both, number,
                     of_type, prop_is, select, text, value_types, values_ok, _result)

IMAGES_NE = "No se pueden descargar las imágenes enlazadas: capture no congela las imágenes (T-049, decisión del usuario)."
RENDERED_NE = "Hace falta el DOM renderizado de la página: el perfil de auditoría (audit-es) no ejecuta JavaScript y capture no guarda un DOM renderizado."
SAMEAS_SITE = re.compile(r"^www\.", re.I)


# --- Small helpers -----------------------------------------------------------------------------

def each(path: str, pred, describe: str, where=None, na: str | None = None):
    """Each entity of the path (that meets `where`) meets `pred`. NA without entities."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        es = [e for e in sel.entities if where is None or where(e)]
        if not es:
            return Result(NA, None, na or f"El marcado no contiene ninguna entidad de {path} que cumpla la condición.")
        bad = [label(e) for e in es if not pred(e)]
        return _result(bad, len(es), sel.refs, describe)
    return run


def has_valid(path: str, prop: str, test, describe: str):
    """Each entity of the path has a value of `prop` that passes `test`."""
    return each(path, lambda e: any(test(v) for v in e.values(prop)), f"sin {prop} {describe}")


def name_of(v) -> str:
    """The name of an entity (its first name), or the text of a literal."""
    if isinstance(v, Entity):
        names = [text(n).strip() for n in v.values("name") if text(n).strip()]
        return names[0] if names else ""
    return text(v).strip()


def string_literal(v) -> bool:
    return isinstance(v, Lit) and v.kind in ("json-string", "text", "value-object") and isinstance(v.value, str)


def unresolved(case: Case, *paths: str) -> list:
    return [r for p in paths for r in select(case, p).refs]


# --- Product ---------------------------------------------------------------------------------

bind("ws-consumer/001", has("Product", "offers", universal=True))
bind("ws-consumer/002", has("Product", "name", universal=True))
bind("ws-consumer/003", has("Product", "image", universal=True))
bind("ws-consumer/150", has("Product", "name", universal=True))
bind("ws-consumer/151", has("Product", "review", "aggregateRating", "offers", universal=True))
bind("ws-consumer/153", has("Product", "offers", universal=True))
bind("ws-consumer/042", has("Product", "sku", universal=True))


def image_urls(e: Entity) -> list[str]:
    out = []
    for v in e.values("image"):
        if isinstance(v, Entity):
            out += [text(u).strip() for p in ("contentUrl", "url") for u in v.values(p) if text(u).strip()]
        elif text(v).strip():
            out.append(text(v).strip())
    return list(dict.fromkeys(out))


def images_crawlable(path: str):
    """Image URLs not excluded by robots.txt for Googlebot-Image (else Googlebot or *), and served
    with success without authentication: the robots.txt of the site's own origins is in the audit;
    the response of each image is not (capture does not freeze images)."""
    def run(case: Case) -> Result:
        urls = [u for e in select(case, path).entities for u in image_urls(e)]
        if not urls:
            return Result(NA, None, "El marcado no contiene URL de imagen.")
        blocked, unknown = [], []
        for url in urls:
            rules = case.site.robots_rules(url) if urlsplit(url).scheme in ("http", "https") else None
            if rules is None:
                unknown.append(url)
            elif not rules.allowed(url, "googlebot-image"):
                blocked.append(url)
        ev = {"URL": capped(urls), "bloqueadas por robots.txt": capped(blocked),
              "host sin robots.txt en la auditoría": capped(unknown)}
        if blocked:
            return Result(UNSAT, ev)
        return Result(NE, ev, IMAGES_NE)
    return run


def images_need_download(path: str):
    def run(case: Case) -> Result:
        urls = [u for e in select(case, path).entities for u in image_urls(e)]
        if not urls:
            return Result(NA, None, "El marcado no contiene URL de imagen.")
        return Result(NE, {"URL": capped(urls)}, IMAGES_NE)
    return run


bind("ws-consumer/004", images_crawlable("Product"))
bind("ws-consumer/005", images_need_download("Product"))
for _n in ("007", "008", "009", "010"):
    bind(f"ws-consumer/{_n}", images_need_download("Product"))
bind("ws-consumer/185", images_crawlable("*"))
bind("ws-consumer/186", images_need_download("*"))


@check("ws-consumer/006")
def _more_than_one_image(case: Case) -> Result:
    es = [e for e in case.graph.of("Product") if image_urls(e)]
    if not es:
        return Result(NA, None, "Ninguna entidad Product tiene image.")
    bad = [f"{label(e)}: {len(image_urls(e))} imagen" for e in es if len(image_urls(e)) < 2]
    return _result(bad, len(es), [], "con una sola imagen")


bind("ws-consumer/011", value_types("Product", "offers", of_type("Offer"), "Offer (y no AggregateOffer)"))
bind("ws-consumer/154", value_types("Product", "offers", of_type("Offer"), "Offer (y no AggregateOffer)"))
bind("ws-consumer/014", value_types("Product", "audience", of_type("PeopleAudience"), "PeopleAudience"))
bind("ws-consumer/016", at_most_one("Product", "brand", key=lambda v: name_of(v).casefold()))
bind("ws-consumer/018", values_ok("Product", "category", lambda v: len(text(v)) < 750 if string_literal(v) else None,
                                  "textos de menos de 750 caracteres"))
bind("ws-consumer/019", has_valid("Product>category:CategoryCode", "inCodeSet",
                                  lambda v: text(v).strip().startswith("https://www.google.com/basepages/producttype/"),
                                  "de la taxonomía de productos de Google"))
CATEGORY_PATH = re.compile(r"^[^>]+(>[^>]+)+$")
bind("ws-consumer/020", has_valid("Product>category:CategoryCode", "codeValue",
                                  lambda v: bool(re.fullmatch(r"\d+", text(v).strip()) or CATEGORY_PATH.match(text(v).strip())),
                                  "con un ID numérico o una ruta separada por >"))
bind("ws-consumer/021", values_ok("Product>category:CategoryCode", "codeValue",
                                  lambda v: all(re.search(r"[^\W\d_]", s) for s in text(v).split(">"))
                                  if CATEGORY_PATH.match(text(v).strip()) else None,
                                  "rutas cuyos segmentos tienen alguna letra"))
GTIN_LENGTHS = re.compile(r"^(\d{8}|\d{12}|\d{13}|\d{14})$")
bind("ws-consumer/025", values_ok("Product", "gtin", lambda v: not GTIN_LENGTHS.match(text(v).strip()),
                                  "GTIN fuera de 8, 12, 13 y 14 dígitos"))


@check("ws-consumer/026")
def _gtin_numeric(case: Case) -> Result:
    pairs = [(e, p, v) for e in case.graph.of("Product") for p in ("gtin", "gtin8", "gtin12", "gtin13", "gtin14")
             for v in e.values(p)]
    if not pairs:
        return Result(NA, None, "Ninguna entidad Product tiene gtin, gtin8, gtin12, gtin13 ni gtin14.")
    bad = [f"{label(e)}: {p} = {text(v)!r}" for e, p, v in pairs if not re.fullmatch(r"\d+", text(v).strip())]
    return _result(bad, len(pairs), [], "que no son solo dígitos")


bind("ws-consumer/027", each("Product", lambda e: any(vocab.load().is_a(t, "Book") for t in e.types),
                             "con isbn y sin el tipo Book", where=lambda e: e.has("isbn")))
bind("ws-consumer/028", values_ok("Product", "isbn", lambda v: bool(re.fullmatch(r"\d{13}", re.sub(r"[-\s]", "", text(v)))),
                                  "ISBN-13"))


@check("ws-consumer/029")
def _adult(case: Case) -> Result:
    if not case.graph.of("Product"):
        return Result(NA, None, "El marcado no contiene ninguna entidad Product.")
    return Result(NE, None, "Determinar si el producto es de orientación adulta exige aplicar la política de Google, "
                            "que no está en la referencia técnica.")


bind("ws-consumer/030", enum("Product", "hasAdultConsideration", {"SexualContentConsideration"}))


# --- Variants --------------------------------------------------------------------------------

def variants(group: Entity) -> list[Entity]:
    """Product entities (not ProductGroup) that are values of its hasVariant or whose isVariantOf
    is the group; the same node counts once."""
    out = [v for v in group.values("hasVariant") if is_type(v, "Product")]
    out += [p for p, prop in group.parents if prop == "isVariantOf" and is_type(p, "Product")]
    seen, unique = set(), []
    for v in out:
        if id(v) not in seen:
            seen.add(id(v))
            unique.append(v)
    return unique


def variant_products(case: Case) -> list[Entity]:
    """Products that are variants: in a group, or with isVariantOf or inProductGroupWithID."""
    out = [v for g in case.graph.of("ProductGroup") for v in variants(g)]
    out += [p for p in case.graph.of("Product") if p.has("isVariantOf") or p.has("inProductGroupWithID")]
    return list({id(p): p for p in out}.values())


def _variant_property(prop: str, req_text: str):
    def run(case: Case) -> Result:
        products = case.graph.of("Product")
        marked = bool(case.graph.of("ProductGroup")) or any(p.has("isVariantOf") or p.has("inProductGroupWithID")
                                                            for p in products)
        if marked:
            vs = variant_products(case)
            if prop == "isVariantOf":
                bad = [label(v) + (" (solo es valor de hasVariant)" if any(pr == "hasVariant" for _, pr in v.parents) else "")
                       for v in vs if not any(is_type(g, "ProductGroup") or isinstance(g, Ref) for g in v.values(prop))]
            else:
                bad = [label(v) for v in vs if not v.has(prop)]
            return _result(bad, len(vs), [], f"sin {prop}")
        if not products:
            return Result(NA, None, "El marcado no contiene ninguna entidad Product.")
        return Result(PENDING, {"Product": capped(label(p) for p in products)},
                      "El marcado no tiene ProductGroup, isVariantOf ni inProductGroupWithID. ¿Ofrece la página elegir "
                      "entre dos o más valores de talla, color u otra dimensión del producto (un selector con un solo "
                      f"valor no cuenta)? Si no, NA. Si sí, el producto es una variante: {req_text}")
    return run


bind("ws-consumer/032", _variant_property("inProductGroupWithID", "no satisfecho si su Product no tiene inProductGroupWithID."))
bind("ws-consumer/034", _variant_property("isVariantOf", "no satisfecho si su Product no tiene isVariantOf con una ProductGroup."))
bind("ws-consumer/033", at_most_one("Product", "inProductGroupWithID"))


def _review_authors(path: str):
    """Code decides what it can: a review without author name is not satisfied; the names, to
    judge whether each is a person's or a team's, go to the agent."""
    def run(case: Case) -> Result:
        reviews = select(case, path).entities
        if not reviews:
            return Result(NA, None, f"El marcado no contiene Review en {path}.")
        names, bad = [], []
        for r in reviews:
            authors = r.values("author")
            found = [name_of(a) for a in authors if name_of(a)]
            if not found:
                bad.append(f"{label(r)}: author sin nombre")
            names += found
        if bad:
            return Result(UNSAT, {"examinadas": len(reviews), "sin nombre de autor": capped(bad)})
        return Result(PENDING, {"autores": capped(dict.fromkeys(names))},
                      "¿Es cada nombre de autor el de una persona o de un equipo u organización, y no un texto de otra "
                      "clase (una promoción, un eslogan, una fecha o el nombre del producto)? Satisfecho si lo son todos.")
    return run


bind("ws-consumer/039", _review_authors("Product>review:Review"))
bind("ws-consumer/156", _review_authors("Product>review:Review"))
bind("ws-consumer/350", _review_authors("@valued>review:Review"))

bind("ws-consumer/041", at_most_one("Product", "size"))
bind("ws-consumer/043", at_most_one("Product", "sku"))


def _valid_unicode(s: str) -> bool:
    for ch in s:
        cp = ord(ch)
        if unicodedata.category(ch) == "Cc" or 0xD800 <= cp <= 0xDFFF or (0xFDD0 <= cp <= 0xFDEF) or (cp & 0xFFFE) == 0xFFFE:
            return False
    return True


bind("ws-consumer/044", values_ok("Product", "sku", lambda v: _valid_unicode(text(v)), "caracteres Unicode válidos"))
bind("ws-consumer/045", values_ok("Product", "sku", lambda v: not re.search(r"\s", text(v)), "sin espacio en blanco"))
bind("ws-consumer/046", values_ok("Product", "sku", lambda v: text(v).isascii(), "solo ASCII"))


def _models(e: Entity) -> list:
    return [v for v in e.values("subjectOf") if is_type(v, "3DModel")]


bind("ws-consumer/048", each("Product", lambda e: len(_models(e)) <= 1, "con más de un 3DModel en subjectOf",
                             where=lambda e: bool(_models(e))))
bind("ws-consumer/049", has("3DModel", "encoding"))
bind("ws-consumer/050", has("3DModel>encoding", "contentUrl"))
bind("ws-consumer/051", values_ok("3DModel>encoding", "contentUrl",
                                  lambda v: urlsplit(text(v).strip()).path.lower().endswith((".gltf", ".glb")),
                                  "URL que terminan en .gltf o .glb"))


# --- Offer and prices ---------------------------------------------------------------------------

def active_price(offer: Entity) -> list[tuple]:
    """(price value, entity that holds it): price in the Offer, or in a priceSpecification without
    priceType or validForMemberTier."""
    out = [(v, offer) for v in offer.values("price")]
    for spec in offer.values("priceSpecification"):
        if isinstance(spec, Entity) and not spec.has("priceType") and not spec.has("validForMemberTier"):
            out += [(v, spec) for v in spec.values("price")]
    return out


bind("ws-consumer/052", each("Offer", lambda e: bool(active_price(e)), "sin precio activo"))
PRICE = re.compile(r"^\d+(\.\d+)?$")


@check("ws-consumer/053")
def _price_positive(case: Case) -> Result:
    pairs = [(o, v) for o in case.graph.of("Offer") for v, _ in active_price(o)]
    if not pairs:
        return Result(NA, None, "Ninguna Offer tiene precio activo.")

    def ok(v):
        s = text(v).strip()
        return bool(PRICE.match(s)) and float(s) > 0
    bad = [f"{label(o)}: {text(v)!r}" for o, v in pairs if not ok(v)]
    return _result(bad, len(pairs), [], "que no son un número mayor que cero con punto decimal")


@check("ws-consumer/054")
def _currency_with_price(case: Case) -> Result:
    offers = [o for o in case.graph.of("Offer") if active_price(o)]
    if not offers:
        return Result(NA, None, "Ninguna Offer tiene precio activo.")
    bad = [label(o) for o in offers if not all(holder.has("priceCurrency") for _, holder in active_price(o))]
    return _result(bad, len(offers), [], "sin la moneda junto al precio activo")


bind("ws-consumer/055", values_ok("Offer|Offer>priceSpecification", "priceCurrency", currency, "códigos ISO 4217"))
bind("ws-consumer/162", values_ok("Offer|Offer>priceSpecification", "priceCurrency", currency, "códigos ISO 4217"))
AVAILABILITY = {"BackOrder", "Discontinued", "InStock", "InStoreOnly", "LimitedAvailability", "OnlineOnly",
                "OutOfStock", "PreOrder", "PreSale", "SoldOut"}
bind("ws-consumer/057", enum("Offer", "availability", AVAILABILITY))
bind("ws-consumer/159", enum("Offer", "availability", AVAILABILITY))
bind("ws-consumer/058", at_most_one("Offer", "availability"))
bind("ws-consumer/160", at_most_one("Offer", "availability"))
bind("ws-consumer/061", enum("Offer", "itemCondition", {"NewCondition", "RefurbishedCondition", "UsedCondition"}))
bind("ws-consumer/062", at_most_one("Offer", "itemCondition"))
bind("ws-consumer/064", values_ok("Offer", "priceValidUntil", iso_date_or_datetime, "fechas ISO 8601"))
bind("ws-consumer/164", values_ok("Offer", "priceValidUntil", iso_date_or_datetime, "fechas ISO 8601"))
bind("ws-consumer/066", has("Offer", "url"))
bind("ws-consumer/067", at_most_one("Offer", "url"))
bind("ws-consumer/070", values_ok("Offer|UnitPriceSpecification", "validFrom", iso_date_or_datetime, "fechas ISO 8601"))
bind("ws-consumer/071", values_ok("Offer|UnitPriceSpecification", "validThrough", iso_date_or_datetime, "fechas ISO 8601"))


@check("ws-consumer/072")
def _sale_dates(case: Case) -> Result:
    pairs = []
    for o in case.graph.of("Offer"):
        specs = [s for s in o.values("priceSpecification") if isinstance(s, Entity)]
        if not any("StrikethroughPrice" == enum_name(t) for s in specs for t in s.values("priceType")):
            continue
        for holder in [o] + specs:
            for p in ("validFrom", "validThrough", "priceValidUntil"):
                pairs += [(holder, p, v) for v in holder.values(p)]
    if not pairs:
        return Result(NA, None, "Ninguna Offer con precio de rebaja (priceType StrikethroughPrice) tiene validFrom, "
                                "validThrough ni priceValidUntil.")
    bad = [f"{label(h)}: {p} = {text(v)!r}" for h, p, v in pairs if not iso_datetime_with_zone(v)]
    return _result(bad, len(pairs), [], "sin hora y zona horaria")


bind("ws-consumer/073", not_both("Offer>priceSpecification", "priceType", "validForMemberTier"))
bind("ws-consumer/074", has("UnitPriceSpecification", "price"))
bind("ws-consumer/165", has("UnitPriceSpecification", "price"))
bind("ws-consumer/075", has("UnitPriceSpecification", "priceCurrency"))
bind("ws-consumer/166", has("UnitPriceSpecification", "priceCurrency"))
bind("ws-consumer/077", has("UnitPriceSpecification", "validForMemberTier", where=lambda e: e.has("membershipPointsEarned")))


def _offer_with_spec(prop: str):
    return lambda o: any(is_type(s, "UnitPriceSpecification") and s.has(prop) for s in o.values("priceSpecification"))


def _visible(question: str, needs=None):
    """A requirement whose applicability is what the page shows: the agent reads the page."""
    def run(case: Case) -> Result:
        if needs is not None:
            na = needs(case)
            if na:
                return Result(NA, None, na)
        return Result(PENDING, None, question)
    return run


def _no(path: str, what: str):
    return lambda case: None if select(case, path).entities else f"El marcado no contiene {what}."


bind("ws-consumer/078", _visible(
    "¿Muestra la página, para el producto de la página, un precio anterior o de referencia junto al precio actual "
    "(tachado, «antes», «PVP» o con un porcentaje de descuento)? Si no, NA. Si sí: satisfecho si la Offer del "
    "producto tiene una UnitPriceSpecification con priceType (el precio original); si no, no satisfecho."))
bind("ws-consumer/079", enum("UnitPriceSpecification", "priceType", {"StrikethroughPrice"}))
bind("ws-consumer/080", each("Offer", lambda o: bool(active_price(o)), "sin precio activo", where=_offer_with_spec("priceType")))
bind("ws-consumer/081", _visible(
    "¿Muestra la página, para el producto de una Offer del marcado, un precio por unidad de medida de cantidad "
    "(por kilo, litro, metro u otra; no por pieza o unidad de venta)? Si no, NA. Si sí: satisfecho si esa Offer tiene "
    "una UnitPriceSpecification con referenceQuantity; si no, no satisfecho.", _no("Offer", "ninguna Offer")))
bind("ws-consumer/082", _visible(
    "¿Muestra la página un precio para miembros de un programa de fidelización? Si no, NA. Si sí: satisfecho si "
    "cada precio para miembros está en una UnitPriceSpecification con validForMemberTier; si no, no satisfecho."))
bind("ws-consumer/083", each("Offer", lambda o: bool(active_price(o)), "sin precio activo",
                             where=_offer_with_spec("validForMemberTier")))
bind("ws-consumer/086", has("UnitPriceSpecification>referenceQuantity", "unitCode"))
bind("ws-consumer/087", has("UnitPriceSpecification>referenceQuantity", "value"))
bind("ws-consumer/088", has("UnitPriceSpecification>referenceQuantity", "valueReference"))
bind("ws-consumer/090", _visible(
    "¿Indica la página un grupo de tallas de prenda del producto (regular, petite, plus, tall, big o maternity; las "
    "medidas y las tallas S/M/L no lo son)? Si no, NA. Si sí: satisfecho si cada SizeSpecification tiene sizeGroup.",
    _no("SizeSpecification", "ninguna SizeSpecification")))
bind("ws-consumer/091", _visible(
    "¿Indica la página el sistema de tallas del producto (europeo, francés, italiano, británico u otro)? Si no, NA. "
    "Si sí: satisfecho si cada SizeSpecification tiene sizeSystem.", _no("SizeSpecification", "ninguna SizeSpecification")))


def _members(enumeration: str) -> set[str]:
    voc = vocab.load()
    return {m for m, types in voc.members.items() if any(voc.is_a(t, enumeration) for t in types)}


bind("ws-consumer/092", enum("SizeSpecification", "sizeGroup", _members("WearableSizeGroupEnumeration")))
bind("ws-consumer/093", enum("SizeSpecification", "sizeSystem", _members("WearableSizeSystemEnumeration")))
bind("ws-consumer/095", values_ok("PeopleAudience", "suggestedGender",
                                  lambda v: enum_name(v).casefold() in ("male", "female", "unisex"),
                                  "Male, Female o Unisex"))
CERT_ISSUERS = {"EC", "European_Commission", "ADEME", "BMWK"}
EU_ISSUERS = {"EC", "European_Commission"}


def _issuers(cert: Entity) -> list[str]:
    return [name_of(v) for v in cert.values("issuedBy") if isinstance(v, Entity)]


bind("ws-consumer/098", each("Certification", lambda c: any(n in CERT_ISSUERS for n in _issuers(c)),
                             "sin issuedBy con un nombre que admite Google"))
bind("ws-consumer/099", each("Certification", lambda c: any(text(n).strip() in ("EPREL", "Vehicle_CO2_Class",
                                                                                  "Vehicle_CO2_Class_Discharged_Battery")
                                                            for n in c.values("name")),
                             "sin un name que admite Google"))
bind("ws-consumer/100", has("Certification", "certificationIdentification",
                            where=lambda c: any(text(n).strip() == "EPREL" for n in c.values("name"))))
bind("ws-consumer/102", has("Certification>certificationRating", "ratingValue"))


def _eu_ratings(prop: str):
    def run(case: Case) -> Result:
        ratings = [r for c in case.graph.of("Certification") if any(n in EU_ISSUERS for n in _issuers(c))
                   for r in c.values("certificationRating") if isinstance(r, Entity)]
        if not ratings:
            return Result(NA, None, "Ninguna Certification de la UE (issuedBy EC o European_Commission) tiene certificationRating.")
        bad = [label(r) for r in ratings if not r.has(prop)]
        return _result(bad, len(ratings), [], f"sin {prop}")
    return run


bind("ws-consumer/103", _eu_ratings("bestRating"))
bind("ws-consumer/104", _eu_ratings("worstRating"))

# --- Shipping details of the offer ------------------------------------------------------------

OSD = "OfferShippingDetails"
bind("ws-consumer/105", has(OSD, "deliveryTime"))
bind("ws-consumer/106", at_most_one(OSD, "deliveryTime"))
bind("ws-consumer/107", has(OSD, "shippingDestination"))
bind("ws-consumer/108", has(OSD, "shippingRate"))
bind("ws-consumer/109", at_most_one(OSD, "shippingRate"))
bind("ws-consumer/110", has(f"{OSD}>shippingRate", "currency"))
bind("ws-consumer/111", values_ok(f"{OSD}>shippingRate", "currency", currency, "códigos ISO 4217"))


@check("ws-consumer/112")
def _shipping_currency(case: Case) -> Result:
    pairs = []
    for o in case.graph.of("Offer"):
        currencies = {text(v).strip() for _, h in active_price(o) for v in h.values("priceCurrency")}
        for d in o.values("shippingDetails"):
            if isinstance(d, Entity):
                for rate in d.values("shippingRate"):
                    if isinstance(rate, Entity):
                        pairs += [(o, currencies, text(c).strip()) for c in rate.values("currency")]
    pairs = [p for p in pairs if p[1]]
    if not pairs:
        return Result(NA, None, "Ninguna Offer con moneda tiene una OfferShippingDetails con shippingRate.currency.")
    bad = [f"{label(o)}: envío {c} y precio {', '.join(sorted(cs))}" for o, cs, c in pairs if c not in cs]
    return _result(bad, len(pairs), [], "con otra moneda")


bind("ws-consumer/113", has(f"{OSD}>shippingRate", "value", "maxValue"))
def _rate_text(test, describe):
    def run(case: Case) -> Result:
        pairs = [(e, p, v) for e in select(case, f"{OSD}>shippingRate").entities for p in ("value", "maxValue")
                 for v in e.values(p) if string_literal(v)]
        if not pairs:
            return Result(NA, None, "Ningún shippingRate.value ni shippingRate.maxValue se da como texto.")
        bad = [f"{label(e)}: {p} = {text(v)!r}" for e, p, v in pairs if not test(text(v))]
        return _result(bad, len(pairs), [], describe)
    return run


def _no_currency(s: str) -> bool:
    from references.read import currency_codes
    if any(unicodedata.category(ch) == "Sc" for ch in s):
        return False
    return not any(w.upper() in currency_codes() for w in re.findall(r"[A-Za-z]{3}", s))


bind("ws-consumer/114", _rate_text(_no_currency, "con símbolo o código de moneda"))
def _no_thousands(s: str) -> bool:
    """A point, a comma or a space grouping digits by three before the decimal separator. A single
    point before three digits (1.500) is the decimal point that Google expects, not a group."""
    s = s.strip()
    return not (re.fullmatch(r"\d{1,3}([ ,\u00a0]\d{3})+(\.\d+)?", s) or re.fullmatch(r"\d{1,3}(\.\d{3})+,\d+", s)
                or re.fullmatch(r"\d{1,3}(\.\d{3}){2,}", s))


bind("ws-consumer/115", _rate_text(_no_thousands, "con separadores de miles"))
bind("ws-consumer/116", _rate_text(lambda s: " " not in s and not re.search(r"\s", s), "con espacios"))
bind("ws-consumer/117", has("DefinedRegion", "addressCountry"))
bind("ws-consumer/118", values_ok("DefinedRegion", "addressCountry", country, "códigos ISO 3166-1 alfa-2"))
bind("ws-consumer/119", _visible(
    "¿Publica la página (o la política de envíos enlazada) condiciones de envío distintas para partes de un país "
    "(regiones o códigos postales)? Si no, NA. Si sí: satisfecho si cada DefinedRegion de una zona menor que un país "
    "tiene addressRegion o postalCode.", _no("DefinedRegion", "ninguna DefinedRegion")))
bind("ws-consumer/120", not_both("DefinedRegion", "addressRegion", "postalCode"))


def _subdivision(v) -> bool:
    s = text(v).strip()
    return bool(re.fullmatch(r"[A-Za-z0-9]{2,3}", s))


bind("ws-consumer/121", values_ok("DefinedRegion", "addressRegion", _subdivision,
                                  "códigos ISO 3166-2 de 2 o 3 caracteres sin prefijo de país"))
TIMES = "*>handlingTime:QuantitativeValue|*>transitTime:QuantitativeValue"
bind("ws-consumer/124", has(TIMES, "minValue"))
bind("ws-consumer/125", has(TIMES, "maxValue"))
bind("ws-consumer/126", values_ok(TIMES, "minValue", non_negative_integer, "enteros no negativos"))
bind("ws-consumer/127", values_ok(TIMES, "maxValue", non_negative_integer, "enteros no negativos"))
bind("ws-consumer/128", has(TIMES, "unitCode"))
DAYS = lambda v: text(v).strip() in ("DAY", "d")  # noqa: E731
bind("ws-consumer/129", values_ok(TIMES, "unitCode", DAYS, "DAY o d"))

# --- Return policy of the offer -----------------------------------------------------------------

MRP = "MerchantReturnPolicy"
OFFER_MRP = f"Offer>hasMerchantReturnPolicy:{MRP}"
CATEGORIES = {"MerchantReturnFiniteReturnWindow", "MerchantReturnNotPermitted", "MerchantReturnUnlimitedWindow"}
FEES = {"FreeReturn", "ReturnFeesCustomerResponsibility", "ReturnShippingFees"}
METHODS = {"ReturnAtKiosk", "ReturnByMail", "ReturnInStore"}
LABELS = {"ReturnLabelCustomerResponsibility", "ReturnLabelDownloadAndPrint", "ReturnLabelInBox"}
FINITE = prop_is("returnPolicyCategory", "MerchantReturnFiniteReturnWindow")
bind("ws-consumer/130", has(OFFER_MRP, "applicableCountry"))
bind("ws-consumer/131", values_ok(MRP, "applicableCountry", country, "códigos ISO 3166-1 alfa-2"))
bind("ws-consumer/132", has(OFFER_MRP, "returnPolicyCategory"))
bind("ws-consumer/133", enum(MRP, "returnPolicyCategory", CATEGORIES))
bind("ws-consumer/134", has(MRP, "merchantReturnDays", where=FINITE))
bind("ws-consumer/136", enum(MRP, "returnFees", FEES))
bind("ws-consumer/137", none_has(MRP, "returnShippingFeesAmount", where=prop_is("returnFees", "FreeReturn")))
bind("ws-consumer/138", none_has(MRP, "returnShippingFeesAmount", where=prop_is("returnFees", "ReturnFeesCustomerResponsibility")))
bind("ws-consumer/139", has(MRP, "returnShippingFeesAmount", where=prop_is("returnFees", "ReturnShippingFees")))


def amount(v) -> float | None:
    """The value (or maxValue) of a MonetaryAmount, or a number given directly."""
    if isinstance(v, Entity):
        for p in ("value", "maxValue"):
            for x in v.values(p):
                n = number(x)
                if n is not None:
                    return n
        return None
    return number(v)


def _nonzero_fee(e: Entity) -> bool:
    return any(amount(v) not in (0, None) for v in e.values("returnShippingFeesAmount"))


bind("ws-consumer/140", each(MRP, prop_is("returnFees", "ReturnShippingFees"), "sin returnFees ReturnShippingFees",
                             where=_nonzero_fee))
bind("ws-consumer/144", enum(MRP, "returnMethod", METHODS))


def _single_currency(case: Case) -> Result:
    found = []
    for o in case.graph.of("Offer") + case.graph.of("AggregateOffer"):
        for holder in [o] + [s for s in o.values("priceSpecification") if isinstance(s, Entity)]:
            found += [(holder, text(v).strip()) for v in holder.values("priceCurrency")]
    if not found:
        return Result(NA, None, "Ninguna Offer ni AggregateOffer tiene moneda.")
    values = sorted({c for _, c in found})
    ev = {"monedas": values, "examinadas": len(found)}
    return Result(SAT if len(values) == 1 else UNSAT, ev)


bind("ws-consumer/147", _single_currency)
bind("ws-consumer/174", _single_currency)


def _car_is_product(case: Case) -> Result:
    cars = [e for e in case.graph.entities if "Car" in e.types and (e.has("review") or e.has("aggregateRating"))]
    if not cars:
        return Result(NA, None, "Ninguna entidad Car tiene review ni aggregateRating.")
    bad = [label(e) for e in cars if "Product" not in e.types]
    return _result(bad, len(cars), [], "sin el tipo Product")


bind("ws-consumer/148", _car_is_product)
bind("ws-consumer/175", _car_is_product)


def _served_vs_rendered(case: Case) -> Result:
    return Result(NE, {"Product en el HTML servido": len(case.graph.of("Product")) + len(case.graph.of("ProductGroup"))},
                  RENDERED_NE)


bind("ws-consumer/149", _served_vs_rendered)
bind("ws-consumer/176", _served_vs_rendered)
bind("ws-consumer/157", each("Offer", lambda o: o.has("price") or any(isinstance(s, Entity) and s.has("price")
                                                                        for s in o.values("priceSpecification")),
                             "sin price ni priceSpecification.price"))
bind("ws-consumer/161", each("Offer", lambda o: o.has("priceCurrency") or any(isinstance(s, Entity) and s.has("priceCurrency")
                                                                                for s in o.values("priceSpecification")),
                             "sin priceCurrency ni priceSpecification.priceCurrency"))
bind("ws-consumer/167", has("AggregateOffer", "lowPrice"))
bind("ws-consumer/168", values_ok("AggregateOffer", "lowPrice",
                                  lambda v: True if isinstance(v, Lit) and isinstance(v.value, (int, float)) else "," not in text(v),
                                  "con punto decimal"))
bind("ws-consumer/169", has("AggregateOffer", "priceCurrency"))
bind("ws-consumer/170", values_ok("AggregateOffer", "priceCurrency", currency, "códigos ISO 4217"))


def _keys(p: Entity) -> set:
    keys = set()
    if p.id:
        keys.add(("id", p.id))
    for prop in ("url", "sku", "gtin", "gtin8", "gtin12", "gtin13", "gtin14", "mpn", "productID", "name"):
        for v in p.values(prop):
            t = text(v).strip()
            if t:
                keys.add((prop, urldefrag(t)[0] if prop == "url" else t.casefold()))
    return keys


def _groups(p: Entity) -> set:
    out = {("pg", id(g)) for g in p.values("isVariantOf") if isinstance(g, Entity)}
    out |= {("pg", id(g)) for g, prop in p.parents if prop == "hasVariant"}
    out |= {("pgid", text(v).strip()) for v in p.values("inProductGroupWithID") if text(v).strip()}
    return out


@check("ws-consumer/173")
def _single_product(case: Case) -> Result:
    products = case.graph.of("Product") + case.graph.of("ProductGroup")
    if not products:
        return Result(NA, None, "El marcado no contiene ninguna entidad Product.")
    # one cluster per product: the same identifier, URL, code or name, or the same group
    clusters: list[tuple[set, list]] = []
    for p in products:
        keys = _keys(p) | _groups(p) | ({("pg", id(p))} if is_type(p, "ProductGroup") else set())
        joined = [c for c in clusters if c[0] & keys]
        merged = (keys.union(*(c[0] for c in joined)), [p] + [x for c in joined for x in c[1]])
        clusters = [c for c in clusters if c not in joined] + [merged]
    ev = {"productos distintos": len(clusters),
          "productos": capped(" · ".join(label(x) for x in c[1][:3]) for c in clusters)}
    return Result(SAT if len(clusters) == 1 else UNSAT, ev)


@check("ws-consumer/177")
def _has_markup(case: Case) -> Result:
    found = case.page.syntaxes
    if found:
        return Result(SAT, found)
    return Result(NE, {"HTML servido": "sin marcado"},
                  "No se encuentra marcado en el HTML servido y no se dispone del DOM renderizado (perfil audit-es).")


@check("ws-consumer/178")
def _all_jsonld(case: Case) -> Result:
    tops = [e for e in case.graph.entities if e.top and any(vocab.load().is_class(t) for t in e.types)]
    if not tops:
        return Result(NA, None, "La página no contiene datos estructurados con Schema.org.")
    bad = [label(e) for e in tops if e.syntax != "json-ld"]
    return _result(bad, len(tops), [], "en Microdata o RDFa")


@check("ws-consumer/179")
def _robots_googlebot(case: Case) -> Result:
    from .web import robots_case
    return robots_case(case, "googlebot", reader="consumer")


@check("ws-consumer/180")
def _noindex(case: Case) -> Result:
    from .web import noindex_rules
    rules = noindex_rules(case.page, include_outside_head=True)
    if rules["noindex"]:
        return Result(UNSAT, rules)
    return Result(SAT, rules)


@check("ws-consumer/184")
def _canonical_same_markup(case: Case) -> Result:
    from .web import canonicals, same_url
    links = canonicals(case.page)
    targets = [u for u, _ in links]
    if not targets:
        return Result(NA, None, "La página no declara URL canónica.")
    others = [u for u in targets if not same_url(u, urldefrag(case.page.url_final)[0])]
    if not others:
        return Result(NA, None, "La URL canónica es la de la propia página.")
    in_audit = [p for p in case.site.pages if p.captured and any(same_url(p.url_final, u) for u in others)]
    if not in_audit:
        return Result(NE, {"canónica": others, "URL final": case.page.url_final}, "No se puede obtener la página canónica: "
                      "la auditoría no la ha capturado.")
    mine = sorted((tuple(sorted(e.types)), tuple(sorted(e.props))) for e in case.graph.entities)
    theirs = sorted((tuple(sorted(e.types)), tuple(sorted(e.props))) for e in in_audit[0].graph.entities)
    ev = {"canónica": others, "página canónica": in_audit[0].id}
    return Result(SAT if mine == theirs else UNSAT, ev)


# --- ProductGroup ---------------------------------------------------------------------------

PG = "ProductGroup"
IDENTIFIERS = ("sku", "gtin", "gtin8", "gtin12", "gtin13", "gtin14", "mpn", "productID")
bind("ws-consumer/187", has(PG, "name"))


@check("ws-consumer/190")
def _pg_brand_name(case: Case) -> Result:
    pairs = [(g, b) for g in case.graph.of(PG) for b in g.values("brand")]
    if not pairs:
        return Result(NA, None, "Ninguna ProductGroup tiene brand.")
    bad = [f"{label(g)}: brand {label(b)}" for g, b in pairs
           if not isinstance(b, Ref) and not (isinstance(b, Entity) and b.has("name"))]
    return _result(bad, len(pairs), [b for _, b in pairs if isinstance(b, Ref)], "sin name")


@check("ws-consumer/192")
def _pg_has_variants(case: Case) -> Result:
    groups = case.graph.of(PG)
    if not groups:
        return Result(NA, None, "El marcado no contiene ninguna ProductGroup.")
    empty = [g for g in groups if not variants(g)]
    if not empty:
        return Result(SAT, {"grupos": capped(f"{label(g)}: {len(variants(g))} variantes" for g in groups)})
    return Result(PENDING, {"grupos sin variantes": capped(label(g) for g in empty)},
                  "¿Muestra la página variantes del producto (un selector de talla, color u otro aspecto con dos o más "
                  "opciones)? Si no, NA. Si sí, no satisfecho: hay ProductGroup sin ninguna variante Product enlazada.")


def _pg_with_variants(case: Case) -> list:
    return [(g, variants(g)) for g in case.graph.of(PG)]


@check("ws-consumer/193")
def _pg_id(case: Case) -> Result:
    groups = _pg_with_variants(case)
    if not groups:
        return Result(NA, None, "El marcado no contiene ninguna ProductGroup.")
    bad = [label(g) for g, vs in groups
           if not g.has("productGroupID") and not (vs and all(v.has("inProductGroupWithID") for v in vs))]
    variants_spelling = [label(e) for e in case.graph.entities if e.has("productGroupId") or e.has("inProductGroupWithId")]
    return _result(bad, len(groups), [], "sin productGroupID ni inProductGroupWithID en todas sus variantes",
                   {"otra grafía (no cuenta)": capped(variants_spelling)} if variants_spelling else None)


@check("ws-consumer/194")
def _pg_id_match(case: Case) -> Result:
    pairs = []
    for g, vs in _pg_with_variants(case):
        ids = {text(v).strip() for v in g.values("productGroupID")}
        if ids:
            pairs += [(g, v, text(x).strip(), ids) for v in vs for x in v.values("inProductGroupWithID")]
    if not pairs:
        return Result(NA, None, "Ninguna ProductGroup con productGroupID tiene variantes con inProductGroupWithID.")
    bad = [f"{label(v)}: {x!r} frente a {sorted(ids)}" for g, v, x, ids in pairs if x not in ids]
    return _result(bad, len(pairs), [], "que no coinciden")


def _real_variants(vs: list) -> list:
    """Variants that are not just a url (links to variants of another page)."""
    return [v for v in vs if set(v.props) - {"url"}]


@check("ws-consumer/195")
def _variant_identifier(case: Case) -> Result:
    vs = [v for _, x in _pg_with_variants(case) for v in _real_variants(x)]
    if not vs:
        return Result(NA, None, "Ninguna variante de una ProductGroup se reduce a algo más que un url.")
    bad = [label(v) for v in vs if not any(v.has(p) for p in IDENTIFIERS)]
    return _result(bad, len(vs), [], "sin identificador")


@check("ws-consumer/196")
def _variant_identifier_unique(case: Case) -> Result:
    groups = [(g, [v for v in _real_variants(vs) if any(v.has(p) for p in IDENTIFIERS)]) for g, vs in _pg_with_variants(case)]
    groups = [(g, vs) for g, vs in groups if len(vs) >= 2]
    if not groups:
        return Result(NA, None, "Ninguna ProductGroup tiene dos o más variantes con identificador.")
    bad = []
    for g, vs in groups:
        for p in IDENTIFIERS:
            seen = {}
            for v in vs:
                for x in v.values(p):
                    t = text(x).strip()
                    if t and t in seen and seen[t] is not v:
                        bad.append(f"{label(g)}: {p} {t!r} repetido")
                    seen.setdefault(t, v)
    return _result(bad, len(groups), [], "con identificadores repetidos")


@check("ws-consumer/197")
def _pg_has_product(case: Case) -> Result:
    if not case.graph.of(PG):
        return Result(NA, None, "El marcado no contiene ninguna ProductGroup.")
    products = case.graph.of("Product")
    return Result(SAT if products else UNSAT, {"Product": capped(label(p) for p in products)})


def variant_url(v: Entity) -> str | None:
    for x in v.values("url"):
        if text(x).strip():
            return text(x).strip()
    for o in v.values("offers"):
        if isinstance(o, Entity):
            for x in o.values("url"):
                if text(x).strip():
                    return text(x).strip()
    return None


def site_kind(case: Case, group: Entity) -> str | None:
    """single (variant URLs share the path of the page and differ in the query), multi (some
    variant URL has another path) or None when a variant gives no URL."""
    urls = [variant_url(v) for v in variants(group)]
    if not urls or any(u is None for u in urls):
        return None
    page_path = urlsplit(case.page.url_final).path
    return "single" if all(urlsplit(u).path == page_path for u in urls) else "multi"


NO_URL = "Las variantes no declaran URL en el marcado, de modo que no se puede saber si el sitio es de una o de varias páginas."


def _by_site_kind(kind: str, fn, na: str):
    def run(case: Case) -> Result:
        groups = case.graph.of(PG)
        if not groups:
            return Result(NA, None, "El marcado no contiene ninguna ProductGroup.")
        kinds = [(g, site_kind(case, g)) for g in groups]
        mine = [g for g, k in kinds if k == kind]
        if not mine:
            if any(k is None for _, k in kinds):
                return Result(NE, {"grupos": capped(label(g) for g, _ in kinds)}, NO_URL)
            return Result(NA, None, na)
        return fn(case, mine)
    return run


def _single_canonical(case: Case, groups) -> Result:
    urls = [variant_url(v) for g in groups for v in variants(g)]
    return Result(NE, {"URL de variante": capped(urls)}, "Hay que obtener las páginas de las URL de variante.")


bind("ws-consumer/198", _by_site_kind("single", _single_canonical, "Ninguna ProductGroup es de un sitio de una sola página."))


def _defined_refs(case: Case, groups) -> Result:
    refs = []

    def walk(e: Entity, seen):
        for vs in e.props.values():
            for v in vs:
                if isinstance(v, Ref):
                    refs.append(f"{label(e)} → {v.id}")
                elif isinstance(v, Entity) and id(v) not in seen:
                    seen.add(id(v))
                    walk(v, seen)
    for g in groups:
        seen = {id(g)}
        walk(g, seen)
        for v in variants(g):
            if id(v) not in seen:
                seen.add(id(v))
                walk(v, seen)
    return Result(UNSAT if refs else SAT, {"referencias sin definir": capped(refs)})


bind("ws-consumer/199", _by_site_kind("multi", _defined_refs, "Ninguna ProductGroup es de un sitio de varias páginas."))


@check("ws-consumer/200")
def _variant_urls_distinct(case: Case) -> Result:
    groups = [(g, vs) for g, vs in _pg_with_variants(case) if len(vs) >= 2]
    if not groups:
        return Result(NA, None, "Ninguna ProductGroup tiene dos o más variantes.")
    bad, missing = [], []
    for g, vs in groups:
        urls = [variant_url(v) for v in vs]
        missing += [label(v) for v, u in zip(vs, urls) if u is None]
        known = [u for u in urls if u]
        bad += [f"{label(g)}: {u}" for u in sorted(set(known)) if known.count(u) > 1]
    if bad:
        return Result(UNSAT, {"URL repetidas": capped(bad)})
    if missing:
        return Result(NE, {"variantes sin URL": capped(missing)}, "Alguna variante no declara URL en el marcado y el "
                      "selector de variantes no está en el marcado.")
    return Result(SAT, {"grupos": len(groups)})


@check("ws-consumer/201")
def _variants_served(case: Case) -> Result:
    groups = case.graph.of(PG)
    if not groups:
        return Result(NE, None, "El HTML servido no contiene marcado de variantes: hace falta el DOM renderizado para "
                                "saber si se genera con JavaScript.")
    return Result(SAT, {"ProductGroup en el HTML servido": capped(label(g) for g in groups)})


bind("ws-consumer/202", _by_site_kind("single", lambda case, gs: _result([label(g) for g in gs if not g.has("url")],
                                                                         len(gs), [], "sin url"),
                                      "Ninguna ProductGroup es de un sitio de una sola página."))


def _group_url_selectors(case: Case, groups) -> Result:
    groups = [g for g in groups if g.has("url")]
    if not groups:
        return Result(NA, None, "Ninguna ProductGroup de un sitio de una sola página tiene url.")
    bad = []
    for g in groups:
        params = [dict(parse_qsl(urlsplit(variant_url(v)).query)) for v in variants(g)]
        keys = {k for p in params for k in p if len({q.get(k) for q in params}) > 1}
        for u in g.values("url"):
            mine = set(dict(parse_qsl(urlsplit(text(u)).query)))
            if mine & keys:
                bad.append(f"{label(g)}: {text(u)} ({', '.join(sorted(mine & keys))})")
    return _result(bad, len(groups), [], "con selectores de variante")


bind("ws-consumer/203", _by_site_kind("single", _group_url_selectors, "Ninguna ProductGroup es de un sitio de una sola página."))
bind("ws-consumer/204", _by_site_kind("multi", lambda case, gs: _result([label(g) for g in gs if g.has("url")],
                                                                        len(gs), [], "con url"),
                                      "Ninguna ProductGroup es de un sitio de varias páginas."))


@check("ws-consumer/205")
def _varies_by(case: Case) -> Result:
    groups = case.graph.of(PG)
    if not groups:
        return Result(NA, None, "El marcado no contiene ninguna ProductGroup.")
    without = [g for g in groups if not g.has("variesBy")]
    if not without:
        return Result(SAT, {"grupos": capped(label(g) for g in groups)})
    return Result(PENDING, {"grupos sin variesBy": capped(label(g) for g in without)},
                  "¿Muestra la página variantes del producto que difieren en algún aspecto (un selector de talla, color u "
                  "otro con dos o más opciones)? Si no, NA. Si sí, no satisfecho: hay ProductGroup sin variesBy.")


VARIES = re.compile(r"^https?://schema\.org/(color|size|suggestedAge|suggestedGender|material|pattern)$")
bind("ws-consumer/206", values_ok(PG, "variesBy", lambda v: bool(VARIES.match(text(v).strip())),
                                  "URL completas de Schema.org de color, size, suggestedAge, suggestedGender, material o pattern"))

# --- Organization: return policies (general view) ------------------------------------------

ORG_MRP = f"Organization>hasMerchantReturnPolicy:{MRP}"


def _owned_by(cls: str, prop: str, excluded_owner: str, what: str):
    """Each entity of `cls` that is not the value of `prop` of an `excluded_owner` is the value of
    `prop` of an Organization."""
    def run(case: Case) -> Result:
        es = [e for e in case.graph.of(cls)
              if not any(is_type(o, excluded_owner) and p == prop for o, p in e.parents)]
        if not es:
            return Result(NA, None, f"El marcado no contiene ninguna {cls} que no sea {prop} de un {excluded_owner}.")
        bad = [label(e) for e in es if not any(is_type(o, "Organization") and p == prop for o, p in e.parents)]
        return _result(bad, len(es), [], f"que no son {prop} de una Organization ({what})")
    return run


bind("ws-consumer/208", _owned_by(MRP, "hasMerchantReturnPolicy", "Offer", "política sin dueño"))
bind("ws-consumer/209", has(ORG_MRP, "applicableCountry", "merchantReturnLink"))
bind("ws-consumer/210", has(ORG_MRP, "returnPolicyCategory", "merchantReturnLink"))
bind("ws-consumer/211", values_ok(ORG_MRP, "applicableCountry", country, "códigos ISO 3166-1 alfa-2"))
bind("ws-consumer/212", enum(ORG_MRP, "returnPolicyCategory", CATEGORIES))
bind("ws-consumer/213", has(ORG_MRP, "merchantReturnDays", where=FINITE))
bind("ws-consumer/215", enum(ORG_MRP, "returnFees", FEES))
bind("ws-consumer/216", has(ORG_MRP, "returnShippingFeesAmount", where=prop_is("returnFees", "ReturnShippingFees")))
bind("ws-consumer/217", each(ORG_MRP, prop_is("returnFees", "ReturnShippingFees"), "sin returnFees ReturnShippingFees",
                             where=lambda e: e.has("returnShippingFeesAmount")))


@check("ws-consumer/218")
def _return_fee_nonzero(case: Case) -> Result:
    es = [e for e in select(case, ORG_MRP).entities
          if prop_is("returnFees", "ReturnShippingFees")(e) and e.has("returnShippingFeesAmount")]
    if not es:
        return Result(NA, None, "Ninguna MerchantReturnPolicy de una Organization con returnFees ReturnShippingFees "
                                "tiene returnShippingFeesAmount.")
    bad = [label(e) for e in es if not _nonzero_fee(e)]
    return _result(bad, len(es), [], "con importe cero o sin value ni maxValue")


bind("ws-consumer/220", enum(ORG_MRP, "returnMethod", METHODS))
bind("ws-consumer/222", enum(ORG_MRP, "customerRemorseReturnFees", FEES))
bind("ws-consumer/224", enum(ORG_MRP, "customerRemorseReturnLabelSource", LABELS))
bind("ws-consumer/225", has(ORG_MRP, "customerRemorseReturnShippingFeesAmount",
                            where=prop_is("customerRemorseReturnFees", "ReturnShippingFees")))
bind("ws-consumer/226", has(ORG_MRP, "itemDefectReturnShippingFeesAmount",
                            where=prop_is("itemDefectReturnFees", "ReturnShippingFees")))
bind("ws-consumer/228", enum(ORG_MRP, "itemCondition", {"DamagedCondition", "NewCondition", "RefurbishedCondition",
                                                       "UsedCondition"}))
bind("ws-consumer/230", enum(ORG_MRP, "itemDefectReturnFees", FEES))
bind("ws-consumer/232", enum(ORG_MRP, "itemDefectReturnLabelSource", LABELS))
bind("ws-consumer/234", enum(ORG_MRP, "refundType", {"ExchangeRefund", "FullRefund", "StoreCreditRefund"}))
bind("ws-consumer/237", enum(ORG_MRP, "returnLabelSource", LABELS))
bind("ws-consumer/239", values_ok(ORG_MRP, "returnPolicyCountry", country, "códigos ISO 3166-1 alfa-2"))
SEASONAL = f"{ORG_MRP}>returnPolicySeasonalOverride"
bind("ws-consumer/240", has(SEASONAL, "returnPolicyCategory"))
bind("ws-consumer/241", enum(SEASONAL, "returnPolicyCategory", CATEGORIES))
bind("ws-consumer/242", has(SEASONAL, "merchantReturnDays", where=FINITE))
bind("ws-consumer/243", has(SEASONAL, "startDate"))
bind("ws-consumer/244", has(SEASONAL, "endDate"))

# --- Organization: shipping services (general view) -------------------------------------------

SS = "Organization>hasShippingService:ShippingService"
SC = f"{SS}>shippingConditions"
bind("ws-consumer/245", _owned_by("ShippingService", "hasShippingService", "OfferShippingDetails", "servicio sin dueño"))
bind("ws-consumer/246", has(SS, "shippingConditions"))


def _org_services(case: Case) -> list:
    return [(o, [s for s in o.values("hasShippingService") if is_type(s, "ShippingService")])
            for o in case.graph.of("Organization")]


@check("ws-consumer/248")
def _service_names(case: Case) -> Result:
    orgs = [(o, [name_of(s).casefold() for s in ss if name_of(s)]) for o, ss in _org_services(case)]
    orgs = [(o, names) for o, names in orgs if len(names) >= 2]
    if not orgs:
        return Result(NA, None, "Ninguna Organization tiene dos o más ShippingService con name.")
    bad = [f"{label(o)}: {n!r}" for o, names in orgs for n in sorted(set(names)) if names.count(n) > 1]
    return _result(bad, len(orgs), [], "con nombres repetidos")


bind("ws-consumer/251", enum(SS, "fulfillmentType", {"FulfillmentTypeDelivery", "FulfillmentTypeCollectionPoint"}))
bind("ws-consumer/253", _visible(
    "¿Muestra alguna página del sitio un servicio de envío reservado a los miembros de un programa de fidelización? "
    "Si no, NA. Si sí: satisfecho si cada Organization tiene al menos un ShippingService con validForMemberTier.",
    _no(SS, "ningún ShippingService de una Organization")))


@check("ws-consumer/254")
def _member_service_and_other(case: Case) -> Result:
    orgs = [(o, ss) for o, ss in _org_services(case) if any(s.has("validForMemberTier") for s in ss)]
    if not orgs:
        return Result(NA, None, "Ningún ShippingService de una Organization tiene validForMemberTier.")
    bad = [label(o) for o, ss in orgs if all(s.has("validForMemberTier") for s in ss)]
    return _result(bad, len(orgs), [], "sin un ShippingService sin validForMemberTier")


HANDLING = f"{SS}>handlingTime"
bind("ws-consumer/257", has(HANDLING, "duration"))
bind("ws-consumer/258", values_ok(HANDLING, "cutoffTime", iso_time, "horas ISO 8601"))


def _durations(base: str, start: int) -> None:
    d = f"{base}>duration"
    n = start
    bind(f"ws-consumer/{n:03d}", has(d, "value", "maxValue"))
    bind(f"ws-consumer/{n + 1:03d}", has(d, "unitCode"))
    bind(f"ws-consumer/{n + 2:03d}", values_ok(d, "unitCode", DAYS, "DAY o d"))
    bind(f"ws-consumer/{n + 3:03d}", values_ok(d, "maxValue", non_negative_integer, "enteros no negativos"))
    bind(f"ws-consumer/{n + 4:03d}", values_ok(d, "minValue", non_negative_integer, "enteros no negativos"))
    bind(f"ws-consumer/{n + 5:03d}", values_ok(d, "value", non_negative_integer, "enteros no negativos"))
    bind(f"ws-consumer/{n + 6:03d}", each(d, lambda e: not e.has("minValue") and not e.has("maxValue"),
                                          "con value y minValue o maxValue", where=lambda e: e.has("value")))


_durations(HANDLING, 259)
DOES_NOT_SHIP = lambda e: any(text(v).strip().lower() == "true" for v in e.values("doesNotShip"))  # noqa: E731
bind("ws-consumer/274", none_has(SC, "shippingRate", where=DOES_NOT_SHIP))
bind("ws-consumer/276", none_has(SC, "transitTime", where=DOES_NOT_SHIP))
REGIONS = f"{SC}>shippingDestination:DefinedRegion|{SC}>shippingOrigin:DefinedRegion"
bind("ws-consumer/277", has(REGIONS, "addressCountry"))
bind("ws-consumer/278", values_ok(REGIONS, "addressCountry", country, "códigos ISO 3166-1 alfa-2"))
bind("ws-consumer/279", values_ok(REGIONS, "addressRegion", _subdivision,
                                  "códigos ISO 3166-2 de 2 o 3 caracteres sin prefijo de país"))
bind("ws-consumer/280", not_both(REGIONS, "addressRegion", "postalCode"))
TRANSIT = f"{SC}>transitTime"
bind("ws-consumer/282", has(TRANSIT, "duration"))
_durations(TRANSIT, 283)
WEIGHT_ITEMS = f"{SC}>weight|{SC}>numItems"
bind("ws-consumer/290", has(WEIGHT_ITEMS, "minValue", "maxValue"))


@check("ws-consumer/291")
def _min_below_max(case: Case) -> Result:
    es = [e for e in select(case, WEIGHT_ITEMS).entities if e.has("minValue") and e.has("maxValue")]
    if not es:
        return Result(NA, None, "Ningún weight ni numItems tiene minValue y maxValue.")
    bad = []
    for e in es:
        lo, hi = number(e.values("minValue")[0]), number(e.values("maxValue")[0])
        if lo is None or hi is None or not lo < hi:
            bad.append(f"{label(e)}: {text(e.values('minValue')[0])} / {text(e.values('maxValue')[0])}")
    return _result(bad, len(es), [], "sin minValue < maxValue")


bind("ws-consumer/292", has(f"{SC}>weight", "unitCode"))
bind("ws-consumer/293", values_ok(f"{SC}>weight", "unitCode", lambda v: text(v).strip() in ("LBR", "KGM"), "LBR o KGM"))
ORDER = f"{SC}>orderValue"
bind("ws-consumer/294", has(ORDER, "currency"))
bind("ws-consumer/295", values_ok(ORDER, "currency", currency, "códigos ISO 4217"))
bind("ws-consumer/296", has(ORDER, "minValue", "maxValue"))
RATE_MONEY = f"{SC}>shippingRate:MonetaryAmount"
bind("ws-consumer/297", has(RATE_MONEY, "currency"))
bind("ws-consumer/298", values_ok(RATE_MONEY, "currency", currency, "códigos ISO 4217"))
bind("ws-consumer/299", has(RATE_MONEY, "maxValue", "value"))
bind("ws-consumer/300", each(RATE_MONEY, lambda e: not e.has("value"), "con maxValue y value",
                             where=lambda e: e.has("maxValue")))
RATE_SETTINGS = f"{SC}>shippingRate:ShippingRateSettings"
bind("ws-consumer/301", has(RATE_SETTINGS, "orderPercentage", "weightPercentage"))
FRACTION = lambda v: (lambda n: n is not None and 0 <= n <= 1)(number(v))  # noqa: E731
bind("ws-consumer/302", values_ok(RATE_SETTINGS, "orderPercentage", FRACTION, "números entre 0 y 1"))
bind("ws-consumer/303", values_ok(RATE_SETTINGS, "weightPercentage", FRACTION, "números entre 0 y 1"))
OVERRIDE = f"{SC}>seasonalOverride"
bind("ws-consumer/304", has(OVERRIDE, "validFrom", "validThrough"))
bind("ws-consumer/305", values_ok(OVERRIDE, "validFrom", iso_date_or_datetime, "fechas ISO 8601"))
bind("ws-consumer/306", values_ok(OVERRIDE, "validThrough", iso_date_or_datetime, "fechas ISO 8601"))

# --- Organization (general view) ------------------------------------------------------------------


@check("ws-consumer/307")
def _store_type(case: Case) -> Result:
    orgs = case.graph.top_of("Organization")
    if not orgs:
        return Result(NA, None, "El marcado no contiene ninguna Organization de nivel superior.")
    voc = vocab.load()
    bad = [label(o) for o in orgs if not any(voc.is_a(t, "OnlineStore") or voc.is_a(t, "LocalBusiness") for t in o.types)]
    return _result(bad, len(orgs), [], "que no son OnlineStore ni LocalBusiness")


bind("ws-consumer/314", values_ok("^Organization>address", "addressCountry", country, "códigos ISO 3166-1 alfa-2"))
PHONE = lambda v: bool(re.match(r"^\s*(\+|00)\s*[1-9]", text(v)))  # noqa: E731
bind("ws-consumer/319", values_ok("^Organization>contactPoint", "telephone", PHONE, "teléfonos con prefijo internacional"))


def logo_urls(o: Entity) -> list[str]:
    out = []
    for v in o.values("logo"):
        if isinstance(v, Entity):
            urls = [text(u).strip() for u in v.values("contentUrl") if text(u).strip()] or \
                   [text(u).strip() for u in v.values("url") if text(u).strip()]
            out += urls[:1]
        elif text(v).strip():
            out.append(text(v).strip())
    return out


def _logo_need_download(case: Case) -> Result:
    urls = [u for o in case.graph.top_of("Organization") for u in logo_urls(o)]
    if not [o for o in case.graph.top_of("Organization") if o.has("logo")]:
        return Result(NA, None, "Ninguna Organization de nivel superior tiene logo.")
    return Result(NE, {"logo": capped(urls)}, "Hay que obtener la imagen del logo: capture no congela imágenes.")


bind("ws-consumer/333", _logo_need_download)
bind("ws-consumer/335", _logo_need_download)
bind("ws-consumer/336", _logo_need_download)


@check("ws-consumer/334")
def _logo_crawlable(case: Case) -> Result:
    orgs = [o for o in case.graph.top_of("Organization") if o.has("logo")]
    if not orgs:
        return Result(NA, None, "Ninguna Organization de nivel superior tiene logo.")
    urls = [u for o in orgs for u in logo_urls(o)]
    blocked, unknown = [], []
    for url in urls:
        rules = case.site.robots_rules(url) if urlsplit(url).scheme in ("http", "https") else None
        if rules is None:
            unknown.append(url)
        elif not rules.allowed(url, "googlebot-image"):
            blocked.append(url)
    ev = {"logo": capped(urls), "bloqueadas": capped(blocked), "host sin robots.txt en la auditoría": capped(unknown)}
    if blocked:
        return Result(UNSAT, ev)
    if unknown or not urls:
        return Result(NE, ev, "Hay que obtener el robots.txt del host de la imagen.")
    return Result(SAT, ev)


bind("ws-consumer/337", has("^Organization>logo:ImageObject", "contentUrl", "url"))
bind("ws-consumer/339", has("^Organization", "name"))


def _matches_website(prop: str):
    def run(case: Case) -> Result:
        sites = [w for w in case.graph.of("WebSite") if w.has(prop)]
        orgs = [o for o in case.graph.top_of("Organization") if o.has(prop)]
        if not sites or not orgs:
            refs = [v for e in case.graph.entities for v in e.values("isPartOf") if isinstance(v, Ref)]
            if orgs and refs and not case.graph.of("WebSite"):
                return Result(NE, {"referencias": capped(r.id for r in refs)}, "El marcado referencia por @id un WebSite "
                              "que no define en las páginas de la auditoría.")
            return Result(NA, None, f"El marcado no tiene una WebSite y una Organization de nivel superior con {prop}.")
        site_names = {text(v).strip() for w in sites for v in w.values(prop)}
        bad = [f"{label(o)}: {text(v).strip()!r} frente a {sorted(site_names)}" for o in orgs for v in o.values(prop)
               if text(v).strip() not in site_names]
        return _result(bad, len(orgs), [], f"con otro {prop}")
    return run


bind("ws-consumer/340", _matches_website("name"))
bind("ws-consumer/341", _matches_website("alternateName"))
bind("ws-consumer/346", values_ok("^Organization", "telephone", PHONE, "teléfonos con prefijo internacional"))

# --- Reviews and ratings (valued entities) -------------------------------------------------------

REVIEW = "@valued>review:Review"
bind("ws-consumer/349", has(REVIEW, "author"))


@check("ws-consumer/351")
def _author_name_length(case: Case) -> Result:
    names = [(r, name_of(a)) for r in select(case, REVIEW).entities for a in r.values("author") if name_of(a)]
    if not names:
        return Result(NA, None, "Ninguna Review de una entidad valorada tiene un author con nombre.")
    bad = [f"{label(r)}: {len(n)} caracteres" for r, n in names if len(n) >= 100]
    return _result(bad, len(names), [], "con 100 caracteres o más")


bind("ws-consumer/352", none_has(REVIEW, "itemReviewed"))
bind("ws-consumer/353", has("@valued", "name", where=lambda e: e.has("review")))
bind("ws-consumer/354", has(REVIEW, "reviewRating", where=lambda e: not (e.has("author") and e.has("datePublished"))))
RATING_FORM = re.compile(r"^\s*([+-]?\d+([.,]\d+)?\s*(/\s*\d+([.,]\d+)?|%)?)\s*$")


def _rating_form(v) -> bool:
    if isinstance(v, Lit) and isinstance(v.value, (int, float)) and not isinstance(v.value, bool):
        return True
    return bool(RATING_FORM.match(text(v)))


def _decimal_point(v):
    if isinstance(v, Lit) and isinstance(v.value, (int, float)):
        return None if float(v.value).is_integer() else True
    s = text(v).strip()
    if not re.search(r"\d[.,]\d", s):
        return None
    return "," not in s


def rating_number(v) -> float | None:
    if isinstance(v, Lit) and isinstance(v.value, (int, float)) and not isinstance(v.value, bool):
        return float(v.value)
    s = text(v).strip()
    if re.fullmatch(r"[+-]?\d+([.,]\d+)?", s):
        return float(s.replace(",", "."))
    return None


def _range(path: str):
    def run(case: Case) -> Result:
        rs = [(r, rating_number(v)) for r in select(case, path).entities for v in r.values("ratingValue")]
        rs = [(r, n) for r, n in rs if n is not None]
        if not rs:
            return Result(NA, None, f"Ningún {path.split('>')[-1]} tiene un ratingValue numérico.")
        bad = []
        for r, n in rs:
            lo = next((rating_number(v) for v in r.values("worstRating") if rating_number(v) is not None), 1.0)
            hi = next((rating_number(v) for v in r.values("bestRating") if rating_number(v) is not None), 5.0)
            if not lo <= n <= hi:
                bad.append(f"{label(r)}: {n} fuera de [{lo}, {hi}]")
        return _result(bad, len(rs), [], "fuera de su escala")
    return run


def _scale(path: str, prop: str):
    """bestRating / worstRating of the ratings whose scale is not 1 to 5. The markup shows it
    (a value out of 1–5, a worstRating other than 1 or a bestRating other than 5); otherwise the
    page may show it, and the agent reads it."""
    def run(case: Case) -> Result:
        rs = [(r, rating_number(v)) for r in select(case, path).entities for v in r.values("ratingValue")]
        rs = [(r, n) for r, n in rs if n is not None]
        if not rs:
            return Result(NA, None, f"Ningún {path.split('>')[-1]} tiene un ratingValue numérico.")

        def declared_scale(r, n):
            worst = [rating_number(v) for v in r.values("worstRating")]
            best = [rating_number(v) for v in r.values("bestRating")]
            return not 1 <= n <= 5 or any(w not in (None, 1) for w in worst) or any(b not in (None, 5) for b in best)
        other = [r for r, n in rs if declared_scale(r, n)]
        unknown = [r for r, n in rs if not declared_scale(r, n) and not (r.has("bestRating") and r.has("worstRating"))]
        bad = [label(r) for r in other if not r.has(prop)]
        if bad:
            return Result(UNSAT, {"en otra escala": capped(label(r) for r in other), f"sin {prop}": capped(bad)})
        if unknown:
            return Result(PENDING, {"valoraciones": capped(f"{label(r)}: {n}" for r, n in rs if r in unknown)},
                          "¿Muestra la página estas valoraciones en una escala distinta de 1 a 5 (sobre 10, sobre 100, de 0 "
                          f"a 5…)? Si no en ninguna, NA. Si sí, no satisfecho si alguna de ellas no tiene {prop}.")
        if other:
            return Result(SAT, {"en otra escala": capped(label(r) for r in other)})
        return Result(NA, None, "Todas las valoraciones están en la escala de 1 a 5 según el marcado.")
    return run


RR = f"{REVIEW}>reviewRating"
bind("ws-consumer/355", has(RR, "ratingValue"))
bind("ws-consumer/356", values_ok(RR, "ratingValue", _rating_form, "números, fracciones o porcentajes"))
bind("ws-consumer/357", values_ok(RR, "ratingValue", _decimal_point, "con punto decimal"))
bind("ws-consumer/358", _range(RR))
bind("ws-consumer/359", _scale(RR, "bestRating"))
bind("ws-consumer/360", _scale(RR, "worstRating"))
bind("ws-consumer/361", has(RR, "bestRating"))
bind("ws-consumer/362", has(RR, "worstRating"))
bind("ws-consumer/364", values_ok(REVIEW, "datePublished", iso_date_or_datetime, "fechas ISO 8601"))
AR = "@valued>aggregateRating"
bind("ws-consumer/365", none_has(AR, "itemReviewed"))
bind("ws-consumer/366", has("@valued", "name", where=lambda e: e.has("aggregateRating")))
bind("ws-consumer/367", has(AR, "ratingCount", "reviewCount"))
bind("ws-consumer/368", has(AR, "ratingValue"))
bind("ws-consumer/369", values_ok(AR, "ratingValue", _rating_form, "números, fracciones o porcentajes"))
bind("ws-consumer/370", values_ok(AR, "ratingValue", _decimal_point, "con punto decimal"))
bind("ws-consumer/371", _range(AR))
bind("ws-consumer/372", _scale(AR, "bestRating"))
bind("ws-consumer/373", _scale(AR, "worstRating"))
bind("ws-consumer/374", has(AR, "bestRating"))
bind("ws-consumer/375", has(AR, "worstRating"))
bind("ws-consumer/376", value_types("@valued", "aggregateRating", of_type("AggregateRating"), "AggregateRating"))
bind("ws-consumer/384", has("@valued", "aggregateRating", where=lambda e: len(e.values("review")) >= 2))


@check("ws-consumer/385")
def _self_serving(case: Case) -> Result:
    from ..site import same_host
    orgs = [o for o in case.graph.of("Organization") if o.has("aggregateRating") or o.has("review")]
    if not orgs:
        return Result(NA, None, "Ninguna Organization tiene aggregateRating ni review.")
    page_url = case.page.url_final if case.page else case.site.url
    sellers = {id(s) for o in case.graph.of("Offer") for s in o.values("seller") if isinstance(s, Entity)}
    about = {id(v) for e in case.graph.of("WebSite") + case.graph.of("WebPage") for p in ("publisher", "about")
             for v in e.values(p) if isinstance(v, Entity)}
    own, unknown = [], []
    for o in orgs:
        urls = [text(u).strip() for u in o.values("url")] + ([o.id] if o.id and not o.id.startswith("_:") else [])
        if any(same_host(u, page_url) for u in urls) or id(o) in sellers or id(o) in about:
            own.append(label(o))
        elif not urls:
            unknown.append(label(o))
    if own:
        return Result(UNSAT, {"organización del propio sitio con valoraciones": capped(own)})
    if unknown:
        return Result(NE, {"sin url ni @id": capped(unknown)}, "La Organization no tiene url ni @id absoluto y no es seller, "
                      "publisher ni about de ninguna entidad del marcado: no se puede saber si es la del propio sitio.")
    return Result(SAT, {"examinadas": len(orgs)})
