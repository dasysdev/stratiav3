---
id: audit-gsc-calibration
title: Casos de aplicación, calibración y prueba de aceptación V1
layer: method
status: propuesta
version: 0.1
updated: 2026-10-24
sources: [GSC0 §15, GSC0 §17, FUND §10]
---

# Casos de aplicación, calibración y prueba de aceptación V1

Los casos son **hipotéticos y metodológicos**. Ilustran pruebas y límites de decisión; **no constituyen auditorías reales ni validan por sí mismos los anclajes**. En una ejecución, las evidencias deben sustituirse por fragmentos y localizadores verdaderamente obtenidos. Los casos A, B y C se basan en los ejemplos vigentes de FUND §10.1–10.3 y los fragmentos que proceden de FUND se marcan como vigentes. En el caso A, FUND §10.1 da valores ilustrativos firmes; GSC0 los formula como orientaciones condicionales, que son las que se recogen aquí.

## Caso A — información general para una cuestión por variante

**RI:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?» · **Ámbito:** Web.
**Recurso:** ficha de un modelo de calzado; tallas 41, 42 y 43 identificadas; afirmación «Disponible para compra online» en la cabecera del modelo; inspección suficiente sin estados individualizados ni regla que atribuya el estado a cada talla; sin contraste suficiente con inventario o referencias de vigencia; el RI no demanda comparación.

**Localización:** listado de tallas = pertinente auxiliar/identificador; afirmación general = pertinente sustantiva parcial. **Disponibilidad efectiva: 1.**

**Hallazgo:** hay información general de disponibilidad, pero no se justifica su extensión a cada variante.

| AC | Orientación ilustrativa | Fundamento que debe comprobarse |
|---|---|---|
| Concreción | **1** | Cobertura sustantiva general, sin el desglose o regla requeridos por variante. |
| Precisión | **2**, si el significado comercial es inequívoco | No confundir significado con atribución. |
| Aplicabilidad | **1**, si hay atribución válida al modelo y no a cada talla | La afirmación tiene alcance parcial respecto del RI. |
| Comparabilidad | **NA**, si no se requiere contraste | No imponer comparación artificial. |
| Fiabilidad | **NE**, si no es posible sustentar un juicio sobre corrección/vigencia | Ausencia de comprobación no prueba falsedad. |
| Justificación | **1**, si la afirmación general fundamenta solo parte del alcance | No permite reconstruir estado por talla. |

Propiedades implicadas: P06, P07, P11, P12; las de fiabilidad y fundamentación para el contraste del estado.

> **Estado: vigente** (FUND §10.1).

**Diagnóstico:** la ficha no permite determinar y fundamentar suficientemente la disponibilidad de la talla 42. La limitación de atribución no es una insuficiencia de disponibilidad efectiva, no demuestra que el inventario sea falso ni refleja una carencia de acceso o lectura. El IR no se calcula: las reglas de síntesis no están definidas. Los valores son **hipótesis de calibración**, no una regla automática para fichas semejantes.

## Caso B — relación legítima y respuesta derivada

**RI:** disponibilidad de cada variante · **Ámbito:** Web.
Contenido admisible: tallas 41, 42 y 43; `Talla 42 ↔ SKU-420`; `SKU-420 ↔ InStock`; mismo modelo y oferta; canal y momento compatibles.

La ruta `talla → SKU → estado` es **pertinente y puede fundamentar** «la talla 42 está en stock» sin aparecer literalmente en una sola frase. Sirve para reconstruir la evidencia, **no para penalizar el número de pasos**. **No extrapolar** a tallas 41 y 43: la Concreción del RI completo depende de lo que se encuentre sobre esas unidades.

> **Estado: vigente** (FUND §10.3): este párrafo y el siguiente.

Por contraste, «producto muy vendido», «fabricación de 10.000 unidades mensuales» o «envío gratuito» no bastan por sí solos para establecer la disponibilidad de una talla; una promesa de reposición sin entidad y periodo identificados puede requerir comprobación adicional antes de decidir su función pertinente.

Análogamente, ante «¿Cuál es el precio final tras el descuento anunciado?», precio base, porcentaje de descuento y condiciones inequívocas pueden permitir una derivación aritmética válida sin que el total figure literalmente. Si faltan las condiciones de aplicación, la carencia se analiza en los AC pertinentes.

**Evidencias exigidas:** correspondencia talla–identificador, estado–identificador, identidad y contexto comercial comparables, recurso/representación y captura.

## Caso C — ausencia de información pertinente bajo el perfil

**RI:** disponibilidad por variante · **Ámbito:** Web; perfil sin interacción ni ejecución del mecanismo concreto que incorpora el contenido (JavaScript).
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

## Caso H — HTML y Schema.org discordantes

**RI:** precio de una oferta. En una instantánea comparable, HTML «79 €» y Schema.org «89 €» para la misma oferta, moneda, condiciones y momento.

- **Web:** comparar ambas afirmaciones; si son realmente comparables, registrar la discrepancia y analizar P16/Fiabilidad y demás consecuencias, sin elegir arbitrariamente una como verdadera.
- **Web Schema.org:** evaluar el valor y soporte del marcado aisladamente; el contraste con HTML sirve como **evidencia diagnóstica de coherencia de Web**, no completa el contenido resolutivo del ámbito Schema.org.
- **Prueba necesaria:** identidad, moneda, oferta, canal, fecha y condiciones. Si la divergencia se explica por momentos u ofertas distintos, no declarar incoherencia material.

> **Estado: vigente** (FUND §10.4).

Regla general: una limitación en Web Schema.org no implica necesariamente una limitación equivalente en Web, porque el HTML puede aportar información complementaria. Los resultados se documentan por separado, conservando procedencia y discrepancias.

## Caso I — popularidad y pertinencia

**RI:** disponibilidad de talla 42. Contenido: «superventas» y «producción de 10.000 unidades mensuales». Tienen asociación comercial pero **no función informativa justificada** para el estado actual de la talla, salvo relaciones concretas adicionales publicadas. No seleccionarlas ni inferir stock desde ellas.

## Caso J — Fiabilidad con verificación no concluyente

**RI:** disponibilidad comercial actual. Afirmación inequívoca «En stock», sin poder corroborar su vigencia ni establecer su falsedad tras comprobaciones adecuadas.

**No asignar Fiabilidad 0 por falta de corroboración.** Distinguir qué aspecto puede juzgarse, si hay soporte parcial materialmente suficiente para GSC 1 o si el juicio **debe quedar NE**. Documentar la metodología y los límites del contraste. La respuesta puede seguir siendo clara, atribuible y reconstruible en otros AC.

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
| Contexto insuficiente | Estado sin canal/variante. | Completar condiciones con conjeturas. |
| Disponibilidad 0 | Ausencia comprobada con cobertura. | Valorar AC cuando no procede. |
| Disponibilidad inconclusa | Lectura/inspección insuficiente. | Falsa ausencia. |
| AC 0/1/2 | Casos negativos, parciales y suficientes por AC. | Fronteras ambiguas de los anclajes. |
| NA/NE | Comparabilidad no pertinente y fiabilidad no evaluable. | Uso incorrecto de estados. |
| Coherencia | Valores distintos con o sin contexto comparable. | Confundir diferencia e incoherencia. |
| Ámbitos | Web vs Web Schema.org vs catálogo. | Completar un ámbito con contenido de otro. |
| Informe | Hallazgo reconstruible con evidencia. | Puntuación opaca o evidencia ornamental. |

Los resultados esperados deben **acordarse por revisión metodológica** antes de usarse como referencia de validación de la Skill. No se define todavía un porcentaje de acuerdo que garantice fiabilidad universal.

## Prueba de aceptación de la V1

**Ejecutabilidad.** La V1 es operativamente ejecutable para pilotaje si, dado un RI y una representación admisible, un agente puede completar **sin inventar decisiones estructurales**: (1) interpretación y validación del perfil de RI; (2) exploración, detección de candidatos y selección por pertinencia; (3) disponibilidad efectiva con cobertura demostrable; (4) captura de evidencias con contexto, procedencia y momento; (5) comprobación de propiedades y hallazgos diferenciados; (6) anclajes por AC → 0/1/2 o NA/NE; (7) revisión de consistencia y salida reexaminable. **No emitir un juicio cuando la evidencia no lo permite** es una capacidad necesaria, no un fallo.

**Condiciones mínimas del piloto:**

- RI de **naturalezas distintas** (atributo simple, atribución por variante, composición/derivación, contraste y condición comercial) y al menos un ámbito bien delimitado.
- Casos **suficientes, parciales, negativos, NA, NE, disponibilidad 0 e inspección inconclusa**.
- Representaciones/instantáneas comparables para que varios auditores apliquen las mismas reglas.
- Revisión de omisiones de localización, sobreinclusión temática, atribuciones indebidas, pruebas negativas, calidad de evidencia y diferencias GSC.
- Ajuste de anclajes y ejemplos antes de adoptar el procedimiento como estándar estable.

**Alcance intencionalmente limitado:** la V1 ejecuta la valoración AC/GSC y la regla **disponibilidad 0 → IR 0**. No exige cerrar coeficientes por importancia relativa, reglas de impacto/indispensabilidad para IR, fórmulas de ICI, métricas comerciales ni la auditoría técnica. Criterio de revisión humana: ver [dossier.md](dossier.md#criterio-de-revisión-humana).

## Relacionado

- [qa.md](qa.md) — auditoría de decisiones y desacuerdos.
- [ac-guides.md](ac-guides.md) — anclajes que se calibran.
