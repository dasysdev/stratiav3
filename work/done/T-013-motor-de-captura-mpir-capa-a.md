---
id: T-013
title: Motor de captura MPIR (capa A)
status: hecha
depends: T-002
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Motor que captura recursos de ecommerce referentes con Chrome real por CDP, a ritmo de lector, comprobando legitimidad (robots.txt RFC 9309, reservas TDM) y parando ante desafíos; capa A del MPIR en ficheros, sin capturas de pantalla

## Criterios de aceptación

- [x] mpir site check guarda robots.txt, TDMRep, cabeceras y meta de reserva, antibot detectado y un veredicto por referente
- [x] mpir capture guarda por recurso HTML de la respuesta, DOM renderizado con bloques ocultos marcados y MHTML, con metadatos y sha256, sin sobrescribir nunca
- [x] Ritmo por dominio (permanencia, pausas, pausas largas, Crawl-delay, tope diario, horario) y dominios en paralelo, cada uno en su ventana
- [x] Ante 403/429 o desafío se para el dominio, se guarda la evidencia y el recurso queda bloqueado; con reserva TDM no se guarda el contenido
- [x] mpir discover (sitemaps), mpir add, mpir ingest (manual) y mpir status (cobertura por estado)
- [x] Pruebas en verde: unitarias y una de extremo a extremo con Chrome contra un servidor local

## Resultado

Motor de captura MPIR (capa A) en mpir/: Chrome real por CDP, robots.txt RFC 9309 y reservas TDM, ritmo de lector en paralelo por referente, parada ante desafíos, discover/add/capture/ingest/status; 29 pruebas en verde y prueba de humo real

## Notas

- 2026-10-25 Prueba de humo (estudio prueba-humo en mpir/var): burritoblanco.com, una ficha. Veredicto ok con Cloudflare presente; capturada en 20 s, HTTP/3 200, 2596 elementos, 39 bloques ocultos marcados, unos 650 KB comprimidos por página.
