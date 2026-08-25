---
id: PRD-SEI-224
title: Lifecycle — Status, Rejection and Payment Reporting
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-24
reviewers: []
related:
  - PRD-SEI-210
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-223
  - PRD-SEI-102
  - PRD-SEI-103
  - PRD-SEI-201
  - PRD-SEI-203
  - PRD-SEI-231
  - PRD-SEI-232
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "876576916"
  page_id: "866148657"
  title: Lifecycle — Status, Rejection and Payment Reporting
  layout: two_left_sidebar
  toc: true
---

# Lifecycle — Status, Rejection and Payment Reporting

## Decision summary

Phase 3 must provide one coherent invoice lifecycle view while retaining the source, authority and delivery obligation of every technical, commercial and payment event. Transport success, commercial acceptance/rejection and payment are separate dimensions; they must not be collapsed into one linear status.

For invoices exchanged privately, the recipient must be able to communicate required commercial and payment information to the issuer and, where applicable, the public solution. Duplicate, late, corrected and conflicting events must remain traceable and recoverable. A customer route change does not transfer historical events to the new route automatically.

> **Product principle:** Preserve facts as events, derive views explicitly, and deliver each event to every required destination exactly once at the business level.

## Phase and outcome

| Phase | Lifecycle behaviour | Phase 3 requirement |
|---|---|---|
| Phase 1 | Public submission/retrieval status | Reuse public status and consultation patterns where evidence proves fitness |
| Phase 2 | Provider status mapping and historical continuity | Reuse source-aware mapping, reconciliation and invoice-origin context |
| **Phase 3** | Sage operates private exchange and status fan-out | Add recipient actions, private interconnection and public rejection/payment reporting |

## Problem and objective

### Problem

An invoice can be technically received but commercially rejected; explicitly accepted but unpaid; partially paid several times; fully paid and later disputed; or reported differently by a private platform and the public solution. Events may arrive out of order or after a customer changes platform.

Without a source-aware lifecycle model:

- transport acknowledgements may be shown as commercial acceptance;
- absence of rejection may be presented as explicit customer approval;
- partial payment may incorrectly close an invoice;
- duplicate events may trigger duplicate public or counterparty reporting;
- a route change may send an old invoice's status to the wrong platform;
- public and private observations may overwrite each other without explanation;
- customers and operations may not know who must correct a rejected or overdue event.

### Objective

Capture immutable source events, validate customer authority, calculate required destinations/deadlines, deliver and reconcile each reporting obligation, and derive an understandable current view without erasing contradictions or historical context.

## Scope and non-goals

### In scope

- Technical exchange, commercial acceptance/rejection and payment-event dimensions.
- Required and optional status types defined for the Spanish system.
- Recipient/customer action, ERP-originated payment evidence and authorised operator reporting.
- Private platform/counterparty and public-solution fan-out.
- Idempotency, ordering, conflict, correction, reconciliation and route-transition continuity.
- Product/API and operations experience, audit and measurement.

### Non-goals

- Payment initiation, bank reconciliation or collections product design.
- Legal determination of commercial disputes.
- Automatically creating a rectifying invoice from a rejection.
- Inventing public-service payloads before the ministerial-order specification.
- Treating optional partial/assignment events as launch scope without product approval.
- Replacing the ERP's accounting ledger as the payment system of record.

## Definitions and distinctions

| Concept | Meaning | Not equivalent to |
|---|---|---|
| Technical state | Validation, transmission, receipt or delivery observation | Commercial acceptance |
| Commercial state | Explicit acceptance/rejection, partial result or applicable derived/presumed view | Payment state |
| Payment state | Unpaid, partially paid, fully paid or a reported discrepancy | Settlement instruction or bank movement by itself |
| Source event | Immutable statement received from an authorised actor/system | The current derived lifecycle view |
| Reporting obligation | Required delivery of an event/fact to a counterparty/platform/public solution | The originating customer action itself |
| Explicit acceptance | Recipient actively reports acceptance | Absence of rejection |
| Presumed acceptance | Regulatory/business derived view when conditions are met | Evidence of an explicit approval event |
| Correction/supersession | New event that corrects or supersedes a prior reported fact | Deletion or mutation of the original event |
| Document relationship | Immutable link between an original invoice and a later country-approved corrective/replacement business document | An event-only status change or mutation of the original invoice |
| Historical lifecycle route | Network/provider context used to continue an existing invoice's events | Customer's current route for new invoices |

## Lifecycle visual

<!-- confluence-html-macro:start -->
<div class="p3life-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3life-visual *{box-sizing:border-box}.p3life-visual h2{margin:0;color:#172b4d;font-size:18px}.p3life-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3life-visual svg{display:block;width:1080px;height:500px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3life-visual .tech{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3life-visual .commercial{fill:#eae6ff;stroke:#6554c0;stroke-width:1.5}.p3life-visual .payment{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3life-visual .event{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3life-visual .conflict{fill:#ffebe6;stroke:#ff5630;stroke-width:1.5}.p3life-visual .title{fill:#172b4d;font-size:11px;font-weight:700}.p3life-visual .copy{fill:#42526e;font-size:9px}.p3life-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3life-visual .path{fill:none;stroke:#7a869a;stroke-width:1.8}.p3life-visual .fan{fill:none;stroke:#00875a;stroke-width:1.8}.p3life-visual .retry{fill:none;stroke:#de350b;stroke-width:1.5;stroke-dasharray:6 4}.p3life-visual .arrow{fill:#7a869a}.p3life-visual .arrow-g{fill:#00875a}.p3life-visual .arrow-r{fill:#de350b}.p3life-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3life-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3life-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Three lifecycle dimensions, one immutable event history</h2>
  <p class="sub">Source facts are retained. Sage derives the customer view and fans each authorised event out to its required historical-network destinations.</p>
  <svg viewBox="0 0 1080 500" role="img" aria-label="Technical exchange, commercial acceptance or rejection, and payment are three independent lifecycle dimensions. Authorised source events enter an immutable event ledger, which validates identity, authority, ordering and deadlines, derives a current customer view, and sends required reports to the issuer or counterparty platform and the public solution. Conflicting or ambiguous outcomes go to reconciliation without deleting source events.">
    <text x="34" y="34" class="label">SOURCE DIMENSIONS</text><text x="350" y="34" class="label">EVENT TRUTH AND DERIVATION</text><text x="805" y="34" class="label">REQUIRED DESTINATIONS</text>
    <rect x="34" y="68" width="236" height="72" rx="9" class="tech"/><text x="52" y="95" class="title">Technical exchange</text><text x="52" y="116" class="copy">Validated • submitted • delivered • failed</text>
    <rect x="34" y="174" width="236" height="82" rx="9" class="commercial"/><text x="52" y="201" class="title">Commercial decision</text><text x="52" y="222" class="copy">Accepted • rejected • partial • presumed view</text><text x="52" y="239" class="copy">explicit and derived remain distinguishable</text>
    <rect x="34" y="290" width="236" height="82" rx="9" class="payment"/><text x="52" y="317" class="title">Payment information</text><text x="52" y="338" class="copy">Unpaid • partial • full • assigned</text><text x="52" y="355" class="copy">effective date and amount retained</text>
    <path d="M270 104 H332 V204" class="path"/><path d="M270 215 H332" class="path"/><path d="M270 331 H332 V226" class="path"/><polygon points="332,215 322,209 322,221" class="arrow"/>
    <rect x="334" y="148" width="238" height="134" rx="9" class="event"/><text x="352" y="177" class="title">Immutable lifecycle event ledger</text><text x="352" y="199" class="copy">Invoice identity • source • actor • authority</text><text x="352" y="217" class="copy">event type • occurred/received time • payload hash</text><text x="352" y="235" class="copy">supersession • route context • rule version</text><text x="352" y="257" class="copy">dedupe • order • obligation calculation</text>
    <path d="M572 215 H618" class="path"/><polygon points="618,215 608,209 608,221" class="arrow"/>
    <rect x="620" y="148" width="154" height="134" rx="9" class="event"/><text x="638" y="177" class="title">Derived customer view</text><text x="638" y="199" class="copy">Technical</text><text x="638" y="217" class="copy">Commercial</text><text x="638" y="235" class="copy">Payment</text><text x="638" y="257" class="copy">pending actions/deadlines</text>
    <path d="M774 194 H806 V104" class="fan"/><polygon points="806,104 800,114 812,114" class="arrow-g"/>
    <path d="M774 236 H806 V329" class="fan"/><polygon points="806,329 800,319 812,319" class="arrow-g"/>
    <rect x="808" y="68" width="238" height="72" rx="9" class="commercial"/><text x="826" y="95" class="title">Issuer / counterparty platform</text><text x="826" y="116" class="copy">Required commercial and payment events</text>
    <rect x="808" y="290" width="238" height="82" rx="9" class="tech"/><text x="826" y="317" class="title">Public solution</text><text x="826" y="338" class="copy">Required rejection/payment reporting</text><text x="826" y="355" class="copy">independent delivery evidence</text>
    <rect x="334" y="392" width="440" height="72" rx="9" class="conflict"/><text x="352" y="419" class="title">Conflict, late event or outcome unknown</text><text x="352" y="440" class="copy">Preserve all observations • stop unsafe retry • reconcile authority and delivery • escalate when unresolved</text>
    <path d="M453 282 V384" class="retry"/><polygon points="453,384 447,374 459,374" class="arrow-r"/><path d="M697 282 V384" class="retry"/><polygon points="697,384 691,374 703,374" class="arrow-r"/>
  </svg>
  <div class="notes"><div class="note"><strong>No single linear status</strong>Delivered, rejected and partially paid can coexist as facts across dimensions.</div><div class="note"><strong>Explicit versus derived</strong>A presumed view never masquerades as an explicit customer event.</div><div class="note"><strong>Historical routing</strong>Events follow the invoice's original network obligations after customer route changes.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors and responsibilities

| Actor | Responsibility |
|---|---|
| Invoice recipient/authorised user | Record commercial decision and payment facts accurately and on time |
| Invoice issuer | Receive relevant events and understand explicit/derived status |
| Sage ERP/accounting product | Supply authoritative accounting/payment facts where authorised and display actions/outcomes |
| Sage lifecycle service | Validate, deduplicate, order, derive, fan out, reconcile and audit events |
| Private-platform operator | Exchange required events with counterparties and the public solution |
| Counterparty platform | Authenticate, acknowledge and forward events to its customer |
| Public solution | Receive/query applicable rejection/payment information using the official contract |
| Operations/support | Resolve delayed, conflicting and ambiguous delivery obligations |
| Legal/compliance | Approve event applicability, timing, authority and retention interpretation |

## Business scenarios

| ID | Scenario | Expected outcome | Exception/continuity |
|---|---|---|---|
| S1 | Recipient explicitly accepts invoice | Issuer sees explicit acceptance with source/time | Payment remains independent/unpaid |
| S2 | Recipient rejects invoice | Rejection reaches issuer and public solution where required | Commercial dispute does not erase invoice or automatically create rectification |
| S3 | No rejection is reported | System may show a clearly labelled presumed/derived acceptance where applicable | Must not fabricate an explicit acceptance event |
| S4 | Recipient pays in full | Effective payment and due date are reported to required destinations | Transport acknowledgement is not payment confirmation |
| S5 | Recipient makes partial payments | Each authorised event is retained; derived balance reflects approved accounting facts | Optional scope and public behaviour require confirmation |
| S6 | Same event arrives from ERP and platform | Dedupe by business event identity/provenance | Preserve both observations if not provably identical |
| S7 | Payment event arrives before delivery acknowledgement | Store source event; derive cautiously and reconcile order | Do not discard valid late/out-of-order facts |
| S8 | Customer switches provider | Older invoice events follow original invoice network obligations | Current route is used only where policy explicitly says so |
| S9 | Public reporting times out after counterparty success | Counterparty success remains; public leg reconciles independently | No duplicate counterparty event |
| S10 | Delivered invoice requires rectification/replacement | Create a new business document and explicit relationship to the original; retain both documents and their lifecycle evidence | Rejection alone does not create the corrective document |
| S11 | Qualifying small natural-person/income-attribution recipient remains inside the additional status transition | Exchange remains governed by its applicable rule while Articles 10/12 status supply is labelled voluntary/not-yet-required | Do not infer that invoice delivery is also deferred |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Technical delivery succeeds | Do not infer commercial acceptance or payment | Product principle |
| BR2 | Recipient makes explicit acceptance/rejection | Preserve decision, effective date, actor/authority and source | RD 238/2026 Article 10 |
| BR3 | Recipient completes payment | Preserve effective payment date and report to required destinations | RD 238/2026 Articles 10 and 12 |
| BR4 | Required Article 10 event occurs | Communicate within the applicable four-day rule excluding Saturdays, Sundays and national holidays | Primary regulation; deadline calculation approval required |
| BR5 | No rejection or later rectifying invoice exists | Any presumed acceptance is a labelled derived view, not an explicit event | RD 238/2026 Article 12 plus product safeguard |
| BR6 | Partial acceptance/payment or assignment is supported | Treat as separate optional event types and never as full acceptance/payment | RD 238/2026 Article 10; launch scope open |
| BR7 | Public solution is used for exchange/interconnection | Apply Article 12 public status rules and avoid duplicate faithful-copy behaviour | RD 238/2026 Articles 11–12 |
| BR8 | Same business event has multiple deliveries | Maintain one source event with independent delivery obligations/outcomes | Proposed model |
| BR9 | Corrected fact is received | Append a superseding event; do not mutate/delete the original | Proposed audit rule |
| BR10 | Customer route changes | Continue the invoice's historical lifecycle through its original network context | Confirmed continuity principle |
| BR11 | Four-day Article 10 deadline is evaluated | Start the clock from the actual status event being communicated; timer expiry does not create explicit acceptance | RD 238/2026 Article 10 and Article 12 distinction |
| BR12 | Qualifying natural person or income-attribution entity at or below EUR 8 million remains within the additional transition | Treat Article 10/12 status supply as voluntary/not-yet-required while preserving any voluntarily supplied facts and evidence | RD 238/2026 transitional provision three |
| BR13 | Invoice requires rectification, replacement or another country-approved corrective document | Create a new document with an immutable relationship to the original; do not overwrite or delete the original | Invoicing traceability principle; exact Spain document rules require approval |
| BR14 | Recipient rejects an invoice | Preserve and report rejection as required; do not automatically create a corrective invoice or treat rejection as deletion/cancellation | RD 238/2026 Article 11.6 plus product safeguard |

## Research and evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| RD 238/2026 Article 10 | Required commercial acceptance/rejection and full-payment information; optional partial/assignment events; four-day communication rule | Primary regulation; exact message contract open | Event catalogue, deadline and interconnection |
| RD 238/2026 Articles 11–12 | Public status uses Article 12; full payment/rejection reporting, authorised platform reporting and public consultation | Primary regulation; service specification depends on ministerial order | Public obligation/fan-out and authority |
| RD 238/2026 Article 11.6 | Commercial disagreement remains between parties and may require rectifying invoice separately | Primary regulation; legal process outside product scope | Rejection is not invoice deletion |
| RD 238/2026 transitional provision three | Qualifying natural persons and income-attribution entities at or below EUR 8 million receive a further transition before Articles 10/12 status supply becomes mandatory | Primary regulation; cohort evidence and effective-date materialisation require approval | Status applicability and customer messaging |
| Spain e-Invoicing Solution Design Brief, 21 August 2026 | Corrections, annulments and replacements should remain linked business documents rather than overwritten invoice state | Medium internal design/research handover; not legal authority | Proposed `DocumentRelationship`, journeys and ERP/platform boundary |
| PRD-SEI-102/103 | Public retrieval/submission status and evidence patterns | Implementation fitness unassessed | Reuse input through FP-SEI-001 |
| PRD-SEI-201/203 | Historical route context, idempotency, unknown outcome and reconciliation | Product intent | Continuity and recovery |

## Proposed conceptual model

| Record | Required information |
|---|---|
| Lifecycle event | Invoice ID, event type, dimension, source/actor/authority, occurred/received time, data, source reference/hash and rule version |
| Event relationship | Duplicate-of, corrects/supersedes, disputes or derives-from links |
| Document relationship | Original/related document identities, country-approved relationship type, correction method, affected scope/value, reason, effective date, actor/authority, source evidence and policy version |
| Delivery obligation | Destination, reason/rule, historical route, deadline, payload version and state |
| Delivery attempt | Idempotency/correlation, transmitted time, acknowledgement/reference, error and observed state |
| Derived lifecycle view | Technical/commercial/payment facts, derivation rule/time, pending actions and conflicts |
| Reconciliation case | Conflicting observations, authority decision, safe action, owner and resolution evidence |

### Proposed document-relationship model

The field names and candidate values are proposed for architecture review. The behavioural distinction—new corrective business document plus retained original—is required wherever the applicable Spain rule requires a new document.

| Field | Required meaning |
|---|---|
| `sourceDocumentId` | Original invoice or credit/corrective document being referenced |
| `relatedDocumentId` | New business document carrying the correction or replacement |
| `relationshipType` | Country-pack-approved relationship, for example `rectifies` or `replaces`; never inferred from a generic status alone |
| `correctionMethod` | Difference/replacement or another approved method and version |
| `affectedScope` | Whole document, specified lines, tax categories or monetary components |
| `previousValue`, `newValue`, `deltaValue` | Values required to explain the approved correction method; optional only when the rule does not require them |
| `reasonCode`, `reason` | Approved structured reason plus safe customer explanation |
| `effectiveDate` | Business-effective date of the relationship/action |
| `actor`, `authorityDecision` | Who created/approved the relationship and why they were authorised for this operation |
| `policyVersion`, `sourceEvidence` | Country rule, ERP intent and external references used to create/prove the relationship |

An event relationship answers how observations relate. A document relationship answers how separately issued business documents relate. Both can exist for the same correction and must remain traceable without becoming the same record.

### Event types and dimensions

| Dimension | Candidate event types | Scope status |
|---|---|---|
| Technical | validated, submitted, network-acknowledged, delivered, technical-rejected | Required for product operation; external mapping varies |
| Commercial | explicit-accepted, explicit-rejected, partial-accepted, partial-rejected | Full acceptance/rejection required; partial is optional scope |
| Payment | full-paid, partial-paid, assigned-for-collection/payment, issuer-reported-collected/unpaid/discrepancy | Full payment/rejection public reporting required; others need scope confirmation |
| Derived | presumed-accepted, payment-overdue, action-required | Product views only; derivation evidence required |

### Delivery-obligation states

`PENDING → READY → SUBMITTED → ACKNOWLEDGED → COMPLETED`

Branches: `REJECTED_CORRECTABLE`, `RETRY_PENDING`, `OUTCOME_UNKNOWN`, `RECONCILING`, `FAILED_TERMINAL`, `SUPERSEDED`.

## Detailed journeys

### J1 — Recipient explicitly rejects

1. Authorised recipient selects full rejection and supplies required effective date/reason fields.
2. Sage validates invoice identity, authority, event applicability and source data.
3. The immutable rejection event is stored before external reporting.
4. Obligations are created for the issuer/counterparty route and public solution where required.
5. Each destination is delivered/reconciled independently; customer sees pending/complete outcomes.

### J2 — Report full payment

1. ERP/user supplies full-payment event, effective payment date and applicable due-date information.
2. Sage checks authority, invoice identity, duplicate/supersession and timing fields.
3. Event and statutory deadline are stored under the approved calendar rules.
4. Required counterparty/public reports are submitted with stable idempotency identities.
5. Acknowledgements are correlated; derived view becomes fully paid without overwriting commercial state.

### J3 — Correct invalid information

1. Validation rejects an event before mutation with actionable field/rule information.
2. User/product corrects the source fact.
3. If no valid event was externally accepted, the same logical operation safely resumes.
4. If a prior event was accepted, an approved correcting/superseding event is appended and separately delivered.
5. Both facts and the current derived view remain explainable.

### J4 — Resolve timeout after one destination succeeds

1. Issuer/counterparty delivery succeeds; public reporting times out after transmission.
2. Only the public obligation becomes `OUTCOME_UNKNOWN`.
3. Sage queries/consults public state when supported or uses the approved reconciliation process.
4. The public leg resumes only if absence and retry safety are established.
5. Counterparty delivery is not repeated.

### J5 — Reconcile duplicate or conflicting events

1. Sage receives events sharing invoice/type/date but with different sources or values.
2. Provable duplicates are linked and ignored for new reporting.
3. Non-identical observations are retained and evaluated against approved authority/precedence rules.
4. Unsafe derivation/reporting pauses and an operational case is opened.
5. Resolution appends a decision/correction; source facts are never deleted.

### J6 — Historical invoice after route change

1. Customer moves from Provider A to Sage or from Sage to another route.
2. A payment/rejection event occurs for an invoice originally exchanged through Provider A.
3. Sage resolves the invoice's historical route and required destinations from immutable context.
4. Event follows the approved historical lifecycle path, not the current route by default.
5. Credentials/access are retained only as required for that continuity obligation.

### J7 — Rectify a delivered invoice without rewriting history

1. ERP/accounting product determines that a new corrective or replacement document is required and supplies the original document identity, proposed relationship, affected values, reason and effective date.
2. Sage resolves the applicable country rule and verifies the actor's client- and operation-specific authority.
3. The new document receives its own immutable identity and lifecycle; the original document remains unchanged and queryable.
4. Sage records the `DocumentRelationship`, validates the approved correction method and establishes the new document's delivery/reporting plan.
5. External delivery and reporting outcomes are correlated to both documents without converting the original delivery, rejection or payment facts into deletion.
6. If the relationship or external outcome is ambiguous, only the unsafe new mutation pauses and reconciles; prior evidence remains intact.

**Expected result:** products, customers and operations can explain what changed, why, who authorised it and which external outcomes belong to each document.

### J8 — Apply the additional status-reporting transition

1. Applicability supplies the recipient's legal form/tax regime, prior-year turnover, effective group and approved policy version.
2. Sage determines that invoice exchange is effective but mandatory Articles 10/12 status supply remains inside the additional transition.
3. Customer experience labels status supply as voluntary/not-yet-required and does not create a missed statutory deadline.
4. Voluntarily supplied events retain their actual source, authority and delivery evidence and are never presented as mandatory compliance proof by implication.
5. When the effective interval expires, only new status obligations use the new policy; historical decisions remain reproducible.

## Functional requirements

### Event capture and authority

| ID | Requirement |
|---|---|
| FR1 | Accept lifecycle events only for a resolvable invoice identity and authorised legal entity/actor. |
| FR2 | Store source events immutably with occurred/received time, source, authority, reference/hash and rule version. |
| FR3 | Distinguish technical, commercial, payment and derived dimensions. |
| FR4 | Represent explicit, presumed/derived, corrected, disputed and superseded facts distinctly. |
| FR5 | Validate event applicability and required data before external mutation. |

### Obligation and deadline management

| ID | Requirement |
|---|---|
| FR6 | Calculate required destinations from event type, exchange route, customer authority and applicable rule version. |
| FR7 | Calculate and expose the applicable reporting deadline using an approved national-calendar implementation. |
| FR8 | Create one independently tracked delivery obligation per required destination. |
| FR9 | Preserve the invoice's historical network route for lifecycle obligations after route changes. |
| FR10 | Prevent an optional event type from activating until product/legal scope and external capability are approved. |

### Delivery and reconciliation

| ID | Requirement |
|---|---|
| FR11 | Deliver each logical event/destination combination idempotently with stable correlation. |
| FR12 | Treat destination acknowledgements and ambiguous outcomes independently. |
| FR13 | Reconcile `OUTCOME_UNKNOWN` before repeating a mutation. |
| FR14 | Deduplicate equivalent source events without discarding their provenance. |
| FR15 | Pause unsafe derivation/reporting when authoritative observations conflict. |
| FR16 | Append correcting/superseding events rather than altering accepted historical events. |
| FR17 | Buffer and reconcile out-of-order events using invoice identity and source chronology. |

### Product and operations

| ID | Requirement |
|---|---|
| FR18 | Expose a three-dimension lifecycle view and distinguish explicit facts from derived interpretations. |
| FR19 | Show pending customer action, reporting deadline and per-destination delivery outcome without internal protocol jargon. |
| FR20 | Let authorised products/users submit supported rejection/acceptance/payment facts and retrieve history. |
| FR21 | Give operations source events, derived rules, obligations, observed state, fault domain and safe recovery actions. |
| FR22 | Audit every customer, automated and manual event/reporting/recovery action. |

### Document correction and transitional applicability

| ID | Requirement |
|---|---|
| FR23 | When the applicable rule requires a new corrective/replacement document, Sage must retain the original and create a separately identified document linked through an immutable `DocumentRelationship`. |
| FR24 | A document relationship must retain relationship type, correction method, affected scope/values, reason, effective date, actor/authority, policy version and source evidence according to the approved country rule. |
| FR25 | Rejection, baja, event supersession and document rectification must remain distinct operations; none may silently imply another. |
| FR26 | The service must validate that the relationship type and correction method are permitted by the effective Spain rule before any external mutation. |
| FR27 | Duplicate or conflicting corrective documents/relationships must be detected using document identity, relationship, source and provenance and must enter controlled reconciliation when not provably equivalent. |
| FR28 | Lifecycle views must show the original and related documents, their independent states and the safe next action without presenting the original as deleted. |
| FR29 | Article 10/12 status obligation decisions must consume an effective-dated cohort outcome and distinguish `required`, `voluntary/not-yet-required`, `not-applicable` and `undetermined`. |
| FR30 | Deadline monitoring must not create an explicit acceptance event; any Article 12 presumed acceptance remains a versioned derived view reversible by later qualifying evidence. |

## Conceptual API/event capabilities

| Capability | Behavioural contract |
|---|---|
| Record lifecycle event | Idempotently accept authorised fact; return event and obligation state |
| Get lifecycle view | Return separate technical/commercial/payment views, sources, derivation and pending actions |
| List lifecycle history | Return ordered immutable events and supersession/conflict links subject to permission |
| Get reporting obligations | Return destinations, deadlines and delivery/reconciliation states |
| Correct event | Append an approved superseding fact; never overwrite prior evidence |
| Create related corrective document | Accept a new document and approved relationship intent; validate authority/rule; return independent document and compliance-plan state |
| Get document relationships | Return original/related identities, relationship type, affected scope, provenance and independent lifecycle states subject to permission |
| Notify product | Emit stable events when customer-relevant fact/action changes after durable persistence |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Protect payment, party and authority data through encryption, least privilege and tenant/environment isolation. |
| NFR2 | Use durable event persistence and idempotency so retries cannot create duplicate business facts or reports. |
| NFR3 | Version event mappings, deadline calendars and derivation rules with historical reproducibility. |
| NFR4 | Derive throughput/latency targets from invoice/event volumes and reporting-deadline headroom. |
| NFR5 | Alert before/at missed reporting risk and track pending/outcome-unknown age by destination. |
| NFR6 | Minimise sensitive invoice/payment detail in logs and operational evidence. |
| NFR7 | Retain events/evidence according to approved legal/privacy policy, including after route change. |
| NFR8 | Provide accessible customer wording that separates network, commercial and payment meaning. |

## Failure and recovery matrix

| Failure | Required behaviour |
|---|---|
| Unknown invoice identity | Reject/quarantine; do not report externally |
| Unauthorised actor | Reject, audit and alert according to security policy |
| Missing payment/effective date | Correctable validation failure before mutation |
| Duplicate event | Link provenance; create no duplicate obligations |
| Conflicting payment values | Preserve both, pause unsafe view/reporting and reconcile authority |
| Out-of-order event | Persist and derive using approved chronology/authority rules |
| Destination unavailable | Retry safely with deadline/age visibility |
| Timeout after mutation | Mark only that obligation outcome unknown and reconcile |
| Internal failure after external success | Recover via correlation/external reference; no duplicate report |
| Route changed since invoice | Use historical invoice route/context |
| Calendar/rule version changes | Apply version effective for the event and preserve calculation evidence |
| Invalid/unsupported document relationship | Reject before mutation with rule, relationship and affected-field guidance |
| Duplicate/conflicting corrective document | Link if provably identical; otherwise quarantine/reconcile without altering the original |
| Missing transition-cohort evidence | Return status applicability undetermined/action-required; do not create a false missed deadline |

## Acceptance criteria

- Given technical delivery success and no commercial event, when the customer views the invoice, then delivery is shown without claiming explicit acceptance or payment.
- Given an explicit rejection, when reporting is created, then source event, actor, effective date and independent issuer/public obligations are auditable.
- Given absence of rejection under an applicable presumed-acceptance rule, when the view is derived, then it is labelled presumed/derived and no explicit acceptance event is fabricated.
- Given full payment with an effective date, when accepted, then the approved four-day deadline calculation and required destinations are recorded.
- Given issuer reporting succeeds but public reporting times out, when reconciliation runs, then issuer delivery is not repeated and only the public obligation is resolved.
- Given duplicate equivalent events from ERP and operator, when deduplication runs, then one set of obligations exists while both source observations remain traceable.
- Given conflicting payment events, when authority cannot be established automatically, then external reporting/derived closure pauses and operations receives a controlled case.
- Given a route change after invoice exchange, when a later payment event occurs, then reporting follows the invoice's historical network obligations rather than the route for new invoices.
- Given four days elapse without an explicit acceptance/rejection event, when the lifecycle view is derived, then no explicit acceptance event or recipient-action timestamp is created.
- Given a delivered invoice requires rectification, when an authorised ERP supplies an approved corrective document and relationship, then a new document lifecycle is created and the original remains unchanged and queryable.
- Given a rejection exists without a corrective document, when the customer views the invoice, then rejection is shown without implying that rectification, cancellation or deletion occurred.
- Given two non-equivalent corrective documents claim to replace the same original, when conflict detection runs, then both are preserved, unsafe external mutation pauses and an owned reconciliation case is created.
- Given a qualifying natural person/income-attribution entity remains within the additional status transition, when Article 10/12 applicability is evaluated, then status supply is shown as voluntary/not-yet-required and no mandatory-deadline breach is generated.

## Measures

| Measure | Purpose | Owner |
|---|---|---|
| Required events reported within applicable deadline | Compliance/operational outcome | Product/compliance |
| Pending and outcome-unknown obligation age | Reconciliation health | Operations |
| Duplicate/conflicting event rate | Source/integration quality | Engineering/product |
| Corrected/superseded event rate | Customer and mapping quality | Product |
| Lifecycle source/authority completeness | Auditability | Data/QA |
| Customer support contacts by lifecycle dimension | Clarity of experience | Support/product |
| Historical-route lifecycle success | Transition continuity | Operations |

## Rollout gates

| Gate | Requirement |
|---|---|
| Discovery | Event catalogue, authority, deadlines, optional scope and public-service dependency confirmed |
| Design | Event/obligation/derived model, precedence, correction, calendar and route-continuity rules approved |
| Sandbox | Duplicate, conflict, ordering, timeout, correction and historical-route cases pass |
| External validation | Counterparty and public reporting/consultation evidenced for launch events |
| Pilot | Deadline monitoring, support, authority and kill/fallback controls pass PRD-SEI-221 |
| Production | Capacity, calendar/version change, BCP, reconciliation and retention tests pass |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| One status hides distinct facts | Three lifecycle dimensions plus immutable event history |
| Presumed acceptance misleads users | Label derived status and retain absence/source reasoning |
| Duplicate public reports | Event/destination idempotency and reconciliation |
| Missed statutory deadline | Approved calendar, early alerts, queue prioritisation and operational ownership |
| ERP and platform payment facts disagree | Source/authority rules and controlled conflict case |
| Route switch breaks old invoice lifecycle | Historical route snapshot and connection-aware continuity |
| Correction deletes evidence | Append-only supersession model |

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Hypothesis |
|---|---|---|---|---|
| Which Article 10 optional events are launch scope? | UI, API and mapping effort | Product/local team | Design | Full rejection/payment first; decide partial/assignment separately |
| Who is authoritative for payment: ERP, user, bank service or operator? | Prevents conflicting facts | Product/accounting/legal | Design/pilot | ERP/accounting truth with explicit authorised exceptions |
| How is the four-day calendar implemented for national holidays and effective time? | Deadline accuracy | Local legal/operations | Pilot | Approved central calendar/version |
| What public API/query supports rejection/payment reconciliation? | Unknown-outcome safety | Public technical team | External validation | Ministerial-order dependency |
| How should presumed acceptance appear and when does it apply? | Customer/legal clarity | Local legal/product | Design | Derived label only, never explicit event |
| How are corrections to an already reported payment/rejection expressed? | Audit and external consistency | Local technical/legal team | Pilot | Append superseding event if contract supports it |
| Which Spain relationship types, correction methods, affected values and identity-reuse rules apply to each rectifying/replacement scenario? | Determines document validation, ERP contract and external mapping | Local legal/tax/product owners | Design/pilot | Proposed model is extensible; activate only approved country-pack values |
| Which evidence source proves eligibility for the additional Article 10/12 transition? | Prevents false deadlines and customer misclassification | Local legal/product/data owners | Pilot/production | Versioned legal-form/tax-regime, turnover and effective-date evidence |
| Who owns older invoice status after route switch? | Credential and operational continuity | Local team/operator | Pilot/production | Original network context retained; owner to approve |
| What retention applies to event and delivery evidence? | Data/security design | Legal/privacy | Production | Configurable until approved |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 status, rejection and payment reporting PRD | PRD-SEI-210, Phase 1/2 lifecycle foundations and RD 238/2026 |
| 2026-08-24 | Working revision | Added proposed document relationships, corrective-document journeys, Article 10/12 timer safeguard and additional status-transition behaviour | RD 238/2026; PRD-SEI-231/232; Spain solution-design brief comparison |
