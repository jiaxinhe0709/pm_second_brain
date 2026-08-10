---
id: ADR-SEI-001
title: Decision — Phase 3 Delivery Model and Accountability
type: decision
status: proposed
owner: TBD
created: 2026-08-10
updated: 2026-08-10
related:
  - PRD-SEI-210
  - FP-SEI-001
  - PRD-SEI-221
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: ""
  title: Decision — Delivery Model and Accountability
  layout: two_left_sidebar
  toc: true
---

# Decision — Phase 3 Delivery Model and Accountability

## Decision status

**Proposed — decision not yet made.**

This record defines how Sage will choose between building, white-labelling, forming an accountable alliance, acquiring capability, or adopting a deliberate hybrid for the Spain private-platform proposition. It does not approve a route.

The decision must identify the named private-platform operator and allocate customer, legal, operational, security, data, support and exit accountability. “Powered by” branding or technical integration alone is not a delivery model.

## Context

Phase 1 provides a public-platform route. Phase 2 integrates customer-selected private providers. Phase 3 proposes a Sage-branded private-platform option while retaining public and existing-provider choice.

Real Decreto 238/2026 makes this an operator-accountability decision. A qualifying private platform must participate in the Spanish system, support admitted structured syntaxes and transformation, interconnect, connect with the public solution, maintain continuity and support, and satisfy applicable trust, security and data duties. Some implementation detail and effective timing remain dependent on the ministerial order for the public solution.

Sage has reusable Phase 1/2 product and platform concepts, but FP-SEI-001 must verify the real implementation and gaps. A partner may provide faster access to regulated capability, but it also introduces contractual, operational, evidence and exit dependencies. A build route offers control but requires Sage to establish and sustain operator capability. Acquisition changes ownership but does not automatically remove integration, control or migration risk.

## Decision to make

Select the Phase 3 delivery model and named accountable entities for discovery, pilot and production:

- **Build:** a Sage legal entity operates the private platform using Sage-owned capability.
- **White-label:** a partner operates material private-platform capability behind a Sage-branded customer experience.
- **Accountable alliance:** Sage and one or more partners retain visible roles under a coordinated proposition and operating model.
- **Acquisition:** Sage acquires an operator or material platform capability and integrates it into the target model.
- **Hybrid:** Sage owns selected platform/control capabilities and sources explicitly bounded operator capabilities.

A hybrid is a decision only when each boundary and owner is explicit. It must not be used as a label for unresolved responsibility.

## Non-negotiable outcomes

Any route must:

1. Preserve the free public-platform route and existing-provider route as valid customer choices.
2. Name the legal private-platform operator and customer-contracting entity.
3. Provide one explainable Sage customer experience for onboarding, exchange, status, failure and support.
4. Preserve invoice-origin context and historical lifecycle through route, partner or operating-model change.
5. Meet the readiness controls and evidence gates in PRD-SEI-221 before pilot or production.
6. Use Phase 1/2 capability where FP-SEI-001 proves fitness, without creating parallel invoice truth.
7. Give Sage sufficient operational evidence and action to meet its customer-facing accountability.
8. Include data portability, service continuity and an executable exit path before launch.
9. Separate regulated exchange capability from optional value-added services and pricing.
10. Keep country/operator behaviour behind product-neutral platform boundaries where feasible.

## Decision criteria

Weights and thresholds must be approved by the decision forum; none are invented here.

| Criterion | Evidence required | Why it matters |
|---|---|---|
| Regulatory accountability | Named operator, legal interpretation, control map, external validation path | Prevents a brand/contract model that cannot operate lawfully |
| Time to credible evidence | Dated plan to sandbox, interconnection test, pilot and production evidence | Measures readiness, not presentation-layer speed |
| Customer experience/control | End-to-end journeys, product contract, exception and support ownership | Sage remains accountable for the proposition it sells |
| Phase 1/2 reuse | FP-SEI-001 approved classifications, gaps and costs | Avoids duplication and false reuse assumptions |
| Security/privacy/data | Trust boundary, certificates, data roles, residency, access, incident and audit | Material external and regulated exposure |
| Operational resilience | BCP, observability, reconciliation, support, incident command and recovery rights | Platform faults affect compliance and customer cash flow |
| Interoperability/coverage | Formats, transformation, public connection, entry point and platform interconnection | Core operator outcome, not an optional feature |
| Economics | Investment, run cost, cost-to-serve, partner fees, pricing and downside sensitivity | Tests sustainable value rather than strategic assertion |
| Scalability and extensibility | Capacity evidence, Sage product coverage and country-specific isolation | Protects delivery and future change |
| Exit and portability | Data/evidence export, transition assistance, licence/IP rights and tested replacement path | Prevents customer harm and partner lock-in |

## Option analysis

| Option | Potential advantages | Material risks/constraints | Evidence needed before selection |
|---|---|---|---|
| Build | Maximum control of roadmap, data and operator experience; direct reuse of fit Sage capability | Longest path to operator maturity; security, interconnection, BCP and support obligations sit with Sage; unknown investment | Capability gap estimate, legal entity, certification/test path, capacity and 24/7-style operating model interpretation |
| White-label | Potentially faster access to existing operator capability and network | Sage brand may mask partner accountability; evidence/action limitations; product coupling; margin and exit risk | Operator status, API/coverage evidence, contract, audit rights, SLA, data roles, incident model, roadmap influence and exit test |
| Accountable alliance | Roles can remain visible; combines Sage product reach with specialist operation | Split ownership can confuse customers and incidents; coordination cost; inconsistent incentives | Joint responsibility matrix, customer contract, support command, evidence exchange, commercial and termination model |
| Acquisition | Brings people, IP, customers and possibly operator experience under Sage control | Due diligence, integration, legacy architecture, concentration and regulatory continuity risks | Operator/control due diligence, technical fit, liabilities, integration/retention plan, economics and transition approval |
| Deliberate hybrid | Allows Sage to own experience/data/control while sourcing bounded specialist services | Boundary complexity; duplicated controls; “hybrid” can hide indecision | Component-by-component responsibility, shared truth model, failure ownership, commercial dependencies and replacement tests |

## Required accountability matrix

The final decision must replace `TBD` with a legal entity or contracted operator and distinguish **accountable**, **responsible**, **consulted** and **informed** roles.

| Outcome/control | Sage proposition owner | Named operator/partner | Sage product/platform | Decision required |
|---|---|---|---|---|
| Customer proposition and eligibility | Accountable | Consulted | Responsible for product experience | Contracting Sage entity |
| Customer authority and route choice | Accountable | Evidence recipient | Responsible for capture/audit | Consent form and retention |
| Operator registration/readiness | Informed or accountable as prime | Responsible/accountable depending on route | Supplies evidence integration | Named legal operator |
| Entry-point publication and lookup | Customer-facing accountable | Operational responsibility may be delegated | Stores observed state | Authoritative registry/lookup |
| Invoice ingress/egress | Customer-facing accountable | Route-dependent responsibility | Orchestrates canonical lifecycle | Technical and failure boundary |
| Format transformation/signature | Accountable for outcome | May perform | Validates and records provenance | Ownership and evidence contract |
| Public faithful copy | Accountable for customer outcome | May transmit | Correlates and reconciles | Submission authority and proof |
| Private-platform interconnection | Accountable for proposition | Operator responsible | Exposes cases/telemetry | Request/test/activation ownership |
| Lifecycle and payment status | Accountable for coherent customer view | Supplies/receives required events | Owns canonical mapping/history | Event authority/conflict rules |
| Monitoring/reconciliation | Accountable | Supplies observability/action | Operates shared cases | Tool access and safe actions |
| Incident and customer support | Accountable for customer communication | Escalation and restoration duties | Diagnosis/runbook responsibility | Incident commander and severity model |
| Security/privacy/data | Sage role must be explicit | Partner role must be explicit | Implements shared controls | Controller/processor and breach duties |
| Audit/regulatory evidence | Accountable for availability to reviewers | Must produce/retain contracted evidence | Correlates evidence | Retention/access/export |
| Partner/model exit | Accountable | Transition assistance | Migration and continuity | Tested exit plan and funding |

## Working hypothesis

A partner-enabled or hybrid route may provide the fastest path to external operator evidence, while a Sage-controlled experience, canonical lifecycle, routing, audit and operations boundary may preserve product value and optionality.

This is a **hypothesis for evidence collection**, not the decision. It must be rejected if the partner cannot provide the required coverage, operational evidence, customer control, economics or executable exit path. A build route must likewise be rejected or deferred if Sage cannot evidence operator readiness within an approved investment and risk envelope.

## Decision process and gates

| Gate | Evidence | Decision/output |
|---|---|---|
| D0 — Forum and authority | Executive sponsor, product, engineering, legal, compliance, security, operations, commercial and finance representatives | Named decision owner and approvers |
| D1 — Outcome baseline | Approved Phase 3 customer proposition, launch scope and non-negotiables | Comparable requirement baseline |
| D2 — Capability evidence | FP-SEI-001 inventory, fitness results, gaps and costs | Internal build/reuse baseline |
| D3 — Market/partner evidence | Structured RFI/due diligence against the same criteria | Evidence-backed external options |
| D4 — Readiness feasibility | PRD-SEI-221 control mapping and external validation route | Feasible legal/operational models |
| D5 — Commercial comparison | Total cost, cost-to-serve, revenue assumptions, sensitivities and exit cost | Approved business case |
| D6 — Decision | Scored evidence, dissent, conditions and selected responsibility matrix | Approved ADR revision |
| D7 — Contract/design gate | Signed controls, architecture boundaries, pilot/exit plan | Authority to implement/pilot |

## Evidence comparison rules

- Compare every option against the same launch scope and mandatory outcomes.
- Separate vendor claims, demonstrated sandbox behaviour, contractual commitments and independently verified controls.
- Include Sage integration, operations, compliance and exit costs in partner options.
- Include opportunity cost, staffing, certification/testing and sustained support in build options.
- Record ranges and confidence where estimates are uncertain; do not use false precision.
- Treat missing legal authority, operator evidence, security approval or exit rights as blockers regardless of aggregate score.
- Record dissent and conditions rather than averaging away a material risk.

## Shortcuts explicitly rejected

| Shortcut | Why it is rejected |
|---|---|
| “Sage-branded” without naming the operator | Branding does not assign regulated or operational accountability |
| UI fronting without failure and evidence access | Sage cannot support or explain outcomes it cannot observe |
| Choosing a partner from feature ticks alone | Feature lists do not prove Spain scope, contract, safety or operational maturity |
| Treating Phase 1/2 PRDs as implementation proof | Product intent is not deployed capability evidence |
| Partner integration without portability/exit rights | Creates unacceptable continuity and customer-lock-in exposure |
| Build because internal concepts look similar | Operator edge, interconnection and service accountability remain distinct gaps |
| Hybrid without component-level ownership | Hides rather than resolves responsibility |

## Consequences to record with the final decision

The approved revision must document:

- selected option and rejected alternatives;
- named legal and customer-contracting entities;
- final accountability matrix;
- capabilities reused, extended, wrapped or sourced;
- data/control boundaries and authoritative records;
- operational and customer-support model;
- regulatory validation and evidence plan;
- investment, run cost, commercial model and sensitivity;
- partner/IP/licensing constraints;
- migration, rollout, rollback and kill conditions;
- exit triggers, data/evidence portability and replacement path;
- review date and triggers for reconsideration.

## Acceptance conditions for a final decision

- Given each viable option, reviewers can trace claims to current evidence and distinguish demonstrated, contracted, proposed and unknown capabilities.
- Given the selected route, every accountability row has one named accountable party and an operationally responsible party.
- Given an invoice failure at any external boundary, Sage support can identify the fault domain, customer message, evidence owner and safe next action.
- Given a route or partner change, existing invoices retain their original network context and required lifecycle access.
- Given partner termination or a failed build readiness gate, the approved exit/rollback path protects customer access and legal evidence.
- Given a missing ministerial-order detail, the decision records the dependency and avoids an irreversible technical assumption.
- Given the selected route's business case, costs include integration, compliance, operations and exit—not only licence or build expenditure.

## Open decisions

| Decision | Owner | Blocks | Evidence needed |
|---|---|---|---|
| Which Sage entity owns the proposition and customer contract? | Legal/commercial leadership | D4/D6 | Entity, permissions, liability and tax analysis |
| Does Sage intend to be the legal operator or accountable prime contractor? | Executive/legal sponsor | D4/D6 | Regulatory interpretation and risk appetite |
| Which customer segment and Sage products form the launch cohort? | Product leadership | D1 | Segment need, product readiness and volume baseline |
| Which capabilities must Sage own strategically? | Product/architecture | D2/D6 | FP-SEI-001 evidence and platform strategy |
| Which partner candidates meet the same evidence baseline? | Partnerships/procurement | D3 | RFI, demonstrations, references and due diligence |
| What support availability and operating model satisfy the regulation? | Legal/operations | D4 | Formal interpretation, supplier coverage and cost |
| What commercial outcome justifies Phase 3? | Commercial/finance | D5 | Pricing, adoption, cost-to-serve and downside sensitivity |
| What exit rights are mandatory? | Legal/product/operations | D3/D7 | Portability, assistance, evidence, licences and transition time |

## Review triggers

Re-open this decision if:

- the ministerial order or official technical specifications materially change the required boundary;
- FP-SEI-001 disproves a material reuse assumption;
- the selected operator loses eligibility, coverage or required controls;
- a material security, availability or evidence failure occurs;
- economics move beyond the approved sensitivity range;
- Sage changes the target segment, countries or value proposition;
- the partner contract approaches termination or change of control.

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial proposed decision framework for the Phase 3 delivery model and accountability | PRD-SEI-210, FP-SEI-001 and official Spain regulatory sources |
