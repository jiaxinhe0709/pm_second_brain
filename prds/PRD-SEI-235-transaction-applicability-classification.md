---
id: PRD-SEI-235
title: "E-Invoicing — Transaction Applicability: B2B, B2C, B2G and Geographic Scope"
type: prd
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-21
updated: 2026-08-21
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-228
  - PRD-SEI-229
  - PRD-SEI-230
  - PRD-SEI-231
  - PRD-SEI-234
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: ""
  title: "E-Invoicing — Transaction Applicability: B2B, B2C, B2G and Geographic Scope"
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Transaction Applicability: B2B, B2C, B2G and Geographic Scope

## Decision summary

`B2B`, `B2C` or `B2G` is one input to an applicability decision; it is not the answer. The platform must also determine the transaction direction, seller and buyer establishments, place and type of supply, tax status, geographic relationship, document type, effective date, rollout cohort and exemptions.

For every transaction, the platform must return three independent compliance decisions:

1. **Document compliance** — must a structured invoice or other compliant document be created, and under which semantic/profile rules?
2. **Delivery compliance** — must it be delivered through a prescribed network, platform or public-sector route, and what acknowledgement completes delivery?
3. **Reporting compliance** — must invoice, transaction or payment data be reported to an authority, by whom and by when?

Each result is `required`, `permitted`, `not applicable`, `exempt` or `undetermined`. `Outside one mandate` must never be treated as `no compliance obligation`.

## Relationship to the cross-border page

[PRD-SEI-234](PRD-SEI-234-cross-border-and-reusable-country-capabilities.md) defines the boundary between reusable platform capabilities and country-owned legal rules. This page owns the detailed facts, classifications, decision contract, scenario catalogue and coverage measures used to decide which country rules activate.

It does not replace tax determination, the country compliance packs or the identity model in [PRD-SEI-231](PRD-SEI-231-country-identifiers-tenancy-and-delegated-accountants.md).

## Outcome

A product or provider adapter can submit one normalized transaction context and receive an explainable, effective-dated compliance plan that:

- distinguishes B2B, B2C and B2G;
- distinguishes domestic, intra-EU, export, import and other international cases;
- resolves which legal entity or fixed establishment supplies and receives the transaction;
- treats issue, receive, deliver and report duties independently;
- identifies every applicable jurisdiction and policy version;
- preserves unresolved facts rather than silently selecting a route;
- provides evidence suitable for operations, audit and customer explanation.

## Scope

### In scope

- Sales and purchase invoices, credit notes and corrective/rectification documents.
- Supplier-issued invoices, self-billing and third-party issuance.
- B2B, B2C and B2G counterparties.
- Domestic, intra-EU and extra-EU transactions, including import and export perspectives.
- Legal-seat, fixed-establishment, domicile and habitual-residence tests where a country rule uses them.
- Issuance, receipt, document, delivery and reporting obligations.
- Effective dates, transition periods, cohorts, thresholds and exemptions.
- France, Spain, Germany, Ireland and the UK as the first evidence set.
- An explainable decision and scenario-test contract for country packs.

### Out of scope

- Calculating VAT amount, tax rate or place of supply; the applicability service consumes the tax result and supporting facts.
- Customs declarations and import-control workflows.
- Filing VAT returns or replacing statutory accounting records.
- Defining the detailed invoice syntax, network protocol or authority API for every country.
- Treating voluntary e-invoice exchange as proof that a statutory mandate applies.

## Product principles

1. **Classify before routing.** Do not select Peppol, a national platform or email before applicability is known.
2. **Evaluate all relevant jurisdictions.** Seller, buyer, establishments and place of supply may activate more than one policy.
3. **Keep the three compliance dimensions separate.** A transaction can require reporting without mandated delivery, or receipt capability without an issuance duty.
4. **Separate facts from legal conclusions.** Product integrations supply facts; versioned country packs decide their effect.
5. **Preserve uncertainty.** Missing or conflicting facts produce `undetermined`, not a guessed compliant answer.
6. **Explain every outcome.** Each obligation or exemption identifies the rule, version, evidence and decisive facts.
7. **Do not infer authority from identity.** A delegate may classify or submit only when the operation-specific authority in PRD-SEI-231 permits it.

## Applicability is multi-dimensional

<!-- confluence-html-macro:start -->
<div class="eita-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eita-map *{box-sizing:border-box}.eita-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eita-map svg{display:block;width:100%;max-width:1100px;height:auto;min-width:800px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eita-map .fact{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.eita-map .policy{fill:#e3fcef;stroke:#36b37e;stroke-width:1.7}.eita-map .result{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eita-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.eita-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eita-map .copy{fill:#42526e;font-size:8.4px}.eita-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eita-map .line{fill:none;stroke:#00875a;stroke-width:1.9}.eita-map .arrow{fill:#00875a}.eita-map .notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;min-width:0;margin-top:10px}.eita-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eita-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Party relationship and geography are separate inputs. The country packs produce independent document, delivery and reporting decisions.</p>
  <svg viewBox="0 0 1100 570" role="img" aria-label="Transaction facts are classified across party relationship, geography, establishments, tax context, document and time. All relevant versioned country policies are evaluated. The output is an explainable applicability decision with independent document, delivery and reporting outcomes; missing or conflicting facts are returned as undetermined.">
    <text x="30" y="28" class="label">TRANSACTION FACTS</text><text x="390" y="28" class="label">POLICY EVALUATION</text><text x="735" y="28" class="label">COMPLIANCE PLAN</text>
    <rect x="30" y="54" width="300" height="66" rx="9" class="fact"/><text x="48" y="80" class="title">Party relationship</text><text x="48" y="101" class="copy">B2B • B2C • B2G • government acting as business</text>
    <rect x="30" y="136" width="300" height="66" rx="9" class="fact"/><text x="48" y="162" class="title">Geographic relationship</text><text x="48" y="183" class="copy">domestic • intra-EU • export • import • other international</text>
    <rect x="30" y="218" width="300" height="78" rx="9" class="fact"/><text x="48" y="244" class="title">Entity and establishment</text><text x="48" y="265" class="copy">seller/buyer seat • fixed establishment • VAT registration</text><text x="48" y="283" class="copy">establishment to which the transaction is addressed</text>
    <rect x="30" y="312" width="300" height="78" rx="9" class="fact"/><text x="48" y="338" class="title">Tax and supply context</text><text x="48" y="359" class="copy">place/type of supply • taxable/exempt • reverse charge</text><text x="48" y="377" class="copy">invoice requirement • B2C special scheme • public procurement</text>
    <rect x="30" y="406" width="300" height="78" rx="9" class="fact"/><text x="48" y="432" class="title">Document, direction and time</text><text x="48" y="453" class="copy">sale/purchase • invoice/credit/self-bill • issue date</text><text x="48" y="471" class="copy">effective date • cohort • threshold • transition</text>
    <path d="M330 87 H365 V269 H390" class="line"/><path d="M330 169 H365" class="line"/><path d="M330 257 H365" class="line"/><path d="M330 351 H365" class="line"/><path d="M330 445 H365 V269" class="line"/><polygon points="390,269 380,263 380,275" class="arrow"/>
    <rect x="392" y="104" width="285" height="330" rx="12" class="policy"/><text x="416" y="137" class="title">Evaluate all relevant country packs</text><text x="416" y="166" class="copy">1. validate required facts and provenance</text><text x="416" y="192" class="copy">2. identify seller, buyer, establishment and tax jurisdictions</text><text x="416" y="218" class="copy">3. select rules effective at transaction time</text><text x="416" y="244" class="copy">4. test relationship, geography, scope and exemptions</text><text x="416" y="270" class="copy">5. test issuance and receipt duties separately</text><text x="416" y="296" class="copy">6. derive document, delivery and reporting legs</text><text x="416" y="322" class="copy">7. retain rule, evidence, decisive facts and unknowns</text><text x="416" y="348" class="copy">8. combine compatible obligations; expose conflicts</text><rect x="416" y="374" width="237" height="38" rx="8" class="warn"/><text x="432" y="398" class="title">Never convert unknown into “not applicable”</text>
    <path d="M677 269 H720" class="line"/><polygon points="720,269 710,263 710,275" class="arrow"/>
    <rect x="722" y="54" width="348" height="92" rx="10" class="result"/><text x="744" y="83" class="title">Document compliance</text><text x="744" y="105" class="copy">required profile/representation • issuer • validation</text><text x="744" y="126" class="copy">outcome + reason + policy/evidence version</text>
    <rect x="722" y="170" width="348" height="92" rx="10" class="result"/><text x="744" y="199" class="title">Delivery compliance</text><text x="744" y="221" class="copy">recipient resolution • prescribed route • acknowledgement</text><text x="744" y="242" class="copy">outcome + reason + policy/evidence version</text>
    <rect x="722" y="286" width="348" height="92" rx="10" class="result"/><text x="744" y="315" class="title">Reporting compliance</text><text x="744" y="337" class="copy">reporting party • data set • authority • deadline • receipt</text><text x="744" y="358" class="copy">outcome + reason + policy/evidence version</text>
    <rect x="722" y="402" width="348" height="82" rx="10" class="warn"/><text x="744" y="431" class="title">Decision context</text><text x="744" y="453" class="copy">applicable jurisdictions • unresolved facts • conflicts</text><text x="744" y="472" class="copy">decision ID • evaluated time • trace/evidence references</text>
    <rect x="206" y="518" width="688" height="30" rx="15" class="result"/><text x="312" y="538" class="title">One transaction can have zero, one or several independent compliance legs</text>
  </svg>
  <div class="notes"><div class="note"><strong>B2B is not enough</strong>A domestic B2B invoice can have a different outcome from an intra-EU B2B invoice or a sale addressed to a local fixed establishment.</div><div class="note"><strong>Direction is asymmetric</strong>A company may have to receive structured invoices before it must issue them, or report a purchase when the seller cannot.</div><div class="note"><strong>B2G is a separate policy</strong>Public-procurement rules and routing identifiers can apply alongside or outside the tax e-invoice mandate.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Classification model

| Dimension | Canonical values | Why it changes the answer |
|---|---|---|
| Counterparty relationship | `B2B`, `B2C`, `B2G`, `G2B`, `unknown` | Selects business, consumer and public-sector policies; government may also act as an economic operator |
| Direction | `outbound_sale`, `inbound_purchase` | Issuer, receiver and reporter can differ |
| Geographic relationship | `domestic`, `intra_eu`, `export_non_eu`, `import_non_eu`, `international_other`, `undetermined` | Selects national, EU cross-border, export/import and destination-country evaluations |
| Seller/buyer presence | seat, fixed establishment, domicile/residence, VAT registration, no local presence | Registration alone may not equal establishment; some mandates use the establishment to which the supply is addressed |
| Tax actor status | taxable person, VAT registered, exempt/non-taxable business, consumer, public body | Determines whether B2B/B2C labels and invoice/reporting duties apply |
| Supply | goods/services, place of supply, tax treatment, reverse charge, intra-community supply/acquisition | Changes invoice, reporting and payment-data obligations |
| Document | invoice, simplified invoice, credit/correction, self-bill, advance, summary | Different documents can be included, excluded or carry different semantics |
| Time and cohort | tax point, issue date, company size/turnover/cohort, transition election | Determines the effective policy and whether issue/receipt duties have started |
| Delegation | supplier, customer self-billing, third party/accountant | Changes the actor performing an obligation, not the principal's underlying legal responsibility |

### Canonical geographic classification

Geography must be computed from country-coded legal and establishment facts, not from the invoice currency, language, delivery address or VAT number prefix alone.

| Classification | Minimum interpretation | Required follow-on evaluation |
|---|---|---|
| Domestic | The country pack's relevant seller and buyer presence/place tests resolve to the same country | Domestic e-invoice, public-sector and domestic reporting rules |
| Intra-EU | Relevant parties/presences are in different EU Member States | Current national rules plus EU cross-border rules effective at the transaction date |
| Export from country | Supplier-side evaluation is local and relevant customer/presence is outside the applicable territory | Export invoice, seller reporting and destination-country checks |
| Import into country | Relevant supplier is outside and buyer/presence is inside the applicable territory | Buyer/self-reporting, import tax and destination-country invoice checks |
| International other | Cross-border relationship that is not fully described by the EU categories | Seller, buyer and place-of-supply jurisdictions independently |
| Undetermined | One or more decisive presence, place or tax facts are missing/conflicting | Hold mandatory routing; return required facts and safe operational action |

`Domestic` is policy-relative. A VAT registration, branch address or ship-to location must not by itself prove that an entity is established in a country or that the transaction is addressed to that establishment.

## Party relationship × geography

This matrix defines which evaluations must run. It does not assert that every cell has a mandate.

| Relationship | Domestic | Intra-EU | Extra-EU / other international |
|---|---|---|---|
| B2B | Domestic country e-invoice, delivery and reporting policies; include cohort/exemption tests | Both national packs plus effective EU cross-border e-invoice/reporting rules | Supplier, buyer/presence, place-of-supply and import/export reporting policies |
| B2C | Consumer invoice/receipt rules, transaction/payment reporting and special schemes | Consumer invoice rules, OSS or other special-scheme facts, seller reporting | Consumer invoice rules, IOSS/import/export and reporting facts where relevant |
| B2G | Public procurement/e-invoice rules plus tax rules where the authority acts as a business | Destination public-sector route plus applicable cross-border/tax rules | Destination public-sector requirements, trade/tax rules and permitted route |
| G2B | Country-specific public-body sales and tax rules | Country-specific public-body and cross-border rules | Country-specific public-body and international rules |
| Unknown | `undetermined`; request counterparty status | `undetermined`; request counterparty status | `undetermined`; request counterparty status |

## Independent duties and asymmetry

| Duty | Question | Actor | Must not be inferred from |
|---|---|---|---|
| Issue | Must a structured invoice be created? | Supplier, customer under self-billing, or authorized third party | The buyer being able to receive |
| Receive | Must/can the buyer accept and process it? | Buyer and its service provider | Supplier issuance cohort alone |
| Deliver | Is a prescribed route/address/acknowledgement required? | Sender and recipient providers | Document validity alone |
| Report transaction | Must transaction/invoice data reach an authority? | Supplier, buyer, platform or another designated actor | Successful invoice delivery |
| Report payment | Must payment/collection data be reported? | Country-defined actor | Transaction reporting alone |
| Retain evidence | Which artifacts and policy decisions must be retained? | Principal and/or provider | A successful transport acknowledgement alone |

## Current five-country comparison

This is an applicability baseline, not a complete legal opinion. Country packs remain authoritative and versioned.

| Country | Confirmed relationship/geography boundary | Compliance consequence evidenced now | Gaps that must remain explicit |
|---|---|---|---|
| France | E-invoicing covers purchases/sales between businesses established in France and subject to French VAT. B2C and transactions with a taxable person not established in France enter transaction e-reporting rules; B2G remains separately mandatory | Domestic B2B can activate document and delivery obligations; B2C/international can activate reporting without using the same domestic invoice route | Detailed territorial cases, exemptions, overseas territories, payment reporting, self-billing and buyer-side international cases |
| Spain | RD 238/2026 applies when the recipient business/professional has a Spanish seat, fixed establishment, domicile or habitual residence and the operation is addressed to it; self-billing/third-party issuance is included | Recipient presence is a decisive fact for the mandatory B2B route | Full sales/purchases matrix; non-Spanish recipient cases; interaction with SII/VERI*FACTU, public sector, exemptions and commencement dependencies |
| Germany | The tax e-invoice rule generally concerns transactions between domestic businesses. B2C is outside that rule; B2G has separate public-sector rules and routes | Domestic B2B and B2G require separate policy evaluation; a Leitweg-ID is not a general B2B requirement | Detailed establishment test, exceptions, thresholds, transition periods, cross-border treatment and state-level B2G variance |
| Ireland | Phase 1 from November 2028 applies issue/reporting duties to VAT-registered large corporates for domestic B2B; businesses must be able to receive from mandated suppliers. Later phases extend domestic and intra-EU B2B scope | Issue and receive duties start for different populations; intra-EU requirements are separately phased | Final technical rules, cohort definition, exemptions, B2G interaction, B2C and detailed domestic/cross-border scenarios |
| UK | Current roadmap states mandatory VAT e-invoicing for B2B and B2G from April 2029 | B2B/B2G are planned policy categories | Legislation, exact VAT-invoice boundary, B2C treatment, geography, cohorts, exemptions, delivery model, reporting and technical specification remain open |

## Applicability decision contract

One evaluation returns an immutable `ApplicabilityDecision` linked to the source transaction version.

| Group | Required fields |
|---|---|
| Decision identity | `decisionId`, `transactionId`, `transactionVersion`, `evaluatedAt`, `evaluationEngineVersion` |
| Facts | relationship, direction, supply, document type, tax point/issue date, tax treatment, currency, self-billing/third-party indicator |
| Parties | seller/buyer legal entity, relevant establishment, country, tax status, verified identifier references and fact provenance |
| Geography | classification, seller jurisdiction, buyer jurisdiction, place-of-supply jurisdiction, relevant country-pack set, reasons |
| Policy | `policyId`, country, version, effective interval, evidence reference, evidence retrieval/verification time |
| Outcome | one decision per document, delivery and reporting leg: `required`, `permitted`, `not_applicable`, `exempt`, `undetermined` |
| Obligation | responsible actor, capability, format/profile, route/authority, deadline, acknowledgement, retention and dependency references |
| Explanation | decisive facts, rule path, exemption reason, unresolved/conflicting facts and allowed next actions |

### Outcome semantics

| Outcome | Meaning | Default platform behaviour |
|---|---|---|
| `required` | An effective policy requires the compliance leg | Create/validate the leg; fail closed if a mandatory dependency is unresolved |
| `permitted` | A compliant optional/contractual route is allowed but not mandated by this rule | Continue only under product/customer policy and record that it is voluntary |
| `not_applicable` | The policy was evaluated and its scope test did not apply | Retain reason; continue evaluating every other relevant policy |
| `exempt` | The transaction is in the policy domain but a cited exemption applies | Retain exemption, evidence and expiry/conditions |
| `undetermined` | Required facts/evidence are absent, contradictory or too stale | Do not claim compliance; request facts or send to controlled review |

## Decision journey

1. Receive a normalized transaction context with provenance for customer-supplied and system-derived facts.
2. Validate identity, counterparty status, relevant establishments, place/type of supply, direction, document and time.
3. Classify the party relationship and geographic relationship independently.
4. Identify every potentially relevant country and EU policy pack.
5. Select the versions effective at the tax point/issue time; do not use today's rule for historical transactions.
6. Evaluate scope, cohort, transition, threshold and exemption rules.
7. Produce document, delivery and reporting outcomes independently.
8. Resolve compatible obligations into a compliance plan; surface conflicts or missing prerequisites.
9. Persist the decision, rule path and evidence before delivery/reporting starts.
10. Re-evaluate only when an input fact or policy correction requires it; preserve prior decisions and actions as history.

## Business rules

| ID | Rule |
|---|---|
| APP-BR1 | The platform shall not derive applicability from `B2B`, `B2C` or `B2G` alone. |
| APP-BR2 | Seller and buyer country shall be resolved at the legal-entity and relevant-establishment levels; a VAT registration is a separate fact. |
| APP-BR3 | Currency, invoice language, bank country, network participant identifier and ship-to address shall not independently determine domestic/international classification. |
| APP-BR4 | Every potentially relevant country pack shall be evaluated; `not_applicable` in one pack shall not stop the others. |
| APP-BR5 | Document, delivery, transaction-reporting and payment-reporting legs shall have separate outcomes and lifecycles. |
| APP-BR6 | Issuance and receipt obligations shall be evaluated separately for phased rollouts. |
| APP-BR7 | B2G shall evaluate public-procurement rules separately from tax e-invoice rules, even if both use the same document or network. |
| APP-BR8 | Self-billing or third-party issuance changes the performing actor only when the country rule permits it and authority evidence is valid. |
| APP-BR9 | An exemption shall include its source, conditions, effective interval and decisive facts. |
| APP-BR10 | Missing or contradictory decisive facts shall return `undetermined`; user-configured defaults cannot be recorded as verified legal facts. |
| APP-BR11 | Policy corrections shall not rewrite the decision or evidence attached to completed historical actions. |
| APP-BR12 | A voluntary e-invoice shall be labelled `permitted`, not `required`, unless an effective mandate or contract supplies that requirement. |

## Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| APP-FR1 | Accept the complete classification model with provenance and verification time for decisive facts | Must |
| APP-FR2 | Resolve B2B/B2C/B2G/G2B without conflating a non-taxable legal entity with a consumer | Must |
| APP-FR3 | Resolve domestic, intra-EU, export, import, international-other or undetermined relative to each policy | Must |
| APP-FR4 | Represent multiple establishments and identify the establishment to which/from which the supply is made | Must |
| APP-FR5 | Evaluate all effective national and EU policy packs and return the rule path for each | Must |
| APP-FR6 | Evaluate issue and receive duties independently, including cohort and transition dates | Must |
| APP-FR7 | Return independent document, delivery, transaction-reporting and payment-reporting legs | Must |
| APP-FR8 | Represent scope exclusions, conditional exemptions, thresholds and expiry | Must |
| APP-FR9 | Return unresolved facts and safe next actions without claiming compliance | Must |
| APP-FR10 | Preserve the input snapshot, decision, policy version and evidence references immutably | Must |
| APP-FR11 | Re-evaluate a corrected transaction without losing the original decision/action trail | Must |
| APP-FR12 | Provide a simulation mode for future-dated rules and customer readiness analysis | Should |
| APP-FR13 | Expose a human-readable explanation and a machine-readable reason code | Must |
| APP-FR14 | Run country-owned reference scenarios automatically when policy configuration changes | Must |
| APP-FR15 | Report scenario and rule-branch coverage by country, relationship, geography and obligation type | Should |

## Representative scenario catalogue

The country owner must convert each row into effective-dated executable tests with expected outcomes and evidence.

| Scenario | Minimum facts being tested | Expected decision shape |
|---|---|---|
| French business → French business | Both established/subject to French VAT; domestic supply | Evaluate French domestic B2B document, delivery and invoice-derived reporting legs |
| French business → French consumer | Consumer status; domestic supply | Do not force B2B delivery; evaluate B2C transaction and payment reporting |
| French business → German business | French supplier, recipient not established in France, intra-EU | Evaluate French international reporting plus effective German/EU obligations |
| Foreign business → French business | Seller establishment, French buyer/presence, supply/tax facts | Evaluate buyer-side and seller-side obligations; do not assume symmetry with outbound case |
| Spanish business → Spanish business | Recipient Spanish presence and operation addressed to it | Evaluate RD 238/2026 B2B route plus separate tax/reporting domains |
| Spanish business → foreign business with no Spanish presence | Recipient-presence test is false | Mark that decree's route not applicable; continue other policies |
| Foreign supplier → Spanish fixed establishment | Recipient PE and operation addressed to it | Evaluate Spanish recipient test and responsible issuance/delivery actors |
| German business → German business | Domestic businesses, applicable date/cohort | Evaluate German domestic B2B document and receipt rules |
| German business → German consumer | Private consumer | Domestic B2B tax e-invoice rule not applicable; evaluate other invoice rules |
| German business → public authority | Public buyer and route facts | Evaluate B2G separately, including buyer reference/routing requirements |
| Irish large corporate → Irish business, November 2028 | Supplier cohort, domestic B2B, effective date | Issue/report required when effective; buyer receive capability evaluated separately |
| Irish non-issuer receives from mandated supplier | Buyer outside issuing cohort | Receive capability can be required before buyer issuance duty |
| Irish business → EU business, July 2030 | Intra-EU B2B and ViDA effective date | Evaluate EU DRR/e-invoice plus effective Irish/destination rules |
| UK VAT business → UK business, April 2029 | B2B VAT invoice and effective policy | Keep undetermined until final legislation/specification supplies rule details |
| UK VAT business → public body, April 2029 | B2G VAT invoice | Evaluate planned B2G category; keep route/reporting details gated |
| Self-billed domestic B2B invoice | Buyer issues for supplier; authority evidence | Preserve principal duty, verify self-billing is permitted and identify reporting actor |
| Cross-border credit note | Original decision link, correction date/reason | Evaluate correction semantics, delivery and reporting under applicable versions |
| Conflicting establishment evidence | Legal seat and transaction-addressed PE disagree | Return `undetermined` and block mandatory route selection pending resolution |

## Failure and recovery

| Failure | Detection | Safe behaviour | Recovery/evidence |
|---|---|---|---|
| Counterparty type missing | No verified business/consumer/public-body classification | Return `undetermined`; do not guess B2B | Request evidence; retain source and correction |
| Establishment conflict | Party, tax or transaction data points to different relevant presences | Hold mandatory routing/reporting where the difference is decisive | Controlled review and corrected fact version |
| No effective policy version | Transaction date falls outside configured interval | Fail closed for statutory automation | Country owner adds/approves version; record gap |
| Policy overlap/conflict | Two rules require incompatible formats, actors or deadlines | Create incident/manual review; do not silently discard one leg | Preserve both rule paths and resolution decision |
| Stale or unverified evidence | Verification age exceeds policy tolerance | Return warning or `undetermined` according to rule criticality | Re-verify official source and publish pack version |
| Route unavailable after required decision | Delivery dependency fails | Preserve compliant document; queue/retry within deadline; escalate before breach | Transport attempts, acknowledgements and incident trail |
| Reporting deadline at risk | Report not accepted within deadline budget | Prioritize retry/fallback allowed by country policy | Authority receipts, failure codes and operator actions |
| Retroactive policy correction | Official interpretation changes | Do not rewrite completed history automatically | Impact assessment, new policy version and controlled remediation |

## Non-functional requirements

| Area | Requirement |
|---|---|
| Explainability | Every outcome exposes decisive facts, policy/rule IDs, evidence and unresolved inputs |
| Determinism | Identical fact and policy versions produce the same result |
| Temporal correctness | Effective-time evaluation supports historical, current and future simulation without overwriting history |
| Isolation | Tenant data, decisions, evidence and delegated access remain isolated |
| Privacy | Tax and personal-derived identifiers are referenced using the minimum data required and policy-controlled access |
| Availability | The service shall define behaviour for cached policy evaluation and fail closed when a mandatory, freshness-sensitive decision cannot be made |
| Observability | Metrics and traces correlate classification, policy results, compliance legs, delivery/reporting outcomes and manual intervention |
| Change safety | A country-pack change cannot be released without schema validation, peer approval, regression scenarios and rollback metadata |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| APP-AC1 | Given a transaction is labelled B2B but the buyer establishment is unknown, when the domestic test depends on that establishment, then the outcome is `undetermined`, not domestic. |
| APP-AC2 | Given a French business sells to a French consumer, when applicability is evaluated, then French domestic B2B delivery is not activated and applicable B2C reporting is evaluated separately. |
| APP-AC3 | Given a French business sells to a business not established in France, when the French pack is evaluated, then the domestic B2B route is not selected and international transaction reporting is evaluated. |
| APP-AC4 | Given a Spanish recipient has a Spanish fixed establishment and the operation is addressed to it, when RD 238/2026 is effective, then that fact participates in the Spanish B2B scope test. |
| APP-AC5 | Given the same Spanish recipient is merely VAT-registered but no qualifying Spanish presence receives the operation, then registration alone does not prove the recipient-presence test. |
| APP-AC6 | Given a German public authority is the buyer, when evaluated, then B2G rules run separately and a Leitweg-ID is not inferred for ordinary B2B. |
| APP-AC7 | Given an Irish buyer is required to receive before it enters the issuing cohort, then receipt capability can be required while issuance remains not yet applicable. |
| APP-AC8 | Given a transaction is outside one country's mandate, then every other relevant national/EU policy still evaluates and the combined answer does not say “no obligation” unless all return that result. |
| APP-AC9 | Given policy version B replaces A, then a historical decision made under A retains A and a future simulation uses B. |
| APP-AC10 | Given two policy legs conflict, then both are preserved, automation stops at the conflict boundary and an evidence-backed resolution is required. |

## Coverage and percentage

A percentage is useful only when its denominator is explicit. The product must not claim “country coverage” from a count of implemented countries.

### Required measures

| Measure | Formula | Purpose |
|---|---|---|
| Scenario decision coverage | scenarios with approved expected outcomes ÷ required reference scenarios | Shows whether important transaction shapes have a verified answer |
| Automated scenario coverage | approved scenarios executed automatically ÷ approved scenarios | Shows how much verified policy is regression protected |
| Rule-branch coverage | effective rule branches exercised ÷ total effective branches in the country pack | Finds untested exemptions, cohorts and edge paths |
| Evidence freshness coverage | active rules with in-tolerance official evidence ÷ active rules | Detects stale legal conclusions |
| Determinate production rate | decisions returning required/permitted/not-applicable/exempt ÷ all evaluations | Operational signal; must be segmented so bad defaults cannot inflate it |
| Obligation completion rate | compliance legs completed with required acknowledgement before deadline ÷ due legs | Measures actual compliance delivery, not classification only |

### Minimum reporting slices

Every percentage must be filterable by country, policy version, B2B/B2C/B2G, domestic/intra-EU/other international, sale/purchase, document type and document/delivery/reporting leg.

The current document does **not** assert an implementation percentage. The baseline is established only after country owners approve the scenario inventory and expected results.

## Operations and governance

| Responsibility | Owner |
|---|---|
| Canonical facts and API contract | Platform product/engineering |
| Legal scope, evidence and interpretation | Named country compliance/legal owner |
| Country policy configuration and regression scenarios | Country pack owner with engineering review |
| Network, platform and authority bindings | Delivery/reporting capability owner |
| Delegated action policy | Identity/delegation owner and country compliance owner |
| Monitoring and incident response | Platform operations with country escalation path |

Every country-pack release requires:

- official evidence and retrieval/verification date;
- effective-from/effective-to dates and transition logic;
- relationship and geography coverage matrix;
- document, delivery and reporting outcomes;
- negative tests for out-of-scope and exemption branches;
- migration/rollback approach;
- named approver and open interpretation log.

## Metrics

- Applicability decisions by outcome and unresolved-fact reason.
- Transactions evaluated by relationship and geography.
- Policy-version selection failures and stale-evidence warnings.
- Manual review rate and median resolution time.
- Decisions changed after fact correction or policy correction.
- Compliance legs completed, late, rejected or awaiting acknowledgement.
- Scenario, branch and evidence-freshness coverage percentages.
- False-positive/false-negative applicability defects found in audit or production.

## Risks and controls

| Risk | Consequence | Control |
|---|---|---|
| `B2B` treated as sufficient | Wrong mandate, route or missing reporting | Mandatory multi-dimensional context and scenario tests |
| VAT number treated as establishment | Domestic/cross-border misclassification | Separate identity, registration and establishment facts with evidence |
| One country's result short-circuits evaluation | Destination/EU obligation omitted | Multi-policy evaluation and combined plan |
| Issuance and receipt conflated | Customers unprepared to receive or issue too early | Independent duty and cohort decisions |
| B2G folded into B2B | Wrong route/reference and public-sector rejection | Separate public procurement policy domain |
| Policy changes overwrite history | Audit evidence no longer matches action | Immutable decision and effective-dated policy versions |
| A high coverage percentage hides gaps | False readiness signal | Declared denominator and mandatory segmentation |

## Evidence register

| Source | Verified finding | Used for |
|---|---|---|
| [French tax authority — e-invoicing overview](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique), accessed 2026-08-21 | E-invoicing concerns purchases and sales between businesses established in France and subject to French VAT | French domestic B2B boundary |
| [French tax authority — transaction e-reporting](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiches_reforme/fiche-e-reporting_transactions.pdf), accessed 2026-08-21 | Transaction reporting covers B2C and international B2B cases, with defined exceptions | Separate French reporting branches |
| [Spain Royal Decree 238/2026, Article 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), 2026-03-25 | Scope uses the recipient's Spanish seat, fixed establishment, domicile or habitual residence and requires the operation to be addressed to it; it also covers permitted self-billing/third-party issuance | Spanish recipient-presence and delegated-issuance facts |
| [German Federal Ministry of Finance — e-invoice FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html), updated 2026-03-23 | The tax e-invoice rule generally concerns domestic B2B; private consumers are not affected; B2G rules apply separately | German relationship/geography split |
| [Irish Revenue — VAT Modernisation Timeline](https://www.revenue.ie/en/vat/vida-vat-modernisation/vat-modernisation-timeline.aspx), published 2026-07-20 | Domestic B2B issue/reporting is phased from November 2028; all businesses must be able to receive from mandated suppliers; intra-EU B2B follows in later phases | Independent issue/receive duties and time cohorts |
| [HMRC Transformation Roadmap progress update](https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/annex-summary-of-hmrcs-planned-activities-listed-in-this-transformation-roadmap-progress-update), published 2026-07-29 | Mandatory VAT e-invoicing is planned for B2B and B2G from April 2029, with detailed guidance, standards, specification and legislation to follow | UK planned relationship categories and evidence gates |
| [European Commission — ViDA 2026 work programme](https://taxation-customs.ec.europa.eu/news/vat-digital-age-2026-work-programme-available-2026-05-22_en), 2026-05-22 | From 1 July 2030 cross-border B2B transactions enter e-invoice-based digital reporting requirements; domestic systems align later | EU effective-time and intra-EU policy evaluation |
| [European Commission — EU VAT invoicing](https://taxation-customs.ec.europa.eu/taxation/vat/vat-businesses/invoicing_en), accessed 2026-08-21 | VAT invoices are generally required for B2B and certain B2C supplies; public administrations accept structured invoices; self-billing/third-party issuance can be allowed | Prevents party label from replacing invoice/supply tests |

## Open decisions and consultation gates

1. Which upstream service owns verified counterparty status, place/type of supply and relevant-establishment facts?
2. Is geographic classification returned by tax determination or recomputed from signed facts by applicability?
3. Which facts are safe customer assertions and which require registry, tax or compliance verification?
4. What is the controlled fallback when mandatory delivery/reporting is due but applicability remains undetermined?
5. How are conflicting obligations across seller, buyer and EU policies resolved and approved?
6. Which B2G layers are national, regional or buyer-specific in each first-wave country?
7. What are the complete France overseas-territory, B2C/payment and international-purchase matrices?
8. What are the complete Spain sales/purchase, fixed-establishment, SII/VERI*FACTU and public-sector interactions?
9. Which Germany exceptions, transition rules and federal/state B2G variants belong in the first release?
10. What final Ireland cohort definitions, technical rules and B2C/B2G boundaries are approved?
11. What UK geographic, exemption, route and reporting boundaries emerge from legislation and specification?
12. What minimum scenario coverage percentage is required at discovery exit, pilot and general availability?

## Readiness assessment

**Status: draft decision contract; not delivery-ready.**

The reusable classification dimensions, outcome model, requirements and initial official evidence are defined. Delivery remains gated by approved country decision tables, upstream fact ownership, policy governance, executable scenario baselines, operational fallback and final technical bindings.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-21 | Initial draft created as a separate detailed applicability page | User request to distinguish B2B/B2C/B2G and domestic/international transaction types; official country and EU evidence |
