# Reglas de la revisión de los casos de control de PAA

Decisiones del usuario del 2026-10-27, al revisar la hoja de los casos de control de PAA (T-042, AC6, pasos 2 a 4). Recogidas en las notas de T-042 y T-052 y depositadas el 2026-10-28 (T-052).

## Paso 2 · Productos vecinos

> Preguntas sobre otro producto (la categoría madre en general, como «calzado» o «zapatos», o un hermano, como almohadas o zapatillas deportivas) quedan FUERA siempre. El perímetro va antes de la lectura sobre la oferta, que solo decide si una pregunta sobre el producto de la clase pide un hecho declarable. Un vecino nunca apoya requisitos de la clase (invariante 10), y su presencia es señal para las semillas (D-114).

Efecto en los casos: en pantuflas salen N1 (afecciones del pie), el criterio salud-del-pie y las tres aportaciones de cuero; en botas sale N1 («¿cede el corte?», apoyado solo en «¿Se estira el calzado de cuero?»). Cojines, sin cambios: las cervicales son de otro producto (almohadas).

## Paso 3 · Moda o tendencia

> La moda o tendencia NUNCA genera («¿qué X se llevan?», «¿qué X están de moda?»): «estar de moda» depende del mercado y del momento (C2/C4), un caso de la excepción de D-110.

Efecto: sale el candidato de estilo decorativo de sofás cama; botas, pantuflas y sofás quedan como «no genera».

## Paso 4 · Popularidad, preferencia general y alternativa de producto

> - La popularidad («la más vendida») no genera (reputación, C4; invariante 14).
> - La preferencia general («¿cuál es el mejor sofá cama?») es un criterio intermedio (D-104), cubierto y descompuesto en las prestaciones, como «calidad» en sábanas; no es «no genera».
> - La alternativa de producto («¿sofá cama o cama abatible?») no genera (C3).

Lo esperado de cada clase queda en `demand-engine/cases/paa/<conjunto>.json`.
