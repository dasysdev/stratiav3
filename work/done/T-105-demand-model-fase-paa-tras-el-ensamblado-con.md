---
id: T-105
title: demand-model: fase PAA tras el ensamblado, con entrada provisional
status: hecha
depends: T-102, T-104, T-107, T-109, T-110
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

/demand-model ejecuta PAA después de ensamblar el modelo: semillas de la clave del modelo con taxo, búsqueda, clasificación y entrada provisional («no compilado», encolada) en el modelo; después, nuevo ensamblado y composición por ámbito. El ensamblado lleva también la marca de comparación de cada RI (D-126). Se aplica a las 2 fichas del piloto.

## Criterios de aceptación

- [x] bin/paa seeds MODEL.json escribe paa/<conjunto>.json con núcleo (categorías de la clave) y valores del rasgo, tomados con taxo
- [x] Una búsqueda ya capturada con la misma semilla en otro conjunto se reutiliza y no se repite
- [x] bin/model assemble incorpora el classified.json del conjunto como provisional: marcado «no compilado» y encolado en var/queue.jsonl
- [x] La skill /demand-model tiene la fase PAA después del ensamblado y vuelve a ejecutar bin/model scope
- [x] Los modelos y las unidades RI × ámbito de bb-barbie-5611 y bb-edredon-6172 se rehacen con la fase PAA y la tarea anota los RI de origen paa
- [x] bin/model assemble copia la marca de comparación (comparison) de cada requisito al RI del modelo, en los bloques y en la capa general
- [x] Un RI sin marca queda señalado en el modelo como pendiente de definición, sin valor por defecto (D-139)
- [x] bin/model scope pasa la marca del RI a cada unidad RI × ámbito, sin decidirla
- [x] El modelo ensamblado anota en engine la versión del catálogo de pistas que usó (D-138)
- [x] Tests en verde

## Resultado

Fase PAA en /demand-model y marca de comparación en el modelo; los 2 modelos del piloto rehechos sobre las fichas audit-es y el catálogo vigente

## Notas

- 2026-10-30 Canon: D-224 (INTAKE 2026-10-30-paa-phase-in-execution). Sección canónica en docs/10-model/paa-training.md#fase-paa-de-la-ejecución. Lo provisional de PAA va fuera de la clave, como una inferida, y en la lista de lo usado sin compilar. Rasgo de los valores sin calibrar: OQ-93.
- 2026-10-30 Alcance añadido (usuario, 2026-10-30): la marca de comparación entra en el modelo al ensamblar (D-126). assemble copia hints pero no comparison (model.py:395 y :488). info-audit la necesita para aceptar un NA de Comparabilidad (T-099).
- 2026-10-30 Saneamiento: los 2 modelos se rehacen una sola vez, con el estado más reciente: /demand-model --page (T-104) sobre las fichas audit-es, catálogo con la pasada PAA v8 (T-107) y las pistas revisadas (T-109), fase PAA de D-224 y composición con content y markup (T-102). Los modelos actuales (var/runs/live/bb-*) son anteriores a todo ello.
- 2026-10-30 Alcance añadido (saneamiento, T-109): D-138 pide que el modelo anote la versión del catálogo de pistas; engine solo lleva rulebook, rules, refs, google_search y assembled (model.py).
- 2026-10-30 Código (agente): bin/paa seeds MODEL.json (núcleo de la clave con taxo; rasgo calibrado fabric/material si el modelo cita ley:UE-1007/2011; si no, para con OQ-93), reutilización de búsquedas por semilla y mercado (SeedSet.reuse, sin DOM, fuera del tope diario), bin/model assemble --paa SET (candidatos paa/N1/<bloque> fuera de la clave; confirmaciones, aportaciones, pistas sin PV-n y marcas «no compilado»; uncompiled.paa en la cola), comparison en el modelo y en cada unidad, pending_definition.comparison, engine.hints. 167 pruebas de demand-engine; workspace en verde.
- 2026-10-30 Abierto para después: info-audit no puede citar en pistas_usadas una pista de PAA sin PV-n (el esquema exige PV-n): afecta a T-099. bin/paa compile sin argumentos compila también los conjuntos que crea cada ejecución: lo decide el entrenamiento (D-224 deja el entrenamiento de PAA sin cambios).
- 2026-10-30 La primera reconstrucción del piloto se abortó: la Barbie clasificó sobre el catálogo con duplicados y el edredón se paró (salidas y el bloque runtime fundas-de-almohada-decorativas que generó, apartados en el scratchpad aborted-pilot-run). Se rehace después de T-110.
- 2026-10-30 Criterio 5: modelos rehechos con /demand-model --page sobre las fichas audit-es, reglamento v5, reglas 8, pistas 0.4 y el catálogo con la pasada de PAA sin duplicados (T-110). Barbie (audit-bb-barbie-5611): Fundas de nórdico + Fundas de almohada · juego; 60 unidades RI × ámbito; conjunto fundas-de-nordico-fundas-de-almohada-juego (7 búsquedas reutilizadas de fundas-nordicas). Edredón (audit-bb-edredon-6172): Colchas y edredones + Fundas de almohada decorativas (Juegos de cama) · juego; 70 unidades; bloque generado cat.fundas-de-almohada-decorativas (6 requisitos, pista /01 reescrita tras el revisor); conjunto colchas-y-edredones-fundas-de-almohada-decorativas-juegos-de (7 búsquedas nuevas, 127 preguntas, sin bloqueo).
- 2026-10-30 RI de origen paa (provisional, no compilado): ningún candidato nuevo en los dos conjuntos. Barbie: 10 RI confirmados (gen/01, …), 4 aportaciones (gen/01, cat.fundas-de-nordico/03, esp.juego/01, cat.ropa-de-cama/02), 9 pistas y 5 marcas; no entran la especialización S1 «protectora» ni 1 revisión (D-179). Edredón: 16 RI confirmados (gen/16, cat.colchas-y-edredones/01, /05, …), 7 aportaciones, 7 pistas y 8 marcas; no entran 2 revisiones. Revisor de pistas: 1 rechazada en cada conjunto, reescrita. Unidades con marca de comparación: Barbie 10 de 60, edredón 14 de 70. Tokens PAA: 1,7 M (Barbie) y 1,9 M (edredón).
- 2026-10-30 Los modelos antiguos del piloto (var/runs/live/bb-barbie-5611 y bb-edredon-6172, fichas reader, unidades web/web-schema-org) quedan obsoletos: T-098 usa los casos audit-bb-*.
