---
id: T-053
title: Decidir I-48 y alinear los casos de PAA con D-141
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Resolver el alcance de «la categoría madre en general» y de las preguntas sobre el material (I-48) y dejar cases/paa coherente con la decisión

## Criterios de aceptación

- [x] I-48 resuelta con una decisión del usuario, en el canon con /docs-update y en el reglamento PAA
- [x] cases/paa de sofás cama, botas y pantuflas actualizados con la decisión (perímetro, criterios y aportaciones afectados), con why
- [x] bin/paa control sobre las cinco clasificaciones v5 de T-052 vuelve a medirse y el informe distingue lo que cambia por la decisión

## Resultado

D-146 (madre en lo heredado, material; enmienda D-141, resuelve I-48), reglamento PAA v6, casos de pantuflas/botas/sofás cama; control v6: fuera no esperados 66→6, criterios 16/16, candidatos 6/6; queda la regresión de salud del pie en pantuflas

## Notas

- 2026-10-28 Decisiones del usuario sobre I-48 (2026-10-28), tras ver los datos de la pasada v5: (1) opción B: una pregunta sobre la categoría madre va DENTRO cuando pregunta por algo que la clase hereda de su bloque (cuidado del ante → cat.calzado/13 en botas; firmeza → cat.sofas/12 en sofás cama; «¿Qué sofá me compro?» → preferencia general); va FUERA si solo tiene sentido para otro producto (calzado para la montaña, podólogos) o si es un hermano. Enmienda D-141 (que decía «la madre en general, fuera siempre») y no toca las semillas: «sofás» sigue en el núcleo de sofás cama. Descartadas: A (madre fuera siempre y semillas solo de la clase) y C (solo la madre genérica fuera). (2) Una pregunta sobre el material va DENTRO si la clase tiene o hereda ese material (como la seda en sábanas); «zapatillas» sin señal de deporte o calle se lee como la clase. Corrige la revisión de T-042 en pantuflas: «¿Cómo saber si unas zapatillas son de piel?», «¿Cómo saber si es 100% cuero?» y «¿Cuáles son los 3 tipos de cuero?» vuelven dentro y sus 3 aportaciones de cuero pasan a esperadas. Siguiente: /docs-update (enmienda de D-141, resuelve I-48), reglamento PAA v6, casos de pantuflas (y repaso de botas, sofás cama con B: la mayoría de sus preguntas de madre ya estaban dentro en los casos) y reclasificar con v6 al menos botas, pantuflas y sofás cama para medir.
- 2026-10-28 Canon: D-146 (enmienda D-141; resuelve I-48), choice-criteria 1.11, construction-routes 1.7, glosario (Producto vecino); INTAKE 2026-10-28-paa-parent-and-material; check_docs 0 errores; revisor sin problemas de fondo (2 ajustes menores aplicados). Reglamento classifier/paa.md v6 (paso 1: madre en lo heredado, material, denominación ambigua; ejemplos hipotéticos fuera del control). Casos: pantuflas (3 de cuero dentro, 3 aportaciones esperadas; podólogos y moda de zapatos siguen fuera), botas («¿Se estira el calzado de cuero?» dentro y su candidato N1 esperado; montaña y podólogos fuera), sofás cama (4 preguntas de moda sobre «sofás» dentro: el caso las tenía fuera y a la vez apoyando el criterio de moda); campo amended[] y perimeter.why (README). Control de las v5 contra los casos nuevos: var/paa/control/2026-10-28T105742/. Reclasificación v6 de botas, pantuflas y sofás cama lanzada (v5 guardada en classify/v5/).
- 2026-10-28 Control v6 (var/paa/control/2026-10-28T110313/; v5 contra los casos nuevos en 2026-10-28T105742/). Tokens v6: botas 511k, pantuflas 724k, sofás cama 738k (1,97 M). LO QUE CAMBIA SOLO POR LOS CASOS (v5 contra casos viejos → nuevos): regresiones de aportaciones 2/3 → 0/0 (cuero de pantuflas pasa a esperado); aportaciones 5/10 → 7/13; fuera 118/124 → 115/118; candidatos 5/5 → 5/6 (botas N1 pasa a esperado y v5 no lo da). LO QUE CAMBIA POR EL REGLAMENTO v6 (v5 → v6, casos nuevos): fuera no esperados 66 → 6 (la madre vuelve dentro); criterios 15/16 → 16/16 (vuelve la moda de sofás cama); candidatos 5/6 → 6/6 (botas N1); aportaciones 7/13 → 9/13 (mecanismo de sofás cama, cuero de pantuflas). LO QUE EMPEORA: el agente v6 lee como heredado lo que el usuario puso como ejemplo de fuera: podólogos y pies doloridos en pantuflas (10 preguntas dentro; vuelven el criterio salud-pie y su candidato N1: 2 regresiones) y montaña y podólogos en botas (solo perímetro). El reglamento v6 solo tiene ejemplos hipotéticos (trekking en mochilas) y no recoge la frontera de «una necesidad que sirve otro producto». Sin relación con D-146: botas 3/5 aportaciones faltan (el agente las da como pistas de cat.botas/04, cat.calzado/08 y /13); traducción al inglés de pantuflas dentro; «marcas italianas de muebles» dentro en sofás cama.
