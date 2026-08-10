---
id: FP-SEI-001
title: Foundation — Existing Capability Reuse and Gap Assessment
type: feature-proposal
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-210
  - PRD-SEI-102
  - PRD-SEI-103
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
  - ADR-SEI-001
  - PRD-SEI-221
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: ""
  title: Foundation — Existing Capability Reuse and Gap Assessment
  layout: two_left_sidebar
  toc: true
---

# Foundation — Existing Capability Reuse and Gap Assessment

## Decision summary

Phase 3 should add a regulated private-platform operator edge to the shared Sage e-Invoicing platform; it should not create a second invoice platform beside the Phase 1 and Phase 2 capabilities.

This proposal defines how Sage will prove which existing capabilities can be reused, which require controlled extension, which should be wrapped behind a new boundary, and which must be built or sourced as new operator capability. It is an evidence-gathering and decision framework, not an assertion that capabilities described in existing PRDs are already implemented or fit for Phase 3.

> **Product principle:** Reuse an existing capability only when implementation evidence proves that its contract, controls, ownership and operational characteristics are fit for the Phase 3 outcome.

## Why this assessment is needed

Phase 1 describes public-platform submission and consultation. Phase 2 describes connection, routing, provider adapters, resilience and transitions. Phase 3 depends on many of the same business concepts, but it introduces a materially different external accountability boundary: Sage or a named partner must operate a private platform within the Spanish system.

Without a formal reuse assessment, Sage risks either:

- rebuilding identity, routing, invoice lifecycle and resilience in parallel;
- assuming that a PRD-level design is equivalent to a production capability;
- extending a component beyond its ownership, capacity, security or data model;
- embedding partner-specific behaviour in the common platform;
- creating two sources of truth for invoices, status or audit;
- underestimating new operator obligations because similar internal components exist.

The intended outcome is an approved capability map with evidence, accountable owners, gaps, dependencies and route recommendations suitable for the Phase 3 operating-model decision.

## Scope and non-goals

### In scope

- Inventory Phase 1 and Phase 2 capabilities relevant to Phase 3.
- Trace each candidate to its source PRD, implementation owner and evidence pack.
- Assess functional, operational, security, regulatory and scale fitness.
- Classify each candidate as reuse, extend, wrap, or build/source new.
- Identify Phase 3-only operator capabilities and their dependency on the delivery model.
- Produce decision-ready gaps and sequence them into delivery gates.

### Non-goals

- Selecting build, white-label, alliance or acquisition; see ADR-SEI-001.
- Approving a component based only on its appearance in a PRD or architecture diagram.
- Performing detailed code, security or capacity reviews inside this document.
- Replacing the operator-readiness control register in PRD-SEI-221.
- Committing a launch date, service level or implementation architecture.
- Migrating or changing any Phase 1 or Phase 2 route during discovery.

## Definitions

| Term | Meaning | Evidence threshold |
|---|---|---|
| Reuse unchanged | Use the existing owned contract and implementation without material behavioural change | Production implementation, owner, contract, controls and capacity are evidenced as fit |
| Extend | Add Phase 3 behaviour to the shared capability without creating a competing source of truth | Extension boundary, compatibility, migration and regression impact are approved |
| Wrap | Retain an existing or partner capability behind a Sage-controlled product-neutral contract | Boundary, observability, data ownership, failure behaviour and exit path are approved |
| Build/source new | Create or procure a capability not present or not fit in the current platform | Need, accountability, integration boundary and lifecycle are approved |
| Capability evidence | Verifiable implementation, contract, test, operational and ownership material | Evidence is current, accessible to reviewers and linked to a named owner |
| PRD evidence | Product intent documented in a managed PRD | Useful for discovery; insufficient by itself for a reuse approval |
| Operator edge | External regulated boundary used to receive, exchange, transform, sign/seal, interconnect and evidence private-platform activity | Readiness is governed by PRD-SEI-221 |

## Reuse decision visual

<!-- confluence-html-macro:start -->
<div class="p3fit-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3fit-visual *{box-sizing:border-box}.p3fit-visual h2{margin:0;color:#172b4d;font-size:18px}.p3fit-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3fit-visual svg{display:block;width:1080px;height:480px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3fit-visual .lane{fill:#f4f5f7;stroke:#dfe1e6}.p3fit-visual .evidence{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3fit-visual .gate{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3fit-visual .reuse{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3fit-visual .extend{fill:#eae6ff;stroke:#6554c0;stroke-width:1.5}.p3fit-visual .new{fill:#ffebe6;stroke:#ff5630;stroke-width:1.5}.p3fit-visual .title{fill:#172b4d;font-size:12px;font-weight:700}.p3fit-visual .copy{fill:#42526e;font-size:9.5px}.p3fit-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3fit-visual .path{fill:none;stroke:#7a869a;stroke-width:1.8}.p3fit-visual .arrow{fill:#7a869a}.p3fit-visual .notes{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;min-width:1080px;margin-top:12px}.p3fit-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3fit-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Evidence-gated Phase 3 reuse decision</h2>
  <p class="sub">Every candidate starts as an unproven hypothesis. The decision concerns the real implementation and operating contract—not the quality of the earlier PRD.</p>
  <svg viewBox="0 0 1080 480" role="img" aria-label="A candidate Phase 1 or Phase 2 capability is matched to a real implementation and evidence pack, assessed for functional, regulatory, operational, security and scale fitness, and then classified as reuse unchanged, extend shared capability, wrap behind a controlled boundary, or build or source new.">
    <text x="34" y="34" class="label">CANDIDATE</text><text x="260" y="34" class="label">PROVE</text><text x="510" y="34" class="label">ASSESS</text><text x="790" y="34" class="label">DECIDE AND CONTROL</text>
    <rect x="34" y="72" width="180" height="92" rx="9" class="lane"/><text x="52" y="99" class="title">Phase 1 / 2 capability</text><text x="52" y="121" class="copy">PRD intent and expected contract</text><text x="52" y="139" class="copy">are a starting hypothesis</text>
    <path d="M214 118 H250" class="path"/><polygon points="250,118 240,112 240,124" class="arrow"/>
    <rect x="252" y="62" width="208" height="112" rx="9" class="evidence"/><text x="270" y="89" class="title">Implementation evidence</text><text x="270" y="110" class="copy">Owner • service/repository • API</text><text x="270" y="128" class="copy">environments • tests • operations</text><text x="270" y="146" class="copy">security • limits • incidents</text>
    <path d="M460 118 H500" class="path"/><polygon points="500,118 490,112 490,124" class="arrow"/>
    <rect x="502" y="52" width="226" height="132" rx="9" class="gate"/><text x="520" y="79" class="title">Five fitness gates</text><text x="520" y="101" class="copy">1. Functional and data fit</text><text x="520" y="119" class="copy">2. Operator/regulatory fit</text><text x="520" y="137" class="copy">3. Security and privacy fit</text><text x="520" y="155" class="copy">4. Reliability, scale and support fit</text><text x="520" y="173" class="copy">5. Ownership, cost and exit fit</text>
    <path d="M728 118 H768" class="path"/><polygon points="768,118 758,112 758,124" class="arrow"/>
    <rect x="770" y="48" width="276" height="62" rx="8" class="reuse"/><text x="788" y="74" class="title">Reuse unchanged</text><text x="788" y="93" class="copy">All gates pass; preserve shared contract</text>
    <rect x="770" y="126" width="276" height="62" rx="8" class="extend"/><text x="788" y="152" class="title">Extend shared capability</text><text x="788" y="171" class="copy">Controlled gap; one source of truth remains</text>
    <rect x="770" y="204" width="276" height="62" rx="8" class="evidence"/><text x="788" y="230" class="title">Wrap behind Sage boundary</text><text x="788" y="249" class="copy">External capability; contract and exit controlled</text>
    <rect x="770" y="282" width="276" height="62" rx="8" class="new"/><text x="788" y="308" class="title">Build or source new</text><text x="788" y="327" class="copy">Capability absent or evidence shows material misfit</text>
    <path d="M615 184 V313 H760" class="path"/><polygon points="760,313 750,307 750,319" class="arrow"/>
    <rect x="252" y="260" width="476" height="98" rx="9" class="lane"/><text x="270" y="287" class="title">No evidence or disputed result</text><text x="270" y="309" class="copy">Remain unassessed; record the missing evidence, owner, impact and decision gate.</text><text x="270" y="329" class="copy">Do not convert uncertainty into an architecture commitment or delivery estimate.</text>
    <path d="M356 174 V252" class="path"/><polygon points="356,252 350,242 362,242" class="arrow"/>
    <rect x="252" y="390" width="794" height="54" rx="8" class="lane"/><text x="270" y="414" class="title">Approved output</text><text x="270" y="433" class="copy">Named owner + evidence links + decision record + gap backlog + dependencies + regression/exit controls + review date</text>
  </svg>
  <div class="notes"><div class="note"><strong>Reuse</strong>Evidence proves the current implementation fits.</div><div class="note"><strong>Extend</strong>Add behaviour to the shared capability without forking truth.</div><div class="note"><strong>Wrap</strong>Protect Sage contracts and operations from an external implementation.</div><div class="note"><strong>New</strong>Reserve for real operator gaps—not undocumented assumptions.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Assessment principles

| ID | Principle | Consequence |
|---|---|---|
| AP1 | One invoice lifecycle truth | A Phase 3 route must not create a parallel invoice or status record when a shared record can represent it |
| AP2 | Current configuration and historical context remain separate | Route or operator changes do not rewrite original provider, identifiers, syntax, signature evidence or status history |
| AP3 | Product-neutral core, country/operator-specific edge | Common contracts stay independent of one Spanish platform or commercial partner |
| AP4 | Evidence before reuse | A documented requirement is not proof of deployed capability, capacity or control effectiveness |
| AP5 | Extend before duplicate | Shared identity, routing, validation, lifecycle, resilience and audit should gain operator behaviour through explicit extensions |
| AP6 | Partner use requires an exit path | White-label or alliance capability must be replaceable without losing customer access, audit or historical continuity |
| AP7 | Regulatory fitness is separate from technical similarity | A technically reusable component may still fail operator-readiness controls |

## Preliminary capability inventory

The classification below is a discovery hypothesis. `Unassessed` means implementation evidence has not yet been attached to this proposal.

| Candidate capability | Source intent | Phase 3 use | Preliminary route | Evidence/maturity | Primary gap to prove |
|---|---|---|---|---|---|
| Legal entity and tenancy | PRD-SEI-102/103/202 | Identify the contracting and invoice parties consistently across routes | Reuse or extend | Unassessed | Multi-product ownership, operator entity and migration integrity |
| Authorisation and credential lifecycle | PRD-SEI-102/103/202 | Customer authority, connection secrets, operator certificates and seals | Extend | Unassessed | Certificate/seal custody, rotation, revocation and separation of duties |
| Canonical invoice model | PRD-SEI-103/202 | One product-neutral invoice representation | Extend | Unassessed | Coverage of admitted syntaxes without information loss |
| Validation packs | PRD-SEI-103/204–208 | Shared business and provider validation | Extend | Unassessed | Versioned Spanish rules, transformation validation and provenance |
| Public submission orchestration | PRD-SEI-103 | Public route and faithful-copy transmission | Extend | Unassessed | Operator copy semantics, evidence and unknown-outcome reconciliation |
| Public consultation scheduler | PRD-SEI-102 | Retrieve public inbound/status activity | Extend | Unassessed | Operator-scale checkpoints, event acceleration and tenancy fairness |
| Connection and readiness model | PRD-SEI-202 | Represent public, external provider and Sage operator connections | Extend | Unassessed | Operator accreditation, entry-point and interconnection readiness dimensions |
| Routing and transition | PRD-SEI-201/202 | Select route by direction/scope and preserve continuity | Reuse or extend | Unassessed | Sage-as-provider route type, coexistence and operating-model transition |
| Invoice network snapshot | PRD-SEI-201/202 | Preserve original route/provider/network facts | Reuse | Unassessed | Syntax, signature, copy and interconnection evidence fields |
| Lifecycle/status orchestration | PRD-SEI-102/103/201 | Map technical, business and payment events | Extend | Unassessed | Multi-platform fan-out, ordering, authority and conflict rules |
| Resilience and reconciliation | PRD-SEI-203 | Idempotency, retry, outcome-unknown and recovery | Reuse or extend | Unassessed | Operator-scale queues, partner fault isolation and regulatory evidence |
| Provider adapter framework | PRD-SEI-204–208 | Isolate provider-specific authentication and APIs | Reuse or wrap | Unassessed | Inbound platform-facing contract differs from customer/provider adapter role |
| Audit and operational cases | PRD-SEI-202/203 | Explain decisions and enable safe support action | Extend | Unassessed | Operator accountability, evidence retention and cross-party case ownership |

## Phase 3-only capability hypotheses

| Capability | Why it is not assumed to exist | Operating-model dependency |
|---|---|---|
| Operator registration/accreditation and governance | Phase 1/2 connect to other platforms; they do not establish Sage as an operator | Named operator and legal entity |
| Published customer entry point and open lookup | External reachability is an operator-facing service | May be Sage-built or partner-operated; Sage accountability must be explicit |
| External private-platform ingress/API | Provider adapters are outbound Sage integrations, not necessarily a public platform contract | Build, partner contract and security perimeter |
| Interconnection request, testing and activation | Requires platform-to-platform onboarding and evidence | Operator owns or contractually delegates the process |
| Full admitted-syntax transformation | Existing provider/public mappings do not prove lossless bidirectional coverage | Build versus partner capability |
| Operator signature/seal service | Customer/provider credentials are not automatically operator trust credentials | Legal operator and trust-service design |
| Faithful-copy orchestration and proof | Similar to public submission but has distinct operator origin, evidence and reconciliation rules | Operator/public technical specification |
| Platform-wide BCP and continuous support | Component resilience does not prove an operator service and support model | Sage, partner or joint responsibility |
| Commercial subscription, metering and exit | Earlier phases do not establish a Sage private-platform proposition | Delivery route and commercial decision |

## Evidence pack required per candidate

| Evidence area | Minimum discovery evidence | Decision question |
|---|---|---|
| Ownership | Product/service owner, engineering owner, support owner and funding route | Who can approve and sustain the extension? |
| Implementation | Repository/service, deployed environments, release status and consuming products | Does a real reusable implementation exist? |
| Contract | API/event/schema versions, compatibility policy and dependency map | Can Phase 3 use it without coupling to one product/provider? |
| Functional fit | Supported actors, directions, documents, states, operations and limits | Which Phase 3 scenarios pass without change? |
| Data fit | Identifiers, immutable context, retention, residency, migration and deletion | Can history remain complete and explainable? |
| Reliability | Idempotency, retry, unknown outcomes, reconciliation, throughput and failure tests | Does it remain safe at operator scale? |
| Security/privacy | Threat model, credentials, permissions, encryption, audit and approvals | Is the trust boundary fit for external operation? |
| Operations | Dashboards, alerts, runbooks, manual actions, incident history and escalation | Can operations distinguish and recover faults? |
| Regulatory | Control mapping and legal/compliance interpretation | Does technical fit satisfy operator obligations? |
| Commercial/exit | Run cost, licence/partner dependency, portability and termination behaviour | Is reuse economically sustainable and replaceable? |

## Assessment journeys

### J1 — Nominate and prove an existing capability

1. A capability owner is nominated against an inventory row.
2. The owner links the implementation, current contract, environments and consumers.
3. Product links the Phase 3 scenarios and requirements that need the capability.
4. Engineering, operations, security and compliance record evidence and gaps.
5. The candidate remains `unassessed` until the minimum evidence pack is complete.

**Expected result:** reviewers assess a real implementation, not a name shared by several documents.

### J2 — Approve reuse unchanged

1. All five fitness gates pass with no material contract or control change.
2. The owner confirms capacity, support and funding for Phase 3 demand.
3. Regression tests cover existing Phase 1/2 consumers and new Phase 3 consumers.
4. The decision, evidence and review date are recorded.

**Expected result:** Phase 3 consumes the existing contract without creating another source of truth.

### J3 — Approve a shared extension

1. Gaps are explicit and confined to an owned extension boundary.
2. The proposed change preserves existing consumers or includes an approved migration.
3. Data backfill, state transition, observability and rollback are defined.
4. Phase 1/2 regression and Phase 3 acceptance tests pass before activation.

**Expected result:** one shared capability gains Phase 3 behaviour safely.

### J4 — Wrap a partner or legacy capability

1. Sage defines a stable product-neutral contract and canonical status/error behaviour.
2. The wrapper exposes intended and observed state, correlation and safe recovery.
3. Customer data, audit ownership, partner outage and contract termination are designed.
4. An exit test proves that the underlying implementation can change without losing history.

**Expected result:** partner choice does not become an irreversible platform dependency.

### J5 — Evidence is missing or disputed

1. The reviewer records the disputed claim, required evidence, owner and decision impact.
2. The candidate remains unassessed; it is not estimated as reusable.
3. Where progress is necessary, a time-boxed hypothesis is labelled and isolated.
4. The production gate remains blocked until the evidence is resolved.

**Expected result:** uncertainty remains visible and does not silently become scope or architecture.

## Assessment requirements

| ID | Requirement |
|---|---|
| AR1 | Every candidate capability must have a unique inventory record linked to its source intent and implementation evidence. |
| AR2 | The assessment must distinguish PRD intent, implemented behaviour, deployed maturity and approved operator fitness. |
| AR3 | Every reuse decision must identify the accountable product, engineering and operational owners. |
| AR4 | Every candidate must be evaluated against functional/data, regulatory, security/privacy, reliability/operations and ownership/exit gates. |
| AR5 | A reuse or extension decision must show how Phase 1 and Phase 2 consumers remain compatible. |
| AR6 | An extension must define its new boundary, migration/backfill impact, failure behaviour, observability and rollback. |
| AR7 | A wrapped capability must expose a Sage-controlled contract, correlation, audit, error mapping, availability evidence and exit mechanism. |
| AR8 | A new-build/source recommendation must identify why reuse and extension were rejected with evidence. |
| AR9 | No option may introduce a second authoritative invoice, route, lifecycle or audit record without an approved architecture decision. |
| AR10 | Every decision must preserve invoice-origin network context across current-route or operating-model changes. |
| AR11 | Missing evidence must have an owner, requested artefact, due decision gate and documented impact. |
| AR12 | Reuse decisions must be reviewed when the implementation contract, operator model, regulation or critical dependency changes. |
| AR13 | Assessment evidence must exclude credentials, customer data and unauthorised confidential exports. |
| AR14 | The approved assessment must produce traceability from Phase 3 outcome to scenario, candidate, gap, decision and acceptance evidence. |

## Failure and safeguard matrix

| Failure | Exposure | Required safeguard |
|---|---|---|
| Capability exists only in a PRD | False reuse estimate | Keep unassessed until implementation evidence is linked |
| Two teams use the same capability name for different services | Wrong dependency/owner | Resolve canonical service and contract before classification |
| Shared extension breaks a Phase 1/2 consumer | Compliance or service regression | Compatibility analysis, consumer tests and controlled rollout |
| Partner wrapper hides an ambiguous external outcome | Duplicate invoice or contradictory status | Persist outcome-unknown state and reconcile before retry |
| Reused component lacks operator-scale capacity | Backlog, missed lifecycle or support failure | Capacity model, load evidence, backpressure and degradation plan |
| Operator evidence is held only by a partner | Audit and exit dependency | Contractual access, retention and export controls |
| Regulation changes after approval | Stale fitness decision | Evidence review trigger and controlled re-assessment |
| No owner accepts a gap | Hidden scope | Gap remains blocking; escalate through the Phase 3 governance forum |

## Outputs and decision gates

| Gate | Required output | Blocks |
|---|---|---|
| G0 — Inventory ready | Complete candidate list with source PRDs and named discovery owners | Reliable discovery estimate |
| G1 — Evidence ready | Minimum evidence pack per candidate; missing evidence explicitly owned | Reuse classification |
| G2 — Fit assessed | Five-gate result, gaps and preliminary route | Architecture and operating-model comparison |
| G3 — Decision approved | Decision record, implementation/backlog boundary and controls | Delivery planning |
| G4 — Regression/exit proven | Cross-phase tests, operational evidence and partner exit test where applicable | Pilot |

## Acceptance criteria

- Given a capability described in a Phase 1 PRD but without a linked implementation, when it is reviewed, then it remains `unassessed` and is not counted as reusable delivery capacity.
- Given an existing routing implementation that passes all five fitness gates, when reuse is approved, then Phase 3 represents Sage as an additional route/connection without creating a new authoritative routing store.
- Given a shared lifecycle extension, when a Phase 1 public invoice and a Phase 2 provider invoice are processed after deployment, then their existing status and historical-context behaviours continue to pass regression tests.
- Given a partner capability behind a Sage wrapper, when the partner times out after a mutation, then Sage records an ambiguous outcome and reconciles it before any unsafe retry.
- Given termination of a partner dependency, when the exit test is performed, then customer configuration, invoice history, audit evidence and an alternative operating path remain available as defined by the approved plan.
- Given an unresolved regulatory interpretation, when the candidate is otherwise technically fit, then it cannot pass the operator-regulatory gate until the designated decision owner approves the interpretation.

## Measures

Targets should be agreed after the inventory baseline exists.

| Measure | Why it matters | Target owner |
|---|---|---|
| Inventory coverage | Shows whether all Phase 3 dependencies have been assessed | Phase 3 product lead |
| Evidence completeness | Prevents PRD intent being mistaken for implementation | Architecture lead |
| Reuse/extend/new distribution | Informs investment without making reuse a success metric by itself | Product and engineering |
| Gaps with named owner and gate | Exposes hidden scope and accountability | Programme lead |
| Phase 1/2 regression coverage | Protects earlier phases | QA/engineering |
| Partner exit-test coverage | Reduces lock-in and continuity risk | Commercial/operations |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Reuse becomes a predetermined cost-saving target | Judge fitness against outcomes and controls; permit evidence-based new capability |
| Discovery stalls because owners or implementations are unclear | Use G0 as an explicit governance gate and escalate orphan capabilities |
| Teams optimise components but miss end-to-end operator accountability | Link every capability decision to PRD-SEI-221 readiness controls |
| Partner route appears faster because internal integration work is omitted | Compare wrapper, evidence, operations and exit costs in ADR-SEI-001 |
| Shared services become Spain-specific | Keep country rules and operator behaviour behind versioned boundaries |
| Multiple successor PRDs create ambiguity | Use permanent IDs and Git as canonical; keep one current Confluence page per topic |

## Open questions and consultation owners

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Which Phase 1/2 components are deployed, and in which environments? | Establishes whether reuse is real | Engineering leadership | G1 | Unknown |
| Who owns each shared capability and its Phase 3 funding? | Extensions require durable accountability | Product/engineering leadership | G2 | Reuse current owners where accepted |
| What are the forecast invoice/event volumes by Sage product and segment? | Capacity and cost fitness cannot be tested without demand | Product/commercial | G2/G3 | Baseline required |
| Can the current canonical model represent all admitted syntaxes without loss? | Determines transformation architecture | Architecture/local compliance | G3 | Extendable, unproven |
| Can existing operational tooling support an operator service across partner and public faults? | Determines support and reconciliation gaps | Operations | G3/G4 | Shared case model should be extended |
| Which evidence must Sage retain versus obtain on demand from a partner? | Affects audit, support and exit | Legal/security/operations | G3 | Sage must control customer-facing evidence access |
| Which technical obligations remain dependent on the ministerial order? | Prevents premature contracts and estimates | Local legal/compliance | Pilot/production | Maintain a live dependency register |

## Recommended next actions

1. Appoint a Phase 3 product lead and technical assessment lead.
2. Nominate an owner for every preliminary inventory row.
3. Run G0/G1 workshops with Phase 1 and Phase 2 service teams.
4. Feed evidence-backed reuse costs and gaps into ADR-SEI-001.
5. Map approved capability decisions to PRD-SEI-221 readiness controls.
6. Select one end-to-end reference journey for a thin-slice proof before a broad delivery commitment.

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 capability reuse and gap-assessment proposal | PRD-SEI-210 and Phase 1/2 managed PRDs |
