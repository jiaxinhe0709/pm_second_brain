# EDICOM API evidence

## Evidence status

Status: no authoritative public endpoint-level documentation was located during the initial discovery pass.

Retrieved: 2026-07-27

## What is not yet confirmed

- EDICOM product and API in contractual scope.
- REST, SOAP, AS2, SFTP, managed connector, or other integration protocol.
- Authentication, certificates, network allow-listing, and environment setup.
- Customer/legal-entity provisioning.
- Spain invoice formats and supported inbound/outbound lifecycle.
- Webhooks, polling, acknowledgements, and reconciliation.
- Idempotency, rate limits, payload limits, and SLA.
- Deregistration and historical access.

## Required PM/vendor action

Request from EDICOM:

1. Spain e-invoicing solution architecture and product name.
2. Current API/integration guide and version history.
3. OpenAPI/WSDL/schema/Postman artefacts as applicable.
4. Sandbox onboarding and non-production credentials through an approved secret channel.
5. Status, acknowledgement, and error catalogue.
6. Webhook/callback or polling specification.
7. Security, certificate, IP allow-listing, data-residency, and retention information.
8. Rate limits, volume model, SLA, support, and escalation contacts.
9. Registration, route change, deregistration, and historical-invoice rules.
10. Permission to store technical artefacts in the Sage repository.

## PRD treatment

`PRD-SEI-206` must remain at discovery status. No EDICOM endpoint, protocol, or authentication requirement should be marked confirmed until provider evidence is received.

