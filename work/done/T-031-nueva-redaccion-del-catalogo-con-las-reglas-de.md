---
id: T-031
title: Nueva redacción del catálogo con las reglas de formulación (D-060)
status: hecha
depends: T-030
milestone: codigo
created: 2026-10-26
closed: 2026-10-26
---

## Objetivo

Antes de escalar a 300 fichas, aplicar a los bloques de catalog/cat las cuatro reglas de formulación de D-060, para que los votos, rasgos y reglas por requisito de T-029 se acumulen sobre cuestiones de una sola necesidad; la capa general no cambia (OQ-45)

## Criterios de aceptación

- [x] Inventario de las cuestiones afectadas en catalog/cat por regla (1 a 4), con su bloque y la redacción propuesta, en training/reports/
- [x] Bloques afectados redactados de nuevo con catalog/DRAFTING.md v3, en versión nueva: la parte principal de un requisito dividido conserva su id y las demás toman ids nuevos; condiciones en applicability; componentes sin fuente propuestos como inferidas; lo retirado, en excluded con su motivo
- [x] Información resolutiva (D-063) en todos los requisitos de categoría: aportaciones de origen «referencias» desde sus fuentes e inferidas provisionales, cada una con su componente; y listas de la capa general redactadas desde la ley y aprobadas por el usuario
- [x] bin/model check sin errores en todos los bloques y bin/run dev test en verde
- [x] induce y compile sobre eci-a, eci-b, v4-a y v4-b sin empeorar ninguna métrica, e informe en training/reports/ con cuántos requisitos cambian por regla

## Resultado

Catálogo redactado con D-060 (382 → 440 requisitos) y capa general dividida (D-065, 27 → 46); información resolutiva en los 486 requisitos; reglas 6 aceptadas sin empeorar ninguna métrica

## Notas

- 2026-10-26 Ampliada con D-061 (2026-10-26): registrar la forma de la respuesta en todos los requisitos al redactar de nuevo.
- 2026-10-26 D-061 sustituida por D-062: se retira el criterio de la forma de la respuesta; la información resolutiva no se registra hasta diseñar sus reglas (OQ-54).
- 2026-10-26 Ampliada con D-063: listas de información resolutiva de los requisitos de categoría y de la capa general (esta, con aprobación del usuario).
- 2026-10-26 Capa general dividida por decisión del usuario (D-065, dos rondas: reglas de D-060 y también partes de igual importancia): 27 → 46 requisitos, gen 0.4; listas de información resolutiva aprobadas (60 marco, 28 inferidas, 1 referencias). Catálogo: 382 → 440 requisitos (58 nuevos: 41 partes, 17 inferidas); 1310 aportaciones en los bloques de categoría (referencias con la ley en el respaldo en los normativos: I-28). Nuevo bin/model check --catalog. Reglas 6: coherencia por requisito 18 → 17 y sin regla 7 → 0 sobre el catálogo nuevo; ninguna métrica peor que las reglas 5; cat.camas-para-mascotas/08-10 pasan a principal porque cambia imp:prestacion@ap-2-9. Abiertas I-26 (condicionados de la oferta en el bloque universal) e I-27 (gen.precio-personalizado/01). Las salidas v2 no traen aportaciones: la observación de la información resolutiva se mide en T-032. Informes: training/reports/2026-10-26-t031-formulation-report.md y 2026-10-26-v6-report.md.
