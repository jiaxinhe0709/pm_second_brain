---
id: PRD-SEI-230
title: UK E-Invoicing Compliance Pack
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-10
updated: 2026-09-23
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-223
  - PRD-SEI-226
  - PRD-SEI-231
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

Spain discovery provides reusable controls but not UK policy: capability-specific onboarding, client-scoped accountant authority, purpose-specific credentials, governed format/transformation packs, provider connection without legal-entity re-onboarding, independent send/receive/download capabilities and reconcile-before-retry. The UK pack must bind those controls to the final UK scope, GB/Northern Ireland transaction context where relevant, Peppol participant model, UK profile and Access Point evidence.

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

## Spain-informed UK capability decomposition

| Decision surface | Reusable platform behaviour | UK binding | Current evidence state |
|---|---|---|---|
| Legal subject | Separate Sage tenant/workspace, legal entity, tax/network identifiers and authority | UK VAT/legal-entity facts; preserve GB/XI and territorial transaction context where relevant to final policy | General VAT distinctions exist; mandate applicability contract open |
| Accountant/delegate | Evaluate firm-client relationship and authority per capability/client | UK authority for participant management, issue, receive and evidence access | Open; no portfolio-wide authority assumption |
| Capability readiness | Independent issue, receive, retrieve/download, participant and route readiness | Final inbound/outbound mandate symmetry, exemptions and transition | Direction confirmed; detailed legal scope open |
| Peppol participant | Model participant identifiers/capabilities independently from the Sage customer and provider connection | UK scheme identifiers, document/process identifiers, registration and migration rules | Open |
| Sending Access Point connection | Connect/change provider without recreating the legal entity or rewriting invoice history | Contracted legal entity, certified role/domain, credentials, environment, SLA, support and exit | Peppol direction confirmed; provider not selected |
| Recipient discovery | Store authoritative query inputs, source, freshness and supported capability | UK discovery/service-metadata policy | Open |
| Format and transformation | Govern syntax/version/profile/rules/mapping by effective route | Final UK profile, Peppol dataset/process and extensions | Open; generic Peppol is not UK compliance |
| Credentials and trust | Purpose-specific custody, expiry, rotation, revocation and historic evidence | Access Point transport trust, participant authority and any future invoice-signature policy remain separate | Partial/OpenPeppol framework only |
| Provider change | Reuse valid identity/authority and recheck affected connection/capabilities | Participant migration, SMP ownership, notice, overlap, portability and historical access | Open |
| Exchange lifecycle | Independent idempotency, correlation, recovery and original/canonical/rendering evidence | UK acknowledgements, corrections, cancellations and statuses | Open |

**Readiness priority:** assess product data and participant/onboarding gaps now, but keep live statutory activation disabled until the UK legal, profile, participant, Access Point and operational contracts are approved.

## Confirmed Peppol direction with policy-controlled activation

<!-- confluence-html-macro:start -->
<div class="uk-pack" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .uk-pack *{box-sizing:border-box}.uk-pack .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.uk-pack svg{display:block;width:1080px;height:700px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.uk-pack .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.uk-pack .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.uk-pack .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.uk-pack .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.uk-pack .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.uk-pack .title{fill:#172b4d;font-size:11px;font-weight:700}.uk-pack .copy{fill:#42526e;font-size:9px}.uk-pack .phase{fill:#172b4d;font-size:10px;font-weight:700;letter-spacing:.05em}.uk-pack .path{fill:none;stroke:#00875a;stroke-width:2}.uk-pack .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.uk-pack .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.uk-pack .path-warn{fill:none;stroke:#ff8b00;stroke-width:1.8;stroke-dasharray:6 4}.uk-pack .arrow{fill:#00875a}.uk-pack .arrow-g{fill:#6b778c}.uk-pack .arrow-r{fill:#de350b}.uk-pack .arrow-a{fill:#ff8b00}.uk-pack .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.uk-pack .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.uk-pack .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The target exchange spine is visible, but each amber gate requires official UK evidence and approval before a live mandate claim or mutation.</p>
  <svg viewBox="0 0 1080 700" role="img" aria-label="A UK seller product submits VAT invoice intent through scope, profile, participant identity and Access Point readiness gates. The approved route then uses Sage's selected certified sending Access Point, the Peppol Network, the buyer's receiving Access Point, which may be a different provider, and the buyer. Peppol is the network rather than the provider. Correctable validation failures return to the seller. Ambiguous delivery outcomes reconcile before retry. HMRC reporting and legacy-system routes remain inactive unless policy defines them. A roadmap shows 2026 co-creation, standards and legislation by end 2027 to 2028, and April 2029 mandate.">
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
    <rect x="858" y="70" width="190" height="92" rx="10" class="main"/><text x="878" y="99" class="title">Sage sending Access Point</text><text x="878" y="120" class="copy">Selected certified provider role</text><text x="878" y="139" class="copy">contract • authority • trust • adapter</text>
    <path d="M953 162 V202" class="path"/><polygon points="953,202 947,192 959,192" class="arrow"/>
    <rect x="858" y="204" width="190" height="76" rx="10" class="main"/><text x="878" y="232" class="title">Peppol Network</text><text x="878" y="253" class="copy">Shared rules • discovery • interoperability</text><text x="878" y="270" class="copy">Network, not Sage's provider</text>
    <path d="M953 280 V316" class="path"/><polygon points="953,316 947,306 959,306" class="arrow"/>
    <rect x="858" y="318" width="190" height="82" rx="10" class="main"/><text x="878" y="347" class="title">Receiving Access Point</text><text x="878" y="368" class="copy">Buyer's chosen certified provider</text><text x="878" y="386" class="copy">may differ from Sage's provider</text>
    <path d="M953 400 V432" class="path"/><polygon points="953,432 947,422 959,422" class="arrow"/>
    <rect x="858" y="434" width="190" height="78" rx="39" class="finish"/><text x="886" y="464" class="title">UK buyer receives</text><text x="884" y="485" class="copy">structured interoperable invoice</text>
    <path d="M858 473 H780" class="path"/><polygon points="780,473 790,467 790,479" class="arrow"/>
    <rect x="568" y="434" width="210" height="78" rx="10" class="main"/><text x="588" y="463" class="title">Evidence and product outcome</text><text x="588" y="484" class="copy">policy • both AP roles • network • audit</text>
    <polygon points="454,218 492,256 454,294 416,256" class="bad"/><text x="426" y="252" class="title">Invalid</text><text x="424" y="268" class="copy">correct data</text>
    <path d="M454 218 V178" class="path-alert"/><polygon points="454,178 448,188 460,188" class="arrow-r"/>
    <path d="M416 256 H200 V160" class="path-alert"/><polygon points="200,160 194,170 206,170" class="arrow-r"/>
    <polygon points="762,520 800,536 816,574 800,612 762,628 724,612 708,574 724,536" class="warn"/><text x="733" y="569" class="title">Unknown</text><text x="729" y="585" class="copy">reconcile delivery</text>
    <path d="M858 359 H820 V520 H762" class="path-warn"/><polygon points="762,520 772,514 772,526" class="arrow-a"/>
    <path d="M708 574 H673 V512" class="path-warn"/><polygon points="673,512 667,522 679,522" class="arrow-a"/>
    <rect x="36" y="434" width="230" height="82" rx="10" class="optional"/><text x="56" y="463" class="title">Legacy-system route</text><text x="56" y="484" class="copy">Role remains under stakeholder engagement</text><text x="56" y="501" class="copy">No permanent exception assumed</text>
    <path d="M266 475 H318" class="path-opt"/><polygon points="318,475 308,469 308,481" class="arrow-g"/>
    <rect x="320" y="434" width="228" height="82" rx="10" class="optional"/><text x="340" y="463" class="title">HMRC reporting leg</text><text x="340" y="484" class="copy">Inactive: no obligation inferred from</text><text x="340" y="501" class="copy">the e-invoice mandate announcement</text>
    <path d="M548 475 H568" class="path-opt"/><polygon points="568,475 558,469 558,481" class="arrow-g"/>
    <text x="30" y="642" class="phase">ROADMAP</text>
    <rect x="86" y="654" width="230" height="36" rx="10" class="main"/><text x="106" y="669" class="title">2026 • co-create + roadmap</text><text x="106" y="684" class="copy">Peppol core announced</text>
    <path d="M316 672 H424" class="path"/><polygon points="424,672 414,666 414,678" class="arrow"/>
    <rect x="426" y="654" width="230" height="36" rx="10" class="optional"/><text x="446" y="669" class="title">By end 2027–28</text><text x="446" y="684" class="copy">guidance • standards • specs • law</text>
    <path d="M656 672 H764" class="path-opt"/><polygon points="764,672 754,666 754,678" class="arrow-g"/>
    <rect x="766" y="654" width="230" height="36" rx="18" class="finish"/><text x="786" y="669" class="title">April 2029 • mandate</text><text x="786" y="684" class="copy">activate approved UK policy</text>
  </svg>
  <div class="notes"><div class="note"><strong>Peppol is the network</strong>Sage still needs a separately selected and approved sending Access Point provider.</div><div class="note"><strong>Independent providers</strong>The buyer's receiving Access Point can be operated by a different certified provider.</div><div class="note"><strong>Direction is not specification</strong>UK profile, participant, provider model and any HMRC reporting still require official artefacts.</div></div>
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
| Peppol Access Point | Peppol-certified service-provider role connecting a participant to the network; Sage's sending provider and the buyer's receiving provider may differ |
| Participant identity and capability lookup | Scheme plus SML/SMP or approved capability metadata used to discover the recipient's eligible receiving service |
| Customer/accountant | Maintains legal entity, VAT/business facts, authority and invoice corrections |
| Sage product | Captures intent/inbound invoices and displays compliance/delivery outcomes |
| UK pack owner | Owns official evidence, scope/profile versions, consultation and activation |
| HMRC/DBT | Policy/legislation/implementation owners |
| Selected sending Access Point provider | Future Sage-contracted legal entity and certified role providing network access, trust and delivery operations; no vendor is selected here |
| Receiving Access Point provider | Buyer's independently chosen certified provider; it need not be Sage's provider |
| Operations/support | Monitors onboarding, directory, access-point, delivery and reconciliation outcomes |

## Business scenarios

| ID | Scenario | Expected outcome | Exception/continuity |
|---|---|---|---|
| UK-S1 | Product performs readiness assessment before final specification | Data and Peppol capability gaps are visible; live mandate compliance remains disabled | No invented default profile/network mutation |
| UK-S2 | In-scope seller submits valid VAT invoice after activation | UK policy validates, recipient resolves and Sage's approved sending Access Point interoperates with the buyer's receiving Access Point | No eligible recipient/provider route blocks with guidance |
| UK-S3 | Buyer receives structured invoice | Original retained, tenant/recipient/trust/profile validated and imported once | Unsafe/unsupported invoice is quarantined |
| UK-S4 | Recipient is not discoverable | Product receives a distinct route/readiness outcome | No email/PDF fallback is inferred as compliant |
| UK-S5 | Access point times out after possible send | Delivery becomes outcome-unknown and reconciles before resend | No duplicate legal invoice |
| UK-S6 | Legacy system cannot interoperate | Approved transition/assisted route is applied only if final policy permits | Exception is effective-dated and audited |
| UK-S7 | Final guidance changes draft assumptions | New pack version activates prospectively after tests/approval | Earlier voluntary/pilot evidence remains intact |
| UK-S8 | Accountant submits a mixed client portfolio | Each client/participant/capability is evaluated independently | No firm-wide participant or invoice authority inference |
| UK-S9 | Participant is registered but Access Point/profile is not ready | Participant evidence remains valid while issue/receive readiness shows precise missing gates | No universal onboarded success |
| UK-S10 | Customer changes sending Access Point | Still-valid legal-subject/authority/participant evidence is reused and affected checks rerun | Existing/in-flight invoices retain original provider context |
| UK-S11 | Access Point credential expires or provider is suspended | Only affected new directions/environment stop with a named action | Historical evidence and unrelated capabilities remain available |
| UK-S12 | GB/Northern Ireland applicability is unresolved | Preserve territorial, goods/services and GB/XI facts and return an evidence gate | Do not guess one UK result |

## Business rules

| ID | Condition | Rule | Status/evidence |
|---|---|---|---|
| UK-BR1 | April 2029 mandate is evaluated | Apply only the final legally confirmed scope, effective date, exemptions and transitions | Mandate date/direction confirmed; detailed law open |
| UK-BR2 | Invoice is represented as compliant e-invoice | It must be structured as required by the final UK standard; PDF/Word/images/HTML/OCR alone are not sufficient under consultation definition | Confirmed consultation direction; final legal definition open |
| UK-BR3 | Network route is selected | Peppol is the core interoperability network, not the provider; bind Sage's approved sending Access Point separately and allow the buyer's receiving Access Point provider to differ | Four-corner distinction confirmed by OpenPeppol; detailed UK model open |
| UK-BR4 | Legacy system cannot interoperate | Apply no exception/fallback unless final policy explicitly permits it | Official engagement ongoing |
| UK-BR5 | Reporting is considered | Create no HMRC report leg without a separate official obligation/specification | Confirmed evidence boundary |
| UK-BR6 | Draft/final policy changes | Use approved effective-dated pack versions and preserve original invoice/route evidence | Proposed shared continuity rule |
| UK-BR7 | Product offers voluntary pre-mandate e-invoicing | Clearly distinguish network delivery from future statutory compliance and use only approved contracts | Proposed; legal/product approval required |
| UK-BR8 | A UK entity is prepared | Record legal subject, authority, participant, issue/receive/download and Access Point readiness separately | Spain learning adopted through PRD-SEI-227 |
| UK-BR9 | Accountant or batch acts | Evaluate every client/capability independently; firm role, client relationship or credential does not create participant or invoice authority | PRD-SEI-231; final UK model open |
| UK-BR10 | Sending Access Point changes | Preserve legal entity and still-valid authority/participant evidence; re-run only affected registration, connection, trust and operational checks | Proposed continuity rule |
| UK-BR11 | Access Point certificate is valid | Treat it as transport/service trust only; do not infer customer invoice-signing authority or participant-management consent | PRD-SEI-226 |
| UK-BR12 | Existing format/transformer is reused | Activate only the final UK profile/dataset and conformance pack; Spain, France or generic Peppol profiles are not UK defaults | Evidence gate |
| UK-BR13 | Transaction has GB/Northern Ireland context | Preserve territorial, goods/services and GB/XI identifier facts required by the final applicability policy; do not force one undifferentiated UK result before evidence | Existing VAT distinctions; mandate interpretation open |

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
| GB/Northern Ireland applicability | Open for the future mandate | Existing VAT invoicing/identifier distinctions must be preserved as inputs; final e-invoicing treatment requires HMRC evidence |

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [HMRC Transformation Roadmap update 2026](https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/annex-summary-of-hmrcs-planned-activities-listed-in-this-transformation-roadmap-progress-update) | April 2029 B2B/B2G VAT e-invoicing; roadmap/co-creation in 2026; full guidance, standards, technical specification and legislation by end 2027–28 | Primary official current roadmap; detail future | Phase/gates and no premature delivery claim |
| [UK tax update 2026](https://www.gov.uk/government/publications/summary-of-tax-update-2026-simplification-modernisation-and-fairness/tax-update-2026-simplification-modernisation-and-fairness-summary) | Peppol announced as core interoperability network; legacy-system role still under engagement | Primary official direction; implementation details absent | Peppol preparation and legacy gate |
| [Government e-invoicing consultation response](https://www.gov.uk/government/consultations/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector/outcome/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector-consultation-response), 2025 | 2029 mandate, structured system-to-system concept, unstructured exclusions, interoperability/network effects and small-business concerns | Primary policy response; predates 2026 Peppol announcement and final law | Problem, outcomes and open policy |
| [OpenPeppol interoperability framework](https://peppol.org/learn-more/peppol-interoperability-framework/), [membership/service-provider roles](https://peppol.org/join/) and [certified-provider register](https://peppol.org/members/peppol-certified-service-providers/), accessed 2026-09-23 | Peppol uses interoperating certified Access Points and capability lookup; AP and SMP are distinct possible service roles; sender and recipient select providers independently | Official network/governance evidence; role/certification does not prove UK scope, operating coverage or Sage selection | Separate network, AP/SMP/provider roles, adapter and recipient destination; verify exact entity, authority, service domain and coverage |
| [HMRC Northern Ireland VAT-invoice guidance](https://www.gov.uk/hmrc-internal-manuals/vat-northern-ireland-and-the-eu/vatnieu7440) and [GB/XI registration guidance](https://www.gov.uk/register-for-vat/selling-or-moving-goods-between-northern-ireland-and-the-eu), accessed 2026-09-23 | Existing VAT rules distinguish some Northern Ireland/EU goods transactions and use XI identifiers | Does not establish the future e-invoicing mandate treatment | Preserve territorial/goods-services/identifier facts and make final GB/NI handling a policy gate |
| Supplied research | UK architecture/details were TBD and a neutral core was recommended | Secondary synthesis; topology conclusion superseded in part by 2026 Peppol announcement | Evidence-change record and shared boundary |

## Proposed UK capability model

This is a consultation model, not an approved HMRC/UK Peppol interface or provider architecture.

| Record | Minimum information | Independence rule |
|---|---|---|
| UK legal-subject context | Sage tenant/workspace, legal entity, UK VAT identity, GB/XI/territorial facts where relevant, evidence source and effective period | Not the Peppol participant registration or Access Point account |
| Authority decision | Principal, direct/delegated actor, participant/invoice capability, environment, evidence, validity and result | Firm relationship or credential possession is insufficient |
| Peppol participant | Scheme/identifier, service metadata/capabilities, registration owner, provider/SMP reference, environment, effective period and status | Participant identity is not the Access Point provider or invoice recipient route observation |
| Capability readiness | `ISSUE`, `RECEIVE`, `RETRIEVE_DOWNLOAD`, participant registration and outbound/inbound connection results | One capability may be ready while another is blocked |
| Sending Access Point connection | Provider legal entity/role/service domain, contract, adapter, credential reference, environment, health, support and lifecycle | Separate from UK policy, participant and recipient's Access Point |
| Recipient capability observation | Queried participant identity, document/process identifiers, endpoint/provider evidence, source, freshness and result | Snapshot used by a route plan, not timeless customer configuration |
| UK format policy | Syntax/version, UK profile/dataset, extensions, validators, mappings and effective period | Peppol network support alone does not approve the UK invoice profile |
| Exchange plan/evidence | Immutable scope, representation, participant/discovery snapshot, both AP roles, network, adapter/trust versions, correlation and outcome | Current provider/profile changes never rewrite an earlier invoice |

### Proposed readiness and execution states

| Dimension | States | Meaning |
|---|---|---|
| Capability readiness | `NOT_REQUESTED`, `EVIDENCE_REQUIRED`, `READY_WITH_LIMITATIONS`, `READY`, `SUSPENDED` | Per legal entity and direction/capability |
| Participant registration | `NOT_REGISTERED`, `PENDING`, `TEST_READY`, `ACTIVE`, `CHANGE_PENDING`, `SUSPENDED`, `RETIRED` | Proposed until final UK governance is known |
| Access Point connection | `NOT_CONFIGURED`, `CONFIGURING`, `TESTING`, `READY`, `EXPIRING`, `DEGRADED`, `SUSPENDED`, `RETIRED` | Provider/adapter operational readiness |
| Delivery | `PLANNED`, `VALIDATED`, `SUBMITTED`, `ACKNOWLEDGED`, `DELIVERED`, `REJECTED`, `OUTCOME_UNKNOWN`, `RECONCILING`, `FAILED_TERMINAL` | Exact meanings require final UK/Peppol profile |

## Detailed journeys

### J1 — Pre-mandate product and entity readiness

1. Product runs a non-mutating assessment for a selected UK legal entity or accountant portfolio.
2. Sage captures VAT/legal-entity and territorial transaction facts, requested directions and current data coverage without claiming statutory compliance.
3. Authority and product permission are evaluated per client/capability.
4. The pack assesses candidate participant data, invoice semantics, inbound/outbound, original/download and operational readiness against explicitly inactive evidence gates.
5. Results identify reusable platform capability, country evidence required and accountable action owner.

### J2 — Connect a sending Access Point after policy approval

1. An authorised actor selects an approved provider legal entity/role and eligible UK service domain; Peppol is displayed as the network, not the provider.
2. Sage reuses the verified legal subject and authority evidence, then creates an isolated TEST connection.
3. Participant/AP/SMP responsibilities, credentials, supported dataset/processes, callbacks/queries, limits, support and exit terms are verified.
4. Conformance and operational scenarios pass before a separate production connection becomes ready.
5. Issue and receive readiness are activated independently according to final UK policy.

### J3 — Register or associate a Peppol participant

1. The approved UK policy resolves the permitted identifier scheme and participant authority for the legal entity.
2. Sage or the approved responsible provider creates/associates the participant and publishes only supported document/process capabilities.
3. Registration evidence, owner, provider/SMP, environment, effective period and current status are retained.
4. Participant success does not automatically make invoice issue/receive ready; format, connection and product checks remain independent.

### J4 — Send and receive after activation

1. The effective UK policy decides scope and resolves the exact UK representation/profile.
2. Outbound planning queries current recipient capability, freezes both AP roles/network/adapter/trust evidence and validates before submission.
3. A possible-send timeout enters outcome unknown and reconciles before retry.
4. Inbound processing verifies tenant/recipient, source/trust, profile and duplication, preserves original bytes and makes the invoice available once.

### J5 — Change Access Point provider

1. An authorised actor configures a replacement connection without recreating the Sage legal entity.
2. Participant/SMP ownership, transfer/notice, credentials, supported capabilities, test evidence, support and exit conditions are resolved under the approved UK rules.
3. In-flight invoices remain with their frozen original provider/route; ambiguous outcomes reconcile before cutover completion.
4. The new provider activates prospectively and historical access/evidence from the old provider remains governed.

### J6 — Credential expiry or provider suspension

1. Purpose-specific monitoring identifies the Access Point/adapter credential and affected directions/environments.
2. The named owner renews/rotates and proves connectivity in the correct environment.
3. Unsafe new use is blocked narrowly; no transport certificate is treated as customer signing authority.
4. Historical invoices, participant evidence and unrelated capabilities remain accessible according to policy.

## Journey summary

| Journey | Spine | Required exception/continuity |
|---|---|---|
| Prepare | Map VAT data → assess Peppol/onboarding gaps → store inactive hypotheses and gates | No mandate claim or live mutation before approved official artefacts |
| Target after activation | Submit → evaluate final policy → validate UK profile → discover recipient capability → bind Sage's sending Access Point → exchange through Peppol to the buyer's Access Point → import once | Missing route/provider blocks; both provider roles and raw acknowledgements remain preserved |
| Correct/recover/change | Correct before send; timeout after possible send → outcome unknown → reconcile before retry | New pack versions apply prospectively; historical context is never rewritten |

## Failure and recovery matrix

| Failure or change | Required behaviour | Prohibited outcome |
|---|---|---|
| Final UK scope/profile evidence absent | Keep readiness assessment non-mutating and identify the owning gate | Claiming statutory compliance from Peppol connectivity |
| Accountant lacks one client/participant capability | Deny only that item/capability with non-enumerating evidence; continue independent safe items | Portfolio-wide authority or client-data leakage |
| Participant active but AP/profile not ready | Preserve participant record and block only dependent issue/receive capability | Collapsing states into one onboarded flag |
| Recipient capability missing/stale/conflicting | Refresh under approved policy or stop unrouteable with evidence | Guessing an endpoint or compliant email/PDF fallback |
| Profile/mapping cannot preserve required meaning | Stop before dispatch, retain diagnostics and require correction/approved mapping | Silent loss or use of another country's profile |
| AP credential expired/revoked/wrong-purpose | Block only affected connection/direction and require renewal/reselection | Treating transport trust as customer signature/authority |
| Timeout after possible Access Point submission | Enter outcome unknown and reconcile provider/network evidence before retry | Blind duplicate dispatch |
| Provider changes while invoice is in flight | Freeze original provider/route plan, reconcile ambiguity and activate replacement prospectively | Moving or re-signing an in-flight invoice silently |
| GB/Northern Ireland policy input unresolved | Preserve facts and return unresolved/evidence-required result | Applying a guessed uniform UK policy |
| Internal persistence failure after external success | Recover from durable correlation and provider evidence | Creating a second legal invoice operation |

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
| UK-FR6 | The Peppol route must use approved UK participant identifier schemes, discovery/service metadata, document/process identifiers and transport/security profile; Sage's provider connection must separately identify the contracted legal entity, Access Point role, applicable authority/certification evidence, adapter/configuration and credential version. |
| UK-FR7 | Recipient resolution must record query identity, source, evidence time, recipient service/capability and receiving Access Point evidence without treating Peppol or the receiving provider as Sage's selected provider; missing eligibility must block dispatch. |
| UK-FR8 | Inbound must verify intended tenant/recipient, source/trust, supported UK profile and duplication, retain the original representation and expose safe validation/import outcome. |
| UK-FR9 | Every delivery must record representation/profile, participant/service, Peppol as network, the selected sending Access Point provider and observed receiving Access Point provider, adapter/configuration version, message/correlation identity, acknowledgements and outcome. |
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

### Onboarding, participant, connection, format and trust

| ID | Requirement |
|---|---|
| UK-FR18 | Onboarding must create separate legal-subject, authority, participant, issue, receive, retrieve/download and Access Point readiness records; it must not use one UK `ONBOARDED` flag. |
| UK-FR19 | The participant model must support the identifier scheme(s), participant capabilities, registration owner/provider/SMP, environment, effective period and status selected by final UK governance without hard-coding one scheme. |
| UK-FR20 | Direct and accountant/batch pathways must use the same client-level policies; every participant or invoice operation must bind the represented legal entity, actor/delegate, capability, environment, authority evidence and effective period. |
| UK-FR21 | Connecting or changing a sending Access Point must reuse still-valid legal-subject/authority evidence, create isolated test/production connection context and re-run only participant, provider, credential, format and operational checks affected by the change. |
| UK-FR22 | Issue, receive and retrieve/download readiness must be evaluated independently by product, legal entity, profile, participant, Access Point and environment; support for one operation must not imply another. |
| UK-FR23 | Credential readiness must distinguish Access Point transport/service identity, Sage workload identity, participant-management authority and any future invoice-signature/seal policy; validity for one purpose must not satisfy another. |
| UK-FR24 | Recipient capability observations must record query identifier/scheme, requested document/process, returned endpoint/capability, source, evidence time/freshness and result and must be refreshed according to the approved UK policy before dispatch. |
| UK-FR25 | The format registry must govern exact syntax/version, UK profile/dataset/process, extensions, validators, mappings, route and effective period; Peppol BIS or any existing country profile must not be assumed until officially selected. |
| UK-FR26 | Provider change must preserve immutable origin/provider/AP/participant context for in-flight and historical invoices, reconcile ambiguous old-provider outcomes and activate the replacement prospectively under approved transfer/rollback rules. |
| UK-FR27 | Original, canonical and human-readable artefacts must remain correlated but distinctly labelled with profile/version, hash, source and transformation/rendering provenance. |
| UK-FR28 | Production activation must require a versioned evidence manifest covering legal scope, GB/Northern Ireland treatment, authority, profile/rules, participant/discovery, provider/AP/SMP roles, trust, environments, limits, lifecycle, retention, operations, switching/exit and rollback. |
| UK-FR29 | The pack must preserve territory, goods/services and applicable GB/XI identifier facts needed by the final policy and must not collapse Great Britain and Northern Ireland into one applicability result before official evidence supports it. |
| UK-FR30 | Candidate shared transformation and validation capability must pass the exact UK profile/dataset, semantic-loss, version-coexistence, security and operational conformance corpus before activation. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| UK-NFR1 | Legal-entity authority, Peppol participant, tenant, environment, invoice and credential boundaries must be isolated and least-privileged. |
| UK-NFR2 | Access-point keys/certificates/secrets must use approved custody, rotation, revocation and non-disclosure controls. |
| UK-NFR3 | Original invoices, transformations and network evidence must use approved integrity, retention, deletion and legal-hold rules; final periods are open. |
| UK-NFR4 | UK policy/profile/identifier/network changes require official provenance, regression fixtures, owner approval, effective date, compatibility analysis and rollback. |
| UK-NFR5 | Availability, throughput, delivery latency, directory freshness, payload and backlog targets require official network/access-point evidence plus product baselines. |
| UK-NFR6 | Observability must distinguish product data, UK policy, Sage platform, participant discovery, sending-provider, Peppol-network, receiving-provider and recipient faults without exposing unnecessary invoice data. |
| UK-NFR7 | Onboarding and correction experiences must be accessible, localisable and usable by SMEs/accountants; success criteria require user research. |
| UK-NFR8 | Accountant portfolio/batch processing must enforce client isolation, fair scheduling, durable item state and independently recoverable participant/readiness results. |
| UK-NFR9 | Participant, provider and credential monitoring must detect expiry, revocation, compromise, capability loss and dependency risk with named remediation/renewal owners. |
| UK-NFR10 | Every policy, participant, discovery, profile, mapping, provider, adapter and credential decision used by an invoice must be reproducible from retained versioned evidence. |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| UK-AC1 | Given final UK legal/technical artefacts are not approved, when live mandate activation is attempted, then the pack blocks external mutation and lists the missing gates. |
| UK-AC2 | Given readiness assessment runs before activation, when a product lacks required semantic/participant data, then gaps are reported without claiming non-compliance or sending data. |
| UK-AC3 | Given Sage's approved sending Access Point and a buyer using another eligible receiving Access Point, when recipient discovery succeeds, then the approved UK profile is delivered once through Peppol and both provider roles are preserved separately from the network. |
| UK-AC4 | Given a PDF-only invoice, when classified under current policy direction, then it is not labelled a compliant structured UK e-invoice. |
| UK-AC5 | Given recipient discovery returns no eligible UK service, when dispatch is requested, then no network mutation occurs and actionable readiness evidence is returned. |
| UK-AC6 | Given the access point times out after possible send, when recovery runs, then the outcome reconciles before retry and no preventable duplicate is produced. |
| UK-AC7 | Given no approved HMRC reporting obligation exists, when an invoice is delivered, then the service creates no authority-report leg or reporting-success claim. |
| UK-AC8 | Given a later UK pack version changes scope/profile, when an older invoice is inspected, then its original policy, profile, participant, route and acknowledgement evidence remain unchanged. |
| UK-AC9 | Given a UK legal entity has been verified but no participant or Access Point connection exists, when readiness is displayed, then identity readiness is visible while issue/receive remain action-required rather than generically onboarded. |
| UK-AC10 | Given an accountant portfolio contains clients with different participant authority, when onboarding runs, then only authorised client/capability combinations progress and no firm-wide participant authority is inferred. |
| UK-AC11 | Given a participant registration is active but outbound profile or Access Point testing is incomplete, when issue readiness is requested, then issue remains blocked while the participant record remains valid. |
| UK-AC12 | Given an Access Point transport certificate is valid, when customer invoice-signing readiness is requested, then the certificate is rejected as wrong-purpose unless a separate approved UK signature policy exists. |
| UK-AC13 | Given a recipient was discoverable earlier but current evidence is stale or no longer supports the required process, when dispatch is requested, then the system refreshes or blocks rather than guessing the route. |
| UK-AC14 | Given the sending Access Point provider changes, when the replacement activates, then the legal entity is not re-created and prior/in-flight invoices retain their original provider and route context. |
| UK-AC15 | Given an invoice concerns facts potentially relevant to Northern Ireland treatment, when final applicability is not evidenced, then the pack preserves GB/XI, territory and goods/services facts and returns an unresolved gate rather than a guessed UK result. |
| UK-AC16 | Given a generic Peppol BIS or transformer works in another country, when UK activation is attempted, then it remains blocked until the exact UK profile/dataset and semantic-preservation corpus pass. |
| UK-AC17 | Given original, canonical and rendered artefacts exist, when an authorised user downloads them, then their roles, hashes, profiles and provenance are distinguishable. |

## Goal traceability

| Goal | Primary requirements | Demonstration |
|---|---|---|
| UK-G1 — April 2029 readiness | UK-FR1–UK-FR5, UK-FR18, UK-FR22, UK-FR28–UK-FR30; UK-NFR4, UK-NFR5, UK-NFR10 | UK-AC1–UK-AC3, UK-AC9, UK-AC15–UK-AC17 |
| UK-G2 — Reusable governed Peppol | UK-FR6, UK-FR7, UK-FR9, UK-FR16, UK-FR19, UK-FR21, UK-FR23–UK-FR26; UK-NFR2, UK-NFR4, UK-NFR9–UK-NFR10 | UK-AC3, UK-AC5, UK-AC8, UK-AC11–UK-AC14, UK-AC16 |
| UK-G3 — Customer onboarding and exchange | UK-FR4–UK-FR10, UK-FR13–UK-FR15, UK-FR18–UK-FR27; UK-NFR6–UK-NFR10 | UK-AC2–UK-AC6, UK-AC9–UK-AC14, UK-AC17 |
| UK-G4 — Low-friction/legacy transition | UK-FR4, UK-FR11, UK-FR17, UK-FR20–UK-FR22, UK-FR26; UK-NFR7–UK-NFR8 | UK-AC1, UK-AC2, UK-AC10, UK-AC14 |
| UK-G5 — Explicit uncertainty | UK-FR1, UK-FR3, UK-FR12, UK-FR25, UK-FR28–UK-FR29; UK-NFR4 | UK-AC1, UK-AC7, UK-AC8, UK-AC15–UK-AC16 |

## Metrics, rollout and gates

| Measure | Baseline/target status | Owner |
|---|---|---|
| UK product semantic-data readiness | Baseline per product required | Portfolio/product |
| Customer/participant onboarding completion and time | User research and access-point model required | Product |
| Recipient discovery success by cohort | Baseline after UK model/test network exists | Operations |
| First-pass profile validation and correction completion | Profile artefacts required | Product + UK pack owner |
| Duplicate/outcome-unknown delivery rate and age | Access-point SLA/evidence required | Operations |
| SME usability/support burden | Research baseline/target required | Product research/support |
| Legal-entity vs participant vs issue/receive readiness | Exposes exact onboarding friction without a false single success state | UK pack owner + product |
| Accountant batch outcomes by client/capability | Measures authority and participant-readiness gaps while protecting isolation | Product/operations |
| Participant/discovery evidence freshness and failure reasons | Measures route confidence and governance health | Platform operations |
| Access Point credential expiry/rotation risk | Prevents avoidable provider outage | Security/provider operations |
| Provider-change completion and disrupted in-flight work | Validates migration without legal-entity re-onboarding | Platform operations |

Rollout gates:

1. Name UK policy/compliance, portfolio/product, architecture, security/privacy and operations owners.
2. Participate in HMRC/DBT/software-industry co-creation and maintain a dated evidence register.
3. Select a bounded reference product/cohort and establish legal-entity/accountant, semantic, invoice-direction, volume, support and GB/Northern Ireland transaction baselines.
4. Run non-mutating readiness across legal subject, participant data, issue, receive, retrieve/download and Access Point capabilities.
5. Approve final legislation, guidance, scope/exemptions/transition, GB/Northern Ireland treatment and enforcement interpretation.
6. Obtain UK invoice profile/schemas/code lists/validators, Peppol participant/discovery/process/transport rules and approved test environment.
7. Select and approve the exact sending Access Point legal entity and role, authority/certification/service-domain scope, operating coverage, adapter and credential model, participant/SMP registration ownership, SLA, security, privacy, retention, support, switching, exit and historical access.
8. Qualify shared transformation/validation against the exact UK profile/dataset and semantic-loss corpus.
9. Demonstrate direct/accountant onboarding, participant registration, inbound/outbound, validation correction, stale/missing recipient, credential expiry, duplicate, unknown outcome, provider switch and historical continuity.
10. Pilot with explicit voluntary/statutory messaging, kill/rollback criteria and small-business support before April 2029 expansion.

## Risks and consultation questions

| Risk/question | Why it matters | Owner | Blocks/current hypothesis |
|---|---|---|---|
| What is final legal scope, including B2B/B2G, exemptions and transition? | Determines applicability and cohort | HMRC/UK compliance | Blocks live policy |
| What UK semantic/syntax profile and validation artefacts apply? | Determines data and representation | HMRC/standards owner | Blocks implementation |
| What participant identifier, discovery and process rules apply? | Determines onboarding/routing | UK Peppol governance | Blocks adapter |
| Who contracts and pays for sending/receiving Access Point service, and who owns participant/capability registration and migration? | Commercial, onboarding, switching and continuity model | Product/legal/procurement | Blocks proposition |
| What role is allowed for legacy systems? | Migration and exclusions | HMRC/DBT | Blocks transition design |
| Is any HMRC reporting required beyond the invoice exchange? | Prevents missing or invented tax flow | HMRC | Blocks reporting only; current hypothesis is no leg |
| What lifecycle/acknowledgement/correction/cancellation semantics are mandated? | Product status and recovery | HMRC/Peppol governance | Blocks lifecycle mapping |
| How does the future regime apply across Great Britain and Northern Ireland, including goods/services and GB/XI identifiers? | Prevents one UK rule from masking existing VAT distinctions | HMRC/UK compliance | Blocks applicability/profile design; preserve facts until answered |
| Which operations may an accountant/delegate perform for participant registration, issue, receive and evidence access, and how is authority verified/revoked? | Prevents firm relationship or certificate possession becoming universal authority | HMRC/UK legal/product | Blocks accountant production onboarding |
| Does the selected provider own AP only, AP plus SMP, or participant registration through another role, and how is each migrated? | Determines onboarding, directory control and exit | UK governance/provider/procurement | Blocks connection/switching design |
| Are invoice signatures/seals required in addition to Peppol transport trust for any UK route/profile? | Determines certificate custody and validation | HMRC/security/standards owner | Blocks signature design; do not copy Spain |
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
| Treat Peppol, the selected sending Access Point provider, the receiving Access Point provider and Sage adapter as separate route concepts; select no vendor in this PRD | Confirmed by user context and official OpenPeppol model | 2026-08-11 |
| Use capability-specific onboarding and keep legal entity, participant and Access Point connection separate | Proposed from Spain reuse and Peppol role boundaries | 2026-09-23 |
| Treat Great Britain/Northern Ireland applicability as an explicit policy gate while preserving territorial and GB/XI facts | Proposed evidence-led boundary | 2026-09-23 |

## Revision history

| Date | Change | Evidence/decision | Pull request |
|---|---|---|---|
| 2026-08-10 | Initial discovery child PRD; updated older topology-TBD research with 2026 Peppol announcement; added Confluence-safe gated roadmap visual | User request and official HMRC/DBT sources | |
| 2026-08-10 | Linked the consolidated parent visual atlas and compressed journey prose for research-stage readability | User direction | |
| 2026-08-10 | Approved for publication to existing page `866140019`; existing hierarchy preserved | User approval | |
| 2026-08-11 | Removed the embedded HTML heading and promoted the diagram title to a native Confluence heading | Confluence rendering feedback | |
| 2026-08-11 | Reworked the Peppol flow into a four-corner route and separated network, sending/receiving providers and Sage adapter across definitions, evidence, requirements and acceptance | User context and official OpenPeppol sources | |
| 2026-09-23 | Applied Spain learnings without importing Spanish policy; added legal-subject/participant/authority/readiness decomposition, accountant batch, AP/SMP connection roles, provider change, purpose-specific trust, UK profile gates, GB/Northern Ireland applicability inputs, detailed journeys and acceptance | Stakeholder direction; PRD-SEI-227/223/226/231; current HMRC/OpenPeppol evidence | |
