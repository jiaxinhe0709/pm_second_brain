---
id: PRD-SEI-223
title: Exchange — Interoperability, Routing and Transformation
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-24
reviewers: []
related:
  - PRD-SEI-210
  - FP-SEI-001
  - ADR-SEI-001
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-224
  - PRD-SEI-103
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-231
  - PRD-SEI-233
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "876576916"
  page_id: "866148656"
  title: Exchange — Interoperability, Routing and Transformation
  layout: two_left_sidebar
  toc: true
---

# Exchange — Interoperability, Routing and Transformation

## Decision summary

Phase 3 must exchange an invoice from a Sage customer to the recipient's authoritative entry point—Sage private platform, another private platform or the public solution—while preserving business meaning, authenticity/integrity evidence, immutable route context and the required public copy.

Routing, transformation, signing and public-copy submission are related but distinct decisions. The platform should establish an immutable exchange plan before the first external mutation, then execute each required leg idempotently and reconcile ambiguous outcomes.

> **Product principle:** Choose the route from authoritative evidence, transform before the applicable signature/seal, and preserve one traceable identity across every network representation.

## Phase and outcome

| Phase | Exchange capability | Phase 3 implication |
|---|---|---|
| Phase 1 | Submit/retrieve through public solution | Reuse where evidence proves fitness; public remains a valid route and required repository/copy boundary |
| Phase 2 | Route through configured external provider adapters | Reuse routing, adapter, context and resilience patterns |
| **Phase 3** | Operate Sage private-platform exchange and interconnection | Add external ingress, admitted-syntax transformation, trust, direct/public bridging and operator evidence |

## Problem and objective

### Problem

A business invoice may be created in one Sage/product format, exchanged in a syntax agreed by trading parties, transformed by an operator, signed or sealed, delivered through a direct private interconnection or the public solution, and copied to the public repository in UBL. Each representation must remain attributable to the same business invoice without losing required content or obscuring which platform performed each action.

Failure risks include:

- routing from stale customer configuration rather than authoritative entry-point evidence;
- sending privately when the recipient must be reached through the public solution;
- transforming after signature and invalidating authenticity/integrity evidence;
- semantic loss between CII, UBL, EDIFACT or Facturae representations;
- duplicate delivery or public copy after a timeout;
- treating successful transport as recipient acceptance;
- allowing direct and public-bridge paths to create competing invoice histories;
- failing to retrieve an invoice deposited in the public solution during interconnection setup;
- exposing partner or country-specific contracts directly to Sage products.

### Objective

Define a product-neutral exchange capability that plans, validates, transforms, signs/seals, submits, receives, acknowledges and reconciles every required exchange leg with stable identities, evidence and operational control.

## Scope and non-goals

### In scope

- Outbound and inbound exchange through Sage, other private platforms and the public solution.
- Recipient entry-point resolution and route decision evidence.
- Admitted syntax/profile negotiation, validation and transformation.
- Advanced signature/seal orchestration and evidence boundaries.
- Required faithful UBL public copy and correlation.
- Direct private interconnection and public-solution bridging.
- Idempotency, duplicate detection, outcome-unknown reconciliation and quarantine.
- Product-neutral API/event capability and operations experience.

### Non-goals

- Final endpoint names, schemas or authentication before official/architecture approval.
- Customer onboarding and route activation; see PRD-SEI-222.
- Full lifecycle/payment business behaviour; see PRD-SEI-224.
- Deciding build/partner/acquisition.
- Supporting proprietary syntax as a launch commitment without approved scope/evidence.
- Tax/legal validation beyond the approved invoice rule packs.
- Recreating provider-specific adapter detail from Phase 2 PRDs.

## Definitions

| Term | Meaning | Not equivalent to |
|---|---|---|
| Business invoice identity | Stable identity of the commercial invoice across representations | One provider's transmission ID |
| Representation | Versioned syntax/profile instance of the invoice | A new commercial invoice |
| Exchange plan | Immutable decision record for required route, transformations, trust and public-copy legs | Current customer route configuration |
| Entry-point evidence | Authoritative observed information used to determine receipt destination | A cached preference without freshness/provenance |
| Direct interconnection | Exchange between qualifying private platforms | A customer-specific ERP API |
| Public bridge | Use of the public solution as the transport/interconnection route | The faithful copy alone |
| Faithful copy | Required UBL copy marked/treated as a copy in the public solution | The recipient-delivered original representation |
| Transport acknowledgement | Evidence that a network accepted a message | Business acceptance of the invoice |
| Transformation provenance | Input/output syntax, mapping/rule version, actor and validation evidence | A generic “converted” flag |
| Outcome unknown | Mutation may have succeeded externally but acknowledgement is absent | Confirmed failure |

## Exchange route visual

<!-- confluence-html-macro:start -->
<div class="p3xchg-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3xchg-visual *{box-sizing:border-box}.p3xchg-visual h2{margin:0;color:#172b4d;font-size:18px}.p3xchg-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3xchg-visual svg{display:block;width:1080px;height:520px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3xchg-visual .sage{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3xchg-visual .decision{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3xchg-visual .private{fill:#eae6ff;stroke:#6554c0;stroke-width:1.5}.p3xchg-visual .public{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3xchg-visual .error{fill:#ffebe6;stroke:#ff5630;stroke-width:1.5}.p3xchg-visual .title{fill:#172b4d;font-size:11px;font-weight:700}.p3xchg-visual .copy{fill:#42526e;font-size:9px}.p3xchg-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3xchg-visual .path{fill:none;stroke:#00875a;stroke-width:2}.p3xchg-visual .private-path{fill:none;stroke:#6554c0;stroke-width:1.8}.p3xchg-visual .public-path{fill:none;stroke:#0052cc;stroke-width:1.8}.p3xchg-visual .retry{fill:none;stroke:#de350b;stroke-width:1.5;stroke-dasharray:6 4}.p3xchg-visual .arrow{fill:#00875a}.p3xchg-visual .arrow-p{fill:#6554c0}.p3xchg-visual .arrow-b{fill:#0052cc}.p3xchg-visual .arrow-r{fill:#de350b}.p3xchg-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3xchg-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3xchg-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>One exchange plan, multiple evidenced legs</h2>
  <p class="sub">The recipient route and public-copy duty are planned once. Direct private delivery and public bridging remain traceable to the same invoice identity.</p>
  <svg viewBox="0 0 1080 520" role="img" aria-label="A Sage product creates invoice intent. The shared platform validates and establishes an immutable exchange plan, transforms to the agreed syntax before applying signature or seal, then routes either directly to another private platform, through the public solution as a bridge, or to a Sage recipient. A separate correlated faithful UBL copy is sent to the public solution where required. Ambiguous outcomes enter reconciliation rather than blind retry.">
    <text x="34" y="34" class="label">PRODUCT INTENT</text><text x="235" y="34" class="label">SHARED EXCHANGE CORE</text><text x="710" y="34" class="label">NETWORK LEGS</text>
    <rect x="34" y="82" width="166" height="84" rx="9" class="sage"/><text x="52" y="109" class="title">Invoice intent</text><text x="52" y="130" class="copy">Legal entity • recipient</text><text x="52" y="147" class="copy">canonical business data</text>
    <path d="M200 124 H232" class="path"/><polygon points="232,124 222,118 222,130" class="arrow"/>
    <rect x="234" y="72" width="184" height="104" rx="9" class="sage"/><text x="252" y="99" class="title">Validate and identify</text><text x="252" y="120" class="copy">Business rules • unique identity</text><text x="252" y="138" class="copy">route snapshot inputs</text><text x="252" y="156" class="copy">reject before mutation if invalid</text>
    <path d="M418 124 H450" class="path"/><polygon points="450,124 440,118 440,130" class="arrow"/>
    <rect x="452" y="62" width="206" height="124" rx="9" class="decision"/><text x="470" y="89" class="title">Immutable exchange plan</text><text x="470" y="110" class="copy">Authoritative entry point and route</text><text x="470" y="128" class="copy">syntax/profile and transformation</text><text x="470" y="146" class="copy">signature/seal and public copy</text><text x="470" y="164" class="copy">idempotency and evidence keys</text>
    <path d="M658 124 H698" class="path"/><polygon points="698,124 688,118 688,130" class="arrow"/>
    <rect x="700" y="72" width="166" height="104" rx="9" class="sage"/><text x="718" y="99" class="title">Transform then trust</text><text x="718" y="120" class="copy">Agreed admitted syntax</text><text x="718" y="138" class="copy">semantic validation</text><text x="718" y="156" class="copy">apply signature / seal</text>
    <path d="M866 104 H902 V78" class="private-path"/><polygon points="902,78 896,88 908,88" class="arrow-p"/>
    <rect x="904" y="48" width="142" height="64" rx="8" class="private"/><text x="922" y="74" class="title">Direct private</text><text x="922" y="94" class="copy">Other platform / Sage</text>
    <path d="M866 142 H902 V194" class="public-path"/><polygon points="902,194 896,184 908,184" class="arrow-b"/>
    <rect x="904" y="196" width="142" height="64" rx="8" class="public"/><text x="922" y="222" class="title">Public bridge</text><text x="922" y="242" class="copy">Recipient retrieval route</text>
    <path d="M555 186 V320 H902" class="public-path"/><polygon points="902,320 892,314 892,326" class="arrow-b"/>
    <rect x="904" y="288" width="142" height="64" rx="8" class="public"/><text x="922" y="314" class="title">Faithful UBL copy</text><text x="922" y="334" class="copy">Correlated public record</text>
    <rect x="452" y="286" width="268" height="84" rx="9" class="sage"/><text x="470" y="313" class="title">Persist evidence and lifecycle handoff</text><text x="470" y="334" class="copy">Transport results • external IDs • representations</text><text x="470" y="352" class="copy">route context • status correlation • audit</text>
    <path d="M975 112 V278 H720 V328" class="private-path"/><polygon points="720,328 714,318 726,318" class="arrow-p"/>
    <path d="M975 260 V278" class="public-path"/>
    <path d="M975 352 V400 H720" class="public-path"/><polygon points="720,400 730,394 730,406" class="arrow-b"/>
    <rect x="452" y="392" width="268" height="82" rx="9" class="error"/><text x="470" y="419" class="title">Outcome unknown / conflicting evidence</text><text x="470" y="440" class="copy">Freeze unsafe retry • reconcile each external leg</text><text x="470" y="458" class="copy">resume, quarantine or escalate with redacted evidence</text>
    <path d="M586 370 V384" class="retry"/><polygon points="586,384 580,374 592,374" class="arrow-r"/>
  </svg>
  <div class="notes"><div class="note"><strong>Route and copy differ</strong>The recipient delivery leg and required public copy are independently evidenced.</div><div class="note"><strong>Transform before signing</strong>Every representation records mapping, validation and trust provenance.</div><div class="note"><strong>Reconcile by leg</strong>A successful private delivery does not imply that the public copy succeeded, or vice versa.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors and responsibilities

| Actor | Responsibility |
|---|---|
| Sage ERP/API consumer | Submit canonical invoice intent and consume stable lifecycle outcomes |
| Sage exchange core | Validate, identify, plan, orchestrate, persist context and reconcile |
| Sage private-platform operator | Perform or govern external ingress/egress, transformation, trust and interconnection |
| Sender/recipient platform | Exchange invoice and required statuses using agreed/required syntax |
| Public solution | Public receipt route, bridge and repository/copy services according to regulation/specification |
| Operations/support | Diagnose each exchange leg and perform only safe recovery |
| Security/compliance | Approve protocols, certificates, transformations, evidence and data controls |

## Business scenarios

| ID | Scenario | Expected route/behaviour | Exception/continuity |
|---|---|---|---|
| S1 | Sage sender and Sage private recipient | Internal/operator exchange using the approved representation | Still produce required public copy and evidence |
| S2 | Sage sender to another private platform with direct interconnection | Deliver through direct platform route in agreed syntax | Public copy remains a separate correlated leg |
| S3 | Direct interconnection not yet operational | Deposit/deliver through public solution bridging according to approved rules | Recipient platform must retrieve; history records bridge route |
| S4 | Recipient has no public private entry point | Use public solution as default receipt route | Do not assume a private destination from stale data |
| S5 | Input syntax differs from recipient syntax | Transform before applicable signature and validate semantic preservation | Quarantine on material loss/invalid mapping |
| S6 | Private delivery succeeds but public copy times out | Preserve private success; reconcile copy independently | Do not redeliver the private invoice |
| S7 | Duplicate inbound representation arrives | Resolve by business identity/network identifiers and retain evidence | Do not create a second business invoice |
| S8 | Status/event arrives before invoice persistence completes | Buffer/reconcile by stable identifiers | Preserve event source/order evidence |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Exchange plan is created | Freeze route, syntax/profile, mapping, trust and copy decisions for that exchange attempt | Proposed safety rule |
| BR2 | Recipient private entry point is authoritative and ready | Use the selected private route for eligible traffic | Entry-point authority details open |
| BR3 | No private receipt entry point is identified | Use public solution as default receipt route | RD 238/2026 Article 6 |
| BR4 | Parties have an approved syntax/specification agreement | Use that agreement when supported and evidenced | RD 238/2026 Article 7 |
| BR5 | No bilateral syntax agreement exists | Use the syntax/specifications required for the public solution | RD 238/2026 Article 7 |
| BR6 | Transformation is required between private platforms | Sender-side platform transforms before the invoice is signed for exchange | RD 238/2026 Article 7; legal/technical review required |
| BR7 | Invoice is not emitted through the public solution | Send the required faithful UBL copy simultaneously as defined by the approved specification | RD 238/2026 Article 6; exact transaction semantics open |
| BR8 | Direct interconnection is unavailable during setup | Use the public solution bridge according to the statutory process | RD 238/2026 Article 9 |
| BR9 | One external leg succeeds and another is unknown | Preserve successful evidence and reconcile only the unknown leg | Proposed resilience rule |
| BR10 | Representation changes | Preserve business identity plus input/output syntax, mapping and trust provenance | Proposed audit rule |
| BR11 | Provider/network supports Peppol | Treat it as one evidenced capability/address family only; do not infer that Peppol is Spain's universal statutory route, participant authority or entry-point directory | RD 238/2026 public/private model plus PRD-SEI-233 |

## Research and evidence register

| Source | Finding | Confidence/limitation | Requirement impact |
|---|---|---|---|
| RD 238/2026 Articles 5–7 | Public/private system, entry-point default, UBL public copy, admitted syntaxes, transformation and signature | Primary regulation; official profiles/specifications still required | Routing, formats, copy and trust |
| RD 238/2026 Articles 8–9 | Direct interconnection, public bridge, invoice/status scope and operational procedure | Primary regulation; detailed interfaces open | Interconnection routing and fallback |
| RD 238/2026 Articles 11–13 | Public UBL boundary, authentication dependency, operator AS2/AS4 and capability requirements | Primary regulation; ministerial-order detail open | Protocol, public adapter and readiness |
| PRD-SEI-103 | Public submission validation, idempotency and evidence patterns | Product intent/implementation fitness unassessed | Reuse candidate via FP-SEI-001 |
| PRD-SEI-202/203 | Route snapshot, adapter boundary, outcome-unknown and reconciliation | Product intent/implementation fitness unassessed | Shared exchange/resilience behaviour |

## Proposed conceptual model

| Record | Required information |
|---|---|
| Business invoice | Legal parties, invoice number/series/date, canonical content/version and internal identity |
| Representation | Syntax/profile/version, payload hash, source, transform mapping, validation result and trust evidence |
| Entry-point observation | Recipient legal subject/presence, participant-address scheme/value, direction/scope, destination, authoritative source, observed time, validity/freshness and evidence |
| Exchange plan | Immutable recipient route, legs, representation plan, trust actor, copy duty, rule versions and created time |
| Exchange leg | Type (`PRIVATE_DIRECT`, `PUBLIC_BRIDGE`, `PUBLIC_COPY`, `INTERNAL`), destination, request/idempotency ID and state |
| External evidence | Platform reference, acknowledgement, timestamp, protocol/certificate evidence and redacted diagnostic |
| Reconciliation case | Intended/observed state, safe actions, owner, attempts, result and audit |

### Proposed exchange-leg states

`PLANNED → VALIDATED → READY_TO_SEND → SUBMITTED → ACKNOWLEDGED → COMPLETED`

Recoverable branches: `REJECTED_CORRECTABLE`, `RETRY_PENDING`, `OUTCOME_UNKNOWN`, `RECONCILING`, `QUARANTINED`, `FAILED_TERMINAL`.

Transport acknowledgement and business lifecycle state remain separate.

## Detailed journeys

### J1 — Outbound direct private exchange

1. Product submits canonical invoice intent with legal entity and recipient.
2. Sage validates business identity and resolves current authoritative entry-point evidence.
3. An immutable exchange plan selects direct private delivery and required public-copy leg.
4. Sage transforms to the agreed admitted syntax, validates semantics and applies the approved signature/seal process.
5. Direct delivery and public copy execute as separately correlated idempotent legs.
6. Evidence and lifecycle handoff are persisted before success is reported.

### J2 — Outbound through public bridge

1. Route resolution finds no direct operational interconnection or the public solution is the applicable route.
2. Exchange plan identifies public bridge/recipient behaviour and UBL representation.
3. Sage validates and submits once using a stable idempotency identity.
4. The receiving platform/customer retrieves through the public route.
5. Sage correlates transport and later lifecycle evidence without creating a duplicate copy leg.

### J3 — Correct a transformation failure

1. Validation identifies unsupported value, mapping loss or profile violation before external mutation.
2. The invoice is rejected to product/user with field-level safe diagnostics and mapping/rule version.
3. The source is corrected or an approved mapping change is versioned.
4. A new representation is generated under the same business invoice with a new attempt identity.
5. The original failed representation remains auditable but is never transmitted.

### J4 — Reconcile a partial/ambiguous outcome

1. Direct private delivery is acknowledged, but public-copy submission times out.
2. Sage records direct success and marks only the copy leg `OUTCOME_UNKNOWN`.
3. Reconciliation queries the public solution using stable correlation/identity.
4. If present, copy succeeds; if absent and resubmission is safe, the same logical copy resumes.
5. The private recipient delivery is never repeated because of copy uncertainty.

### J5 — Inbound direct private exchange

1. A qualifying platform authenticates and submits an admitted signed representation.
2. Sage validates sender platform, transport, signature/integrity, syntax/profile and unique identity.
3. Duplicate detection checks business and external identifiers before product delivery.
4. Sage transforms into canonical form while retaining the original representation/evidence.
5. The invoice is delivered once to the correct legal entity/product and acknowledged according to the approved contract.

### J6 — Inbound retrieved from public bridge

1. Consultation/event trigger identifies an invoice addressed to a Sage private-platform customer.
2. Sage retrieves using an idempotent checkpoint and validates recipient route/effective interval.
3. Original public representation and reference are retained.
4. Canonical invoice is delivered once; checkpoint advances only after durable persistence.
5. Late/direct duplicate is reconciled to the existing business invoice.

## Functional requirements

### Planning and routing

| ID | Requirement |
|---|---|
| FR1 | Resolve recipient route from approved authoritative evidence with source, freshness and scope. |
| FR2 | Create an immutable exchange plan before any external mutation. |
| FR3 | Record the exact route/rule version and effective observation used for the decision. |
| FR4 | Support direct private, public bridge, public copy and internal Sage legs without merging their outcomes. |
| FR5 | Refuse or quarantine exchange when no eligible, explainable route exists. |

### Identity, validation and transformation

| ID | Requirement |
|---|---|
| FR6 | Assign/preserve a stable business invoice identity and the applicable statutory unique-code components. |
| FR7 | Validate canonical content and every external representation against versioned syntax/profile/business rules. |
| FR8 | Transform between activated admitted syntaxes without material semantic loss and with recorded provenance. |
| FR9 | Apply the approved signature/seal only after the required transformation for the selected representation. |
| FR10 | Retain original received representation and evidence according to approved retention rules. |
| FR11 | Prevent a syntax/profile from activation until conformance and semantic-preservation tests pass. |

### Outbound and public copy

| ID | Requirement |
|---|---|
| FR12 | Execute every mutating exchange leg with a stable logical idempotency/correlation identity. |
| FR13 | Generate and submit the faithful UBL public copy where required, marked and correlated as a copy. |
| FR14 | Persist internal invoice/plan state before external mutation or provide a proven recovery mechanism for external-first success. |
| FR15 | Treat each leg's acknowledgement, rejection and unknown outcome independently. |
| FR16 | Never repeat a completed recipient-delivery leg solely because another leg is incomplete. |

### Inbound and interconnection

| ID | Requirement |
|---|---|
| FR17 | Authenticate and authorise inbound platform traffic by operator, environment and capability. |
| FR18 | Validate transport, signature/integrity, syntax/profile, recipient and unique identity before product delivery. |
| FR19 | Deduplicate direct, retried and public-bridge representations to one business invoice while retaining all source evidence. |
| FR20 | Deliver an accepted inbound invoice durably to the correct legal entity/product exactly once at the business level. |
| FR21 | Support the approved interconnection request/test/activation and public-bridge transition defined by PRD-SEI-221. |

### Resilience and operations

| ID | Requirement |
|---|---|
| FR22 | Classify operations as safe retry, idempotent resume, reconcile-first or manual-only. |
| FR23 | Reconcile `OUTCOME_UNKNOWN` against the relevant external leg before retransmission. |
| FR24 | Quarantine invalid, untrusted, conflicting or unrouteable inbound content with redacted operational evidence. |
| FR25 | Expose intended/observed state, correlation, representation, external reference, safe action and owner per leg. |
| FR26 | Preserve a complete audit chain from product intent through every representation, route leg and outcome. |
| FR27 | Entry-point and participant addresses must remain scheme-qualified and separate from NIF, provider resource IDs and credentials, including when several addresses exist for one legal subject. |
| FR28 | Peppol capability or address discovery must not be treated as Spain route authority unless the approved customer/regulatory entry-point evidence selects it for the scoped exchange. |

## Conceptual API/event capabilities

Names and payloads are proposed boundaries, not approved endpoints.

| Capability | Minimum contract behaviour |
|---|---|
| Submit invoice intent | Accept canonical identity/content plus legal entity; return stable request/invoice identity and asynchronous state |
| Get exchange plan/outcome | Return route snapshot, representation/leg states and customer-safe failure information |
| Receive invoice event | Notify product after durable canonical persistence with source network context |
| Retrieve original/evidence | Authorised retrieval of original representation and redacted exchange evidence |
| Correct/resubmit | Create a new attempt/representation without changing the original failed evidence |
| Reconcile operation | Operations-only action to compare intended/observed external state without blind mutation |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Use approved AS2/AS4 and/or official public-solution protocols according to the activated boundary. |
| NFR2 | Protect signing/sealing keys and credentials using approved custody, rotation, revocation and separation of duties. |
| NFR3 | Derive throughput, payload, latency, queue and recovery targets from an approved volume/format model. |
| NFR4 | Apply backpressure and fair scheduling so one tenant/platform cannot starve others. |
| NFR5 | Encrypt invoice content/evidence and minimise sensitive data in logs, metrics and support artefacts. |
| NFR6 | Isolate tenant, operator, environment and certificate contexts. |
| NFR7 | Version schemas, profiles, mappings and route rules with backward/rollout controls. |
| NFR8 | Provide end-to-end correlation and immutable audit sufficient to reconstruct each exchange plan and leg. |
| NFR9 | Make customer/product status accessible and distinguish transport, validation and business outcomes. |

## Failure and recovery matrix

| Failure | Required response |
|---|---|
| Stale/missing entry-point evidence | Refresh or stop as unrouteable; do not guess private destination |
| Unsupported syntax/profile | Reject before mutation with supported alternatives |
| Semantic transformation loss | Quarantine and require corrected mapping/source |
| Signature/certificate invalid | Reject/quarantine; never deliver as trusted |
| Recipient validation rejection | Preserve rejection evidence; allow corrected new attempt according to business rules |
| Throttle/transient outage before mutation | Backoff/resume safely according to contract |
| Timeout after mutation | Mark only affected leg outcome unknown; reconcile first |
| Internal persistence failure after external success | Recover via correlation and external evidence; prevent duplicate leg |
| Duplicate direct/public inbound | Merge to one business invoice; retain all delivery evidence |
| Out-of-order status before invoice | Buffer/reconcile; never invent invoice state |
| Direct interconnection unavailable | Apply approved public bridge without rewriting route history |
| Conflicting representations for same identity | Quarantine, preserve both and escalate |

## Acceptance criteria

- Given a recipient with an observed-ready private entry point and direct interconnection, when a valid invoice is submitted, then the exchange plan records direct delivery plus any required public-copy leg before transmission.
- Given no published private entry point, when route resolution runs, then the public solution is selected and the decision source/time is auditable.
- Given transformation from EDIFACT to UBL, when conformance runs, then required semantic content, business identity and provenance are preserved before signing.
- Given direct delivery succeeds and the public copy is outcome-unknown, when reconciliation runs, then the copy is resolved independently and direct delivery is not repeated.
- Given the same invoice arrives directly and through public bridge, when deduplication runs, then one business invoice is delivered while both network references remain auditable.
- Given a certificate is invalid, when inbound validation runs, then the invoice is quarantined and no product delivery or trusted acknowledgement occurs.
- Given interconnection is not operational, when the approved bridge applies, then exchange through the public solution remains traceable to the same invoice identity and route decision.
- Given a provider advertises Peppol and a Spanish recipient has no approved Peppol entry-point selection, when route resolution runs, then Peppol is not selected by capability presence alone and the approved Spain public/private route rule is applied.
- Given one legal subject has multiple scheme-qualified participant addresses, when exchange is planned, then the exact address, scheme, source, scope and observation used are frozen in the exchange plan.

## Measures

| Measure | Purpose | Owner |
|---|---|---|
| Exchange success by route/leg/syntax | Reliability and coverage | Product/operations |
| Transformation rejection and semantic-loss cases | Mapping quality | Engineering/local compliance |
| Duplicate rate and dedupe conflicts | Identity quality | Engineering |
| Outcome-unknown count/age by external leg | Reconciliation health | Operations |
| Route-resolution failures/stale observations | Entry-point health | Platform operations |
| Public-copy completeness/correlation | Regulatory evidence | Compliance/operations |
| End-to-end and queue latency percentiles | Capacity/customer experience | Engineering/product |

## Rollout gates

| Gate | Requirement |
|---|---|
| Discovery | Official profiles, public contract, entry-point authority and launch syntax/route scope confirmed |
| Design | Exchange plan, identity, trust, transformation, adapter and evidence boundaries approved |
| Internal conformance | Positive, negative, duplicate, timeout, persistence and semantic-loss corpus passes |
| External conformance | Public and at least one counterparty platform validate each launch route/syntax |
| Pilot | PRD-SEI-221 controls, monitoring, operations and bridge/fallback criteria approved |
| Production | Capacity, BCP, certificate rotation, reconciliation and version rollout tests pass |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| One invoice becomes multiple business records | Stable identity, representation/leg model and cross-route dedupe |
| Transformation corrupts business meaning | Versioned mappings, semantic comparison and quarantine |
| Signature applied at wrong point | Exchange-plan trust sequence and conformance tests |
| Public copy and delivery become coupled retries | Independent leg state and reconciliation |
| Stale directory data misroutes invoices | Source/freshness evidence, refresh and no-guess rule |
| Partner adapter leaks into Sage products | Product-neutral capability contract and controlled wrapper |
| Protocol/certificate operations underestimated | PRD-SEI-221 security and readiness controls |

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Hypothesis |
|---|---|---|---|---|
| What is the authoritative entry-point query and freshness model? | Route correctness | Local technical/regulatory team | Design/external test | Record source/freshness and refresh before plan |
| Which syntax profiles and mapping rules are launch scope? | Transformation/test effort | Local compliance/product | Design | Minimum legally required scope, subject to evidence |
| What exactly makes the public UBL copy “faithful”? | Mapping/evidence | Local legal/technical team | Conformance | Semantic equivalence plus required marking/reference |
| What are official idempotency/query capabilities for the public solution? | Unknown-outcome safety | Public technical team | Pilot | Reconcile-first wrapper required |
| How is bilateral syntax agreement discovered and evidenced? | Route/transform decision | Legal/product/operator | Design | Explicit trading agreement record |
| Who signs: issuer, delegated operator or platform? | Trust model and transform order | Legal/security/operator | Design | Support approved modes with explicit evidence |
| Can direct and bridge deliveries coexist during interconnection cutover? | Duplicate/reachability risk | Local/operator | External test | Dedupe and effective intervals required |
| Which statuses must interconnection exchange? | Boundary with PRD-SEI-224 | Local team | Lifecycle design | Article 10 minimum plus approved extensions |
| Which authoritative Spain source selects among multiple participant addresses and networks, including Peppol? | Prevents capability discovery becoming route authority | Local technical/regulatory team | Design/external test | Use PRD-SEI-233 precedence model only after Spain evidence approves the source |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 interoperability, routing and transformation PRD | PRD-SEI-210, Phase 1/2 foundations and RD 238/2026 |
| 2026-08-24 | Working revision | Added scheme-qualified multi-address routing and explicit prohibition on treating Peppol availability as Spain's universal statutory route | PRD-SEI-231/233; RD 238/2026 |
