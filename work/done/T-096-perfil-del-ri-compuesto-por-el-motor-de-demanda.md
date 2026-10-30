---
id: T-096
title: Perfil del RI compuesto por el motor de demanda (D-177)
status: hecha
depends: T-095
milestone: piloto-gsc-bb
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

bin/model scope añade a cada unidad RI × ámbito el perfil del RI que pide ri-profile: componentes_respuesta y aportaciones (información resolutiva), objeto, alcance y casos_frontera (descripción, partes 1 y 3), pistas_valoracion y expresiones_ejemplo. El auditor no rellena esos campos (D-177).

## Criterios de aceptación

- [x] Cada unidad de CASO.web.json y CASO.web-schema-org.json trae los campos del perfil del RI que fija D-177, D-135 y D-155
- [x] Un requisito sin información resolutiva o sin descripción queda señalado en la salida, no se completa
- [x] Las 2 fichas del piloto (T-095) tienen sus unidades con el perfil del RI
- [x] Pruebas de demand-engine en verde; demand-engine/README lo describe

## Resultado

Perfil del RI en cada unidad RI × ámbito (D-177, D-135, D-155); las 2 fichas del piloto recompuestas

## Notas

- 2026-10-30 Descripción: objeto, alcance y casos_frontera reciben el texto entero, sin cortar (decisión del usuario). Solo 5 de 1594 requisitos del catálogo tienen descripción (capa general): Barbie 47 de 51 unidades y edredón 62 de 66 quedan «sin descripción». componentes_respuesta no separa sustantivos y auxiliares: el catálogo no lo registra. Pistas: Barbie 102, edredón 114. Modelos reensamblados iguales salvo pistas y descripción.
