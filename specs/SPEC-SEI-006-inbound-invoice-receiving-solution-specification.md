---
id: SPEC-SEI-006
title: Inbound Invoice Receiving Solution Specification
type: solution-spec
status: draft
owner: TBD — E-Invoicing Inbound Solution Designer
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-06
reviewers: []
related:
  - PRD-SEI-102
  - PRD-SEI-211
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-227
  - PRD-SEI-231
  - PRD-SEI-236
  - PRD-SEI-241
  - PRD-SEI-244
  - SPEC-SEI-001
  - SPEC-SEI-005
  - SPEC-SEI-009
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Inbound Invoice Receiving Solution Specification

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices still need review; **open** decisions still need an owner’s recorded answer. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### 1 Purpose, authority and boundary

This **proposed logical design** explains how Sage could receive invoices through an approved private platform or retrieve them from the public platform. The service checks the source, recipient and original file, recognises duplicates, and makes one invoice available to the correct Sage product. [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md) owns exchange/routing requirements; [PRD-SEI-102](../prds/PRD-SEI-102-public-platform-invoice-consultation-retrieval.md) owns scheduled public discovery, checkpoints and freshness; [PRD-SEI-244](../prds/PRD-SEI-244-e-invoicing-process-flow-specification.md) supplies the inbound process boundary. [SPEC-SEI-005](SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) owns the outbound UBL validation/correction contract; this spec calls an activated inbound validation profile with separate trust and quarantine policy. [SPEC-SEI-009](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) owns lifecycle interpretation after durable receipt.

The service starts when an external invoice is available. Public consultation decides **whether and when to fetch it**. Receiving decides **what to do with the fetched invoice**.

Transport, download, technical acknowledgement, product availability, buyer acceptance and payment or rejection reporting have separate results. The exact operations, response codes, acknowledgement meaning, accepted profiles, retention and deadlines still need confirmation.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Intake, evidence and one business invoice | Preserve source observations, identify repeats, quarantine problems and deliver one invoice to the permitted product. | Reusable unchanged | Reuse receipt, audit and repeat-handling patterns. Receiving, Records and Product. |
| Recipient, trust, mapping and acknowledgement | Check the Spain recipient and route interval, approved inbound rules and source contract. | Reusable with country binding | Bind local identity, invoice-key rules, trust/profile packs and provider acknowledgement timing. Routing, Security and integration owner. |
| Spain receipt channels | Join public-platform retrieval and approved private receipt, preserving original/copy classification and source history. | Country-specific | Public checkpoints, bridge behaviour and Spain invoice identity need their own evidence. Do not assume the same topology elsewhere. Spain technical owner and consultation owner. |
| Existing receiving and transformation services | Assess adapters, receiving storage, product delivery and DTS mapping/validation functions. | Unknown | No complete reusable receiving implementation is proven here. DTS is a transformation candidate, not proof of retrieval or delivery support. Architecture and receiving/DTS owners. |

The existing DTS reuse direction comes from [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md). It identifies a preferred candidate; it does not certify a deployed build or Spain acceptance.

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
| Capability | A supported function, such as receiving invoices or signing them. |
| Route | The platform and connection used to send or receive an invoice. |
| Idempotency | A repeat of the same request has no additional effect. The contract must define how the system recognises that request. |
| Reconciliation | Check the original operation against a reliable source to establish what actually happened before deciding the next action. |
| Gate | A condition, decision or evidence check that must pass before the next step can proceed. |
| Tenant | The customer account boundary used to keep one customer’s data and access separate from another’s. |
| Immutable / append-only | A saved item cannot be changed; new information is added as a new record instead of overwriting earlier records. |
| Provenance | The record of where data came from and which versions, checks and changes produced the result. |
| Contract | The agreed inputs, outputs, behaviour and responsibilities between services or parties. |
| Durable | Saved so the record remains available after a service restart. |
| Source observation | A record of an invoice arriving or being retrieved from a particular platform. |
| Quarantine | Hold an item in restricted storage until an authorised owner resolves a trust, content or routing problem. |
| Canonical representation | The common data form used by Sage products. It is derived from the received invoice and does not replace the original. |
| Technical acknowledgement | A response defined by the platform contract. It does not by itself prove buyer approval or product availability. |
| Outbox / checkpoint | A saved record of an event waiting to be delivered; a saved position showing how far retrieval has progressed. |
| Hash / SLA | A calculated content fingerprint; and a service-level agreement. Service targets still need approval. |

### 2 Endpoints and responsibility

| Outcome | Meaning | Not implied |
|---|---|---|
| Available to product | Original and canonical references are durable; one authorised entity/product receives one business invoice event | Buyer approval or bookkeeping completion |
| Duplicate linked | Another source observation maps to an existing business invoice with its own route/reference evidence | A second product invoice |
| Quarantined | Untrusted, invalid, conflicting or unrouteable item is preserved safely with owner and reason | Trusted receipt or business delivery |
| Pending external outcome | Acknowledgement or source operation is uncertain and being reconciled | Permission to send a new acknowledgement blindly |
| No public result | A successful consultation found no new item and updated freshness | A receiving failure or proof that all historical gaps are closed |

External operator/public adapter supplies source evidence; receiving owns source classification, security gate, duplicate decision, original preservation and product publication; identity/routing owns recipient match; trust and validation services own their decisions; operations owns quarantine/recovery; the ERP owns buyer workflow after availability.

### 3 Process diagrams

**Inbound intake and delivery:** ![Inbound receiving process](../assets/diagrams/receiving-intake-and-delivery-process.svg)

[Editable Draw.io](../assets/diagrams/receiving-intake-and-delivery-process.drawio) · [PNG](../assets/diagrams/receiving-intake-and-delivery-process.png). The existing [inbound exchange overview](../assets/diagrams/e-invoicing-inbound-exchange.drawio) shows the same cross-service route at a broader level.

Text equivalent: RCV-01 accepts one public-retrieved or private-arrived item with durable source reference → RCV-02 authenticates channel and resolves the exact recipient/route interval → RCV-03 verifies file safety, trust, integrity and replay → RCV-04 classifies duplicate or conflict → RCV-05 validates activated syntax/profile and preserves exact original → RCV-06 maps approved canonical semantics → RCV-07 commits one business invoice and publishes to the authorised product → RCV-08 issues only the acknowledgement allowed by the confirmed source contract. Wrong recipient, untrusted, invalid or conflicting content is quarantined with an owner; duplicate observations are linked without a second business invoice.

**Public discovery and gap recovery:** ![Public consultation and reconciliation](../assets/diagrams/e-invoicing-public-consultation-reconciliation.svg)

[Editable Draw.io](../assets/diagrams/e-invoicing-public-consultation-reconciliation.drawio) · [PNG](../assets/diagrams/e-invoicing-public-consultation-reconciliation.png). This existing process is owned by PRD-SEI-102. The intake handoff occurs only after a retrieved item and source context are durable. A public cursor advances under that PRD's committed-page rule, not merely because RCV-01 accepted a notification.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Owner |
|---|---|---|
| RCV-01 Register observation | Source channel, external reference, original bytes/hash and receipt time are durable | Adapter/receiving |
| RCV-02 Match recipient | Authenticated operator/public context and exact tenant/legal entity/route interval established | Identity/routing |
| RCV-03 Assess safety/trust | File, transport, signature/integrity, replay and environment result evidenced | Trust/security |
| RCV-04 Resolve identity | Technical duplicate, business duplicate, new invoice or conflicting identity decided | Receiving/records |
| RCV-05 Validate original | Exact activated inbound syntax/profile/rules applied; invalid item quarantined | Validation |
| RCV-06 Map semantics | Approved transform produces distinct canonical representation with loss check | Transformation |
| RCV-07 Publish once | Original, context and canonical record commit; authorised product receives one business event | Receiving/product |
| RCV-08 Acknowledge/reconcile | Contractual technical response or uncertain outcome is recorded separately | Adapter/operations |
| RCV-09 Recover | Quarantine, missed delivery, cursor gap or unknown external effect has owner and safe action | Operations |

### 5 Decisions and risks

| Decision / impact | Owner and gate |
|---|---|
| Official public consultation/download and private provider ingress/acknowledgement contracts | Local technical owner and providers; integration |
| Recipient/route granularity, effective publication evidence and mixed public/private receipt | Routing/Compliance; design/pilot |
| Exact admitted syntax/profile and inbound validation/trust policy per route | Country/standards, Security; activation |
| Statutory/business unique identity components and handling of a changed payload under same identity | Spain technical/Legal + records; design |
| When to acknowledge: after durable raw receipt, quarantine classification, or product delivery | Provider owner, Compliance, Operations; contract |
| Data retention, original/copy classification, export and cross-product delivery ownership | Legal/Privacy/Product; production |

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Scope model and invariants

The source observation key includes (sourceNetwork, operator, environment, externalReference, retrieval/arrival identity). Business identity uses the approved country components plus seller, buyer, document type and issuer reference where required; no single raw field is assumed universally unique. Every record is partitioned by tenant, legal subject and environment. Source route and effective route interval are frozen when observed; a later onboarding/offboarding transition cannot rewrite them.

| ID | Rule that must always hold |
|---|---|
| RCV-I01 | Public retrieval and private arrival are alternative intake paths; both preserve their own source references and original bytes. |
| RCV-I02 | Channel authentication does not prove recipient match, legal invoice validity or buyer acceptance. |
| RCV-I03 | Wrong-tenant or unrouteable content is never exposed to another tenant/product; it is denied or quarantined with evidence with sensitive values removed. |
| RCV-I04 | Duplicate network observations can attach to one business invoice; conflicting bytes under the same asserted identity are not silently merged. |
| RCV-I05 | Original, derived canonical form, faithful copy and rendering are separately labelled, hashed and retained under policy. |
| RCV-I06 | Product delivery is business-idempotent: a retry or public/private duplicate cannot create another business invoice. |
| RCV-I07 | A technical acknowledgement is distinct from durable product availability and any later lifecycle status. |
| RCV-I08 | An uncertain external acknowledgement or consultation effect is reconciled before repeating an unsafe mutation. |

### 2 Detailed behaviour

**RCV-01 Register observation.** An approved adapter supplies source network/operator, environment, authenticated channel reference, external item ID, arrival/retrieval time, declared document/profile, exact payload bytes/reference/hash and available public original/copy classification. Persist a durable intake receipt and correlation before downstream processing or any irreversible acknowledgement. Same observation key/hash returns prior state; same key with changed hash is a conflict and enters RCV-09. Public consultation may provide a checkpoint/page identity, but cursor ownership remains with PRD-SEI-102.

A successful empty public query creates freshness evidence there, not an invoice here.

**RCV-02 Match recipient.** Verify source operator/channel and effective inbound capability, then resolve the addressed legal entity using scheme-qualified identifiers, tenant/product binding, route direction/scope and effective interval. Do not infer recipient from a user session, unqualified identifier or current route alone when the invoice was observed under an earlier interval. A wrong or ambiguous match is denied/quarantined without revealing another tenant. Delegate access is separate from receiving eligibility.

**RCV-03 Assess safety and trust.** Apply file/content-type/size/attachment safety, transport identity, signature or seal/integrity policy, status/time evidence and replay checks according to route/profile. [Certificate management](SPEC-SEI-001-certificate-management-solution-specification.md) owns purpose-specific trust validation. A failed or undetermined required check quarantines the item; no product event or trusted acknowledgement is issued. Retain safe evidence of the original and exact trust policy version, not private keys or raw confidential content in logs.

**RCV-04 Resolve identity.** First compare the identity of the source observation. Then compare the approved business invoice identity, content and source history. A repeated observation with the same content links to its existing result.

If the same business invoice arrives through both a private platform and the public bridge, link both source records to one business invoice. Keep each source’s original route and evidence. If the claimed identity is the same but the file or recipient differs materially, quarantine it for investigation. Never overwrite the earlier invoice.

Use a unique business key and transaction, or another approved concurrency control, so simultaneous requests cannot create conflicting identity decisions.

**RCV-05 Validate original.** Resolve exact activated inbound syntax, document type, country, route, profile and rule pack. Validate the received original, not an unlabelled canonical substitute; record parse/schema, business/profile and route outcomes separately. Inbound validation also requires trust, recipient and quarantine policy beyond outbound preflight. An unsupported or missing profile is UNSUPPORTED/UNDETERMINED, not accepted because a parser can read it. Invalid content is preserved under restricted quarantine with a safe reason and responsible source/customer/operations actor.

**RCV-06 Map semantics.** Transform only through an approved versioned mapping into facts in the agreed common data form for the product. Store source/target hashes, mapper and comparison of business meaning. Missing required meaning or unsupported extension blocks business delivery while preserving original evidence. An authorised rendering is derived and labelled as such; it cannot replace the exchanged original. If mapping fails due to service configuration, operations owns repair and replay from the original without creating a second business invoice.

**RCV-07 Publish once.** Save the original reference, validation and trust decisions, common data representation, business identity and product-delivery outbox together, either atomically or through a coordinated process that can recover from partial completion.

The ERP-facing event identifies the tenant and business, invoice ID, original source route, file references, status and correlation. It excludes secrets. The product uses stable event and invoice IDs to recognise repeats and acknowledge delivery.

If the product is unavailable, keep delivery pending with visible retry status. Do not report the invoice as absent or retrieve it externally again without a reason. The ERP separately manages review, acceptance, accounting and later rejection or payment actions.

**RCV-08 Acknowledge/reconcile.** Send a technical response only at the point allowed by the confirmed provider or public-platform contract and supported by the saved state. Record the acknowledgement kind, operation identity, content and meaning, provider reference and observed response. Keep these separate from invoice validation and buyer status.

A timeout after a possible acknowledgement produces OUTCOME_UNKNOWN. Check the original operation before another external change, unless an effective idempotency guarantee is proven. A transport acknowledgement alone cannot establish delivery to the buyer.

**RCV-09 Recover.** Quarantines retain safe original and source context, fault category, owner, deadline and allowed action. A corrected replacement from sender is a new observation linked to the old one; the original is not edited. Reprocess after rule/mapper repair from preserved bytes under explicit current or historically frozen policy as appropriate, recording which version yielded the new result. For public retrieval, incomplete pages/cursors and historical gap scans follow PRD-SEI-102; receiving returns saved classification for each item (ingested, duplicate, quarantined/conflict) for its safe progress decision.

Route switching preserves old invoice history and late-arrival handling.

### 3 Requirements and quality controls

| ID | Requirement / source |
|---|---|
| RCV-R01 | Authenticate/authorise inbound platform and exact environment/capability; PRD-SEI-223 FR17. |
| RCV-R02 | Verify recipient, trust/integrity, syntax/profile and identity before product delivery; FR18. |
| RCV-R03 | Deduplicate private, retry and public-bridge observations to one business invoice with all evidence; FR19. |
| RCV-R04 | Deliver durably to correct entity/product once at business level; FR20. |
| RCV-R05 | Preserve original and versioned transformation/validation evidence; FR7–10. |
| RCV-R06 | Quarantine invalid, untrusted, conflicting or unrouteable content with owner; FR24. |
| RCV-R07 | Classify retry/idempotent resume/reconcile-first/manual-only and expose state; FR22–26. |
| RCV-R08 | Return durable classification for each item to public consultation and preserve freshness/gap recovery; PRD-SEI-102. |
| RCV-R09 | Keep transport, validation, product availability and lifecycle/buyer status distinct; PRD-SEI-223/224. |

Protect source documents, credentials and recipient data with encryption, least privilege and tenant/environment isolation. Support access is audited and redacted. Monitor receipt-to-availability latency, quarantine age, duplicate/conflict rate, product backlog, stale public freshness, time spent with an unknown acknowledgement result and wrong-recipient attempts. Objectives require provider contracts, volume baselines and Product/Operations approval; no cadence or SLA is invented here.

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Keep the source-observation, original-file, duplicate and product-delivery contracts shared. Country/route policies determine recipient identity, business duplicate keys, accepted profiles, trust and acknowledgements. Public consultation stays a separate source adapter with its own checkpoint rules. Qualify any reused DTS mapping or validation function for the exact inbound contract; it does not own receipt or buyer workflow.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Interaction contracts

These are logical operations, not approved endpoints. Each command/event carries tenant/entity/environment, source, external reference, observationId, correlationId, payload hash, route/profile version and expected record version where applicable.

| ID | Caller → owner | Contract and safety |
|---|---|---|
| RCV-INT-01 | Private adapter/public retrieval → receiving | Register source observation and immutable payload reference; duplicate key returns prior outcome, changed hash conflicts. |
| RCV-INT-02 | Receiving → identity/routing | Resolve operator/source and recipient at observation effective time; returns scoped entity/product or ambiguous/denied. |
| RCV-INT-03 | Receiving → trust/security | Verify channel, file, integrity, signature/status and replay under effective policy; returns evidence reference or quarantine reason. |
| RCV-INT-04 | Receiving → identity index | Claim/link technical and business identity with concurrency control; returns new, duplicate or conflict. |
| RCV-INT-05 | Receiving → inbound validation | Validate exact original under activated profile/rules; returns layered outcome and issues; no silent repair. |
| RCV-INT-06 | Receiving → transformation | Produce separate canonical representation and comparison of business meaning; loss blocks delivery. |
| RCV-INT-07 | Receiving → product | Commit invoice and publish at-least-once event with stable invoice/event IDs; product deduplicates. |
| RCV-INT-08 | Receiving → adapter | Issue/query technical acknowledgement under approved contract; unknown outcome reconciles before unsafe repeat. |
| RCV-INT-09 | Receiving → public consultation | Return durable classification for each item and evidence reference; consultation alone owns checkpoint/freshness. |
| RCV-INT-10 | Operations → receiving | Inspect/reprocess quarantine or delivery backlog under authority, version and audit controls. |

Proposed events are INBOUND_ITEM_CLASSIFIED, INBOUND_INVOICE_AVAILABLE, INBOUND_QUARANTINE_OPENED and INBOUND_DELIVERY_RECOVERED. Notifications follow durable commit, are at least once, and cannot stand in for original bytes or provider evidence.

### 2 Data inventory

| ID | Record / owner | Essential fields and handling | Consumer |
|---|---|---|---|
| RCV-D01 | Source observation / receiving | Source/operator/environment, external ref, arrival time, original bytes/hash, original/copy flag, correlation; sensitive/immutable | RCV-01–09 |
| RCV-D02 | Recipient/route decision / identity/routing | Entity/tenant/product, qualified identifiers, route interval/version, source/freshness, decision reason; restricted/versioned | RCV-02/07 |
| RCV-D03 | Trust/safety result / trust | Channel, file, replay, signature/status policy/result/evidence; restricted/append-only | RCV-03/05/08 |
| RCV-D04 | Identity link / receiving | Observation IDs, business key, invoice ID, hashes, duplicate/conflict reason; concurrency protected | RCV-04/07 |
| RCV-D05 | Validation/representation / validation + transformation | Exact original/profile/rules, issues, canonical hash, mapper/comparison of business meaning, rendering labels; sensitive/append-only | RCV-05–07 |
| RCV-D06 | Business inbound invoice / records | Stable invoice ID, buyer/seller, source route, original/canonical refs, product delivery state; restricted | RCV-07/09 |
| RCV-D07 | Product outbox / receiving | Event ID, invoice ID, target product/entity, delivery attempt and acknowledged version; restricted/replayable | RCV-07 |
| RCV-D08 | External acknowledgement / adapter | Ack kind/operation, response, external reference, observed state, safety class; restricted | RCV-08/09 |
| RCV-D09 | Quarantine/recovery case / operations | Fault, original reference, owner, deadline, allowed action, evidence with sensitive values removed and audit; restricted | RCV-09 |
| RCV-D10 | Public consultation checkpoint / consultation | Cursor/window/page classification/freshness; owned by PRD-SEI-102, referenced here only | RCV-01/09 |

Retention and deletion follow approved legal/privacy/contract policy. The original received bytes and provenance must remain explainable after canonical mapping, route change or provider exit. D10 cannot advance merely because a product event was emitted; consultation applies its own committed-page and reconciliation rules.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

| Scenario | Requirement → activity / interaction / data | Expected evidence |
|---|---|---|
| RCV-A01 Direct private invoice | R01–05 → RCV-01–07, INT-01–07, D01–07 | Authenticated source, exact original/trust/profile, correct entity and one product invoice. |
| RCV-A02 Public retrieved invoice | R02–05/08 → RCV-01–07/09, INT-01/09, D01/D10 | Durable item classification; cursor/freshness remains consultation-owned. |
| RCV-A03 Wrong recipient | R02/06 → RCV-02/09, INT-02/10, D02/09 | No cross-tenant disclosure or product event; redacted owned case. |
| RCV-A04 Invalid trust or file | R02/06 → RCV-03/09, INT-03/10, D03/09 | Quarantine; no trusted ack or product delivery. |
| RCV-A05 Same invoice via two paths | R03/04 → RCV-04/07, INT-04/07, D04/06/07 | One business invoice, both source observations retained. |
| RCV-A06 Identity collision, different bytes | R03/06 → RCV-04/09, INT-04/10, D04/09 | Conflict quarantine; prior invoice not overwritten. |
| RCV-A07 Transformation loses meaning | R05/06 → RCV-06/09, INT-06/10, D05/09 | Original preserved; no product event until approved repair. |
| RCV-A08 Product outage | R04/07 → RCV-07/09, INT-07/10, D06/07 | Durable invoice/outbox; one business event after recovery. |
| RCV-A09 Ack timeout | R07/09 → RCV-08/09, INT-08, D08/09 | Unknown result reconciled; no repeated acknowledgement without checking the original outcome. |
| RCV-A10 Public gap or late item | R07/08 → RCV-09, INT-09, D01/D10 | Revisit window without duplicate invoice; freshness truthful. |
| RCV-A11 Country-bound receipt and identity | R01–03/05/06/09 → RCV-02–06/08, INT-02–06/08, D02–05/08 | Shared intake uses the selected country’s recipient, invoice-key, trust, profile and acknowledgement rules. Spain bridge observations do not define another country’s receipt model. Missing local policy quarantines or blocks the affected item without changing another country’s records. |

**Review gate:** confirm inbound operator/source contracts, recipient identity, duplicate keys, accepted profiles, trust and acknowledgement policy. **Pilot gate:** direct/private and public retrieval flows, cross-tenant denial, signature/file failures, mixed-route duplicate, conflicting hash, incomplete public page, product outage and unknown acknowledgement drills. **Production gate:** conformance evidence, retention/portability, support runbook, monitoring baselines and measured service objectives. Unsupported or unverified routes remain disabled or manually gated.
