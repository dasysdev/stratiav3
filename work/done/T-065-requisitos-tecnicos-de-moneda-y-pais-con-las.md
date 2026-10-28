---
id: T-065
title: Requisitos técnicos de moneda y país con las listas ISO de references
status: hecha
depends: T-062
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Desde T-062, references tiene ISO 4217 (iso-4217, SIX) e ISO 3166-1 alfa-2 (iso-3166-1, EU Vocabularies) con sus lectores (references.read.currency_codes, country_codes). Los requisitos de web-audit que comprueban priceCurrency, shippingRate.currency y addressCountry dan NE por no tener la lista: ponerlos al día con /web-reference.

## Criterios de aceptación

- [x] Los requisitos de ISO 4217 e ISO 3166-1 de web-audit/reference/requirements citan la fuente de references y ya no tienen como causa de NE la falta de la lista
- [x] La diferencia de la tabla de la UE con los códigos asignados de ISO (EU, IC, CP, CQ, reservados excepcionalmente) queda tratada en el método del requisito
- [x] web-audit/bin/reqs check correcto y pruebas en verde

## Resultado

Fichas iso-4217/iso-3166-1 (instrumento del sistema) y 13 requisitos de moneda y país contrastados con las listas fijadas; sin NE por lista; EU/IC/CP/CQ excluidos

## Notas

- 2026-10-28 web-audit/bin/reqs check lista iso-4217 e iso-3166-1 como «sin ficha» (aviso): con /web-reference, su ficha de fuente con las citas.
- 2026-10-28 Fichas iso-4217 e iso-3166-1 como instrumento del sistema, sin citas: XML/RDF sin texto citable, y las citas de un requisito han de ser de especificación aplicable; la fuente se nombra en el método (con su lector). 13 requisitos (ws-vocabulary/010; ws-consumer/055 111 118 131 162 170 211 239 278 295 298 314): método con la lista fijada, mayúsculas y sin espacios; 6 pierden el NE de lista no disponible. País: tabla UE 253 = 249 asignados + EU IC CP CQ (reservados excepcionalmente), excluidos en el método. Moneda: solo lista uno; los retirados (lista tres) no cumplen. Ojo: consumer.json y vocabulary.json llevaban cambios de T-055 sin confirmar; preservados (formato comprobado contra HEAD).
