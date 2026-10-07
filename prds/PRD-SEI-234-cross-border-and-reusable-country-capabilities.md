---
id: PRD-SEI-234
title: E-Invoicing — Cross-Border Applicability and Reusable Country Capabilities
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-10-07
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-228
  - PRD-SEI-229
  - PRD-SEI-230
  - PRD-SEI-231
  - PRD-SEI-232
  - PRD-SEI-233
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

An **exchange action** is one separately tracked action, such as delivering an invoice, submitting a public copy or reporting an invoice event. Each action has its own result. See the [shared definition](../context/GLO-SEI-001-e-invoicing-terminology.md#invoices-representations-and-rules).

## Decision summary

Reuse capability frameworks, not another country's legal conclusions. A country pack decides applicability and activates reusable modules with its own evidence, dates, schemas, statuses, route and reporting rules.

Current official evidence supports two deliberately different examples:

- France: domestic B2B e-invoicing is complemented by transaction e-reporting for B2C and operators established abroad.
- Spain: Royal Decree 238/2026 applies mandatory B2B e-invoicing when the recipient business/professional has its seat, permanent establishment, domicile or habitual residence in Spain and the operation is addressed to that Spanish presence. A foreign-recipient sale is therefore outside that decree's mandatory B2B route on the cited test; this does **not** prove that no other invoicing, VAT, reporting or destination-country obligation applies.

## Actual country applicability terms before reusable classification

`B2B`, `B2C`, `B2G`, `domestic` and `cross-border` are useful common labels, but they are not country rules. Preserve each official scope term, exemption and rollout condition first; only then map it to a reusable applicability contract.

| Country | Actual official term or scope test | Current compliance consequence | Must remain country-specific |
|---|---|---|---|
| France | Purchases and sales of goods/services between businesses established in France and subject to French VAT | French e-invoicing; the platform handling the invoice also sends invoice-derived data to the administration | Establishment/VAT scope, effective cohort/date, exempt operations, approved-platform and profile rules |
| France | Transactions with non-taxable persons, for example consumers (`B2C`) | Transaction e-reporting rather than the domestic B2B invoice-delivery route | Aggregation/detail, frequency, fields, responsible reporter and exceptions |
| France | Transactions with operators established abroad, including relevant exports, intra-Community supplies/acquisitions and other international cases | Transaction e-reporting can apply even though the French domestic B2B route does not | Seller/buyer reporting responsibility, place/tax treatment, foreign identifier treatment and excluded operations |
| France | Operations for which VAT is payable on collection, such as relevant services where no debit option or reverse-charge exclusion applies | Payment/collection e-reporting | Applicability, reporter, date/amount semantics and reporting schedule |
| France | Transactions to public entities (`B2G`) | Separate public-sector invoicing route and rules | Chorus Pro/public-sector identifiers, profiles and acknowledgements |
| Spain | Recipient is an entrepreneur/professional with its business seat, permanent establishment, domicile or habitual residence in Spain, and the operation is addressed to that Spanish presence | Mandatory electronic invoice under RD 238/2026, subject to commencement and exceptions | Evidence for recipient status/presence and the establishment to which the operation is addressed |
| Spain | Simplified invoice under the general simplified-invoice rule | Excluded from the mandatory electronic-invoice obligation unless it is a qualified simplified invoice under the cited exception | Document classification and any later ministerial exclusions |
| Spain | Recipient or third party materially issues the invoice under permitted self-billing/third-party arrangements | Electronic-invoice scope can still apply; the legally obliged supplier remains responsible | Agreement, authority, performing actor, invoice identity and reporting responsibility |
| Spain | Private platform, public solution or a combination is selected | Delivery/public-copy/interconnection obligations differ even for the same in-scope B2B invoice | Destination, faithful-copy, signature, format, status and acknowledgement rules |
| Spain | `B2C`, public-sector (`B2G`), SII or VERI*FACTU/SIF context | Not converted into RD 238/2026 domestic B2B merely because invoice data is shared | Each domain retains its own scope, actor, route, lifecycle and evidence |
| Germany | Transaction between domestic businesses (`inländische Unternehmer`) | German structured e-invoice rules generally apply, subject to transition and exceptions | Domestic-business test, effective date, allowed syntax and agreed transmission channel |
| Germany | End consumer (`B2C`) or many tax-exempt transactions under §4 numbers 8–29 UStG | Outside the ordinary mandatory B2B e-invoice rule | Exact exemption and ordinary invoice duty |
| Germany | Small-value invoice up to €250 gross, ticket treated as an invoice, or supply by a small business covered by the stated exception | E-invoice issuance exception can apply | Threshold/version, supplier status and document evidence |
| Germany | Public-administration transaction (`B2G`) | Separate federal/state public-sector rules; not the same tax B2B route | Buyer jurisdiction, XRechnung/profile, Leitweg-ID and transport |
| Ireland | VAT-registered large corporate managed by Revenue's Large Corporates Division and established or fixed-established in Ireland issues a domestic B2B invoice from 1 November 2028 | Must issue an EN 16931 structured invoice and report a subset of invoice data to Revenue | Cohort evidence, technical profile, reporting subset, route and acknowledgement |
| Ireland | Any business in Ireland receiving from 1 November 2028 | Must be able to receive structured e-invoices even if not yet in the issuing cohort | Recipient capability, delivery network/profile and onboarding |
| United Kingdom | HMRC roadmap wording: mandatory e-invoicing for all VAT invoices from April 2029; Peppol announced as the core interoperability network | Product planning can prepare for VAT-invoice and Peppol capability | Legislation, B2B/B2G/B2C boundary, geography, exemptions, participant schemes, profiles, reporting and rollout details remain open |

Sources: [France — scope of e-invoicing and transaction/payment e-reporting](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique), [France — foreign businesses without a permanent establishment](https://www.impots.gouv.fr/international-professionnel/le-reporting-pour-les-entreprises-etrangeres-sans-etablissement-stable), [Spain RD 238/2026 Articles 3–6](https://www.boe.es/eli/es/rd/2026/03/25/238), [Germany BMF e-invoice FAQ, March 2026](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html), [Ireland Revenue Phase One](https://www.revenue.ie/en/vat/vida-vat-modernisation/large-corporates-vat-modernisation.aspx), [UK HMRC Transformation Roadmap 2026](https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/hmrc-transformation-roadmap-update-2026) and [UK Tax Update 2026](https://www.gov.uk/government/publications/summary-of-tax-update-2026-simplification-modernisation-and-fairness/tax-update-2026-simplification-modernisation-and-fairness-summary), accessed 2026-08-25.

### Spain customer-segmentation research reconciliation

The internal [E-Invoicing Customer Segmentation — Spanish Legislation Knowledge](https://confluence.sage.com/spaces/SLK/pages/771503855/E-Invoicing+Customer+Segmentation) page adds a useful product lens: classify a Spanish seller's customers by relationship (`B2B`, `B2G`, `B2C`) and geography (`domestic`, `EU`, `ROW`), then consider whether additional platform services create customer value. It is an internal research input, not the legal or technical source of record.

The matrix below preserves that insight while separating confirmed obligations, planning direction and evidence still required.

| Customer segment from Spanish seller perspective | Evidence-backed current treatment | Format/route treatment | Third-party/platform opportunity | Evidence status and correction to source wording |
|---|---|---|---|---|
| `B2B — domestic` | RD 238/2026 applies when the recipient is an entrepreneur/professional with the relevant Spanish seat, permanent establishment, domicile or habitual residence and the operation is addressed there, subject to exceptions | Structured EN16931 message using `CII`, `UBL`, `EDIFACT` or `Facturae`; public solution uses UBL under the future ministerial order | Lifecycle extensions, partial-payment/status capability, payment integration, managed routing and reconciliation may add value | **Confirmed scope and syntax families.** Do not fix `01/07/2027`, `2027–2028`, `UBL 2.5` or `CIUS ES` until the ministerial order/profile does so. Effective application is `+12 months` for turnover over EUR 8m and `+24 months` for others after that order enters into force |
| `B2B — EU` | Not generally brought into Spain's mandatory domestic B2B route merely because the seller is Spanish; evaluate the recipient presence, place/tax treatment and each relevant destination-country rule | Use the evidenced destination/bilateral profile and route. From 1 July 2030, ViDA introduces cross-border B2B digital reporting based on e-invoicing | Destination-country transformation, Peppol or other approved delivery, reporting and reconciliation can add value | **ViDA direction confirmed; current transaction treatment remains multi-policy.** Replace broad “EU mandatory 2030” and “any format including PDF” with an effective-dated destination and ViDA decision |
| `B2B — ROW` | A recipient with no relevant Spanish presence is outside the cited RD 238/2026 mandatory-recipient test; this does not prove that no invoicing, VAT, customs, reporting or destination-country obligation applies | Apply the destination/bilateral format and channel supported by evidence; Peppol is not universal | Multi-country format, destination routing, evidence and exception handling can add value | **Corrected:** replace unconditional “No” with `outside this Spanish mandate / continue other policy evaluations` |
| `B2G — domestic` | Separate Spanish public-sector invoicing rules apply; do not classify the transaction through the RD 238/2026 B2B route | Facturae/FACe and any applicable EN16931/CIUS or public-body profile must be selected from the current B2G contract | High-volume, multi-administration, validation, routing and status consolidation may add value | **Separate domain confirmed; exact supported versions/profile require B2G-owned evidence.** Do not infer them from the B2B ministerial-order gap |
| `B2G — EU or ROW` | Evaluate the destination public-procurement mandate and buyer authority; no single worldwide rule applies | Use the destination public-sector profile, identifiers and network. Peppol may be required or useful only where the applicable authority/profile confirms it | Destination transformation, authority discovery, Peppol/other transport and acknowledgement management may add value | **Country-specific.** “Usually Peppol” is a product hypothesis, not a universal compliance rule |
| `B2C — domestic` | Outside mandatory RD 238/2026 B2B. Spanish general invoicing rules require recipient consent for electronic invoicing except where mandatory e-invoicing applies | Preserve an accessible/human-readable customer representation as required by the applicable product/legal policy; do not make PDF universally mandatory without evidence | Digital delivery, consent evidence and customer access may add value but are not private-platform interconnection | **Consent principle confirmed; “always PDF/human-readable” needs a precise source and accessibility/retention contract** |
| `B2C — EU or ROW` | Evaluate destination consumer, VAT, invoicing and consent requirements; the B2B ViDA statement does not automatically classify B2C | Select destination-compliant presentation, delivery and evidence rules | Multi-country consumer delivery and tax/reporting services may add value | **Open by destination.** Do not reuse the domestic B2C or cross-border B2B conclusion |

#### Product conclusions from the segmentation

1. Relationship, geography and legal applicability are separate facts. `B2B + EU` is not itself a compliance decision.
2. “Mandatory e-invoice,” “permitted electronic invoice,” “mandatory reporting” and “customer may benefit from a platform” must be returned as separate outcomes.
3. A format family is not a complete profile. Version, CIUS, validation artefacts, route and effective dates belong to the applicable country/B2G/destination binding.
4. Peppol is a selectable network capability, not the default answer for every EU, ROW or B2G transaction.
5. Effective dates must retain their legal trigger. Until the ministerial order is effective, Spain B2B rollout is represented as relative rules rather than an assumed calendar date.

Sources: [BOE — RD 238/2026 Article 3 scope, Article 7 formats and final provision 4 commencement](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), [AEAT — mandatory e-invoicing overview](https://sede.agenciatributaria.gob.es/Sede/iva/novedades-iva/novedades-normativa-2026/real-decreto-238-2026-25-marzo.html), [BOE — consolidated invoicing regulation, Articles 8 bis and 9](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696), and [European Commission — VAT in the Digital Age](https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en), accessed 2026-09-11.

### Reusable applicability contract derived from those terms

| Actual country variation | Reusable fact or decision shape |
|---|---|
| Business, consumer or public body wording | `counterpartyRelationship` plus verified tax/economic-operator status; never label from identifier alone |
| Seat, establishment, domicile, residence and “operation addressed to” tests | Seller/buyer legal-subject and relevant-presence references with provenance |
| Domestic, intra-EU, export/import or operator-abroad wording | Policy-relative geographic classification; evaluate every relevant jurisdiction |
| Goods/services, tax-on-collection, reverse charge and exemptions | Supply/tax-result inputs; applicability consumes rather than recalculates tax |
| Invoice, qualified/simplified invoice, credit/correction or self-billing | Document classification plus principal and performing actor |
| Cohort, threshold, transition and effective date | Effective-dated policy version and explicit `required`, `permitted`, `not_applicable`, `exempt` or `undetermined` result |
| E-invoice, recipient delivery, public copy and authority reporting | Independent document, delivery and reporting obligation actions |
| Country route/profile/status terminology | Country-owned binding to shared validation, routing, lifecycle, evidence and recovery frameworks |

## Applicability first; reusable modules second

<!-- confluence-html-macro:start -->
<div class="eicb-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eicb-map *{box-sizing:border-box}.eicb-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eicb-map svg{display:block;width:100%;max-width:1100px;height:auto;min-width:760px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eicb-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eicb-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eicb-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eicb-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eicb-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eicb-map .copy{fill:#42526e;font-size:8.5px}.eicb-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eicb-map .path{fill:none;stroke:#00875a;stroke-width:2}.eicb-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eicb-map .arrow{fill:#00875a}.eicb-map .arrow-g{fill:#6b778c}.eicb-map .notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;min-width:0;margin-top:10px}.eicb-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eicb-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">The same transaction facts can activate different document, delivery and reporting plans. Optional modules are reusable only through country-owned bindings.</p>
  <svg viewBox="0 0 1100 590" role="img" aria-label="Seller, buyer and transaction facts enter an effective-dated applicability engine. It determines relevant seller, buyer and establishment jurisdictions and evaluates each approved country pack. The French example routes domestic B2B through e-invoicing and international or B2C transactions through applicable e-reporting. The Spanish example applies the mandatory B2B e-invoice route when the recipient has the relevant Spanish seat or establishment; otherwise the transaction leaves that specific mandatory route and continues to other applicable tax, invoice and destination-country evaluations. Germany, Ireland and UK packs remain evidence-gated. A module library provides optional reporting, Peppol delivery, status mapping, public copy, payment events and discovery frameworks, but each country pack supplies its own binding, schema, route, dates and evidence.">
    <text x="32" y="30" class="label">FACTS</text><text x="312" y="30" class="label">COUNTRY POLICY</text><text x="744" y="30" class="label">COMPLIANCE PLAN</text>
    <rect x="32" y="62" width="230" height="174" rx="10" class="main"/><text x="52" y="91" class="title">Transaction context</text><text x="52" y="114" class="copy">seller legal entity + establishment</text><text x="52" y="136" class="copy">buyer legal entity + establishment</text><text x="52" y="158" class="copy">VAT registrations + tax treatment</text><text x="52" y="180" class="copy">B2B/B2C/B2G • domestic/cross-border</text><text x="52" y="202" class="copy">document type • supply • effective time</text><text x="52" y="224" class="copy">evidence/confidence for missing facts</text>
    <path d="M262 149 H310" class="path"/><polygon points="310,149 300,143 300,155" class="arrow"/>
    <rect x="312" y="62" width="244" height="174" rx="10" class="finish"/><text x="332" y="91" class="title">Applicability engine</text><text x="332" y="114" class="copy">identify relevant jurisdictions</text><text x="332" y="136" class="copy">select effective country policy versions</text><text x="332" y="158" class="copy">evaluate scope / exemption / dependency</text><text x="332" y="180" class="copy">return reasons + evidence + unknowns</text><text x="332" y="202" class="copy">create independent obligation actions</text><text x="332" y="224" class="copy">never default unknown to compliant</text>
    <path d="M556 149 H604 V94 H652" class="path"/><polygon points="652,94 642,88 642,100" class="arrow"/>
    <path d="M556 149 H604 V214 H652" class="path"/><polygon points="652,214 642,208 642,220" class="arrow"/>
    <path d="M556 149 H604 V334 H652" class="path-opt"/><polygon points="652,334 642,328 642,340" class="arrow-g"/>
    <rect x="654" y="52" width="412" height="84" rx="10" class="main"/><text x="674" y="80" class="title">France pack example</text><text x="674" y="101" class="copy">FR domestic B2B → e-invoice route + invoice-derived authority data</text><text x="674" y="120" class="copy">B2C / operator abroad → applicable transaction e-reporting route</text>
    <rect x="654" y="172" width="412" height="84" rx="10" class="main"/><text x="674" y="200" class="title">Spain pack example</text><text x="674" y="221" class="copy">Recipient Spanish seat/PE/residence in scope → mandatory B2B route</text><text x="674" y="240" class="copy">Otherwise → outside this test; continue other applicable evaluations</text>
    <rect x="654" y="292" width="412" height="84" rx="10" class="optional"/><text x="674" y="320" class="title">Germany • Ireland • UK packs</text><text x="674" y="341" class="copy">Activate only official, effective rules; unknown details remain gates</text><text x="674" y="360" class="copy">ViDA compatibility does not erase national policy versions</text>
    <text x="32" y="310" class="label">REUSABLE CAPABILITY LIBRARY — FRAMEWORKS, NOT COUNTRY RULES</text>
    <rect x="32" y="336" width="174" height="72" rx="10" class="optional"/><text x="52" y="365" class="title">Reporting action</text><text x="52" y="386" class="copy">schedule • transform • ack</text>
    <rect x="224" y="336" width="174" height="72" rx="10" class="optional"/><text x="244" y="365" class="title">Peppol delivery</text><text x="244" y="386" class="copy">discover • route • reconcile</text>
    <rect x="416" y="336" width="174" height="72" rx="10" class="optional"/><text x="436" y="365" class="title">Lifecycle mapping</text><text x="436" y="386" class="copy">raw event → dimensions</text>
    <rect x="32" y="430" width="174" height="72" rx="10" class="optional"/><text x="52" y="459" class="title">Public copy</text><text x="52" y="480" class="copy">submit • retrieve • evidence</text>
    <rect x="224" y="430" width="174" height="72" rx="10" class="optional"/><text x="244" y="459" class="title">Payment events</text><text x="244" y="480" class="copy">scope • deadline • status</text>
    <rect x="416" y="430" width="174" height="72" rx="10" class="optional"/><text x="436" y="459" class="title">Identity/discovery</text><text x="436" y="480" class="copy">scheme • source • freshness</text>
    <path d="M590 372 H620 V458 H654" class="path-opt"/><path d="M590 466 H620" class="path-opt"/><polygon points="654,458 644,452 644,464" class="arrow-g"/>
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
| Reporting-action orchestration | Required data, aggregation, deadline, authority route and acknowledgement |
| Peppol discovery/transport framework | Participant schemes, BIS/process, onboarding and national governance |
| Validation/transformation engine | CIUS/profile, mandatory fields, code lists and semantic exceptions |
| Lifecycle event ledger/mapping engine | Raw status catalog, mapping, precedence and customer wording |
| Identity/delegation model | Country identifiers, permitted representatives and operation-specific authority |

## Requirements and acceptance

| ID | Requirement / acceptance |
|---|---|
| CB-FR1 | Evaluate seller, buyer, relevant establishments, VAT/tax context, transaction type, supply, document and effective time before selecting obligations. |
| CB-FR2 | Return each relevant country-policy result with applied version, evidence, reason, obligation actions, exemption and unresolved facts. |
| CB-FR3 | Treat `outside this mandate` separately from `no obligation applies`; continue all configured country/tax/reporting evaluations. |
| CB-FR4 | Activate a reusable module only through an approved country binding with schema/profile, route, statuses, dates, exceptions, owner and tests. |
| CB-FR5 | Keep Spanish B2B e-invoicing, Spanish VERI*FACTU/SII and French e-reporting as separate policy domains even when they reuse orchestration. |
| CB-FR6 | Preserve the country policy and module versions selected for every invoice/reporting action; later reuse or policy changes do not rewrite history. |
| CB-FR7 | Preserve the official country scope term, source/version, decisive facts, exemption and result before mapping it to a common relationship/geography classification. |
| CB-FR8 | Evaluate issuance, receipt, recipient delivery, public-copy and authority-reporting obligations independently, including cohort asymmetry. |
| CB-FR9 | Classify counterparty relationship and geography independently from legal applicability, format/profile, route and optional service recommendation. |
| CB-FR10 | Return mandatory e-invoice, permitted electronic invoice, reporting obligations and value-added platform capabilities as separate results with their own evidence. |
| CB-FR11 | Store relative commencement rules with their legal trigger and resolve a fixed date only from an effective, approved policy version. |
| CB-FR12 | Select syntax family, version, CIUS/profile, validation artefacts and route from the applicable country/public-sector/destination binding rather than from `B2B`, `B2G`, `B2C`, `EU` or `ROW` labels alone. |
| CB-AC1 | Given a French seller invoices a business established abroad, then the French pack evaluates transaction e-reporting and does not route it as French domestic B2B e-invoicing. |
| CB-AC2 | Given a Spanish seller invoices a foreign recipient with no relevant Spanish seat/establishment, then the RD 238/2026 recipient test is out of scope and the engine continues other applicable evaluations. |
| CB-AC3 | Given Ireland later requires a reporting action similar in shape to Spain, then the shared reporting framework is reused but Ireland supplies its own rule, schema, dates, route, statuses and evidence. |
| CB-AC4 | Given a German sale to a private consumer or a qualifying small-value invoice, then the German domestic B2B rule is not activated merely because both parties or the currency are German. |
| CB-AC5 | Given an Irish business must receive from 1 November 2028 but is not in the large-corporate issuing cohort, then receipt readiness can be required while issuance remains not applicable for that cohort. |
| CB-AC6 | Given a UK VAT invoice dated before final legislation and technical rules are approved, then the future Peppol direction remains a planning input and the production applicability result is not guessed. |
| CB-AC7 | Given a domestic Spanish B2B transaction is evaluated before the ministerial-order trigger is known, then the result preserves the `+12/+24 months` rule and does not assert `01/07/2027` as its effective date. |
| CB-AC8 | Given a Spanish seller invoices an EU business, then the result separately evaluates Spanish scope, destination-country obligations and the effective ViDA rule; it does not return “EU mandatory 2030” as a complete current compliance answer. |
| CB-AC9 | Given a B2G or cross-border route could use Peppol, then the route is activated only when the destination authority/profile and participant evidence support it. |

## Evidence and open gates

| Evidence | Finding | Impact |
|---|---|---|
| [Spain Royal Decree 238/2026, Article 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), 2026-03-25 | Mandatory B2B e-invoicing applies when the recipient business/professional has the relevant seat, permanent establishment, domicile or habitual residence in Spain | Supports Spanish recipient-presence scope test; other obligations still require separate evaluation |
| [Internal E-Invoicing Customer Segmentation — Spanish Legislation Knowledge](https://confluence.sage.com/spaces/SLK/pages/771503855/E-Invoicing+Customer+Segmentation), supplied 2026-09-11 | Proposes a useful `B2B/B2G/B2C × domestic/EU/ROW` customer and service-needs matrix | Retained as product segmentation; dates, formats and universal Peppol statements are corrected or evidence-gated against primary sources |
| [AEAT mandatory e-invoicing overview](https://sede.agenciatributaria.gob.es/Sede/iva/novedades-iva/novedades-normativa-2026/real-decreto-238-2026-25-marzo.html), accessed 2026-09-11 | Confirms AEAT's public-solution role and the commencement dependency on the future ministerial order | Operational corroboration; BOE remains the statutory source and future AEAT specifications remain a delivery gate |
| [French tax authority e-invoicing overview](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique), modified 2026-05-26 | Domestic French B2B is in e-invoicing; transactions with non-taxable persons or operators established abroad are in transaction e-reporting | Confirms France-specific reporting branch, not a universal country pattern |
| [European Commission ViDA 2026 work programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en), 2026-05-22 | Cross-border B2B DRR based on e-invoicing moves toward 2030 EU implementation | Drives future compatibility/versioning; does not replace current national rules |
| [German BMF e-invoice FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html), updated 2026-03 | Uses the actual domestic-business scope and identifies B2C, tax-exempt, small-value, ticket, small-business and B2G boundaries | Supplies Germany reference terms; detailed channel/profile and transition fixtures remain country-owned |
| [Ireland Revenue Phase One](https://www.revenue.ie/en/vat/vida-vat-modernisation/large-corporates-vat-modernisation.aspx), accessed 2026-08-25 | Defines November 2028 large-corporate domestic B2B issuance/reporting and all-business receipt asymmetry | Supplies Ireland reference scenarios; later phases and technical artefacts remain open |
| [UK HMRC Transformation Roadmap 2026](https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/hmrc-transformation-roadmap-update-2026) and [Tax Update 2026](https://www.gov.uk/government/publications/summary-of-tax-update-2026-simplification-modernisation-and-fairness/tax-update-2026-simplification-modernisation-and-fairness-summary) | State April 2029 mandatory e-invoicing for all VAT invoices and Peppol as the core interoperability network | Confirms direction/date wording, not final country-policy or technical bindings |

Open gates: Spain ministerial order, fixed rollout dates and technical profile; current B2G format/version/CIUS contracts; full Spain sales/purchases and cross-border decision table; interaction with VERI*FACTU/SII; destination-country B2B/B2G/B2C fixtures; France territorial/exemption and buyer-side international cases; Germany transition/channel and state-level B2G fixtures; Ireland later phases/technical artefacts; final UK legislation/profile/reporting rules; module ownership/versioning; and reference scenarios approved by country legal/compliance owners.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-12 | Initial child discovery PRD for cross-border applicability and safe country-capability reuse | User feedback and official Spanish, French and EU sources |
| 2026-08-12 | Published as a child of commonality page `866150169` | User publication approval |
| 2026-08-12 | Rerouted reusable-module connectors through a clear gutter into the country binding and made the diagram responsive | Confluence visual review |
| 2026-08-25 | Added actual five-country relationship, geography, exemption, cohort and route terms before deriving the reusable applicability contract | User request; official France, Spain, Germany, Ireland and UK sources |
| 2026-09-11 | Reconciled the internal Spain customer-segmentation matrix against primary scope, format, commencement, consent and ViDA evidence; retained its product-service lens while correcting or gating unsupported dates, profiles and universal network assumptions | User-supplied Spanish Legislation Knowledge page; BOE RD 238/2026; AEAT; BOE invoicing regulation; European Commission ViDA |
