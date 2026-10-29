---
id: T-100
title: Revisión del piloto GSC de Burrito Blanco y calibración de la V1
status: pendiente
depends: T-099
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

El usuario revisa con Claude los GSC del piloto y aprueba los resultados esperados. Con lo aprendido, Claude ajusta el método V1 por /docs-update y deja el siguiente paso.

## Criterios de aceptación

- [ ] El usuario revisa las NE, las comprobaciones inconclusas y una muestra de GSC de cada AC; los esperados aprobados quedan guardados como casos de calibración en info-audit
- [ ] Cada divergencia entre lo emitido y lo esperado tiene su causa anotada en la tarea (regla, pista, perfil del RI o captura)
- [ ] Un intake procesado con /docs-update ajusta anclajes y reglas y anota OQ-19, OQ-20, OQ-21, OQ-22, OQ-24, OQ-27 y OQ-67; check_docs.py pasa
- [ ] Queda abierta la tarea siguiente: la skill de auditoría o una segunda ronda del piloto

## Notas
