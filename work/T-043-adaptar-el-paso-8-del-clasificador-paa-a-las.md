---
id: T-043
title: Adaptar el paso 8 del clasificador PAA a las pistas de valoración
status: pendiente
depends:
milestone:
created: 2026-10-27
---

## Objetivo

El paso 8 del clasificador de PAA deja de producir pertinencia de AC (OQ-59, superada) y produce evidencia para pistas de valoración de Precisión y Comparabilidad y para la marca de dimensión de comparación (D-125 a D-128).

## Criterios de aceptación

- [ ] demand-engine/classifier/paa.md: el paso 8 habla de pistas de valoración (criterios breves con propiedad y AC afectados, no listas) y de la marca de dimensión de comparación, citando D-125 a D-128; ya no cita OQ-59 como propuesta
- [ ] demand-engine/src/demand_engine/paa/README.md ya no describe la pertinencia de los AC como propuesta de OQ-59
- [ ] classify.py valida el nuevo formato de salida del paso 8 y bin/run dev test pasa
- [ ] Una clasificación de sábanas con el reglamento nuevo produce pistas y marcas coherentes con la prueba de assessment-hints (composición e hilos: se comparan; tamaño de cama: no)

## Notas
