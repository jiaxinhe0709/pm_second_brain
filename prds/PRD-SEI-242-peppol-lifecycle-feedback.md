---
id: PRD-SEI-242
title: E-Invoicing — Peppol Lifecycle Feedback
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-02
updated: 2026-10-07
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-232
  - PRD-SEI-233
  - PRD-SEI-235
  - PRD-SEI-240
  - PRD-SEI-241
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: ""
  title: E-Invoicing — Peppol Lifecycle Feedback
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Peppol Lifecycle Feedback

An **exchange action** is one separately tracked action, such as delivering an invoice, submitting a public copy or reporting an invoice event. Each action has its own result. See the [shared definition](../context/GLO-SEI-001-e-invoicing-terminology.md#invoices-representations-and-rules).

## Decision summary

**Discovery proposal:** Give Sage ERP products a reliable, explainable view of invoice progress after a Peppol send, built from source-qualified network, message-level and buyer-response evidence. The Domain Service must preserve the exact Peppol/AP/provider observation first, then map it to independent delivery and buyer-processing meanings. A generic `sent` or `accepted` field cannot stand for the whole lifecycle.

This PRD owns **post-send Peppol feedback, history, notification and recovery**. [PRD-SEI-241](PRD-SEI-241-ubl-validation-service.md) separately owns pre-send UBL validation. [PRD-SEI-232](PRD-SEI-232-country-lifecycle-status-mapping.md) owns the wider country-status framework; this PRD specialises the Peppol signal sources and ERP experience. [PRD-SEI-233](PRD-SEI-233-peppol-multi-address-and-endpoint-routing.md) owns address/endpoint selection, and [PRD-SEI-240](PRD-SEI-240-peppol-access-point-service-readiness.md) owns the AP operating-model decision.

**Readiness:** consultation-ready discovery. The first country, AP/provider, process profile, supported feedback types and exact product wording are open. No Peppol process or Confluence publication is activated here.

## Outcome and problem

After sending, a seller needs to know what happened and what to do next. A developer needs durable correlated events and a current view that can be recovered after a missed callback. Operations need to distinguish a failed send, an uncertain delivery, receiving-side message rejection and a buyer business decision before retrying or advising a customer.

Peppol has multiple response layers with different producers and meanings. A transport acknowledgement can prove a protocol hop; a receiving provider may report message validation or delivery; a buyer may send an Invoice Response about its processing. If these become one status, products can claim buyer approval from network delivery, hide a rejection, or resend an invoice whose outcome is merely unknown.

| Stakeholder | Needed outcome | Failure if absent |
|---|---|---|
| Seller or accountant | Clear status and action with source/evidence age | False confidence or unresolved rejected invoice |
| ERP developer | Stable event and history contract | Fragile provider-specific webhook handling |
| AP/provider operations | Correlate original send and every response | Duplicate send or lost feedback after timeout |
| Domain Service | Govern source-to-product mappings | Same code interpreted differently across products |
| Country/process owner | Decide which feedback is expected or required | Missing optional response treated as failed, or required response ignored |

## Phase and capability boundary

| Phase | Lifecycle capability | Status |
|---|---|---|
| Discovery | Select first country/Peppol process, AP/provider, response types, correlation and customer wording | Current |
| Reference pilot | Preserve available transport and message-level observations; provide independent delivery view, durable history and unknown-outcome reconciliation | Proposed |
| Expansion | Ingest buyer Invoice Responses where selected process and counterparties support or require them; apply country reporting/status packs separately | Proposed, capability-gated |

This PRD does not specify UBL validation rules, SMP route selection, AP certification, a national mandate or statutory reporting semantics. It must be able to show a separate reporting dimension when a country pack requires one, without treating Peppol network evidence as authority reporting.

## Peppol signal vocabulary

| Signal | Producer and potential meaning | Must not be inferred |
|---|---|---|
| Domain Service send acceptance | Sage service accepted an authorised operation for processing | AP/network receipt or recipient delivery |
| Transport acknowledgement | A specified protocol hop succeeded or failed | Payload conformance, final recipient delivery or buyer decision |
| Message Level Response (MLR), if used | Content-oriented response under the applicable Peppol BIS | Buyer commercial decision or universal final-delivery proof |
| Message Level Status (MLS), if used | Receiving service provider C3 tells sending provider C2 about rejection, confirmed delivery, or forwarding without confirmation | Buyer approval or payment |
| Invoice Response, if used | Buyer-to-seller business feedback about processing of a particular invoice | Network delivery or legal settlement by itself |
| Country/authority event | Separate obligation and outcome under a country pack | Peppol buyer response or network delivery |

**Code namespaces matter.** MLS `AP` describes confirmed delivery towards C4 under the MLS specification. Invoice Response `AP` describes buyer approval in the Invoice Response process. MLS `AB` describes forwarding without confirmation of delivery. A response code is meaningful only with source, message type, profile/version, producer and invoice/action correlation.

### Peppol feedback code list

These are the published codes relevant to this invoice journey, grouped by the message that carries them. They are **external Peppol codes**, not proposed Sage status numbers. A code must be stored with its message type and applicable specification version; the same letters have different meanings in different messages.

**Invoice Response (buyer processing).** The [Peppol BIS Invoice Response code list](https://docs.peppol.eu/poacc/upgrade-3/codelist/UNCL4343-T111/) defines these seven `cbc:ResponseCode` values. The [Invoice Response process](https://docs.peppol.eu/poacc/upgrade-3/profiles/63-invoiceresponse/) defines their order and use.

| Code | Buyer-side meaning | Seller interpretation |
|---|---|---|
| `AB` | Message acknowledged | Buyer received a readable invoice and can submit it for processing; no approval yet. |
| `IP` | In process | Buyer has started processing the invoice. |
| `UQ` | Under query | Processing is paused pending information from the seller; clarification is required. |
| `CA` | Conditionally accepted | Buyer intends to proceed under stated conditions; clarification is required. |
| `RE` | Rejected | Buyer will not process this invoice further; final Invoice Response status. The commercial transaction is not necessarily cancelled. |
| `AP` | Accepted/approved | Buyer has finally approved the invoice; payment is the next step. This is not payment confirmation. |
| `PD` | Paid reported | Buyer reports that payment has been initiated; final when fully paid. `PD` with clarification reason `PPD` reports partial payment and may be followed by full `PD`. This is not independent bank settlement evidence. |

The process may start at any listed status and omit intermediate statuses. `RE` and full `PD` are final; after `AP`, only `PD` may follow through Invoice Response. A seller may need an external process to dispute or correct a buyer decision. These rules apply only when the selected process and parties actually use Invoice Response.

**Message-level feedback (document/delivery).** These codes do not express buyer approval. The [Peppol BIS Message Level Response](https://docs.peppol.eu/poacc/upgrade-3/profiles/36-mlr/) describes MLR; the [Peppol MLS specification](https://docs.peppol.eu/edelivery/specs/mls/v1.1.0/mls/spec/) describes MLS.

| Message | Code | Meaning at that layer |
|---|---|---|
| MLR | `AB` | Document acknowledged without validation. |
| MLR | `AP` | Document accepted after validation; no fatal validation errors. |
| MLR | `RE` | Document rejected after validation; inspect the description/errors. |
| MLS | `AB` | C3 forwarded the message towards C4 without confirmation of arrival. |
| MLS | `AP` | C3 has verifiable confirmation of delivery towards C4. |
| MLS | `RE` | C3 rejected the message or delivery towards C4 failed; inspect reason codes. |

**HTTP status codes in official Peppol interfaces.** The list below comes from **OpenPeppol, Peppol Service Metadata Publishing (SMP) v1.4.0, section 5.1, “The use of HTTPS”**. It applies to **SMP metadata `GET` requests** for participant and service metadata. It is the complete set that section says an SMP `GET` must return; the specification permits other HTTP codes. These codes describe lookup outcomes, not invoice progress.

| Interface | HTTP code | Official meaning | Source | Invoice-lifecycle consequence |
|---|---|---|---|---|
| SMP metadata `GET` | `200` | Requested resource was retrieved correctly. | [OpenPeppol SMP v1.4.0, §5.1](https://docs.peppol.eu/edelivery/smp/Peppol-EDN-Service-Metadata-Publishing-1.4.0-2025-02-06.pdf) | Lookup succeeded; no invoice delivery or buyer-processing claim follows. |
| SMP metadata `GET` | `404` | Requested resource was not found, for example a participant identifier absent from that SMP. | [OpenPeppol SMP v1.4.0, §5.1](https://docs.peppol.eu/edelivery/smp/Peppol-EDN-Service-Metadata-Publishing-1.4.0-2025-02-06.pdf) | Route/capability lookup needs investigation; it is not an invoice rejection. |
| SMP metadata `GET` | `500` | SMP had an internal processing error. | [OpenPeppol SMP v1.4.0, §5.1](https://docs.peppol.eu/edelivery/smp/Peppol-EDN-Service-Metadata-Publishing-1.4.0-2025-02-06.pdf) | Lookup failed technically; invoice outcome remains separate. |

Peppol uses [AS4 between sending and receiving Access Points](https://docs.peppol.eu/edelivery/as4/specification/) for document exchange. A provider may expose its own HTTP API to Sage, but that API's `200` means only what its documented endpoint contract says. For a Peppol send, retain the AS4 transport receipt or other qualified transport evidence separately from the HTTP result. There is no `200` in the Invoice Response, MLR or MLS code lists above; neither an SMP `200` nor a provider HTTP `200` proves buyer receipt, approval or payment.

## Research and evidence

Sources reviewed 2026-10-05. Official specifications describe possible signals; actual AP/provider and buyer capability still requires pilot evidence.

| Source | Confirmed finding | Limit / consequence |
|---|---|---|
| [Peppol Message Level Status v1.1.0](https://docs.peppol.eu/edelivery/specs/mls/v1.1.0/mls/spec/), sections 2 and 5 | Separates transport acknowledgements, message-level feedback and business responses. MLS runs from C3 to C2; `RE` rejects or reports failed delivery, `AP` confirms delivery towards C4, and `AB` reports forwarding without confirmation | MLS availability and configuration are AP/provider-specific. Its success never proves buyer approval. |
| [Peppol SMP v1.4.0](https://docs.peppol.eu/edelivery/smp/Peppol-EDN-Service-Metadata-Publishing-1.4.0-2025-02-06.pdf), section 5.1 | Defines HTTP `200`, `404` and `500` for SMP metadata `GET`; allows other HTTP codes | These are metadata lookup outcomes, not Peppol invoice lifecycle statuses or a provider send-API contract. |
| [Peppol BIS Invoice Response](https://docs.peppol.eu/poacc/upgrade-3/profiles/63-invoiceresponse/) | Invoice Response is buyer-to-seller feedback; multiple responses may occur for one invoice and status has process rules | It is not a transport status. Exact active release, process and buyer participation must be confirmed. |
| [Peppol BIS Billing 3.0 release notes, v3.0.21](https://docs.peppol.eu/poacc/billing/3.0/release-notes/) | May 2026 adds an optional billing-with-response process profile with separate SMP registration | Response expectation varies by selected process; do not promise a response for every Peppol invoice. |
| [PRD-SEI-232](PRD-SEI-232-country-lifecycle-status-mapping.md) | Existing Sage discovery preserves raw source status and derives separate technical, document, delivery, commercial, payment and reporting dimensions | This PRD defines the Peppol-specific inputs and product handoff, without replacing country mappings. |
| [PRD-SEI-227](PRD-SEI-227-e-invoicing-as-a-service.md) and [PRD-SEI-235](PRD-SEI-235-provider-api-for-e-invoicing-service.md) | Existing Sage direction calls for idempotency, durable history, status query and missed-event recovery | These are product requirements, not proof that a provider exposes every signal. |

**Working inference:** a single ERP-facing event envelope can carry source-qualified raw details and a safe derived customer view while maintaining both histories. Architecture and reference ERP review must validate that contract.

## Actors, scenarios and business rules

| ID | Trigger / actor | Expected outcome | Exception or continuity |
|---|---|---|---|
| S1 | ERP sends through a selected AP | Operation and original route/message IDs are bound before mutation | No `delivered` claim from local acceptance alone |
| S2 | Transport acknowledges a hop | Technical observation is stored and shown at its actual evidence level | Buyer processing remains unknown |
| S3 | MLS reports `RE` after local validation passed | Product shows receiving-side rejection/failure and reason-specific next action | Earlier local validation remains true and traceable |
| S4 | MLS reports `AP` or `AB` | Product distinguishes confirmed delivery from forwarding without confirmation | Neither is buyer approval |
| S5 | Buyer sends Invoice Response | Raw code and reason map to commercial processing with source/time | Late or conflicting responses are retained for reconciliation |
| S6 | Buyer sends no response | View reflects process expectation and evidence: not expected, awaiting, or unknown | No fabricated acceptance or arbitrary failure |
| S7 | Send times out after possible mutation | Reconcile original operation and provider/network identities | No blind resend or endpoint switch |
| S8 | Provider/endpoint or process version changes | Older invoice feedback follows original context | New configuration does not reinterpret historical evidence silently |
| S9 | Product misses a callback | Authorised query/history restores complete state | Callback is not the only source of truth |

| ID | Condition | Business rule | Basis/status |
|---|---|---|---|
| PEP-BR1 | Any post-send observation arrives | Persist raw message/code/reason, source and timestamps before mapping | Existing PRD-SEI-232; proposed Peppol handoff |
| PEP-BR2 | Code is interpreted | Qualify it by message type, source, version and actor; never map a bare `AP` or `RE` | Official Peppol specifications |
| PEP-BR3 | Transport or message-level success is observed | Do not infer buyer approval, payment or country-reporting success | Official Peppol specifications |
| PEP-BR4 | Buyer response is absent | Distinguish not expected, awaiting and unknown using the selected process/capability evidence | Proposed product rule |
| PEP-BR5 | Possible external mutation has no known result | Reconcile original send before retry, endpoint or AP/provider change | Existing PRD-SEI-227/233 |
| PEP-BR6 | Source event is late, duplicate, conflicting or unfamiliar | Keep evidence and derive cautiously; never erase a prior event solely to make a linear status | Existing PRD-SEI-232 |
| PEP-BR7 | Route/profile/provider changes | Existing invoices retain original route, process and mapping versions for follow-up | Existing continuity principle |

## Proposed Domain Service journey

This is a **conceptual product contract**, not an approved event schema or endpoint design.

1. On an authorised send, the service binds invoice identity, source product, final representation reference, Peppol participant/process/document IDs, sending AP/provider, selected receiving endpoint, message/operation correlation and route/profile versions. Local validation evidence is supplied by [PRD-SEI-241](PRD-SEI-241-ubl-validation-service.md).
2. The AP/provider binding delivers every supported transport, MLR, MLS and Invoice Response observation through authenticated webhooks, polling, files or another approved mechanism. The service records producer, source message type/version, raw code/reason, occurred/observed times and external IDs before deriving meaning.
3. The service validates authenticity and correlation. Duplicate observations are identified by source identity; unmatched or conflicting ones are retained and queued for reconciliation rather than silently discarded.
4. A versioned Peppol/process mapping updates independent technical, delivery and buyer-processing dimensions. Country reporting and payment remain separate dimensions owned by applicable packs or authoritative sources.
5. The service exposes a current view and complete authorised event history. Notifications tell products that new evidence exists; if a notification is missed, products can recover from the authoritative read.
6. The ERP shows customer-safe wording, evidence freshness and next action. Operations see raw observations, correlation, route, attempted recovery and unresolved conflicts with suitable redaction.

## Status and expectation model

| View question | Candidate answer set for discovery | Source of truth |
|---|---|---|
| Was the send attempted? | Pending, attempted, failed before mutation, outcome unknown | Durable Domain Service command/attempt evidence |
| What happened in transport? | No evidence, hop acknowledged, hop failed, unknown | AP/protocol observation |
| What happened towards recipient C4? | No evidence, rejected/failed, forwarded without confirmation, delivered with confirmation, unknown | Qualified MLS/other approved delivery evidence |
| What did buyer decide? | Not expected, awaiting, in process/query, rejected, approved, paid-reported, unknown | Qualified Invoice Response or other approved buyer source |
| What does country reporting show? | Not applicable, pending, accepted, rejected, unknown | Separate country-pack reporting action |

These are **proposed view meanings**, not a universal Peppol state machine. The service must retain actual external vocabulary, effective mapping version and evidence for each derived answer. A buyer's `PD` response indicates the buyer has reported payment initiation under its process; it is not independent bank settlement evidence.

## Conceptual event, API and history contract

| Object | Minimum information |
|---|---|
| Send context | Tenant/legal entity, invoice and revision identity, product, participant/process/document IDs, original provider/route, exact sent representation reference/hash, message/operation IDs |
| Raw observation | Source namespace, message type/profile/version, producer, raw code/reason and payload reference, occurred/observed times, authentication, original message/action correlation |
| Mapping result | Effective mapping version, independent dimension effects, confidence, customer-safe meaning, next action and unresolved/conflict flag |
| Current view | Each dimension, source/evidence age, response expectation, latest relevant event IDs and reconciliation state |
| History | Append-only observed events, superseding/resolution events, original versions and authorised audit access |

**Proposed operations:** get current invoice view, get full event history, subscribe to notifications and retrieve missed events, plus operations-only reconcile/resolution actions. Exact endpoint/event shapes, callback guarantees and retention remain architecture decisions. Event identity must be stable across notification and history reads.

## Failure, recovery and operations

| Condition | Required behaviour |
|---|---|
| AP/provider lacks a signal type | Mark capability and expectation explicitly; do not invent events |
| Provider callback is lost or delayed | Preserve authoritative history and allow replay/recovery without duplicate business effects |
| Transport ack arrives without MLS | Show the hop evidence and recipient-delivery uncertainty, according to selected process/support |
| MLS `AB` arrives | Show forwarded without confirmation, never confirmed C4 delivery |
| MLS `RE` arrives after local validation passed | Retain both facts and reason; assign customer correction or AP operations action based on cause |
| Invoice Response is absent | Use process-specific expectation and evidence age; do not treat absence alone as approval |
| Duplicate, out-of-order or conflicting response arrives | Preserve raw data, deduplicate where identity proves duplication, and reconcile conflicts |
| Timeout after possible send | Mark outcome unknown and query/reconcile original message before retry or route change |
| External success precedes internal persistence failure | Recover via durable intent/correlation and reconcile; do not create another send blindly |
| Provider/endpoint/process changes | Keep historical invoice's original route and feedback path; apply new configuration only to eligible new work |

Support must see intended send plan, observed AP/protocol events, raw versus derived meaning, evidence freshness, response expectation, safe next action and escalation owner. Sensitive invoice content and credentials must be redacted from broad operational views.

## Requirements

| ID | Functional requirement |
|---|---|
| PEP-FR1 | Before external mutation, the service must bind the invoice to an immutable Peppol send context containing original route, process/document identifiers, provider roles and correlation identities. |
| PEP-FR2 | Each supported transport, MLR, MLS or Invoice Response observation must be authenticated, correlated and preserved with raw message type/version, code, reason, producer and event times before mapping. |
| PEP-FR3 | The service must interpret external codes only within their source/message/profile namespace; identical code strings in MLS and Invoice Response must remain distinguishable. |
| PEP-FR4 | Current views must expose technical/send, delivery, buyer processing and applicable country reporting independently, with source and evidence freshness. |
| PEP-FR5 | A transport acknowledgement, MLR or MLS must never by itself set buyer approval or payment. |
| PEP-FR6 | The service must determine buyer-response expectation from the selected process, AP/provider and recipient capability evidence, or mark it unknown; it must not assume an Invoice Response for every invoice. |
| PEP-FR7 | Unknown, late, duplicate and conflicting observations must remain in authorised history; unresolved conflicts must be identifiable for reconciliation without a false success state. |
| PEP-FR8 | A possible external send with unknown outcome must reconcile the original message/attempt before retry, endpoint change or provider switch. |
| PEP-FR9 | Products must be able to retrieve current view and full authorised history and recover missed event notifications from an authoritative read. |
| PEP-FR10 | Route, provider, process and mapping changes must apply prospectively; historical invoices retain original correlation and interpretation versions. |
| PEP-FR11 | The service must provide customer-safe next actions separately from detailed operations diagnostics, including when the issue owner is customer, ERP, AP/provider or Sage operations. |
| PEP-FR12 | Events and views must retain a reference to the final validation/sent representation evidence without changing the meaning of that earlier validation result. |

| ID | Quality constraint / gate |
|---|---|
| PEP-NFR1 | Event reads, subscriptions and operational resolutions require tenant-scoped authorisation and auditable actor identity. |
| PEP-NFR2 | Raw payload references, customer data and provider credentials follow approved retention, classification, access and redaction policy. |
| PEP-NFR3 | Mapping rules and provider adapters must be versioned so historical decisions can be reproduced across rollout and rollback. |
| PEP-NFR4 | Pilot readiness requires measured event lag, callback loss/recovery, unknown-outcome age and reconciliation backlog by provider/process; targets need named owners. |
| PEP-NFR5 | Customer status wording must be localisable, accessible, source-qualified and clear about uncertainty and next action. |
| PEP-NFR6 | Monitoring must separate send, transport, MLR/MLS, buyer response and country-reporting failures. |

## Acceptance criteria

| ID | Demonstrable condition |
|---|---|
| PEP-AC1 | Given the Domain Service accepts a send but no AP evidence exists, the product shows send in progress or delivery unknown rather than delivered. |
| PEP-AC2 | Given transport acknowledgement only, the view states the acknowledged hop and leaves recipient delivery and buyer decision unset. |
| PEP-AC3 | Given MLS `AP`, the view records confirmed delivery towards C4 while buyer approval/payment remain unset; given MLS `AB`, it states forwarding without confirmation. |
| PEP-AC4 | Given local validation passed and MLS `RE` arrives, both facts remain in history and the current view shows external rejection/failure with a cause-specific next action. |
| PEP-AC5 | Given Invoice Response `AP`, the code maps to buyer approval in the Invoice Response namespace and cannot be confused with MLS `AP`. |
| PEP-AC6 | Given no buyer response is expected or received, the product never fabricates approval and distinguishes `not expected` from `awaiting` when process evidence permits. |
| PEP-AC7 | Given an unknown send outcome and new SMP endpoint, the original attempt is reconciled before retry or endpoint switch. |
| PEP-AC8 | Given a callback is missed, an authorised ERP reads full history and resumes without losing or duplicating a business observation. |
| PEP-AC9 | Given a late or conflicting status, raw events remain visible and the derived view flags reconciliation rather than regressing silently. |
| PEP-AC10 | Given provider or mapping version changes, historical status remains explainable under original route/version while eligible new sends use approved new configuration. |

## Measures, risks and rollout

| Measure | Why | Baseline/target owner |
|---|---|---|
| Status evidence completeness by signal type | Reveals what the pilot AP/provider actually supplies | AP Operations; baseline open |
| Event-to-product lag and missed-event recovery | Tests timeliness and durable handoff | Domain Service + ERP Product; baseline open |
| Unknown-outcome age and reconciliation backlog | Tests safe recovery | Operations; baseline open |
| Customer status-related support contacts | Tests clarity of wording/actions | ERP Product/Support; baseline open |

| Risk | Mitigation / gate |
|---|---|
| `accepted` hides several distinct meanings | Namespaced raw events and independent derived dimensions |
| Optional buyer response is treated as guaranteed | Verify selected process, SMP registration, AP support and buyer capability |
| Missing callback loses lifecycle | Durable history with recoverable reads and deduplicated notifications |
| New route rewrites old invoices | Freeze original route/process/provider and mapping context per send |

**Rollout gates:** name Domain Service Product Owner, Solution Designer, Engineering, Operations, reference ERP and AP/provider owner; obtain actual transport/MLR/MLS/Invoice Response contracts and correlation semantics; approve process-specific response expectation and safe customer wording; prove duplicate, late, conflict, timeout, missed-callback and historical-route scenarios in sandbox; run a limited pilot before production approval. A rollback stops new affected sends or new mappings prospectively while retaining historic feedback and recovery access.

## Open decisions and consultation

| Question | Owner | Blocks | Working hypothesis |
|---|---|---|---|
| Which country, ERP, process and AP/provider form the reference journey? | E-invoicing Product Owner + country owner | Pilot | Select on evidence and readiness, not provider name alone |
| Which transport, MLR, MLS and Invoice Response signals does the provider expose, and by what mechanism? | AP/provider owner + Engineering | Event contract | Preserve every supported raw observation; show absent capability honestly |
| Is billing-with-response profile 02 selected, or another process with optional buyer response? | Product + AP/provider + country owner | Response expectation and customer wording | Do not require response without process evidence |
| Which actors may issue or relay buyer Invoice Responses, and how are they authenticated/correlated? | AP/provider + Security + Architecture | Buyer status trust | Bind producer and original invoice/message IDs |
| What source wins when provider data and Peppol messages conflict? | Architecture + AP Operations | Reconciliation policy | Keep both raw facts and require governed resolution |
| What time-based “awaiting” wording is acceptable when feedback can be absent? | Product UX + Support + country owner | Customer experience | Show evidence age; avoid arbitrary acceptance deadlines |
| How are old invoice responses obtained after AP/provider switch? | AP Operations + Architecture | Historical continuity | Preserve original route and follow-up path |
| What retention and audit access apply to raw feedback and derived history? | Legal/Compliance + Security | Production | Country/route policy, no universal default |

## Decisions and change log

No AP/provider, Peppol process, buyer-response guarantee, API shape or customer wording is approved here. This PRD is the lifecycle-feedback decision surface, separate from UBL validation.

| Date | Change | Basis |
|---|---|---|
| 2026-10-02 | Created separate Peppol lifecycle discovery PRD from the initial combined draft, with PRD-SEI-241 retaining validation scope | User correction to create two separate PRDs; official OpenPeppol sources and existing PRD-SEI-227/232/233/235/240 |
| 2026-10-05 | Added published Peppol Invoice Response, MLR and MLS code lists; documented the official SMP HTTP `200`/`404`/`500` meanings separately from invoice lifecycle feedback | Official OpenPeppol Invoice Response, MLR, MLS, SMP and AS4 specifications |
