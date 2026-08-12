---
id: PRD-SEI-234
title: E-Invoicing — Cross-Border Applicability and Reusable Country Capabilities
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-08-12
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-228
  - PRD-SEI-229
  - PRD-SEI-230
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: "866152237"
  title: E-Invoicing — Cross-Border Applicability and Reusable Country Capabilities
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Cross-Border Applicability and Reusable Country Capabilities

## Decision summary

Reuse capability frameworks, not another country's legal conclusions. A country pack decides applicability and activates reusable modules with its own evidence, dates, schemas, statuses, route and reporting rules.

Current official evidence supports two deliberately different examples:

- France: domestic B2B e-invoicing is complemented by transaction e-reporting for B2C and operators established abroad.
- Spain: Royal Decree 238/2026 applies mandatory B2B e-invoicing when the recipient business/professional has its seat, permanent establishment, domicile or habitual residence in Spain and the operation is addressed to that Spanish presence. A foreign-recipient sale is therefore outside that decree's mandatory B2B route on the cited test; this does **not** prove that no other invoicing, VAT, reporting or destination-country obligation applies.

## Applicability first; reusable modules second

<!-- confluence-html-macro:start -->
<div class="eicb-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eicb-map *{box-sizing:border-box}.eicb-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eicb-map svg{display:block;width:1100px;height:590px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eicb-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eicb-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eicb-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eicb-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eicb-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eicb-map .copy{fill:#42526e;font-size:8.5px}.eicb-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eicb-map .path{fill:none;stroke:#00875a;stroke-width:2}.eicb-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eicb-map .arrow{fill:#00875a}.eicb-map .arrow-g{fill:#6b778c}.eicb-map .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1100px;margin-top:10px}.eicb-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eicb-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The same transaction facts can activate different document, delivery and reporting plans. Optional modules are reusable only through country-owned bindings.</p>
  <svg viewBox="0 0 1100 590" role="img" aria-label="Seller, buyer and transaction facts enter an effective-dated applicability engine. It determines relevant seller, buyer and establishment jurisdictions and evaluates each approved country pack. The French example routes domestic B2B through e-invoicing and international or B2C transactions through applicable e-reporting. The Spanish example applies the mandatory B2B e-invoice route when the recipient has the relevant Spanish seat or establishment; otherwise the transaction leaves that specific mandatory route and continues to other applicable tax, invoice and destination-country evaluations. Germany, Ireland and UK packs remain evidence-gated. A module library provides optional reporting, Peppol delivery, status mapping, public copy, payment events and discovery frameworks, but each country pack supplies its own binding, schema, route, dates and evidence.">
    <text x="32" y="30" class="label">FACTS</text><text x="312" y="30" class="label">COUNTRY POLICY</text><text x="744" y="30" class="label">COMPLIANCE PLAN</text>
    <rect x="32" y="62" width="230" height="174" rx="10" class="main"/><text x="52" y="91" class="title">Transaction context</text><text x="52" y="114" class="copy">seller legal entity + establishment</text><text x="52" y="136" class="copy">buyer legal entity + establishment</text><text x="52" y="158" class="copy">VAT registrations + tax treatment</text><text x="52" y="180" class="copy">B2B/B2C/B2G • domestic/cross-border</text><text x="52" y="202" class="copy">document type • supply • effective time</text><text x="52" y="224" class="copy">evidence/confidence for missing facts</text>
    <path d="M262 149 H310" class="path"/><polygon points="310,149 300,143 300,155" class="arrow"/>
    <rect x="312" y="62" width="244" height="174" rx="10" class="finish"/><text x="332" y="91" class="title">Applicability engine</text><text x="332" y="114" class="copy">identify relevant jurisdictions</text><text x="332" y="136" class="copy">select effective country policy versions</text><text x="332" y="158" class="copy">evaluate scope / exemption / dependency</text><text x="332" y="180" class="copy">return reasons + evidence + unknowns</text><text x="332" y="202" class="copy">create independent obligation legs</text><text x="332" y="224" class="copy">never default unknown to compliant</text>
    <path d="M556 149 H604 V94 H652" class="path"/><polygon points="652,94 642,88 642,100" class="arrow"/>
    <path d="M556 149 H604 V214 H652" class="path"/><polygon points="652,214 642,208 642,220" class="arrow"/>
    <path d="M556 149 H604 V334 H652" class="path-opt"/><polygon points="652,334 642,328 642,340" class="arrow-g"/>
    <rect x="654" y="52" width="412" height="84" rx="10" class="main"/><text x="674" y="80" class="title">France pack example</text><text x="674" y="101" class="copy">FR domestic B2B → e-invoice route + invoice-derived authority data</text><text x="674" y="120" class="copy">B2C / operator abroad → applicable transaction e-reporting route</text>
    <rect x="654" y="172" width="412" height="84" rx="10" class="main"/><text x="674" y="200" class="title">Spain pack example</text><text x="674" y="221" class="copy">Recipient Spanish seat/PE/residence in scope → mandatory B2B route</text><text x="674" y="240" class="copy">Otherwise → outside this test; continue other applicable evaluations</text>
    <rect x="654" y="292" width="412" height="84" rx="10" class="optional"/><text x="674" y="320" class="title">Germany • Ireland • UK packs</text><text x="674" y="341" class="copy">Activate only official, effective rules; unknown details remain gates</text><text x="674" y="360" class="copy">ViDA compatibility does not erase national policy versions</text>
    <text x="32" y="310" class="label">REUSABLE CAPABILITY LIBRARY — FRAMEWORKS, NOT COUNTRY RULES</text>
    <rect x="32" y="336" width="174" height="72" rx="10" class="optional"/><text x="52" y="365" class="title">Reporting leg</text><text x="52" y="386" class="copy">schedule • transform • ack</text>
    <rect x="224" y="336" width="174" height="72" rx="10" class="optional"/><text x="244" y="365" class="title">Peppol delivery</text><text x="244" y="386" class="copy">discover • route • reconcile</text>
    <rect x="416" y="336" width="174" height="72" rx="10" class="optional"/><text x="436" y="365" class="title">Lifecycle mapping</text><text x="436" y="386" class="copy">raw event → dimensions</text>
    <rect x="32" y="430" width="174" height="72" rx="10" class="optional"/><text x="52" y="459" class="title">Public copy</text><text x="52" y="480" class="copy">submit • retrieve • evidence</text>
    <rect x="224" y="430" width="174" height="72" rx="10" class="optional"/><text x="244" y="459" class="title">Payment events</text><text x="244" y="480" class="copy">scope • deadline • status</text>
    <rect x="416" y="430" width="174" height="72" rx="10" class="optional"/><text x="436" y="459" class="title">Identity/discovery</text><text x="436" y="480" class="copy">scheme • source • freshness</text>
    <path d="M590 372 H654" class="path-opt"/><path d="M590 466 H620 V372" class="path-opt"/><polygon points="654,372 644,366 644,378" class="arrow-g"/>
    <rect x="654" y="414" width="412" height="88" rx="10" class="warn"/><text x="674" y="443" class="title">Country-pack binding required</text><text x="674" y="464" class="copy">applicability • schema/profile • route • statuses • deadlines</text><text x="674" y="483" class="copy">authority • exception • evidence owner/version • rollout controls</text>
    <rect x="190" y="534" width="720" height="32" rx="16" class="finish"/><text x="300" y="555" class="title">Reuse the engine and module contract; never inherit another country's legal answer</text>
  </svg>
  <div class="notes"><div class="note"><strong>Cross-border is multi-policy</strong>Seller, buyer, establishments, tax treatment and date can make more than one jurisdiction relevant.</div><div class="note"><strong>Outside one mandate is not “nothing applies”</strong>Continue tax, invoice, reporting and destination-country evaluation with explicit evidence.</div><div class="note"><strong>Optional means policy-activated</strong>A module can be reused in UK or Ireland only when that pack supplies approved bindings.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Reuse boundary

| Reusable framework | Must remain country-specific |
|---|---|
| Applicability engine and explainable decision envelope | Scope tests, exemptions, establishments, dates and legal source |
| Reporting-leg orchestration | Required data, aggregation, deadline, authority route and acknowledgement |
| Peppol discovery/transport framework | Participant schemes, BIS/process, onboarding and national governance |
| Validation/transformation engine | CIUS/profile, mandatory fields, code lists and semantic exceptions |
| Lifecycle event ledger/mapping engine | Raw status catalog, mapping, precedence and customer wording |
| Identity/delegation model | Country identifiers, permitted representatives and operation-specific authority |

## Requirements and acceptance

| ID | Requirement / acceptance |
|---|---|
| CB-FR1 | Evaluate seller, buyer, relevant establishments, VAT/tax context, transaction type, supply, document and effective time before selecting obligations. |
| CB-FR2 | Return each relevant country-policy result with applied version, evidence, reason, obligation legs, exemption and unresolved facts. |
| CB-FR3 | Treat `outside this mandate` separately from `no obligation applies`; continue all configured country/tax/reporting evaluations. |
| CB-FR4 | Activate a reusable module only through an approved country binding with schema/profile, route, statuses, dates, exceptions, owner and tests. |
| CB-FR5 | Keep Spanish B2B e-invoicing, Spanish VERI*FACTU/SII and French e-reporting as separate policy domains even when they reuse orchestration. |
| CB-FR6 | Preserve the country policy and module versions selected for every invoice/reporting leg; later reuse or policy changes do not rewrite history. |
| CB-AC1 | Given a French seller invoices a business established abroad, then the French pack evaluates transaction e-reporting and does not route it as French domestic B2B e-invoicing. |
| CB-AC2 | Given a Spanish seller invoices a foreign recipient with no relevant Spanish seat/establishment, then the RD 238/2026 recipient test is out of scope and the engine continues other applicable evaluations. |
| CB-AC3 | Given Ireland later requires a reporting leg similar in shape to Spain, then the shared reporting framework is reused but Ireland supplies its own rule, schema, dates, route, statuses and evidence. |

## Evidence and open gates

| Evidence | Finding | Impact |
|---|---|---|
| [Spain Royal Decree 238/2026, Article 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), 2026-03-25 | Mandatory B2B e-invoicing applies when the recipient business/professional has the relevant seat, permanent establishment, domicile or habitual residence in Spain | Supports Spanish recipient-presence scope test; other obligations still require separate evaluation |
| [French tax authority e-invoicing overview](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique), modified 2026-05-26 | Domestic French B2B is in e-invoicing; transactions with non-taxable persons or operators established abroad are in transaction e-reporting | Confirms France-specific reporting branch, not a universal country pattern |
| [European Commission ViDA 2026 work programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en), 2026-05-22 | Cross-border B2B DRR based on e-invoicing moves toward 2030 EU implementation | Drives future compatibility/versioning; does not replace current national rules |

Open gates: full Spain cross-border decision table (sales, purchases, intra-EU, exports/imports, fixed establishments, reverse charge); interaction with VERI*FACTU/SII; France edge cases; Germany/Ireland/UK official rules; module ownership/versioning; and reference scenarios approved by country legal/compliance owners.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-12 | Initial child discovery PRD for cross-border applicability and safe country-capability reuse | User feedback and official Spanish, French and EU sources |
| 2026-08-12 | Published as a child of commonality page `866150169` | User publication approval |
