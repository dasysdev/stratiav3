---
id: T-014
title: Sonda de acceso del MPIR con candidatos de ropa de cama
status: pendiente
depends: T-013
milestone: codigo
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
