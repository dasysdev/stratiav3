---
id: T-083
title: Universo de la auditoría: cruce con los sitemaps y páginas de D-167 sobre el rastreo
status: hecha
depends: T-082
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Sobre lo que capturó la araña: el universo es la unión del rastreo y los sitemaps. Cada URL registra si se alcanzó, si está en los sitemaps y su tipo de página (ficha, categoría, política, portada u otra), con varias señales y no solo el marcado. Las URL de los sitemaps no alcanzadas se capturan una vez. Las páginas de D-167 (portada, políticas desde el pie, categoría por las migas) se localizan sobre lo capturado. pages audit toma las fichas del universo.

## Criterios de aceptación

- [x] El manifiesto lista el universo: cada URL con alcanzada (sí/no), in_sitemaps y tipo de página; lo dudoso queda sin clasificar
- [x] Las URL de los sitemaps no alcanzadas se capturan una vez y quedan registradas como no alcanzadas
- [x] Portada, políticas y categorías de D-167 se localizan sobre lo capturado; no se pide nada aparte
- [x] Las fichas auditadas se eligen del universo (sin lista del encargo, todas sus fichas); pruebas de capture en verde

## Resultado

Universo en crawl.json (alcanzada, en sitemaps, tipo) y pages audit sobre el rastreo sin pedir nada (D-217)

## Notas

- 2026-10-29 D-215 (2026-10-29): las categorías de la auditoría son todas las del sitio, no solo la inmediata de cada ficha. pages audit (capture/audit) sigue con la inmediata: cambiarlo aquí. La araña ya registra crawl.audit_pages (políticas y categorías de las migas) y category_shapes.
- 2026-10-29 Usuario (2026-10-29): pages audit trabaja sobre el rastreo, en su carpeta; la auditoría solo se hace sobre el resultado del rastreo (no se pide nada aparte); sin lista del encargo, todas las fichas del universo. Manifiesto de la araña en crawl.json; audit.json, las páginas auditadas (forma que lee web-audit).
- 2026-10-29 Hecho: spider lee los sitemaps tras la portada (diario {sitemaps}), captura una vez sus URL no alcanzadas (chosen_as sitemap, source sitemaps; enlaces registrados, no seguidos), escribe crawl.json con universe (reached, in_sitemaps, type por señales; null lo dudoso) y coverage.crawl_complete. pages audit (audit.run) elige sobre crawl.json sin Chrome ni peticiones: fichas del encargo o todas las del universo, portada, políticas, categorías del universo sin paginación e inmediatas; audit.json en la forma que lee web-audit; reserva → código 3; un rastreo auditado no se reanuda. burritoblanco-t083 (40 URL): 6 sitemaps, 791 URL, universo 957, 29 fichas, 34 páginas elegidas. Los rastreos anteriores (t082, t088, t093*) tienen el manifiesto en audit.json: no sirven para pages audit. Canon D-217. 64 pruebas de capture y 36 de web-audit en verde.
