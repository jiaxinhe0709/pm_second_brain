---
id: PRD-SEI-225
title: Operations — Resilience, Support and Reconciliation
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-210
  - PRD-SEI-203
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-226
  - ADR-SEI-001
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: "866148658"
  title: Operations — Resilience, Support and Reconciliation
  layout: two_left_sidebar
  toc: true
---

# Operations — Resilience, Support and Reconciliation

## Decision summary

Phase 3 requires an operator-grade service model that can detect degradation, protect invoices, reconcile ambiguous external outcomes, coordinate Sage and partner recovery, and communicate customer impact across public, private and historical routes.

The operating model must be designed around safe outcomes rather than generic retry. Each external operation must have a known safety class; each case must show intended and observed state, fault domain, customer impact, deadline exposure, evidence and the next authorised action. Support availability and measurable service objectives remain subject to legal, risk and operating-model approval.

> **Product principle:** Preserve the invoice first, establish the external truth second, and mutate again only when the next action is proven safe.

## Phase and outcome

| Phase | Operational scope | Phase 3 consequence |
|---|---|---|
| Phase 1 | Public submission/consultation monitoring and recovery | Reuse public-route telemetry and reconciliation where proven fit |
| Phase 2 | Multiple provider adapters, route transitions and outcome-unknown handling | Reuse shared cases, safety classification and route continuity |
| **Phase 3** | Sage-branded private-platform operation | Add platform-wide incident command, interconnection operations, partner accountability, BCP and regulated support evidence |

## Problem and objective

### Problem

Private-platform operation spans Sage products, shared services, an operator edge, the public solution, counterparties and potentially an underlying partner. A failure may occur before a mutation, after an external success, during internal persistence, or after one of several required delivery legs completes. Customers see one Sage proposition, but support must identify the actual fault and safe action.

Without a shared operating model:

- blind retries may duplicate invoices, registrations or lifecycle reports;
- a successful private delivery may be repeated because its public-copy leg failed;
- backlog may conceal statutory or commercial deadline exposure;
- support may tell a customer “failed” while the external platform accepted the mutation;
- Sage and a partner may each wait for the other to lead an incident;
- historical-route work may stop after a customer switches provider;
- manual recovery may bypass permissions, evidence or lifecycle rules;
- nominal availability may hide an unusable service with no reconciliation or support capacity.

### Objective

Provide one operational control plane and service model for health, cases, reconciliation, safe recovery, incident command, capacity, continuity, supplier escalation and customer communication across every Phase 3 route and lifecycle obligation.

## Scope and non-goals

### In scope

- End-to-end observability and service health by component, route, operator and obligation.
- Operation-safety classification, idempotency and reconciliation-first recovery.
- Operational case lifecycle, queues, ownership, escalation and evidence.
- Incident command across Sage, public solution, counterparty and partner boundaries.
- Backlog, deadline, capacity, degradation, BCP/DR and controlled suspension.
- Customer/support experience and historical-route continuity.
- Runbooks, manual action permissions, audit and operational readiness gates.

### Non-goals

- Setting invented availability, response, recovery or support targets.
- Replacing corporate incident, security or supplier-management processes.
- Defining cryptographic and data-security controls in depth; see PRD-SEI-226.
- Deciding the operator/delivery model.
- Resolving commercial invoice disputes.
- Making every provider/platform failure automatically recoverable.

## Definitions

| Term | Meaning | Not equivalent to |
|---|---|---|
| Intended state | What Sage has durably requested/selected | Proof that an external system applied it |
| Observed state | Last evidenced external state with source/time | Current truth when evidence is stale |
| Operation safety class | Approved rule for retry/resume/reconcile/manual handling | An HTTP method assumption |
| Outcome unknown | Mutation may have succeeded but acknowledgement is absent | Confirmed failure |
| Reconciliation | Compare intended and observed state and converge safely | Repeating the mutation |
| Operational case | Owned unit of diagnosis/recovery with evidence and audit | A raw log alert |
| Degraded mode | Restricted service that protects safe capabilities and history | Full service availability |
| Suspension | Controlled stop of new affected activity after readiness/control loss | Deletion or final offboarding |
| BCP | Organisational and technical continuity for the service outcome | Disaster recovery technology alone |
| Customer-impact clock | Product/operational measure of elapsed risk or missed outcome | An unapproved statutory SLA |

## Operational control visual

<!-- confluence-html-macro:start -->
<div class="p3ops-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3ops-visual *{box-sizing:border-box}.p3ops-visual h2{margin:0;color:#172b4d;font-size:18px}.p3ops-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3ops-visual svg{display:block;width:1080px;height:510px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3ops-visual .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3ops-visual .gate{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3ops-visual .fault{fill:#ffebe6;stroke:#ff5630;stroke-width:1.5}.p3ops-visual .external{fill:#fff;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3ops-visual .done{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3ops-visual .title{fill:#172b4d;font-size:11px;font-weight:700}.p3ops-visual .copy{fill:#42526e;font-size:9px}.p3ops-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3ops-visual .path{fill:none;stroke:#00875a;stroke-width:2}.p3ops-visual .warn{fill:none;stroke:#ff8b00;stroke-width:1.7;stroke-dasharray:6 4}.p3ops-visual .alert{fill:none;stroke:#de350b;stroke-width:1.7;stroke-dasharray:6 4}.p3ops-visual .handoff{fill:none;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3ops-visual .arrow{fill:#00875a}.p3ops-visual .arrow-a{fill:#ff8b00}.p3ops-visual .arrow-r{fill:#de350b}.p3ops-visual .arrow-g{fill:#7a869a}.p3ops-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3ops-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3ops-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Detect, contain, reconcile and recover safely</h2>
  <p class="sub">Every alert becomes actionable only when it is correlated to a customer outcome, safety class, observed external state and accountable owner.</p>
  <svg viewBox="0 0 1080 510" role="img" aria-label="Telemetry from Sage products, shared services, the operator edge, public solution and counterparties feeds a health and deadline view. A detected issue is contained, classified by operation safety, and reconciled against external state. Safe operations resume automatically, ambiguous or unsafe cases go to an owned operational case and incident command, and recovery is validated before customer communication and closure. Historical lifecycle work continues during degradation.">
    <text x="34" y="34" class="label">SIGNALS</text><text x="270" y="34" class="label">CONTROL AND DIAGNOSIS</text><text x="765" y="34" class="label">RECOVERY AND ACCOUNTABILITY</text>
    <rect x="34" y="68" width="190" height="74" rx="9" class="external"/><text x="52" y="95" class="title">Multi-boundary telemetry</text><text x="52" y="116" class="copy">Sage • operator • public • partner</text>
    <rect x="34" y="177" width="190" height="74" rx="9" class="external"/><text x="52" y="204" class="title">Queues and deadlines</text><text x="52" y="225" class="copy">Backlog • age • capacity • expiry</text>
    <rect x="34" y="286" width="190" height="74" rx="9" class="external"/><text x="52" y="313" class="title">Customer/support signals</text><text x="52" y="334" class="copy">Cases • complaints • route mismatch</text>
    <path d="M224 105 H260 V203" class="path"/><path d="M224 214 H260" class="path"/><path d="M224 323 H260 V225" class="path"/><polygon points="260,214 250,208 250,220" class="arrow"/>
    <rect x="262" y="151" width="188" height="126" rx="9" class="main"/><text x="280" y="178" class="title">Detect and contain</text><text x="280" y="199" class="copy">Identify affected route/leg/scope</text><text x="280" y="217" class="copy">Protect queues and historical work</text><text x="280" y="235" class="copy">Stop only unsafe new mutations</text><text x="280" y="253" class="copy">create correlated case</text>
    <path d="M450 214 H486" class="path"/><polygon points="486,214 476,208 476,220" class="arrow"/>
    <rect x="488" y="141" width="216" height="146" rx="9" class="gate"/><text x="506" y="168" class="title">Classify safety and truth</text><text x="506" y="190" class="copy">Safe retry • idempotent resume</text><text x="506" y="208" class="copy">reconcile-first • manual-only</text><text x="506" y="230" class="copy">Compare intended vs observed</text><text x="506" y="248" class="copy">assign fault domain and owner</text><text x="506" y="266" class="copy">assess deadline/customer exposure</text>
    <path d="M704 180 H750" class="path"/><polygon points="750,180 740,174 740,186" class="arrow"/>
    <rect x="752" y="132" width="294" height="96" rx="9" class="done"/><text x="770" y="159" class="title">Safe recovery path</text><text x="770" y="180" class="copy">Resume/retry/replay using stable identity</text><text x="770" y="198" class="copy">validate external and customer outcome</text><text x="770" y="216" class="copy">communicate and close with evidence</text>
    <path d="M704 252 H750 V329" class="warn"/><polygon points="750,329 744,319 756,319" class="arrow-a"/>
    <rect x="752" y="331" width="294" height="104" rx="9" class="fault"/><text x="770" y="358" class="title">Ambiguous / unsafe / material incident</text><text x="770" y="379" class="copy">Owned case • incident command • partner escalation</text><text x="770" y="397" class="copy">manual approval or controlled suspension</text><text x="770" y="415" class="copy">revalidate readiness before resumption</text>
    <path d="M899 331 V238" class="alert"/><polygon points="899,238 893,248 905,248" class="arrow-r"/>
    <rect x="262" y="389" width="442" height="76" rx="9" class="external"/><text x="280" y="416" class="title">Continuity rail</text><text x="280" y="437" class="copy">Historical invoices, reconciliation, evidence access and required reporting continue</text><text x="280" y="454" class="copy">even when new affected traffic is degraded, suspended or switched.</text>
    <path d="M450 277 V381" class="handoff"/><polygon points="450,381 444,371 456,371" class="arrow-g"/>
  </svg>
  <div class="notes"><div class="note"><strong>Safety before automation</strong>Retry is allowed only by the approved operation class.</div><div class="note"><strong>One accountable case</strong>Sage and partner actions share correlation, owner, customer impact and evidence.</div><div class="note"><strong>Degrade narrowly</strong>Protect historical lifecycle and unaffected routes while containing the failed scope.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors and operating responsibilities

| Actor | Operational responsibility |
|---|---|
| Sage product support | Customer communication, first diagnosis and product-context evidence |
| Sage platform operations | Shared health, queues, reconciliation, safe recovery and incident coordination |
| Legal private-platform operator | Operator-edge availability, interconnection, BCP and evidence |
| Underlying partner | Contracted restoration, telemetry, evidence and escalation where applicable |
| Sage engineering/on-call | Component diagnosis, repair, controlled deployment and problem management |
| Security/privacy | Security incident coordination and restrictions on operational evidence/actions |
| Local compliance/product | Deadline/rule interpretation, customer priority and regulatory escalation |
| Public/counterparty platform | External state/evidence and incident coordination through approved channels |

## Operational scenarios

| ID | Trigger | Expected operational outcome | Continuity rule |
|---|---|---|---|
| S1 | Provider unavailable before submission | Queue/back off according to safety and capacity policy | No duplicate; customer sees delayed state |
| S2 | Timeout after invoice/public-copy mutation | Mark only affected leg outcome unknown and reconcile | Completed legs are not repeated |
| S3 | Internal persistence fails after external success | Recover from correlation and external evidence | Do not create a second invoice/leg |
| S4 | Entry-point intent differs from observed state | Block activation/new unsafe routing and open reconciliation case | Last known safe route remains |
| S5 | Lifecycle backlog approaches reporting deadline | Prioritise by approved deadline/risk policy and escalate capacity | Source events/history remain durable |
| S6 | Counterparty/public outage affects one route | Degrade that route/scope, preserve unaffected routes | Historical and reconciliation work continues |
| S7 | Partner cannot supply incident evidence | Escalate contractual control failure and restrict/suspend affected service | Sage retains customer communication ownership |
| S8 | Disaster or regional service loss | Invoke approved BCP/DR and validate data/external state before resumption | Recovery cannot assume external mutations failed |
| S9 | Customer switches provider during incident | Freeze conflicting mutations and coordinate transition case | Invoice-origin lifecycle remains on historical route |

## Business and operational rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | An external mutation times out after transmission | Treat as outcome unknown; reconcile before repeating | Confirmed shared resilience principle |
| BR2 | Multiple delivery/reporting legs exist | Track and recover each leg independently | PRD-SEI-223/224 |
| BR3 | Control/route is degraded | Stop only affected unsafe new activity; retain safe read, history and reconciliation where possible | Proposed safety rule |
| BR4 | Manual recovery is proposed | Require authorised runbook action, safety precondition, correlation, reason and audit | Proposed control |
| BR5 | Sage presents the proposition | Sage owns coherent customer communication even when a partner restores the service | ADR-SEI-001 accountability principle |
| BR6 | Partner/public evidence is stale or unavailable | Do not present assumed external state as confirmed | Proposed evidence rule |
| BR7 | Historical invoice requires action after route change | Use its immutable original network context and approved credentials/access | Confirmed continuity principle |
| BR8 | Support/availability target is needed | Approve it through legal, operations and risk review; do not infer a target from regulatory wording | PRD-SEI-221/open interpretation |
| BR9 | Incident recovery appears complete | Validate customer outcome, backlog, reconciliations and external state before closure | Proposed control |
| BR10 | Critical readiness/security control fails | Enter controlled suspension/degradation and require re-approval before resumption | PRD-SEI-221/226 |

## Research and evidence register

| Source | Finding | Confidence/limitation | Operational impact |
|---|---|---|---|
| RD 238/2026 Article 13 | Private platform requires BCP appropriate to volume/criticality, service availability and support resources available at all times | Primary regulation; measurable service model requires legal/operations approval | BCP, staffing, service objectives and evidence gates |
| RD 238/2026 Articles 8–10 | Interconnection queue/process, public bridging and time-bound lifecycle communication create operational cases/deadlines | Primary regulation; detailed interfaces open | Queue ownership, test-bank support, deadline monitoring |
| PRD-SEI-203 | Shared idempotency, outcome-unknown, reconciliation and operational case model | Product intent; implementation fitness unassessed | Reuse/extend through FP-SEI-001 |
| PRD-SEI-221 | Readiness, suspension, ongoing assurance and supplier control | Discovery PRD | Production and resumption gates |
| ADR-SEI-001 | Sage/partner accountability must be explicit | Proposed decision framework | Incident command, evidence and contract model |

## Proposed operational model

### Fault domains

`CUSTOMER_CONFIGURATION`, `SAGE_PRODUCT`, `SAGE_SHARED_PLATFORM`, `SAGE_OPERATOR_EDGE`, `PARTNER_OPERATOR`, `PUBLIC_SOLUTION`, `COUNTERPARTY_PLATFORM`, `NETWORK_TRUST`, `UNKNOWN`.

Fault domain is an observation for ownership/routing; it must not conceal shared accountability or change invoice history.

### Operation safety classes

| Class | Meaning | Permitted automation |
|---|---|---|
| `READ_SAFE` | Non-mutating and safe to repeat within limits | Controlled retry/backoff |
| `IDEMPOTENT_MUTATION` | Stable external idempotency proves repeats cannot duplicate effect | Resume/retry with same logical identity |
| `RECONCILE_FIRST` | Mutation may have occurred and external query/evidence is available | Query/compare before mutation |
| `MANUAL_ONLY` | No proven idempotency/query or consequence is high risk | Controlled case and authorised action |
| `PROHIBITED` | Action would violate lifecycle, authority or safety rules | No execution |

### Operational case record

| Area | Required information |
|---|---|
| Identity | Case, legal entity, invoice/route/operation correlation and environment |
| State | Intended, observed, evidence source/time and discrepancy |
| Impact | Customers/entities/routes, invoice count, deadlines and data/security exposure |
| Safety | Operation class, safe/unsafe actions, blocking condition and rollback option |
| Ownership | Sage lead, component/partner owner, escalation and incident link |
| Evidence | Redacted requests/references, timestamps, state observations and audit |
| Resolution | Action, approval, validation, customer communication and closure evidence |

### Case lifecycle

`DETECTED → TRIAGED → CONTAINED → RECONCILING/RECOVERING → VALIDATING → RESOLVED → CLOSED`

Branches: `WAITING_EXTERNAL`, `MANUAL_APPROVAL`, `SUSPENDED`, `KNOWN_LIMITATION`, `PROBLEM_MANAGEMENT`.

## Detailed journeys

### J1 — Detect and triage degradation

1. Health, backlog, discrepancy, deadline or support signal triggers a correlated alert.
2. Platform identifies affected operator, route, direction, leg, cohort and customer outcomes.
3. Unsafe new mutations are contained at the narrowest reliable scope.
4. A case is created with intended/observed state, evidence freshness and preliminary fault domain.
5. The case receives an accountable Sage owner and any partner escalation.

### J2 — Reconcile an outcome-unknown mutation

1. A mutating operation times out after transmission.
2. The operation/leg becomes `OUTCOME_UNKNOWN`; duplicates are prevented.
3. Reconciliation queries or obtains external evidence using stable correlation.
4. If success is confirmed, Sage persists/repairs internal state; if absent and safe, the same logical mutation resumes.
5. Unresolved/high-risk cases require authorised manual handling and customer-safe messaging.

### J3 — Recover a partial multi-leg failure

1. Recipient delivery succeeds while public-copy or lifecycle reporting fails.
2. Completed leg evidence is frozen and excluded from retry.
3. Failed/unknown leg is handled according to its safety class and deadline.
4. Derived customer state shows partial progress without claiming end-to-end completion.
5. Case closes only after every required leg is complete, terminally resolved or explicitly accepted as a known exception.

### J4 — Coordinate a partner incident

1. Sage detects customer impact or receives partner notification.
2. Sage incident lead establishes shared severity, scope, timestamps, evidence and update cadence under the approved contract.
3. Partner restores its responsibility; Sage protects queues/routes and owns customer communication.
4. Both parties reconcile external/internal state and backlog before resumption.
5. Post-incident review records control, contract, runbook and product improvements.

### J5 — Invoke BCP/DR

1. Approved trigger invokes continuity/failover for a defined service boundary.
2. New work is queued, rerouted or suspended only under pre-approved rules.
3. Recovery restores durable data and establishes external state for in-flight operations.
4. Reconciliation and backlog drain occur under capacity/deadline controls.
5. Service resumes after readiness/security validation and recorded approval.

### J6 — Continue historical work during switch/suspension

1. New activity moves or stops for an affected route.
2. Historical invoice obligations are identified by original network context.
3. Required credentials/access remain constrained to those operations.
4. Status, payment, reconciliation, read and evidence actions continue where required.
5. Access is removed only after the approved continuity/retention gate.

## Functional requirements

### Observability and health

| ID | Requirement |
|---|---|
| FR1 | Correlate health and operations across legal entity, invoice, route, connection, exchange leg, lifecycle obligation, external reference and environment. |
| FR2 | Expose intended and observed state with evidence source, timestamp and freshness. |
| FR3 | Monitor availability, errors, latency, queues, age, capacity, deadlines, control expiry and reconciliation outcomes by route/operator. |
| FR4 | Distinguish customer, Sage, partner, public, counterparty, trust/network and unknown fault domains. |
| FR5 | Alert on customer/business outcomes and deadline risk, not only infrastructure thresholds. |

### Cases and recovery

| ID | Requirement |
|---|---|
| FR6 | Create/deduplicate operational cases using stable correlation and affected outcome. |
| FR7 | Assign every case one accountable Sage owner, responsible technical/partner owners and escalation state. |
| FR8 | Store operation safety class and permitted actions before automated/manual recovery. |
| FR9 | Reconcile every outcome-unknown mutation before unsafe retransmission. |
| FR10 | Recover each multi-leg operation independently without repeating completed legs. |
| FR11 | Prevent concurrent recovery actions from producing conflicting route/invoice/lifecycle state. |
| FR12 | Permit manual action only through approved role, runbook, precondition, reason, correlation and audit. |
| FR13 | Validate external/customer outcome and backlog before resolving/closing a case. |

### Degradation, continuity and incident command

| ID | Requirement |
|---|---|
| FR14 | Contain degradation by operator, environment, product/cohort, direction, route, capability or event type. |
| FR15 | Preserve safe read, historical lifecycle, evidence and reconciliation capabilities during degradation where technically/legal possible. |
| FR16 | Provide controlled queue, backpressure, prioritisation and drain behaviour using approved business/deadline rules. |
| FR17 | Maintain incident command, partner/public escalation, customer communication and decision audit for material events. |
| FR18 | Invoke controlled suspension when critical readiness/security controls fail and require revalidation before resumption. |
| FR19 | Maintain and exercise BCP/DR for the scoped service and volume/criticality model. |
| FR20 | Preserve historical route credentials/access only for approved continuity operations and revoke when no longer required. |

### Support and governance

| ID | Requirement |
|---|---|
| FR21 | Provide support with customer-safe status, affected scope, expected action, last evidence and escalation without exposing secrets/content unnecessarily. |
| FR22 | Maintain versioned runbooks, ownership, service catalogue, escalation contacts and known limitations. |
| FR23 | Provide partner-control evidence, telemetry and action rights required by the selected accountability model. |
| FR24 | Produce post-incident/problem records and track corrective actions to closure. |
| FR25 | Preserve complete audit for alert, case, evidence, action, approval, communication and closure. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Define service objectives, support coverage, RTO/RPO, capacity and escalation only from approved legal/risk/volume analysis. |
| NFR2 | Make operational control available through redundant, access-controlled paths appropriate to the service criticality. |
| NFR3 | Protect invoice/identity/evidence content through minimisation, encryption, masking and least privilege. |
| NFR4 | Ensure monitoring and case data are tenant/environment isolated and historically reproducible. |
| NFR5 | Sustain backlog/drain performance under approved peak, partner outage and recovery scenarios. |
| NFR6 | Retain operational/audit evidence for approved periods and prevent support exports from containing secrets. |
| NFR7 | Provide accessible customer messaging and consistent status semantics across Sage products. |
| NFR8 | Version safety classes, runbooks, thresholds and reconciliation logic with controlled rollout/rollback. |

## Failure and recovery matrix

| Failure | Required response |
|---|---|
| Alert without correlation | Enrich or create diagnostic case; do not mutate blindly |
| Provider/public unavailable before mutation | Queue/backoff within limits; expose delay |
| Timeout after mutation | Outcome unknown; reconcile first |
| Internal success/external unknown mismatch | Preserve both observations; block unsafe state advancement |
| Internal persistence fails after external success | Rebuild from correlation/external evidence |
| Duplicate/out-of-order event | Dedupe/order; retain provenance |
| Backlog exceeds safe headroom | Apply approved prioritisation/degradation and capacity escalation |
| Partner evidence unavailable | Invoke contract escalation; restrict/suspend affected operation if unsafe |
| Operator credential/control expires | Stop affected mutations and enter readiness/security recovery |
| DR restores stale internal state | Reconcile every in-flight boundary before traffic resumes |
| Manual action fails midway | Record partial outcome and reclassify/reconcile before further action |
| Route switches during incident | Serialise transition/recovery and preserve invoice-origin context |

## Acceptance criteria

- Given a timeout after a private invoice submission, when operations reviews the case, then intended/observed state, safety class, correlation, affected customer and safe next action are visible before retry.
- Given private delivery succeeds and public-copy reporting fails, when recovery runs, then the completed private leg is not repeated.
- Given an outage affects one operator route, when degradation is activated, then unaffected routes and required historical lifecycle remain available where safe.
- Given a partner-led incident, when customer impact occurs, then one Sage incident owner coordinates evidence, customer communication and recovery validation.
- Given a manual reconcile/replay action, when it is invoked, then permission, runbook, precondition, reason, correlation and result are auditable.
- Given DR restores service, when traffic is considered for resumption, then in-flight external outcomes and backlog are reconciled and readiness/security approval is recorded.
- Given a customer has switched provider, when an old invoice requires payment/status reporting, then operations can continue it through the historical network context without changing the new route.

## Measures

| Measure | Purpose | Owner |
|---|---|---|
| Customer-impacting availability by route/capability | Service outcome | Operations/product |
| Outcome-unknown cases and age | Reconciliation health | Operations |
| Backlog/headroom and deadline exposure | Capacity/compliance risk | Engineering/operations |
| Detection, ownership, containment and recovery times | Incident effectiveness | Operations |
| Repeat/duplicate mutation prevented | Safety effectiveness | Engineering/QA |
| Cases reopened after closure | Recovery validation quality | Operations |
| Historical-route lifecycle success | Transition continuity | Product/operations |
| Partner evidence/escalation failures | Supplier-control health | Supplier management |
| BCP/DR exercises passed | Continuity evidence | Operator/operations |

## Rollout and operational gates

| Gate | Required evidence |
|---|---|
| Discovery | Named operator/support owners, service boundaries, volume/deadline model and legal support interpretation |
| Design | Telemetry, safety classes, case model, runbooks, degradation, BCP and partner responsibility approved |
| Sandbox | Retry, unknown outcome, persistence split-brain, duplicate, concurrency and manual-action tests pass |
| Load/resilience | Peak, outage, backlog, drain, failover and reconciliation scenarios pass approved criteria |
| Pilot | Staffing/escalation, dashboards, communications, kill criteria and partner support pass PRD-SEI-221 |
| Production | BCP/DR exercise, security approval, on-call/support coverage and operational acceptance complete |
| Ongoing | Incidents, control expiry, capacity, partner performance and exercises trigger reassessment |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Retry causes duplicate legal/business effect | Operation safety classes and reconciliation-first recovery |
| Infrastructure health masks customer failure | Outcome, queue and deadline-based observability |
| Partner accountability becomes a support gap | Contracted telemetry/action/evidence and Sage incident leadership |
| Degradation stops all customer value | Narrow containment and continuity rail |
| BCP restores inconsistent state | External-state reconciliation before resumption |
| Manual recovery creates hidden mutation | Restricted runbooks and immutable audit |
| Support commitment is undercosted | Approve measurable model after legal/risk/volume analysis |

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Hypothesis |
|---|---|---|---|---|
| What measurable service/support model satisfies “available at all times”? | Staffing, contract and cost | Legal/operations | Pilot/production | Formal interpretation required |
| Which Sage team is incident commander and service owner? | Eliminates ownership gaps | Engineering/operations leadership | Design | One Sage lead regardless of operator route |
| What volumes, peaks and deadline headroom apply? | Capacity and prioritisation | Product/data/local team | Load gate | Baseline required |
| Which external operations support query/idempotency? | Recovery safety | Public/operator technical owners | Sandbox/pilot | Classify per operation from evidence |
| What partner telemetry and recovery rights are mandatory? | Sage customer accountability | Legal/procurement/operations | Contract/pilot | Full outcome evidence and escalation required |
| Which functions remain available during suspension? | Continuity/customer promise | Product/legal/operations | Design | History/reconciliation preserved where safe |
| What RTO/RPO and support targets are approved? | Architecture/staffing | Risk/product/operations | Production | Do not invent before analysis |
| How are regulatory deadlines prioritised against commercial traffic? | Queue fairness/compliance | Local compliance/product | Design | Approved policy recorded by event/obligation |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 operations, resilience, support and reconciliation PRD | PRD-SEI-203/210/221–224 and RD 238/2026 |
