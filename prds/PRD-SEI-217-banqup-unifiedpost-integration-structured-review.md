---
id: PRD-SEI-217
title: Provider Integration — Banqup (Unifiedpost) — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-205
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/banqup-unifiedpost/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "855180247"
  page_id: ""
  title: Provider Integration — Banqup (Unifiedpost) — Structured Review
  layout: two_left_sidebar
  toc: true
---

# Provider Integration — Banqup (Unifiedpost) — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-205, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-217, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-205. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-205; this successor introduces no new product decision. |

## Summary

Connect eligible Spanish e-invoicing customers to Banqup (Unifiedpost) through the shared private-platform connection, routing, and resilience foundation.

This Phase 2 provider PRD defines the Banqup-specific identity, consent, document, network, event, and lifecycle boundary. Shared route activation, transition continuity, resilience, and operations remain owned by PRD-SEI-201–203.

> **Product principle:** A Banqup space grants access to documents and services; it is not itself proof that Banqup is the active Sage route for that legal entity and direction.

## Problem

Sage requires a consistent way to onboard customers to Banqup and exchange invoices without exposing provider-specific behaviour to every Sage ERP. Provider capabilities and constraints have not yet been confirmed and must be established during discovery.

Banqup publishes API guides, an API explorer, recipes, release notes, and a developer portal. Public recipes cover application credentials, access tokens, OAuth 2.0 authorisation-code flow, sales-invoice upload/validation/send, and purchase-invoice processing. Phase 2 must narrow this broad API surface to the Spain private-platform product and map Banqup spaces, entities, connections, and permissions to Sage resources.

## Evidence and research findings

This section is self-contained for Confluence readers. Evidence was rechecked against official Banqup documentation on 2026-07-29. The public material confirms a broad platform and concrete recipes; it does not prove which services, regions, networks, or endpoints Sage will contract for Spain.

### Evidence register

| Ref | Official source | Confirmed finding | Confidence and limitation | PRD impact |
|---|---|---|---|---|
| E1 | [Choose your integration](https://docs.btx.banqup.com/docs/api-guides/getting-started/choose-integration) | Banqup documents Client Credentials for workflow/ERP automation and Authorization Code Grant for customer-facing multi-tenant integrations. Entity represents a company; Space is a workspace within an entity. | **Confirmed public model.** Sage flow, regional endpoints, scopes and consent owner remain open. | FR11–FR15; identity gate G2 |
| E2 | [API authentication](https://docs.btx.banqup.com/docs/api-guides/api-fundamentals/api-authentication) | API calls use OAuth 2.0 bearer tokens; resource access is tied to entities and space-administrator permission. | **Confirmed public behaviour.** Token lifetime, refresh/revocation and Sage application approval require testing. | FR4, FR11–FR14, FR28–FR29 |
| E3 | [API recipe overview](https://docs.btx.banqup.com/docs/recipes/overview) | Public recipes cover permissions, credentials, tokens, OAuth user flow, sales invoices, purchase invoices and message listeners. | **Confirmed journey coverage, not Spain entitlement.** | Discovery inventory and G1/G3 |
| E4 | [Automated sales invoice recipe](https://docs.btx.banqup.com/docs/recipes/e-invoicing/sales-invoices-automatic) | Sales processing creates file metadata, uploads via a temporary presigned URL, validates asynchronously, then sends; UBL, XML and PDF prerequisites are described. | **Confirmed public flow.** Exact Spain structured format, URL security, retention value ownership and terminal delivery semantics remain open. | FR16–FR20, API examples, NFR3 |
| E5 | [Sales invoice lifecycle](https://docs.btx.banqup.com/docs/api-guides/e-invoicing/sales-invoice-flow) | Banqup separates general, document, delivery and payment statuses; examples include awaiting validation, validated, refused/disputed, sending/received/delivery failed, unpaid/partially/fully paid. | **Confirmed vocabulary.** Some states are workflow/payment concepts, not mandatory network lifecycle. | FR6, FR18, FR22, FR30 |
| E6 | [Documents](https://docs.btx.banqup.com/docs/workspace/business/documents) | Documents receive a UUID `documentId`; actions are space-scoped; some documented operations are explicitly preview/deprecated. | **Confirmed identity and maturity signals.** Selected stable endpoints/version must be approved. | FR19, FR23–FR24, version gate G1 |
| E7 | [January 2025 release notes](https://docs.btx.banqup.com/docs/release-notes/january-2025) | Banqup announced a Peppol connector that can send, receive and register/discover network participants, plus email and document-processing services. | **Confirmed product announcement, not proof of Spain private-platform contract.** | BR5; network/service boundary gate G3 |
| E8 | [March 2026 release notes](https://docs.btx.banqup.com/docs/release-notes/march-2026) | Document endpoints and recipes can change; current release notes record replaced endpoints. | **Confirmed change risk.** | Version pinning, fixture and change-monitoring requirements |

### Capability matrix

| Capability | Evidence status | Phase 2 treatment | Evidence/decision still required |
|---|---|---|---|
| Client Credentials | Confirmed | Candidate Sage-managed automation flow | Application owner, whitelist/install, scopes, token lifecycle |
| Authorization Code Grant | Confirmed | Candidate delegated customer flow | Consent roles, redirect/PKCE/state requirements, revocation |
| Entity and Space | Confirmed concepts | Proposed legal-entity/workspace mapping | Cardinality, accountant delegation, regional tenancy |
| Sales invoice upload/validation/send | Confirmed public recipe | Candidate outbound flow | Spain formats, connection selection, delivery semantics |
| Purchase invoice workflow | Confirmed public recipe | Candidate inbound source | Retrieval/events, network vs approval/payment scope |
| Document UUID | Confirmed | Required provider identity | Retention and cross-space uniqueness |
| Message listeners | Confirmed concept | Candidate event mechanism | Authentication, identity, ordering, retries, replay, retention |
| Peppol connector | Confirmed product announcement | Do not assume selected Spain route | Contracted network, participant registration and applicability |
| Document/payment/approval workflows | Confirmed platform capability | Include only mandatory e-invoice lifecycle subset | Product boundary and customer ownership |
| Endpoint/schema version stability | Change risk confirmed | Pin/version/test selected surface | Version policy and migration window |
| Spain private-platform registration | Unknown | Production blocker | Provider/local-team confirmation |
| Idempotency, reconciliation, limits, SLA, archive/exit | Unknown/partial | Production blockers | Provider technical/contract pack |

### What public evidence does not prove

- which Banqup/Unifiedpost regional service and network Sage will contract;
- that a Space or Peppol connection is Spain's authoritative route;
- that PDF upload satisfies the Phase 2 structured-invoice requirement;
- that Banqup approval/payment workflows belong in Sage's mandatory network lifecycle;
- that an uploaded or validated document has been delivered;
- that presigned upload URLs may be logged or retained;
- that preview endpoints are suitable for production;
- that customer consent, app installation and participant registration are one event.

### Evidence confidence summary

| Evidence class | Assessment |
|---|---|
| Public API guides and recipes | High |
| OAuth flow choices and entity/space concepts | High; Sage mapping open |
| Sales-document processing | High for generic flow; medium/low for Spain contract |
| Purchase/event/reconciliation detail | Medium/low |
| Spain private-platform registration and route authority | Low |
| Limits, SLA, retention, deregistration and historical access | Low |
| Overall readiness | **Consultation-ready; not delivery-ready** |

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

- **Customer administrator:** grants or manages access to the intended Banqup entity/space and authorises route activation separately.
- **Accountant/delegate:** manages permitted companies without gaining access to unrelated entities or spaces.
- **Sage ERP/API consumer:** starts onboarding and exchanges documents through stable Sage APIs.
- **Sage platform services:** resolve the route, hold immutable provider context, and invoke the Banqup adapter.
- **Operations/support:** inspect consent, token, document, event and reconciliation state without seeing secrets or presigned URLs.
- **Security/compliance:** approves OAuth flow, application ownership, scopes, tenant segregation, retention and evidence handling.

## Business scenarios and rules

| Scenario | Expected outcome | Provider-specific exception |
|---|---|---|
| Customer delegates access | Sage receives only approved scopes/entities/spaces; denial changes no route | User lacks space-admin authority or app is not installed/whitelisted |
| Sage-managed automation | Application token accesses only contracted resources | Credential scope spans unintended entities |
| Prepare Banqup outbound | Space, connection and format capability validate; route stays unchanged | Upload works but selected network connection is not ready |
| Send sales invoice | File upload, validation, send and lifecycle remain separately visible | Validation, delivery or presigned upload fails |
| Receive purchase invoice | Original document is ingested once; optional approval/payment actions remain separate | Message listener is missed or document is outside selected space |
| Route moves away | Historical Banqup documents retain original space/document/network context | Consent revocation removes required history |

| ID | Condition | Business rule | Evidence/status |
|---|---|---|---|
| BR1 | Banqup access is granted | Consent/access makes a connection configurable, not an active route. | Confirmed Phase 2 rule |
| BR2 | Multiple entities/spaces are visible | Sage must bind the connection to an explicitly selected legal entity/space; broad token access is not route scope. | E1/E2; proposed mapping |
| BR3 | File metadata returns a presigned upload URL | Treat the URL as a short-lived secret and never persist it as durable invoice context. | E4; confirmed risk |
| BR4 | File is uploaded/awaiting validation/validated | None of these alone proves recipient delivery. | E4/E5 |
| BR5 | Peppol/network connector exists | Connector availability must not be treated as Spain registration or route authority until contracted and confirmed. | E7; open |
| BR6 | Approval/payment states exist | Mandatory network states and optional AP/AR workflow states must remain distinguishable. | E5; confirmed product distinction |
| BR7 | Route changes away | Existing Banqup documents retain their original provider context and required access. | PRD-SEI-201 |
| BR8 | Mutation outcome is unknown | Query/reconcile before retry unless operation-specific idempotency is proven. | PRD-SEI-203; provider evidence open |

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

### Illustrative API interaction

This compact example is drawn from the official sales-invoice recipe and is suitable for Confluence context, not as an approved production fixture:

```http
POST /datastore/documents/transaction/v1/spaces/{SPACE_ID}/files
Authorization: Bearer <token from approved OAuth flow>
Content-Type: application/json
```

```json
{
  "filename": "synthetic-invoice.xml",
  "retentionTime": "{APPROVED_RETENTION_TIMESTAMP}",
  "fileSize": 12345,
  "fileType": "application/xml",
  "contentType": "application/xml",
  "metadata": {
    "folder": "SALES",
    "documentCategory": "INVOICE"
  }
}
```

The evidenced response includes a document/file identifier, status such as `AWAITING_UPLOAD`, and a temporary `uploadUrl`. Sage must upload the binary to that URL without logging it, then observe validation/document events. Exact regional base URL, scopes, response schema and the subsequent send/connection operation must come from the approved API version.

### Operation-safety and lifecycle treatment

| Provider stage/operation | Sage treatment | Safety/decision |
|---|---|---|
| OAuth authorisation/token exchange | Connection access, not readiness | Validate state/redirect/consent and selected resource scope |
| Create file metadata | Outcome-unknown mutation after transmission | Query by stable document/file identity before recreating |
| Upload to presigned URL | Binary transfer | Do not log URL; verify content hash/size and expiry handling |
| Awaiting validation / validated | Processing/non-terminal | Map validation errors; do not claim delivery |
| Sending / received / delivery failed | Delivery lifecycle | Confirm connection-specific semantics and provenance |
| Disputed/refused/approved | Business-document lifecycle | Keep distinct from technical rejection |
| Payment states | Optional payment lifecycle | Exclude unless separately approved |
| Message event | Notification evidence | Authenticate, deduplicate, order-tolerate and reconcile |

### Required versioned assets

Before delivery approval, create sanitised fixtures under `assets/provider-apis/banqup/{APPROVED_API_VERSION}/` for OAuth success/denial/revocation, entity/space discovery, file metadata and upload, validation success/failure, send lifecycle, purchase retrieval, message events, timeout/reconciliation and historical access. Do not store tokens, presigned URLs, customer data or provider material without storage permission.

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

### Correct or reconcile a failed outbound document

1. If validation fails, Sage maps actionable document errors and does not send or repeat the unchanged file.
2. If metadata creation or send times out after transmission may have occurred, Sage records an unknown outcome.
3. Adapter searches the selected Space using the approved stable identity and document evidence.
4. Exactly one proven match is adopted; proven absence permits a controlled retry; ambiguity becomes an operations case.

### Recover events and preserve history

1. Monitoring detects stale message-listener or document-state evidence.
2. Adapter runs the approved authoritative document/event reconciliation for the selected Space.
3. Duplicates and older observations do not duplicate or regress Sage lifecycle.
4. After a route change, the original Banqup entity, Space, document and connection identifiers continue to resolve historical lifecycle.

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

| ID | Demonstrable criterion |
|---|---|
| AC1 | Given authorised OAuth/app access, Sage exposes only permitted entities/spaces and binds the connection to the explicitly selected legal entity. |
| AC2 | Denied or revoked consent creates an actionable connection state, exposes no token, and changes no route. |
| AC3 | A validated Banqup connection can exist without an active route. |
| AC4 | A representative sales invoice completes metadata creation, binary upload, validation, send and lifecycle correlation with presigned URLs redacted. |
| AC5 | Awaiting-upload, validation and sending stages are not displayed as recipient delivery. |
| AC6 | A representative purchase invoice is ingested once with original Banqup entity/Space/document context; optional payment/approval workflow remains separate. |
| AC7 | Validation failures are actionable and the unchanged document is not sent/retried. |
| AC8 | Timed-out metadata/send mutations are reconciled before retry. |
| AC9 | Duplicate/out-of-order event tests do not duplicate or regress state; a missed event is recovered by authoritative read. |
| AC10 | Test and production applications, tokens, entities, spaces and documents cannot be mixed. |
| AC11 | Route deactivation preserves historical Banqup access and does not automatically revoke consent or participant registration. |

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

| Gate | Evidence required | Blocks |
|---|---|---|
| G1 — Product/API | Contracted Banqup/Unifiedpost service, region, stable API surface/version and artefact permission | Engineering commitment |
| G2 — Identity/consent | OAuth flow, app ownership/install/whitelist, scopes, token lifecycle, entity/Space mapping | Connection build |
| G3 — Spain/network | Formats, directions, connection/participant registration, lifecycle and route authority | Production scope |
| G4 — Events/safety | Message security, identity/order/retry/replay, idempotency and authoritative reconciliation | Async production |
| G5 — Service/exit | Limits, retention, data location, historical access, deregistration, SLA/support | Production readiness |
| G6 — Fixtures/pilot | Synthetic end-to-end, revocation, validation, timeout, duplicate, reconciliation and route-change evidence | Pilot |

## Risks

- Ambiguous Banqup and Unifiedpost product boundaries.
- Environment or tenant provisioning delays.
- Provider status semantics not mapping cleanly.
- Credential ownership differing between customer and Sage.

## Open questions

| ID | Decision required | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| OQ1 | Contracted product, region and stable API version? | Vendor/commercial + architecture | G1 | Public docs are discovery evidence only |
| OQ2 | Client Credentials or Authorization Code per Sage/customer scenario? | Product/security | G2 | Customer-facing multi-tenant flow likely needs delegated OAuth |
| OQ3 | Entity/Space/connection cardinality for one Sage legal entity? | Provider/architecture | G2 | Explicit selected Space is required |
| OQ4 | Spain networks, formats, directions and participant registration? | Local team/provider | G3 | Do not infer from Peppol announcement |
| OQ5 | Which Banqup document/delivery states are mandatory network lifecycle? | Product/local team | G3 | Exclude payment/approval unless approved |
| OQ6 | Message authentication, replay, order and reconciliation mechanism? | Provider/security/operations | G4 | Authoritative reads must back events |
| OQ7 | Idempotency, limits, retention, historical access and SLA? | Provider/operations/legal | G4/G5 | Open |
| OQ8 | Is Banqup a reference adapter/pilot? | Product/engineering | Pilot | Candidate; not decided |

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | Banqup (Unifiedpost) is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
| 2026-07-29 | Embedded official evidence, business rules, API example, lifecycle/safety analysis, testable acceptance and production gates | |
