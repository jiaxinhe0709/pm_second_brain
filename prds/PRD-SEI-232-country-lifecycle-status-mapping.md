---
id: PRD-SEI-232
title: E-Invoicing — Country Lifecycle Status Mapping
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-08-26
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

Keep the external country/provider status, code, phase, actor, reason and requested action exactly as observed. Map them through an effective-dated country-pack catalog into one or more shared compliance dimensions. Product views are derived from evidence; they are not the legal record and do not force every country into one linear state machine.

For France, use the actual reform lifecycle codes and French terms before deriving a Sage view. For Spain, preserve the exact statutory event terms and reporting obligations while the implementing order has not yet supplied a technical code catalogue. Sage workflow states and UUIDs remain a separate namespace in both cases.

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

## Layered ownership — Sage Network and country packs

Sage Network provides the reusable lifecycle capability. A country pack does not replace that capability; it supplies the official meaning and constraints that Sage Network must apply. A route/provider binding then translates between the governed country contract and the selected external interface.

| Responsibility | Sage Network core | Country compliance pack | Route/provider binding | Sage product |
|---|---|---|---|---|
| Intake | Durable event/command envelope, invoice and correlation identity | Determines whether the event/capability exists for the country | Converts provider webhook, poll, API or file into the envelope | Creates a permitted command or displays an observed event |
| Vocabulary | Namespaced Sage technical/orchestration events and shared lifecycle dimensions | Exact official terms, codes, phase, actors, reasons and actions | Exact provider/protocol values and endpoint version | Customer wording without replacing source evidence |
| Validation | Schema, deduplication, ordering, authority hooks and immutable persistence | Producer role, permitted event, transition, data, deadline and precedence rules | Provider authentication, payload and transport constraints | Product permission and field-level correction experience |
| Execution | Idempotent orchestration, delivery-leg tracking, retry/reconciliation | Required destinations and country-specific reporting obligations | Makes and observes the external operation | Supplies authorised business facts |
| State/view | Technical, document, delivery, commercial, payment and reporting dimensions | Mapping effects and rules for explicit versus derived status | Provider acknowledgement/error observations | Workflow/UI state and next action |
| Governance | Contract compatibility, audit, observability and runtime pack selection | Effective dates, source/version, owner approval, fixtures and retirement | Provider contract/version, environment and readiness evidence | Product adoption/version support |

### Execution direction

| Direction | Sequence | Important control |
|---|---|---|
| Outbound command | Sage product → Sage Network intake → effective country-pack validation/mapping → route/provider binding → external participant/authority | The country pack is evaluated **before** emission; Network must not send a generic status that the country/actor does not permit |
| Inbound observation | External participant/authority → route/provider binding → immutable Sage Network raw event → effective country-pack interpretation → derived view/product | The raw source event is persisted **before** mapping; an unknown mapping never causes the evidence to be discarded |
| Product-only workflow | Sage product/Network workflow event → Sage-qualified state/history | `New`, `File Uploaded` or an internal review state never enters a country namespace unless an evidenced country event separately occurs |
| Reconciliation/replay | Stored raw evidence + original pack/binding versions → compare intended and observed legs → append resolution | Replay must not silently use today's rules to rewrite a historical decision |

This means the country pack is a **governing plug-in to Sage Network**, not a country-specific fork and not merely a lookup table used after delivery.

## How to specify an actual country lifecycle

A useful country lifecycle guide needs the same navigable detail as the supplied Sage Network example, but it must keep the following four namespaces separate.

| Namespace | Examples | Owner | Rule |
|---|---|---|---|
| Country/source lifecycle | France `200 — Déposée`; Spain `Aceptación comercial de la factura` | Country authority, standard or approved provider contract | Preserve exact term, code, actor, event time, obligation and version |
| Provider/protocol observation | HTTP/API result, webhook event, CDAR field or provider error | Route/provider binding | Preserve provider value and version; map only through an approved binding |
| Sage Network event/view | Technical accepted, delivery available, commercial refused, payment received, outcome unknown | Sage Network lifecycle service | May map one source event into several independent dimensions; never replace the source fact |
| Product/workflow state | `New`, `File Uploaded`, review queue, internal UUID/status ID | Sage product | Must use a Sage-qualified product namespace and must not be presented as a regulatory status |

### Country-pack lifecycle contract

Each effective country-pack version must provide or explicitly mark unknown:

| Contract area | Required content |
|---|---|
| Applicability | Jurisdiction, transaction/document type, direction, cohort and effective dates |
| External catalogue | Exact event/status codes and terms, phase, actor, reason/action catalogues and source version |
| Behaviour | Preconditions, permitted paths, repeatability, terminal/correction semantics, precedence and conflict handling |
| Obligations | Mandatory/optional classification, destination, deadline/calendar and acknowledgement evidence |
| Canonical mapping | Effects on each shared dimension plus customer-safe wording and action |
| Binding eligibility | Approved network/channel/provider profiles and versions able to carry the event |
| Verification | Positive, negative, out-of-order, duplicate, correction and historical-version fixtures |
| Governance | Owner, reviewer, confidence, activation/retirement dates and rollback compatibility |

The supplied guide therefore contributes a good **presentation pattern**, not a complete country contract:

| Supplied element | Treatment here |
|---|---|
| `New` and `File Uploaded` | Retained only as possible Sage workflow events; they are not French lifecycle statuses |
| Codes `200`–`213` | Treated as French reform status codes only when matched to the applicable XP Z12-012 catalogue; do not assign `200` to internal workflow states |
| Internal UUID identifier | Keep as an internal mapping ID, outside the country pack's external-code namespace |
| Mandatory/optional and actor | Preserved and expanded with phase, event meaning and reporting boundary |
| Blocked-transition matrix | Not copied as authoritative: its terminal-state rows contradict its own definition and it omits correction, repeated payment and source-leg rules |
| Downloaded matrix | May become a governed fixture only after source, version, owner and checksum are registered |

### Minimum catalogue fields

| Field | Purpose |
|---|---|
| `country`, `source`, `sourceVersion` | Identifies the authority or provider contract actually interpreted |
| `externalPhase`, `externalCode`, `externalTerm`, `externalReasonCode` | Preserves the country vocabulary |
| `producerRole`, `recipientRole`, `direction`, `exchangeLeg` | Distinguishes the actor and point in the lifecycle |
| `obligationClass`, `reportingDestination`, `deadlineRule` | Separates occurrence from mandatory reporting |
| `occurredAt`, `observedAt`, `externalMessageId`, `invoiceIdentity` | Supports ordering, deduplication and reconciliation |
| `requestedActionCode`, `amount`, `currency`, `effectiveDate` | Carries status-specific business detail |
| `mappingVersion`, `dimensionEffects`, `confidence` | Explains the derived Sage view |
| `internalStatusId` | Optional Sage identifier; never reused as the external code |

## Country lifecycle catalogues — actual events and counts

The six boxes in the shared model are **dimensions**, not a claim that every country has six lifecycle statuses. Country totals must state whether they count official labels, legal event categories, outcome variants, technical acknowledgements or derived product states.

| Country | Confirmed catalogue count at this review | Counting basis | Important boundary |
|---|---:|---|---|
| France | **15 distinct standards-level labels / 16 source contexts** | 5 transmission labels plus 10 treatment labels; `Rejetée` has issuing- and receiving-platform contexts. The DGFiP customer guide displays 14 labels because it omits optional `Annulée` | Four statuses are mandatory to the public reporting path when applicable; the implementation catalogue must follow the effective XP Z12-012 version |
| Spain | **5 statutory categories / 7 explicit outcome variants** | Article 10: 2 required categories producing 3 variants, plus 3 optional categories producing 4 variants | Public-solution reporting under Article 12 is a subset; technical platform statuses await the implementing order |
| Germany | No national total confirmed | Reviewed evidence does not establish one central B2B lifecycle catalogue | Channel/profile acknowledgements must be catalogued separately |
| Ireland | No final domestic B2B total confirmed | Future technical and reporting artefacts remain incomplete | Do not reuse France or Spain counts |
| UK | No final mandate total confirmed | Final lifecycle/profile and reporting artefacts remain open | Peppol direction alone does not establish the UK status catalogue |

### Cross-country commonality and existing-evidence matrix

This matrix puts the shared Sage Network capability beside what is **actually evidenced today** in each country. It is not a target-state checklist and a blank technical catalogue must not be filled with another country's terms.

Evidence-state labels:

- **Named** — an authoritative country/standards term is available and can be registered in the country pack.
- **Legal event** — legislation names the business event, but the technical code/message contract is still open.
- **Channel** — the outcome depends on the selected network, provider, profile or bilateral route; it is not one national lifecycle term.
- **Open** — future official detail is required before the country pack can emit or claim that outcome.
- **Not active** — current evidence says the obligation is absent or must remain disabled; this is different from an unknown requirement.

| Lifecycle capability | Reusable Sage Network core | France — existing term/evidence | Spain — existing term/evidence | Germany — existing term/evidence | Ireland — existing term/evidence | UK — existing term/evidence | Commonality decision |
|---|---|---|---|---|---|---|---|
| Technical submission accepted | Technical dimension; raw acknowledgement, actor, source time, message identity and mapping version | **Named:** `200 — Déposée` | **Open:** implementing order/platform catalogue pending; Article 10 commercial events do not prove technical acceptance | **Channel:** validation/acceptance evidence comes from the chosen format and agreed delivery channel | **Open:** delivery and Revenue acknowledgement contracts are not published | **Open:** final UK profile and Access Point acknowledgement contract pending | Reuse the ledger and technical dimension; country/binding supplies the term and proof |
| Technical/document rejection | Failed/rejected dimensions; leg, reason, requested action and retry eligibility | **Named:** `213 — Rejetée à l’émission` or `Rejetée en réception`; the leg must be retained | **Open:** keep technical rejection separate from statutory commercial rejection | **Channel:** profile validator or chosen channel supplies the rejection; no national B2B status term confirmed | **Open:** rejection and correction detail remains specification-dependent and leg-specific | **Open:** Peppol/profile rejection semantics await the approved UK artefacts | Reuse failure handling; never collapse technical rejection into buyer refusal |
| Dispatch, receipt and recipient availability | Delivery dimension with independent dispatched, received, available, failed and unknown observations | **Named:** `201 — Émise par la plateforme`, `202 — Reçue par la plateforme`, `203 — Mise à disposition` | **Open:** platform/interconnection statuses await the technical specification | **Channel:** retain evidence from email, API, portal, shared store or approved EDI route; no universal network state | **Open:** buyer-delivery leg is confirmed, but transport, recipient resolution and acknowledgement are TBD | **Open:** Peppol is the intended network, but final UK delivery/acknowledgement semantics are TBD | Reuse delivery-leg tracking and reconciliation; bind proof to the actual route |
| Commercial processing and full acceptance | Commercial dimension with explicit actor, authority and occurrence time | **Named:** `204 — Prise en charge`; `205 — Approuvée` | **Legal event:** `Aceptación comercial de la factura` | No national B2B event confirmed; any buyer approval is product or bilateral workflow unless later evidenced | **Open:** no national commercial-status catalogue confirmed | **Open:** no final UK commercial-status catalogue confirmed | Reuse the commercial dimension only where the pack activates evidenced semantics |
| Partial acceptance | Partial commercial outcome with affected amount/part and later-event handling | **Named:** `206 — Approuvée partiellement` | **Legal event:** `Aceptación comercial parcial de la factura` | No national B2B event confirmed | **Open** | **Open** | Reuse partial-outcome mechanics; country pack defines eligibility and required detail |
| Commercial rejection | Commercial dimension, reason/evidence and correction path; never technical failure | **Named:** `210 — Refusée` | **Legal event:** `Rechazo comercial de la factura`; full rejection also creates an Article 12 reporting obligation | No national B2B event confirmed | **Open** | **Open** | Reuse commercial refusal and linked reporting-obligation creation where required |
| Partial rejection, dispute or requested information | Dispute/action-required dimension with reason, requested action and resumption evidence | **Named:** `207 — En litige`, `208 — Suspendue`, `209 — Complétée` | **Legal event:** `Rechazo comercial parcial de la factura`; no Article 10 equivalent of France's suspension/completion pair | No national B2B catalogue confirmed; correction follows format/channel and commercial process | **Open** | **Open** | Reuse dispute/action mechanics, but do not invent equivalent country labels |
| Payment initiated | Payment dimension distinct from settlement | **Named:** `211 — Paiement transmis` | No separate Article 10 payment-instruction event | No national e-invoice lifecycle event confirmed | **Open** | **Open** | Keep the shared capability optional and inactive unless the country/process evidences it |
| Partial or full payment received | Repeatable payment events with amount, currency, date and settlement derivation | **Named:** `212 — Encaissée`; may represent partial or full collection and can recur | **Legal event:** `Pago parcial de la factura` and `Pago efectivo completo de la factura`; full payment also creates Article 12 reporting | No national e-invoice lifecycle event confirmed | **Open:** Revenue report content/status and any payment treatment are unpublished | **Open:** no HMRC payment-status obligation confirmed | Reuse payment accounting and aggregation; pack controls event meaning and reporting side effects |
| Assignment for collection/payment | Assignment event and party relationship without implying settlement | No separate named event in the reviewed France reform status list | **Legal event:** `Cesión de la factura a un tercero para su cobro o pago` | No national e-invoice lifecycle event confirmed | **Open** | **Open** | Shared model should support assignment, activated first where Spain evidence requires it |
| Cancellation, replacement or correction | Supersession links, immutable original evidence and correction lineage | **Named:** `220 — Annulée`; link the original to the replacing/correcting invoice | Rectifying invoice process is separate; no Article 10 cancellation-status term | **Channel/profile:** correction and cancellation rules require format/channel evidence | **Open:** correction/cancellation contract pending | **Open:** final correction/cancellation semantics pending | Reuse immutable lineage; country pack defines the valid document/event sequence |
| Government reporting outcome | Separate reporting leg, destination, acknowledgement, failure and reconciliation | **Named obligation:** applicable `Déposée`, `Rejetée`, `Refusée` and `Encaissée` reporting through the public path | **Named obligation:** Article 12 reporting for full rejection and full payment; technical acknowledgement catalogue pending | **Not active:** no current government transaction-reporting leg in this pack | **Legal obligation/open contract:** Revenue report leg is confirmed, but payload, timing and acknowledgements are TBD | **Not active:** no HMRC reporting leg may be inferred from the announced mandate | Reuse the reporting engine; create a leg only when effective country policy requires one |
| Deadline, transition and precedence | Effective-dated rules, calendars, permitted paths, conflict handling and historical version retention | **Named catalogue; incomplete fixture:** mandatory/optional classes and paths exist; full Annex A/deadline fixture still required | **Named rule:** Article 10 four-day communication rule plus event precedence; implementation calendar fixture required | **Channel/policy:** no universal status deadline; preserve agreed-channel and correction evidence | **Open:** report timing, acknowledgements and corrections await Revenue specifications | **Open:** final UK lifecycle/transition rules await official artefacts | Reuse the rule engine; all legal clocks and transitions remain country-owned |

The visual conclusion is not that every country has the same statuses. The common platform surface is the **event ledger, namespaces, independent dimensions, leg correlation, deduplication, ordering, reconciliation, audit and effective-dated execution**. The variable surface is the **actual term/code, actor, permitted event, route proof, deadline, transition, reason/action catalogue and reporting obligation**.

The matrix also exposes where discovery should focus next:

1. France is the reference for a rich, named status catalogue, but not the universal vocabulary.
2. Spain is the reference for statutory commercial/payment events and event-to-reporting side effects while technical status codes remain open.
3. Germany is the reference for channel-neutral lifecycle evidence without a central national B2B status list.
4. Ireland is the reference for two correlated obligations—buyer delivery and authority reporting—whose technical outcomes must remain independent.
5. The UK is the reference for separating a confirmed network direction from still-unconfirmed country lifecycle semantics.

### France — actual reform catalogue

The current XP Z12-012 structure distinguishes **transmission** (`MDT-77 = 305`) from **treatment** (`MDT-77 = 23`). The reform status is carried in `MDT-105`/`MDT-115`; a UNTDID 1373 status is carried separately in `MDT-88`; reasons and requested actions use `MDT-113` and `MDT-121`. These fields must not be replaced by an English label or internal UUID.

#### Status list

| Reform code | Exact French term/context | Public-reporting class | Phase | Set by | External meaning | Shared interpretation |
|---:|---|---|---|---|---|---|
| `200` | `Déposée` | Mandatory | Transmission | Issuing PA | Issuing platform has accepted/deposited the invoice after its applicable controls | Technical submission accepted; recipient delivery remains unproven |
| `201` | `Émise par la plateforme` | Optional | Transmission | Issuing PA | Issuing platform has emitted the invoice towards the receiving route | Delivery dispatched |
| `202` | `Reçue par la plateforme` | Optional | Transmission | Receiving PA | Receiving platform has received the invoice | Delivery received at platform boundary |
| `203` | `Mise à disposition` | Optional | Transmission | Receiving PA | Invoice is available to the buyer | Recipient availability; not commercial acceptance |
| `204` | `Prise en charge` | Optional | Treatment | Buyer or authorised actor | Buyer has started processing the invoice | Commercial processing |
| `205` | `Approuvée` | Optional | Treatment | Buyer or authorised actor | Buyer approves the invoice in full | Explicit commercial acceptance |
| `206` | `Approuvée partiellement` | Optional | Treatment | Buyer or authorised actor | Buyer approves only the identified part/amount | Partial commercial acceptance; details required |
| `207` | `En litige` | Optional | Treatment | Buyer or authorised actor | Commercial dispute requires resolution | Disputed/action required; not technical rejection |
| `208` | `Suspendue` | Optional | Treatment | Buyer or authorised actor | Processing is paused pending information or supporting material | Action required; lifecycle remains open |
| `209` | `Complétée` | Optional | Treatment | Seller or authorised actor | Seller provides the requested complement to a suspended invoice | Additional evidence supplied; buyer must resume its decision |
| `210` | `Refusée` | Mandatory | Treatment | Buyer or authorised actor | Buyer refuses the invoice for an approved business reason | Commercial refusal; distinct from code `213` |
| `211` | `Paiement transmis` | Optional | Treatment | Buyer/payer or authorised actor | Payment or reimbursement instruction has been sent | Payment initiated; funds receipt is unproven |
| `212` | `Encaissée` | Mandatory when applicable | Treatment | Seller/payee or authorised actor | Seller records an effective partial or full collection | Payment received amount; may recur and need amount/date detail |
| `213` | `Rejetée à l’émission` | Mandatory | Transmission | Issuing PA | Issuing-platform controls prevent the invoice continuing | Technical/document rejection on issuing leg |
| `213` | `Rejetée en réception` | Mandatory | Transmission | Receiving PA | Receiving-platform controls prevent the invoice continuing | Technical/document rejection on receiving leg |
| `220` | `Annulée` | Optional | Treatment | Buyer or seller under the applicable correction scenario | Original invoice lifecycle is closed after the replacing/correcting invoice is taken into account | Superseded/cancelled original; preserve link to replacement |

This is **15 distinct terms but 16 observable source contexts**. `Rejetée` cannot be de-duplicated without its issuing/receiving leg. The 14-label DGFiP customer illustration omits `Annulée`; it remains present in the standards/official FAQ lifecycle and must not be lost from the implementation catalogue.

`Encaissée` is not automatically terminal: a partial collection, later collection or approved correction can create further events. “Mandatory” means the relevant status must be reported through the required public path when its regulatory condition occurs; it does not mean every invoice will experience all four mandatory-status types.

#### France transition paths

The country pack should encode guarded **events and paths**, not a single “current status can never move backwards” list.

| Path | Evidenced sequence | Guard/meaning | End behaviour |
|---|---|---|---|
| Nominal transmission | `200 Déposée` → `201 Émise` → `202 Reçue` → `203 Mise à disposition` | Optional visibility events may be absent; a later event must not fabricate a missing earlier event | Opens buyer treatment |
| Issuing technical rejection | Intake/control → `213 Rejetée à l’émission` | Preserve technical reason, action and issuing leg | Terminal for that invoice instance; correction creates a new valid invoice flow |
| Receiving technical rejection | `200/201` → `213 Rejetée en réception` | Preserve receiving leg and rejection reason | Terminal for that invoice instance; do not convert to commercial refusal |
| Nominal treatment/payment | `203` → optional `204` → `205` → optional/repeatable `211` → one or more `212` | Approval, payment instruction and collection are different facts | Payment view derives from amounts; history remains open to reconciliation/correction |
| Suspension/completion | Processing → `208 Suspendue` → `209 Complétée` → buyer processing/decision | Completion answers the missing-information request; it is not final invoice completion | Returns control to buyer |
| Dispute resolution | Processing → `207 En litige` → `205`, `206`, `210`, or correction route | Resolution outcome must be explicit | Do not infer acceptance from dispute closure |
| Commercial refusal | Processing → `210 Refusée` | Approved refusal reason required; business decision, not schema failure | Terminal for that invoice instance; accounting/corrective treatment remains separate |
| Replacement/correction | Original F1 under correction → replacement F2 taken into account → `220 Annulée` on F1 | Preserve F1/F2 relationship and actor | Terminal for F1 only; F2 has its own lifecycle |
| Payment correction | Prior `211` → new `211` with correcting/negative amount where permitted | A status event is appended; the original is not deleted | Derived payment is recalculated with both events |

#### Transition validation classes

| Result | Connector behaviour | Examples |
|---|---|---|
| `ACCEPT` | Persist the source event and derive mapped dimensions | `208 Suspendue` followed by seller `209 Complétée` |
| `INCONSISTENT` | Persist, do not silently advance, and create reconciliation | Late `203 Mise à disposition` observed after a buyer decision; duplicate event with different payload |
| `REJECT` | Reject the attempted command before emission while retaining safe audit evidence | Buyer tries to emit platform-only `200 Déposée`; seller tries to emit buyer-only `210 Refusée` |
| `NEW_DOCUMENT_REQUIRED` | Close/reject the current invoice instance according to the applicable rule and require a new/replacing document | Attempt to re-submit the same rejected invoice as though code `213` had not occurred |

A complete all-pairs matrix remains a governed delivery fixture to import from the applicable XP Z12-012 Annex A/version. It must include role, phase, reason/action requirements, repeatability and correction behaviour; a hand-authored blocked list is insufficient.

Sources: [DGFiP — receiving and following an electronic invoice, June 2026](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-6_comment-mon-entreprise-va-recevoir-les-factures.pdf), [DGFiP — applicable external specifications and XP Z12 standards](https://www.impots.gouv.fr/specifications-externes-b2b), [AFNOR — XP Z12-012, June 2026](https://www.boutique.afnor.org/fr-fr/norme/xp-z12012/formats-et-profils-des-messages-factures-et-statuts-de-cycle-de-vie-constit/fa301169/601641) and [AIFE/Chorus Pro — PA lifecycle FAQ](https://portail.chorus-pro.gouv.fr/aife_documentation?id=kb_article_view&sysparm_article=KB0012866), accessed 2026-08-26.

### Spain — actual statutory events and reporting legs

Royal Decree 238/2026 Article 10 defines event categories rather than a numeric end-to-end state machine. The Spanish term and statutory data are therefore the external truth today; the English uppercase name below is only a proposed Sage canonical event. Numeric source codes remain `TBD_BY_IMPLEMENTING_ORDER`, not `200`–`213` copied from France.

#### Status/event list

| Exact Spanish statutory term | Proposed Sage event | Obligation | Set by | Required event data | Deadline/destination | Shared interpretation |
|---|---|---|---|---|---|---|
| `Aceptación comercial de la factura` | `FULL_ACCEPTED` | Required Article 10 outcome | Recipient or authorised actor | Decision and occurrence date | Communicate to issuer within the Article 10 four-day rule | Explicit commercial acceptance |
| `Rechazo comercial de la factura` | `FULL_REJECTED` | Required Article 10 outcome | Recipient or authorised actor | Decision and occurrence date; technical reason contract pending | Communicate to issuer within four-day rule; also report rejection to public solution under Article 12 | Explicit commercial rejection plus independent reporting obligation |
| `Pago efectivo completo de la factura` | `FULL_PAID` | Required | Recipient or authorised actor | Effective payment date | Communicate to issuer within four-day rule and public solution within Article 12 rule | Payment complete plus independent public-reporting obligation |
| `Aceptación comercial parcial de la factura` | `PARTIALLY_ACCEPTED` | Optional | Recipient or authorised actor | Decision date and affected part/amount when the technical contract defines it | Communicate to issuer within four-day rule | Partial commercial acceptance |
| `Rechazo comercial parcial de la factura` | `PARTIALLY_REJECTED` | Optional | Recipient or authorised actor | Decision date and affected part/amount when defined | Communicate to issuer within four-day rule | Partial commercial rejection |
| `Pago parcial de la factura` | `PARTIALLY_PAID` | Optional | Recipient or authorised actor | Amount paid and payment date | Communicate to issuer within four-day rule | Partial payment; repeatable until/corrected by full payment evidence |
| `Cesión de la factura a un tercero para su cobro o pago` | `ASSIGNED` | Optional | Recipient or authorised actor | Assignee identity and assignment date | Communicate to issuer within four-day rule | Collection/payment responsibility changed; no payment inferred |

The four-day rule is a maximum of four calendar days while excluding Saturdays, Sundays and national holidays, measured from the date the reported event occurs. Its calendar implementation and time-zone/cut-off interpretation require an approved Spain rule fixture.

#### Spain event eligibility and precedence

| Existing evidence | New event | Treatment |
|---|---|---|
| No commercial decision | Full or partial acceptance/rejection | Accept when actor/authority and required data are valid |
| Partial acceptance/rejection | Later full decision | Append; derive the latest approved commercial view without deleting the partial event |
| Explicit full acceptance | Conflicting full rejection, or vice versa | Retain both and reconcile/supersede through an approved correction rule; do not overwrite |
| One or more partial payments | Full payment | Append and derive paid total from source amounts; do not erase instalments |
| Assignment | Partial/full payment | Accept independently; assignment never proves settlement |
| Full rejection | Public-solution rejection report | Create a reporting obligation/outcome referencing the same business event, not another commercial event |
| Full payment | Public-solution payment report | Create a reporting obligation/outcome referencing the same payment event |
| No rejection and no later correcting invoice | Presumed acceptance | Derive `PRESUMED_ACCEPTED`; never store it as an explicit recipient event |
| Technical platform acknowledgement/rejection | Any Article 10 event | Preserve in a separate technical/delivery catalogue; do not map it into commercial status solely by order |

None of the seven Article 10 variants is declared by the decree to be a universal terminal state. Rectifying invoices, discrepancies, public-reporting outcomes and later evidence remain separate events. Technical states such as schema validation, platform receipt, interconnection delivery, faithful-copy deposit and authority acknowledgement must be added when the ministerial order/service specifications define them.

Source: [Spain Royal Decree 238/2026, Articles 10–12](https://www.boe.es/eli/es/rd/2026/03/25/238), accessed 2026-08-26.

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
| LS-FR8 | Country/source codes, UNTDID codes, Sage canonical events, product workflow states and internal UUIDs must use distinct namespaces and remain independently queryable. |
| LS-FR9 | France code `213` must retain issuing-versus-receiving platform leg; its original reason and requested action must be preserved. |
| LS-FR10 | Outbound status commands must validate producer role, phase, invoice identity, authority, required reason/action data and permitted transition before emission. |
| LS-FR11 | Repeatable payment/collection events must retain individual amount, currency, occurrence date and correction/supersession evidence; a `212 Encaissée` event must not automatically mark the full invoice settled. |
| LS-FR12 | Spain technical status codes must remain unknown/open until an applicable implementing-order or approved provider catalogue is registered; French or internal codes must not be reused as placeholders. |
| LS-FR13 | Sage Network must select and record the effective country-pack and route/provider-binding versions for every outbound command before external emission. |
| LS-FR14 | Sage Network must persist an inbound provider/country event with its raw namespace and binding version before country-pack mapping or derived-view changes. |
| LS-FR15 | Country packs must declare applicable events, actors, transitions, obligations and fixtures without implementing separate country event stores, retry engines or product lifecycle APIs. |
| LS-FR16 | Provider bindings must not change country meaning; an unmapped provider value must remain raw/unknown and enter mapping review or reconciliation. |
| LS-FR17 | Sage Network technical success must not imply country document, delivery, commercial, payment or reporting success unless the effective pack maps evidenced source events to those dimensions. |
| LS-FR18 | The cross-country matrix and every country pack must show an actual source term where evidenced and an explicit `legal event`, `channel`, `open` or `not active` state where it is not; a visually empty cell or borrowed country term is not an acceptable substitute. |
| LS-AC1 | Given delivery succeeds and authority reporting fails, then product and operations views show both outcomes and recover only the reporting leg. |
| LS-AC2 | Given an unmapped country status, then the raw event is visible, current status is not falsely advanced and a mapping/reconciliation action is created. |
| LS-AC3 | Given a late rejection after a prior acknowledgement, then both events remain and the derived view follows the approved country precedence with an explanation. |
| LS-AC4 | Given a French `Rejetée` event and a French `Refusée` event, then they remain distinct technical/document and commercial rejection facts with their original labels and evidence. |
| LS-AC5 | Given a Spanish full-payment event that must also be reported to the public solution, then one business event creates a separate reporting obligation/outcome rather than a duplicate payment event. |
| LS-AC6 | Given France code `213` is received from the receiving PA, then the event is stored as receiving-leg `Rejetée` and cannot be mistaken for an issuing-leg rejection solely because the reform code matches. |
| LS-AC7 | Given a product state named `New` or `File Uploaded`, then its API/audit representation uses the Sage namespace and is never emitted or displayed as France code `200`. |
| LS-AC8 | Given a partial French collection followed by another collection, then both code `212` events remain and the payment view is derived from their amounts rather than treating the first as terminal. |
| LS-AC9 | Given a Spain event has no technical source code in the governing contract, then the statutory Spanish term is preserved and the source code remains absent/unknown rather than receiving a fabricated number. |
| LS-AC10 | Given a Sage Network command requests a French buyer-only status from a seller actor, then the active France pack rejects the command before the provider binding is called. |
| LS-AC11 | Given a provider sends an unknown lifecycle code, then Sage Network retains the raw event and binding version, leaves the country-derived view unchanged and creates a mapping/reconciliation action. |
| LS-AC12 | Given a country pack is upgraded after an invoice event, then audit and replay retain the original pack/binding versions unless a governed re-derivation appends a new interpretation. |
| LS-AC13 | Given a country has no confirmed national lifecycle term for a shared capability, when the matrix or product contract is generated, then it identifies the evidence state and does not present another country's term as the local equivalent. |

## Research matrix

| Country | Current discovery position | Required next evidence |
|---|---|---|
| France | The standards-level catalogue has 15 distinct terms and 16 source contexts; the customer illustration shows 14 because it omits optional `Annulée`. Reform codes, phases and principal actors are now named in this discovery | Import the applicable XP Z12-012 Annex A reason/action lists and complete transition matrix into governed, checksum-pinned fixtures; confirm implementation against the June 2026 edition |
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
| 2026-08-26 | Expanded the lifecycle into implementation-oriented source catalogues: corrected France to 15 terms/16 contexts, added reform codes, phases, actors, guarded paths and namespace rules; added Spain's exact statutory terms, event data and precedence without inventing technical codes | User-supplied Sage guide as presentation input; current XP Z12-012/DGFiP/AIFE evidence; Spain RD 238/2026 Articles 10–12 |
| 2026-08-26 | Made Sage Network, country-pack, route/provider-binding and product responsibilities explicit for outbound, inbound and historical reconciliation flows | User product-direction clarification; PRD-SEI-227 shared-platform boundary |
| 2026-08-26 | Added a cross-country commonality matrix showing the reusable Sage Network capability beside actual terms, legal-only events, channel-specific evidence, open specifications and inactive obligations for France, Spain, Germany, Ireland and the UK | User request for an overall visual comparison; PRD-SEI-228/229/230 country-pack evidence |
