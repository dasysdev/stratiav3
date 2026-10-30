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

- 2026-10-30 Entrada (T-097): las unidades de bin/model scope no llevan la marca de comparación (comparison) y el catálogo solo marca 9 de 527 requisitos. Sin la marca en la unidad, bin/audit validate rechaza todo NA de Comparabilidad (D-126). Añadir comparison a las unidades en demand-engine antes de la fase 2.
- 2026-10-30 Corrige la nota anterior: la marca de comparación la lleva el modelo del producto (D-126). bin/model assemble copia hints pero no comparison (model.py:395 y :488); que la copie y que bin/model scope la pase a la unidad. Un RI sin marca queda señalado, sin valor por defecto (D-139).
- 2026-10-30 La marca de comparación pasa a T-105.
- 2026-10-30 Riesgo (saneamiento): solo 9 de 527 requisitos tienen marca de comparación. Sin marca, el RI queda señalado (D-139) y no admite NA de Comparabilidad (D-126): casi todos los RI del piloto valoran Comparabilidad. Lo mide T-100.
