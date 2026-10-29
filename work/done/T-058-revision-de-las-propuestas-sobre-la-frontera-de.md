---
id: T-058
title: Revisión de las propuestas sobre la frontera de D-146 (pies doloridos en pantuflas, montaña en botas)
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-29
---

## Objetivo

Que el usuario revise y decida las dos propuestas que salieron del control v6 (T-053) antes de tocar canon, reglamento o casos en T-057

## Criterios de aceptación

- [x] Decisión del usuario sobre la prueba propuesta para la madre: si la pregunta pide elegir un producto de la madre para una necesidad, va dentro solo si un producto de la clase es una respuesta natural; lo que la clase comparte (cuidado, material, precio) sigue dentro
- [x] Decisión del usuario sobre «¿Cuál es el mejor calzado para andar por la montaña?» en botas: vuelve dentro en el caso (cat.botas/19 cubre el uso montaña) o sigue fuera
- [x] Decisiones anotadas en T-057 con su siguiente paso

## Resultado

Decididas la prueba de la respuesta natural y la especialización nueva de montaña desde PAA

## Notas

- 2026-10-28 Contexto (control v6, var/paa/control/2026-10-28T110313/): (1) Pantuflas: el agente v6 deja dentro 10 preguntas de podólogos y pies doloridos («¿Qué calzado recomiendan los podólogos?», «¿Qué zapatos debo usar para que no me duelan los pies?»…) leyéndolas como criterio heredado; vuelven el criterio salud-pie y su candidato N1 (2 regresiones). D-146 las pone fuera («solo tiene sentido para otro producto»), pero el reglamento v6 no da una prueba operativa. Propuesta de Claude: la prueba de la respuesta natural (ver AC1); con ella podólogos fuera en pantuflas y «¿Cómo cuidar los zapatos de ante?» dentro en botas. Es una precisión de D-146: /docs-update + reglamento v7 + reclasificar pantuflas y botas (~1,2 M tokens). (2) Botas: el usuario puso «calzado para la montaña» como ejemplo de fuera, pero la clase tiene cat.botas/19 («¿Para qué uso o actividad está pensada (montaña, trabajo, nieve…)?») y el caso ya deja dentro «¿Cuáles son las 10 mejores marcas de botas de montaña?». Propuesta de Claude: la pregunta de la montaña vuelve dentro en el caso; los podólogos de botas siguen fuera. Alternativas: un ejemplo hipotético más cercano en el reglamento sin regla nueva, o aceptar la lectura del agente y cambiar los casos (contradice el ejemplo del usuario).
