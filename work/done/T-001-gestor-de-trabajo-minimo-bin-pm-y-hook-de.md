---
id: T-001
title: Gestor de trabajo mínimo (bin/pm) y hook de arranque
status: hecha
depends:
milestone: harness
created: 2026-10-24
closed: 2026-10-24
---

## Objetivo

Gestión de proyectos ligera para agentes: estado calculado, una tarea por fichero, cierre que compacta (opción A, aprobada el 2026-10-24).

## Criterios de aceptación

- [x] bin/pm cubre ready, show, new, start, next, note, check, block, close y log, probado en un directorio temporal
- [x] El hook SessionStart de .claude/settings.json inyecta bin/pm ready
- [x] CLAUDE.md documenta el flujo (una tarea = una sesión, relevo con next, cierre con close)

## Resultado

bin/pm, work/, hook SessionStart y sección «Gestión del trabajo» en CLAUDE.md.

## Notas

- 2026-10-24 Diagnóstico de partida (bbb2c2026, 16 sesiones del 5 al 22-oct): los ficheros de gestión pesan ~3 % de la entrada; el grueso (~80 %) es la conversación acumulada en sesiones largas. De ahí la regla una tarea = una sesión.
