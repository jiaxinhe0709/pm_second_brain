---
id: PRD-SEI-229
title: Ireland E-Invoicing Compliance Pack
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-227
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "771496799"
  page_id: "866140021"
  title: 2.6 E-Invoicing Ireland
  layout: two_left_sidebar
  toc: true
---

# Ireland E-Invoicing Compliance Pack

## Decision summary

Define Ireland as a phased country pack on PRD-SEI-227. Phase One begins on 1 November 2028: Irish VAT-registered large corporates in Revenue's defined cohort issue EN 16931 e-invoices for domestic B2B transactions and report a subset of invoice data to Revenue, while all Irish businesses must be able to receive structured e-invoices.

The product must model invoice delivery and Revenue reporting as separate correlated obligations. It must not invent the transport network, detailed syntax/profile, reporting payload, timing, acknowledgement, correction, identity or lifecycle rules that Revenue has not yet published.

> **Country principle:** Build early around confirmed phase, scope and semantic requirements; activate delivery and reporting details only through approved official specifications.

## Parent relationship, outcome and readiness

| Area | Position |
|---|---|
| Parent PRD | PRD-SEI-227 — shared service and country-pack contract |
| Visual research | PRD-SEI-227 contains the consolidated source-diagram atlas; this child keeps only the Ireland-specific phased flow |
| Confluence position | Existing page `866140021`; preserve current parent `771496799` |
| Customer outcome | Irish businesses can receive structured invoices and in-scope issuers can deliver compliant invoices and report required data through normal Sage workflows. |
| Current phase | Regulatory/solution discovery ahead of 2028 Phase One |
| Readiness | **Discovery-ready**: official direction is strong, but technical specifications and product cohort/readiness evidence block delivery design. |

## Confirmed phase model

| Phase/date | Confirmed scope | Required capability | Open detail |
|---|---|---|---|
| Phase One — 2028-11-01 | VAT-registered large corporates managed by Revenue Large Corporates Division and established/fixed-established in Ireland issue for domestic B2B; all Irish businesses receive | EN 16931 structured invoice; issuer reports a relevant subset to Revenue | Syntax/profile, network/transport, report payload/timing/API, corrections, acknowledgements, exemptions |
| Phase Two — 2029-11 | Revenue's implementation publication says domestic obligation extends to all VAT-registered businesses engaged in intra-EU trade | Broader domestic issue/report readiness | Precise legal scope, detailed definition and technical standards require updated official confirmation |
| Phase Three — 2030-07-01 | EU ViDA cross-border B2B DRR based on mandatory e-invoicing | Intra-EU e-invoice/reporting compatibility | Final EU/national implementation artefacts and transition behaviour |

## Ireland phased-flow visual

<!-- confluence-html-macro:start -->
<div class="ie-pack" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .ie-pack *{box-sizing:border-box}.ie-pack h2{margin:0;color:#172b4d;font-size:18px}.ie-pack .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.ie-pack svg{display:block;width:1080px;height:560px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.ie-pack .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.ie-pack .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.ie-pack .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.ie-pack .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.ie-pack .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.ie-pack .title{fill:#172b4d;font-size:11px;font-weight:700}.ie-pack .copy{fill:#42526e;font-size:9px}.ie-pack .phase{fill:#172b4d;font-size:10px;font-weight:700;letter-spacing:.05em}.ie-pack .path{fill:none;stroke:#00875a;stroke-width:2}.ie-pack .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.ie-pack .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.ie-pack .path-warn{fill:none;stroke:#ff8b00;stroke-width:1.8;stroke-dasharray:6 4}.ie-pack .arrow{fill:#00875a}.ie-pack .arrow-g{fill:#6b778c}.ie-pack .arrow-r{fill:#de350b}.ie-pack .arrow-a{fill:#ff8b00}.ie-pack .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.ie-pack .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.ie-pack .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Phase One separates recipient delivery from Revenue reporting</h2>
  <p class="sub">Both obligations use one invoice context but have independent validation, correlation, acknowledgement and recovery. Later phases widen policy; they do not rewrite earlier evidence.</p>
  <svg viewBox="0 0 1080 560" role="img" aria-label="In Ireland Phase One, a large corporate Sage product submits domestic B2B invoice intent. The Ireland pack checks cohort and scope, validates an EN 16931 representation, then creates separate buyer-delivery and Revenue-reporting legs. Each leg records an independent outcome. Validation failure loops to the product. A timeout after a possible external mutation reconciles only the affected leg. A lower phased timeline shows November 2028 Phase One, November 2029 Phase Two and July 2030 ViDA Phase Three.">
    <text x="32" y="32" class="phase">PHASE ONE JOURNEY — 1 NOVEMBER 2028</text>
    <rect x="32" y="78" width="178" height="84" rx="10" class="main"/><text x="52" y="108" class="title">Large corporate product</text><text x="52" y="129" class="copy">Domestic B2B invoice intent</text><text x="52" y="146" class="copy">verified Irish entity context</text>
    <path d="M210 120 H260" class="path"/><polygon points="260,120 250,114 250,126" class="arrow"/>
    <rect x="262" y="72" width="188" height="96" rx="10" class="main"/><text x="282" y="100" class="title">Evaluate Phase One scope</text><text x="282" y="121" class="copy">VAT registration • LCD cohort</text><text x="282" y="140" class="copy">establishment • domestic B2B • date</text>
    <path d="M450 120 H490" class="path"/><polygon points="490,120 480,114 480,126" class="arrow"/>
    <rect x="492" y="72" width="188" height="96" rx="10" class="main"/><text x="512" y="100" class="title">Validate representation</text><text x="512" y="121" class="copy">EN 16931 • Irish rules/profile</text><text x="512" y="140" class="copy">version and technical detail gated</text>
    <path d="M680 120 H724 V82 H766" class="path"/><polygon points="766,82 756,76 756,88" class="arrow"/>
    <path d="M680 120 H724 V196 H766" class="path"/><polygon points="766,196 756,190 756,202" class="arrow"/>
    <rect x="768" y="43" width="220" height="78" rx="10" class="main"/><text x="788" y="72" class="title">Deliver structured e-invoice</text><text x="788" y="93" class="copy">Irish business recipient • transport TBD</text>
    <rect x="768" y="157" width="220" height="78" rx="10" class="main"/><text x="788" y="186" class="title">Report required subset</text><text x="788" y="207" class="copy">Revenue • data/timing/interface TBD</text>
    <path d="M988 82 H1030 V286 H696" class="path"/><path d="M988 196 H1010 V286 H696" class="path"/><polygon points="696,286 706,280 706,292" class="arrow"/>
    <rect x="488" y="247" width="206" height="80" rx="40" class="finish"/><text x="513" y="278" class="title">Return two leg outcomes</text><text x="513" y="299" class="copy">Delivery and reporting remain independent</text>
    <polygon points="356,204 394,242 356,280 318,242" class="bad"/><text x="329" y="238" class="title">Invalid</text><text x="326" y="254" class="copy">correct data</text>
    <path d="M356 204 V168" class="path-alert"/><polygon points="356,168 350,178 362,178" class="arrow-r"/>
    <path d="M318 242 H210 V162" class="path-alert"/><polygon points="210,162 204,172 216,172" class="arrow-r"/>
    <polygon points="875,260 913,276 929,314 913,352 875,368 837,352 821,314 837,276" class="warn"/><text x="846" y="309" class="title">Unknown</text><text x="842" y="325" class="copy">reconcile one leg</text>
    <path d="M875 235 V260" class="path-warn"/><polygon points="875,260 869,250 881,250" class="arrow-a"/>
    <path d="M821 314 H694" class="path-warn"/><polygon points="694,314 704,308 704,320" class="arrow-a"/>
    <text x="32" y="407" class="phase">EFFECTIVE-DATED POLICY EXPANSION</text>
    <rect x="62" y="438" width="250" height="76" rx="10" class="main"/><text x="82" y="466" class="title">Phase One • 2028-11-01</text><text x="82" y="486" class="copy">Large corporates issue/report; all receive</text>
    <path d="M312 476 H414" class="path"/><polygon points="414,476 404,470 404,482" class="arrow"/>
    <rect x="416" y="438" width="250" height="76" rx="10" class="optional"/><text x="436" y="466" class="title">Phase Two • 2029-11</text><text x="436" y="486" class="copy">Broader domestic cohort; detail confirmation gate</text>
    <path d="M666 476 H768" class="path-opt"/><polygon points="768,476 758,470 758,482" class="arrow-g"/>
    <rect x="770" y="438" width="250" height="76" rx="38" class="optional"/><text x="790" y="466" class="title">Phase Three • 2030-07-01</text><text x="790" y="486" class="copy">ViDA cross-border B2B e-invoice + DRR</text>
  </svg>
  <div class="notes"><div class="note"><strong>Inbound asymmetry</strong>All Irish businesses receive in Phase One; only the defined large-corporate cohort must issue/report.</div><div class="note"><strong>No invented interface</strong>Network, syntax/profile and Revenue API behaviour remain named delivery gates.</div><div class="note"><strong>Independent recovery</strong>A successful buyer delivery never masks a failed or unknown Revenue report, and vice versa.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Problem and value

Ireland has confirmed enough direction to begin product and data readiness, but not enough technical detail to implement production exchange. Waiting for a final API would leave products with insufficient invoice data and no cohort/inbound plan. Inventing a network, payload or status model now would create false certainty and rework.

The country pack therefore separates confirmed behaviour from specification-dependent adapters. Sage can assess EN 16931 data coverage, legal-entity/cohort identity, inbound readiness, dual-leg lifecycle and operations before activating external endpoints.

## Goals

| ID | Goal |
|---|---|
| IE-G1 | Make all selected Irish Sage products able to receive, validate and import structured invoices for verified Irish entities by the applicable phase. |
| IE-G2 | Enable Phase One in-scope large corporates to issue EN 16931-compliant domestic B2B invoices. |
| IE-G3 | Report the officially required subset to Revenue through a separate, correlated and safely recoverable leg once specifications are approved. |
| IE-G4 | Expand eligibility by effective phase without changing the product contract or historical evidence. |
| IE-G5 | Prepare semantic/reporting compatibility for ViDA cross-border obligations from 2030. |

## Non-goals

- Choosing or claiming an Irish transmission network, access-point model, syntax/profile or Revenue API before official publication and approval.
- Defining “real-time” as a specific SLA/deadline without evidence.
- Treating buyer delivery acknowledgement as Revenue reporting acceptance.
- Applying Phase One issuance/reporting to all Irish businesses.
- Changing tax rates, VAT liability or payment rules; Revenue states the modernisation changes invoicing/reporting processes.
- Covering B2C, B2G, self-billing, credit-note or cross-border details beyond evidence-backed scope; these remain consultation items.

## Definitions and actors

| Term/actor | Meaning/responsibility |
|---|---|
| Structured e-invoice | Issued, transmitted and received in a structured format supporting automated processing; Phase One must comply with EN 16931 |
| Large corporate | Phase One definition requires VAT registration, management by Revenue Large Corporates Division and Irish establishment/fixed establishment |
| Invoice delivery leg | Exchange of the structured invoice with the business recipient |
| Revenue report leg | Required subset of invoice data reported separately to Revenue |
| Sage customer/accountant | Maintains business facts, entity identity, corrections and authorised configuration |
| Sage product | Captures invoice intent, inbound experience and two-leg outcomes |
| Ireland pack owner | Owns source evidence, phase/scope policy, official artefacts and release approval |
| Revenue | Defines mandate, cohort, reporting and official technical/legal behaviour |
| Operations/support | Reconciles buyer/Revenue outcomes independently and communicates safe actions |

## Business scenarios

| ID | Scenario | Expected outcome | Exception/continuity |
|---|---|---|---|
| IE-S1 | Any Irish business in a selected product receives a Phase One e-invoice | Original structured invoice is validated, deduplicated and imported/displayed safely | Unsupported syntax/identity/trust failure is quarantined |
| IE-S2 | Phase One large corporate issues domestic B2B invoice | Scope and EN 16931 validation pass; invoice and required report are created as separate legs | Missing official adapter blocks production but not local validation |
| IE-S3 | Irish business is not in Phase One issuer cohort | Scope explains no Phase One issue/report obligation while inbound readiness remains active | Voluntary issuance policy, if offered, needs explicit evidence/product decision |
| IE-S4 | Buyer accepts invoice; Revenue rejects report | Delivery remains successful; report shows rejection/correction path | Do not resend buyer invoice solely due to report failure |
| IE-S5 | Revenue report times out after possible acceptance | Only report leg enters outcome-unknown and reconciles before retry | Buyer delivery history remains unchanged |
| IE-S6 | Phase Two activates | Newly eligible transactions use Phase Two policy | Phase One invoices retain original cohort/policy/report evidence |
| IE-S7 | ViDA cross-border phase activates | Approved EU/national pack version creates required cross-border behaviour | Domestic historical work is not reclassified silently |

## Business rules

| ID | Condition | Rule | Status/evidence |
|---|---|---|---|
| IE-BR1 | Date is 2028-11-01 or later and issuer meets official Phase One definition | Domestic B2B e-invoice issuance and reporting subset apply, subject to final legislation/specifications | Confirmed Revenue direction; detailed legal rule gate |
| IE-BR2 | Phase One begins | All Irish businesses must be able to receive structured e-invoices | Confirmed Revenue |
| IE-BR3 | Phase One invoice is created | Representation must comply with EN 16931; PDF/scanned paper alone is excluded | Confirmed Revenue |
| IE-BR4 | Report is required | Delivery and report are independent legs sharing invoice/policy context | Proposed product rule derived from official dual obligation |
| IE-BR5 | Technical detail is absent | Mark capability unknown and block live mutation rather than inventing syntax, route, deadline or acknowledgement | Confirmed evidence discipline |
| IE-BR6 | Phase policy changes | Use effective-dated policy and preserve original invoice/report context | Proposed shared continuity rule |
| IE-BR7 | Cross-border ViDA date arrives | Apply approved EU/national implementation version; do not assume domestic rules are identical | Official EU direction; implementation open |

## Scope and capability evidence

| Capability | State | Pack position |
|---|---|---|
| Phase/cohort applicability | Partially confirmed | Phase One date/large-corporate definition confirmed; detailed transaction/exemption rules open |
| Inbound | Confirmed direction | All businesses receive from Phase One; product/channel/profile scope open |
| Outbound | Confirmed direction | Phase One large corporates domestic B2B |
| Semantic standard | Confirmed | EN 16931; CIUS/syntax/profile version open |
| Transport/recipient resolution | Unknown | Must remain adapter/configuration gate |
| Revenue reporting | Confirmed obligation, technical detail unknown | Separate report leg; payload/timing/API/correction open |
| Lifecycle/status | Unknown/proposed | Shared technical events plus official mapping when published |
| Identity/authentication | Unknown | Customer entity, recipient, network and Revenue trust models require official artefacts |
| Phase Two | Direction confirmed, detail open | Effective policy placeholder only |
| ViDA Phase Three | Confirmed EU date/direction | National integration artefacts open |

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [Revenue: Phase One large corporates](https://www.revenue.ie/en/vat/vida-vat-modernisation/large-corporates-vat-modernisation.aspx), accessed 2026-08-10 | 2028-11-01, large-corporate definition, domestic B2B issue/report subset, all businesses receive, EN 16931 and no PDF/scans | Primary official current page; technical detail not present | Scope, inbound asymmetry, semantic requirement and gates |
| [Revenue: VAT Modernisation — Implementation of eInvoicing](https://www.revenue.ie/en/vat/documents/implementation-einvoicing.pdf), 2026 | Three phases; structured invoices plus key data reported to Revenue; invoicing/reporting process change only | Primary official overview; extracted Phase Two/Three details need later confirmation against final law/specs | Phase model and product preparation |
| [European Commission ViDA 2026 Work Programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en) | 2030-07-01 cross-border B2B DRR based on mandatory e-invoicing | Primary EU direction; implementation work continues | Phase Three compatibility/gate |
| Supplied research | Reusable reporting framework and neutral core hypothesis | Secondary synthesis; technical specifics not official | Shared/country boundary |

## Proposed journeys

| Journey | Spine | Required exception/continuity |
|---|---|---|
| Prepare | Map EN 16931 data → capture entity/cohort evidence → assess inbound and issue/report readiness | Live adapters remain disabled until official artefacts and approval |
| Phase One | Submit → confirm cohort/scope → validate EN 16931 → create buyer and Revenue legs → record both outcomes | Delivery and report never inherit or overwrite each other's result |
| Correct/recover/change | Correct before send; reject or timeout affects one leg → reconcile before retry | Later phase/route/rule changes affect new work; original context remains |

## Requirements

### Applicability and invoice capability

| ID | Requirement |
|---|---|
| IE-FR1 | The pack must evaluate transaction date, VAT registration, Revenue cohort, Irish establishment/fixed establishment, parties, domestic/cross-border status and transaction/document type before applying a phase obligation. |
| IE-FR2 | Scope results must identify phase, policy version, issue/receive/report obligations, reason and any unresolved evidence. |
| IE-FR3 | Phase One outbound must validate against the approved EN 16931 semantic/profile/rule artefacts before external mutation. |
| IE-FR4 | Phase One inbound must support all configured Irish legal entities independently of whether they are required to issue/report. |
| IE-FR5 | Inbound processing must retain original structured data, verify tenant/recipient/source as defined by the approved trust model, deduplicate and expose validation/import outcome. |
| IE-FR6 | PDF, image or scanned paper without qualifying structured data must not be represented as a Phase One compliant e-invoice. |

### Delivery and reporting

| ID | Requirement |
|---|---|
| IE-FR7 | The service must not activate an Irish delivery route until official/approved transport, recipient-resolution, identity and acknowledgement behaviour are configured and tested. |
| IE-FR8 | For every in-scope Phase One outbound invoice, the platform must create independent buyer-delivery and Revenue-report legs linked to the same immutable invoice/scope context. |
| IE-FR9 | The report leg must contain only the officially required subset and version once specified; the platform must not infer the payload from the full invoice. |
| IE-FR10 | Delivery/report status, rejection, correction, cancellation and retry must remain leg-specific and preserve official raw reason/evidence. |
| IE-FR11 | Success of one leg must not complete, retry or overwrite the other leg. |
| IE-FR12 | Phase Two/Three behaviour must remain disabled until the corresponding official policy/specification version is approved and effective. |

### Resilience, continuity and operations

| ID | Requirement |
|---|---|
| IE-FR13 | Duplicate invoice/report requests and inbound events must be idempotent within their defined identity scope. |
| IE-FR14 | A timeout after possible buyer or Revenue mutation must enter outcome-unknown and reconcile only that leg before retry. |
| IE-FR15 | Operations must see scope/cohort evidence, representation validation, each intended/observed leg, evidence freshness and permitted recovery action. |
| IE-FR16 | Policy, cohort, route or adapter changes must apply to new eligible work and must not rewrite historical invoice/report evidence. |
| IE-FR17 | Pack activation/suspension must be controllable by phase, direction, adapter, cohort and environment with authorised audit. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| IE-NFR1 | Customer/entity, invoice, report and credential data must be tenant/environment isolated and minimised by purpose. |
| IE-NFR2 | Secrets, certificates and consent/authority evidence must follow approved custody, rotation, revocation and audit controls. |
| IE-NFR3 | Report and invoice retention/deletion/legal-hold rules require Revenue/legal/privacy evidence; no period is assumed in discovery. |
| IE-NFR4 | Policy, EN 16931/Irish profile and report-schema changes require regression fixtures, owner approval, effective dating and rollback. |
| IE-NFR5 | Availability, latency, report-timing, capacity and backlog targets must use official deadlines plus reference-product baselines before delivery approval. |
| IE-NFR6 | Observability must distinguish product data, country policy, Sage platform, delivery network/recipient and Revenue faults without exposing unnecessary invoice data. |
| IE-NFR7 | Customer-facing status/correction must be accessible, localisable and explicit about whether buyer delivery or Revenue reporting is affected. |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| IE-AC1 | Given an Irish business outside the Phase One issuer cohort, when scope is evaluated after 2028-11-01, then inbound readiness is required while issue/report obligations are not falsely applied. |
| IE-AC2 | Given a Phase One large corporate domestic B2B invoice, when valid official artefacts are configured, then EN 16931 validation passes before separate delivery/report legs are created. |
| IE-AC3 | Given required invoice data is invalid, when submitted, then no external leg is mutated and rule/field/version correction guidance is returned. |
| IE-AC4 | Given buyer delivery succeeds and Revenue rejects the report, when status is viewed, then delivery remains successful and only the report exposes correction/recovery. |
| IE-AC5 | Given the Revenue report times out after possible acceptance, when recovery runs, then the report reconciles before retry and the buyer invoice is not resent. |
| IE-AC6 | Given the technical transport/report specification is not approved, when live activation is attempted, then external mutation is blocked with the named decision gate. |
| IE-AC7 | Given a Phase Two policy becomes effective, when a newly eligible invoice is evaluated, then the new policy applies while a Phase One invoice retains original scope and evidence. |
| IE-AC8 | Given an inbound PDF without structured data, when processed, then it is not labelled a compliant Irish e-invoice. |

## Goal traceability

| Goal | Primary requirements | Demonstration |
|---|---|---|
| IE-G1 — Receive structured invoices | IE-FR4–IE-FR6, IE-FR13, IE-FR15; IE-NFR1, IE-NFR6 | IE-AC1, IE-AC8 |
| IE-G2 — Phase One compliant issuance | IE-FR1–IE-FR3, IE-FR7; IE-NFR4 | IE-AC2, IE-AC3, IE-AC6 |
| IE-G3 — Independent Revenue reporting | IE-FR8–IE-FR11, IE-FR14 | IE-AC4, IE-AC5 |
| IE-G4 — Effective-dated expansion | IE-FR12, IE-FR16, IE-FR17; IE-NFR4 | IE-AC7 |
| IE-G5 — ViDA readiness | IE-FR1, IE-FR2, IE-FR12; IE-NFR4, IE-NFR5 | IE-AC6, IE-AC7 |

## Metrics, rollout and gates

| Measure | Baseline/target status | Owner |
|---|---|---|
| Irish product/entity EN 16931 data readiness | Coverage baseline required per product | Product + Ireland pack owner |
| Phase One cohort identification completeness | Target/authoritative source approval required | Compliance |
| Inbound receipt/import success by future syntax/route | Blocked until artefacts/cohort selected | Product/operations |
| Delivery vs reporting success and unknown-age | Thresholds need official interface/SLA evidence | Operations |
| First-pass validation and correction completion | Baseline required | Product |

Rollout gates:

1. Name Revenue/regulatory, product, engineering, security/privacy and operations owners.
2. Identify Sage products and customers matching the Phase One definition; validate authoritative cohort evidence handling.
3. Complete EN 16931 data-gap assessment and inbound product experience.
4. Obtain and approve Irish legal text, CIUS/syntax/schema/code lists, transport/directory, identity and Revenue reporting specifications.
5. Confirm report timing, corrections/cancellations, acknowledgements, idempotency, retention and support/SLA.
6. Demonstrate local validation, inbound, dual-leg success/failure, unknown outcome, phase change and historical continuity in sandbox.
7. Complete security/privacy/operations/customer communication and kill/rollback readiness.
8. Pilot an approved Phase One cohort before expansion.

## Risks and consultation questions

| Risk/question | Why it matters | Owner | Blocks/current hypothesis |
|---|---|---|---|
| Which Sage products/customers are Phase One large corporates? | Defines delivery cohort and data gaps | Ireland product/compliance | Blocks cohort; authoritative evidence required |
| What Irish syntax, CIUS/profile and version apply? | Controls representation and validation | Revenue/compliance | Blocks technical design |
| What transport/network and recipient discovery model applies? | Determines onboarding, identity, routing and operations | Revenue/architecture | Blocks live delivery; adapter placeholder only |
| What exact subset, deadline, API and acknowledgement apply to reporting? | Determines report contract and recovery | Revenue/compliance | Blocks live reporting |
| How are corrections, credit notes, self-billing, exemptions and cancellations treated? | Material business scenarios | Compliance | Blocks detailed rule set |
| How is “all businesses receive” enforced across Sage products and non-issuer cohorts? | Inbound scope/adoption | Portfolio/product | Blocks rollout plan |
| How do Phase Two domestic and ViDA cross-border obligations interact? | Prevents double reporting/conflicting policy | Revenue/EU compliance | Blocks Phase Two/Three design |
| Early design hardens around an invented API | Rework/compliance risk | Keep interfaces capability-based and live-disabled until evidence | Proposed mitigation |

## Decisions

| Decision | Status | Owner/date |
|---|---|---|
| Ireland is a child country pack of PRD-SEI-227 | Confirmed by user request | 2026-08-10 |
| Model buyer delivery and Revenue reporting as independent legs | Proposed product requirement from confirmed dual obligation | TBD |
| Use EN 16931 as confirmed Phase One semantic basis | Confirmed Revenue evidence | 2026-08-10 |
| Keep technical adapters disabled until official artefacts and approvals exist | Confirmed discovery boundary | 2026-08-10 |

## Revision history

| Date | Change | Evidence/decision | Pull request |
|---|---|---|---|
| 2026-08-10 | Initial discovery child PRD with Confluence-safe phased dual-leg visual | User request, Revenue and EU official sources | |
| 2026-08-10 | Linked the consolidated parent visual atlas and compressed journey prose for research-stage readability | User direction | |
| 2026-08-10 | Approved for publication to existing page `866140021`; existing hierarchy preserved | User approval | |
