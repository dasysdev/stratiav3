# Reglamento operativo del modelo de demanda · v2

Procedimiento del **clasificador** en la ejecución: a partir de la ficha de un producto, decide lo que el motor no puede decidir solo (composición, especializaciones, cuestiones inferidas, aplicación) y vota la importancia; los bloques, la importancia compilada, la clave y el nombre los pone el código (`bin/model`). Condensa el canon (`docs/10-model/demand-model.md`, `study-class.md`, `model-training.md`; decisiones D-020 a D-052). Si el reglamento y el canon discrepan, prevalece el canon y la discrepancia se anota en `doubts`.

## 0. Propósito

El modelo establece **requisitos informativos**: las cuestiones que la información comercial de la oferta debe permitir resolver. Que una característica sea especialización o valor es instrumental: importa qué cuestiones entran y con qué importancia.

- **Modelo de demanda (del producto):** bloques de categoría (sector y clase) y de especialización, más los condicionados de la capa general que son del producto (elementos digitales). Su clave y su nombre no dependen de la oferta.
- **Aplicación (de la oferta):** condiciones de la capa general activas en esta oferta (variantes, unidad no nueva, descuento, cantidad limitada, precio personalizado, suscripción). Si no hay ninguna, la oferta es **estándar**. Lo que no se da en la oferta queda en gris (NA).
- **La oferta no aporta requisitos:** solo activa requisitos condicionados. Una cuestión que solo procede con una condición de la oferta (p. ej., la salud de la batería de un smartphone reacondicionado) es una cuestión de la clase condicionada a esa condición (paso 5).
- **Tú no redactas bloques del catálogo ni decides importancias.** Los bloques de categoría vienen del catálogo compilado; la importancia, de las reglas. Tú das tu **voto** (la importancia que darías con las pruebas del paso 7); el voto solo cuenta si no hay regla, y alimenta el entrenamiento.

## 1. Parámetros

| ID | Parámetro | Valor vigente | Fuente |
|---|---|---|---|
| P1 | Versiones de las referencias | Las fijadas en `references/var/pins.json` | refs |
| P2 | Eje de la clase | Shopify Standard Product Taxonomy | D-021 |
| P3 | Base de una categoría (para decidir especializaciones) | Requisitos de sus bloques y de los de sus madres (`bin/model blocks`) + propiedades y `special_feature` del PTD de Amazon | D-029, D-030, D-039 |
| P4 | Apoyo de una especialización | Estricto: la dimensión existe en algún componente | D-024 |
| P5 | Entrada de una categoría | Aporta requisitos al producto o a una pieza, o clasificación objetiva cuando tiene sentido (alias si no aporta) | D-023, D-028, D-033 |
| P6 | Capa general | Fija (parte del marco); no se vota ni se revisa. Incluye la pregunta universal de promociones (un «no» fundamentado la resuelve) | D-034, D-045, D-049 |
| P7 | Bloques de categoría | Del catálogo; si falta uno, se genera (paso 3) y queda «no compilado» | D-040, D-044, D-045 |
| P8 | Cuestiones inferidas | Permitidas, provisionales, fuera de la clave | D-036, D-041 |
| P9 | Relevancia e importancia | Reglas compiladas; tu voto con la prueba de relevancia y las de D-035 | D-035, D-045, D-050 |
| P10 | Rasgos | Vocabulario cerrado de `catalog/traits.json` | D-045 |

## 2. Herramientas

Desde `demand-engine/`:

- Ficha congelada: `bin/taxo page facts ID [palabras…]`, `bin/taxo page section ID ENCABEZADO`, `bin/taxo page grep ID REGEX`.
- Shopify: `bin/taxo shopify REGEX`; `bin/taxo category ID` (madres, hijas, mapeo a Google y atributos); `bin/taxo values REGEX`. Google: `bin/taxo google REGEX`. Amazon: `bin/taxo amazon REGEX`, `bin/taxo ptd TIPO [REGEX]`, `bin/taxo ptd TIPO --enum PROP`.
- Motor: `bin/model blocks CAT_ID…` (capa general y bloques de la clase con sus requisitos y rasgos); `bin/blocks plan CAT_ID [--ptd CAT_ID=PTD[:NODO]]`; `bin/model register FICHERO` o `bin/model register --empty CAT_ID`; `bin/model check SALIDA.json`.

En Shopify en español hay nombres repetidos y traducciones engañosas: decide siempre por identificador, nombre inglés y atributos.

## 3. Procedimiento

### Paso 1 · Leer la ficha

Extrae lo **declarado** en el texto y en los datos estructurados: tipo de producto, piezas, materiales, construcción, usos, funciones, medidas y variantes, condiciones de la oferta (estado, precio y precio de referencia, disponibilidad y cantidad, envío, devoluciones, garantía) y beneficios que reclama. Cita la evidencia. No cuenta como declarado lo que solo aparece en nombres de ficheros, iconos o atributos HTML, ni las afirmaciones genéricas de la tienda. No completes hechos ausentes con conjeturas ni con conocimiento externo.

### Paso 2 · Composición de la clase

1. Busca la categoría de Shopify del producto. Si es un **juego** con piezas de categorías distintas, la de **cada pieza**: la clase es la composición de esas categorías, no su ancestro común.
2. Una categoría **entra** si aporta requisitos al producto o a una pieza, o si el producto entra en ella por **clasificación objetiva** cuando tiene sentido para nombrar lo que es; si entra sin aportar requisitos, es **alias** (nombre, no modelo).
3. **No entra** si traería requisitos que no aplican, si es una entrada duplicada de otra para el mismo tipo de producto, si el uso que la define depende solo de una variante o si solo hay proximidad temática.
4. Prefiere la categoría más específica cuya definición cumple el producto.

### Paso 3 · Bloques

1. Ejecuta `bin/model blocks` con las categorías de la composición (no los alias). Verás la capa general y, para cada categoría y sus madres, su bloque con los requisitos (`id [rasgo] pregunta`).
2. Si sale **«FALTA EL BLOQUE»** para alguna categoría, genéralo:
   - Busca el PTD de Amazon que corresponde a la categoría (`bin/taxo amazon`, `bin/taxo ptd`); si ninguno encaja, sin PTD.
   - `bin/blocks plan CAT_ID --ptd CAT_ID=PTD:NODO` y redacta solo los bloques que faltan siguiendo `catalog/DRAFTING.md` (cada requisito con `trait` y `vote`). Escríbelo en la carpeta de la ejecución y regístralo con `bin/model register FICHERO`. Si la categoría no tiene requisitos propios, `bin/model register --empty CAT_ID`.
   - Si `register` responde que la categoría ya tiene bloque (en un lote, otro caso lo generó mientras redactabas), no lo redactes de nuevo: vuelve a `bin/model blocks` y vota sus requisitos. `--replace` sirve solo para corregir un bloque que registraste tú en este caso.
   - Anota en `runtime_blocks` lo que generes.

### Paso 4 · Especializaciones

Cada característica declarada que la clase no recoge como categoría:

| Caso | Tratamiento |
|---|---|
| Variante (medida, talla, color elegido) | Activa `gen.variantes`; no es especialización |
| Valor estético, etiqueta promocional, nombre comercial | No aporta requisitos |
| Beneficio reclamado | No es especialización, salvo que las referencias tengan un tipo de producto definido por él. El material reciclado no es beneficio |
| Condición o situación de la oferta (outlet, liquidación, exposición, reacondicionado, descuento, última unidad…) | Activa bloques condicionados de la capa general (paso 6); nunca es especialización. Si trae cuestiones que nada prevé, son inferidas condicionadas (paso 5) |
| Revela una dimensión que **tienen todos** los productos de la clase | No forma bloque: su cuestión ya está en un bloque de categoría (el valor declarado es la respuesta) o es una cuestión inferida (paso 5) |
| Trae cuestiones que **no se aplican** a los demás productos de la clase | Candidata a **especialización** |

Una candidata es especialización si cumple las cinco condiciones: (1) del producto (no de la oferta), declarada y estable; (2) trae cuestiones propias, concretas y neutrales, que no salen de la base (P3) ni de la capa general (si solo cambia valores esperados o activa cuestiones ya previstas, es valor que condiciona); (3) relevantes para evaluar la clase; (4) con apoyo (P4); (5) fijada en el nivel más general cuyos miembros comparten sus cuestiones. Un conjunto de piezas de categorías distintas es `esp.juego` (qué piezas, cuántas y en qué medidas).

Cada especialización: `id` (`esp.<nombre>`, español, minúsculas y guiones), `name` breve para el nombre del modelo, `order` (juego, uso, material o función), `trigger`, `support` (fuentes) y sus requisitos (pregunta, dimensión, entidad, `trait`, `vote`, fuentes, aplicabilidad, fundamento).

### Paso 5 · Cuestiones inferidas

Cuestiones que afectan a **todos** los productos de la clase y que ni la capa general ni los bloques del paso 3 recogen: neutrales, justificadas, sin duplicar la base. Pueden estar **condicionadas por un hecho de la oferta**: si una condición de la oferta (unidad no nueva, por ejemplo) trae una cuestión que nada prevé, es una inferida de la clase con `applicability` «si la unidad no es nueva». Indica el bloque de categoría al que pertenecerían (`block`), su `trait`, su `applicability` y tu `vote`. Son provisionales y quedan fuera de la clave.

### Paso 6 · Aplicación

Bloques condicionados de la capa general que se activan, con la evidencia declarada. El disparador es el **hecho declarado**, no la etiqueta: una liquidación puede ser de producto nuevo, y «outlet» sin estado declarado no activa `gen.unidad-no-nueva`. Lista aquí también `gen.elementos-digitales` si el producto los tiene: el motor lo lleva al modelo, porque es del producto. Sin condiciones activas, la lista va vacía (oferta estándar). La pregunta universal de promociones (`gen/16`) recoge en `answers` cualquier promoción declarada, o el «no» si la ficha lo dice.

### Paso 7 · Votos

Para **cada requisito de los bloques de categoría** del paso 3 (también los marcados «excluido en esta clase»), y para los de tus especializaciones e inferidas, da tu voto **en esta clase**. Primero la relevancia; después, si es relevante, la importancia:

- **no relevante** si no informa sobre nada que importe para evaluar o comparar ofertas de esta clase (p. ej., el color de un pienso, heredado del sector). No es lo mismo que «no aplica a este producto» (el número de hilos en un tejido que no es de calada): eso es relevante en la clase y la auditoría lo pone en gris. La duda no excluye: si dudas, es relevante. Nunca votes «no relevante» la medida que fija lo vendido ni un requisito de origen normativo;

- **crítico** si, sin resolverlo, la oferta deja de ser evaluable (no se sabe qué se vende, cuánto cuesta o si se puede adquirir);
- **principal** si es uno de los criterios con los que se comparan y eligen ofertas de la clase;
- **complementario** si es relevante sin ser indispensable ni central.

La duda no baja la importancia. Los críticos son pocos. No votes la capa general.

### Paso 8 · Cobertura

Para cada hecho declarado del paso 1, indica en `answers` el identificador del requisito del modelo que lo pregunta (capa general, categoría, especialización o `inf/NN` de tus inferidas, en su orden), o `null` si ninguno lo pregunta. Marca su `role`: valor, valor que condiciona, variante, condición de oferta, estético, promocional o beneficio reclamado.

### Paso 9 · Comprobar

Escribe la salida y ejecuta `bin/model check SALIDA.json`; corrige lo que señale. No ejecutes `bin/model assemble`: lo hace el orquestador.

## 4. Salida

Un fichero JSON (claves en inglés; valores en español):

```json
{
  "case": "id-del-caso", "rulebook": "v2", "product": "nombre", "url": "…",
  "declared": [{"feature": "…", "scope": "producto|oferta|variante", "role": "valor|valor que condiciona|variante|condición de oferta|estético|promocional|beneficio reclamado",
                "evidence": "cita breve", "answers": "cat.…/NN | gen/NN | esp.…/NN | inf/NN | null"}],
  "composition": {
    "categories": [{"shopify": "id", "name": "…", "piece": "… o null", "entry": "aporta requisitos|clasificación objetiva", "alias": false}],
    "rejected_categories": [{"shopify": "id", "name": "…", "reason": "…"}]
  },
  "runtime_blocks": ["cat.… generado en esta ejecución"],
  "specializations": [{"id": "esp.…", "name": "…", "order": "juego|uso|material|función", "trigger": "característica declarada",
                       "support": ["shopify-attr:…"],
                       "requirements": [{"id": "esp.…/01", "question": "…", "dimension": "…", "entity": "producto|variante|oferta|entrega|condiciones|vendedor",
                                         "trait": "…", "vote": "crítico|principal|complementario", "sources": [], "applicability": "…", "rationale": "…"}]}],
  "inferred": [{"id": "inf/01", "block": "cat.…", "question": "…", "dimension": "…", "entity": "…", "trait": "…", "applicability": "universal o condición (p. ej., si la unidad no es nueva)", "vote": "…", "rationale": "…"}],
  "application": [{"block": "gen.…", "evidence": "…"}],
  "votes": {"cat.…/01": "principal", "cat.…/02": "no relevante"},
  "features": [{"feature": "…", "role": "…", "reason": "…"}],
  "doubts": ["regla ambigua o dato que falta, con el paso afectado"]
}
```

Anota en `doubts` cada vez que el reglamento no te deje decidir con seguridad.
