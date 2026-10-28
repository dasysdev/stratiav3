---
id: T-050
title: Piloto de pistas de valoración y marcas de comparación en sábanas
status: hecha
depends:
milestone:
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Probar a mano el formato de las pistas de valoración (D-125 a D-128, D-134 a D-138) y de la marca de comparación (D-139) con los nueve requisitos de sábanas de la prueba de assessment-hints y los tipos y fuentes que citan, antes de automatizar nada. Lo aprendido decide el paso de taxo (OQ-71), el lote por tipo (OQ-66) y la tarea de PAA (T-043).

## Criterios de aceptación

- [x] demand-engine/catalog/hints.json contiene, escritas por Claude, las pistas dirigidas a los nueve requisitos (cat.ropa-de-casa/01, /03, /05, cat.sabanas/03, cat.ropa-de-cama/01, gen/03, gen/04, gen/12, gen.variantes/02), a sus tipos y a las fuentes que citan; cada una con los seis campos (id PV-n sin ceros delante, pista, propiedad, ac, para, origen) y origen «marco», «normativa», «referencias» o «paa»
- [x] Ninguna pista es una lista ni una frase exacta: cada una es un criterio breve con su porqué, que nombra propiedad y AC (D-128)
- [x] Los nueve requisitos llevan en el catálogo su marca de dimensión de comparación explícita y con motivo según el criterio de D-139 (composición, hilos, gramaje y precio: se compara; tamaño de cama, garantía legal, identificadores y variantes disponibles: no, con su caso a, b o c)
- [x] Una comprobación con código da 0 errores: seis campos, destino existente, id sin ceros delante, origen admitido, ninguna duplicada con el mismo destino y la misma propiedad
- [x] Una búsqueda por etiquetas, solo con código, devuelve para cada uno de los nueve requisitos sus pistas de tipo, fuente y requisito sin repetir; el resultado queda anotado en la tarea
- [x] Lo aprendido sobre el formato (lo que no encaja, campos que faltan o sobran, dudas) queda anotado en la tarea y, si afecta al canon, como cuestión abierta o incidencia en docs/30-governance

## Resultado

Piloto de pistas: hints.json 0.1 (36 vigentes, 5 retiradas) y marcas de comparación en los nueve requisitos de sábanas; bin/model hints check|find; hallazgos en I-42…I-46 y OQ-73

## Notas

- 2026-10-27 Hecho: demand-engine/catalog/hints.json 0.1 (41 pistas, 36 vigentes, 5 retiradas: PV-4…7 y PV-19); marca «comparison» {mark, case, reason} en los nueve requisitos (cat/ropa-de-casa, sabanas, ropa-de-cama y gen.json); código en demand_engine/demand/hints.py: «bin/model hints check» (0 errores) y «bin/model hints find REQ…»; pruebas en tests/demand/test_hints.py (57 pasan en el contenedor).
- 2026-10-27 Búsqueda por etiquetas (bin/model hints find), sin repetir: ropa-de-casa/01 [material×producto, se compara] PV-1,2,3 tipo · PV-18 fuente · PV-23 req. ropa-de-casa/03 [seguridad×producto, se compara] PV-38,39,40 fuente · PV-24,25 req. ropa-de-casa/05 [magnitud×producto, se compara] PV-8,41 tipo · PV-26,27 req. sabanas/03 [construccion×producto, se compara] PV-9 tipo · PV-28,29 req. ropa-de-cama/01 [medida-que-fija×producto, no (b)] PV-10,11 tipo · PV-30 req. gen/03 [—×producto, no (c)] PV-21 fuente · PV-31,32,33 req. gen/04 [—×oferta, se compara] PV-14,15 tipo · PV-20,22 fuente · PV-34,35 req. gen/12 [—×condiciones, no (a)] PV-16,17 tipo · PV-36 req. gen.variantes/02 [—×variante, no (c)] PV-12,13 tipo · PV-37 req. De 3 a 6 pistas por requisito; las de tipo llegan a 4–67 requisitos, las de fuente a 1–4.
- 2026-10-27 Aprendido 1 (fuentes): casi todas las fuentes de los nueve las cita un solo requisito (Amazon thread/fabric_weight/compliance_fabric_weight, bedding-size, TRLGDCU-97.1.n, RD-3423): ahí una pista por fuente duplica la del requisito. Criterio aplicado: a la fuente solo si la pista vale para todos los requisitos que la citan. shopify-attr:fabric sin pista: «un tejido no es una composición» sería falso en cat.fundas-de-nordico/02, que pregunta por el tejido. shopify-attr:material (8 requisitos de sectores distintos) no da nada que no diga el tipo.
- 2026-10-27 Aprendido 2 (etiquetas): «se compara por el comienzo de la etiqueta» falla: el guion separa el artículo en las leyes (ley:UE-1007/2011-16.1) pero es parte del nombre en Shopify (fabric / fabric-weave). Implementado: en ley:, separan - . @; en atributos y propiedades, = @. 3 (para de un solo valor): las certificaciones están en dos rasgos (seguridad, certificacion-origen) y tres atributos (safety-certifications, organic-certification, product-certifications-standards); ninguna llave las cubre una sola vez. Se dirigieron a la fuente safety-certifications (4 requisitos, todos certificaciones); cat.sabanas/02 y las de certificacion-origen se quedan sin ellas.
- 2026-10-27 Aprendido 4 (rasgos heterogéneos): una pista por tipo llega a todos los sectores del rasgo. PV-7 decía «gramaje en g/m², no en g» y llega a cat.discos-y-lp/08 (vinilo, en g): retirada y reescrita (PV-41). Seguridad mezcla certificaciones con alérgenos, vibración, edad y advertencias: PV-4…6 retiradas y dirigidas a la fuente. Para el lote por tipo (OQ-66): revisar cada pista contra la lista de requisitos a que llega (el código la da). 5 (capa general sin rasgo): sus pistas solo van por entidad o id; el GTIN (dígito de control, por variante) quedó como pista por requisito con origen «marco», que D-136 reserva a las de tipo; y la de variante no llega a gen/03 (entidad producto).
- 2026-10-27 Aprendido 6 (duplicadas): «mismo destino y misma propiedad» no detectó nada; la duplicada real (PV-19 «100 %/puro» frente a PV-2) llegaba al mismo requisito por llaves distintas (fuente y tipo). Implementado aviso sobre lo que llega a cada requisito (misma propiedad y AC por llaves distintas): 4 avisos, 1 duplicada real. 7: «criterio, no lista» solo se comprueba con código en su forma (≤2 frases, ≤280 car.); el resto es de un revisor. 8: corregir antes de que ningún modelo use el catálogo dejó 5 retiradas en la 0.1. 9: sin origen para lo que sale de la justificación o de aportaciones inferidas (cabos del recuento): se usó «referencias». 10: arts. 5, 7 y 9 del Reglamento 1007/2011 citados de memoria; las leyes no están congeladas en var/refs. 11: la marca y las pistas aún no pasan al modelo ensamblado (D-135); la compilación conserva el campo; las versiones de bloque no se suben a mano. Certificación marcada «se compara» como dudosa (¿filtro?).
- 2026-10-27 Gobernanza (/docs-update, revisado por docs-reviewer): nuevas I-42 (separadores de la etiqueta), I-43 (para con un solo valor; certificaciones), I-44 (duplicadas por llaves distintas), I-45 (pistas de tipo en la capa general; origen «marco»), I-46 (qué comprueba el código de «criterio, no lista»); nueva OQ-73 (corregir en sitio antes de usar); OQ-66 y OQ-71 anotadas; assessment-hints 1.5 con marcas ⚠. Lo de las leyes no congeladas (arts. 5 y 9 del 1007/2011 en PV-18) queda solo aquí.
