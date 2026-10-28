---
id: T-048
title: Contraste de los requisitos técnicos con fichas reales
status: pendiente
depends: T-047
milestone:
created: 2026-10-27
---

## Objetivo

Aplicar los requisitos técnicos v0.1 a una muestra de las fichas congeladas con JSON-LD y microdatos (demand-engine/var/pages/) y contrastar con Schema Markup Validator y Rich Results Test, para corregir los requisitos que no se puedan comprobar o sean ambiguos

## Criterios de aceptación

- [ ] Muestra de al menos 10 fichas de tiendas distintas, con JSON-LD y microdatos, evaluada requisito a requisito
- [ ] Contraste manual con Schema Markup Validator y Rich Results Test registrado por ficha
- [ ] Requisitos no comprobables o ambiguos corregidos con /web-reference e informe del contraste

## Notas

- 2026-10-27 De T-047: var/pages tiene 45 fichas de solo 6 tiendas (ECI 30, Burrito Blanco 9, Guaw 2, Grupo Todoplano 2, 5V Valverde 1, Kiwoko 1); 5 con Microdata, ninguna con RDFa. Para 10 tiendas hay que capturar más, con Microdata. Casos a mirar: array raíz con @graph (ws-serialization/002), productGroupId en Grupo Todoplano, AggregateRating de la Organization en Burrito Blanco, reseñas con texto en description. Lecturas discutibles a contrastar: web-audit/reference/reports/2026-10-27-primera-pasada.md (Pendiente).
- 2026-10-28 De T-067: las fichas están ahora en capture/var/pages/ (el almacén común, D-150; las 45 de T-047, sin cambios). Para las fichas nuevas de las 10 tiendas: capture/bin/pages fetch ID URL desde el host (delega en el contenedor; si no está levantado, bin/run dev up), con un ID kebab-case nuevo por ficha (uno existente se rechaza: nunca se sustituye una ficha), p. ej. tienda-producto. Robots.txt y las reservas TDM se respetan; una negativa o un desafío deja solo la evidencia en capture/var/pages/ID/ y el ID sigue libre. Cada ficha queda en capture/var/pages/ID.html (DOM renderizado) e ID.json; para Microdata, el DOM renderizado conserva los atributos itemprop.
