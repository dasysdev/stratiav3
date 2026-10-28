---
id: T-056
title: Incluir en el motor de demanda los requisitos que salen de las referencias de datos estructurados (ámbito Web Schema.org)
status: pendiente
depends: T-055, T-061
milestone:
created: 2026-10-28
---

## Objetivo

Que el motor de demanda (demand-engine) use como fuente las propiedades que los consumidores de datos estructurados del perfil (Google Search: fichas de comerciante, variantes, políticas, organización, fragmentos) recomiendan sin exigir, para el ámbito Web Schema.org. La presencia de la propiedad en la referencia es apoyo («referencias»), no importancia: la importancia la decide el modelo, como D-052 con los PTD de Amazon. Una propiedad no es un RI por sí misma: apoya un requisito o una aportación existentes, o propone un candidato si ninguno la cubre.

## Criterios de aceptación

- [ ] Diseño acordado con el usuario: vía de construcción, mapeo propiedad → requisito o aportación, cómo se marca el ámbito pertinente Web Schema.org y cómo se versiona la referencia
- [ ] Mapeo de los requisitos de presencia recomendada retirados en T-055 a requisitos o aportaciones del catálogo, con los no cubiertos como candidatos
- [ ] Implantado en demand-engine con pruebas en verde y modelo de ejemplo de una ficha real que muestre el apoyo «referencias» de Web Schema.org
- [ ] Canon actualizado con /docs-update si el diseño introduce una vía o un origen nuevo

## Notas

- 2026-10-28 Reorganización de referencias (T-059 a T-061): las propiedades de Google Search y su versión se leen de references (lector de T-061), con la versión fijada compartida con web-audit, y se citan fuente:Tipo.propiedad@versión. Qué recomendados siguen siendo técnicos (mínimo D-147, formación estructural D-148) lo fija T-055; cómo lo recibe demand-engine (el registro de retirados como contrato entre los dos sistemas, o el canon aplicado en el mapa y contrastado con la referencia técnica) es parte del diseño de OQ-76 que se acuerda con el usuario.
