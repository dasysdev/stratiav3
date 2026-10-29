---
id: T-095
title: Piloto GSC: modelos de demanda de las 2 fichas de Burrito Blanco
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

demand-engine construye el modelo de demanda de las 2 fichas del piloto y lo compone por ámbito (D-155): unidades RI × ámbito de Contenido y Marcado (D-220; los ficheros siguen con los nombres del código hasta su tarea de cambio de nombre).

## Criterios de aceptación

- [ ] /demand-model deja el modelo ensamblado de cada ficha y bin/model check no da errores
- [ ] bin/model scope escribe por ficha CASO.web.json y CASO.web-schema-org.json con sus unidades RI × ámbito
- [ ] La tarea anota la ruta de cada modelo, la clase, el número de RI por ámbito y los bloques generados sin compilar

## Notas

- 2026-10-29 Sin dependencia dura de T-094: /demand-model congela la ficha con reader. Si T-094 ya está hecha, comprobar que el modelo y la captura audit-es son del mismo producto y del mismo estado.
