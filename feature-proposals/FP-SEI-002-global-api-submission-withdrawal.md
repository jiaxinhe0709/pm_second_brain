---
id: FP-SEI-002
title: Global API submission withdrawal — review proposal
type: feature-proposal
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-29
updated: 2026-10-29
reviewers: []
related:
  - SPEC-SEI-023
  - SPEC-SEI-024
  - SPEC-SEI-011
  - SPEC-SEI-013
  - SPEC-SEI-029
  - SPEC-SEI-041
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
---

# Global API submission withdrawal — review proposal

## Purpose and scope

An authorised business or accountant may need to withdraw an earlier public submission. [Sending OUT-SPFE-R02](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#4-shared-controls-and-spain-binding) already defines the functional boundary. The supplied Sage contracts do not establish how a product requests that action.

This separate proposal records the API gap for the sending author and API/Architecture owners. The sending specs remain unchanged while work continues on another branch. This is review input, not a replacement specification, approved endpoint or delivery commitment.

## Evidence and gap

SPFE defines `CancelInvoice` for permitted withdrawal of a submitted invoice. The supplied Sage lifecycle contract defines `POST /datasets/{datasetId}/e-invoices/{e-invoiceId}/status`, but documents no withdrawal action or cancellation response value. `Refused`, `Rejected` or a local status change cannot establish external withdrawal. SPFE-S03 §6.3; SPFE-S10; FR-LIF01.

Invoice withdrawal is separate from `CANCELPAYMENT`, `CANCELREJECTION`, `CANCELSETTLEMENT` and `CANCELDEFAULT`. Those retract earlier business reports and remain in [the lifecycle mapping](../specs/invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#spfe-action-mapping).

## Proposed direction and decisions

Assess a distinct withdrawal command within the existing Global API, following REF-GLOBAL. Spain is the only documented country use case in this assessment. Other countries/providers require their own capability and rule qualification.

| Review question | Recommendation / evidence needed | Accountable roles |
|---|---|---|
| Existing mechanism or new endpoint? | First assess whether the existing command mechanism supports withdrawal intent, an independent result and compatible responses. A possible alternative is `POST /datasets/{datasetId}/e-invoices/{e-invoiceId}/withdrawals`. This path is illustrative; no endpoint, payload or wire status is selected. | API, Architecture |
| What is withdrawn? | Bind the request to the earlier submission, original/copy purpose, represented business, environment and original destination. Confirm exact reference fields. Hold ambiguous targets and preserve unrelated delivery/copy results. Apply OUT-SPFE-R02. | Sending, API, Integration, Spain Compliance |
| What is shared? | Assess reuse of authority checks, duplicate prevention, operation receipts, audit, reads and events. Track request acceptance separately from external success. Actual implementation coverage is unknown. | API, Identity, Lifecycle, Operations |
| What stays in Spain? | Eligibility rules and the mapping to `CancelInvoice`. SPEC011 owns SOAP/ebMS/MIME, certificate/seal ports, faults and uncertain effects. Country rules must not enable withdrawal for another country/provider by default. | Spain Compliance, Public Integration |
| How is an uncertain result recovered? | Preserve the invoice, earlier evidence and original withdrawal attempt. After possible transmission, return an unresolved outcome and owner until qualified evidence establishes the result. Do not automatically resend the invoice or repeat withdrawal. | API, Public Integration, Operations |

## Review outcome and acceptance evidence

Before activation, obtain the selected contract/build and evidence for permitted, denied and unsupported requests; ambiguous targets; duplicate requests; and a lost external response. Prove separate withdrawal outcomes, preserved unrelated results and country/client isolation. Regress existing France statuses and consumers. These are checks to obtain, not completed tests. OUT-SPFE-A02/03; OUT-A16/21; SND-G02/04/05/07.

After the sending branch is reconciled, its author can incorporate the reviewed result into SPEC024's API assessment and existing gates. SPEC023 remains the functional authority; SPEC011 remains the SPFE transport authority. Lifecycle may reference the withdrawal outcome while retaining separate report-cancellation semantics. No integration into the sending files is made by this proposal.

## REF Source references

| ID | Original source / exact locator | Supported claim and limit |
|---|---|---|
| SPFE-S03 | [Service catalogue](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), version 0.1.0, 9 October 2026, §6.3 pp. 11–12 | Withdrawal purpose and business request/result description. Technical evidence; final legal eligibility remains governed by OUT-SPFE-R02 and its final BOE references. |
| SPFE-S10 | [CancelInvoice WSDL](<../context/WSDL servicios web - PRE_29:10:2026/CancelInvoice.wsdl>), reviewed local PRE release 29 October 2026; documentation, `CancelInvoicePortType`, binding/action and certificate/seal ports | Exact transport contract. Opaque attachments do not establish the complete business schema, Sage API support or safe repeats. |
| FR-LIF01 | [Sage status POST OpenAPI](<../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>), API 1.0.0, received 28 October 2026; `LifecycleChange-Document`, `InvoiceStatusRequest`, `InvoiceStatusResponse` | Existing status shape and documented values. Open attributes do not prove a withdrawal command or deployed Spain support. |
| REF-GLOBAL | [SPEC013](../specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md#2-proposed-api-decision-and-alternatives), draft updated 20 October 2026, Part 1 §2 | Shared Global API direction; does not approve a withdrawal endpoint. |
| REF-SENDING | [SPEC023](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#4-shared-controls-and-spain-binding), OUT-SPFE-R02 and OUT-SPFE-A02/03; [SPEC024](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#4-open-engineering-decisions), SND-G02/04/05/07; drafts updated 29 October 2026 | Existing behaviour, review gates and acceptance references; branch changes need reconciliation before incorporation. |
| REF-CONNECTOR | [SPEC011](../specs/SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding), draft updated 29 October 2026, PCN-SPFE-R01–04 | Shared transport and recovery design; implementation qualification remains open. |
