# Gobierno de las pistas de valoración y cuándo se definen

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de diseño del sistema de pistas de valoración. Claude estudió si ya estaba todo lo necesario para definir las pistas y propuso lo que faltaba. Ortografía de las citas normalizada.

Palabras del usuario: «te acepto todas las recomendaciones. Lo demás vayamos resolviendo poco a poco. Una cosa por si no ha quedado claro: mediante una pasada manual de Claude podemos construir pistas. Pero luego las pistas se irán definiendo al crear modelos de demanda, incluso cuando se realizan entrenamientos.»

## 1. Cómo nace y se acepta una pista

- Las pistas las **redactan los agentes sin aprobación del usuario**, como la información resolutiva; el usuario las revisa cuando quiere.
- Una pista **entra** si pasa unas comprobaciones automáticas: tiene los seis campos, su destino existe y es un criterio, no una lista.
- Por ahora **no hay métrica de calidad** de las pistas, porque aún no hay auditorías con las que medirla.

## 2. Cuándo se definen

- **Arranque:** una pasada manual de Claude construye un primer lote.
- **Las pistas por tipo** de ese primer lote las redacta Claude por rasgo × entidad, a partir de la guía de los AC y de las tres familias de comprobación; el entrenamiento las guarda y las coloca.
- **Después se van definiendo al crear modelos de demanda y en los entrenamientos** (palabras del usuario).

Lectura de Claude, que el usuario puede corregir: encaja en el mecanismo que ya existe. Al crear un modelo, el motor escribe también las pistas de los bloques o requisitos nuevos; quedan marcadas «sin compilar» y se encolan, como los bloques nuevos (D-045). Los entrenamientos de taxo y de PAA añaden pistas y consolidan las encoladas.

## 3. Duplicadas y contradictorias

- Antes de añadir una pista se busca si ya hay otra con el mismo destino y la misma propiedad.
- Si dice lo mismo, no se añade.
- Si la contradice, se marca como **duda** y no se suma en silencio.

## 4. Corregir una pista

- Una pista no se borra: se **retira**. Queda marcada como retirada y su número no se reutiliza.
- «Nunca se quitan» vale entre escritores, no para corregir.

## 5. Valores de `origen`

«marco» (las pistas por tipo que redacta Claude), «normativa», «referencias» y «paa».

## 6. Aclaraciones

- **Los niveles no son exclusivos.** Dicen dónde se concentran las pistas, no que un tipo solo pueda tocar dos AC (la prueba mostró una pista por tipo de Justificación: el número de certificado).
- **Ámbito.** Las pistas no dicen ámbito: el auditor las aplica a lo que vea en cada ámbito. Si algún día una pista solo tiene sentido en uno, se añade el campo.
- **Trazabilidad.** El registro del GSC cita las pistas que usó el auditor (`PV-n`), para poder reexaminar la valoración.
- **Versión.** El modelo de una ficha anota qué versión del catálogo de pistas usó, como ya hace con el catálogo de requisitos.

## 7. Orden de trabajo (aceptado)

1. Gobierno de las pistas (puntos 1, 3, 4 y 5 de este artefacto).
2. Cerrar OQ-69, la marca de comparación.
3. Piloto pequeño: escribir a mano las pistas de los nueve requisitos de sábanas de la prueba y las de sus tipos, para probar el formato antes de automatizar.
4. Con lo aprendido: el paso de taxo, el lote por tipo y la tarea de PAA (T-043).

## 8. Pendiente

- En qué paso de la creación de modelos y de los entrenamientos se escriben las pistas, y con qué material (descripciones de las propiedades de Amazon, valores de Shopify, la ley, la justificación del requisito, las preguntas de PAA).
- Métrica de calidad de las pistas, cuando haya auditorías.
