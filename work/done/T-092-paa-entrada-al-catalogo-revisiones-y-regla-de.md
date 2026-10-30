---
id: T-092
title: PAA: entrada al catálogo, revisiones y regla de aceptación
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

Llevar a demand-engine/paa lo que fijan D-178, D-179 y D-180

## Criterios de aceptación

- [x] Lo que escribe PAA entra al compilar la pasada, como versión nueva del bloque con origen «paa», si el control no empeora (D-178)
- [x] La fuente de un requisito «paa» guarda el texto literal de la pregunta (D-178)
- [x] La compilación de taxo lee las revisiones de los classified.json (D-179)
- [x] bin/paa control decide con la regla por apartado sobre el total de conjuntos (D-180)
- [x] Tests en verde

## Resultado

bin/paa compile y control: entrada «paa» con texto literal, revisiones para taxo (D-179) y regla D-180; la ejecución real pasa a T-107

## Notas

- 2026-10-29 Repaso de incidencias (D-213): la compilación de taxo lee también las revisiones «reformular» de los classified.json, con el mismo tratamiento que separar, sacar y partir.
- 2026-10-29 Diseño aprobado por el usuario: texto literal en catalog/paa-questions.json; línea base D-180 en training/reports/paa/accepted.json (la primera pasada se acepta); train compile lista las revisiones (salida e informe del ciclo), no las aplica. bin/paa compile simulado en memoria con los 12 conjuntos: 65 entradas en 15 bloques, model check sin problemas. No se ejecutó sobre el catálogo real (catalog/ tiene cambios sin commit).
- 2026-10-30 Saneamiento (2026-10-30): el código está hecho y probado; la pasada nunca se ejecutó sobre el catálogo real. La ejecución, con el reglamento v8 y los 12 conjuntos reclasificados, pasa a T-107.
