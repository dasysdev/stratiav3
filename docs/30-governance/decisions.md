---
id: decisions
title: Registro de decisiones
layer: governance
status: vigente
version: 1.0
updated: 2026-10-25
sources: [GSC0 §18.4]
---

# Registro de decisiones

Registro **de solo adición**. Una decisión no se borra: se marca como `sustituida por D-NNN`.

**Estados:** `propuesta` · `aceptada` · `provisional` (aplicada a falta de confirmación) · `sustituida` · `rechazada`.

**Plantilla:**

```markdown
### D-NNN
**Título.** · Estado · Fecha
- **Contexto:** …
- **Decisión:** …
- **Consecuencias:** módulos afectados, efectos sobre evaluaciones previas.
- **Relacionado:** I-NN, OQ-NN.
```

| ID | Título | Estado | Fecha |
|---|---|---|---|
| [D-001](#d-001) | Documentación modular por capas | aceptada | 2026-10-24 |
| [D-002](#d-002) | Archivo v0 inmutable como línea base | aceptada | 2026-10-24 |
| [D-003](#d-003) | Denominaciones canónicas de indicadores | aceptada | 2026-10-24 |
| [D-004](#d-004) | «Ámbito de evaluación» como término de la unidad evaluada | sustituida por D-010 | 2026-10-24 |
| [D-005](#d-005) | Precedencia por capas | aceptada | 2026-10-24 |
| [D-006](#d-006) | Decisiones metodológicas explícitamente no adoptadas (V1) | aceptada | 2026-10-24 |
| [D-007](#d-007) | Las propiedades de calidad son exclusivamente informativas; P01–P05 retirados | aceptada | 2026-10-24 |
| [D-008](#d-008) | Antecedentes documentales no incorporados | aceptada | 2026-10-24 |
| [D-009](#d-009) | Dos vías de construcción del modelo de demanda: taxonomía y MPIR | aceptada (ampliada por D-036; enmendada por D-039) | 2026-10-24 |
| [D-010](#d-010) | «Interfaz» y «ámbito» son sinónimos en la unidad de evaluación | aceptada | 2026-10-24 |
| [D-011](#d-011) | Nombre del proyecto: stratia.cic | aceptada | 2026-10-24 |
| [D-012](#d-012) | Denominación «Taxonomía de clases de producto» | aceptada | 2026-10-24 |
| [D-013](#d-013) | Tres ámbitos de evaluación también en CTX | aceptada | 2026-10-24 |
| [D-014](#d-014) | P07 en las asociaciones orientativas de Aplicabilidad | aceptada | 2026-10-24 |
| [D-015](#d-015) | Intake de updates y skill `docs-update` | aceptada (modificada por D-016) | 2026-10-24 |
| [D-016](#d-016) | El intake prevalece; aplicación sin aprobación previa | aceptada | 2026-10-24 |
| [D-017](#d-017) | Escala del IR: 0–10 | aceptada | 2026-10-24 |
| [D-018](#d-018) | Prominencia informativa, IP y calidad ajustada (propuesta) | aceptada | 2026-10-24 |
| [D-019](#d-019) | Estado binario de resolución = «suficientemente resuelto» de la TRI | aceptada | 2026-10-24 |
| [D-020](#d-020) | Clase de estudio: clase general más especializaciones relevantes | aceptada (precisada por D-033) | 2026-10-24 |
| [D-021](#d-021) | Shopify fija el eje de base de la clase general | aceptada (modificada por D-023) | 2026-10-24 |
| [D-022](#d-022) | Criterio de especialización: cinco condiciones y evidencia | aceptada (precisada por D-024 y D-026, ampliada por D-025; condición 1 enmendada por D-027; matizada por D-041; validación precisada por D-044; condición 1 restablecida por D-048) | 2026-10-24 |
| [D-023](#d-023) | Composición de la clase de estudio por categorías y piezas | aceptada (modificada por D-028, precisada por D-029) | 2026-10-25 |
| [D-024](#d-024) | Condición 4 del criterio de especialización: lectura estricta | aceptada (precisada por D-029 y D-030) | 2026-10-25 |
| [D-025](#d-025) | Beneficios reclamados: no son especializaciones | aceptada (precisada por D-031) | 2026-10-25 |
| [D-026](#d-026) | Regla de las cuestiones propias para dimensiones que todo producto tiene | aceptada (precisada por D-029 y D-030; consecuencia del sofá cama revisada por D-032; ampliada por D-037) | 2026-10-25 |
| [D-027](#d-027) | La condición 1 incluye la oferta: especializaciones de oferta | sustituida por D-048 (ejemplo de outlet sustituido antes por D-037) | 2026-10-25 |
| [D-028](#d-028) | Clasificación objetiva: una categoría entra aunque no aporte requisitos | aceptada (precisada por D-032 y D-033: alias) | 2026-10-25 |
| [D-029](#d-029) | Base de una categoría de Shopify: atributos propios y de sus madres | aceptada | 2026-10-25 |
| [D-030](#d-030) | Características especiales de un PTD: dimensiones de la base y apoyo | aceptada | 2026-10-25 |
| [D-031](#d-031) | El material reciclado es especialización, no beneficio reclamado | aceptada | 2026-10-25 |
| [D-032](#d-032) | Propósito de la clase de estudio: los requisitos informativos | aceptada (precisada por D-033) | 2026-10-25 |
| [D-033](#d-033) | Identidad del modelo de demanda: composición de bloques de requisitos | aceptada (formato y denominación fijados por D-038; precisada por D-040; la aplicación pasa a la oferta por D-047) | 2026-10-25 |
| [D-034](#d-034) | Capa general de requisitos: universales y condicionados | aceptada (borrador revisado por D-038; importancias fijas por D-045; elementos digitales al modelo por D-047; pregunta universal de promociones por D-049; fabricante, origen y seguridad por D-052) | 2026-10-25 |
| [D-035](#d-035) | Pruebas operativas de importancia relativa | aceptada (la duda no baja la importancia ni excluye: D-050) | 2026-10-25 |
| [D-036](#d-036) | Cuestiones inferidas: tercera vía de construcción, provisional | aceptada (régimen: lectura de Claude no objetada; matizada por D-041; enmendada por D-044) | 2026-10-25 |
| [D-037](#d-037) | Valores de oferta y activación de cuestiones condicionadas | aceptada (sin especializaciones de oferta por D-048) | 2026-10-25 |
| [D-038](#d-038) | Catálogo de bloques: capa general contrastada, identificadores propios y denominación | aceptada (precisada por D-040; matizada por D-041; estados y clave enmendados por D-045; clave y nombre sin aplicación por D-047) | 2026-10-25 |
| [D-039](#d-039) | Los PTD de Amazon, fuente de requisitos de la categoría | aceptada (precisada por D-044; ampliada por D-052: fuente también de la capa general) | 2026-10-25 |
| [D-040](#d-040) | Bloques de categoría deterministas y catálogo revisado | aceptada (matizada por D-041; precisada por D-044 y D-045) | 2026-10-25 |
| [D-041](#d-041) | Entrenamiento y ejecución: la revisión humana no bloquea la ejecución | aceptada (enmendada por D-044) | 2026-10-25 |
| [D-042](#d-042) | Capa original del MPIR: sin capturas de pantalla y políticas de acceso del motor | aceptada (motor compartido: D-046) | 2026-10-25 |
| [D-043](#d-043) | Criterios de redacción del catálogo de bloques de categoría | aceptada (criterio 5 sustituido por D-044; criterio 1 precisado por D-051) | 2026-10-25 |
| [D-044](#d-044) | Marco humano y reglas inducidas: el usuario define el marco, no revisa reglas ni requisitos | aceptada (operación: D-045) | 2026-10-25 |
| [D-045](#d-045) | Operación del entrenamiento, primera versión: rasgos, reglas de importancia por el árbol de Shopify y métricas | aceptada (relevancia inducida por D-050; vocabulario ampliado por D-051) | 2026-10-25 |
| [D-046](#d-046) | Motor de captura compartido por el MPIR y el entrenamiento del modelo de demanda | aceptada | 2026-10-25 |
| [D-047](#d-047) | El modelo de demanda va con el producto; la aplicación, con la oferta | aceptada | 2026-10-25 |
| [D-048](#d-048) | La oferta no aporta requisitos: activa requisitos condicionados de la clase | aceptada | 2026-10-25 |
| [D-049](#d-049) | Pregunta universal de promociones y descuentos | aceptada | 2026-10-25 |
| [D-050](#d-050) | Filtro de relevancia aprendido: lo no relevante sale del modelo de la clase | aceptada | 2026-10-25 |
| [D-051](#d-051) | Peso, grosor y gramaje: rasgo «magnitud física», fuera de la regla de las medidas | aceptada | 2026-10-25 |
| [D-052](#d-052) | Fabricante, país de fabricación y seguridad en la capa general, según su origen | aceptada | 2026-10-25 |

---

### D-001

**Documentación modular por capas.** · aceptada · 2026-10-24

- **Contexto:** el corpus v0 (~310 KB) repetía definiciones en 3–4 documentos y mezclaba normativa, fundamento, procedimiento y pendientes. Ya habían aparecido divergencias ([I-01](issues.md#i-01), [I-08](issues.md#i-08)).
- **Decisión:** reorganizar en capas (`00-context`, `10-model`, `20-methods`, `30-governance`) con módulos por tema de 80–250 líneas, una sola fuente de verdad por concepto y un glosario como capa de enrutamiento. Se descartaron los documentos íntegros con índice (no resuelven la deriva) y la atomización por concepto (fragmenta las relaciones; vocabulario aún en calibración).
- **Consecuencias:** las reglas de mantenimiento están en [docs/CLAUDE.md](../CLAUDE.md) y la validación en `tools/check_docs.py`.

### D-002

**Archivo v0 inmutable como línea base.** · aceptada · 2026-10-24

- **Contexto:** el proyecto no usa control de versiones por ahora.
- **Decisión:** copiar los originales a `docs/archive/v0-2026-10-24/` en modo solo lectura. `tmp/docs/` se conserva hasta que el propietario decida eliminarlo.
- **Actualización (2026-10-24):** el propietario eliminó `tmp/docs/`. `docs/archive/v0-2026-10-24/` es ahora la única copia de los originales.
- **Consecuencias:** cada módulo traza sus fuentes v0 en el frontmatter `sources`. Las líneas base futuras se archivan como carpetas nuevas.

### D-003

**Denominaciones canónicas de indicadores.** · aceptada · 2026-10-24

- **Contexto:** [I-01](issues.md#i-01).
- **Decisión:** usar las denominaciones de BASE (IR, ICI, **TRI**, **Tasa de cumplimiento técnico**) con los alias de FUND.
- **Consecuencias:** [scoring-systems](../10-model/scoring-systems.md).
- **Confirmación (2026-10-24):** el propietario la confirma como definitiva. Cierra I-01.

### D-004

**«Ámbito de evaluación» como término de la unidad evaluada.** · sustituida por [D-010](#d-010) · 2026-10-24

- **Contexto:** [I-03](issues.md#i-03).
- **Decisión:** en texto nuevo, la unidad informativa se expresa como **RI × ámbito**, alineado con GSC0 y con el uso mayoritario en FUND §5.1 y §8.6; ambos términos conviven dentro de BASE y FUND. «Interfaz» designa el medio técnico. Las citas literales de BASE y FUND se conservan tal cual y se marcan con ⚠ I-03.
- **Consecuencias:** módulos de `10-model/` y `20-methods/audit-gsc/`.

### D-005

**Precedencia por capas.** · aceptada · 2026-10-24

- **Contexto:** en v0, la precedencia se definía por documento (CTX y BASE rectores; FUND interpretativo; métodos subordinados).
- **Decisión:** `00-context` y `10-model` contienen el canon (citas literales de CTX/BASE más desarrollo de FUND) y prevalecen sobre `20-methods`. Los métodos no pueden introducir conceptos, criterios, propiedades, escalas, pesos ni indicadores. Dentro del canon, una cita literal de CTX/BASE prevalece sobre la interpretación de FUND.
- **Consecuencias:** [docs/CLAUDE.md](../CLAUDE.md#capas-y-precedencia).

### D-006

**Decisiones metodológicas explícitamente no adoptadas (V1).** · aceptada · 2026-10-24

- **Contexto:** línea base heredada de GSC0 §18.4.
- **Decisión.** **No se adopta:**
  - una escala de «grado o número de derivaciones» para decidir pertinencia o GSC;
  - reglas que penalicen automáticamente respuestas obtenidas mediante relaciones justificadas;
  - una lista universal de campos obligatorios ni una equivalencia entre pertinencia y coincidencia literal;
  - nuevas puntuaciones para las propiedades P06–P18 ni promedios automáticos para el GSC;
  - una disponibilidad efectiva ternaria (un proceso inconcluso se registra fuera de la escala binaria);
  - inferir falsedad de la ausencia de corroboración, ni verdad de la ausencia de contradicciones;
  - mezclar información de Web Schema.org con HTML ajeno al marcado como contenido resolutivo de ese ámbito;
  - trasladar los requisitos técnicos directamente a descuentos del GSC;
  - calcular IR/ICI con fórmulas no establecidas;
  - interpretar un GSC como probabilidad de recomendación, de conversión o de éxito de una IA concreta.
- **Consecuencias:** son invariantes de trabajo, recogidas en el `CLAUDE.md` raíz.

### D-007

**Las propiedades de calidad son exclusivamente informativas; P01–P05 retirados.** · aceptada · 2026-10-24

- **Contexto:** [I-08](issues.md#i-08) e [I-05](issues.md#i-05).
  - BASE §5.3 decía que las propiedades fundamentan también «los requisitos técnicos generales». Eso contradecía BASE §3.1 y FUND §4.2 y §5.2.
  - El origen es la arquitectura anterior. El antecedente «Calidad de representación de oferta comercial» (21/10/2026) y el registro de cambio «Perspectivas de evaluación v1.3» (20/10/2026) daban a las propiedades doble función: diagnóstico técnico por interfaz y fundamentación de indicadores.
  - Esa arquitectura incluía cinco propiedades técnicas: **P01 Localizabilidad, P02 Distribución efectiva, P03 Recuperabilidad, P04 Legibilidad técnica y P05 Conformidad técnica**.
  - Los documentos del 24/10 retiraron esa función, y la frase de BASE §5.3 quedó como residuo.
- **Decisión:**
  - Se enmienda la definición canónica de BASE §5.3, eliminando «y los requisitos técnicos generales».
  - Las propiedades pertenecen solo al modelo informativo. La evaluación técnica se basa en los requisitos técnicos generales y en su sistema cuantitativo propio.
  - Los IDs **P01–P05 quedan retirados** y no se reutilizan.
  - El contenido de P03 y P04 (obtención y legibilidad) pervive como condición dentro de la [disponibilidad efectiva](../10-model/effective-availability.md), no como propiedad.
- **Consecuencias:** [quality-properties](../10-model/quality-properties.md) pasa a la versión 1.1. El archivo v0 conserva el texto original de BASE §5.3. Cierra I-05 e I-08.
- **Alternativa descartada:** recuperar P01–P05 para el diagnóstico técnico por interfaz. Revertía la decisión más reciente, reiterada en BASE §3.1, FUND §4.2 y FUND §5.2.

### D-008

**Antecedentes documentales no incorporados.** · aceptada · 2026-10-24

- **Contexto:** [I-06](issues.md#i-06).
  - FUND y GSC0 citan tres documentos de apoyo.
  - Solo se localizó «Calidad de representación de oferta comercial», fuera del proyecto: `Downloads/Idea_general_calidad_representacion_oferta_comercial.md`.
  - Junto a él están otros antecedentes del mismo linaje que no se citan: `Sistema_de_evaluacion.md`, con el sistema anterior de 7 indicadores, escala 0–3, pesos y bandas, y los registros de cambio v1.3 (perspectivas) y v1.4 (importancia relativa).
  - «Fundamento metodológico… IA» y «Estrategia metodológica… RI/GSC» no existen en ningún lugar accesible.
- **Decisión:**
  - Los antecedentes **no se incorporan** al proyecto.
  - Los dos documentos no encontrados se registran como **no disponibles**; su contenido se considera absorbido por FUND y GSC0.
  - Las correspondencias entre los nombres de fichero citados y los reales son las de la tabla de claves v0 de [docs/CLAUDE.md](../CLAUDE.md#frontmatter-obligatorio-todo-md-salvo-archive-y-este-fichero).
- **Consecuencias:** las citas a esos documentos en el archivo v0 son solo históricas. Ningún módulo depende de ellos. Cierra I-06.

### D-009

**Dos vías de construcción del modelo de demanda: taxonomía y MPIR.** · aceptada · 2026-10-24

- **Contexto:** [I-02](issues.md#i-02).
  - BASE §4.2 citaba como fuentes la Shopify Product Taxonomy y la información de ecommerce referentes.
  - Los marcos TAX y MPIR desarrollan dos vías: una taxonomía propia, que integra Shopify, Amazon y Google, y el MPIR.
- **Decisión:** se enmienda BASE §4.2 en el canon. El catálogo se construye por inferencia a partir de **dos vías de referencia complementarias**:
  1. **Taxonomía de clases de producto.** La estructura principal es Shopify; Amazon (especialización) y Google (contraste) son fuentes **de apoyo de la taxonomía, no fuentes directas de RI**.
  2. **MPIR.** Información comercial publicada por ecommerce referentes.

  El recorrido de construcción (observar → inferir → formular y normalizar → justificar) no cambia.
- **Consecuencias:**
  - [demand-model](../10-model/demand-model.md) pasa a la versión 1.1.
  - Se retiran las marcas ⚠ I-02 de [product-taxonomy](../20-methods/product-taxonomy/README.md) y [mpir](../20-methods/mpir/README.md).
  - La denominación de la vía taxonómica sigue pendiente en [I-09](issues.md#i-09).

### D-010

**«Interfaz» y «ámbito» son sinónimos en la unidad de evaluación.** · aceptada · 2026-10-24

- **Contexto:** [I-03](issues.md#i-03). BASE y FUND alternan «RI × interfaz» y «RI × ámbito».
- **Decisión:**
  - En el contexto de la unidad de evaluación y de los sistemas de valoración, ambos términos son **sinónimos**: RI × interfaz ≡ RI × ámbito.
  - No hay incoherencia. Las citas literales se conservan sin marca.
  - En texto nuevo se prefiere «ámbito», por continuidad con GSC0 y el glosario.
  - Fuera de ese contexto, «interfaz de exposición» designa también el medio técnico de publicación.
- **Consecuencias:**
  - Sustituye a [D-004](#d-004).
  - Se retiran las marcas ⚠ I-03 de `10-model` y `20-methods`.
  - La propuesta de [I-04](issues.md#i-04) («2 interfaces y 3 ámbitos») deja de sostenerse y se reformula.

### D-011

**Nombre del proyecto: stratia.cic.** · aceptada · 2026-10-24

- **Contexto:** [I-07](issues.md#i-07). Los métodos TAX y MPIR usaban «Calidad de información v1» y el directorio se llama `stratiav3`.
- **Decisión:** el proyecto y su sistema de auditoría se denominan **stratia.cic** (stratia, calidad de información comercial). «Calidad de información v1» queda como denominación histórica del corpus v0. `stratiav3` es solo el nombre del directorio.
- **Consecuencias:** encabezado del `CLAUDE.md` raíz.

### D-012

**Denominación «Taxonomía de clases de producto».** · aceptada · 2026-10-24

- **Contexto:** [I-09](issues.md#i-09). TAX hablaba de «taxonomía de clases de producto» y MPIR de «Modelo de Taxonomía de Productos».
- **Decisión:** el nombre único es **Taxonomía de clases de producto**. Es el título del propio marco y encaja con «clase de producto u oferta» del canon.
- **Consecuencias:** se ajustan las menciones en [mpir](../20-methods/mpir/README.md), `concepts-architecture`, `interpretation-transfer` y `operation-validation`, y en [demand-model](../10-model/demand-model.md).

### D-013

**Tres ámbitos de evaluación también en CTX.** · aceptada · 2026-10-24

- **Contexto:** [I-04](issues.md#i-04). CTX §5 enumeraba dos ámbitos y BASE §3, tres. Con [D-010](#d-010) («interfaz» ≡ «ámbito» en la unidad de evaluación) dejaba de sostenerse la lectura «2 interfaces y 3 ámbitos».
- **Decisión:** se enmienda CTX §5 en el canon. Los ámbitos de evaluación son tres: **Catálogos distribuidos**, **Web** y **Web Schema.org**.
- **Consecuencias:** [scope](../00-context/scope.md) pasa a la versión 1.1 y se retira la marca ⚠ I-04 de [evaluation-scopes](../10-model/evaluation-scopes.md).

### D-014

**P07 en las asociaciones orientativas de Aplicabilidad.** · aceptada · 2026-10-24

- **Contexto:** [I-10](issues.md#i-10). La tabla de FUND §7.4 no incluía P07 en Aplicabilidad, aunque su texto lo admitía. GSC0 §10.3 sí lo incluía.
- **Decisión:** la tabla canónica asocia Aplicabilidad con P10, P11 y P12 y, **según el hallazgo**, también con P07. Las asociaciones siguen siendo orientativas, no cerradas ni automáticas.
- **Consecuencias:** [quality-properties](../10-model/quality-properties.md) pasa a la versión 1.2 y se retira la marca ⚠ I-10 de [property-checks](../20-methods/audit-gsc/property-checks.md).

### D-015

**Intake de updates y skill `docs-update`.** · aceptada · 2026-10-24

- **Contexto:** el propietario crea `docs/intake/` para depositar los artefactos que constituyen un update. Hace falta un procedimiento repetible para incorporarlos sin deriva ni cambios silenciosos.
- **Decisión:** los updates se procesan con la skill `/docs-update` (`.claude/skills/docs-update/SKILL.md`), que sigue estos pasos:
  1. Lectura del artefacto.
  2. Análisis de impacto (confirma, precisa, amplía, enmienda, contradice, nuevo concepto, cierra o abre pendiente, fuera de alcance).
  3. Plan y **aprobación del propietario**.
  4. Aplicación del flujo de cambio.
  5. Archivado del artefacto en `docs/archive/intake/AAAA-MM-DD-<slug>`, en solo lectura.
  6. Validación y, si hay cambios de canon, revisión independiente.

  Los artefactos archivados se citan como `INTAKE <stem>` en `sources`; el validador comprueba que existen. `docs/intake/` no es canon y queda fuera del validador.
- **Consecuencias:** se actualizan `docs/CLAUDE.md` (capa Intake, clave `INTAKE`, versionado), el `CLAUDE.md` raíz y `tools/check_docs.py`.
- **Precisión (2026-10-24):** a petición del propietario, **todo artefacto procesado se archiva** en `archive/intake/`, tanto si se aplica entero como en parte o se rechaza. El resultado consta en el changelog. Solo permanece en `intake/` lo pendiente o lo aplazado a petición expresa.

### D-016

**El intake prevalece; aplicación sin aprobación previa.** · aceptada · 2026-10-24

- **Contexto:** instrucción del propietario: «Todo intake prevalece sobre lo que hay. Sobreescribe. Por lo demás tú decides; no quiero gestionarlo».
- **Decisión:**
  - Lo que se deposita en `docs/intake/` **prevalece sobre todo el contenido existente**, incluidas las invariantes del `CLAUDE.md` raíz y las decisiones aceptadas, y lo sobrescribe.
  - La skill `/docs-update` decide y aplica **sin pedir aprobación**. Resuelve las ambigüedades con la interpretación más fiel al texto, las registra en la decisión correspondiente e informa al terminar.
  - Desaparece la vía de «rechazo»; se mantiene el aplazamiento a petición expresa.
- **Consecuencias:**
  - Modifica el paso de aprobación de [D-015](#d-015).
  - Se actualizan la skill, `docs/CLAUDE.md` (precedencia y flujo de cambio), `docs/intake/README.md` y el `CLAUDE.md` raíz.
  - Fuera del intake, las incoherencias se siguen registrando en `issues.md`.

### D-017

**Escala del IR: 0–10.** · aceptada · 2026-10-24

- **Contexto:** FUND §8.2 no fijaba escala ni fórmula del IR (invariante 7). El artefacto `INTAKE 2026-10-24-prominencia-informativa` afirma: «IR (0–10): mide la capacidad de resolución del RI mediante los criterios de aceptación. No se modifica».
- **Decisión:** el IR se expresa en **escala 0–10**. La fórmula de agregación de los GSC sigue sin fijar ([OQ-28](open-questions.md)). La regla «disponibilidad efectiva = 0 → IR = 0» es coherente con la escala.
- **Interpretación adoptada:** el artefacto presenta la escala como existente («no se modifica»), así que se incorpora como **vigente**, aunque el resto del artefacto sea provisional.
- **Consecuencias:** [scoring-systems](../10-model/scoring-systems.md) pasa a la versión 1.1. Se reformula la invariante 7 y se actualizan el glosario y OQ-28.
- **Sustituye:** la afirmación de FUND §8.2 de que no hay escala final del IR.

### D-018

**Prominencia informativa, IP y calidad ajustada (propuesta).** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-prominencia-informativa`, «propuesta metodológica provisional».
- **Decisión:** se incorporan con **estado propuesta**, en el nuevo módulo [informative-prominence](../10-model/informative-prominence.md):
  - la clasificación binaria de prominencia (HTML) por componente;
  - el IP (0–100 %, `100 × C/N`, NA si N = 0);
  - la calidad ajustada (modificador secundario, sin fórmula ni peso).
- **Interpretaciones adoptadas:**
  - Va a `10-model` porque introduce indicadores.
  - El IP y la calidad ajustada se calculan por **RI × ámbito**.
  - Solo están definidos para **Web**. En Web Schema.org y Catálogos distribuidos el IP es **NA** hasta que haya reglas específicas.
  - «IP» se mantiene sin expandir, como en la fuente.
  - Las tensiones con FUND §2.3, PR-06 y D-006 (respuestas derivadas no prominentes) **no bloquean**, porque el intake prevalece. Se registran como OQ-33 y OQ-35.
- **Consecuencias:** OQ-31 a OQ-36 en la sección G de [open-questions](open-questions.md). Cambian el glosario, el índice, `scoring-systems` y la invariante 7.

### D-019

**Estado binario de resolución = «suficientemente resuelto» de la TRI.** · aceptada · 2026-10-24

- **Contexto:** el artefacto introduce una «normalización binaria del IR (0/1)» que distingue resolución suficiente e insuficiente. La TRI (BASE §6.1) ya se basa en RI «suficientemente resueltos».
- **Decisión:** el estado binario de resolución es **la misma noción** que usa la TRI. Así hay un único concepto, con la regla de normalización pendiente (OQ-31). Su estado es propuesta.
- **Consecuencias:** sección «Estado binario de resolución» en [scoring-systems](../10-model/scoring-systems.md) y entrada en el glosario.

### D-020

**Clase de estudio: clase general más especializaciones relevantes.** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-define-class`. El canon define el modelo de demanda sobre una «clase de producto u oferta» (BASE §4), pero no decía cómo se determina esa clase. La taxonomía (propuesta) ofrece subclases, facetas y aplicabilidad condicionada, y dejaba abierto el grado de especialización ([OQ-09](open-questions.md)).
- **Decisión:**
  - La **clase objeto del modelo de demanda** se compone de una **clase general** y de **todas las especializaciones aplicables** (por uso, material, función u otras características) que introduzcan o modifiquen cuestiones informativas relevantes. No es necesario que formen una jerarquía estricta: pueden ser facetas que concurren.
  - El modelo de demanda integra los requisitos comunes y los específicos, sin duplicados y revisando su aplicabilidad e importancia relativa.
  - «La medida de cama (por ejemplo, 90 cm) caracteriza una variante, pero no obliga por sí sola a crear otra clase».
  - **Principio:** buscar la especificidad informativa necesaria, no el mayor número posible de subclases.
  - Cierra OQ-09.
- **Interpretaciones adoptadas:**
  - «Clase objeto del modelo de demanda» y «clase de estudio» son sinónimos en el artefacto. El término canónico es **clase de estudio**, y la «clase estudiada» de BASE §4.1 y §4.2 designa la misma clase.
  - Va a `10-model` porque introduce conceptos. Se incorpora como **vigente**, porque el artefacto la formula como regla y no la presenta como provisional.
  - El ejemplo de los juegos de sábanas se marca como **ilustrativo**: no es una clase aprobada (regla de ejemplos hipotéticos de `docs/CLAUDE.md`).
  - El artefacto no deroga la taxonomía: la prueba de especialización y sus cuatro salidas siguen como propuesta de método. Sus umbrales («cambien sustancialmente», «cuestiones informativas centrales distintas») se refieren a crear subclases o niveles. Para incorporar una especialización a la clase de estudio rige el criterio del artefacto, menos exigente, y la relación entre ambos umbrales pasa a OQ-38. Queda abierto cómo se representa en la taxonomía una clase de estudio compuesta ([OQ-37](open-questions.md)) y qué evidencia acredita que una especialización es pertinente ([OQ-38](open-questions.md)).
  - OQ-09 se cierra porque el artefacto fija el criterio de grado: tantas especializaciones como sean relevantes, con la especificidad informativa necesaria. Los criterios operativos y la evidencia mínima siguen en OQ-06 y OQ-38.
  - El paso 4 («construir el modelo de demanda») se realiza con el recorrido vigente del sistema de construcción (observar → inferir → formular y normalizar → justificar), que no cambia.
  - La frase de la medida de cama se recoge literal, como ejemplo, sin generalizarla a una regla sobre variantes.
  - OQ-05 sigue abierta: la regla trata de la composición de la clase de estudio, no de la estructura de padres de las clases internas.
- **Consecuencias:**
  - [demand-model](../10-model/demand-model.md) pasa a la versión 1.2, con la nueva sección «Clase de estudio».
  - Se enlaza desde [product-taxonomy](../20-methods/product-taxonomy/README.md), [subclasses](../20-methods/product-taxonomy/subclasses.md), [integration](../20-methods/product-taxonomy/integration.md) y [data-model-governance](../20-methods/product-taxonomy/data-model-governance.md), todos en la versión 1.1.
  - Nuevas entradas del glosario: clase de estudio, clase general y especialización. Nuevas OQ-37 y OQ-38.
- **Relacionado:** OQ-05, OQ-06, OQ-09, OQ-37, OQ-38.

### D-021

**Shopify fija el eje de base de la clase general.** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-specialization-criterion`, bloque A, procedente del caso de trabajo T-005 (juego de sábanas de coralina). [D-020](#d-020) pedía «identificar la clase general» sin decir con qué referencia. [D-009](#d-009) fijaba Shopify como estructura principal de la vía taxonómica.
- **Decisión:**
  - La clase general de una clase de estudio es una categoría de la Shopify Standard Product Taxonomy, en la versión fijada.
  - Lo que Shopify no distingue como categoría entra como especialización.
- **Interpretaciones adoptadas:**
  - Es un update descrito por el usuario en la conversación, sin artefacto en `intake/`. Se transcribe literal en `archive/intake/2026-10-24-specialization-criterion.md` para conservar la trazabilidad.
  - Va a `10-model`, como precisión del paso 1 de la regla de D-020, y se incorpora como **vigente** porque el usuario la formula como regla (misma situación que [I-11](issues.md#i-11)).
  - «Versión fijada» es la versión de Shopify adoptada como referencia: hoy, v2026-08 ([sources](../20-methods/product-taxonomy/sources.md#shopify-base-estructural-y-vocabulario-de-atributos)).
  - La regla determina **qué categoría** es la clase general, no cómo se representa como clase interna, que sigue en [OQ-37](open-questions.md). Tampoco convierte cada categoría de Shopify en una clase aprobada.
  - «Lo que Shopify no distingue como categoría entra como especialización» se lee como **candidata** a especialización: se examina con el criterio de [D-022](#d-022) y no se incorpora automáticamente. En el propio caso, el diseño, el color y la medida no son categorías y se descartan.
- **Consecuencias:** [demand-model](../10-model/study-class.md#clase-general-el-eje-de-base) 1.3; glosario (clase general); caso de trabajo en [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina).
- **Relacionado:** D-009, D-020, OQ-37.

### D-022

**Criterio de especialización: cinco condiciones y evidencia.** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-specialization-criterion`, bloques B y C. [OQ-38](open-questions.md) pedía la evidencia y el criterio operativo para reconocer que una especialización «introduce o modifica cuestiones informativas relevantes» ([D-020](#d-020)). El criterio se probó a mano en el caso T-005.
- **Decisión:**
  - Una característica es especialización de la clase de estudio cuando cumple cinco condiciones: es del producto y estable; tiene un efecto comparativo sobre las cuestiones; las cuestiones afectadas son relevantes para la clase; tiene apoyo en las referencias; y se fija en el nivel más general cuyos miembros comparten las cuestiones que introduce.
  - No cuentan: un nodo o valor que solo existe en una referencia, un cambio de los valores esperados, una característica de variante, la proximidad temática ni un requisito de plataforma o de feed.
  - Evidencia: con las cinco condiciones razonadas en la ficha, la especialización queda provisional. La valida el responsable. El contraste con ecommerce referentes (MPIR) la confirma o la revisa después, cuando exista. No se fija ningún umbral numérico.
  - Cierra OQ-38.
- **Interpretaciones adoptadas:**
  - Va a `10-model` porque introduce un criterio, y se incorpora como **vigente** (misma situación que [I-11](issues.md#i-11)).
  - «La valida el usuario, como responsable» designa al responsable de la taxonomía, el propietario del proyecto. La cita del canon omite, marcándolo con […], el paréntesis «(opción B elegida por el usuario)», que solo indica cuál de las opciones discutidas se eligió.
  - «La ficha» es la ficha de clase del método ([Anexo A](../20-methods/product-taxonomy/data-model-governance.md#anexo-a-ficha-de-clase-propuesta)), que incluye el campo «responsable». Si una clase de estudio compuesta tiene ficha propia depende de [OQ-37](open-questions.md).
  - La lista de la condición 1 («un uso, material o función declarados») no se lee como cerrada. El artefacto no deroga el «u otras características» de D-020, que sigue citado literalmente. Lo decisivo de la condición es que la característica sea del producto, declarada y estable. En el caso, «juego» se clasifica como función o composición.
  - «Un nodo o valor que solo existe en una referencia» significa que su mera existencia en una referencia no basta (coherente con subclasses). No significa «que existe en una sola referencia»: el nodo de «juego» solo está en Amazon y sí cuenta como apoyo (condición 4).
  - Relación con la prueba de especialización de la taxonomía: el criterio rige la incorporación de una especialización a la clase de estudio. La prueba sigue rigiendo la creación de subclases o niveles jerárquicos de la taxonomía. Es más exigente en el umbral de efecto («cambien sustancialmente», «cuestiones informativas centrales distintas», frente a «al menos un efecto»), pero el criterio añade exigencias propias: el anclaje en Shopify, Amazon o Google (la prueba admite también ecommerce referentes) y la condición de nivel. Así se resuelve la parte de OQ-38 sobre la relación entre ambos umbrales.
  - OQ-06 sigue abierta para las equivalencias entre conceptos y la aprobación de subclases. El criterio solo resuelve el reconocimiento de especializaciones.
  - El caso del bloque C es **ilustrativo** y va al método ([subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina)). El ejemplo literal de D-020 se conserva; una nota indica que, con la condición 5, el tejido queda en «polar» y la coralina como valor.
  - Las «observaciones del caso» se recogen como observaciones del método, sin convertirlas en reglas.
- **Consecuencias:**
  - [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.3, con las secciones «Clase general: el eje de base» y «Criterio de especialización».
  - [subclasses](../20-methods/product-taxonomy/subclasses.md) 1.2, con el caso de trabajo y el enlace al criterio.
  - [integration](../20-methods/product-taxonomy/integration.md) 1.2: el umbral de la clase de estudio remite al criterio y deja de citar OQ-38 como pendiente.
  - OQ-38 cerrada; OQ-06, OQ-09 y OQ-37 anotadas; [I-11](issues.md#i-11) ampliada. Glosario: especialización (redefinida con el criterio) y nueva entrada «criterio de especialización».
- **Relacionado:** D-020, D-021, OQ-06, OQ-37, OQ-38.

### D-023

**Composición de la clase de estudio por categorías y piezas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-class-composition`, bloques A y D, procedente de la evaluación del método con tres casos más (tarea T-006). [D-021](#d-021) decía que la clase general es «una» categoría de Shopify. El juego de toallas tiene piezas de dos categorías distintas de Toallas (Toallas de baño y Toallas de mano), y el sofá cama encaja también en la hermana Sofás de dos plazas.
- **Decisión:**
  - El modelo de clase es un sistema de composición de requisitos. Cada componente (categoría de Shopify o especialización) aporta sus requisitos, y el modelo de demanda de la clase de estudio los integra sin duplicados.
  - Si el producto abarca varias categorías de Shopify, la clase general es la composición de esas categorías, no su ancestro común.
  - Una categoría entra en la composición si aporta requisitos al producto o a alguna de sus piezas. En un juego, cada pieza es una entidad. Una categoría que no aporta requisitos propios no entra.
  - La especialización «juego» aporta los requisitos del conjunto: qué piezas incluye, cuántas y en qué medidas.
  - Modifica D-021: la clase general sigue fijada por el eje de Shopify, pero puede ser una composición de varias categorías.
- **Interpretaciones adoptadas:**
  - Es un update descrito por el usuario en la conversación; se transcribe en `archive/intake/2026-10-25-class-composition.md` (situación descrita en [I-11](issues.md#i-11)).
  - Va a `10-model` como enmienda de la regla de D-021 y se incorpora como **vigente**. La cita de D-021 se sustituye por su formulación enmendada. La cita del bloque A omite, marcándolo con […], las palabras del usuario que el artefacto recoge, porque no añaden regla.
  - El artefacto no dice cómo se comprueba «aportar requisitos». Aplicarle el efecto comparativo de la condición 2 sería circular, porque esa condición compara con la clase general que estas categorías forman. La prueba operativa queda abierta en [OQ-39](open-questions.md). En los casos se aplicó así: en el sofá, Sofás de dos plazas no aporta (mismos atributos en Shopify; en Amazon es un valor). En las toallas, Toallas de mano aporta porque sus requisitos recaen sobre otra pieza, aunque sean del mismo tipo que los de Toallas de baño.
  - La regla no decide si las composiciones se registran como clases internas o se componen en cada estudio: sigue en [OQ-37](open-questions.md), que se anota.
  - El caso de las sábanas se recompone por piezas en el método. La composición anterior («Sábanas + juego») deja de figurar en el canon.
- **Consecuencias:** [demand-model](../10-model/study-class.md#composición-de-la-clase) 1.4, con la nueva sección «Composición de la clase» y la cita de D-021 marcada como enmendada; [subclasses](../20-methods/product-taxonomy/subclasses.md) 1.3, con el caso de las sábanas recompuesto y los tres casos nuevos; glosario (clase general y nueva entrada «componente de la clase de estudio»); OQ-05 y OQ-37 anotadas; nueva OQ-39. La revisión independiente detectó que el caso de las sábanas apoya «juego» y «tejido polar» en Sábanas, que ya no es componente: [I-12](issues.md#i-12).
- **Relacionado:** D-020, D-021, D-022, OQ-05, OQ-37.

### D-024

**Condición 4 del criterio de especialización: lectura estricta.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-class-composition`, bloque B. En el sofá cama, el mecanismo de apertura solo tenía apoyo en una categoría afín (Futones). La condición 4 de [D-022](#d-022) no decía si ese apoyo bastaba.
- **Decisión:**
  - La dimensión debe existir en algún componente de la clase de estudio, en cualquiera de las tres referencias: atributos de la categoría de Shopify, nodo o PTD de Amazon, o categoría de Google.
  - El apoyo en una categoría afín se anota en la ficha como evidencia complementaria, pero no basta por sí solo.
  - Una distinción que no cumple la condición no se pierde: sus cuestiones quedan en la clase general como requisitos condicionados (salida «conservar la clase y condicionar requisitos»).
- **Interpretaciones adoptadas:** precisa la condición 4 sin cambiar su texto; el artefacto la denomina «lectura estricta».
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.4; glosario (criterio de especialización).
- **Relacionado:** D-022, D-023.

### D-025

**Beneficios reclamados: no son especializaciones.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-class-composition`, bloque C. El hueso de cuerda declara que favorece la higiene dental. La condición 1 de [D-022](#d-022) excluía las etiquetas promocionales, pero no los beneficios funcionales.
- **Decisión:** un beneficio que el producto reclama no es especialización, salvo que las referencias tengan un tipo de producto definido por él. Su fundamento se evalúa en la auditoría, no en la clase.
- **Interpretaciones adoptadas:** amplía las exclusiones del criterio. «Se evalúa en la auditoría» remite a la [auditoría](../20-methods/audit-gsc/README.md) en general. Cómo llega a ella el fundamento de un beneficio que no entra en la clase (como RI, como requisito condicionado…) queda abierto en [OQ-40](open-questions.md).
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.4; glosario (especialización); nueva OQ-40.
- **Relacionado:** D-022.

### D-026

**Regla de las cuestiones propias para dimensiones que todo producto tiene.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-own-questions-offer`, bloque A, procedente de la evaluación con cuatro casos más (tarea T-007). La condición 2 de [D-022](#d-022) compara con «la clase general sin esa característica», pero no existe sofá sin tapicería ni pienso sin forma. Los casos aplicaban la observación «el material habitual de la clase queda como valor», de `INTAKE 2026-10-25-class-composition` (sección E), y con ella la tela del sofá cama Luna figuraba como valor.
- **Decisión:**
  - Para una dimensión que todo producto de la clase tiene, un valor es especialización solo si trae cuestiones propias, que no salen de las dimensiones de la clase general.
  - Si solo cambia los valores, o solo hace que algunas cuestiones dejen de aplicarse, es un valor que condiciona (como en [D-024](#d-024)).
  - Consecuencias aceptadas, con las razones del artefacto: polar (sábanas) sigue siendo especialización («trae bolitas, electricidad estática y pérdida de pelo»); algodón (sábanas, toallas, funda nórdica) es valor («número de hilos, ligamento y gramaje ya están en la base»); polipropileno (cuerda) es valor; la tela del sofá cama Luna pasa a especialización («trae resistencia a la abrasión, desenfundable y antimanchas»); la piel del Stressless es especialización («tipo y acabado de la piel»); el pienso seco es especialización («tamaño de la croqueta»); adulto es valor («solo deja de aplicar lo de crecimiento»).
- **Interpretaciones adoptadas:**
  - Precisa la condición 2 sin cambiar su texto; va a `10-model` y se incorpora como **vigente**.
  - «Las dimensiones de la clase general» se comprueban en sus referencias, incluidos los PTD de Amazon y no solo los atributos de Shopify. Se lee así a partir de una observación del artefacto, que este marca como «no son reglas»: `leather_type` está en PTD `BOOT` pero no en `SOFA`, así que la piel es valor en botas y especialización en sofás.
  - El artefacto no trata dos efectos de la condición 2 para estas dimensiones: «cambia el alcance o la desagregación» y «cambia la importancia relativa». Queda abierto en [OQ-41](open-questions.md).
  - Corrige el caso del sofá cama Luna documentado con [D-023](#d-023): la tela pasa de valor a especialización («tapicería textil»). La regla de D-023 no cambia.
  - El bloque C (aplicación a los casos) lo elaboró Claude a partir de las reglas, como indica el artefacto, y va al método como ilustración.
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.5; nueva OQ-41; [I-13](issues.md#i-13), sobre la revisión del caso de las sábanas y el apoyo de la piel del Stressless; dos observaciones de `INTAKE 2026-10-25-class-composition` quedan superadas; nuevo módulo de método [cases](../20-methods/product-taxonomy/cases.md), que recibe los casos de evaluación de subclasses (1.4) con el sofá cama corregido y cuatro casos nuevos; glosario (criterio de especialización).
- **Relacionado:** D-022, D-023, D-024.

### D-027

**La condición 1 incluye la oferta: especializaciones de oferta.** · sustituida por [D-048](#d-048) · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-own-questions-offer`, bloque B. El sofá Stressless es la última unidad de exposición, con garantía reducida «por ser producto outlet». La condición 1 de [D-022](#d-022) exigía que la característica fuera del producto. El canon habla de «clase de producto u oferta» (BASE §4), y [OQ-37](open-questions.md) preguntaba si la regla se aplica a las clases de oferta.
- **Decisión:**
  - La condición 1 pasa a decir: «es del producto o de la oferta, y estable».
  - Lo de outlet, exposición o reacondicionado pasa a ser una especialización de oferta. (Sustituida por [D-048](#d-048): la oferta no aporta requisitos ni especializaciones.)
  - Resuelve la parte de OQ-37 sobre las clases de oferta.
- **Interpretaciones adoptadas:**
  - Enmienda el texto de la condición 1: la cita del canon se sustituye por la versión enmendada. El resto de la condición («un uso, material o función declarados…») se conserva.
  - El artefacto no dice cómo se aplican las demás condiciones a una especialización de oferta; se aplican igual, como lectura sin fundamento expreso. En el caso, el apoyo de la condición 4 está en el grupo de oferta de PTD (`condition_type`, `condition_note`, garantía).
  - «Outlet» puede chocar con la exclusión de las etiquetas promocionales de la misma condición. Si outlet o exposición cuentan cuando declaran el estado de la unidad, como en el caso, queda abierto en [OQ-42](open-questions.md).
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.5, con la condición 1 enmendada y la lectura del criterio ajustada («del producto o de la oferta»); glosario (especialización y nueva entrada «especialización de oferta»); OQ-37 anotada; nueva OQ-42.
- **Relacionado:** D-022, D-026, OQ-37.

### D-028

**Clasificación objetiva: una categoría entra aunque no aporte requisitos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque A, procedente de la evaluación con cinco casos más (tarea T-008). El plaid de punto entra objetivamente en Mantas decorativas (`hg-15-1-4-2`), que no añade requisitos a los de su madre Mantas. [D-023](#d-023) decía que «una categoría que no aporta requisitos propios no entra».
- **Decisión:**
  - Palabras del usuario: «Por ordenamiento y coherencia, si hubiera una candidata que el producto entraría por clasificación objetiva, aunque no aporte nada, la añadimos. […]».
  - Una categoría candidata en la que el producto entra por clasificación objetiva forma parte de la composición aunque no aporte requisitos propios.
  - Sustituye «Una categoría que no aporta requisitos propios no entra»: aportar requisitos al producto o a alguna de sus piezas sigue siendo vía de entrada, pero no la única.
  - Lecturas aceptadas por el usuario: en el plaid entra Mantas decorativas y no Mantas para sillones y sofás (`hg-3-77`), que es una entrada duplicada en Decoración para el mismo tipo de producto; en la manta Nacarina, la clasificación objetiva es Mantas (`hg-15-1-4`) y no Mantas decorativas, porque el uso en sofá depende de la variante (medida).
  - Consecuencia aceptada: el sofá cama Luna, que es objetivamente un sofá de dos plazas, pasa a Sofás cama + Sofás de dos plazas (`fr-22-4`).
- **Interpretaciones adoptadas:**
  - Enmienda la regla de D-023: la cita del canon sustituye su tercer punto por la formulación enmendada. El resto de D-023 no cambia.
  - El artefacto no dice cómo se prueba que un producto entra «por clasificación objetiva», ni cómo se reconoce una entrada duplicada de Shopify. Queda abierto en [OQ-43](open-questions.md). Las dos lecturas aceptadas se documentan como casos.
  - El bloque E (aplicación a los casos) lo elaboró Claude, como indica el artefacto, y va al método como ilustración.
- **Consecuencias:** [demand-model](../10-model/study-class.md#composición-de-la-clase) 1.6; [cases](../20-methods/product-taxonomy/cases.md) 1.1, con el sofá cama Luna corregido y cinco casos nuevos; glosario (componente de la clase de estudio y nueva entrada «clasificación objetiva»); OQ-39 anotada; nueva OQ-43.
- **Relacionado:** D-021, D-023, OQ-39, OQ-43.

### D-029

**Base de una categoría de Shopify: atributos propios y de sus madres.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque B. En Shopify v2026-08, 1749 de 14580 categorías hijas tienen solo una parte de los atributos de su madre: Mantas decorativas tiene 3 y Mantas, 9; Sofás cama, 9 y Sofás, 17. Con la lectura literal, Mantas para sillones y sofás aportaría al plaid tejido, color, cuidados y patrón, y entraría como segunda categoría de un producto de una sola pieza.
- **Decisión:** la base de una categoría de Shopify son sus atributos propios más los de sus categorías madre (una categoría hija es un tipo de su madre).
- **Interpretaciones adoptadas:**
  - Precisa qué son los atributos de una categoría de Shopify en [D-023](#d-023) (aportar requisitos), [D-024](#d-024) (condición 4) y [D-026](#d-026) (dimensiones de la clase general), sin cambiar su texto. Se incorpora como **vigente** en `10-model`.
  - «Sus categorías madre» se lee como todas sus categorías ascendientes: el plural y la razón («una categoría hija es un tipo de su madre») se aplican de forma transitiva.
  - Resuelve [I-12](issues.md#i-12): en el caso de las sábanas, `bedding-pieces-included` y `fabric` están en Sábanas (`hg-15-1-2`), la madre de Sábanas planas y Sábanas ajustables, así que forman parte de la base de esos componentes. Los apoyos de «juego» y «tejido polar» quedan en componentes de la clase.
- **Consecuencias:** [demand-model](../10-model/study-class.md#composición-de-la-clase) 1.6; [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina) 1.5, con los apoyos del caso de las sábanas en la base heredada; I-12 resuelta; observación del sofá cama en [cases](../20-methods/product-taxonomy/cases.md) actualizada.
- **Relacionado:** D-023, D-024, D-026, I-12.

### D-030

**Características especiales de un PTD: dimensiones de la base y apoyo.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque C. En la manta, la electricidad estática y la pelusa solo figuran en la base como valores de `special_feature` de PTD `BLANKET` («Antiestático», «Sin pelusa»). En las zapatillas, la absorción figura igual en `SLIPPER` («Absorbe la humedad»), y en el cojín, el material reciclado en `PILLOW` («Reciclada»).
- **Decisión:** los valores de la propiedad «Características especiales» (`special_feature`) de un PTD de Amazon cuentan como dimensiones de la base de la clase (regla de las cuestiones propias) y como apoyo (condición 4).
- **Interpretaciones adoptadas:**
  - Precisa [D-024](#d-024) y [D-026](#d-026) sin cambiar su texto. Se incorpora como **vigente** en `10-model`.
  - Presupone y confirma la lectura adoptada en D-026: las dimensiones de la clase general se comprueban en sus referencias, incluidos los PTD.
  - El artefacto reconoce un riesgo y no lo trata: el resultado depende de qué valores incluyó Amazon en cada lista (la de `BLANKET` no tiene «Resistente a la formación de bolitas»; la de `SLIPPER` sí). Se registra en la decisión. No se abre cuestión, porque las especializaciones ya quedan provisionales hasta su validación y el contraste MPIR ([D-022](#d-022)).
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.6; glosario (criterio de especialización); [cases](../20-methods/product-taxonomy/cases.md) 1.1 (manta, zapatillas y cojín). La revisión independiente detectó que la regla cambia la base de casos ya documentados: [I-14](issues.md#i-14).
- **Relacionado:** D-022, D-024, D-026, I-14.

### D-031

**El material reciclado es especialización, no beneficio reclamado.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque D. El cojín declara 87 % algodón reciclado y 13 % poliéster reciclado, y se presenta como «producto sostenible». [D-025](#d-025) excluye los beneficios reclamados.
- **Decisión:** «material reciclado» es especialización, no beneficio reclamado: es composición verificable y trae cuestiones propias (qué proporción y en qué parte). «Sostenible» sí es beneficio reclamado (D-025).
- **Interpretaciones adoptadas:**
  - Precisa D-025 sin cambiar su texto. Se incorpora como **vigente** en `10-model`.
  - La especialización sigue sometida a las cinco condiciones; en el caso, el apoyo está en `PILLOW` (`special_feature` «Reciclada», [D-030](#d-030)).
  - La decisión se refiere al material reciclado. El artefacto no la extiende a otras características ambientales del material; se examinan con el criterio.
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.6; glosario (especialización); [cases](../20-methods/product-taxonomy/cases.md) 1.1 (cojín).
- **Relacionado:** D-022, D-025, D-030.

### D-032

**Propósito de la clase de estudio: los requisitos informativos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirements-purpose`, procedente de la tarea T-008. La revisión independiente del update anterior abrió [I-14](issues.md#i-14): con [D-029](#d-029) y [D-030](#d-030), algunas cuestiones que los casos contaban como propias están en la base, y la tela del sofá cama Luna, especialización por una consecuencia aceptada de [D-026](#d-026), pasaría a valor. En el juego de funda nórdica bordada, la clasificación objetiva ([D-028](#d-028)) planteaba si entra Juegos de cama (`hg-15-1-11`).
- **Decisión:**
  - Palabras del usuario: «Recuerda que el propósito es establecer requisitos informativos. Esto es lo más importante (+ el matiz de denominación que hemos especificado cuando tiene sentido aunque no aporte)». El matiz es la clasificación objetiva (D-028).
  - Lectura aceptada: la pregunta que manda es qué requisitos informativos produce la clase; que algo sea especialización o valor es instrumental. Lo único que entra sin aportar requisitos es lo que nombra la clase por clasificación objetiva, cuando tiene sentido.
  - Sofá cama Luna: los requisitos no cambian. La resistencia a la abrasión, el desenfundable y el antimanchas siguen siendo requisitos, que ahora salen de la base de PTD `SOFA` (D-030). Que la tela pase a valor es un cambio de etiqueta, y el matiz de denominación no se aplica porque no es una categoría de clasificación objetiva. La clase queda en Sofás cama + Sofás de dos plazas. Sofás de dos plazas sí está bien añadido: no aporta requisitos, pero nombra lo que el producto es.
  - Resto de I-14: no cambia ningún requisito. El lavado de la cuerda y la resistencia a la mordida siguen siendo requisitos, igual que las bolitas, la electricidad estática y la pérdida de pelo del polar, y qué piezas incluye el juego, cuántas y en qué medidas. Se aplican las propuestas: la cuerda sigue siendo especialización por el deshilachado y la ingestión de fibras, y el lavado pasa a la base; el polar de las sábanas sigue siendo especialización, porque la pérdida de pelo no está en ninguna base; el efecto del juego se escribe con los requisitos del conjunto de [D-023](#d-023); se documenta el apoyo del polar en la manta. Leer la base pieza a pieza o para todo el juego no altera el resultado.
  - Juegos de cama no entra en el juego de funda nórdica: no aporta requisitos y traería uno que no aplica (el nivel de calidez «del edredón o la colcha», en un juego de fundas sin relleno). Añadirlo empeoraría los requisitos, así que tampoco tiene sentido por denominación. Además, Amazon separa los juegos de edredón o colcha (PTD `BEDDING_SET`, con `fill_material`) de los juegos de fundas (`BED_LINEN_SET`).
- **Interpretaciones adoptadas:**
  - Es un principio de lectura de la clase de estudio; va a `10-model` junto al principio de especificidad informativa necesaria y se incorpora como **vigente**. No cambia el texto de las reglas D-020 a D-031.
  - Revisa la consecuencia de D-026 sobre la tela del sofá cama Luna. Con ella, la observación de `INTAKE 2026-10-25-class-composition` «el método no fuerza especializaciones (sofá cama)» deja de estar superada.
  - Mordedor: la propuesta aceptada de I-14 era comprobar si «Uso rudo» cubre la resistencia a la mordida. PTD `PET_TOY` tiene en `special_feature` «Uso rudo» y «Tecnología Chew Guard». Se lee que «Uso rudo» la cubre; «Chew Guard» es el nombre de una tecnología y solo refuerza la lectura. Con el mismo criterio que la tela del sofá cama, el mordedor pasa a valor que condiciona, y la resistencia a la mordida sigue siendo requisito. Es una interpretación de Claude, provisional hasta que la valide el usuario.
  - En el juguete de cuerda, la base de Amazon se lee en `PET_TOY`, el PTD de los nodos hijos (Cuerdas, Juguetes para morder…), porque el nodo de la clase general (`13441958031`) tiene `PET_SUPPLIES`, que no tiene `special_feature`.
  - Juegos de cama precisa cómo se aplica «cuando tiene sentido»: una categoría que traería requisitos que no aplican no entra por denominación. Se anota en [OQ-43](open-questions.md).
  - El bloque C (casos) lo elaboró Claude y va al método como ilustración.
- **Consecuencias:** [demand-model](../10-model/study-class.md) 1.7, con el principio y la lectura citados, la precisión de la clasificación objetiva y sin la frase que repetía el paso 3 de la regla; [cases](../20-methods/product-taxonomy/cases.md) 1.2 (sofá cama, juguete de cuerda, manta, juego de funda nórdica, protector y nuevo caso del juego de funda nórdica bordada); `product-taxonomy` (README) 1.5; I-11 ampliada; I-13 anotada; [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina) 1.6; I-14 resuelta; OQ-43 anotada; glosario (clase de estudio, componente de la clase de estudio y clasificación objetiva). La revisión independiente detectó que `warmth-level` no está solo en Juegos de cama, como dice el caso de las sábanas: [I-15](issues.md#i-15).
- **Relacionado:** D-020, D-026, D-028, D-029, D-030, I-14, OQ-43.

### D-033

**Identidad del modelo de demanda: composición de bloques de requisitos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloques A y G, procedente de la tarea T-010 tras el experimento base del clasificador (T-009). Hasta ahora la clase de estudio (categorías + especializaciones) identificaba el modelo, y la clasificación objetiva podía entrar en su denominación aunque no aportara requisitos ([D-028](#d-028), [D-032](#d-032)).
- **Decisión:**
  - Palabras del usuario: «el modelo de demanda de un producto se "denomine" por su composición de requisitos. Es decir, composición de clase <> composición de requisitos».
  - La unidad de composición son bloques de requisitos (general universal, generales condicionados, sector, categoría, especialización). Un bloque agrupa las cuestiones que trae un mismo hecho y lleva su importancia por defecto, revisable por el modelo con justificación.
  - (Enmendada por [D-047](#d-047): el modelo va con el producto y se identifica por sus bloques; la aplicación es de la oferta.) Identidad = modelo de requisitos (conjunto de bloques, incluidos los condicionados con su disparador) + aplicación concreta (qué bloques condicionados se activan o dejan de aplicarse en una oferta); ambos se identifican en la denominación.
  - Las categorías que entran por clasificación objetiva sin aportar requisitos son alias: «el objetivo de esto es puramente de etiquetado, denominación».
  - La composición de la clase es el medio de descubrimiento. La especialización es la característica que forma un bloque; una característica que revela una dimensión de toda la clase no forma bloque: su cuestión va al bloque de la clase y el valor declarado es la respuesta.
  - Estructura: la clase de estudio pasa a su propio módulo canónico, `study-class`.
- **Interpretaciones adoptadas:**
  - Va a `10-model` como vigente: es un concepto del modelo de demanda.
  - Precisa D-028 y D-032: la clasificación objetiva sigue rigiendo qué categorías se nombran, pero como alias, fuera de la identidad.
  - Resuelve la parte de [OQ-37](open-questions.md) sobre si las composiciones se registran: se registran los modelos como composiciones de bloques. El resto de OQ-37 sigue abierto.
  - El artefacto no fija el formato ni los identificadores de los bloques ni la sintaxis de la denominación más allá del ejemplo: [OQ-44](open-questions.md).
  - «Bloques de sector (atributos heredados de Shopify)» se lee como los atributos que una categoría hereda de sus madres, y los bloques de categoría como sus atributos propios, para no contar dos veces los de la base de D-029.
  - Precisa [D-020](#d-020): la clase de estudio deja de identificar el modelo y pasa a ser el medio para descubrir sus bloques.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.0 (reestructurado); nuevo módulo [study-class](../10-model/study-class.md) 1.0, con la sección que salió de demand-model y las reglas nuevas; nuevo módulo de método [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.0; enlaces actualizados; glosario.
- **Relacionado:** D-020, D-028, D-032, D-034, OQ-37.

### D-034

**Capa general de requisitos: universales y condicionados.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloque B. Hay requisitos que aplican a cualquier producto, como el precio. El canon preveía «requisitos comunes» sin definirlos, y la taxonomía de producto no cubre la oferta.
- **Decisión:**
  - La capa general tiene cuestiones universales y cuestiones condicionadas con disparador declarado; el disparador es el hecho declarado, no la etiqueta.
  - Sus importancias son valores por defecto revisables por clase con justificación. (Enmendada por [D-045](#d-045): quedan fijas como parte del marco.)
  - Borrador inicial aceptado «para empezar, lo iremos perfeccionando» (catálogo en `requirement-blocks`).
- **Interpretaciones adoptadas:** el concepto va a `10-model` como vigente; el catálogo, a `20-methods` como propuesta. Las dudas del artefacto (envío ¿crítico?, medios de pago, opiniones, información precontractual por comprobar) quedan abiertas en [OQ-44](open-questions.md). En los casos, un descuento declarado activa la cuestión condicionada de descuento (aplicación «con descuento»).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#capa-general) 2.0; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general).
- **Relacionado:** D-033, D-035, D-037.

### D-035

**Pruebas operativas de importancia relativa.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloque C. El canon define crítico, principal y complementario, pero su calibración estaba abierta ([OQ-02](open-questions.md)).
- **Decisión:**
  - Pruebas aceptadas «para empezar, lo iremos perfeccionando»: crítico, si sin resolverla la oferta deja de ser evaluable; principal, si es criterio para comparar y elegir ofertas de la clase; complementario, si es relevante sin ser indispensable ni central.
  - La confianza en un requisito es independiente de su importancia.
- **Interpretaciones adoptadas:** son lectura operativa de las definiciones del canon, sin escala nueva; van al método como propuesta. La regla de la confianza va al canon como vigente. OQ-02 se anota, no se cierra: falta la calibración con casos comparables.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#importancia-relativa) 2.0; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#pruebas-de-importancia); OQ-02 anotada.
- **Relacionado:** D-034.

### D-036

**Cuestiones inferidas: tercera vía de construcción, provisional.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloques D y F. Hay cuestiones de toda la clase que ninguna referencia recoge (el mecanismo de apertura de un sofá cama). El sistema de construcción solo tenía dos vías (taxonomía y MPIR).
- **Decisión:**
  - Palabras del usuario: «quizás no debemos esperar a validarlos por el MPIR sino darlos por válidos, confiar en el agente que los infiere».
  - Entran en el modelo como provisionales, en el régimen de [D-022](#d-022): las propone el clasificador; se usan en la auditoría, el usuario valida siempre las críticas y una muestra del resto, y el MPIR las confirma o revisa cuando exista; con los controles del artefacto (toda la clase, neutrales, justificadas, sin duplicar la base, origen marcado, informe con y sin ellas, dos ejecuciones por caso).
- **Interpretaciones adoptadas:**
  - El régimen provisional es una lectura de Claude que siguió a la propuesta del usuario y que este no objetó; así lo indica el artefacto, y así se cita.
  - Enmienda BASE §4.2 (dos vías, ya enmendada por [D-009](#d-009)): se añade una tercera vía, sin cambiar las otras dos.
  - Casos: el mecanismo de apertura del sofá cama Luna y la preparación y el acabado del algodón (funda bordada) entran como cuestiones inferidas del bloque de la clase.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 2.0; READMEs de product-taxonomy y mpir (tercera vía); D-009 ampliada; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas); [cases](../20-methods/product-taxonomy/cases.md) 1.3; OQ-01 anotada.
- **Relacionado:** D-009, D-022, D-033.

### D-037

**Valores de oferta y activación de cuestiones condicionadas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloques E y F. Con la capa general, la condición de la unidad es un requisito general. [D-027](#d-027) ponía como ejemplo «lo de outlet, exposición o reacondicionado pasa a ser una especialización de oferta», y [OQ-42](open-questions.md) preguntaba si el outlet cuenta como estado o como etiqueta promocional.
- **Decisión:**
  - Outlet, liquidación, exposición o reacondicionado son valores de la oferta que condicionan cuestiones generales, no especializaciones, para cualquier producto.
  - Extensión de [D-026](#d-026): un valor que activa cuestiones condicionadas ya previstas en la base también es valor que condiciona; solo es especialización si trae cuestiones que la base no prevé.
- **Interpretaciones adoptadas:**
  - Sustituye el ejemplo de D-027; se mantiene que la condición 1 incluye la oferta. (Sustituida por [D-048](#d-048): la condición 1 solo admite características del producto.)
  - Cierra OQ-42: en ambos casos el valor condiciona cuestiones generales.
  - Revisión de casos (bloque F, aplicación de Claude aceptada): en el Stressless, el reclinable pasa a valor que condiciona, la piel sigue siendo especialización y el outlet pasa a valor (aplicación: unidad no nueva); polar, punto, seco y cuerda siguen siendo especialización.
- **Consecuencias:** [study-class](../10-model/study-class.md#criterio-de-especialización) 1.0, con la cita «Oferta» sustituida; [cases](../20-methods/product-taxonomy/cases.md) 1.3; OQ-42 cerrada.
- **Relacionado:** D-026, D-027, D-034, OQ-42.

### D-038

**Catálogo de bloques: capa general contrastada, identificadores propios y denominación.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-block-catalog`, tarea T-011. [OQ-44](open-questions.md) dejaba abiertos el formato y los identificadores de los bloques, la sintaxis de la denominación y las dudas del borrador de la capa general ([D-033](#d-033), [D-034](#d-034)). Claude comprobó el artículo 97.1 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (RDL 1/2007), versión consolidada del BOE a 28/02/2026.
- **Decisión:**
  - Capa general contrastada con el artículo 97.1 (aceptado: «1. ok. opiniones como complementaria»): precio y envío se unen en una cuestión crítica de precio total; lo que hace variar el envío es principal; los medios de pago entran como complementaria; el contacto del vendedor, complementaria; se reformulan desistimiento y devoluciones (97.1.j, k, m) y garantías y posventa (97.1.n, ñ); nuevas condicionadas: precio personalizado (97.1.f) y elementos digitales (97.1.s, t), principales, y duración, suscripción y depósitos (97.1.p, q, r); quedan fuera las letras g, i, o y u; las opiniones de clientes entran como complementaria.
  - Identificadores propios. Palabras del usuario: «el formato de id debe ser nuestro, no quiero acoplarme por si en el futuro cambian las referencias. Para mantener trazabilidad con referencia puedes especificar un formato como el propuesto pero no como el campo de id, sino más bien como de referencias o algo del estilo. Lo dejo a tu criterio».
  - Denominación en dos niveles, clave y nombre (aceptada: «3. si»).
  - Del resto del bloque B, aceptado por el usuario: los campos del bloque (identificador, tipo, nombre, disparador, versión, estado y requisitos) y del requisito (identificador, pregunta, dimensión, entidad, importancia por defecto, origen —referencias, inferida o normativa—, fundamento y aplicabilidad); las cuestiones inferidas dentro del bloque de su categoría, con el origen marcado en cada requisito; el catálogo como datos en `demand-engine/catalog/`.
  - Los medios de pago entran porque son información previa a la compra, aunque la transacción quede fuera del alcance.
- **Interpretaciones adoptadas:**
  - Formato de identificadores, por delegación del usuario: `gen`, `gen.<hecho>`, `cat.<nombre>` y `esp.<nombre>` para bloques, y `<bloque>/<nn>` para requisitos; `<nombre>` es un nombre propio, estable y único que no se deriva de las etiquetas de las referencias. Las referencias van en un campo aparte con formato `<fuente>:<identificador>@<versión>`. El tipo de bloque único para sector y categoría que propuso Claude (`shp:`) se mantiene como `cat.`, con los atributos propios de cada categoría.
  - Las opiniones entran como cuestión universal complementaria, con la parte de la propuesta de Claude sobre cómo se garantiza que proceden de compradores reales, si se publican. La trasposición de la directiva Omnibus queda por comprobar.
  - El artefacto no da importancia a la condicionada de duración, suscripción y depósitos: queda por fijar ([OQ-45](open-questions.md)). Las tres letras (p, q, r) se agrupan en un bloque `gen.suscripcion`, cuyo disparador es «si es una suscripción o hay depósito».
  - Precisiones de formato de Claude: valores del estado (propuesta o validado; enmendados por [D-045](#d-045): no compilado o compilado); campo «referencias» del bloque y campo «fuentes» del requisito, este a nivel de atributo cuando procede (`shopify-attr:…`, `amazon-ptd-prop:…`); las entidades del catálogo incluyen entrega y condiciones.
  - La cuestión universal de disponibilidad se separa de la cantidad, que pasa a la condicionada `gen.cantidad-limitada` (crítica, como la cuestión original), para que coincida con el disparador «si la cantidad es limitada» de la capa general.
  - La sintaxis de la denominación va al canon (cita literal); el formato del catálogo y la capa general, al método.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.1; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.1 (catálogo de la capa general, formato del catálogo y denominación); OQ-44 cerrada; nueva OQ-45; glosario (bloque de requisitos).
- **Relacionado:** D-033, D-034, OQ-44, OQ-45.

### D-039

**Los PTD de Amazon, fuente de requisitos de la categoría.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-amazon-source-blocks`, tarea T-016, tras el segundo experimento del clasificador (T-012). Se perdió un 35 % de las cuestiones clave por un hueco entre [D-009](#d-009), [D-030](#d-030) y [D-036](#d-036): una cuestión que solo recoge Amazon contaba como base para decidir la etiqueta, pero no era fuente de requisitos ni podía ser inferida.
- **Decisión (aceptada: «ok a 1 y 2»):** alternativa descartada: mantener D-009 y tratarlas como inferidas con Amazon de apoyo, lo que exigía redefinir «inferida». Se decide que las propiedades de los PTD de Amazon, incluidos los valores de special_feature, pueden ser fuente de requisitos de la categoría cuando son relevantes para la clase, con origen «referencias». Enmienda D-009.
- **Interpretaciones adoptadas:**
  - Se enmienda la frase del canon según la cual Amazon y Google son fuentes de apoyo, «no fuentes directas de RI»: Amazon puede serlo a través de sus PTD; Google sigue siendo solo de apoyo, porque el artefacto no lo menciona.
  - «Relevantes para la clase» se decide en la revisión del catálogo de bloques de categoría ([D-040](#d-040)). (Precisada por [D-044](#d-044): lo deciden las reglas inducidas en el entrenamiento.)
  - Las cuestiones inferidas siguen siendo las que no recoge ninguna referencia, ahora incluidos los PTD de Amazon; D-036 no cambia.
- **Capas:** la regla va al canon (`demand-model`, vigente); su operación, al método (`requirement-blocks`, `sources`, propuesta).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 2.2; [README de product-taxonomy](../20-methods/product-taxonomy/README.md) 1.7; [sources](../20-methods/product-taxonomy/sources.md) 1.1; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.3; [data-model-governance](../20-methods/product-taxonomy/data-model-governance.md); [cases](../20-methods/product-taxonomy/cases.md) 1.4 (el acabado del algodón deja de ser inferido); glosario (cuestión inferida). La revisión independiente detectó una posible tensión con D-030 en el filtro de relevancia: [I-17](issues.md#i-17).
- **Relacionado:** D-009, D-030, D-036, D-040.

### D-040

**Bloques de categoría deterministas y catálogo revisado.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-amazon-source-blocks`. En el segundo experimento, los bloques de sector coincidieron en 4 de 14 casos entre ejecuciones: Shopify repite atributos como propios en varios niveles y cada agente los asignaba a un nivel distinto. [D-038](#d-038) fijaba que un bloque de categoría lleva los atributos propios de su categoría.
- **Decisión (aceptada: «ok a 1 y 2»):** construir los bloques de categoría de forma determinista: un atributo repetido va siempre al bloque de la categoría más general que lo lista. Crear un catálogo de bloques cat. (preguntas e importancia por defecto), generado con la herramienta y revisado una vez por categoría; el clasificador elige bloques en lugar de redactarlos.
- **Interpretaciones adoptadas:**
  - Precisa D-033 y D-038: un bloque de categoría lleva los atributos propios de su categoría que no lista ninguna de sus madres.
  - La revisión la hace el usuario; hasta entonces el bloque está en estado propuesta. (Con [D-044](#d-044) y [D-045](#d-045): lo compila el entrenamiento; hasta entonces está «no compilado».) El clasificador sigue redactando las cuestiones inferidas y las especializaciones.
  - Las propiedades de Amazon (D-039) van al bloque de la categoría que la tabla de correspondencia `catalog/amazon-map.json` asocia a su PTD (una por categoría; si varias de la cadena comparten PTD, la más general); una propiedad que solo se aplica a una categoría hija va al bloque de la hija; si repite una dimensión que ya cubre un atributo de Shopify, no se duplica. El artefacto no lo dice; es la lectura necesaria para que el generador sea determinista.
  - **Capas:** la regla de asignación va al canon (`demand-model`); el catálogo y su generación, al método y al motor.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.2; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.3; glosario (bloque de requisitos); el catálogo de bloques se genera en `demand-engine/catalog/`. La revisión independiente detectó que las cuestiones inferidas dentro de un bloque de categoría hacen variar su contenido: [I-16](issues.md#i-16).
- **Relacionado:** D-033, D-038, D-039.

### D-041

**Entrenamiento y ejecución: la revisión humana no bloquea la ejecución.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-runtime`, tarea T-016. Palabras del usuario: «la revisión humana solo debe ser en tiempo de entrenamiento, en tiempo de ejecución debe ser automático». El canon podía leerse como bloqueante en dos puntos: una categoría que aún no está en el catálogo ([D-040](#d-040)) y la validación de las cuestiones inferidas críticas ([D-036](#d-036)). La incidencia [I-16](issues.md#i-16) señalaba además que las inferidas dentro de un bloque de categoría hacían variar su contenido.
- **Decisión (aceptada: «si»):**
  - Entrenamiento, con revisión humana: el usuario revisa los bloques nuevos del catálogo, las cuestiones inferidas, las especializaciones y las importancias, y calibra con el conjunto de casos; lo aprobado pasa a «validado».
  - Ejecución, totalmente automática: se usan los bloques del catálogo; si la categoría no está, el motor genera y redacta el bloque, lo usa marcado «no revisado» y lo encola. Las inferidas y las especializaciones nuevas se usan como provisionales y se encolan.
  - Trazabilidad: cada resultado indica qué partes del modelo usó sin revisar, para que la auditoría pueda informar con ellas y sin ellas.
  - Una cuestión inferida se usa en la ejecución como añadido provisional del modelo, marcado y fuera de la clave; al aceptarse, se incorpora al bloque del catálogo como nueva versión. Resuelve I-16.
- **Interpretaciones adoptadas:**
  - Matiza [D-022](#d-022), D-036, [D-038](#d-038) y D-040: sus validaciones se hacen en entrenamiento, y las cuestiones inferidas dejan de ir directamente al bloque de su categoría (D-038). El texto citado de D-036 («el usuario valida siempre las críticas…») se mantiene: «siempre» significa que ninguna crítica queda sin revisar, no que la ejecución espere.
  - La regla va al canon (`demand-model`, vigente); la operación del catálogo, al método (`requirement-blocks`, propuesta). La implantación de la redacción automática, la caché y la cola en el motor queda fuera de la documentación.
  - Alcance: las palabras del usuario son generales, pero el update se refiere a la construcción del modelo de demanda (catálogo, inferidas, especializaciones e importancias). Las revisiones humanas del MPIR y de la auditoría no se tocan; si el principio se extiende a ellas queda abierto en [OQ-46](open-questions.md).
  - La revisión independiente detectó tres lagunas de estados y versiones (qué cuenta como «no revisado», muestra frente a aceptación de las inferidas, versión del bloque en la clave): [I-19](issues.md#i-19).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#entrenamiento-y-ejecución) 2.3; [study-class](../10-model/study-class.md#criterio-de-especialización) 1.1; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.4; [cases](../20-methods/product-taxonomy/cases.md) 1.5; I-16 resuelta; nuevas I-19 y OQ-46; glosario (entrenamiento, ejecución).
- **Relacionado:** D-022, D-036, D-038, D-040, I-16, I-19, OQ-46.

### D-042

**Capa original del MPIR: sin capturas de pantalla y políticas de acceso del motor.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-mpir-capture-engine`, tareas T-002 y T-013. El usuario pidió empezar el MPIR por la infraestructura y un motor de captura que evite bloqueos sin tardar «una eternidad». Claude propuso conservar también una captura de pantalla por recurso; el usuario respondió: «no hace falta captura de pantalla. Implementa el motor».
- **Decisión:**
  - La capa original del MPIR no conserva capturas de pantalla. El método no las exige y evitan la tentación de juzgar por la prominencia (cautela 4: «prominencia editorial ≠ importancia relativa»).
  - Entre las políticas aplicables que el método manda respetar, el motor aplica robots.txt (RFC 9309) y las reservas de minería de textos y datos expresadas por medios de lectura mecánica (art. 67.3 TRLPI: TDMRep, cabecera y meta `tdm-reservation`).
- **Interpretaciones adoptadas:**
  - Las políticas de acceso precisan «el rastreo respetará las políticas aplicables» y no crean conceptos. Aplicar una reserva significa no conservar el contenido del recurso; sí se conservan los metadatos de la visita.
  - La divergencia sobre el renderizado (el motor renderiza siempre) no se resuelve aquí: se registra en [I-18](issues.md#i-18).
  - OQ-14 y OQ-15 quedan anotadas con lo que fija el motor de forma provisional, sin cerrarse: la configuración definitiva la decide la sonda T-014.
- **Consecuencias:** [sampling-capture](../20-methods/mpir/sampling-capture.md#qué-se-conserva-en-la-capa-original) 1.1; I-18 abierta; OQ-14 y OQ-15 anotadas.
- **Relacionado:** I-18, OQ-14, OQ-15.

### D-043

**Criterios de redacción del catálogo de bloques de categoría.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-catalog-criteria`, tarea T-016. Tres agentes redactaron un borrador de 27 bloques de categoría ([D-040](#d-040)) con criterios distintos: importancia de las medidas, atributos con muchos valores, solapes con la capa general, propiedades repetidas de Amazon y cuestiones inferidas.
- **Decisión (aceptada: «si»):** cinco criterios: una medida es crítica cuando fija qué se vende y principal cuando solo describe; los atributos que mezclan temas se dividen por tema; un bloque de categoría solo repite una cuestión general si la concreta con algo propio de la clase, y las piezas incluidas pasan a esp.juego; una propiedad de Amazon repetida en categorías hermanas sube a la madre común solo si vale para todas sus hijas; las cuestiones inferidas propuestas se incluyen como provisionales y el usuario las aprueba una a una.
- **Interpretaciones adoptadas:**
  - Son criterios de método (`requirement-blocks`, propuesta) que aplican las pruebas de importancia de [D-035](#d-035) y la asignación de [D-040](#d-040); no cambian el canon.
  - El criterio 4 completa la lectura de D-040 sobre las propiedades de Amazon (que van a la categoría que la tabla de correspondencia asocia a su PTD).
  - Las tres tareas anunciadas por Claude se recogen en el método: la composición textil con origen «normativa» (Reglamento (UE) 1007/2011, art. 16.1, comprobado en el DOUE L 272 de 18.10.2011; importancia principal), la lectura de las propiedades descriptivas del grupo de cumplimiento de Amazon y la entidad «producto» para el color.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#criterios-de-redacción-del-catálogo) 1.5; el catálogo de `demand-engine/catalog/cat/` se corrige con estos criterios.
- **Relacionado:** D-035, D-038, D-040, D-041.

### D-044

**Marco humano y reglas inducidas: el usuario define el marco, no revisa reglas ni requisitos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-induced-rules`, tarea T-016. [D-041](#d-041) preveía que en entrenamiento el usuario revisara bloques, inferidas, especializaciones e importancias, y [D-036](#d-036) que validara siempre las inferidas críticas. Ante el borrador del catálogo de bloques de categoría, el usuario rechazó la revisión manual de requisitos y también la de reglas sueltas.
- **Decisión:**
  - Palabras del usuario: «Lo que defino es el marco general, objetivos, características del resultado, etc. Las reglas concretas deben ser producto del entrenamiento también» y «La parametrización específica puede formar parte del sistema, pero como un resultado compilado, no como un diseño específico».
  - Marco del usuario, única intervención humana: propósito, objetivos y características del resultado, criterios de éxito e invariantes del canon. El usuario lee el informe agregado del entrenamiento y, si hace falta, ajusta el marco.
  - Entrenamiento en ocho pasos (reunir casos, aplicar las reglas vigentes dos veces por caso, medir contra el marco, detectar patrones, inducir reglas generales y específicas, compilar el catálogo, validar automáticamente, publicar versión e informe) y ejecución automática con lo compilado, según el diagrama aprobado («documenta»).
- **Interpretaciones adoptadas:**
  - Enmienda D-041 (el entrenamiento ya no es una revisión humana) y [D-036](#d-036) (la validación de las inferidas la hace el entrenamiento contra el marco). Precisa [D-022](#d-022) (la «validación del usuario» de una especialización pasa a ser la del entrenamiento), [D-039](#d-039) (la relevancia de las propiedades de Amazon la deciden las reglas inducidas, paso 5 del entrenamiento) y [D-040](#d-040) (el catálogo se compila, no se revisa a mano). Sustituye el criterio 5 de [D-043](#d-043) (la aprobación una a una de las inferidas) por la validación automática.
  - Las decisiones ya aceptadas del canon, incluidos los criterios de [D-035](#d-035) y D-043, forman parte del marco: las reglas inducidas operan dentro de ellas. Si el entrenamiento las encuentra contraproducentes, lo dice en el informe agregado; no las cambia.
  - La capa general ([D-034](#d-034), [D-038](#d-038)) está dentro del rango «D-020 a D-043» del marco: el principio «ningún bloque ni importancia se diseña a mano» se aplica al catálogo que compila el entrenamiento, no a la capa general. Sus importancias siguen siendo valores por defecto.
  - La revisión de la importancia por defecto «por clase con justificación» ([D-033](#d-033), [D-034](#d-034)) la hacen las reglas específicas inducidas en el entrenamiento; la ejecución no revisa importancias. (Precisada por [D-045](#d-045): no se aplica a la capa general, que queda fija.)
  - «Cada requisito guarda la regla que lo decidió» se traduce en un campo «regla» del requisito en el formato del catálogo.
  - «No revisado», en la cita de la ejecución de D-041, significa no compilado por el entrenamiento.
  - Va a `10-model` como vigente, en un módulo nuevo, `model-training`, que recibe la sección «Entrenamiento y ejecución» de `demand-model`. El diagrama no fija el vocabulario de rasgos, la forma operativa de las métricas ni el formato del informe: [OQ-47](open-questions.md).
- **Consecuencias:** nuevo módulo [model-training](../10-model/model-training.md) 1.0; [demand-model](../10-model/demand-model.md#entrenamiento-y-ejecución) 2.4; [study-class](../10-model/study-class.md#criterio-de-especialización) 1.2; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.6; D-039 precisada; I-17 e I-19 anotadas; OQ-02 y OQ-46 anotadas; nueva OQ-47; glosario (entrenamiento, ejecución, marco, regla inducida, catálogo compilado, bloque de requisitos, criterio de especialización); índice de `docs/README.md`.
- **Relacionado:** D-022, D-033, D-034, D-035, D-036, D-038, D-039, D-040, D-041, D-043, I-17, I-19, OQ-02, OQ-46, OQ-47.

### D-045

**Operación del entrenamiento, primera versión: rasgos, reglas de importancia por el árbol de Shopify y métricas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-operation`, tarea T-019. [OQ-47](open-questions.md) dejaba abiertos el vocabulario de rasgos, la forma operativa de las métricas, el informe agregado y los casos de entrenamiento; [I-19](issues.md#i-19), la versión de los bloques en la clave y el estado de los bloques generados en ejecución. Claude propuso un plan para una primera versión. El usuario objetó que las reglas de importancia se miraran a nivel global («Lo único que no me encaja es que se mire a nivel global. Estas reglas deberían ser al menos para clases generales»). Claude respondió que lo global contradice D-035 («principal» es relativo a la clase) y arrastraría el sesgo textil del catálogo, y que solo por clase no generaliza; el usuario aprobó la opción C (por el árbol de Shopify) y el resto del plan. Después, con su matiz sobre el entrenamiento a escala ([D-046](#d-046)), aprobó los ajustes de los casos y de la cobertura.
- **Decisión:**
  - **Rasgos:** el rasgo principal de un requisito es qué resuelve la cuestión, de una lista cerrada (identidad, contenido, medida que fija lo vendido, medida descriptiva, material, construcción, prestación, uso y compatibilidad, seguridad, cuidado, estética, certificación u origen), más la entidad, el origen, la aplicabilidad y la posición del bloque. Cada atributo de Shopify o propiedad de Amazon se etiqueta una sola vez y se reutiliza.
  - **Reglas de importancia por el árbol de Shopify:** la regla vive en la clase y sube a la categoría madre solo si vale para todas sus hijas (el principio de [D-043](#d-043), criterio 4). El crítico es global. Su prueba no depende de la clase: «sin la cuestión, ¿se sabe qué se vende, cuánto cuesta y si se puede adquirir?». A una clase sin regla no se le aplica la de otra rama: se usa la importancia que propone el agente, provisional y encolada. Las importancias de partida salen del catálogo y de los votos de los agentes con las pruebas de [D-035](#d-035); manda la regla compilada. El marco pone límites que ninguna regla puede saltarse: «ninguna regla puede hacer crítica la estética, ni tocar la capa general ni el criterio de las medidas».
  - **Métricas, sin umbrales:** cobertura (en el conjunto de control, cuestiones clave esperadas presentes; en el catálogo de entrenamiento, hechos declarados sin pregunta en el modelo); estabilidad (mismo resultado en dos ejecuciones: composición, bloques e importancia); coherencia (cuántos requisitos con los mismos rasgos tienen importancias distintas). Una regla se acepta si ninguna métrica empeora y al menos una mejora.
  - **Casos:** el conjunto de entrenamiento es un catálogo grande capturado con el motor de captura compartido ([D-046](#d-046)); los 14 casos actuales son el conjunto de control.
  - **Alcance de la primera versión:** solo se induce la importancia; para composición, especializaciones, relevancia de Amazon e inferidas se miden las divergencias y el informe las agrupa por patrón.
  - **I-19:** la clave del modelo lleva la versión de cada bloque; un bloque generado en ejecución lleva el estado «no compilado» hasta que el entrenamiento lo compila.
  - **Ejecución:** un comando de Claude Code (`/demand-model URL`) que lanza los agentes y llama al código determinista, para probar productos reales; el entrenamiento a escala, por lotes con la API (T-020).
- **Interpretaciones adoptadas:**
  - La opción C sustituye solo el ámbito global del punto 2 («lo único que no me encaja es que se mire a nivel global»); el resto del mecanismo explicado se mantiene: etiquetas, regla que sale de las importancias con la misma etiqueta, excepciones constantes como reglas específicas, votos, «manda la regla» y límites del marco.
  - Se incorpora a `10-model` como vigente, igual que D-044: es la operación aprobada para la primera versión; lo que no fija queda en OQ-48 y OQ-49.
  - «Vale para todas sus hijas» cuenta las hijas que tienen requisitos o votos de ese rasgo. Una regla sube cuando al menos dos hijas con datos la comparten y ninguna la contradice. Es un mínimo estructural, no un umbral de calidad: con una sola hija no se distingue la regla de la madre de la de la hija, y subir aplicaría a sus hermanas la regla de otra rama, que el artefacto excluye. Es la misma lectura que D-043, criterio 4, que trata de una propiedad «en varias categorías hermanas». Las hijas sin datos heredan la regla de la madre. Las reglas no suben por encima de las verticales de Shopify: una vertical sin datos no hereda reglas de otra.
  - En el ejemplo del artefacto, Cojines no es hija de Ropa de casa (cuelga de Decoración), así que su excepción no impide que la regla de la estética suba a Ropa de casa.
  - Dentro de una misma clase, la regla es la importancia mayoritaria de sus requisitos y votos («la regla sale de mirar qué importancia tienen hoy los requisitos con la misma etiqueta»). En un empate, Claude elige la más alta, por analogía con que la duda no baja la importancia ([D-035](#d-035)); es una elección propia, revisable en el marco.
  - La importancia de un requisito en un modelo se resuelve desde la clase del producto hacia arriba: la regla más específica del rasgo en la cadena de la categoría. En un juego, desde cada pieza a la que se aplica el bloque, y se toma la más alta.
  - «El crítico es global» y su prueba («¿se sabe qué se vende, cuánto cuesta y si se puede adquirir?»): solo pueden ser críticos los rasgos que dicen qué se vende (identidad, contenido, medida que fija lo vendido). La medida que fija lo vendido es siempre crítica y la medida descriptiva siempre principal (D-043, criterio 1). Para identidad y contenido, si son críticos lo decide una regla global; si no lo son, el árbol decide entre principal y complementario. Un voto crítico en otro rasgo cuenta como principal y el informe lo señala. El artefacto solo excluye expresamente la estética; la restricción a tres rasgos es lectura de Claude (el catálogo solo tiene críticos de esos rasgos) y tiene un riesgo: una cuestión de compatibilidad o de seguridad que fijara qué se vende no podría ser crítica. Se revisa en el marco si el informe lo muestra.
  - «Coherencia» se mide dentro de cada clase: requisitos con el mismo rasgo en la misma clase. Una excepción legítima de una clase (la estética de Cojines) no cuenta como incoherencia, porque la opción C la admite.
  - «No tocar la capa general»: sus importancias quedan fijas como parte del marco, y ninguna regla, general ni específica, las revisa por clase. Enmienda en este punto [D-034](#d-034) («revisables por clase con justificación») y la interpretación de D-044 sobre la revisión por clase, que queda para los bloques de categoría. La capa general no tiene estado de compilación: no es «no compilado» ni se encola.
  - «Compila al vuelo» un bloque generado en ejecución: se le aplican el índice de rasgos y las reglas vigentes; queda en estado «no compilado» («no revisada» en la cita de D-044) hasta que lo compila el entrenamiento. Si su rama no tiene regla, la importancia es el voto del agente, provisional.
  - **Quién decide cada cosa en la primera versión:** la importancia, las reglas compiladas (o el voto, sin regla); la composición, las especializaciones, las inferidas y la aplicación, el clasificador, con las especializaciones y las inferidas siempre provisionales; la relevancia de las propiedades de Amazon, la redacción automática del bloque cuando se genera. Las reglas de las demás decisiones quedan en OQ-49.
  - En el rasgo «certificación u origen», «origen» es el lugar de fabricación; no es el origen del requisito (referencias, inferida o normativa), que es otro rasgo.
  - Un requisito toma el rasgo de sus fuentes. Las cuestiones inferidas y las de especialización, sin fuente de referencia, se etiquetan en el propio requisito.
  - Los votos los emite el agente de cada caso para los requisitos de categoría, especialización e inferidos de su modelo, no para la capa general, que es fija. Se registran con la clase en que se emiten.
  - **Cobertura:** las cuestiones clave esperadas se miden en el conjunto de control; los hechos declarados sin pregunta, en todos los casos. Cuentan todos los hechos declarados menos lo estético y lo promocional (el artefacto) y los beneficios reclamados, que [D-025](#d-025) deja fuera de la clase.
  - **Informe agregado:** métricas frente a la versión anterior, reglas añadidas o retiradas con el número de requisitos que decide cada una, votos que contradicen el marco, lo usado sin compilar y las divergencias de las decisiones no inducidas agrupadas por patrón.
  - **Estados:** los estados del bloque de [D-038](#d-038) (propuesta o validado) pasan a ser no compilado o compilado. El catálogo actual está no compilado hasta la primera compilación.
  - **Versión en la clave:** cada bloque se escribe `<bloque>@<versión>`.
- **Consecuencias:**
  - módulos: [model-training](../10-model/model-training.md#operación-de-la-primera-versión) 1.1, [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.5 y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.7;
  - decisiones: D-034 enmendada (capa general fija), D-038 enmendada (estados y clave), D-040 y D-044 precisadas;
  - registros: OQ-47 cerrada, I-19 resuelta, I-17 y OQ-02 anotadas; nuevas OQ-48 (selección del catálogo de entrenamiento) y OQ-49 (inducción de las demás decisiones);
  - glosario: rasgo, voto, conjunto de control, regla inducida y catálogo compilado.
- **Relacionado:** D-025, D-034, D-035, D-038, D-040, D-043, D-044, D-046, I-17, I-19, OQ-02, OQ-47, OQ-48, OQ-49.

### D-046

**Motor de captura compartido por el MPIR y el entrenamiento del modelo de demanda.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-operation`, tareas T-019 y T-020. El motor de captura se construyó para la capa original del MPIR (T-013, [D-042](#d-042)). Al plantear el entrenamiento del modelo de demanda, el usuario fijó su alcance.
- **Decisión:**
  - Palabras del usuario: «El entrenamiento lo vamos a hacer con un catálogo de miles de productos de diferentes tipos. Deberá usar el motor de captura del MPIR, que está preparado para el scraping. Entonces el motor de captura ya no es algo exclusivo del MPIR. Es algo que nos permite capturar información de ecommerce de referencia. Tenemos un motor de captura compartido para el modelo de taxo y MPIR».
  - El catálogo de entrenamiento ([D-045](#d-045)) se captura con ese motor, sin Amazon.es.
  - El código se traslada a un módulo de captura común en una tarea aparte (T-020), porque otra sesión trabaja con el motor (T-014, T-015). En la documentación solo se declara que es compartido.
- **Interpretaciones adoptadas:**
  - «Modelo de taxo» es el modelo de demanda que construye `demand-engine` con la taxonomía.
  - Las políticas de acceso del motor ([D-042](#d-042): robots.txt y reservas de minería de textos y datos) se aplican igual a las capturas del entrenamiento, porque son del motor. Lo demás de D-042 sigue siendo propio de la capa original del MPIR.
  - La selección de tiendas y fichas queda abierta: [OQ-48](open-questions.md).
- **Consecuencias:** [model-training](../10-model/model-training.md#operación-de-la-primera-versión) 1.1; mapa del código en `CLAUDE.md` y en `demand-engine/README.md`; glosario (motor de captura); nueva OQ-48.
- **Relacionado:** D-042, D-045, OQ-11, OQ-12, OQ-48.

### D-047

**El modelo de demanda va con el producto; la aplicación, con la oferta.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-offer-application`, tarea T-019. [D-033](#d-033) y [D-038](#d-038) identificaban el modelo por sus bloques más la aplicación, y el nombre terminaba en la aplicación («— unidad no nueva, con descuento»). El usuario propuso tratar las promociones como requisitos siempre presentes y, al estudiarlo, sacar la aplicación de la denominación.
- **Decisión:**
  - Palabras del usuario: «Consideremos sacar la aplicación de la denominación. Ya que parecen ser cuestiones de estado temporal. Entonces las vinculamos a la oferta y no al producto. Modelo de demanda se vincula al producto, aplicación a la oferta».
  - **Modelo de demanda (producto):** bloques de categoría y especialización. Clave: sus bloques con versión. Nombre: «Categorías (alias) · especializaciones».
  - **Aplicación (oferta):** las condiciones activas de esa oferta. No entra en la clave ni en el nombre del modelo; se registra con la oferta. Una oferta sin condiciones activas es **estándar**: es un resultado comprobado, no una ausencia.
  - Lo que se audita es la oferta: el modelo de su producto más su aplicación. Los requisitos condicionados que no se dan en esa oferta quedan en gris, como NA justificado; la pregunta universal nunca es NA.
  - `gen.elementos-digitales` es del producto: entra en el modelo, como un bloque más de la clave («Televisores · con elementos digitales»). Las variantes son de la oferta.
- **Interpretaciones adoptadas:**
  - «Estado temporal» se lee como todo lo que depende de la oferta y no del producto: variantes ofrecidas, unidad no nueva, descuento, cantidad limitada, precio personalizado y suscripción o depósito. Los elementos digitales no son un estado de la oferta.
  - Lo que pone en gris un requisito condicionado es el hecho declarado, como en [D-037](#d-037). Si la ficha no declara la condición, sus requisitos son NA, el estado del canon que «se justifica y se separa de las unidades pertinentes». En el descuento, la duda de si lo hay se valora una sola vez, en la pregunta universal de promociones ([D-049](#d-049)). Las demás condiciones (precio personalizado, suscripción…) no tienen pregunta universal: sin hecho declarado, sus requisitos son NA.
  - **La capa general forma parte de todo modelo.** El artefacto dice que el detalle condicionado «está siempre en el modelo» y vive «en el modelo del producto». Por eso todo modelo incluye la capa general completa, universal y condicionada con su disparador. Lo que distingue un modelo son sus bloques de categoría y de especialización y los condicionados del producto; la aplicación es la lista de condiciones de la oferta que se dan, no un conjunto de bloques.
  - La clave empieza por la versión de la capa general (`gen@<versión>`), común a todos los modelos, para que un cambio del marco quede trazado; después van los bloques que distinguen el modelo, con su versión ([D-045](#d-045)).
  - En el nombre del modelo, un bloque de la capa general que sea del producto se nombra tras las especializaciones con su nombre breve («con elementos digitales»).
  - «Estándar» sustituye al «—» del estudio. Se descartan «por defecto», ya usado para la importancia, y «general», que choca con «capa general». Significa que el clasificador no encuentra ninguna condición declarada; no afirma los hechos (unidad nueva, precio sin rebaja…), y cuándo vale como «no» lo que la ficha calla lo fija la auditoría ([OQ-50](open-questions.md)).
- **Consecuencias:**
  - módulos: [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.6, [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.8 y [cases](../20-methods/product-taxonomy/cases.md) 1.6;
  - decisiones: D-033 y D-038 enmendadas en la identidad, la clave y el nombre; D-034 precisada (elementos digitales);
  - glosario: aplicación, ahora de la oferta, y oferta estándar.
- **Relacionado:** D-033, D-034, D-037, D-038, D-048, D-049.

### D-048

**La oferta no aporta requisitos: activa requisitos condicionados de la clase.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-offer-application`, tarea T-019. Con [D-047](#d-047), el usuario preguntó cómo se resuelve que la aplicación traiga requisitos que no podrían haberse inferido sin ella: la salud de la batería de un móvil reacondicionado, que [D-037](#d-037) dejaba como posible especialización de oferta.
- **Decisión:**
  - La oferta nunca aporta requisitos: solo activa requisitos condicionados que viven en el modelo del producto (capa general o bloques de la clase).
  - Una cuestión que solo procede con una condición de la oferta es un requisito condicionado del bloque de la clase (p. ej., en smartphones, la salud de la batería, aplicable si la unidad no es nueva). El producto nuevo y el reacondicionado comparten modelo; en la oferta estándar la pregunta está en gris.
  - Se descubre como cuestión inferida de la clase con esa aplicabilidad: provisional y encolada, hasta que el entrenamiento la incorpora al bloque como nueva versión.
  - Una condición de oferta que la capa general no tenga (p. ej., preventa o reserva) es un hueco del marco: el informe del entrenamiento la señala y no se inventa.
- **Interpretaciones adoptadas:**
  - Sustituye [D-027](#d-027): no hay especializaciones de oferta, y la condición 1 del criterio de especialización solo admite características del producto. El requisito condicionado es el de [D-024](#d-024).
  - Precisa D-037: la salud de la batería del reacondicionado, su ejemplo hipotético, pasa a ser un requisito condicionado de la clase. El otro ejemplo (repuestos y accesorios de bienes de fin de serie) no tiene disparador en la capa general (un fin de serie puede ser nuevo): sería un hueco del marco, según el último punto de la decisión.
  - La «clase de oferta» (BASE §4) se lee como las ofertas de una clase de producto, cada una evaluada con el modelo de su producto más su aplicación; no crea clases. Anota OQ-37.
  - El ejemplo de la batería es hipotético; ninguno de los 14 casos lo tiene.
- **Consecuencias:**
  - módulos: [study-class](../10-model/study-class.md#criterio-de-especialización) 1.3 (condición 1) y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas) 1.8;
  - registros: OQ-37 anotada;
  - glosario: especialización, especialización de oferta (retirada) y requisito condicionado.
- **Relacionado:** D-024, D-027, D-037, D-041, D-045, D-047.

### D-049

**Pregunta universal de promociones y descuentos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-offer-application`, tarea T-019. La capa general solo tenía la parte condicionada del descuento (`gen.descuento`). El usuario propuso tratar promociones y descuentos como requisitos siempre presentes, porque «responder que no hay promoción o descuento podría ser útil y esto podría aplicar a cualquier producto del mundo».
- **Decisión:** la capa general añade una cuestión universal sobre si la oferta tiene alguna promoción o descuento vigente y en qué consiste. Un «no» fundamentado la resuelve. Los detalles siguen en `gen.descuento`, condicionado a la oferta, y quedan en gris cuando no hay descuento ([D-047](#d-047)).
- **Interpretaciones adoptadas:**
  - Con D-047, la aplicación ya no forma parte de la identidad. De la propuesta queda la pregunta universal, como recomendó Claude («para las promociones basta añadir la pregunta universal «¿tiene promoción o descuento?», si se quiere que un «no» cuente»), aprobada con «todo aparece OK».
  - Redacción del borrador: «¿Tiene la oferta alguna promoción o descuento vigente (rebaja, cupón, regalo, unidades gratis…) y en qué consiste?». Importancia por defecto: complementaria, la del borrador. Es un valor de la capa general, que es marco ([D-045](#d-045)).
  - Las dos preguntas condicionadas del borrador (precio anterior y cuánto se rebaja; condiciones y vigencia) no se incorporan, siguiendo «los detalles siguen siendo condiciones de la oferta»: queda `gen.descuento/01`, que pregunta por el precio de referencia y las condiciones, pero no por la vigencia, y solo se activa con descuento, no con promociones sin rebaja (regalo, unidades gratis). Ese hueco queda en OQ-50.
  - Cuándo vale derivar el «no» de una ficha que no lo dice (precio sin tachar ni etiqueta) es una regla de la auditoría: [OQ-50](open-questions.md).
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.8 (fila nueva en la capa general); `demand-engine/catalog/gen.json` (`gen/16`, capa general en la versión 0.2); nueva OQ-50.
- **Relacionado:** D-034, D-037, D-045, D-047.

### D-050

**Filtro de relevancia aprendido: lo no relevante sale del modelo de la clase.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-relevance-origin`. En la pasada de control, el modelo del pienso incluía el color, el estampado y el material, heredados de los bloques de sector de Productos para mascotas y Productos para perros ([D-040](#d-040)), y los agentes los votaron «complementario» porque no tenían otra opción. El usuario: «Nuestro modelo solo debe incluir cuestiones relevantes, las complementarias siendo las de menor relevancia».
- **Decisión** (opción A de Claude, aprobada con «OK»):
  - Antes de la importancia, cada requisito pasa una prueba de relevancia: «¿informa sobre algo que importa para evaluar o comparar ofertas de esta clase?». Si no la pasa, sale del modelo de esa clase. No es un cuarto nivel de importancia: la escala sigue siendo crítico, principal y complementario.
  - Lo decide el entrenamiento: los agentes votan con un cuarto valor, «no relevante», y se inducen reglas de relevancia por requisito y clase a lo largo del árbol de Shopify, con el mismo mecanismo que la importancia ([D-045](#d-045)).
  - Sin regla compilada, la duda no excluye: un requisito votado «no relevante» se queda en el modelo, marcado como provisional («relevancia dudosa»), y se encola.
  - Nunca se excluyen la capa general, los requisitos normativos ni la medida que fija lo vendido.
  - Lo excluido se lista aparte con su regla. No es NA: no forma parte de lo que se audita.
  - La validación añade la coherencia de relevancia y una salvaguarda de cobertura: una exclusión que deja sin pregunta un hecho que declaran las fichas de la clase empeora la cobertura, y la regla se descarta.
- **Interpretaciones adoptadas:**
  - Los datos de partida son el catálogo (un requisito incluido en un bloque es relevante en su categoría) y los votos, registrados en la clase del producto. La regla es la mayoría en la clase; en empate, relevante. Sube a la madre con el mínimo estructural de D-045 (al menos dos hijas con datos, sin ninguna en contra) y no por encima de las verticales.
  - Se amplía el alcance de la primera versión de D-045: además de la importancia, se induce la relevancia. Las demás decisiones siguen en [OQ-49](open-questions.md).
  - «Se queda como complementario» (artefacto) se aplica cuando el requisito no tiene regla de importancia. Si la tiene, conserva su nivel: manda la regla compilada (D-045), y la duda no baja la importancia ([D-035](#d-035)).
  - La prueba es la de la condición 3 del criterio de especialización: cuestiones «relevantes para evaluar la clase, no para un comprador concreto» ([D-022](#d-022)). Se descartan la opción B (decidirlo solo al redactar el bloque, que no resuelve los bloques de sector) y la C (resolverlo en la auditoría con NA, que mezcla «no aplica» con «no importa»).
  - El filtro va antes de la importancia. El marco fija la importancia de lo relevante, no su relevancia: una medida descriptiva o una identidad pueden excluirse en una clase si sus votos lo dicen. Solo protegen de la exclusión la capa general, lo normativo y la medida que fija lo vendido.
  - En un modelo de varias piezas, un requisito solo se excluye si lo excluyen todas las clases a las que se aplica. El dato del catálogo cuenta como un voto «relevante» en la categoría del bloque.
  - Con la relevancia de las propiedades de Amazon ([D-039](#d-039)) se distinguen dos decisiones: incluir la propiedad en el bloque (la redacción del bloque) y excluirla en una clase concreta (este filtro). La salvaguarda de cobertura evita en parte el hueco de [I-17](issues.md#i-17).
  - Hay tres casos distintos: «no relevante para la clase» (este filtro); «no aplica al producto», como el número de hilos en unas sábanas de coralina, que es un requisito condicionado a un hecho del producto ([D-024](#d-024)) y queda en gris en la auditoría; y «no aplica a la oferta» ([D-047](#d-047)).
  - En la pasada de control no había votos «no relevante» (el valor no existía): las primeras reglas de relevancia saldrán de las próximas ejecuciones.
- **Consecuencias:**
  - módulos: [model-training](../10-model/model-training.md#relevancia) 1.2, [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.7 y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.9;
  - registros: I-17 anotada y retitulada, OQ-49 anotada;
  - glosario: filtro de relevancia;
  - motor: votos de relevancia, reglas `rel:` y lista de excluidos.
- **Relacionado:** D-022, D-024, D-035, D-039, D-040, D-045, D-047, I-17, OQ-49.

### D-051

**Peso, grosor y gramaje: rasgo «magnitud física», fuera de la regla de las medidas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-relevance-origin`. La regla del marco «la medida descriptiva es principal» ([D-043](#d-043), criterio 1) tuvo 27 votos en contra en la pasada de control con las reglas 1 (informe `demand-engine/training/reports/2026-10-25-v2-report.md` de entonces). Claude explicó en la conversación que el criterio habla de «la medida o la talla», con dimensiones y tallas como ejemplos, y que el peso, el grosor y el gramaje habían entrado en «medida descriptiva» por la definición del vocabulario que él redactó. Los votos sobre esas tres magnitudes dependen de la clase: el gramaje es principal en toallas y en la manta polar, y complementario en fundas nórdicas y en el protector.
- **Decisión** (opción A, «2. Confirmo»): el peso, el grosor y el gramaje salen de «medida descriptiva» y pasan a un rasgo propio, **magnitud física**, sin regla fija: su importancia la decide el árbol por clase. D-043, criterio 1, se aplica a las dimensiones y las tallas.
- **Interpretaciones adoptadas:**
  - El vocabulario cerrado de D-045 pasa a tener 13 rasgos.
  - Las dimensiones de detalle (altura de tacón, medidas de uso del sofá, largo reclinado) siguen bajo D-043, criterio 1, hasta tener datos del entrenamiento a escala: [OQ-51](open-questions.md).
  - Una pregunta que mezcla una dimensión con un peso se etiqueta por su parte dominante.
- **Consecuencias:** [model-training](../10-model/model-training.md#rasgos) 1.2; glosario (rasgo); catálogo reetiquetado y recompilado; nueva OQ-51.
- **Relacionado:** D-043, D-045, OQ-51.

### D-052

**Fabricante, país de fabricación y seguridad en la capa general, según su origen.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-relevance-origin`. Seguían pendientes dos propuestas de Claude para la capa general. La primera, el país de fabricación, era casi el único hecho declarado sin pregunta en la pasada de control. La segunda era el art. 19 del Reglamento (UE) 2023/988 de seguridad general de los productos (GPSR), comprobado antes en la sesión: fabricante y contacto, persona responsable en la UE, identificación del producto, y advertencias e información de seguridad. El usuario respondió: «Según su origen. Si es claramente por normativa, lo ponemos en normativa».
- **Decisión:**
  - Lo que exige el art. 19 del GPSR entra en la capa general con origen «normativa»:
    - la marca, el modelo y los identificadores (gen/02 y gen/03) pasan de «inferida» a «normativa» (art. 19.a y 19.c);
    - nuevas cuestiones: fabricante y contacto (19.a), complementaria; persona responsable en la UE si el fabricante no está establecido en ella (19.b), complementaria y condicionada; advertencias e información de seguridad (19.d), principal.
  - El país de fabricación entra como cuestión universal, complementaria, con origen «referencias»: no hay una obligación legal general comprobada, y lo recoge una referencia común a todos los tipos de producto.
- **Interpretaciones adoptadas:**
  - «Según su origen» se lee como el campo de origen de cada requisito: «normativa» solo si una norma lo exige con claridad; si no, la fuente que lo apoya. Las importancias son las de las propuestas de Claude, que el usuario no objetó. La capa general es marco ([D-045](#d-045)).
  - Se descarta otra lectura: que lo no normativo entre por el camino de su fuente, es decir, `country_of_origin` en los bloques de categoría ([D-039](#d-039), [D-040](#d-040)). La propiedad está en los 1.877 PTD de Amazon (`amazon-ptd@2026-10-24`; etiqueta «País de origen», y «País de publicación» en 33 PTD de mascotas). Ir por los bloques la repetiría en todos ellos, con la inestabilidad que ya se vio: los agentes la pusieron como inferida en tres bloques distintos. Una cuestión de cualquier producto va en la capa general. Esto amplía D-039, que solo admitía los PTD como fuente de la categoría. El apoyo es la presencia de la propiedad en el PTD, no su obligatoriedad, que es un requisito de la plataforma.
  - El GPSR no se aplica a alimentos ni piensos, entre otras exclusiones (art. 2.3). Las cuestiones del fabricante y de las advertencias siguen siendo universales: tienen sentido en cualquier producto, y un «no» o los datos del operador las resuelven. Su origen es normativo por el GPSR, y fuera de su ámbito su apoyo normativo está por comprobar ([OQ-45](open-questions.md)). Lo mismo vale para la marca, el modelo y los identificadores.
  - La persona responsable en la UE es un requisito condicionado a un hecho del producto (el fabricante no está establecido en la UE) dentro del bloque universal, como los requisitos condicionados de los bloques de categoría ([D-024](#d-024)). Lo evalúa la auditoría y no distingue el modelo. Precisa [D-034](#d-034) y [D-047](#d-047): un bloque universal puede llevar requisitos condicionados a un hecho del producto; sus demás cuestiones se aplican siempre.
  - La «imagen» que pide el art. 19.c no es una cuestión nueva: es un medio de responder qué es el producto (gen/01) y su identificación.
  - La capa general pasa a la versión 0.3.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.9; [demand-model](../10-model/demand-model.md#capa-general) 2.7; `demand-engine/catalog/gen.json`; OQ-45 anotada.
- **Relacionado:** D-024, D-034, D-038, D-039, D-040, D-045, D-047, D-049, OQ-45.
