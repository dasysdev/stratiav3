---
id: product-taxonomy-data-model-governance
title: Taxonomía — modelo de datos, procedimiento, gobierno y decisiones pendientes
layer: method
status: propuesta
version: 1.2
updated: 2026-10-25
sources: [TAX §8, TAX §9, TAX §10, TAX §11, TAX Anexo A, TAX Anexo B, INTAKE 2026-10-24-define-class, INTAKE 2026-10-25-amazon-source-blocks]
---

# Taxonomía — modelo de datos, procedimiento, gobierno y decisiones pendientes

Parte de [Taxonomía de clases de producto](README.md).

## Modelo de datos de referencia (sin importar árboles completos)

La implementación mínima necesita separar fuentes, conceptos externos, clases internas, correspondencias, evidencia comercial y requisitos. Los campos siguientes son **orientativos**, no un esquema informático cerrado.

| Entidad lógica | Campos esenciales |
|---|---|
| `source_snapshot` | sistema, versión, marketplace/idioma, fecha, URL, condiciones de acceso, huella y estado de revisión. |
| `external_concept` | ID origen, nombre, ruta, clase de objeto (nodo, atributo, valor, PTD), referencia a instantánea. |
| `product_class` | ID interno, nombre, definición, inclusiones, exclusiones, clase(s) padre, estado, versión. |
| `class_facet` | faceta, valores, criterio de uso, relación con clases pertinentes. |
| `concept_mapping` | concepto externo, clase interna, tipo de relación, evidencia, justificación, estado, fecha de revisión. |
| `commercial_evidence` | ecommerce/recurso, observación, fecha, característica, clase candidata y fundamento de uso. |
| `information_requirement` | ID, pregunta, dimensión, objeto/alcance, aplicabilidad, importancia, justificación, fuente. |
| `class_requirement` | clase, RI, condición, estado de reutilización, diferencias de importancia o alcance. |
| `change_log` | versión de clase, cambio, motivo, fuentes afectadas, impacto y aprobación. |

**Regla de trazabilidad:** una clase interna puede mapearse a varios conceptos externos y una misma categoría externa puede servir de referencia a varias clases. Una pregunta informativa puede derivarse de múltiples evidencias; una evidencia de atributo puede sugerir más de una pregunta. Ninguna relación debe forzarse a ser uno-a-uno.

## Procedimiento de construcción y revisión

| Etapa | Actividad | Entregable / control |
|---|---|---|
| 0. Delimitación | Definir familias piloto, mercado, versión y objetivos de especialización. | Alcance aprobado. |
| 1. Fijar fuentes | Congelar Shopify; inventariar Google; obtener Amazon autorizado si está disponible. | Registro de fuentes, versiones y accesos. |
| 2. Recoger candidatos | Identificar categorías, atributos, valores y rutas que sugieran especializaciones. | Inventario de conceptos candidatos. |
| 3. Alinear | Crear correspondencias semánticas y registrar solapamientos, ausencias y dudas. | Tabla de mapeos con evidencia y estado. |
| 4. Delimitar clases | Formular definiciones, inclusiones, exclusiones, padres y facetas. | Fichas de clase propuestas. |
| 5. Contrastar | Revisar ecommerce referentes y casos fronterizos; decidir entre subclase, faceta o aplicabilidad. | Clases validadas o pendientes, con motivos. |
| 6. Construir demanda | Inferir, normalizar y justificar las preguntas por clase, reutilizando núcleos comunes. | Primeros modelos de demanda. |
| 7. Calibrar | Detectar duplicaciones, clases artificiales, vacíos, reglas ambiguas e importancia inconsistente. | Registro de cambios y aprobación de piloto. |
| 8. Mantener | Revisar versiones externas, nuevos usos y evidencias comerciales, controlando impacto. | Versionado y gobierno del catálogo. |

**Condiciones para cerrar una clase:** definición positiva; al menos una regla clara de pertenencia; frontera de exclusión documentada; correspondencias con origen y estado; evidencia suficiente de diferenciación; y decisión explícita sobre si necesita modelo propio o condiciones de aplicabilidad. No se establece una cuota numérica universal de categorías por rama.

### Prueba piloto aconsejada

La familia **calzado > botas** es idónea para probar las decisiones porque incluye estilos comerciales y usos técnicos potencialmente diferentes. Un piloto acotado debería: seleccionar la categoría Shopify base, identificar posibles facetas y especializaciones, comprobar Amazon.es si se dispone de acceso, contrastar un conjunto razonado de ecommerce referentes, formular modelos de demanda provisionales y decidir qué distinciones soportan clases independientes.

El éxito no se mide por el número de nodos creados, sino por la **claridad de fronteras, coherencia de la asignación de productos y explicabilidad de las diferencias de requisitos**.

## Gobierno, versiones y riesgos

### Política de cambio

- Cada fuente externa conserva su versión y ámbito geográfico o de marketplace; no se mezcla información de diferentes fechas como si fuese una única instantánea.
- Los identificadores propios de clase permanecen estables mientras la definición conceptual sea equivalente; una división, fusión o redefinición significativa genera un cambio controlado.
- Los mapeos deben revisarse al cambiar un origen externo o aparecer evidencia que altere fronteras conceptuales.
- Cambios de etiqueta o traducción no deben modificar por sí mismos la identidad de clase.
- Los cambios de clase deben acompañarse de un **análisis de impacto** sobre requisitos informativos, aplicabilidad e importancia relativa; no se reescriben automáticamente.
- La consulta y reutilización de datos Amazon queda supeditada a permisos y condiciones de uso aplicables; la taxonomía propia no debe prometer una descarga pública completa de Amazon.

### Riesgos y medidas preventivas

| Riesgo | Prevención |
|---|---|
| Unir árboles por nombres | Mapear semántica con IDs, inclusiones, contraejemplos y evidencia. |
| Crear un modelo por hoja externa | Exigir justificación de homogeneidad y diferencia informativa. |
| Convertir atributo o variante en clase | Distinguir dimensión, valor, faceta, subclase y entidad comercial. |
| Ignorar solapamiento funcional | Admitir varias relaciones, pertenencia múltiple o facetas. |
| Usar PTD Amazon como nodo BTG | Registrar por separado tipo de producto y nodo de navegación. |
| Tomar `product_type` de Google como oficial | Tratarlo como clasificación declarada por comerciante. |
| Presentar mapeos Shopify-Google como actuales sin fecha | Registrar que Shopify documenta versión Google 2021-09-21. |
| Confundir requisitos de plataforma con demanda | Justificar preguntas e importancia por relevancia informativa, no por validación técnica. |
| Suponer un nodo Amazon.es sin extracción vigente | Marcar no verificado y no asignar ID definitivo. |
| Reutilizar criticidad sin revisar clase | Confirmar importancia y aplicabilidad en cada clase. |

### Indicadores útiles de salud de la taxonomía

Porcentaje de clases con definición completa y evidencias; porcentaje de correspondencias validadas frente a provisionales; conceptos sin mapeo; fronteras con solapamiento documentado; tasa de asignaciones de producto ambiguas en muestras; número de clases nuevas que no aportan diferencias relevantes de requisitos; proporción de requisitos compartidos frente a específicos; y cambios pendientes de propagación a modelos de demanda.

Son **medidas de gobierno y cobertura**, no los indicadores IR, ICI, GSC o los indicadores técnicos de la auditoría ([sistemas de valoración](../../10-model/scoring-systems.md)).

## Conclusiones

### Respaldadas por fuentes

1. Shopify ofrece una clasificación estructurada con categorías y atributos versionados, adecuada como punto de partida abierto [R1-R4].
2. Amazon aporta nodos de navegación y esquemas PTD diferentes, que pueden suministrar especializaciones, atributos y, a través de los PTD, requisitos de la categoría ([D-039](../../30-governance/decisions.md#d-039)); su consulta completa mediante informes requiere acceso de vendedor [R5-R8].
3. Google dispone de categorías propias, especificaciones de atributos, `product_type` comerciante y `product_detail`, pero no equivale a un árbol universal de subclases funcionales con atributos cerrados [R9-R15].
4. Las correspondencias entre sistemas pueden ser jerárquicas, aproximadas o asociativas; la normalización semántica requiere decisiones explícitas y evidencia [R16].
5. El modelo de demanda del proyecto exige requisitos inferidos y justificados; no se obtiene automáticamente de campos taxonómicos.

Referencias R1–R16 en [sources.md](sources.md#referencias-externas-consulta-24-de-octubre-de-2026).

### Orientaciones de diseño recomendadas (no decisiones rectoras ya aprobadas)

- Adoptar **Shopify v2026-08 como instantánea inicial** y estructura principal de familias.
- Incorporar **Amazon** como fuente de especializaciones, atributos y requisitos de la categoría ([D-039](../../30-governance/decisions.md#d-039)), cuando el acceso y las evidencias lo permitan.
- Incorporar **Google** como referencia de clasificación, atributos y reglas comerciales, separando semántica de obligación de interfaz.
- Mantener **clases internas con IDs propios**, definiciones, facetas y mapeos versionados.
- Crear subclases solo cuando existan **fronteras positivas y diferencias sustantivas de necesidades de información**.
- Reutilizar requisitos comunes con reglas explícitas de aplicabilidad; validar la importancia relativa en cada clase.

## Decisiones pendientes

> **Estado: pendiente.** Consolidadas también en [cuestiones abiertas](../../30-governance/open-questions.md).

- Si las clases internas admiten varios padres o si habrá un padre principal más facetas y relaciones adicionales.
- Los criterios operativos y la evidencia mínima para aprobar equivalencias y nuevas subclases.
- La disponibilidad de acceso SP-API para obtener el árbol vigente de Amazon.es y las restricciones de reutilización de esos datos.
- La selección de ecommerce referentes y casos frontera para el piloto de botas.
- El mecanismo de gobierno, revisión y calendario de actualización de fuentes externas.

El grado de especialización que reduce la ambigüedad sin fragmentar innecesariamente los modelos de demanda quedó resuelto en el canon ([D-020](../../30-governance/decisions.md#d-020)): tantas especializaciones como sean relevantes, buscando la especificidad informativa necesaria ([clase de estudio](../../10-model/study-class.md)).

## Anexo A. Ficha de clase propuesta

- **Identidad:** ID interno; nombre canónico ES; otras denominaciones; estado; versión.
- **Definición:** función principal y alcance; reglas positivas de inclusión; exclusiones; ejemplos positivos y negativos.
- **Estructura:** padre(s); facetas relevantes; especializaciones; relaciones no jerárquicas.
- **Correspondencias:** Shopify/Amazon/Google (sistema, versión, marketplace, ID, ruta, relación, grado de verificación).
- **Diferenciación de demanda:** preguntas compartidas, preguntas específicas, condiciones de aplicabilidad y justificación de modelo propio.
- **Evidencia y revisión:** fuentes, ecommerce observados, casos frontera, responsable, fecha y cambios.

## Anexo B. Ficha de correspondencia propuesta

- **Origen:** sistema, versión, marketplace, ID, etiqueta y ruta.
- **Destino:** clase interna (ID y versión).
- **Relación:** equivalente / cercana / más amplia / más específica / relacionada / solapamiento / sin correspondencia.
- **Fundamento:** definición comparada, inclusiones, exclusiones y ejemplos.
- **Estado:** validado / provisional / no verificado / rechazado; fecha; responsable; vínculos a evidencia.
- **Consecuencia:** efecto sobre pertenencia de productos, facetas y requisitos de demanda si cambia el mapeo.
