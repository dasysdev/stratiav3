---
id: T-028
title: Ciclo de entrenamiento sobre el catálogo de ECI e informe agregado
status: hecha
depends: T-027
milestone: codigo
created: 2026-10-25
closed: 2026-10-26
---

## Objetivo

Validar el sistema de entrenamiento con el piloto de 30 fichas: índice de rasgos, inducción y compilación de reglas sobre las ejecuciones de ECI y del control, pasada de control e informe agregado

## Criterios de aceptación

- [x] bin/train index, induce y compile sobre las ejecuciones de T-027; reglas aceptadas o descartadas según las métricas
- [x] Pasada de control con los 14 casos tras la compilación, sin empeorar
- [x] Informe agregado en demand-engine/training/reports/
- [x] Hallazgos metodológicos (OQ-51 con datos, entre otros) registrados con /docs-update; check_docs sin errores
- [x] Veredicto del piloto anotado en T-029: qué cambiar antes de escalar a 300

## Resultado

Ciclo de reglas 4 sobre el piloto de ECI: 161 reglas de importancia + 12 de relevancia aceptadas, 32 bloques de ejecución compilados, control v4 sin empeorar (importancia 314/314), informe 2026-10-26-v4-report.md, OQ-51 con datos, I-20 a I-22, veredicto en T-029

## Notas

- 2026-10-26 Ciclo reglas 4: train index (1003 fuentes; ambiguas amazon-ptd-prop:BOOT.toe_style prestación/estética y CE-767/2009-11.3 identidad/material); induce sobre eci-a, eci-b, v3-a, v3-b (382 etiquetas del catálogo + 1422 votos; 161 reglas de importancia + 12 de relevancia; 16 votos críticos fuera del marco); compile: las dos familias aceptadas (coherencia del catálogo 31 → 0, de los modelos 184 → 0, estabilidad de la importancia 664 → 707, sin regla 162 → 0, coherencia de relevancia 9 → 0); 32 bloques de ejecución compilados (60 en cat/, 41 con versión nueva), 5 categorías vacías de ejecución pasan al catálogo. Copia previa del catálogo en el scratchpad de la sesión.
- 2026-10-26 Código: train.pairs empareja las ejecuciones de dos en dos (A/B de cada ciclo) para la estabilidad; el acuerdo de votos del informe se resuelve con las reglas vigentes (antes usaba la importancia guardada al ensamblar, caducada en ejecuciones de reglas anteriores). Prueba test_runs_pair_in_order_given; 72 pruebas en verde.
- 2026-10-26 Pasada de control v4 (var/runs/2026-10-26-v4-a y -b, 28 agentes, 25,34 M tokens: A 13,07 M, B 12,27 M; 0,9 M por caso; 80 min de agente; sin bloques generados ni reintentos). Frente a v2 (última pasada de 14): composición 10+12 → 11+11, cuestiones clave 26+28 → 27+27, especializaciones 7+7 → 7+6, aplicación 5+6 → 5+5, inferida esperada 0+1 → 0+0, hechos sin pregunta 5+7 → 7+7: dentro de la variación A/B del clasificador, que las reglas no deciden. Estabilidad del control: composición 12 → 14/14, clave 13 → 13, especializaciones 13 → 13, aplicación 13 → 14, importancia 308 → 314/314 (v2 bajo reglas 4). Coherencia de los modelos 5 (4 son el marco D-043.6 frente a imp:material@hg-15-1-4 en mantas; 1 entre dos inferidas provisionales). Votos que coinciden con la regla: 758/1050 (control 453/658, ECI 305/392). Informe training/reports/2026-10-26-v4-report.md.
