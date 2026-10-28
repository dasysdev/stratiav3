# Frontera general entre la evaluación técnica y la informativa en Web Schema.org

Fecha: 2026-10-28. Update descrito por el usuario en la sesión sobre la estructura de la auditoría y su coordinación con la calidad informativa. Responde a OQ-75. Claude clasificó los requisitos técnicos de Web Schema.org que siguen en pie (414, tras el triaje), comparó tres reglas y recomendó una. Ortografía de las citas normalizada.

Palabras del usuario:

- Planteamiento inicial: «una idea es que la evaluación técnica mire, con la representación que hay, cómo se está generando, si se cumplen las pautas y requisitos técnicos. Luego la evaluación de calidad informativa, a través de los mecanismos de disponibilidad (apoyado en lo que se considera acceso efectivo: si un dato está mal formado no se considera disponible), podemos estudiar la suficiencia informativa requerida». Y: «de las referencias se pueden extraer requisitos informativos de diferente importancia relativa que aplican al ámbito de Schema.org».
- Ante la propuesta: «lo que has recomendado. A su vez, documenta para una tarea aparte incluir en el sistema de demand-model la inclusión de requisitos provenientes de las referencias de datos estructurados (para su ámbito)».

## 1. Regla: decide la especificación (alternativa A)

- **Evaluación técnica:** cómo está construido lo que se publica, más la presencia de lo que el consumidor **exige**:
  - sintaxis y vocabulario;
  - acceso y exposición;
  - forma del valor (formatos, códigos, enumeraciones, cardinalidad);
  - estructura y relaciones;
  - completitud de lo publicado que el consumidor exige (si hay una política de envío, que tenga plazo de entrega);
  - presencia de lo que el consumidor exige (name, image y offers del Product; precio y moneda de la Offer).
- **Evaluación informativa:** si se publica lo que el consumidor solo **recomienda**, como cualquier otra cuestión del modelo de demanda: disponibilidad efectiva y criterios de aceptación.
- **El criterio es la naturaleza que fija la especificación** (obligatoria o recomendada), no un juicio del auditor. Vale igual en el primer nivel y en lo anidado.
- **Excepción:** los recomendados que no añaden un hecho, sino que sirven para interpretar un valor ya publicado, siguen en la técnica: `bestRating` y `worstRating`, la unidad del peso, la URL del logo.
- **Doble lectura, solo en lo exigido.** Si falta el precio, la técnica dice que el consumidor lo exige y falta; la informativa, que la cuestión no tiene respuesta en el ámbito. No es doble cómputo: el canon ya registra por separado la incidencia técnica y su efecto sobre la disponibilidad.
- **Mínimo de representación:** sus datos principales ya son exigidos (name, image, offers). Con esta regla, el mínimo sirve para mantener en la técnica los datos del mínimo que el consumidor recomienda sin exigir. OQ-74 queda como la lista de esos datos; candidatos: la url de la oferta, los identificadores y la marca.

## 2. Lo recomendado, al modelo de demanda del ámbito

- La presencia de lo que el consumidor recomienda sale de la referencia técnica y pasa a ser **apoyo del modelo de demanda del ámbito Web Schema.org**.
- Cuenta que la propiedad aparezca en la referencia, no su naturaleza. La importancia la decide el modelo, no Google: es lo que hizo D-052 con los PTD de Amazon.
- Una propiedad no es un requisito informativo por sí misma (un RI es una cuestión). Apoya un requisito o una aportación existentes, o propone un candidato si ninguno la cubre.
- **Incluir en el motor de demanda los requisitos que salen de las referencias de datos estructurados** es una tarea aparte (palabras del usuario): **T-056**.

## 3. La referencia técnica

- Los **126 requisitos de presencia recomendada** (48 de primer nivel y 78 de completitud) salen de la referencia técnica, salvo los datos que OQ-74 incluya en el mínimo de representación. Se conservan en un registro con su motivo, para T-056.
- Los **83 requisitos que el usuario apartó en el triaje** para tratarlos como informativos se reparten así:

| Bloque | Pasan a la informativa (presencia recomendada) | Siguen técnicos (forma o completitud exigida) |
|---|---|---|
| Atributos recomendados | 11 | 5 |
| Certificaciones | 2 | 6 |
| Fragmentos de producto | 9 | 18 |
| Reseñas y valoraciones | 7 | 25 |
| **Total** | **29** | **54** |

- La retirada en `web-audit/reference/` (estos y los 26 que no se auditan) es la tarea **T-055**, después de decidir OQ-74.

## 4. Perfil de implementación

En la tabla del perfil de Web Schema.org, lo que fija el nivel del consumidor deja de ser «propiedades exigidas y recomendadas por ese consumidor» y pasa a dos partes:

- lo que el consumidor exige → evaluación técnica;
- la presencia de lo que solo recomienda → apoyo del modelo de demanda del ámbito.

## 5. Evidencia: qué comprueban los 414 requisitos

Clasificación de Claude por lo que comprueba cada condición (aproximada, por patrones y revisada a ojo):

| Qué comprueban | Obligatorios | Recomendados |
|---|---|---|
| Sintaxis y vocabulario | 39 | 14 |
| Acceso y exposición | 9 | 5 |
| Forma del valor | 66 | 66 |
| Estructura y relaciones | 4 | 4 |
| Completitud de lo publicado | 71 | 78 |
| Presencia de primer nivel | 10 | 48 |

Unos 280 son técnicos con cualquier regla. La frontera solo afecta a los que piden que se publique algo: 136.

## 6. Alternativas descartadas

- **B, decide la función:** la técnica mira cómo está construido lo publicado más la presencia del mínimo de representación; la informativa, la presencia de cualquier hecho de contenido, aunque el consumidor lo exija. Obliga a juzgar dato a dato si es mínimo o contenido, y a separar el primer nivel de lo anidado sin un criterio firme.
- **C, todo el perfil es técnico** (el canon anterior): produce ruido, porque un producto sin una propiedad recomendada que no le es pertinente sale «no satisfecho», y la misma ausencia se informa dos veces.

## 7. Pendiente

- **OQ-74:** qué datos del mínimo de representación que el consumidor solo recomienda se quedan en la técnica.
- **T-055:** retirar los requisitos de la referencia técnica y dejar el registro de retirados.
- **T-056:** diseño e implantación en el motor de demanda (vía de construcción, mapeo propiedad → requisito o aportación, ámbito pertinente, versión de la referencia).
