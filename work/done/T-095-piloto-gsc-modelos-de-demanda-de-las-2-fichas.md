---
id: T-095
title: Piloto GSC: modelos de demanda de las 2 fichas de Burrito Blanco
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

demand-engine construye el modelo de demanda de las 2 fichas del piloto y lo compone por ámbito (D-155): unidades RI × ámbito de Contenido y Marcado (D-220; los ficheros siguen con los nombres del código hasta su tarea de cambio de nombre).

## Criterios de aceptación

- [x] /demand-model deja el modelo ensamblado de cada ficha y bin/model check no da errores
- [x] bin/model scope escribe por ficha CASO.web.json y CASO.web-schema-org.json con sus unidades RI × ámbito
- [x] La tarea anota la ruta de cada modelo, la clase, el número de RI por ámbito y los bloques generados sin compilar

## Resultado

Modelos de demanda y unidades RI × ámbito de las 2 fichas de Burrito Blanco: Barbie 51 RI, edredón 66 RI (bloque nuevo cat.colchas-y-edredones sin compilar)

## Notas

- 2026-10-29 Sin dependencia dura de T-094: /demand-model congela la ficha con reader. Si T-094 ya está hecha, comprobar que el modelo y la captura audit-es son del mismo producto y del mismo estado.
- 2026-10-30 Fichas reader: bb-edredon-6172 (var/pages/bb-edredon-6172/20261030T004701) y bb-barbie-5611 (var/pages/bb-barbie-5611/20261030T004718). Mismo producto y estado que las audit-es de T-094: título, canónica, precios, disponibilidad y SKU iguales.
- 2026-10-30 Barbie: demand-engine/var/runs/live/bb-barbie-5611.model.json; clase Fundas de nórdico + Fundas de almohada · juego, con descuento; 7 crítico, 24 principal, 19 complementario y 1 inferido (51 RI); web 51 unidades (22 con localización), web-schema-org 51 (22); sin bloques generados sin compilar; 1 hecho sin pregunta de 53.
- 2026-10-30 Edredón: demand-engine/var/runs/live/bb-edredon-6172.model.json; clase Colchas y edredones + Fundas de almohada (Juegos de cama) · juego, con descuento y variantes; 10 crítico, 27 principal, 29 complementario (66 RI); web 66 unidades (22 con localización), web-schema-org 66 (22); bloque generado sin compilar: cat.colchas-y-edredones (16 requisitos, 11 sin regla, catalog/runtime/; 3 pistas inferidas aceptadas por el revisor, D-211); 1 hecho sin pregunta de 57.
