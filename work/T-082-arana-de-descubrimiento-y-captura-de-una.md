---
id: T-082
title: Araña de descubrimiento y captura de una auditoría en capture
status: pendiente
depends: T-080, T-081
milestone:
created: 2026-10-29
---

## Objetivo

Un proceso de capture que, desde la portada, descubre las páginas de un sitio por los enlaces <a href> del documento sin JavaScript y captura cada página una sola vez con audit-es. Ritmo: 1 página/s como máximo, o el Crawl-delay si es mayor. Tope: 50.000 URL. Es reanudable y aplica la legitimidad del motor y la parada por reserva TDM. audit-es consulta el origen (RIPEstat) una vez por ejecución; lo demás del perfil no cambia.

## Criterios de aceptación

- [ ] Un comando de capture rastrea y captura un sitio en var/audits/AUDIT/, con la instantánea audit-es y los enlaces de cada página
- [ ] El manifiesto registra la cobertura: completa, o los topes, bloqueos y pendientes que la dejan incompleta
- [ ] Un rastreo interrumpido se reanuda sin volver a pedir las páginas ya capturadas
- [ ] audit-es consulta el origen una vez por ejecución y lo registra en cada página; reader no cambia
- [ ] Pruebas con un sitio local (enlace creado por JS, nofollow, ruta prohibida en robots.txt, redirección, facetas sin fin) y pruebas de capture en verde

## Notas

- 2026-10-29 Medido el 2026-10-29 en las 30 páginas de las 5 auditorías de capture/var/audits: mediana ~18 s por página (3–28 s). Causa: profiles.origin() hace 4 consultas a RIPEstat en cada visita y agota la espera de 15 s en 20 de 30 páginas (el origen queda como error). Con el origen por ejecución, 2–8 s. Además, sin aprobar todavía (T-085): wait_ready espera a load, wait_stable ≥1,5 s sin JS, dom.html ≈ respuesta, page.mhtml de 3 a 200 veces la respuesta (hasta 14 MB). Tamaños: response.html.gz ~38 KB de mediana, meta.json ~5 KB. Perfiles: audit-es solo lo usan pages audit y 3 fichas sueltas (audit-cojin-018, audit-cuerda-tootoy, audit-eci-aceite-010695); reader, PAA, entrenamiento, MPIR y taxo.
- 2026-10-29 Canon: D-170 (universo = rastreo ∪ sitemaps; enlaces <a href> del documento sin JS, nofollow se sigue y se registra; los enlaces no se auditan; «no rastreable» solo con rastreo completo, si no se registra la cobertura; la instantánea de la página auditada es la de la visita del rastreo). Al terminar, actualizar capture/README y la fila de capture del CLAUDE.md raíz.
