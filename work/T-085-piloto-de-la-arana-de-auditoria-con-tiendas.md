---
id: T-085
title: Piloto de la araña de auditoría con tiendas reales y contraste con Screaming Frog
status: pendiente
depends: T-083, T-084
milestone:
created: 2026-10-29
---

## Objetivo

Rastrear y capturar burritoblanco y 2-3 tiendas españolas más. Contrastar el universo con Screaming Frog (versión gratuita, hasta 500 URL) en una tienda pequeña. Medir tiempo por página, disco, desafíos y fichas fuera del sitemap. Decidir con esos datos la aceleración aparcada de audit-es (DOM, MHTML, espera a load).

## Criterios de aceptación

- [ ] Informe por tienda: URL descubiertas, alcanzadas, fuera del sitemap, no alcanzadas, tiempo por página, disco y desafíos
- [ ] Diferencias con Screaming Frog explicadas una a una en la tienda de contraste
- [ ] Propuesta sobre la aceleración de audit-es con los datos medidos

## Notas

- 2026-10-29 Pregunta del usuario (2026-10-29): por qué se guarda MHTML. El MHTML lleva imágenes y CSS (portada de burritoblanco: 38 imágenes, 15 CSS, 1,8 MB comprimido); solo lo lee el MPIR (aparcado), web-audit no.
- 2026-10-29 2026-10-29 Usuario: quitar el MHTML de audit-es. Hecho: Profile.mhtml (False en audit-es). burritoblanco, 10 páginas: 1,0 MB sin MHTML frente a 6,8 MB con él; 2,8 s por página.
- 2026-10-29 2026-10-29 D-172: el motor no guarda el MHTML en ningún perfil (canon: sampling-capture 1.6). Retirados Profile.mhtml y Page.mhtml(); mpir ingest sigue aceptando .mhtml a mano. 198 pruebas en verde.
