# T-032 · Tanda de control con los 14 casos tras T-030 y T-031

Fecha: 2026-10-26. Tanda de control de los cambios de canon del 2026-10-26: D-055 a D-063 (crítico y excepciones por requisito y clase, rasgos abiertos, reglas de formulación, información resolutiva), junto con D-064 a D-076, que el reglamento v3 ya recoge.

**Ejecuciones comparadas:**

| | v4 (referencia) | v6 (esta tanda) |
|---|---|---|
| Carpetas | `var/runs/2026-10-26-v4-a` y `-b` | `var/runs/2026-10-26-v6-a` y `-b` |
| Reglamento | v2 | v3 |
| Reglas | 4 | 6 |
| Catálogo | 382 requisitos de categoría | 440 requisitos, redactado de nuevo en T-031 |
| Capa general | 0.3 | 0.5 |

Los 14 casos de `cases/`, con un agente por caso y ejecución. No se induce ni se compila.

**Fuentes de las cifras:**
- `bin/train report` sobre cada par (copia de la v6 en [2026-10-26-t032-train-report.md](2026-10-26-t032-train-report.md)). La v4 se mide con las reglas 6, para comparar con las mismas reglas.
- Una medición de solo lectura sobre los modelos, las salidas y el inventario de T-031 ([informe de formulación](2026-10-26-t031-formulation-report.md)). Cubre la formulación, los condicionados, las inferidas, los críticos, los rasgos y la información resolutiva, y hace en seco la inducción de excepciones, el índice de rasgos y la información resolutiva.
- Las señales de redacción salen de una heurística y se revisaron a mano.

## Resumen

**Lo que funciona:**
- **Formulación (D-060).** Los modelos ya llevan el catálogo nuevo: los 54 requisitos de categoría que T-031 redactó de nuevo y los 45 requisitos que salen de sus divisiones. En las especializaciones e inferidas que redacta el clasificador no queda ninguna pregunta compuesta ni ninguna condición interna; en la v4 había 7. Las condiciones pasan a la aplicabilidad.
- **Crítico por requisito y clase (D-055, D-058).** Cinco críticos por excepción por ejecución, además de los diez del marco. La v4 solo tenía los del marco.
- **Composición (D-057).** Pasa de 11/14 a 13/14 y 14/14: la hoja más específica entra como categoría y la hermana entra como alias.
- **Clave del modelo.** Estable en 14 de 14 casos, frente a 13 de 14 en la v4.

**Lo que empeora o no se cumple:**
- **La oferta.** La aplicación solo coincide entre A y B en 8 de 14 casos (14 de 14 en la v4). Las causas son reglas ambiguas: I-30, I-31 e I-34.
- **Los hechos sin pregunta.** Pasan de 14 a 66. Son sobre todo el plazo de cambio (I-35) y «diseño y control de calidad».
- **Los votos de importancia.** Suben: en la misma pregunta, caso y ejecución, 73 suben y 6 bajan de 542.
- **El consumo.** Se multiplica por 2,4.
- **La información resolutiva.** Se registra en todos los hechos, pero el control no puede aceptar ninguna aportación nueva: 9 de los 14 casos son de una sola tienda.
- **Los rasgos.** Los votos apenas se apartan del rasgo vigente: 12 de 730.

## Ejecución y consumo

28 agentes, todos con `bin/model check` «correcto» al terminar. Ningún reintento, ningún bloque generado y las 28 salidas declaran `rulebook: v3`.

| | v4 | v6 |
|---|---|---|
| Tokens A / B | 13,07 M / 12,27 M | 30,68 M / 29,62 M |
| Total | 25,34 M | **60,31 M** (× 2,4) |
| Por caso | 0,90 M | 2,15 M |
| Tokens de salida | 0,39 M | 1,23 M (× 3,1) |
| Peticiones | 445 | 764 |
| Minutos de agente | 80 | 204 |

**Por qué crece el consumo:**
- Cada hecho lleva su aportación.
- Cada requisito lleva su voto de rasgo.
- Los requisitos que redacta el clasificador llevan su información resolutiva.
- La capa general tiene más requisitos: 46 frente a 27.
- Se cuentan el doble de hechos: 1337 frente a 641.

A este ritmo, las 300 fichas de T-029 costarían unos 650 M de tokens por ejecución: 1,3 G con las dos, frente a los 500 M que se estimaron con el piloto.

## Formulación (D-060)

### Requisitos de categoría en los modelos

Cifras por ejecución; A y B dan lo mismo, porque lo decide el catálogo.

| | v4 | v6 |
|---|---|---|
| Requisitos de categoría en los 14 modelos | 314 | 359 |
| Redactados de nuevo por T-031 (regla 1 / 2 / 3 / 4) | 54 con la redacción antigua (3 / 10 / 32 / 9) | los mismos 54, con la nueva |
| Nuevos de T-031 (por regla) | — | 45 (1 / 9 / 29 / 6) |

### Preguntas compuestas y condiciones internas, antes y después

Señales de la heurística, por ejecución:

| Señal | Categoría v4 → v6 | Capa general v4 → v6 |
|---|---|---|
| Pregunta compuesta | 73 → 51 | 168 → 112 |
| Condición sobre un hecho dentro de la pregunta | 12 → 5 | 28 → 14 |
| Condición sobre la existencia de la información | 2 → 1 | 28 → 0 |

La capa general pasa de 364 a 574 apariciones en los modelos, porque se dividió (D-065).

Revisión a mano de las 27 preguntas de categoría distintas que dan señal en la v6:
- **24 son formas admitidas:**
  - sí o no con el detalle del mismo hecho («¿Tiene puntera de protección y de qué tipo…?»);
  - partes que solo tienen sentido juntas (talla y sistema de tallas);
  - el mismo rasgo (material y composición).
- **3 quedan dudosas:** `cat.sofas-cama/02` (incluye colchón, su medida y si se retira), `cat.mantas/05` (peso y grosor) y `cat.juguetes-para-perros/06` (pilas, si se incluyen y si es recargable). Son partes que toman otro rasgo o importancia dentro de la forma de sí o no (I-37).

Especializaciones e inferidas redactadas por el clasificador:

| | v4-a | v4-b | v6-a | v6-b |
|---|---|---|---|---|
| Requisitos redactados | 20 | 15 | 18 | 15 |
| Que incumplen D-060 | 4 | 3 | 0 | 0 |
| Dudosos (dos partes del mismo rasgo) | 3 | 0 | 0 | 1 |

| v4 | v6 |
|---|---|
| ¿Qué piezas incluye el juego, cuántas de cada una y en qué medidas, para cada medida de cama? | ¿Qué piezas componen el juego y cuántas unidades de cada una? (por variante cuando la composición cambia con la medida de cama) |
| ¿Qué piezas incluye el juego y cuántas de cada una (también si cambian según la medida)? | ¿Qué piezas componen el juego y cuántas unidades de cada una incluye? (por variante cuando el número de piezas cambia con la medida) |
| ¿Qué abrigo o sensación térmica ofrece el tejido y para qué temporada está pensada la sábana…? | ¿Qué nivel de abrigo tiene? |
| ¿Qué espacio total ocupa abierto en cama… y cuánto espacio libre necesita delante para desplegarlo? | ¿Qué fondo total ocupa abierto como cama…? |

Las preguntas de sí o no con detalle se mantienen, como pide la regla 2 («¿Tiene embozo? Si lo tiene, ¿de qué ancho es?»).

Las condiciones van a `applicability` («si el tejido es de fibras naturales hiladas»). Todo lo redactado lleva su `resolving_info`.

### Requisitos condicionados nuevos

- **Condicionados de categoría en los modelos:** de 34 a 47 por ejecución.
- **Los 10 nuevos de T-031 que aparecen:** `cat.botas/20`, `/21`, `/23`, `cat.juguetes-para-perros/15`, `cat.pantuflas/18`, `cat.sofas-cama/16`, `/17`, `cat.sofas/32`, `/33` y `/34`.
- **Lo que redacta el clasificador:** inferidas condicionadas, 0 y 1 en la v4 y 1 y 0 en la v6; ninguna condicionada a un hecho de la oferta en ninguna de las dos. Requisitos de especialización condicionados: de 9 y 7 a 4 y 5. Las condiciones de la pieza o de la variante pasan a la aplicabilidad.

### Componentes sin fuente pasados a inferidas

- **Requisitos de categoría con origen «inferida» en los modelos:** de 6 a 14 distintos (de 9 a 20 apariciones por ejecución).
  - 4 son nuevos por la regla 4: `cat.calzado/25`, `cat.comida-para-perros/17`, `/18` y `cat.sofas/33`.
  - Otros 4 son partes condicionadas sin fuente de las reglas 1 y 2: `cat.botas/23`, `cat.sofas-cama/16`, `/17` y `cat.sofas/34`.
- **Inferidas del clasificador:** 11 y 8 en la v4; 13 y 9 en la v6.
- **Inferidas con fuente:** `plaid-punto-101` B redacta dos con fuente en el PTD de Amazon, que el bloque no recoge (I-38).

## Críticos y excepciones (D-055, D-058)

### Críticos por ejecución

| | v4-a | v4-b | v6-a | v6-b |
|---|---|---|---|---|
| Del marco (medida que fija) | 11 | 10 | 10 | 11 |
| Por excepción | 0 | 0 | 5 | 5 |
| Por voto (especialización sin regla) | 1 | 1 | 0 | 0 |

**Críticos por excepción**, en las dos ejecuciones:

| Requisito | Clase | Caso |
|---|---|---|
| `cat.cojines-decorativos/01` | hg-3-64 | cojín |
| `cat.ropa-de-cama/02` | hg-15-1-4 | manta y plaid |
| `cat.productos-para-mascotas/01` | ap-2-3-3-1 | pienso |
| `cat.sofas/01` | fr-22 | Stressless |

`cuerda-tootoy` y `sofa-cama-luna` siguen sin ningún requisito de categoría crítico.

### Excepciones y votos

- **Excepciones de las reglas 6 aplicadas en cada ejecución:** 56 distintas, que deciden 69 requisitos (37 principales, 27 complementarios y 5 críticos).
  - Los votos coinciden en 107 de 138.
  - Los que discrepan son sobre todo complementario → principal (23).
- **Votos «crítico»:** de 21 y 21 a 27 y 30.
  - Pares requisito y clase con algún voto crítico: de 21 a 30.
  - Con mayoría crítica: de 15 a 20.
  - Mayorías críticas nuevas que ninguna regla recoge aún: `cat.comida-para-perros/02` (forma del pienso), `cat.fundas-de-almohada/01` (6 votos), `cat.juguetes-para-perros/01` (tipo de juguete), `cat.sofas-cama/02` (incluye colchón), `cat.sofas/03` (plazas) y `cat.sofas/04` (medidas exteriores).
- **Inducción en seco con eci + v6 en lugar de eci + v4:**
  - 126 excepciones (15 críticas) frente a las 103 vigentes (10 críticas);
  - 47 excepciones nuevas o cambiadas y 24 que dejarían de salir;
  - se añadirían las seis críticas citadas y caería `cat.cojines-decorativos/01@hg-3-64`, en la que A y B se reparten.
  - Con dos votos por clase, las excepciones cambian mucho de un ciclo a otro.
- **Votos que contradicen el marco:** de 13 a 5.

## Rasgos (D-056)

- **Votos:** el reglamento v2 no votaba rasgos. En la v6, los 203 requisitos de categoría de los modelos reciben 730 votos de rasgo; ningún agente propone un rasgo nuevo.
- **Votos que se apartan del rasgo vigente:** 12 (1,6 %), en 8 requisitos. El índice en seco cambiaría uno: `cat.comida-para-perros/11`, de material a certificacion-origen, con 2 votos. No se aprobaría ninguno.
- **Desacuerdo de fondo:** qué medida fija lo vendido depende de la clase.
  - `cat.ropa-de-cama/01` (tamaño de cama): medida-que-fija 10, medida 1, uso 1.
  - `cat.ropa-de-cama/02` (centímetros): medida 9, medida-que-fija 3. Los votos de «medida que fija» vienen de la manta y el plaid.
  - El rasgo es uno por requisito; la diferencia por clase ya la recoge la excepción crítica `cat.ropa-de-cama/02@hg-15-1-4`.
- **Que los votos sigan el rasgo que muestra `bin/model blocks`** es coherente con un catálogo revisado en T-031. El control no prueba bien el vocabulario abierto; se mide en T-029, con categorías nuevas.

## Información resolutiva (D-062 a D-064)

### Listas en los modelos

Por requisito distinto presente en los modelos:

| Requisitos | Referencias | Inferidas | Marco |
|---|---|---|---|
| 203 de categoría | 459 | 171 | — |
| 41 de la capa general | 1 | 28 | 55 |

Las especializaciones e inferidas del clasificador llevan además su propia lista.

### Hechos declarados

| | v4-a | v4-b | v6-a | v6-b |
|---|---|---|---|---|
| Responden con una aportación de la lista | — | — | 597 | 625 |
| Proponen una aportación nueva | — | — | 24 | 25 |
| Responden sin aportación | 322 | 305 | 0 | 0 |
| Sin pregunta | 30 | 33 | 81 | 84 |
| No cuentan (estético, promocional, beneficio) | 41 | 40 | 20 | 19 |

Todos los nombres de aportación que escriben los agentes están en la lista de su requisito.

### Inducción en seco (sin compilar)

Sobre los 244 requisitos con lista presentes en los modelos (714 aportaciones):

| | Aportaciones |
|---|---|
| Observadas | 178 (43 en dos tiendas o más) |
| Nunca observadas | 536 (75 %) |
| Propuestas aceptadas | 0 |
| Propuestas pendientes (una tienda) | 24 |
| Propuestas rechazadas | 0 |

- **Por qué no se acepta ninguna:** 9 de los 14 casos son de burritoblanco.com y cada propuesta sale de una sola tienda. La aceptación por dos tiendas se mide en T-029.
- **Propuestas que se repiten:**
  - «indicación sobre el uso de lejía» (`cat.ropa-de-casa/02`), en 6 casos, también en `cat.calzado/13`.
  - Las mismas tres en A y B de `cuerda-tootoy` (grosor, resistencia cualitativa, advertencias en la ficha).
  - Dos que fija la norma y faltan en las listas aprobadas de la capa general (I-39): precio más bajo de los 30 días anteriores y precio por unidad de medida.
- **Estabilidad A/B:** 311 de 386 requisitos respondidos en las dos ejecuciones nombran las mismas aportaciones (81 %).

## Cobertura

| Ejecución | Composición | Especializaciones | Cuestiones clave | Aplicación | Inferida esperada |
|---|---|---|---|---|---|
| v4-a | 11/14 | 7/14 | 27/40 | 5/6 | 0/2 |
| v4-b | 11/14 | 6/14 | 27/40 | 5/6 | 0/2 |
| v6-a | **13/14** | 6/14 | 27/40 | 5/6 | 0/2 |
| v6-b | **14/14** | 6/14 | 26/40 | **6/6** | 0/2 |

- **Composición.**
  - Aciertan el sofá cama (Sofás de dos plazas como alias), el plaid (la hoja Mantas decorativas) y las fundas nórdicas.
  - Falla `funda-nordica-salvia-642` A, que mete Juegos de cama como alias; la B y las dos de la bordada lo rechazan.
- **Especializaciones.** Las esperadas (equitación, material reciclado, cuerda, polar, pienso seco, punto, tapicería de piel, uso invernal) siguen como valores, por el apoyo estricto (P4), como en la v4.
- **Inferidas esperadas.** Las dos no se pueden cumplir como están escritas:
  - el mecanismo de apertura del sofá cama ya es un requisito del catálogo (`cat.sofas-cama/03`);
  - la preparación del algodón la redacta la A como pregunta de la clase («las fibras o el hilo»), sin «algodón», que es lo que busca el control.
  - Las expectativas del control necesitan una revisión (anotada en la tarea).
- **Hechos que cuentan:** de 329 y 312 a 653 y 684.
- **Hechos sin pregunta:** de 7 y 7 a 32 y 34. Los 66 de la v6 son:

| Hechos sin pregunta | Veces |
|---|---|
| Diseño y control de calidad de Burrito Blanco | 24 |
| Plazo de cambio de 14 días (I-35) | 18 |
| «Garantía de calidad» sin contenido (I-33) | 7 |
| Valoración de la tienda (D-076) | 3 |
| Otros | 14 |

## Estabilidad A/B y coherencia

| Medida | v4 | v6 |
|---|---|---|
| Composición | 14/14 | 13/14 |
| Clave del modelo | 13/14 | 14/14 |
| Especializaciones | 13/14 | 14/14 |
| Aplicación de la oferta | 14/14 | **8/14** |
| Importancia en los requisitos de categoría comunes | 314/314 | 359/359 |
| Coherencia por rasgo en los modelos | 2 | 2 |
| Coherencia por requisito (pares con mayoría de votos en contra) | 11/313 | **46/358** |
| Votos que coinciden con la regla | 599/658 (91 %) | 606/751 (81 %) |

**Ofertas que cambian entre A y B:**

| Caso | A | B | Causa |
|---|---|---|---|
| `cojin-018` | estándar | con descuento | descuento por suscribirse al boletín (I-30) |
| `manta-nacarina-046` | con descuento | sin descuento | ídem |
| `sabanas-coralina-999` | sin descuento | con descuento | ídem |
| `stressless-wave-outlet` | — | unidad no nueva | «visita la exposición para aprovechar la última unidad» (I-31) |
| `toallas-azul-080` | — | con variantes | muestras de color sin nombre visible (I-34) |
| `protector-basic-010` | — | con opiniones | A no ve las opiniones del producto («4,8 (4)»): fallo del agente, no de la regla |

**Coherencia por requisito.** Las reglas 6 se indujeron con los votos de la v4, así que la v4 coincide con ellas por construcción. La v6 es la primera medida fuera de muestra.
- De los 46 pares, 34 suben y 12 bajan.
- 10 son requisitos nuevos de T-031, cuya importancia puso quien redactó.
- El resto son requisitos que ya existían, sobre todo de complementario a principal en sofás, juguetes y ropa de casa.
- La subida es general: en los votos con la misma pregunta, caso y ejecución, 73 suben y 6 bajan de 542. Principal pasa del 43 al 49 % y crítico del 5 al 7 %.

## Efectos no deseados y reglas que no se cumplen

| # | Efecto | Propuesta | Registro |
|---|---|---|---|
| 1 | Oferta inestable por el descuento del boletín | Precisar D-074: un descuento condicionado también activa `gen.descuento` | [I-30](../../../docs/30-governance/issues.md#i-30) |
| 2 | Unidad de exposición leída de dos formas | Ejemplo en D-057 y en el paso 6 | [I-31](../../../docs/30-governance/issues.md#i-31) |
| 3 | El importador con marca propia va a `gen/18`, `gen/13` o `gen/17` | Quien comercializa con su marca es fabricante (RSGP); aportación en `gen/17` | [I-32](../../../docs/30-governance/issues.md#i-32) |
| 4 | «Garantía de calidad» activa la garantía comercial solo en las toallas | Sin contenido, no activa el bloque | [I-33](../../../docs/30-governance/issues.md#i-33) |
| 5 | Variantes por muestras sin nombre visible | Varias opciones visibles activan `gen.variantes`; una sola, no | [I-34](../../../docs/30-governance/issues.md#i-34) |
| 6 | El plazo de cambio no tiene pregunta: 18 de los 66 hechos sin pregunta | Bloque condicionado de cambios, o fuera del modelo | [I-35](../../../docs/30-governance/issues.md#i-35) |
| 7 | `esp.juego` con o sin medidas según el agente | «Juego» aporta piezas y cuántas; las medidas, los bloques de cada pieza | [I-36](../../../docs/30-governance/issues.md#i-36) |
| 8 | Sí o no con detalle de otra importancia (`cat.sofas-cama/02`) | La regla 3 prevalece; revisar tres requisitos | [I-37](../../../docs/30-governance/issues.md#i-37) |
| 9 | Inferidas con fuente en el PTD | Proponerlas al bloque con su fuente | [I-38](../../../docs/30-governance/issues.md#i-38) |
| 10 | Faltan aportaciones de la norma en la capa general | Añadirlas con origen marco, con aprobación | [I-39](../../../docs/30-governance/issues.md#i-39) |
| 11 | Consumo × 2,4: unos 1,3 G de tokens para las dos ejecuciones de las 300 fichas de T-029 | Medir antes de escalar dónde va el contexto (listas de `bin/model blocks`, comprobaciones repetidas) | T-029 |
| 12 | Los votos de importancia suben de forma general | Sin cambio de regla. La inducción decide; revisar la deriva con el ciclo siguiente antes de dar las excepciones por buenas | T-032 |
| 13 | Expectativas del control anteriores al catálogo y al canon nuevos (inferidas, aplicación) | Revisar `cases/` | T-032 |
| 14 | `train report` toma los rasgos y la información resolutiva del catálogo compilado, no de las ejecuciones: sin compilar, salen a 0 | Calcularlos desde las ejecuciones, como en esta medición | T-032 |
| 15 | Ninguna aportación nueva se puede aceptar en el control (una sola tienda) | Medir la aceptación en T-029 | T-029 |

## Dudas de los agentes que se repiten

- **El descuento del boletín**, en 14 salidas: I-30.
- **La garantía de calidad sin contenido**, en 18: I-33.
- **El importador y el fabricante**, en 18: I-32.
- **El alcance de `esp.juego`**, en 8: I-36.
- **El IVA no declarado.** Varias salidas asignan el precio a «precio con impuestos incluidos» aunque la ficha no lo dice; una lo deduce de un dato oculto. Va contra el paso 1 («no completes hechos ausentes»): es un fallo de aplicación, sin regla nueva.
- **Las contradicciones de las fichas** (devolución en 14 o 45 días, composición, secado) se registran como hechos y quedan para la auditoría.
