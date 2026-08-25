---
id: PRD-SEI-232
title: E-Invoicing — Country Lifecycle Status Mapping
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-08-25
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-231
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
    .eis-map *{box-sizing:border-box}.eis-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eis-map svg{display:block;width:100%;max-width:1100px;height:auto;min-width:760px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eis-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eis-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eis-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eis-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eis-map .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.eis-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eis-map .copy{fill:#42526e;font-size:8.5px}.eis-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eis-map .path{fill:none;stroke:#00875a;stroke-width:2}.eis-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eis-map .arrow{fill:#00875a}.eis-map .arrow-g{fill:#6b778c}.eis-map .notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;min-width:0;margin-top:10px}.eis-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eis-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
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
    <path d="M884 117 H940" class="path"/><polygon points="940,117 930,111 930,123" class="arrow"/>
    <path d="M884 221 H940" class="path"/><polygon points="940,221 930,215 930,227" class="arrow"/>
    <path d="M884 325 H940" class="path"/><polygon points="940,325 930,319 930,331" class="arrow"/>
    <rect x="942" y="76" width="124" height="82" rx="10" class="finish"/><text x="960" y="105" class="title">Product view</text><text x="960" y="126" class="copy">clear next action</text><text x="960" y="143" class="copy">safe wording</text>
    <rect x="942" y="180" width="124" height="82" rx="10" class="finish"/><text x="960" y="209" class="title">Operations view</text><text x="960" y="230" class="copy">each external leg</text><text x="960" y="247" class="copy">recovery evidence</text>
    <rect x="942" y="284" width="124" height="82" rx="10" class="finish"/><text x="960" y="313" class="title">Audit view</text><text x="960" y="334" class="copy">raw + mapped</text><text x="960" y="351" class="copy">version lineage</text>
    <path d="M572 332 H600 V400 H720" class="path-opt"/><polygon points="720,400 710,394 710,406" class="arrow-g"/>
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

## Country lifecycle catalogues — actual events and counts

The six boxes in the shared model are **dimensions**, not a claim that every country has six lifecycle statuses. Country totals must state whether they count official labels, legal event categories, outcome variants, technical acknowledgements or derived product states.

| Country | Confirmed catalogue count at this review | Counting basis | Important boundary |
|---|---:|---|---|
| France | **14 named invoice-status labels** | 4 mandatory + 10 optional labels shown in current DGFiP guidance | The applicable message/profile implementation must follow the effective XP Z12-012 version |
| Spain | **5 statutory categories / 7 explicit outcome variants** | Article 10: 2 required categories producing 3 variants, plus 3 optional categories producing 4 variants | Public-solution reporting under Article 12 is a subset; technical platform statuses await the implementing order |
| Germany | No national total confirmed | Reviewed evidence does not establish one central B2B lifecycle catalogue | Channel/profile acknowledgements must be catalogued separately |
| Ireland | No final domestic B2B total confirmed | Future technical and reporting artefacts remain incomplete | Do not reuse France or Spain counts |
| UK | No final mandate total confirmed | Final lifecycle/profile and reporting artefacts remain open | Peppol direction alone does not establish the UK status catalogue |

### France — 14 named status labels

Current DGFiP customer guidance, updated June 2026, identifies four mandatory statuses and shows ten additional optional statuses. The catalogue must preserve the French label and applicable XP Z12-012 code/profile version before mapping it to shared dimensions.

| Classification | French source status | Primary producer/meaning | Shared dimension effect |
|---|---|---|---|
| Mandatory | `Déposée` | Invoice accepted into the sender platform and timestamped | Technical/document submission evidence; not recipient delivery |
| Mandatory | `Rejetée` | Platform rejects for a technical, consistency or conformity reason | Technical/document rejection |
| Mandatory | `Refusée` | Recipient refuses for a business/commercial reason | Commercial rejection; distinct from technical rejection |
| Mandatory when applicable | `Encaissée` | Supplier records receipt of payment | Payment received/reporting evidence |
| Optional | `Émise par la plateforme` | Sender platform emitted the invoice | Delivery processing |
| Optional | `Reçue par la plateforme` | Recipient platform received the invoice | Delivery evidence at platform boundary |
| Optional | `Mise à disposition` | Invoice made available to the recipient | Delivery/availability; not proof of commercial acceptance |
| Optional | `Prise en charge` | Recipient started handling the invoice | Commercial processing |
| Optional | `Complétée` | Supplier supplied requested supporting information | Document/commercial correction context |
| Optional | `Suspendue` | Processing paused, for example pending supporting material | Commercial/action-required |
| Optional | `En litige` | A dispute exists | Commercial dispute |
| Optional | `Approuvée` | Recipient approved the invoice | Commercial acceptance |
| Optional | `Approuvée partiellement` | Recipient approved only part | Commercial partial acceptance |
| Optional | `Paiement transmis` | Payment instruction/remittance was sent | Payment in progress; not proof of receipt by supplier |

The total is **14 labels**, not “14 steps that every invoice must pass through.” Branching, optionality and applicability mean several labels may never occur for a particular invoice.

Sources: [DGFiP — receiving and following an electronic invoice, June 2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-6_comment-mon-entreprise-va-recevoir-les-factures.pdf) and [DGFiP — applicable external specifications and XP Z12 standards](https://www.impots.gouv.fr/specifications-externes-b2b), accessed 2026-08-25.

### Spain — five legal categories and seven explicit outcome variants

Royal Decree 238/2026 Article 10 defines event categories rather than one end-to-end technical state machine. Splitting “acceptance or rejection” into observable outcomes produces seven explicit variants.

| Obligation | Article 10 category | Explicit outcome variant | Data/timing | Shared dimension effect |
|---|---|---|---|---|
| Required | Full commercial decision | `FULL_ACCEPTED` | Decision date; communicate within the applicable four-day rule | Commercial acceptance |
| Required | Full commercial decision | `FULL_REJECTED` | Decision date and reason/evidence contract to be confirmed | Commercial rejection |
| Required | Effective full payment | `FULL_PAID` | Effective payment date; communicate within the applicable four-day rule | Payment complete |
| Optional | Partial commercial decision | `PARTIALLY_ACCEPTED` | Decision date and affected scope/amount contract to be confirmed | Commercial partial acceptance |
| Optional | Partial commercial decision | `PARTIALLY_REJECTED` | Decision date and affected scope/amount contract to be confirmed | Commercial partial rejection |
| Optional | Partial payment | `PARTIALLY_PAID` | Amount paid and payment date | Payment partial |
| Optional | Assignment to a third party for collection or payment | `ASSIGNED` | Assignee identity, assignment date and collection/payment purpose | Commercial/payment responsibility context; not payment itself |

Article 12 then requires communication to the public solution of **full payment or rejection**. These are not two additional business events when the same fact has already occurred; they are separate reporting obligations/delivery legs for those events. In the absence of rejection or a later correcting invoice, acceptance may be presumed, but `PRESUMED_ACCEPTED` is a **derived view**, not an eighth explicit recipient event.

Technical states such as schema validation, platform receipt, interconnection delivery, public-copy deposit and authority acknowledgement must be added as separate source catalogues when the ministerial order and service specifications define them. They must not be inserted into the seven Article 10 variants merely to reach a target count.

Source: [Spain Royal Decree 238/2026, Articles 10 and 12](https://www.boe.es/eli/es/rd/2026/03/25/238), accessed 2026-08-25.

## Requirements and acceptance

| ID | Requirement / acceptance |
|---|---|
| LS-FR1 | Persist source, country, raw status/reason, source/observed time, correlation, document/exchange-leg identity and payload integrity reference before mapping. |
| LS-FR2 | Map through an immutable, effective-dated catalog identified by country, source, process/document, direction and version. |
| LS-FR3 | Permit one raw event to affect zero, one or several shared dimensions without fabricating a total order. |
| LS-FR4 | Preserve duplicate, unknown, conflicting, regressive and out-of-order evidence; reconciliation appends resolution rather than editing history. |
| LS-FR5 | Keep document, delivery, commercial, payment and reporting status separately queryable and expose technical processing separately. |
| LS-FR6 | A new mapping version applies prospectively unless a governed re-derivation explicitly records old/new versions and reason. |
| LS-FR7 | Every published country count must identify its source/version, counting basis, obligation class and whether entries are explicit source events, technical observations or derived views. |
| LS-AC1 | Given delivery succeeds and authority reporting fails, then product and operations views show both outcomes and recover only the reporting leg. |
| LS-AC2 | Given an unmapped country status, then the raw event is visible, current status is not falsely advanced and a mapping/reconciliation action is created. |
| LS-AC3 | Given a late rejection after a prior acknowledgement, then both events remain and the derived view follows the approved country precedence with an explanation. |
| LS-AC4 | Given a French `Rejetée` event and a French `Refusée` event, then they remain distinct technical/document and commercial rejection facts with their original labels and evidence. |
| LS-AC5 | Given a Spanish full-payment event that must also be reported to the public solution, then one business event creates a separate reporting obligation/outcome rather than a duplicate payment event. |

## Research matrix

| Country | Current discovery position | Required next evidence |
|---|---|---|
| France | Current DGFiP guidance exposes 14 named labels: 4 mandatory and 10 optional | Import the applicable XP Z12-012 codes/profiles, reason/precedence rules and effective versions into governed fixtures |
| Spain | RD 238/2026 Article 10 confirms 5 legal categories/7 explicit outcome variants; Article 12 defines the public full-payment/rejection reporting subset | Keep B2B e-invoice, public-reporting and VERI*FACTU/SII events in separate bounded contexts; add the implementing-order technical catalogue when issued |
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
| 2026-08-12 | Added distinct view connectors, moved reconciliation routing into an open gutter and made the diagram responsive | Confluence visual review |
| 2026-08-25 | Added explicit France and Spain lifecycle catalogues, counting rules and source-to-shared mapping boundaries; recorded unknown totals for Germany, Ireland and UK | User request; DGFiP June 2026 guidance and Spain RD 238/2026 Articles 10/12 |
