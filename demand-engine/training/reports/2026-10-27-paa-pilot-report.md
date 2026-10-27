# Informe del piloto de medición del entrenamiento de PAA · 2026-10-27

Tarea T-042, criterio 5. Piloto sin inducción ([D-114](../../../docs/30-governance/decisions.md#d-114)): mide qué varía entre clases en semillas, clics, criterios y dudas. Las clases son las de los 14 casos de referencia: 12 conjuntos, uno por clave distinta ([D-116](../../../docs/30-governance/decisions.md#d-116)).

- **Captura:** `paa run` del 2026-10-27: sábanas por la mañana y el resto de 14:30 a 16:48; 68 búsquedas, 8 clics, pausa de 5 s.
- **Clasificación:** una pasada por conjunto, con el reglamento `classifier/paa.md` v3 y un agente por conjunto.
- **Catálogo:** la clave del modelo v6-b de cada conjunto (tabla 1).
- **Datos:** `var/paa/sets/<conjunto>/` (`classified.json`, `report.md`). Cifras calculadas sobre `classified.json` y los `record.json` de cada búsqueda.

Lo que aquí se llama «observación» es lectura de los datos. Lo que se llama «propuesta» no se ha aplicado: crear o retirar reglas lo decide el usuario (D-114).

## 1. Conjuntos

| Conjunto | Caso (modelo v6-b) | Catálogo | Búsq. | Preguntas únicas | Fuera | Tokens |
|---|---|---|---|---|---|---|
| sabanas | sabanas-coralina-999 | gen@0.5 cat.casa-y-jardin@2 cat.ropa-de-casa@4 cat.ropa-de-cama@2 cat.sabanas@2 cat.fundas-de-almohada-y-cojines@2 cat.sabanas-ajustables@2 cat.sabanas-planas@2 cat.fundas-de-almohada@3 esp.juego@0 | 10 | 200 | 10 % | 730k |
| botas | bota-polo-e | gen@0.5 cat.ropa-y-accesorios@2 cat.calzado@4 cat.botas@4 | 5 | 100 | 6 % | 563k |
| cojines | cojin-018 | gen@0.5 cat.casa-y-jardin@2 cat.decoracion@3 cat.cojines-decorativos@3 | 5 | 97 | **76 %** | 270k |
| comida-perros | pienso-josera-sea-fish | gen@0.5 cat.productos-para-mascotas@2 cat.productos-para-perros@3 cat.comida-para-perros@4 | 4 | 77 | 12 % | 283k |
| cubrecolchones | protector-basic-010 | gen@0.5 cat.casa-y-jardin@2 cat.ropa-de-casa@4 cat.ropa-de-cama@2 cat.protectores-de-colchon@3 cat.cubrecolchones@2 | 6 | 81 | 22 % | 450k |
| fundas-nordicas | funda-nordica-bordada-401 | gen@0.5 cat.casa-y-jardin@2 cat.ropa-de-casa@4 cat.ropa-de-cama@2 cat.sabanas@2 cat.fundas-de-nordico@3 cat.fundas-de-almohada-y-cojines@2 cat.sabanas-ajustables@2 cat.fundas-de-almohada@3 esp.juego@0 | 8 | 157 | 36 % | 713k |
| juguetes-perros | cuerda-tootoy | gen@0.5 cat.productos-para-mascotas@2 cat.productos-para-perros@3 cat.juguetes-para-perros@5 | 5 | 61 | **49 %** | 429k |
| mantas | manta-nacarina-046 | gen@0.5 cat.casa-y-jardin@2 cat.ropa-de-casa@4 cat.ropa-de-cama@2 cat.mantas@4 | 5 | 104 | 28 % | 481k |
| pantuflas | zapatillas-bano-50 | gen@0.5 cat.ropa-y-accesorios@2 cat.calzado@4 cat.pantuflas@4 | 5 | 62 | 21 % | 413k |
| sofas | stressless-wave-outlet | gen@0.5 cat.mobiliario@2 cat.sofas@3 | 4 | 89 | 9 % | 570k |
| sofas-cama | sofa-cama-luna | gen@0.5 cat.mobiliario@2 cat.sofas@3 cat.sofas-cama@4 | 5 | 84 | 7 % | 586k |
| toallas | toallas-azul-080 | gen@0.5 cat.casa-y-jardin@2 cat.ropa-de-casa@4 cat.toallas@2 esp.juego@0 | 6 | 127 | 28 % | 561k |
| **Total** | | | **68** | **1239** | | **6,05 M** |

- **Coste:** 0,27–0,73 M tokens por clase, por debajo de la estimación de 0,7–1,3 M (D-114). El coste va con el número de preguntas y el tamaño del catálogo, no con la clase.
- **Bloqueo:** uno, un HTTP 429 en la búsqueda 41 seguida, unos 20 minutos después de empezar. Se levantó en menos de 1 h 49 min. Las 13 búsquedas restantes pasaron sin otro, con el mismo ritmo. Detalle en el README del motor PAA, «Bloqueos observados».

## 2. Rendimiento por grupo de semillas

Columnas:
- **Únicas:** preguntas distintas que trae el grupo.
- **Exclusivas:** las que solo trae ese grupo.
- **Útiles:** preguntas dentro del perímetro que confirman un requisito, sostienen un candidato o un criterio que genera.

| Conjunto | Grupo | Búsq. | Vacías | Únicas | Exclusivas | Dentro | Útiles | Sostienen candidato |
|---|---|---|---|---|---|---|---|---|
| sabanas | núcleo | 5 | 0 | 109 | 85 | 91 | 41 | 1 |
| | material | 5 | 0 | 115 | 91 | 112 | 52 | 11 |
| botas | núcleo | 1 | **1** | 0 | 0 | 0 | 0 | 0 |
| | material | 4 | 0 | 100 | 100 | 94 | 58 | 1 |
| cojines | núcleo | 1 | **1** | 0 | 0 | 0 | 0 | 0 |
| | relleno | 4 | 0 | 97 | 97 | 23 | 16 | 4 |
| comida-perros | núcleo | 1 | 0 | 27 | 14 | 21 | 1 | 0 |
| | forma | 3 | 0 | 63 | 50 | 59 | 22 | 6 |
| cubrecolchones | núcleo | 2 | 0 | 44 | 15 | 38 | 16 | 1 |
| | material | 4 | 0 | 66 | 37 | 49 | 23 | 3 |
| fundas-nordicas | núcleo | 4 | 0 | 100 | 75 | 62 | 40 | 1 |
| | material | 4 | 0 | 82 | 57 | 50 | 30 | 5 |
| juguetes-perros | núcleo | 1 | 0 | 27 | 5 | 13 | 5 | 2 |
| | material | 4 | 0 | 56 | 34 | 28 | 12 | 8 |
| mantas | núcleo | 1 | 0 | 27 | 20 | 13 | 5 | 0 |
| | material | 4 | 0 | 84 | 77 | 67 | 32 | 4 |
| pantuflas | núcleo | 1 | 0 | 27 | 18 | 20 | 7 | 4 |
| | material | 4 | **2** | 44 | 35 | 36 | 20 | 6 |
| sofas | núcleo | 1 | 0 | 27 | 20 | 26 | 5 | 1 |
| | tapicería | 3 | 0 | 69 | 62 | 62 | 29 | 6 |
| sofas-cama | núcleo | 2 | 0 | 53 | 28 | 52 | 19 | 5 |
| | mecanismo | 3 | 0 | 56 | 31 | 51 | 17 | 2 |
| toallas | núcleo | 2 | 0 | 46 | 30 | 36 | 9 | 0 |
| | material | 4 | 0 | 97 | 81 | 72 | 26 | 2 |

Observaciones:

1. **Los candidatos salen de las semillas de valores.** De los 30 candidatos, 21 se apoyan solo en preguntas de valores y 8 en los dos grupos. Solo uno, durabilidad en sofás cama, sale solo del núcleo.
2. **El núcleo de una palabra puede no tener caja.** «botas» y «cojines» no tuvieron caja «Más preguntas»: Google mostró solo resultados de compra (200, `paa_box` falso). Tampoco la tuvieron «zapatillas de casa de lana» y «… de borreguito». Son 4 búsquedas vacías de 68 (6 %).
3. **Una semilla de valores puede traer el producto vecino.** El rendimiento del perímetro depende de que el valor no nombre otro producto:
   - cojines: las semillas de relleno traen almohadas de dormir, 76 % fuera;
   - juguetes-perros: el material trae el comportamiento del perro, 49 % fuera;
   - fundas-nordicas: el material trae el nórdico de relleno, 36 % fuera;
   - toallas: el bambú trae la planta, y salen también toallas higiénicas, 28 % fuera;
   - pantuflas: «zapatillas» trae calzado deportivo y de trabajo, 21 % fuera.
   
   Donde el valor solo se aplica a la clase (sofás, sofás cama, botas, comida-perros), la parte fuera baja al 6–12 %.
4. **Las semillas casi no se solapan.** Cada pregunta única aparece en 1,1–1,4 búsquedas en 9 de los 12 conjuntos. En cubrecolchones son 2,0, porque «protector de colchón» y «cubrecolchón» son casi sinónimos. En juguetes-perros son 2,2. Más semillas de valores siguen trayendo preguntas nuevas.
5. **El grupo de valores elegido fuera de las referencias funciona.** En sofás cama, el mecanismo no viene de las referencias (nota de `paa/sofas-cama.json`): trae 31 exclusivas, 51 dentro y 2 que sostienen candidatos. En sofás, la tapicería sin valores en las referencias trae 6 de 6. Las dos excepciones a la regla dan resultado comparable al de las demás.

## 3. Rendimiento por clic

Cada búsqueda trae 27 preguntas como máximo: unas 4 en la caja inicial y 2-3 por clic. Datos de las 68 búsquedas:

| Clic | Nuevas únicas del conjunto | De ellas, dentro | Primer apoyo de un candidato |
|---|---|---|---|
| 0 (caja inicial) | 222 | 196 (88 %) | 7 |
| 1 | 99 | 80 (81 %) | 2 |
| 2 | 144 | 115 (80 %) | 2 |
| 3 | 150 | 112 (75 %) | 7 |
| 4 | 128 | 98 (77 %) | 2 |
| 5 | 131 | 89 (68 %) | 4 |
| 6 | 129 | 89 (69 %) | 3 |
| 7 | 114 | 75 (66 %) | 2 |
| 8 | 122 | 79 (65 %) | 1 |

«Primer apoyo» cuenta, para cada candidato, el clic más temprano en que apareció alguna de las preguntas que lo sostienen.

Observaciones:

1. **Los clics 5 a 8 traen un 40 % de las preguntas únicas** (496 de 1239). Con solo 4 clics, 10 de los 30 candidatos no tendrían ninguna pregunta de apoyo.
2. **La deriva fuera del perímetro crece con el clic:** de un 88 % de preguntas dentro en la caja inicial a un 65–69 % desde el clic 5. Las preguntas expandidas se alejan de la semilla, pero siguen dando candidatos.
3. **El clic 8 no está agotado:** todavía trae 122 únicas nuevas. Los datos no dicen dónde está el punto de saturación.

## 4. Candidatos

30 candidatos en 12 clases, entre 0 y 6 por clase. Su número no es un objetivo (D-114).

| Conjunto | Id | Rasgo | Voto | Preguntas | Bloque | Pregunta, resumida |
|---|---|---|---|---|---|---|
| sabanas | N1 | sensorial | principal | 1 | cat.sabanas, cat.fundas-de-almohada-y-cojines | Tacto del tejido |
| sabanas | N2 | prestacion | principal | 3 | cat.sabanas, cat.fundas-de-almohada | Resistencia a las arrugas |
| sabanas | N3 | prestacion | complementario | 4 | cat.sabanas | Resistencia al uso y al lavado |
| sabanas | N4 | prestacion | complementario | 1 | cat.sabanas | Transpiración |
| sabanas | N5 | material | principal | 1 | cat.ropa-de-casa | Variedad de la fibra |
| sabanas | N6 | certificacion-origen | complementario | 1 | cat.ropa-de-casa | País o región de la fibra |
| botas | N1 | uso | complementario | 1 | cat.calzado | Si el corte cede con el uso |
| cojines | N1 | magnitud | principal | 4 | cat.cojines-decorativos | Densidad de la espuma |
| comida-perros | N1 | uso | complementario | 3 | cat.comida-para-perros | Combinación con otros alimentos |
| comida-perros | N2 | uso | complementario | 2 | cat.comida-para-perros | Preparación para servir |
| comida-perros | N3 | uso | complementario | 1 | cat.comida-para-perros | Transición desde el alimento anterior |
| cubrecolchones | N1 | sensorial | principal | 1 | cat.protectores-de-colchon | Tacto de la cara superior |
| cubrecolchones | N2 | prestacion | complementario | 2 | cat.ropa-de-casa | Durabilidad (lavados que resiste) |
| cubrecolchones | N3 | uso | complementario | 1 | cat.protectores-de-colchon | Compatibilidad con tipos de colchón |
| fundas-nordicas | N1 | uso | principal | 3 | cat.fundas-de-nordico, cat.sabanas, cat.fundas-de-almohada | Temporada o nivel de abrigo |
| fundas-nordicas | N2 | sensorial | principal | 1 | cat.ropa-de-casa | Tacto del tejido |
| fundas-nordicas | N3 | construccion | complementario | 1 | cat.fundas-de-nordico | Sujeción interior del relleno |
| juguetes-perros | N1 | prestacion | complementario | 5 | cat.juguetes-para-perros | Efecto calmante |
| juguetes-perros | N2 | uso | complementario | 4 | cat.juguetes-para-perros | Nivel de actividad del perro |
| mantas | N1 | material | complementario | 1 | cat.ropa-de-casa | Variedad de la fibra |
| mantas | N2 | prestacion | complementario | 1 | cat.ropa-de-casa | Encogimiento al lavado |
| mantas | N3 | uso | principal | 2 | cat.mantas | Uso o lugar (cama, sofá…) |
| pantuflas | N1 | uso | complementario | 8 | cat.calzado | Indicación para afecciones del pie |
| sofas | N1 | prestacion | principal | 5 | cat.sofas | Durabilidad declarada |
| sofas | N2 | prestacion | complementario | 2 | cat.sofas | Transpirabilidad de la tapicería |
| sofas | N3 | prestacion | complementario | 1 | cat.sofas | Resistencia a las arrugas |
| sofas-cama | N1 | prestacion | principal | 2 | cat.sofas | Durabilidad declarada |
| sofas-cama | N2 | estetica | principal | 4 | cat.sofas | Estilo decorativo |
| toallas | N1 | construccion | complementario | 1 | cat.ropa-de-casa | Acabado del tejido |
| toallas | N2 | uso | complementario | 1 | cat.ropa-de-casa | Indicaciones de uso |

Observaciones:

1. **15 de los 30 se apoyan en una sola pregunta.** D-102 lo admite, pero son los más expuestos a cambiar sin la doble pasada de estabilidad, que el piloto no hace (D-114).
2. **Algunos candidatos se repiten entre clases sin coordinación entre los agentes:**
   - **Tacto:** en sábanas, cubrecolchones y fundas nórdicas, en tres bloques distintos (cat.sabanas, cat.protectores-de-colchon y cat.ropa-de-casa).
   - **Durabilidad declarada:** en sofás y sofás cama, los dos en cat.sofas. En cubrecolchones y sábanas aparece como resistencia al uso y al lavado.
   - **Variedad de la fibra:** en sábanas y mantas, los dos en cat.ropa-de-casa.
   - **Resistencia a las arrugas:** en sábanas y sofás.
   
   La misma necesidad cae en bloques de distinta altura según el conjunto. Para fijar la altura hay que ver el candidato en varias clases a la vez, y una clasificación por conjunto no la ve.
3. **El rasgo `sensorial` no está en `catalog/traits.json`.** Lo proponen como rasgo nuevo los agentes de sábanas, cubrecolchones y fundas nórdicas, con definiciones distintas: la de fundas nórdicas incluye el olor. El tacto viene de D-105 y D-108.

## 5. Criterios de elección por clase

| Conjunto | Criterios | Intermedios | Generan |
|---|---|---|---|
| sabanas | 12 | 3 | transpiración, arrugas, origen de la fibra |
| botas | 9 | 3 | — |
| cojines | 1 | 1 | — |
| comida-perros | 7 | 3 | combinación, preparación |
| cubrecolchones | 10 | 4 | tacto |
| fundas-nordicas | 10 | 3 | abrigo, tacto |
| juguetes-perros | 10 | 1 | efecto calmante, nivel de actividad del perro |
| mantas | 8 | 4 | — |
| pantuflas | 11 | 3 | salud del pie |
| sofas | 14 | 5 | durabilidad, frescor, arrugas |
| sofas-cama | 17 | 6 | estilo |
| toallas | 7 | 3 | — |

En total salen 72 identificadores de criterio distintos.

**Vocabulario común:**
- `marca` aparece en 10 clases y no genera en ninguna (C4).
- `calidad` aparece en 9, siempre como intermedio cubierto.
- `material` aparece en 6, `color` en 5 y `comodidad` en 5.
- `tendencia` y `popularidad` aparecen en 3 y 2 clases y no generan nunca.

**Vocabulario que diverge** (observación):

1. **Sinónimos:**
   - `transpiracion`, `transpirabilidad` y `frescor` nombran la misma necesidad;
   - `tendencia` y `popularidad`, también;
   - `estilo` y `estilizacion`, también.
   - `material` aparece partido por pieza: `material-corte`, `material-suela`, `material-relleno`, `material-tapiceria`, `tejido`, `tipo-de-tejido` y `variedad-de-fibra`.
2. **Mismo criterio, veredicto distinto:**
   - `tacto` genera en cubrecolchones y fundas nórdicas, pero está cubierto en mantas.
   - `abrigo` genera en fundas nórdicas y está cubierto en mantas.
   - `frescor` genera en sofás y está cubierto en cubrecolchones.
   
   Parte de la diferencia es legítima, porque el catálogo de cada clase es distinto. Pero el vocabulario es la parte que el entrenamiento refina solo (D-114).
3. **`comodidad` como intermedio:** se usa como intermedio cubierto en 4 clases y como no intermedio en botas. Tres agentes dudan de si es intermedio o si no genera por C2. D-104 no la pone de ejemplo de intermedio.

## 6. Revisiones de requisitos existentes

Hay 18 revisiones en 9 conjuntos; tres conjuntos no proponen ninguna.

- **Estructurales, para el registro de taxo** (D-115):
  - sacar: 7, sobre cat.fundas-de-almohada/05 (en sábanas y en fundas nórdicas), cat.fundas-de-almohada/06, cat.protectores-de-colchon/03, cat.sofas/07 («Transpirable») y cat.toallas/05 («Zero twist»);
  - separar: 1;
  - partir por tema: 2;
  - mover: 1.
- **Reformular:** 7.
  - 4 son sobre inferidas: confirmarlas o revisarlas es el papel 3. Son inf/01 en sábanas y en fundas nórdicas, inf/02 en sábanas, y cat.sofas-cama/03 y /04, que también confirman.
  - 3 son sobre requisitos de las referencias: cat.calzado/23, cat.juguetes-para-perros/12 y cat.sofas/08.

Observaciones:

1. **Las prestaciones metidas en listas de otro tema se repiten en varias clases.** Son «Transpirable» en cat.sofas/07, «Zero twist» en cat.toallas/05 y, sin pregunta que les dé destino, «Antideslizante» en cat.sofas/15 y «Ergonómico» en cat.sofas/05. Es un patrón de las referencias que conviene que vea el próximo entrenamiento de taxo.
2. **`inf/01` no significa lo mismo en cada modelo.** En sábanas es el nivel de abrigo y en fundas nórdicas, la sujeción de la bajera. Por eso fundas nórdicas vuelve a proponer el nivel de abrigo como candidato N1. Los ids `inf/NN` se numeran por modelo, de modo que confirmar una inferida exige identificarla por su contenido, no por el número.

## 7. Dudas y divergencias repetidas

| # | Qué | Conjuntos | Afecta a |
|---|---|---|---|
| 1 | Una semilla de valores trae el producto vecino y el perímetro queda dudoso | cojines, juguetes-perros, fundas-nordicas, toallas, pantuflas | Semillas |
| 2 | Una semilla ambigua: «zapatillas» (deportivas o de casa), «bambú» (planta o fibra), «tela fresca» (transpirable o tacto fresco) | pantuflas, toallas, sofas | Semillas, perímetro |
| 3 | El rasgo `sensorial` no está en el índice | sabanas, cubrecolchones, fundas-nordicas | Rasgos (D-105) |
| 4 | `comodidad` y otros intermedios dudosos frente a C2 | botas, cubrecolchones, pantuflas, sofas, sofas-cama | Vocabulario, D-104 |
| 5 | Marcas o fabricantes «españoles»: a gen/17 (fabricante y su dirección) o a gen/20 (país de fabricación) | sofas, sofas-cama, pantuflas | Contraste, divergencia entre agentes |
| 6 | La altura del bloque de un candidato que se repite (cat.ropa-de-casa, cat.sofas o el bloque de la clase) | sabanas, mantas, cubrecolchones, fundas-nordicas, toallas, sofas, sofas-cama | Candidatos |
| 7 | El enfriamiento sale del nivel térmico y pasa al tacto | sabanas, fundas-nordicas | D-108 |
| 8 | Saber doméstico frente a cuidado declarado (cómo lavar o secar) | toallas, mantas, cubrecolchones | C2 |

## 8. Qué sugiere para lo que el entrenamiento refina

Son propuestas que nadie ha decidido. Se validan contra los casos de control (criterio 6) y no se aplican sin ellos.

**Estrategia de semillas:**
- El núcleo de una sola palabra, como «botas» o «cojines», puede quedarse sin caja. Una variante del núcleo con dos palabras, como el nombre de mercado con un calificativo genérico, rendiría más. Falta definir esa variante sin conocimiento externo, así que queda como cuestión, no como regla.
- Al elegir los valores, convendría descartar el valor que nombra otro producto por sí solo, como el relleno de un cojín o el bambú, o acompañarlo del nombre de la clase. Medida: la parte fuera del conjunto.

**Clics:** mantener 8. El piloto no apoya reducirlos: con 4 se perderían 10 de los 30 candidatos. Tampoco mide si más de 8 rinde, porque el clic 8 todavía trae preguntas.

**Vocabulario:**
- Normalizar los sinónimos de la sección 5 con un índice de criterios por analogía con el de rasgos (D-056).
- Fijar `comodidad` y `calidad` en ese índice como intermedios, si el usuario lo confirma.

**Contraste:**
- Pendiente de decisión del usuario: «español», ¿por gen/17 o por gen/20?
- Pendiente de decisión del usuario: añadir `sensorial` al índice de rasgos.
- Confirmar una inferida exige reconocerla por su contenido, no por su id.

**Calibración:** el piloto no mide ningún parámetro de la prueba (a). Hace falta el control.

## 9. Lo que falta

- **Criterio 6 de T-042:** los casos de control de PAA, con lo esperado de cada clase decidido por el usuario, sábanas incluida.
- **OQ-64:** las métricas del entrenamiento de PAA frente al control. Las de este informe son candidatas: parte fuera, preguntas únicas y útiles por búsqueda, candidatos por clic de primer apoyo y divergencias de vocabulario.
