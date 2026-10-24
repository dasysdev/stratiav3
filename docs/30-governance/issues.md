---
id: issues
title: Registro de incidencias e incoherencias documentales
layer: governance
status: vigente
version: 1.0
updated: 2026-10-24
sources: []
---

# Registro de incidencias e incoherencias documentales

Divergencias detectadas entre fuentes o dentro de una misma fuente. **No se resuelven en silencio:** cada una lleva una propuesta y espera decisión. Al resolverla, se registra la decisión en [decisions](decisions.md), se actualizan los módulos afectados y la incidencia pasa a `resuelta`.

| ID | Asunto | Gravedad | Estado |
|---|---|---|---|
| [I-01](#i-01) | Denominación de los indicadores generales | Media | resuelta → [D-003](decisions.md#d-003) |
| [I-02](#i-02) | Fuentes del sistema de construcción del modelo de demanda | Media | resuelta → [D-009](decisions.md#d-009) |
| [I-03](#i-03) | Unidad de evaluación: «RI × interfaz» frente a «RI × ámbito» | Media | resuelta → [D-010](decisions.md#d-010) |
| [I-04](#i-04) | Número de interfaces/ámbitos en CTX frente a BASE | Baja | resuelta → [D-013](decisions.md#d-013) |
| [I-05](#i-05) | Numeración de propiedades desde P06 | Baja | resuelta → [D-007](decisions.md#d-007) |
| [I-06](#i-06) | Documentos de apoyo citados y nombres de fichero inexistentes | Baja | resuelta → [D-008](decisions.md#d-008) |
| [I-07](#i-07) | Nombre del proyecto | Baja | resuelta → [D-011](decisions.md#d-011) |
| [I-08](#i-08) | Alcance de las propiedades: ¿también fundamentan requisitos técnicos? | Media | resuelta → [D-007](decisions.md#d-007) |
| [I-09](#i-09) | Denominación del artefacto taxonómico | Baja | resuelta → [D-012](decisions.md#d-012) |
| [I-10](#i-10) | P07 en las propiedades asociadas a Aplicabilidad | Baja | resuelta → [D-014](decisions.md#d-014) |

---

### I-01

**Denominación de los indicadores generales.**

- **BASE §6.1–6.2** (rector): «**Tasa de resolución informativa (TRI)**» y «**Tasa de cumplimiento técnico**».
- **FUND §8.4–8.5**: «Indicador general de resolución informativa» e «Indicador general de resolución técnica».
- **Afecta a:** [scoring-systems](../10-model/scoring-systems.md).
- **Propuesta:** adoptar las denominaciones de BASE como canónicas, con las de FUND como alias (ya aplicado provisionalmente, [D-003](decisions.md#d-003)). Alternativa: renombrar en BASE.
- **Resolución (2026-10-24):** aceptada la propuesta: nombres de BASE con alias de FUND. → [D-003](decisions.md#d-003).

### I-02

**Fuentes del sistema de construcción del modelo de demanda.**

- **BASE §4.2** (rector): dos fuentes, **Shopify Product Taxonomy** e **información de ecommerce referentes**.
- **TAX**: una taxonomía propia que integra **Shopify (base), Amazon (especialización) y Google (contraste)**.
- **MPIR**: formaliza la vía de referentes como base de conocimiento.
- **Afecta a:** [demand-model](../10-model/demand-model.md), [product-taxonomy](../20-methods/product-taxonomy/README.md).
- **Propuesta:** actualizar BASE §4.2 en el canon para reflejar las dos vías (Modelo de Taxonomía de Productos y MPIR). Se mantendría que Amazon y Google son fuentes de apoyo de la taxonomía, no fuentes directas de RI. Requiere tu aprobación porque modifica una definición rectora.
- **Resolución (2026-10-24):** aceptada tal como se propuso. → [D-009](decisions.md#d-009).

### I-03

**Unidad de evaluación: «RI × interfaz» frente a «RI × ámbito».**

- **BASE §5, §5.1, §6.1** usa «en cada interfaz», «requisito informativo × interfaz pertinente» y «para un requisito informativo y una interfaz».
- **TAX §3.2** (capa 4: «cada requisito en cada interfaz pertinente») y **MPIR §10.2** («interfaces pertinentes (Catálogos distribuidos, Web y Web Schema.org)») mantienen el mismo uso.
- **FUND** usa ambos términos. «RI × ámbito» aparece en §5.1, §8.6 y §9. «Interfaz» aparece en §5.3 («requisito informativo × interfaz pertinente»), §6.1, §8.1 («un criterio, un requisito informativo y una interfaz»), §8.2, §8.3 y §8.5.
- **BASE** también usa «ámbito» en §3 («Cada ámbito dispone de…») y §6.1 (TRI: «conjunto pertinente para el ámbito evaluado»).
- **GSC0** usa de forma consistente «RI × ámbito».
- La divergencia es, por tanto, **interna a BASE y a FUND**, no entre documentos.
- Como Web y Web Schema.org son dos ámbitos sobre el mismo recurso web, «interfaz» resulta ambiguo como unidad.
- **Afecta a:** [evaluation-architecture](../10-model/evaluation-architecture.md), [evaluation-scopes](../10-model/evaluation-scopes.md), [effective-availability](../10-model/effective-availability.md).
- **Propuesta:** fijar **ámbito de evaluación** como término de la unidad y reservar **interfaz** para el medio técnico ([D-004](decisions.md#d-004), provisional).
- **Resolución (2026-10-24):** no hay divergencia. En el contexto de la unidad de evaluación, «interfaz» y «ámbito» son sinónimos. Las citas se conservan sin marca y en texto nuevo se prefiere «ámbito». Sustituye a D-004. → [D-010](decisions.md#d-010).

### I-04

**Número de interfaces/ámbitos en CTX frente a BASE.**

- **CTX §5** enumera dos «interfaces y ámbitos de evaluación»: Catálogos distribuidos y Web.
- **BASE §3** establece **tres ámbitos**: añade Web Schema.org.
- **Afecta a:** [scope](../00-context/scope.md), [evaluation-scopes](../10-model/evaluation-scopes.md).
- ~~**Propuesta inicial:** interpretarlo como 2 interfaces y 3 ámbitos.~~ Superada por [D-010](decisions.md#d-010): si «interfaz» y «ámbito» son sinónimos en la unidad de evaluación, la distinción 2/3 deja de sostenerse.
- **Propuesta revisada:** actualizar CTX §5 para enumerar los **tres** ámbitos de evaluación (Catálogos distribuidos, Web, Web Schema.org), en coherencia con BASE §3.
- **Resolución (2026-10-24):** aceptada. → [D-013](decisions.md#d-013).

### I-05

**Numeración de propiedades desde P06.**

- Las propiedades vigentes van de **P06 a P18**. P01–P05 no aparecen en ningún documento vigente.
- Lo más probable es que fueran propiedades técnicas, retiradas al reservar las propiedades al modelo informativo (BASE §3.1).
- **Propuesta:** confirmarlo y registrar que P01–P05 están **reservados/retirados**, para no reutilizar esos IDs.
- **Resolución (2026-10-24):** confirmado. P01–P05 eran las propiedades técnicas del modelo anterior (Localizabilidad, Distribución efectiva, Recuperabilidad, Legibilidad técnica y Conformidad técnica); quedan retiradas. → [D-007](decisions.md#d-007).

### I-06

**Documentos de apoyo citados y nombres de fichero inexistentes.**

- FUND (pie, por título) cita «Fundamento metodológico: calidad informativa orientada a su interpretación y utilización por sistemas de IA», «Estrategia metodológica de evaluación informativa…» y «Calidad de representación de oferta comercial». GSC0 (cabecera y fuentes) los cita por nombre de fichero: `Fundamento_metodologico_IA_y_calidad_informativa.md` y `Estrategia_metodologica_RI_localizacion_pertinencia_evidencias_GSC.md`. **Ninguno está en el corpus v0.**
- Las referencias de GSC0, TAX y MPIR usan nombres que no coinciden con los ficheros reales (`Contexto_marco_de_estudio.md`, `Conceptos_base_sistema_de_estudio.md`, `Fundamentos_consolidados_…md`, `…taxonomia_modelos_demanda(1).md`). El mapa de correspondencias está en [docs/CLAUDE.md](../CLAUDE.md#frontmatter-obligatorio-todo-md-salvo-archive-y-este-fichero) (claves v0).
- **Propuesta:** si esos documentos existen, incorporarlos al archivo como v0 complementario. Si no, registrarlos como antecedentes no disponibles.
- **Resolución (2026-10-24):** «Calidad de representación de oferta comercial» se localizó fuera del proyecto y se decide no incorporarlo. Los otros dos no existen y quedan como no disponibles. → [D-008](decisions.md#d-008).

### I-07

**Nombre del proyecto.**

- TAX y MPIR usan «**Calidad de información v1**».
- El repositorio se llama `stratiav3`.
- **Propuesta:** fijar nombre del producto/sistema y nombre del proyecto metodológico, y usarlos de forma consistente.
- **Resolución (2026-10-24):** **stratia.cic** (stratia, calidad de información comercial). → [D-011](decisions.md#d-011).

### I-08

**Alcance de las propiedades: ¿también fundamentan requisitos técnicos?**

- **BASE §5.3** define que las propiedades sirven para fundamentar «las valoraciones de los criterios de aceptación **y los requisitos técnicos generales**».
- **BASE §3.1** afirma que «las propiedades de calidad pertenecen **exclusivamente** al modelo de evaluación informativa».
- **FUND §4.2** lo confirma: «no constituyen unidades de evaluación del cumplimiento técnico». **FUND §5.2** añade: «pertenecen exclusivamente al modelo de evaluación informativa». **FUND §7** las refiere al «propósito informativo de un RI».
- La contradicción está **dentro del propio documento rector**.
- **Afecta a:** [quality-properties](../10-model/quality-properties.md).
- **Propuesta:** corregir la definición de BASE §5.3 eliminando «y los requisitos técnicos generales», en coherencia con el resto del canon.
- **Resolución (2026-10-24):** aceptada. La frase era un residuo de la arquitectura anterior, en la que las propiedades tenían doble función (técnica e informativa). Definición canónica enmendada. → [D-007](decisions.md#d-007).

### I-09

**Denominación del artefacto taxonómico.**

- TAX se titula «Marco metodológico para construir la **taxonomía de clases de producto**».
- MPIR lo denomina «**Modelo de Taxonomía de Productos**».
- **Afecta a:** [product-taxonomy](../20-methods/product-taxonomy/README.md), [mpir](../20-methods/mpir/README.md).
- **Propuesta:** fijar un nombre único (p. ej. «Taxonomía de clases de producto») y usarlo en ambos métodos.
- **Resolución (2026-10-24):** «Taxonomía de clases de producto». → [D-012](decisions.md#d-012).

### I-10

**P07 en las propiedades asociadas a Aplicabilidad.**

- La tabla de **FUND §7.4** asocia Aplicabilidad con P10, P11 y P12.
- **GSC0 §10.3** añade «también P07 según el hallazgo».
- El texto de FUND §7.4 ya admite que P07 contribuya a la aplicabilidad («la granularidad puede contribuir… a su aplicabilidad a una variante determinada»). La divergencia está en la tabla, no en el concepto.
- **Afecta a:** [quality-properties](../10-model/quality-properties.md#asociaciones-orientativas-con-los-criterios), [property-checks](../20-methods/audit-gsc/property-checks.md).
- **Propuesta:** añadir P07 a la tabla canónica de Aplicabilidad, con la marca «según el hallazgo». Las asociaciones son orientativas, así que el cambio no altera ninguna regla.
- **Resolución (2026-10-24):** aceptada. → [D-014](decisions.md#d-014).
