---
id: PRD-SEI-204
title: Spain B2B Router Integration
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-07-27
updated: 2026-07-27
reviewers: []
related:
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/b2b-router/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "855180241"
  title: B2B Router integration
---

# Spain B2B Router Integration

## Summary

Connect eligible Spanish e-invoicing customers to B2B Router through the shared private-platform connection, routing, and resilience foundation.

## Problem

Sage requires a consistent way to onboard customers to B2B Router and exchange invoices without exposing provider-specific behaviour to every Sage ERP. Provider capabilities and constraints have not yet been confirmed and must be established during discovery.

B2B Router exposes public REST documentation covering accounts, contacts, directory lookup, transports, invoice creation/import, invoice retrieval, document rendering, attachments, webhooks, and Spain tax-reporting functions. Phase 2 must identify which of these capabilities implement private B2B exchange and avoid conflating them with VeriFactu or other tax-reporting services.

## Evidence and confidence

Evidence source: `research/provider-apis/b2b-router/README.md`

| Area | Current confidence |
|---|---|
| Public REST API availability | Confirmed |
| API-key authentication and API version header | Confirmed; production convention to validate |
| Sandbox/staging and production environments | Confirmed |
| Account, contact, directory, transport, and invoice resources | Confirmed |
| Issued and received invoice concepts | Confirmed |
| Webhook capability | Confirmed; delivery guarantees to validate |
| Spain private-platform registration and routing sequence | Unconfirmed |
| Contractual service limits and SLA | Unconfirmed |

## Goals

- Confirm B2B Router's supported Spain capabilities.
- Establish secure sandbox and production connections.
- Support eligible inbound and outbound flows through the shared adapter contract.
- Translate provider lifecycle statuses and errors into the Sage model.
- Support reconciliation, monitoring, and controlled deactivation.

## Non-goals

- Features not supported by the shared Phase 2 scope.
- Direct provider integration independently implemented by each Sage ERP.
- Private-to-private provider switching.
- Provider-specific commercial contracting.

## Users and use cases

- ERP products initiate B2B Router connection setup through shared APIs.
- Customers or accountants supply the required provider configuration.
- Invoice services send or receive eligible documents.
- Operations reconcile failures without accessing secrets.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | Discovery must document supported Spain document types, directions, and customer segments. |
| FR2 | The adapter must implement only declared shared capabilities. |
| FR3 | Credentials must be stored through an approved secure mechanism and referenced by ID. |
| FR4 | Sandbox and production configuration must be isolated. |
| FR5 | External customer, registration, invoice, and event identifiers must be retained. |
| FR6 | Provider statuses and errors must map to stable Sage categories without discarding diagnostic detail. |
| FR7 | Submission and registration operations must use provider idempotency or Sage duplicate protection. |
| FR8 | Webhook and/or polling behaviour must recover missed or duplicate events. |
| FR9 | The adapter must expose reconciliation and health capabilities where provider APIs permit. |
| FR10 | Disablement and deregistration must require explicit authorised actions. |

### Account and legal-entity mapping

| ID | Requirement |
|---|---|
| FR11 | Discovery must determine whether each Sage legal entity maps to a B2B Router account, project, subaccount, or another provider resource. |
| FR12 | Sage must retain the stable B2B Router account identifier without using customer-visible names as keys. |
| FR13 | Accountant-managed legal entities must remain segregated according to B2B Router ownership and privacy capabilities. |
| FR14 | Test data must use non-production accounts and must not use unrelated real-party tax identifiers. |

### Directory, contact, and transport

| ID | Requirement |
|---|---|
| FR15 | Where directory lookup is used, Sage must store the lookup input, result, provider schemes, resolved transport, and observation time. |
| FR16 | A directory result must not be treated as the authoritative Spain route until confirmed by the local-team consultation. |
| FR17 | Contact creation or embedded-contact processing must be deterministic and protected against duplicates. |
| FR18 | Sage must map B2B Router transport configuration to the shared connection capability model rather than expose transport codes as Sage routes. |
| FR19 | A transport must be validated before the connection becomes eligible for route activation. |

### Outbound invoice flow

| ID | Requirement |
|---|---|
| FR20 | The adapter must support the approved create/import invoice operation for the selected payload strategy. |
| FR21 | Invoice creation and sending must remain distinguishable where B2B Router processes sending asynchronously. |
| FR22 | Sage must retain B2B Router invoice ID, account ID, selected transport, document type, and relevant tax-report references separately. |
| FR23 | Provider validation failures must map to actionable Sage validation errors without retry. |
| FR24 | Sage must retrieve the resulting invoice state and legal document reference where required for audit or customer access. |
| FR25 | The decision to use B2B Router JSON or import a recognised XML format must be recorded before implementation. |

### Inbound and lifecycle flow

| ID | Requirement |
|---|---|
| FR26 | Discovery must confirm the authoritative received-invoice API and incremental retrieval or notification model. |
| FR27 | Webhook events must be authenticated, deduplicated, correlated to provider invoices, and tolerant of reordering. |
| FR28 | Missed webhook events must be recoverable through invoice listing/retrieval or an agreed reconciliation mechanism. |
| FR29 | Sage must not regress an invoice lifecycle state solely because an older provider event arrives later. |
| FR30 | Legal document and attachment retrieval must follow content-size, security-scanning, retention, and access-control requirements. |

## Proposed API mapping

The paths below are confirmed from public documentation but remain subject to the selected API version and commercial product.

| Sage capability | B2B Router operation |
|---|---|
| List provider accounts | `GET /accounts` |
| Configure transport | `POST /accounts/{ACCOUNT_ID}/transports` |
| Resolve directory entry | `GET /directory/{country}/{identifier}` |
| List contacts | `GET /accounts/{ACCOUNT_ID}/contacts` |
| Create contact | `POST /accounts/{ACCOUNT_ID}/contacts` |
| Create/import invoice | `POST /accounts/{ACCOUNT_ID}/invoices` |
| List invoices | `GET /accounts/{ACCOUNT_ID}/invoices` |
| Retrieve invoice | `GET /invoices/{INVOICE_ID}` |
| Render selected format | `GET /invoices/{INVOICE_ID}/as/{document_type_code}` |
| Retrieve legal document | `GET /invoices/{INVOICE_ID}/as/legal` |
| Add attachment | `POST /invoices/{INVOICE_ID}/add_attachment` |

## Detailed journeys

### Establish connection

1. Sage creates a draft B2B Router connection for one legal entity and environment.
2. Authorised credentials are supplied through secure storage.
3. Adapter retrieves or validates the intended account.
4. Adapter discovers required identifier schemes and transport capabilities.
5. Required transport is configured or verified.
6. Sage records provider identifiers and connection capability.
7. Connection becomes ready but no Sage route changes automatically.

### Send invoice

1. Shared routing resolves the B2B Router connection.
2. Sage maps the canonical invoice to the approved JSON or XML strategy.
3. Adapter creates/imports the invoice using a stable correlation identity.
4. B2B Router validates and, where requested, queues the invoice for sending.
5. Sage stores the provider invoice ID and initial state.
6. Sage consumes webhook or retrieval updates until the required terminal state.
7. Sage makes the legal document or reference available according to retention rules.

### Receive invoice

1. B2B Router receives an invoice for the configured account.
2. Sage receives a webhook or detects it through incremental retrieval.
3. Adapter deduplicates using provider identity.
4. Sage imports the original document and mapped canonical data.
5. Sage records B2B Router as the original connection.
6. Subsequent lifecycle events use that original context after any later route change.

## Failure behaviour

| Scenario | Expected behaviour |
|---|---|
| API key rejected | Mark action required; do not retry until credential change |
| Account or transport missing | Keep connection non-ready and return setup action |
| Invoice returns validation error | Return mapped field errors; do not retry unchanged payload |
| Create/send request times out | Retrieve using correlation/provider identity before resubmission |
| Webhook duplicated | Acknowledge safely and process once |
| Directory returns no result | Follow approved no-route policy; do not invent a transport |
| Attachment exceeds applicable limit | Reject before provider submission where limit is known |
| Provider degradation | Apply shared queue, retry, circuit-breaking, and incident handling |

## Security and non-functional requirements

- API keys must be held in approved secret storage and never returned through client APIs.
- Staging and production credentials and account IDs must remain isolated.
- Provider requests must carry Sage correlation and the selected B2B Router API version.
- Logs must redact credentials, invoice contents, and download URLs where those URLs grant access.
- Pagination must be used for list/reconciliation operations.
- The selected version must be pinned and monitored through the provider changelog.

## Acceptance criteria

1. A Sage legal entity can establish a validated non-production B2B Router connection without activating a route.
2. Account, transport, and capability identifiers are visible to authorised operations without exposing API keys.
3. A representative outbound invoice is created, sent, retrieved, and correlated end to end.
4. A representative inbound invoice is ingested exactly once and retains B2B Router context.
5. Validation errors are actionable and not automatically retried.
6. A timed-out mutation is reconciled before resubmission.
7. Duplicate and out-of-order webhook tests do not duplicate or regress invoice state.
8. Test and production data and credentials cannot be mixed.
9. A public/private route transition does not alter existing B2B Router invoice context.
10. Disablement and deregistration follow separate authorised workflows.

## User experience

The shared onboarding experience must show B2B Router-specific data requirements, validate them before activation, and distinguish configuration, registration, readiness, and active route status.

## Metrics

- Successful connection rate.
- Successful invoice submission and receipt rate by operation.
- Provider status mapping coverage.
- Duplicate and unreconciled outcome count.
- Mean time to identify and recover provider failures.

## Rollout

1. Complete provider discovery checklist.
2. Obtain sandbox access and test credentials through approved channels.
3. Implement connection and capability discovery.
4. Validate representative inbound and outbound journeys.
5. Pass shared resilience and operational readiness checks.
6. Pilot with an agreed ERP/customer cohort.

### Provider readiness gate

- Intended B2B Router subscription and transaction model confirmed.
- Spain private B2B exchange and registration scope confirmed.
- Authentication, webhook security, idempotency, limits, retention, and SLA documented.
- API version and payload strategy approved.
- Sandbox evidence covers inbound, outbound, validation, timeout, duplication, and reconciliation.

## Risks

- Provider capability differs from the shared assumptions.
- Sandbox behaviour differs from production.
- Status or error mappings lose important semantics.
- Registration or invoice submission is not safely idempotent.

## Open questions

1. Which Spain formats, directions, and lifecycle operations are supported?
2. What authentication and customer-registration models are used?
3. Are webhooks available and what delivery guarantees apply?
4. Which idempotency and reconciliation facilities are available?
5. What rate limits, payload limits, and service levels apply?
6. How are historical invoices accessed after route deactivation?
7. Is B2B Router a candidate for the reference integration?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | B2B Router is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
