---
id: T-092
title: PAA: entrada al catálogo, revisiones y regla de aceptación
status: pendiente
depends:
milestone:
created: 2026-10-29
---

## Objetivo

Llevar a demand-engine/paa lo que fijan D-178, D-179 y D-180

## Criterios de aceptación

- [ ] Lo que escribe PAA entra al compilar la pasada, como versión nueva del bloque con origen «paa», si el control no empeora (D-178)
- [ ] La fuente de un requisito «paa» guarda el texto literal de la pregunta (D-178)
- [ ] La compilación de taxo lee las revisiones de los classified.json (D-179)
- [ ] bin/paa control decide con la regla por apartado sobre el total de conjuntos (D-180)
- [ ] Tests en verde

## Notas

- 2026-10-29 Repaso de incidencias (D-213): la compilación de taxo lee también las revisiones «reformular» de los classified.json, con el mismo tratamiento que separar, sacar y partir.
