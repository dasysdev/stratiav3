---
id: T-003
title: Decidir si el proyecto adopta git
status: hecha
depends:
milestone: harness
created: 2026-10-24
closed: 2026-10-28
---

## Objetivo

Diffs para revisar cambios de agentes, marcha atrás, worktrees y registro de cambios sin mantenimiento manual.

## Criterios de aceptación

- [x] Decisión del usuario registrada; si es sí, git init con .gitignore y CLAUDE.md actualizado

## Resultado

Git adoptado (ya en uso en main); .gitignore con los var/ desechables fuera y CLAUDE.md actualizado

## Notas

- 2026-10-24 Si se adopta git, decidir qué parte de refs/ se versiona (≈143 MB en la primera descarga, 128 MB de ellos PTD). Ver T-004.
- 2026-10-24 Decidido por el usuario: refs/ entero queda fuera de git, incluidos los manifiestos y pins.json (.gitignore).
- 2026-10-28 Decisión del usuario (2026-10-28): git adoptado; ya estaba en uso (7 commits en main). .gitignore deja fuera demand-engine/var/, capture/var/ y references/var/ (el antiguo refs/ está ahora en references/var/). CLAUDE.md actualizado: el proyecto usa git; la trazabilidad del canon sigue en changelog.md y el archivo v0.
