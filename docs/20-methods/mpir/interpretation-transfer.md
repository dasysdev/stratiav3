---
id: mpir-interpretation-transfer
title: MPIR — interpretación semántica, consolidación y transferencia al modelo de demanda
layer: method
status: propuesta
version: 1.0
updated: 2026-10-24
sources: [MPIR §8, MPIR §9, MPIR §10]
---

# MPIR — interpretación semántica, consolidación y transferencia al modelo de demanda

Parte de [MPIR](README.md).

## Identificación de prácticas: análisis semántico separado

### Preguntas obligatorias de interpretación

Para cada unidad o conjunto relacionado de unidades se revisa:

1. **Qué se observa:** ¿qué contenido, estructura o mecanismo ha publicado el ecommerce, sin añadir hechos?
2. **Qué función cumple:** ¿describe, identifica, explica, relaciona, contextualiza, compara, recomienda, advierte o sustenta algo?
3. **Qué cuestión podría revelar:** ¿qué conocimiento del producto u oferta parece querer facilitar al comprador?
4. **Sobre qué objeto y condiciones:** ¿producto, variante, oferta, vendedor, uso, mercado, situación o momento?
5. **Cuál es el fundamento:** ¿qué fragmentos y relaciones justifican la interpretación?
6. **Qué no puede afirmarse:** ¿qué parte permanece ambigua, es puramente promocional o requeriría supuestos externos?

La **proximidad temática no basta** para inferir una necesidad. Una frase genérica sobre «aventura» no prueba una cuestión técnica concreta si no establece una relación informativa identificable.

### Uso de IA

Se recomienda utilizar un LLM para **proponer anotaciones estructuradas**, no para declarar unilateralmente prácticas definitivas. El analizador recibe bloques con contexto e IDs y devuelve:

- señal o señales candidatas y su función informativa;
- práctica observada formulada neutralmente;
- cuestión o cuestiones candidatas de demanda;
- entidades, alcance, aplicabilidad o condiciones sugeridos;
- citas/localizadores de soporte;
- incertidumbres, relaciones pendientes y motivos de exclusión;
- estado de revisión.

Cada salida debe ser trazable a unidades del corpus. **No se aceptan citas inventadas, atribuciones no publicadas, identidades supuestas ni preguntas inferidas solo por conocimiento externo del modelo.** Las inferencias pueden apoyarse en varias unidades enlazadas; deben explicitar las relaciones utilizadas.

### Estados de las anotaciones

- **Candidata:** interpretación plausible pendiente de contraste o revisión.
- **Sustentada:** la función informativa está apoyada por evidencia identificable y el alcance está suficientemente delimitado.
- **Pendiente por contexto:** faltan recursos, identidades o relaciones para aceptar o descartar la interpretación.
- **Descartada:** la inferencia no queda justificada, es ajena al alcance o era duplicado mal atribuido.

Estos estados controlan **la investigación del MPIR**. No son GSC, IR, ICI, indicadores técnicos ni clases de importancia de un RI ([sistemas de valoración](../../10-model/scoring-systems.md)).

### Revisión humana y consistencia

La revisión debe concentrarse en casos nuevos, fronterizos, conflictivos, potencialmente críticos para la clase y en una muestra de anotaciones rutinarias. En el piloto se comparan las anotaciones automáticas con una lectura humana de recursos seleccionados y se registran **omisiones, sobreinferencias, pérdidas de contexto y desacuerdos de clasificación**. Las reglas o instrucciones del analizador se versionan; su actualización permite reprocesar el mismo corpus.

## Consolidación interfuente: de señales a patrones

La consolidación agrupa señales por su **significado funcional**, no por igualdad literal de términos o formatos. Por ejemplo, un filtro por terreno, una guía sobre superficies húmedas y una comparación de suelas pueden apuntar a una misma necesidad de evaluar el agarre según condiciones de uso, aunque tengan formas distintas.

### Procedimiento

1. Agrupar señales candidatas por clase, dimensión, objeto y función, conservando agrupaciones cruzadas cuando proceda.
2. Proponer una descripción canónica de la práctica o patrón, sin eliminar matices que alteren la cuestión.
3. Comparar **alcance, condiciones, entidades, segmentación y fundamento**; separar patrones solo cuando la diferencia sea informativamente sustantiva.
4. Asociar todas las evidencias y fuentes de apoyo; registrar replicaciones editoriales para no inflar el contraste entre comercios.
5. Conservar variantes, excepciones y conflictos, sin fabricar consenso donde las referencias discrepan.
6. Marcar los patrones que proponen **nuevas facetas o subclases** para revisión en la [Taxonomía de clases de producto](../product-taxonomy/subclasses.md).

Un patrón puede estar sustentado en **una única fuente especializada** si su función resulta justificable. La recurrencia refuerza la observación de uso comercial, pero **no constituye una regla de aceptación, relevancia o criticidad**.

### Campos de un patrón MPIR

- ID y versión de patrón.
- Denominación y formulación neutral de la práctica informativa.
- Clase(s), faceta(s), segmentos, entidades y condiciones a las que se refiere.
- Función para la comprensión, comparación o evaluación comercial.
- Relación con otros patrones: equivalente, más general, más específico, complementario, condicionado o en conflicto.
- Lista de señales y unidades de evidencia que lo sustentan.
- Ecommerce y recursos representados; procedencia editorial y posibles dependencias.
- Variantes y contraejemplos; incertidumbres y límites interpretativos.
- Cuestiones informativas candidatas que podría fundamentar.
- Estado de revisión y trazabilidad de cambios.

## Contraste con taxonomías y transferencia al modelo de demanda

El MPIR no aprueba directamente requisitos. Ofrece **patrones, observaciones y cuestiones candidatas** que se contrastan con el inventario taxonómico y con los requisitos que se estén desarrollando para la clase.

### Tipos de aportación

| Resultado del contraste | Interpretación | Tratamiento |
|---|---|---|
| **Confirmación** | La práctica observada aporta evidencia sobre una cuestión ya inferida mediante la taxonomía. | Vincular la evidencia sin crear un RI duplicado. |
| **Ampliación** | Aparece una cuestión relevante no reconocida suficientemente en las fuentes taxonómicas. | Formular nueva cuestión candidata y justificar su pertinencia. |
| **Profundización** | Se descubre contexto, relación, desagregación o condición necesaria para formular mejor una cuestión conocida. | Revisar formulación, núcleo de conocimiento o alcance del RI candidato. |
| **Diferenciación** | La necesidad cambia para una subclase, faceta, uso o circunstancia. | Valorar requisito específico, condicionado o revisión de clase; no crear subclase automáticamente. |
| **Tensión o discrepancia** | Distintas prácticas muestran enfoques incompatibles o fronteras dudosas. | Conservar perspectivas, investigar condiciones y evitar síntesis artificial. |

### Filtro de transferencia

Antes de trasladar una cuestión al catálogo de demanda, comprobar:

1. **Necesidad de conocimiento:** ¿se formula qué debe poder determinarse sobre una oferta, no simplemente qué campo aparece o qué consejo recibe una persona?
2. **Relevancia para la clase:** ¿poder responderla desempeña un papel justificable en la comprensión, comparación o evaluación general de esa clase?
3. **Objeto y alcance:** ¿se identifica la entidad, relación, desagregación y condiciones de aplicación?
4. **Generalización prudente:** ¿la pregunta trasciende la redacción o estrategia de un comercio, sin perder diferencias relevantes?
5. **Solapamiento y fragmentación:** ¿ya existe otra pregunta equivalente o conviene separar/componer requisitos?
6. **Fundamento:** ¿qué observaciones del MPIR y/o de la taxonomía sustentan la inclusión y qué incertidumbres quedan?

La clasificación final como **crítico, principal o complementario** se realiza **en el [modelo de demanda](../../10-model/demand-model.md)**, por el papel de poder resolver la cuestión para la clase, **no** por el número de ecommerce que la mencionan. Las interfaces pertinentes ([ámbitos](../../10-model/evaluation-scopes.md)) se relacionan con los RI en la fase correspondiente, de acuerdo con la función de cada ámbito.
