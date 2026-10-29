---
id: T-097
title: info-audit: sistema nuevo, esquemas JSON y validador de los registros (D-199)
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

Crear el sistema info-audit (directorio de primer nivel, miembro del workspace de uv, patrón de web-audit) con los esquemas JSON versionados de la auditoría informativa y un validador. Base de las fases 1 y 2 (D-153).

## Criterios de aceptación

- [ ] info-audit/ existe como miembro del workspace de uv, con README, bin/audit y pruebas que pasan con bin/run dev test
- [ ] Hay esquemas JSON versionados para la disponibilidad con su cobertura (fase 1), la evidencia con localizador y contenido original, el GSC por AC (fase 2) y las NE con la comprobación que falló
- [ ] bin/audit validate rechaza: un fragmento citado que no está literal en la representación del ámbito; un 0 de disponibilidad sin registro de cobertura; AC valorados con disponibilidad 0; un NA de criterio salvo Comparabilidad en requisitos no dimensión de comparación; un GSC fuera de 0/1/2
- [ ] Ningún esquema tiene campos de pesos, medias ni GSC global, ni fórmula de IR (invariantes 4, 5 y 7)
- [ ] Fila de info-audit en el CLAUDE.md raíz

## Notas
