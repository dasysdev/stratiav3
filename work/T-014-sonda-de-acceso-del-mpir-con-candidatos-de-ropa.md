---
id: T-014
title: Sonda de acceso del MPIR con candidatos de ropa de cama
status: bloqueada
depends: T-013
milestone: codigo
reason: Aparcada por D-095 (MPIR aparcado); retomarlo es una decisión nueva
created: 2026-10-25
---

## Objetivo

Probar el motor con 6-8 candidatos de ropa de cama (3-5 páginas cada uno) y decidir con datos la configuración (Chrome del contenedor o del host)

## Criterios de aceptación

- [ ] Candidatos validados por el usuario antes de capturar
- [ ] Informe por dominio: veredicto de legitimidad, bloqueos o desafíos, tiempos y diferencias entre configuraciones
- [ ] Configuración elegida registrada en el README del motor

## Notas

- 2026-10-25 Hallazgo de T-013: en el contenedor Chrome bloquea WebGL (webgl: null con y sin MPIR_DISABLE_GPU), señal delatora. Comparar con el Chrome del host (GPU de WSLg); valorar también --enable-unsafe-swiftshader. navigator.webdriver=false, UA sin Headless, es-ES y Europe/Madrid ya correctos.
- 2026-10-25 Desde T-021 las variables son CAPTURE_DISPLAY, CAPTURE_DISABLE_GPU, CAPTURE_CDP_PORT y CAPTURE_PROFILE; perfil de Chrome en demand-engine/var/capture/. Diagnóstico: demand-engine/bin/mpir browser (capture.browser.signals).
- 2026-10-27 Hallazgo de T-037 (PAA, 2026-10-27): en el Chrome del contenedor (gpu_compositing disabled_software, también sin --disable-gpu) las páginas con bucles de requestAnimationFrame saturan el hilo principal (las respuestas de IA de Google). Si la captura del MPIR interactúa con páginas animadas, comparar con el Chrome del host con GPU.
