---
id: training-catalog
title: Catálogo de entrenamiento
layer: model
status: vigente
version: 1.1
updated: 2026-10-29
sources: [INTAKE 2026-10-25-training-operation, INTAKE 2026-10-25-training-catalog-selection, INTAKE 2026-10-28-curated-training-catalog, INTAKE 2026-10-29-oq-review]
---

# Catálogo de entrenamiento

Parte del [entrenamiento del modelo de demanda](model-training.md). Define los casos de los que aprende el entrenamiento: un **catálogo curado**, no cualquier ficha que se haya evaluado ([D-158](../30-governance/decisions.md#d-158)). Las reglas que salen de él y la ejecución que las usa están en [model-training](model-training.md).

## Definición

> Otra idea que quiero que explores, y creo que es la que vamos a hacer, es mantener un catálogo de casos relevantes para entrenamiento. Cada caso evaluado podrá ser candidato a entrar al catálogo si el sistema lo considera (definir qué criterios aplican). Puedo añadir manualmente un caso que considere aunque no se haya auditado. Revisa este enfoque. Esto lo que busca es basarnos en un catálogo curado, no en cualquier ficha que hayamos auditado.
>
> — INTAKE 2026-10-28-curated-training-catalog (palabras del usuario; ortografía normalizada)

> El entrenamiento solo aprende del **catálogo de casos**, en git y con versión. Se llega a él por la selección inicial (como la de El Corte Inglés), por un caso evaluado (auditoría o `/demand-model`) que el sistema admite por unos criterios, o por un caso que el usuario añade a mano aunque no se haya auditado. Una ficha auditada no entrena por haberse auditado: es candidata.
>
> — INTAKE 2026-10-28-curated-training-catalog (revisión de Claude, aprobada por el usuario)

## Reglas e invariantes

### Filtros

> - **F1 · Validez:** captura legítima y completa (sin desafío ni error) y modelo que pasa `bin/model check`.
> - **F2 · Es una ficha de producto:** el clasificador le ha dado una clase.
> - **F3 · Sin duplicados:** la misma tienda con la misma clave que un caso ya admitido queda fuera; así se excluyen variantes y productos hermanos.
> - **F4 · Topes por clase y por tienda y clase:** de partida, 3 por clase (como en D-053) y 1 por tienda y clase. Son parámetros del usuario.
>
> — INTAKE 2026-10-28-curated-training-catalog

Todo candidato cumple los cuatro. Un caso manual cumple F1, F2 y F3 y no tiene topes. Si un manual tiene la misma tienda y clave que otro caso, se rechaza ([D-189](../30-governance/decisions.md#d-189)).

### Motivos de admisión

> - **A1 · Clase poco representada:** está por debajo de su tope.
> - **A2 · Trae algo no compilado:** un bloque generado, requisitos sin regla, inferidas, un rasgo propuesto o una categoría sin bloque.
> - **A3 · Contradice una regla compilada:** sus votos van contra una regla de importancia o relevancia; es la prueba de que la regla puede estar mal.
> - **A4 · Deja huecos de cobertura:** declara hechos sin pregunta.
> - **A5 · Tienda nueva para la clase:** alimenta también la regla de las dos tiendas de la información resolutiva.
> - **A6 · Composición nueva:** una especialización o una combinación que el catálogo no tiene.
>
> — INTAKE 2026-10-28-curated-training-catalog

Un candidato que pasa los filtros entra si aporta al menos un motivo.

- **Clase en su tope.** Solo entra lo que aporta A2 o A3, sustituyendo a un caso que no aporte nada de eso. El caso sustituido se retira con registro; no se borra.
- **Casos manuales.** Llevan origen «manual» y un motivo. Añadir un caso es dar material al entrenamiento, no revisar reglas, así que encaja en el [marco](model-training.md#marco).
- **Retirada a mano.** El usuario puede retirar a mano cualquier caso, manual o admitido por el sistema, con registro y motivo. El caso sale del catálogo sin borrarse y deja de aportar votos desde el ciclo siguiente ([D-189](../30-governance/decisions.md#d-189)).
- **Fichas de un cliente auditado.** Pueden entrar como candidatas, con las reglas de admisión de siempre. El encargo lleva una cláusula: si el cliente se opone, sus fichas no son candidatas y las ya admitidas se retiran ([D-188](../30-governance/decisions.md#d-188)).
- **Caso que viene de una auditoría.** Su ejecución cuenta en el paso 2 del [entrenamiento](model-training.md#entrenamiento) solo si se hizo con el reglamento y el catálogo vigentes ([D-194](../30-governance/decisions.md#d-194)).
- **Registro de cada caso:** origen, motivo de admisión, fecha, tienda, la clave con la que entró y la versión del reglamento.
- **Conservación.** Las fichas congeladas de los casos del catálogo se conservan: un caso cuya ficha se pierde ya no se puede reclasificar. El resto del almacén de fichas sigue siendo desechable.

## Distinciones

- **Catálogo frente a conjunto de control.** El catálogo no tiene resultados esperados: es la materia de la que se inducen las reglas. El conjunto de control (los 14 casos con resultado esperado) detecta si una versión empeora ([D-045](../30-governance/decisions.md#d-045)). Un caso manual podría pasar a control si el usuario decide lo esperado.
- **Caso evaluado frente a caso del catálogo.** Toda ficha que la ejecución evalúa es candidata; solo entrena la que el sistema admite o la que el usuario añade.
- **Curar frente a elegir fichas buenas.**

  > Si solo entran fichas completas, el clasificador nunca aprende con las pobres, que son justo las que más se auditan. Los motivos miden lo que el caso enseña, no la calidad de la ficha.
  >
  > — INTAKE 2026-10-28-curated-training-catalog

## Interpretación

> - Separa operar de aprender: el volumen de auditorías no decide el coste ni el sesgo del entrenamiento, que depende del tamaño del catálogo.
> - Resuelve que una tienda domine las reglas sin tocar la regla de mayoría: basta con limitar cuántos casos entran por tienda y clase.
> - Es reproducible: se sabe con qué casos se entrenó cada versión.
> - Es la evolución natural del catálogo de entrenamiento de D-053, que hoy es un sorteo único y pasaría a estar vivo y curado.
>
> — INTAKE 2026-10-28-curated-training-catalog (revisión de Claude)

La admisión la decide el sistema: el usuario no admite candidatos, solo añade casos manuales y retira casos.

Lecturas de Claude que el usuario ratificó ([D-189](../30-governance/decisions.md#d-189)):

- **Clase de los topes:** cada categoría de Shopify de la composición del caso. Un juego de dos piezas cuenta en las dos categorías.
- **Cuándo se admite:** al reunir los casos, en el paso 1 del [entrenamiento](model-training.md#entrenamiento). Los motivos A2 y A3 se miden contra las reglas vigentes de ese ciclo.
- **Sustitución:** con la clase en su tope, sale el caso más antiguo sin A2 ni A3. Un caso manual nunca se sustituye. Si no hay ninguno que sustituir, el candidato no entra.
- **Selección inicial y topes:** la selección de D-053 entra tal cual, fuera de los topes, que rigen para los candidatos. Aunque tiene 3 fichas por tipo de una misma tienda, no está sujeta al tope de 1 por tienda y clase.

- **Selección inicial.** La selección de El Corte Inglés ([D-053](../30-governance/decisions.md#d-053)) es la primera vía de entrada al catálogo:

  > utiliza un grupo pequeño de productos de cada categoría, pero quiero suficiente variedad de categorías para que sea de utilidad para el entrenamiento. […] sí a 3 fichas. […] empecemos con 30 para validar el sistema de entrenamiento.
  >
  > — INTAKE 2026-10-25-training-catalog-selection (palabras del usuario)

  Tiene 3 fichas por tipo de producto y 100 tipos (300 fichas), con un piloto previo de 30. El tipo es una aproximación conocida antes de capturar, y la clase la da el clasificador. Se captura sin desplazamiento, porque basta el HTML de la primera carga. El usuario ratificó las lecturas de D-053: «categoría» como tipo de producto; sorteo determinista por departamentos, una ficha por producto y reservas; exclusión de entradas, tarifas y tarjetas regalo ([D-187](../30-governance/decisions.md#d-187)).
- **Otras tiendas.** No hay otra selección inicial. Las demás tiendas llegan como candidatas (auditorías y `/demand-model`) y como casos manuales. No hace falta una relación fija con el panel del MPIR: si el MPIR vuelve, sus tiendas entran por esas mismas vías ([D-187](../30-governance/decisions.md#d-187)).

## Ejemplo mínimo

Ejemplo hipotético. Una auditoría evalúa 2.000 camisetas de una tienda. La clase Camisetas ya tiene 3 casos de otras tres tiendas, todos admitidos por A1.

- Una camiseta con un bloque generado en la ejecución (A2) entra y sustituye a uno de esos 3 (el más antiguo sin A2 ni A3). Como es el primer caso de esta tienda en la clase, el tope de 1 por tienda y clase no la frena.
- Las demás camisetas de la tienda quedan fuera por el tope de tienda y clase (F4) o por tener la misma clave que esa camiseta (F3).

## Pendiente

Ver [open-questions](../30-governance/open-questions.md):

- casos de control por vertical nueva, que se deciden al auditar la primera vertical que el control no cubra, y conexión de código de la auditoría con el entrenamiento, T-071 ([OQ-81](../30-governance/open-questions.md#b-taxonomía-de-clases-de-producto)).

## Relacionado

- [model-training](model-training.md): entrenamiento, ejecución y marco
- [demand-model](demand-model.md): clave e identidad del modelo
- [resolving-information](resolving-information.md): regla de las dos tiendas
