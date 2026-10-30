---
id: T-107
title: PAA: primera pasada al catálogo con el reglamento v8 (D-178, D-180)
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

El catálogo compilado tiene la primera pasada de PAA con el reglamento vigente antes de rehacer los modelos del piloto. Simulación en memoria (2026-10-30, clasificaciones antiguas): 69 entradas en 17 bloques; cambian 4 de los 8 bloques de la Barbie y 3 de los 8 del edredón.

## Criterios de aceptación

- [ ] Los 12 conjuntos de PAA se clasifican de nuevo con classifier/paa.md v8 (/paa-classify); cada classified.json registra v8 y su uso de tokens
- [ ] bin/paa control sobre los 12 conjuntos deja su informe y la decisión D-180; la tarea anota el total por apartado
- [ ] bin/paa compile mete la pasada en el catálogo: bloques con versión nueva, catalog/paa-questions.json y training/reports/paa/accepted.json
- [ ] bin/model check --catalog, bin/model hints check y bin/model refs terminan sin errores
- [ ] La tarea anota los bloques de la clave de bb-barbie-5611 y bb-edredon-6172 que cambian de versión y las revisiones D-179 que los tocan
- [ ] Tests en verde

## Notas
