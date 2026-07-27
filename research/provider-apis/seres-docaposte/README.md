# SERES (Docaposte) API evidence

## Evidence status

Status: public product information confirms ERP/API integration and invoice capabilities, but no authoritative public endpoint reference was located.

Retrieved: 2026-07-27

## Official public source

| Source | URL |
|---|---|
| SERES e-Factura product page | https://www.groupseres.com/e-factura |

## Confirmed public capability snapshot

SERES publicly states that its e-Factura solution:

- sends and receives electronic invoices;
- supports structured formats including CEFACT, UBL, EDIFACT, and Facturae;
- integrates and synchronises with ERPs through APIs;
- connects with public and private platforms;
- handles invoice states including acceptance/rejection and payment;
- supports multi-company usage and electronic archive/access capabilities.

These are product claims, not an endpoint contract.

## Information still required

- Exact SERES/Docaposte product and API in scope.
- API/protocol specification and environment base addresses.
- Authentication, certificates, allow-listing, and tenant provisioning.
- Spain-specific registration and route model.
- Endpoint and schema catalogue for outbound, inbound, statuses, correction, cancellation, and retrieval.
- Webhook/polling behaviour and security.
- Idempotency, rate limits, payload limits, acknowledgements, and reconciliation.
- Archive and historical access after route deactivation.
- SLA, support, data residency, retention, and security evidence.
- Machine-readable specifications and permission to store them.

## Required PM/vendor action

Request an API discovery pack and sandbox workshop from the SERES technical contact. `PRD-SEI-207` must distinguish public product claims from provider-confirmed technical requirements.

