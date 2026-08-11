---
id: PRD-SEI-230
title: UK E-Invoicing Compliance Pack
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-10
updated: 2026-08-11
reviewers: []
related:
  - PRD-SEI-227
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "771496799"
  page_id: "866140019"
  title: 2.5 E-Invoicing UK
  layout: two_left_sidebar
  toc: true
---

# UK E-Invoicing Compliance Pack

## Decision summary

Define the UK as an evidence-led country pack on PRD-SEI-227. The UK government has moved beyond the earlier research position: mandatory e-invoicing for VAT invoices is planned from April 2029, and Peppol has been announced as the core interoperability network. However, full guidance, standards, technical specifications and legislation remain under development, with continuing consultation about legacy systems.

The pack may prepare shared Peppol, invoice-semantic, onboarding, validation, exchange and evidence capabilities. It must not infer the final UK invoice profile, participant identifiers, access-point obligations, scope/exemptions, reporting to HMRC, lifecycle statuses, transition or enforcement before official artefacts are approved.

> **Country principle:** Treat Peppol and April 2029 as confirmed direction; treat every unissued legal or technical rule as a visible gate, not an implicit requirement.

## Parent relationship, outcome and readiness

| Area | Position |
|---|---|
| Parent PRD | PRD-SEI-227 — shared service and country-pack contract |
| Visual research | PRD-SEI-227 contains the consolidated source-diagram atlas; this child keeps only the UK-specific Peppol and policy-gate flow |
| Confluence position | Existing page `866140019`; preserve current parent `771496799` |
| Customer outcome | UK businesses issue and receive interoperable structured VAT invoices through supported Sage products with low-friction onboarding and explainable compliance outcomes. |
| Current phase | Pre-legislation discovery and co-creation readiness |
| Readiness | **Discovery-ready**, not delivery-ready: architecture direction is known, but the legal/technical contract is incomplete. |

## Confirmed roadmap and product posture

| Period/date | Confirmed official direction | Product posture |
|---|---|---|
| 2026 | HMRC/DBT co-creation and implementation-roadmap work; Peppol announced as core interoperability network | Participate in consultation; assess Peppol capability and product data/onboarding gaps |
| By end 2027–28 | HMRC roadmap says full guidance, standards, technical specification and legislation will be published | Convert official artefacts into a governed UK policy/profile/adapter and close delivery gates |
| April 2029 | VAT e-invoicing mandate planned for B2B/B2G transactions/all VAT invoices as defined by final regime | Activate only for confirmed scope/cohorts and approved transition rules |
| Future/unknown | Any HMRC transaction-reporting, status, payment or additional tax-data obligation | No reporting leg unless official evidence later defines it |

## Confirmed Peppol direction with policy-controlled activation

<!-- confluence-html-macro:start -->
<div class="uk-pack" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .uk-pack *{box-sizing:border-box}.uk-pack h2{margin:0;color:#172b4d;font-size:18px}.uk-pack .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.uk-pack svg{display:block;width:1080px;height:570px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.uk-pack .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.uk-pack .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.uk-pack .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.uk-pack .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.uk-pack .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.uk-pack .title{fill:#172b4d;font-size:11px;font-weight:700}.uk-pack .copy{fill:#42526e;font-size:9px}.uk-pack .phase{fill:#172b4d;font-size:10px;font-weight:700;letter-spacing:.05em}.uk-pack .path{fill:none;stroke:#00875a;stroke-width:2}.uk-pack .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.uk-pack .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.uk-pack .path-warn{fill:none;stroke:#ff8b00;stroke-width:1.8;stroke-dasharray:6 4}.uk-pack .arrow{fill:#00875a}.uk-pack .arrow-g{fill:#6b778c}.uk-pack .arrow-r{fill:#de350b}.uk-pack .arrow-a{fill:#ff8b00}.uk-pack .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.uk-pack .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.uk-pack .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The target exchange spine is visible, but each amber gate requires official UK evidence and approval before a live mandate claim or mutation.</p>
  <svg viewBox="0 0 1080 570" role="img" aria-label="A UK seller product submits VAT invoice intent to the shared service. Before April 2029 activation, the UK pack must pass scope and legislation, UK invoice profile, participant identity and discovery, and access-point trust gates. The confirmed direction routes through a Peppol core network to the buyer. Correctable validation failures return to the seller. Ambiguous delivery outcomes reconcile before retry. HMRC reporting and legacy-system routes are dashed optional branches that remain inactive until official policy defines them. A timeline shows 2026 co-creation, standards and legislation by end 2027 to 2028, and April 2029 mandate.">
    <text x="30" y="30" class="phase">TARGET EXCHANGE — LIVE ONLY AFTER OFFICIAL GATES</text>
    <rect x="30" y="78" width="170" height="82" rx="10" class="main"/><text x="50" y="108" class="title">UK seller product</text><text x="50" y="129" class="copy">VAT invoice intent</text><text x="50" y="146" class="copy">verified legal entity and buyer</text>
    <path d="M200 119 H250" class="path"/><polygon points="250,119 240,113 240,125" class="arrow"/>
    <polygon points="300,70 338,86 354,124 338,162 300,178 262,162 246,124 262,86" class="warn"/><text x="270" y="113" class="title">Scope gate</text><text x="268" y="130" class="copy">law/exemptions</text><text x="276" y="146" class="copy">effective date</text>
    <path d="M354 124 H404" class="path-warn"/><polygon points="404,124 394,118 394,130" class="arrow-a"/>
    <polygon points="454,70 492,86 508,124 492,162 454,178 416,162 400,124 416,86" class="warn"/><text x="421" y="113" class="title">Profile gate</text><text x="420" y="130" class="copy">semantics/syntax</text><text x="430" y="146" class="copy">validation</text>
    <path d="M508 124 H558" class="path-warn"/><polygon points="558,124 548,118 548,130" class="arrow-a"/>
    <polygon points="608,70 646,86 662,124 646,162 608,178 570,162 554,124 570,86" class="warn"/><text x="574" y="113" class="title">Identity gate</text><text x="571" y="130" class="copy">participant/discovery</text><text x="581" y="146" class="copy">authority/trust</text>
    <path d="M662 124 H712" class="path-warn"/><polygon points="712,124 702,118 702,130" class="arrow-a"/>
    <polygon points="762,70 800,86 816,124 800,162 762,178 724,162 708,124 724,86" class="warn"/><text x="729" y="113" class="title">Access gate</text><text x="728" y="130" class="copy">AP contract/SLA</text><text x="729" y="146" class="copy">test/operations</text>
    <path d="M816 124 H856" class="path"/><polygon points="856,124 846,118 846,130" class="arrow"/>
    <rect x="858" y="78" width="190" height="82" rx="10" class="main"/><text x="878" y="108" class="title">Peppol core network</text><text x="878" y="129" class="copy">Confirmed UK direction</text><text x="878" y="146" class="copy">final implementation detail gated</text>
    <path d="M953 160 V244" class="path"/><polygon points="953,244 947,234 959,234" class="arrow"/>
    <rect x="858" y="246" width="190" height="78" rx="39" class="finish"/><text x="886" y="276" class="title">UK buyer receives</text><text x="884" y="297" class="copy">structured interoperable invoice</text>
    <path d="M858 285 H780" class="path"/><polygon points="780,285 790,279 790,291" class="arrow"/>
    <rect x="568" y="246" width="210" height="78" rx="10" class="main"/><text x="588" y="275" class="title">Evidence and product outcome</text><text x="588" y="296" class="copy">validation • route • delivery • audit</text>
    <polygon points="454,218 492,256 454,294 416,256" class="bad"/><text x="426" y="252" class="title">Invalid</text><text x="424" y="268" class="copy">correct data</text>
    <path d="M454 218 V178" class="path-alert"/><polygon points="454,178 448,188 460,188" class="arrow-r"/>
    <path d="M416 256 H200 V160" class="path-alert"/><polygon points="200,160 194,170 206,170" class="arrow-r"/>
    <polygon points="762,345 800,361 816,399 800,437 762,453 724,437 708,399 724,361" class="warn"/><text x="733" y="394" class="title">Unknown</text><text x="729" y="410" class="copy">reconcile delivery</text>
    <path d="M762 324 V345" class="path-warn"/><polygon points="762,345 756,335 768,335" class="arrow-a"/>
    <path d="M708 399 H673 V324" class="path-warn"/><polygon points="673,324 667,334 679,334" class="arrow-a"/>
    <rect x="36" y="346" width="230" height="82" rx="10" class="optional"/><text x="56" y="375" class="title">Legacy-system route</text><text x="56" y="396" class="copy">Role remains under stakeholder engagement</text><text x="56" y="413" class="copy">No permanent exception assumed</text>
    <path d="M266 387 H338 V324 H568" class="path-opt"/><polygon points="568,324 558,318 558,330" class="arrow-g"/>
    <rect x="318" y="346" width="230" height="82" rx="10" class="optional"/><text x="338" y="375" class="title">HMRC reporting leg</text><text x="338" y="396" class="copy">Inactive: no obligation inferred from</text><text x="338" y="413" class="copy">the e-invoice mandate announcement</text>
    <path d="M548 387 H568 V324" class="path-opt"/><polygon points="568,324 562,334 574,334" class="arrow-g"/>
    <text x="30" y="486" class="phase">ROADMAP</text>
    <rect x="86" y="500" width="230" height="52" rx="10" class="main"/><text x="106" y="522" class="title">2026 • co-create + roadmap</text><text x="106" y="540" class="copy">Peppol core announced</text>
    <path d="M316 526 H424" class="path"/><polygon points="424,526 414,520 414,532" class="arrow"/>
    <rect x="426" y="500" width="230" height="52" rx="10" class="optional"/><text x="446" y="522" class="title">By end 2027–28</text><text x="446" y="540" class="copy">guidance • standards • specs • law</text>
    <path d="M656 526 H764" class="path-opt"/><polygon points="764,526 754,520 754,532" class="arrow-g"/>
    <rect x="766" y="500" width="230" height="52" rx="26" class="finish"/><text x="786" y="522" class="title">April 2029 • mandate</text><text x="786" y="540" class="copy">activate approved UK policy</text>
  </svg>
  <div class="notes"><div class="note"><strong>Research updated</strong>Peppol is now confirmed direction, replacing the earlier topology-TBD position.</div><div class="note"><strong>Direction is not specification</strong>UK profile, participant and access-point operating rules still require official artefacts.</div><div class="note"><strong>No assumed tax report</strong>An e-invoice mandate does not by itself define a separate HMRC transaction-reporting leg.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Problem and value

The UK now has a mandate date and interoperability-network direction, creating a credible preparation window. But implementing “generic Peppol” as final UK compliance would be premature: Peppol deployments still depend on jurisdictional profiles, identifier schemes, participant discovery, access-point rules, security, acknowledgements, onboarding and legal scope.

Sage needs two speeds: begin shared data/Peppol/product-readiness discovery now, while preventing external production claims until the official UK contract is complete. This reduces late rework without converting consultation hypotheses into commitments.

## Goals

| ID | Goal |
|---|---|
| UK-G1 | Prepare Sage products and the shared service for April 2029 structured VAT e-invoicing. |
| UK-G2 | Reuse a governed Peppol capability while isolating UK profile, scope, participant and policy rules in the country pack. |
| UK-G3 | Provide simple customer onboarding, recipient discovery, validation, delivery and inbound receipt once official rules permit. |
| UK-G4 | Support low-cost/interoperable product options and legacy transition without creating an unsafe permanent bypass. |
| UK-G5 | Preserve explicit uncertainty for reporting, lifecycle and enforcement until official evidence exists. |

## Non-goals

- Claiming Peppol alone satisfies the future UK mandate.
- Selecting a final Peppol authority, access-point commercial model, UK invoice profile or participant identifier before evidence/approval.
- Assuming every B2C transaction is in scope; official consultation material says VAT invoices are typically B2B/B2G, with final regime detail pending.
- Inventing an HMRC transaction-reporting, payment-status or tax-clearance obligation.
- Guaranteeing a legacy-system exception or transition period.
- Replacing final law, guidance or HMRC/DBT consultation.

## Definitions and actors

| Term/actor | Meaning/responsibility |
|---|---|
| UK VAT e-invoice | Future legally defined structured VAT invoice; PDFs/images/word/HTML/OCR alone were excluded from the government's consultation definition |
| Peppol core interoperability network | Confirmed UK network direction; detailed UK implementation and governance remain open |
| Access point | Service boundary connecting participants to Peppol; operating/contract model is not approved here |
| Participant identity/discovery | Scheme and service metadata used to find an eligible recipient |
| Customer/accountant | Maintains legal entity, VAT/business facts, authority and invoice corrections |
| Sage product | Captures intent/inbound invoices and displays compliance/delivery outcomes |
| UK pack owner | Owns official evidence, scope/profile versions, consultation and activation |
| HMRC/DBT | Policy/legislation/implementation owners |
| Access-point/network operator | Future contracted exchange/trust/availability boundary |
| Operations/support | Monitors onboarding, directory, access-point, delivery and reconciliation outcomes |

## Business scenarios

| ID | Scenario | Expected outcome | Exception/continuity |
|---|---|---|---|
| UK-S1 | Product performs readiness assessment before final specification | Data and Peppol capability gaps are visible; live mandate compliance remains disabled | No invented default profile/network mutation |
| UK-S2 | In-scope seller submits valid VAT invoice after activation | UK policy validates, recipient resolves and approved access point delivers once | No eligible recipient/route blocks with guidance |
| UK-S3 | Buyer receives structured invoice | Original retained, tenant/recipient/trust/profile validated and imported once | Unsafe/unsupported invoice is quarantined |
| UK-S4 | Recipient is not discoverable | Product receives a distinct route/readiness outcome | No email/PDF fallback is inferred as compliant |
| UK-S5 | Access point times out after possible send | Delivery becomes outcome-unknown and reconciles before resend | No duplicate legal invoice |
| UK-S6 | Legacy system cannot interoperate | Approved transition/assisted route is applied only if final policy permits | Exception is effective-dated and audited |
| UK-S7 | Final guidance changes draft assumptions | New pack version activates prospectively after tests/approval | Earlier voluntary/pilot evidence remains intact |

## Business rules

| ID | Condition | Rule | Status/evidence |
|---|---|---|---|
| UK-BR1 | April 2029 mandate is evaluated | Apply only the final legally confirmed scope, effective date, exemptions and transitions | Mandate date/direction confirmed; detailed law open |
| UK-BR2 | Invoice is represented as compliant e-invoice | It must be structured as required by the final UK standard; PDF/Word/images/HTML/OCR alone are not sufficient under consultation definition | Confirmed consultation direction; final legal definition open |
| UK-BR3 | Network route is selected | Peppol is the core interoperability network; use only approved UK participant/profile/access-point configuration | Core network confirmed; detailed model open |
| UK-BR4 | Legacy system cannot interoperate | Apply no exception/fallback unless final policy explicitly permits it | Official engagement ongoing |
| UK-BR5 | Reporting is considered | Create no HMRC report leg without a separate official obligation/specification | Confirmed evidence boundary |
| UK-BR6 | Draft/final policy changes | Use approved effective-dated pack versions and preserve original invoice/route evidence | Proposed shared continuity rule |
| UK-BR7 | Product offers voluntary pre-mandate e-invoicing | Clearly distinguish network delivery from future statutory compliance and use only approved contracts | Proposed; legal/product approval required |

## Scope and capability evidence

| Capability | State | Pack position |
|---|---|---|
| Mandate date/direction | Confirmed | April 2029; final legal scope still gated |
| Structured definition | Direction confirmed | Consultation excludes unstructured-only formats; final standard/profile open |
| Core network | Confirmed direction | Peppol; governance/access-point/participant detail open |
| Applicability/exemptions | Unknown | Policy placeholder only |
| Inbound/outbound symmetry | Direction, not complete law | Government response describes issuing/receiving electronically; final requirements open |
| Recipient identity/discovery | Unknown | Must be supplied by official UK Peppol model |
| Validation/profile | Unknown | Shared framework ready; live pack disabled |
| Reporting to HMRC | Unknown/not currently evidenced | No report leg |
| Lifecycle/status/payment | Unknown | Do not import France/Spain statuses |
| Legacy transition | Open | Explicit consultation/decision gate |

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [HMRC Transformation Roadmap update 2026](https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/annex-summary-of-hmrcs-planned-activities-listed-in-this-transformation-roadmap-progress-update) | April 2029 B2B/B2G VAT e-invoicing; roadmap/co-creation in 2026; full guidance, standards, technical specification and legislation by end 2027–28 | Primary official current roadmap; detail future | Phase/gates and no premature delivery claim |
| [UK tax update 2026](https://www.gov.uk/government/publications/summary-of-tax-update-2026-simplification-modernisation-and-fairness/tax-update-2026-simplification-modernisation-and-fairness-summary) | Peppol announced as core interoperability network; legacy-system role still under engagement | Primary official direction; implementation details absent | Peppol preparation and legacy gate |
| [Government e-invoicing consultation response](https://www.gov.uk/government/consultations/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector/outcome/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector-consultation-response), 2025 | 2029 mandate, structured system-to-system concept, unstructured exclusions, interoperability/network effects and small-business concerns | Primary policy response; predates 2026 Peppol announcement and final law | Problem, outcomes and open policy |
| Supplied research | UK architecture/details were TBD and a neutral core was recommended | Secondary synthesis; topology conclusion superseded in part by 2026 Peppol announcement | Evidence-change record and shared boundary |

## Proposed journeys

| Journey | Spine | Required exception/continuity |
|---|---|---|
| Prepare | Map VAT data → assess Peppol/onboarding gaps → store inactive hypotheses and gates | No mandate claim or live mutation before approved official artefacts |
| Target after activation | Submit → evaluate final policy → validate UK profile → discover participant → deliver by approved access point → import once | Missing route blocks; raw acknowledgements remain preserved |
| Correct/recover/change | Correct before send; timeout after possible send → outcome unknown → reconcile before retry | New pack versions apply prospectively; historical context is never rewritten |

## Requirements

### Policy and readiness

| ID | Requirement |
|---|---|
| UK-FR1 | The pack must keep live mandate behaviour disabled until UK legislation, scope/exemptions/transition, invoice standard/profile, Peppol implementation and operational controls are officially evidenced and approved. |
| UK-FR2 | Once available, applicability must evaluate effective date, legal entity/VAT status, parties, transaction/document type, B2B/B2G classification, exemption and transition. |
| UK-FR3 | Scope results must identify policy version, applicable issue/receive obligations, reason and unresolved evidence without treating consultation hypotheses as law. |
| UK-FR4 | Product readiness tooling must assess semantic data, legal-entity identity, inbound/outbound, Peppol participant and operational gaps without making external mutations. |

### Invoice and Peppol exchange

| ID | Requirement |
|---|---|
| UK-FR5 | Outbound must validate against the approved UK syntax/profile/business rules before network submission and return stable correction guidance. |
| UK-FR6 | The Peppol adapter must use approved UK participant identifier schemes, discovery/service metadata, document/process identifiers, transport/security profile and access-point contract versions. |
| UK-FR7 | Recipient resolution must record query identity, source, evidence time, selected service/route and failure reason; missing eligibility must block dispatch. |
| UK-FR8 | Inbound must verify intended tenant/recipient, source/trust, supported UK profile and duplication, retain the original representation and expose safe validation/import outcome. |
| UK-FR9 | Every delivery must record representation/profile, participant/service, access point, message/correlation identity, acknowledgements and observed outcome. |
| UK-FR10 | Unstructured-only PDF/Word/image/HTML/OCR content must not be represented as compliant unless final law explicitly defines an eligible structured wrapper/profile. |
| UK-FR11 | A legacy-system route or exception must remain disabled unless final policy explicitly permits it, and must be effective-dated and auditable. |
| UK-FR12 | The pack must create no HMRC reporting/payment-status leg without a separate approved official obligation. |

### Resilience, continuity and operations

| ID | Requirement |
|---|---|
| UK-FR13 | Outbound/inbound requests and network events must deduplicate by approved invoice/message/idempotency identities. |
| UK-FR14 | A timeout after possible Peppol/access-point mutation must enter outcome-unknown and reconcile network/provider evidence before retry. |
| UK-FR15 | Operations must see policy/profile, intended and observed participant/route/access-point state, acknowledgement freshness, fault domain and permitted recovery. |
| UK-FR16 | Policy/profile/participant/access-point changes must apply only to eligible new work and retain historical invoice/route/evidence access. |
| UK-FR17 | The UK pack/adapter must support scoped pilot, suspension and rollback by product, cohort, direction, access point and environment. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| UK-NFR1 | Legal-entity authority, Peppol participant, tenant, environment, invoice and credential boundaries must be isolated and least-privileged. |
| UK-NFR2 | Access-point keys/certificates/secrets must use approved custody, rotation, revocation and non-disclosure controls. |
| UK-NFR3 | Original invoices, transformations and network evidence must use approved integrity, retention, deletion and legal-hold rules; final periods are open. |
| UK-NFR4 | UK policy/profile/identifier/network changes require official provenance, regression fixtures, owner approval, effective date, compatibility analysis and rollback. |
| UK-NFR5 | Availability, throughput, delivery latency, directory freshness, payload and backlog targets require official network/access-point evidence plus product baselines. |
| UK-NFR6 | Observability must distinguish product data, UK policy, Sage platform, participant discovery, access point/network and recipient faults without exposing unnecessary invoice data. |
| UK-NFR7 | Onboarding and correction experiences must be accessible, localisable and usable by SMEs/accountants; success criteria require user research. |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| UK-AC1 | Given final UK legal/technical artefacts are not approved, when live mandate activation is attempted, then the pack blocks external mutation and lists the missing gates. |
| UK-AC2 | Given readiness assessment runs before activation, when a product lacks required semantic/participant data, then gaps are reported without claiming non-compliance or sending data. |
| UK-AC3 | Given an in-scope valid invoice after activation, when recipient discovery succeeds, then the approved UK profile is delivered once through the approved Peppol route with durable evidence. |
| UK-AC4 | Given a PDF-only invoice, when classified under current policy direction, then it is not labelled a compliant structured UK e-invoice. |
| UK-AC5 | Given recipient discovery returns no eligible UK service, when dispatch is requested, then no network mutation occurs and actionable readiness evidence is returned. |
| UK-AC6 | Given the access point times out after possible send, when recovery runs, then the outcome reconciles before retry and no preventable duplicate is produced. |
| UK-AC7 | Given no approved HMRC reporting obligation exists, when an invoice is delivered, then the service creates no authority-report leg or reporting-success claim. |
| UK-AC8 | Given a later UK pack version changes scope/profile, when an older invoice is inspected, then its original policy, profile, participant, route and acknowledgement evidence remain unchanged. |

## Goal traceability

| Goal | Primary requirements | Demonstration |
|---|---|---|
| UK-G1 — April 2029 readiness | UK-FR1–UK-FR5; UK-NFR4, UK-NFR5 | UK-AC1–UK-AC3 |
| UK-G2 — Reusable governed Peppol | UK-FR6, UK-FR7, UK-FR9, UK-FR16; UK-NFR2, UK-NFR4 | UK-AC3, UK-AC5, UK-AC8 |
| UK-G3 — Customer onboarding and exchange | UK-FR4–UK-FR10, UK-FR13–UK-FR15; UK-NFR6, UK-NFR7 | UK-AC2–UK-AC6 |
| UK-G4 — Low-friction/legacy transition | UK-FR4, UK-FR11, UK-FR17; UK-NFR7 | UK-AC1, UK-AC2 |
| UK-G5 — Explicit uncertainty | UK-FR1, UK-FR3, UK-FR12; UK-NFR4 | UK-AC1, UK-AC7, UK-AC8 |

## Metrics, rollout and gates

| Measure | Baseline/target status | Owner |
|---|---|---|
| UK product semantic-data readiness | Baseline per product required | Portfolio/product |
| Customer/participant onboarding completion and time | User research and access-point model required | Product |
| Recipient discovery success by cohort | Baseline after UK model/test network exists | Operations |
| First-pass profile validation and correction completion | Profile artefacts required | Product + UK pack owner |
| Duplicate/outcome-unknown delivery rate and age | Access-point SLA/evidence required | Operations |
| SME usability/support burden | Research baseline/target required | Product research/support |

Rollout gates:

1. Name UK policy/compliance, portfolio/product, architecture, security/privacy and operations owners.
2. Participate in HMRC/DBT/software-industry co-creation and maintain a dated evidence register.
3. Select candidate Sage products/cohorts and assess semantic, inbound, identity and onboarding readiness.
4. Approve final legislation, guidance, scope/exemptions/transition and enforcement interpretation.
5. Obtain UK invoice profile/schemas/code lists/validators, Peppol participant/discovery/process/transport rules and test environment.
6. Select/contract/approve access-point operating model, SLA, security, privacy, retention, support and exit.
7. Demonstrate onboarding, inbound/outbound, validation correction, recipient missing, duplicate, unknown outcome, adapter switch and historical continuity.
8. Pilot with explicit voluntary/statutory messaging, kill/rollback criteria and small-business support before April 2029 expansion.

## Risks and consultation questions

| Risk/question | Why it matters | Owner | Blocks/current hypothesis |
|---|---|---|---|
| What is final legal scope, including B2B/B2G, exemptions and transition? | Determines applicability and cohort | HMRC/UK compliance | Blocks live policy |
| What UK semantic/syntax profile and validation artefacts apply? | Determines data and representation | HMRC/standards owner | Blocks implementation |
| What participant identifier, discovery and process rules apply? | Determines onboarding/routing | UK Peppol governance | Blocks adapter |
| Must every business use an access point, and who contracts/pays? | Commercial/customer/operational model | Product/legal/procurement | Blocks proposition |
| What role is allowed for legacy systems? | Migration and exclusions | HMRC/DBT | Blocks transition design |
| Is any HMRC reporting required beyond the invoice exchange? | Prevents missing or invented tax flow | HMRC | Blocks reporting only; current hypothesis is no leg |
| What lifecycle/acknowledgement/correction/cancellation semantics are mandated? | Product status and recovery | HMRC/Peppol governance | Blocks lifecycle mapping |
| Which Sage products/SME cohorts are first? | Data, UX, scale and support | Portfolio/product | Blocks rollout |
| Generic Peppol is mistaken for UK compliance | False compliance/rework | UK policy pack and activation gates | Proposed mitigation |
| Cost/onboarding burden harms SMEs | Adoption/support failure | Co-create low-friction onboarding and measure burden | Evidence/target open |

## Decisions

| Decision | Status | Owner/date |
|---|---|---|
| UK is a child country pack of PRD-SEI-227 | Confirmed by user request | 2026-08-10 |
| Update research conclusion: Peppol is the confirmed core-network direction | Confirmed 2026 official source | 2026-08-10 |
| Keep detailed UK policy/profile/reporting/lifecycle as gates | Confirmed evidence boundary | 2026-08-10 |
| Prepare reusable Peppol capability without claiming final UK compliance | Proposed product approach | TBD |

## Revision history

| Date | Change | Evidence/decision | Pull request |
|---|---|---|---|
| 2026-08-10 | Initial discovery child PRD; updated older topology-TBD research with 2026 Peppol announcement; added Confluence-safe gated roadmap visual | User request and official HMRC/DBT sources | |
| 2026-08-10 | Linked the consolidated parent visual atlas and compressed journey prose for research-stage readability | User direction | |
| 2026-08-10 | Approved for publication to existing page `866140019`; existing hierarchy preserved | User approval | |
| 2026-08-11 | Removed the embedded HTML heading and promoted the diagram title to a native Confluence heading | Confluence rendering feedback | |
