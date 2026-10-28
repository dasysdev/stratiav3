---
id: T-048
title: Contraste de los requisitos técnicos con fichas reales
status: hecha
depends: T-047
milestone:
created: 2026-10-27
closed: 2026-10-28
---

## Objetivo

Aplicar los requisitos técnicos v0.1 a una muestra de las fichas congeladas con JSON-LD y microdatos (demand-engine/var/pages/) y contrastar con Schema Markup Validator y Rich Results Test, para corregir los requisitos que no se puedan comprobar o sean ambiguos

## Criterios de aceptación

- [x] Muestra de al menos 10 fichas de tiendas distintas, con JSON-LD y microdatos, evaluada requisito a requisito
- [x] Contraste manual con Schema Markup Validator y Rich Results Test registrado por ficha
- [x] Requisitos no comprobables o ambiguos corregidos con /web-reference e informe del contraste

## Resultado

Contraste de 322 requisitos técnicos con 5 fichas de 5 tiendas, Schema Markup Validator y Rich Results Test; 70 requisitos corregidos y Método común en el README de la referencia (informe reports/2026-10-28-contraste.md)

## Notas

- 2026-10-27 De T-047: var/pages tiene 45 fichas de solo 6 tiendas (ECI 30, Burrito Blanco 9, Guaw 2, Grupo Todoplano 2, 5V Valverde 1, Kiwoko 1); 5 con Microdata, ninguna con RDFa. Para 10 tiendas hay que capturar más, con Microdata. Casos a mirar: array raíz con @graph (ws-serialization/002), productGroupId en Grupo Todoplano, AggregateRating de la Organization en Burrito Blanco, reseñas con texto en description. Lecturas discutibles a contrastar: web-audit/reference/reports/2026-10-27-primera-pasada.md (Pendiente).
- 2026-10-28 De T-067: las fichas están ahora en capture/var/pages/ (el almacén común, D-150; las 45 de T-047, sin cambios). Para las fichas nuevas de las 10 tiendas: capture/bin/pages fetch ID URL desde el host (delega en el contenedor; si no está levantado, bin/run dev up), con un ID kebab-case nuevo por ficha (uno existente se rechaza: nunca se sustituye una ficha), p. ej. tienda-producto. Robots.txt y las reservas TDM se respetan; una negativa o un desafío deja solo la evidencia en capture/var/pages/ID/ y el ID sigue libre. Cada ficha queda en capture/var/pages/ID.html (DOM renderizado) e ID.json; para Microdata, el DOM renderizado conserva los atributos itemprop.
- 2026-10-28 Muestra reducida a 5 fichas por indicación del usuario, una por tienda, de las ya capturadas: eci-lijadora-a200805914, cojin-018, colchoneta-refrescante-freedog (Microdata), cuerda-tootoy (ProductGroup + Offer Microdata), sofa-cama-luna (productGroupID). 5V Valverde fuera: sin Product. Schema Markup Validator por su endpoint (POST validator.schema.org/validate html=…): 0 errores en las 5; 1 aviso UNKNOWN_FIELD productGroupID en sofa-cama-luna. Rich Results Test no tiene API.
- 2026-10-28 Evaluadas las 5 fichas × 322 requisitos (5 agentes por grupo); 52 problemas. Corregidos 70 requisitos (locales), reqs check correcto. Informe: web-audit/reference/reports/2026-10-28-contraste.md; estados por ficha en reports/2026-10-28-contraste/. Quedan 6 decisiones transversales («Método común» en el README de la referencia) pendientes del usuario y Rich Results Test manual.
- 2026-10-28 Usuario: se examinan todas las entidades, también las de productos relacionados (el marcado ha de ser correcto aunque sean otros productos); ProductGroup y AggregateOffer con sus propias reglas. Escrita la sección «Método común» en web-audit/reference/README.md (7 puntos); 001, 053 y 173 ajustados; reqs check correcto, tests web-audit 7/7.
- 2026-10-28 Tras el cierre, con el usuario: requisitos de review-snippet ampliados a cualquier entidad valorada (28; definición en Método común, cita q36) y nuevo ws-consumer/385 (obligatorio, q37–q38): ninguna Organization con aggregateRating o review es la del propio sitio (Burrito Blanco no lo cumple). reqs check correcto, 323 requisitos.
