---
id: RES-SEI-006
title: Peppol document profiles and validation
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-003
  - PRD-SEI-223
  - PRD-SEI-236
  - PRD-SEI-241
  - PRD-SEI-242
confluence:
  publish: false
  page_id: ""
---

# Peppol document profiles and validation

A valid invoice must fit the selected business process and receiving capability. “UBL supported” or “Peppol enabled” is too broad to establish this. Product and engineering need a versioned profile assessment that identifies required business facts, mapping gaps and validation evidence.

## Standards and contract layers

External facts below refer to the [source register](../RES-SEI-003-peppol-source-register.md#global-network-sources). Product implications are proposed controls for review.

| Layer | Confirmed distinction | Product implication |
|---|---|---|
| Business semantics | EN 16931 defines invoice business meaning; BIS Billing applies a more specific usage profile. P06 §§1, 15 | A schema pass cannot establish every business rule |
| XML syntax | BIS Billing identifies UBL 2.1 Invoice and CreditNote schemas. P06 §14 | Do not assume another route's UBL version or document shape is accepted |
| Peppol profile | Document and process identifiers qualify the supported exchange. P06 §§13–15 | Select identifiers and rules with recipient capability |
| Global PINT model | PINT Billing 1.1.3 provides a basis for jurisdiction specialisations. P08 | Evaluate each specialisation; a global model is not one worldwide tax rule pack |
| Rule artefacts | The Billing release publishes syntax links, code lists and Schematron files. P13 | Record the actual deployed artefact versions and test coverage |

The shared service should expose a precise supported-capability statement: country/context, direction, document type, syntax version, profile, process, rule release and effective period. This is a proposed assessment model; [PRD-SEI-241](../../../prds/PRD-SEI-241-ubl-validation-service.md) remains the authority for product validation behaviour.

## Release and response implications

BIS Billing 3.0.21 was published on 20 May 2026 and became mandatory on 17 August 2026. It adds an optional process with required invoice response and separate SMP registration. **P07, version 3.0.21.** This distinction matters to both discovery and product promises: a response expectation follows the selected process and counterparty capability, rather than the Peppol label alone.

The exact future UK profile remains an evidence gate in RES-SEI-009. Current Billing or PINT availability must not silently select it. A new release also needs regression assessment; a live documentation link alone cannot identify the validator that handled an earlier invoice.

## Field mapping qualification

Complete this assessment against the selected country/profile artefacts and real product inputs. The table names assessment areas, not final UK field requirements.

| Business information | Questions for product and mapping owners | Evidence before claiming coverage |
|---|---|---|
| Seller and buyer identities | Which legal, tax and electronic-address facts exist? Which schemes and formats apply? | Source-field-to-business-term-to-target-path mapping; valid and invalid samples |
| References | Can products supply the required buyer, order, contract or previous-invoice references? | Applicable rule IDs and correction guidance |
| Lines and adjustments | Are quantities, units, discounts, charges and their bases preserved? | Rounding and calculation boundary cases |
| Tax | Can source codes express the selected tax categories, exemptions and explanations? | Country tax mapping with owner and unsupported cases |
| Payment information | Which means, terms and payment references are represented? | Profile rules and product support evidence |
| Corrections and credits | Does the selected process use Invoice, CreditNote or another qualified method? | Document-type-specific examples and links to originals |
| Attachments and rendering | Are types, sizes and links supported by the selected contract? | Published limits, security controls and readability checks |

Do not infer complete mapping coverage from a source inventory, a single example or a successful happy-path document.

## Qualification cases

| Case | Proposed acceptance demonstration |
|---|---|
| Valid XML with missing required business information | Return the applicable rule and a correction action; no dispatch claim |
| Valid document for a different profile/process | Identify the mismatch before dispatch; do not relabel the document |
| Warning and fatal errors together | Preserve rule severity and apply the selected contract's disposition |
| Rule release changes | New work uses the approved release; historical results retain their original rule context |
| Same transaction under two country packs | Each runs only its applicable rules; one country's rule activation does not alter the other |
| Transformation changes bytes after a pass | Validate the final dispatch candidate under its target rules |
| Invoice and CreditNote | Prove each supported document type separately |

These cases extend qualification coverage; they do not duplicate the owning validation PRD or define a new validation endpoint.

## DTS and existing capability reuse

Assess existing DTS as the preferred transformation reuse candidate where transformation is needed, following [PRD-SEI-223](../../../prds/PRD-SEI-223-interoperability-routing-transformation.md). Obtain the deployed build and owner, input/output contracts, mapping versions, supported profiles, unsupported terms, error contract, capacity and operations evidence. Assess validation separately from transformation, even when one implementation supplies both.

Spain mappings and rule packs are evidence of their stated Spain scope. For UK or another country, record required changes and gaps before activation. Reuse of the proposed mapping/validation pattern does not establish that the current DTS implementation already supports a Peppol profile.

Open decisions: first global reference profile; UK profile after official selection; supported product/document cohorts; ownership of rule updates; exact artefact distribution and compatibility policy. Proposed owners: format/validation owner, DTS owner and country compliance owner.
