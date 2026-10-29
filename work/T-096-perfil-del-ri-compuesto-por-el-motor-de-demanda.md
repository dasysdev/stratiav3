---
id: T-096
title: Perfil del RI compuesto por el motor de demanda (D-177)
status: pendiente
depends: T-095
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

bin/model scope añade a cada unidad RI × ámbito el perfil del RI que pide ri-profile: componentes_respuesta y aportaciones (información resolutiva), objeto, alcance y casos_frontera (descripción, partes 1 y 3), pistas_valoracion y expresiones_ejemplo. El auditor no rellena esos campos (D-177).

## Criterios de aceptación

- [ ] Cada unidad de CASO.web.json y CASO.web-schema-org.json trae los campos del perfil del RI que fija D-177, D-135 y D-155
- [ ] Un requisito sin información resolutiva o sin descripción queda señalado en la salida, no se completa
- [ ] Las 2 fichas del piloto (T-095) tienen sus unidades con el perfil del RI
- [ ] Pruebas de demand-engine en verde; demand-engine/README lo describe

## Notas
