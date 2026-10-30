---
id: T-110
title: PAA: fundir los duplicados entre conjuntos en la pasada al catálogo
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

Que la pasada de PAA no meta dos requisitos para el mismo hecho cuando dos conjuntos lo proponen. Decisión del usuario (2026-10-30): compile avisa de los posibles duplicados, un revisor decide si son el mismo hecho y se funden en un requisito con las fuentes de todos. Caso real: mantas y sábanas metieron cat.ropa-de-casa/07 y /08 (variedad de la fibra).

## Criterios de aceptación

- [x] bin/paa compile lista los posibles duplicados: candidatos de conjuntos distintos con el mismo rasgo en el mismo bloque o en un bloque y su antepasado
- [x] bin/paa compile no escribe nada si un posible duplicado no tiene decisión, y lo dice
- [x] Las decisiones del revisor quedan en training/reports/paa/ con su motivo; un grupo fundido entra como un solo requisito, en el bloque más alto, con las fuentes de todos
- [x] La pasada se compila de nuevo sin duplicados: model check --catalog, hints check y refs sin errores; la tarea anota los grupos y su decisión
- [x] El canon recoge la regla con /docs-update
- [x] Tests en verde

## Resultado

Pasada de PAA sin duplicados: compile los lista, un revisor decide y se funden; 4 fusiones, 57 entradas en 16 bloques

## Notas

- 2026-10-30 Código (agente, 1a1af9d): bin/paa compile --duplicates lista los grupos por el árbol de Shopify (catalog.under), mismo rasgo y conjuntos distintos; borrador en var/paa/compile/duplicates.json; decisiones en training/reports/paa/merges.json (entries, same, keep, reason); un grupo con varios hechos se parte en varias decisiones; sin decisión válida, compile no escribe nada y no pasa al control. Al fundir, keep toma las fuentes paa-q de todas; la información resolutiva de las fundidas no pasa (el intake solo pide las fuentes). 62 pruebas de tests/paa en verde.
- 2026-10-30 Grupos reales (12 conjuntos): prestación en cat.ropa-de-casa y sus hijas (8 entradas: durabilidad del cubrecolchón, absorción y nivel térmico de la toalla, temporada de la funda nórdica, arrugas, resistencia al uso, transpiración); material (variedad de la fibra, mantas y sábanas); prestación en cat.sofas (durabilidad ×2, transpirabilidad, arrugas); construcción (acabado del tejido, sujeciones del relleno, sujeción de la bajera ×2); sensorial (tacto ×4).
- 2026-10-30 Canon: D-225 y paa-training 1.8 (721a04b).
- 2026-10-30 Decisiones del revisor (training/reports/paa/merges.json): fundidos variedad de la fibra (mantas:N1 queda, sabanas:N5), durabilidad del sofá (sofas-cama:N1 queda, sofas:N1), sujeción de la bajera (fundas-nordicas:inf/01 queda, sabanas:inf/02) y tacto (fundas-nordicas:N3 en cat.ropa-de-cama queda; sabanas:N1 ×2 y cubrecolchones:N2). No son el mismo hecho: las 8 prestaciones de ropa de casa, transpirabilidad y arrugas del sofá, acabado del tejido y sujeciones del relleno.
- 2026-10-30 Compilada: 57 entradas en 16 bloques, 24 requisitos nuevos (30 con los duplicados); model check --catalog correcto (515 requisitos), hints check y refs sin errores. Avisos del revisor: el tacto entra en cat.ropa-de-cama para todas sus hijas (doseles, cubrecanapés), aunque sabanas y cubrecolchones lo habían dejado más abajo; se pierde la información resolutiva de las fundidas (longitud de la fibra de sabanas:N5, fatiga del relleno de sofas:N1); toallas:N2 y fundas-nordicas:N2 (nivel térmico) entran en bloques hermanos con preguntas distintas.
