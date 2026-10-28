---
id: T-043
title: Adaptar el paso 8 del clasificador PAA a las pistas de valoración
status: hecha
depends:
milestone:
created: 2026-10-27
closed: 2026-10-28
---

## Objetivo

El paso 8 del clasificador de PAA deja de producir pertinencia de AC (OQ-59, superada) y produce evidencia para pistas de valoración de Precisión y Comparabilidad y para la marca de dimensión de comparación (D-125 a D-128).

## Criterios de aceptación

- [x] demand-engine/classifier/paa.md: el paso 8 habla de pistas de valoración (criterios breves con propiedad y AC afectados, no listas) y de la marca de dimensión de comparación, citando D-125 a D-128; ya no cita OQ-59 como propuesta
- [x] demand-engine/src/demand_engine/paa/README.md ya no describe la pertinencia de los AC como propuesta de OQ-59
- [x] classify.py valida el nuevo formato de salida del paso 8 y bin/run dev test pasa
- [x] Una clasificación de sábanas con el reglamento nuevo produce pistas y marcas coherentes con la prueba de assessment-hints (composición e hilos: se comparan; tamaño de cama: no)
## Resultado

Paso 8 del clasificador PAA (reglamento v4): pistas de valoración y marcas de comparación en lugar de la pertinencia de AC; prepare muestra las vigentes; check/report nuevos; sábanas coherente con la prueba

## Notas

- 2026-10-28 Reglamento PAA v4: el paso 8 escribe «hints» (pistas de requisito con propiedad y AC, sin PV-n; el código pone origen paa y apoyo) y «marks» (marca de comparación; todo candidato lleva la suya; una contraria a la vigente queda como duda). prepare enseña las pistas que ya llegan a cada requisito y su marca. T-052 subirá a v5. Ejecución anterior de sábanas guardada en classify/v3/.
- 2026-10-28 Sábanas con v4 (1,35 M tokens, 15 peticiones): 12 pistas (todas criterio, ninguna lista; no repite PV-28/29 de hilos ni las de composición) y 15 marcas. Composición sí, hilos sí y tamaño de cama no (b): confirman las vigentes; medidas en cm no (b) y color no (b), nuevas; ninguna contradice. A revisar en el entrenamiento: una pista de Justificación (P18) en la composición, que se solapa con la aportación de sustento; N1 y N6 marcados sí por duda, sin preguntas.
