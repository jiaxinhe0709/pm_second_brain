---
id: PRD-SEI-218
title: Provider Integration — EDICOM — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-206
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/edicom/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "855180243"
  title: Provider Integration — EDICOM
  layout: two_left_sidebar
  toc: true
---

# Provider Integration — EDICOM — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-206, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-218, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-206. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-206; this successor introduces no new product decision. |

## Summary

Connect eligible Spanish e-invoicing customers to EDICOM through the shared private-platform connection, routing, and resilience foundation.

This Phase 2 PRD defines the evidence contract and observable behaviour required before an EDICOM adapter can be designed. It deliberately avoids choosing REST, SOAP, AS2, SFTP, Web Services, a managed connector, or another protocol without contracted provider evidence.

> **Product principle:** An EDICOM product claim can justify discovery; only the contracted Spain integration pack and tested environment can justify an implementation contract.

## Problem

Sage requires a shared EDICOM adapter rather than separate ERP implementations. The exact Spain capabilities, onboarding process, protocols, and operational constraints must be confirmed during discovery.

No authoritative public endpoint-level EDICOM documentation has been located. The integration might use REST, SOAP, AS2, SFTP, a managed connector, or another contracted protocol. The PRD therefore defines the required product behaviour and evidence gates without presenting an unverified protocol as fact.

## Evidence and research findings

This section is self-contained for Confluence readers. Official public material was rechecked on 2026-07-29. It confirms EDICOM's platform positioning and broad capability, not Sage's Spain endpoint contract.

### Evidence register

| Ref | Official source | Confirmed finding | Confidence and limitation | PRD impact |
|---|---|---|---|---|
| E1 | [Global electronic invoicing platform](https://edicomgroup.com/electronic-invoicing) | EDICOM publicly describes a SaaS platform integrated with ERPs for issuance, receipt, validation and electronic archiving across many jurisdictions, including Spain. | **Confirmed product claim.** No Sage contract, endpoint, schema or Spain private-platform sequence. | Justifies discovery; G1/G3 remain blocking |
| E2 | [EDICOM Spain](https://edicomgroup.com/es/) | EDICOM publicly describes EDI/e-invoicing, multi-standard/multi-protocol interoperability, Peppol Access Point capability, SaaS infrastructure and managed services. | **Confirmed broad platform claim.** Does not select protocol/product for Sage. | FR11–FR14; protocol-neutral adapter requirement |
| E3 | [SAP Ariba connector example](https://edicomgroup.com/connectors/ariba-network) | EDICOM describes API-based validation/integration for a named connector and multi-stage invoice processing. | **Confirmed capability in another product context only.** Must not be reused as Spain endpoint evidence. | Supports need to distinguish stages; no endpoint mapping |

### Capability matrix

| Capability | Public evidence | Phase 2 treatment | Required provider evidence |
|---|---|---|---|
| ERP integration and SaaS platform | Confirmed product claim | Discovery basis | Contracted architecture/service name |
| Issuance, receipt, validation, archive | Confirmed broad claim | Candidate capabilities | Spain direction/document/lifecycle matrix |
| Multi-standard/multi-protocol | Confirmed broad claim | Keep design protocol-neutral | Selected protocol, schemas, versions |
| Peppol Access Point | Confirmed broad claim | Do not assume selected Spain route | Contract and Spain applicability |
| Managed service/support | Confirmed broad claim | Candidate operating model | Sage/customer responsibilities, SLA/escalation |
| Tenant/legal-entity registration | Unknown | Production blocker | Resource/provisioning model |
| Authentication/certificates/network | Unknown | Production blocker | Credential, signing, VPN/allow-list details |
| Endpoint/message contract | Unknown | Engineering blocker | API/WSDL/schema/file specification |
| Acknowledgement/status/error model | Unknown | Engineering blocker | Code catalogue and provenance |
| Idempotency/reconciliation/limits | Unknown | Production blocker | Per-operation safety contract |
| Deregistration/historical access | Unknown | Production blocker | Exit and archive procedure |

### What public evidence does not prove

- which EDICOM product, tenant, access point or managed service Sage will use;
- whether the exchange is API, Web Service, EDI transport, file transfer or managed connector;
- which party owns certificates, signing, network configuration or provider registration;
- that Peppol is the intended Spain private-platform path;
- which acknowledgement proves technical receipt, validation, routing, delivery or business acceptance;
- that public claims about other countries/connectors apply to Spain;
- any endpoint, payload, idempotency, limit, SLA, retention or exit behaviour.

| Evidence class | Assessment |
|---|---|
| Provider/platform existence and broad capability | High |
| Spain contracted product and private-platform role | Low |
| Protocol, schema, identity and onboarding | Low |
| Lifecycle, reconciliation, service and exit | Low |
| Overall readiness | **Provider-consultation ready; blocked for solution design** |

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

- **Customer/accountant administrator:** completes contracted legal-entity provisioning and any certificate/network actions.
- **Sage ERP/API consumer:** uses shared Sage APIs without needing the selected EDICOM protocol.
- **Sage adapter/invoice services:** transform, exchange and retain provider/interchange evidence.
- **Operations/support:** see manual/provider/Sage steps, acknowledgements and reconciliation without secrets.
- **Security/network/compliance:** approve certificate/key custody, endpoints, allow-lists, data flows and retention.
- **EDICOM technical/support owner:** supplies authoritative artefacts and resolves ambiguous provider state.

## Business scenarios and rules

| Scenario | Expected outcome | Evidence dependency |
|---|---|---|
| Contract discovery | One named EDICOM product/protocol/version and owner | Contracted technical pack |
| Manual provisioning | Pending/action-required states remain visible and auditable | Onboarding/certification guide |
| Outbound exchange | Submission, technical ACK, validation, delivery and business state remain distinct | Status/ack catalogue |
| Inbound exchange | Trusted, incremental, deduplicated receipt with original document | Delivery/query specification |
| Ambiguous submission | Reconcile via authoritative query/receipt/support path before repeat | Idempotency/reconciliation procedure |
| Route moves away | Historical provider/interchange context remains usable | Archive/credential/exit procedure |

| ID | Business rule | Status/evidence |
|---|---|---|
| BR1 | EDICOM provisioning/readiness must not activate a Sage route. | Confirmed Phase 2 rule |
| BR2 | No protocol or endpoint may be treated as confirmed until linked to the contracted Spain product/version. | Confirmed evidence rule |
| BR3 | Technical receipt, schema/business validation, network delivery and recipient lifecycle must not be collapsed. | Product requirement; provider mapping open |
| BR4 | Manual provisioning/certification is a tracked workflow state, not an undocumented project activity. | Proposed pending provider process |
| BR5 | Unknown post-transmission outcome must reconcile before repeat unless operation-specific idempotency is proven. | PRD-SEI-203 |
| BR6 | Route deactivation, provider deregistration, certificate revocation and archive termination are separate actions. | Confirmed Phase 2 rule |

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

### Correct, reconcile and preserve history

1. Schema/business rejection returns an actionable correction without repeating the unchanged document.
2. Timeout after possible transmission enters an unknown-outcome state with durable Sage correlation.
3. Adapter uses the contracted query, acknowledgement or support reconciliation path before retry.
4. Duplicate/later acknowledgements do not duplicate or regress lifecycle.
5. After route deactivation, older EDICOM documents retain provider IDs, protocol/schema version and required archive/status access.

## Proposed integration contract — protocol neutral

Until G1/G2 pass, architecture may rely only on these conceptual fields, not an EDICOM payload:

| Context | Required fields |
|---|---|
| Connection | EDICOM product/service, environment, legal entity/tenant/mailbox, protocol profile, credential/certificate references, enabled directions/formats |
| Outbound operation | Sage correlation, document fingerprint, schema/version, transmission reference, submission time, acknowledgement references |
| Inbound operation | Provider document/interchange ID, source/legal entity, original format/version, received time, integrity evidence |
| Lifecycle event | Provider code, stage category, provenance, provider timestamp, observed time, related document/transmission |
| Reconciliation | Intended Sage state, last observed EDICOM state, evidence source/freshness, permitted recovery action |

No sample EDICOM API payload is included because no authoritative endpoint/schema has been obtained. The first approved samples must be synthetic fixtures from the contracted sandbox and stored under `assets/provider-apis/edicom/{CONTRACT_VERSION}/`.

### Operation-safety classification

| Operation | Default treatment before evidence |
|---|---|
| Connectivity/status read | Bounded retry if read-only is proven |
| Registration/configuration mutation | Reconcile intended/observed state; no blind repeat |
| Invoice submission | Outcome unknown after possible transmission; reconcile first |
| Inbound ACK | Deduplicate and prove provider retry semantics |
| Deregistration/certificate revocation | Explicit authorisation, historical dependency check and post-action verification |

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

| ID | Demonstrable criterion |
|---|---|
| AC1 | Every implementation claim links to the contracted EDICOM product, protocol and versioned source. |
| AC2 | Sandbox connection/capability validation completes without changing an active route. |
| AC3 | Manual provisioning/certification steps expose owner, evidence, status and next action. |
| AC4 | Representative outbound and inbound invoices retain EDICOM document/interchange IDs, original format and protocol/schema version. |
| AC5 | Technical receipt, validation, delivery and business states remain distinguishable and preserve raw EDICOM codes/provenance. |
| AC6 | Duplicate inbound documents/ACKs process once; out-of-order ACKs do not regress state. |
| AC7 | A post-transmission timeout reconciles before resubmission and cannot create an uncontrolled duplicate. |
| AC8 | Certificate expiry, network failure or allow-list mismatch creates an actionable, redacted connection state. |
| AC9 | Existing EDICOM invoices retain historical retrieval/lifecycle after route change. |
| AC10 | Production activation is impossible until G1–G6 pass. |

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

| Gate | Required evidence | Blocks |
|---|---|---|
| G1 — Product/owner | Named EDICOM service, Spain scope, commercial/technical owner | Solution design |
| G2 — Contract/protocol | Protocol/profile/version, API/WSDL/schema/file pack and storage permission | Engineering |
| G3 — Identity/onboarding | Tenant/legal entity, credentials/certificates/network, manual provisioning/certification | Connection build |
| G4 — Capability/lifecycle | Directions, formats, ACK/status/error catalogue, correction/cancellation and registration | Delivery scope |
| G5 — Safety/service | Idempotency, query/reconciliation, limits, security, residency/retention, SLA/support | Production |
| G6 — Fixtures/exit | Synthetic happy/failure/timeout/duplicate tests plus deregistration/historical access | Pilot |

## Risks

- Multiple EDICOM protocols or products create scope ambiguity.
- Certificate or network setup delays onboarding.
- Multi-stage acknowledgements do not map cleanly.
- Production connectivity differs from sandbox.

## Open questions

| ID | Decision required | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| OQ1 | Named EDICOM Spain service and protocol/version? | Vendor/commercial + architecture | G1/G2 | No protocol assumed |
| OQ2 | Legal-entity/tenant/mailbox and onboarding/certification model? | Provider/security | G3 | Manual steps likely; unconfirmed |
| OQ3 | Supported directions, formats and registration/coexistence? | Provider/local team | G4 | Prove inbound/outbound separately |
| OQ4 | Authoritative ACK/status/error stages and provenance? | Provider/product | G4 | Multi-stage model required |
| OQ5 | Idempotency and ambiguous-outcome reconciliation? | Provider/resilience owner | G5 | Reconcile before retry |
| OQ6 | Limits, security, retention, archive, SLA/support and exit? | Provider/operations/legal | G5/G6 | Open |
| OQ7 | Is EDICOM a reference adapter/pilot? | Product/engineering | Pilot | Not decidable before G2 |

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | EDICOM is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
| 2026-07-29 | Embedded public evidence/limitations, business rules, protocol-neutral contract, safety analysis, testable acceptance and provider gates | |
