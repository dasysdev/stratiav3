---
id: T-082
title: Araña de descubrimiento y captura de una auditoría en capture
status: hecha
depends: T-080, T-081
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Un proceso de capture que, desde la portada, descubre las páginas de un sitio por los enlaces <a href> del documento sin JavaScript y captura cada página una sola vez con audit-es. Ritmo: 1 página/s como máximo, o el Crawl-delay si es mayor. Tope: 50.000 URL. Es reanudable y aplica la legitimidad del motor y la parada por reserva TDM. audit-es consulta el origen (RIPEstat) una vez por ejecución; lo demás del perfil no cambia.

## Criterios de aceptación

- [x] Un comando de capture rastrea y captura un sitio en var/audits/AUDIT/, con la instantánea audit-es y los enlaces de cada página
- [x] El manifiesto registra la cobertura: completa, o los topes, bloqueos y pendientes que la dejan incompleta
- [x] Un rastreo interrumpido se reanuda sin volver a pedir las páginas ya capturadas
- [x] audit-es consulta el origen una vez por ejecución y lo registra en cada página; reader no cambia
- [x] Pruebas con un sitio local (enlace creado por JS, nofollow, ruta prohibida en robots.txt, redirección, facetas sin fin) y pruebas de capture en verde

## Resultado

Araña de auditoría en capture (pages crawl): rastreo sin parámetros, captura audit-es, cobertura y reanudación (D-170, D-173)

## Notas

- 2026-10-29 Medido el 2026-10-29 en las 30 páginas de las 5 auditorías de capture/var/audits: mediana ~18 s por página (3–28 s). Causa: profiles.origin() hace 4 consultas a RIPEstat en cada visita y agota la espera de 15 s en 20 de 30 páginas (el origen queda como error). Con el origen por ejecución, 2–8 s. Además, sin aprobar todavía (T-085): wait_ready espera a load, wait_stable ≥1,5 s sin JS, dom.html ≈ respuesta, page.mhtml de 3 a 200 veces la respuesta (hasta 14 MB). Tamaños: response.html.gz ~38 KB de mediana, meta.json ~5 KB. Perfiles: audit-es solo lo usan pages audit y 3 fichas sueltas (audit-cojin-018, audit-cuerda-tootoy, audit-eci-aceite-010695); reader, PAA, entrenamiento, MPIR y taxo.
- 2026-10-29 Canon: D-170 (universo = rastreo ∪ sitemaps; enlaces <a href> del documento sin JS, nofollow se sigue y se registra; los enlaces no se auditan; «no rastreable» solo con rastreo completo, si no se registra la cobertura; la instantánea de la página auditada es la de la visita del rastreo). Al terminar, actualizar capture/README y la fila de capture del CLAUDE.md raíz.
- 2026-10-29 Prueba 2026-10-29 con prototipo desechable (capture/var/probes/crawl_probe.py, BFS, audit-es, origen 1 vez, 1 pág/s, tope 50) en burritoblanco.com: 50/50 capturadas en 146 s (visita 2,2–3,2 s, mediana 2,6), 26 MB; sin Crawl-delay, tdmrep 404, sin reserva. ~280 enlaces/página: 1341 URL descubiertas desde 50 páginas, 71 % con query (facetas ?q=, ?page=): el tope de 50.000 se agotaría en facetas; el BFS recorre primero las categorías (-c-) y no llega a ninguna ficha (-p-, 267 descubiertas) en 50. Decidir el tratamiento de query/facetas y el orden de la cola.
- 2026-10-29 Usuario (2026-10-29): sin facetas; la araña solo rastrea URL sin parámetros (query). Prueba 2 en burritoblanco: 1298 enlaces con query descartados; 392 URL descubiertas desde 50 páginas (antes 1341); las 50 visitas, portada y 49 categorías: el BFS sigue sin llegar a fichas en 50. Enmienda D-170 (enlaces <a href> sin filtro): registrar en el canon con /docs-update.
- 2026-10-29 Hecho: capture.spider + pages crawl (--resume, --max-urls); diario crawl.jsonl, links.json.gz por página, cobertura con motivos; origen una vez por ejecución en audit, crawl y spider (visit(origin=)); _Links con nofollow y <base href>. Real en burritoblanco: 2,2–3,0 s y ~110 KB por página (50.000 páginas ≈ 37 h y 5,5 GB). Canon: D-173 (sin parámetros; lecturas de host, recursos, anchura, bloqueo y cobertura). 253 pruebas en verde.
- 2026-10-29 Corrección: 251 pruebas del proyecto en verde (58 de capture), no 253. Revisor de docs: 3 hallazgos menores corregidos (cabecera de D-170, http(s) y «cuyos enlaces no se leyeron» en evaluation-scopes).
