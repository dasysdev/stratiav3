---
id: T-070
title: Retirar las pistas de registro de certificados (D-154)
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-29
---

## Objetivo

Aplicar D-154 al catálogo de pistas de demand-engine: la auditoría no consulta registros externos, así que las pistas que lo piden se retiran y las del alcance de la certificación pasan a Aplicabilidad.

## Criterios de aceptación

- [x] PV-39 retirada en catalog/hints.json con el motivo de D-154, sin reutilizar su número (PV-5 ya estaba retirada)
- [x] PV-40 retirada y sustituida por PV-45 (Aplicabilidad, P12, misma fuente, origen marco con apoyo D-154; PV-6 ya estaba retirada)
- [x] bin/model hints check correcto y pruebas de demand-engine en verde

## Resultado

Retiradas PV-39 y PV-40; PV-45 a PV-47 juzgan las certificaciones por lo publicado (D-154)

## Notas

- 2026-10-29 PV-5 y PV-6 ya estaban retiradas desde el 2026-10-27 (las sustituyeron PV-39 y PV-40). Además de PV-45 se añaden PV-46 (Fiabilidad, P14: fecha vencida o sello incompatible con la composición) y PV-47 (Precisión, P09: norma concreta), las dos comprobaciones que nombra D-154. Pendiente en docs: assessment-hints.md:123 dice «pendiente» y D-154 cita PV-5 y PV-6.
