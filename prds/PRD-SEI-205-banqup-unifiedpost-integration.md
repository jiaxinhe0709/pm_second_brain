---
id: PRD-SEI-205
title: Spain Banqup Unifiedpost Integration
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
  - research/provider-apis/banqup-unifiedpost/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "855180247"
  title: Banqup (Unifiedpost) integration
---

# Spain Banqup Unifiedpost Integration

## Summary

Connect eligible Spanish e-invoicing customers to Banqup (Unifiedpost) through the shared private-platform connection, routing, and resilience foundation.

## Problem

Sage requires a consistent way to onboard customers to Banqup and exchange invoices without exposing provider-specific behaviour to every Sage ERP. Provider capabilities and constraints have not yet been confirmed and must be established during discovery.

Banqup publishes API guides, an API explorer, recipes, release notes, and a developer portal. Public recipes cover application credentials, access tokens, OAuth 2.0 authorisation-code flow, sales-invoice upload/validation/send, and purchase-invoice processing. Phase 2 must narrow this broad API surface to the Spain private-platform product and map Banqup spaces, entities, connections, and permissions to Sage resources.

## Evidence and confidence

Evidence source: `research/provider-apis/banqup-unifiedpost/README.md`

| Area | Current confidence |
|---|---|
| Public developer documentation and API explorer | Confirmed |
| Developer-managed application credentials | Confirmed |
| Access token and OAuth 2.0 authorisation-code patterns | Confirmed |
| Sales and purchase invoice recipes | Confirmed |
| Space, entity, plugin-interface, and connection identifiers | Confirmed concepts; exact use to validate |
| Spain private-platform product and API scope | Unconfirmed |
| Webhook, idempotency, rate-limit, retention, and SLA details | Unconfirmed |

## Goals

- Confirm Banqup's supported Spain capabilities and Unifiedpost service boundary.
- Establish secure sandbox and production connections.
- Support eligible inbound and outbound flows through the shared adapter contract.
- Translate provider lifecycle statuses and errors into the Sage model.
- Support reconciliation, monitoring, and controlled deactivation.

## Non-goals

- Features outside the shared Phase 2 scope.
- Direct integration independently implemented by each Sage ERP.
- Private-to-private provider switching.
- Commercial or contractual migration between Unifiedpost services.

## Users and use cases

- ERP products initiate Banqup connection setup through shared APIs.
- Customers or accountants provide required configuration.
- Invoice services exchange eligible documents.
- Operations investigate and reconcile provider failures.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | Discovery must document Banqup and Unifiedpost product boundaries relevant to Spain. |
| FR2 | Supported formats, directions, registrations, and lifecycle operations must be explicitly recorded. |
| FR3 | The adapter must use the shared connection and capability contract. |
| FR4 | Credentials and identifiers must be stored and handled securely. |
| FR5 | Sandbox and production configuration must be isolated. |
| FR6 | Provider statuses and errors must map to stable Sage categories. |
| FR7 | Duplicate registration and invoice operations must be prevented. |
| FR8 | Webhook and/or polling processing must tolerate missed, repeated, and reordered events. |
| FR9 | Reconciliation and provider-health operations must be exposed where available. |
| FR10 | Disablement and deregistration must remain separate from route deactivation. |

### Identity, consent, and tenant model

| ID | Requirement |
|---|---|
| FR11 | The integration must select either application-credential or delegated OAuth flow per approved customer and operational scenario. |
| FR12 | Required scopes and permissions must be documented at least privilege. |
| FR13 | Where customer consent is required, Sage must show the permissions requested and handle denial or revocation. |
| FR14 | Sage must map Banqup space, entity, and connection identifiers to stable Sage legal-entity and connection resources. |
| FR15 | Revoking Sage application access must not be represented as customer offboarding without separate confirmation. |

### Outbound sales invoices

| ID | Requirement |
|---|---|
| FR16 | Adapter must implement the approved sales-invoice upload or creation operation. |
| FR17 | Banqup validation must complete before the invoice is treated as eligible for sending. |
| FR18 | Upload, validation, send, and delivery/lifecycle states must remain distinguishable. |
| FR19 | Sage must store Banqup document ID, entity/space ID, connection/network context, and relevant external references. |
| FR20 | A repeated request must not create or send a duplicate invoice. |

### Inbound purchase invoices

| ID | Requirement |
|---|---|
| FR21 | Discovery must identify the authoritative purchase-invoice retrieval or event mechanism. |
| FR22 | Sage must separate mandatory network lifecycle operations from optional Banqup approval or payment workflows. |
| FR23 | Inbound documents must be deduplicated using stable Banqup identity. |
| FR24 | Original content, canonical mapping, attachments, and lifecycle status must remain traceable. |
| FR25 | Historical purchase-invoice operations must retain the original Banqup connection after route changes. |

### Notifications and reconciliation

| ID | Requirement |
|---|---|
| FR26 | Webhook or event authentication, event identity, ordering, retry, and replay behaviour must be confirmed before implementation. |
| FR27 | Adapter must provide an authoritative read/reconciliation path for missed or ambiguous events. |
| FR28 | OAuth token refresh or application-token renewal must be automated where supported and safely recoverable. |
| FR29 | Permission or consent revocation must create an actionable connection state. |
| FR30 | Banqup lifecycle statuses and error details must map to stable Sage categories without losing diagnostic evidence. |

## Proposed resource mapping

This mapping is a design hypothesis pending API explorer and partner validation.

| Sage concept | Candidate Banqup concept |
|---|---|
| Customer workspace | Space |
| Legal entity | Entity |
| Provider connection | Connection and/or plugin interface |
| Credential grant | App credential or OAuth grant |
| Outbound invoice | Sales invoice/document |
| Inbound invoice | Purchase invoice/document |
| Provider lifecycle | Document/network status and events |

The implementation must not assume these are one-to-one until confirmed.

## Detailed journeys

### Delegated customer authorisation

1. Sage creates a draft Banqup connection.
2. Customer is redirected to the approved Banqup authorisation flow.
3. Banqup presents requested scopes.
4. Customer authorises or denies access.
5. Sage exchanges the returned code through the secure backend.
6. Sage resolves permitted spaces/entities and confirms the selected legal entity.
7. Connection becomes configured; readiness and route activation remain separate.

### Application-managed connection

1. An authorised integration administrator creates or provisions application credentials.
2. Credentials are stored using the approved secret mechanism.
3. Sage obtains an access token.
4. Sage validates permitted spaces, entities, and API capabilities.
5. Connection becomes ready for declared operations.

### Process outbound sales invoice

1. Shared routing selects Banqup.
2. Sage uploads or creates the sales invoice.
3. Banqup validation is requested or observed.
4. Validation failures return actionable errors.
5. Valid document is sent through the approved connection/network.
6. Sage consumes lifecycle events or reconciles through reads.
7. Provider document and network references remain attached to the invoice.

### Process inbound purchase invoice

1. Banqup makes a purchase invoice available or emits an event.
2. Sage authenticates, deduplicates, and retrieves the document.
3. Canonical mapping and original artefact are recorded.
4. Required network lifecycle states are mapped.
5. Optional approval/payment actions remain outside scope unless separately approved.

## Failure behaviour

| Scenario | Expected behaviour |
|---|---|
| Customer denies OAuth consent | Keep connection non-ready; return no-access status |
| Consent or token revoked | Stop affected calls, notify responsible actor, preserve queued work |
| Incorrect entity selected | Prevent route activation until legal-entity match is confirmed |
| Invoice validation fails | Return mapped corrections; do not send |
| Upload/send outcome unknown | Query document state before retry |
| Event duplicated or reordered | Process idempotently without lifecycle regression |
| Banqup permission changes | Re-evaluate capability and show action required |
| Provider unavailable | Apply shared resilience and incident behaviour |

## Security and non-functional requirements

- OAuth state, redirect URI, PKCE/client-secret handling, token encryption, refresh, and revocation must pass security review.
- Application credentials and tokens must never be returned through ERP-facing APIs.
- Scopes must be minimal and recorded with the connection.
- Test and production tenants, applications, tokens, and entity identifiers must be isolated.
- The selected API version and release-note monitoring owner must be defined.
- Customer-visible errors must not expose internal Banqup tenant or security information.

## Acceptance criteria

1. A customer can authorise Sage and select the correct Banqup entity without exposing tokens.
2. Denied or revoked consent creates an actionable state and does not change routing.
3. A validated connection can exist without an active route.
4. A representative sales invoice completes upload, validation, send, and lifecycle correlation.
5. A representative purchase invoice is ingested once with original Banqup context.
6. Validation failures are mapped and do not send the invoice.
7. Timed-out mutations are reconciled before retry.
8. Duplicate and out-of-order event tests do not duplicate or regress state.
9. Test and production resources cannot be mixed.
10. Route deactivation does not automatically revoke consent or deregister the entity.

## User experience

The shared onboarding flow must display Banqup-specific requirements without exposing unnecessary provider terminology. Users must see whether configuration, registration, readiness, or route activation needs attention.

## Metrics

- Successful connection and registration rate.
- Successful invoice operation rate.
- Status mapping coverage.
- Duplicate and unreconciled outcome count.
- Support escalation rate.

## Rollout

1. Confirm the Banqup/Unifiedpost technical service in scope.
2. Complete the provider discovery checklist.
3. Obtain sandbox access through approved channels.
4. Implement and validate representative journeys.
5. Pass resilience and operations readiness.
6. Pilot with an agreed cohort.

### Provider readiness gate

- Spain product/API boundary and commercial entitlement confirmed.
- Authentication flow, scopes, consent roles, and entity mapping approved.
- Endpoint and schema inventory extracted from the API explorer.
- Webhook, idempotency, reconciliation, limits, retention, and SLA documented.
- Sandbox covers outbound, inbound, revocation, validation, timeout, and duplicate-event scenarios.

## Risks

- Ambiguous Banqup and Unifiedpost product boundaries.
- Environment or tenant provisioning delays.
- Provider status semantics not mapping cleanly.
- Credential ownership differing between customer and Sage.

## Open questions

1. Which Unifiedpost/Banqup product and API are authoritative for this integration?
2. Which Spain formats, directions, and lifecycle operations are supported?
3. What authentication, tenant, and customer-registration models apply?
4. What webhook, idempotency, and reconciliation facilities are available?
5. What service and rate limits apply?
6. How is historical access maintained after route changes?
7. Is Banqup a candidate for the reference integration?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | Banqup (Unifiedpost) is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
