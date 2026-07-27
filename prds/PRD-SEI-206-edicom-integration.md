---
id: PRD-SEI-206
title: Spain EDICOM Integration
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
  - research/provider-apis/edicom/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "855180243"
  title: EDICOM integration
---

# Spain EDICOM Integration

## Summary

Connect eligible Spanish e-invoicing customers to EDICOM through the shared private-platform connection, routing, and resilience foundation.

## Problem

Sage requires a shared EDICOM adapter rather than separate ERP implementations. The exact Spain capabilities, onboarding process, protocols, and operational constraints must be confirmed during discovery.

No authoritative public endpoint-level EDICOM documentation has been located. The integration might use REST, SOAP, AS2, SFTP, a managed connector, or another contracted protocol. The PRD therefore defines the required product behaviour and evidence gates without presenting an unverified protocol as fact.

## Evidence and confidence

Evidence source: `research/provider-apis/edicom/README.md`

| Area | Current confidence |
|---|---|
| EDICOM is in the intended Phase 2 provider portfolio | Confirmed internally |
| Exact EDICOM product and Spain service | Unconfirmed |
| API or transport protocol | Unconfirmed |
| Authentication, certificates, and network setup | Unconfirmed |
| Invoice directions, formats, and status model | Unconfirmed |
| Sandbox, idempotency, reconciliation, limits, and SLA | Unconfirmed |

## Goals

- Establish the EDICOM capability and integration profile for Spain.
- Provide secure sandbox and production connectivity.
- Support eligible inbound and outbound document journeys.
- Map EDICOM statuses, identifiers, and errors into the Sage model.
- Provide reconciliation, monitoring, and controlled connection lifecycle.

## Non-goals

- Features outside the shared Phase 2 scope.
- Direct ERP-specific EDICOM implementations.
- Private-to-private switching.
- Unrelated EDICOM products or countries.

## Users and use cases

- ERP teams use common APIs to configure EDICOM.
- Customers or accountants complete required onboarding.
- Invoice services exchange supported documents.
- Operations diagnose and reconcile failures.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | The integration must document the EDICOM product, protocol, and country scope. |
| FR2 | Supported directions, formats, document types, and lifecycle actions must be declared. |
| FR3 | The adapter must implement the shared capability contract. |
| FR4 | Customer identifiers, credentials, and certificates must use approved secure handling. |
| FR5 | Sandbox and production must be isolated. |
| FR6 | EDICOM acknowledgements and statuses must map to stable Sage lifecycle states. |
| FR7 | Idempotency or duplicate protection must apply to registration and document operations. |
| FR8 | Event delivery must tolerate duplication, delay, and reordering. |
| FR9 | Reconciliation and health checks must be implemented where supported. |
| FR10 | Route deactivation must not implicitly deregister EDICOM. |

### Provider discovery and contracting

| ID | Requirement |
|---|---|
| FR11 | EDICOM must identify the contracted product, service region, protocol, and technical version in writing. |
| FR12 | Sage must obtain the applicable API/integration guide, schemas, status/error catalogue, and change policy. |
| FR13 | Sage must confirm whether onboarding includes manual provisioning, certificates, VPN, IP allow-listing, or provider certification. |
| FR14 | Sandbox and production access, support ownership, volume model, and SLA must be agreed before delivery commitment. |

### Connection and registration

| ID | Requirement |
|---|---|
| FR15 | The adapter must represent EDICOM configuration through the shared connection model regardless of underlying protocol. |
| FR16 | Required certificate, key, endpoint, mailbox, tenant, or interchange identifiers must be stored as secure references and metadata. |
| FR17 | Sage must validate connectivity and legal-entity registration before route activation. |
| FR18 | Manual provider steps must be represented as trackable pending/action-required states. |
| FR19 | Production activation must require evidence that the intended inbound/outbound capability is enabled. |

### Invoice exchange

| ID | Requirement |
|---|---|
| FR20 | The selected canonical-to-EDICOM format mapping must be versioned and testable. |
| FR21 | Submission receipt, technical acknowledgement, business validation, network delivery, and final lifecycle status must remain distinguishable where the protocol provides them. |
| FR22 | Every outbound document must have a stable Sage correlation identity and retained EDICOM interchange/document references. |
| FR23 | Inbound ingestion must be incremental, idempotent, and recoverable after interruption. |
| FR24 | Original provider payload or document evidence must be retained according to approved security and retention policy. |
| FR25 | Correction, cancellation, rejection, and payment-status behaviour must not be assumed until included in the provider capability matrix. |

### Reconciliation and lifecycle

| ID | Requirement |
|---|---|
| FR26 | The provider must identify the authoritative query or support procedure for ambiguous submissions. |
| FR27 | The adapter must translate EDICOM statuses into Sage lifecycle states while retaining raw codes and timestamps. |
| FR28 | Acknowledgements or files received more than once must not duplicate invoices or lifecycle events. |
| FR29 | Route changes must preserve the EDICOM connection context required for historical invoices. |
| FR30 | Deregistration must follow an approved EDICOM process and must not be inferred from route deactivation. |

## Provisional journeys requiring provider validation

### Establish connection

1. Create EDICOM draft connection.
2. Complete provider/customer provisioning and legal-entity registration.
3. Supply protocol configuration and credentials/certificates securely.
4. Validate connectivity in sandbox.
5. Complete any EDICOM certification tests.
6. Confirm enabled directions, formats, and lifecycle capabilities.
7. Mark connection ready without activating a route.

### Outbound invoice

1. Resolve EDICOM route.
2. Transform and validate the canonical invoice using the approved schema/version.
3. Submit through the confirmed protocol.
4. Retain submission and acknowledgement references.
5. Process technical and business acknowledgements without collapsing them into one status.
6. Reconcile ambiguous or missing acknowledgements.

### Inbound invoice

1. Receive notification/document or poll the confirmed EDICOM channel.
2. Authenticate and validate message integrity.
3. Deduplicate using provider identity and document fingerprint.
4. Store original context and canonical mapping.
5. Acknowledge according to the provider protocol.

## Required provider artefacts

- product architecture and Spain scope;
- API guide or protocol specification;
- OpenAPI, WSDL/XSD, file layout, or Postman collection as applicable;
- sandbox onboarding and certification guide;
- authentication/certificate/network guide;
- document-format and field mapping;
- acknowledgement, status, and error catalogue;
- callback, polling, or mailbox behaviour;
- retry, idempotency, reconciliation, limits, and SLA;
- deregistration and historical-access procedure;
- security, data-residency, and retention evidence.

## Acceptance criteria

1. All provider claims used in implementation are traceable to a versioned EDICOM source.
2. The connection can be validated in sandbox without changing an active route.
3. Required manual provisioning is visible and auditable.
4. Representative outbound and inbound invoices complete with retained provider references.
5. Technical acknowledgements and business lifecycle statuses map without loss of meaning.
6. Duplicate inbound and acknowledgement tests remain idempotent.
7. Ambiguous outbound outcomes have a documented reconciliation procedure.
8. Certificate expiry or connectivity loss creates an actionable connection state.
9. Existing EDICOM invoices retain their original connection after route change.
10. Production cannot be enabled until security, resilience, support, and deregistration gates pass.

## User experience

Provider-specific onboarding data must be collected within the shared experience. Progress must distinguish local configuration, external registration, connection readiness, and active route.

## Metrics

- Connection and registration success rate.
- Invoice operation success rate.
- Acknowledgement and status mapping coverage.
- Duplicate and unreconciled outcomes.
- Operational recovery time.

## Rollout

1. Confirm product and protocol scope.
2. Complete discovery and security assessment.
3. Obtain sandbox access.
4. Implement representative outbound and inbound flows.
5. Validate resilience and support runbooks.
6. Pilot and expand by agreed cohort.

### Provider readiness gate

- Named EDICOM technical owner and product confirmed.
- Contracted integration protocol and version confirmed.
- Technical pack and storage permission received.
- Sandbox, credentials, schemas, acknowledgements, and error catalogue available.
- Idempotency/reconciliation, limits, security, retention, SLA, and support approved.

## Risks

- Multiple EDICOM protocols or products create scope ambiguity.
- Certificate or network setup delays onboarding.
- Multi-stage acknowledgements do not map cleanly.
- Production connectivity differs from sandbox.

## Open questions

1. Which EDICOM service, API, and protocol are in scope?
2. Which Spain formats and directions are supported?
3. What provisioning, certificate, and authentication processes apply?
4. What acknowledgement and lifecycle events are authoritative?
5. What idempotency, webhook, polling, and reconciliation facilities exist?
6. What commercial, rate, payload, and SLA limits apply?
7. Is EDICOM a candidate for the reference integration?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | EDICOM is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
