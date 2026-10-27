---
id: assessment-hints
title: Pistas de valoración
layer: model
status: vigente
version: 1.0
updated: 2026-10-27
sources: [INTAKE 2026-10-27-assessment-hints]
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

   Concreción y Justificación no necesitan pistas nuevas: Concreción se apoya en los componentes de la [información resolutiva](resolving-information.md), y Justificación en el marco general.
2. **Alcance:** las pistas dicen **qué mirar**, no cuánto pesa cada criterio. El peso de cada criterio en un requisito es de la síntesis del IR ([OQ-28](../30-governance/open-questions.md)).
3. **Son criterios, no listas** ([D-128](../30-governance/decisions.md#d-128)).
   - Una pista es un criterio que el auditor aplica razonando, no una lista contra la que se compara palabra por palabra.
   - Es **breve pero suficientemente clara**, y dice su porqué.
   - Los ejemplos solo ilustran, nunca cierran: el auditor juzga también lo que no aparece en ellos.
   - Las fuentes justifican la pista, no son lo que se busca. Si una norma fija una lista cerrada (los nombres de fibras del Reglamento (UE) 1007/2011), la pista es «usa la denominación legal» y la norma se cita como fuente; no se copia la lista.
   - El entrenamiento rechaza las pistas que sean una lista o una frase exacta y las reformula como criterio.
   - Las comprobaciones de estructura del dato (dígito de control, suma de porcentajes) son cálculos exactos, pero son reglas generales que valen para cualquier dato: encajan.
4. **Se apoyan en las propiedades** ([D-128](../30-governance/decisions.md#d-128)). Cada pista dice **qué [propiedad](quality-properties.md) hay que observar** y **a qué AC afecta**. Respeta la cadena del canon: lo observado → la propiedad afectada → la consecuencia para el AC → el GSC. Una sola pista puede servir a varios AC sin repetirse. Las pistas orientan qué observar; **nunca puntúan propiedades**.
5. **Marca de dimensión de comparación** ([D-126](../30-governance/decisions.md#d-126)). El requisito lleva en el modelo de demanda una marca (sí / no). Si no es una dimensión de comparación, **Comparabilidad es NA** en ese requisito. Lo decide el modelo, no el auditor. Es la única excepción a la aplicación de los seis criterios ([acceptance-criteria](acceptance-criteria.md#reglas-e-invariantes), regla 9).
6. **Quién las escribe** ([D-127](../30-governance/decisions.md#d-127)):
   - **pistas por tipo:** una tabla de reglas por rasgo × entidad, como la de importancia, que compila el entrenamiento;
   - **pistas por requisito:** taxo, desde las referencias, la normativa que es fuente del requisito y la justificación del requisito; y PAA, desde sus preguntas;
   - cada pista lleva su **origen**; las pistas **se suman y nunca se quitan**.

## Distinciones

- **Pista de valoración frente a lista de vocabulario.** «Un recuento de hilos solo es claro si dice sobre qué superficie se cuenta y si cuenta hilos simples o de varios cabos» sirve también para «300 TC» o para cualquier forma nueva; «términos ambiguos: microfibra, 144 hilos, Queen» no.
- **Pista de valoración frente a «un solo escritor por requisito»** ([D-115](../30-governance/decisions.md#d-115)). Esa regla protege la estructura del requisito (separar, partir, sacar). Las pistas, como las aportaciones de la información resolutiva, admiten varios orígenes y solo se suman.

## Interpretación

La prueba con nueve requisitos del catálogo que aplican a unas sábanas (`cat.ropa-de-casa/01`, `cat.ropa-de-casa/05`, `cat.sabanas/03`, `cat.ropa-de-cama/01`, `cat.ropa-de-casa/03`, `gen/04`, `gen.variantes/02`, `gen/12` y `gen/03`) sostiene el reparto por niveles:

| AC | Dónde se concreta | Ejemplos de la prueba |
|---|---|---|
| **Concreción** | Ya está en el catálogo: componentes de la información resolutiva | Fibras y porcentajes, composición de cada parte; hilo simple o de varios cabos; estado de cada variante |
| **Justificación** | Marco general | La base es la declaración del vendedor o una derivación reconstruible. En certificaciones, el número de certificado sale del tipo |
| **Aplicabilidad** | Tipo (entidad) | Variante: estado y GTIN de cada talla. Juego de piezas: composición de cada pieza. Oferta: precio de cada variante |
| **Fiabilidad** | Tipo (rasgo × entidad) | Identidad: dígito de control y GS1. Certificación: registro y clases válidas. Material: la composición suma 100 % y usa las denominaciones legales. Oferta: aritmética del precio. Tamaño de cama coherente con las medidas de la pieza |
| **Precisión** | Requisito (las unidades de las magnitudes, por tipo) | Qué términos son ambiguos y qué los fija: «microfibra» no es una fibra; «144 hilos» sin superficie ni cabos; «Queen» o «full»; «OEKO-TEX» sin decir qué norma; «garantía de 3 años» sin decir si es legal o comercial |
| **Comparabilidad** | Requisito | Si es una dimensión de comparación y sobre qué base: composición (fibra y % en peso), hilos (misma superficie, hilo simple), gramaje (g/m²), precio (total) |

— INTAKE 2026-10-27-assessment-hints

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

- formato de las pistas en el catálogo y de la tabla por tipo, y cómo las usa la auditoría en el perfil del RI ([OQ-68](../30-governance/open-questions.md));
- cómo se fija la marca de dimensión de comparación: valor por defecto y qué prueba la establece ([OQ-69](../30-governance/open-questions.md));
- contenido de la tabla por tipo para las comprobaciones de corrección ([OQ-66](../30-governance/open-questions.md)).

## Relacionado

- [acceptance-criteria](acceptance-criteria.md): los seis AC y su aplicación.
- [quality-properties](quality-properties.md): propiedades que observan las pistas.
- [resolving-information](resolving-information.md): información resolutiva.
- [paa-training](paa-training.md): lo que escribe PAA en el catálogo.
- [model-training](model-training.md): compilación del catálogo y reglas por rasgo.
