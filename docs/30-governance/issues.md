---
id: issues
title: Registro de incidencias e incoherencias documentales
layer: governance
status: vigente
version: 1.0
updated: 2026-10-25
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
| [I-11](#i-11) | Definición del estado `vigente` frente al contenido procedente del intake | Baja | abierta |
| [I-12](#i-12) | Apoyo del caso de las sábanas en una categoría que ya no es componente | Baja | resuelta → [D-029](decisions.md#d-029) |
| [I-13](#i-13) | Casos que no reflejan del todo la regla de las cuestiones propias | Baja | abierta |
| [I-14](#i-14) | Casos documentados que cambian con la base ampliada | Media | resuelta → [D-032](decisions.md#d-032) |
| [I-15](#i-15) | `warmth-level` no está solo en Juegos de cama | Baja | abierta |
| [I-16](#i-16) | Cuestiones inferidas dentro de un bloque de categoría de contenido fijo | Media | resuelta → [D-041](decisions.md#d-041) |
| [I-17](#i-17) | Relevancia de las propiedades de Amazon (D-039) frente a la base de D-030 | Media | abierta |
| [I-18](#i-18) | Renderizado selectivo del MPIR frente al motor de captura, que renderiza siempre | Baja | abierta |
| [I-19](#i-19) | Estados y versiones del catálogo en ejecución | Media | resuelta → [D-045](decisions.md#d-045) |

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

### I-11

**Definición del estado `vigente` frente al contenido procedente del intake.**

- [docs/CLAUDE.md](../CLAUDE.md#estados) define `vigente` como lo «definido en los documentos rectores (CTX, BASE) o en FUND».
- [D-016](decisions.md#d-016) y la skill `docs-update` incorporan como vigente lo que un intake afirma como vigente. Así lo hacen [D-017](decisions.md#d-017) (escala del IR), [D-020](decisions.md#d-020) (clase de estudio), [D-021](decisions.md#d-021) (eje de base), [D-022](decisions.md#d-022) (criterio de especialización) y [D-023](decisions.md#d-023) a [D-037](decisions.md#d-037) (composición de la clase, condición 4, beneficios reclamados, cuestiones propias, especializaciones de oferta, clasificación objetiva, base de la clase en las referencias, material reciclado, propósito de la clase, bloques de requisitos, capa general, importancia, cuestiones inferidas y valores de oferta).
- D-021 a D-037 proceden de updates descritos por el usuario en la conversación, que la skill transcribió como artefactos archivados. D-016 habla de lo que «se deposita en `docs/intake/`»; conviene precisar que los updates conversacionales se tratan igual.
- **Afecta a:** [docs/CLAUDE.md](../CLAUDE.md#estados).
- **Propuesta:** ampliar la definición: «`vigente` — definido en los documentos rectores (CTX, BASE), en FUND o en un intake procesado que lo formule como vigente (D-016); forma parte del canon».

### I-12

**Apoyo del caso de las sábanas en una categoría que ya no es componente.**

- [D-023](decisions.md#d-023) recompone el caso por piezas (Sábanas planas, Sábanas ajustables y Fundas de almohada) y el artefacto dice que «el resto del análisis anterior se mantiene».
- Pero el caso apoya «juego» (`bedding-pieces-included`) y «tejido polar» (`fabric__fleece` en «Tejido») en Sábanas (`hg-15-1-2`), la madre, que ya no es componente. Con la lectura estricta de la condición 4 ([D-024](decisions.md#d-024)), ese apoyo solo vale como evidencia complementaria.
- En las referencias: Sábanas planas y Sábanas ajustables solo tienen `product-certifications-standards`; `fabric` está en Fundas de almohada (`hg-15-1-8-2`); `bedding-pieces-included` solo está en la madre.
- **Afecta a:** [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina).
- **Propuesta:** volver a anclar los apoyos en los componentes («juego» en Amazon `BED_LINEN_SET`; «tejido polar» en el «Tejido» de Fundas de almohada y en el material de PTD) y marcar como complementario el apoyo en Sábanas. Las tres especializaciones seguirían cumpliendo la condición 4.
- **Resolución (2026-10-25):** la base de una categoría de Shopify incluye los atributos de sus madres, así que `bedding-pieces-included` y `fabric` de Sábanas forman parte de la base de Sábanas planas y Sábanas ajustables. Los apoyos quedan en componentes de la clase. → [D-029](decisions.md#d-029).

### I-13

**Casos que no reflejan del todo la regla de las cuestiones propias.**

- En el caso de las sábanas, polar «añade bolitas, electricidad estática, transpirabilidad, abrigo y gramaje, pérdida de pelo» (`INTAKE 2026-10-24-specialization-criterion`). Con [D-026](decisions.md#d-026), polar «trae bolitas, electricidad estática y pérdida de pelo», y el gramaje está en la base. El artefacto no dice si transpirabilidad y abrigo son cuestiones propias o de la base.
- En el sofá reclinable, la tapicería de piel es especialización, pero el artefacto no documenta su apoyo para la condición 4 ([D-024](decisions.md#d-024)).
- **Afecta a:** [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina) y [cases](../20-methods/product-taxonomy/cases.md#sofá-reclinable-de-exposición).
- **Propuesta:** reescribir el efecto del polar con solo las cuestiones propias y dejar transpirabilidad, abrigo y gramaje como cuestiones de la base condicionadas por el tejido; comprobar en Shopify Sofás (`material`) y en PTD `SOFA` si hay un valor de piel que dé apoyo a la tapicería de piel y, si no lo hay, tratarla como requisito condicionado de Sofás.
- **Anotación (2026-10-25):** en las sábanas, el abrigo no está en la base: lo trae «uso invernal» (caso de la manta, `INTAKE 2026-10-25-objective-classification`). La propuesta debe dejar el abrigo fuera de las cuestiones de la base. Las características especiales de los PTD ([D-030](decisions.md#d-030)) también afectan al polar: ver [I-14](#i-14), resuelta por [D-032](decisions.md#d-032). El polar sigue siendo especialización, porque la pérdida de pelo no está en ninguna base; queda por reescribir su efecto.

### I-14

**Casos documentados que cambian con la base ampliada.**

- [D-029](decisions.md#d-029) (atributos de las categorías madre) y [D-030](decisions.md#d-030) (características especiales de los PTD) amplían la base de la clase, y algunos casos documentados cuentan como cuestiones propias otras que ahora están en la base.
- **Sofá cama Luna:** la tapicería textil es especialización porque «trae resistencia a la abrasión, desenfundable y antimanchas», consecuencia de [D-026](decisions.md#d-026) aceptada por el usuario. El `special_feature` de PTD `SOFA` incluye «Resistente a la abrasión», «Resistente a las manchas» y «Funda extraíble». Con D-030, las tres cuestiones están en la base y, por D-026, la tela sería un valor.
- **Juguete de cuerda:** PTD `PET_TOY` tiene «Lavable», que afecta al lavado de la cuerda (le quedan el deshilachado y la ingestión de fibras), y «Tecnología Chew Guard» y «Uso rudo», que podrían afectar a la resistencia a la mordida del mordedor.
- **Sábanas:** PTD `PILLOWCASE`, de la pieza Fundas de almohada, tiene «Resistente a la estática» y «Resistente a la formación de bolitas»; `FLAT_SHEET` y `FITTED_SHEET` no tienen `special_feature`. Dos de las cuestiones propias del polar están en la base de una pieza; la pérdida de pelo no está en ninguna. No está decidido si la base se lee por pieza o para toda la composición.
- **Juego (sábanas y funda nórdica):** con D-029, `bedding-pieces-included` está en la base heredada de las piezas, y el caso de las sábanas dice que el juego «añade las piezas incluidas».
- **Manta:** el apoyo de la condición 4 del tejido polar no está documentado. En las referencias hay Shopify Mantas `fabric` «Vellón» y `BLANKET` `material` «Forro polar» y `weave_type` «Tejido de pelo».
- **Afecta a:** [cases](../20-methods/product-taxonomy/cases.md) (sofá cama, juguete de cuerda, manta, funda nórdica) y [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina).
- **Propuesta:**
  - Sofá cama: aplicar D-030 y pasar la tapicería textil a valor que condiciona. Conservar la consecuencia aceptada exigiría una excepción a D-030; lo decide el usuario.
  - Juguete de cuerda: la cuerda sigue siendo especialización (deshilachado e ingestión de fibras) y el lavado pasa a la base; comprobar si «Uso rudo» cubre la resistencia a la mordida.
  - Sábanas: decidir si la base se lee por pieza. En ambos casos el polar sigue siendo especialización, porque la pérdida de pelo no está en ninguna base.
  - Juego: escribir su efecto con los requisitos del conjunto de [D-023](decisions.md#d-023) (qué piezas, cuántas y en qué medidas).
  - Manta: documentar el apoyo con los valores citados.
- **Resolución (2026-10-25):** aceptada. Ningún requisito cambia: el propósito de la clase son los requisitos informativos. Se aplican las propuestas, y la tela del sofá cama pasa a valor que condiciona. El mordedor también pasa a valor, por una interpretación de D-032 pendiente de validar. → [D-032](decisions.md#d-032).

### I-15

**`warmth-level` no está solo en Juegos de cama.**

- El caso de las sábanas dice, en la fila «Uso invernal», que el atributo `warmth-level` está «solo asignado a Juegos de cama» (`INTAKE 2026-10-24-specialization-criterion`).
- En Shopify v2026-08 también lo tienen Colchas y edredones (`hg-15-1-10`) y Cubrecolchones (`hg-15-1-12`, *Mattress Toppers*). Ninguna de las dos es componente del caso, así que el apoyo de «uso invernal» no cambia.
- **Afecta a:** [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina).
- **Propuesta:** corregir el dato: «asignado a Juegos de cama, Colchas y edredones y Cubrecolchones (*Mattress Toppers*), que no son componentes del caso».

### I-16

**Cuestiones inferidas dentro de un bloque de categoría de contenido fijo.**

- [D-040](decisions.md#d-040) busca que un bloque `cat.` tenga el mismo contenido sea cual sea el producto, y la clave del modelo ([D-038](decisions.md#d-038)) supone que dos ofertas con los mismos bloques tienen los mismos requisitos.
- Pero las cuestiones inferidas ([D-036](decisions.md#d-036)) van «dentro del bloque de su categoría» y el clasificador las redacta en cada ejecución, así que el mismo bloque puede cambiar de contenido según el producto.
- **Afecta a:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) y [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo).
- **Propuesta:** una cuestión inferida se usa en la ejecución como añadido provisional del modelo, marcado como tal y fuera de la clave; cuando se acepta en la revisión, se incorpora al bloque del catálogo como nueva versión. Se resolvería con la separación entre entrenamiento y ejecución planteada al usuario.
- **Resolución (2026-10-25):** aceptada. → [D-041](decisions.md#d-041).

### I-17

**Relevancia de las propiedades de Amazon (D-039) frente a la base de D-030.**

- [D-030](decisions.md#d-030) cuenta todos los valores de `special_feature` de un PTD como base de la clase; con eso, una característica pasa a valor que condiciona.
- [D-039](decisions.md#d-039) solo admite las propiedades de Amazon como requisitos «cuando son relevantes para la clase», y eso se decide en la revisión del catálogo.
- Si la revisión descarta una propiedad, la característica sigue siendo valor y su cuestión vuelve a quedarse sin sitio: el hueco que D-039 cierra reaparece en parte.
- **Afecta a:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) y [study-class](../10-model/study-class.md#criterio-de-especialización).
- **Propuesta:** la comprobación de base de D-030 usa solo las propiedades que retiene el catálogo; o bien, descartar una propiedad en la revisión obliga a revisar su efecto según D-030.
- **Anotación (2026-10-25):** con [D-041](decisions.md#d-041), un bloque generado en ejecución no ha pasado aún por la revisión que decide qué propiedades son relevantes; la propuesta debe cubrir también ese caso.
- **Anotación (2026-10-25):** con [D-044](decisions.md#d-044), la relevancia de las propiedades de Amazon la deciden reglas inducidas en el entrenamiento, no una revisión. La propuesta se reformula: la comprobación de base de D-030 usa las propiedades que retienen esas reglas, o el efecto sobre D-030 se mide como parte de la validación automática.
- **Anotación (2026-10-25):** la primera versión del entrenamiento ([D-045](decisions.md#d-045)) no induce todavía la relevancia de Amazon ([OQ-49](open-questions.md)); hasta entonces, la decide la redacción automática del bloque, como declara D-045.
- **Anotación (2026-10-25):** con [D-050](decisions.md#d-050), además de incluir la propiedad en el bloque (redacción), se puede excluir en una clase concreta (filtro de relevancia). La exclusión puede reabrir este hueco; la salvaguarda de cobertura lo evita en parte, porque una exclusión que deja sin pregunta un hecho declarado se descarta.

### I-18

**Renderizado selectivo del MPIR frente al motor de captura, que renderiza siempre.**

- [sampling-capture](../20-methods/mpir/sampling-capture.md#contenido-dinámico-e-interacción-selectiva) dice que el renderizado con navegador automatizado «se empleará **selectivamente** para evitar coste y complejidad innecesarios».
- El [motor de captura](../../demand-engine/src/demand_engine/capture/README.md) (T-013), con la aprobación del usuario (2026-10-25), renderiza siempre con Chrome real por CDP. En una sola visita guarda el HTML de la respuesta, el DOM renderizado y el MHTML.
- Motivos: la incoherencia entre capas (curl con user-agent de navegador, headless) es lo que más bloqueos provoca; con el volumen del piloto, el coste es despreciable. — INTAKE 2026-10-25-mpir-capture-engine
- **Afecta a:** [sampling-capture](../20-methods/mpir/sampling-capture.md#contenido-dinámico-e-interacción-selectiva).
- **Propuesta:** actualizar `sampling-capture` para que el renderizado sea el procedimiento por defecto, con esa justificación, y mantener que la presencia de JavaScript no es una limitación metodológica.

### I-19

**Estados y versiones del catálogo en ejecución.**

- [D-041](decisions.md#d-041) obliga a indicar qué partes del modelo se usaron «sin revisar», pero el catálogo tiene estados «propuesta» y «validado» ([D-038](decisions.md#d-038)) y no se dice si un bloque en propuesta cuenta como no revisado, ni qué estado recibe un bloque generado en ejecución.
- [D-036](decisions.md#d-036) prevé validar las críticas y «una muestra del resto», y D-041 que una inferida solo pasa al bloque «cuando se acepta»: las inferidas no críticas que no entren en la muestra se quedarían siempre fuera del bloque y de la clave.
- La clave del modelo es «la lista ordenada de bloques», sin versión ([D-038](decisions.md#d-038)), pero D-041 crea versiones nuevas de un bloque al aceptar inferidas: dos ofertas con la misma clave podrían tener requisitos distintos.
- **Afecta a:** [model-training](../10-model/model-training.md#ejecución), [demand-model](../10-model/demand-model.md#entrenamiento-y-ejecución) y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo).
- **Propuesta:** «no revisado» = todo lo que no está en estado validado; un bloque generado en ejecución entra en el catálogo en estado propuesta; en entrenamiento se revisan todas las inferidas encoladas (la muestra solo para las ya incorporadas); la clave incluye la versión de cada bloque.
- **Anotación (2026-10-25):** con [D-044](decisions.md#d-044) desaparece la muestra humana: lo encolado lo convierte el entrenamiento en casos y reglas, que se aceptan o descartan por validación automática; queda resuelta la parte de muestra frente a aceptación. «No revisado» pasa a significar no compilado por el entrenamiento. Siguen abiertas la versión en la clave y el estado de los bloques generados en ejecución.
- **Resuelta → [D-045](decisions.md#d-045) (2026-10-25):** la clave lleva la versión de cada bloque (`<bloque>@<versión>`), y un bloque generado en ejecución está «no compilado» hasta que el entrenamiento lo compila; los estados del bloque pasan a ser «no compilado» y «compilado».
