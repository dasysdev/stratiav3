---
id: T-090
title: Entrenamiento: inducir las especializaciones
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Que el entrenamiento induzca las especializaciones en vez de solo medir sus divergencias (D-190); revisar el diseño con el usuario al empezar

## Criterios de aceptación

- [x] Diseño de la inducción revisado con el usuario antes de escribir código
- [x] bin/train induce las especializaciones con reglas citables y las compila
- [x] La clave inestable por el nombre de la especialización (lijadoras) desaparece en una pasada de control
- [x] Pasada de control sin empeorar e informe en training/reports/

## Resultado

Especializaciones como bloques del catálogo inducidos por el entrenamiento (D-216): sinónimos, anclaje por el árbol, puerta de métricas; reglamento v4; control sin empeorar

## Notas

- 2026-10-29 Diseño revisado con el usuario (recomendaciones aceptadas): bloques de especialización en catalog/esp/ con regla esp:<id>@<nodo>; el clasificador reutiliza por id o registra en ejecución; sinónimos fusionados de forma determinista (palabras del nombre y del disparador, misma vertical; id canónico el más frecuente); admisión solo por la puerta de métricas (sin umbral de casos); nivel por el árbol (sube a la madre con dos hijas, no pasa de las verticales); requisitos: semilla = primera propuesta registrada y lo demás, propuestas al bloque (como D-088); puerta con estabilidad de la clave y de las especializaciones. Pasada: control + 5 casos de ECI con especializaciones, A y B.
- 2026-10-29 Código: catalog/esp/ y catalog/runtime/esp/, demand/specializations.py (inducción), familia «especializaciones» en train (puerta con estabilidad de la clave, de las especializaciones y especializaciones sin compilar), model blocks/register/assemble por id (reglamento v4; v3 guardado en rulebook-v3.md), tests/demand/test_specializations.py. Reglas 7 compiladas con v6-a, v6-b, eci-a, eci-b (importancia aceptada: coherencia por requisito 52 → 11; especializaciones: solo esp.juego; esp.bateria, esp.luces y esp.compartimento-portatil, fuera del marco por no tener información resolutiva, D-063). Informe training/reports/2026-10-29-v7-report.md. Copia del catálogo previo en el scratchpad de la sesión.
- 2026-10-29 Pasada v7 (A y B, 38 casos, 51,6 M tokens): las lijadoras quedan estables (esp.a-bateria@0 en A y B; clave de ECI 3/5 → 5/5). Reglas 8: compiladas esp.a-bateria (sinónimo esp.bateria), esp.luces, esp.equitacion y esp.juego; importancia descartada por la puerta. Control: clave 14 → 13 (bota-polo-e: esp.equitacion solo en B, de existencia), composición 13 → 11 (alias Juegos de cama y nivel de la manta; no inducida, OQ-49); hechos sin pregunta 32/34 → 19/19. Informes: training/reports/2026-10-29-v8-report.md y 2026-10-29-t090-control-report.md. Canon: D-216 (docs-update, revisado).
- 2026-10-29 Repaso con el usuario de las divergencias del control: causas inducidas y guiadas por lo esperado en los casos. Reglamento v4: P4, el valor de un atributo del componente es apoyo (boot-style=Equitación; afín, solo evidencia, D-024); paso 2.3, ejemplo de la manta (Mantas, no Mantas decorativas, D-028) y la prueba de requisitos que no aplican vale para el alias (Juegos de cama en juego de fundas, D-032; la divergencia del alias ya existía en v2, v4 y v6). Verificación: var/runs/2026-10-29-v7r-a y -b con bota, las dos fundas nórdicas y la manta.
- 2026-10-29 Verificación v7r (4 casos, A y B, 19,5 M tokens): bota, las dos fundas y la manta, con clave y composición iguales en A y B y como lo esperado. Control v7 + v7r frente a v6: clave 14/14, especializaciones 14/14, composición 14/14 (13), aplicación 9/14 (8), importancia 382/382. Informe actualizado: training/reports/2026-10-29-t090-control-report.md. Consumo total de la tarea: unos 71 M tokens.
