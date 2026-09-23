---
id: PRD-SEI-229
title: Ireland E-Invoicing Compliance Pack
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
  page_id: "866140021"
  title: 2.6 E-Invoicing Ireland
  layout: two_left_sidebar
  toc: true
---

# Ireland E-Invoicing Compliance Pack

## Decision summary

Define Ireland as a phased country pack on PRD-SEI-227. Phase One begins on 1 November 2028: Irish VAT-registered large corporates in Revenue's defined cohort issue EN 16931 e-invoices for domestic B2B transactions and report a subset of invoice data to Revenue, while all Irish businesses must be able to receive structured e-invoices.

The product must model invoice delivery and Revenue reporting as separate correlated obligations. It must not invent the transport network, detailed syntax/profile, reporting payload, timing, acknowledgement, correction, identity or lifecycle rules that Revenue has not yet published.

Spain discovery provides reusable product controls but not Irish policy: capability-specific onboarding, client-scoped accountant authority, purpose-specific credentials, governed format/transformation packs, provider connection without recreating the legal entity, independent external legs and reconcile-before-retry. Ireland must bind those controls to its own Revenue cohort, identity, delivery, reporting, format and trust evidence.

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

## Spain-informed Ireland capability decomposition

| Decision surface | Reusable platform behaviour | Ireland binding | Current evidence state |
|---|---|---|---|
| Legal subject | Separate Sage tenant/workspace, legal entity and statutory identity | Irish VAT registration, Irish establishment/fixed establishment and Revenue-managed cohort | Phase One definition confirmed; authoritative machine-verification method open |
| Accountant/delegate | Evaluate firm-client relationship and authority per capability/client | Irish representation mechanism for issue, receive, report and evidence access | Open; no portfolio-wide authority assumption |
| Capability readiness | Independent issue, receive, report, retrieve/download and route states | All configured Irish businesses need receive readiness; only in-scope large corporates require issue/report readiness in Phase One | Confirmed direction; product/channel activation open |
| Delivery connection | Connect a provider/network route without recreating the legal entity | Irish delivery network, recipient discovery, provider and switching rules | Open |
| Revenue reporting connection | Separate authority adapter, authentication and status from buyer delivery | Revenue report subset, interface, credentials, timing and acknowledgements | Obligation and real-time direction confirmed; detailed contract open |
| Format and transformation | Govern syntax/version/profile/rules/mapping by effective route | EN 16931 confirmed; Irish syntax, CIUS, extensions and report representation open | Partial |
| Credentials and trust | Purpose-specific custody, expiry, rotation, revocation and historic evidence | Delivery authentication, Revenue authentication and any invoice signature/seal are separate policies | Open; Spanish signature requirements do not apply by inference |
| Provider change | Reuse still-valid identity/authority; recheck only affected connection/capabilities | Registration transfer, notice, portability, overlap, exit and historical access | Open |
| Exchange lifecycle | Independent idempotency, correlation and recovery per external leg | Buyer delivery and Revenue report never inherit each other's result | Product requirement proposed from confirmed dual obligation |

**Delivery-depth priority:** first prove receive readiness across the selected Irish product estate, then prove issue plus reporting for a bounded Phase One large-corporate cohort. The shared model must support both without a universal `ONBOARDED` state.

## Phase One separates recipient delivery from Revenue reporting

<!-- confluence-html-macro:start -->
<div class="ie-pack" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .ie-pack *{box-sizing:border-box}.ie-pack h2{margin:0;color:#172b4d;font-size:18px}.ie-pack .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.ie-pack svg{display:block;width:1080px;height:560px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.ie-pack .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.ie-pack .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.ie-pack .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.ie-pack .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.ie-pack .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.ie-pack .title{fill:#172b4d;font-size:11px;font-weight:700}.ie-pack .copy{fill:#42526e;font-size:9px}.ie-pack .phase{fill:#172b4d;font-size:10px;font-weight:700;letter-spacing:.05em}.ie-pack .path{fill:none;stroke:#00875a;stroke-width:2}.ie-pack .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.ie-pack .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.ie-pack .path-warn{fill:none;stroke:#ff8b00;stroke-width:1.8;stroke-dasharray:6 4}.ie-pack .arrow{fill:#00875a}.ie-pack .arrow-g{fill:#6b778c}.ie-pack .arrow-r{fill:#de350b}.ie-pack .arrow-a{fill:#ff8b00}.ie-pack .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.ie-pack .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.ie-pack .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
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
| IE-S8 | Accountant submits a mixed portfolio | Each client/capability is evaluated independently and authorised items continue | No batch-wide cohort, authority or credential inference |
| IE-S9 | Business changes delivery/reporting provider | Still-valid legal-subject/authority evidence is reused and affected readiness is retested | Existing and in-flight invoices retain original connection context |
| IE-S10 | Delivery or Revenue credential expires | Only dependent new operations stop with a named remediation owner | Historical evidence and unrelated capabilities remain available |
| IE-S11 | Non-issuer business has receive readiness only | Inbound invoice is accepted/imported safely without issue/report readiness | Product does not show a false universal onboarding failure |

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
| IE-BR8 | An Irish entity is prepared | Record identity, authority and receive/issue/report/download readiness independently | Spain learning adopted through PRD-SEI-227 |
| IE-BR9 | Accountant or batch acts | Evaluate every client/capability independently; no firm role, relationship or credential creates universal authority | PRD-SEI-231; Irish legal mechanism open |
| IE-BR10 | Delivery or Revenue connection changes | Reuse still-valid legal-subject/authority evidence and recheck only affected provider, credential, format and operational readiness | Proposed continuity rule |
| IE-BR11 | Credential/certificate is required | Resolve purpose, custodian, environment, validity and dependency separately for delivery authentication, Revenue authentication and any future invoice signature/seal | PRD-SEI-226; Irish trust policy open |
| IE-BR12 | Existing transformer/profile is considered | Qualify the exact Irish syntax/profile/rules and semantic preservation; Spanish or French validation packs are never Ireland defaults | Shared DTS/format governance |

## Scope and capability evidence

| Capability | State | Pack position |
|---|---|---|
| Phase/cohort applicability | Partially confirmed | Phase One date/large-corporate definition confirmed; detailed transaction/exemption rules open |
| Inbound | Confirmed direction | All businesses receive from Phase One; product/channel/profile scope open |
| Outbound | Confirmed direction | Phase One large corporates domestic B2B |
| Semantic standard | Confirmed | EN 16931; CIUS/syntax/profile version open |
| Transport/recipient resolution | Unknown | Must remain adapter/configuration gate |
| Revenue reporting | Confirmed obligation, technical detail unknown | Separate real-time report direction; exact subset, trigger/deadline, API, acknowledgement and correction open |
| Lifecycle/status | Unknown/proposed | Shared technical events plus official mapping when published |
| Identity/authentication | Partial/open | VAT registration, Irish establishment and LCD cohort define Phase One scope; verification, representation, network and Revenue trust models require official artefacts |
| Phase Two | Direction confirmed, detail open | Effective policy placeholder only |
| ViDA Phase Three | Confirmed EU date/direction | National integration artefacts open |

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [Revenue: Phase One large corporates](https://www.revenue.ie/en/vat/vida-vat-modernisation/large-corporates-vat-modernisation.aspx), accessed 2026-09-23 | 2028-11-01, large-corporate definition, domestic B2B issue/report subset, all businesses receive, EN 16931 and no PDF/scans; Revenue will notify in-scope large corporates and publish technical material | Primary official current page; notification evidence format and technical contract are not yet published | Scope, onboarding/cohort evidence, inbound asymmetry, semantic requirement and gates |
| [Revenue: VAT Modernisation timeline](https://www.revenue.ie/en/vat/vida-vat-modernisation/vat-modernisation-timeline.aspx), accessed 2026-09-23 | Confirms Phase One/Two/Three sequencing and receive readiness across phases | Primary official current page; detailed transaction rules remain open | Effective-dated capability policy |
| [Revenue: VAT Modernisation — Implementation of eInvoicing](https://www.revenue.ie/en/vat/documents/implementation-einvoicing.pdf), 2026 | Three phases; structured invoices plus key data reported to Revenue in real time; detailed guidance/specifications will follow stakeholder engagement | Primary official overview; exact trigger/deadline/API and final legislation remain open | Phase model, separate report connection and evidence gate |
| [Revenue: initial consultation report](https://www.revenue.ie/en/corporate/documents/consultations/public-consultation.pdf), 2024 | Stakeholders raised technical engagement, business-model flexibility, security and alignment with commercial invoicing/ViDA | Official consultation synthesis, not final Revenue policy | Consultation scenarios and non-invention rule |
| [European Commission ViDA 2026 Work Programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en) | 2030-07-01 cross-border B2B DRR based on mandatory e-invoicing | Primary EU direction; implementation work continues | Phase Three compatibility/gate |
| Supplied research | Reusable reporting framework and neutral core hypothesis | Secondary synthesis; technical specifics not official | Shared/country boundary |

## Proposed Ireland capability model

This is a product model for consultation, not an approved Revenue interface or architecture.

| Record | Minimum information | Independence rule |
|---|---|---|
| Irish legal-subject context | Sage tenant/workspace, legal entity, VAT identity, establishment/fixed-establishment evidence, source and effective period | Not the delivery provider account or Revenue credential |
| Phase/cohort observation | Revenue cohort, source/notification evidence, observed/effective time, status and review owner | Cohort evidence informs scope; it does not by itself activate a connection |
| Authority decision | Principal, direct/delegated actor, capability, environment, evidence, validity and result | Accountant relationship or credential possession is insufficient |
| Capability readiness | `RECEIVE`, `ISSUE`, `REPORT`, `RETRIEVE_DOWNLOAD`, delivery route and Revenue route results with limitations/actions | One capability may be ready while another is blocked |
| Delivery connection | Network/channel, provider legal entity/role, external participant/account, adapter, credential reference, environment and health | Separate from the Revenue reporting connection |
| Revenue reporting connection | Revenue account/registration if required, adapter, authentication/authority reference, environment, schema version and health | Separate from buyer delivery and invoice format readiness |
| Format policy | EN 16931 binding, syntax/version, Irish CIUS/extensions, validation artefacts, mapping and effective period | EN 16931 alone does not select a syntax or live profile |
| Invoice compliance plan | Immutable scope result, representation, delivery leg, Revenue-report leg, policy/connection/trust versions and correlations | Frozen per invoice attempt; later configuration does not rewrite it |
| External-leg evidence | Intended/observed state, request/idempotency ID, raw acknowledgement/reason, timestamps and safe next action | Delivery and reporting evidence remain independent |

### Proposed readiness and execution states

| Dimension | States | Meaning |
|---|---|---|
| Capability readiness | `NOT_REQUESTED`, `EVIDENCE_REQUIRED`, `READY_WITH_LIMITATIONS`, `READY`, `SUSPENDED` | Per legal entity and capability |
| Connection | `NOT_CONFIGURED`, `CONFIGURING`, `TESTING`, `READY`, `EXPIRING`, `DEGRADED`, `SUSPENDED`, `RETIRED` | Separate delivery and Revenue connections |
| External leg | `PLANNED`, `VALIDATED`, `SUBMITTED`, `ACKNOWLEDGED`, `COMPLETED`, `REJECTED`, `OUTCOME_UNKNOWN`, `RECONCILING`, `FAILED_TERMINAL` | Independent state for buyer delivery and Revenue reporting |

## Detailed journeys

### J1 — Prepare one Irish legal entity

1. Customer or authorised accountant selects the Sage legal entity and requested capabilities.
2. Sage records Irish VAT identity, establishment facts and any Revenue Phase One cohort evidence without claiming an unconfirmed external registration.
3. Authority is evaluated independently for receive configuration, issue, Revenue reporting and evidence access.
4. The product assesses EN 16931 data coverage and creates separate readiness results for receive, issue, report and retrieve/download.
5. Delivery and Revenue connections remain `NOT_CONFIGURED` until official contracts and an approved provider/adapter exist.

**Result:** the entity can be data-ready or receive-ready without being falsely marked ready to issue or report.

### J2 — Onboard an accountant portfolio

1. The firm submits an idempotent portfolio batch containing stable client references and requested capabilities.
2. Sage validates the batch envelope, then evaluates the current firm-client relationship, Irish subject facts and capability authority for each client independently.
3. Each client receives its own cohort observation, readiness findings and action owner; one failure does not fail or disclose another client.
4. A reusable credential or evidence reference applies only where its verified scope covers the named client and operation.
5. Aggregate progress reports counts while authorised users retrieve client-level detail.

### J3 — Issue and report a Phase One invoice

1. The effective policy confirms the issuer cohort and domestic B2B scope.
2. The active format policy validates the final Irish representation before external mutation.
3. An immutable plan freezes the delivery connection, Revenue connection, representation and trust/evidence versions.
4. Buyer delivery and Revenue reporting execute as separately correlated, idempotent legs.
5. The product displays both outcomes; failure or uncertainty on one leg never repeats or overwrites the other.

### J4 — Receive an invoice for a non-issuer business

1. The delivery channel identifies an invoice addressed to a configured Irish legal entity.
2. Sage verifies recipient/tenant, source/trust and activated Irish profile, preserves the original representation and deduplicates observations.
3. Canonical conversion and rendering remain labelled derivatives.
4. The invoice is made available once to the product even though the entity has no Phase One issue/report obligation.

### J5 — Change delivery or reporting provider/adapter

1. An authorised actor configures a replacement connection without creating a new legal subject.
2. Sage reuses still-valid identity and authority evidence, then rechecks only provider registration, credential, environment, format and operational readiness affected by the change.
3. Existing invoices and in-flight legs retain their original connection/context; ambiguous old-provider operations reconcile before cutover completion.
4. The new connection activates prospectively at an effective boundary with rollback and historical-access controls.

### J6 — Credential expiry or revocation

1. Purpose-specific monitoring identifies the affected delivery or Revenue credential and every dependent capability.
2. The named owner renews/rotates and tests replacement material under the relevant connection policy.
3. Expired, revoked, compromised or validation-unknown material blocks new dependent use without suspending unrelated capabilities.
4. Historical invoice/report evidence remains attributable after rotation; private keys never enter product storage or support surfaces.

## Journey summary

| Journey | Spine | Required exception/continuity |
|---|---|---|
| Prepare | Map EN 16931 data → capture entity/cohort evidence → assess inbound and issue/report readiness | Live adapters remain disabled until official artefacts and approval |
| Phase One | Submit → confirm cohort/scope → validate EN 16931 → create buyer and Revenue legs → record both outcomes | Delivery and report never inherit or overwrite each other's result |
| Correct/recover/change | Correct before send; reject or timeout affects one leg → reconcile before retry | Later phase/route/rule changes affect new work; original context remains |

## Failure and recovery matrix

| Failure or change | Required behaviour | Prohibited outcome |
|---|---|---|
| Cohort evidence absent or contradictory | Return evidence-required with source/owner; do not apply issue/report obligation or exemption silently | Guessing Phase One membership |
| Accountant lacks one client/capability authority | Deny only that item/capability with non-enumerating evidence; continue independent safe items | Firm-wide success/failure or client-data leakage |
| Delivery ready but Revenue connection unavailable | Preserve receive/readiness and any safe pre-send work; block the dependent Phase One issue/report plan with separate action | Reporting failure represented as buyer-delivery failure |
| Profile or mapping cannot preserve required meaning | Stop before signing/submission, retain diagnostics and require corrected data/mapping | Silent field loss or fallback to PDF |
| Credential expired/revoked/wrong-purpose | Block only dependent connection/capability and require renewal/reselection | Reuse through another purpose or secret exposure |
| Timeout after possible delivery/report mutation | Mark only that leg outcome unknown and reconcile by stable identity before retry | Repeating both legs or duplicating the invoice/report |
| Provider change while invoice is in flight | Freeze old connection for that plan, reconcile ambiguity and activate replacement only for eligible new work | Moving an in-flight invoice silently |
| Internal persistence failure after external success | Recover using durable plan/correlation and external evidence | Creating a second invoice/report operation |
| Later phase/profile becomes effective | Apply to eligible new work after approval and tests | Reclassifying or regenerating historical invoices |

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

### Onboarding, connections, formats and trust

| ID | Requirement |
|---|---|
| IE-FR18 | Onboarding must create separate legal-subject, cohort-observation, authority and capability-readiness records; it must not use one Irish `ONBOARDED` flag. |
| IE-FR19 | From the effective Phase One date, every configured Irish business in the approved product scope must be evaluated for receive readiness independently from issue/report scope. |
| IE-FR20 | Issue and Revenue-report readiness must require the effective Phase One cohort/scope evidence and must not be granted merely because receive readiness or a delivery connection exists. |
| IE-FR21 | Direct and accountant/batch pathways must use the same client-level policies; reusable relationship, authority or credential evidence must be re-evaluated for every client and capability. |
| IE-FR22 | Buyer-delivery and Revenue-report connections must be separate resources with their own provider/authority, external identity, adapter, credential, environment, health and lifecycle evidence. |
| IE-FR23 | Credential readiness must be purpose-specific and expose owner/custodian, validity/expiry, status/revocation, dependency and remediation; Spanish private-platform signature or seal policy must not be inferred for Ireland. |
| IE-FR24 | Connecting, changing or retiring a delivery/reporting provider must reuse still-valid legal-subject and authority evidence, re-run only affected readiness checks and preserve original connection context for historical/in-flight work. |
| IE-FR25 | The pack must govern exact syntax, version, Irish CIUS/profile, extensions, operations, validation artefacts, mappings and effective period; EN 16931 conformance alone must not imply route acceptance. |
| IE-FR26 | Reused transformation capability, including DTS, must pass Irish profile, semantic-loss, version-coexistence and rollback qualification before production activation. |
| IE-FR27 | Original, canonical, Revenue-report, delivery and human-readable artefacts must be correlated but distinctly labelled with format/profile, hash and provenance. |
| IE-FR28 | Production activation must require a versioned evidence manifest covering cohort/applicability, authority, format/rules, delivery connection, Revenue connection, trust, environments, limits, lifecycle, retention, support and rollback. |

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
| IE-NFR8 | Accountant portfolio/batch processing must enforce client isolation, fair scheduling, durable item state and independently recoverable results. |
| IE-NFR9 | Delivery and Revenue credential monitoring must detect expiry, revocation, compromise and dependency risk under purpose-specific policies with named renewal owners. |
| IE-NFR10 | Every policy, format, validation, mapping, connection and credential decision used by an invoice/report must be reproducible from retained versioned evidence. |

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
| IE-AC9 | Given an Irish business is outside the Phase One issuer cohort, when onboarding completes, then receive readiness can become ready while issue/report remain not applicable or evidence-required. |
| IE-AC10 | Given an accountant portfolio contains clients with different authority/cohort evidence, when processed, then only eligible client/capability combinations become ready and no firm-wide authority is inferred. |
| IE-AC11 | Given buyer-delivery readiness is complete but the Revenue connection is not configured, when a Phase One issuer views readiness, then issue/report remains blocked with the missing Revenue action while receive readiness is unchanged. |
| IE-AC12 | Given a valid delivery transport credential is selected for Revenue reporting, when readiness runs, then it is rejected as wrong-purpose unless the approved Revenue policy explicitly permits it. |
| IE-AC13 | Given a provider connection changes, when the replacement becomes ready, then the Irish legal entity is not re-created and prior invoices retain their original connection and external references. |
| IE-AC14 | Given DTS supports EN 16931 elsewhere, when Ireland activation is attempted, then it remains blocked until the exact Irish syntax/profile and semantic-preservation corpus passes. |
| IE-AC15 | Given a delivery or Revenue credential expires, when a new dependent operation begins, then only the affected capability is blocked and historical evidence remains accessible. |
| IE-AC16 | Given an archived invoice has original, canonical, delivery and report artefacts, when an authorised user downloads evidence, then each artefact's role, hash, profile and provenance are distinguishable. |

## Goal traceability

| Goal | Primary requirements | Demonstration |
|---|---|---|
| IE-G1 — Receive structured invoices | IE-FR4–IE-FR6, IE-FR13, IE-FR15, IE-FR18–IE-FR19, IE-FR27; IE-NFR1, IE-NFR6 | IE-AC1, IE-AC8–IE-AC9, IE-AC16 |
| IE-G2 — Phase One compliant issuance | IE-FR1–IE-FR3, IE-FR7, IE-FR20–IE-FR26, IE-FR28; IE-NFR4, IE-NFR9–IE-NFR10 | IE-AC2, IE-AC3, IE-AC6, IE-AC10–IE-AC15 |
| IE-G3 — Independent Revenue reporting | IE-FR8–IE-FR11, IE-FR14, IE-FR22–IE-FR24; IE-NFR9 | IE-AC4, IE-AC5, IE-AC11–IE-AC13, IE-AC15 |
| IE-G4 — Effective-dated expansion | IE-FR12, IE-FR16–IE-FR18, IE-FR24–IE-FR28; IE-NFR4, IE-NFR10 | IE-AC7, IE-AC13–IE-AC16 |
| IE-G5 — ViDA readiness | IE-FR1, IE-FR2, IE-FR12, IE-FR25–IE-FR28; IE-NFR4, IE-NFR5, IE-NFR10 | IE-AC6, IE-AC7, IE-AC14, IE-AC16 |

## Metrics, rollout and gates

| Measure | Baseline/target status | Owner |
|---|---|---|
| Irish product/entity EN 16931 data readiness | Coverage baseline required per product | Product + Ireland pack owner |
| Phase One cohort identification completeness | Target/authoritative source approval required | Compliance |
| Inbound receipt/import success by future syntax/route | Blocked until artefacts/cohort selected | Product/operations |
| Delivery vs reporting success and unknown-age | Thresholds need official interface/SLA evidence | Operations |
| First-pass validation and correction completion | Baseline required | Product |
| Receive/issue/report readiness by product and legal entity | Exposes asymmetric preparation without a false single onboarding result | Ireland pack owner + portfolio product |
| Accountant batch outcomes by client/capability | Measures authority and data-readiness friction while protecting isolation | Product/operations |
| Credential expiry/rotation risk by delivery/report purpose | Prevents avoidable connection outage | Security/operations |
| Provider/adapter change completion and disrupted in-flight work | Validates connection change without legal-entity re-onboarding | Platform operations |

Rollout gates:

1. Name Revenue/regulatory, product, engineering, security/privacy and operations owners.
2. Select one delivery-depth reference product/cohort and establish legal-entity, accountant, volume, invoice-direction, format and support baselines.
3. Inventory receive/issue/report/download readiness across the selected product and confirm how Revenue cohort notification/evidence will be captured and refreshed.
4. Complete EN 16931 data-gap assessment, original/canonical/rendering handling and inbound product experience.
5. Obtain and approve Irish legal text, CIUS/syntax/schema/code lists, transport/directory, identity, authority and Revenue reporting specifications.
6. Confirm separate delivery/Revenue connection contracts, credentials, environments, report trigger/timing, corrections/cancellations, acknowledgements, idempotency, switching/exit, retention and support/SLA.
7. Qualify DTS/other shared transformation and validation capability against the exact Irish profile and semantic-loss corpus.
8. Demonstrate direct/accountant onboarding, inbound, dual-leg success/failure, credential expiry, provider change, unknown outcome, phase change and historical continuity in sandbox.
9. Complete security/privacy/operations/customer communication and kill/rollback readiness.
10. Pilot an approved Phase One cohort before expansion.

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
| What Irish mechanism authorises an accountant/delegate to configure, issue, receive, report and access evidence for a client? | Prevents firm relationship or credential possession becoming universal authority | Ireland legal/Revenue liaison | Blocks accountant production onboarding |
| Are buyer delivery and Revenue reporting provided through one organisation/contract or independent provider/authority connections? | Determines customer setup, commercial ownership, fault isolation and switching | Revenue/product/procurement/architecture | Blocks connection design; model separately until evidenced |
| Which authentication, certificate, consent or signing/seal policies apply to delivery and Revenue reporting? | Determines custody, expiry, rotation and runtime trust | Revenue/security/identity owner | Blocks production trust; do not copy Spain |
| What provider/participant transfer and historical-access rules apply when a delivery service changes? | Prevents re-onboarding and stranded invoices | Network/provider/legal | Blocks switching runbook |
| Early design hardens around an invented API | Rework/compliance risk | Keep interfaces capability-based and live-disabled until evidence | Proposed mitigation |

## Decisions

| Decision | Status | Owner/date |
|---|---|---|
| Ireland is a child country pack of PRD-SEI-227 | Confirmed by user request | 2026-08-10 |
| Model buyer delivery and Revenue reporting as independent legs | Proposed product requirement from confirmed dual obligation | TBD |
| Use EN 16931 as confirmed Phase One semantic basis | Confirmed Revenue evidence | 2026-08-10 |
| Keep technical adapters disabled until official artefacts and approvals exist | Confirmed discovery boundary | 2026-08-10 |
| Use capability-specific onboarding and keep delivery and Revenue connections separate until official evidence proves a combined contract | Proposed from Spain reuse and Ireland's dual obligation | 2026-09-23 |
| Prioritise Ireland as the first UK/Ireland delivery-depth track, subject to reference product/cohort approval | Proposed sequencing | 2026-09-23 |

## Revision history

| Date | Change | Evidence/decision | Pull request |
|---|---|---|---|
| 2026-08-10 | Initial discovery child PRD with Confluence-safe phased dual-leg visual | User request, Revenue and EU official sources | |
| 2026-08-10 | Linked the consolidated parent visual atlas and compressed journey prose for research-stage readability | User direction | |
| 2026-08-10 | Approved for publication to existing page `866140021`; existing hierarchy preserved | User approval | |
| 2026-08-11 | Removed the embedded HTML heading and promoted the diagram title to a native Confluence heading | Confluence rendering feedback | |
| 2026-09-23 | Applied Spain learnings without importing Spanish policy; added legal-subject/cohort/authority/readiness decomposition, accountant batch, separate delivery/Revenue connections, provider change, purpose-specific trust, format/DTS gates, detailed journeys and acceptance | Stakeholder direction; PRD-SEI-227/223/226/231; current Revenue evidence | |
