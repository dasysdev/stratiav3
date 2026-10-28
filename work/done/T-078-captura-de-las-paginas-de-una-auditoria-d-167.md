---
id: T-078
title: Captura de las páginas de una auditoría (D-167) en capture
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Que capture congele, con el perfil audit-es, todo lo que D-167 fija para una auditoría de un sitio: las fichas del encargo, la portada, las políticas (envíos, devoluciones, contacto, aviso legal) localizadas desde la portada y su pie, la categoría inmediata de cada ficha por sus migas de pan, robots.txt y los sitemaps (declarados en robots.txt o /sitemap.xml, con índices y gzip), con el tipo de página registrado

## Criterios de aceptación

- [x] Un comando de capture congela una auditoría a partir de la lista de fichas del encargo, con el perfil audit-es, en un directorio por auditoría
- [x] Portada, políticas y categoría inmediata se localizan y se registran con su tipo de página; la que no se localiza queda registrada como no localizada, sin sustituirla
- [x] robots.txt y los sitemaps (índices y gzip) quedan congelados, y para cada ficha si su URL está en ellos
- [x] Probado con una tienda real de las ya capturadas; pruebas de capture en verde

## Resultado

capture.audit y pages audit: páginas de una auditoría (D-167) con audit-es en var/audits/AUDIT/; probado con Burrito Blanco; 44 pruebas en verde

## Notas

- 2026-10-28 Decidido con el usuario: todo en var/audits/AUDIT/ (también las fichas del encargo; no pasan al almacén var/pages), 3–8 s entre páginas (o Crawl-delay), sitemaps con tope 50 ficheros/200 MB y cobertura yes/no/undetermined. Consecuencia para D-167 («la misma instantánea que la informativa»): la auditoría informativa (y web-audit, T-049) leen las fichas de la auditoría con capture.audit.read, no con pages.read.
- 2026-10-28 Prueba real: burritoblanco-t078 (cojín 018), 6/6 páginas en ~3 min; envíos no localizado (la portada solo enlaza /faqs); la ficha del encargo (…-p-5777-92767.html, con variante) no está en el sitemap, que lista …-p-5777.html: la comparación es literal; si cuenta la canónica lo decide quien interpreta (web-audit).
- 2026-10-28 Ampliado a petición del usuario: la pertenencia al sitemap también coincide por la canónica que declara la ficha (link rel=canonical; campo canonical, by=url|url_final|canonical). Burrito Blanco: la ficha del encargo está en el sitemap por su canónica (…-p-5777.html).
