---
id: PRD-SEI-232
title: E-Invoicing — Country Lifecycle Status Mapping
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-08-12
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-224
  - PRD-SEI-225
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: "866152235"
  title: E-Invoicing — Country Lifecycle Status Mapping
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Country Lifecycle Status Mapping

## Decision summary

Keep the external country/provider status and reason exactly as observed. Map it through an effective-dated country-pack catalog into one or more shared compliance dimensions. Product views are derived from evidence; they are not the legal record and do not force every country into one linear state machine.

## Preserve first, map second, derive last

<!-- confluence-html-macro:start -->
<div class="eis-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eis-map *{box-sizing:border-box}.eis-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eis-map svg{display:block;width:1100px;height:510px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eis-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eis-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eis-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eis-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eis-map .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.eis-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eis-map .copy{fill:#42526e;font-size:8.5px}.eis-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eis-map .path{fill:none;stroke:#00875a;stroke-width:2}.eis-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eis-map .arrow{fill:#00875a}.eis-map .arrow-g{fill:#6b778c}.eis-map .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eis-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eis-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">A raw event is immutable. Mapping versions can improve future interpretation, while historical decisions retain the version actually used.</p>
  <svg viewBox="0 0 1100 510" role="img" aria-label="Country, provider, network and authority events enter an immutable raw event ledger. Each event records source, raw code and reason, timestamps, correlation and country context. An effective-dated country status catalog maps the raw event into independent technical, document, delivery, commercial, payment and reporting dimensions. Unknown, duplicate, conflicting and out-of-order events go to reconciliation without being discarded. Product and operational views are derived from the retained evidence and mapping version.">
    <text x="34" y="30" class="label">OBSERVE</text><text x="348" y="30" class="label">INTERPRET</text><text x="790" y="30" class="label">DERIVE VIEWS</text>
    <rect x="34" y="62" width="230" height="116" rx="10" class="main"/><text x="54" y="91" class="title">External event</text><text x="54" y="112" class="copy">country • provider • network • authority</text><text x="54" y="132" class="copy">raw code + reason + source time</text><text x="54" y="152" class="copy">correlation • document/leg identity</text>
    <path d="M264 120 H322" class="path"/><polygon points="322,120 312,114 312,126" class="arrow"/>
    <rect x="324" y="62" width="248" height="116" rx="10" class="finish"/><text x="344" y="91" class="title">Immutable raw event ledger</text><text x="344" y="112" class="copy">deduplicate by source identity</text><text x="344" y="132" class="copy">retain unknown/out-of-order/conflict</text><text x="344" y="152" class="copy">never replace country vocabulary</text>
    <path d="M448 178 V224" class="path"/><polygon points="448,224 442,214 454,214" class="arrow"/>
    <rect x="324" y="226" width="248" height="126" rx="10" class="main"/><text x="344" y="255" class="title">Country status catalog</text><text x="344" y="276" class="copy">country + source + raw status/reason</text><text x="344" y="296" class="copy">document/process/direction + effective time</text><text x="344" y="316" class="copy">mapping version + owner + confidence</text><text x="344" y="336" class="copy">canonical events + dimension effects</text>
    <path d="M572 289 H638" class="path"/><polygon points="638,289 628,283 628,295" class="arrow"/>
    <rect x="640" y="62" width="244" height="290" rx="10" class="main"/><text x="660" y="91" class="title">Independent dimensions</text><text x="660" y="121" class="copy">TECHNICAL — accepted / failed / unknown</text><text x="660" y="157" class="copy">DOCUMENT — valid / rejected / corrected</text><text x="660" y="193" class="copy">DELIVERY — dispatched / delivered / failed</text><text x="660" y="229" class="copy">COMMERCIAL — accepted / disputed / cancelled</text><text x="660" y="265" class="copy">PAYMENT — due / partial / paid / reversed</text><text x="660" y="301" class="copy">REPORTING — not due / accepted / rejected</text><text x="660" y="329" class="copy">A country activates only evidenced meanings</text>
    <path d="M884 207 H940" class="path"/><polygon points="940,207 930,201 930,213" class="arrow"/>
    <rect x="942" y="76" width="124" height="82" rx="10" class="finish"/><text x="960" y="105" class="title">Product view</text><text x="960" y="126" class="copy">clear next action</text><text x="960" y="143" class="copy">safe wording</text>
    <rect x="942" y="180" width="124" height="82" rx="10" class="finish"/><text x="960" y="209" class="title">Operations view</text><text x="960" y="230" class="copy">each external leg</text><text x="960" y="247" class="copy">recovery evidence</text>
    <rect x="942" y="284" width="124" height="82" rx="10" class="finish"/><text x="960" y="313" class="title">Audit view</text><text x="960" y="334" class="copy">raw + mapped</text><text x="960" y="351" class="copy">version lineage</text>
    <path d="M448 352 V400 H720" class="path-opt"/><polygon points="720,400 710,394 710,406" class="arrow-g"/>
    <rect x="722" y="382" width="344" height="92" rx="10" class="warn"/><text x="742" y="411" class="title">Reconciliation queue</text><text x="742" y="432" class="copy">unknown • conflicting • missing dependency • late event</text><text x="742" y="451" class="copy">human/system resolution appends evidence; history remains</text>
    <rect x="34" y="394" width="498" height="80" rx="10" class="bad"/><text x="54" y="423" class="title">Rejected shortcut: one universal status field</text><text x="54" y="444" class="copy">“DELIVERED” cannot prove document validity, commercial acceptance, payment or authority reporting.</text><text x="54" y="461" class="copy">A later status must not erase a rejection, dispute or reporting failure.</text>
  </svg>
  <div class="notes"><div class="note"><strong>Country owns meaning</strong>The country pack owns the source catalog, effective dates and approved mapping.</div><div class="note"><strong>Shared dimensions aid products</strong>Products can show consistent actions without pretending country statuses are identical.</div><div class="note"><strong>No false success</strong>Document, delivery, commercial, payment and reporting outcomes remain independent.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Shared contract and country ownership

| Shared platform | Country pack |
|---|---|
| Raw-event envelope, append-only evidence, deduplication and ordering metadata | Source/status/reason catalog and official semantics |
| Common dimensions and customer-safe outcome contract | Which dimensions/statuses apply, mapping effects and precedence |
| Derived views, reconciliation and observability | Effective dates, owner approval, test fixtures and retirement |
| Mapping engine/version contract | Country/provider/network-specific mapping artefact |

## Requirements and acceptance

| ID | Requirement / acceptance |
|---|---|
| LS-FR1 | Persist source, country, raw status/reason, source/observed time, correlation, document/exchange-leg identity and payload integrity reference before mapping. |
| LS-FR2 | Map through an immutable, effective-dated catalog identified by country, source, process/document, direction and version. |
| LS-FR3 | Permit one raw event to affect zero, one or several shared dimensions without fabricating a total order. |
| LS-FR4 | Preserve duplicate, unknown, conflicting, regressive and out-of-order evidence; reconciliation appends resolution rather than editing history. |
| LS-FR5 | Keep document, delivery, commercial, payment and reporting status separately queryable and expose technical processing separately. |
| LS-FR6 | A new mapping version applies prospectively unless a governed re-derivation explicitly records old/new versions and reason. |
| LS-AC1 | Given delivery succeeds and authority reporting fails, then product and operations views show both outcomes and recover only the reporting leg. |
| LS-AC2 | Given an unmapped country status, then the raw event is visible, current status is not falsely advanced and a mapping/reconciliation action is created. |
| LS-AC3 | Given a late rejection after a prior acknowledgement, then both events remain and the derived view follows the approved country precedence with an explanation. |

## Research matrix

| Country | Current discovery position | Required next evidence |
|---|---|---|
| France | Existing platform analysis provides candidate invoice, directory, transaction/payment-reporting and business-lifecycle vocabularies | Approved source catalog, exact reason/precedence rules and effective versions |
| Spain | Existing analysis provides candidate invoice, platform, payment and correction events | Keep B2B e-invoice and VERI*FACTU/SII events in separate bounded contexts; approve mappings |
| Germany | Flexible delivery methods mean document and delivery evidence cannot be inferred from one network status | Format/channel-specific acknowledgements, rejection and correction rules |
| Ireland | Phased mandate is known; detailed reporting/transport events remain incomplete | Revenue technical specifications and official event catalog |
| UK | Peppol direction is known; final UK lifecycle and HMRC reporting rules remain open | Final legislation, BIS/profile and reporting artefacts |

Evidence: parent [PRD-SEI-227](PRD-SEI-227-e-invoicing-as-a-service.md), lifecycle analysis [PRD-SEI-224](PRD-SEI-224-lifecycle-rejection-payment-reporting.md), resilience analysis [PRD-SEI-225](PRD-SEI-225-operations-resilience-support-reconciliation.md), and the Germany/Ireland/UK country-pack PRDs. This child page adds the mapping boundary; it does not declare unverified country codes.

Open gates: approve the shared dimensions; name country owners; obtain authoritative status/reason catalogs; define conflict/precedence tests; confirm customer wording; and set reconciliation ownership/SLOs from operational evidence.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-12 | Initial child discovery PRD for preserved country status and shared lifecycle dimensions | User feedback and PRD-SEI-224/225 analysis |
| 2026-08-12 | Published as a child of commonality page `866150169` | User publication approval |
