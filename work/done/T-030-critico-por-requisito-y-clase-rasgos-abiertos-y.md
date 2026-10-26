---
id: T-030
title: Crítico por requisito y clase, rasgos abiertos y reglamento v3
status: hecha
depends: T-028
milestone: codigo
created: 2026-10-26
closed: 2026-10-26
---

## Objetivo

Aplicar al motor de demanda las decisiones de la revisión del ciclo de reglas 4 (D-055, D-056, D-057) antes de escalar a 300 fichas

## Criterios de aceptación

- [x] bin/train induce: excepciones por requisito y clase en todos los niveles (D-058, D-055): regla imp:<requisito>@<clase> por mayoría de votos en la clase con el catálogo como voto de partida, empate: se queda la regla del rasgo, subida por el árbol con el mínimo estructural; cualquier propiedad puede ser crítica por su excepción; la regla por rasgo no da crítico; la medida que fija sigue siempre crítica y las excepciones no bajan lo que fija el marco; la resolución del modelo aplica antes la excepción; la coherencia no cuenta las excepciones; nueva métrica de aceptación, coherencia por requisito (97 con las reglas 4); con pruebas
- [x] Vocabulario de rasgos abierto (D-056): catalog/traits.json con los rasgos de partida y los propuestos (nombre y definición); voto de rasgo por requisito en la salida del clasificador y en bin/model check; train index asigna a cada requisito el rasgo más votado (empate: el actual), el índice por fuentes solo da el rasgo de partida (una fuente con requisitos de rasgos distintos sale del índice) y un rasgo propuesto entra cuando gana; con pruebas
- [x] Reglamento v3 y catalog/DRAFTING.md: voto y propuesta de rasgos, crítico por requisito, paso 2 con D-057 (hoja más específica como categoría, hermana que nombra otra característica como alias), paso 6 con la unidad de exposición y las cuatro reglas de formulación de D-060 (sin condiciones sobre la existencia de la información; condición sobre un hecho → requisito condicionado; división cuando las partes tomarían otro rasgo u otra importancia; cada componente con fuente o como inferida); las reglas 1 a 3 también para las especializaciones y las inferidas que redacta el clasificador
- [x] Información resolutiva (D-062, D-063): campo de cada requisito (aportaciones resolutivas con componente, origen y respaldo, y tiendas en que se observan; D-064) en el formato de catalog/DRAFTING.md y en el modelo (json y md); en la salida del clasificador, la aportación de cada hecho declarado o una aportación nueva propuesta con su componente, comprobado por bin/model check; bin/train extrae títulos y descripciones de las referencias (propiedades y subpropiedades de Amazon, atributos y valores de Shopify), acepta una aportación observada cuando aparece en dos tiendas distintas y aporta a un componente, no retira ninguna por no observarse e informa de las propuestas, aceptadas, rechazadas y nunca observadas; con pruebas
- [x] Informe agregado con las excepciones por requisito y clase (también las de crítico), los rasgos propuestos y aprobados y los votos que contradicen el marco (capa general, medida que fija, mínimos de las medidas)
- [x] induce y compile sobre eci-a, eci-b, v4-a y v4-b con el mecanismo nuevo, sin empeorar ninguna métrica, e informe en training/reports/; bin/run dev test en verde

## Resultado

Excepciones por requisito y clase (crítico incluido), rasgos abiertos, información resolutiva, reglamento v3 y DRAFTING con D-060; reglas 5 aceptadas (coherencia por requisito 130 → 17)

## Notas

- 2026-10-26 Ampliada con D-058 (2026-10-26): excepciones de importancia por requisito y clase en todos los niveles; cualquier propiedad puede ser crítica si sus votos lo dicen (el color en calzado y sofás, el abrigo de las pantuflas y el mecanismo del sofá cama son los casos del piloto); métrica coherencia por requisito.
- 2026-10-26 Revisión de D-058: el docstring de demand_engine/demand/train.py aún describe la regla global de identidad y contenido; actualizarlo con el código. I-24 («críticos pocos» sin métrica) propone que el informe dé, por clase, cuántos requisitos son críticos y cuántos cambian; pendiente de decisión del usuario, no se implementa sin ella.
- 2026-10-26 I-24 resuelta por D-059 (no aplica): «críticos pocos» sale del marco; no hay que contar ni limitar los críticos en el informe.
- 2026-10-26 Ampliada con D-060 (2026-10-26): reglas de formulación de las cuestiones en el reglamento v3 y DRAFTING.md. La nueva redacción del catálogo con ellas va en una tarea aparte, que T-029 espera.
- 2026-10-26 D-059: retirar del reglamento (paso 7, «Los críticos son pocos») y de catalog/DRAFTING.md («Los críticos son raros fuera de la capa general») las frases que sesgan los votos hacia pocos críticos.
- 2026-10-26 Ampliada con D-061 (2026-10-26): campo forma de la respuesta en el formato, el clasificador, el modelo y bin/model check.
- 2026-10-26 D-061 sustituida por D-062 (información resolutiva): se retira el criterio de la forma de la respuesta; el campo espera al diseño de sus reglas (OQ-54).
- 2026-10-26 Ampliada con D-063 (2026-10-26): información resolutiva en el formato, el clasificador, bin/model check y bin/train (extracción de referencias, aceptación en dos tiendas, informe). El usuario quiere que la tanda de control con los 14 casos la mida también.
- 2026-10-26 Coherencia por requisito: solo requisitos de categoría, porque los ids de las inferidas (inf/NN) no son estables entre casos; con las reglas 4 da 83/312 en el piloto (el 97 registrado incluía inferidas). Excepción: la importancia del catálogo cuenta como voto de partida en cada clase con votos; un empate deja la regla del rasgo. Ciclo de reglas 5 (eci-a, eci-b, v4-a, v4-b): importancia aceptada (coherencia por requisito 130 → 17; de los modelos 5 → 2; ninguna peor), 104 excepciones (10 de crítico, entre ellas el color en calzado y sofás, el abrigo de las pantuflas y el mecanismo del sofá cama como principal); relevancia descartada (sin mejora; siguen las de la v4); votos que coinciden con la regla 758 → 942/1050. Algunas reglas por rasgo cambian porque la v4 se indujo con v3-a/b y esta con v4-a/b. Las salidas v2 no traen votos de rasgo ni aportaciones: rasgos e información resolutiva se medirán en T-032. Informe: demand-engine/training/reports/2026-10-26-v5-report.md. Reglamento v2 archivado en classifier/rulebook-v2.md.
