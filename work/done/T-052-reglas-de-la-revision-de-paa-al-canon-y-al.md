---
id: T-052
title: Reglas de la revisión de PAA al canon y al reglamento v4, y comparador contra cases/paa
status: hecha
depends:
milestone:
created: 2026-10-27
closed: 2026-10-28
---

## Objetivo

Llevar al canon y al reglamento PAA las reglas que decidió el usuario al revisar los casos de control (T-042) y poder medir una pasada de PAA contra cases/paa

## Criterios de aceptación

- [x] Canon (/docs-update): preguntas sobre productos vecinos fuera del perímetro, antes de la lectura sobre la oferta y sin apoyar requisitos; la moda nunca genera (caso de la excepción de D-110)
- [x] classifier/paa.md v4 con las dos reglas y la preferencia general como criterio intermedio (D-104), con sus pruebas
- [x] Comparador de una clasificación PAA contra cases/paa/<conjunto>.json, por contenido y no por ids (perímetro, criterios, candidatos, revisiones, aportaciones; expected true/false), con informe
- [x] Pasada de control con el reglamento v4 sobre los 12 conjuntos (o una muestra acordada) y su concordancia medida

## Resultado

Canon D-141/D-142, reglamento PAA v5, comparador bin/paa control y pasada de control v5 en 5 conjuntos (regresiones de candidatos y criterios corregidas; I-48 abierta por el alcance de la madre)

## Notas

- 2026-10-27 Origen: revisión del usuario en T-042 (pasos 2 a 4; ver sus notas). Reglas: (a) preguntas sobre otro producto (la categoría madre en general o un hermano) FUERA siempre; el perímetro va antes de la lectura sobre la oferta (D-100), que solo decide si una pregunta sobre el producto de la clase pide un hecho declarable; un vecino nunca apoya requisitos (invariante 10); su presencia es señal para las semillas (D-114). (b) La moda o tendencia nunca genera (C2/C4), caso de la excepción de D-110. (c) La popularidad no genera (C4; invariante 14). (d) «El mejor» es un criterio intermedio (D-104), no «no genera». (e) La alternativa de producto no genera (C3).
- 2026-10-27 Coordinar con T-043, que también cambia classifier/paa.md (paso 8: pistas de valoración, D-125 a D-128). Conviene hacer las dos en la misma versión del reglamento (v4) o T-043 primero.
- 2026-10-28 T-043 ya publicó classifier/paa.md v4 (paso 8: pistas y marcas). Las reglas de T-052 van en v5.
- 2026-10-28 Canon: D-141 (productos vecinos fuera, el perímetro antes de la lectura sobre la oferta; enmienda D-100) y D-142 (moda nunca genera, popularidad C4, preferencia general intermedia, alternativa de producto C3); choice-criteria 1.10, construction-routes 1.6, glosario (Producto vecino). Reglamento PAA v5 con ejemplos hipotéticos de clases fuera del control (para no sesgar la pasada). Comparador: bin/paa control [SET…] (paa/control.py), por contenido; sobre las clasificaciones v3 de las que salieron los casos da 26/26 candidatos con las 4 regresiones que marcó la revisión, 306/324 fuera (faltan las 18 añadidas por la revisión).
- 2026-10-28 Pasada de control v5, muestra acordada con el usuario (pantuflas, botas, sofás cama, sofás, cojines; 2,96 M tokens: 468k, 556k, 619k, 889k, 429k). Control (var/paa/control/2026-10-28T100536/): fuera 118/124 (95 %); criterios 15/16 y 0/1 regresiones (antes la de salud del pie); candidatos 5/5 (coinciden 3: durabilidad sube a cat.mobiliario en sofás y sofás cama) y 0/3 regresiones (antes 3: pantuflas N1, botas N1, estilo de sofás cama); revisiones 5/5; aportaciones 5/10 con 2/3 regresiones (cuero en pantuflas). Las reglas nuevas corrigen las regresiones de candidatos y criterios. Lo que empeora sale de aplicar D-141 al pie de la letra: 63 preguntas más fuera (35 de «sofá» sin más en sofás cama, 18 de zapatos/calzado en botas, 8 en pantuflas) y, con ellas, aportaciones y el criterio de moda de sofás cama. Registrado como I-48 (alcance de «la madre en general» y de las preguntas de material), con propuesta; los casos se actualizan cuando el usuario decida.
