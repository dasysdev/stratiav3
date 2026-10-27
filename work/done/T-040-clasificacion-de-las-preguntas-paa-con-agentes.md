---
id: T-040
title: Clasificación de las preguntas PAA con agentes
status: hecha
depends: T-038, T-039
milestone: codigo
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Clasificar con agentes las preguntas consolidadas de un conjunto PAA (perímetro, objeto: clase, marca, tienda o valorativa; contraste con el catálogo y regla C1–C4) y sacar los requisitos candidatos para el catálogo

## Criterios de aceptación

- [x] Comando o skill que clasifica questions.json de un conjunto y guarda el resultado en var/paa/sets/<conjunto>/
- [x] Conjunto sabanas clasificado: reparto por tipo y criterios de elección con sus preguntas de soporte
- [x] Requisitos candidatos (C1–C4) con su soporte, comparados con la clasificación manual de la sonda de 25 semillas (probe-20261026T204606/classified.json)
- [x] Incluida la propuesta de subir sensación térmica, resistencia y efectos sobre la piel de cat.fundas-de-almohada a cat.ropa-de-cama, y el tacto como requisito nuevo, para decidirla en el entrenamiento

## Resultado

Clasificación PAA con un agente: /paa-classify, paa classify, reglamento classifier/paa.md; sabanas clasificado, 4 candidatos «paa» (frescor, arrugas, resistencia, tacto) contrastados con la sonda manual

## Notas

- 2026-10-27 D-097: origen «paa» para requisitos que entran solo por PAA (fuentes: sus preguntas) y para inferidas que PAA confirma. demand_engine/demand/model.py (check de origen, ~l. 206-210) aún solo admite referencias/normativa/inferida: añadir «paa».
- 2026-10-27 D-099: PAA también propone requisitos desde preguntas factuales (clase, sin marca ni tienda) que ningún requisito responde, si cumplen C1–C4; origen «paa», la pregunta como fuente. Las valorativas siguen por su criterio de elección.
- 2026-10-27 OQ-58 abierta: estado y paso del entrenamiento en que entra un requisito candidato de PAA, y formato de una pregunta PAA como fuente.
- 2026-10-27 Hecho: classifier/paa.md (reglamento v1), paa/classify.py + bin/paa classify prepare|check|usage|report (host), skill /paa-classify, tests/paa/test_classify.py; model.py admite origen «paa» con fuentes paa-q: (D-097), con prueba; norm pasa a paa/text.py para importar el paquete en el host. Suite completa en verde.
- 2026-10-27 sabanas (200 preguntas, 1 agente, 980k tokens: 832k de lectura de caché, 40k de salida, 6 min): fuera 13, clase 86 (30 respondidas, 9 candidatas, 47 no generan por C2), marca 16, tienda 20, valorativas 65. 17 criterios: generan frescor-transpiración→N1, arrugas→N2, encogimiento/durabilidad/secado→N3 y tacto→N4. Cubiertos: calidad (descompuesta), material, hilos, sujeción (inf/02 + ajustables/01), abrigo (inf/01), etc. Confirmadas inf/01 e inf/02 (pasan a «paa», D-097). Resultado en var/paa/sets/sabanas/report.md.
- 2026-10-27 Candidatos, todos en cat.ropa-de-cama con rasgo prestacion: N1 frescor/transpiración (sube fundas-de-almohada/05); N2 arrugas y N3 resistencia al lavado y al uso (parten fundas-de-almohada/06 y suben las dos partes); N4 tacto (requisito nuevo, 1 pregunta). Dudas para el entrenamiento: /06 es compuesto; N2/N3 se separan solo por el voto; el tacto no tiene rasgo sensorial en el vocabulario. Mantas y protectores tienen cuestiones equivalentes fuera de la clave.
- 2026-10-27 Propuesta para decidir en el entrenamiento: subir también fundas-de-almohada/04 (efectos sobre la piel, el cabello y la almohada) a cat.ropa-de-cama. El agente no lo propuso: da por cubierta la piel en las sábanas con cat.sabanas/02 (declaraciones hipoalergénicas) y solo encontró 2 preguntas. En contra: /04 pregunta por la prestación (protección frente a ácaros, efecto en la piel), mientras sabanas/02 pregunta por certificaciones y estándares.
- 2026-10-27 Contraste con la sonda manual (161 preguntas comunes) y con sus conclusiones (choice-criteria, ejemplo mínimo): frescor, arrugas y durabilidad generan, como allí; ajuste y calidad quedan cubiertos; MKT→marca/tienda, salvo 7 preguntas de precio sin tienda que van a gen/04; OTRA→fuera 6/6; DEF/USO→C2. Novedades: el tacto como requisito y la partición de /06. Pendiente de canon (/docs-update): las líneas «Pendiente» de choice-criteria y construction-routes que citan T-040.
