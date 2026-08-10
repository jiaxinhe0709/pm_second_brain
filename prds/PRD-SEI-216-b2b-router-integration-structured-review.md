---
id: PRD-SEI-216
title: Provider Integration — B2B Router — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-204
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - research/provider-apis/b2b-router/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "855180241"
  page_id: "866148399"
  title: Provider Integration — B2B Router — Structured Review
  layout: two_left_sidebar
  toc: true
---

# Provider Integration — B2B Router — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-204, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-216, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-204. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-204; this successor introduces no new product decision. |

## Summary

Connect eligible Spanish e-invoicing customers to B2B Router through the shared private-platform connection, routing, and resilience foundation.

This is a Phase 2 provider-integration PRD. It defines the B2B Router-specific evidence, product behaviour, provider boundary, journeys, risks, and readiness gates. It does not redefine the shared connection, routing, transition, or resilience model owned by PRD-SEI-201–203.

> **Product principle:** B2B Router may determine how a document is exchanged after Sage selects this connection; it must not silently determine whether B2B Router is the customer's active Sage route.

## Problem

Sage requires a consistent way to onboard customers to B2B Router and exchange invoices without exposing provider-specific behaviour to every Sage ERP. Provider capabilities and constraints have not yet been confirmed and must be established during discovery.

B2B Router exposes public REST documentation covering accounts, contacts, directory lookup, transports, invoice creation/import, invoice retrieval, document rendering, attachments, webhooks, and Spain tax-reporting functions. Phase 2 must identify which of these capabilities implement private B2B exchange and avoid conflating them with VeriFactu or other tax-reporting services.

### Why a generic adapter is insufficient

- B2B Router distinguishes accounts, contacts, transports, document types, issued invoices, and received invoices; these concepts do not map one-to-one to a Sage route.
- Invoice sending may continue asynchronously after creation or import, so an accepted API request is not equivalent to final delivery.
- B2B Router may derive transport and document type from a contact, directory result, or account default. Sage must not allow this fallback behaviour to override an authorised route decision without visibility.
- Webhooks provide asynchronous notification capability, but public documentation reviewed so far does not establish the authentication, retry, ordering, or retention guarantees Sage needs for production.
- B2B Router documents VeriFactu and other tax-reporting capabilities alongside invoice exchange. Those capabilities must remain outside this private-platform integration unless separately approved.

## Delivery boundary

| Capability | This PRD | Shared PRD owner | Current treatment |
|---|---|---|---|
| B2B Router account and credential mapping | Define | PRD-SEI-202 supplies shared connection model | Discovery |
| B2B Router transport and document-type mapping | Define | PRD-SEI-202 supplies route/capability model | Discovery |
| B2B Router invoice submission and retrieval | Define | PRD-SEI-203 supplies resilience rules | Discovery |
| Public ↔ Private route activation | Consume | PRD-SEI-201 and PRD-SEI-202 | Must not be reimplemented here |
| Historical invoice continuity | Consume and prove for B2B Router | PRD-SEI-201–203 | Required |
| Provider monitoring and reconciliation | Define provider evidence/actions | PRD-SEI-203 supplies common operations model | Required |
| VeriFactu or AEAT tax reporting | Exclude | Separate product scope | Out of scope |
| Private Provider A → B2B Router switching | Exclude | Phase 3 | Future |

## Evidence and research findings

This section is intentionally self-contained for Confluence readers. The repository research note remains a working evidence index, but no decision in this PRD requires access to that file.

### Evidence register

Evidence was rechecked against B2B Router's public documentation on 2026-07-29. Public documentation confirms API surface and observable behaviour; it does **not** confirm Sage's contracted product, Spain private-platform eligibility, commercial limits, production support, or regulatory routing authority.

| Ref | Official source | Confirmed finding | Confidence and limitation | PRD impact |
|---|---|---|---|---|
| E1 | [API introduction](https://docs.b2brouter.net/en/developers/start-using-our-api/introduction/) | REST access uses `X-B2B-API-Key`; environment-specific keys are documented; responses are JSON; a group default API version can be overridden using `X-B2B-API-Version`. | **Confirmed public behaviour.** Exact contracted version and credential ownership remain open. | FR3, FR4, FR31–FR34; production gate G2 |
| E2 | [API introduction — environments and limits](https://docs.b2brouter.net/en/developers/start-using-our-api/introduction/) | Sandbox, staging, and production are documented. Current public limits state 1,000 requests/minute in production and 600 requests/minute in sandbox/staging, returning HTTP 429 when exceeded. | **Confirmed in current public docs.** Contractual limits and headers must be tested; values may change by plan/version. | NFR5–NFR7; capacity and throttling tests |
| E3 | [List invoices](https://developer.b2brouter.net/reference/get-invoices) | Account-scoped invoice listing is paginated; the reference exposes issued/received invoice types and lifecycle-related filters. | **Confirmed API surface.** Incremental-watermark suitability and retention window are not established. | FR26, FR28, FR35; reconciliation design |
| E4 | [Import invoice](https://developer.b2brouter.net/reference/import-invoice) | A supported file can be imported; `send_after_import=true` may queue sending asynchronously. Transport and document-type selection can be taken from the contact, directory, or account default. | **Confirmed API behaviour.** Sage payload strategy and permitted fallback policy are open. | BR4, FR20–FR25, FR36–FR38; architecture decision D2 |
| E5 | [Get invoice](https://developer.b2brouter.net/reference/get-invoice) | B2B Router exposes a provider-unique invoice identifier and retrieves issued or received invoice information. | **Confirmed API surface.** Full historical-access duration and redirect/download behaviour require testing. | FR5, FR22, FR24, FR30; continuity tests |
| E6 | [Create webhook](https://developer.b2brouter.net/reference/create-web-hook) and [issued-invoice state-change event](https://developer.b2brouter.net/reference/getnewinvoicestatechange) | Webhooks can be created for selected events under the API key's integration group. The documented invoice state-change event carries `code`, `triggered_at`, and `data`; `X-B2Brouter-Signature` uses HMAC-SHA256 over timestamp and JSON data. | **Confirmed public mechanism.** Secret provisioning/rotation, replay window, retry schedule, ordering, event identity, replay and retention still require provider/sandbox proof. | FR8, FR27–FR29, FR39–FR42; production blocker G4 |
| E7 | [Spain VeriFactu guide](https://docs.b2brouter.net/en/developers/guides-by-country/spain/verifactu/) | B2B Router documents a separate tax-report lifecycle with AEAT submission, tax-report IDs, webhooks/polling, correction, and annulment. | **Confirmed tax-report product capability, not evidence of private B2B routing.** | BR6 and explicit scope exclusion |
| E8 | [Public API reference](https://developer.b2brouter.net/reference) | Accounts, transports, contacts, directory, invoices, documents, attachments, events, and webhook resources are publicly discoverable. | **Confirmed breadth, not contracted entitlement.** Machine-readable specification and permission to retain it are still required. | Discovery inventory and production gate G1 |
| E9 | [Invoice state-change operation](https://developer.b2brouter.net/v2025-10-13/reference/mark-as-invoice) and [invoice-state catalogue](https://developer.b2brouter.net/reference/get-invoice-states) | Public documentation exposes different issued/received invoice states and allows some states to be changed or notified manually. | **Confirmed public state vocabulary.** Event provenance, permitted automated transitions, terminality and Spain contract behaviour require validation. | FR6, FR29, FR38 and lifecycle mapping |

### Provider capability matrix

| Capability | Public evidence status | Phase 2 treatment | Evidence or decision still required |
|---|---|---|---|
| API-key authentication | Confirmed | Proposed provider credential type | Key scope, rotation, expiry, revocation, customer/group ownership |
| Versioned REST/JSON API | Confirmed | Pin an approved version | Contracted version, deprecation window, changelog owner |
| Sandbox, staging, production | Confirmed | Isolate all environments | Sage access, representative test data, production parity |
| Account discovery | Confirmed | Proposed legal-entity anchor | Account/group/organisational-unit ownership and tenancy mapping |
| Contact management | Confirmed | Use only if selected design requires it | Duplicate rules, customer ownership, update authority |
| Directory lookup | Confirmed capability | Supporting route evidence only | Whether it is authoritative for Spain private reachability |
| Transport configuration | Confirmed capability | Map to connection capability, not Sage route | Supported Spain transport codes and activation prerequisites |
| JSON invoice creation | Confirmed capability | Candidate outbound strategy | Supported Spain fields, validation, corrections, credit notes |
| Structured-file invoice import | Confirmed capability | Candidate outbound strategy | Approved formats, schema versions, lossless mapping |
| Asynchronous sending | Confirmed | Required lifecycle handling | Provider state model, terminal states, timeout reconciliation |
| Issued and received invoice retrieval | Confirmed capability | Candidate inbound and reconciliation mechanism | Incremental cursor/watermark, retention, acknowledgement semantics |
| Webhooks and HMAC signature | Confirmed capability/mechanism | Preferred notification candidate | Secret lifecycle, replay tolerance, retries, ordering and stable event identity |
| Legal document/rendering | Confirmed capability | Candidate audit/customer retrieval | Trusted-copy status, format fidelity, retention and access |
| Attachments | Confirmed capability | Conditional | Size/type limits, malware scanning, retrieval and retention |
| Provider idempotency | Unknown | Do not assume | Keys, duplicate response, expiry window, safe retry by operation |
| Spain private-platform onboarding/registration | Unknown | Production blocker | Contracted workflow, legal authority, coexistence and deregistration |
| Lifecycle/status mapping | Partially evidenced | Discovery mapping required | Complete provider states/events and Sage mapping approval |
| SLA, support and incident escalation | Unknown | Production blocker | Contract, severity model, escalation channel and evidence pack |
| Historical access after deactivation | Unknown | Production blocker | Access duration, credential dependency and deregistration effect |
| VeriFactu/tax reporting | Confirmed separate capability | Out of scope | Separate approval if ever combined |

### What the public evidence does not prove

The following must not be inferred from the endpoint inventory:

- that Sage is entitled to use every documented endpoint in its intended subscription;
- that a B2B Router directory result is Spain's authoritative public/private routing decision;
- that B2B Router is approved as a Spanish private platform for every Sage customer segment;
- that inbound and outbound availability are symmetrical;
- that an HTTP success means an invoice has reached its final recipient;
- that webhook delivery alone is sufficient for lifecycle completeness;
- that account defaults are safe substitutes for an explicit Sage routing decision;
- that tax-reporting configuration is part of the private-platform onboarding journey.

### Evidence confidence summary

| Evidence class | Current assessment |
|---|---|
| Public API discoverability | High |
| Basic authentication, version and environment model | High for public API; medium for Sage contract |
| Outbound create/import and asynchronous-send capability | High |
| Invoice listing/retrieval and webhook availability | High for existence; low/medium for production guarantees |
| Sage legal-entity/account mapping | Low |
| Spain private-platform registration and route authority | Low |
| Idempotency, retention, SLA, support and deregistration | Low |
| Overall readiness | **Consultation-ready; not delivery-ready** |

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

- **Customer administrator:** authorises one legal entity to use an eligible B2B Router account and understands which invoice direction will be activated.
- **Accountant or delegated administrator:** configures permitted entities without gaining visibility of unrelated B2B Router accounts.
- **Sage ERP/API consumer:** initiates connection setup and exchanges invoices through stable Sage APIs rather than provider endpoints.
- **Sage routing and invoice services:** resolve the effective connection, persist the routing decision, and invoke the adapter.
- **Sage operations and support:** distinguish Sage, customer, credential, configuration, provider, and recipient failures without accessing secrets or unrestricted invoice content.
- **Security/compliance:** approves credential custody, tenant segregation, data flows, retention, logging, and provider access.

## Business scenarios and rules

### Priority scenarios

| Scenario | Trigger and actor | Expected outcome | Provider-specific exception |
|---|---|---|---|
| Prepare without activation | Administrator supplies B2B Router configuration | Connection becomes validated/ready; current public routes remain unchanged | Account or required transport cannot be proven |
| Activate outbound only | Authorised route transition selects B2B Router outbound | New outbound invoices use B2B Router; inbound route is unchanged | Selected transport/document type is unsupported |
| Receive through B2B Router | Provider makes a received invoice available | Sage ingests it once and stores original provider context | Webhook is missed, duplicated, reordered, or unauthenticated |
| Correct outbound validation | Provider rejects the document before send | Customer receives actionable correction details; unchanged payload is not retried | Provider error cannot be mapped safely |
| Reconcile ambiguous send | Sage times out after transmitting a mutation | Outcome is marked unknown and reconciled before repeat | No stable correlation or search mechanism exists |
| Route changes away | Customer activates another route for new invoices | Existing B2B Router invoices retain retrieval and lifecycle access | Deregistration or credential revocation would remove required access |
| Disable compromised connection | Security/operations disables new operations | New calls stop; evidence and historical identifiers remain auditable | In-flight provider work still requires controlled retrieval |

### Business rules

| ID | Condition | Rule | Rationale/evidence | Status |
|---|---|---|---|---|
| BR1 | A B2B Router account and credentials have been validated | Validation may make the connection ready but must not activate a Sage route. | Shared Phase 2 routing decision | Confirmed |
| BR2 | Public and B2B Router connections coexist | Inbound and outbound may select different effective connections. | PRD-SEI-201/202 | Confirmed |
| BR3 | A route selects B2B Router | Sage must persist the B2B Router account, actual transport/document type, provider invoice ID, direction, and API version used for the invoice. | Historical continuity requirement | Confirmed product requirement |
| BR4 | B2B Router can derive transport/document type from contact, directory, or defaults | Sage must detect and expose the actual resolved values; an incompatible fallback must not silently contradict the authorised route. | E4 | Proposed pending sandbox proof |
| BR5 | B2B Router accepts an invoice for asynchronous sending | Accepted/imported/queued is not equivalent to delivered, accepted by recipient, or terminal. | E4 | Confirmed provider constraint |
| BR6 | VeriFactu/tax-report capability is present | Tax reporting remains logically and operationally separate from Phase 2 private B2B routing. | E7 | Confirmed scope rule |
| BR7 | Route moves away from B2B Router | Historical B2B Router invoices retain their original provider context and required lifecycle access. | PRD-SEI-201 | Confirmed |
| BR8 | Provider outcome is unknown | Sage must reconcile before repeating a mutation unless idempotency is proven for that operation and version. | PRD-SEI-203; idempotency evidence open | Confirmed product requirement |

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

### Authentication, version and environment

| ID | Requirement |
|---|---|
| FR31 | Each B2B Router credential reference must identify its environment, owning customer/account scope, creation/rotation status, and last successful validation without exposing the key. |
| FR32 | Every provider request must use the approved explicit API version; Sage must not rely on a mutable group default in production. |
| FR33 | Connection validation must prove that the credential can access the intended account and must not accept access to an unrelated account as readiness. |
| FR34 | Credential rejection or revocation must make new provider operations ineligible, preserve audit/history, and expose an authorised recovery action. |

### Resolution, events and reconciliation

| ID | Requirement |
|---|---|
| FR35 | Invoice-list reconciliation must use bounded pagination and a durable high-water mark or other proven incremental strategy; the selected strategy must tolerate overlapping reads. |
| FR36 | After create/import, Sage must retain the actual transport and document type returned or observed from B2B Router rather than only the values requested. |
| FR37 | If B2B Router substitutes a default transport or document type that is incompatible with the authorised route/capability, Sage must stop progression and surface a configuration discrepancy. |
| FR38 | Sage must represent provider acceptance/import, queued sending, delivery/lifecycle progress, and terminal outcome as distinct observable stages where B2B Router exposes them. |
| FR39 | Webhook processing must validate `X-B2Brouter-Signature` using the provider-documented HMAC-SHA256 construction, enforce an approved timestamp/replay policy, and define signing-secret provisioning and rotation before production. |
| FR40 | Every webhook/event must be correlated and deduplicated using a provider event identity or a documented composite identity; delivery time alone is insufficient. |
| FR41 | Webhook gaps must be recoverable through an approved replay, event listing, invoice listing, or equivalent reconciliation path. |
| FR42 | Webhook configuration, subscribed event types, endpoint state, last successful receipt, and reconciliation freshness must be visible to authorised operations. |

## Proposed solution and API mapping

### Conceptual provider boundary

The following is a **proposed model for architecture review**, not an approved implementation:

| Sage concept | Proposed B2B Router context | Context Sage must retain | Open design point |
|---|---|---|---|
| Provider connection | API credential + B2B Router group/account access | Credential reference, environment, approved API version, validation evidence | Whether credential belongs to customer, accountant, Sage, or integration group |
| Customer legal entity | B2B Router account or organisational unit | Stable account identifier and ownership scope | Exact account/group/unit mapping |
| Connection capability | Available transport + document type + direction | Provider codes, observed availability, evidence time | Whether capabilities can be discovered reliably |
| Receiver evidence | Contact and/or directory lookup result | Lookup inputs, schemes, result, resolved values, observation time | Whether directory is authoritative in Spain |
| Sage route | Shared Sage route referencing the B2B Router connection | Route scope/version/effective time | Never represented only by a B2B Router transport |
| Invoice context | B2B Router invoice and selected exchange values | Provider invoice ID, account, direction, actual transport/document type, API version | Complete lifecycle/status fields |
| Provider event | Webhook/event or invoice-list observation | Event/composite identity, observed time, payload version/hash, processing result | Signing, ordering, replay and retention |

### Publicly documented operation inventory

The paths below are publicly documented but remain subject to the selected API version, contracted product, sandbox proof, and architecture approval. They are included so Confluence readers can understand the current integration hypothesis without opening a separate research file.

| Sage capability | B2B Router operation |
|---|---|
| List provider accounts | `GET /accounts` |
| Configure transport | `POST /accounts/{ACCOUNT_ID}/transports` |
| Resolve directory entry | `GET /directory/{country}/{identifier}` |
| List contacts | `GET /accounts/{ACCOUNT_ID}/contacts` |
| Create contact | `POST /accounts/{ACCOUNT_ID}/contacts` |
| Create invoice from JSON | `POST /accounts/{ACCOUNT_ID}/invoices` |
| Import supported invoice file | `POST /accounts/{ACCOUNT_ID}/invoices/import` |
| List invoices | `GET /accounts/{ACCOUNT_ID}/invoices` |
| Retrieve invoice | `GET /invoices/{INVOICE_ID}` |
| Render selected format | `GET /invoices/{INVOICE_ID}/as/{document_type_code}` |
| Retrieve legal document | `GET /invoices/{INVOICE_ID}/as/legal` |
| Add attachment | `POST /invoices/{INVOICE_ID}/add_attachment` |
| Configure webhook candidate | `POST /web_hooks` |

### Illustrative API interactions

These compact examples expose the currently evidenced contract shape to Confluence readers. They are **not approved test fixtures** and deliberately omit invoice fields whose final mapping depends on the selected API version and Spain product scope.

#### Create and asynchronously send an outbound invoice

The public reference confirms the account-scoped path, API headers, JSON invoice wrapper, and `send_after_import` behaviour:

```http
POST /accounts/{B2B_ROUTER_ACCOUNT_ID}/invoices
X-B2B-API-Key: <secret supplied by approved credential store>
X-B2B-API-Version: {APPROVED_API_VERSION}
Content-Type: application/json
```

```json
{
  "send_after_import": true,
  "invoice": {
    "...": "approved canonical-to-B2B-Router field mapping"
  }
}
```

Expected evidenced response class: HTTP `201` with the created invoice representation. Product interpretation: created/queued is non-terminal; Sage must retain the returned provider invoice identity and observe later lifecycle state.

#### Import an approved structured invoice file

```http
POST /accounts/{B2B_ROUTER_ACCOUNT_ID}/invoices/import?send_after_import=true
X-B2B-API-Key: <secret supplied by approved credential store>
X-B2B-API-Version: {APPROVED_API_VERSION}
Content-Type: <approved structured document media type>

<approved UBL, CII, Facturae, or other selected document>
```

The exact media type, format/schema version, validation response, signing compatibility, and lossless mapping must be captured from the approved OpenAPI version and sandbox tests before implementation commitment.

#### Receive a signed invoice state-change webhook

The public webhook reference confirms this top-level event shape and signature header:

```http
X-B2Brouter-Signature: t={UNIX_TIMESTAMP},s={HMAC_SHA256_SIGNATURE}
Content-Type: application/json
```

```json
{
  "code": "issued_invoice.state_change",
  "triggered_at": 1732530071,
  "data": {
    "...": "event fields defined by the approved API version"
  }
}
```

Sage must verify the signature and replay window before using `data`. The final event identity, invoice correlation fields, state values, and ordering behaviour must be captured as tested fixtures rather than inferred.

#### Reconcile received invoices

```http
GET /accounts/{B2B_ROUTER_ACCOUNT_ID}/invoices?type=ReceivedInvoice&offset={OFFSET}&limit={LIMIT}
X-B2B-API-Key: <secret supplied by approved credential store>
X-B2B-API-Version: {APPROVED_API_VERSION}
```

The current reference documents pagination and received-invoice filtering. The implementation must add an approved overlap/high-water-mark strategy because offset pagination alone does not prove gap-free incremental retrieval.

### Required versioned API assets

Full samples belong in GitHub assets and automated tests, not as large unverified payloads in this PRD. Before the delivery gate, the team must create a sanitised, approved evidence pack under `assets/provider-apis/b2b-router/{APPROVED_API_VERSION}/` containing:

| Asset | Required content |
|---|---|
| API contract | Provider OpenAPI or approved extracted contract, with storage permission recorded |
| Outbound fixtures | Minimal valid create/import request, accepted response, asynchronous state progression |
| Inbound fixtures | Received invoice/list response and original structured document |
| Event fixtures | Validly signed event, invalid signature, expired timestamp, duplicate and out-of-order events |
| Error fixtures | Authentication, validation, not-found, conflict if supported, throttling and server failure |
| Reconciliation fixtures | Timeout after possible success, provider match, proven absence and ambiguous match |
| Format fixtures | Approved Spain formats, credit/correction examples and expected lossless mappings |

Fixtures must contain synthetic parties and identifiers only. They must not contain API keys, customer data, confidential exports, or unrestricted provider material.

### Operation-safety classification

This table defines required treatment until sandbox evidence proves stronger provider guarantees.

| Operation class | Examples | Default safety treatment | Evidence needed to change treatment |
|---|---|---|---|
| Read-only | List accounts, directory lookup, list/get invoices, retrieve document | Retry with bounds where response is not received; record freshness | Rate-limit headers, timeout behaviour, retention |
| Locally deduplicated mutation | Contact or configuration change where Sage controls a stable desired state | Compare intended/observed state before repeating | Provider uniqueness and update semantics |
| Outcome-unknown mutation | Create/import/send invoice, configure transport, create webhook | Do not blindly repeat after post-transmission timeout; reconcile first | Provider idempotency key/duplicate guarantee and search identity |
| Human-authorised destructive action | Deregistration, credential revocation, historical-access removal | Explicit approval, dependency check, audit, and post-action verification | Contracted provider sequence and rollback behaviour |

### Proposed lifecycle mapping

This mapping is for product and provider consultation. It is not approved until sandbox events, retrieval responses, and manual-versus-network provenance are understood.

| B2B Router observation | Proposed Sage category | Customer meaning allowed now | Validation required |
|---|---|---|---|
| `new` | Prepared/draft | Provider record exists but no delivery claim | Whether state can appear for both issued and received invoices in selected flow |
| `issued` | Issued/non-terminal | Document is read-only/issued within B2B Router; not necessarily sent | Exact event and transition source |
| queued after `send_after_import` | Submitted/processing | Provider accepted asynchronous work | Returned field/event identifying queued state |
| `sent` | Sent by provider | B2B Router reports sent; do not call it recipient delivery without evidence | Transport-specific meaning and proof |
| `registered` | Registered | Provider records registration; registration reference may exist | Whether state is network-received or manual |
| `accepted` | Accepted | Acceptance recorded | Actor/provenance and whether recipient acceptance is authoritative |
| `refused` | Rejected/refused | Refusal recorded with reason where available | Actor, reason schema and correction path |
| `paid` / `allegedly_paid` | Payment-related | Payment indication only, preserving provider wording/provenance | Legal/customer meaning and direction |
| `closed` | Closed | Provider record is closed | Whether terminal and which later events remain possible |
| received-invoice `annotated` | Annotated | Provider/customer annotation exists | Whether relevant to Sage lifecycle |
| unknown/new provider state | Unmapped provider state | Do not discard or silently coerce; retain raw value and alert mapping owner | Changelog/mapping review |

Sage must retain whether a status originated from provider network evidence, a customer/manual action, a Sage action, or an inferred reconciliation observation. Identical state labels with different provenance must not automatically carry identical business meaning.

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

### Correct a validation failure

1. B2B Router rejects the create/import request with provider validation detail.
2. Adapter classifies the response as a correctable business/document error rather than a transient provider failure.
3. Sage maps provider paths/codes to the closest stable Sage field/category and retains the redacted provider detail for diagnosis.
4. Customer or ERP corrects the invoice and submits a new Sage attempt with a new audit entry.
5. Sage does not automatically repeat the unchanged invalid payload.

Expected result: the customer can correct the document without duplicate provider invoices or an opaque support request.

### Reconcile an unknown submission outcome

1. Sage sends a create/import or send-triggering mutation and loses the response after transmission may have occurred.
2. Operation enters `OUTCOME_UNKNOWN` (proposed state) with the Sage correlation identity and request evidence.
3. Adapter searches the approved provider retrieval surface using stable provider/customer/document context.
4. If exactly one matching provider invoice is proven, Sage records its provider ID and resumes lifecycle processing.
5. If absence is proven and retry is safe, Sage resubmits under the approved duplicate-protection policy.
6. If outcome remains ambiguous, operations receives a controlled recovery case; automatic resubmission stops.

Expected result: uncertainty never becomes an automatic duplicate.

### Recover a webhook gap

1. Monitoring detects stale webhook receipt, a sequence gap, or provider/Sage state discrepancy.
2. Adapter lists/retrieves invoices using an overlapping bounded window or other approved reconciliation cursor.
3. Already processed invoices/events are deduplicated.
4. Missing lifecycle observations are applied without regressing later states.
5. Reconciliation records its range, result, freshness, and unresolved discrepancies.

Expected result: webhook delivery is an acceleration mechanism, not the only record of provider state.

### Deactivate route while preserving historical access

1. Customer transitions new invoice routing away from B2B Router through the shared transition workflow.
2. Sage stops selecting the connection for the deactivated route scope.
3. Existing B2B Router invoices retain account, provider ID, original transport/document type, and lifecycle context.
4. Credentials and provider registration remain available only for required historical operations until the retention/exit decision permits removal.
5. Final deregistration or credential revocation runs as a separate authorised action.

Expected result: changing the current route does not make older invoices unreadable or unauditable.

## Failure behaviour

| Scenario | Classification | Expected behaviour | Recovery evidence |
|---|---|---|---|
| API key rejected/revoked | Customer/security action required | Stop new provider calls, keep connection/history visible, request authorised credential recovery | Successful validation against intended account |
| Credential can access wrong account | Tenancy/security discrepancy | Connection remains non-ready; do not expose unrelated account data | Correct account-scope proof |
| Account or transport missing | Configuration incomplete | Keep connection non-ready and return specific setup action | Account/transport capability revalidation |
| Directory returns no result | Recipient unresolved | Follow approved no-route policy; do not invent a transport | New authoritative lookup/route evidence |
| Provider substitutes a default | Configuration discrepancy | Compare actual values with approved capability; stop when incompatible | Corrected contact/transport configuration |
| Invoice returns validation error | Correctable document failure | Return mapped field errors; do not retry unchanged payload | Corrected payload creates a new attempt |
| HTTP 429 throttling | Transient capacity control | Honour provider guidance where available; apply bounded backoff and queue visibility | Successful later response and reduced pressure |
| Timeout before transmission | Safe transient failure if proven | Retry within shared policy | Transport evidence proves request was not sent |
| Timeout after possible mutation | Outcome unknown | Retrieve/reconcile before resubmission | Unique provider match, proven absence, or manual decision |
| Provider success before Sage persistence | Cross-system inconsistency | Recover from durable intent/correlation and provider retrieval; never recreate immediately | Provider ID persisted and operation reconciled |
| Webhook duplicated | Duplicate event | Acknowledge safely and process once | Deduplication record |
| Webhook out of order | Stale observation | Retain evidence but do not regress lifecycle | State precedence/version or later provider retrieval |
| Webhook missing or unverifiable | Notification gap/security failure | Do not trust unverified content; reconcile from provider API | Fresh authenticated retrieval |
| Attachment exceeds applicable limit | Pre-submission validation | Reject before upload where limit is known | Customer supplies compliant attachment |
| Concurrent route/credential change | Conflict | Use configuration version; reject or restart stale work | Current route and credential version |
| Provider degradation | External incident | Apply shared queue, circuit breaking, reconciliation, communication, and escalation | Health recovery plus backlog reconciliation |
| Historical retrieval fails after deactivation | Continuity failure | Stop deregistration/revocation progression and escalate | Required history accessible or approved retention outcome |

## Security and non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | API keys must be held in approved secret storage, encrypted in transit/at rest, access-audited, and never returned through client APIs or diagnostic exports. |
| NFR2 | Sandbox, staging, and production credentials, account IDs, webhooks, data, queues, and monitoring must remain isolated. |
| NFR3 | Logs and support evidence must redact credentials, invoice contents, personal data not required for diagnosis, and any document URL that grants access. |
| NFR4 | Provider requests, responses, and events must be traceable using Sage correlation, provider identifiers, environment, and approved API version. |
| NFR5 | Capacity design must account for the currently documented public limits of 1,000 requests/minute in production and 600 requests/minute in sandbox/staging, while treating the contracted limits as the production authority. |
| NFR6 | HTTP 429 handling must use bounded delay/backoff, preserve work, avoid retry storms, and expose throttling/backlog health. |
| NFR7 | Pagination and reconciliation scans must be bounded, resumable, overlap-safe, and observable. |
| NFR8 | The selected API version must be pinned; provider changelog review and compatibility ownership must be assigned before production. |
| NFR9 | No production dependency may rely solely on webhook delivery until authentication, retry/replay, and reconciliation have passed failure testing. |
| NFR10 | Required availability, latency, recovery, retention, and support targets remain production gates until product/operations owners approve baselines and contracted commitments. |

## Acceptance criteria

| ID | Demonstrable acceptance criterion | Traces to |
|---|---|---|
| AC1 | Given valid non-production credentials scoped to the intended B2B Router account, when an administrator validates the connection, then Sage records account/capability evidence and marks the connection ready without changing any route. | BR1, FR3–FR4, FR11–FR12, FR31–FR33 |
| AC2 | Given credentials that can access an unintended account, when validation runs, then the connection remains non-ready and no unrelated account data is exposed to the customer. | FR13, FR33, NFR1–NFR3 |
| AC3 | Given public inbound and ready B2B Router outbound connections, when authorised outbound activation completes, then only new outbound invoices select B2B Router. | BR2, PRD-SEI-201/202 |
| AC4 | Given an approved outbound invoice, when B2B Router imports/accepts it for asynchronous send, then Sage stores provider identity and actual transport/document type while showing a non-terminal lifecycle stage. | BR3–BR5, FR20–FR22, FR36–FR38 |
| AC5 | Given B2B Router substitutes an incompatible default transport/document type, when Sage observes the result, then progression stops with a configuration discrepancy rather than reporting successful routing. | BR4, FR36–FR37 |
| AC6 | Given a correctable provider validation response, when Sage maps the error, then the ERP/customer sees actionable detail and the unchanged payload is not automatically retried. | FR6, FR23 |
| AC7 | Given a post-transmission timeout, when the outcome is unknown, then Sage reconciles provider state and does not resubmit until one result, proven absence, or authorised manual decision establishes safety. | BR8, FR7, PRD-SEI-203 |
| AC8 | Given duplicate and out-of-order webhook events, when they are processed, then one invoice lifecycle is retained and a later state is not regressed. | FR27, FR29, FR40 |
| AC9 | Given a webhook gap, when reconciliation runs over an overlapping invoice window, then missing observations are recovered without duplicate invoices and reconciliation freshness is recorded. | FR28, FR35, FR41–FR42, NFR7 |
| AC10 | Given a received invoice exposed by the approved provider mechanism, when Sage ingests it, then the original document/provider ID is stored exactly once with B2B Router as immutable origin context. | FR5, FR26–FR30 |
| AC11 | Given test credentials or account IDs, when a production operation is attempted, then Sage blocks the cross-environment use before provider submission. | FR4, FR14, NFR2 |
| AC12 | Given a route transition away from B2B Router, when an older B2B Router invoice receives a status or retrieval request, then Sage uses its original provider context and does not rewrite it to the new route. | BR7, PRD-SEI-201 |
| AC13 | Given historical lifecycle dependencies remain, when deregistration or credential revocation is requested, then Sage blocks or sequences the action according to the approved exit policy and records the authorisation. | FR10, continuity journey |
| AC14 | Given tax-reporting fields or IDs appear in a provider response, when Phase 2 processes the invoice, then those fields remain separately identifiable and do not silently activate VeriFactu behaviour. | BR6 |

## User experience

The shared onboarding experience must show B2B Router-specific data requirements, validate them before activation, and distinguish configuration, registration, readiness, and active route status.

## Metrics

Targets must not be fabricated before a pilot baseline and contracted service commitments exist.

| Measure | Why it matters | Segmentation | Baseline/target owner |
|---|---|---|---|
| Connection validation completion rate | Shows onboarding/configuration friction | ERP, environment, failure category | Product; baseline in sandbox/pilot |
| Outbound accepted, sent, and terminal-success rates | Separates API acceptance from exchange outcome | Operation, transport, document type | Product/operations |
| Inbound ingestion completeness and duplication | Tests notification plus reconciliation design | Webhook vs reconciliation source | Engineering/operations |
| Validation failure correction rate | Shows whether errors are actionable | Provider code and Sage category | Product/ERP teams |
| Outcome-unknown count and age | Exposes duplicate/loss risk | Operation and environment | Operations |
| Reconciliation freshness and discrepancy backlog | Shows lifecycle completeness | Account and direction | Operations |
| Throttled request and backlog age | Shows capacity pressure | Endpoint class/environment | Engineering |
| Status/error mapping coverage | Prevents opaque provider behaviour | Provider API version | Product/QA |
| Historical-access failures after route change | Tests continuity promise | Invoice age and transition | Product/operations |

## Rollout

1. **Contract discovery:** confirm the intended B2B Router product, commercial owner, Spain scope, API version, technical contacts, and permission to retain technical artefacts.
2. **Sandbox evidence:** obtain isolated test access and capture approved synthetic fixtures for connection, outbound, inbound, validation, webhook, timeout, duplication, reconciliation, and historical retrieval.
3. **Architecture decision:** approve legal-entity/account mapping, credential ownership, payload strategy, status/error model, webhook/reconciliation design, and exit sequence.
4. **Adapter implementation:** implement only the approved capability subset behind shared connection/routing/resilience contracts.
5. **Operational proving:** complete security review, load/throttling tests, fault injection, dashboards, alerts, runbooks, support escalation, and evidence redaction.
6. **Controlled pilot:** activate an agreed ERP/customer cohort with explicit success/stop criteria and recoverable routing.
7. **Production expansion:** expand only after pilot measures and provider/Sage state reconciliation meet approved thresholds.

### Provider readiness gate

| Gate | Evidence required | Blocks |
|---|---|---|
| G1 — Contract and artefacts | Intended subscription/transaction model, technical owner, approved API/OpenAPI version, storage permission | Engineering commitment |
| G2 — Identity and access | Customer/group/account mapping, credential owner/scope/rotation, sandbox/staging/production access | Connection implementation |
| G3 — Spain capability | Private B2B registration, supported segments, directions, formats, transports, lifecycle, coexistence and deregistration | Production scope |
| G4 — Events and safety | HMAC secret lifecycle/replay policy, event identity, retry/order/replay behaviour, idempotency and reconciliation proof | Asynchronous production processing |
| G5 — Limits and service | Contracted rate/payload limits, availability/support commitments, retention, data residency and incident escalation | Production readiness |
| G6 — Tested fixtures | Approved synthetic inbound/outbound, validation, timeout, duplicate, out-of-order, throttling, reconciliation and historical-access evidence | Delivery approval |
| G7 — Operating model | Monitoring, reconciliation freshness, runbooks, manual recovery, audit, support handoff and pilot stop criteria | Pilot activation |

## Risks

| Risk | Consequence | Mitigation/control | Remaining evidence |
|---|---|---|---|
| Public API differs from contracted capability | Build unusable or unsupported features | G1/G3 contract confirmation; implement declared subset only | Contract/product pack |
| Account/group mapping is wrong | Cross-customer data exposure | Explicit account-scope validation and tenancy tests | Provider ownership model |
| Directory/default transport silently overrides intent | Misrouted or wrongly formatted invoice | Persist requested/actual values; discrepancy stop; BR4/FR36–37 | Sandbox transport tests |
| Async acceptance is shown as delivery | False customer/compliance status | Distinct stages and terminal-state mapping | Complete state/event inventory |
| Mutation is not safely idempotent | Duplicate registration/invoice | Outcome-unknown workflow and reconciliation-before-retry | Per-operation guarantees |
| Webhook is missed, replayed or forged | Missing/incorrect lifecycle | HMAC verification, replay policy, dedupe and independent reconciliation | Secret lifecycle and delivery behaviour |
| Offset listing changes while scanning | Reconciliation gap/duplicate | Overlap-safe cursor strategy and test under concurrent arrivals | Sandbox pagination behaviour |
| Sandbox differs from production | Undetected production failure | Staging/pilot proving and environment-specific health | Provider parity statement |
| Status/error mapping loses semantics | Opaque or wrong customer action | Preserve raw redacted detail, mapping coverage and unknown category | Full code/state inventory |
| Route deactivation removes historical access | Lifecycle/audit break | Separate route, deregistration and credential lifecycle | Retention and exit contract |
| API version changes | Behaviour/schema regression | Explicit pinned version, changelog owner, compatibility testing | Deprecation policy |
| Tax reporting becomes coupled accidentally | Scope/compliance confusion | BR6, separate identifiers/configuration and acceptance test AC14 | Product boundary review |

## Open questions

| ID | Question/decision required | Why it matters | Proposed owner | Blocks | Current hypothesis |
|---|---|---|---|---|---|
| OQ1 | Which contracted B2B Router product and API version will Sage use? | Determines entitlement, schema and support | Commercial/provider owner + architecture | G1; engineering commitment | Current public reference is discovery evidence only |
| OQ2 | How does a Sage legal entity map to B2B Router group, account or organisational unit? | Determines tenancy, credential scope and invoice ownership | Provider + architecture + security | G2 | One stable provider account scope per Sage legal entity unless delegation model proves otherwise |
| OQ3 | What is the authoritative Spain private-platform onboarding/registration sequence? | Determines readiness, route activation and deregistration | Spain local team + provider | G3; production | Do not infer it from account/transport creation |
| OQ4 | Which directions, formats, document types, corrections, credit notes and lifecycle actions are contracted? | Defines delivery scope and mappings | Product + local team + provider | G3/G6 | Inbound and outbound must be proven separately |
| OQ5 | Can B2B Router directory evidence determine Spain reachability, and with what freshness/authority? | Prevents incorrect route decisions | Spain local team + provider | Route design | Supporting evidence only |
| OQ6 | Will Sage create JSON invoices or import a structured document, and which schema/version is canonical? | Determines transformation ownership and data-loss risk | Product + architecture | Adapter build | Decide after representative lossless mapping tests |
| OQ7 | What idempotency/duplicate guarantees exist per mutating operation? | Determines safe retry and duplicate exposure | Provider + resilience owner | G4 | Reconcile before retry until proven |
| OQ8 | How are webhook secrets issued/rotated and events retried, ordered, retained or replayed? | Determines secure complete lifecycle ingestion | Provider + security + operations | G4 | HMAC verification confirmed; remaining lifecycle open |
| OQ9 | What incremental retrieval strategy is safe under concurrent invoice arrival? | Determines reconciliation completeness | Provider + engineering | G4/G6 | Overlapping bounded reads with dedupe unless stronger cursor exists |
| OQ10 | What contracted request, payload, attachment and concurrency limits apply? | Determines capacity, backpressure and customer limits | Provider + engineering | G5 | Public request limits are planning inputs, not contract |
| OQ11 | What data residency, retention, archive and historical-access terms apply after route deactivation? | Determines continuity, credentials and exit | Legal/security + provider + product | G5; offboarding | Preserve access until explicit policy permits removal |
| OQ12 | What SLA, incident escalation and support evidence will be available? | Determines operating model and customer communication | Operations + vendor management | G5/G7 | Open |
| OQ13 | Is B2B Router the Phase 2 reference adapter/pilot? | Determines sequencing and shared-contract validation | Product/engineering leadership | Pilot planning | Strong candidate due to public documentation, not yet decided |

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | B2B Router is included in the Phase 2 provider portfolio | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
| 2026-07-29 | Embedded official evidence, capability confidence, business rules, API interactions, operation safety, failure/continuity journeys, testable acceptance criteria and production gates for standalone Confluence use | |
