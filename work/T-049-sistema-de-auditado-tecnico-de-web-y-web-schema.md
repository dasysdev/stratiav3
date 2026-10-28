---
id: T-049
title: Sistema de auditado técnico de Web y Web Schema.org
status: bloqueada
depends: T-048
milestone:
reason: Aparcada hasta tener requisitos contrastados (T-048) y el sistema cuantitativo técnico en el canon (OQ-30)
created: 2026-10-27
---

## Objetivo

Construir en web-audit el auditor técnico: extracción del marcado (primera carga y renderizado, con el motor de captura), comprobaciones de los requisitos técnicos y expediente técnico, cuando el canon tenga el sistema cuantitativo

## Criterios de aceptación

- [x] Decidida con el usuario la forma de compartir el motor de captura de demand-engine
- [ ] Sistema cuantitativo técnico fijado en el canon (OQ-30)
- [ ] Auditor que produce el expediente técnico de una URL con los estados de cada requisito

## Notas

- 2026-10-27 De T-047, decisiones de método comunes a los niveles: HTML servido o DOM renderizado (serialización usa el servido; el consumidor contempla el renderizado; JSON-LD inyectado deja serialización en NA), NE por bloque JSON-LD roto (ws-serialization/001), asimetría de términos no definidos (Microdata los exige, JSON-LD y Schema.org no), alcance en RDFa (Open Graph). Detalle: web-audit/reference/reports/2026-10-27-primera-pasada.md.
- 2026-10-28 2026-10-28 Forma de compartir el motor decidida con el usuario (T-063, alternativa B): sistema de primer nivel capture/ con el motor y el almacén de fichas congeladas comunes; se implanta en T-066 y T-067.
