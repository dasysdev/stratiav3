---
id: audit-gsc-property-checks
title: Comprobación operativa de propiedades P06–P18
layer: method
status: propuesta
version: 0.4
updated: 2026-10-29
sources: [GSC0 §10, FUND §7, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-29-oq-review]
---

# Comprobación operativa de propiedades P06–P18

Las definiciones de las propiedades y sus asociaciones orientativas con los AC son canon: ver [propiedades de calidad](../../10-model/quality-properties.md). Este módulo especifica **cómo comprobarlas**.

## Método común (PR-01 a PR-09)

Las propiedades **describen características observables de información pertinente**. Se comprueban según el RI, ámbito y hallazgo. **No se valoran individualmente con GSC, 0/1/2 ni con pesos**.

**Registro** ([D-198](../../30-governance/decisions.md#d-198)): la valoración del AC lista las propiedades consideradas y su efecto en la justificación, como la [plantilla del GSC](gsc-decision.md#plantilla-de-valoración-por-ac-yaml-ilustrativo). Si una propiedad muestra un defecto, produce para ella una ficha propia con: **pregunta de comprobación, elementos examinados, método aplicado, resultado observado, evidencia, limitación y efecto específico para el AC**.

**PR-01.** Seleccionar propiedades a partir de las necesidades del AC y de los hallazgos, no mediante una lista obligatoria e idéntica para todos los RI.

**PR-02.** Formular qué condición observable se espera comprobar antes de interpretar su satisfacción.

**PR-03.** Aplicar la comprobación a la información **pertinente y utilizable** del ámbito; no ampliar el universo para completar deficiencias.

**PR-04.** Contrastar las unidades necesarias del RI: objeto, desagregación, condiciones, relaciones y componentes de respuesta.

**PR-05.** Distinguir carencia **acreditada** de imposibilidad de obtener evidencia suficiente.

**PR-06.** Evitar considerar defectuosa una representación solo por no utilizar el campo, vocabulario, orden o forma literal preferida por el auditor.

**PR-07.** Identificar cuando una propiedad incide en varios AC; motivar por separado cada repercusión.

**PR-08.** Registrar limitaciones que se refieren al **contenido comercial** sin transformarlas en evaluaciones generales de sintaxis, publicación o conformidad técnica.

**PR-09.** Una observación favorable de una propiedad no garantiza por sí sola GSC 2: el juicio corresponde a la condición íntegra del AC.

## Fichas por propiedad

Cada ficha: **Pregunta** · **Prueba** · **Evidencia** · **Precaución** · **Incidencia típica**.

### P06 · Completitud

- **Pregunta:** ¿están presentes los componentes de conocimiento necesarios para la cuestión y su alcance?
- **Prueba:** comparar el inventario de componentes del RI con afirmaciones y relaciones pertinentes efectivamente disponibles; registrar qué piezas sustantivas/auxiliares aparecen y qué ausencias han sido comprobadas.
- **Evidencia:** componentes del RI, elementos originales que los soportan y prueba de cobertura para los componentes ausentes.
- **Precaución:** no exigir atributos ajenos al RI ni confundir información de identidad con el estado solicitado. Puede existir información pertinente aunque falte la respuesta sustantiva.
- **Incidencia típica:** Concreción; también Justificación o Aplicabilidad cuando los componentes faltantes afectan su fundamento o atribución.

### P07 · Granularidad

- **Pregunta:** ¿el nivel de diferenciación de la información coincide con la desagregación que exige el RI?
- **Prueba:** comparar unidades del RI (modelo, variante, oferta, vendedor, periodo, condiciones) con las unidades a las que se refiere cada afirmación; examinar si existe vínculo suficiente para desagregar.
- **Evidencia:** enumeración del conjunto evaluado, unidades con datos, relación de estados por entidad y prueba de las unidades sin resolución.
- **Precaución:** una afirmación a nivel de modelo no equivale automáticamente a afirmaciones por variante; tampoco todo RI requiere detalle por variante.
- **Incidencia típica:** Concreción y, según la cuestión, Aplicabilidad o Comparabilidad.

### P08 · Explicitud

- **Pregunta:** ¿los hechos comerciales pueden conocerse mediante expresiones directas o derivaciones suficientemente justificadas, sin introducir suposiciones que compensen información ausente?
- **Prueba:** clasificar qué afirmaciones están publicadas, cuáles se obtienen de relaciones/operaciones sustentadas y qué conclusiones necesitarían asumir hechos no expresados.
- **Evidencia:** texto o valor original, vínculos/operaciones empleados y límites de la interpretación.
- **Precaución:** una derivación válida no se penaliza por longitud; literalidad o redundancia no son equivalentes a calidad.
- **Incidencia típica:** Concreción, Precisión o Justificación según el efecto.

### P09 · Claridad

- **Pregunta:** ¿el significado de los términos, afirmaciones y valores pertinentes puede interpretarse sin ambigüedades materiales?
- **Prueba:** identificar términos polisémicos, unidades o etiquetas no definidas, alcance ambiguo y lecturas alternativas razonables que cambien la respuesta.
- **Evidencia:** fragmento original, contexto semántico y alternativas de interpretación materialmente distintas.
- **Precaución:** no confundir dificultad técnica de lectura con ambigüedad semántica; tampoco confundir ambigüedad de significado con mera falta de atribución a una variante.
- **Incidencia típica:** Precisión.

### P10 · Estructuración semántica

- **Pregunta:** ¿se distinguen los componentes y sus relaciones significativas para la cuestión?
- **Prueba:** reconstruir sujetos, atributos, valores, agrupaciones, vínculos y condiciones; verificar si el contenido admite relaciones válidas o las presenta equívocas.
- **Evidencia:** elementos de estructura o texto donde figuran agrupaciones/vínculos, rutas de relación y posibles alternativas.
- **Precaución:** no premiar sintaxis Schema.org conforme por sí misma ni penalizar falta de marcado cuando otra representación admisible es semánticamente suficiente.
- **Incidencia típica:** Precisión, Aplicabilidad, Comparabilidad o Justificación según la consecuencia.

### P11 · Identificabilidad

- **Pregunta:** ¿las entidades que intervienen pueden distinguirse suficientemente entre sí y vincularse con la información pertinente?
- **Prueba:** confrontar productos, variantes, ofertas, vendedores e identificadores; localizar homónimos, identificadores ambiguos, referencias incompletas o uniones no acreditadas.
- **Evidencia:** denominaciones, SKU/IDs o relaciones que establecen identidad, con condiciones de alcance.
- **Precaución:** no equiparar «identificador existente» a identificación inequívoca; no exigir un tipo único de identificador si el contenido distingue adecuadamente las entidades.
- **Incidencia típica:** Aplicabilidad, Concreción o Justificación.

### P12 · Contextualización

- **Pregunta:** ¿se conocen las circunstancias necesarias para entender y aplicar las afirmaciones al RI?
- **Prueba:** examinar periodo, mercado, canal, unidad, configuración, oferta y condiciones comerciales relevantes; distinguir contextos exigidos del RI de detalles accesorios.
- **Evidencia:** condiciones publicadas, asociación con afirmaciones, alcance y momentos.
- **Precaución:** no exigir por defecto todas las circunstancias posibles; exigir las que cambian materialmente el significado, cobertura o aplicabilidad.
- **Incidencia típica:** Concreción, Aplicabilidad, Precisión, Comparabilidad.

### P13 · Normalización

- **Pregunta:** ¿los conceptos, unidades, categorías y referencias permiten las equivalencias justificadas que necesita el RI?
- **Prueba:** identificar bases de medida o convenciones y probar conversiones/equivalencias cuando sean necesarias para interpretar o contrastar valores.
- **Evidencia:** valores y unidades originales, convención de referencia, regla de equivalencia y resultado derivado.
- **Precaución:** no imponer formatos idénticos; una conversión fundamentada puede ser suficiente. La falta de normalización solo afecta el GSC si perjudica una condición relevante.
- **Incidencia típica:** Precisión y Comparabilidad.

### P14 · Exactitud

- **Pregunta:** ¿qué comprobaciones sustentan la correspondencia de la afirmación con un hecho comercial comprobable?
- **Prueba:** identificar la afirmación y su tipo de dato; aplicar las comprobaciones de estructura del dato y de conocimiento del dominio (solo refuta, con la regla general y su fuente, o una imposibilidad física o lógica), sin fuentes externas ([D-122](../../30-governance/decisions.md#d-122), [D-154](../../30-governance/decisions.md#d-154)); documentar defectos, sospechas y alcance de la verificación.
- **Evidencia:** dato publicado, comprobación aplicada y fuente de la regla, momento, método y resultado, sin confundir la ausencia de defectos con certeza.
- **Precaución:** falta de contraste no prueba falsedad; coincidencia de dos representaciones del mismo origen no demuestra exactitud; un dato sin defectos detectados no es por ello exacto.
- **Incidencia típica:** Fiabilidad.

### P15 · Actualidad (retirada)

Retirada porque no hay forma de evaluarla ([D-123](../../30-governance/decisions.md#d-123)). Una fecha de validez vencida en la captura se trata como defecto de estructura del dato (P14); un feed desfasado, como hallazgo de [consistencia transversal](../../10-model/evaluation-scopes.md#consistencia-transversal).

### P16 · Coherencia

- **Pregunta:** ¿son compatibles entre sí las afirmaciones sobre la misma realidad comercial bajo condiciones y momentos comparables?
- **Prueba:** comparar afirmaciones internas y entre representaciones admitidas; verificar identidad, unidades, condiciones y tiempo antes de concluir contradicción.
- **Evidencia:** pares/conjuntos de afirmaciones originales, metadatos de sujeto/alcance/momento y explicación del conflicto o compatibilidad.
- **Precaución:** ausencia de contradicción no demuestra exactitud; diferencias legítimas de oferta, canal o instante no son incoherencias materiales.
- **Incidencia típica:** Fiabilidad y, según el caso, Precisión o Justificación.

### P17 · Trazabilidad

- **Pregunta:** ¿puede identificarse y seguirse la procedencia y trayectoria relevante de la información que sustenta una respuesta?
- **Prueba:** buscar autoría, fuente, versiones, referencias o cadenas de origen de las afirmaciones cuando sean pertinentes para la cuestión; distinguir la trazabilidad del ecommerce de la que crea el expediente auditor.
- **Evidencia:** referencias, registros y relaciones de procedencia efectivamente expuestos o identificables; límites de la cadena.
- **Precaución:** registrar una URL o un fragmento como auditor no convierte automáticamente la afirmación comercial en trazable.
- **Incidencia típica:** Justificación; puede contribuir a Fiabilidad cuando sustenta comprobaciones.

### P18 · Verificabilidad

- **Pregunta:** ¿las afirmaciones pueden contrastarse mediante pruebas o referencias pertinentes y suficientemente identificables?
- **Prueba:** determinar qué evidencia o referencia podría contrastar la afirmación, si es accesible bajo el método y qué alcance tiene el contraste; distinguir posibilidad de contrastar de comprobación ya concluida.
- **Evidencia:** referencias verificables, procedimiento de contraste, resultados obtenidos o límites documentados.
- **Precaución:** la posibilidad de contrastar un dato no prueba que sea verdadero; no crear verificabilidad artificial mediante afirmaciones libres del auditor.
- **Incidencia típica:** Justificación, incluida la falta del identificador que permitiría verificar un dato ([D-122](../../30-governance/decisions.md#d-122)).

## Relaciones orientativas, no automáticas

| AC | Propiedades especialmente relevantes |
|---|---|
| **Concreción** | P06, P07, P08, P12. |
| **Precisión** | P08, P09, P10, P13. |
| **Aplicabilidad** | P10, P11, P12; también P07 según el hallazgo. |
| **Comparabilidad** | P07, P10, P12, P13. |
| **Fiabilidad** | P14 y P16. |
| **Justificación** | P08, P17, P18, relaciones de soporte; otras propiedades si condicionan la reconstrucción. |

La elección se explica por el RI, el AC y el hallazgo, no por una correspondencia fija muchos-a-uno. (La tabla de FUND §7.4 lista para Aplicabilidad solo P10, P11, P12, aunque su texto admite que P07 contribuya a la aplicabilidad a una variante.)

## Relacionado

- [Propiedades de calidad (canon)](../../10-model/quality-properties.md).
- [ac-guides.md](ac-guides.md) — uso de las propiedades en cada AC.
