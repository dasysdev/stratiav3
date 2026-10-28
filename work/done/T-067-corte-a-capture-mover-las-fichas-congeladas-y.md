---
id: T-067
title: Corte a capture: mover las fichas congeladas y el perfil de Chrome y repuntar los consumidores
status: hecha
depends: T-066
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Pasar demand-engine y web-audit al sistema capture/ (T-066): las fichas congeladas y el perfil de Chrome del motor se mueven sin volver a capturar ni alterar nada, demand_engine.capture y pages.py se retiran y sus consumidores leen y capturan con capture. Condición: ninguna ficha existente se vuelve a capturar ni cambia.

## Criterios de aceptación

- [x] demand-engine/var/pages movido a capture/var/pages sin descargas: el sha256 de las 45 fichas (ID.html y ID.json) y de cada fichero de las 30 instantáneas es idéntico antes y después, y las rutas snapshot de cada ID.json resuelven
- [x] demand-engine/var/capture/chrome-profile movido a capture/var/chrome-profile (no se recrea); el perfil propio de PAA sigue en demand-engine/var/paa
- [x] demand_engine.capture y pages.py retirados; taxo (page fetch, facts, section, grep), train discover y capture (selection, collect), MPIR y PAA usan capture; taxo page fetch sigue funcionando igual, sin cambios en las skills ni en el reglamento
- [x] taxo page facts, section y grep dan la misma salida que antes del corte en los 45 IDs
- [x] CLAUDE.md, los README (demand-engine, web-audit, training/selection), las skills demand-model y classify-batch, el campo page de cases/*.json y el inventario de web-audit nombran capture/var/pages
- [x] Nota en T-048 de cómo capturar las fichas nuevas con capture/; todas las pruebas del proyecto en verde (bin/run dev test)

## Resultado

Corte a capture: fichas y perfil de Chrome movidos sin alterar (sha256 idénticos), demand_engine.capture y pages.py retirados, consumidores y documentación repuntados; 188 pruebas en verde

## Notas

- 2026-10-28 De T-066: capture/var no existe todavía (la prueba manual se limpió), así que el corte mueve demand-engine/var/pages → capture/var/pages y demand-engine/var/capture/{chrome-profile,chrome.log} → capture/var/ sin choque. El campo snapshot (var/pages/ID/INSTANTE) es relativo a la raíz del sistema y resuelve igual bajo capture/. demand-engine/tests/capture está duplicado en capture/tests (copiado, no movido, para no tocar demand-engine en T-066): se borra con demand_engine.capture. freeze ahora rechaza un ID con ficha y exige ID kebab-case (los 45 cumplen); collect ya no revisita lo capturado por su registro. page_path dice «usa: capture/bin/pages fetch ID URL»; taxo puede capturar su PageError y mantener su texto. Al retirar el motor de demand-engine, websockets puede salir de demand-engine/pyproject.toml (PAA lo usa a través de capture) y bin/run dev lock. PYTHONPATH, COPY del Dockerfile y .dockerignore ya incluyen capture/.
- 2026-10-28 Corte hecho: var/pages y var/capture/{chrome-profile,chrome.log} renombrados a capture/var/ (mismos inodos; 210 sha256 de fichas e instantáneas y 1754 del perfil idénticos; las 30 rutas snapshot resuelven bajo capture/). 13 módulos de demand-engine importan capture (absoluto); bin/taxo y bin/train ponen capture/src en la ruta y bin/paa (classify, control) en PYTHONPATH. taxo conserva su texto «usa: taxo page fetch» al faltar una ficha y rechaza en el host un ID existente o no válido sin delegar (prueba nueva). collect: la ruta snapshot del registro pasa a relativa a capture/, como la de ID.json (los registros viejos ya resuelven así). websockets sale de demand-engine (uv.lock regenerado). Retiradas 22 pruebas duplicadas del motor y la de lectores (ya en capture/tests): 188 en verde. Skill demand-model: si el ID ya tiene ficha, sufijo (antes solo si era de otra URL), porque page fetch lo rechaza. cases/*.json: page relativo a la raíz, como source. Prueba manual desde el host contra un servidor local: captura con el perfil en capture/var, rechazo del ID repetido; limpiada. El informe web-audit/reference/reports/2026-10-27 conserva la ruta antigua (histórico).
