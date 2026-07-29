---
id: PRD-SEI-208
title: Provider Integration — ZeroComa
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-07-27
updated: 2026-07-29
reviewers: []
related:
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/zerocoma/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "855180249"
  title: Provider Integration — ZeroComa
---

# Provider Integration — ZeroComa

## Summary

Connect eligible Spanish e-invoicing customers to ZeroComa through the shared private-platform connection, routing, and resilience foundation.

## Problem

Sage requires a reusable ZeroComa integration for its ERPs. ZeroComa's exact Spain capabilities, onboarding process, API model, and operational constraints must be verified during discovery.

ZeroComa publicly describes B2B invoice issuance and receipt, ERP integration, traceability, conservation, VeriFactu, reporting, and AEAT connectivity. The public material does not expose an endpoint contract or prove which capabilities form the Phase 2 private-platform service. The PRD therefore separates confirmed product claims from technical requirements requiring vendor evidence.

## Evidence and confidence

Evidence source: `research/provider-apis/zerocoma/README.md`

| Area | Current confidence |
|---|---|
| B2B invoice issuance and receipt | Confirmed public product claim |
| ERP integration, traceability, and conservation | Confirmed public product claim |
| VeriFactu/reporting and AEAT connectivity | Confirmed public product claim; separate scope |
| Private-platform API role | Unconfirmed |
| API/protocol, authentication, endpoints, and schemas | Unconfirmed |
| Registration, lifecycle, reconciliation, limits, and SLA | Unconfirmed |

## Goals

- Confirm ZeroComa's supported Spanish e-invoicing capabilities.
- Establish secure sandbox and production connectivity.
- Support eligible inbound and outbound journeys.
- Map provider identifiers, statuses, and errors.
- Provide monitoring, reconciliation, and controlled deactivation.

## Non-goals

- Features outside the shared Phase 2 scope.
- Direct ERP-specific provider integrations.
- Private-to-private switching.
- Unsupported ZeroComa services or countries.

## Users and use cases

- ERP products configure ZeroComa through common APIs.
- Customers or accountants provide required provider setup.
- Invoice services exchange supported documents.
- Operations diagnose and reconcile failures.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | Discovery must document the authoritative ZeroComa product and API scope. |
| FR2 | Supported formats, directions, document types, and lifecycle operations must be declared. |
| FR3 | The adapter must implement the shared capability contract. |
| FR4 | Credentials, certificates, and external identifiers must use approved secure handling. |
| FR5 | Sandbox and production must be isolated. |
| FR6 | Provider statuses and errors must map to stable Sage categories. |
| FR7 | Idempotency or duplicate protection must apply to registration and invoice operations. |
| FR8 | Webhook and/or polling processing must recover missed and duplicate events. |
| FR9 | Reconciliation and provider-health functions must be implemented where available. |
| FR10 | Route deactivation and external deregistration must be separately controlled. |

### Scope separation

| ID | Requirement |
|---|---|
| FR11 | Discovery must identify the ZeroComa product specifically providing private B2B exchange. |
| FR12 | Private invoice exchange, VeriFactu, tax reporting, AEAT communication, and archive services must be represented as separate capabilities. |
| FR13 | Phase 2 must not activate or purchase an unrelated ZeroComa capability implicitly. |
| FR14 | Capability dependencies and commercial packaging must be documented before estimation. |

### Connection and onboarding

| ID | Requirement |
|---|---|
| FR15 | ZeroComa tenant, customer, legal-entity, mailbox, and connection concepts must map to stable Sage resources. |
| FR16 | Credentials, certificates, signing keys, endpoint configuration, and network controls must use approved secure handling. |
| FR17 | Manual onboarding or provider approval must be represented as explicit workflow states. |
| FR18 | Connection readiness must be confirmed independently for inbound, outbound, status, and archive capabilities. |
| FR19 | Route activation must not occur until private-platform registration and capability are verified. |

### Invoice exchange and lifecycle

| ID | Requirement |
|---|---|
| FR20 | Supported canonical and provider formats and versions must be documented and tested. |
| FR21 | Outbound invoice submission must retain ZeroComa document, transmission, and lifecycle references. |
| FR22 | Inbound ingestion must support secure, incremental, idempotent processing. |
| FR23 | Validation, routing, delivery, rejection, acceptance, payment, correction, and cancellation states must be confirmed rather than inferred. |
| FR24 | The adapter must retain original network context after later route changes. |
| FR25 | Conservation/archive access must follow the approved retention and customer-access model. |

### Resilience and operations

| ID | Requirement |
|---|---|
| FR26 | Each mutating provider operation must have a documented idempotency or reconciliation treatment. |
| FR27 | Webhook/callback, polling, mailbox, or file delivery behaviour must be documented, authenticated, and monitored. |
| FR28 | Provider status and error codes must map to Sage categories while retaining raw evidence. |
| FR29 | Rate, batch, payload, attachment, maintenance, and availability limits must be enforced or monitored. |
| FR30 | Deregistration, credential revocation, archive access, and route deactivation must remain separate lifecycle actions. |

## Provisional journeys requiring provider validation

### Establish ZeroComa private-platform connection

1. Create a draft connection.
2. Confirm private B2B product entitlement and legal-entity provisioning.
3. Supply credentials/certificates securely.
4. Validate connectivity and provider registration in sandbox.
5. Confirm enabled directions, formats, status, and archive capabilities.
6. Mark the connection ready without altering public routes.

### Send invoice

1. Resolve the ZeroComa private route.
2. Transform and validate using the approved format.
3. Submit through the confirmed API/protocol.
4. Retain external document and transmission references.
5. Process confirmed provider lifecycle events.
6. Reconcile ambiguous outcomes before retry.

### Receive invoice

1. Receive a trusted notification/document or poll the confirmed source.
2. Validate integrity and legal-entity scope.
3. Deduplicate and store original context.
4. Map canonical invoice and lifecycle.
5. Preserve ZeroComa context through future route changes.

## Required provider artefacts

- product architecture separating private B2B, VeriFactu, reporting, AEAT, and archive;
- API/protocol specification and schemas;
- sandbox and production onboarding;
- authentication, certificate, signing, and network controls;
- supported formats, directions, and lifecycle matrix;
- status and error catalogue;
- webhook/polling/mailbox/file-exchange specification;
- idempotency and reconciliation;
- limits, retention, archive, deregistration, SLA, and support;
- permission to retain technical artefacts.

## Acceptance criteria

1. Private B2B capability is identified independently from VeriFactu and tax reporting.
2. All implementation behaviour is traceable to provider evidence.
3. Connection readiness is independently represented by direction and capability.
4. Representative inbound and outbound flows pass in sandbox.
5. Duplicate documents/events do not create duplicate invoices or states.
6. Ambiguous mutations are reconciled before retry.
7. Provider errors map to actionable Sage categories.
8. Archive access and historical lifecycle are verified after route deactivation.
9. Test and production credentials and data remain isolated.
10. Production remains gated until technical, security, operational, and commercial evidence is complete.

## User experience

The common onboarding flow must incorporate ZeroComa-specific configuration and validation while preserving shared connection, registration, readiness, and route terminology.

## Metrics

- Successful connection and registration rate.
- Successful invoice operation rate.
- Status and error mapping coverage.
- Duplicate and unreconciled outcome count.
- Operational recovery time.

## Rollout

1. Complete provider and product discovery.
2. Confirm security and data-processing requirements.
3. Obtain sandbox access.
4. Implement representative journeys.
5. Pass shared resilience and operational readiness checks.
6. Pilot and expand with an agreed cohort.

### Provider readiness gate

- ZeroComa private B2B product and commercial entitlement confirmed.
- Technical owner, API pack, schemas, sandbox, and storage permission obtained.
- Capability separation and direction/status matrix approved.
- Security, idempotency, reconciliation, limits, retention, deregistration, SLA, and support approved.

## Risks

- Limited or changing technical documentation.
- Manual provisioning or certification steps.
- Provider lifecycle semantics differ from the shared model.
- Sandbox coverage is insufficient for failure testing.

## Open questions

1. Which ZeroComa product and API are authoritative for this integration?
2. Which Spanish formats, directions, and lifecycle operations are supported?
3. What authentication, certificate, and registration model applies?
4. What webhook, polling, idempotency, and reconciliation facilities exist?
5. What rate, payload, commercial, and SLA limits apply?
6. How is historical invoice access maintained after route changes?
7. Is ZeroComa a candidate for the reference integration?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | ZeroComa is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
