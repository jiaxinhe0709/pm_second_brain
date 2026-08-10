---
id: PRD-SEI-220
title: Provider Integration — ZeroComa — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-208
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/zerocoma/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "855180249"
  page_id: ""
  title: Provider Integration — ZeroComa — Structured Review
  layout: two_left_sidebar
  toc: true
---

# Provider Integration — ZeroComa — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-208, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-220, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-208. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-208; this successor introduces no new product decision. |

## Summary

Connect eligible Spanish e-invoicing customers to ZeroComa through the shared private-platform connection, routing, and resilience foundation.

This Phase 2 PRD first requires confirmation that the intended ZeroComa service is a private-platform integration product rather than a desktop invoicing, FACeB2B, VeriFactu, reporting, archive, or other adjacent product.

> **Product principle:** Do not design an adapter around a vendor name. Design it around one contracted ZeroComa service, protocol, capability set and lifecycle.

## Problem

Sage requires a reusable ZeroComa integration for its ERPs. ZeroComa's exact Spain capabilities, onboarding process, API model, and operational constraints must be verified during discovery.

ZeroComa publicly describes B2B invoice issuance and receipt, ERP integration, traceability, conservation, VeriFactu, reporting, and AEAT connectivity. The public material does not expose an endpoint contract or prove which capabilities form the Phase 2 private-platform service. The PRD therefore separates confirmed product claims from technical requirements requiring vendor evidence.

## Evidence and research findings

This section is self-contained for Confluence readers. Official public material was rechecked on 2026-07-29. The evidence is narrower than for B2B Router or Banqup and exposes a material product-boundary risk.

### Evidence register

| Ref | Official source | Confirmed finding | Confidence/limitation | PRD impact |
|---|---|---|---|---|
| E1 | [ZeroComa EdasInvoiZE product sheet](https://www.zerocoma.com/wp-content/uploads/2023/12/HOJA-DE-PRODUCTO-EDASINVOIZE.pdf) | EdasInvoiZE is described as a desktop solution for automated electronic-invoice issue/receipt using signed PDF and Facturae 3.2, with FACeB2B integration. | **Confirmed product claim.** Does not prove Phase 2 private-platform API/service. | Product identity gate G1/G3 |
| E2 | [ZeroComa EdasInvoiZE product sheet](https://www.zerocoma.com/wp-content/uploads/2023/12/HOJA-DE-PRODUCTO-EDASINVOIZE.pdf) | The product sheet states integration through APIs or Web Services and manual data loading. | **Confirmed generic integration claim.** No endpoint, protocol, schema, environment or auth detail. | G2; no payload may be assumed |
| E3 | [ZeroComa EdasInvoiZE product sheet](https://www.zerocoma.com/wp-content/uploads/2023/12/HOJA-DE-PRODUCTO-EDASINVOIZE.pdf) | Product claims include certified digitisation, document management, backups, proof of sending and integration with public bodies/companies. | **Confirmed broad product claim.** Archive/legal status, private routing and contracted scope unknown. | Scope separation, archive/exit gates |

### Capability matrix

| Capability | Public evidence | Phase 2 treatment | Evidence required |
|---|---|---|---|
| Signed PDF and Facturae 3.2 issue/receipt | Confirmed EdasInvoiZE claim | Adjacent/candidate only | Contracted private-platform formats and directions |
| FACeB2B integration | Confirmed claim | Do not equate with Phase 2 private route | Intended Spain network/service |
| APIs or Web Services | Confirmed generic claim | Discovery basis | Technical pack, protocol/version, endpoints |
| Desktop deployment | Confirmed for EdasInvoiZE | Potential architecture mismatch | Whether Sage integrates to desktop, hosted service or another product |
| Manual loading | Confirmed option | Not a platform integration | Automated contract required |
| Document management/backups | Confirmed claim | Candidate archive capability | Retention, trusted copy, access/exit |
| Private-platform registration/routing | Unconfirmed | Production blocker | Provider/local-team confirmation |
| Tenant/legal-entity and credentials | Unconfirmed | Engineering blocker | Identity/onboarding model |
| Status/events/reconciliation | Unconfirmed | Engineering blocker | Lifecycle and safety contract |
| Limits/SLA/support/security | Unconfirmed | Production blocker | Contract pack |

### Product-boundary concern

The named Phase 2 provider is “ZeroComa,” but the concrete public artefact found is for “EdasInvoiZE,” a desktop-oriented product. Before solution design, the vendor must confirm:

- the exact legal/product/service name Sage will contract;
- whether EdasInvoiZE is the integration target or only adjacent evidence;
- whether the target is hosted, tenant-based, customer-installed or managed;
- how it participates in Spain private B2B routing rather than only FACeB2B/public-sector or desktop invoicing;
- which API/Web Service specification applies to that target.

| Evidence class | Assessment |
|---|---|
| EdasInvoiZE product existence/features | High |
| ZeroComa private-platform product identity | Low |
| API/protocol/onboarding/lifecycle | Low |
| Resilience, service and exit | Low |
| Overall readiness | **Product consultation ready; blocked for solution design** |

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

- **Customer/accountant administrator:** completes the contracted product onboarding and legal-entity actions.
- **Sage ERP/API consumer:** uses shared Sage APIs rather than desktop/vendor-specific operations.
- **Sage adapter/invoice services:** invoke the verified automated contract and preserve provider evidence.
- **Operations/support:** distinguish customer-installed, Sage and provider-hosted failures.
- **Security/compliance:** approve deployment boundary, credentials/certificates, data flows, archive and support access.
- **ZeroComa technical owner:** confirms the target service and supplies authoritative sandbox/contract evidence.

## Business scenarios and rules

| Scenario | Expected outcome | Evidence dependency |
|---|---|---|
| Product selection | One contracted private-platform service and deployment boundary | Vendor architecture/product confirmation |
| Prepare connection | Automated connectivity and direction capability validate; route unchanged | API/Web Service and onboarding pack |
| Send/receive | Supported structured document exchanged with stable provider references | Format/lifecycle contract |
| Customer-installed component fails | Sage shows ownership/action without unsafe retry | Deployment/support model |
| Ambiguous submission | Authoritative provider query/reconciliation before repeat | Idempotency/reconciliation |
| Route moves away | Historical status/document/archive remains accessible | Exit/retention model |

| ID | Business rule | Status/evidence |
|---|---|---|
| BR1 | ZeroComa/EdasInvoiZE product identity must be confirmed before architecture or estimation. | E1; confirmed discovery gate |
| BR2 | Desktop/manual loading is not sufficient evidence of an automated Sage platform contract. | E1/E2 |
| BR3 | FACeB2B, private B2B, signed PDF, Facturae, VeriFactu/reporting and archive are separate capabilities. | E1/E3; product rule |
| BR4 | Provider readiness does not activate a Sage route. | Confirmed Phase 2 rule |
| BR5 | Unknown mutation outcome reconciles before repeat unless idempotency is proven. | PRD-SEI-203 |
| BR6 | Route deactivation, software/connection disablement, deregistration, credential revocation and archive termination are separate. | Phase 2 continuity |

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

### Correct, reconcile and preserve history

1. Provider/schema validation failure returns an actionable correction and does not repeat unchanged content.
2. Timeout after possible submission enters an unknown-outcome state with durable correlation/fingerprint.
3. Adapter uses the contracted query, receipt or support reconciliation path before retry.
4. Duplicate/missed/out-of-order documents or events process once and reconcile.
5. Route change preserves ZeroComa service, document/transmission IDs, actual format/version and required archive/lifecycle access.

## Proposed integration contract — product and endpoint pending

| Context | Required evidence/data |
|---|---|
| Product/deployment | Contracted service name/version, hosted vs customer-installed boundary, environment and support owner |
| Connection | Tenant/legal entity/mailbox, endpoint/protocol, credential/certificate references, enabled capabilities |
| Outbound | Correlation, original/target format/version, provider document/transmission IDs and acknowledgement evidence |
| Inbound | Provider ID, source/legal-entity scope, original artefact/integrity and received time |
| Lifecycle | Raw provider code, stage, provenance, timestamps and supporting reference |
| Archive/exit | Trusted-copy status, retention/access, credential/software dependency and termination sequence |

No ZeroComa API payload is included because “APIs or Web Services” is the only verified public technical statement. Approved synthetic samples must come from the contracted target and be stored under `assets/provider-apis/zerocoma/{CONTRACT_VERSION}/`; desktop screenshots or marketing examples are not API fixtures.

### Operation-safety classification

| Operation | Default treatment before evidence |
|---|---|
| Connectivity/read | Retry only if read-only and remote/local ownership are proven |
| Provision/configure | Track manual and automated intended/observed state; no blind repeat |
| Submit invoice | Unknown after possible transmission; reconcile first |
| Receive/acknowledge | Authenticate, deduplicate and prove retry semantics |
| Backup/archive retrieval | Separate from active route; audit access and integrity |
| Deregister/revoke/uninstall | Explicit dependency check, authorisation and post-action verification |

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

| ID | Demonstrable criterion |
|---|---|
| AC1 | The contracted target/deployment is named and private B2B is separated from EdasInvoiZE desktop, FACeB2B, VeriFactu/reporting and archive capabilities. |
| AC2 | Every implementation behaviour links to a provider versioned technical source and synthetic sandbox evidence. |
| AC3 | Connection readiness is independently represented by legal entity, direction, format and capability without activating a route. |
| AC4 | Representative automated inbound/outbound flows pass in the contracted sandbox and retain provider/original-format context. |
| AC5 | Customer-installed/hosted ownership failures show the correct responsible actor and recovery action. |
| AC6 | Duplicate/out-of-order documents/events process once; missing observations reconcile. |
| AC7 | Ambiguous mutation reconciles before retry. |
| AC8 | Provider validation/status/error evidence maps actionably without discarding raw code/provenance. |
| AC9 | Archive/historical lifecycle remains available after route deactivation according to the approved exit model. |
| AC10 | Test/production resources remain isolated and production cannot activate until G1–G6 pass. |

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

| Gate | Required evidence | Blocks |
|---|---|---|
| G1 — Product/deployment | Contracted ZeroComa service, relationship to EdasInvoiZE, hosted/desktop boundary and owners | Solution design |
| G2 — Technical contract | API/Web Service/protocol/version, schemas, environments and storage permission | Engineering |
| G3 — Spain capability | Private B2B role, legal entity/registration, directions, formats and capability separation | Delivery scope |
| G4 — Lifecycle/safety | Status/error/event, idempotency and authoritative reconciliation | Async production |
| G5 — Security/service/exit | Credentials/certificates/network, limits, retention/archive, SLA/support, deregistration/uninstall | Production |
| G6 — Fixtures/pilot | Synthetic happy/failure/timeout/duplicate/deployment/archive tests and pilot stop criteria | Pilot |

## Risks

- Limited or changing technical documentation.
- Manual provisioning or certification steps.
- Provider lifecycle semantics differ from the shared model.
- Sandbox coverage is insufficient for failure testing.

## Open questions

| ID | Decision required | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| OQ1 | Is EdasInvoiZE the target, and is it hosted, desktop or managed? | Vendor/commercial + architecture | G1 | Current public artefact may be adjacent |
| OQ2 | Which API/Web Service/protocol/version and environments? | Provider/architecture | G2 | No endpoint assumed |
| OQ3 | How does target participate in Spain private B2B vs FACeB2B/public/tax services? | Provider/local team | G3 | Capabilities must remain separate |
| OQ4 | Legal-entity, credential/certificate, onboarding and registration model? | Provider/security | G3/G5 | Open |
| OQ5 | Formats, directions, lifecycle/status and archive semantics? | Provider/product | G3/G4/G5 | Facturae 3.2 claim is not enough |
| OQ6 | Events/polling, idempotency and reconciliation? | Provider/resilience owner | G4 | Reconcile before retry |
| OQ7 | Limits, data/retention, SLA/support and exit/uninstall? | Provider/operations/legal | G5 | Open |
| OQ8 | Is ZeroComa a reference adapter/pilot? | Product/engineering | Pilot | Not decidable before G2 |

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | ZeroComa is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
| 2026-07-29 | Embedded product evidence and mismatch risk, business rules, endpoint-pending contract, safety/continuity, acceptance and gates | |
