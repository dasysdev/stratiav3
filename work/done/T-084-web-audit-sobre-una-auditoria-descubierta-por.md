---
id: T-084
title: web-audit sobre una auditoría descubierta por la araña
status: hecha
depends: T-083
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Que web-audit/bin/audit lea una auditoría hecha con la araña (universo y páginas de D-167) y evalúe el requisito del sitemap en cada página auditada, también en las que solo encontró el rastreo.

## Criterios de aceptación

- [x] bin/audit run funciona sobre una auditoría de la araña sin cambiar el método de los requisitos
- [x] El requisito del sitemap se evalúa en cada página auditada, también en las que no están en los sitemaps
- [x] Pruebas de web-audit en verde

## Resultado

web-audit evalúa una auditoría de la araña sin cambios; 014 en cada página, prueba nueva

## Notas

- 2026-10-29 burritoblanco-t083 (araña, 34 páginas): bin/audit run sin cambios de código, 8097 casos en 6 s. w-consumer/014 en las 34: portada, categoría y 1 política satisfechas; 2 políticas fuera de los sitemaps y 29 fichas no satisfechas. Las fichas son URL de variante (…-p-2024-964.html): capture marca in_sitemaps por la canónica (sitemaps_by canonical) y el método de 014 busca la URL final; el resultado sigue el método. 29 NE de ws-consumer/184: canónicas no capturadas por el tope de 40 URL. Prueba nueva test_crawl_audit_evaluates_sitemap_on_every_page; 37 en verde.
- 2026-10-29 Usuario (2026-10-29): w-consumer/014 busca la URL canónica que declara la página; sin canónica, la URL final; varias distintas, NE. burritoblanco-t083: las 29 fichas de variante pasan a satisfecho; quedan 2 políticas fuera de los sitemaps. 38 pruebas en verde.
