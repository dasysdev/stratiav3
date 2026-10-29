---
id: choice-criteria
title: Criterios de elección
layer: model
status: vigente
version: 1.13
updated: 2026-10-29
sources: [INTAKE 2026-10-26-choice-criteria-and-descriptions, INTAKE 2026-10-27-paa-construction-route, INTAKE 2026-10-27-paa-new-requirements, INTAKE 2026-10-27-paa-classification-criteria, INTAKE 2026-10-27-paa-classification-criteria-2, INTAKE 2026-10-27-paa-bottom-sheet-hold, INTAKE 2026-10-27-paa-training, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-27-hint-fields, INTAKE 2026-10-28-paa-control-review-rules, INTAKE 2026-10-28-paa-parent-and-material, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-29-paa-natural-answer-and-specializations]
---

# Criterios de elección

## Definición

> Las preguntas valorativas de PAA («¿Cuál es el mejor tipo de sábana para dormir?», «¿Qué se arruga más, el satén o el percal?») no son requisitos informativos:
>
> - no preguntan por una oferta;
> - no son neutrales respecto de la respuesta;
> - dependen del comprador.
>
> Revelan, en cambio, los **criterios de elección** de la clase: los aspectos por los que los compradores juzgan si una oferta les conviene (frescor o abrigo, arrugas, durabilidad, tacto…). — INTAKE 2026-10-26-choice-criteria-and-descriptions

«Criterios de elección» se prefiere a «criterios de evaluación», que se confundiría con los [criterios de aceptación](acceptance-criteria.md). Se reconocen por People Also Ask (PAA), vía de construcción del modelo ([D-094](../30-governance/decisions.md#d-094)); el MPIR, que también los cuenta entre lo que permite reconocer, está aparcado ([D-095](../30-governance/decisions.md#d-095)). Ver [construction-routes](construction-routes.md). Un requisito que entra solo por PAA lleva origen «paa» ([D-097](../30-governance/decisions.md#d-097)). PAA también propone requisitos desde preguntas factuales sobre la oferta que ningún requisito responde: pasan C1–C4 sin un criterio de elección de por medio ([D-099](../30-governance/decisions.md#d-099)).

## Reglas e invariantes

### Cuándo un criterio de elección genera un requisito

> Entonces los criterios de elección en algunos casos sí deberían generar requisitos — palabras del usuario, INTAKE 2026-10-26-choice-criteria-and-descriptions

Un criterio de elección genera un requisito cuando cumple **todas** estas condiciones ([D-091](../30-governance/decisions.md#d-091)):

> | # | Condición | Si no se cumple |
> |---|---|---|
> | C1 | Ningún requisito existente lo responde sin derivar. | Ya está cubierto. Ejemplo: la «calidad» medida en hilos la cubre `cat.sabanas/03`. |
> | C2 | Es un hecho que la oferta puede declarar (una prestación, un resultado de ensayo, una indicación de uso). | Si solo lo puede juzgar quien compra («que me guste»), no genera requisito. |
> | C3 | Se aplica a toda la clase o a una especialización, no a un comprador. | Es una condición de compra o un escenario. |
> | C4 | Se puede formular neutral y sobre la oferta. | Si solo admite «mejor/peor» (marca, reputación), se descarta. |
>
> — INTAKE 2026-10-26-choice-criteria-and-descriptions

### Cómo se aplica

> - El requisito resultante es un requisito ordinario; en el catálogo de rasgos, casi siempre `prestacion`. **No** se crea un concepto nuevo en el modelo.
> - El criterio de elección queda como **fundamento** del requisito.
> - Su información resolutiva es la declaración de la prestación, un ensayo o una certificación. Nunca el atributo del que se deduciría la prestación (punto 1).
> - Que los compradores usen un criterio para elegir no prueba su importancia relativa: la importancia sigue saliendo de las reglas.
>
> — INTAKE 2026-10-26-choice-criteria-and-descriptions («punto 1» es la sección siguiente)

El requisito se formula con los [principios de formulación](demand-model.md#reglas-e-invariantes) de cualquier RI, lleva su [rasgo](model-training.md#rasgos), su [información resolutiva](resolving-information.md) y su [descripción](requirement-description.md), y su importancia la deciden las reglas del [entrenamiento](model-training.md).

### Prestación derivada de un atributo

> Que una ficha declare el tejido o la composición («percal», «100 % algodón») no resuelve un requisito sobre la prestación («¿qué sensación térmica ofrece?»). La derivación tiene demasiados pasos y se apoya en conocimiento del dominio.
>
> Quien lo dictamina es la **pertinencia**, en la auditoría, no la valoración de los criterios de aceptación ni el modelo de demanda: el atributo por sí solo no es pertinente para la prestación, de modo que la disponibilidad efectiva es 0. Si la ficha declara la prestación, el atributo puede acompañarla como contexto. — INTAKE 2026-10-27-ac-applicability-and-reliability
>
> Para que la auditoría pueda dictaminarlo, el requisito de la prestación **tiene que existir** en el modelo. — INTAKE 2026-10-26-choice-criteria-and-descriptions

El segundo párrafo de la cita original de 2026-10-26 («lo dictamina la valoración de los criterios de aceptación») está enmendado por [D-119](../30-governance/decisions.md#d-119). La regla y la prueba que separa una derivación admitida de una tendencia están en [effective-availability](effective-availability.md#pertinencia-de-lo-derivado) ([D-120](../30-governance/decisions.md#d-120)).

**Interpretación adoptada** ([D-090](../30-governance/decisions.md#d-090)): «demasiados pasos» se lee como una derivación que completa con conocimiento del dominio una prestación que la oferta no declara. El número de pasos sigue sin ser un criterio ([acceptance-criteria](acceptance-criteria.md#reglas-e-invariantes), regla 7; invariante 9).

### Lectura de las preguntas de PAA

Reglas decididas por el usuario al resolver las dudas de las dos primeras clasificaciones con un agente (`INTAKE 2026-10-27-paa-classification-criteria` e `INTAKE 2026-10-27-paa-classification-criteria-2`), al revisar los casos de control de PAA (`INTAKE 2026-10-28-paa-control-review-rules`) y a la vista de su pasada de control (`INTAKE 2026-10-28-paa-parent-and-material`):

- **Productos vecinos** ([D-141](../30-governance/decisions.md#d-141), enmendada por [D-146](../30-governance/decisions.md#d-146)):

  > Preguntas sobre otro producto (un hermano, como almohadas o zapatillas deportivas) quedan FUERA siempre. El perímetro va antes de la lectura sobre la oferta, que solo decide si una pregunta sobre el producto de la clase pide un hecho declarable. Un vecino nunca apoya requisitos de la clase (invariante 10), y su presencia es señal para las semillas (D-114). — INTAKE 2026-10-28-paa-control-review-rules (enmendada por D-146: la categoría madre ya no queda fuera siempre)

- **Categoría madre** ([D-146](../30-governance/decisions.md#d-146)):

  > Una pregunta sobre la categoría madre va DENTRO cuando pregunta por algo que la clase hereda de su bloque (cuidado del ante → cat.calzado/13 en botas; firmeza → cat.sofas/12 en sofás cama; «¿Qué sofá me compro?» → preferencia general). Va FUERA si solo tiene sentido para otro producto (calzado para la montaña, podólogos) o si es un hermano. — INTAKE 2026-10-28-paa-parent-and-material

  Interpretación adoptada ([D-146](../30-governance/decisions.md#d-146)): lo que la clase hereda se lee como un requisito o una aportación de un bloque heredado, o un criterio de elección que vale igual para el producto de la clase. Las semillas no cambian: «sofás» sigue en el núcleo de sofás cama.
- **Prueba de la respuesta natural** ([D-218](../30-governance/decisions.md#d-218)), que precisa «solo tiene sentido para otro producto»:

  > Si la pregunta pide elegir un producto de la madre para una necesidad, va dentro solo si un producto de la clase es una respuesta natural. Lo que la clase comparte (cuidado, material, precio) sigue dentro. — INTAKE 2026-10-29-paa-natural-answer-and-specializations

  En pantuflas, «¿Qué calzado recomiendan los podólogos?» y «¿Qué zapatos debo usar para que no me duelan los pies?» quedan fuera; en botas, «¿Cómo cuidar los zapatos de ante?» queda dentro. «Calzado para la montaña», el ejemplo de fuera de D-146, vale en pantuflas. En botas, el usuario lleva esa pregunta a una especialización nueva (abajo).
- **Especializaciones desde PAA** ([D-218](../30-governance/decisions.md#d-218)):

  > En este caso esas preguntas no irían a la especialización de botas de equitación y no irían a las de botas en general sino a una nueva especialización: botas de montaña. Es decir PAA puede generar especializaciones. — INTAKE 2026-10-29-paa-natural-answer-and-specializations

  Una pregunta sobre una especialización de la clase que el catálogo no tiene va a una especialización nueva que propone PAA, no a la del caso ni a la categoría. En propuesta (lectura de Claude, [D-218](../30-governance/decisions.md#d-218)): si el catálogo ya la tiene, PAA usa su id; la propuesta entra «no compilada» y encolada, como la del clasificador en ejecución, y la admite el entrenamiento con el [criterio de especialización](study-class.md#criterio-de-especialización) ([D-216](../30-governance/decisions.md#d-216)). Cómo entra en el catálogo queda abierto ([OQ-87](../30-governance/open-questions.md)).
- **Material** ([D-146](../30-governance/decisions.md#d-146)):

  > Una pregunta sobre el material va DENTRO si la clase tiene o hereda ese material (como la seda en sábanas). «Zapatillas» sin señal de deporte o calle se lee como la clase. — INTAKE 2026-10-28-paa-parent-and-material

  «¿Qué país produce la mejor seda?» sigue dentro en sábanas. La lectura de «zapatillas» es de pantuflas: una denominación ambigua se lee como la clase cuando no hay señal del vecino.
- **Lectura sobre la oferta** ([D-100](../30-governance/decisions.md#d-100)):

  > Antes de aplicar C2 a una pregunta de clase, se relee sobre la oferta: «¿… esta oferta?». Si un hecho que la oferta puede declarar la responde, la pregunta confirma ese requisito o propone un candidato. C2 solo se aplica cuando ningún hecho de la oferta la responde: hábitos («¿cada cuánto se lavan?»), saber doméstico («¿cómo se dobla?»).

- **Apoyo mínimo** ([D-102](../30-governance/decisions.md#d-102)): basta una pregunta para que un candidato que cumple C1–C4 entre como tal. Este apoyo es para que el requisito exista; para separarlo hace falta la [separación por dimensión](../20-methods/product-taxonomy/requirement-blocks.md#separación-por-dimensión) ([D-103](../30-governance/decisions.md#d-103)).
- **Entrada en el catálogo** ([D-178](../30-governance/decisions.md#d-178)): un requisito candidato entra de forma automática al compilar la pasada del [entrenamiento de PAA](paa-training.md), si el control no empeora ([D-180](../30-governance/decisions.md#d-180)). Entra como versión nueva del bloque, con origen «paa». Su fuente guarda el texto literal de la pregunta PAA, no solo su referencia. El clasificador de preguntas PAA aplica estas reglas con el reglamento de su agente (`demand-engine/classifier/paa.md`).
- **Criterios intermedios** ([D-104](../30-governance/decisions.md#d-104)): un criterio como el «material» o la «calidad» queda cubierto y se descompone en las prestaciones. El «material» lo cubre la composición en cuanto a qué material es (funciones Comprender y Comparar); en cuanto a si es mejor, se descompone en las prestaciones (función Evaluar): nivel térmico, arrugas, duración y resistencia, humedad, tacto y piel, en sábanas. Deducir esas prestaciones del material es lo que D-090 no admite. Una pregunta genérica («¿es bueno el lino?») no nombra ninguna prestación: apoya la composición, no a una prestación concreta.
- **Preguntas de grado** ([D-110](../30-governance/decisions.md#d-110)): una pregunta de grado («tan suaves», «las más frescas», «cuál se arruga menos») indica el aspecto; C2 se juzga sobre el requisito, formulado por tipo o por declaración. Si la oferta puede declarar el tipo, la pregunta de grado apoya ese requisito. No genera cuando el aspecto solo admite más o menos y ninguna categoría declarable lo resuelve (la marca, C4).
- **Tacto** ([D-105](../30-governance/decisions.md#d-105)): aplicación de la regla anterior. Cumple C2 si se formula por el tipo de tacto (sedoso o liso, crujiente, afelpado, fresco al tacto), no por el grado de suavidad, que solo admite más o menos.
- **Moda o tendencia** ([D-142](../30-governance/decisions.md#d-142)): caso de la excepción de [D-110](../30-governance/decisions.md#d-110).

  > La moda o tendencia NUNCA genera («¿qué X se llevan?», «¿qué X están de moda?»): «estar de moda» depende del mercado y del momento (C2/C4), un caso de la excepción de D-110. — INTAKE 2026-10-28-paa-control-review-rules

- **Popularidad, preferencia general y alternativa de producto** ([D-142](../30-governance/decisions.md#d-142)):

  > - La popularidad («la más vendida») no genera (reputación, C4; invariante 14).
  > - La preferencia general («¿cuál es el mejor sofá cama?») es un criterio intermedio (D-104), cubierto y descompuesto en las prestaciones, como «calidad» en sábanas; no es «no genera».
  > - La alternativa de producto («¿sofá cama o cama abatible?») no genera (C3).
  >
  > — INTAKE 2026-10-28-paa-control-review-rules

- **Certificación y prestación** ([D-106](../30-governance/decisions.md#d-106)): si el requisito de certificaciones recoge la declaración de una prestación (por ejemplo, «hipoalergénico»), la cubre, salvo que PAA muestre que esa prestación es una dimensión de comparación de la clase ([D-109](../30-governance/decisions.md#d-109)).

## Distinciones

| Par | Diferencia |
|---|---|
| Criterio de elección frente a **criterio de aceptación** | El primero es un aspecto por el que el comprador juzga si una oferta le conviene; el segundo, una condición con que la auditoría valora la información de un RI en un ámbito. |
| Criterio de elección frente a **RI** | El criterio es el fundamento; el RI, la cuestión neutral sobre la oferta que genera cuando cumple C1–C4. |
| Criterio de elección frente a **condición de compra** o **escenario** | Si solo se aplica a un comprador, es una condición de compra o un escenario (C3), no un criterio de la clase ([demand-model](demand-model.md#distinciones)). |
| Uso del criterio frente a **importancia relativa** | Que los compradores lo usen no prueba la [importancia](demand-model.md#importancia-relativa) del requisito. |
| Criterio **intermedio** frente a prestación | El intermedio («material», «calidad») no es una prestación: queda cubierto y se descompone en las prestaciones ([D-104](../30-governance/decisions.md#d-104)). |
| Prestación frente a **atributo** | El atributo («percal») no resuelve la prestación («fresca»); la prestación se resuelve con su declaración, un ensayo o una certificación. |

## Ejemplo mínimo

Clase de sábanas: sondas de PAA del 2026-10-26 (`INTAKE 2026-10-26-choice-criteria-and-descriptions`) y clasificaciones con un agente, con las decisiones de [D-108](../30-governance/decisions.md#d-108), [D-110](../30-governance/decisions.md#d-110) y [D-112](../30-governance/decisions.md#d-112) (`INTAKE 2026-10-27-paa-classification-criteria`, `INTAKE 2026-10-27-paa-classification-criteria-2` e `INTAKE 2026-10-27-paa-bottom-sheet-hold`). Los requisitos que se generan son candidatos: aún no están en el catálogo de la clase. Los escribe el entrenamiento de PAA ([D-115](../30-governance/decisions.md#d-115)) y entran al compilar su pasada ([D-178](../30-governance/decisions.md#d-178)).

| Criterio de elección | Preguntas PAA que lo apoyan | ¿Genera requisito? |
|---|---|---|
| Frescor o abrigo | «¿Las de microfibra dan calor?», «¿Cuáles son las sábanas más frescas?» | Sí: una sola dimensión térmica con dos polos; `inf/01` se reformula («¿Qué nivel de abrigo o de frescor ofrece…?») y pasa a origen «paa». |
| Arrugas | «¿Qué se arruga más, el satén o el percal?», «¿Se arruga mucho el lino?» | Sí, requisito propio: pasa las dos pruebas de la separación por dimensión ([D-103](../30-governance/decisions.md#d-103)). |
| Durabilidad | «¿Cuánto dura la coralina?», «¿Se encoge el lino al lavarlo?» | Sí, como lista agrupada encabezada por la duración («¿Qué duración y resistencia al uso y al lavado tiene…?»). |
| Tacto | «¿Por qué las sábanas de los hoteles son tan suaves?» | Sí, por tipo de tacto, con origen «paa»: la pregunta es de grado y apoya el requisito formulado por tipo, porque la oferta puede declarar el tipo ([D-110](../30-governance/decisions.md#d-110)); una sola pregunta basta ([D-102](../30-governance/decisions.md#d-102)). Rasgo «sensorial» ([D-105](../30-governance/decisions.md#d-105)). |
| Ajuste de la bajera | «¿Cómo hacer para que no se salga la sábana de abajo?», «¿Qué sábanas no se salen?» | Ya cubierto (`inf/02`, `cat.sabanas-ajustables/01`): que se salga depende sobre todo de que el bolsillo encaje con el colchón de quien compra (C3) ([D-112](../30-governance/decisions.md#d-112)). |
| Calidad en general | «¿Cuáles son las sábanas de mejor calidad?» | No: criterio intermedio, se descompone en los anteriores (C1). |
| Material | «¿Qué es mejor, lino o algodón?», «¿Son malas las de microfibra?» | No: criterio intermedio, cubierto por la composición y descompuesto en las prestaciones ([D-104](../30-governance/decisions.md#d-104)). |
| Marca | «¿Cuál es la mejor marca de sábanas en España?» | No (C4). |

## Relacionado

- [demand-model](demand-model.md): requisito informativo, principios de formulación y vías de construcción.
- [requirement-description](requirement-description.md): descripción de un requisito.
- [resolving-information](resolving-information.md): información resolutiva.
- [acceptance-criteria](acceptance-criteria.md): derivaciones admitidas.
- [effective-availability](effective-availability.md#pertinencia-de-lo-derivado): pertinencia de lo derivado y prueba de derivación.
- [MPIR](../20-methods/mpir/README.md) (método, propuesta).
