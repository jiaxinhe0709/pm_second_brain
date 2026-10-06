---
id: SPEC-SEI-009
title: Invoice Lifecycle Status Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-06
reviewers: []
related:
  - PRD-SEI-222
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-232
  - PRD-SEI-242
  - PRD-SEI-243
  - PRD-SEI-244
  - SPEC-SEI-003
  - SPEC-SEI-006
  - SPEC-SEI-007
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Invoice Lifecycle Status Solution Specification

## Part 1 Feature Solution Summary

### 1 Purpose, authority and scope

This **proposed logical design** turns authenticated invoice and network observations into an explainable lifecycle history and current customer view. It also coordinates any independent issuer/counterparty or public reporting obligations created by an authorised commercial or payment event. [PRD-SEI-224](../prds/PRD-SEI-224-lifecycle-rejection-payment-reporting.md) owns the Spain lifecycle outcome; [PRD-SEI-232](../prds/PRD-SEI-232-country-lifecycle-status-mapping.md) owns source-preserving country mapping; [PRD-SEI-242](../prds/PRD-SEI-242-peppol-lifecycle-feedback.md) supplies a source-specific Peppol feedback contract. [SPEC-SEI-007](SPEC-SEI-007-spain-invoice-preparation-and-outbound-solution-specification.md) hands off outbound leg evidence; [SPEC-SEI-006](SPEC-SEI-006-inbound-invoice-receiving-solution-specification.md) hands off inbound receipt evidence. This spec owns the resulting event history, interpretation, obligations, recovery and product views.

The design distinguishes raw external vocabulary from Sage canonical events, derived status and ERP workflow state. It does not approve provider APIs, Spanish technical status codes, a universal status sequence, a statutory calendar implementation, Peppol signal availability, payment authority, post-switch actor or retention period. Country pack, provider binding, endpoint and payload choices remain review gates.

### Spain use and reuse boundaries

This is a **Spain reference design**. Reuse classifications describe proposed behaviour, not proof that existing code is ready. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md) and [country lifecycle mapping](../prds/PRD-SEI-232-country-lifecycle-status-mapping.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Another country needs its own event and reporting assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Raw history and independent views | Keep original source events, versions, duplicate/conflict links and separate status dimensions. | Reusable unchanged | Reuse the event-ledger, audit and derived-view patterns. Lifecycle, Records and Product. |
| Mapping and reporting orchestration | Interpret source events and create independently tracked reporting obligations. | Reusable with country binding | Bind local event catalogues, provider namespaces, actor authority, destination, calendar and deadline rules. Country owner, lifecycle and adapters. |
| Spain lifecycle and historical follow-up | Resolve Spain Article 10/12 events, public reporting and post-switch actors/channels. | Country-specific | Codes, calendar, presumed acceptance and reporting contracts remain evidence gates. Do not reuse French codes or another country’s legal meaning for Spain. Spain Legal/Tax and technical owner. |
| Existing lifecycle implementation | Assess event capture, projection, reporting and provider feedback support. | Unknown | No complete deployed lifecycle implementation is proven here. Peppol signals are source-specific inputs, not proof of the Spain reporting contract. Architecture and lifecycle/provider owners. |

### 2 Outcome dimensions and endpoints

The underlying projection keeps **technical processing, document validation, recipient delivery, commercial decision, payment information and reporting** independently queryable. Product UX may group the first three as “exchange”, then show commercial and payment separately; reporting progress and pending actions remain visible. One event may affect zero, one or several dimensions under a versioned rule. A technical acknowledgement never sets commercial acceptance or payment. An absent response is not an explicit approval; a presumed view, where approved, is labelled derived.

| Endpoint | Observable outcome | Boundary |
|---|---|---|
| Event accepted | Authenticated source fact is durable with raw code/term, actor, route and version | Current customer status may still be unresolved |
| View derived | Independent dimensions, evidence age/source, conflicts and next actions are available | View is rebuildable, not the legal raw event record |
| Reporting pending/complete | One obligation per required event/destination, with deadline and outcome | Originating customer action is separate from delivery of its report |
| Unknown/conflicting | Raw observations persist; unsafe derivation or reporting pauses for owned reconciliation | No silent overwrite or false terminal state |
| Historical follow-up | Old invoice uses its recorded network context and approved actor/channel | Current route for new invoices is not substituted |

### 3 Process diagrams and text equivalent

**Capture, map and derive:** ![Lifecycle event capture and status derivation](../assets/diagrams/lifecycle-event-derivation-process.svg)

[Editable Draw.io](../assets/diagrams/lifecycle-event-derivation-process.drawio) · [PNG preview](../assets/diagrams/lifecycle-event-derivation-process.png). Text equivalent: LCS-01 receives a platform/ERP/buyer/payment observation → LCS-02 authenticates actor, invoice and source namespace → LCS-03 appends the exact raw fact and duplicate/conflict link → LCS-04 applies the effective country/provider catalogue → LCS-05 derives independent dimensions with explicit source and rule evidence → LCS-06 notifies product after commit. Unknown code, unmatched invoice or conflict is preserved for LCS-10 rather than mapped to a guessed success.

**Report and reconcile obligations:** ![Lifecycle reporting and reconciliation](../assets/diagrams/lifecycle-reporting-reconciliation-process.svg)

[Editable Draw.io](../assets/diagrams/lifecycle-reporting-reconciliation-process.drawio) · [PNG preview](../assets/diagrams/lifecycle-reporting-reconciliation-process.png). Text equivalent: an authorised rejection/payment fact passes LCS-02/04 → LCS-07 calculates applicable historical-route destinations and approved deadline → LCS-08 creates one durable obligation per destination → LCS-09 transmits each independently with stable identity → a possible external effect with no known result enters LCS-10, which observes the original operation before any repeat → LCS-05/06 update the view with per-destination evidence.

The existing [lifecycle and reporting overview](../assets/diagrams/e-invoicing-lifecycle-reporting.drawio) shows the cross-service relationship among technical, commercial and payment information. These two process diagrams show the detailed handoffs and exception paths.

### 4 Ordered lifecycle

| Activity | Trigger and postcondition | Owner |
|---|---|---|
| LCS-01 Receive | Raw external or authorised product fact enters durable intake with source identity | Adapter / product |
| LCS-02 Verify | Invoice, tenant/entity, actor/role, source namespace and historical route correlate | Identity / lifecycle |
| LCS-03 Preserve | Immutable raw event and provenance/duplicate/conflict relation commit | Event ledger |
| LCS-04 Interpret | Effective country pack and provider binding yield canonical effects or unknown | Country pack / lifecycle |
| LCS-05 Derive | Independent status dimensions and pending actions are rebuilt with source/rule evidence | Projection |
| LCS-06 Publish | Customer-safe view/history and change notification become available | Product API / lifecycle |
| LCS-07 Plan obligations | Applicable actor, destination, historical route, deadline and rule version resolved | Country pack / lifecycle |
| LCS-08 Create obligations | One event/destination record persists with idempotency and dependency | Lifecycle |
| LCS-09 Deliver | Each destination leg records attempt, raw result and observed state independently | Provider/public adapter |
| LCS-10 Reconcile | Unknown, late, duplicate, conflicting or missing outcomes get safe action and owner | Operations / lifecycle |

### 5 Decisions and risk controls

| Decision / impact | Owner and gate |
|---|---|
| Spain event catalogue, optional variants, technical codes, applicability and statutory deadline calendar | Spain Legal/Tax + local technical owner; country-pack approval |
| Public rejection/payment reporting and authoritative query/idempotency contract | Public-platform technical owner + Operations; external integration |
| Authority for recipient events and payment facts, including ERP/bank/operator conflict precedence | Product, Accounting, Legal, Banking Domain Service; design/pilot |
| Presumed acceptance rule and wording | Spain Legal + Product UX; design |
| Peppol process and actual MLR/MLS/Invoice Response signals by AP/provider | AP owner + Product; pilot |
| Historical Article 10/12 actor/channel after provider switch | Compliance/Tax + providers; migration/exit pilot |
| Event correction/supersession wire contract and raw/evidence retention | Local technical/Legal/Privacy; production |

Principal risks are “accepted” meaning several different things, missing callbacks hiding a status, duplicate public reports, late payment information falsely closing an invoice, and current-route data replacing the original network context. The append-only ledger, namespaced mapping, per-destination obligation ledger and source-qualified projection address these risks.

## Part 2 Logical Feature Specification

### 1 Identity, dimensions and invariants

The proposed aggregate key is (tenant, legalSubject, environment, invoiceBusinessIdentity, originalExchangeContext). The original exchange context contains route/operator/provider, direction, profile/process, source message and leg identifiers, and effective plan/binding versions. External source event identity is (producer namespace, message type/profile/version, external event ID, invoice/leg correlation, payload hash). Where no reliable external event ID exists, a governed fingerprint is used only to propose a duplicate; conflicting payloads are never discarded.

| ID | Invariant |
|---|---|
| LCS-I01 | Raw source code/term, reason, actor, source time, observed time, namespace and payload integrity reference remain immutable. |
| LCS-I02 | Mapping and current view are interpretations. They never replace raw evidence or collapse all dimensions to one linear state. |
| LCS-I03 | Country/provider codes, Peppol message codes, Sage canonical events, workflow states and internal IDs occupy separate namespaces. |
| LCS-I04 | A technical/admission/delivery observation cannot by itself prove explicit commercial approval, payment or authority reporting. |
| LCS-I05 | Presumed acceptance or overdue state is a labelled derived view with rule/time/evidence; it is not a fabricated source event. |
| LCS-I06 | One business event may create several independent reporting obligations; success or uncertainty of one cannot mutate another. |
| LCS-I07 | Duplicate observations retain provenance, while conflicting facts are held for authority/precedence review. |
| LCS-I08 | A route or mapping upgrade applies prospectively; an old invoice's follow-up uses original context unless approved country rules say otherwise. |
| LCS-I09 | Correcting an accepted fact appends an authorised superseding event and separate required reports; it never deletes the first fact. |

### 2 Detailed behaviour

**LCS-01 Receive.** Accept an external adapter observation, authorised recipient/customer action, ERP accounting fact, or qualified banking/payment observation. Capture source network/producer, message type and profile/version, raw code/term/reason, exact payload reference/hash, occurredAt and observedAt, invoice and leg references, actor role, environment and idempotency key. A bank observation is evidence for the banking service; it does not independently decide legal invoice payment status. Persist ingress intent before downstream mapping; retries with same identity/hash return the existing observation. A lost callback is recovered through authorised history/query where the source supports it.

**LCS-02 Verify and correlate.** Authenticate source or user, then check legal entity, actor authority, event type, producer role, invoice identity, original route/process/leg and applicable country-pack capability. For a customer command, authority and required data are rechecked before any external reporting. For an external observation, preserve even an unmatched or unrecognised event in restricted quarantine with source evidence; no arbitrary invoice is chosen. Cross-tenant and wrong-environment attempts are denied and audited. If a provider omits a signal type, record that capability gap; absence of a signal cannot be mapped to a positive outcome.

**LCS-03 Preserve and relate.** Append the raw event before mapping. Attach source/binding version, receipt sequence, original payload hash and relationship to duplicate-of, corrects, supersedes, disputes or derives-from as appropriate. Exact duplicate observations can share one business event while retaining delivery/provenance references. Distinct payloads with same asserted identity become a conflict case; earlier facts remain. Out-of-order events are stored with both occurrence and observation times. The ledger does not reorder or delete source truth to force a preferred current state.

**LCS-04 Interpret.** Resolve an effective-dated country lifecycle pack by country, process/document, direction, route, source namespace, producer role and event time. Apply a versioned provider binding that translates only transport shape and qualified raw source vocabulary; it cannot change country meaning. A Peppol MLS AP, Invoice Response AP and MLR AP remain distinct because message type/version and actor differ. A Spanish statutory event may have a term without a technical code; no French or Sage number is substituted. An unmapped value stays RAW_UNKNOWN and enters catalogue review. Map one raw event to zero or more independent dimension effects and obligation candidates with rule IDs/evidence.

**LCS-05 Derive projection.** Rebuild technical processing, document validation, recipient delivery, commercial, payment and reporting dimensions from accepted event effects, corrections, precedence and approved chronology. Retain latest relevant event IDs, source, evidence time/freshness, confidence, unresolved conflicts and next action for each dimension. Explicit acceptance and presumed acceptance are distinct. Full payment must follow an authorised source/effective date rule; repeated partial payments retain amount/currency and do not close the invoice merely because one event exists. A later rejection after delivery leaves delivery fact intact. Governed re-derivation after a mapping change records old/new mapping version and reason; historical source facts stay unchanged.

**LCS-06 Expose view and history.** Authorised product/API callers read current dimensions, raw/source-qualified history, supersession/conflict links and obligations with separate customer-safe and operations detail. Return view version and evidence freshness so a product can recover after missing a notification. Emit a change event only after durable ledger/projection commit; at-least-once consumers deduplicate by invoice/view version. A callback or event notification is not the authoritative history. Product wording says whether a buyer response is not expected, awaited or unknown only when selected process/capability evidence supports that distinction.

**LCS-07 Calculate obligation.** For an authorised event, country pack determines which issuer/counterparty, provider and public-solution destinations apply; it also calculates the approved deadline from event occurrence, country calendar/version and applicable rule. The invoice's original route/provider and access path are inputs. If the post-switch execution actor or technical channel is unconfirmed, create a blocked obligation with owner; do not send via the customer's current route by default. Optional event types are disabled until Product/Legal and provider capability approve them. Deadline calculation is versioned and auditable; no fixed delay is invented in this spec.

**LCS-08 Create independent obligations.** Persist one obligation per (source business event, destination, rule version, purpose) with stable identity, payload version, historical route, deadline, expected authority and state. A full rejection or full payment can therefore create issuer/counterparty and public obligations without creating a second commercial/payment event. State is proposed PENDING, READY, SUBMITTED, ACKNOWLEDGED, COMPLETED, REJECTED_CORRECTABLE, RETRY_PENDING, OUTCOME_UNKNOWN, RECONCILING, BLOCKED or SUPERSEDED. A duplicate source event cannot create duplicate obligations. Correcting an already reported event creates a new supersession event and its own obligations under the approved external contract.

**LCS-09 Deliver and observe.** Before each external mutation, persist operation ID, exact event/payload hash, destination, adapter/contract version, idempotency scope and correlation. Execute only when actor/channel/capability and required data are approved. Record raw acknowledgement/reference and normalized delivery result at its actual evidence level. One destination's success cannot complete another. A definite validation rejection gives a correction owner; safe retry follows proved idempotency/read semantics and a versioned budget. Reporting acceptance is separate from invoice business status. Monitor approaching/missed deadline risk per obligation.

**LCS-10 Reconcile.** A timeout after possible mutation marks only that obligation OUTCOME_UNKNOWN; query authoritative state using original correlation before retry. Proven success commits once; proven absence permits retry only if the provider contract makes it safe. Unresolved/unsupported query opens a manual operations case. Unknown, late, conflicting or regressive source events also open a case where authority, chronology or mapping cannot be decided automatically. Preserve all observations; append resolution/correction evidence. After route switch, reconcile through the original invoice/provider context, retaining purpose-bound access under [offboarding controls](SPEC-SEI-003-offboarding-solution-specification.md).

### 3 Requirements and quality controls

| ID | Requirement / source |
|---|---|
| LCS-R01 | Preserve raw source events with namespace, actor, time, identity, hash and versions before mapping; PRD-SEI-224 FR1–3 and PRD-SEI-232 LS-FR1/14. |
| LCS-R02 | Map only through effective country pack/provider binding; unknown codes stay raw and cannot advance status; PRD-SEI-232 LS-FR2/12/16. |
| LCS-R03 | Keep independent technical, document, delivery, commercial, payment and reporting dimensions; explicit versus derived distinct; PRD-SEI-224 FR3–4/18. |
| LCS-R04 | Validate actor/authority, event applicability and required data before reporting; PRD-SEI-224 FR1/5. |
| LCS-R05 | Calculate destinations/deadlines from approved policy and historical invoice context; PRD-SEI-224 FR6–10. |
| LCS-R06 | Persist and deliver each event/destination obligation independently and idempotently; PRD-SEI-224 FR8/11–13. |
| LCS-R07 | Preserve duplicate, late, conflicting and superseding evidence; pause unsafe projection/reporting; PRD-SEI-224 FR14–17. |
| LCS-R08 | Expose current view, full authorised history, pending actions, obligation outcomes and missed-notification recovery; PRD-SEI-224 FR18–23, PRD-SEI-242 PEP-FR9. |
| LCS-R09 | Interpret Peppol transport, MLR, MLS and Invoice Response only in their qualified namespaces; PRD-SEI-242 PEP-FR2–6. |
| LCS-R10 | Retain original route/process/mapping context after provider change; PRD-SEI-224 FR9 and PRD-SEI-242 PEP-FR10. |

Encrypt sensitive invoice, payment and authority evidence; enforce tenant/legal-entity/environment and delegated-access checks on commands, reads, subscriptions and operations actions. Logs and broad metrics use redacted references, never raw bank/payment payloads or credentials. Version mapping, calendar, provider binding and derivation rules for historical reproduction. Monitor source lag, event-to-product lag, unknown mapping, duplicate/conflict rate, obligation age/deadline risk, missed notification recovery, unknown outcome and historical-route failures. Targets require approved volumes and baselines.

## Part 3 Logical Service Interactions and Data Inventory

### Spain and reuse boundary in contracts

Keep the raw-event, independent-dimension and reporting-obligation models shared. Select interpretation and destinations through approved country packs and provider bindings. Raw source codes and Peppol message namespaces remain separate from Sage’s common events; a matching label does not establish the same business or legal meaning.

Spain Article 10/12 reporting, presumed acceptance, deadlines and historical actors/channels must not become universal defaults. Keep mapping, calendar and binding versions with each result. Reuse assessment must record the existing implementation or design pattern, local changes, missing functions, owner and qualification evidence before the dependent release gate passes. Exact physical APIs remain proposed.

### 1 Interaction contracts

These are proposed logical operations, not approved endpoints. Each command/observation carries eventId or idempotencyKey, tenant/legalSubject/environment, invoice and original route/leg references, source namespace/type/version, actor/source authority, occurredAt, observedAt, payload reference/hash and expectedVersion as applicable. Responses distinguish accepted fact, mapped effect, obligation state and current view.

| ID | Caller → owner | Contract and failure semantics |
|---|---|---|
| LCS-INT-01 | Exchange/receiving/provider/ERP → lifecycle ingress | Submit raw event or authorised fact; immutable receipt, duplicate-safe; unmatched/conflicting retained for review. |
| LCS-INT-02 | Lifecycle → identity/invoice registry | Resolve invoice, legal entity, actor/producer role, original route/process and access; unknown/denied blocks action. |
| LCS-INT-03 | Lifecycle → country pack/provider binding | Interpret namespaced source event with effective versions; returns dimension effects/obligation candidates or RAW_UNKNOWN. |
| LCS-INT-04 | Lifecycle → projection | Rebuild dimensions and source-qualified current view from ledger/version; returns view ID/version and conflicts. |
| LCS-INT-05 | ERP/product → lifecycle | Record supported rejection/acceptance/payment fact or supersession; authority/version checks; returns event and obligations. |
| LCS-INT-06 | Lifecycle → obligation planner | Calculate destination, historical actor/channel and approved deadline; unresolved gate returns BLOCKED with owner. |
| LCS-INT-07 | Lifecycle → provider/public adapter | Execute one obligation with frozen payload/idempotency identity; returns raw response or OUTCOME_UNKNOWN. |
| LCS-INT-08 | Operations → adapter/lifecycle | Reconcile original external operation or resolve conflict with source evidence/approval; no blind replay. |
| LCS-INT-09 | Product/operations → lifecycle | Read current dimensions, history and obligations with pagination/version and redacted role-specific fields. |
| LCS-INT-10 | Lifecycle → product | Publish committed view/obligation change at least once; consumer deduplicates and can recover missed events by authoritative read. |

Proposed notifications are LIFECYCLE_EVENT_RECORDED, LIFECYCLE_VIEW_CHANGED, LIFECYCLE_OBLIGATION_CHANGED and LIFECYCLE_RECONCILIATION_REQUIRED. They contain stable IDs, versions and safe status, not raw invoice/payment content. Provider callbacks may arrive out of order; the ledger is authoritative.

### 2 Data inventory

| ID | Record / owner | Essential fields and handling | Consumer |
|---|---|---|---|
| LCS-D01 | Raw lifecycle event / lifecycle ledger | External term/code/reason, namespace/message/profile, producer/actor, occurred/observed time, invoice/leg, route, payload hash/ref, binding version; immutable/restricted | LCS-01–06/10 |
| LCS-D02 | Event relationship / lifecycle | Duplicate-of, corrects/supersedes, disputes, derives-from, conflict group and resolution; append-only | LCS-03–06/10 |
| LCS-D03 | Invoice network context / exchange/receiving | Original route/operator/provider, message IDs, issue/receipt identity, direction, process/profile and versions; immutable | LCS-02/07–10 |
| LCS-D04 | Country catalogue/binding / country owner + adapter | Source namespace, raw vocabulary, actor/phase, effective period, mapping effects, obligations, deadline/calendar rules and approved version | LCS-04/05/07 |
| LCS-D05 | Mapped event effect / lifecycle | Raw event ID, mapping/binding version, dimension effects, confidence, rule IDs and unknown flag; versioned | LCS-05–08 |
| LCS-D06 | Current projection / lifecycle | Independent dimension facts, source event IDs, derivation version/time, evidence age, conflict and next action; rebuildable | LCS-05/06 |
| LCS-D07 | Reporting obligation / lifecycle | Event/destination/purpose, actor/channel, historical route, rule/deadline/version, payload hash and state; restricted | LCS-07–10 |
| LCS-D08 | Delivery attempt/observation / adapter | Operation/idempotency ID, destination, raw response, external ref, safety class and observed state; append-only | LCS-09/10 |
| LCS-D09 | Reconciliation case / operations | Conflicting/unknown refs, evidence, owner, deadline, unsafe actions, manual approval and resolution; restricted | LCS-10 |
| LCS-D10 | Product notification cursor / lifecycle/product | Invoice/view version, event ID, delivery/replay state; rebuildable | LCS-06/10 |

Payment facts and authority evidence have tighter access than generic technical status. Exact retention is an approved legal/privacy policy by country and data class; route exit cannot delete an unfinished obligation's required evidence. A projection can be rebuilt, but D01/D03/D07/D08 preserve the historic interpretation and external outcome.

## Part 4 Assurance and Traceability View

| Scenario | Requirement → activity / interaction / data | Expected evidence |
|---|---|---|
| LCS-A01 Delivery without buyer decision | R01–03 → LCS-01–06, INT-01–04/09, D01/05/06 | Delivery fact shown; explicit acceptance and payment remain unset. |
| LCS-A02 Peppol code collision | R02/09 → LCS-03/04, INT-03, D01/04/05 | MLS AP and Invoice Response AP retain distinct namespaces and effects. |
| LCS-A03 Explicit rejection | R04–06 → LCS-02–09, INT-05–07, D01/07/08 | One source rejection; independently tracked issuer and public obligations when required. |
| LCS-A04 Full payment versus bank observation | R03–06 → LCS-02/04/07, INT-01/05/06, D01/05/07 | Approved actor/effective date determine event; bank movement alone does not settle legal view. |
| LCS-A05 Presumed acceptance | R03 → LCS-05/06, INT-04/09, D05/06 | Labelled derived rule/time; no explicit acceptance event fabricated. |
| LCS-A06 Duplicate and conflicting facts | R07 → LCS-03/10, INT-01/08, D01/02/09 | Provable duplicate links; conflicting payment pauses unsafe closure/reporting. |
| LCS-A07 Late or out-of-order event | R07 → LCS-03–05/10, INT-03/04/08, D01/05/06 | Raw chronology retained; governed projection, no silent regression. |
| LCS-A08 One reporting leg times out | R06 → LCS-08–10, INT-07/08, D07–09 | Known leg stays complete; only unknown original leg reconciles. |
| LCS-A09 Provider switch | R05/10 → LCS-02/07–10, INT-02/06–08, D03/07/08 | Old invoice uses original actor/channel; current new-invoice route does not overwrite. |
| LCS-A10 Missed callback/notification | R08 → LCS-01/06, INT-09/10, D01/06/10 | Authorised history read recovers current view without duplicate business event. |
| LCS-A11 Unknown Spain/provider code | R02/07 → LCS-03/04/10, INT-03/08, D01/04/09 | Raw code preserved, projection not falsely advanced, mapping review owned. |
| LCS-A12 Superseding payment/rejection | R07 → LCS-03/07–09, INT-05–07, D01/02/07 | Original event remains; approved new event and obligations carry correction link. |
| LCS-A13 Country mapping and reporting isolation | R01–05/09/10 → LCS-03–05/07, INT-03/04/06, D01/03–07 | The shared ledger preserves source vocabulary while each country uses its own approved mapping, actor, calendar and reporting rules. France or Peppol labels do not imply Spain equivalence. A pack change does not affect another country or overwrite earlier source events. |

**Review gate:** agree country event catalogue, actor authority, mapping namespaces/precedence, deadline calendar, optional scope and response expectations. **Pilot gate:** prove source authenticity, duplicate/out-of-order/conflict, full rejection/payment, independently failing destinations, unknown mutation, missed callback and historical-route cases with actual provider/public contracts. **Production gate:** approved Spain technical rules and external APIs, named e-invoicing and banking domain owners where relevant, support/operations runbooks, measurable monitoring/deadline headroom, privacy/retention and conformance evidence. Until the open decisions in Part 1 are resolved, affected reporting or derived acceptance paths remain disabled or visibly manual.
