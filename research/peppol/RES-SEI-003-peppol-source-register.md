---
id: RES-SEI-003
title: Peppol global and UK source register
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - PRD-SEI-230
  - PRD-SEI-233
  - PRD-SEI-242
  - PRD-SEI-245
confluence:
  publish: false
  page_id: ""
---

# Peppol global and UK source register

Use these source IDs beside material external claims in this research pack. All sources were checked on 15 October 2026 unless an access limit says otherwise. A publication date, effective date and review date have different meanings. A live documentation URL must be rechecked before implementation or activation.

Final legislation establishes legal obligations. Official guidance explains policy or operation within its stated scope. A network specification establishes its own contract, not a national mandate. Repository PRDs establish product intent, not deployed capability.

## Global network sources

| ID | Original source and version | Exact section or element | Supported claim and limit |
|---|---|---|---|
| P01 | [OpenPeppol Interoperability Framework](https://peppol.org/learn-more/peppol-interoperability-framework/), live page; no version displayed | Governance framework; Authority Agreement; Service Provider Agreement; conceptual and technical models | Governance, four-corner roles, discovery and trust. Overview does not replace signed agreements or national rules. |
| P02 | [eDEC specification catalogue](https://docs.peppol.eu/edelivery/), last modified 2026-07-15 | Release/version and validity columns | SML 1.3.0, SMP 1.4.0, AS4 2.0.3, SBDH 2.0.2, identifier policy 4.4.0, MLS 1.1.0 and code lists 9.7. Catalogue identifies versions; linked contracts govern behaviour. |
| P03 | [SMP 1.4.0](https://docs.peppol.eu/edelivery/smp/Peppol-EDN-Service-Metadata-Publishing-1.4.0-2025-02-06.pdf), 2025-02-06; catalogue valid from 2025-11-01 | §2 discovery; §4.3 ServiceMetadata, pp. 13–18; §5.1 HTTPS, p. 21 | Document/process-specific metadata, multiple service endpoints and lookup HTTP outcomes. Does not define a provider's customer-registration API. |
| P04 | [Identifier policy 4.4.0](https://docs.peppol.eu/edelivery/policies/Peppol-EDN-Policy-for-use-of-identifiers-4.4.0-2025-02-06.pdf), 2025-02-06; catalogue valid from 2025-11-01 | “Participant Identifiers”, pp. 10–11; document and process identifier sections | Business-document identity and envelope participant identity need qualified association. Scheme presence does not establish country-mandate eligibility. |
| P05 | [Participant identifier schemes 9.7](https://docs.peppol.eu/edelivery/codelists/v9.7/Peppol%20Code%20Lists%20-%20Participant%20identifier%20schemes%20v9.7.html), catalogue valid from 2026-07-02 | `ICD Value`, `State`, `Registrable?`, structure and usage columns | Versioned scheme eligibility, including active `9932` GB:VAT and `0088` GLN. Not proof of a participant registration or final UK policy. |
| P06 | [BIS Billing 3.0](https://docs.peppol.eu/poacc/billing/3.0/bis/), May 2026 release | §§1, 12–15, profile, code lists, identifiers, UBL schemas and validation | Billing profile, UBL 2.1 Invoice/CreditNote and staged validation. Does not select the future UK profile. |
| P07 | [BIS Billing release notes](https://docs.peppol.eu/poacc/billing/3.0/release-notes/), 3.0.21; published 2026-05-20; mandatory from 2026-08-17 | Version 3.0.21, “Changes to BIS document” | Optional billing-with-response process and separate SMP registration. Optional profile does not mean every invoice receives business feedback. |
| P08 | [PINT Billing 1.1.3](https://docs.peppol.eu/poac/pint/pint/), released 2026-06-05 | Introductory model, transactions, compliance and specialisation links | Shared model for jurisdiction specialisations, with separate semantic, syntax and rule artefacts. Does not make different specialisations automatically interchangeable. |
| P09 | [MLS 1.1.0](https://docs.peppol.eu/edelivery/specs/mls/v1.1.0/mls/spec/), 2026-07-02 | §§2.1–2.3; §4 SBDH extension; §7.2 response codes | C3-to-C2 message and delivery evidence; `AB`, `AP`, `RE` meanings. Not buyer commercial acceptance. Usage duties also require current network policy. |
| P10 | [BIS Invoice Response 3.2](https://docs.peppol.eu/poacc/upgrade-3/profiles/63-invoiceresponse/), live profile | Response-code table and status advancement rules | Buyer processing responses, including `AP` approval and `PD` payment reporting. Does not prove bank settlement or actual counterparty support. |
| P11 | [OpenPeppol support guidance](https://peppol.org/support/) and [Testbed](https://www.testbed.peppol.org/), live pages | “Acceptance Testing - centralised testbed”, Functionality and Access; “Peppol Directory” | Successful accreditation tests support production PKI requests; testbed access uses a test certificate. Directory coverage can be incomplete. Testbed page text could not be parsed; authenticated suites and Sage results were not inspected. Some support-page rollout wording is undated; obtain current suite details before planning tests. |
| P12 | [Peppol Authorities](https://peppol.org/members/peppol-authorities/), live register | Jurisdiction headings; England entry; OpenPeppol fallback role | Authority inventory. England's NHS/SCCL entry does not establish the future UK-wide mandate authority. No named contacts are copied into the pack. |
| P13 | [BIS Billing artefact index](https://docs.peppol.eu/poacc/billing/3.0/), May 2026 release | Syntax, Rules, Code lists and Downloads | Published Schematron, schema links and examples. Availability is not evidence that Sage runs the same artefacts. |

## Country comparison sources

| ID | Original source and version | Exact section | Supported claim and limit |
|---|---|---|---|
| C01 | [ATO developer eInvoicing guidance](https://softwaredevelopers.ato.gov.au/eInvoicing), live page | Australian and New Zealand eInvoice specifications; Becoming an accredited service provider | A-NZ profile and local accreditation checks. No claim that general B2B use is mandatory. |
| C02 | [Japan Digital Agency JP PINT](https://www.digital.go.jp/policies/electronic_invoice), updated 2026-10-09; specification update 2026-06-08 | Overview and JP PINT Specifications | Digital Agency role and Japan-specific invoice, self-billing and non-tax-registered-business specifications. Japanese original governs; English analysis is a reading aid. |
| C03 | [Belgian official B2B FAQ](https://einvoice.belgium.be/en/FAQ/general-questions-b2b), live page | Questions 9, 14 and 18 | Scoped structured-invoice obligation from 2026-01-01, voluntary use and Peppol exchange context. Guidance is not a complete legal applicability assessment; exemptions and alternatives need separate qualification. |
| C04 | [IRAS GST InvoiceNow FAQ](https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/gst/frequently-asked-questions-for-gst-invoicenow-requirement.pdf?sfvrsn=fb2849aa_5), version 2026-04-16 | Opening scope, p. 1; §1.3, p. 5 | Phased tax-data submission and separation from ordinary customer exchange. This dated FAQ needs rechecking against current e-Tax guidance before a Singapore activation decision. |
| C05 | [Irish OGP supplier guidance](https://www.gov.ie/en/office-of-government-procurement/publications/suppliers-and-einvoicing/) | Peppol transmission for public procurement | Official search-index text corroborates the public-procurement use case. Full page retrieval failed; limited discovery lead, not a complete current contract or legal baseline. |

## UK sources

| ID | Original source and version | Exact section | Supported claim and limit |
|---|---|---|---|
| UK01 | [Tax update 2026](https://www.gov.uk/government/publications/summary-of-tax-update-2026-simplification-modernisation-and-fairness/tax-update-2026-simplification-modernisation-and-fairness-summary), updated 2026-06-23 | “E-invoicing: core interoperability network announcement” | Peppol direction; continued engagement on legacy systems. No final invoice profile or technical contract. |
| UK02 | [HMRC roadmap progress annex](https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/annex-summary-of-hmrcs-planned-activities-listed-in-this-transformation-roadmap-progress-update), updated 2026-07-27 | “Deliverable: E-Invoicing”, Description and 2026–2027 planned activity | April 2029 B2B/B2G VAT direction; full artefacts by end 2027–2028; roadmap planned at Budget 2026. Plans do not prove later milestones have completed. |
| UK03 | [Government consultation response](https://www.gov.uk/government/consultations/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector/outcome/promoting-electronic-invoicing-across-uk-businesses-and-the-public-sector-consultation-response), updated 2025-11-26 | Executive summary; §§2, 6 and 8; government response on real-time reporting | Structured-invoice policy direction; real-time reporting will not launch alongside the 2029 mandate. Consultation outcome is not final implementing law. |
| UK04 | [Cabinet Office electronic invoicing guidance](https://www.gov.uk/government/publications/procurement-act-2023-guidance-documents-manage-phase/guidance-electronic-invoicing-and-payment-html), updated 2026-07-20 | Paragraphs 3–5 and 11–17 | Explains section 67, required form and acceptance of undisputed public-contract invoices. Not a universal supplier Peppol mandate; contract and territorial applicability need review. |
| UK05 | [Procurement Act 2023, section 67](https://www.legislation.gov.uk/ukpga/2023/54/section/67) | Subsections (1)–(4), as identified by UK04 | Original legal reference. Direct and enacted-page retrieval failed; this pack relies on UK04 for the description and leaves original-text, commencement and territorial checks open. |
| UK06 | [NHS Supply Chain eDirect guidance](https://www.supplychain.nhs.uk/programmes/edirect-in-focus-a-project-designed-to-enhance-capability/), live page | “Third party P2P orders transmitted via PEPPOL” and “What are other NHS trusts doing?” | Existing four-corner exchange and AP context. Its loose cXML terminology is not adopted as a Peppol normative definition; programme guidance does not define the future UK mandate. |

## Evidence gaps and refresh rules

| Gap | Next evidence and proposed owner |
|---|---|
| UK final legal and technical contracts | UK compliance owner tracks final law, standards, scope, transition and governance. No claim here that an exhaustive legislative search has closed this gate. |
| UK Budget roadmap | UK policy owner checks the announced roadmap when published and reconciles it with UK01–UK03. No later roadmap was verified in this baseline. |
| Authority-specific agreements and current network policy | Network/legal owner obtains the applicable versions and exact service domains before conformance planning. Catalogue presence alone is insufficient. |
| Sage implementation and certification | AP engineering/security owners supply entity, build, environment, agreement, certificate metadata and accepted test evidence. No credentials or private keys belong here. |
| Country implementation coverage | Country owners qualify current laws, profiles, mappings and provider contracts. Authority-list presence is only discovery evidence. |

Refresh a source when its version changes, an effective date approaches, a contract changes or a new country/cohort is proposed. Record the resulting finding in the owning research document; do not maintain a second manual change log.
