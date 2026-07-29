---
id: PRD-SEI-207
title: Provider Integration — SERES (Docaposte)
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
  - research/provider-apis/seres-docaposte/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "855180245"
  title: Provider Integration — SERES (Docaposte)
---

# Provider Integration — SERES (Docaposte)

## Summary

Connect eligible Spanish e-invoicing customers to SERES (Docaposte) through the shared private-platform connection, routing, and resilience foundation.

## Problem

Sage requires a consistent SERES integration for its ERPs, but the exact service boundary, onboarding model, supported document journeys, and operating constraints require provider discovery.

SERES publicly describes sending and receiving electronic invoices, API synchronisation with ERPs, public/private platform connectivity, multiple structured formats, invoice status exchange, multi-company operation, and document access/archiving. These are credible product capabilities but not an endpoint contract. Technical implementation must wait for the provider API pack.

## Evidence and confidence

Evidence source: `research/provider-apis/seres-docaposte/README.md`

| Area | Current confidence |
|---|---|
| Sending and receiving e-invoices | Confirmed public product claim |
| ERP integration and synchronisation by API | Confirmed public product claim |
| CEFACT, UBL, EDIFACT, and Facturae support | Confirmed public product claim |
| Acceptance/rejection and payment-state management | Confirmed public product claim |
| Public and private platform connectivity | Confirmed public product claim |
| Exact API, authentication, endpoints, and schemas | Unconfirmed |
| Spain registration, reconciliation, limits, and SLA | Unconfirmed |

## Goals

- Confirm the relevant SERES and Docaposte service scope.
- Establish secure sandbox and production connectivity.
- Support eligible inbound and outbound journeys.
- Translate provider identifiers, statuses, and errors.
- Provide monitoring, reconciliation, and controlled deactivation.

## Non-goals

- Features outside the shared Phase 2 scope.
- Separate ERP-specific integrations.
- Private-to-private switching.
- Unrelated Docaposte services or country implementations.

## Users and use cases

- ERP products configure SERES through shared APIs.
- Customers or accountants complete required provider onboarding.
- Invoice services exchange supported documents.
- Operations inspect and recover failed work.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | Discovery must identify the authoritative SERES/Docaposte product and API. |
| FR2 | Supported Spain formats, directions, and lifecycle operations must be declared. |
| FR3 | The adapter must follow the shared capability contract. |
| FR4 | Provider credentials, certificates, and identifiers must use approved secure handling. |
| FR5 | Sandbox and production must be isolated. |
| FR6 | Provider statuses and errors must map to stable Sage categories. |
| FR7 | Registration and invoice operations must have idempotency or duplicate protection. |
| FR8 | Webhook and/or polling processing must tolerate missed and duplicate events. |
| FR9 | Reconciliation and provider-health functions must be implemented where available. |
| FR10 | Route deactivation and provider deregistration must remain separate actions. |

### Customer and multi-company setup

| ID | Requirement |
|---|---|
| FR11 | Discovery must map SERES organisation, account, mailbox, and legal-entity concepts to Sage resources. |
| FR12 | Accountant or multi-company access must preserve tenant and legal-entity isolation. |
| FR13 | Manual provider onboarding steps must be visible as pending or action-required rather than hidden outside the workflow. |
| FR14 | Connection readiness must be declared separately by invoice direction and format where capabilities differ. |

### Formats and transformation

| ID | Requirement |
|---|---|
| FR15 | Sage and SERES must agree the canonical exchange format and version for each supported journey. |
| FR16 | CEFACT, UBL, EDIFACT, and Facturae support must not imply that every format is available through the contracted API. |
| FR17 | Transformation validation errors must identify source field, target rule, severity, and responsible actor where provider evidence permits. |
| FR18 | Original submitted/received artefacts and SERES references must remain traceable. |

### Invoice and lifecycle operations

| ID | Requirement |
|---|---|
| FR19 | Outbound submission must distinguish accepted-by-SERES, validated, routed, delivered, rejected, and other confirmed stages. |
| FR20 | Inbound ingestion must be incremental, idempotent, and recoverable. |
| FR21 | Acceptance, rejection, and payment states must map to the shared lifecycle without discarding provider status codes. |
| FR22 | Correction and cancellation support must be confirmed per format and route. |
| FR23 | Historical invoices must remain accessible for the agreed continuity and retention period after route deactivation. |

### API and resilience

| ID | Requirement |
|---|---|
| FR24 | Authentication, signing, certificate, webhook/callback, and network security must be confirmed from provider documentation. |
| FR25 | Every mutating operation must have documented idempotency or reconcile-before-retry behaviour. |
| FR26 | The adapter must support authoritative status retrieval or an agreed operational reconciliation procedure. |
| FR27 | Provider throttling, size limits, batch limits, and maintenance windows must be reflected in Sage controls. |
| FR28 | SERES operational incidents must use the shared provider health and escalation model. |
| FR29 | Route deactivation must not automatically revoke archive access or deregister the customer. |
| FR30 | Production use must pin a supported API/schema version and monitor provider change notices. |

## Provisional journeys requiring provider validation

### Establish SERES connection

1. Create draft connection for legal entity and environment.
2. Complete SERES tenant/mailbox provisioning.
3. Supply credentials, certificates, endpoints, or network configuration securely.
4. Confirm contracted inbound/outbound formats and capabilities.
5. Complete connectivity and provider certification tests.
6. Mark direction-specific capabilities ready.
7. Activate routes only through the shared transition workflow.

### Send invoice

1. Resolve SERES route and selected format.
2. Transform and validate canonical invoice.
3. Submit through confirmed SERES API/protocol.
4. Store document and transmission references.
5. Consume acknowledgements and business lifecycle states.
6. Reconcile missing or ambiguous outcomes.

### Receive invoice

1. Receive provider event/document or perform incremental retrieval.
2. Validate source and integrity.
3. Deduplicate.
4. Retain original format and map canonical invoice.
5. Apply acceptance/rejection/payment lifecycle events according to confirmed responsibility.

## Required provider artefacts

- SERES/Docaposte product and API scope;
- API/protocol reference and machine-readable schemas;
- sandbox and production onboarding;
- authentication, certificates, signing, and network security;
- supported direction/format matrix;
- statuses, acknowledgements, and errors;
- webhook/callback or polling specification;
- idempotency, reconciliation, rate, batch, attachment, and payload limits;
- archive, retention, historical access, and deregistration;
- versioning, SLA, support, and escalation.

## Acceptance criteria

1. Public product claims are not treated as endpoint commitments without provider evidence.
2. Multi-company setup preserves legal-entity isolation.
3. Direction and format capabilities are visible before route activation.
4. Representative outbound and inbound invoices retain SERES references and original formats.
5. Acceptance, rejection, and payment states map without lifecycle regression.
6. Duplicate events/documents are processed once.
7. Ambiguous submissions are reconciled before retry.
8. Archive access is tested after route deactivation.
9. Credential/certificate failures are actionable and do not leak secrets.
10. Production remains gated on the complete technical and operational pack.

## User experience

The shared onboarding flow must collect SERES-specific configuration, validate readiness, and show actionable status without exposing secrets or avoidable protocol detail.

## Metrics

- Successful connection and registration rate.
- Successful invoice journey rate.
- Status and error mapping coverage.
- Duplicate and unreconciled outcome count.
- Mean recovery time.

## Rollout

1. Confirm SERES/Docaposte service scope.
2. Complete discovery and security assessment.
3. Obtain sandbox access.
4. Implement representative journeys.
5. Pass resilience and operational checks.
6. Pilot and expand by agreed cohort.

### Provider readiness gate

- Named SERES technical owner and contracted product confirmed.
- API pack, schemas, sandbox, and storage permission obtained.
- Direction/format/status matrix and registration flow approved.
- Security, idempotency, reconciliation, limits, archive, SLA, and support approved.

## Risks

- SERES and Docaposte naming obscures the technical service boundary.
- Customer provisioning includes manual provider steps.
- Status or acknowledgement semantics differ from shared assumptions.
- Production enablement has long lead times.

## Open questions

1. Which SERES/Docaposte service and API are in scope?
2. Which formats, directions, and lifecycle operations are supported in Spain?
3. What tenant, authentication, certificate, and registration processes apply?
4. What webhook, polling, idempotency, and reconciliation facilities are available?
5. What limits and service levels apply?
6. How is historical lifecycle access retained?
7. Is SERES a candidate for the reference integration?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | SERES (Docaposte) is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
