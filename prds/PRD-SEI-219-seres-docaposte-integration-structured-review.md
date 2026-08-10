---
id: PRD-SEI-219
title: Provider Integration — SERES (Docaposte) — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-207
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/seres-docaposte/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "855180245"
  page_id: "866148402"
  title: Provider Integration — SERES (Docaposte) — Structured Review
  layout: two_left_sidebar
  toc: true
---

# Provider Integration — SERES (Docaposte) — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-207, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-219, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-207. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-207; this successor introduces no new product decision. |

## Summary

Connect eligible Spanish e-invoicing customers to SERES (Docaposte) through the shared private-platform connection, routing, and resilience foundation.

This Phase 2 PRD converts SERES's public Spain product claims into an explicit provider-discovery and delivery contract. Shared routing, transitions and resilience remain owned by PRD-SEI-201–203.

> **Product principle:** SERES may support many formats, networks and workflows; Sage must activate only the contracted, evidenced capability for the intended legal entity and route.

## Problem

Sage requires a consistent SERES integration for its ERPs, but the exact service boundary, onboarding model, supported document journeys, and operating constraints require provider discovery.

SERES publicly describes sending and receiving electronic invoices, API synchronisation with ERPs, public/private platform connectivity, multiple structured formats, invoice status exchange, multi-company operation, and document access/archiving. These are credible product capabilities but not an endpoint contract. Technical implementation must wait for the provider API pack.

## Evidence and research findings

This section is self-contained for Confluence readers. The official SERES Spain product page was rechecked on 2026-07-29. It provides unusually relevant Spain capability claims, but no endpoint-level contract.

### Evidence register

| Ref | Official source | Confirmed finding | Confidence/limitation | PRD impact |
|---|---|---|---|---|
| E1 | [SERES e-Factura](https://www.groupseres.com/e-factura) | SERES publicly claims sending/receiving, Spain B2B connectivity, CEFACT/UBL/EDIFACT/Facturae, public/private platform connectivity and ERP synchronisation by API. | **Confirmed product claims.** Contracted formats/endpoints/protocols unknown. | FR1–FR20; G1–G4 |
| E2 | [SERES e-Factura](https://www.groupseres.com/e-factura) | Product page distinguishes acceptance/rejection and payment statuses, notifications, discrepancies and invoice-state management. | **Confirmed product scope.** Mandatory network vs optional workflow provenance unknown. | BR5, FR19–FR22 |
| E3 | [SERES e-Factura](https://www.groupseres.com/e-factura) | Multi-company operation, API/ERP integration, interaction auditability, online archive/access and format conversion are claimed. | **Confirmed product claims.** Tenant model, audit fields, archive terms and transformation fidelity unknown. | FR11–FR18, FR23, FR29 |
| E4 | [SERES e-Factura](https://www.groupseres.com/e-factura) | SERES describes specialised connection with Spanish tax/public capabilities and also separate value-added services. | **Confirmed broad scope.** Private provider, public repository/tax, archive, finance and workflow boundaries must be contracted separately. | Scope separation and G3 |

### Capability matrix

| Capability | Public evidence | Phase 2 treatment | Evidence required |
|---|---|---|---|
| Send/receive e-invoices | Confirmed claim | Candidate core | Endpoint/protocol and direction matrix |
| CEFACT, UBL, EDIFACT, Facturae | Confirmed claim | Candidate formats only | Contracted subset, versions, lossless tests |
| API/ERP synchronisation | Confirmed claim | Integration basis | API pack, auth, environments |
| Public/private connectivity | Confirmed claim | Do not infer active route | Spain registration/route authority |
| Acceptance/rejection/payment | Confirmed claim | Map provenance and mandatory subset | Status/event catalogue |
| Multi-company | Confirmed claim | Candidate delegated model | Organisation/legal-entity segregation |
| Archive/customer access | Confirmed claim | Candidate continuity support | Retention, trusted copy, access after deactivation |
| Format conversion | Confirmed claim | Candidate provider responsibility | Fidelity/data-loss policy |
| Notifications/audit | Confirmed claim | Candidate operations inputs | Event security, identity, retry/replay and audit schema |
| Endpoint/idempotency/limits/SLA | Not public | Production blockers | Provider technical/contract pack |

### What public evidence does not prove

- that every named format is available through Sage's contracted API;
- the SERES organisation/mailbox/legal-entity cardinality;
- whether API, file, callback or another protocol is used;
- whether directory/public/private capability is Spain's authoritative route;
- which statuses are provider-network evidence versus manual/workflow actions;
- that transformation is lossless for Sage's canonical model;
- archive duration, trusted-copy status or access after deregistration;
- idempotency, reconciliation, limits, security, SLA or support.

| Evidence class | Assessment |
|---|---|
| Spain product/capability relevance | High |
| Format/network/workflow claims | High as product claims; medium/low as contract |
| Endpoint, security and tenant model | Low |
| Resilience, archive terms and service model | Low |
| Overall readiness | **Provider-consultation ready; blocked for engineering** |

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

- **Customer/accountant administrator:** selects the intended SERES company/mailbox and completes provider onboarding.
- **Sage ERP/API consumer:** exchanges invoices through stable Sage APIs independent of SERES protocol.
- **Sage adapter/invoice services:** transform, submit/retrieve and preserve provider evidence.
- **Operations/support:** inspect provider, transformation, event and archive state without secrets.
- **Security/compliance:** approve identity, certificates, signing, network, archive and data controls.
- **SERES technical/support owner:** supplies the contracted API pack and authoritative reconciliation.

## Business scenarios and rules

| Scenario | Expected outcome | Provider-specific exception |
|---|---|---|
| Multi-company onboarding | One Sage legal entity binds to an explicitly authorised SERES scope | Account exposes unrelated companies |
| Outbound format selection | Only contracted format/version becomes route-capable | Product supports format generally but not through selected API |
| Send invoice | Technical acceptance, transformation, route/delivery and business status remain distinct | Provider converts or rejects format |
| Receive invoice | Secure incremental ingestion preserves original document | Notification missed or duplicate |
| Exchange acceptance/rejection/payment | Provenance determines Sage meaning | Status may be manual/value-added rather than network-required |
| Route moves away | Archive and lifecycle remain available for existing invoices | Deregistration/credential removal threatens history |

| ID | Business rule | Status/evidence |
|---|---|---|
| BR1 | SERES provisioning/readiness does not activate a Sage route. | Confirmed Phase 2 rule |
| BR2 | Public support for a format/network does not prove contracted availability. | E1; evidence rule |
| BR3 | Original and transformed artefacts, format versions and provider references must remain traceable. | E1/E3; product requirement |
| BR4 | Provider conversion cannot silently discard canonical invoice meaning. | E3; proposed pending mapping |
| BR5 | Acceptance/rejection/payment states require actor/provenance before Sage assigns business meaning. | E2; open mapping |
| BR6 | Archive access, route deactivation, deregistration and credential revocation are separate lifecycles. | E3; Phase 2 continuity |
| BR7 | Unknown mutation outcome reconciles before repeat unless idempotency is proven. | PRD-SEI-203 |

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

### Correct, reconcile and preserve history

1. Transformation/validation rejection returns field/rule/responsible-actor evidence and does not repeat unchanged data.
2. Timeout after possible submission creates an unknown outcome with Sage correlation and document fingerprint.
3. Adapter uses the contracted authoritative query/receipt/reconciliation path before retry.
4. Missed/duplicate/reordered provider observations reconcile without duplication or regression.
5. Route change preserves SERES document/transmission IDs, original/transformed artefacts, status provenance and archive access.

## Proposed integration contract — endpoint pending

| Sage context | Required SERES evidence/context |
|---|---|
| Connection | Contracted product, environment, organisation/company/mailbox, credentials/certificates, enabled directions/formats/networks |
| Outbound | Sage correlation, original canonical version, selected target format/version, transformation evidence, provider document/transmission IDs |
| Inbound | Provider ID, original format/version/document, sender/receiver scope, received timestamp/integrity evidence |
| Lifecycle | Raw code, category, actor/provenance, provider and observed timestamps, supporting reference |
| Archive | Trusted-copy status, retention/access policy, download evidence and dependency on active credential/registration |
| Reconciliation | Intended state, observed provider state, evidence freshness and safe recovery action |

No SERES API payload is included because no authoritative endpoint/schema is public. Approved synthetic request, response, status, event, transformation and archive fixtures must come from the contracted sandbox and be stored under `assets/provider-apis/seres-docaposte/{CONTRACT_VERSION}/`.

### Operation-safety classification

| Operation | Default treatment |
|---|---|
| Directory/capability/status read | Bounded retry only when read-only semantics are confirmed |
| Organisation/registration/configuration | Compare intended/observed state before repeat |
| Transform/submit invoice | Validation failure corrects; timeout after transmission reconciles before retry |
| Event/callback processing | Authenticate, deduplicate, preserve provenance and reconcile independently |
| Archive retrieval | Read-only with access/freshness audit; never treat archive availability as active route |
| Deregistration/revocation | Authorised dependency check, post-action verification and historical continuity |

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

| ID | Demonstrable criterion |
|---|---|
| AC1 | Every endpoint/schema behaviour used in implementation links to the contracted SERES version, not only a product claim. |
| AC2 | Multi-company discovery exposes only authorised legal entities and binds one explicit SERES scope to the connection. |
| AC3 | Direction, format/version, network and archive capabilities are visible before route activation. |
| AC4 | Representative outbound/inbound invoices retain original/transformed artefacts, SERES IDs and actual format/version. |
| AC5 | Transformation loss or incompatible format stops progression with actionable evidence. |
| AC6 | Acceptance/rejection/payment states preserve actor/provenance and do not regress lifecycle. |
| AC7 | Duplicate/out-of-order documents/events process once; missing observations reconcile. |
| AC8 | Ambiguous submission reconciles before retry. |
| AC9 | Archive/historical access works after route deactivation without silently maintaining a route. |
| AC10 | Credential/certificate failures are actionable/redacted; production is blocked until G1–G6 pass. |

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

| Gate | Required evidence | Blocks |
|---|---|---|
| G1 — Product/owner | Contracted SERES/Docaposte service and owners | Solution design |
| G2 — API/security | Endpoint/protocol/version, schemas, auth/certificates/network and storage permission | Engineering |
| G3 — Scope/registration | Legal-entity model, directions, formats, networks, Spain registration/coexistence | Delivery scope |
| G4 — Lifecycle/safety | Status/error/provenance, events, idempotency and reconciliation | Async production |
| G5 — Archive/service | Transformation fidelity, archive/retention/history, limits, SLA/support/exit | Production |
| G6 — Fixtures/pilot | Synthetic happy/failure/timeout/duplicate/transformation/archive tests and stop criteria | Pilot |

## Risks

- SERES and Docaposte naming obscures the technical service boundary.
- Customer provisioning includes manual provider steps.
- Status or acknowledgement semantics differ from shared assumptions.
- Production enablement has long lead times.

## Open questions

| ID | Decision required | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| OQ1 | Contracted SERES/Docaposte service, API/protocol/version? | Vendor/commercial + architecture | G1/G2 | Product page is discovery evidence |
| OQ2 | Organisation/company/mailbox cardinality and delegated access? | Provider/security | G3 | Explicit legal-entity binding required |
| OQ3 | Contracted directions, networks, formats/versions and Spain registration? | Provider/local team | G3 | Prove each capability separately |
| OQ4 | Transformation owner, fidelity and canonical/trusted-copy rules? | Product/architecture/legal | G5 | Preserve original and actual transformed artefact |
| OQ5 | Status provenance and mandatory acceptance/rejection/payment subset? | Product/local team/provider | G4 | Do not equate manual and network states |
| OQ6 | Event security, idempotency and authoritative reconciliation? | Provider/security/operations | G4 | Reconcile independently |
| OQ7 | Limits, archive/retention/history, SLA/support and exit? | Provider/operations/legal | G5 | Open |
| OQ8 | Is SERES a reference adapter/pilot? | Product/engineering | Pilot | Candidate only after G2 |

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | SERES (Docaposte) is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
| 2026-07-29 | Embedded Spain product evidence/limitations, business rules, endpoint-pending contract, transformation/lifecycle safety, acceptance and gates | |
