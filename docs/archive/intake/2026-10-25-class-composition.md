# Composición de la clase de estudio, condición 4 estricta y beneficios reclamados

*Update descrito por el usuario en la conversación del 2026-10-24 y 2026-10-25 y transcrito para su trazabilidad. Procede de la evaluación del método con tres casos más (tarea T-006): juego de toallas Azul 080 de burritoblanco.com (https://www.burritoblanco.com/juego-de-toallas-azul-080-p-1820-1879.html), sofá cama Luna de dos plazas de grupotodoplano.com (https://www.grupotodoplano.com/sofa-cama-luna-de-dos-plazas) y hueso mordedor de cuerda Tootoy! de kiwoko.com (https://www.kiwoko.com/perros/accesorios-para-perros/juguetes-para-perros/cuerdas/tootoy-hueso-mordedor-de-cuerda-verde-y-azul-para-perros/TOO43945_M.html). El usuario aceptó expresamente los bloques A, B y C y la recomposición del caso de las sábanas.*

## A. Composición de la clase

Modifica D-021, que decía que la clase general es «una» categoría de Shopify.

- El modelo de clase es un sistema de composición de requisitos. Cada componente (categoría de Shopify o especialización) aporta sus requisitos, y el modelo de demanda de la clase de estudio los integra sin duplicados.
- Si el producto abarca varias categorías de Shopify (por ejemplo, un juego con piezas de categorías distintas), la clase general es la composición de esas categorías, no su ancestro común. Palabras del usuario: «la clase debe ser una composición. Ten en cuenta que nos interesan requisitos de ambas categorías. De hecho el modelo de clase es justamente un sistema de composición de requisitos».
- Una categoría entra en la composición si aporta requisitos al producto o a alguna de sus piezas. En un juego, cada pieza es una entidad. Una categoría que no aporta requisitos propios no entra.
- La especialización «juego» aporta los requisitos del conjunto: qué piezas incluye, cuántas y en qué medidas.

## B. Condición 4 del criterio de especialización, lectura estricta

Precisa D-022. La dimensión debe existir en algún componente de la clase de estudio, en cualquiera de las tres referencias: atributos de la categoría de Shopify, nodo o PTD de Amazon, o categoría de Google. El apoyo en una categoría afín se anota en la ficha como evidencia complementaria, pero no basta por sí solo. Una distinción que no cumple la condición no se pierde: sus cuestiones quedan en la clase general como requisitos condicionados (la salida «conservar la clase y condicionar requisitos»).

## C. Beneficios reclamados

Amplía D-022. Un beneficio que el producto reclama (por ejemplo, «favorece la higiene dental») no es especialización, salvo que las referencias tengan un tipo de producto definido por él. Su fundamento se evalúa en la auditoría, no en la clase.

## D. Casos ilustrativos (no son clases aprobadas)

1. **Juego de sábanas Coralina**, recompuesto por piezas. Sustituye la composición «Sábanas + juego» del caso documentado en D-022:
   - Sábanas planas (Shopify hg-15-1-2-2; Amazon 3250024031 «Sábanas encimeras», PTD FLAT_SHEET) para la encimera.
   - Sábanas ajustables (hg-15-1-2-1; Amazon 3250023031 «Bajeras ajustables», PTD FITTED_SHEET) para la bajera.
   - Fundas de almohada (hg-15-1-8-2 → Google 2927; Amazon 3250027031, PTD PILLOWCASE) para las fundas.
   - Más «juego» (Amazon 3250028031, PTD BED_LINEN_SET), «uso invernal» y «tejido polar», con la coralina como valor. El resto del análisis anterior se mantiene, incluido el descarte de «Juegos de cama».
2. **Juego de toallas Azul 080**: juego de 3 toallas (bidé 30×50, lavabo 50×100, ducha 70×140), 100 % algodón, liso con cenefa jacquard.
   - Toallas de baño (Shopify hg-15-4-1-1 → Google 576) para la de ducha.
   - Toallas de mano (hg-15-4-5 → Google 4077, más amplia) para la de lavabo.
   - La de bidé queda provisional entre Toallas de mano y Toallitas (hg-15-4-1-2).
   - Más «juego» (Amazon 3244792031 «Juegos de toallas», PTD TOWEL con towel_form_type; Shopify no tiene atributo de piezas incluidas en Toallas).
   - Toallas de baño y Toallas de mano tienen los mismos atributos en Shopify (color, fabric, pattern, towel-weave) y el mismo PTD: la de mano entra porque aporta requisitos a otra pieza.
   - Algodón, cenefa jacquard y azul son valores. La especialización «uso de baño» que se consideró al subir a la categoría madre Toallas deja de ser necesaria.
3. **Sofá cama Luna de dos plazas**: tapizado en tela Victor, apertura italiana, revistero lateral, 2 cojines, sofá 92×131×94 cm y cama 131×180 cm, para uso diario o para invitados.
   - Clase de estudio: Sofás cama (Shopify fr-22-7 → Google 460, más amplia; Amazon «Sofás cama con patas» 56171664031 con PTD BED, y Salón > Sofás con PTD SOFA: sofa_type = Sofá cama, mattress, sleeping_area_dimensions).
   - «Sofás de dos plazas» (fr-22-4) no entra: tiene los mismos 9 atributos que Sofás cama, y en Amazon «dos plazas» es un valor de sofa_type y de seating_capacity, sin PTD propio.
   - El mecanismo de apertura italiana no cumple la condición 4 estricta (solo hay apoyo en Futones, futon-frame-conversion-mechanism); sus cuestiones sobre el colchón quedan como requisitos condicionados de Sofás cama.
   - Tela, color, revistero, cojines y medidas son valores.
   - Observaciones: lo que distingue a Sofás cama solo lo recoge Amazon; en Shopify, las hojas tienen menos atributos que la madre (Sofás tiene 17 y sus hijas, 9).
4. **Hueso mordedor de cuerda Tootoy!**: fibra de polipropileno trenzada, para morder, lanzar o tirar, 20 cm, apto para todos los tamaños, con efecto declarado de higiene dental.
   - Composición: Juguetes para perros (Shopify ap-2-3-7 = Google 5010; Amazon 13441958031) + «cuerda» (Shopify dog-toy-type = Soga; Amazon 13442235031 «Cuerdas»; PTD PET_TOY pet_toy_type = Juguete para tirar; añade deshilachado, ingestión de fibras, lavado) + «mordedor» (Shopify Mordedor y Mordedor agresivo; Amazon 13442241031 «Juguetes para morder»; añade resistencia a la mordida).
   - Tirar y lanzar quedan absorbidos por «cuerda» (condición 5).
   - La higiene dental es un beneficio reclamado (bloque C): «Dental» solo existe en las referencias para snacks.
   - Polipropileno, forma de hueso, 20 cm y color son valores.

## E. Observaciones de la evaluación (no son reglas)

- Google solo confirmó la clase general en todos los casos.
- Amazon aportó el anclaje más fino (juegos, cuerdas, mordedores) y PTD las dimensiones (seasons, pet_toy_type, mattress).
- El «juego» se repite como especialización, y en Shopify solo aparece como atributo en algunas categorías (Sábanas sí, Toallas no).
- El material habitual de la clase (algodón, tela, polipropileno) queda como valor.
- El método no fuerza especializaciones (sofá cama).
