---
id: audit-gsc-evidence
title: Protocolo transversal de evidencias
layer: method
status: propuesta
version: 0.5
updated: 2026-10-30
sources: [GSC0 §9, GSC0 §14.3, FUND §9.4, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Protocolo transversal de evidencias

## Principio

> **Estado: vigente** (FUND §9.4).

Toda valoración ha de resultar de **comprobaciones identificables y evidencias suficientes, contextualizadas y reexaminables** para reconstruir el camino desde el recurso publicado hasta el juicio. El orden lógico es **contenido o resultado observado → evidencia → interpretación → hallazgo → propiedad afectada → efecto sobre el AC → GSC**; el resultado no puede ser una afirmación libre sin soporte. *(GSC0 §9.1:)* La evidencia no es una explicación inventada a posteriori.

Las evidencias pueden acreditar **presencia y contenido; identidad y atribución; relaciones y derivaciones; condiciones y contexto; coherencia y contraste; procedencia o verificabilidad; ausencia y cobertura; y limitaciones de obtención o evaluación**. Una pieza puede servir a varios hallazgos sin duplicarse artificialmente.

La base sustantiva de la respuesta a un RI es la **información comercial utilizable en el ámbito evaluado**. La auditoría no consulta referencias externas sobre el producto, ni para contrastar ([D-154](../../30-governance/decisions.md#d-154), [prueba de derivación](../../10-model/effective-availability.md#prueba-de-derivación)): ni se incorporan como contenido publicado por el ecommerce para suplir carencias ni sirven para refutar. Las reglas generales que se citan (una norma, una especificación de formato) no son referencias sobre el producto.

## Tipos de registro

1. **Recurso/instantánea:** representación comercial efectivamente obtenida, con momento y condiciones de lectura.
2. **Evidencia elemental:** fragmento, valor, afirmación, relación o resultado de comprobación identificable y localizable.
3. **Cobertura de inspección:** registro de qué se examinó y con qué límites ([availability-coverage.md](availability-coverage.md#cobertura)).
4. **Hallazgo:** interpretación fundada que expresa suficiencia, limitación, discrepancia o ausencia respecto de una propiedad o AC.
5. **Juicio GSC:** aplicación de las reglas del criterio a hallazgos y evidencias.

Estas entidades **se relacionan** y no deben reducirse a una sola nota narrativa. La **evidencia** (2) es contenido o resultado obtenido mediante una comprobación identificable; el **hallazgo** (4) se vincula a propiedad, AC y RI.

## Dimensiones del registro de evaluación

> **Estado: vigente** (FUND §9.4). Es una estructura orientativa: el protocolo definitivo concretará los mínimos y opcionales por tipo de evidencia.

| Dimensión | Contenido a preservar |
|---|---|
| **Identificación y origen** | Caso, RI, ámbito, ecommerce, recurso, URL/feed, representación y localizador del contenido. |
| **Contenido original** | Dato, fragmento literal, afirmación, valor, relación o resultado de prueba tal como se obtuvo. |
| **Contexto, identidad y alcance** | Entidades, vínculos, unidades, condiciones, canal, mercado, momento de referencia y relaciones necesarias para interpretar la evidencia. |
| **Método y condiciones de obtención** | Perfil de consumo, vía de recuperación, momento de inspección y operaciones de comprobación. |
| **Cobertura y limitaciones** | Partes y representaciones examinadas, recursos no consumibles, candidatos pendientes y límites de las búsquedas, especialmente ante ausencias. |
| **Contribución al RI** | Necesidad o componente del RI, función informativa del elemento y fundamento de su pertinencia. |
| **Resultado y juicio** | Hallazgos, propiedades afectadas, AC correspondientes, consecuencia y justificación del GSC o del estado NE (incidencia). |
| **Soporte reexaminable** | Referencia al recurso conservado, extracto, artefacto o comprobación que permita revisar la observación. |

La riqueza buscada es la necesaria para justificar y revisar las decisiones, no acumular capturas indiscriminadamente.

## Campos obligatorios del registro de evidencia

> **Estado: propuesta V1.** FUND §9.4 presenta una estructura orientativa; el protocolo definitivo concretará mínimos u opcionales por tipo de evidencia.

| Campo | Obligación |
|---|---|
| `evidencia_id`, `caso_id` | Siempre: identificación y enlace al expediente. |
| `fuente`, `ambito`, `representacion` | Siempre: ecommerce/recurso y ámbito bajo examen. |
| `localizador` | Siempre que el formato lo permita: URL y sección/selector, ruta JSON/XML, fila/columna, identificador de entidad o fragmento. Si no existe localizador estable, aportar extracto/instantánea que lo supla. |
| `contenido_original` | Siempre: dato literal, valor, afirmación, relación o resultado de prueba; distinguirlo de la paráfrasis. |
| `captura_fecha_hora`, `perfil_consumo` | Siempre: cuándo y bajo qué condiciones se obtuvo. |
| `entidad_y_alcance` | Cuando afecten la interpretación: sujeto, producto/variante/oferta/vendedor, mercado, canal, periodo o condición. Si es desconocido, registrarlo, no inventarlo. |
| `contexto_necesario` | Cuando se necesite para comprender etiqueta, unidad, sujeto, condición o relación; puede remitir a evidencias vinculadas. |
| `metodo_comprobacion` | Siempre para resultados analíticos, negativos o derivados; indicar operación ejecutada y material inspeccionado. |
| `resultado_observado` | Siempre: qué acredita literalmente esta pieza, sin convertirlo en juicio GSC. |
| `soporte_reexaminable` | Siempre: referencia a recurso conservado, extracto verificable, evidencia conjunta o artefacto disponible. |
| `limitaciones` | Siempre que exista incertidumbre relevante, ausencia de identidad, contexto incompleto o restricción de cobertura. |

La vinculación funcional (`ri_id`, `componente`, `funcion`) y la evaluativa (`hallazgo_id`, `AC`, propiedades) pueden almacenarse en registros asociados para evitar duplicar la evidencia. **No son opcionales para un juicio que dependa de ella.** La riqueza buscada es la necesaria para justificar y revisar decisiones, no acumular capturas indiscriminadamente.

## Reglas generales (EV-01 a EV-15)

**EV-01.** Guardar el contenido observado **literalmente** y separar la versión interpretada o normalizada.

**EV-02.** Mantener procedencia, representación, localizador, fecha/hora y perfil de consumo; un enlace sin captura contextual no siempre basta si el dato puede cambiar.

**EV-03.** Conservar el contexto mínimo necesario para interpretar la afirmación sin desanclarla de sujeto, atributo, unidad o condición.

**EV-04.** Documentar la conexión entre cada evidencia y el componente o función del RI al que contribuye.

**EV-05.** Identificar expresamente qué relaciones están **publicadas**, cuáles son interpretaciones válidas y cuáles son hipótesis pendientes o excluidas.

**EV-06.** En pruebas de **ausencia**, conservar objetivo, alcance, métodos, cobertura, posibles localizaciones inspeccionadas y límites; una búsqueda sin resultados no es prueba suficiente por sí sola.

**EV-07.** En pruebas de **atribución**, incluir soporte que permita reconocer identidad de entidades y vínculo afirmación–entidad.

**EV-08.** En **derivaciones**, conservar operandos/datos, relaciones, reglas admitidas, condiciones y conclusión obtenida; distinguir resultado derivado de dato literal.

**EV-09.** En **contradicciones**, preservar las afirmaciones comparadas y justificar identidad, alcance, condiciones y momento comparables antes de declararlas materiales.

**EV-10.** No presentar la hora de captura como prueba de que el contenido se actualizó o es vigente. La actualidad ya no se juzga ([D-123](../../30-governance/decisions.md#d-123)); una fecha de validez publicada y vencida en la captura se registra como defecto de estructura del dato.

**EV-11.** Para **exactitud**, no presentar como comprobación de verdad la mera ausencia de contradicción entre representaciones del mismo origen; registrar qué sustento existe y qué no puede confirmarse.

**EV-12.** Diferenciar **trazabilidad/verificabilidad ofrecidas por la información** (P17/P18) de la capacidad del auditor para conservar un registro. Una captura auditora no confiere automáticamente esas propiedades al ecommerce.

**EV-13.** Reutilizar la misma evidencia para distintos hallazgos/AC cuando corresponda, explicando su consecuencia específica en cada uno; no duplicar ni multiplicar penalizaciones automáticamente.

**EV-14.** La regla general citada en una comprobación (definición, norma que fija el significado de un término, especificación de formato) se etiqueta como **fuente de la regla**, nunca como contenido comercial publicado en la interfaz auditada. No se registra como evidencia ningún hecho particular del producto tomado de fuera ([D-154](../../30-governance/decisions.md#d-154)).

**EV-15.** Mantener el vínculo entre registro estructurado e informe. El informe puede resumir, pero ha de conservar referencias que permitan acceder a las evidencias relevantes.

## Reglas por tipo de evidencia

| Tipo | Contenido adicional que debe conservarse | Riesgo que controla |
|---|---|---|
| **Presencia/contenido** | Fragmento, etiqueta, unidad y sujeto pertinentes. | Citar un valor fuera de contexto. |
| **Identidad/atribución** | Identificadores, relaciones y alcance del sujeto. | Confundir variante, modelo u oferta. |
| **Relación/derivación** | Nodos, vínculos, condiciones y regla inferencial legítima. | Introducir una relación o dato supuesto. |
| **Normalización/comparación** | Valores originales, unidades, equivalencia/conversión y bases comparables. | Comparar magnitudes no equivalentes. |
| **Coherencia/conflicto** | Ambas afirmaciones, identidad, contexto y momentos. | Falsas contradicciones. |
| **Exactitud** | Comprobaciones aplicadas (estructura del dato, regla del dominio y su fuente, consistencia del ámbito), momento y resultado; sospechas con su motivo. | Confundir captura reciente o concordancia interna con verdad; presentar una sospecha como defecto. |
| **Ausencia** | Universo examinable, rutas de inspección y cobertura negativa. | Ausencias falsas por mala búsqueda. |
| **Limitación de acceso/lectura** | Petición/perfil, respuesta y condición que impide consumir el contenido. | Confundir incidente técnico y efecto sobre RI. |

## Suficiencia de evidencia para emitir un GSC

- **Correspondencia:** ¿las evidencias sostienen precisamente el hallazgo y el AC, para el mismo RI y entidad?
- **Contexto:** ¿se conocen el alcance y las condiciones necesarios, o la falta de ellos es precisamente el hallazgo acreditado?
- **Cobertura:** ¿se han examinado las unidades, componentes y representaciones necesarios para el juicio, especialmente si es negativo?
- **Resolución de conflictos:** ¿se han tratado las contradicciones/candidatos potencialmente decisivos, o se ha documentado el límite?
- **Reexamen:** ¿otro auditor puede recuperar o reconstruir las afirmaciones, pruebas y relaciones suficientes para revisar la valoración?

Si alguna respuesta es negativa y compromete **materialmente** el juicio, ampliar las comprobaciones. Si una comprobación no puede hacerse, registrar **NE** como incidencia del AC, con la comprobación fallida, o **comprobación de disponibilidad inconclusa** si el problema está en la puerta previa; no asignar un 0 sin fundamento.

## Plantilla de registro de evidencia (YAML ilustrativo)

Los registros de la auditoría informativa son **JSON validado y versionado**, con el mismo patrón que web-audit ([D-199](../../30-governance/decisions.md#d-199)). Los campos exactos se fijan al implementar el auditor; hasta entonces, esta plantilla es solo ilustrativa.

```yaml
evidencia_id: "E-XXX"
caso_id: "AUD-XXX"
fuente:
  ecommerce: "<ecommerce>"
  recurso: "<URL, identificador de feed o artefacto>"
  ambito: "Contenido"
  representacion: "alfa/1"
  localizador: "<selector, ruta, fila o segmento>"
contenido_original: "<fragmento o valor observado literalmente>"
contexto_necesario: "<etiquetas y contexto relevante>"
entidad_y_alcance: "<sujeto y condiciones conocidas>"
captura_fecha_hora: "<fecha-hora y zona>"
perfil_consumo: "<version del perfil> + <filtro/versión>"
metodo_comprobacion: "<recuperacion/lectura/contraste>"
resultado_observado: "<hecho observado, sin valoracion de calidad>"
soporte_reexaminable: "<referencia a instantanea o extracto>"
limitaciones: []
vinculos:
  componente_ri: "<componente>"
  funcion_informativa: "<funcion>"
  hallazgos: []
```

## Relacionado

- [dossier.md](dossier.md) — expediente e informe vinculados a evidencias.
- [gsc-decision.md](gsc-decision.md) — uso de la evidencia en la decisión.
