---
id: T-033
title: Resolver I-26, I-27 e I-28 en la capa general y la información resolutiva
status: hecha
depends:
milestone:
created: 2026-10-26
closed: 2026-10-26
---

## Objetivo

Aplicar las decisiones del usuario sobre las incidencias abiertas en T-031: condicionados de la oferta en bloques propios, retirada de gen.precio-personalizado/01 y origen de las aportaciones normativas

## Criterios de aceptación

- [x] Decisiones registradas con /docs-update y check_docs sin errores
- [x] catalog/gen.json con gen.garantia-comercial, gen.posventa y gen.opiniones (disparador, alcance oferta) y sin gen.precio-personalizado/01; versiones al alza
- [x] Reglamento del clasificador (paso 6) con los nuevos disparadores
- [x] bin/model check --catalog correcto y bin/run dev test en verde

## Resultado

I-26, I-27 e I-28 resueltas (D-066 a D-068): bloques de garantía comercial, posventa y opiniones; sin la pregunta redundante del precio personalizado; la norma da referencias. Aprobación de las listas de la capa general registrada (D-069); nueva I-29

## Notas

- 2026-10-26 Implantado: gen.json 0.5 con gen.garantia-comercial, gen.posventa y gen.opiniones (alcance oferta; requisitos /01 con la información resolutiva aprobada) y sin gen.precio-personalizado/01 (bloque 0.3, 97.1.f en sus refs); reglamento v3, paso 0 y paso 6 con los nuevos disparadores (la garantía legal no activa gen.garantia-comercial). Ensamblado comprobado con bota-polo-e. Para T-032: las salidas antiguas no votan los requisitos nuevos, y las tres condiciones nuevas (sobre todo opiniones publicadas) pueden bajar la estabilidad de la aplicación entre ejecuciones; los casos de control comparan la aplicación como subconjunto.
- 2026-10-26 Revisión independiente aplicada (11 hallazgos): D-069 registra la aprobación de las listas de la capa general (dada en T-031); nueva I-29 (opiniones sobre la tienda frente a las del producto: decide si activan gen.opiniones); resolving.json recompilado con la capa 0.5 (reglas 6 sin cambios, catálogo sin versiones nuevas).
