---
id: T-022
title: Filtro de relevancia, magnitud física y capa general 0.3
status: hecha
depends:
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Aplicar D-050 (filtro de relevancia aprendido), D-051 (rasgo magnitud física) y D-052 (fabricante, país de fabricación y seguridad en la capa general) a la documentación y al motor de demanda

## Criterios de aceptación

- [x] D-050 a D-052 documentadas con /docs-update, validador sin errores y revisión independiente aplicada
- [x] Motor: votos «no relevante», reglas rel: inducidas y validadas (coherencia de relevancia, salvaguarda de cobertura), lista de excluidos en el modelo y relevancia dudosa
- [x] Catálogo con el rasgo magnitud y capa general 0.3; reglas recompiladas e informe de control regenerado
- [x] Pruebas de reglas y de relevancia en verde

## Resultado

D-050 a D-052: filtro de relevancia aprendido, rasgo magnitud física y capa general 0.3 (GPSR art. 19, país de fabricación); reglas 2; motor y pruebas actualizados

## Notas

- 2026-10-25 Motor: votos «no relevante» (VOTES), relevance() y protected() en catalog; model: excluidos aparte, relevancia dudosa, aplicabilidad de la capa general visible; train: relevance_points, induce_relevance, métricas de coherencia de relevancia, cobertura y requisitos sin regla. Rasgo magnitud (calzado/18, mantas/05, ropa-de-casa/05). gen.json 0.3 (gen/02-03 normativa GPSR; gen/17-20). Reglas 2 publicadas (sin regla 15 → 0; estabilidad 318 → 320; coherencia catálogo 2 → 0, modelos 7 → 4); compilados los 2 bloques generados en vivo (camas para mascotas). 15 pruebas en verde en el host. Sin votos «no relevante» todavía: las primeras reglas de relevancia saldrán de la próxima ejecución.
- 2026-10-25 Revisión independiente aplicada: gen/17 y gen/19 universales (GPSR como apoyo en su ámbito; fuera, OQ-45); gen/18 requisito condicionado a un hecho del producto dentro del bloque universal; «se queda como complementario» solo sin regla de importancia; filtro antes de la importancia (el marco no protege la relevancia de las medidas descriptivas); país de fabricación por referencias amplía D-039; I-17 retitulada; OQ-45, OQ-49 y OQ-51 anotadas.
- 2026-10-25 Pasada reducida v3 (5 casos × 2, 462 k tokens): reglas 3 publicadas por familias; relevancia aceptada (6 exclusiones: color, estampado y material en Comida para perros sin prescripción; estampado en Cubrecolchones; puntera y ocasión en Pantuflas; coherencia de relevancia 6 → 0, sin huecos de cobertura nuevos); importancia descartada (no mejora ninguna métrica). Estabilidad 5/5 en composición, clave, especializaciones y aplicación; importancia 113/113. Validación por familias en train compile. Informe runs/2026-10-25-v3-report.md.
