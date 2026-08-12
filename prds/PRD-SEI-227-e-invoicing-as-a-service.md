---
id: PRD-SEI-227
title: E-Invoicing as a Service — Shared Platform and Country Packs
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-10
updated: 2026-08-12
reviewers: []
related:
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-228
  - PRD-SEI-229
  - PRD-SEI-230
  - PRD-SEI-231
  - PRD-SEI-232
  - PRD-SEI-233
  - PRD-SEI-234
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: ""
  page_id: "866150169"
  title: e invoice as service commonality
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing as a Service — Shared Platform and Country Packs

## Decision summary

Create one jurisdiction-neutral e-invoicing platform that accepts business invoice intent, determines applicable policy, validates and transforms invoice data, selects the required delivery and reporting routes, normalises lifecycle events, and preserves audit evidence. Country compliance packs provide effective-dated rules, mappings and adapters without forking the shared service.

This PRD is the parent product decision surface. Germany, Ireland and the UK are separate child PRDs because their mandate maturity, delivery topology and reporting obligations differ. France and Spain remain evidence/reference contexts; this document does not silently redefine their approved scope.

> **Product principle:** Sage products express invoice intent; the shared service owns jurisdictional compliance orchestration and returns explainable outcomes through a stable contract.

## Outcome, phase and readiness

| Area | Position |
|---|---|
| Customer outcome | A Sage product can send and receive compliant invoices across supported jurisdictions without embedding each country's regulation and network topology. |
| Business outcome | New country launches reuse tested platform capabilities while country teams retain accountable control of local policy. |
| Current phase | Discovery: validate the shared boundary, canonical semantics, first reference cohort and country-pack governance. |
| Future direction | Add country packs through governed contracts; converge EU behaviour with EN 16931 and ViDA while retaining non-EU variation. |
| Readiness | **Consultation-ready**, not approved for delivery. Architecture, legal, security, operations and country owners must close the named gates. |

## Document and publication hierarchy

| Role | Canonical Git document | Intended Confluence relationship |
|---|---|---|
| Parent | PRD-SEI-227 | Existing page `866150169` — e invoice as service commonality |
| Related page | PRD-SEI-228 — Germany | Existing page `771498625`; preserve current Confluence hierarchy |
| Related page | PRD-SEI-229 — Ireland | Existing page `866140021`; preserve current Confluence hierarchy |
| Related page | PRD-SEI-230 — UK | Existing page `866140019`; preserve current Confluence hierarchy |
| Child analysis | PRD-SEI-231 — Identifiers, tenancy and delegated accountants | New child under page `866150169` |
| Child analysis | PRD-SEI-232 — Country lifecycle status mapping | New child under page `866150169` |
| Child analysis | PRD-SEI-233 — Peppol multi-address and endpoint routing | New child under page `866150169` |
| Child analysis | PRD-SEI-234 — Cross-border applicability and reusable capabilities | New child under page `866150169` |

The original commonality and country documents use existing stable Confluence pages. The four focused research analyses are canonical Git documents published as new children of the commonality page.

## Phased capability model

| Phase | Shared capability | Country-pack responsibility | Delivery claim |
|---|---|---|---|
| 0 — Discover | Common terminology, evidence model, capability contract and gap assessment | Confirm mandate, actors, scope, formats, topology, dates and unresolved policy | Current PRD scope |
| 1 — Reference foundation | Canonical invoice semantics, intake, validation framework, lifecycle evidence, idempotency and audit | First approved scope/validation pack and reference boundary adapter | Proposed; reference country to be selected |
| 2 — Multi-country exchange | Transformation, recipient resolution, pluggable transports, inbound/outbound contract and reconciliation | Germany/Ireland/UK adapters only when official detail and readiness evidence support them | Proposed |
| 3 — Reporting and scale | Government-reporting orchestration, pack versioning, operational controls and country onboarding governance | Effective-dated reporting rules, authority adapters, exception handling and local assurance | Proposed; jurisdiction dates vary |
| Later | Reusable onboarding kit, compatibility policy and retirement controls | Additional jurisdictions and revised policy versions | Direction only |

## One compliance journey, policy and adapters by country

<!-- confluence-html-macro:start -->
<div class="eias-core" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-core *{box-sizing:border-box}.eias-core h2{margin:0;color:#172b4d;font-size:18px}.eias-core .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-core svg{display:block;width:1100px;height:560px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-core .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eias-core .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eias-core .pack{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-core .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.eias-core .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eias-core .title{fill:#172b4d;font-size:11px;font-weight:700}.eias-core .copy{fill:#42526e;font-size:9px}.eias-core .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-core .path{fill:none;stroke:#00875a;stroke-width:2}.eias-core .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.eias-core .path-warn{fill:none;stroke:#ff8b00;stroke-width:1.8;stroke-dasharray:6 4}.eias-core .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-core .arrow{fill:#00875a}.eias-core .arrow-r{fill:#de350b}.eias-core .arrow-a{fill:#ff8b00}.eias-core .arrow-g{fill:#6b778c}.eias-core .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:12px}.eias-core .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eias-core .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The static happy path remains common. Country packs decide applicability and supply rules or adapters; correction and unknown-outcome recovery stay explicit.</p>
  <svg viewBox="0 0 1100 560" role="img" aria-label="A Sage product submits invoice intent to the shared platform. The platform normalises the canonical invoice, determines scope, uses an effective country pack to validate, transform, resolve, transmit and report, then records lifecycle evidence and returns outcomes. Correctable validation failures loop to the product. Timeouts after transmission enter reconciliation before retry. Country packs are optional side modules, not separate products.">
    <text x="35" y="32" class="label">PRODUCT INTENT</text><text x="300" y="32" class="label">SHARED E-INVOICING PLATFORM</text><text x="878" y="32" class="label">EXTERNAL ECOSYSTEM</text>
    <rect x="35" y="80" width="190" height="74" rx="10" class="main"/><text x="55" y="108" class="title">Sage product / ERP</text><text x="55" y="128" class="copy">Create or receive business invoice intent</text>
    <path d="M225 117 H285" class="path"/><polygon points="285,117 275,111 275,123" class="arrow"/>
    <rect x="287" y="70" width="190" height="94" rx="10" class="main"/><text x="307" y="97" class="title">Intake and canonical semantics</text><text x="307" y="118" class="copy">Identity • parties • lines • tax • totals</text><text x="307" y="137" class="copy">payment • references • source provenance</text>
    <path d="M477 117 H517" class="path"/><polygon points="517,117 507,111 507,123" class="arrow"/>
    <rect x="519" y="70" width="190" height="94" rx="10" class="main"/><text x="539" y="97" class="title">Scope and policy decision</text><text x="539" y="118" class="copy">Jurisdiction • transaction • effective date</text><text x="539" y="137" class="copy">document • delivery • reporting duties</text>
    <path d="M709 117 H749" class="path"/><polygon points="749,117 739,111 739,123" class="arrow"/>
    <rect x="751" y="70" width="210" height="94" rx="10" class="main"/><text x="771" y="97" class="title">Execute compliance plan</text><text x="771" y="118" class="copy">Validate • transform • resolve • route</text><text x="771" y="137" class="copy">report • correlate each external leg</text>
    <path d="M961 117 H1025 V245" class="path"/><polygon points="1025,245 1019,235 1031,235" class="arrow"/>
    <rect x="888" y="247" width="174" height="108" rx="10" class="main"/><text x="908" y="275" class="title">External destinations</text><text x="908" y="296" class="copy">Buyer / supplier network</text><text x="908" y="315" class="copy">platform / authority</text><text x="908" y="334" class="copy">acknowledgements and events</text>
    <path d="M888 310 H812" class="path"/><polygon points="812,310 822,304 822,316" class="arrow"/>
    <rect x="590" y="264" width="220" height="92" rx="10" class="finish"/><text x="610" y="292" class="title">Lifecycle and evidence</text><text x="610" y="313" class="copy">Observed events • canonical outcomes</text><text x="610" y="332" class="copy">immutable context • audit • callbacks</text>
    <path d="M590 310 H508" class="path"/><polygon points="508,310 518,304 518,316" class="arrow"/>
    <rect x="286" y="264" width="220" height="92" rx="46" class="finish"/><text x="313" y="300" class="title">Return explainable outcome</text><text x="313" y="322" class="copy">Compliance • delivery • reporting status</text>
    <path d="M396 264 V190 H382 V164" class="path-alert"/><polygon points="382,164 376,174 388,174" class="arrow-r"/>
    <polygon points="382,190 420,228 382,266 344,228" class="bad"/><text x="356" y="224" class="title">Invalid</text><text x="353" y="240" class="copy">correct data</text>
    <path d="M751 164 V212 H792" class="path-warn"/><polygon points="792,212 782,206 782,218" class="arrow-a"/>
    <polygon points="816,184 854,200 870,238 854,276 816,292 778,276 762,238 778,200" class="warn"/><text x="788" y="233" class="title">Outcome unknown</text><text x="792" y="249" class="copy">reconcile first</text>
    <path d="M816 292 V332 H810" class="path-warn"/><polygon points="810,332 820,326 820,338" class="arrow-a"/>
    <rect x="310" y="432" width="176" height="74" rx="10" class="pack"/><text x="330" y="460" class="title">Germany pack</text><text x="330" y="480" class="copy">EN 16931 • formats • transport choice</text>
    <rect x="520" y="432" width="176" height="74" rx="10" class="pack"/><text x="540" y="460" class="title">Ireland pack</text><text x="540" y="480" class="copy">Phases • EN 16931 • Revenue reporting</text>
    <rect x="730" y="432" width="176" height="74" rx="10" class="pack"/><text x="750" y="460" class="title">UK pack</text><text x="750" y="480" class="copy">Peppol direction • 2029 • open policy</text>
    <path d="M398 432 V394 H614 V164" class="path-opt"/><path d="M608 432 V394" class="path-opt"/><path d="M818 432 V394 H614" class="path-opt"/><polygon points="614,164 608,174 620,174" class="arrow-g"/>
  </svg>
  <div class="notes"><div class="note"><strong>Neutral core</strong>No country topology becomes the universal domain model.</div><div class="note"><strong>Independent obligations</strong>Document, delivery and reporting outcomes are correlated but not collapsed.</div><div class="note"><strong>Safe recovery</strong>Validation returns correction details; an ambiguous mutation is reconciled before retry.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Problem and value

Country-by-country products duplicate invoice semantics, validation, lifecycle, API, security and operational behaviour. They also encourage a first country's regulatory topology to become the de facto platform model. That creates four material consequences:

- customers and Sage products experience different contracts and error handling for equivalent invoice tasks;
- country teams repeatedly fund shared foundations while still carrying local accountability;
- operations must learn disconnected status, retry and evidence models;
- regulatory change becomes coupled to product releases instead of governed, effective-dated policy.

The opportunity is not a promised percentage of code reuse. It is a reusable capability contract that confines country work to evidence-backed scope rules, validation profiles, representations, routes, reporting obligations, status mappings and exceptions.

## Goals

| ID | Goal | Measure approach |
|---|---|---|
| G1 | Give Sage products one stable invoice-intent and lifecycle contract across supported countries. | Contract compatibility and country onboarding evidence |
| G2 | Keep regulatory policy explainable, effective-dated and owned by an accountable country team. | Policy provenance and decision audit completeness |
| G3 | Reuse validation, transformation, routing, lifecycle, reporting, resilience, security and operations frameworks. | Capability reuse assessment; no unsupported percentage target |
| G4 | Separate document, delivery and reporting compliance so each can succeed, fail and reconcile independently. | Scenario and operational test results |
| G5 | Add a country without forking the platform or rewriting historical invoice context. | Reference country-pack onboarding exercise |

## Non-goals

- Declaring the France implementation to be the core model or automatically reusable.
- Approving a canonical physical schema, API endpoint shape, rules engine, workflow product or provider.
- Replacing country legal/compliance interpretation.
- Combining Spain B2B e-invoicing and fiscal-record/VERI*FACTU obligations into one domain.
- Committing UK/Ireland behaviours that official policy has not specified.
- Migrating existing France or Spain production traffic in this discovery phase.
- Setting unsupported reuse, latency, availability, volume, retention or rollout targets.

## Definitions and product boundaries

| Concept | Meaning | Must not be confused with |
|---|---|---|
| Invoice intent | Product-supplied business facts and requested operation | A country-compliant outbound representation |
| Canonical invoice semantics | Jurisdiction-neutral business meaning with extension/provenance support | One mandatory physical payload or lossless replacement for source evidence |
| Country policy version | Effective-dated applicability, validation and obligation decisions | Application release version |
| Country pack | Governed rules, mappings, adapters, status translation and evidence | A separate country product or code fork |
| Network or channel | Interoperability ecosystem or delivery mechanism selected by evidence-backed policy, such as Peppol, a national platform, private interoperability or an agreed direct channel | The organisation providing Sage's connection |
| Service provider | Contracted organisation performing one or more network, platform, reporting, directory or compliance roles | The network, regulation or Sage adapter |
| Peppol Access Point | Peppol-certified service-provider role connecting a participant to the Peppol Network; sender and recipient may choose different providers | Peppol itself or a universal provider selection |
| SMP / capability lookup | Service that publishes or discovers participant addressing and supported document capabilities; it may be supplied with or separately from Access Point service | The sending Access Point or the invoice profile |
| Technical adapter | Sage-controlled connector and configuration for a provider, platform, authority or direct channel | Country regulation or the external service itself |
| Document compliance | Whether the structured invoice representation satisfies applicable semantic/business rules | Delivery or authority reporting success |
| Delivery compliance | Whether the invoice reached the required recipient through an eligible route | Government reporting |
| Reporting compliance | Whether required transaction/invoice/payment data reached the authority | Buyer delivery |
| External status | Provider/network/authority vocabulary | Canonical lifecycle event |
| Current route | Configuration used for a new eligible exchange | The immutable route/context of an existing invoice |

## Separate regulation, network, provider and adapter

<!-- confluence-html-macro:start -->
<div class="eias-route-model" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-route-model *{box-sizing:border-box}.eias-route-model .sub{margin:0 0 16px;color:#6b778c;font-size:12px}.eias-route-model svg{display:block;width:1100px;height:500px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-route-model .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eias-route-model .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eias-route-model .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-route-model .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-route-model .copy{fill:#42526e;font-size:8.5px}.eias-route-model .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-route-model .path{fill:none;stroke:#00875a;stroke-width:2}.eias-route-model .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-route-model .arrow{fill:#00875a}.eias-route-model .arrow-g{fill:#6b778c}.eias-route-model .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-route-model .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eias-route-model .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Policy selects an eligible route; execution binds a separate provider role and Sage adapter. Provider examples remain research candidates, not approved architecture or procurement choices.</p>
  <svg viewBox="0 0 1100 500" role="img" aria-label="A decision chain separates country or jurisdiction, regulatory model, eligible network or channel, provider service role and Sage technical adapter. A Peppol execution example then shows a Sage product using a Sage adapter, a selected sending Access Point provider, the Peppol Network, a recipient Access Point that may be a different provider, and the buyer. Peppol is explicitly the network, not the provider, and no vendor is selected.">
    <text x="30" y="30" class="label">ROUTE DECISION — CONCEPTS REMAIN DISTINCT</text>
    <rect x="30" y="58" width="178" height="82" rx="10" class="main"/><text x="50" y="88" class="title">Country / jurisdiction</text><text x="50" y="109" class="copy">Legal and operating context</text><text x="50" y="126" class="copy">UK • Germany • Ireland • etc.</text>
    <path d="M208 99 H236" class="path"/><polygon points="236,99 226,93 226,105" class="arrow"/>
    <rect x="238" y="58" width="178" height="82" rx="10" class="main"/><text x="258" y="88" class="title">Regulatory model</text><text x="258" y="109" class="copy">Scope • duties • effective policy</text><text x="258" y="126" class="copy">document • delivery • reporting</text>
    <path d="M416 99 H444" class="path"/><polygon points="444,99 434,93 434,105" class="arrow"/>
    <rect x="446" y="58" width="178" height="82" rx="10" class="main"/><text x="466" y="88" class="title">Network / channel</text><text x="466" y="109" class="copy">Peppol • national platform</text><text x="466" y="126" class="copy">private or agreed direct route</text>
    <path d="M624 99 H652" class="path-opt"/><polygon points="652,99 642,93 642,105" class="arrow-g"/>
    <rect x="654" y="58" width="178" height="82" rx="10" class="optional"/><text x="674" y="88" class="title">Provider service / role</text><text x="674" y="109" class="copy">Contracting entity • authority</text><text x="674" y="126" class="copy">AP • SMP • platform • reporting</text>
    <path d="M832 99 H860" class="path-opt"/><polygon points="860,99 850,93 850,105" class="arrow-g"/>
    <rect x="862" y="58" width="208" height="82" rx="10" class="optional"/><text x="882" y="88" class="title">Sage adapter / configuration</text><text x="882" y="109" class="copy">API or transport connector</text><text x="882" y="126" class="copy">credentials • version • environment</text>
    <line x1="30" y1="184" x2="1070" y2="184" stroke="#dfe1e6"/>
    <text x="30" y="218" class="label">PEPPOL FOUR-CORNER EXECUTION EXAMPLE — NO VENDOR SELECTED</text>
    <rect x="30" y="254" width="146" height="76" rx="10" class="main"/><text x="50" y="283" class="title">Sage product</text><text x="50" y="304" class="copy">Invoice intent</text>
    <path d="M176 292 H202" class="path"/><polygon points="202,292 192,286 192,298" class="arrow"/>
    <rect x="204" y="254" width="146" height="76" rx="10" class="main"/><text x="224" y="283" class="title">Sage adapter</text><text x="224" y="304" class="copy">Provider-specific boundary</text>
    <path d="M350 292 H376" class="path"/><polygon points="376,292 366,286 366,298" class="arrow"/>
    <rect x="378" y="246" width="172" height="92" rx="10" class="main"/><text x="398" y="276" class="title">Sending Access Point</text><text x="398" y="297" class="copy">Selected certified provider role</text><text x="398" y="316" class="copy">Sage-side contract and trust</text>
    <path d="M550 292 H576" class="path"/><polygon points="576,292 566,286 566,298" class="arrow"/>
    <rect x="578" y="246" width="154" height="92" rx="10" class="main"/><text x="598" y="276" class="title">Peppol Network</text><text x="598" y="297" class="copy">Shared rules • discovery</text><text x="598" y="316" class="copy">trust and interoperability</text>
    <path d="M732 292 H758" class="path"/><polygon points="758,292 748,286 748,298" class="arrow"/>
    <rect x="760" y="246" width="184" height="92" rx="10" class="main"/><text x="780" y="276" class="title">Receiving Access Point</text><text x="780" y="297" class="copy">Buyer's chosen provider</text><text x="780" y="316" class="copy">may differ from Sage's provider</text>
    <path d="M944 292 H970" class="path"/><polygon points="970,292 960,286 960,298" class="arrow"/>
    <rect x="972" y="254" width="98" height="76" rx="38" class="finish"/><text x="995" y="284" class="title">Buyer</text><text x="991" y="305" class="copy">Receives</text>
    <rect x="250" y="388" width="600" height="52" rx="26" class="finish"/><text x="335" y="410" class="title">ExecutionRoute = policy + channel + provider role + adapter + recipient</text><text x="382" y="429" class="copy">Each element is evidenced, versioned and retained with invoice history</text>
  </svg>
  <div class="notes"><div class="note"><strong>Peppol is not the provider</strong>It supplies shared specifications, discovery, trust and network interoperability.</div><div class="note"><strong>Independent choice</strong>Sender and recipient can use different certified Access Point providers.</div><div class="note"><strong>No vendor decision</strong>Certification, jurisdiction, role, contract, coverage and operations still require evidence and approval.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Document, delivery and reporting compliance

<!-- confluence-html-macro:start -->
<div class="eias-domains" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1040px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-domains *{box-sizing:border-box}.eias-domains h2{margin:0;color:#172b4d;font-size:18px}.eias-domains .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-domains svg{display:block;width:960px;height:360px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-domains .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.7}.eias-domains .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-domains .title{fill:#172b4d;font-size:12px;font-weight:700}.eias-domains .copy{fill:#42526e;font-size:9px}.eias-domains .path{fill:none;stroke:#00875a;stroke-width:2}.eias-domains .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-domains .arrow{fill:#00875a}.eias-domains .arrow-g{fill:#6b778c}.eias-domains .legend{display:flex;gap:18px;min-width:960px;margin-top:10px;color:#42526e;font-size:10px}.eias-domains .key{display:flex;gap:6px;align-items:center}.eias-domains .sw{width:18px;height:10px;border-radius:4px;background:#e3fcef;border:1px solid #36b37e}.eias-domains .sw.opt{background:#f4f5f7;border-color:#6b778c;border-style:dashed}
  </style>
  <p class="sub">Country policy activates only the applicable branches; no branch inherits success from another.</p>
  <svg viewBox="0 0 960 360" role="img" aria-label="Invoice intent is evaluated by country policy and then branches into document compliance, delivery compliance and reporting compliance. Each branch produces an independent outcome and evidence record. Reporting can be inactive when the country has no current obligation.">
    <rect x="40" y="135" width="170" height="76" rx="10" class="main"/><text x="62" y="164" class="title">Invoice intent</text><text x="62" y="184" class="copy">Business facts and requested action</text>
    <path d="M210 173 H292" class="path"/><polygon points="292,173 282,167 282,179" class="arrow"/>
    <rect x="294" y="128" width="170" height="90" rx="10" class="main"/><text x="316" y="158" class="title">Country policy</text><text x="316" y="178" class="copy">Scope • effective date • exemptions</text><text x="316" y="196" class="copy">required obligations and versions</text>
    <path d="M464 173 H510 V68 H550" class="path"/><polygon points="550,68 540,62 540,74" class="arrow"/>
    <path d="M464 173 H550" class="path"/><polygon points="550,173 540,167 540,179" class="arrow"/>
    <path d="M464 173 H510 V278 H550" class="path-opt"/><polygon points="550,278 540,272 540,284" class="arrow-g"/>
    <rect x="552" y="32" width="230" height="76" rx="10" class="main"/><text x="574" y="60" class="title">Document compliance</text><text x="574" y="80" class="copy">Semantic/profile validation and representation</text>
    <rect x="552" y="135" width="230" height="76" rx="10" class="main"/><text x="574" y="163" class="title">Delivery compliance</text><text x="574" y="183" class="copy">Recipient resolution, route and acknowledgement</text>
    <rect x="552" y="240" width="230" height="76" rx="10" class="optional"/><text x="574" y="268" class="title">Reporting compliance</text><text x="574" y="288" class="copy">Authority data, deadline and acknowledgement</text>
    <path d="M782 70 H846" class="path"/><path d="M782 173 H846" class="path"/><path d="M782 278 H846" class="path-opt"/><polygon points="846,70 836,64 836,76" class="arrow"/><polygon points="846,173 836,167 836,179" class="arrow"/><polygon points="846,278 836,272 836,284" class="arrow-g"/>
    <rect x="848" y="120" width="76" height="106" rx="38" class="main"/><text x="865" y="162" class="title">Evidence</text><text x="863" y="182" class="copy">3 outcomes</text><text x="861" y="199" class="copy">1 context</text>
  </svg>
  <div class="legend"><span class="key"><span class="sw"></span>Required active obligation</span><span class="key"><span class="sw opt"></span>Policy-activated optional route</span></div>
</div>
<!-- confluence-html-macro:end -->

## Visual research atlas

The strategic, route-model and compliance visuals above plus the atlas below consolidate every distinct diagrammatic idea from the research. Repeated country variants share one comparison visual; code-like snippets remain text where visual treatment adds noise.

### One semantic invoice, many compliant boundary forms

<!-- confluence-html-macro:start -->
<div class="eias-canonical" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-canonical *{box-sizing:border-box}.eias-canonical h2{margin:0;color:#172b4d;font-size:18px}.eias-canonical .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-canonical svg{display:block;width:1100px;height:610px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-canonical .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eias-canonical .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eias-canonical .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-canonical .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.eias-canonical .title{fill:#172b4d;font-size:11px;font-weight:700}.eias-canonical .copy{fill:#42526e;font-size:9px}.eias-canonical .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-canonical .path{fill:none;stroke:#00875a;stroke-width:2}.eias-canonical .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-canonical .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.eias-canonical .arrow{fill:#00875a}.eias-canonical .arrow-g{fill:#6b778c}.eias-canonical .arrow-r{fill:#de350b}.eias-canonical .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-canonical .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-canonical .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The core stores business meaning and provenance once; country-specific names, formats and fields remain at governed boundaries.</p>
  <svg viewBox="0 0 1100 610" role="img" aria-label="A red country-fork anti-pattern with FrenchInvoice, SpanishInvoice and GermanInvoice is replaced by one canonical invoice. The canonical invoice contains identity, supplier, buyer, lines, tax, totals, payment, references and governed country extensions. Versioned country mappers produce French, Spanish, German, Irish and future UK compliant representations, while provenance remains attached.">
    <text x="34" y="30" class="label">AVOID COUNTRY DOMAIN FORKS</text><text x="332" y="30" class="label">SHARED SEMANTICS</text><text x="820" y="30" class="label">BOUNDARY REPRESENTATIONS</text>
    <polygon points="145,72 205,132 145,192 85,132" class="bad"/><text x="108" y="116" class="title">Country types</text><text x="101" y="136" class="copy">FrenchInvoice</text><text x="101" y="152" class="copy">SpanishInvoice</text><text x="101" y="168" class="copy">GermanInvoice</text>
    <path d="M205 132 H290" class="path-alert"/><polygon points="290,132 280,126 280,138" class="arrow-r"/>
    <rect x="292" y="62" width="420" height="444" rx="12" class="main"/><text x="316" y="92" class="title">CanonicalInvoice — proposed semantic model</text><text x="316" y="112" class="copy">Stable business meaning • source provenance • versioned extensions</text>
    <rect x="316" y="138" width="170" height="62" rx="8" class="finish"/><text x="334" y="162" class="title">Identity</text><text x="334" y="181" class="copy">ID • type • date • currency • original ref</text>
    <rect x="514" y="138" width="174" height="62" rx="8" class="finish"/><text x="532" y="162" class="title">Supplier</text><text x="532" y="181" class="copy">Legal/tax IDs • e-address • postal</text>
    <rect x="316" y="218" width="170" height="62" rx="8" class="finish"/><text x="334" y="242" class="title">Buyer</text><text x="334" y="261" class="copy">Legal/tax IDs • e-address • postal</text>
    <rect x="514" y="218" width="174" height="62" rx="8" class="finish"/><text x="532" y="242" class="title">Invoice lines</text><text x="532" y="261" class="copy">Item • quantity • price • tax • discount</text>
    <rect x="316" y="298" width="170" height="62" rx="8" class="finish"/><text x="334" y="322" class="title">Tax breakdown</text><text x="334" y="341" class="copy">Categories • rates • taxable/charged amounts</text>
    <rect x="514" y="298" width="174" height="62" rx="8" class="finish"/><text x="532" y="322" class="title">Totals</text><text x="532" y="341" class="copy">Line • tax-exclusive/inclusive • payable</text>
    <rect x="316" y="378" width="170" height="62" rx="8" class="finish"/><text x="334" y="402" class="title">Payment</text><text x="334" y="421" class="copy">Method • due date • bank details</text>
    <rect x="514" y="378" width="174" height="62" rx="8" class="finish"/><text x="532" y="402" class="title">References</text><text x="532" y="421" class="copy">PO • contract • delivery • previous invoice</text>
    <rect x="316" y="458" width="372" height="32" rx="8" class="optional"/><text x="334" y="479" class="title">Governed CountryExtensions + source evidence</text>
    <path d="M712 118 H780 V84 H824" class="path"/><polygon points="824,84 814,78 814,90" class="arrow"/>
    <path d="M712 198 H780 V178 H824" class="path"/><polygon points="824,178 814,172 814,184" class="arrow"/>
    <path d="M712 278 H780 V272 H824" class="path"/><polygon points="824,272 814,266 814,278" class="arrow"/>
    <path d="M712 358 H780 V366 H824" class="path"/><polygon points="824,366 814,360 814,372" class="arrow"/>
    <path d="M712 438 H780 V460 H824" class="path-opt"/><polygon points="824,460 814,454 814,466" class="arrow-g"/>
    <rect x="826" y="52" width="238" height="64" rx="10" class="main"/><text x="846" y="77" class="title">France mapper</text><text x="846" y="96" class="copy">Approved French representation/profile</text>
    <rect x="826" y="146" width="238" height="64" rx="10" class="main"/><text x="846" y="171" class="title">Spain mapper</text><text x="846" y="190" class="copy">Approved Spanish representation/profile</text>
    <rect x="826" y="240" width="238" height="64" rx="10" class="main"/><text x="846" y="265" class="title">Germany mapper</text><text x="846" y="284" class="copy">XRechnung • eligible ZUGFeRD</text>
    <rect x="826" y="334" width="238" height="64" rx="10" class="main"/><text x="846" y="359" class="title">Ireland mapper</text><text x="846" y="378" class="copy">EN 16931 implementation • detail gated</text>
    <rect x="826" y="428" width="238" height="64" rx="10" class="optional"/><text x="846" y="453" class="title">UK / future mapper</text><text x="846" y="472" class="copy">Activate only when profile is approved</text>
    <rect x="292" y="536" width="772" height="44" rx="22" class="finish"/><text x="430" y="563" class="title">Invariant: inside the platform, business meaning uses CanonicalInvoice; formats remain at boundaries</text>
  </svg>
  <div class="notes"><div class="note"><strong>Not a physical-schema decision</strong>This is a semantic coverage model for discovery.</div><div class="note"><strong>Extensions are governed</strong>Country facts retain source, owner and effective version.</div><div class="note"><strong>Transformation proves no loss</strong>Every mapper records validation and representation provenance.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Same primitives, different government-facing topology

<!-- confluence-html-macro:start -->
<div class="eias-topologies" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-topologies *{box-sizing:border-box}.eias-topologies h2{margin:0;color:#172b4d;font-size:18px}.eias-topologies .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-topologies svg{display:block;width:1100px;height:650px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-topologies .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-topologies .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-topologies .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-topologies .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-topologies .copy{fill:#42526e;font-size:8.5px}.eias-topologies .country{fill:#172b4d;font-size:11px;font-weight:700}.eias-topologies .path{fill:none;stroke:#00875a;stroke-width:2}.eias-topologies .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-topologies .arrow{fill:#00875a}.eias-topologies .arrow-g{fill:#6b778c}.eias-topologies .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-topologies .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-topologies .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Delivery and reporting are shown separately. Dashed routes are optional, future or policy-dependent.</p>
  <svg viewBox="0 0 1100 650" role="img" aria-label="Five country lanes compare e-invoicing topologies. France sends from seller through approved platforms to buyer and separately reports invoice, transaction and payment data to DGFiP. Spain sends through private platforms, provides a faithful UBL copy to the public solution, and can alternatively use the public solution. Germany delivers a structured invoice through a counterparty-agreed channel. Ireland delivers to the buyer and separately reports a subset to Revenue. The UK Peppol route is a newer confirmed direction with reporting still inactive.">
    <text x="34" y="30" class="country">FRANCE</text>
    <rect x="120" y="48" width="130" height="54" rx="8" class="main"/><text x="158" y="80" class="title">Seller</text><path d="M250 75 H306" class="path"/><polygon points="306,75 296,69 296,81" class="arrow"/>
    <rect x="308" y="48" width="150" height="54" rx="8" class="main"/><text x="337" y="72" class="title">Approved platform A</text><text x="340" y="88" class="copy">transmit + report</text><path d="M458 75 H514" class="path"/><polygon points="514,75 504,69 504,81" class="arrow"/>
    <rect x="516" y="48" width="150" height="54" rx="8" class="main"/><text x="545" y="72" class="title">Approved platform B</text><text x="554" y="88" class="copy">recipient route</text><path d="M666 75 H722" class="path"/><polygon points="722,75 712,69 712,81" class="arrow"/>
    <rect x="724" y="48" width="130" height="54" rx="27" class="finish"/><text x="762" y="80" class="title">Buyer</text><path d="M383 102 V128 H902" class="path-opt"/><polygon points="902,128 892,122 892,134" class="arrow-g"/>
    <rect x="904" y="102" width="160" height="54" rx="8" class="optional"/><text x="955" y="125" class="title">DGFiP</text><text x="925" y="141" class="copy">invoice • transaction • payment data</text>
    <line x1="34" y1="174" x2="1066" y2="174" stroke="#dfe1e6"/>
    <text x="34" y="204" class="country">SPAIN</text>
    <rect x="120" y="222" width="130" height="54" rx="8" class="main"/><text x="158" y="254" class="title">Seller</text><path d="M250 249 H306" class="path"/><polygon points="306,249 296,243 296,255" class="arrow"/>
    <rect x="308" y="222" width="150" height="54" rx="8" class="main"/><text x="337" y="246" class="title">Private platform A</text><text x="346" y="262" class="copy">transform + sign</text><path d="M458 249 H514" class="path"/><polygon points="514,249 504,243 504,255" class="arrow"/>
    <rect x="516" y="222" width="150" height="54" rx="8" class="main"/><text x="545" y="246" class="title">Private platform B</text><text x="552" y="262" class="copy">interconnection</text><path d="M666 249 H722" class="path"/><polygon points="722,249 712,243 712,255" class="arrow"/>
    <rect x="724" y="222" width="130" height="54" rx="27" class="finish"/><text x="762" y="254" class="title">Buyer</text>
    <path d="M383 276 V306 H516" class="path-opt"/><polygon points="516,306 506,300 506,312" class="arrow-g"/><rect x="518" y="286" width="210" height="54" rx="8" class="optional"/><text x="568" y="309" class="title">Public solution</text><text x="549" y="325" class="copy">faithful UBL copy / alternate route</text><path d="M728 313 H854 V276" class="path-opt"/><polygon points="854,276 848,286 860,286" class="arrow-g"/>
    <line x1="34" y1="358" x2="1066" y2="358" stroke="#dfe1e6"/>
    <text x="34" y="388" class="country">GERMANY</text>
    <rect x="120" y="406" width="180" height="54" rx="8" class="main"/><text x="159" y="430" class="title">Seller + structured invoice</text><text x="165" y="446" class="copy">XRechnung / eligible ZUGFeRD</text><path d="M300 433 H442" class="path"/><polygon points="442,433 432,427 432,439" class="arrow"/>
    <rect x="444" y="406" width="250" height="54" rx="8" class="optional"/><text x="498" y="430" class="title">Counterparty-agreed channel</text><text x="492" y="446" class="copy">email • API • portal • shared store • EDI</text><path d="M694 433 H780" class="path"/><polygon points="780,433 770,427 770,439" class="arrow"/><rect x="782" y="406" width="150" height="54" rx="27" class="finish"/><text x="835" y="438" class="title">Buyer</text>
    <line x1="34" y1="482" x2="1066" y2="482" stroke="#dfe1e6"/>
    <text x="34" y="512" class="country">IRELAND</text>
    <rect x="120" y="530" width="180" height="54" rx="8" class="main"/><text x="165" y="554" class="title">EN 16931 invoice</text><text x="158" y="570" class="copy">Phase One cohort and date apply</text><path d="M300 557 H500" class="path"/><polygon points="500,557 490,551 490,563" class="arrow"/><rect x="502" y="530" width="160" height="54" rx="27" class="finish"/><text x="532" y="562" class="title">Business buyer</text><path d="M300 557 H370 V615 H722" class="path-opt"/><polygon points="722,615 712,609 712,621" class="arrow-g"/><rect x="724" y="590" width="208" height="50" rx="8" class="optional"/><text x="790" y="613" class="title">Revenue</text><text x="756" y="629" class="copy">required subset • interface detail gated</text>
    <text x="954" y="388" class="country">UK</text><rect x="944" y="406" width="122" height="54" rx="8" class="optional"/><text x="972" y="430" class="title">Peppol core</text><text x="957" y="446" class="copy">see UK child PRD</text>
  </svg>
  <div class="notes"><div class="note"><strong>Document ≠ route</strong>The same semantic invoice can travel through different approved topologies.</div><div class="note"><strong>Delivery ≠ reporting</strong>Buyer and authority legs keep separate evidence and recovery.</div><div class="note"><strong>Country pack owns delta</strong>Topology, identifiers, formats, reports and statuses are policy-specific.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Events preserve country language; canonical meaning powers products

<!-- confluence-html-macro:start -->
<div class="eias-lifecycle" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-lifecycle *{box-sizing:border-box}.eias-lifecycle h2{margin:0;color:#172b4d;font-size:18px}.eias-lifecycle .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-lifecycle svg{display:block;width:1100px;height:570px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-lifecycle .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-lifecycle .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-lifecycle .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.eias-lifecycle .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-lifecycle .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-lifecycle .copy{fill:#42526e;font-size:8.5px}.eias-lifecycle .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-lifecycle .path{fill:none;stroke:#00875a;stroke-width:2}.eias-lifecycle .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.eias-lifecycle .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-lifecycle .arrow{fill:#00875a}.eias-lifecycle .arrow-r{fill:#de350b}.eias-lifecycle .arrow-g{fill:#6b778c}.eias-lifecycle .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-lifecycle .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-lifecycle .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The lifecycle is an event vocabulary, not a promise that every country uses every state or follows one linear path.</p>
  <svg viewBox="0 0 1100 570" role="img" aria-label="A proposed canonical invoice lifecycle flows from Created to Validated to Sent to Received to Accepted and Paid, with a red rejected branch from Received. A side mapping converts French and Spanish external statuses to canonical events while preserving the original value. An InvoiceEvent record stores invoice ID, event and effective timestamps, actor, country, raw and canonical status, reason, amount and metadata.">
    <text x="34" y="30" class="label">PROPOSED CANONICAL EVENT SPINE</text><text x="770" y="30" class="label">RAW-TO-CANONICAL MAPPING</text>
    <rect x="34" y="72" width="128" height="58" rx="9" class="main"/><text x="70" y="106" class="title">CREATED</text><path d="M162 101 H204" class="path"/><polygon points="204,101 194,95 194,107" class="arrow"/>
    <rect x="206" y="72" width="128" height="58" rx="9" class="main"/><text x="235" y="106" class="title">VALIDATED</text><path d="M334 101 H376" class="path"/><polygon points="376,101 366,95 366,107" class="arrow"/>
    <rect x="378" y="72" width="128" height="58" rx="9" class="main"/><text x="425" y="106" class="title">SENT</text><path d="M506 101 H548" class="path"/><polygon points="548,101 538,95 538,107" class="arrow"/>
    <rect x="550" y="72" width="128" height="58" rx="9" class="main"/><text x="584" y="106" class="title">RECEIVED</text>
    <path d="M614 130 V186 H334" class="path"/><polygon points="334,186 344,180 344,192" class="arrow"/><rect x="206" y="157" width="128" height="58" rx="9" class="finish"/><text x="237" y="191" class="title">ACCEPTED</text><path d="M270 215 V258" class="path"/><polygon points="270,258 264,248 276,248" class="arrow"/><rect x="206" y="260" width="128" height="58" rx="29" class="finish"/><text x="251" y="294" class="title">PAID</text>
    <path d="M614 130 V186 H548" class="path-alert"/><polygon points="548,186 558,180 558,192" class="arrow-r"/><polygon points="486,144 528,186 486,228 444,186" class="bad"/><text x="458" y="182" class="title">REJECTED</text><text x="459" y="198" class="copy">reason retained</text>
    <rect x="764" y="62" width="302" height="176" rx="10" class="optional"/><text x="784" y="88" class="title">Versioned external status mapping</text><text x="784" y="116" class="copy">France “Déposée” → SUBMITTED</text><text x="784" y="140" class="copy">France “Rejetée” → REJECTED</text><text x="784" y="164" class="copy">Spain aceptación → ACCEPTED</text><text x="784" y="188" class="copy">Spain rechazo → REJECTED</text><text x="784" y="212" class="copy">Spain pago completo → PAID</text><path d="M764 150 H704 V101 H678" class="path-opt"/><polygon points="678,101 688,95 688,107" class="arrow-g"/>
    <text x="34" y="370" class="label">DURABLE EVENT EVIDENCE</text>
    <rect x="34" y="394" width="1032" height="132" rx="10" class="main"/><text x="56" y="422" class="title">InvoiceEvent</text>
    <rect x="56" y="440" width="180" height="58" rx="8" class="finish"/><text x="74" y="464" class="title">Identity and time</text><text x="74" y="483" class="copy">invoiceId • event/effective timestamp</text>
    <rect x="256" y="440" width="180" height="58" rx="8" class="finish"/><text x="274" y="464" class="title">Source context</text><text x="274" y="483" class="copy">actor • country • network • provider</text>
    <rect x="456" y="440" width="180" height="58" rx="8" class="finish"/><text x="474" y="464" class="title">Status evidence</text><text x="474" y="483" class="copy">externalStatus • canonicalStatus</text>
    <rect x="656" y="440" width="180" height="58" rx="8" class="finish"/><text x="674" y="464" class="title">Business detail</text><text x="674" y="483" class="copy">reasonCode • amount • document leg</text>
    <rect x="856" y="440" width="180" height="58" rx="8" class="finish"/><text x="874" y="464" class="title">Provenance</text><text x="874" y="483" class="copy">mapping version • metadata • evidence</text>
  </svg>
  <div class="notes"><div class="note"><strong>Build once</strong>A shared lifecycle service handles durable events and derived views.</div><div class="note"><strong>Do not erase language</strong>Raw country/provider status remains available beside its mapping.</div><div class="note"><strong>Optional states stay optional</strong>Acceptance, payment or clearance activate only where evidence requires them.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Resolve destinations and transform formats through shared interfaces

<!-- confluence-html-macro:start -->
<div class="eias-boundaries" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-boundaries *{box-sizing:border-box}.eias-boundaries h2{margin:0;color:#172b4d;font-size:18px}.eias-boundaries .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-boundaries svg{display:block;width:1100px;height:650px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-boundaries .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-boundaries .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-boundaries .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-boundaries .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-boundaries .copy{fill:#42526e;font-size:8.5px}.eias-boundaries .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-boundaries .path{fill:none;stroke:#00875a;stroke-width:2}.eias-boundaries .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-boundaries .arrow{fill:#00875a}.eias-boundaries .arrow-g{fill:#6b778c}.eias-boundaries .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-boundaries .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-boundaries .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Country adapters answer different destination questions; route planning later binds the selected provider role and Sage adapter. Parsing and mapping occur only at system boundaries.</p>
  <svg viewBox="0 0 1100 650" role="img" aria-label="A recipient, country and document type enter a shared recipient resolver. France resolves through a SIREN directory to an approved platform, Spain resolves a tax ID to a private or public endpoint, and Germany uses customer configuration. The resolver returns recipient scheme, identifier, supported network or channel, capability or endpoint and evidence time without treating the network as Sage's provider. A separate route plan binds the provider and adapter. A shared format service parses inbound XML to the canonical invoice and maps outbound canonical invoices to UBL, CII, Factur-X, XRechnung or Facturae.">
    <text x="34" y="30" class="label">RECIPIENT RESOLUTION</text>
    <rect x="34" y="66" width="190" height="88" rx="9" class="main"/><text x="54" y="94" class="title">resolve(recipient, country, documentType)</text><text x="54" y="116" class="copy">Tax/legal ID • address scheme</text><text x="54" y="134" class="copy">direction • policy/effective context</text><path d="M224 110 H286" class="path"/><polygon points="286,110 276,104 276,116" class="arrow"/>
    <rect x="288" y="66" width="200" height="88" rx="9" class="main"/><text x="308" y="94" class="title">RecipientResolutionService</text><text x="308" y="116" class="copy">Select country resolver</text><text x="308" y="134" class="copy">preserve source and evidence time</text>
    <path d="M488 110 H540 V62 H594" class="path"/><polygon points="594,62 584,56 584,68" class="arrow"/><path d="M488 110 H594" class="path"/><polygon points="594,110 584,104 584,116" class="arrow"/><path d="M488 110 H540 V158 H594" class="path-opt"/><polygon points="594,158 584,152 584,164" class="arrow-g"/>
    <rect x="596" y="36" width="208" height="52" rx="8" class="main"/><text x="616" y="59" class="title">FranceResolver</text><text x="616" y="75" class="copy">SIREN → directory → approved platform</text>
    <rect x="596" y="84" width="208" height="52" rx="8" class="main"/><text x="616" y="107" class="title">SpainResolver</text><text x="616" y="123" class="copy">Tax ID → private or public endpoint</text>
    <rect x="596" y="132" width="208" height="52" rx="8" class="optional"/><text x="616" y="155" class="title">GermanyResolver</text><text x="616" y="171" class="copy">Counterparty/customer configuration</text>
    <path d="M804 62 H842 V112 H870" class="path"/><path d="M804 110 H870" class="path"/><path d="M804 158 H842 V112 H870" class="path-opt"/><polygon points="870,112 860,106 860,118" class="arrow"/>
    <rect x="872" y="48" width="194" height="128" rx="9" class="finish"/><text x="892" y="76" class="title">RecipientDestination</text><text x="892" y="98" class="copy">scheme • participant identifier</text><text x="892" y="117" class="copy">network/channel • capability</text><text x="892" y="136" class="copy">endpoint/discovery evidence</text><text x="892" y="155" class="copy">source • observed/effective time</text>
    <line x1="34" y1="222" x2="1066" y2="222" stroke="#dfe1e6"/>
    <text x="34" y="252" class="label">FORMAT SERVICE — INBOUND AND OUTBOUND</text>
    <rect x="34" y="286" width="150" height="62" rx="8" class="optional"/><text x="70" y="313" class="title">Inbound XML</text><text x="54" y="331" class="copy">UBL • CII • country syntax</text><path d="M184 317 H236" class="path"/><polygon points="236,317 226,311 226,323" class="arrow"/>
    <rect x="238" y="286" width="150" height="62" rx="8" class="main"/><text x="275" y="313" class="title">Syntax parser</text><text x="259" y="331" class="copy">parse • validate • preserve original</text><path d="M388 317 H440" class="path"/><polygon points="440,317 430,311 430,323" class="arrow"/>
    <rect x="442" y="278" width="216" height="78" rx="9" class="finish"/><text x="488" y="309" class="title">CanonicalInvoice</text><text x="474" y="331" class="copy">shared internal semantic boundary</text>
    <path d="M550 356 V414" class="path"/><polygon points="550,414 544,404 556,404" class="arrow"/><rect x="442" y="416" width="216" height="70" rx="9" class="main"/><text x="492" y="445" class="title">Semantic mapper</text><text x="468" y="465" class="copy">target profile + no-loss validation</text>
    <path d="M442 451 H374 V532 H306" class="path"/><polygon points="306,532 316,526 316,538" class="arrow"/><path d="M472 486 V566 H420" class="path"/><polygon points="420,566 430,560 430,572" class="arrow"/><path d="M550 486 V566" class="path"/><polygon points="550,566 544,556 556,556" class="arrow"/><path d="M628 486 V566 H680" class="path"/><polygon points="680,566 670,560 670,572" class="arrow"/><path d="M658 451 H726 V532 H794" class="path-opt"/><polygon points="794,532 784,526 784,538" class="arrow-g"/>
    <rect x="186" y="506" width="120" height="52" rx="8" class="main"/><text x="234" y="538" class="title">UBL</text><rect x="300" y="540" width="120" height="52" rx="8" class="main"/><text x="349" y="572" class="title">CII</text><rect x="490" y="540" width="120" height="52" rx="8" class="main"/><text x="516" y="572" class="title">Factur-X</text><rect x="680" y="540" width="120" height="52" rx="8" class="main"/><text x="704" y="572" class="title">XRechnung</text><rect x="794" y="506" width="120" height="52" rx="8" class="optional"/><text x="826" y="538" class="title">Facturae</text>
    <rect x="238" y="610" width="624" height="28" rx="14" class="finish"/><text x="377" y="629" class="title">Formats exist at boundaries; shared orchestration uses canonical semantics</text>
  </svg>
  <div class="notes"><div class="note"><strong>Resolver is an interface</strong>Country evidence decides directory, endpoint or configuration authority.</div><div class="note"><strong>Provider is bound separately</strong>The execution route combines the destination with provider role, adapter/configuration and credential reference.</div><div class="note"><strong>Representations preserve evidence</strong>Inbound original and mapping provenance remain durable.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Build capabilities once; plug in country policy and edges

<!-- confluence-html-macro:start -->
<div class="eias-packs" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-packs *{box-sizing:border-box}.eias-packs h2{margin:0;color:#172b4d;font-size:18px}.eias-packs .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-packs svg{display:block;width:1100px;height:650px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-packs .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-packs .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-packs .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-packs .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-packs .copy{fill:#42526e;font-size:8.5px}.eias-packs .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-packs .path{fill:none;stroke:#00875a;stroke-width:2}.eias-packs .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-packs .arrow{fill:#00875a}.eias-packs .arrow-g{fill:#6b778c}.eias-packs .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-packs .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-packs .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Reuse is measured by proven capability fitness—not by a promised percentage of existing France code.</p>
  <svg viewBox="0 0 1100 650" role="img" aria-label="The shared e-invoicing core contains invoice API, canonical semantics, validation, transformation, routing, workflow, reporting, identity, resilience, errors, audit, storage, observability and security. Country packs provide scope and effective dates, required data and validation, syntax profiles, topology and recipient discovery, trust, authority reporting, lifecycle mappings, retention and exceptions. France, Spain, Germany, Ireland and UK packs connect through one governed pack contract. Most reusable capability belongs in the core while deltas remain in packs.">
    <text x="34" y="30" class="label">SHARED PLATFORM CAPABILITY</text><text x="758" y="30" class="label">COUNTRY DELTA</text>
    <rect x="34" y="56" width="650" height="526" rx="12" class="main"/><text x="58" y="84" class="title">E-INVOICING CORE</text>
    <rect x="58" y="106" width="180" height="58" rx="8" class="finish"/><text x="78" y="131" class="title">Contract + semantics</text><text x="78" y="149" class="copy">Invoice API • canonical model • identity</text>
    <rect x="260" y="106" width="180" height="58" rx="8" class="finish"/><text x="280" y="131" class="title">Compliance frameworks</text><text x="280" y="149" class="copy">scope • validation • rules • effective date</text>
    <rect x="462" y="106" width="180" height="58" rx="8" class="finish"/><text x="482" y="131" class="title">Boundary frameworks</text><text x="482" y="149" class="copy">transform • resolve • route • report</text>
    <rect x="58" y="188" width="180" height="58" rx="8" class="finish"/><text x="78" y="213" class="title">Lifecycle + events</text><text x="78" y="231" class="copy">workflow • statuses • callbacks/webhooks</text>
    <rect x="260" y="188" width="180" height="58" rx="8" class="finish"/><text x="280" y="213" class="title">Resilience</text><text x="280" y="231" class="copy">idempotency • retry • reconcile • errors</text>
    <rect x="462" y="188" width="180" height="58" rx="8" class="finish"/><text x="482" y="213" class="title">Evidence + operations</text><text x="482" y="231" class="copy">audit • storage • observability • support</text>
    <rect x="58" y="270" width="584" height="58" rx="8" class="finish"/><text x="78" y="295" class="title">Security and platform governance</text><text x="78" y="313" class="copy">authentication • authorisation • tenant/environment isolation • policy release • compatibility</text>
    <rect x="58" y="360" width="584" height="174" rx="10" class="optional"/><text x="78" y="386" class="title">Country-pack contract</text>
    <text x="78" y="414" class="copy">Who/what/when is in scope • exemptions • VAT/business rules • identifiers • mandatory fields</text><text x="78" y="438" class="copy">Allowed formats/CIUS • topology • recipient discovery • authentication/signature • authority reporting</text><text x="78" y="462" class="copy">Status mappings • deadlines • retention • exceptions • rollout dates • evidence owner/version</text><text x="78" y="500" class="copy">Every capability state: confirmed • proposed • unsupported • not applicable • unknown</text>
    <path d="M684 319 H736" class="path"/><polygon points="736,319 726,313 726,325" class="arrow"/>
    <rect x="738" y="56" width="328" height="526" rx="12" class="optional"/><text x="760" y="84" class="title">COUNTRY PACKS</text>
    <rect x="762" y="108" width="280" height="70" rx="9" class="main"/><text x="782" y="134" class="title">France</text><text x="782" y="153" class="copy">approved platforms • directory • DGFiP • statuses</text>
    <rect x="762" y="194" width="280" height="70" rx="9" class="main"/><text x="782" y="220" class="title">Spain</text><text x="782" y="239" class="copy">public/private • faithful copy • formats • events</text>
    <rect x="762" y="280" width="280" height="70" rx="9" class="main"/><text x="782" y="306" class="title">Germany</text><text x="782" y="325" class="copy">scope • XRechnung/ZUGFeRD • agreed transport</text>
    <rect x="762" y="366" width="280" height="70" rx="9" class="main"/><text x="782" y="392" class="title">Ireland</text><text x="782" y="411" class="copy">phases • EN 16931 • Revenue reporting</text>
    <rect x="762" y="452" width="280" height="70" rx="9" class="optional"/><text x="782" y="478" class="title">UK</text><text x="782" y="497" class="copy">2029 • Peppol • profile/reporting gates</text>
    <path d="M738 143 H704 V462 H642" class="path-opt"/><path d="M738 229 H704" class="path-opt"/><path d="M738 315 H704" class="path-opt"/><path d="M738 401 H704" class="path-opt"/><path d="M738 487 H704" class="path-opt"/><polygon points="642,462 652,456 652,468" class="arrow-g"/>
    <rect x="214" y="604" width="672" height="30" rx="15" class="finish"/><text x="349" y="624" class="title">Product target: shared capabilities dominate; country work concentrates in governed deltas</text>
  </svg>
  <div class="notes"><div class="note"><strong>Policy, not forks</strong>Country change is configuration plus adapters under one contract.</div><div class="note"><strong>Unsupported stays visible</strong>Unknown and not-applicable are valid research outcomes.</div><div class="note"><strong>Reuse requires evidence</strong>Existing France/Spain assets are assessed, not presumed reusable.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Applicability is a reusable, explainable decision

<!-- confluence-html-macro:start -->
<div class="eias-scope" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-scope *{box-sizing:border-box}.eias-scope h2{margin:0;color:#172b4d;font-size:18px}.eias-scope .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-scope svg{display:block;width:1100px;height:630px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-scope .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-scope .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-scope .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-scope .bad{fill:#ffebe6;stroke:#de350b;stroke-width:1.6}.eias-scope .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-scope .copy{fill:#42526e;font-size:8.5px}.eias-scope .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-scope .path{fill:none;stroke:#00875a;stroke-width:2}.eias-scope .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-scope .path-alert{fill:none;stroke:#de350b;stroke-width:1.8;stroke-dasharray:6 4}.eias-scope .arrow{fill:#00875a}.eias-scope .arrow-g{fill:#6b778c}.eias-scope .arrow-r{fill:#de350b}.eias-scope .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-scope .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-scope .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Effective-dated policy replaces scattered country and company-size conditionals.</p>
  <svg viewBox="0 0 1100 630" role="img" aria-label="A transaction enters a scope decision engine with seller, buyer and transaction attributes. Seller and buyer inputs include country, VAT status and establishment; transaction inputs include B2B, B2C or B2G, domestic or cross-border, document type and date. The engine selects an effective-dated country policy version and returns whether e-invoicing and reporting are required, the format profile, route, effective date and exemptions. A red hard-coded country conditional is rejected in favour of versioned CountryPolicy rules. Example routes include French domestic, French to German, Spanish B2C and B2B, Irish to French, B2G, credit note, self-billing and reverse charge.">
    <text x="34" y="30" class="label">DECISION INPUTS</text><text x="440" y="30" class="label">POLICY EVALUATION</text><text x="806" y="30" class="label">EXPLAINABLE RESULT</text>
    <rect x="34" y="60" width="220" height="120" rx="9" class="main"/><text x="54" y="88" class="title">Seller</text><text x="54" y="112" class="copy">country • VAT status • establishment</text><text x="54" y="132" class="copy">legal entity • size/cohort • identifiers</text><text x="54" y="152" class="copy">issue date and product context</text>
    <rect x="34" y="204" width="220" height="120" rx="9" class="main"/><text x="54" y="232" class="title">Buyer</text><text x="54" y="256" class="copy">country • VAT status • establishment</text><text x="54" y="276" class="copy">legal/public/consumer classification</text><text x="54" y="296" class="copy">recipient identifiers and route evidence</text>
    <rect x="34" y="348" width="220" height="140" rx="9" class="main"/><text x="54" y="376" class="title">Transaction</text><text x="54" y="400" class="copy">B2B • B2C • B2G</text><text x="54" y="420" class="copy">domestic • cross-border • intra-EU</text><text x="54" y="440" class="copy">invoice • credit note • self-billing</text><text x="54" y="460" class="copy">reverse charge • tax treatment • amount</text>
    <path d="M254 120 H404 V226 H442" class="path"/><path d="M254 264 H442" class="path"/><path d="M254 418 H404 V302 H442" class="path"/><polygon points="442,226 432,220 432,232" class="arrow"/><polygon points="442,264 432,258 432,270" class="arrow"/><polygon points="442,302 432,296 432,308" class="arrow"/>
    <rect x="444" y="166" width="280" height="200" rx="12" class="main"/><text x="464" y="196" class="title">Scope Decision Engine</text><text x="464" y="222" class="copy">Select country + policy version</text><text x="464" y="244" class="copy">Evaluate effective interval and evidence</text><text x="464" y="266" class="copy">Apply scope, exemption and obligation rules</text><text x="464" y="288" class="copy">Return reasons and missing evidence</text><rect x="470" y="312" width="228" height="34" rx="8" class="finish"/><text x="487" y="334" class="title">CountryPolicy FR-2026.09</text>
    <path d="M724 266 H798" class="path"/><polygon points="798,266 788,260 788,272" class="arrow"/>
    <rect x="800" y="144" width="266" height="244" rx="12" class="finish"/><text x="822" y="174" class="title">ComplianceResult</text><text x="822" y="204" class="copy">eInvoiceRequired</text><text x="822" y="226" class="copy">reportingRequired</text><text x="822" y="248" class="copy">formatProfile</text><text x="822" y="270" class="copy">route / recipient-resolution method</text><text x="822" y="292" class="copy">effectiveDate + policyVersion</text><text x="822" y="314" class="copy">exemptions[] + reasons[]</text><text x="822" y="336" class="copy">missingEvidence[]</text><text x="822" y="358" class="copy">confidence / owner / decision gate</text>
    <polygon points="374,402 426,454 374,506 322,454" class="bad"/><text x="342" y="438" class="title">Avoid</text><text x="336" y="456" class="copy">if country == FR</text><text x="333" y="474" class="copy">if companySize...</text>
    <path d="M426 454 H584 V366" class="path-alert"/><polygon points="584,366 578,376 590,376" class="arrow-r"/>
    <rect x="444" y="424" width="280" height="120" rx="9" class="optional"/><text x="464" y="452" class="title">Versioned CountryPolicy</text><text x="464" y="476" class="copy">version • effectiveFrom • effectiveTo</text><text x="464" y="498" class="copy">Rules[] • evidence source • owner</text><text x="464" y="520" class="copy">test pack • approval • rollback metadata</text>
    <rect x="800" y="430" width="266" height="142" rx="9" class="optional"/><text x="822" y="456" class="title">Representative discovery cases</text><text x="822" y="480" class="copy">FR→FR • FR→DE • ES→consumer • ES→business</text><text x="822" y="502" class="copy">IE→FR • B2G • credit note • self-billing</text><text x="822" y="524" class="copy">reverse charge • domestic/cross-border</text><text x="822" y="546" class="copy">Each becomes an explicit scenario/test, not code sprawl</text>
    <rect x="204" y="590" width="692" height="28" rx="14" class="finish"/><text x="365" y="609" class="title">Historical invoices retain the policy and result that governed their original exchange</text>
  </svg>
  <div class="notes"><div class="note"><strong>Explain before mutating</strong>Out-of-scope and missing-evidence results are first-class outcomes.</div><div class="note"><strong>Dates are policy data</strong>Mandate changes do not require scattered application conditionals.</div><div class="note"><strong>History is immutable</strong>New policy versions govern new eligible work only.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Spain: share invoice data, keep regulatory domains separate

<!-- confluence-html-macro:start -->
<div class="eias-spain-boundary" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1100px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-spain-boundary *{box-sizing:border-box}.eias-spain-boundary h2{margin:0;color:#172b4d;font-size:18px}.eias-spain-boundary .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-spain-boundary svg{display:block;width:1020px;height:370px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-spain-boundary .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-spain-boundary .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-spain-boundary .title{fill:#172b4d;font-size:11px;font-weight:700}.eias-spain-boundary .copy{fill:#42526e;font-size:9px}.eias-spain-boundary .path{fill:none;stroke:#00875a;stroke-width:2}.eias-spain-boundary .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-spain-boundary .arrow{fill:#00875a}.eias-spain-boundary .arrow-g{fill:#6b778c}.eias-spain-boundary .notes{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;min-width:1020px;margin-top:10px}.eias-spain-boundary .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-spain-boundary .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">B2B exchange and fiscal-record/VERI*FACTU obligations interact but do not become one Spanish service.</p>
  <svg viewBox="0 0 1020 370" role="img" aria-label="The shared invoice domain branches into an e-invoice compliance service and a fiscal-record compliance service. The Spain B2B pack uses the e-invoice service for structured document, validation, routing, intermediary, transformation, status events and government copy or reporting. A separate Spain VeriFactu pack uses the fiscal-record service for billing-system and anti-fraud traceability obligations. Both can reuse source invoice facts without merging responsibility.">
    <rect x="365" y="34" width="290" height="70" rx="10" class="main"/><text x="427" y="63" class="title">Shared invoice facts</text><text x="398" y="84" class="copy">identity • parties • lines • tax • totals • provenance</text>
    <path d="M510 104 V140 H270 V174" class="path"/><polygon points="270,174 264,164 276,164" class="arrow"/><path d="M510 140 H750 V174" class="path-opt"/><polygon points="750,174 744,164 756,164" class="arrow-g"/>
    <rect x="70" y="176" width="400" height="150" rx="12" class="main"/><text x="92" y="206" class="title">E-Invoice Compliance Service</text><text x="92" y="230" class="copy">Spain B2B pack</text><text x="92" y="254" class="copy">structured document • validation • routing • intermediary</text><text x="92" y="276" class="copy">transformation • status events • public copy/reporting</text><text x="92" y="300" class="copy">Outcome: compliant business invoice exchange</text>
    <rect x="550" y="176" width="400" height="150" rx="12" class="optional"/><text x="572" y="206" class="title">Fiscal Record Compliance Service</text><text x="572" y="230" class="copy">Spain VERI*FACTU / SIF pack</text><text x="572" y="254" class="copy">billing-system controls • record integrity • anti-fraud traceability</text><text x="572" y="276" class="copy">separate evidence, lifecycle and authority behaviour</text><text x="572" y="300" class="copy">Outcome: compliant fiscal-record production</text>
  </svg>
  <div class="notes"><div class="note"><strong>Reuse underneath</strong>Shared invoice facts avoid duplicate capture and contradictory totals.</div><div class="note"><strong>Do not merge policy</strong>Separate owners, requirements, tests and evidence prevent a giant country-specific service.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Products express intent; the service owns jurisdiction complexity

<!-- confluence-html-macro:start -->
<div class="eias-contract" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1100px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-contract *{box-sizing:border-box}.eias-contract h2{margin:0;color:#172b4d;font-size:18px}.eias-contract .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-contract svg{display:block;width:1020px;height:400px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-contract .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-contract .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-contract .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-contract .title{fill:#172b4d;font-size:11px;font-weight:700}.eias-contract .copy{fill:#42526e;font-size:9px}.eias-contract .path{fill:none;stroke:#00875a;stroke-width:2}.eias-contract .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-contract .arrow{fill:#00875a}.eias-contract .arrow-g{fill:#6b778c}.eias-contract .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1020px;margin-top:10px}.eias-contract .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-contract .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The endpoint shape is illustrative, not an approved API contract.</p>
  <svg viewBox="0 0 1020 400" role="img" aria-label="Sage Accounting, ERP and Cloud products submit a simple common invoice request such as POST invoices. The E-Invoicing as a Service boundary determines jurisdiction, policy, format, route, reporting and lifecycle. It returns invoice ID plus separate compliance, delivery, reporting and business status. France approved platforms, Spain public and private platforms, Germany agreed transports, Ireland Revenue and UK Peppol remain hidden behind the country-pack boundary.">
    <rect x="34" y="70" width="210" height="124" rx="10" class="main"/><text x="54" y="100" class="title">Sage products</text><text x="54" y="124" class="copy">Accounting • ERP • Cloud</text><text x="54" y="146" class="copy">Provide business invoice intent</text><rect x="58" y="162" width="162" height="24" rx="6" class="finish"/><text x="92" y="179" class="title">POST /invoices</text>
    <path d="M244 132 H330" class="path"/><polygon points="330,132 320,126 320,138" class="arrow"/>
    <rect x="332" y="42" width="356" height="260" rx="14" class="main"/><text x="390" y="76" class="title">E-INVOICING AS A SERVICE</text><text x="360" y="110" class="copy">Determine jurisdiction and applicable policy</text><text x="360" y="138" class="copy">Validate and produce required representation</text><text x="360" y="166" class="copy">Resolve recipient and select approved route</text><text x="360" y="194" class="copy">Report required data to authority</text><text x="360" y="222" class="copy">Normalise lifecycle events and preserve evidence</text><text x="360" y="250" class="copy">Correct • retry safely • reconcile unknown outcomes</text><rect x="360" y="266" width="300" height="24" rx="6" class="finish"/><text x="390" y="283" class="title">Country policy + adapters hidden from product</text>
    <path d="M688 132 H774" class="path"/><polygon points="774,132 764,126 764,138" class="arrow"/>
    <rect x="776" y="70" width="210" height="200" rx="10" class="finish"/><text x="798" y="100" class="title">Explainable result</text><text x="798" y="130" class="copy">invoiceId</text><text x="798" y="154" class="copy">complianceStatus</text><text x="798" y="178" class="copy">deliveryStatus</text><text x="798" y="202" class="copy">reportingStatus</text><text x="798" y="226" class="copy">businessStatus</text><text x="798" y="250" class="copy">reasons + safe next actions</text>
    <rect x="100" y="330" width="820" height="40" rx="20" class="optional"/><text x="185" y="355" class="title">Product does not encode French platforms, Spanish repositories, German channels, Irish reporting or UK Peppol rules</text><path d="M510 302 V330" class="path-opt"/><polygon points="510,330 504,320 516,320" class="arrow-g"/>
  </svg>
  <div class="notes"><div class="note"><strong>Stable intent contract</strong>Country change should not require every product to change.</div><div class="note"><strong>Statuses stay separate</strong>Compliance, delivery, reporting and business outcomes do not collapse.</div><div class="note"><strong>API remains proposed</strong>Architecture must approve endpoint and event shapes.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Different national paths, increasing EU semantic convergence

<!-- confluence-html-macro:start -->
<div class="eias-convergence" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1100px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-convergence *{box-sizing:border-box}.eias-convergence h2{margin:0;color:#172b4d;font-size:18px}.eias-convergence .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-convergence svg{display:block;width:1020px;height:430px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-convergence .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.eias-convergence .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.7}.eias-convergence .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eias-convergence .title{fill:#172b4d;font-size:11px;font-weight:700}.eias-convergence .copy{fill:#42526e;font-size:9px}.eias-convergence .path{fill:none;stroke:#00875a;stroke-width:2}.eias-convergence .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eias-convergence .arrow{fill:#00875a}.eias-convergence .arrow-g{fill:#6b778c}.eias-convergence .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1020px;margin-top:10px}.eias-convergence .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-convergence .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">ViDA strengthens the case for shared semantics and reporting frameworks without erasing national implementation differences.</p>
  <svg viewBox="0 0 1020 430" role="img" aria-label="In 2025 and 2026 France, Spain, Germany, Ireland and other EU countries follow different national e-invoicing paths. These converge toward EN 16931 and ViDA digital reporting from 1 July 2030 for cross-border B2B transactions. By 1 January 2035 domestic real-time reporting systems must align with the EU framework, producing greater interoperability while country rules and routes remain distinct.">
    <text x="50" y="40" class="title">2025–2029 • national paths</text><text x="442" y="40" class="title">2030 • ViDA cross-border DRR</text><text x="805" y="40" class="title">2035 • aligned domestic systems</text>
    <rect x="50" y="72" width="190" height="52" rx="8" class="main"/><text x="72" y="103" class="title">France • platforms + reporting</text>
    <rect x="50" y="140" width="190" height="52" rx="8" class="main"/><text x="72" y="171" class="title">Spain • public/private</text>
    <rect x="50" y="208" width="190" height="52" rx="8" class="main"/><text x="72" y="239" class="title">Germany • flexible transport</text>
    <rect x="50" y="276" width="190" height="52" rx="8" class="main"/><text x="72" y="307" class="title">Ireland • phased rollout</text>
    <rect x="50" y="344" width="190" height="52" rx="8" class="optional"/><text x="72" y="375" class="title">Other EU country paths</text>
    <path d="M240 98 H350 V218 H414" class="path"/><path d="M240 166 H350" class="path"/><path d="M240 234 H414" class="path"/><path d="M240 302 H350 V250 H414" class="path"/><path d="M240 370 H350 V282 H414" class="path-opt"/><polygon points="414,218 404,212 404,224" class="arrow"/><polygon points="414,234 404,228 404,240" class="arrow"/><polygon points="414,250 404,244 404,256" class="arrow"/><polygon points="414,282 404,276 404,288" class="arrow-g"/>
    <rect x="416" y="144" width="250" height="184" rx="12" class="main"/><text x="444" y="177" class="title">EN 16931 + ViDA model</text><text x="444" y="207" class="copy">1 July 2030</text><text x="444" y="229" class="copy">cross-border B2B mandatory e-invoicing</text><text x="444" y="251" class="copy">digital reporting requirements</text><text x="444" y="273" class="copy">common semantic/reporting direction</text><text x="444" y="295" class="copy">national implementation still applies</text>
    <path d="M666 236 H760" class="path"/><polygon points="760,236 750,230 750,242" class="arrow"/>
    <rect x="762" y="166" width="208" height="140" rx="70" class="finish"/><text x="803" y="210" class="title">Greater interoperability</text><text x="796" y="236" class="copy">1 January 2035 alignment</text><text x="797" y="258" class="copy">shared semantics and reports</text><text x="807" y="280" class="copy">country deltas remain</text>
  </svg>
  <div class="notes"><div class="note"><strong>Convergence is directional</strong>It does not justify one hard-coded EU workflow today.</div><div class="note"><strong>Semantic investment compounds</strong>Common invoice meaning and report orchestration serve later phases.</div><div class="note"><strong>Dates are sourced</strong>Country and EU policy versions remain independently effective-dated.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Ask the same ten questions for every country

<!-- confluence-html-macro:start -->
<div class="eias-capabilities" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eias-capabilities *{box-sizing:border-box}.eias-capabilities h2{margin:0;color:#172b4d;font-size:18px}.eias-capabilities .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.eias-capabilities svg{display:block;width:1100px;height:710px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eias-capabilities .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.4}.eias-capabilities .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.6}.eias-capabilities .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.4;stroke-dasharray:7 5}.eias-capabilities .title{fill:#172b4d;font-size:10px;font-weight:700}.eias-capabilities .copy{fill:#42526e;font-size:8.5px}.eias-capabilities .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eias-capabilities .path{fill:none;stroke:#00875a;stroke-width:1.8}.eias-capabilities .arrow{fill:#00875a}.eias-capabilities .grid{stroke:#dfe1e6;stroke-width:1}.eias-capabilities .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eias-capabilities .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px}.eias-capabilities .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">✓ means shared framework; Δ means country policy/adapter; ? means regulation or design remains open.</p>
  <svg viewBox="0 0 1100 710" role="img" aria-label="A ten-capability research map covers determine applicability, enrich, validate, transform, resolve recipient, authenticate or sign, transmit, report, track lifecycle and provide evidence. A country matrix then compares France, Spain, Germany, Ireland and UK, showing common shared frameworks for the canonical model, transformation, transport, status, reporting, audit and resilience, country deltas for policy, formats, routing, statuses and reporting rules, and unknowns for still-developing Ireland and UK details.">
    <text x="34" y="30" class="label">TEN-CAPABILITY WORKSHOP MAP</text>
    <rect x="34" y="56" width="190" height="64" rx="8" class="main"/><text x="54" y="82" class="title">1 • Determine applicability</text><text x="54" y="101" class="copy">Does this transaction require invoice/reporting?</text>
    <rect x="246" y="56" width="190" height="64" rx="8" class="main"/><text x="266" y="82" class="title">2 • Enrich invoice</text><text x="266" y="101" class="copy">Which jurisdiction data is missing?</text>
    <rect x="458" y="56" width="190" height="64" rx="8" class="main"/><text x="478" y="82" class="title">3 • Validate</text><text x="478" y="101" class="copy">Is the representation compliant?</text>
    <rect x="670" y="56" width="190" height="64" rx="8" class="main"/><text x="690" y="82" class="title">4 • Transform</text><text x="690" y="101" class="copy">Which syntax/profile is required?</text>
    <rect x="882" y="56" width="184" height="64" rx="8" class="main"/><text x="902" y="82" class="title">5 • Resolve recipient</text><text x="902" y="101" class="copy">Where does it go?</text>
    <rect x="34" y="142" width="190" height="64" rx="8" class="main"/><text x="54" y="168" class="title">6 • Authenticate/sign</text><text x="54" y="187" class="copy">How are identity and integrity proved?</text>
    <rect x="246" y="142" width="190" height="64" rx="8" class="main"/><text x="266" y="168" class="title">7 • Transmit</text><text x="266" y="187" class="copy">Which network, platform or API?</text>
    <rect x="458" y="142" width="190" height="64" rx="8" class="main"/><text x="478" y="168" class="title">8 • Report</text><text x="478" y="187" class="copy">What must reach government?</text>
    <rect x="670" y="142" width="190" height="64" rx="8" class="main"/><text x="690" y="168" class="title">9 • Track lifecycle</text><text x="690" y="187" class="copy">What events/statuses matter?</text>
    <rect x="882" y="142" width="184" height="64" rx="8" class="finish"/><text x="902" y="168" class="title">10 • Evidence</text><text x="902" y="187" class="copy">Can we prove what happened?</text>
    <text x="34" y="252" class="label">COUNTRY × CAPABILITY MATRIX</text>
    <rect x="34" y="274" width="1032" height="398" rx="8" fill="#fff" stroke="#dfe1e6"/>
    <line x1="334" y1="274" x2="334" y2="672" class="grid"/><line x1="480" y1="274" x2="480" y2="672" class="grid"/><line x1="626" y1="274" x2="626" y2="672" class="grid"/><line x1="772" y1="274" x2="772" y2="672" class="grid"/><line x1="918" y1="274" x2="918" y2="672" class="grid"/>
    <text x="54" y="300" class="title">Capability</text><text x="385" y="300" class="title">FR</text><text x="531" y="300" class="title">ES</text><text x="677" y="300" class="title">DE</text><text x="823" y="300" class="title">IE</text><text x="969" y="300" class="title">UK</text>
    <line x1="34" y1="316" x2="1066" y2="316" class="grid"/><line x1="34" y1="350" x2="1066" y2="350" class="grid"/><line x1="34" y1="384" x2="1066" y2="384" class="grid"/><line x1="34" y1="418" x2="1066" y2="418" class="grid"/><line x1="34" y1="452" x2="1066" y2="452" class="grid"/><line x1="34" y1="486" x2="1066" y2="486" class="grid"/><line x1="34" y1="520" x2="1066" y2="520" class="grid"/><line x1="34" y1="554" x2="1066" y2="554" class="grid"/><line x1="34" y1="588" x2="1066" y2="588" class="grid"/><line x1="34" y1="622" x2="1066" y2="622" class="grid"/>
    <text x="54" y="338" class="copy">Scope engine / country policy</text><text x="400" y="338" class="title">Δ</text><text x="546" y="338" class="title">Δ</text><text x="692" y="338" class="title">Δ</text><text x="838" y="338" class="title">Δ</text><text x="984" y="338" class="title">?</text>
    <text x="54" y="372" class="copy">Canonical model + validation framework</text><text x="400" y="372" class="title">✓/Δ</text><text x="546" y="372" class="title">✓/Δ</text><text x="692" y="372" class="title">✓/Δ</text><text x="838" y="372" class="title">✓/Δ</text><text x="984" y="372" class="title">✓/?</text>
    <text x="54" y="406" class="copy">Transformation framework / syntax profile</text><text x="400" y="406" class="title">✓/Δ</text><text x="546" y="406" class="title">✓/Δ</text><text x="692" y="406" class="title">✓/Δ</text><text x="838" y="406" class="title">✓/?</text><text x="984" y="406" class="title">✓/?</text>
    <text x="54" y="440" class="copy">Recipient resolver</text><text x="400" y="440" class="title">Δ</text><text x="546" y="440" class="title">Δ</text><text x="692" y="440" class="title">Δ</text><text x="838" y="440" class="title">?</text><text x="984" y="440" class="title">Δ/?</text>
    <text x="54" y="474" class="copy">Transport framework / adapter</text><text x="400" y="474" class="title">✓/Δ</text><text x="546" y="474" class="title">✓/Δ</text><text x="692" y="474" class="title">✓/Δ</text><text x="838" y="474" class="title">✓/?</text><text x="984" y="474" class="title">✓/Δ</text>
    <text x="54" y="508" class="copy">Status engine / country mapping</text><text x="400" y="508" class="title">✓/Δ</text><text x="546" y="508" class="title">✓/Δ</text><text x="692" y="508" class="title">✓/Δ</text><text x="838" y="508" class="title">✓/?</text><text x="984" y="508" class="title">✓/?</text>
    <text x="54" y="542" class="copy">Reporting framework / rules</text><text x="400" y="542" class="title">✓/Δ</text><text x="546" y="542" class="title">✓/Δ</text><text x="692" y="542" class="title">✓/?</text><text x="838" y="542" class="title">✓/Δ</text><text x="984" y="542" class="title">✓/?</text>
    <text x="54" y="576" class="copy">Audit, resilience and security</text><text x="400" y="576" class="title">✓</text><text x="546" y="576" class="title">✓</text><text x="692" y="576" class="title">✓</text><text x="838" y="576" class="title">✓</text><text x="984" y="576" class="title">✓</text>
    <text x="54" y="610" class="copy">Authority/participant identity and trust</text><text x="400" y="610" class="title">Δ</text><text x="546" y="610" class="title">Δ</text><text x="692" y="610" class="title">Δ</text><text x="838" y="610" class="title">?</text><text x="984" y="610" class="title">Δ/?</text>
    <text x="54" y="652" class="copy">Research meaning</text><text x="382" y="652" class="copy">✓ shared</text><text x="520" y="652" class="copy">Δ country delta</text><text x="670" y="652" class="copy">? open</text><text x="816" y="652" class="copy">combined cells show framework/delta</text>
  </svg>
  <div class="notes"><div class="note"><strong>One workshop pattern</strong>Country discovery asks the same ten questions instead of starting from a blank page.</div><div class="note"><strong>Matrix is research, not commitment</strong>Every symbol still needs evidence and an owner.</div><div class="note"><strong>Open is visible</strong>Ireland/UK uncertainty becomes a gate rather than invented behaviour.</div></div>
</div>
<!-- confluence-html-macro:end -->

### Source-diagram coverage

| Source blocks | Treatment in the PRDs |
|---|---|
| 1, 36 | Strategic service visual |
| 2–5 | Canonical invoice and country representations; short naming examples retained as text semantics |
| 6–13, 30–32 | Compliance-domain and country-topology visuals |
| 14–18 | Lifecycle and event-normalisation visual |
| 19–25 | Recipient-resolution and format-boundary visual; resolver signature retained as concise text |
| 26–27, 39 | Shared-core, country-pack and reuse-boundary visual |
| 28–29, 34–35 | Scope-decision and effective-policy visual; example cases included as visual notes |
| 33 | Spain domain-boundary visual |
| 37–38 | Simple product-contract visual; endpoint remains explicitly illustrative |
| 40 | Regulatory-convergence visual |
| 41–42 | Ten-capability map and country matrix visual |
| Additional Peppol/provider context | Route-model and four-corner visual; vendor names remain research examples rather than selections |

## Actors and business scenarios

| ID | Actor/context | Scenario | Expected outcome | Continuity/exception |
|---|---|---|---|---|
| S1 | Customer/accountant | Creates an invoice for a supported legal entity | Applicability and required data are explained before external mutation | Out-of-scope invoices return a reason, not a false compliance success |
| S2 | Sage product/API consumer | Submits the same intent twice | One logical invoice/operation is produced | Duplicate response is stable and auditable |
| S3 | Country compliance owner | Activates a future policy version | Only eligible transactions at/after the effective boundary use it | Historical invoices retain original version/context |
| S4 | Platform | Sends to recipient and separately reports to authority | Each leg has independent correlation, outcome and recovery | One successful leg does not imply another succeeded |
| S5 | Customer | Corrects a validation rejection | Corrected version is re-evaluated with traceable lineage | Rejected representation and reasons remain available |
| S6 | Platform/operations | Times out after an external mutation may have occurred | Outcome becomes unknown and is reconciled before resubmission | No blind duplicate invoice/report |
| S7 | Recipient/Sage product | Provides or receives lifecycle events | External vocabulary is preserved and mapped to explainable canonical events | Unknown/out-of-order events are retained for reconciliation |
| S8 | Support | Investigates an invoice after a route/policy change | Intended and observed state plus immutable origin context are visible | Current configuration never rewrites historical evidence |
| S9 | Security/compliance | Suspends a compromised adapter or credential | Affected scope stops safely with audit and recovery guidance | Unaffected country/routes remain isolated where safe |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | A country is supported | Support requires an accountable owner, evidence register, versioned policy and approved readiness gates | Proposed governance rule |
| BR2 | A transaction is evaluated | Applicability must use legal entity, parties, transaction, document type and effective time; absence of evidence cannot default to compliant | Proposed |
| BR3 | Multiple obligations apply | Document, delivery and reporting status remain independently observable | Confirmed product principle from research; approval required |
| BR4 | A representation crosses a boundary | Preserve source facts, mapping/profile version, validation result and representation hash/reference | Proposed |
| BR5 | Country policy changes | Apply changes prospectively by effective version unless an approved legal correction explicitly requires otherwise | Proposed |
| BR6 | External vocabulary differs | Preserve the raw status/reason and map it through a versioned country mapping | Proposed |
| BR7 | A mutation outcome is ambiguous | Reconcile external state before retry unless the operation is proven idempotent end-to-end | Existing resilience principle; related PRD-SEI-225 |
| BR8 | A route changes | New eligible work may use the new route; historical work retains invoice-origin context and supported follow-up access | Existing continuity principle; related PRD-SEI-223/224 |
| BR9 | Spain capability is considered | B2B e-invoice exchange and fiscal-record/VERI*FACTU compliance remain separate bounded contexts | Confirmed research distinction; country confirmation required |
| BR10 | Reuse is assessed | Measure capability fitness and avoided duplication; do not treat a percentage of France code as a product commitment | Confirmed product direction |
| BR11 | A delivery route is planned | Record regulation, network/channel, provider service role and Sage adapter as separate dimensions; never represent Peppol or another interoperability network as the provider | Confirmed Peppol distinction; proposed cross-network rule |

## Scope

### In scope for discovery

- shared business capability contract and country-pack contract;
- canonical semantic coverage and provenance requirements;
- applicability, validation, transformation, recipient resolution, delivery, reporting, lifecycle and evidence frameworks;
- inbound/outbound asymmetry, idempotency, reconciliation and historical continuity;
- country-policy lifecycle and governance;
- API/client, operations, security and audit expectations;
- Germany, Ireland and UK child discovery boundaries;
- identifier/tenancy/delegation, lifecycle mapping, Peppol multi-address routing and cross-border reuse child analyses;
- fit assessment against relevant existing France/Spain capabilities.

### Deferred until evidence/approval

- physical canonical schema and public API;
- network/channel and provider-role selection, contracts and endpoint mappings;
- performance, availability, capacity and retention targets;
- first production country/cohort;
- migration/cutover from existing implementations;
- commercial packaging and charge model.

## Research findings and evidence register

| Source | Finding | Confidence/limitation | Requirement impact |
|---|---|---|---|
| Supplied cross-country research, 2026-08-10 | Repeated capabilities support a core-plus-country-pack hypothesis; text diagrams and detailed analysis are product input | Secondary synthesis; source URLs were not supplied and solution claims are not approved | Informs capability map and consultation, not legal acceptance |
| [European Commission ViDA 2026 Work Programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en), 2026-05-22 | Cross-border B2B DRR based on mandatory e-invoicing starts 2030-07-01; domestic real-time systems align by 2035-01-01 | Official EU summary; implementation detail continues through work programme | Versioned EU policy, reporting framework and future compatibility |
| [German Federal Ministry of Finance FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html), updated 2026-03 | German B2B structured invoice requirements, transition, formats and flexible transmission | Official tax guidance; B2G and detailed technical implementation differ | Germany pack must not impose a universal network |
| [Irish Revenue Phase One](https://www.revenue.ie/en/vat/vida-vat-modernisation/large-corporates-vat-modernisation.aspx), accessed 2026-08-10 | 2028-11-01 large-corporate domestic B2B issuance/reporting; all businesses receive; EN 16931 | Official; later transport/reporting specifications remain open | Ireland pack gates and inbound/outbound asymmetry |
| [UK 2026 tax update](https://www.gov.uk/government/publications/summary-of-tax-update-2026-simplification-modernisation-and-fairness/tax-update-2026-simplification-modernisation-and-fairness-summary), 2026 | Peppol announced as core interoperability network | Official direction; detailed standards/legislation and legacy treatment remain in development | UK pack can prepare Peppol capability but must keep policy gates open |
| [OpenPeppol interoperability framework](https://peppol.org/learn-more/peppol-interoperability-framework/) and [certified-provider register](https://peppol.org/members/peppol-certified-service-providers/), accessed 2026-08-11 | Peppol uses interoperating Access Point providers plus participant capability lookup; sender and recipient can use different providers | Official network/governance evidence; provider register states legal residence rather than operating coverage and is not a Sage shortlist | Separate network, provider role, adapter and recipient destination; verify exact legal entity, authority, service role and coverage before selection |
| Existing PRD-SEI-223–226 | Spain routing, lifecycle, resilience, operations, security and audit requirements | Canonical internal product context; capability fitness not proven for multi-country use | Reuse assessment input; do not duplicate implementation assumptions |

## Proposed conceptual model

The atlas is a **proposed model**, not approved architecture. Its minimum durable distinctions are:

| Layer | Includes | Historical rule |
|---|---|---|
| Intent and semantics | Invoice intent, canonical meaning, extensions and source provenance | Corrections retain lineage; source evidence is not discarded |
| Policy and plan | Scope result, country-policy version, obligations and dependencies | Original inputs, reasons and effective policy remain immutable |
| Boundary execution | Representations plus independent recipient/authority exchange legs; each route binds network/channel, provider role, technical adapter and recipient destination separately | Each leg retains profile, provider/adapter versions, route, correlation and recovery evidence |
| Lifecycle and governance | Raw/canonical events, pack owner/version, approval and rollback | Events append; later policy/configuration does not rewrite history |

Every country-pack capability is explicitly `confirmed`, `proposed`, `unsupported`, `not applicable` or `unknown`; the capability-map visual is the discovery checklist.

## Lifecycle and recovery behaviour

Proposed canonical events describe business meaning, not a universal linear state machine. `CREATED`, `VALIDATION_PASSED`, `DISPATCHED`, `DELIVERED`, `REJECTED`, `ACCEPTED`, `PAID`, `CANCELLED`, `REPORT_ACCEPTED` and `REPORT_REJECTED` may apply by country and document. External values remain preserved.

| Failure | Required behaviour |
|---|---|
| Missing/invalid data | Reject before external mutation with field/rule/policy version and correction guidance |
| No applicable country policy | Return unsupported/decision-required; do not silently send a non-compliant representation |
| Transformation loss or invalid output | Stop the affected leg and retain mapping/validation evidence |
| No eligible recipient route | Hold before dispatch, explain missing resolution evidence and permit authorised correction |
| Authentication/consent/certificate failure | Stop affected leg; do not expose secret material; show owner/action |
| Provider/authority unavailable before send | Retry only within approved policy and idempotency boundary |
| Timeout after possible mutation | Mark outcome unknown and reconcile using external identity/correlation before retry |
| Duplicate/out-of-order event | Deduplicate by source identity; retain sequence evidence; recompute view without erasing history |
| External success then internal persistence failure | Recover from durable intent/correlation and reconcile; never create a second invoice blindly |
| Concurrent policy/route change | Use optimistic concurrency/effective boundary; one approved plan wins for new work |
| Current route removed with historical work | Block destructive removal or retain scoped historical capability until obligations close |

## Requirements

### Shared contract and policy

| ID | Requirement |
|---|---|
| FR1 | When a Sage product submits invoice intent, the service must bind tenant, legal entity, actor, source identity and idempotency identity before any external mutation. |
| FR2 | The service must return an explainable scope decision identifying applied country policy/version, applicable obligations, exemptions and missing evidence. |
| FR3 | Country policy must be effective-dated, owner-approved, immutable after activation, testable before activation and rollback-capable for new work without rewriting historical decisions. |
| FR4 | The product contract must distinguish unsupported country/capability, out-of-scope transaction, correctable invalid invoice, permanent external rejection, transient failure and outcome unknown. |

### Invoice semantics, validation and transformation

| ID | Requirement |
|---|---|
| FR5 | The shared semantic model must represent invoice identity/type/date/currency, supplier, buyer, lines, tax, totals, payment and references, while supporting governed country extensions and provenance. |
| FR6 | Validation must apply common semantic rules and the selected country/profile rules, returning stable rule IDs, affected fields, severity, policy version and customer-safe correction guidance. |
| FR7 | Every outbound/inbound transformation must record source/target syntax and profile, mapper version, validation result, integrity reference and any approved semantic exception. |
| FR8 | A transformed representation that loses mandatory meaning or fails the target profile must not be dispatched. |

### Routing, exchange and reporting

| ID | Requirement |
|---|---|
| FR9 | Recipient resolution must be pluggable by country and return the recipient scheme/identifier, supported network or channel, destination/capability, source/evidence time and confidence/authority without silently selecting Sage's provider connection. |
| FR10 | The service must create independent exchange legs for recipient delivery and each required authority report, with separate correlation, idempotency, status and recovery. |
| FR11 | A country pack must be able to select an approved network/channel without changing the product contract; before execution, the route plan must separately bind the provider legal entity and role, applicable certification/authority evidence, technical adapter/configuration, credential reference and recipient destination. Four-corner routes must allow sender and recipient providers to differ. |
| FR12 | Inbound invoice handling must verify tenant/recipient, deduplicate, preserve the original representation and provenance, map to canonical semantics and expose validation/trust failures without silently delivering unsafe content. |

### Lifecycle, continuity and operations

| ID | Requirement |
|---|---|
| FR13 | External events must retain raw value/reason/source and map through a versioned country mapping to canonical event meaning. |
| FR14 | The current invoice view must be derived from durable events and must not discard conflicting, duplicate, unknown or out-of-order evidence. |
| FR15 | A timeout after a mutation may have reached an external party must enter outcome-unknown and reconcile before resubmission unless end-to-end idempotency is proven. |
| FR16 | Operations must see intended plan, each observed external leg, evidence freshness, safe next actions and customer-safe status without direct database correction. |
| FR17 | Route, provider, credential or policy changes must apply only to eligible new work; historical invoices retain origin context and supported follow-up/retrieval paths. |
| FR18 | The platform must support scoped suspension/kill control by country, pack version, provider, credential, direction or environment with authorised audit and recovery. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Secrets/private keys must use approved custody, rotation and environment isolation and must never appear in invoice payloads, logs or audit events. |
| NFR2 | Tenant, legal entity, country and environment boundaries must be enforced for data, keys, routes, events, diagnostics and support actions. |
| NFR3 | Every compliance decision and external mutation must have immutable actor/source/time, policy, representation, route, correlation and result evidence. |
| NFR4 | Data must be minimised and classified; retention/deletion/legal-hold periods require country, legal, privacy and security approval rather than a universal invented period. |
| NFR5 | Availability, latency, throughput, payload and backlog targets must be baselined per product/country and approved before delivery commitment. |
| NFR6 | Observability must distinguish customer-data, Sage-policy/platform, country-pack, service-provider, network/channel and authority failures without exposing confidential invoice content. |
| NFR7 | APIs/events must have explicit versioning, compatibility and deprecation policy; country-pack change must not force unrelated product contract changes. |
| NFR8 | Customer-facing validation and recovery information must be accessible, localisable and safe to disclose. |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| AC1 | Given the same valid business invoice intent evaluated for two supported countries, when policy is applied, then the product contract remains stable while the service records distinct country policy, representations and routes. |
| AC2 | Given a transaction is outside a mandate, when scope is evaluated, then the result identifies the policy and reason and does not claim compliant external delivery. |
| AC3 | Given a correctable country validation failure, when the product receives the result, then it includes stable rule/field/version guidance and no external mutation occurred. |
| AC4 | Given recipient delivery succeeds but authority reporting fails, when status is requested, then delivery and reporting show independent outcomes and only the failed safe leg is recovered. |
| AC5 | Given a dispatch times out after bytes may have reached a network, when retry policy executes, then no second mutation occurs until reconciliation establishes safety. |
| AC6 | Given a policy or route changes after an invoice is sent, when the invoice is retrieved or updated, then its original policy, representation, route and external references remain unchanged. |
| AC7 | Given an inbound external event is duplicated or arrives out of order, when processed, then one durable source event identity is retained, history remains explainable and the current view is deterministic. |
| AC8 | Given an unapproved/expired country pack is selected, when an invoice is submitted, then the service blocks external mutation and identifies the owning decision gate. |
| AC9 | Given the Germany, Ireland and UK pack definitions, when reviewed against the pack contract, then every capability has an explicit evidence state rather than an implicit assumption. |
| AC10 | Given Sage uses one certified Access Point and a buyer uses another, when a Peppol route is planned, then both provider roles and the shared network are recorded separately and the invoice can route without requiring a common provider. |

## Goal traceability

| Goal | Primary requirements | Demonstration |
|---|---|---|
| G1 — Stable product contract | FR1, FR4, FR5, FR13; NFR7 | AC1, AC7, AC9 |
| G2 — Governed country policy | FR2, FR3, FR17; NFR3, NFR4 | AC2, AC6, AC8 |
| G3 — Reusable capability frameworks | FR5–FR12, FR18; NFR1, NFR2, NFR6 | AC1, AC3, AC9, AC10 |
| G4 — Independent obligation outcomes | FR10, FR15, FR16 | AC4, AC5 |
| G5 — Add countries without forks/history loss | FR3, FR7, FR9, FR11, FR13, FR17; NFR7 | AC1, AC6, AC9, AC10 |

## Metrics and measurement plan

| Measure | Why | Baseline/target status | Owner |
|---|---|---|---|
| Country onboarding lead time by capability | Tests whether the shared boundary reduces repeated discovery/delivery work | Baseline required from France/Spain and first new pack; no target yet | Platform product |
| Percentage of country requirements satisfied by proven shared capability | Measures capability reuse, not code reuse | Assessment method/target open | Architecture + product |
| First-pass validation and correction completion | Shows product/customer data readiness | Baseline per product/country required | Product + country owner |
| Duplicate external mutation rate | Detects idempotency/recovery failure | Target must be approved; objective is no preventable duplicates | Operations |
| Outcome-unknown age/backlog | Measures reconciliation health | Thresholds require provider/authority evidence | Operations |
| Policy/evidence completeness | Ensures every decision is explainable | Target proposal: 100%; governance approval required | Compliance |
| Country-pack escape/change incidents | Detects unsafe policy release | Baseline and severity policy required | Country owner |

## Rollout, dependencies and decision gates

1. Approve shared vs country responsibility matrix and accountable owners.
2. Inventory France/Spain capabilities against FR1–FR18; label reusable, adaptable, missing or country-bound with evidence.
3. Select a reference product, country/direction and bounded cohort; confirm volume/data/support baseline.
4. Approve canonical semantic/provenance model and API/event compatibility principles.
5. Build country-pack authoring, test, approval, effective-date and rollback governance before live policy.
6. Demonstrate happy, correction, retry, outcome-unknown, duplicate, rollback and historical-continuity scenarios in a sandbox.
7. Complete legal, regulatory, security, privacy, operations and support readiness for the reference pack.
8. Pilot with kill criteria and reconciled evidence; expand only after success measures and incident review.

Dependencies include country legal/compliance owners, Sage product teams, existing France/Spain capability evidence, architecture, platform engineering, security/privacy, identity/trust, operations/support, network governance plus provider contracts, official technical specifications and sandbox access.

## Risks and mitigations

| Risk | Impact | Mitigation/gate |
|---|---|---|
| France/Spain topology leaks into core | Other countries require workarounds/forks | Capability contract and Germany counter-example review |
| Canonical model loses country/source meaning | Non-compliance or irreconcilable evidence | Extensions, provenance, round-trip/loss analysis and country-owner approval |
| Policy-as-code is treated as ungoverned configuration | Incorrect obligations activate silently | Approval, signed artefact, tests, effective interval, rollback and audit |
| UK/Ireland open policy becomes invented requirements | Rework and false commitment | Explicit unknown states and production gates |
| Delivery/reporting outcomes collapse into one status | False success and unsafe retry | Independent exchange legs and acceptance tests |
| Reuse target drives premature coupling | Platform complexity without proven value | Measure capability fitness and onboarding outcomes, not code percentage |
| External outage/timeout duplicates legal documents | Customer/compliance harm | Durable intent, idempotency, outcome-unknown and reconciliation |
| Local accountability becomes unclear | Slow decisions and regulatory exposure | Named pack owner/RACI and evidence provenance |

## Consultation questions

| Question | Why it matters | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Which product, country and direction is the reference cohort? | Determines data, API and operational depth | Portfolio/platform product | Delivery start | Germany inbound/outbound assessment is a useful topology test; no choice approved |
| What existing France/Spain capabilities are demonstrably reusable? | Avoids rewrite and false reuse assumptions | Architecture + current teams | Architecture baseline | Reuse frameworks only after fitness evidence |
| Who legally approves and operationally owns each pack/version? | Controls policy activation and incidents | Country compliance + platform | Production | Country owns policy; platform owns safe execution |
| Is one physical canonical schema appropriate, or a semantic layer over versioned contracts? | Affects compatibility and loss | Architecture | Detailed design | Semantic contract first |
| Which lifecycle meanings are genuinely universal? | Prevents country events being forced into a false linear state | Product + country teams | API/event design | Use event vocabulary with optional meanings |
| What are product/country volume, latency and retention baselines? | Needed for measurable NFRs | Product/operations/legal | Production SLO/data policy | Per-country tiers may differ |
| How are policy artefacts signed, promoted and rolled back? | Prevents unapproved regulation changes | Security + platform engineering | Live policy | Treat packs as governed deployable artefacts |
| What is the stable Confluence parent page and space? | Required for requested child-page hierarchy | Document owner | Publication only | Create only after explicit approval |

## Decisions

| Decision | Status | Owner/date |
|---|---|---|
| Use one shared-platform parent and separate country PRDs | Confirmed by user request | User, 2026-08-10 |
| Keep GitHub Markdown canonical and publish all four PRDs to the user-supplied stable pages | Confirmed by user | 2026-08-10 |
| Use a neutral core plus governed country packs as the product hypothesis | Proposed; consultation required | TBD |
| Separate document, delivery and reporting compliance | Proposed product principle | TBD |
| Treat lifecycle as preserved events plus derived views | Proposed solution; architecture approval required | TBD |
| Do not promise 70–80% reuse | Confirmed drafting constraint; evidence required for any target | 2026-08-10 |
| Keep network/channel, provider service role and Sage adapter as separate route concepts; no vendor is selected by this PRD | Confirmed by user-supplied Peppol context and official OpenPeppol model | 2026-08-11 |
| Create four focused child analyses under the commonality page for identifiers/delegation, lifecycle mapping, Peppol multi-address routing and cross-border reuse | Confirmed by user feedback | 2026-08-12 |

## Revision history

| Date | Change | Evidence/decision | Pull request |
|---|---|---|---|
| 2026-08-10 | Initial discovery PRD; converted research text diagrams into Confluence-safe service and compliance-domain visuals; added Germany/Ireland/UK child structure | User request, supplied research and official sources | |
| 2026-08-10 | Added a consolidated 12-visual research atlas covering all source diagram themes and retained only code-like snippets as text | User direction | |
| 2026-08-10 | Approved for publication to existing page `866150169`; existing page hierarchy preserved | User approval | |
| 2026-08-11 | Removed embedded HTML headings from all diagrams and promoted their titles to native Confluence headings | Confluence rendering feedback | |
| 2026-08-11 | Added a diagram-led route model separating regulation, network, provider and adapter; strengthened Peppol four-corner evidence, requirements and acceptance | User context and official OpenPeppol sources | |
| 2026-08-12 | Added four child research PRDs covering country identifiers and accountants, lifecycle mappings, Peppol multi-address routing, and cross-border reusable capability boundaries | User feedback and supplied accountant research | |
