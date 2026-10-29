---
id: T-099
title: info-audit: fase 2, los seis AC por lotes y expediente del piloto
status: pendiente
depends: T-098
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

Agentes por lote de RI con disponibilidad 1 valoran los seis AC con sus pistas (OP-08…10) y info-audit ensambla el expediente y un borrador de informe de las 2 fichas, con los hallazgos de consistencia Contenido ↔ Marcado (D-124, D-220) y de alcance de lectura (D-222).

## Criterios de aceptación

- [ ] Hay un reglamento de la fase 2 en info-audit, con cada regla citando su módulo de audit-gsc o su decisión
- [ ] Cada RI con disponibilidad 1 tiene los seis AC con GSC 0/1/2, NA de Comparabilidad solo donde el modelo lo marca, o NE con la comprobación que falló
- [ ] Cada GSC cita sus evidencias y las propiedades consideradas con su efecto (D-198); las salidas pasan bin/audit validate
- [ ] El expediente de cada ficha y ámbito queda en info-audit/var/audits/AUDIT/ y el borrador de informe sigue dossier.md
- [ ] La consistencia transversal son hallazgos por RI sin escala y no cambia ningún GSC
- [ ] La lista de NE y comprobaciones inconclusas para la revisión humana (D-186) sale aparte

## Notas
