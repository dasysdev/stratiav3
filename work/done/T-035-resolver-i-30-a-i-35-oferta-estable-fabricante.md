---
id: T-035
title: Resolver I-30 a I-35: oferta estable, fabricante con marca propia y política de cambios
status: hecha
depends:
milestone:
created: 2026-10-26
closed: 2026-10-26
---

## Objetivo

Aplicar las propuestas recomendadas de I-30 a I-35 (decisión del usuario del 2026-10-26) en el canon, el reglamento del clasificador y la capa general (gen.json), antes de escalar en T-029

## Criterios de aceptación

- [x] Decisiones registradas e I-30 a I-35 resueltas; módulos, glosario y changelog al día; check_docs sin errores
- [x] Reglamento del clasificador (pasos 1, 6 y 8) con las seis precisiones
- [x] catalog/gen.json: aportación de gen/17 para quien comercializa con su marca y bloque gen.cambios con su información resolutiva; bin/model check --catalog sin errores y bin/run dev test en verde

## Resultado

I-30 a I-35 resueltas (D-078 a D-083): descuento condicionado, unidad de exposición, fabricante con marca propia, garantía sin contenido, variantes y bloque gen.cambios; gen.json 0.6 y reglamento al día

## Notas

- 2026-10-26 Revisión independiente aplicada: D-078 a D-082 fieles; corregidos el porcentaje de D-078 (método y reglamento), «ni gen/13» del reglamento y la nota de cases.md (1.10). D-083, segunda ronda con el usuario: gen.cambios/01 principal; coste del cambio en un requisito propio, gen.cambios/02 (principal, paralelo a gen/26); aprobadas las cuatro aportaciones de /01. La aportación de /02 queda pendiente de aprobación (D-069). Pendiente fuera de esta tarea: expected_v1.application de cases/ sin las decisiones nuevas; CLAUDE.md raíz dice que el reglamento condensa «D-020 a D-064» (ahora D-020 a D-083). /docs-update abaratada: revisor docs-reviewer (Sonnet, solo si cambia 00-context o 10-model) y lectura por grep de los registros; el clasificador sigue con general-purpose.
- 2026-10-26 Corrección del usuario (D-085, sustituye a D-083): los cambios son condiciones de devolución y cambio, no de la oferta; se retira gen.cambios; gen/11 pregunta también por el cambio (aportaciones inferidas) y gen/26 por su coste. D-084: las listas de información resolutiva de la capa general no requieren aprobación del usuario.
