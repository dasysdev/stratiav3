# Reglamento operativo del modelo de demanda · v1

Procedimiento para obtener, a partir de la ficha de un producto, su **modelo de demanda**: un conjunto de bloques de requisitos, su aplicación a la oferta concreta y su denominación. Condensa el canon (`docs/10-model/demand-model.md`, `docs/10-model/study-class.md` y las decisiones D-020 a D-038). Si el reglamento y el canon discrepan, prevalece el canon y la discrepancia se anota en el informe del experimento.

## 0. Propósito

El modelo sirve para establecer **requisitos informativos**: las cuestiones que la información comercial de la oferta debe permitir resolver. Ese es el criterio que manda. Que una característica sea «especialización» o «valor» es instrumental: lo que importa es qué cuestiones entran en el modelo y con qué importancia.

- **Modelo de requisitos:** conjunto de bloques. Es lo que se reutiliza entre productos.
- **Aplicación:** qué bloques condicionados de la capa general se activan en esta oferta.
- **Identidad = modelo de requisitos + aplicación.** Dos ofertas con los mismos bloques comparten modelo aunque su aplicación difiera.

## 1. Parámetros

| ID | Parámetro | Valor vigente | Fuente |
|---|---|---|---|
| P1 | Versiones de las referencias | Las fijadas en `references/var/pins.json` | refs |
| P2 | Eje de la clase | Shopify Standard Product Taxonomy | D-021 |
| P3 | Base de una categoría de Shopify (para decidir especializaciones) | Atributos propios + los de todas sus ascendientes | D-029 |
| P4 | Base en Amazon (para decidir especializaciones) | Propiedades del PTD + valores de `special_feature` | D-030 |
| P5 | Apoyo de una especialización | Estricto: la dimensión existe en algún componente; lo afín solo es complementario | D-024 |
| P6 | Entrada de una categoría | Aporta requisitos al producto o a una pieza, o clasificación objetiva cuando tiene sentido (alias si no aporta) | D-023, D-028, D-033 |
| P7 | Capa general | `catalog/gen.json` (consultable con `taxo gen`): no se reescribe | D-034, D-038 |
| P8 | Fuente de los requisitos de categoría | Atributos **propios** de cada categoría de Shopify; Amazon y Google solo apoyan | D-009, D-038 |
| P9 | Cuestiones inferidas | Permitidas, provisionales, con origen «inferida» | D-036 |
| P10 | Importancia | Pruebas operativas (paso 4) | D-035 |

## 2. Herramientas

Todo con `demand-engine/bin/taxo` (ver `taxo --help`):

- Ficha: `taxo page facts ID [palabras…]`, `taxo page section ID ENCABEZADO`, `taxo page grep ID REGEX`.
- Capa general: `taxo gen`.
- Shopify: `taxo shopify REGEX`; `taxo category ID` (madres, hijas, mapeo a Google y base completa); `taxo category ID --own` (solo los atributos propios: el contenido de un bloque `cat.`); `taxo values REGEX`.
- Google: `taxo google REGEX`. Amazon: `taxo amazon REGEX`, `taxo ptd TIPO [REGEX]`, `taxo ptd TIPO --enum PROP`.

En Shopify en español hay nombres repetidos y traducciones engañosas: decide siempre por identificador, nombre inglés y atributos.

## 3. Procedimiento

### Paso 1 · Leer la ficha

- Extrae lo **declarado** en el texto y en los datos estructurados: tipo de producto, piezas, materiales, construcción, usos, funciones, medidas y variantes, condiciones de la oferta (estado, precio y precio de referencia, disponibilidad y cantidad, envío, devoluciones, garantía) y beneficios que reclama. Cita la evidencia.
- No cuenta como declarado lo que solo aparece en nombres de ficheros, iconos o atributos HTML, ni las afirmaciones genéricas de la tienda («todos nuestros productos…»).
- No completes hechos ausentes con conjeturas ni con conocimiento externo.

### Paso 2 · Composición de la clase (categorías)

1. Busca la categoría de Shopify del producto. Si es un **juego** con piezas de categorías distintas, busca la de **cada pieza**: la clase es la composición de esas categorías, no su ancestro común.
2. Una categoría candidata **entra** si aporta requisitos al producto o a una pieza, o si el producto entra en ella por **clasificación objetiva** cuando tiene sentido para nombrar lo que el producto es. Si entra sin aportar requisitos, es un **alias**: aparece en el nombre, no en el modelo.
3. **No entra** si traería requisitos que no aplican (lee la descripción de sus atributos distintivos), si es una entrada duplicada de otra para el mismo tipo de producto, si el uso que la define depende solo de una variante o si solo hay proximidad temática.
4. Prefiere la categoría más específica cuya definición cumple el producto. Lo que Shopify distingue como categoría va en la clase, no como especialización.

### Paso 3 · Especializaciones

Cada característica declarada que la clase no recoge como categoría se clasifica así:

| Caso | Tratamiento |
|---|---|
| Variante (medida, talla, color elegido) | Activa `gen.variantes`; no es especialización |
| Valor estético, etiqueta promocional, nombre comercial | No aporta requisitos |
| Beneficio reclamado (un efecto que el producto dice producir) | No es especialización, salvo que las referencias tengan un tipo de producto definido por él; su fundamento se evalúa en la auditoría. El material reciclado no es beneficio |
| Condición o situación de la oferta (outlet, liquidación, exposición, reacondicionado, descuento, última unidad…) | Activa bloques condicionados de la capa general (paso 5) |
| Revela una dimensión que **tienen todos** los productos de la clase | No forma bloque: su cuestión va al bloque de la categoría (de las referencias o como inferida, paso 4) y el valor declarado es la respuesta |
| Trae cuestiones que **no se aplican** a los demás productos de la clase | Candidata a **especialización** (bloque `esp.`) |

Una candidata es especialización si cumple las cinco condiciones:

1. Es del producto o de la oferta, declarada y estable.
2. Trae cuestiones propias: concretas, neutrales y que no salen de la base de la clase (P3, P4) ni de la capa general. Si solo cambia valores esperados, solo hace que dejen de aplicarse cuestiones o solo activa cuestiones condicionadas ya previstas, es un valor que condiciona.
3. Esas cuestiones son relevantes para evaluar la clase, no para un comprador concreto.
4. Tiene apoyo (P5): la dimensión existe en algún componente (atributos de Shopify, nodo o PTD de Amazon incluido `special_feature`, categoría de Google). Si falla, sus cuestiones no se pierden: van al bloque de la categoría como requisitos condicionados.
5. Se fija en el nivel más general cuyos miembros comparten sus cuestiones; el valor concreto del producto es el valor de esa dimensión.

Un conjunto de piezas de categorías distintas es la especialización `esp.juego`: aporta qué piezas incluye, cuántas y en qué medidas.

### Paso 4 · Bloques y requisitos

1. **Capa general:** no la reescribas. Solo puedes revisar la importancia de un requisito `gen` para esta clase, con justificación (en `general_overrides`).
2. **Un bloque `cat.` por categoría** de la composición y **por cada categoría madre** (sector), con los atributos **propios** de esa categoría (`taxo category ID --own`). Cada atributo pertinente da un requisito formulado como cuestión neutral; si un atributo no aplica a la clase, déjalo fuera y dilo en `doubts`. En el bloque de la categoría del producto añade también:
   - las **cuestiones inferidas**: cuestiones que afectan a todos los productos de la clase y que ni las referencias ni la capa general recogen; solo de toda la clase, neutrales, justificadas y sin duplicar la base; origen «inferida»;
   - los requisitos condicionados de las distinciones que no cumplen la condición 4.
3. **Un bloque `esp.` por especialización**, con sus cuestiones propias.
4. **Importancia** de cada requisito, con estas pruebas: **crítico** si, sin resolverlo, la oferta deja de ser evaluable (no se sabe qué se vende, cuánto cuesta o si se puede adquirir); **principal** si es uno de los criterios con los que se comparan y eligen ofertas de la clase; **complementario** si es relevante sin ser indispensable ni central. La confianza no cambia la importancia: un requisito dudoso no se baja de nivel por dudoso. Los críticos son pocos y casi todos están en la capa general.
5. Identificadores: `cat.<nombre>` y `esp.<nombre>` con un nombre propio en español, en minúsculas y con guiones (no copies la etiqueta de la referencia si es ambigua); requisitos `<bloque>/<nn>`. Las referencias van en `refs` con el formato `<fuente>:<identificador>@<versión>` (p. ej., `shopify:<id>@v2026-08`, `google:<id>@2021-09-21`, `amazon-ptd:<TIPO>@2026-10-24`, `amazon-btg:<nodo>@2026-10-24`), y las fuentes de cada requisito en `sources` (p. ej., `shopify-attr:<handle>`, `amazon-ptd-prop:<TIPO>.<propiedad>`).

### Paso 5 · Aplicación

Indica qué bloques condicionados de la capa general se activan en esta oferta, con la evidencia declarada. El disparador es el **hecho declarado**, no la etiqueta: una liquidación puede ser de producto nuevo, y «outlet» sin estado declarado no activa `gen.unidad-no-nueva`.

### Paso 6 · Denominación

- **Clave:** `model` = lista ordenada de los identificadores de bloque `cat.` y `esp.` del modelo (la capa general está siempre y no se lista); `application` = lista ordenada de bloques `gen.` activos.
- **Nombre:** «Categorías (alias) · especializaciones — aplicación». Los bloques de sector no se nombran. Las categorías se unen con «+», en el orden de las piezas; las especializaciones van en orden fijo: juego, uso, material, función; la aplicación lista solo los bloques condicionados activos, con un nombre breve («con variantes», «con descuento», «unidad no nueva»…).

## 4. Salida

Un fichero JSON por caso (claves en inglés; valores en español):

```json
{
  "case": "id-del-caso",
  "rulebook": "v1",
  "product": "nombre",
  "declared": [{"feature": "…", "scope": "producto|oferta|variante", "evidence": "cita breve"}],
  "composition": {
    "categories": [{"shopify": "id", "name": "…", "piece": "… o null", "entry": "aporta requisitos|clasificación objetiva", "alias": false}],
    "rejected_categories": [{"shopify": "id", "name": "…", "reason": "…"}]
  },
  "blocks": [
    {"id": "cat.…", "type": "categoría", "position": "categoría|sector", "name": "…",
     "refs": ["shopify:…@v2026-08", "google:…@2021-09-21", "amazon-ptd:…@2026-10-24"],
     "requirements": [{"id": "cat.…/01", "question": "…", "dimension": "…", "entity": "producto|variante|oferta|entrega|condiciones|vendedor",
                       "importance": "crítico|principal|complementario", "origin": "referencias|inferida", "sources": ["shopify-attr:…"],
                       "applicability": "universal o condición", "rationale": "por qué esta importancia"}]},
    {"id": "esp.…", "type": "especialización", "trigger": "característica declarada", "refs": ["…"], "requirements": ["…"]}
  ],
  "general_overrides": [{"requirement": "gen/NN", "importance": "…", "rationale": "…"}],
  "application": {"active": [{"block": "gen.…", "evidence": "…"}]},
  "features": [{"feature": "…", "role": "valor|valor que condiciona|variante|estético|promocional|beneficio reclamado|no declarado", "reason": "…"}],
  "denomination": {"key": {"model": ["cat.…", "esp.…"], "application": ["gen.…"]}, "name": "…"},
  "doubts": ["regla ambigua o dato que falta, con el paso afectado"]
}
```

Anota en `doubts` cada vez que el reglamento no te deje decidir con seguridad.
