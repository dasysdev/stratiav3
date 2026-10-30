# Saneamiento de la base del piloto GSC (2026-10-30)

Origen: la sesión que dejó aplicado a los sistemas lo pendiente antes del piloto GSC de Burrito Blanco (milestone piloto-gsc-bb). Tareas: T-079, T-102, T-103, T-104, T-105, T-106, T-107, T-108 y T-109. Este artefacto lleva al canon lo que esas tareas dejaron fuera de `docs/`. No cambia ninguna regla del modelo.

## 1. Pistas de valoración retiradas y sustituidas (T-109, T-102)

- **PV-47 y PV-24 se funden en PV-48** (revisión de los avisos de D-209, T-109). Las dos pedían la norma concreta de una certificación y no solo el sello («OEKO-TEX»). PV-24 añadía la clase o el nivel. PV-48 dice: «Una certificación solo es precisa si nombra la norma o el estándar concreto que certifica y, si la norma tiene clases o niveles, con cuál se certifica: el sello o el organismo solos ("OEKO-TEX") no dicen qué se ha certificado.» Llega a los mismos 10 requisitos que PV-47. PV-47 y PV-24 quedan retiradas con fecha, porque un modelo ya las usó (D-202).
  - En `docs/10-model/assessment-hints.md`, la lista de pistas de certificaciones dice «Nueva: PV-47». Debe decir que PV-47 se retiró y que la sustituye PV-48.
- **Los otros tres avisos de D-209 no son duplicados** (gen/03: PV-21 y PV-33; gen/04: PV-20 y PV-34; gen/04: PV-20 y PV-35). El aviso queda, porque el código no tiene forma de marcar un aviso resuelto como «no dicen lo mismo». Propuesta: que la revisión de un aviso de D-209 pueda quedar registrada para que no se repita.
- **PV-13 se sustituye por PV-49** (T-102). PV-13 decía «coincide en todo el ámbito (selector, texto y, en Web, su marcado)». Con D-220, Contenido no usa el marcado, y el contraste entre el contenido y el marcado es consistencia transversal (D-124). PV-49 dice lo mismo sin el marcado.

## 2. Ejemplo del filtro Alfa con la implementación alfa/1 (T-103)

`docs/10-model/reading-filters.md`, ejemplo mínimo: dice que la composición del edredón empieza en el carácter 10.035. Ese dato salía del texto de la prueba de canarios (T-101). Con la implementación de alfa/1 sobre la ficha audit-es del piloto (`audit-bb-edredon-6172`), el texto tiene 14.208 caracteres y el panel de composición empieza en el carácter 9.638. La conclusión no cambia: queda dentro de las dos lecturas del corte de Gemini Flash (unos 12.800 caracteres).

Limitación conocida de alfa/1: `button`, `td`, `label`, `legend` y `hr` no son bloques en la especificación. Dos botones seguidos salen pegados («DescripciónEnvíos» en la ficha de canarios). Es candidata a una versión alfa/2; no se decide aquí.

## 3. Ejecución de decisiones fuera de `docs/`

- **D-220** (Contenido y Marcado): renombrados en demand-engine (fichas de ámbito `content@0.2`, sin la localización de Marcado, y `markup@0.2`; `bin/model scope` escribe `CASO.content.json` y `CASO.markup.json`), info-audit (sin la equivalencia con Web y Web Schema.org), web-audit (referencia, auditado, expediente y sus skills; los nombres de fichero y los prefijos de id no cambian), capture y references. T-102 y T-108.
- **D-221** (filtro Alfa): implementado en info-audit como `bin/audit alfa PAGE-ID` (alfa/1). T-103.
- **D-224** (fase PAA de la ejecución): implementada en demand-engine (`bin/paa seeds`, reutilización de búsquedas por semilla, `bin/model assemble --paa`) y en la skill `/demand-model`. T-105.
- **D-126 y D-139**: el modelo lleva la marca de comparación de cada RI; sin marca, el RI queda en `pending_definition`, sin valor por defecto; cada unidad RI × ámbito lleva la marca. T-105.
- **D-138**: el modelo anota la versión del catálogo de pistas (`engine.hints`). T-105.
- **D-178 y D-180**: primera pasada de PAA en el catálogo compilado, con el reglamento PAA v8 y los 12 conjuntos reclasificados sobre modelos del reglamento del clasificador v5. Control sin regresiones; 63 entradas en 18 bloques. T-107.
- El reglamento del clasificador pasa a v5 (T-079: redacción con las reglas de estilo, sin cambiar reglas) y el de PAA a v8 (T-106: ampliar un requisito solo vale para el mismo hecho).

## 4. Coste medido

- Clasificador con el reglamento v5: 2,75 M de tokens por caso de control (38,5 M en 14 casos), frente a 1,26–1,49 M con el v4. El clasificador cuenta un 11–14 % más de hechos declarados. Ninguna medida del control empeora.
- Clasificación PAA con el reglamento v8: 1,5 M de tokens por conjunto (18,1 M en 12 conjuntos). D-224 estimaba 0,7–1,3 M por clase en cada ejecución.

## 5. Cuestiones que quedan abiertas

- **OQ-93** (rasgo de los valores de las semillas): la implementación de `bin/paa seeds` toma como clase calibrada la que cita la norma de etiquetado textil (`ley:UE-1007/2011`) y aplica la regla de los textiles (tejido o, si no hay, material). Fuera de ella, la orden no elige y pide la decisión. Es una interpretación provisional; la cuestión sigue abierta.
- **Pistas provisionales sin número en la auditoría informativa.** La fase PAA (D-224) añade al modelo pistas sin `PV-n`: se numeran al compilar (D-201). El método de la auditoría informativa cita las pistas por su `PV-n` (`pistas_usadas`). Incoherencia: una pista provisional no se puede citar. Propuesta: citarla por el requisito y su posición, o por su texto, hasta que se compile.
## 6. Duplicados entre conjuntos en la pasada de PAA (decisión del usuario, T-110)

La primera pasada compilada (T-107) metió en el catálogo requisitos duplicados: dos conjuntos proponen el mismo hecho y la compilación solo descartaba la misma pregunta en el mismo bloque. Casos reales:

- variedad de la fibra: mantas («¿De qué variedad es la fibra natural de la composición (p. ej., lana merino)?») y sábanas («¿Qué variedad de fibra es (seda de morera, algodón de fibra larga…)?»), los dos en cat.ropa-de-casa;
- tacto: fundas nórdicas en cat.ropa-de-cama y sábanas en sus hijas cat.sabanas y cat.fundas-de-almohada-y-cojines (y cubrecolchones en cat.protectores-de-colchon);
- sujeción de la bajera: fundas nórdicas y sábanas, en cat.sabanas-ajustables;
- durabilidad del sofá: sofás y sofás cama, en cat.sofas.

Decisión del usuario: la pasada se rehace sin duplicados.

- Son **posibles duplicados** dos candidatos de conjuntos distintos con el mismo rasgo que entran en el mismo bloque, o en un bloque y en uno de sus antepasados.
- La compilación los lista y no escribe nada mientras un posible duplicado no tenga decisión.
- Un **revisor** decide si son el mismo hecho, con la prueba del mismo hecho del reglamento PAA (paso 3), y deja su motivo.
- Si son el mismo hecho, entra **un solo requisito**: en el bloque más alto del grupo, con las preguntas de todos los conjuntos como fuente. Si no lo son, entran los dos.
- Las decisiones quedan registradas con la pasada (training/reports/paa/).

## 7. Cuestiones que quedan abiertas (continuación)

- **Conjuntos PAA de las ejecuciones en la pasada del entrenamiento.** `bin/paa compile` sin argumentos compila todos los conjuntos clasificados, también los que crea cada ejecución. D-224 deja el entrenamiento de PAA sin cambios, pero no dice si los conjuntos de las ejecuciones entran en la pasada siguiente, ni cómo los mide el control (D-180), que solo decide sobre los conjuntos con caso de control.
