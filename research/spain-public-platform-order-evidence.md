---
id: RES-SEI-001
title: Spain public platform order — retrieval and download evidence
type: research
status: draft
owner: TBD — Spain Compliance and Public Platform Technical Owners
created: 2026-10-06
updated: 2026-10-06
---

# Spain public platform order — retrieval and download evidence

This supporting evidence note records the supplied **Order HAC/1028/2026**, dated 2 October and published on 5 October 2026. Its identity and publication details were checked against the [official BOE publication](https://www.boe.es/eli/es/o/2026/10/02/hac1028) on 6 October 2026. This is the final published order, replacing the April draft as the regulatory source for the affected requirements. It is not a complete production API contract.

## Source and provenance

- [XML snapshot](../assets/regulatory/spain/BOE-A-2026-20587.xml): user-supplied BOE XML, with only the browser's introductory display message removed. The XML parses successfully. No text within the document was rewritten.
- BOE identifier: `BOE-A-2026-20587`; publication: issue 247, pages 129349–129390; XML update attribute: `20261005112601`.
- SHA-256 of the saved UTF-8 XML: `636c666e6d73f826626595bc07f3daf60b33478d8647f865b3e0a66c75fc1076`. This identifies this local snapshot; it does not prove byte equality with a separately downloaded BOE file.
- [Official text](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20587&lang=es) and [official PDF](https://www.boe.es/boe/dias/2026/10/05/pdfs/BOE-A-2026-20587.pdf).
- The final provision states entry into force on the day after publication. This starts the referenced staged application periods; it does not make all customer obligations immediately applicable. Compliance owns the detailed applicability calendar.

## Findings and their limits

| ID | Confirmed from the supplied order | Product or design consequence | Still open |
|---|---|---|---|
| E-01 | Article 9.1–9.2 requires the relevant private platforms to recover exchanged invoice messages and automate retrieval of invoices received by their customers. | Automated retrieval is required for this operating model. Customer login cannot be the only trigger. | Sage's selected operator model, discovery operations, notifications, cadence, limits and pagination. |
| E-02 | Article 9.2 requires recovered invoices to be made available immediately to customers for conservation. Article 9.3 allows recipients to recover invoices at any time, directly or automatically. | Separate durable source-file availability from successful ERP processing. Define a secure conservation-access path even if mapping or ERP delivery is delayed. | Compliance's interpretation of immediate availability, service target, records duties and handling of unsafe files. |
| E-03 | Article 10 provides web-service and form access to invoices and faithful copies, plus consultation of states and payments. Technical conditions are delegated to AEAT's electronic office. | Distinguish retrieval, file download and status consultation. Do not infer one combined API. | Exact operations, schemas, identity fields, filters, retention and side effects. |
| E-04 | Article 11 requires accepted certificates. Third-party access to Article 9 recovery and Article 10 consultation requires registered power of attorney, through automated/web-service access as well as forms. | Check legal authority separately from transport authentication, for the represented legal entity and action. | Required AEAT authorisation procedure/code, verification and revocation contract, and whether one request can span represented entities. |
| E-05 | Articles 3–4 require EN 16931/UBL public invoices and identify faithful copies as copies; embedded files are prohibited. | Keep received structured bytes and copy classification. A rendering is a derived file. | Exact UBL version/profile, schemas and technical representation of the copy indicator. The order does not establish UBL 2.5 acceptance. |
| E-06 | Article 6 defines the invoice code using issuer NIF, series, number and issue date. | Preserve the provider identity and these business identity elements. | Exact encoding, separators, normalisation and collision handling in the published technical contract. |
| E-07 | Article 7.1 provides presumed acceptance where there is no rejection or later rectifying invoice. | Show this as a derived legal view. File download, technical receipt and an explicit customer acceptance remain distinct. | Lifecycle precedence and the approved country rule pack. This is not a four-day automatic-acceptance timer. |
| E-08 | Article 5 defines validation, admitted/rejected results, receipt evidence, duplicate cases and a technical-outage provision for sending. | Submission must follow the final order, with reconciliation before unsafe repeat or copy withdrawal. | Technical schemas/error catalogue and operational interpretation. Sending outage rules must not become retrieval deadlines. |

## What “bulk download” could mean

1. **Automated collection of many received invoices over time:** required retrieval capability; the API may still require individual entity scopes and paginated or individual file requests.
2. **One AEAT request across several customers:** unconfirmed. Accountants or shared credentials do not remove each customer's authority boundary.
3. **A customer selecting many stored invoices and receiving a ZIP/export:** a separate product option. Keep it outside the initial proposed scope until demand, cost, security and retention are assessed.

The absence of a France feature and the expected size of Spanish customers are stakeholder hypotheses, not evidence that a Spanish obligation can be removed. Product should obtain usage and customer evidence before deciding on a multi-file export.

## Targeted consistency review

| Canonical document | Update in this pass | Remaining gate / owner |
|---|---|---|
| [PRD-SEI-211](../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md) | Final evidence, automated recovery, conservation availability, authority and distinct bulk questions. | Discovery/API contract, availability target and records policy / Spain Technical Owner, Compliance, Product and Records Owner. |
| [PRD-SEI-212](../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md) | Replaces draft-order evidence with final Articles 3–6. | Full annex/schema mapping and safe copy-withdrawal procedure / Submission Owner. |
| [PRD-SEI-221](../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md) | Records final publication and applicability-calendar gate. | Approve staged dates and operator responsibilities / Compliance. |
| [PRD-SEI-226](../prds/PRD-SEI-226-security-trust-identity-data-audit.md) | Adds Article 11 authority requirements for recovery/consultation. | Carry authority scope into onboarding and certificate implementation contracts / Security and Spain Technical Owner. |
| [PRD-SEI-236](../prds/PRD-SEI-236-ubl-format-profile.md) | Adds final public UBL and copy evidence without declaring version acceptance. | Annex mapping and exact active profile / Format Owner. |
| [PRD-SEI-224](../prds/PRD-SEI-224-lifecycle-rejection-payment-reporting.md), [PRD-SEI-232](../prds/PRD-SEI-232-country-lifecycle-status-mapping.md) | Clarifies presumed acceptance and final-order status catalogue dependency. | Annex II mapping, timing and country rule approval / Lifecycle Owner and Compliance. |
| [SPEC-SEI-006](../specs/SPEC-SEI-006-invoice-receiving-solution.md) | Uses PRD-SEI-211 as current retrieval authority; links the separate retrieval/storage/download design. | Final integration contracts / Receiving and Retrieval Owners. |
| [SPEC-SEI-010](../specs/SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md) | New logical proposal for retrieval, source storage and authorised file access. | Named design gates in Part 4. |

PRD-SEI-102 and PRD-SEI-103 are preserved predecessors. This targeted pass is not a full legal review of every Spain document or an approval of the existing specs. Onboarding, certificates, outbound and lifecycle designs must consume the approved country contracts before production.
