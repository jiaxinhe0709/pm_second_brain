---
id: FP-SEI-002
title: Global API submission withdrawal — review proposal
type: feature-proposal
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-29
updated: 2026-11-12
reviewers: []
related:
  - SPEC-SEI-023
  - SPEC-SEI-024
  - SPEC-SEI-011
  - SPEC-SEI-013
  - SPEC-SEI-029
  - SPEC-SEI-030
  - SPEC-SEI-041
  - SPEC-SEI-043
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
---

# Global API submission withdrawal — review proposal

## Purpose and scope

An authorised business or accountant may need to withdraw an earlier public submission. [SPEC-SEI-023 OUT-SPFE-R02](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#withdrawal-and-correction-boundaries) defines the functional boundary. The supplied Sage contracts do not establish how a product requests that action.

This proposal records the Product analysis, proposed approach and open questions. Architecture owns the final decision and technical design. SPEC-SEI-023 owns the logical proposal; SPEC-SEI-024 owns the interaction and reuse assessment. The proposal does not approve an endpoint, wire contract, implementation or delivery commitment.

## Evidence and gap

SPFE defines `CancelInvoice` for permitted withdrawal of a submitted invoice. The supplied Sage lifecycle contract defines `POST /datasets/{datasetId}/e-invoices/{e-invoiceId}/status`, but documents no withdrawal action or cancellation response value. `Refused`, `Rejected` or a local status change cannot establish external withdrawal. SPFE-S03 §6.3; SPFE-S10; FR-LIF01.

Invoice withdrawal is separate from `CANCELPAYMENT`, `CANCELREJECTION`, `CANCELSETTLEMENT` and `CANCELDEFAULT`. Those retract earlier business reports and remain in [the lifecycle mapping](../specs/invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#spfe-action-mapping).

## Analysis and proposed direction

**Proposed direction:** the recommended option is a distinct issuer action on the existing e-invoice resource within the Global API, following REF-GLOBAL, subject to Architecture decision and design. Withdrawal is not an Article 10 lifecycle status. [SPEC-SEI-023 OUT-SPFE-R02](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#withdrawal-and-correction-boundaries) owns the eligibility evidence, proposed case classification, original/copy boundary and linked-instance safeguards. [SPEC-SEI-024 §2.4](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#24-proposed-withdrawal-interaction) assesses execution and recovery. Spain is the only documented country use case here; other countries/providers require separate qualification. SPFE-S02 Articles 3.5/5.5; ES-RD10.

| Review question | Proposal / open evidence needed | Accountable roles |
|---|---|---|
| Existing mechanism or new endpoint? | Recommended option: a distinct action on the existing resource. Alternatives: a flag on send or a new capability. Architecture owns the decision and technical design, including the command mechanism and independent result. No endpoint, payload, flag, field or wire status is approved. | Architecture, API |
| What is withdrawn? | Apply OUT-SPFE-R02. Confirm how the contract binds the exact submission instance, original/copy purpose, represented business, environment and original destination. Qualify the §2.4 protection against stale/repeated cancellation after identifier reuse; the business identifier alone cannot distinguish instances. | Sending, API, Integration, Spain Compliance |
| What is shared? | Assess reuse of authority checks, duplicate prevention, operation receipts, audit, reads and events. Track request acceptance separately from external success. Actual implementation coverage is unknown. | API, Identity, Lifecycle, Operations |
| What stays in Spain? | Eligibility rules and the mapping to `CancelInvoice`. SPEC011 owns SOAP/ebMS/MIME, certificate/seal ports, faults and uncertain effects. Country rules must not enable withdrawal for another country/provider by default. | Spain Compliance, Public Integration |
| How is an uncertain result recovered? | Qualify original-attempt observation, safe replay and concurrency under SND-G04/G05/G07. Without that evidence, §2.4 retains an unresolved outcome and owner; neither a repeated cancellation nor a new invoice resolves uncertainty. | API, Public Integration, Operations |
| Is withdrawal allowed after acceptance or payment? | **Open:** obtain Compliance interpretation and AEAT behaviour, including existing reports, refunds and their association after identifier reuse. The reviewed evidence establishes neither a universal ban nor unrestricted permission. Do not infer eligibility from a lifecycle status alone. | Spain Compliance, ERP Product, AEAT liaison |
| What happens on a private route? | **Open:** qualify each provider's withdrawal support, authorised actor, recipient communication, public-copy action and independent results. A successful SPFE-copy withdrawal does not prove withdrawal of the private original. Do not assume the private platform already supports coordinated withdrawal. | Private-provider Integration, Operations, Spain Compliance |
| How is a copy changed to an interconnected original? | Article 5.5 second paragraph requires prior withdrawal of the stored copy. **Open:** qualify the authority, `CancelInvoice` binding, result and failure recovery for this separate procedure. Do not treat it as permission to cancel a business invoice for a real operation. | Spain Compliance, Public Integration, AEAT liaison |
| Are the public schema and result codes complete? | **Open:** obtain and qualify the ApplicationResponse schema/mapping, original/copy targeting, DocumentStatus result/error codes, repeated-request behaviour and query visibility after cancellation and reuse. SPFE-S08 §5.3 is pending publication; the WSDL's opaque attachments are not a complete business contract. | Public Integration, DTS, API, AEAT liaison |
| What is required for VERI*FACTU? | **Open:** ERP and SIF Compliance must determine any separate billing-record cancellation/correction, numbering and reporting consequences. SPFE withdrawal proves no VERI*FACTU outcome and does not reverse ERP issuance. | SIF Compliance, ERP Product, Spain Compliance |

## Review outcome and acceptance evidence

Before activation, obtain the selected contract/build and execute [SPEC-SEI-023 OUT-SPFE-A02/03](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#6-functional-acceptance) and [SPEC-SEI-024 withdrawal qualification](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#5-api-qualification-checks). These include stale cancellation after identifier reuse, separate outcomes, country/client isolation and France compatibility. These are checks to obtain, not completed tests. SND-G04/05/07.

SPEC-SEI-043 records the proposed API action without selecting fields or an endpoint. SPEC-SEI-011 remains the SPFE transport authority. SPEC-SEI-029/030 reference Sending and retain ownership of report cancellation.

## REF Source references

| ID | Original source / exact locator | Supported claim and limit |
|---|---|---|
| SPFE-S02 | [Final Order HAC/1028/2026](<../context/BOE-A-2026-20587.pdf>), published 5 October 2026; Article 3.5, Article 5.5 second and final paragraphs, Annex I withdrawal table pp. 28–29 | Nonexistent-operation withdrawal of originals/copies with traceability; separate copy-to-original transition and withdrawal data. Does not select a Sage endpoint or prove safe replay. |
| ES-RD10 | [Original RD 238/2026](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-7295), published 31 March 2026; Article 10.1–10.2 | Recipient lifecycle statuses; invoice-submission withdrawal is not one of the listed statuses. |
| SPFE-S03 | [Service catalogue](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), version 0.1.0, 9 October 2026, §6.3 pp. 11–12 | Withdrawal purpose and business request/result description. Technical evidence; final legal eligibility remains governed by OUT-SPFE-R02 and its final BOE references. |
| SPFE-S08 | [Input/output formats](<../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), draft 0.1.0, 9 October 2026; §5.3 p. 14 | Cancellation section remains pending publication; not evidence of a complete executable business contract. |
| SPFE-S10 | [CancelInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/CancelInvoice.wsdl>), reviewed local PRE release 29 October 2026; documentation, `CancelInvoicePortType`, binding/action and certificate/seal ports | Exact transport contract. Opaque attachments do not establish the complete business schema, Sage API support or safe repeats. |
| FR-LIF01 | [Sage status POST OpenAPI](<../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>), API 1.0.0, received 28 October 2026; `LifecycleChange-Document`, `InvoiceStatusRequest`, `InvoiceStatusResponse` | Existing status shape and documented values. Open attributes do not prove a withdrawal command or deployed Spain support. |
| REF-GLOBAL | [SPEC013](../specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md#2-proposed-api-decision-and-alternatives), draft updated 20 October 2026, Part 1 §2 | Shared Global API direction; does not approve a withdrawal endpoint. |
| REF-SENDING | [SPEC-SEI-023](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#withdrawal-and-correction-boundaries), OUT-SPFE-R02 and OUT-SPFE-A02/03; [SPEC-SEI-024](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#24-proposed-withdrawal-interaction), §2.4 and SND-G04/05/07; drafts updated 12 November 2026 | Proposed functional boundaries, interaction and qualification checks, subject to Architecture decision; no implementation or endpoint approval. |
| REF-CONNECTOR | [SPEC011](../specs/SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding), draft updated 29 October 2026, PCN-SPFE-R01–04 | Shared transport and recovery design; implementation qualification remains open. |
