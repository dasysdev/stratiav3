---
id: T-094
title: Piloto GSC: auditoría de capture de Burrito Blanco con 2 fichas
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

capture deja una auditoría nueva de Burrito Blanco con el rastreo completo y, como fichas del encargo, https://www.burritoblanco.com/edredon-color-nude-diseno-geometrico-266-p-6172.html y https://www.burritoblanco.com/funda-nordica-barbie-algodon-100-diseno-malibu-003-rosa-p-5611.html. Es la entrada del piloto de la auditoría informativa.

## Criterios de aceptación

- [ ] capture/bin/pages crawl rastrea Burrito Blanco en una auditoría nueva y termina sin error ni reserva TDM
- [ ] pages audit AUDIT con las 2 URL deja en audit.json las 2 fichas capturadas con audit-es, la portada, las políticas y las categorías (D-167)
- [ ] Si el rastreo capturó una ficha con la URL de su variante, audit.json la asocia a la URL del encargo; el criterio queda anotado en la tarea
- [ ] La tarea anota el ID de la auditoría y el page-ID de cada ficha

## Notas

- 2026-10-29 URL del encargo: las canónicas sin variante. En burritoblanco-t083 el edredón se capturó como …-p-6172-95132.html (sitemaps_by: canonical) y la de Barbie quedó pendiente (…-p-5611.html, reached: undetermined). Por eso, auditoría nueva con el código actual (D-215, D-217).
