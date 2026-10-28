# Catálogo curado de casos de entrenamiento

Conversación del usuario con Claude del 2026-10-28, recogida por Claude el mismo día. El usuario planteó el enfoque, Claude lo revisó y propuso criterios, y el usuario lo aprobó con un «sí». Sigue a la idea de entrenar con los modelos de una auditoría completa (`INTAKE 2026-10-28-audit-training-idea`, OQ-81).

## Palabras del usuario

> Otra idea que quiero que explores, y creo que es la que vamos a hacer, es mantener un catálogo de casos relevantes para entrenamiento. Cada caso evaluado podrá ser candidato a entrar al catálogo si el sistema lo considera (definir qué criterios aplican). Puedo añadir manualmente un caso que considere aunque no se haya auditado. Revisa este enfoque. Esto lo que busca es basarnos en un catálogo curado, no en cualquier ficha que hayamos auditado.

(Ortografía normalizada.)

## Revisión de Claude

- El entrenamiento solo aprende del **catálogo de casos**, en git y con versión. Se llega a él por la selección inicial (como la de El Corte Inglés), por un caso evaluado (auditoría o `/demand-model`) que el sistema admite por unos criterios, o por un caso que el usuario añade a mano aunque no se haya auditado. Una ficha auditada no entrena por haberse auditado: es candidata.
- **Es mejor que entrenar con todo lo auditado:**
  - Separa operar de aprender: el volumen de auditorías no decide el coste ni el sesgo del entrenamiento, que depende del tamaño del catálogo.
  - Resuelve que una tienda domine las reglas sin tocar la regla de mayoría: basta con limitar cuántos casos entran por tienda y clase.
  - Es reproducible: se sabe con qué casos se entrenó cada versión.
  - Es la evolución natural del catálogo de entrenamiento de D-053, que hoy es un sorteo único y pasaría a estar vivo y curado.

## Criterios propuestos por Claude

**Filtros** (los cumple todo candidato; los manuales, salvo el último):

- **F1 · Validez:** captura legítima y completa (sin desafío ni error) y modelo que pasa `bin/model check`.
- **F2 · Es una ficha de producto:** el clasificador le ha dado una clase.
- **F3 · Sin duplicados:** la misma tienda con la misma clave que un caso ya admitido queda fuera; así se excluyen variantes y productos hermanos.
- **F4 · Topes por clase y por tienda y clase:** de partida, 3 por clase (como en D-053) y 1 por tienda y clase. Son parámetros del usuario.

**Motivos de admisión** (el caso entra si aporta al menos uno):

- **A1 · Clase poco representada:** está por debajo de su tope.
- **A2 · Trae algo no compilado:** un bloque generado, requisitos sin regla, inferidas, un rasgo propuesto o una categoría sin bloque.
- **A3 · Contradice una regla compilada:** sus votos van contra una regla de importancia o relevancia; es la prueba de que la regla puede estar mal.
- **A4 · Deja huecos de cobertura:** declara hechos sin pregunta.
- **A5 · Tienda nueva para la clase:** alimenta también la regla de las dos tiendas de la información resolutiva.
- **A6 · Composición nueva:** una especialización o una combinación que el catálogo no tiene.

**Clase en su tope:** solo entra lo que aporta A2 o A3, sustituyendo a un caso que no aporte nada de eso. El caso sustituido se retira con registro; no se borra.

**Casos manuales:** pasan F1 y F2 y no tienen topes. Llevan origen «manual» y un motivo. Añadir un caso es dar material al entrenamiento, no revisar reglas, así que encaja en el marco.

**Registro de cada caso:** origen, motivo de admisión, fecha, tienda, la clave con la que entró y la versión del reglamento.

## Puntos que Claude señaló

1. **Curar no es elegir fichas buenas.** Si solo entran fichas completas, el clasificador nunca aprende con las pobres, que son justo las que más se auditan. Los motivos miden lo que el caso enseña, no la calidad de la ficha.
2. **Las fichas del catálogo no pueden vivir en `capture/var/`, que es desechable.** Un caso cuya ficha se pierde ya no se puede reclasificar. Hay que cambiar qué se conserva, solo para esas fichas.
3. **Votos ya hechos.** Un caso que viene de una auditoría trae una ejecución hecha; sigue valiendo el punto 2 de OQ-81 (que cuente como una de las dos).
4. **El catálogo no es el control.** Sus casos no tienen nada esperado. Un caso manual podría pasar a control si el usuario decide lo esperado; el punto 3 de OQ-81 (control por vertical) sigue en pie.
5. **Fichas de clientes.** Son públicas y se capturan con robots.txt y TDM comprobados. Usar para entrenar las de una tienda auditada es una cuestión de negocio o de contrato que decide el usuario.

Con esto, de OQ-81 sobra el punto 1 (el voto por tienda lo sustituyen F3 y F4), y el punto 4 pasa a ser el recorrido auditoría → candidato → admisión → catálogo.

## Pregunta de Claude y respuesta del usuario

> ¿Lo llevo al canon como decisión con estos criterios? Antes necesito que confirmes tres cosas: los topes de partida (3 y 1), que las fichas del catálogo se conserven, y si los casos manuales también se pueden retirar a mano.

> sí

— Usuario
