---
id: T-065
title: Requisitos técnicos de moneda y país con las listas ISO de references
status: pendiente
depends: T-062
milestone: codigo
created: 2026-10-28
---

## Objetivo

Desde T-062, references tiene ISO 4217 (iso-4217, SIX) e ISO 3166-1 alfa-2 (iso-3166-1, EU Vocabularies) con sus lectores (references.read.currency_codes, country_codes). Los requisitos de web-audit que comprueban priceCurrency, shippingRate.currency y addressCountry dan NE por no tener la lista: ponerlos al día con /web-reference.

## Criterios de aceptación

- [ ] Los requisitos de ISO 4217 e ISO 3166-1 de web-audit/reference/requirements citan la fuente de references y ya no tienen como causa de NE la falta de la lista
- [ ] La diferencia de la tabla de la UE con los códigos asignados de ISO (EU, IC, CP, CQ, reservados excepcionalmente) queda tratada en el método del requisito
- [ ] web-audit/bin/reqs check correcto y pruebas en verde

## Notas

- 2026-10-28 web-audit/bin/reqs check lista iso-4217 e iso-3166-1 como «sin ficha» (aviso): con /web-reference, su ficha de fuente con las citas.
