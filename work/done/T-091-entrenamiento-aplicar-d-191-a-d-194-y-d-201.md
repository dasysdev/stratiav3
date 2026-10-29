---
id: T-091
title: Entrenamiento: aplicar D-191 a D-194 y D-201
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Llevar a bin/train las reglas del repaso de OQ: dimensiones de detalle sin suelo (D-191), rasgos propuestos (D-192), aportación inferida por dos tiendas (D-193), ejecución de auditoría vigente en el paso 2 (D-194) y pistas al redactar un bloque (D-201)

## Criterios de aceptación

- [x] Las dimensiones de detalle no tienen suelo de principal en la inducción (D-191)
- [x] Sinónimos de rasgos fusionados, rasgos sin victorias retirados con registro y rasgos sin votos marcados como provisionales (D-192)
- [x] Una aportación inferida observada en dos tiendas pasa a aceptada (D-193)
- [x] Un caso de auditoría con reglamento y catálogo vigentes cuenta como una de las dos ejecuciones (D-194)
- [x] Quien redacta un bloque escribe sus pistas sin compilar y el entrenamiento las consolida (D-201)
- [x] Tests en verde y pasada de control sin empeorar

## Resultado

bin/train aplica D-191 (rasgo medida-detalle, D-219), D-192, D-193, D-194 y D-201; pasada sin empeorar

## Notas

- 2026-10-29 Hecho (2026-10-29): D-191 con el rasgo nuevo «medida-detalle» (traits.json, sin regla fija ni suelo; decisión del usuario: rasgo, no marca), la línea del suelo del reglamento v4 y las definiciones de los rasgos en bin/model blocks; los requisitos pasan a él por votos. D-192: train index fusiona sinónimos (la mitad de las palabras del nombre y la etiqueta), retira con registro («retired») el propuesto que ya no gana y lo devuelve si gana; el modelo marca y encola como provisional el requisito con un rasgo propuesto sin votos (uncompiled.provisional_traits). D-193: resolving.induce da «inferred_accepted» y for_model marca aceptada/provisional. D-194: pairs() empareja un modelo de auditoría («audit») con reglamento y reglas vigentes con una ejecución nueva (decisión del usuario: regla ya, sin datos hasta T-071). D-201: train compile numera las pistas sin id (hints.consolidate). Pasada con v7-a/b y eci-a/b: reglas siguen en 8 (candidata 9 descartada: coherencia de los modelos 0 → 1), 12 inferidas aceptadas, 0 pistas que consolidar; el índice llevó cat.cojines-decorativos/01 a medida-que-fija (2 votos, D-056) y pasa a crítico. Copia del catálogo previo en el scratchpad de la sesión.
