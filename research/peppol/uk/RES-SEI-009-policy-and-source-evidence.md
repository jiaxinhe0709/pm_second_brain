---
id: RES-SEI-009
title: UK Peppol policy and source evidence
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-003
  - PRD-SEI-230
  - PRD-SEI-227
  - PRD-SEI-245
confluence:
  publish: false
  page_id: ""
---

# UK Peppol policy and source evidence

UK product preparation needs to distinguish current public-sector exchange, voluntary business exchange and the announced VAT e-invoicing mandate. These contexts can share Peppol capabilities, but one context's contract does not establish another's legal scope or technical profile.

This is a research baseline checked on 15 October 2026. Source IDs resolve through [RES-SEI-003](../RES-SEI-003-peppol-source-register.md#uk-sources). [PRD-SEI-230](../../../prds/PRD-SEI-230-uk-e-invoicing-compliance-pack.md) remains the canonical UK product requirements document.

## Confirmed direction and its limits

| Finding | Evidence | Product consequence and limit |
|---|---|---|
| Peppol is the announced core interoperability network | UK01, network announcement | Shared Peppol readiness work is justified. Final UK governance, profile and participant rules are not specified by this announcement. |
| HMRC plans mandatory B2B/B2G VAT e-invoicing from April 2029 | UK02, E-Invoicing description | Use April 2029 as the planning direction. Final applicability, exemptions and transition need legal qualification. |
| Full guidance, standards, technical specification and legislation are planned by the end of 2027–2028 | UK02, same description | Preserve the roadmap's period; do not invent a precise publication day or treat the artefacts as already delivered. |
| A further implementation roadmap is planned at Budget 2026 | UK02, planned activity | Check and reconcile that roadmap when available. This baseline has not verified a later published roadmap. |
| Real-time reporting will not be introduced alongside the 2029 mandate | UK03 §8, government response | Do not include a new real-time invoice-data feed to HMRC in the 2029 baseline. Later reporting remains a separate policy decision. |
| Legacy-system treatment is still subject to stakeholder engagement in the announcement | UK01, following paragraph | Discover affected products and assisted routes; do not promise an exemption or permanent PDF route. |

The reporting finding is narrower than “HMRC reporting is unknown”. It concerns real-time reporting alongside this mandate; it does not remove existing tax obligations or establish that no future tax-data obligation can arise.

## Current public-sector context

Cabinet Office guidance describes a requirement for relevant contracting authorities to accept and process qualifying, undisputed electronic invoices under section 67. It identifies the required standard/syntax and version context, and explains the relationship with the earlier regime. **UK04, paragraphs 3–5 and 11–17.** This is acceptance guidance within its public-contract scope, not evidence that every UK supplier must now send every invoice through Peppol.

The original section 67 page could not be retrieved in this review. Legal qualification therefore remains open for original text, amendments, commencement, territorial scope and the selected contract. **UK05.** Do not use this research to settle a specific customer's legal obligation.

NHS Supply Chain describes an existing four-corner exchange and AP context. **UK06.** Qualify the actual buyer, programme, purchase references, message types and integration contract before using it as a product requirement. Its programme wording does not define Peppol syntax for all markets or the future VAT mandate.

## UK applicability questions

The following are evidence gaps, not inferred requirements.

| Area | Question to settle | Interim preparation |
|---|---|---|
| Parties and VAT status | Which issuer/recipient categories and registrations are in scope? How are VAT groups and entities handled? | Preserve legal-entity and tax facts separately from Sage tenants |
| Transaction scope | How do domestic, cross-border, B2B/B2G and any other cases differ? | Record the transaction context; avoid universal eligibility |
| Territorial treatment | Which GB/Northern Ireland and goods/services distinctions affect the mandate? | Preserve relevant facts and seek current HMRC interpretation |
| Document classes | Which invoice, credit, correction, simplified or self-billing cases are covered? | Inventory product capability without choosing final document forms |
| Profile and versions | Which UK semantic, syntax, process and code-list artefacts apply? | Qualify global candidates; keep UK statutory selection open |
| Identity and authority | Which participant schemes, identity checks and delegation rules apply? | Separate represented business, caller and registration authority |
| Network governance | Which authority and additional provider obligations govern the UK offer? | Do not generalise P12's England NHS/SCCL entry into a future UK-wide authority |
| Receiving and responses | What must recipients support, and which feedback is required? | Keep receipt, import, buyer decision and payment separate |
| Transition and enforcement | Which cohorts, grace periods, sanctions or assisted options exist? | Catalogue affected users and products; avoid invented deadlines or exceptions |
| Retention and access | What evidence, readability, storage and exit duties apply? | Assess current controls and retain the unresolved country binding |

## Implications for existing documents

| Owning document | Proposed follow-up after research review |
|---|---|
| PRD-SEI-230 | Refine reporting wording with UK03's explicit 2029 position; retain later reporting as a separate decision. Link final scope and profile decisions to the applicable original sources. |
| PRD-SEI-233 | Qualify any final UK participant rules separately from P05's globally registrable schemes. |
| PRD-SEI-245 | Confirm the legal entity, authority, scope and conformance evidence for the intended UK cohort. |
| PRD-SEI-242 | Bind response expectations to the actual selected UK process and counterparty capability. |

No PRD is changed by this research. The immediate next evidence and readiness decisions are owned by [RES-SEI-011](RES-SEI-011-readiness-and-open-decisions.md).
