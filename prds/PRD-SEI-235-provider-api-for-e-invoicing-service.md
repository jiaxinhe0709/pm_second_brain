---
id: PRD-SEI-235
title: Provider API for e-Invoicing Service
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-09-11
updated: 2026-09-11
reviewers: []
related:
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-213
  - PRD-SEI-214
  - PRD-SEI-215
  - PRD-SEI-216
  - PRD-SEI-217
  - PRD-SEI-218
  - PRD-SEI-219
  - PRD-SEI-220
  - PRD-SEI-223
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "899154047"
  title: Provider API for e-Invoicing service
  layout: two_left_sidebar
  toc: true
---

# Provider API for e-Invoicing Service

## Decision summary

Provide a Sage-owned, product-neutral API contract through which authorised private platforms and ecosystem partners can exchange invoices and lifecycle information with Sage e-Invoicing services. Spain is the first delivery context; the contract should remain reusable for later country and network packs.

The Provider API and a Sage-managed provider adapter are different integration boundaries:

| Pattern | Initiating integration | Appropriate when | Decision status |
|---|---|---|---|
| `PROVIDER_API` | Provider consumes Sage-owned operations and events | The provider can implement the standard Sage contract | Target strategic pattern; provider conformance and delivery scope require approval |
| `SAGE_ADAPTER` | Sage consumes a provider-owned API, mailbox, callback or file contract | The provider cannot consume the Sage contract or a contracted capability requires its interface | Existing Phase 2 discovery pattern; retain where evidenced |
| `HYBRID` | Capabilities are deliberately split across both boundaries | One boundary cannot safely own every required operation | Open exception; each operation must have one authoritative mutation and reconciliation owner |

Bidirectional business exchange is required, but it does not always mean both parties initiate network connections. A provider may push to a Sage endpoint, retrieve from Sage, receive Sage callbacks, or expose a provider endpoint that Sage polls. Direction, initiation, authentication and readiness must be explicit per capability.

## Outcome and value

The capability should allow an authorised provider to connect once, serve approved customers and capabilities, and exchange invoices without requiring each Sage ERP to implement the provider's technical model.

| Beneficiary | Outcome |
|---|---|
| Customer | Exchange invoices across provider boundaries while retaining provider choice and traceable routing |
| Provider | Integrate through a consistent contract, onboarding process, sandbox and conformance model |
| Sage ERP/product | Consume stable e-invoicing capabilities without provider-specific endpoints or credentials |
| Domain service | Add providers and country packs with bounded incremental work and observable ownership |
| Operations/compliance | Attribute each request, route, event, failure and recovery action to the correct provider, customer and rule version |

## Scope

### In scope for discovery

- Provider onboarding, authentication, credential and service-level authorisation.
- Customer/context association and authority for each requested capability.
- Provider submission of single and batch invoices to Sage.
- Provider retrieval of customer invoices from Sage.
- Status query, lifecycle history, error and audit access.
- Asynchronous lifecycle notification and missed-event reconciliation.
- Routing/discovery access where approved for the provider and country.
- Spain private-platform interconnection workflow and evidence.
- Sandbox, documentation, conformance, versioning, support and exit controls.

### Not assumed

- That every existing provider will consume the Provider API.
- That the Provider API replaces all Sage-managed adapters.
- A specific endpoint shape, OAuth grant, payload format, SLA or retry interval before architecture/provider evidence.
- That access to one service grants access to every customer, direction or operation.
- That “within 30 days” is an approved implementation clock; the applicable Spanish trigger, calendar and evidence require Compliance validation.

## Actors and responsibilities

| Actor | Responsibility |
|---|---|
| External provider | Complete onboarding/conformance, protect credentials, identify the represented customer and use only approved capabilities |
| Provider administrator/developer | Configure environments, credentials, callbacks/subscriptions and operational contacts |
| Sage Domain Service Product Owner | Accountable for Provider API outcomes, scope, priorities, roadmap and partner proposition |
| Domain-service Solution Designer | Define the reusable capability boundary, journeys, contract semantics, country extension points and failure/reconciliation behaviour for Product Owner decision |
| Sage Engineering | Build, version, secure, test and operate the API and asynchronous delivery mechanisms |
| Sage ERP/product | Supply or consume business intent through internal Sage contracts; no provider credentials or provider-specific branching |
| Spain PM/Compliance | Validate country applicability, interconnection obligations, legal authority and customer/provider responsibilities |
| Security/Privacy | Approve provider identity, credential, tenant/customer isolation, data classification and audit access |
| Operations/Support | Monitor provider health, reconcile outcomes, coordinate incidents and enforce support boundaries |

## Business scenarios

| ID | Scenario | Expected outcome | Important exception |
|---|---|---|---|
| S1 | Provider authenticates | Sage resolves provider, environment, credential and permitted services | Authentication alone grants no customer authority |
| S2 | Provider submits one invoice | Invoice is authorised, validated, durably accepted or rejected with stable correlation | Acceptance by API is not final recipient delivery |
| S3 | Provider submits a batch | Each item receives isolated authority, validation and outcome handling | One failure does not roll back unrelated accepted items |
| S4 | Provider retrieves invoices | Only invoices within approved customer, direction and service scope are returned | Empty result is distinguishable from denied or unavailable |
| S5 | Provider queries status/history | Current lifecycle and immutable source events are returned with timestamps and provenance | Derived state does not replace original evidence |
| S6 | Lifecycle changes | Provider receives a subscribed event or later reconciles it through an authoritative read | Callback delivery is not the only record of truth |
| S7 | Interconnection is requested | Request, evidence, clock, responsible parties and resolution are tracked | Exact Spanish time/calendar rule remains a compliance gate |
| S8 | Provider access changes or ends | New protected operations stop at the effective time while historical evidence and approved continuity remain | Credential revocation, customer offboarding and route deactivation are separate |

## Business rules

| ID | Condition | Rule | Status |
|---|---|---|---|
| BR1 | Provider accesses the API | Authenticate provider, environment and service scope on every operation | Confirmed product principle |
| BR2 | Provider acts for a customer | Evaluate the provider-customer-capability-direction authority independently | Confirmed product principle |
| BR3 | An invoice/status mutation is requested | Assign one authoritative mutation owner and stable idempotency/correlation identity | Confirmed safety principle |
| BR4 | Request is accepted asynchronously | Return durable receipt/state without claiming downstream completion | Proposed shared behaviour |
| BR5 | Lifecycle state changes | Correlate it to the originating invoice and retain source/provenance | Confirmed source requirement |
| BR6 | Notification is missed or ambiguous | Reconcile through an authoritative read before unsafe replay | Confirmed resilience principle |
| BR7 | Provider requests routing/discovery | Return only evidence and decisions permitted by the effective country/network policy | Proposed; country contract required |
| BR8 | Customer changes provider | Apply new routing prospectively and retain the original context of existing invoices | Confirmed continuity principle |

## Proposed integration-direction contract

This is a behavioural model for architecture/provider review, not an approved endpoint design.

| Capability | Business direction | Possible network initiator | Endpoint/system owner | Independent readiness evidence |
|---|---|---|---|---|
| Provider onboarding/configuration | Provider ↔ Sage | Provider and Sage administration | Sage Provider API/control plane | Contract, credential, environment, callback/subscription and conformance state |
| Provider submits invoice | Provider → Sage | Provider | Sage | Authentication, authority, payload/profile and idempotency tests |
| Provider retrieves invoice | Sage → Provider business delivery | Provider pulls from Sage, or Sage pushes if separately approved | Sage for pull; callback endpoint owner for push | Customer/direction scope, paging/watermark, acknowledgement and duplicate tests |
| Sage sends to provider through adapter | Sage → Provider | Sage | Provider | Provider-specific contract, credential, submission and reconciliation tests |
| Lifecycle/status notification | Sage → Provider | Sage callback/event service | Provider callback or broker boundary | Authentication/signature, ordering, replay, retry and subscription evidence |
| Lifecycle/status query | Provider → Sage | Provider | Sage | Authorised read, history completeness and freshness evidence |
| Reconciliation | Either boundary | Usually the party observing a gap | Authoritative state owner | Query/cursor, correlation, overlap, retention and safe replay proof |

No single `CONNECTED` flag is sufficient. Readiness must be represented independently for authentication, provider/customer authority, submission, retrieval, notification and reconciliation, by environment and supported direction.

## Functional requirements

### Provider identity, access and onboarding

| ID | Requirement |
|---|---|
| PA-FR1 | The service must identify provider, environment, credential, contract/version and permitted service scope on every request. |
| PA-FR2 | Provider onboarding must expose draft, validating, ready, suspended/revoked and action-required outcomes without activating customer routes implicitly. |
| PA-FR3 | Customer access must be authorised per provider, customer context, capability, direction, country/route scope and effective interval. |
| PA-FR4 | Add, change and remove access must be separately permissioned, idempotent or reconcilable, and audited. |
| PA-FR5 | Sandbox and production identities, credentials, data, callbacks and rate controls must remain isolated. |

### Invoice exchange

| ID | Requirement |
|---|---|
| PA-FR6 | Support authorised single and bounded batch invoice submission with per-item validation and outcomes. |
| PA-FR7 | Return a durable correlation/receipt when work continues asynchronously and expose later processing outcomes. |
| PA-FR8 | Prevent duplicate business effect for repeated submissions and reconcile post-transmission unknown outcomes before replay. |
| PA-FR9 | Support authorised invoice retrieval with deterministic pagination/cursor behaviour, deduplication identity and acknowledgement semantics. |
| PA-FR10 | Preserve original document, provider, customer, direction, route, schema/profile version and external references for historical explanation. |

### Lifecycle, history and events

| ID | Requirement |
|---|---|
| PA-FR11 | Expose separate technical, validation, delivery, commercial and applicable payment/reporting states without collapsing them into one status. |
| PA-FR12 | Status and history reads must include event time, observed time, actor/source, provenance, correlation and customer-safe error/action information. |
| PA-FR13 | Event delivery must be authenticated, subscription-scoped, deduplicated, replay-protected and tolerant of retry and reordering. |
| PA-FR14 | A missed-event reconciliation path must exist independently of notifications. |
| PA-FR15 | Audit access must be permissioned and must not expose another provider/customer or secrets/raw restricted evidence. |

### Routing, interconnection and operations

| ID | Requirement |
|---|---|
| PA-FR16 | Routing/discovery responses must retain applied country/network rule version, evidence source/time, selected destination and unresolved/ambiguous outcome. |
| PA-FR17 | Spain interconnection requests must record request/effective timestamps, parties, scope, evidence, state, deadline rule and escalation without inventing the final statutory clock. |
| PA-FR18 | The service must expose provider health, limits, pending/outcome-unknown age and reconciliation freshness to authorised operations. |
| PA-FR19 | Versioning and deprecation must provide an approved compatibility/migration window before removing provider capability. |
| PA-FR20 | Route deactivation, provider/customer access removal, credential revocation, subscription termination and historical retention must remain separate actions. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| PA-NFR1 | Encrypt data in transit and at rest and apply least privilege, tenant/provider/customer/environment isolation and approved secret custody. |
| PA-NFR2 | Availability, latency, throughput, batch, payload, concurrency and deadline-headroom targets require measured baselines and accountable owners before commitment. |
| PA-NFR3 | Every request, event, external mutation, decision and recovery action must be correlation-addressable and auditable. |
| PA-NFR4 | Monitoring must distinguish provider, customer/authority, Sage API, internal processing, route/network and destination fault domains. |
| PA-NFR5 | Capacity and backpressure must prevent one provider or customer backlog from starving others. |

## Failure and recovery

| Failure | Required behaviour |
|---|---|
| Invalid/revoked provider credential | Deny, audit and expose an authorised recovery path without leaking credential detail |
| Provider lacks customer/capability authority | Deny only that scoped operation; do not widen or revoke unrelated access implicitly |
| Invalid invoice | Return stable, actionable validation/profile evidence; do not retry unchanged content |
| Duplicate submission | Return or reconcile the original logical result; create no second business effect |
| Timeout after possible mutation | Mark only that operation outcome unknown and reconcile before replay |
| Callback unavailable | Retain durable event, retry within approved policy and allow provider reconciliation read |
| Duplicate/out-of-order event | Deduplicate by event identity/provenance and prevent lifecycle regression |
| Several routes appear eligible | Do not choose arbitrarily; return unresolved/reconciliation outcome with evidence |
| Provider suspended/offboarded | Stop new protected operations while preserving approved historical access/evidence |

## Acceptance criteria

- Given an authenticated provider without authority for customer A, when it submits or retrieves for A, then access is denied and audited without exposing A's data.
- Given an authorised single or batch submission, when the API accepts asynchronous work, then it returns stable correlation and per-item state without claiming final delivery.
- Given the same logical invoice is submitted twice, when duplicate protection runs, then no second invoice effect is created.
- Given a provider callback is unavailable, when lifecycle changes, then events remain durable and the provider can recover them through the approved reconciliation read.
- Given outbound submission is ready but inbound retrieval is not, when readiness is queried, then only outbound is eligible; the connection is not shown as universally connected.
- Given an existing provider requires Sage to call its API, when the integration-mode decision is recorded, then the provider adapter may remain for named capabilities without duplicating Provider API mutation ownership.
- Given a customer changes provider, when an older invoice receives a lifecycle event, then its original provider/route context and required destinations remain unchanged.

## Measures and rollout gates

| Gate | Evidence required | Blocks |
|---|---|---|
| G1 — Product ownership | Named Domain Service Product Owner, Solution Designer, Engineering and Operations owners; initial partner/cohort | Scope approval |
| G2 — Contract | Versioned API/schema/event/error documentation and provider integration-mode decision | Engineering commitment |
| G3 — Security and authority | Provider onboarding, credentials, customer authority, isolation and audit threat tests | Sandbox exit |
| G4 — Bidirectional capability | Submission, retrieval, status/history, events and reconciliation proved independently | Pilot |
| G5 — Spain interconnection | Compliance-approved process/clock/evidence plus routing and provider responsibility | Spain production |
| G6 — Service | Capacity, service levels, support, monitoring, incident and BCP/DR evidence | Production |
| G7 — Exit/change | Revocation, deprecation, offboarding, historical access and migration tests | Production expansion |

Metrics should include provider onboarding lead time, conformance pass rate, unique implementation effort, exchange success by independent leg, duplicate prevention, event/reconciliation age and customer interoperability. Baselines and targets remain open.

## Relationship to provider-specific PRDs

PRD-SEI-216–220 retain the evidence and limitations of B2B Router, Banqup, EDICOM, SERES and ZeroComa. They do not automatically become five bespoke adapters. For each provider and capability, architecture and the provider must record whether the provider consumes this API, Sage retains an adapter, or an approved hybrid assigns one authoritative owner to each operation.

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Which provider and capability is the first Provider API reference integration? | Validates the reusable contract | Domain Service Product Owner + providers | G1/G2 | Select using readiness evidence, not provider name alone |
| Which operations are provider-push, provider-pull, Sage-push or Sage-pull? | Defines endpoints, security and reliability | Solution Designer + architecture + provider | G2/G4 | Decide per capability; business direction does not determine network initiator |
| What customer-authority evidence may each provider use? | Prevents cross-customer access | Product + Compliance + Security | G3 | Capability/direction/time-scoped grant |
| What is the approved Spain interconnection clock and evidence? | Prevents missed statutory commitment | Spain Compliance/PM + Operations | G5 | Preserve the source statement as research; do not hard-code 30 days yet |
| What API lifecycle and compatibility promise can Sage support? | Determines partner adoption and upgrade risk | Product + Engineering + Operations | G2/G6 | Versioned compatibility window required |
| Which current provider adapters remain necessary? | Avoids duplicate platforms and wasted delivery | Architecture + Product + provider owners | Roadmap/estimate | Prefer standard API where fit; retain adapters only for evidenced gaps |

## Decisions

| Decision | Status |
|---|---|
| Sage Provider API is a provider-facing contract and not another name for a Sage-to-provider adapter | Confirmed clarification from user review |
| Bidirectional exchange and readiness must be explicit per capability | Confirmed product principle |
| Provider API, provider adapter or hybrid selection | Open per provider/capability |
| Spain first with reusable country/network extension points | Proposed strategic direction from source brief |

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-09-11 | Created canonical Git discovery source for existing Confluence page `899154047`; retained the source brief's provider-authentication, submission, retrieval, status, events, history, audit and interconnection intent; separated Provider API from provider adapters and added bidirectional readiness, authority, resilience and delivery gates | Confluence page v7 supplied by user; user discussion of mutual connectivity |
