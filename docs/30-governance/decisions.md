---
id: decisions
title: Registro de decisiones
layer: governance
status: vigente
version: 1.0
updated: 2026-10-24
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
| [D-009](#d-009) | Dos vías de construcción del modelo de demanda: taxonomía y MPIR | aceptada | 2026-10-24 |
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
