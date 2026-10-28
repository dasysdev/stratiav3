---
id: T-056
title: Incluir en el motor de demanda los requisitos que salen de las referencias de datos estructurados (ámbito Web Schema.org)
status: hecha
depends: T-055, T-061
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Que el motor de demanda (demand-engine) use como fuente las propiedades que los consumidores de datos estructurados del perfil (Google Search: fichas de comerciante, variantes, políticas, organización, fragmentos) recomiendan sin exigir, para el ámbito Web Schema.org. La presencia de la propiedad en la referencia es apoyo («referencias»), no importancia: la importancia la decide el modelo, como D-052 con los PTD de Amazon. Una propiedad no es un RI por sí misma: apoya un requisito o una aportación existentes, o propone un candidato si ninguno la cubre.

## Criterios de aceptación

- [x] Diseño acordado con el usuario: vía de construcción, mapeo propiedad → requisito o aportación, cómo se marca el ámbito pertinente Web Schema.org y cómo se versiona la referencia
- [x] Mapeo de los requisitos de presencia recomendada retirados en T-055 a requisitos o aportaciones del catálogo, con los no cubiertos como candidatos
- [x] Implantado en demand-engine con pruebas en verde y modelo de ejemplo de una ficha real que muestre el apoyo «referencias» de Web Schema.org
- [x] Canon actualizado con /docs-update si el diseño introduce una vía o un origen nuevo

## Resultado

D-155: un modelo y una ficha por ámbito; 92 propiedades de Google Search como apoyo «referencias» (gen 0.8, google-search.json con contrato y candidatos), fichas web y web-schema-org, bin/model scope; 197 pruebas en verde

## Notas

- 2026-10-28 Reorganización de referencias (T-059 a T-061): las propiedades de Google Search y su versión se leen de references (lector de T-061), con la versión fijada compartida con web-audit, y se citan fuente:Tipo.propiedad@versión. Qué recomendados siguen siendo técnicos (mínimo D-147, formación estructural D-148) lo fija T-055; cómo lo recibe demand-engine (el registro de retirados como contrato entre los dos sistemas, o el canon aplicado en el mapa y contrastado con la referencia técnica) es parte del diseño de OQ-76 que se acuerda con el usuario.
- 2026-10-28 D-155 (OQ-76 cerrada, «si como dices»): un modelo de demanda y una ficha por ámbito. Diseño: (a) las 92 propiedades de retired.json (reason «modelo de demanda») se mapean a requisitos o aportaciones como apoyo «referencias» SIN ámbito (como amazon-ptd-prop), con candidatos para lo no cubierto; citas google-search-…:Tipo.propiedad@versión comprobadas con bin/model refs; (b) ficha de Web Schema.org versionada: pertinencia (todo RI pertinente; excepciones solo por función del ámbito, como reglas, nunca por falta de propiedad; previsiblemente ninguna) y localización (propiedad → aportación, que llega al perfil del RI como expresiones ilustrativas). Pendiente de implantación: dónde vive la ficha y su formato, y cómo la usa el ensamblado del modelo. Fuera de docs/ quedan menciones a OQ-76 como abierta en web-audit/reference/README.md (65, 104) y en reports/2026-10-28-retirada.md (43): actualizarlas al implantar.
- 2026-10-28 Implantado (D-155): gen.json 0.8 con 42 aportaciones apoyadas por propiedades de Google Search (21 nuevas: preparación y tránsito, días y hora límite, etiqueta, estado y país de devolución, defectuoso y reposición, NIF, descripción y web del vendedor, categoría, rango de precios, zonas sin envío, periodos de envío, fecha de opinión); gen/06, 07, 15 y 16 de «inferida» a «referencias». catalog/google-search.json 0.1: contrato con los 92 retirados de web-audit (mismos ids, cada propiedad cubierta), 11 equivalencias con atributos de Shopify (color, pattern, material y *-material, tallas, público y edad, certificaciones) y 5 candidatos (2 propuestos: programa de fidelización, origen del envío; 3 descartados: offerCount, modelo 3D y logo por D-144). catalog/scopes/web-schema-org.json y web.json 0.1 (sin excepciones; localización del catálogo + 24 propiedades exigidas o del mínimo). Código: demand/scopes.py, bin/model scope, references en el modelo y sección «Apoyo de Google Search» en el .md; check --catalog valida fichas y contrato. Modelo de ejemplo: var/runs/2026-10-28-t056/bota-polo-e (69 unidades × ámbito, 0 NA, 24 con localización). Docs: requirement-blocks 1.33, D-155 (interpretación de implantación), changelog; READMEs, CLAUDE.md, skill demand-model y web-audit/reference/README.
