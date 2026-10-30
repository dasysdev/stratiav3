---
id: T-107
title: PAA: primera pasada al catálogo con el reglamento v8 (D-178, D-180)
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

El catálogo compilado tiene la primera pasada de PAA con el reglamento vigente antes de rehacer los modelos del piloto. Simulación en memoria (2026-10-30, clasificaciones antiguas): 69 entradas en 17 bloques; cambian 4 de los 8 bloques de la Barbie y 3 de los 8 del edredón.

## Criterios de aceptación

- [x] Los modelos de los 12 conjuntos (campo model de paa/<SET>.json, hoy del 2026-10-26: reglamento v3, reglas 6, gen@0.5) se reensamblan en una ejecución nueva desde la última salida v4 de cada caso, con las reglas 8 y el catálogo vigente; cada paa/<SET>.json apunta a su modelo nuevo
- [x] Los 12 conjuntos de PAA se clasifican de nuevo con classifier/paa.md v8 (/paa-classify); cada classified.json registra v8 y su uso de tokens
- [x] bin/paa control sobre los 12 conjuntos deja su informe y la decisión D-180; la tarea anota el total por apartado
- [x] bin/paa compile mete la pasada en el catálogo: bloques con versión nueva, catalog/paa-questions.json y training/reports/paa/accepted.json
- [x] bin/model check --catalog, bin/model hints check y bin/model refs terminan sin errores
- [x] La tarea anota los bloques de la clave de bb-barbie-5611 y bb-edredon-6172 que cambian de versión y las revisiones D-179 que los tocan
- [x] Tests en verde

## Resultado

Primera pasada de PAA con v8: 12 conjuntos reclasificados sobre modelos v5, control sin regresiones, 63 entradas en 18 bloques

## Notas

- 2026-10-30 Orden: primero los modelos de los conjuntos y después la reclasificación. classify prepare toma el catálogo de la clase del modelo del conjunto (classify.py, model_path), y compile usa los id de requisito de ese modelo. Las últimas salidas v4 están en var/runs/2026-10-29-v7-b (reglas 7) y v7r-b (3 casos, reglas 8). No reensambles dentro de esos directorios: el entrenamiento los lee.
- 2026-10-30 Modelos de los 12 conjuntos: los del control v5 (var/runs/2026-10-30-v5-a, reglamento v5, reglas 8, catálogo con pistas 0.4); clasificaciones anteriores guardadas en classify/<versión>/ o classify/pre-<fecha>/. Corregido classify: pistas redactadas sin número (D-201) y especializaciones de la clave en check (paa.md paso 1).
- 2026-10-30 Clasificación v8 de los 12 conjuntos: 18,1 M de tokens, más las continuaciones (1,5 M por conjunto, unas 2,5 veces la anterior). Revisor de pistas: 78 aceptadas y 4 rechazadas (mantas 1, sofas-cama 3, regla 1 y regla 3), reescritas por su clasificador.
- 2026-10-30 Control (var/paa/control/2026-10-30T133356): fuera 302/317; criterios 33/33; candidatos 24/27; revisiones 13/18; aportaciones 25/37; especializaciones 1/1; 0 regresiones en todos los apartados. D-180: se acepta (primera pasada).
- 2026-10-30 Compile: 63 entradas en 18 bloques; catalog/paa-questions.json con 142 preguntas literales; training/reports/paa/accepted.json. Fuera: 2 aportaciones a la capa general (gen/01, gen/17) y N2 de mantas en una especialización propuesta (S1, eléctrica). model check --catalog correcto (521 requisitos), hints check y refs sin errores.
- 2026-10-30 Fallo de compile: una segunda ejecución sin nada nuevo sobrescribe accepted.json con 0 entradas. Restaurado desde var/paa/compile/2026-10-30T133406.json. Pendiente de corregir en compile.py: sin entradas, no reescribir la línea base.
- 2026-10-30 Claves del piloto: Barbie cambia cat.ropa-de-casa 4→5, cat.ropa-de-cama 2→3, cat.fundas-de-nordico 4→5, cat.fundas-de-almohada-y-cojines 2→3, cat.fundas-de-almohada 4→5; edredón, las mismas salvo fundas-de-nordico. Revisiones D-179 sobre esos bloques (se listan, no se aplican): fundas-nordicas R1 reformular fundas-de-nordico/05, R3 reformular fundas-de-almohada/08, R4 reformular ropa-de-casa/02, R5 partir fundas-de-almohada/04, R6 sacar fundas-de-almohada/05; sabanas R1 separar fundas-de-almohada/06, R2 sacar /05, R5 reformular /08, R6 partir /04.
- 2026-10-30 Corregido el fallo de compile (4f8a66b): sin entradas nuevas, no reescribe accepted.json; prueba en test_compile.py. Queda el criterio 7 (tests del workspace) para cuando termine T-105, que cambia el mismo código.
- 2026-10-30 Reabierta en la práctica por T-110: la pasada compilada (f7aa1e9) metió 4 grupos de duplicados entre conjuntos (variedad de la fibra, tacto, sujeción de la bajera, durabilidad del sofá) y se deshizo (76686be). La clasificación v8, el control y los modelos v5 de los conjuntos siguen valiendo; T-110 vuelve a compilar.
- 2026-10-30 Compilada de nuevo sin duplicados en T-110: 57 entradas en 16 bloques. Barbie cambia cat.ropa-de-casa 4→5, cat.ropa-de-cama 2→3, cat.fundas-de-nordico 4→5, cat.fundas-de-almohada 4→5; edredón, las mismas salvo fundas-de-nordico.
