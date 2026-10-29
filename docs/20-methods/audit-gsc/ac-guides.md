---
id: audit-gsc-ac-guides
title: Guías operativas de los seis criterios de aceptación
layer: method
status: propuesta
version: 0.7
updated: 2026-10-29
sources: [GSC0 §11, GSC0 Anexo B, FUND §6.2, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-29-issues-review]
---

# Guías operativas de los seis criterios de aceptación

La **condición vigente** de cada AC se cita literalmente del canon ([criterios de aceptación](../../10-model/acceptance-criteria.md)). Las pruebas y los **anclajes 0/1/2 son reglas universales provisionales V1**, pendientes de calibración.

## Cómo utilizar los anclajes

Las expresiones «fundamental», «parcial» y «material» se interpretan **respecto del RI**, nunca como porcentajes inventados ni como un umbral válido automáticamente para toda categoría de oferta.

En todos los AC, antes de asignar 0/1/2: verificar **evidencia suficiente** y **cobertura apropiada**. Los seis AC se aplican siempre; NE solo registra una incidencia, según [gsc-decision.md](gsc-decision.md) ([D-117](../../30-governance/decisions.md#d-117)). Lo que mira cada AC en un requisito concreto lo orientan sus [pistas de valoración](../../10-model/assessment-hints.md): por tipo, en Aplicabilidad y Fiabilidad; por requisito, en Precisión y Comparabilidad. No confundir una limitación de un AC con una insuficiencia universal de la respuesta.

## Concreción

**Condición vigente:** la información cubre los componentes de la cuestión con la extensión y el detalle necesarios, directamente o mediante derivaciones justificadas.

**Pruebas:** (a) desplegar componentes sustantivos y auxiliares del RI; (b) contrastar su presencia y suficiencia; (c) comprobar la desagregación por entidad; (d) identificar componentes ausentes o solo cubiertos parcialmente; (e) validar derivaciones pertinentes.

**Propiedades habituales:** P06, P07, P08, P12; otras si el hallazgo lo requiere.

| GSC | Anclaje provisional |
|---|---|
| **0** | La cobertura sustantiva de la cuestión **no queda satisfecha**: los elementos presentes, aunque pertinentes o auxiliares, no proporcionan una contribución suficiente a los componentes centrales del RI; insuficiencia acreditada mediante cobertura apropiada. En un conjunto de unidades, lo presente no cubre ninguna unidad. |
| **1** | Existe **cobertura sustantiva parcial**: se aporta información relevante sobre parte de lo solicitado, pero faltan componentes, unidades del conjunto, desagregación o condiciones materialmente necesarias. En un conjunto de unidades, basta una unidad cubierta ([D-197](../../30-governance/decisions.md#d-197)). |
| **2** | Los componentes, alcance y desagregación requeridos están **suficientemente cubiertos**, por afirmaciones directas o derivaciones justificadas. |

**Evidencias mínimas:** matriz componente del RI ↔ soporte; población/unidades del alcance cuando proceda; pruebas de ausencias; contexto y rutas de derivación.

**Fronteras:** disponibilidad efectiva 1 puede coexistir con GSC 0 en Concreción si solo se dispone, por ejemplo, de una identificación auxiliar sin el hecho solicitado. En un conjunto de unidades, si al menos una unidad está cubierta, la Concreción es 1 como mínimo; el 0 queda para cuando lo presente no cubre ninguna unidad (solo información general o auxiliar) ([D-197](../../30-governance/decisions.md#d-197)). Solo un conjunto declarado (en la pregunta o en la descripción) cuenta: una lista con «p. ej.» o «…» orienta y no forma componentes ([RI-07](ri-profile.md#procedimiento-de-elaboración-ri-01-a-ri-09)). La prueba de materialidad en RI multiatributo sigue en propuesta V1 ([OQ-22](../../30-governance/open-questions.md)); no adoptar un porcentaje universal.

## Precisión

**Condición vigente:** el significado de afirmaciones, términos, valores y relaciones puede interpretarse inequívocamente.

**Pruebas:** (a) identificar afirmaciones relevantes; (b) revisar significado, unidades, conceptos, etiquetas y relaciones; (c) buscar lecturas alternativas razonables; (d) determinar si estas cambian materialmente la respuesta o dejan parte interpretable.

**Propiedades habituales:** P08, P09, P10, P13.

| GSC | Anclaje provisional |
|---|---|
| **0** | El significado de la información necesaria **no puede determinarse suficientemente** por ambigüedades materiales que impiden interpretar la condición examinada. |
| **1** | Existe significado interpretable en una parte relevante, pero permanecen ambigüedades que limitan materialmente el juicio sobre la cuestión. |
| **2** | El significado de los componentes relevantes es **suficientemente inequívoco** para el RI, incluso si requiere equivalencias o conversiones fundamentadas. |

**Evidencias:** fragmentos originales, contexto, unidades, definiciones y lecturas alternativas materiales con su fundamento.

**Fronteras:** «disponible» puede ser un término semánticamente claro (Precisión suficiente) aunque no esté correctamente atribuido a una variante (limitación de Aplicabilidad). No duplicar sin razón una carencia de atribución como ambigüedad del significado.

## Aplicabilidad

**Condición vigente:** la información puede atribuirse con claridad a la entidad, el alcance y las condiciones concretas que plantea el requisito.

**Pruebas:** (a) enumerar entidades y condiciones del RI; (b) establecer sujeto/alcance de cada afirmación; (c) verificar identidad y vínculos; (d) comprobar cobertura de atribución para el conjunto requerido; (e) registrar atribuciones ambiguas o ausentes.

**Propiedades habituales:** P10, P11, P12 y, cuando aporta el hallazgo, P07.

| GSC | Anclaje provisional |
|---|---|
| **0** | No es posible establecer con fundamento una atribución relevante **suficiente** a la entidad o condiciones centrales del RI. |
| **1** | La atribución está acreditada para parte del conjunto o del alcance, pero subsisten vínculos, identidades o condiciones materialmente insuficientes. |
| **2** | Las afirmaciones necesarias pueden atribuirse **claramente** a las entidades, alcance y condiciones requeridos por el RI. |

**Evidencias:** sujetos, IDs, relaciones, ubicación semántica de la afirmación, canal, momento y condiciones de aplicación.

**Fronteras:** una afirmación general de disponibilidad puede ser parcialmente aplicable al modelo y no permitir atribución por cada talla; no inferir que se aplica a todas las variantes. La existencia de valor no acredita atribución.

## Comparabilidad

**Condición vigente:** la información permite efectuar o evaluar el contraste requerido sobre bases equivalentes o equivalencias justificadas.

**Pruebas:** (a) leer la **marca de dimensión de comparación** del requisito: si lo es, hay contraste aunque el RI trate de una sola oferta; (b) identificar objetos de comparación y dimensiones/condiciones; (c) determinar equivalencia de bases o conversión justificable; (d) identificar datos faltantes o asimetrías materiales; (e) evaluar si puede efectuarse el contraste solicitado.

**Propiedades habituales:** P07, P10, P12, P13.

| GSC | Anclaje provisional |
|---|---|
| **0** | El contraste requerido no puede establecerse válidamente con los elementos disponibles, por falta acreditada de bases compatibles o componentes decisivos. |
| **1** | El contraste puede efectuarse **parcialmente**, pero existen asimetrías, contextos o equivalencias que limitan materialmente su alcance o fundamento. |
| **2** | El contraste requerido puede efectuarse o evaluarse **suficientemente** con bases equivalentes o conversiones/equivalencias justificadas. |

**Evidencias:** elementos comparados, dimensiones, valores originales, unidades, condiciones equivalentes, reglas de conversión y resultado contrastable.

**Aplicación del criterio:** si la respuesta es una dimensión de comparación de la clase, Comparabilidad evalúa si se expresa sobre bases contrastables (unidad, denominación normalizada, escala oficial) ([D-118](../../30-governance/decisions.md#d-118)); la falta de datos comparables es una posible deficiencia, no una razón para NA. Si no lo es, Comparabilidad es NA según la marca de dimensión de comparación del requisito en el modelo, no por decisión del auditor ([D-126](../../30-governance/decisions.md#d-126)); es la única excepción a la aplicación de los seis AC; no asignar 0 porque no haya alternativas para una cuestión que no las requiere.

## Fiabilidad

**Condición vigente:** la información supera las comprobaciones de corrección y consistencia proporcionadas a su naturaleza: no se acreditan errores ni contradicciones materiales.

**Lectura refutadora** (canon: [acceptance-criteria](../../10-model/acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones), [D-121](../../30-governance/decisions.md#d-121), [D-122](../../30-governance/decisions.md#d-122), [D-154](../../30-governance/decisions.md#d-154)): el grado sale de las comprobaciones superadas, no de la corroboración. La auditoría no consulta fuentes externas.

**Pruebas:** (a) identificar las afirmaciones esenciales y su tipo de dato; (b) aplicar las comprobaciones de **estructura del dato**; (c) contrastar con el **conocimiento del dominio**, solo para refutar, enunciando la regla general y su fuente, o la imposibilidad física o lógica; (d) buscar contradicciones **dentro del ámbito** (entre sus representaciones y entre requisitos); (e) registrar las familias aplicadas, sus resultados y las sospechas anotadas: «sin defectos detectados en estructura, dominio y consistencia del ámbito; sin contraste externo».

**Propiedades habituales:** P14 y P16.

| GSC | Anclaje provisional |
|---|---|
| **0** | Las comprobaciones acreditan un **defecto material**: un error de corrección o una contradicción que impide considerar fiable la información para el RI. |
| **1** | Hay un **defecto no material**, o uno que afecta solo a parte de lo examinado. |
| **2** | La información **supera las comprobaciones** que tocan a ese tipo de dato: sin defectos detectados. |

**Evidencias:** afirmaciones, comprobaciones aplicadas (estructura, regla del dominio y su fuente, consistencia), pares comparables, defectos y sospechas anotadas con su motivo.

**Fronteras decisivas:**

- **Ausencia de corroboración no es falsedad, ni NE.** Un dato que nada refuta ni confirma recibe el grado de las comprobaciones superadas.
- **Sin defectos detectados no significa exacto.** El resultado dice «sin defectos detectados en…», nunca «exacto».
- **Sospecha frente a defecto.** Una regla que solo hace improbable el dato no gradúa: se anota. «Percal 100 % poliéster» no se refuta, porque existe percal de poliéster.
- **La hora de captura no acredita que el dato sea exacto ni que esté al día.** Una fecha de validez vencida en la captura sí es un defecto de estructura.
- **Conocimiento del modelo:** frena una refutación libremente, pero solo la produce con una regla general citada o una imposibilidad física o lógica. Lo que el auditor sepa de un producto, una marca o un modelo concretos es una sospecha: se anota con su motivo, no gradúa y pasa al informe como «a verificar por el ecommerce» ([D-154](../../30-governance/decisions.md#d-154)).
- **Certificaciones:** no se validan. Aquí solo cuentan estructura, dominio y consistencia (fecha de validez vencida, sello incompatible con la composición).
- **Identificador ausente:** si falta el que permitiría verificar un dato (número de certificado), cuenta en Justificación, no aquí.
- **Sintaxis frente a valor:** una sintaxis inválida del marcado es técnica; un valor imposible con sintaxis válida (dígito de control erróneo) es Fiabilidad. Si un perfil exige el valor válido, el expediente técnico lo evalúa también, sin contarlo dos veces ([D-206](../../30-governance/decisions.md#d-206)).
- **Discrepancia entre ámbitos:** es un hallazgo de [consistencia transversal](../../10-model/evaluation-scopes.md#consistencia-transversal) y no reduce este GSC.

## Justificación

**Condición vigente:** la información expuesta aporta una base identificable y suficiente para sostener y reconstruir la respuesta mediante afirmaciones y relaciones de soporte justificadas.

**Pruebas:** (a) identificar conclusión o posibles respuestas; (b) vincular cada afirmación necesaria con elementos de soporte publicados y relaciones admitidas; (c) reconstruir las rutas que conduzcan al hecho solicitado; (d) detectar saltos, supuestos o referencias que no sustentan la conclusión; (e) determinar si un tercero puede reconstruir el fundamento pertinente.

**Propiedades habituales:** P08, P17, P18 y relaciones de soporte; otras si condicionan la reconstrucción.

| GSC | Anclaje provisional |
|---|---|
| **0** | No existe base identificable suficiente para **sostener y reconstruir** la conclusión requerida: los vínculos decisivos no están fundamentados. |
| **1** | Existe una base de soporte **parcial**, pero faltan afirmaciones, relaciones o referencias materialmente necesarias para reconstruir la respuesta con el alcance solicitado. |
| **2** | Las afirmaciones y relaciones expuestas proporcionan una base **identificable, suficiente y reconstruible** para sostener la respuesta pertinente. |

**Evidencias:** afirmaciones de origen, relaciones, referencias de procedencia/contraste pertinentes, conclusiones derivadas diferenciadas de los datos originales.

**Fronteras:** justificar una respuesta **no equivale** a demostrar la corrección de cada afirmación (Fiabilidad). La falta del identificador que permitiría verificar un dato (número de certificado) cuenta aquí, no en Fiabilidad ([D-122](../../30-governance/decisions.md#d-122)). Un auditor puede conservar una captura de un dato y aun así hallar insuficiencia de trazabilidad o de relaciones ofrecidas por la información comercial. Las derivaciones fundadas no se penalizan por su número.

**Beneficio reclamado** ([D-183](../../30-governance/decisions.md#d-183)): el fundamento de un beneficio que el producto reclama («favorece la higiene dental») se valora aquí, en el requisito de esa prestación, si el modelo lo tiene. Si el modelo no tiene ese requisito, el fundamento no se audita. No hay un requisito propio para el fundamento de un beneficio.

## Separación de juicios sobre una misma observación

**Ejemplo:** «Producto disponible» en la cabecera de un modelo con variantes. *(Hipotético.)*

- Puede ser **pertinente y obtenible** → disponibilidad efectiva 1.
- Puede proporcionar **cobertura parcial** del hecho por variante → consecuencia para **Concreción**.
- Puede significar inequívocamente «disponible para compra online» → **Precisión** potencialmente suficiente.
- Puede no identificar qué talla está disponible → consecuencia para **Aplicabilidad**.
- Puede no sostener una conclusión sobre la talla 42 → consecuencia para **Justificación**.
- Su corrección no se contrasta fuera de la ficha → **Fiabilidad** según las comprobaciones superadas (estructura del dato, consistencia con el marcado), no NE ni falsedad automática.
- Si la respuesta no es una dimensión de comparación, **Comparabilidad = NA**, según la marca de dimensión de comparación del requisito ([D-126](../../30-governance/decisions.md#d-126)).

Una observación puede afectar varios AC **solo** si se razona la consecuencia **diferenciada** para cada condición. No se computan penalizaciones mecánicas ni se deduce el resultado de un AC a partir del valor de otro.

## Pregunta decisiva por AC

| AC | Pregunta antes de emitir el GSC |
|---|---|
| **Concreción** | ¿Los componentes sustantivos y el detalle del RI están suficientemente cubiertos? |
| **Precisión** | ¿Puede interpretarse inequívocamente el significado pertinente, sin lecturas materialmente alternativas? |
| **Aplicabilidad** | ¿Cada afirmación necesaria se atribuye a la entidad y las condiciones concretas del RI? |
| **Comparabilidad** | ¿Puede realizarse el contraste requerido sobre bases equivalentes o equivalencias justificadas? |
| **Fiabilidad** | ¿Qué comprobaciones de corrección y consistencia se hicieron y qué defectos acreditaron? |
| **Justificación** | ¿La respuesta se sostiene y reconstruye con afirmaciones y relaciones de soporte identificables? |

## Relacionado

- [gsc-decision.md](gsc-decision.md) — procedimiento de decisión y materialidad.
- [property-checks.md](property-checks.md) — fichas de propiedades.
- [calibration.md](calibration.md) — casos de frontera.
