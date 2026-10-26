---
id: mpir-operation-validation
title: MPIR — cobertura, ciclo operativo, piloto, riesgos y entregables
layer: method
status: propuesta
version: 1.1
updated: 2026-10-26
sources: [MPIR §11, MPIR §12, MPIR §14, MPIR §15, MPIR §16, MPIR §17, MPIR §18, INTAKE 2026-10-26-open-issues-resolution]
---

# MPIR — cobertura, ciclo operativo, piloto, riesgos y entregables

Parte de [MPIR](README.md).

## Cobertura, calidad del proceso y condición de cierre

La sistematicidad del MPIR depende de poder explicar **qué se observó, qué quedó fuera y por qué se considera suficiente el trabajo efectuado para su finalidad exploratoria**.

### Tres controles de cobertura

- **Cobertura de referentes y recursos:** proporción y diversidad efectiva de comercios, segmentos, productos y tipos de recurso inspeccionados respecto de la muestra planificada.
- **Cobertura temática:** dimensiones conocidas de la taxonomía examinadas, relaciones nuevas observadas, temas sin evidencia y exploración abierta no restringida al vocabulario inicial.
- **Cobertura del procesamiento:** recursos recuperados, bloques extraídos, fallos de parseo, contenido dinámico pendiente, señales sin revisar y relaciones no resueltas.

Un resultado negativo exige precisar **el perímetro inspeccionado**: «no identificado en la muestra y perfiles examinados» no equivale a «no lo demanda el mercado».

### Saturación cualitativa

En ciclos sucesivos se observa si nuevos ecommerce y recursos aportan **patrones sustantivamente diferentes**, nuevas condiciones o casos fronterizos, o si principalmente replican lo ya identificado. La saturación se examina **por clase y segmento** y se documenta junto con la diversidad de fuentes y las limitaciones. No se adopta por ahora un porcentaje universal, número fijo de páginas ni umbral de saturación: deberán calibrarse con el piloto para evitar falsa precisión.

### Condición de cierre de una iteración

Puede cerrarse una iteración cuando:

- la muestra y sus desviaciones están documentadas;
- las capturas y unidades estructuradas pertinentes son recuperables y revisables;
- las señales de mayor interés, novedosas o fronterizas han recibido revisión adecuada;
- se han consolidado patrones sin duplicidades significativas no justificadas;
- las cuestiones candidatas y las relaciones con taxonomía quedan trazadas;
- están explicitados los vacíos, recursos inaccesibles y límites de generalización.

El cierre significa **suficiencia operativa de la iteración**, no demostración de cobertura exhaustiva de la demanda.

## Ciclo operativo de ejecución

| Etapa | Operación | Producto / control |
|---|---|---|
| **0. Preparación** | Fijar clase, alcance, taxonomía de referencia, segmentos, panel y matriz de cobertura. | Plan de observación versionado. |
| **1. Descubrimiento** | Inventariar recursos relevantes por ecommerce y perfil. | Lista de recursos candidatos, motivos y cobertura. |
| **2. Captura** | Recuperar y preservar recursos, renderizados con navegador real ([D-073](../../30-governance/decisions.md#d-073)), con interacción si procede. | Corpus original versionado. |
| **3. Estructuración** | Segmentar bloques y conservar entidades, tablas, filtros, relaciones y contexto. | Corpus estructurado de unidades informativas. |
| **4. Anotación** | Detectar señales y proponer prácticas/cuestionamientos mediante reglas y análisis semántico. | Anotaciones candidatas ligadas a evidencias. |
| **5. Revisión** | Comprobar interpretaciones y corregir omisiones, sobreinferencias o atribuciones. | Anotaciones sustentadas o descartadas. |
| **6. Consolidación** | Normalizar prácticas y patrones entre referentes. | Versión del MPIR para la clase. |
| **7. Contraste** | Comparar con taxonomías y trasladar cuestiones candidatas justificadas. | Matriz de aportaciones al modelo de demanda. |
| **8. Iteración** | Ampliar muestra, corregir extractores y reprocesar corpus cuando sea necesario. | Nueva versión trazable y análisis de cobertura. |

**Regla de operación:** el análisis puede comenzar tras un primer lote razonable, antes de completar todo el panel. Si revela contenidos omitidos, se ajusta la extracción; las versiones previas de las fuentes permanecen conservadas. **No se generan «prácticas definitivas» en el mismo acto de descargar una página.**

## Ejemplo ilustrativo: botas de senderismo

> **Ejemplo hipotético**, no evidencia real de ecommerce concreto.

| Fuente hipotética | Unidad de contenido conservada | Tipo de recurso |
|---|---|---|
| Ecommerce A | Filtro «Tipo de terreno» con opciones diferenciadas. | Categoría / filtros. |
| Ecommerce B | Guía que relaciona el diseño de la suela con roca húmeda y barro. | Guía de compra. |
| Ecommerce C | Tabla que compara agarre en distintas superficies para varios modelos. | Comparador. |

Cada observación conserva URL, localizador, fecha, texto o estructura exacta y correspondencias entre producto y dato.

- **Señales:** criterio de selección (`SI-02`), contexto de uso (`SI-04`), relación funcional (`SI-05`) y comparación (`SI-03`).
- **Prácticas observadas:** segmentar por terreno; explicar adecuación del agarre a superficies; comparar alternativas bajo condiciones de uso.
- **Patrón normalizado:** utilización del **tipo y estado del terreno** para orientar la evaluación del agarre de las botas.
- **Cuestión informativa candidata:** «¿Para qué tipos de superficie y condiciones de terreno está diseñado el agarre del calzado?».
- **Aportación al modelo de demanda frente a la taxonomía:** posible **profundización** de características de suela o agarre, al incorporar un alcance funcional y condiciones de aplicación que pueden no estar expresados en los atributos.

La pregunta se traslada al proceso de construcción de demanda para decidir **pertinencia, objeto, alcance, aplicabilidad, posible solapamiento e importancia relativa**. Ni la repetición de tres señales ni su presencia en comparadores prueba que la cuestión sea crítica. Tampoco se concluye que un modelo determinado sea adecuado para roca húmeda: eso exigiría información sobre esa oferta concreta.

## Validación piloto y parámetros que deben calibrarse

Se recomienda comenzar con **una clase acotada**, alineada con el piloto taxonómico de **calzado > botas** ([taxonomía](../product-taxonomy/data-model-governance.md#prueba-piloto-aconsejada)), seleccionando subsegmentos informativamente diferenciados. La prueba debe incluir recursos de tipos distintos y ecommerce con perspectivas editoriales diversas.

### Preguntas de validación del piloto

1. ¿El sistema captura correctamente las estructuras informativas relevantes (FAQ, filtros, tablas y relaciones), no solo texto editorial?
2. ¿Aparecen cuestiones que no podíamos inferir suficientemente a partir de las taxonomías?
3. ¿Podemos distinguir observaciones, interpretación y pregunta inferida sin perder trazabilidad?
4. ¿Las anotaciones automáticas reproducen razonablemente la revisión humana o producen omisiones y asociaciones temáticas injustificadas?
5. ¿Qué parte del corpus permite identificar patrones nuevos, profundizaciones o diferencias de aplicabilidad?
6. ¿Cómo cambia el rendimiento de descubrimiento al incorporar nuevos ecommerce y perfiles de recursos?
7. ¿Qué cambios de clase, faceta o requisito candidato surgen de la evidencia y cuáles eran meras diferencias editoriales?

### Parámetros abiertos, sin alterar el método adoptado

> **Estado: pendiente.** Consolidados también en [cuestiones abiertas](../../30-governance/open-questions.md).

- Tamaño y combinación concreta del panel de ecommerce por tipo de clase.
- Número de páginas y productos por perfil y segmento.
- Umbrales o reglas prácticas de suficiencia de cobertura y saturación.
- Campos finales obligatorios/opcionales y almacenamiento físico de recursos.
- Herramientas y selectores por plataforma, navegador y configuración de captura.
- Taxonomía fina de funciones o señales tras resolver casos fronterizos.
- Proporción y procedimiento de revisión humana, medición de errores y tratamiento de discrepancias.
- Política de actualización periódica y antigüedad tolerada de las evidencias.

Estos aspectos requieren **calibración operativa**; no se presentan como acuerdos cerrados.

## Riesgos metodológicos y medidas de control

| Riesgo | Medida preventiva |
|---|---|
| Confundir lo que publica un referente con lo que demanda el mercado. | Formular resultados como evidencia indirecta, con límites de generalización. |
| Seleccionar solo ecommerce con contenidos abundantes o plantillas semejantes. | Diversificar perfiles, segmentos e independencia editorial; documentar sesgos. |
| Extraer solo atributos conocidos. | Combinar exploración abierta y dirigida; preservar bloques no previstos. |
| Transformar páginas directamente en requisitos o prácticas definitivas. | Separar corpus, anotaciones, patrones y transferencia al modelo de demanda. |
| Perder contexto al limpiar HTML o convertir tablas en texto. | Preservar DOM, cabeceras, relaciones, entidades y localizadores. |
| Sobreinferir con IA o asumir conocimiento externo. | Exigir evidencia enlazada, revisión de casos inciertos y reglas versionadas. |
| Duplicar señales reproducidas de un mismo fabricante. | Registrar procedencia editorial y dependencias; consolidar sin inflar apoyo. |
| Confundir ausencia de captura con ausencia de práctica. | Registrar cobertura, errores, recursos no inspeccionados y límites de acceso. |
| Asignar criticidad por frecuencia o prominencia. | Evaluar importancia únicamente en el modelo de demanda y por su relevancia para la clase. |
| Tratar contenido de referencia como evidencia de oferta auditada. | Mantener separación entre fuentes de construcción de demanda e interfaces de evaluación. |
| Automatización sin permisos o con rastreo intrusivo. | Respetar condiciones aplicables, no eludir controles y limitar la tasa de acceso. |

## Entregables y criterio de aceptación

**Entregables de una iteración por clase:**

1. **Plan de observación:** definición de clase y muestra, panel de ecommerce, perfiles y cobertura prevista.
2. **Corpus de Evidencias Comerciales de Referencia:** instantáneas originales, metadatos, bloqueos y limitaciones.
3. **Corpus estructurado:** unidades contextualizadas, relaciones y trazabilidad a originales.
4. **Registro semántico:** señales, prácticas candidatas, fundamentos, incertidumbres y estados de revisión.
5. **MPIR consolidado:** catálogo versionado de patrones informativos por clase, con evidencias y variantes.
6. **Matriz de contraste taxonomía–MPIR:** confirmaciones, ampliaciones, profundizaciones, diferenciaciones y tensiones.
7. **Propuesta de transferencia:** cuestiones informativas candidatas con su justificación, para evaluación en el modelo de demanda.
8. **Informe de cobertura y limitaciones:** qué se examinó, qué no pudo examinarse y qué decisiones quedan abiertas.

La iteración es metodológicamente aceptable cuando sus observaciones importantes son **reexaminables**, sus interpretaciones son **rastreables a evidencia**, las prácticas están **normalizadas sin borrar diferencias sustantivas** y la transferencia al modelo de demanda distingue **hipótesis de cuestiones** de **requisitos aprobados**.

## Conclusión metodológica

El MPIR constituye la **segunda base de referencia** para la construcción sistemática del modelo de demanda, paralela y complementaria a la Taxonomía de clases de producto. Su contribución diferencial es revelar **cómo los ecommerce especializados y referentes transforman características, relaciones, contextos y condiciones comerciales en información destinada a apoyar decisiones de compra**.

Se adopta una secuencia **captura original → corpus estructurado → interpretación semántica → consolidación de prácticas → contraste con taxonomía → inferencia justificada de requisitos**, ejecutable por lotes y con retroalimentación controlada. **No** se generan prácticas definitivas mientras se realiza el scraping ni se prescinde del original una vez interpretado.

El éxito del método no se mide por el volumen de HTML acumulado ni por la cantidad de requisitos sugeridos, sino por **la capacidad de descubrir aportaciones informativas diferenciales al modelo de demanda, justificar su significado y alcance, y reconstruir cada inferencia desde fuentes comerciales concretas**.
