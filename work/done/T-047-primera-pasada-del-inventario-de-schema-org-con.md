---
id: T-047
title: Primera pasada del inventario de Schema.org con web-reference
status: hecha
depends: T-045, T-046
milestone:
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Procesar con /web-reference el inventario de fuentes (tmp/inventario_fuentes_auditoria_schema_org.md) más los huecos detectados (Microdata, RDFa, procesado JSON-LD, vocabulario en formato máquina, Product snippet, JS, tipos de las fichas reales) y obtener la v0.1 de los requisitos técnicos de Web Schema.org

## Criterios de aceptación

- [x] web-audit/reference/inventory.md con todas las fuentes, su función y estado, incluidos los huecos añadidos
- [x] Ficha con citas literales de cada especificación aplicable congelada
- [x] Requisitos técnicos v0.1 de Web Schema.org (serialización, vocabulario 30.1 y perfil Google) que pasan bin/reqs check
- [x] Informe de la pasada en web-audit/reference/reports/ con lo que queda pendiente

## Resultado

Primera pasada de la referencia técnica: 7 fuentes nuevas, 29 fichas, 440 requisitos (208 obligatorias, 232 recomendadas) que pasan reqs check; inventario, informe e I-47

## Notas

- 2026-10-27 Viene de T-045: los huecos (Microdata, RDFa 1.1, JSON-LD 1.1 Processing Algorithms and API, Product snippet, JS) no están en sources.json; se añaden con la skill (entrada + web-audit/bin/refs fetch ID). No se congelan VAL-01/02 ni SKL-*. refs diff schemaorg 30.0→30.1 (probado aparte) muestra muchos términos que salen de pending (p. ej. Certification, CategoryCode): mirarlo al escribir los requisitos de vocabulario.
- 2026-10-27 Viene de T-046: formato B en web-audit/reference/README.md; skill /web-reference. Por lotes: primero un agente por fuente (solo su ficha), después uno por nivel (su fichero de requisitos y citas en fichas de su nivel). gs1-smartsearch es PDF: no tiene texto citable. Si dos especificaciones fijan la misma condición, cada una tiene su requisito (la tasa es de OQ-30).
- 2026-10-27 Hecho con /web-reference y 7 agentes (fichas y requisitos por nivel; los fragmentos se fusionaron y renumeraron). reqs check: correcto · 29 fichas (23 aplicables), 502 citas, 440 requisitos (208 obligatorias, 232 recomendadas); serialización 44, vocabulario 12 (todas recomendadas), consumidor 384. Fuentes nuevas: w3c-json-ld11-api, whatwg-html-microdata, w3c-rdfa-core, w3c-html-rdfa, google-search-product-snippet, google-search-javascript y google-search-review-snippet (por remisión de las filas review/aggregateRating, igual que sd-policies por la de #guidelines). Sin ficha: GS1-01/03 (I-47, clase «vocabulario complementario»). I-41 anotada: el dígito de control del GTIN lo recomienda Schema.org 30.1, no las fichas de comerciante. Skill: inventory.md y reports/ añadidos al formato. Pendiente en el informe: HTML LS §4 (meta/link/time/script), ISO 4217/3166, formatos de Google Images; lecturas discutibles (naturaleza de la cabecera en reglas de valor, obligatorias por cláusula general, presencia frente a contenido visible).
