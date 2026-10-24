# Prominencia informativa como modificador de calidad

**Propuesta metodológica provisional — versión simplificada**

## Objetivo

Incorporar la **prominencia de la información** a la valoración de calidad sin confundir la ubicación de las evidencias con la capacidad de resolver un requisito informativo (RI).

## Indicadores y función

- **IR (0–10):** mide la capacidad de resolución del RI mediante los criterios de aceptación. No se modifica.
- **Normalización binaria del IR (0/1):** distingue resolución suficiente e insuficiente; la regla de normalización está pendiente de definir.
- **IP (0–100 %):** expresa el porcentaje de componentes informativos efectivamente resueltos que cuentan con soporte suficiente en ubicaciones prominentes.
- **Calidad ajustada:** utiliza el IP como modificador secundario, sin cambiar el IR original ni su clasificación binaria.

## Clasificación binaria de prominencia (HTML)

| Valor | Condición | Ubicaciones orientativas |
|---|---|---|
| **1 — Prominente** | La información que sustenta el componente aparece en una zona de alta prominencia. | `<title>` (metatítulo), metadescripción, H1, descripción inicial o síntesis destacada. |
| **0 — No prominente** | No existe soporte suficiente para ese componente en una de esas zonas. | Resto del contenido, incluidas descripciones extensas, tablas, especificaciones y secciones secundarias. |

La clasificación se aplica **a cada componente informativo**, no al RI completo. Una simple mención en una zona prominente no basta: debe aportar el contenido necesario para sustentar el componente.

La delimitación concreta de las zonas prominentes es provisional; no presupone que los contenidos no prominentes sean de menor suficiencia o precisión. Para Schema.org y catálogos distribuidos habrá que definir, si procede, reglas específicas.

## Cálculo del IP

**IP = 100 × (C / N)**

- **C:** número de componentes informativos efectivamente resueltos con soporte suficiente en una ubicación prominente.
- **N:** número total de componentes informativos efectivamente resueltos considerados en la evaluación.

Cada componente se cuenta una sola vez, aunque aparezca repetido. Por ejemplo, si de cuatro componentes resueltos dos están sustentados en zonas prominentes, **IP = 50 %**.

Si **N = 0**, el IP es **no aplicable**. No se fragmenta artificialmente la información para aumentar el número de componentes.

## Integración en la valoración

El IP **diferencia la calidad dentro de un mismo estado binario de resolución**, con influencia limitada.

Una mayor prominencia no transforma un RI insuficientemente resuelto en suficiente ni compensa carencias informativas.

Se registran por separado **IR, estado binario, IP y calidad ajustada**.

**Pendiente de validar:** ubicación exacta de las zonas prominentes, identificación de componentes y rutas alternativas de resolución, fórmula y peso del modificador, así como posibles duplicidades con aspectos ya recogidos por los criterios de aceptación.