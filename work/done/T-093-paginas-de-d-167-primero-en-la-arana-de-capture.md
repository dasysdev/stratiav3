---
id: T-093
title: Páginas de D-167 primero en la araña de capture
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Con la prioridad de fichas (D-204), la araña también encuentra y captura las páginas de la auditoría de D-167: las políticas (envíos, devoluciones, contacto, aviso legal), localizadas en los enlaces de la portada, y la categoría inmediata de cada ficha, por sus migas. Van antes que las fichas. Petición del usuario (2026-10-29).

## Criterios de aceptación

- [x] Con un tope que corta el rastreo de un sitio local, la araña captura las políticas de la portada y la categoría de cada ficha capturada
- [x] Cada página elegida así registra para qué página de D-167 se eligió; el manifiesto lista esos objetivos y si se capturaron
- [x] La reanudación conserva esos objetivos; canon y README al día; pruebas en verde

## Resultado

La araña captura primero las políticas y va categoría a categoría (paginación y fichas); todas las categorías (D-215)

## Notas

- 2026-10-29 Hecho: políticas de la portada primero (audit); después categoría a categoría: categoría, paginación mientras la página liste fichas, fichas listadas (links.json.gz de las páginas del grupo), siguiente categoría (migas a cualquier nivel, después por forma); categoría capturada antes de saberse se recorre sin pedirla ({group} en el diario). Usuario rechazó la alternancia ficha/categoría. burritoblanco 60 URL: portada, 3 políticas, «lo más nuevo» con 5 páginas y 49 fichas. Canon D-215 (enmienda D-167 y D-204). Chrome huérfano en 9297 rompía test_profiles; la araña usa 9295. 259 pruebas en verde.
