# Información resolutiva: qué información puede resolver cada requisito

*Update decidido en la conversación del 2026-10-26, a continuación de `INTAKE 2026-10-26-answer-form` (D-061), que sustituye. Se transcribe para su trazabilidad: las palabras del usuario, con las erratas corregidas, y el texto de la propuesta y de la opción que aprobó.*

## Antecedente

Tras D-061, el usuario pidió montar en el motor de demanda un sistema de reglas que determinara el campo («En el motor de demanda debe haber un sistema de reglas que determinan esto. ¿Cómo lo montamos?») y una muestra simulada con el modelo `sofa-cama-luna`. Claude presentó la forma de la respuesta de cada requisito resuelta por capas (marco, tipo de las fuentes, excepción por votos).

## Planteamiento del usuario

«No me convence el resultado. Revisa en el canon para qué sirve "Tipos de información que pueden resolverlo":
1. localizar información pertinente;
2. recomendación.»

## Datos que aportó Claude

- El campo está en `demand-model` entre los registros operativos del catálogo, junto a las interfaces pertinentes (FUND §3.3), sin definición. El canon lo sitúa en dos funciones:
  - **Localizar información pertinente:** «para localizar la información que puede responder un RI, el catálogo debe caracterizar su núcleo de conocimiento», y el perfil de resolución «orienta la exploración y limita las selecciones arbitrarias» (FUND §3.6). En la auditoría lo usan la exploración dirigida (L-04), la prueba de pertinencia (PF-01) y la prueba de cobertura de una ausencia (invariante 11).
  - **Recomendar:** las recomendaciones deben decir si hay que «publicar, concretar, aclarar, atribuir, normalizar, corregir, actualizar, relacionar o fundamentar» información, sobre qué entidad y en qué ámbito (FUND §9.5).
- La forma de la respuesta (D-061) describe cómo es el dato, no qué información resuelve la cuestión: no sirve para ninguna de las dos funciones. D-061 llegó a excluir la localización.

## Propuesta de Claude

«Para cada requisito, los tipos de información comercial (datos, afirmaciones, relaciones o contenidos, en palabras del canon) que pueden contribuir a resolverla, cada uno ligado al componente de la cuestión al que aporta. Límites del canon: es orientativo y no exhaustivo (RI-07); admite otras representaciones (RI-06); no impone formato ni ubicación (PR-06); no son valores esperados.»

Ejemplos con el modelo `sofa-cama-luna` (la columna «Tipos de información que pueden resolverlo» de la muestra):

| Requisito | Tipos de información que pueden resolverlo |
|---|---|
| `cat.sofas-cama/01`, medidas de la cama abierta | largo y ancho de la superficie de descanso, con unidad · altura de esa superficie al suelo · plano o imagen acotada · equivalencia con un tamaño estándar de colchón |
| `cat.sofas/07`, tapicería | nombre del material o del tejido · composición en fibras con porcentajes · material por zona (asiento, respaldo) |
| `cat.sofas/23`, normas y certificaciones | norma citada con su código (fuego, emisiones) · certificado, informe de ensayo o declaración de conformidad · sello o etiqueta · clase o resultado obtenido |

Consecuencias propuestas: «D-061: enmendar la definición, la finalidad (localizar y recomendar) y el contenido (tipos propios de cada requisito). El vocabulario de formas se retiraría, y OQ-53 dejaría de aplicar.» Las reglas del motor: «Lo diseñaría una vez fijado el contenido.» Pregunta: «¿Enmiendo D-061 con esta definición y diseñamos después las reglas sobre ella?»

## Decisión del usuario

«Sí. Lo único es en la tabla que me has dado: solo me interesa la columna "Tipos de información que pueden resolverlo" (por ahora). Antes de documentar: ¿crees que esta propiedad del requisito la podemos denominar "guía de resolución"? O propón varios términos y elijámoslo antes de documentar.»

## Denominación

Claude desaconsejó «guía de resolución» («guía» ya nombra las guías de los AC y las guías de compra del MPIR; «resolución» nombra el IR, la TRI, el estado binario de resolución y el perfil de resolución y pertinencia; suena a procedimiento y empuja a leer la lista como algo que cumplir, contra la RI-07) y propuso cuatro términos: «Información resolutiva», «Guía de resolución», «Contribuciones posibles» y «Repertorio de información».

Opción elegida: **«Información resolutiva (Recomendado)»:** «Forma corta del término que ya está en el canon (FUND §3.3, «tipos de información potencialmente resolutiva»): no crea un concepto nuevo y dice lo que contiene. La definición conserva el «potencialmente».»
