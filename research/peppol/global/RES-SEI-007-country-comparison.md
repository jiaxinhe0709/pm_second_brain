---
id: RES-SEI-007
title: Peppol country comparison
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-003
  - PRD-SEI-228
  - PRD-SEI-229
  - PRD-SEI-230
  - PRD-SEI-234
confluence:
  publish: false
  page_id: ""
---

# Peppol country comparison

Global reuse depends on knowing which concerns stay shared and which change by market. This baseline provides a broad authority inventory and selected comparisons. It does not treat authority presence, a reachable recipient or a Peppol identifier as proof of domestic tax compliance.

## Authority inventory

The official authority register lists the following jurisdictions on 15 October 2026. **P12**, jurisdiction headings in the [source register](../RES-SEI-003-peppol-source-register.md#global-network-sources). Regional groups are navigation aids, not legal territories or a measure of production adoption.

| Group | Listed jurisdictions |
|---|---|
| Europe | Belgium, Denmark, England, Finland, France, Germany, Greece, Iceland, Ireland, Italy, Luxembourg, Norway, Poland, Portugal, Slovakia, Sweden, Netherlands |
| Asia and Middle East | Japan, Malaysia, Oman, Singapore, Taiwan, United Arab Emirates |
| Oceania | Australia, New Zealand |
| Africa | Nigeria |

P12 also identifies OpenPeppol's authority role where no national authority exists. This is an authority inventory, not a complete list of countries with participants. The “England” entry must retain that scope; it is not evidence for the future UK-wide mandate authority.

## Selected comparisons

These findings establish why a uniform worldwide configuration would be unsafe. Source versions and limits are in [RES-SEI-003](../RES-SEI-003-peppol-source-register.md#country-comparison-sources).

| Market | Confirmed evidence | What needs separate qualification | Implication for shared capability |
|---|---|---|---|
| UK | Government selected Peppol as core interoperability direction. UK01 | Final scope, profile, identifiers, governance and transition | Prepare shared exchange while retaining UK activation gates |
| Belgium | Official FAQ dates the scoped structured-invoice obligation to 1 January 2026 and describes Peppol exchange. C03 Q14/18 | Original law, transaction scope, exceptions, alternatives and receiving capability | Keep mandatory/voluntary use and permitted fallback as country rules |
| Australia and New Zealand | ATO describes shared A-NZ invoice specifications and links PINT A-NZ; local accreditation includes due diligence, security and tests. C01 | Exact profile release, country-specific obligations and provider evidence | Shared semantic patterns still need local accreditation and version binding |
| Japan | Digital Agency manages JP PINT and publishes distinct invoice, self-billing and non-tax-registered-business specifications. C02 | Selected process, exact release, tax treatment and product field coverage | Profile support must distinguish document and business variants |
| Singapore | IRAS FAQ separates phased tax-data submission from customer exchange; without activation of that submission feature, customer exchange can continue without transmission to IRAS. C04 p. 1 and §1.3 | Current e-Tax Guide, cohort, data contract, local accreditation and reporting outcomes | Preserve independently tracked delivery and reporting actions |
| Ireland | OGP official indexed guidance describes Peppol for public-procurement invoice transmission. C05, limited retrieval | Full current guidance, buyer contract and applicable legal scope | Do not extend a B2G use case into a universal domestic B2B claim |

These are findings from the cited public guidance, not delivery approvals. In particular, the Belgium and Singapore rows require original legal and current technical qualification before implementation. The UK is the first detailed country workstream in this pack; other rows are comparative evidence.

## Cross-border scenario assessment

| Scenario | Questions the country owners must settle | Safe product outcome while unresolved |
|---|---|---|
| UK seller sends to an overseas Peppol participant | Which seller and buyer rules apply? Does the selected document/process satisfy both ends? Is domestic reporting independent? | Distinguish technical reachability from an approved legal route |
| Sender and receiver use different local PINT specialisations | Which common or receiving profile is advertised? Which mappings and extensions are valid? | Identify unsupported profile or mapping without changing the invoice silently |
| Participant uses an international scheme | Is the scheme allowed for the intended legal entity and process? How is identity established? | Keep identity association open until qualified |
| Buyer is reachable but has no required business-response capability | Which process is selected and which response is expected? | Explain the delivery evidence without promising buyer approval |
| Invoice exchange succeeds but local reporting fails | Is a separate action required, and what is its correction path? | Keep each action's evidence and owner separate |

These are proposed research scenarios. They do not assert that every pair of local profiles can interoperate or that transformation is always permitted.

## Country assessment record

For each country proposed for delivery, capture:

| Area | Minimum decision evidence |
|---|---|
| Business scope | Customer segment, B2B/B2G context, domestic/cross-border scope and intended benefit |
| Authority and law | Original legal instruments, applicable authority, effective dates and exclusions |
| Process | Document types, directions, invoice/correction/self-billing processes and response expectations |
| Identity | Legal/tax/network identifiers, scheme state, verification and delegated authority |
| Profile | Syntax, specialisation, release, mapping and validation artefacts |
| Exchange and reporting | Recipient capability, transport requirements and separate tax actions |
| Operations | Local accreditation, support, incident, data, retention and exit obligations |
| Implementation | Source capability, owner, proven coverage, local changes and remaining tests |

Do not copy an entire national pack into this comparison. Link to its authoritative research and PRD when one exists.

## Next depth and country selection

1. Complete the UK evidence and scenario gates in RES-SEI-009–011.
2. Use Belgium as a candidate comparison for scoped mandatory exchange, A-NZ/Japan for profile specialisation and Singapore for exchange/reporting separation. This shortlist is proposed, not a delivery-market commitment.
3. Extend Germany and Ireland through [PRD-SEI-228](../../../prds/PRD-SEI-228-germany-e-invoicing-compliance-pack.md) and [PRD-SEI-229](../../../prds/PRD-SEI-229-ireland-e-invoicing-compliance-pack.md), rather than creating competing country requirements here.
4. Prioritise remaining markets by Sage customer demand, counterparties, applicable dates, implementation gaps and operating cost. Product owners need to supply these inputs before a rollout order can be justified.

Spain remains governed by its own public/private platform evidence and PRDs. Neither its appearance in a participant code list nor a shared UBL pattern replaces the Spain-specific rules.
