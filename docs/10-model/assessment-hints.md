---
id: assessment-hints
title: Pistas de valoración
layer: model
status: vigente
version: 1.11
updated: 2026-10-29
sources: [INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-27-hints-catalog, INTAKE 2026-10-27-hint-fields, INTAKE 2026-10-27-hints-governance, INTAKE 2026-10-27-comparison-mark, INTAKE 2026-10-27-requirement-hints-location, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-28-scope-sheet, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-29-issues-review]
---

# Pistas de valoración

## Definición

> Las **pistas de valoración** son lo que cada requisito fija para orientar la valoración de sus criterios de aceptación. — INTAKE 2026-10-27-assessment-hints

Sustituyen a lo que [D-115](../30-governance/decisions.md#d-115) llamaba «reglas de AC de un requisito» ([D-125](../30-governance/decisions.md#d-125)).

## Reglas e invariantes

1. **Tres niveles** ([D-125](../30-governance/decisions.md#d-125)):
   - **marco general**, para todos los AC;
   - **tipo de requisito** (rasgo × entidad), para Aplicabilidad y Fiabilidad; en Aplicabilidad, la prueba muestra que cuenta sobre todo la entidad;
   - **requisito**, para Precisión y Comparabilidad.

   Concreción y Justificación casi no necesitan pistas nuevas: Concreción se apoya en los componentes de la [información resolutiva](resolving-information.md), y Justificación en el marco general, salvo casos como el número de certificado.

   **Los niveles no son exclusivos** ([D-138](../30-governance/decisions.md#d-138)): dicen dónde se concentran las pistas, no que un tipo solo pueda tocar dos AC. La prueba mostró una pista por tipo de Justificación (el número de certificado).
2. **Alcance:** las pistas dicen **qué mirar**, no cuánto pesa cada criterio. El peso de cada criterio en un requisito es de la síntesis del IR ([OQ-28](../30-governance/open-questions.md)).
3. **Son criterios, no listas** ([D-128](../30-governance/decisions.md#d-128)).
   - Una pista es un criterio que el auditor aplica razonando, no una lista contra la que se compara palabra por palabra.
   - Es **breve pero suficientemente clara**, y dice su porqué.
   - Los ejemplos solo ilustran, nunca cierran: el auditor juzga también lo que no aparece en ellos.
   - Las fuentes justifican la pista, no son lo que se busca. Si una norma fija una lista cerrada (los nombres de fibras del Reglamento (UE) 1007/2011), la pista es «usa la denominación legal» y la norma se cita como fuente; no se copia la lista.
   - Si una pista es una lista o una frase exacta, la rechaza el agente revisor del paso que escribe las pistas, y se reformula como criterio. El código solo comprueba la forma ([D-211](../30-governance/decisions.md#d-211), regla 11).
   - Las comprobaciones de estructura del dato (dígito de control, suma de porcentajes) son cálculos exactos, pero son reglas generales que valen para cualquier dato: encajan.
4. **Se apoyan en las propiedades** ([D-128](../30-governance/decisions.md#d-128)). Cada pista dice **qué [propiedad](quality-properties.md) hay que observar** y **a qué AC afecta**. Respeta la cadena del canon: lo observado → la propiedad afectada → la consecuencia para el AC → el GSC. Una sola pista puede servir a varios AC sin repetirse. Las pistas orientan qué observar; **nunca puntúan propiedades**.
5. **Marca de dimensión de comparación** ([D-126](../30-governance/decisions.md#d-126)). El requisito lleva en el modelo de demanda una marca (sí / no). Si no es una dimensión de comparación, **Comparabilidad es NA** en ese requisito. Lo decide el modelo, no el auditor. Es la única excepción a la aplicación de los seis criterios ([acceptance-criteria](acceptance-criteria.md#reglas-e-invariantes), regla 9).
   - **Se fija por requisito**, no por tipo; el árbol de bloques evita la duplicidad ([D-139](../30-governance/decisions.md#d-139)).
   - **Se decide con un criterio:**

     > Un requisito **se compara** si su respuesta cambia de una oferta a otra y el comprador elige por ese valor: prefiere más, menos o uno mejor. **No se compara** si: (a) es igual en todas las ofertas, porque lo fija la ley o es universal (garantía legal); (b) solo sirve para que la oferta encaje con una **necesidad o un gusto** que ya se tiene: es un filtro (tamaño de cama, compatibilidad, idioma, color); (c) identifica la oferta o dice en qué estado está (identificadores, vendedor, disponibilidad). — INTAKE 2026-10-27-comparison-mark

   - **Sin valor por defecto:** cada requisito lleva su marca explícita y un motivo corto según el criterio. Los **dudosos**, «se compara» mientras no haya pruebas, para no quitar un criterio sin motivo.
   - **Pruebas:** preguntas comparativas de PAA; la justificación del requisito en taxo; una ley que exista para poder comparar (precio por unidad, etiqueta energética).
   - **Quién y cuándo:** como las pistas: una pasada manual de Claude para el catálogo actual; después, al crear modelos y en los entrenamientos. Si dos fuentes se contradicen, se marca como duda; mientras tanto la marca queda como dudosa, es decir, «se compara» (interpretación de Claude, [D-139](../30-governance/decisions.md#d-139)).
   - En una muestra al azar de 70 requisitos salieron mitad y mitad (49 % se compara, 43 % no, 9 % dudoso); el rasgo orienta (material: se compara; prestación: casi siempre; estética y medida: casi nunca; uso, identidad y construcción: mezclados), pero no es regla.
6. **Quién las escribe** ([D-127](../30-governance/decisions.md#d-127)):
   - **pistas dirigidas a un tipo:** las compila el entrenamiento;
   - **pistas dirigidas a una fuente:** las escribe taxo ([D-135](../30-governance/decisions.md#d-135));
   - **pistas de un requisito:** taxo, desde las referencias, la normativa que es fuente del requisito y la justificación del requisito; y PAA, desde sus preguntas. Las escriben en el propio requisito ([D-140](../30-governance/decisions.md#d-140));
   - quien redacta un bloque nuevo escribe sus pistas, sin compilar ([D-201](../30-governance/decisions.md#d-201), regla 12);
   - cada pista lleva su **origen**; las pistas **se suman y nunca se quitan** entre escritores; las correcciones siguen la regla 13.
7. **Dónde viven** ([D-134](../30-governance/decisions.md#d-134), enmendada por [D-140](../30-governance/decisions.md#d-140) y [D-208](../30-governance/decisions.md#d-208)).

   > Las pistas viven en **un catálogo propio** del motor de demanda, junto al índice de rasgos y a las reglas. Cada pista se escribe **una sola vez** y lleva **a quién va dirigida**, con una de tres llaves: **un tipo de requisito** (rasgo × entidad, o solo uno de los dos) […]; **los requisitos que citan una misma fuente** (una norma, un atributo de Shopify o una propiedad de Amazon) […]. — INTAKE 2026-10-27-hints-catalog, enmendada por D-140

   > Las **pistas dirigidas a un requisito concreto** viven **en el propio requisito** del catálogo de demanda, no en el catálogo de pistas. — INTAKE 2026-10-27-requirement-hints-location

   - **Una llave, uno o varios valores** ([D-208](../30-governance/decisions.md#d-208)): `para` admite una lista de valores de una misma llave, varias fuentes o varios tipos. Así una pista de un tema repartido (las certificaciones, en dos rasgos y tres atributos de Shopify) se escribe una sola vez. Una lista no mezcla llaves.
   - Los requisitos no copian ni referencian las pistas de tipo y de fuente: se encuentran por las etiquetas que el requisito ya lleva. Las suyas las lleva en una lista propia, como la [información resolutiva](resolving-information.md).
   - Los niveles de la regla 1 dicen para qué AC es una pista; las llaves y el requisito, a quién llega.
   - Las pistas de un requisito llegan también, por el árbol de bloques, a todas las clases que lo heredan.
   - Al montar el modelo de una ficha, el motor junta las pistas de tipo, las de fuente y las del requisito sin repetir ninguna. El modelo lleva las pistas resueltas; se genera, no se escribe. «Solo se suman» se cumple solo.
8. **Encontrarlas es código, sin LLM** ([D-134](../30-governance/decisions.md#d-134)). Es una búsqueda por etiquetas exactas: las pistas del rasgo y la entidad del requisito, más las de cada una de sus fuentes, más las que lleva el propio requisito, sin repetir.
   - Una pista dirigida a una fuente encaja con las citas de esa fuente que llevan artículo, fecha o valor: se compara por el comienzo de la etiqueta, hasta un separador propio de cada clase de fuente ([D-207](../30-governance/decisions.md#d-207)):
     - en una ley, el guion y el punto (artículo y apartado) y la arroba (fecha): `ley:UE-1007/2011` encaja con `ley:UE-1007/2011-16.1@2011-10-18`;
     - en un atributo o una propiedad, el igual (valor) y la arroba: `shopify-attr:fabric` no encaja con `shopify-attr:fabric-weave`.
   - Los requisitos de la capa general no tienen rasgo: sus pistas se dirigen por entidad o las lleva el propio requisito. Las comprobaciones de tipo de un requisito de la capa general (la longitud y el dígito de control del GTIN en `gen/03`) las lleva el propio requisito, con origen «marco» ([D-210](../30-governance/decisions.md#d-210), regla 9).
   - Las etiquetas son controladas: el código avisa de las pistas que no llegan a ningún requisito.
   - **Aplicar** las pistas a una ficha la hace el auditor razonando: el código las entrega y el auditor juzga con ellas.
9. **Campos de una pista** ([D-135](../30-governance/decisions.md#d-135)):

   | Campo | Para qué sirve |
   |---|---|
   | `id` | Número que pone el sistema, **sin ceros delante**: `PV-1`, `PV-2`… Nadie elige nombres y el número no cambia aunque se reescriba el texto. |
   | `pista` | El criterio y su porqué, en una o dos frases. |
   | `propiedad` | Qué propiedades hay que observar. |
   | `ac` | A qué criterios afecta. |
   | `para` | A quién va dirigida: un tipo (rasgo, entidad o ambos) o una fuente; o una lista de tipos o de fuentes ([D-208](../30-governance/decisions.md#d-208)). Las pistas de un requisito no lo llevan: su destino es el requisito que las contiene ([D-140](../30-governance/decisions.md#d-140)). |
   | `origen` | Quién la escribió y en qué se apoya (ley, referencia, preguntas de PAA), como en la información resolutiva. Valores: «marco» (las pistas por tipo que redacta Claude y, [D-210](../30-governance/decisions.md#d-210), las pistas de un requisito de la capa general, que es parte del marco), «normativa», «referencias», «paa» ([D-136](../30-governance/decisions.md#d-136)) e «inferida»: una pista sin apoyo directo en una fuente (la justificación del requisito, una aportación inferida), provisional hasta que la valida el entrenamiento ([D-201](../30-governance/decisions.md#d-201)). |

   — INTAKE 2026-10-27-hint-fields, enmendada por D-140 y D-208 (`para`), D-201 (`origen` «inferida») y D-210 (`origen` «marco» en la capa general)

   Ejemplo (hipotético): `{"id": "PV-3", "pista": "La composición usa el nombre legal de cada fibra, con su % en peso: es lo que permite entenderla y compararla.", "propiedad": ["P09", "P13"], "ac": ["Precisión", "Comparabilidad"], "para": {"fuente": "ley:UE-1007/2011"}, "origen": {"tipo": "normativa", "apoyo": ["ley:UE-1007/2011-16.1"]}}`.
10. **Cómo le llegan al auditor** ([D-135](../30-governance/decisions.md#d-135)). Al montar el modelo de una ficha, el código busca las pistas de cada requisito y las guarda ya resueltas en el modelo. El perfil del RI tiene un campo, `pistas_valoracion`, que se rellena solo desde el modelo: el auditor no lo escribe, solo lo usa ([ri-profile](../20-methods/audit-gsc/ri-profile.md)).
    - El registro del GSC **cita las pistas que usó el auditor** (`PV-n`), para poder reexaminar la valoración ([D-138](../30-governance/decisions.md#d-138)).
    - El modelo de una ficha **anota qué versión del catálogo de pistas usó**, como ya hace con el catálogo de requisitos. Las pistas de un requisito van con la versión de su bloque ([D-140](../30-governance/decisions.md#d-140)).
    - Las pistas **no dicen ámbito**: el auditor las aplica a lo que vea en cada ámbito. Si algún día una pista solo tiene sentido en uno, se añade el campo. Lo que cambia por ámbito es dónde y cómo aparece el dato: localización, en la [ficha del ámbito](demand-model.md#ficha-de-ámbito), no valoración ([D-155](../30-governance/decisions.md#d-155)).
11. **Cómo nace y se acepta una pista** ([D-136](../30-governance/decisions.md#d-136)).
    - Las redactan los agentes **sin aprobación del usuario**, como la información resolutiva; el usuario las revisa cuando quiere.
    - Una pista **entra** si pasa dos controles en el paso que la escribe ([D-211](../30-governance/decisions.md#d-211)):
      - **automático, de forma:** tiene los seis campos, su destino existe y su longitud es una o dos frases;
      - **un agente revisor** juzga si es un criterio, no una lista ni una frase exacta. No pide aprobación al usuario.
    - **Revisión de las pistas dirigidas a un tipo** ([D-200](../30-governance/decisions.md#d-200)). Cada una se revisa contra la lista de requisitos a los que llega, que da el código. Si la pista no vale en todos, se reescribe más general o pasa a ser una pista dirigida a una fuente o a un requisito. Ejemplo: «un gramaje en g/m²» no vale para un vinilo.
    - Por ahora **no hay métrica de calidad** de las pistas, porque aún no hay auditorías con las que medirla.
12. **Cuándo se definen** ([D-137](../30-governance/decisions.md#d-137)).

    > Mediante una pasada manual de Claude podemos construir pistas. Pero luego las pistas se irán definiendo al crear modelos de demanda, incluso cuando se realizan entrenamientos. — INTAKE 2026-10-27-hints-governance

    - **Arranque:** una pasada manual de Claude construye un primer lote. Sus pistas por tipo las redacta Claude por rasgo × entidad, a partir de la guía de los AC y de las tres familias de comprobación; el entrenamiento las guarda y las coloca. El contenido de las comprobaciones por tipo es este trabajo de redacción, con la revisión de la regla 11 ([D-200](../30-governance/decisions.md#d-200)).
    - **Después** se van definiendo al crear modelos de demanda y en los entrenamientos.
    - **Bloque nuevo** ([D-201](../30-governance/decisions.md#d-201)): quien redacta un bloque nuevo escribe sus pistas, sin compilar. El entrenamiento las consolida.
    - Una pista sin apoyo directo en una fuente lleva origen «inferida» (regla 9) y queda provisional hasta que la valida el entrenamiento, como en la [información resolutiva](resolving-information.md).
13. **Duplicadas, contradictorias y retiradas** ([D-136](../30-governance/decisions.md#d-136)).
    - Antes de añadir una pista se busca si ya hay otra con el mismo destino y la misma propiedad. Si dice lo mismo, no se añade. Si la contradice, se marca como **duda** y no se suma en silencio.
    - La búsqueda se hace también sobre lo que llega a cada requisito ([D-209](../30-governance/decisions.md#d-209)): el código avisa de las pistas que le llegan por llaves distintas con la misma propiedad y el mismo AC. Un revisor resuelve cada aviso.
    - Una pista no se borra: se **retira**. Queda marcada como retirada y su número no se reutiliza. «Nunca se quitan» vale entre escritores, no para corregir.
    - **Corregir una pista** ([D-202](../30-governance/decisions.md#d-202), que enmienda D-136):
      - si ninguna versión que la contiene la ha usado un modelo ni un registro del GSC, se corrige en su sitio, sin retirarla;
      - si un modelo o un registro del GSC ya usó esa versión, corregirla es retirarla y crear otra. La retirada protege lo que citan los modelos y los registros del GSC ([D-138](../30-governance/decisions.md#d-138)).

## Distinciones

- **Pista de valoración frente a lista de vocabulario.** «Un recuento de hilos solo es claro si dice sobre qué superficie se cuenta y si cuenta hilos simples o de varios cabos» sirve también para «300 TC» o para cualquier forma nueva; «términos ambiguos: microfibra, 144 hilos, Queen» no.
- **Pista de valoración frente a «un solo escritor por requisito»** ([D-115](../30-governance/decisions.md#d-115)). Esa regla protege la estructura del requisito (separar, partir, sacar, reformular; [D-213](../30-governance/decisions.md#d-213)). Las pistas, como las aportaciones de la información resolutiva, admiten varios orígenes y solo se suman (las correcciones siguen la regla 13).

## Interpretación

La prueba con nueve requisitos del catálogo que aplican a unas sábanas (`cat.ropa-de-casa/01`, `cat.ropa-de-casa/05`, `cat.sabanas/03`, `cat.ropa-de-cama/01`, `cat.ropa-de-casa/03`, `gen/04`, `gen.variantes/02`, `gen/12` y `gen/03`) sostiene el reparto por niveles:

| AC | Dónde se concreta | Ejemplos de la prueba |
|---|---|---|
| **Concreción** | Ya está en el catálogo: componentes de la información resolutiva | Fibras y porcentajes, composición de cada parte; hilo simple o de varios cabos; estado de cada variante |
| **Justificación** | Marco general | La base es la declaración del vendedor o una derivación reconstruible. En certificaciones, el número de certificado sale del tipo |
| **Aplicabilidad** | Tipo (entidad) | Variante: estado y GTIN de cada talla. Juego de piezas: composición de cada pieza. Oferta: precio de cada variante |
| **Fiabilidad** | Tipo (rasgo × entidad) | Identidad: dígito de control. Certificación: estructura, dominio y consistencia de lo publicado. Material: la composición suma 100 % y usa las denominaciones legales. Oferta: aritmética del precio. Tamaño de cama coherente con las medidas de la pieza |
| **Precisión** | Requisito (las unidades de las magnitudes, por tipo) | Qué términos son ambiguos y qué los fija: «microfibra» no es una fibra; «144 hilos» sin superficie ni cabos; «Queen» o «full»; «OEKO-TEX» sin decir qué norma; «garantía de 3 años» sin decir si es legal o comercial |
| **Comparabilidad** | Requisito | Si es una dimensión de comparación (hoy, la marca de la regla 5) y sobre qué base: composición (fibra y % en peso), hilos (misma superficie, hilo simple), gramaje (g/m²), precio (total) |

— INTAKE 2026-10-27-assessment-hints; fila de Fiabilidad enmendada por [D-154](../30-governance/decisions.md#d-154) (sin consulta a registros de GS1 ni de certificados; el dígito de control sigue siendo una regla citable)

- **Pistas de certificaciones** ([D-154](../30-governance/decisions.md#d-154)): van dirigidas a la fuente `shopify-attr:safety-certifications` y juzgan solo lo publicado (regla 13).
  - Retirada y sustituida: PV-39, que pedía que el número existiera en el registro del emisor, por PV-46.
  - Retirada y sustituida: PV-40 por PV-45 (Aplicabilidad: la certificación se atribuye al producto que se vende).
  - PV-46 (Fiabilidad): fecha de validez vencida o sello incompatible con la composición.
  - Nueva: PV-47 (Precisión: la norma concreta).
  - Se mantiene: PV-38 (número de certificado y organismo, Justificación).
  - PV-4, PV-5 y PV-6 se retiraron antes, al pasar del rasgo «seguridad» a la fuente.
- La prueba mostró además una comprobación de **consistencia entre requisitos del mismo ámbito** (una bajera de 90 × 190 en una ficha que dice «cama de 150»). Es consistencia por ámbito (P16) y sale del tipo.
- Requisitos de la prueba que **no son dimensiones de comparación**: tamaño de cama (es un filtro: primero se elige el tamaño y luego se compara), variantes disponibles, garantía legal (es la misma para todos) e identificadores (sirven para emparejar ofertas, no para compararlas). Valorar Comparabilidad en ellos daría un 2 automático o repetiría lo que ya mira Precisión.

## Ejemplo mínimo (hipotético)

| Pista | Propiedad | AC afectados |
|---|---|---|
| El recuento de hilos dice sobre qué superficie se cuenta y si cuenta cabos. | P13 Normalización | Precisión, Comparabilidad |
| La composición se da con nombres de fibra, no de tejido ni de acabado. | P09 Claridad | Precisión |
| El estado se da por cada variante. | P11 Identificabilidad | Aplicabilidad |
| El tamaño de cama encaja con las medidas de la pieza. | P16 Coherencia | Fiabilidad |

## Pendiente

Ver [open-questions](../30-governance/open-questions.md):

- métrica de calidad de las pistas, cuando haya auditorías ([OQ-72](../30-governance/open-questions.md));
- un índice generado de pistas por requisito, aplazado ([OQ-70](../30-governance/open-questions.md), [D-174](../30-governance/decisions.md#d-174)).

## Relacionado

- [acceptance-criteria](acceptance-criteria.md): los seis AC y su aplicación.
- [quality-properties](quality-properties.md): propiedades que observan las pistas.
- [resolving-information](resolving-information.md): información resolutiva.
- [paa-training](paa-training.md): lo que escribe PAA en el catálogo de demanda, incluidas las pistas de cada requisito.
- [model-training](model-training.md): compilación del catálogo y reglas por rasgo.
