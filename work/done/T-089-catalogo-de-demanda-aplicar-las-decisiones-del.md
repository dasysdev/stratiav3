---
id: T-089
title: Catálogo de demanda: aplicar las decisiones del repaso de OQ
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Llevar a demand-engine/catalog lo que fijan D-184, D-185, D-196 y D-201 (repaso de OQ del 2026-10-29)

## Criterios de aceptación

- [x] gen.suscripcion: p y q críticas, r principal (D-184)
- [x] gen.opiniones/01 con origen normativa y fuente TRLGDCU art. 20.4; aportación «cómo se procesan las reseñas» de origen marco (D-184)
- [x] Cuestión del fabricante en alimentos y piensos con fuentes 1169/2011 art. 9.1.h y 767/2009 art. 15.b (D-184)
- [x] gen/26 y gen/09 con su conjunto declarado en la descripción (D-185)
- [x] Bloques de categoría revisados con la regla de D-196 y cat.sofas/13 partida en asiento y cojines
- [x] Origen «inferida» admitido en el esquema de las pistas de valoración (D-201)
- [x] La nota de catalog/amazon-map.json deja de decir «pendiente de revisión»: la valida el entrenamiento (D-174, D-040)
- [x] bin/model check sin errores y tests en verde

## Resultado

Capa general (D-184, D-185), 19 cuestiones de categoría partidas (D-196), pistas con «inferida», lista en para, bloques nuevos y revisor (D-201, D-208, D-211)

## Notas

- 2026-10-29 Repaso de incidencias (D-208, D-211): (1) en hints.py, «para» admite una lista de valores de una misma llave (fuentes o tipos), sin mezclar llaves; la revisión de D-200 cubre todos sus valores; dirigir las pistas de certificaciones a sus dos rasgos y tres atributos. (2) En el paso que escribe las pistas, un agente revisor juzga «criterio, no lista»; bin/model check solo comprueba la forma.
- 2026-10-29 D-196: revisadas las 445 cuestiones de catalog/cat. Criterio: se divide si la cabeza de la pregunta junta necesidades distintas; los ejemplos entre paréntesis no cuentan (D-197). Partidos 19 (sofas/13→35 y 18 más: botellas-de-agua/07→14, calzado/17→27, calzado/19→28, camas-para-mascotas/08→16 y /10→17, cd-de-musica/07→16, clips/05→10, cojines-decorativos/07→15, fundas-de-almohada/07→09, joyas-para-piercings/01→12, juguetes-para-perros/11→17 y /14→18, lijadoras/13→15, mantas/05→15, mochilas-escolares/04→09, mochilas-para-portatil/04→11, sofas/14→36, soperas/04→11). Cada parte conserva rasgo, importancia y regla; rules/resolving.json repartido por aportación. El campo dimension de las partes conserva el texto original.
- 2026-10-29 Pistas: PV-38, PV-45, PV-46 y PV-47 van ahora a la lista de los tres atributos de certificaciones (D-208), corregidas en su sitio porque ningún modelo las usa (D-202). No se dirigen a los rasgos seguridad ni certificacion-origen: una lista no mezcla llaves, y los dos rasgos llegan también a requisitos que no son certificaciones (D-200). Pistas de un bloque nuevo: sin id, validadas en register y en hints check. Revisor de D-211: classifier/hint-review.md, enlazado desde paa-classify, demand-model y classify-batch. Pendiente fuera de T-089: que el entrenamiento numere al compilar las pistas de un bloque de ejecución.
