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

- [ ] Los modelos de los 12 conjuntos (campo model de paa/<SET>.json, hoy del 2026-10-26: reglamento v3, reglas 6, gen@0.5) se reensamblan en una ejecución nueva desde la última salida v4 de cada caso, con las reglas 8 y el catálogo vigente; cada paa/<SET>.json apunta a su modelo nuevo
- [ ] Los 12 conjuntos de PAA se clasifican de nuevo con classifier/paa.md v8 (/paa-classify); cada classified.json registra v8 y su uso de tokens
- [ ] bin/paa control sobre los 12 conjuntos deja su informe y la decisión D-180; la tarea anota el total por apartado
- [ ] bin/paa compile mete la pasada en el catálogo: bloques con versión nueva, catalog/paa-questions.json y training/reports/paa/accepted.json
- [ ] bin/model check --catalog, bin/model hints check y bin/model refs terminan sin errores
- [ ] La tarea anota los bloques de la clave de bb-barbie-5611 y bb-edredon-6172 que cambian de versión y las revisiones D-179 que los tocan
- [ ] Tests en verde

## Notas

- 2026-10-30 Orden: primero los modelos de los conjuntos y después la reclasificación. classify prepare toma el catálogo de la clase del modelo del conjunto (classify.py, model_path), y compile usa los id de requisito de ese modelo. Las últimas salidas v4 están en var/runs/2026-10-29-v7-b (reglas 7) y v7r-b (3 casos, reglas 8). No reensambles dentro de esos directorios: el entrenamiento los lee.
