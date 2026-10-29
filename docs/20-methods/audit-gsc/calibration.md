---
id: audit-gsc-calibration
title: Casos de aplicación, calibración y prueba de aceptación V1
layer: method
status: propuesta
version: 0.5
updated: 2026-10-30
sources: [GSC0 §15, GSC0 §17, FUND §10, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Casos de aplicación, calibración y prueba de aceptación V1

Los casos son **hipotéticos y metodológicos**. Ilustran pruebas y límites de decisión; **no constituyen auditorías reales ni validan por sí mismos los anclajes**. En una ejecución, las evidencias deben sustituirse por fragmentos y localizadores verdaderamente obtenidos. Los casos A, B y C se basan en los ejemplos vigentes de FUND §10.1–10.3 y los fragmentos que proceden de FUND se marcan como vigentes. En el caso A, FUND §10.1 da valores ilustrativos firmes; GSC0 los formula como orientaciones condicionales, que son las que se recogen aquí.

## Caso A — información general para una cuestión por variante

**RI:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?» · **Ámbito:** Contenido.
**Recurso:** ficha de un modelo de calzado; tallas 41, 42 y 43 identificadas; afirmación «Disponible para compra online» en la cabecera del modelo; inspección suficiente sin estados individualizados ni regla que atribuya el estado a cada talla; sin contraste con inventario; el RI no demanda comparación.

**Localización:** listado de tallas = pertinente auxiliar/identificador; afirmación general = pertinente sustantiva parcial. **Disponibilidad efectiva: 1.**

**Hallazgo:** hay información general de disponibilidad, pero no se justifica su extensión a cada variante.

| AC | Orientación ilustrativa | Fundamento que debe comprobarse |
|---|---|---|
| Concreción | **1** | Cobertura sustantiva general, sin el desglose o regla requeridos por variante. |
| Precisión | **2**, si el significado comercial es inequívoco | No confundir significado con atribución. |
| Aplicabilidad | **1**, si hay atribución válida al modelo y no a cada talla | La afirmación tiene alcance parcial respecto del RI. |
| Comparabilidad | **NA**, si la marca de dimensión de comparación del requisito dice que la disponibilidad por variante no es dimensión de comparación ([D-126](../../30-governance/decisions.md#d-126)) | No imponer comparación artificial. |
| Fiabilidad | **2**, si supera las comprobaciones de estructura del dato y de consistencia dentro del ámbito; NE solo si una comprobación no pudo hacerse | Sin corroboración no es falsedad ni NE: lectura refutadora ([D-121](../../30-governance/decisions.md#d-121)). |
| Justificación | **1**, si la afirmación general fundamenta solo parte del alcance | No permite reconstruir estado por talla. |

Propiedades implicadas: P06, P07, P11, P12; las de fiabilidad y fundamentación para el contraste del estado.

> **Estado: vigente** (FUND §10.1; Fiabilidad enmendada por [D-121](../../30-governance/decisions.md#d-121)).

**Diagnóstico:** la ficha no permite determinar y fundamentar suficientemente la disponibilidad de la talla 42. La limitación de atribución no es una insuficiencia de disponibilidad efectiva, no demuestra que el inventario sea falso ni refleja una carencia de acceso o lectura. El IR no se calcula: las reglas de síntesis no están definidas. Los valores son **hipótesis de calibración**, no una regla automática para fichas semejantes.

## Caso B — relación legítima y respuesta derivada

**RI:** disponibilidad de cada variante · **Ámbito:** Contenido.
Contenido admisible: tallas 41, 42 y 43; `Talla 42 ↔ SKU-420`; `SKU-420 ↔ InStock`; mismo modelo y oferta; canal y momento compatibles.

La ruta `talla → SKU → estado` es **pertinente y puede fundamentar** «la talla 42 está en stock» sin aparecer literalmente en una sola frase. Sirve para reconstruir la evidencia, **no para penalizar el número de pasos**. **No extrapolar** a tallas 41 y 43: la Concreción del RI completo depende de lo que se encuentre sobre esas unidades.

> **Estado: vigente** (FUND §10.3): este párrafo y el siguiente.

Por contraste, «producto muy vendido», «fabricación de 10.000 unidades mensuales» o «envío gratuito» no bastan por sí solos para establecer la disponibilidad de una talla; una promesa de reposición sin entidad y periodo identificados puede requerir comprobación adicional antes de decidir su función pertinente.

Análogamente, ante «¿Cuál es el precio final tras el descuento anunciado?», precio base, porcentaje de descuento y condiciones inequívocas pueden permitir una derivación aritmética válida sin que el total figure literalmente. Si faltan las condiciones de aplicación, la carencia se analiza en los AC pertinentes.

**Evidencias exigidas:** correspondencia talla–identificador, estado–identificador, identidad y contexto comercial comparables, recurso/representación y captura.

## Caso C — ausencia de información pertinente bajo el perfil

**RI:** disponibilidad por variante · **Ámbito:** Contenido; perfil sin interacción ni ejecución del mecanismo concreto que incorpora el contenido (JavaScript).
El HTML obtenido contiene únicamente un contenedor vacío; tras inspección adecuada no hay elementos pertinentes recuperables en las representaciones admitidas.

**Disponibilidad efectiva = 0 → IR = 0 → AC no valorados.**

**Evidencia negativa necesaria:** perfil, recurso recuperado, representación original, zona inspeccionada, posibles fuentes admitidas revisadas y condición que impide obtener/leer contenido pertinente. El problema no es la mera presencia de JavaScript, sino que, **bajo el perfil concreto de obtención y lectura**, no se accede a contenido pertinente; la conformidad del mecanismo se analiza en los requisitos técnicos aplicables.

## Caso D — búsqueda insuficiente

La herramienta recupera solo una porción del recurso; no se sabe si el resto contiene información pertinente y no puede completarse la inspección.

**Resultado:** disponibilidad **inconclusa**, no 0. Registrar qué se obtuvo, qué falló, qué revisión adicional sería necesaria y qué decisiones quedan suspendidas. Este estado describe el **procedimiento**, no un tercer grado de disponibilidad efectiva.

## Caso E — Precisión frente a Aplicabilidad

**RI:** ¿qué variantes están disponibles? Afirmación «Disponible» en una cabecera; sin correspondencia por variante.

El término puede tener **significado comercial claro** y faltar **atribución** a la entidad requerida. La limitación principal corresponde a Aplicabilidad, y la cobertura por variante puede afectar Concreción; no degradar Precisión por duplicación automática.

## Caso F — información directa

**RI:** «¿Cuál es el material principal de la funda?» Afirmación: «Composición principal: 100 % algodón», atribuida inequívocamente a la funda, sin condiciones omitidas.

Puede satisfacer **Concreción**, **Precisión**, **Aplicabilidad** y aportar base **identificable** para **Justificación** sin cadenas de inferencia ni referencias externas innecesarias. **Fiabilidad** requiere su propio análisis; no se deduce del resto.

## Caso G — comparación que requiere equivalencia

**RI:** «¿Cuál de dos ofertas tiene menor precio por kilogramo?» Oferta A: 750 g por 6 €; oferta B: 1 kg por 7 €. Bajo condiciones de precio comparables y sin costes ni condiciones relevantes omitidos, una conversión aritmética fundamentada permite el contraste.

Las distintas unidades de masa **no son por sí solas** deficiencia de Comparabilidad si la equivalencia es justificable. Si un precio incluye condiciones distintas no aclaradas, examinar los límites de contexto y aplicabilidad.

## Caso H — Contenido y Marcado discordantes

**RI:** precio de una oferta. En una instantánea comparable, el contenido dice «79 €» y el marcado «89 €» para la misma oferta, moneda, condiciones y momento.

- **Contenido:** evaluar «79 €» con lo que da el filtro Alfa, sin el marcado.
- **Marcado:** evaluar «89 €» y su soporte aisladamente; el contenido no completa el contenido resolutivo del marcado.
- **Prueba necesaria:** identidad, moneda, oferta, canal, fecha y condiciones. Si la divergencia se explica por momentos u ofertas distintos, no declarar incoherencia material.
- **Transversal:** registrar la discrepancia como hallazgo de [consistencia transversal](../../10-model/evaluation-scopes.md#consistencia-transversal) Contenido ↔ Marcado. No modifica ningún GSC ([D-124](../../30-governance/decisions.md#d-124)). El contraste ya no es consistencia dentro de un ámbito: ningún ámbito ve los dos precios.

> **Estado: vigente** (FUND §10.4; enmendado por [D-220](../../30-governance/decisions.md#d-220): el contraste entre el contenido y el marcado solo es hallazgo transversal).

Regla general: una limitación en Marcado no implica una limitación en Contenido, ni al revés. Los resultados se documentan por separado, conservando procedencia y discrepancias.

## Caso I — popularidad y pertinencia

**RI:** disponibilidad de talla 42. Contenido: «superventas» y «producción de 10.000 unidades mensuales». Tienen asociación comercial pero **no función informativa justificada** para el estado actual de la talla, salvo relaciones concretas adicionales publicadas. No seleccionarlas ni inferir stock desde ellas.

## Caso J — Fiabilidad sin corroboración

**RI:** disponibilidad comercial actual. Afirmación inequívoca «En stock», sin poder corroborarla ni refutarla tras comprobaciones adecuadas.

**No asignar Fiabilidad 0 por falta de corroboración, ni NE.** Con la lectura refutadora, el grado sale de las comprobaciones superadas: estructura del dato y consistencia dentro del ámbito (p. ej., el estado visible coincide con el marcado). Sin defectos detectados, **2**, con el registro de lo comprobado y sin afirmar que el stock sea exacto. NE solo si una comprobación no pudo hacerse ([D-117](../../30-governance/decisions.md#d-117), [D-121](../../30-governance/decisions.md#d-121)). La respuesta puede seguir siendo clara, atribuible y reconstruible en otros AC.

## Caso K — característica ausente

**RI:** «¿Incluye el producto una batería recargable?» Contenido: «No incluye batería recargable», atribuido claramente al producto. La respuesta negativa **resuelve informativamente** la cuestión si está suficientemente determinada y fundamentada; no degradar Concreción o Justificación porque la característica no esté presente.

## Caso L — ausencia acreditada frente a no comprobada

**RI:** disponibilidad por cada variante. Ficha con diez variantes; estado encontrado en ocho. Comprobar qué variantes integran el conjunto, si hay relación por otros identificadores, afirmaciones generales legítimamente aplicables y qué representaciones se examinaron. Acreditadas las ausencias, documentar su efecto sobre Concreción y Aplicabilidad. **No calcular GSC a partir de 8/10 automáticamente**: la materialidad y la naturaleza de la condición deben justificarse según el RI.

## Matriz mínima de calibración

| Dimensión de prueba | Caso representativo | Error que se pretende detectar |
|---|---|---|
| Pertinencia directa | Afirmación que expresa el hecho solicitado. | Omitir información clara. |
| Pertinencia auxiliar | Identificador y relación de variante. | Excluir piezas que no son la respuesta literal. |
| Solo relación temática | Popularidad frente a stock. | Sobreinclusión del LLM auditor. |
| Derivación válida | SKU–estado, precio calculable. | Penalizar inferencias justificadas. |
| Prueba de derivación | Atributo frente a prestación; regla normativa; hecho particular tomado de fuera. | Admitir tendencias o completar con la ley o con datos externos. |
| Conocimiento del modelo | Dato que contradice lo que el auditor sabe del producto concreto, sin regla general. | Refutar con memoria del modelo en vez de anotar una sospecha ([D-154](../../30-governance/decisions.md#d-154)). |
| Contexto insuficiente | Estado sin canal/variante. | Completar condiciones con conjeturas. |
| Disponibilidad 0 | Ausencia comprobada con cobertura. | Valorar AC cuando no procede; falsos 0 de la fase 1 ([D-153](../../30-governance/decisions.md#d-153)). |
| Disponibilidad inconclusa | Lectura/inspección insuficiente. | Falsa ausencia. |
| AC 0/1/2 | Casos negativos, parciales y suficientes por AC. | Fronteras ambiguas de los anclajes. |
| NE y NA | Comprobación que no pudo hacerse; requisito marcado como no dimensión de comparación (NA). | Usar NE por falta de corroboración. |
| Coherencia | Valores distintos con o sin contexto comparable. | Confundir diferencia e incoherencia. |
| Ámbitos | Contenido vs Marcado vs catálogo. | Completar un ámbito con contenido de otro. |
| Consistencia transversal | Feed frente a web en un momento comparable. | Rebajar el GSC de un ámbito por una discrepancia entre ámbitos. |
| Informe | Hallazgo reconstruible con evidencia. | Puntuación opaca o evidencia ornamental. |

Los resultados esperados deben **acordarse por revisión metodológica** antes de usarse como referencia de validación de la Skill. No se define todavía un porcentaje de acuerdo que garantice fiabilidad universal.

## Prueba de aceptación de la V1

**Ejecutabilidad.** La V1 es operativamente ejecutable para pilotaje si, dado un RI y una representación admisible, un agente puede completar **sin inventar decisiones estructurales**: (1) interpretación y validación del perfil de RI; (2) exploración, detección de candidatos y selección por pertinencia; (3) disponibilidad efectiva con cobertura demostrable; (4) captura de evidencias con contexto, procedencia y momento; (5) comprobación de propiedades y hallazgos diferenciados; (6) anclajes por AC → 0/1/2, o NE si una comprobación no pudo hacerse; (7) revisión de consistencia y salida reexaminable. **No emitir un juicio cuando la evidencia no lo permite** es una capacidad necesaria, no un fallo.

**Condiciones mínimas del piloto:**

- RI de **naturalezas distintas** (atributo simple, atribución por variante, composición/derivación, contraste y condición comercial) y al menos un ámbito bien delimitado.
- Casos **suficientes, parciales, negativos, NE por incidencia, disponibilidad 0 e inspección inconclusa**.
- Representaciones/instantáneas comparables para que varios auditores apliquen las mismas reglas.
- Revisión de omisiones de localización, sobreinclusión temática, atribuciones indebidas, pruebas negativas, calidad de evidencia y diferencias GSC.
- Ajuste de anclajes y ejemplos antes de adoptar el procedimiento como estándar estable.

**Alcance intencionalmente limitado:** la V1 ejecuta la valoración AC/GSC y la regla **disponibilidad 0 → IR 0**. No exige cerrar coeficientes por importancia relativa, reglas de impacto/indispensabilidad para IR, fórmulas de ICI, métricas comerciales ni la auditoría técnica. Criterio de revisión humana: ver [dossier.md](dossier.md#criterio-de-revisión-humana).

## Relacionado

- [qa.md](qa.md) — auditoría de decisiones y desacuerdos.
- [ac-guides.md](ac-guides.md) — anclajes que se calibran.
