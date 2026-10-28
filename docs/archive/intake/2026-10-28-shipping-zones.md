# Envío y plazos por zona de España: un conjunto explícito valorado por los AC

Decisión del usuario del 2026-10-28, tomada en la sesión de T-076 y recogida por Claude el mismo día.

## Petición del usuario

«Quiero expandir los requisitos informativos de envío para tratar de forma específica las zonas de envío en España: península, canarias, baleares, ceuta y melilla. Estudia cómo abordarlo. Creo que son requisitos específicos, tanto si se envía como si no.»

Primera propuesta de Claude: requisitos universales por zona («¿Se envía a Canarias y cuánto cuesta?»), con el plazo y los impuestos condicionados a que se envíe.

Respuesta del usuario: «Tanta especificidad me hace dudar si debería ser un requisito general único de envío y modular el cumplimiento a través de los AC. ¿Hay otras cuestiones sobre los plazos de entrega que podrían funcionar similar? No puedo crear un requisito para cada tipo; ¿es más bien si se puede determinar por precisión? Quizás es una cuestión de reformular la pregunta. Estúdiamelo.»

## Análisis de Claude

- **Partes de la cuestión frente a unidades de un conjunto.**
  - Las partes son necesidades distintas (el precio y el coste del envío; el plazo y el coste de una devolución). Las divide la regla 3 de D-060 (ampliada en la capa general por D-065).
  - Las unidades de un conjunto son la misma necesidad repetida sobre varios destinos, modalidades o variantes. No son partes. El canon ya las trata así: «¿Qué variantes están disponibles?» es un solo requisito, y en el ejemplo mínimo de los AC la falta de una talla es Concreción 1 y Aplicabilidad 1. La RI-02 pide fijar «conjunto, alcance y condiciones» y la GSC-09 examina la satisfacción mixta por unidades, sin porcentaje.
- **Las zonas de España son unidades de un conjunto.** Lo que falta es que la pregunta lo declare: hoy «¿Cuánto cuesta el envío a España?» trata España como un solo destino, y «4,95 € a Península» lo resuelve entero.
- **Cada AC recoge un fallo distinto**, no solo la Precisión (ejemplos hipotéticos):

  | Lo publicado | AC | Por qué |
  |---|---|---|
  | Solo «Envío a Península 4,95 €» | Concreción | Cubre una zona de cuatro; las otras no son un «no» (invariante 11). |
  | «Envío 4,95 €» sin zona | Aplicabilidad | No dice a qué zonas se atribuye; no se extiende a Canarias. |
  | «Envío nacional gratis» | Precisión, si «nacional» admite dos lecturas materiales (toda España / solo Península): a calibrar | |
  | «Envíos a toda España 4,95 €» | Concreción 2 en el coste | Derivación admitida: «toda España» incluye las cuatro zonas. |
  | Ficha «gratis a toda España» y página de envíos que excluye Canarias | Fiabilidad | Contradicción dentro del ámbito. |
  | «No enviamos a Canarias, Ceuta ni Melilla» y tarifas de Península y Baleares | Concreción 2 | El «no» resuelve (invariante 13). |

- **Los plazos de entrega siguen el mismo patrón.** Varían por destino, por modalidad (estándar, exprés, recogida), por variante o disponibilidad (en stock o bajo pedido) y por el momento del pedido (hora límite, fines de semana, temporada): todo son unidades del mismo conjunto. La Precisión encaja sobre todo aquí: «envío en 24 h» dice cuándo sale, no cuándo llega; días hábiles o naturales; desde cuándo cuenta; «24/48 h» o «envío inmediato» sin más.
- **Lo que se pierde:**
  - **Severidad:** con requisitos por zona, el silencio sobre Canarias daba disponibilidad 0 → IR 0; ahora es Concreción 1. Es coherente con las variantes, pero un hueco total de una zona pesa menos.
  - El resultado por zona no es una nota: queda en la matriz componente ↔ soporte del registro de Concreción, y el informe puede listar «Canarias: sin información».
  - La frontera 0/1 de Concreción (una zona cubierta de cuatro) depende de la prueba de materialidad (OQ-22).
  - Hace falta precisar que las unidades de un conjunto no son partes: sin ello, la regla 3 ampliada de D-065 empuja a partir por zona.
- **Los impuestos de Canarias, Ceuta y Melilla sí son otra parte:** impuestos y aduana no son transporte. Canarias está fuera del territorio del IVA; Ceuta y Melilla, fuera del IVA y del territorio aduanero de la UE (Ley 37/1992, art. 3; Directiva 2006/112/CE, art. 6; Reglamento (UE) 952/2013, art. 4). Allí el precio con IVA no es el que se paga. El art. 97.1.e TRLGDCU exige el precio total «incluidos los impuestos y tasas» y «cualquier otro gasto».

## Propuestas de Claude

1. **Un requisito por necesidad, con el conjunto explícito, valorado por los AC.** Las unidades de un conjunto (destinos, modalidades de entrega, variantes, momentos del pedido) no son partes de la cuestión y no se divide por ellas. Las cubre la **Concreción** (cobertura de las unidades), la **Aplicabilidad** (atribución de cada valor a su unidad) y la **Precisión** (significado de lo expresado: «nacional», «24/48 h»). Precisa la regla 3 de D-060 y D-065.
2. **`gen/25` se reformula:** «¿A qué zonas de España se envía y cuánto cuesta el envío a cada una?». El conjunto, en la descripción: Península, Baleares, Canarias, y Ceuta y Melilla. Componentes por zona en la información resolutiva. Una pista de Aplicabilidad del requisito: un coste vale solo para la zona a la que se atribuye.
3. **Requisito condicionado nuevo**, si se envía a Canarias, Ceuta o Melilla: «¿Qué impuestos y gastos de aduana asume el comprador en los envíos a Canarias, Ceuta y Melilla?». Origen normativa (97.1.e), con apoyo en Ley 37/1992, art. 3, Directiva 2006/112/CE, art. 6, y Reglamento (UE) 952/2013, art. 4. Importancia: crítico, por el mismo argumento con el que D-038 hizo crítico el envío: forma el precio total.
4. **`gen/08` se reformula:** «¿En qué plazo se entrega, según la zona y la modalidad de entrega?». Conjunto: destino, modalidad, variante o disponibilidad y momento del pedido. Pistas de Precisión: envío no es entrega; días hábiles o naturales; desde cuándo cuenta.
5. **Candidatos del mismo criterio:** `gen/26` (coste de devolver desde las islas) y `gen/09` (recogida solo en la Península), sin crear requisitos.

Severidad asumida: un hueco de zona es Concreción parcial, no IR 0; la materialidad, en OQ-22.

## Decisión del usuario

Claude preguntó: (1) ¿un requisito con el conjunto explícito y los AC, o requisitos por zona?; (2) impuestos y aduana: ¿requisito condicionado propio o componente de `gen/25`?; (3) ¿el mismo criterio de conjunto en `gen/08` (destino, modalidad y variante), con `gen/26` y `gen/09` como siguientes candidatos?

Usuario: «todo si».
