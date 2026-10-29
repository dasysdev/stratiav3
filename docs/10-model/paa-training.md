---
id: paa-training
title: Entrenamiento de PAA
layer: model
status: vigente
version: 1.6
updated: 2026-10-29
sources: [INTAKE 2026-10-27-paa-training, INTAKE 2026-10-27-paa-pilot-classes, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-27-hint-fields, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-29-issues-review]
---

# Entrenamiento de PAA

People Also Ask (PAA) es una [vía de construcción](construction-routes.md) del modelo de demanda ([D-094](../30-governance/decisions.md#d-094)). Tiene un **entrenamiento propio**, independiente del [entrenamiento del modelo de demanda](model-training.md) (el de taxo), que refina cómo se recogen y se leen las preguntas y escribe en el catálogo lo que es de PAA ([D-114](../30-governance/decisions.md#d-114), [D-115](../30-governance/decisions.md#d-115)).

## Definición

> Entrenamiento propio de PAA, independiente del de taxo, con pasadas solo de PAA, «para que se autorefine en reglas, criterios, definición de semillas».
>
> — INTAKE 2026-10-27-paa-training (palabras del usuario entre comillas)

> aportar nuevos requisitos, aportar reglas para AC de un requisito constituido y confirmar requisitos inferidos. […] Si es así no habría conflicto.
>
> — INTAKE 2026-10-27-paa-training (palabras del usuario)

## Reglas e invariantes

### Lo que refina solo

> Alcance de lo que se refina solo: estrategia de semillas, vocabulario de criterios de elección (como el índice de rasgos, D-056) y calibración de reglas.
>
> — INTAKE 2026-10-27-paa-training

1. **Estrategia de semillas:** la regla de semillas (núcleo y valores del rasgo que más condiciona las prestaciones), que hoy está calibrada con una sola clase. Vive en el [README del motor PAA](../../demand-engine/src/demand_engine/paa/README.md#estrategia-de-semillas).
2. **Vocabulario de criterios de elección:** los nombres de los [criterios de elección](choice-criteria.md), por analogía con el vocabulario abierto de rasgos ([D-056](../30-governance/decisions.md#d-056)).
3. **Calibración de reglas:**

   > «Calibración de reglas» = ajustar parámetros dentro de las reglas vigentes (por ejemplo, cuántas preguntas o materiales exige la prueba (a)), validado contra los casos de control y con informe.
   >
   > — INTAKE 2026-10-27-paa-training

   El ejemplo es la prueba (a) de la [separación por dimensión](../20-methods/product-taxonomy/requirement-blocks.md#separación-por-dimensión) ([D-103](../30-governance/decisions.md#d-103), [D-109](../30-governance/decisions.md#d-109)).

**Límites** (INTAKE 2026-10-27-paa-training):

- **Crear o retirar reglas** de lectura de las preguntas ([D-100](../30-governance/decisions.md#d-100) a [D-113](../30-governance/decisions.md#d-113)) sigue siendo **decisión del usuario**. El entrenamiento solo ajusta sus parámetros.
- **Nada se acepta si empeora una métrica frente al control.**
- **Regla de aceptación** ([D-180](../30-governance/decisions.md#d-180)): un ajuste de semillas, vocabulario o parámetros se acepta si ningún apartado baja en esperados encontrados ni sube en regresiones. Se cuenta sobre el total de los conjuntos de control. Los apartados son los del comparador `bin/paa control`: perímetro, criterios, candidatos, revisiones y aportaciones. El informe muestra cada conjunto. Lo nuevo y la eficiencia se informan, pero no deciden. No hay umbrales numéricos.
- **El número de candidatos no es objetivo**, como no lo es el de críticos ([D-059](../30-governance/decisions.md#d-059)).

### Lo que escribe en el catálogo

El entrenamiento de PAA **sí modifica el catálogo**. Tiene cuatro papeles, todos aditivos o sobre lo que es de PAA ([D-115](../30-governance/decisions.md#d-115)):

| # | Papel | Sobre qué |
|---|---|---|
| 1 | **Requisitos nuevos**, con id propio y origen «paa» ([D-097](../30-governance/decisions.md#d-097), [D-099](../30-governance/decisions.md#d-099)) | Lo que ningún requisito responde |
| 2 | **[Pistas de valoración](assessment-hints.md)** de un requisito, desde lo que muestran las preguntas: sobre todo de Precisión (qué términos son ambiguos) y de Comparabilidad (sobre qué base se compara); sus preguntas comparativas son además prueba para la [marca de dimensión de comparación](assessment-hints.md#reglas-e-invariantes) ([D-139](../30-governance/decisions.md#d-139)) | Un requisito ya constituido, de cualquier origen |
| 3 | **Confirmar o revisar cuestiones inferidas** ([D-094](../30-governance/decisions.md#d-094)); p. ej. `inf/01`, reformulado con los dos polos de la dimensión térmica ([D-108](../30-governance/decisions.md#d-108)) | Requisitos de origen «inferida» |
| 4 | **Aportaciones aditivas** de precisión y de sustento ([D-101](../30-governance/decisions.md#d-101)) | Requisitos existentes, de cualquier origen |

**Entrada en el catálogo** ([D-178](../30-governance/decisions.md#d-178)):

- Los requisitos «paa», las inferidas confirmadas o revisadas y las aportaciones de PAA entran de forma automática al compilar la pasada de PAA, si el control no empeora (regla de aceptación de D-180).
- Entran como versión nueva del bloque, con origen «paa».
- La fuente guarda el texto literal de la pregunta PAA, no solo su referencia.

Lo que D-115 llamaba «reglas de AC» son las pistas de valoración ([D-125](../30-governance/decisions.md#d-125)): dicen qué mirar, no puntúan ni ponderan. PAA las escribe junto con taxo, cada una con su origen, y solo se suman, salvo retirada ([D-136](../30-governance/decisions.md#d-136); [D-127](../30-governance/decisions.md#d-127)). Sus campos los fija [D-135](../30-governance/decisions.md#d-135) ([assessment-hints](assessment-hints.md#reglas-e-invariantes)).

### Un solo escritor por requisito

> Las revisiones estructurales de requisitos que nacen de las referencias (separar, sacar, partir) entran a la compilación de taxo: PAA deja un **registro** que lee el próximo entrenamiento de taxo, que las reevalúa al compilar. Un solo escritor por requisito.
>
> — INTAKE 2026-10-27-paa-training

Enmendado por [D-179](../30-governance/decisions.md#d-179): no hay un registro propio de revisiones. La compilación de taxo lee las revisiones de los `classified.json` de `demand-engine/var/paa/sets/`. `var/` es desechable: si se limpia antes de compilar, esas revisiones se pierden y hay que volver a clasificar el conjunto. Ampliado por [D-213](../30-governance/decisions.md#d-213): «reformular» es una revisión más, con el mismo tratamiento que separar, sacar y partir.

- Un requisito que nace de las referencias lo escribe el entrenamiento de taxo; por analogía, también uno de origen «normativa» ([D-115](../30-governance/decisions.md#d-115), interpretación). PAA solo le suma lo aditivo (papeles 2 y 4) y deja en su clasificación (`classified.json`) las revisiones estructurales (separar, sacar, partir, reformular), como la separación por dimensión ([D-103](../30-governance/decisions.md#d-103)).
- Un requisito de origen «paa» lo escribe el entrenamiento de PAA.
- Las inferidas las propone y compila taxo ([D-036](../30-governance/decisions.md#d-036)). PAA las confirma o revisa (papel 3); al confirmarlas pasan a origen «paa» ([D-097](../30-governance/decisions.md#d-097)).

## Distinciones

| | Entrenamiento del modelo de demanda (taxo) | Entrenamiento de PAA |
|---|---|---|
| Casos | Fichas del catálogo de entrenamiento y conjunto de control de 14 casos | Conjuntos de semillas por clase y casos de control de PAA |
| Refina | Reglas inducidas: importancia, relevancia, rasgos | Semillas, vocabulario de criterios, parámetros de las reglas de lectura |
| Escribe | Bloques compilados, requisitos de las referencias e inferidas propuestas | Requisitos «paa», pistas de valoración, confirmación o revisión de inferidas y aportaciones aditivas; revisiones para taxo, en sus `classified.json` |
| Importancia | La deciden sus reglas | No la decide: PAA no prueba la importancia ([D-094](../30-governance/decisions.md#d-094)) |

## Piloto de medición

> Empieza por un piloto de medición de 3-4 clases [las clases, enmendadas por D-116], sin inducción.
>
> Clasificación única: sin doble pasada de estabilidad en el piloto.
>
> — INTAKE 2026-10-27-paa-training; las clases, enmendadas por [D-116](../30-governance/decisions.md#d-116)

- **Clases:** las de los 14 casos de referencia, el [conjunto de control](model-training.md#casos-alcance-y-ejecución) del entrenamiento del modelo de demanda, cada una con su conjunto de semillas por la regla vigente. Enmendado por [D-116](../30-governance/decisions.md#d-116):

  > usaremos los 14 casos de referencia.
  >
  > — INTAKE 2026-10-27-paa-pilot-classes (palabras del usuario)

  Un conjunto por clase distinta, no por caso: los casos que comparten la clave del modelo comparten conjunto. Con los 14 casos son 12 clases, sábanas incluida.
- **Qué mide:** qué varía entre clases: semillas, clics, criterios y dudas.
- **Clasificación:** una por conjunto, con la versión del catálogo anotada.
- **Casos de control de PAA:** lo esperado de cada uno lo decide el usuario, con sábanas entre ellos ([D-114](../30-governance/decisions.md#d-114)).

**Riesgos** (INTAKE 2026-10-27-paa-training):

- volumen de búsquedas en Google: el primer bloqueo es probable ([D-096](../30-governance/decisions.md#d-096));
- sobreajuste a sábanas, la única clase con que se calibró la regla de semillas;
- dependencia de la versión del catálogo.

Con 12 clases el volumen de búsquedas, y con él el riesgo de bloqueo, es mayor ([D-116](../30-governance/decisions.md#d-116)). Coste orientativo por clase: ~10 búsquedas (~5 min) y 0,7-1,3 M tokens, casi todo caché.

## Pendiente

Ver [open-questions](../30-governance/open-questions.md):

- índice generado de pistas de valoración por requisito, aplazado ([OQ-70](../30-governance/open-questions.md)).

## Relacionado

- [construction-routes](construction-routes.md) — PAA como vía de construcción y origen «paa»
- [choice-criteria](choice-criteria.md) — criterios de elección, C1–C4 y lectura de las preguntas PAA
- [model-training](model-training.md) — entrenamiento y ejecución del modelo de demanda
- [acceptance-criteria](acceptance-criteria.md) — los seis AC
- [Motor PAA](../../demand-engine/src/demand_engine/paa/README.md) — captura, semillas y clasificación
