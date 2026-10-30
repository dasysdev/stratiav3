---
id: T-105
title: demand-model: fase PAA tras el ensamblado, con entrada provisional
status: pendiente
depends: T-102, T-104, T-107, T-109
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

/demand-model ejecuta PAA después de ensamblar el modelo: semillas de la clave del modelo con taxo, búsqueda, clasificación y entrada provisional («no compilado», encolada) en el modelo; después, nuevo ensamblado y composición por ámbito. El ensamblado lleva también la marca de comparación de cada RI (D-126). Se aplica a las 2 fichas del piloto.

## Criterios de aceptación

- [ ] bin/paa seeds MODEL.json escribe paa/<conjunto>.json con núcleo (categorías de la clave) y valores del rasgo, tomados con taxo
- [ ] Una búsqueda ya capturada con la misma semilla en otro conjunto se reutiliza y no se repite
- [ ] bin/model assemble incorpora el classified.json del conjunto como provisional: marcado «no compilado» y encolado en var/queue.jsonl
- [ ] La skill /demand-model tiene la fase PAA después del ensamblado y vuelve a ejecutar bin/model scope
- [ ] Los modelos y las unidades RI × ámbito de bb-barbie-5611 y bb-edredon-6172 se rehacen con la fase PAA y la tarea anota los RI de origen paa
- [ ] bin/model assemble copia la marca de comparación (comparison) de cada requisito al RI del modelo, en los bloques y en la capa general
- [ ] Un RI sin marca queda señalado en el modelo como pendiente de definición, sin valor por defecto (D-139)
- [ ] bin/model scope pasa la marca del RI a cada unidad RI × ámbito, sin decidirla
- [ ] Tests en verde

## Siguiente paso

Diseñar bin/paa seeds MODEL.json (clave → núcleo; taxo values → valores) y la reutilización de búsquedas por semilla; después, la entrada provisional en bin/model assemble

## Notas

- 2026-10-30 Canon: D-224 (INTAKE 2026-10-30-paa-phase-in-execution). Sección canónica en docs/10-model/paa-training.md#fase-paa-de-la-ejecución. Lo provisional de PAA va fuera de la clave, como una inferida, y en la lista de lo usado sin compilar. Rasgo de los valores sin calibrar: OQ-93.
- 2026-10-30 Alcance añadido (usuario, 2026-10-30): la marca de comparación entra en el modelo al ensamblar (D-126). assemble copia hints pero no comparison (model.py:395 y :488). info-audit la necesita para aceptar un NA de Comparabilidad (T-099).
- 2026-10-30 Saneamiento: los 2 modelos se rehacen una sola vez, con el estado más reciente: /demand-model --page (T-104) sobre las fichas audit-es, catálogo con la pasada PAA v8 (T-107) y las pistas revisadas (T-109), fase PAA de D-224 y composición con content y markup (T-102). Los modelos actuales (var/runs/live/bb-*) son anteriores a todo ello.
