---
id: T-021
title: Motor de captura común (capture/) usado por el MPIR y por taxo page fetch
status: hecha
depends:
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Separar el motor de captura en src/demand_engine/capture/ (navegador, legitimidad, desafíos, ritmo, visita, sitemaps, orquestación por sitio) y dejar en mpir/ solo lo propio del MPIR; taxo page fetch captura con el motor (Chrome real, robots.txt y reservas TDM), sin ritmo de lector en las capturas sueltas

## Criterios de aceptación

- [x] capture/ sin dependencias de mpir/; mpir/ usa capture/ para comprobar, descubrir y capturar
- [x] taxo page fetch usa el motor: legitimidad, parada ante desafíos, DOM renderizado en var/pages/ID.html y metadatos ampliados; desde el host se ejecuta en el contenedor
- [x] Un solo Chrome y perfil por contenedor (var/capture/chrome-profile); variables CAPTURE_*
- [x] Pruebas en verde, incluida una de extremo a extremo de taxo page fetch con Chrome
- [x] README de capture y de mpir, README de demand-engine, CLAUDE.md y enlaces de docs al día; check_docs sin errores

## Resultado

Motor de captura común en src/demand_engine/capture/ (lotes con crawl, página suelta con once) usado por el MPIR y por taxo page fetch; mpir/ con lo propio del MPIR; 52 pruebas en verde; probado con una ficha real tras Cloudflare

## Notas

- 2026-10-25 capture/: browser, cdp, robots, tdm, detect, legitimacy (access + check_site), pacing, crawl (SiteRun, un hilo por sitio), visit, once (captura suelta), files, sitemaps; sin dependencias de mpir/. mpir/: store, scheduler (capturable, comprobaciones con ficha, inventario sobre crawl), ingest, CLI. taxo page fetch → pages.fetch → capture_once: DOM renderizado en var/pages/ID.html, instantánea en var/pages/ID/<fecha>/; desde el host delega en el contenedor (bin/run dev exec). Probado desde el host con burritoblanco.com: HTTP 200 a través de Cloudflare en 15 s (la descarga simple recibía un desafío). Marca de bloque oculto renombrada a data-capture-hidden; perfil en var/capture/; variables CAPTURE_*. 52 pruebas en verde; 37/37 salidas de solo lectura iguales. Skill /demand-model: nota de que page fetch necesita el entorno levantado.
