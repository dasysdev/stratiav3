---
id: T-060
title: Corte a references: mover las fuentes congeladas y repuntar demand-engine y web-audit
status: hecha
depends: T-059
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Pasar demand-engine y web-audit a references/ sin cambiar su comportamiento: mover (no volver a descargar: las versiones de documento llevan la fecha de descarga) los dos var/refs a references/var/ con un solo pins.json, cambiar los imports de los consumidores, retirar los refs propios de cada sistema y dejar al día la documentación operativa. Desde aquí no queda ninguna dependencia entre demand-engine y web-audit.

## Criterios de aceptación

- [x] Copia previa de demand-engine/var/refs y web-audit/var/refs fuera del proyecto; datos movidos a references/var/ sin descargar de nuevo; refs status muestra las 36 fuentes con las mismas versiones fijadas que antes del corte
- [x] demand-engine (taxo, blocks, demand/, paa/) y web-audit (reqs) leen de references; ya no existen demand_engine/refs.py, web_audit/refs.py, demand-engine/bin/refs, web-audit/bin/refs, web-audit/reference/sources.json ni los var/refs de los dos sistemas
- [x] Credenciales de SP-API en references/.env (con .env.example); refs check amazon-btg amazon-ptd funciona con ellas
- [x] engine.refs de cada modelo y refs de rules/importance.json registran solo las versiones de las fuentes cuyo uses incluye demand-engine: un modelo de demanda reensamblado de un caso de control sale idéntico al de antes del corte
- [x] web-audit/bin/reqs check correcto y todas las pruebas en verde (bin/run dev test)
- [x] READMEs de los tres sistemas, CLAUDE.md, .gitignore, .dockerignore y la skill /web-reference apuntan a references/; grep de demand-engine/bin/refs, web-audit/bin/refs y var/refs sin resultados fuera de docs/archive y del changelog

## Resultado

Corte a references: datos movidos sin descarga (36 fuentes, mismas versiones), demand-engine y web-audit leen de references, refs propios retirados, credenciales en references/.env; modelos, taxo y reqs check idénticos; 151 pruebas en verde

## Notas

- 2026-10-28 Copia previa en ~/stratia-backup/T-060-refs-2026-10-28/ (los dos var/refs y demand-engine/.env, idénticos por diff -r): se puede borrar cuando se quiera. Datos movidos con mv (sin descarga); pins.json fusionado sin colisiones; web-audit/var quedó vacío y se retiró (también de .gitignore).
- 2026-10-28 Equivalencia antes/después: refs status (36 fuentes, mismas versiones fijadas), reqs check (29 fichas, 502 citas, 440 requisitos; mismo resumen), salida de taxo (shopify, category, values, google, amazon, ptd y error de PTD) y los 14 modelos de var/runs/2026-10-26-v6-a reensamblados en memoria: idénticos. pins('demand-engine') = refs de catalog/rules/importance.json.
- 2026-10-28 Código: imports a references.read/references.store; pins('demand-engine') en model, train y blocks; reqs filtra el registro por uses (una ficha de una fuente que web-audit no usa da error) y toma secciones y RefsError de references.read (ReqsError retirado); test_sections de web-audit retirado (cubierto en references/tests/test_read.py). Los envoltorios de bin/ ponen references/src en la ruta (bin/paa classify, en PYTHONPATH). 151 pruebas en verde.
- 2026-10-28 Grep del criterio: quedan var/refs solo en los reglamentos históricos rulebook-v0/v1/v2 (versiones congeladas, no se tocan; rulebook.md v3 sí al día) y en work/done y work/log (registro). refs check 2026-10-28: amazon-ptd con cambios publicados desde 2026-10-24 (1877 tipos); no se descargó.
- 2026-10-28 2026-10-28 A petición del usuario, rulebook-v0/v1/v2 también apuntan a references/var/pins.json: el grep del criterio queda limpio fuera de docs/archive, el changelog y el registro de trabajo (work/done, work/log.md).
