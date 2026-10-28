---
id: T-044
title: Marco de la evaluación técnica de Web Schema.org en el canon
status: hecha
depends:
milestone:
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Llevar al canon (/docs-update) el marco aprobado por el usuario el 2026-10-27 para la evaluación técnica de Web Schema.org: alcance de web-audit (solo técnico), perfil de implementación en tres niveles (serialización, vocabulario Schema.org 30.1, consumidor Google), estados del requisito técnico, función de cada clase de fuente y ubicación de la referencia (web-audit/reference/)

## Criterios de aceptación

- [x] Intake con las decisiones del usuario procesado con /docs-update y archivado
- [x] Perfil de implementación definido en el canon, con sus tres niveles y la naturaleza obligatoria o recomendada relativa al perfil
- [x] Estados del requisito técnico fijados (satisfecho, no satisfecho, NA, NE como incidencia); el sistema cuantitativo sigue abierto
- [x] Función de cada clase de fuente registrada: solo una especificación aplicable fundamenta un requisito técnico
- [x] OQ-30 acotada a lo que queda abierto y abierta la incidencia de la frontera del GTIN (sintaxis o valor)
- [x] check_docs.py con 0 errores y revisión de docs-reviewer hecha

## Resultado

Marco técnico de Web Schema.org en el canon: web-audit solo técnico, perfil de implementación (serialización, Schema.org 30.1, Google), estados, función de las fuentes y referencia en web-audit/reference/ (D-129–D-133); OQ-30 acotada; I-41 abierta

## Notas

- 2026-10-27 Decisiones del usuario (2026-10-27), respuesta al plan: «1. solo tecnico» (web-audit es solo evaluación técnica de Web y Web Schema.org); «2. si. version mas reciente 30.1 (ahora)» (perfil en tres niveles: serialización JSON-LD/Microdata/RDFa, vocabulario Schema.org fijado en 30.1, consumidor Google; Merchant Center solo para Catálogos y consistencia transversal); «3. si» (estados satisfecho / no satisfecho / NA / NE incidencia; sistema cuantitativo abierto); «4. si, A» (referencia en web-audit/reference/). Interpretación de Claude: el «si» de 2 aprueba la recomendación sin añadir consumidores (Bing u otros quedan fuera por ahora; se pueden añadir con la skill).
