# Reglamento operativo de la clase de estudio · v0

Procedimiento para componer, a partir de la ficha de un producto, la **clase de estudio** que determina sus requisitos informativos. Condensa el canon (`docs/10-model/demand-model.md`, sección «Clase de estudio», decisiones D-020 a D-032). Si el reglamento y el canon discrepan, prevalece el canon y la discrepancia se anota en el informe del experimento.

## 0. Propósito

La clase de estudio sirve para establecer **requisitos informativos**: las cuestiones que la información comercial del producto debe permitir resolver. Ese es el criterio que manda. Que algo sea «especialización» o «valor» es instrumental: dos clasificaciones que producen las mismas cuestiones son equivalentes (D-032).

Clase de estudio = **clase general** (una o varias categorías de Shopify) + **especializaciones** pertinentes. Se busca la especificidad informativa necesaria, no el mayor número de subclases.

## 1. Parámetros

Son las opciones de lectura que fija el canon. Un experimento puede variarlas; el valor vigente es el de la tabla.

| ID | Parámetro | Valor vigente | Fuente |
|---|---|---|---|
| P1 | Versiones de las referencias | Las fijadas en `references/var/pins.json` | refs |
| P2 | Eje de la clase general | Shopify Standard Product Taxonomy | D-021 |
| P3 | Base de una categoría de Shopify | Atributos propios + los de todas sus ascendientes | D-029 |
| P4 | Base en Amazon | Propiedades del PTD + valores de `special_feature` | D-030 |
| P5 | Condición 4 (apoyo) | Estricta: la dimensión existe en algún componente; lo afín solo es complementario | D-024 |
| P6 | Entrada de una categoría | Aporta requisitos al producto o a una pieza, o clasificación objetiva cuando tiene sentido | D-023, D-028, D-032 |
| P7 | Características de la oferta | Pueden ser especialización (outlet, exposición, reacondicionado) | D-027 |
| P8 | Beneficios reclamados | No son especialización, salvo tipo de producto definido por ellos; el material reciclado no es beneficio | D-025, D-031 |
| P9 | Nivel de la especialización | El más general cuyos miembros comparten las cuestiones | D-022 |

## 2. Herramientas

Todo con `demand-engine/bin/taxo` (ver `taxo --help`):

- Ficha: `taxo page facts ID [palabras…]`, `taxo page section ID ENCABEZADO`, `taxo page grep ID REGEX`.
- Shopify: `taxo shopify REGEX` (buscar), `taxo category ID` (madres, hijas, mapeo oficial a Google y **base** con atributos propios y heredados), `taxo values REGEX` (qué atributos tienen un valor y en cuántas categorías).
- Google: `taxo google REGEX`. El mapeo oficial Shopify → Google sale en `taxo category`.
- Amazon: `taxo amazon REGEX` (nodos con su PTD), `taxo ptd TIPO [REGEX]` y `taxo ptd TIPO --enum PROP` (valores completos, p. ej. `special_feature`).

En Shopify en español hay nombres repetidos (dos categorías distintas con la misma etiqueta) y traducciones engañosas: decide siempre por identificador, nombre inglés y atributos.

## 3. Procedimiento

### Paso 1 · Leer la ficha

- Extrae lo **declarado**: tipo de producto, piezas que incluye, materiales, construcción, usos, funciones, medidas y variantes, condiciones de la oferta, beneficios que reclama. Cita la evidencia (texto breve de la página).
- No completes hechos ausentes con conjeturas ni con conocimiento externo. Lo que el nombre comercial sugiere pero la ficha no declara queda «no declarado».
- Separa lo que es del **producto**, de la **oferta** (estado de la unidad, garantía, descuento) y de la **variante** (medida, talla, color elegido).

### Paso 2 · Clase general

1. Busca en Shopify la categoría del producto. Si el producto es un **juego** con piezas de categorías distintas, busca la categoría de **cada pieza**: la clase general es la composición de esas categorías, no su ancestro común.
2. Una categoría candidata **entra** si:
   - **aporta requisitos** al producto o a alguna de sus piezas (en un juego, cada pieza es una entidad; una categoría aporta a su pieza aunque sus requisitos sean del mismo tipo que los de otra pieza); o
   - el producto entra en ella por **clasificación objetiva**, aunque no aporte requisitos, **cuando tiene sentido** para nombrar lo que el producto es (p. ej., hipotético: un portátil que es objetivamente también «ultraligero», si existiera esa categoría hermana).
3. Una categoría **no entra**:
   - si traería requisitos que no aplican al producto (lee la descripción de sus atributos distintivos: si están definidos para otro tipo de producto, no aplican);
   - si es una entrada duplicada de otra para el mismo tipo de producto (se elige una);
   - si el uso que la define depende solo de una variante (p. ej., solo una de las medidas se presenta para ese uso);
   - si solo hay proximidad temática.
4. Prefiere la categoría más específica cuya definición cumple el producto. Su base incluye la de las madres (P3), así que no hace falta añadir las madres como componentes.
5. Contrasta cada componente con Google (mapeo oficial; anota la relación: equivalente, más amplia…) y con Amazon (nodo y PTD). Google y Amazon no cambian el eje: lo confirman o aportan base y apoyo.
6. Lo que Shopify distingue como categoría va en la clase general, no como especialización: si una característica declarada define una categoría hija que el producto cumple, el producto va en esa hija.

### Paso 3 · Base de cada componente

- Shopify: `taxo category ID` (P3).
- Amazon: el PTD del nodo que corresponde al producto: propiedades y valores de `special_feature` (P4). Si el PTD del nodo general no tiene `special_feature`, usa el PTD de los nodos hijos que corresponden al producto y anótalo.
- La base son las dimensiones de la clase general: sus cuestiones ya están en el modelo sin necesidad de especializaciones.

### Paso 4 · Candidatas a especialización

Cada característica declarada que la clase general no recoge como categoría es candidata. Para cada una:

**4.1 Exclusiones (no son especialización):**

| Caso | Tratamiento |
|---|---|
| Variante: medida, talla, color elegido | `variante` |
| Valor estético: color, estampado, diseño, adornos | `estético` |
| Etiqueta promocional: descuento, «alta calidad», «novedad» | `promocional` |
| Beneficio reclamado: un efecto que el producto dice producir («favorece…», «mejora…», «más…», «sostenible») | `beneficio reclamado` (su fundamento se evalúa en la auditoría). Excepción: si las referencias tienen un tipo de producto definido por él. |
| Solo en el nombre comercial, o sugerido pero no declarado | `no declarado` |
| Partes del producto que la categoría ya modela con sus propios atributos | `cubierta por la categoría` (no son piezas de un juego) |
| La unidad de venta normal de la clase | no es «juego» |

El material reciclado **no** es beneficio: es composición verificable (pasa a 4.2).

**4.2 Las cinco condiciones:**

1. **Es del producto o de la oferta, y estable:** un uso, material, función, construcción u otra característica declarada (la lista no es cerrada).
2. **Efecto comparativo:** añade una cuestión, cambia el alcance o la desagregación de una cuestión, cambia la aplicabilidad o cambia la importancia relativa. Exprésalo como cuestiones concretas y neutrales.
   - **Regla de las cuestiones propias.** Si **todo** producto de la clase tiene esa dimensión (p. ej., el material, la forma, la construcción o la etapa de uso), el valor solo es especialización si trae **cuestiones propias que no salen de la base** (paso 3, incluidos los valores de `special_feature`). Si solo cambia los valores esperados, o solo hace que algunas cuestiones dejen de aplicarse, es un **valor que condiciona**.
   - Ejemplo hipotético: en una clase cuya base ya tiene el tipo de pantalla y sus cuestiones, «OLED» es valor; en una clase cuya base no tiene ninguna cuestión de pantalla, una pantalla declarada trae cuestiones propias. La misma característica puede ser valor en una clase y especialización en otra: depende de la base.
3. **Relevancia:** las cuestiones importan para evaluar la clase, no a un comprador concreto.
4. **Apoyo (P5):** la dimensión existe en algún componente: atributos de la base de Shopify, nodo o PTD de Amazon (incluido `special_feature`) o categoría de Google. El valor se ancla con una relación tipada. El apoyo en una categoría afín solo es complementario. **Si falla**, la distinción no se pierde: sus cuestiones quedan como **requisitos condicionados** de la clase general.
5. **Nivel (P9):** fija la especialización en el nivel más general cuyos miembros comparten las cuestiones que introduce, y registra el valor concreto del producto como valor de esa dimensión (p. ej., hipotético: «suela de goma» como nivel y un compuesto comercial concreto como valor). Baja de nivel solo si el inferior añade o modifica cuestiones.

**4.3 Casos especiales:**

- **Juego:** un conjunto de piezas de categorías distintas es especialización «juego». Aporta los requisitos del conjunto: qué piezas incluye, cuántas y en qué medidas.
- **Oferta (P7):** outlet, exposición o reacondicionado es especialización de oferta si la ficha declara el estado de la unidad. Su apoyo está en el grupo de oferta del PTD (`condition_type`, `condition_note`).
- Una misma característica puede cumplir varias especializaciones a la vez: pueden ser facetas concurrentes.

### Paso 5 · Requisitos que produce

Para cada especialización y cada requisito condicionado, escribe las cuestiones que aporta. Revisa que ninguna cuestión esté duplicada entre componentes y que ningún componente traiga cuestiones que no aplican.

## 4. Salida

Un fichero JSON por caso, con esta forma (claves en inglés; valores en español):

```json
{
  "case": "id-del-caso",
  "rulebook": "v0",
  "product": "nombre del producto",
  "declared": [{"feature": "…", "scope": "producto|oferta|variante", "evidence": "cita breve"}],
  "pieces": ["…"],
  "components": [{"shopify": "id", "name": "…", "piece": "… o null", "entry": "aporta requisitos|clasificación objetiva",
                  "google": "id y relación", "amazon": "nodo y PTD"}],
  "rejected_categories": [{"shopify": "id", "name": "…", "reason": "…"}],
  "specializations": [{"name": "…", "kind": "producto|oferta", "dimension": "…", "value": "… o null",
                       "questions": ["…"], "support": ["…"]}],
  "features": [{"feature": "…", "role": "valor|valor que condiciona|variante|estético|promocional|beneficio reclamado|requisito condicionado|no declarado|cubierta por la categoría",
                "reason": "…", "questions": ["… (solo si condiciona o es requisito condicionado)"]}],
  "class": "Categoría + Categoría → especialización + especialización",
  "doubts": ["regla ambigua o dato que falta, con el paso afectado"]
}
```

Anota en `doubts` cada vez que el reglamento no te deje decidir con seguridad: es la información más útil del experimento.
