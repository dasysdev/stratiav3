---
id: T-003
title: Decidir si el proyecto adopta git
status: bloqueada
depends:
milestone: harness
reason: Pendiente de decisión del usuario
created: 2026-10-24
---

## Objetivo

Diffs para revisar cambios de agentes, marcha atrás, worktrees y registro de cambios sin mantenimiento manual.

## Criterios de aceptación

- [ ] Decisión del usuario registrada; si es sí, git init con .gitignore y CLAUDE.md actualizado

## Notas

- 2026-10-24 Si se adopta git, decidir qué parte de refs/ se versiona (≈143 MB en la primera descarga, 128 MB de ellos PTD). Ver T-004.
- 2026-10-24 Decidido por el usuario: refs/ entero queda fuera de git, incluidos los manifiestos y pins.json (.gitignore).
