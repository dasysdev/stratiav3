---
id: T-094
title: Piloto GSC: auditoría de capture de Burrito Blanco con 2 fichas
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

capture deja una auditoría nueva de Burrito Blanco con el rastreo completo y, como fichas del encargo, https://www.burritoblanco.com/edredon-color-nude-diseno-geometrico-266-p-6172.html y https://www.burritoblanco.com/funda-nordica-barbie-algodon-100-diseno-malibu-003-rosa-p-5611.html. Es la entrada del piloto de la auditoría informativa.

## Criterios de aceptación

- [x] Decisión del usuario (2026-10-30): el piloto no usa el rastreo completo ni audit.json; solo captura las 2 fichas del encargo
- [x] capture/bin/pages fetch con --profile audit-es congela las 2 fichas con HTTP 200, URL final igual a la del encargo y canónica propia
- [x] La tarea anota el page-ID de cada ficha

## Resultado

Piloto: 2 fichas de Burrito Blanco capturadas con audit-es (audit-bb-edredon-6172, audit-bb-barbie-5611), sin rastreo completo

## Notas

- 2026-10-29 URL del encargo: las canónicas sin variante. En burritoblanco-t083 el edredón se capturó como …-p-6172-95132.html (sitemaps_by: canonical) y la de Barbie quedó pendiente (…-p-5611.html, reached: undetermined). Por eso, auditoría nueva con el código actual (D-215, D-217).
- 2026-10-30 Decisión del usuario (2026-10-30): sin rastreo completo para el piloto; se capturan solo las 2 fichas con pages fetch --profile audit-es. Rastreo burritoblanco-t094 interrumpido (138 capturadas) y sin uso: desechable.
- 2026-10-30 Page-ID: edredón → audit-bb-edredon-6172 (var/pages/audit-bb-edredon-6172/20261030T004525); Barbie → audit-bb-barbie-5611 (var/pages/audit-bb-barbie-5611/20261030T004541). Ambas: HTTP 200, URL final = URL del encargo, canónica propia, título del producto.
