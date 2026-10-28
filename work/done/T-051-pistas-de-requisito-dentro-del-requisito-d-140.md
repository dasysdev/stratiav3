---
id: T-051
title: Pistas de requisito dentro del requisito (D-140)
status: hecha
depends:
milestone:
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Aplicar D-140: las pistas dirigidas a un requisito viven en el propio requisito del catálogo de demanda; las de tipo y fuente siguen en hints.json.

## Criterios de aceptación

- [x] PV-23…PV-37 están en el campo hints de sus requisitos (cat/ropa-de-casa, sabanas, ropa-de-cama y gen.json), sin «para», y ya no en hints.json
- [x] bin/model hints check valida también las pistas de los requisitos (cinco campos, id único en todo el sistema) y da 0 errores
- [x] bin/model hints find devuelve para los nueve requisitos las mismas pistas que antes del cambio
- [x] Las pruebas del motor pasan en el contenedor

## Resultado

Pistas de requisito dentro del requisito (D-140): 15 movidas, hints.py y pruebas adaptados, find sin cambios

## Notas

- 2026-10-27 PV-23…PV-37 movidas al campo «hints» de sus nueve requisitos (sin «para»); hints.json 0.2 con 26 pistas (21 vigentes, 5 retiradas), solo de tipo y fuente; el catálogo rechaza la llave «requisito». hints.py valida también las pistas de los requisitos (cinco campos, id único en catálogo y requisitos, duplicadas dentro del requisito). bin/model hints check: 0 errores; find de los nueve requisitos idéntico al de antes; 58 pruebas pasan; bin/model check --catalog correcto. Docs: D-140, assessment-hints 1.6, demand-model 3.4, glosario; revisado por docs-reviewer y corregido.
