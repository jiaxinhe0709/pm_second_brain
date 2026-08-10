---
id: PRD-SEI-228
title: Germany E-Invoicing Compliance Pack
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
  page_id: "771498625"
  title: 2.3 E-invoicing Germany
  layout: two_left_sidebar
  toc: true
---

# Germany E-Invoicing Compliance Pack

## Decision summary

Define Germany as a country pack on PRD-SEI-227, using shared invoice semantics, validation, transformation, lifecycle, evidence and operations while preserving Germany's current B2B characteristic: the invoice must be structured, but the tax rules do not prescribe one universal transmission network.

Germany is a critical neutrality test. The shared platform must support XRechnung, eligible ZUGFeRD profiles and other evidence-backed interoperable formats, plus counterparty-agreed channels, without forcing a France/Spain intermediary or authority-reporting topology.

> **Country principle:** Validate the legal invoice representation independently from how contracting parties choose to exchange it.

## Parent relationship, outcome and readiness

| Area | Position |
|---|---|
| Parent PRD | PRD-SEI-227 — shared service and country-pack contract |
| Visual research | PRD-SEI-227 contains the consolidated source-diagram atlas; this child keeps only the Germany-specific operational flow |
| Confluence position | Existing page `771498625`; preserve current parent `771496799` |
| Customer outcome | German businesses can receive and issue compliant structured B2B invoices through supported Sage products and agreed channels. |
| Current phase | Discovery and reference-pack assessment |
| Readiness | **Consultation-ready**, not delivery-ready: product cohort, detailed scope, supported transports, format/profile versions, B2G boundary, retention and operations evidence remain open. |

## Regulatory phase model

| Effective period | Confirmed official position | Product implication |
|---|---|---|
| From 2025-01-01 | In-scope domestic businesses must be able to receive structured e-invoices; the BMF says an email mailbox is sufficient for receipt | Inbound readiness is already required; transport cannot be assumed to be a platform/network |
| 2025-01-01 to 2026-12-31 | Issuers may generally use transition options for other invoice forms | Products must explain eligibility/effective rules; do not treat transition as permanent target behaviour |
| Through 2027 | Issuers with prior-year turnover up to EUR 800,000 receive an extended transition; certain EDI transition also runs through 2027 | Effective policy must include the evidence-backed transition dimensions; exact product eligibility needs legal confirmation |
| After applicable transition | In-scope domestic B2B issuance uses structured e-invoices, subject to exemptions/rules | Outbound compliance becomes the target capability |
| Future | German e-invoicing prepares for a later reporting system; current rules do not yet define that shared reporting obligation here | Do not invent current authority reporting; keep reporting adapter capability inactive and versionable |

## German exchange visual

<!-- confluence-html-macro:start -->
<div class="de-pack" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .de-pack *{box-sizing:border-box}.de-pack h2{margin:0;color:#172b4d;font-size:18px}.de-pack .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.de-pack svg{display:block;width:1060px;height:520px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.de-pack .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.de-pack .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.de-pack .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.de-pack .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.de-pack .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.de-pack .title{fill:#172b4d;font-size:11px;font-weight:700}.de-pack .copy{fill:#42526e;font-size:9px}.de-pack .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.de-pack .path{fill:none;stroke:#00875a;stroke-width:2}.de-pack .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.de-pack .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.de-pack .path-warn{fill:none;stroke:#ff8b00;stroke-width:1.8;stroke-dasharray:6 4}.de-pack .arrow{fill:#00875a}.de-pack .arrow-g{fill:#6b778c}.de-pack .arrow-r{fill:#de350b}.de-pack .arrow-a{fill:#ff8b00}.de-pack .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1060px;margin-top:12px}.de-pack .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.de-pack .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Structured invoice, counterparty-agreed delivery</h2>
  <p class="sub">The German pack validates and renders the invoice; an approved product configuration selects an eligible exchange channel. Government reporting is a future optional branch, not a current implied step.</p>
  <svg viewBox="0 0 1060 520" role="img" aria-label="A German seller's Sage product submits an invoice to the shared service. The Germany pack checks scope, validates the structured representation and produces XRechnung, eligible ZUGFeRD or another approved interoperable format. An agreed channel such as email, API, portal or approved EDI delivers it to the buyer. Validation failures loop to correction. Ambiguous channel outcomes reconcile before retry. A future reporting adapter is shown as inactive and optional.">
    <text x="34" y="32" class="label">SELLER</text><text x="258" y="32" class="label">SHARED SERVICE + GERMANY PACK</text><text x="820" y="32" class="label">BUYER / FUTURE</text>
    <rect x="34" y="85" width="180" height="78" rx="10" class="main"/><text x="54" y="114" class="title">German seller product</text><text x="54" y="134" class="copy">Invoice intent and counterparty context</text>
    <path d="M214 124 H268" class="path"/><polygon points="268,124 258,118 258,130" class="arrow"/>
    <rect x="270" y="76" width="190" height="96" rx="10" class="main"/><text x="290" y="104" class="title">Determine German scope</text><text x="290" y="125" class="copy">Domestic B2B • entity • exemptions</text><text x="290" y="144" class="copy">transition and effective policy version</text>
    <path d="M460 124 H500" class="path"/><polygon points="500,124 490,118 490,130" class="arrow"/>
    <rect x="502" y="76" width="190" height="96" rx="10" class="main"/><text x="522" y="104" class="title">Validate and represent</text><text x="522" y="125" class="copy">EN 16931-compatible business rules</text><text x="522" y="144" class="copy">XRechnung • eligible ZUGFeRD • approved EDI</text>
    <path d="M692 124 H732" class="path"/><polygon points="732,124 722,118 722,130" class="arrow"/>
    <rect x="734" y="76" width="190" height="96" rx="10" class="main"/><text x="754" y="104" class="title">Select agreed channel</text><text x="754" y="125" class="copy">Email • API • portal • shared store</text><text x="754" y="144" class="copy">or evidence-backed EDI/other route</text>
    <path d="M829 172 V245" class="path"/><polygon points="829,245 823,235 835,235" class="arrow"/>
    <rect x="734" y="247" width="190" height="86" rx="43" class="finish"/><text x="761" y="280" class="title">Buyer receives structured data</text><text x="765" y="301" class="copy">Leading structured part retained</text>
    <path d="M734 290 H661" class="path"/><polygon points="661,290 671,284 671,296" class="arrow"/>
    <rect x="449" y="247" width="210" height="86" rx="10" class="main"/><text x="469" y="277" class="title">Record delivery evidence</text><text x="469" y="298" class="copy">Format/profile • route • integrity • result</text><text x="469" y="316" class="copy">return product-safe outcome</text>
    <polygon points="365,201 403,239 365,277 327,239" class="bad"/><text x="338" y="235" class="title">Invalid</text><text x="336" y="251" class="copy">correct data</text>
    <path d="M365 201 V172" class="path-alert"/><polygon points="365,172 359,182 371,182" class="arrow-r"/>
    <path d="M327 239 H214 V163" class="path-alert"/><polygon points="214,163 208,173 220,173" class="arrow-r"/>
    <polygon points="829,360 867,376 883,414 867,452 829,468 791,452 775,414 791,376" class="warn"/><text x="800" y="409" class="title">Unknown</text><text x="799" y="425" class="copy">reconcile route</text>
    <path d="M829 333 V360" class="path-warn"/><polygon points="829,360 823,350 835,350" class="arrow-a"/>
    <path d="M775 414 H658 V333" class="path-warn"/><polygon points="658,333 652,343 664,343" class="arrow-a"/>
    <rect x="90" y="383" width="250" height="84" rx="10" class="optional"/><text x="110" y="412" class="title">Future German reporting adapter</text><text x="110" y="433" class="copy">Inactive until legislation/specification and</text><text x="110" y="451" class="copy">country approval define reportable behaviour</text>
    <path d="M340 425 H449 V333" class="path-opt"/><polygon points="449,333 443,343 455,343" class="arrow-g"/>
  </svg>
  <div class="notes"><div class="note"><strong>No prescribed B2B network</strong>The product must not require an intermediary solely because other countries do.</div><div class="note"><strong>Structured part leads</strong>For a hybrid invoice, the structured data is authoritative when it differs from the visual part.</div><div class="note"><strong>Reporting remains gated</strong>Future German transaction reporting must activate through a new evidence-backed pack version.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Problem and value

German businesses already need inbound readiness, while issuance transition rules continue through 2026/2027. A product that treats Germany as “send XML by email” under-specifies validation, source/visual precedence, counterparty agreement, audit and inbound processing. A product that assumes a mandatory platform over-specifies the law and reduces customer choice.

The Germany pack creates a precise boundary: shared services handle invoice semantics, validation, transformation, lifecycle, resilience and evidence; German policy determines scope, transition, accepted representation and locally valid delivery configuration.

## Goals

| ID | Goal |
|---|---|
| DE-G1 | Enable in-scope German legal entities to receive structured e-invoices with provenance, validation and safe product import. |
| DE-G2 | Enable eligible issuers to create compliant structured invoices using approved format/profile versions after scope/transition evaluation. |
| DE-G3 | Support counterparty-agreed transmission without declaring one universal German B2B network. |
| DE-G4 | Preserve the leading structured representation, human-readable view and all correction/delivery evidence. |
| DE-G5 | Keep future transaction reporting and B2G requirements explicit but outside current B2B commitment. |

## Non-goals

- Defining German B2G federal/state invoice requirements; they require a separate scope assessment.
- Mandating Peppol, a portal, email, API or provider for all German B2B exchange.
- Treating a PDF without the required structured data as an e-invoice.
- Claiming all ZUGFeRD versions/profiles or all EDI formats are eligible.
- Implementing future transaction reporting before law and technical specifications are approved.
- Providing tax/legal advice or finalising exemptions and transition decisions without German compliance review.

## Definitions and actors

| Term/actor | Meaning/responsibility |
|---|---|
| E-Rechnung | Invoice issued, transmitted and received in a structured electronic format enabling electronic processing under current German rules |
| Other invoice | Paper or electronic representation that does not meet the structured e-invoice definition, subject to transition/consent rules |
| XRechnung | Common German structured standard based on EN 16931; exact supported version requires approval |
| ZUGFeRD | Hybrid representation; eligible versions/profiles must meet German requirements; structured data leads |
| Seller/customer | Provides accurate business facts and uses the invoice route agreed with the buyer |
| Buyer/recipient | Supplies/accepts the exchange channel and processes the structured representation |
| Sage product | Captures intent, corrections and customer-safe outcomes |
| Germany pack owner | Owns evidence, policy versions, profile/rule approval and regulatory updates |
| Operations/support | Investigates validation, route, duplicate and unknown outcomes with redacted evidence |

## Business scenarios

| ID | Scenario | Expected outcome | Exception/continuity |
|---|---|---|---|
| DE-S1 | German business receives XRechnung by an approved channel | Recipient/entity is verified, original retained, invoice validated and imported once | Invalid/untrusted content is quarantined with actionable status |
| DE-S2 | Issuer submits valid invoice after applicable transition | Scope/profile validates and agreed channel receives the structured invoice | Unsupported profile/route blocks before dispatch |
| DE-S3 | Eligible issuer uses a transition option | Scope result explains why another invoice form is currently permitted | Historical decision stores policy/evidence version |
| DE-S4 | Seller and buyer agree API rather than email | Same invoice compliance applies; channel-specific delivery evidence differs | Configuration change affects only new work |
| DE-S5 | Hybrid visual and structured contents differ | Structured data is treated as leading and discrepancy is surfaced/audited | Do not silently derive legal values from PDF view |
| DE-S6 | Channel times out after send | Outcome becomes unknown and is reconciled/corroborated before resend | No blind duplicate invoice |
| DE-S7 | Future reporting law activates | New approved policy creates a separate reporting leg | Earlier invoices are not retroactively reported without legal decision |

## Business rules

| ID | Condition | Rule | Status/evidence |
|---|---|---|---|
| DE-BR1 | Domestic B2B transaction is evaluated | Determine entity/transaction/exemption and applicable transition using an effective policy version | Official BMF guidance; detailed rule set requires local approval |
| DE-BR2 | Invoice is an e-invoice | It must be structured and enable electronic processing; plain PDF/scans are not sufficient | Confirmed BMF |
| DE-BR3 | Format is selected | XRechnung and eligible ZUGFeRD profiles may qualify; other formats require evidence of correct/full extractability/interoperability | Confirmed BMF; exact versions open |
| DE-BR4 | Hybrid data conflicts | The structured part is leading | Confirmed BMF |
| DE-BR5 | Transmission route is selected | The tax rules do not impose one route; parties agree the practical route | Confirmed BMF |
| DE-BR6 | Business receives e-invoice | Receiving capability applies from 2025-01-01, including small businesses; email mailbox can be sufficient under tax rules | Confirmed BMF |
| DE-BR7 | B2G invoice is involved | Apply separate public-procurement requirements; do not infer B2B route/threshold behaviour | Confirmed BMF distinction |
| DE-BR8 | Reporting is considered | Current pack records no active government transaction-report leg until new approved evidence activates it | Confirmed current gap |

## Scope and capability evidence

| Capability | State | Pack position |
|---|---|---|
| Applicability | Partially confirmed | Domestic business scope/transition confirmed at summary level; exemptions and product decisions need legal matrix |
| Inbound | Confirmed obligation | Receive structured invoice from 2025-01-01; supported channels/cohort open |
| Outbound | Confirmed with transition | Build target capability; evaluate transition/effective rules |
| Validation | Confirmed direction | EN 16931-related plus German tax/business rules; exact artefacts/version open |
| Formats | Partially confirmed | XRechnung and eligible ZUGFeRD; other interoperable/EDI evidence needed |
| Recipient resolution | Not prescribed | Customer/counterparty configuration is current hypothesis |
| Transport | Flexible | Email/API/portal/shared store/other agreed channel possible; product support set open |
| Lifecycle | Proposed | Technical/validation/delivery events; no invented French/Spanish business-status mandate |
| Reporting | Future/unknown | No active adapter in current pack |
| B2G | Out of scope | Separate requirements and routes |

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [BMF E-Rechnung FAQ, March 2026](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) | Domestic B2B requirement/transition, receiving since 2025, formats, structured-part precedence and multiple delivery methods | Primary official tax guidance; technical/B2G details delegated elsewhere | DE-BR1–DE-BR8 and requirements |
| [BMF letter, 15 October 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5) | Detailed administrative application including formats and transmission | Primary official material in German; local legal review required | Detailed policy/rule artefact input |
| [European Commission ViDA 2026 Work Programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en) | EU cross-border DRR/e-invoicing from 2030 and alignment through 2035 | Official strategic timeline; German domestic reporting detail remains future | Extensibility, not current reporting requirement |
| Supplied research | Germany is a strong counter-example to a mandatory-intermediary core | Secondary synthesis; validated against BMF at principle level | Neutral transport framework |

## Proposed journeys

| Journey | Spine | Required exception/continuity |
|---|---|---|
| Inbound | Configure entity/channel → receive → verify/deduplicate/validate → preserve original and visualise → import once | Structured data leads; unsafe content is quarantined |
| Outbound | Submit intent → evaluate scope/transition → validate/profile → correct if needed → deliver by agreed channel | No send before correction; record profile, route and result |
| Recover/change | Timeout after possible send → outcome unknown → reconcile → retry only if safe | Later channel/profile change affects new work; history retains origin context |

## Requirements

### Scope, representation and validation

| ID | Requirement |
|---|---|
| DE-FR1 | The pack must evaluate domestic B2B scope, legal-entity context, transaction date, exemption and applicable transition before declaring e-invoice issuance required. |
| DE-FR2 | The scope result must identify the German policy version, effective rule, reason and any evidence/customer action still required. |
| DE-FR3 | Outbound invoices must pass the selected syntax/profile and German business-rule validation before delivery. |
| DE-FR4 | Supported XRechnung/ZUGFeRD/other profiles must be versioned and allowlisted; unsupported or ineligible profiles must be rejected before transmission. |
| DE-FR5 | For hybrid invoices, the service must treat structured data as leading, retain the visual part and expose material discrepancy evidence. |
| DE-FR6 | Inbound processing must retain the original structured representation, verify recipient/tenant, deduplicate and preserve validation/provenance results. |

### Route and lifecycle

| ID | Requirement |
|---|---|
| DE-FR7 | A customer/product must configure or select an eligible counterparty-agreed route from the product-supported German channel set; no route may be inferred solely from country. |
| DE-FR8 | Channel readiness validation must not activate or change an existing route without authorised confirmation. |
| DE-FR9 | Each outbound delivery must record format/profile, destination, route/channel, message identity, integrity evidence, times and observed outcome. |
| DE-FR10 | Lifecycle must distinguish validation, dispatch, delivery/availability, technical rejection, business correction and outcome unknown without inventing unsupported mandated statuses. |
| DE-FR11 | No government-reporting mutation may occur unless a future approved German policy version explicitly activates and defines a separate reporting leg. |
| DE-FR12 | B2G intent must be rejected or routed to a separately approved capability; the B2B pack must not claim B2G compliance. |

### Recovery and operations

| ID | Requirement |
|---|---|
| DE-FR13 | Duplicate inbound/outbound operations must resolve to one logical invoice/exchange using source/message/idempotency identity. |
| DE-FR14 | A timeout after possible dispatch must reconcile the configured channel before retry unless end-to-end idempotency is proven. |
| DE-FR15 | Operations must see applied scope/transition, profile validation, route configuration, intended/observed delivery and safe next actions with customer-safe German/English messaging. |
| DE-FR16 | Changing profile, channel or counterparty configuration must not rewrite historical invoices or prevent approved historical retrieval/correction. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| DE-NFR1 | German tenant/entity/channel data and credentials must be isolated by environment and least privilege. |
| DE-NFR2 | Original structured invoices and legally/audit-relevant transformations must use approved integrity, retention, deletion and access controls; periods require German legal/privacy approval. |
| DE-NFR3 | XML/hybrid parsing and visualisation must be hardened against unsafe content and must not execute embedded active content. |
| DE-NFR4 | Format/profile/rule changes require regression fixtures, country-owner approval, effective dates and rollback for new work. |
| DE-NFR5 | Volume, payload, delivery-latency and availability targets require reference-product/channel baselines before delivery approval. |
| DE-NFR6 | Operational diagnostics must distinguish data/profile, configuration, Sage platform, channel/provider and recipient faults without exposing unnecessary invoice data. |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| DE-AC1 | Given a valid supported structured German invoice received for a verified entity, when processed, then the original is retained, imported once and linked to profile/validation/channel evidence. |
| DE-AC2 | Given a plain PDF with no qualifying structured data, when classified, then it is not represented as a compliant German e-invoice. |
| DE-AC3 | Given an eligible ZUGFeRD invoice whose visual and structured tax total differ, when processed, then structured data leads and the discrepancy is surfaced and audited. |
| DE-AC4 | Given two buyers use different agreed eligible channels, when identical compliant semantics are sent, then invoice validation remains consistent while route evidence differs. |
| DE-AC5 | Given a correctable XRechnung validation failure, when submitted, then no dispatch occurs and rule/field/profile guidance is returned. |
| DE-AC6 | Given a delivery timeout after possible send, when recovery starts, then the platform reconciles before any resend. |
| DE-AC7 | Given a future reporting adapter is not activated, when a German invoice is delivered, then no authority report is inferred or claimed. |
| DE-AC8 | Given current route/profile configuration changes, when an older invoice is inspected, then its original representation, route and policy evidence are unchanged. |

## Goal traceability

| Goal | Primary requirements | Demonstration |
|---|---|---|
| DE-G1 — Receive structured invoices | DE-FR5, DE-FR6, DE-FR13, DE-FR15; DE-NFR1–DE-NFR3 | DE-AC1–DE-AC3 |
| DE-G2 — Issue compliant invoices | DE-FR1–DE-FR5; DE-NFR4 | DE-AC3, DE-AC5 |
| DE-G3 — Support agreed channels | DE-FR7–DE-FR10, DE-FR14 | DE-AC4, DE-AC6 |
| DE-G4 — Preserve representation/evidence | DE-FR5, DE-FR9, DE-FR16; DE-NFR2 | DE-AC3, DE-AC8 |
| DE-G5 — Keep B2G/reporting boundaries explicit | DE-FR11, DE-FR12 | DE-AC7 |

## Metrics, rollout and gates

| Measure | Baseline/target status | Owner |
|---|---|---|
| Inbound structured-invoice import success by profile/channel | Baseline from reference product required | Product |
| First-pass outbound validation and top rule failures | Baseline required; informs data readiness | Germany pack owner |
| Duplicate/unknown delivery outcomes | Thresholds require chosen channel evidence | Operations |
| Profile/version coverage by customer cohort | Cohort and target open | Product + compliance |
| Support cases by fault domain | Baseline required | Support |

Rollout gates:

1. Name German tax/compliance, product, engineering and operations owners.
2. Approve detailed applicability/exemption/transition matrix.
3. Select reference product, legal-entity cohort, directions, formats and channels.
4. Obtain approved schemas, profile versions, code lists, validators and test cases.
5. Confirm B2G handling boundary and future-reporting monitoring owner.
6. Demonstrate inbound/outbound, correction, duplicate, ambiguous outcome, channel change and historical access.
7. Approve security/privacy/retention, operational SLOs, support and customer communication.
8. Pilot with rollback/kill controls before production expansion.

## Risks and consultation questions

| Risk/question | Why it matters | Owner | Blocks/current hypothesis |
|---|---|---|---|
| Which German Sage products/customer cohorts are first? | Determines channels, volumes and data gaps | Portfolio/product | Blocks delivery; no cohort chosen |
| Which XRechnung and ZUGFeRD versions/profiles are supported? | Eligibility and regression scope | Compliance + architecture | Blocks technical contract; allowlist versions |
| Which channels must Sage operate vs accept from a provider? | Security, support and acknowledgement differ | Product + architecture | Blocks design; start from cohort evidence |
| How is counterparty route agreement captured and changed? | Prevents misdelivery | Legal/product | Blocks activation; explicit authorised config |
| What inbound trust is sufficient for email/API/portal? | Prevents spoofing/misrouting | Security | Blocks production |
| What corrections/cancellations are legally and technically supported by profile/channel? | Avoids false lifecycle promise | Compliance | Blocks detailed lifecycle |
| What German retention/access rules apply to original and transformed representations? | Data lifecycle and audit | Legal/privacy | Blocks production data policy |
| B2G leaks into B2B pack | False compliance | Separate capability and hard routing gate | B2G remains out of scope |
| Flexible routes create operational fragmentation | Higher support/reconciliation cost | Limit supported route catalogue by cohort; shared evidence contract | Proposed mitigation |

## Decisions

| Decision | Status | Owner/date |
|---|---|---|
| Germany is a child country pack of PRD-SEI-227 | Confirmed by user request | 2026-08-10 |
| Do not prescribe one German B2B transmission network | Confirmed official evidence/product boundary | 2026-08-10 |
| Keep German authority reporting inactive until future evidence/approval | Confirmed current-scope boundary | 2026-08-10 |
| Use Germany as a neutrality/reference-pack assessment candidate | Proposed, not selected for delivery | TBD |

## Revision history

| Date | Change | Evidence/decision | Pull request |
|---|---|---|---|
| 2026-08-10 | Initial discovery child PRD with Confluence-safe German exchange visual | User request, BMF and EU official sources | |
| 2026-08-10 | Linked the consolidated parent visual atlas and compressed journey prose for research-stage readability | User direction | |
| 2026-08-10 | Approved for publication to existing page `771498625`; existing hierarchy preserved | User approval | |
