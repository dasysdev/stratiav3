# Campo «tipos de información que pueden resolverlo»: forma de la respuesta

*Update decidido en la conversación del 2026-10-26, tras revisar la estructura de propiedades del requisito en el canon (después de D-060). Se transcribe para su trazabilidad: las palabras del usuario, con las erratas corregidas, y el texto de la opción que eligió.*

## Antecedente

El usuario pidió: «Revisa en el canon la estructura de propiedades del requisito. ¿Qué está faltando?». En la revisión, Claude señaló que el canon (`demand-model`, FUND §3.3) nombra como registro opcional del catálogo los «tipos de información potencialmente resolutiva», sin definirlos, y que ni el método ni el catálogo los registran.

## Decisión del usuario

«Empezaremos por añadir este campo: "Tipos de información que pueden resolverlo".»

## Datos que aportó Claude

El canon solo nombra el campo, sin definición ni vocabulario. Tres lecturas, compatibles con el canon («contenidos, datos, afirmaciones y relaciones», `commercial-information`):

- **Forma de la respuesta:** valor con unidad, valor de lista, sí/no, relación, condición… Sirve a la Precisión (unidades) y a la Comparabilidad (bases equivalentes), y prepara el campo de los ámbitos pertinentes: un feed lleva valores, no políticas. En buena parte se deduce de las `sources` (los atributos de Shopify tienen listas de valores; las propiedades de Amazon, tipo o unidades), así que es objetivo y estable entre ejecuciones.
- **Soporte donde suele aparecer:** atributo estructurado, tabla, texto, imagen o etiqueta, documento, condiciones generales. Sirve a la exploración y a la prueba de cobertura (invariante 11), pero se solapa con los ámbitos pertinentes y roza la regla de no imponer formato ni ubicación (PR-06): solo podría ser orientativo.
- **Las dos**, en listas separadas.

Recomendación de Claude: la primera, porque es la que menos interpreta quien redacta y la que más rinde en la valoración de los AC.

## Opción elegida

**«Forma de la respuesta (Recomendado)»:** «Qué clase de dato o afirmación responde la cuestión, con vocabulario cerrado. Se deduce en parte de las fuentes; sirve a Precisión, Comparabilidad y a los ámbitos pertinentes.»

Vocabulario cerrado (borrador), tal como se presentó:

| Valor | Ejemplos |
|---|---|
| valor con unidad | medidas, peso, capacidad, importe, plazo |
| valor de lista | material, tipo, color, mecanismo |
| sí/no | presencia o ausencia de una característica |
| relación | variante → estado, pieza → material |
| condición | reglas con plazos, costes y excepciones |
| identidad | nombre, dirección, identificador |
| acreditación | certificado, norma, declaración |
| descripción | cómo funciona, se usa o se monta |

Ejemplos con el modelo `sofa-cama-luna`: `cat.sofas/04`, valor con unidad; `cat.sofas-cama/02`, sí/no · valor con unidad; `gen/06`, relación; `gen/11`, condición; `cat.sofas/23`, acreditación.

Opciones descartadas: «Soporte donde aparece» y «Ambas, en dos listas».
