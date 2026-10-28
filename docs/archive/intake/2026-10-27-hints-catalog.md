# Dónde viven las pistas de valoración

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de diseño del sistema de pistas de valoración. Continúa `INTAKE 2026-10-27-assessment-hints` y resuelve en parte su pendiente de formato (OQ-68). Ortografía de las citas normalizada.

Pregunta del usuario: «¿Dónde viven las reglas de pistas? Me interesa montar un sistema eficiente que reduzca al máximo la duplicidad, usando algún sistema de catálogo y referencias.»

## 1. Catálogo de pistas con destinatario

Claude comparó tres formas: pistas dentro de cada requisito (duplicidad alta), un catálogo de pistas en el que cada pista dice a quién va dirigida (duplicidad mínima) y un catálogo con referencias desde cada requisito (hay que mantener las referencias). Recomendó la segunda. Usuario: «podría ser» y, tras la explicación, «Así es».

- Las pistas viven en **un catálogo propio** del motor de demanda, junto al índice de rasgos y a las reglas.
- Cada pista se escribe **una sola vez** y lleva **a quién va dirigida**, con una de tres llaves:
  - **un tipo de requisito:** rasgo × entidad, o solo uno de los dos. Ejemplo: «el código de barras cumple su dígito de control» llega a todos los requisitos de identificadores;
  - **los requisitos que citan una misma fuente:** una norma, un atributo de Shopify o una propiedad de Amazon. Ejemplo: «la composición usa el nombre legal de cada fibra», dirigida a la ley de fibras, llega a todos los requisitos que la citan, en cualquier rama;
  - **un requisito concreto**, por su id. Ejemplo: «el recuento de hilos dice sobre qué superficie se cuenta» llega a `cat.sabanas/03` y, por el árbol de bloques, a todas las clases que lo heredan.
- Los requisitos **no copian ni referencian** sus pistas: se encuentran por las etiquetas que el requisito ya lleva.
- Al montar el modelo de una ficha, el motor junta las pistas de las tres llaves sin repetir ninguna. El modelo lleva las pistas resueltas; se genera, no se escribe.
- «Solo se suman» se cumple solo: se juntan todas las que encajan.

## 2. Encontrar las pistas es código, sin LLM

Usuario: «Confírmame si esto permite al sistema auditor encontrar las pistas aplicables a un requisito, si es posible mediante un sistema de etiquetado para no usar LLM. Solo con código.» Claude confirmó y el usuario: «Así es».

- Encontrar las pistas de un requisito es una **búsqueda por etiquetas exactas**, solo con código: las de su rasgo y entidad, más las de cada una de sus fuentes, más las de su id, sin repetir.
- Detalles que resuelve el código:
  - una pista dirigida a una fuente encaja con las citas de esa fuente que llevan artículo, fecha o valor (se compara por el comienzo de la etiqueta);
  - los requisitos de la capa general no tienen rasgo: sus pistas se dirigen por entidad o por id;
  - las etiquetas son controladas: el código avisa de las pistas que no llegan a ningún requisito.
- **Aplicar** las pistas a una ficha concreta lo hace el auditor razonando: el código las entrega y el auditor juzga con ellas.

## 3. Pendiente

- La marca de dimensión de comparación podría usar las mismas llaves (un valor por tipo o por fuente que el requisito precise); se decide con OQ-69.
- Campos exactos de una pista en el catálogo y su lugar en el perfil del RI (resto de OQ-68).
