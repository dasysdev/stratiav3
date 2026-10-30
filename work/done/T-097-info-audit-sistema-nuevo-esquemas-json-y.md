---
id: T-097
title: info-audit: sistema nuevo, esquemas JSON y validador de los registros (D-199)
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

Crear el sistema info-audit (directorio de primer nivel, miembro del workspace de uv, patrón de web-audit) con los esquemas JSON versionados de la auditoría informativa y un validador. Base de las fases 1 y 2 (D-153).

## Criterios de aceptación

- [x] info-audit/ existe como miembro del workspace de uv, con README, bin/audit y pruebas que pasan con bin/run dev test
- [x] Hay esquemas JSON versionados para la disponibilidad con su cobertura (fase 1), la evidencia con localizador y contenido original, el GSC por AC (fase 2) y las NE con la comprobación que falló
- [x] bin/audit validate rechaza: un fragmento citado que no está literal en la representación del ámbito; un 0 de disponibilidad sin registro de cobertura; AC valorados con disponibilidad 0; un NA de criterio salvo Comparabilidad en requisitos no dimensión de comparación; un GSC fuera de 0/1/2
- [x] Ningún esquema tiene campos de pesos, medias ni GSC global, ni fórmula de IR (invariantes 4, 5 y 7)
- [x] Fila de info-audit en el CLAUDE.md raíz

## Resultado

info-audit: miembro del workspace, esquemas v1 de disponibilidad y valoración y bin/audit validate (D-199, QA-15)

## Notas

- 2026-10-30 Decisión del usuario (2026-10-30): los esquemas no llevan campo de causa técnica que cite web-audit, e info-audit no depende de web-audit en el piloto.
- 2026-10-30 Validador con biblioteca estándar (subconjunto de JSON Schema; una palabra fuera del subconjunto es error). Campos con los nombres de las plantillas del método. Ámbitos del modelo: acepta Web/Web Schema.org hasta T-102. 24 pruebas de info-audit; suite completa 329 en verde. Imagen dev reconstruida (.dockerignore, Dockerfile, uv.lock).
