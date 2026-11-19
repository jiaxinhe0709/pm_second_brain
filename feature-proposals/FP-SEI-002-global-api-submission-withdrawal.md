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

**PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026)** - Proposed paragraph replacement; existing wording retained below: ~~**Proposed direction:** the recommended option is a distinct issuer action on the existing e-invoice resource within the Global API, following REF-GLOBAL, subject to Architecture decision and design. Withdrawal is not an Article 10 lifecycle status. [SPEC-SEI-023 OUT-SPFE-R02](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#withdrawal-and-correction-boundaries) owns the eligibility evidence, proposed case classification, original/copy boundary and linked-instance safeguards. [SPEC-SEI-024 §2.4](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#24-proposed-withdrawal-interaction) assesses execution and recovery. Spain is the only documented country use case here; other countries/providers require separate qualification. SPFE-S02 Articles 3.5/5.5; ES-RD10.~~

> Replacement proposal: cancellation is an issuer action and a resulting invoice state. Sending owns the cancellation request, response and failure recovery using a status-update (cancellation) message carrying no invoice UBL; Lifecycle owns cancelled and its triggers. Cancellation and rectification are independent. Apply the [SPEC-SEI-023 proposed eligibility table](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#proposed-cancel-eligibility), including technical rejection, sent/pending, full/partial rejection, accepted, paid and cancelled. No endpoint, payload or new Article 10 report is selected. SD-CANCEL01 C-1/P-1/P-2.

> **PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026)** — Finality and numbering: AEAT retains as cancelled the document SPFE holds for that invoice: the original when the original passed through SPFE (direct submission, or a private platform submitting the original through SPFE), or the faithful copy when the original was exchanged only through private platforms. The fiscal number remains attached to that invoice: consumed, never reused. Cancelled invoices cannot be rectified or reactivated. The technical identifier capability described in catalogue §6.3.2 is separate and does not authorise fiscal-number reuse. This replaces reuse as intended behaviour in this proposal; struck text remains for comparison. SD-CANCEL01 C-2; SPFE-S03 §6.3.2.

> **PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026)** - Acceptance and action availability follow [SPEC-SEI-029 proposed Spain states](../specs/invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#proposed-spain-invoice-states). Keep four days as Solution Design input from the 16 November 2026 workshop, Xavier's slides, pending verification against SPFE-S02 Article 7 of the start event and calendar. Notify the issuer on acceptance by silence that cancellation is no longer available. SD-CANCEL01 P-2/P-3.

> **PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026)** - Cancellation requires BOTH an eligible state (sent/pending or fully rejected) AND an operation that did not take place. If the operation took place and fiscal content is wrong, rectify even when no response has arrived. Nestor's "Reject -> Cancel" choice is valid only when the operation did not take place. The [SPEC-SEI-023 table and examples](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#proposed-cancel-eligibility) own the rule; this marker also covers the replacement proposals in the review table. SPFE-S02 Articles 3.5/5.5; SD-CANCEL01.

| Review question | Proposal / open evidence needed | Accountable roles |
|---|---|---|
| Existing mechanism or new endpoint? | Recommended option: a distinct action on the existing resource. Alternatives: a flag on send or a new capability. Architecture owns the decision and technical design, including the command mechanism and independent result. No endpoint, payload, flag, field or wire status is approved. | Architecture, API |
| What is withdrawn? | ~~Apply OUT-SPFE-R02. Confirm how the contract binds the exact submission instance, original/copy purpose, represented business, environment and original destination. Qualify the §2.4 protection against stale/repeated cancellation after identifier reuse; the business identifier alone cannot distinguish instances.~~ Replacement proposal: Bind the exact earlier invoice, represented business, original/copy purpose, environment and destination. Keep its fiscal number consumed after cancellation; retain repeated/late-request protection without planning a later invoice with that number. SD-CANCEL01 C-2. | Sending, API, Integration, Spain Compliance |
| What is shared? | Assess reuse of authority checks, duplicate prevention, operation receipts, audit, reads and events. Track request acceptance separately from external success. Actual implementation coverage is unknown. | API, Identity, Lifecycle, Operations |
| What stays in Spain? | Eligibility rules and the mapping to `CancelInvoice`. SPEC011 owns SOAP/ebMS/MIME, certificate/seal ports, faults and uncertain effects. Country rules must not enable withdrawal for another country/provider by default. | Spain Compliance, Public Integration |
| How is an uncertain result recovered? | Qualify original-attempt observation, safe replay and concurrency under SND-G04/G05/G07. Without that evidence, §2.4 retains an unresolved outcome and owner; neither a repeated cancellation nor a new invoice resolves uncertainty. | API, Public Integration, Operations |
| Is withdrawal allowed after acceptance or payment? | ~~**Open:** obtain Compliance interpretation and AEAT behaviour, including existing reports, refunds and their association after identifier reuse. The reviewed evidence establishes neither a universal ban nor unrestricted permission. Do not infer eligibility from a lifecycle status alone.~~ Replacement proposal: Apply SPEC-SEI-023: cancellation is unavailable after explicit acceptance, acceptance by silence or payment. Even in an eligible state, require a nonexistent operation. If fiscal data for a real operation is wrong, use rectification under SPEC-SEI-015; do not cancel first. SD-CANCEL01 C-1/P-2; SPFE-S02 Articles 3.5/5.5. | Spain Compliance, ERP Product, AEAT liaison |
| What happens on a private route? | **Open:** qualify each provider's withdrawal support, authorised actor, recipient communication, public-copy action and independent results. A successful SPFE-copy withdrawal does not prove withdrawal of the private original. Do not assume the private platform already supports coordinated withdrawal. | Private-provider Integration, Operations, Spain Compliance |
| How is a copy changed to an interconnected original? | Article 5.5 second paragraph requires prior withdrawal of the stored copy. **Open:** qualify the authority, `CancelInvoice` binding, result and failure recovery for this separate procedure. Do not treat it as permission to cancel a business invoice for a real operation. | Spain Compliance, Public Integration, AEAT liaison |
| Are the public schema and result codes complete? | ~~**Open:** obtain and qualify the ApplicationResponse schema/mapping, original/copy targeting, DocumentStatus result/error codes, repeated-request behaviour and query visibility after cancellation and reuse. SPFE-S08 §5.3 is pending publication; the WSDL's opaque attachments are not a complete business contract.~~ Replacement proposal: Qualify cancellation of the exact original/copy, retained cancelled visibility, business results and repeated-request behaviour. Fiscal-number reuse is excluded. The WSDL does not establish a complete business contract. SD-CANCEL01 C-2; SPFE-S08 section 5.3; SPFE-S10. | Public Integration, DTS, API, AEAT liaison |
| What is required for VERI*FACTU? | **Open:** ERP and SIF Compliance must determine any separate billing-record cancellation/correction, numbering and reporting consequences. SPFE withdrawal proves no VERI*FACTU outcome and does not reverse ERP issuance. | SIF Compliance, ERP Product, Spain Compliance |

## Review outcome and acceptance evidence

**PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026)** - Proposed paragraph replacement; existing wording retained below: ~~Before activation, obtain the selected contract/build and execute [SPEC-SEI-023 OUT-SPFE-A02/03](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#6-functional-acceptance) and [SPEC-SEI-024 withdrawal qualification](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#5-api-qualification-checks). These include stale cancellation after identifier reuse, separate outcomes, country/client isolation and France compatibility. These are checks to obtain, not completed tests. SND-G04/05/07.~~

> Replacement acceptance proposal: use the proposed OUT-SPFE-A02/03 and SPEC-SEI-024 withdrawal checks for combined state/reason eligibility, retained cancelled history, consumed numbering and response-led recovery. Verify the five examples, technical representation-only same-number recovery versus fiscal rectification, issuer notification, optional rectification after partial rejection and country isolation. These are evidence to obtain, not completed tests. SD-CANCEL01; SND-G04/05/07.

SPEC-SEI-043 records the proposed API action without selecting fields or an endpoint. SPEC-SEI-011 remains the SPFE transport authority. SPEC-SEI-029/030 reference Sending and retain ownership of report cancellation.

## PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026): related conflicts retained for review

> The following table lists remaining source checks and terminology boundaries; the named source/companion files are unchanged. SD-CANCEL01; SPFE-S02 Articles 3.5/5.5.

| Repository evidence retained unchanged | Conflict / boundary to reconcile |
|---|---|
| [Original catalogue](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), v0.1.0, §§6.2.3/6.3.2 pp. 11–12; [RES-SEI-002 SPFE-Q08](../context/RES-SEI-002-spain-public-platform-technical-evidence.md#conflicts-and-missing-evidence). | The catalogue describes removal and technical identifier reuse after cancellation. C-2 requires retained cancelled history and permanent fiscal-number association. Preserve the original source and distinguish inactive availability, retained history and fiscal numbering. |
| [RES-SEI-002 Raw event codes and outcome meanings](../context/RES-SEI-002-spain-public-platform-technical-evidence.md#raw-event-codes-and-outcome-meanings); [PRD-SEI-224 Final public-order evidence](../prds/PRD-SEI-224-lifecycle-rejection-payment-reporting.md#final-public-order-evidence); [PRD-SEI-232 Final public-order evidence](../prds/PRD-SEI-232-country-lifecycle-status-mapping.md#final-public-order-evidence); [research/spain-public-platform-order-evidence.md, E-07](../research/spain-public-platform-order-evidence.md); [Spain use-case evidence UC1](../research/PRD-SEI-201-spain-use-case-evidence.md#use-cases-identified). | The four-day acceptance-by-silence proposal comes from the 16 November 2026 workshop, Xavier's slides. Verify its start event and calendar against SPFE-S02 Article 7. The recorded reviews do not establish the timer; keep the issuer notification as proposed. |
| [SPEC-SEI-005 UV-06](../specs/SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md#2-detailed-behaviour); [PRD-SEI-246 Agreed business boundaries / Decisions still to validate](../prds/PRD-SEI-246-spain-invoice-preparation-and-outbound-flow.md#agreed-business-boundaries); [PRD-SEI-103 Problem and business objective / Journeys 3–5](../prds/PRD-SEI-103-public-platform-invoice-submission.md#problem-and-business-objective); [PRD-SEI-212 corresponding sections](../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md#problem-and-business-objective). | Issued fiscal content remains immutable. The clarified proposal permits same-number resend only for sending/routing or format/UBL representation issues; errors in issued amounts, NIF or tax require a rectifying invoice. The PRDs retain earlier rejected-number questions. |
| [Selected CancelInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/CancelInvoice.wsdl>), manifest-selected PRE release 29 October 2026, documentation and operation; [SPEC-SEI-011 SPFE source contract binding](../specs/SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding). | Cancellation is a status-update (cancellation) message carrying no invoice UBL. The public contract documents UBL business attachments; qualify the cancellation-specific business document separately. This clarification does not add an invoice file or define a new payload. |
| [PRD-SEI-103 Journey 12](../prds/PRD-SEI-103-public-platform-invoice-submission.md#journey-12--withdraw-or-correct-an-improper-admitted-invoice); [PRD-SEI-212 Journey 12](../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md); [PRD-SEI-201 Additional Spain use-case coverage](../prds/PRD-SEI-201-public-private-platform-transition.md#additional-spain-use-case-coverage); [PRD-SEI-213 corresponding coverage](../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md#additional-spain-use-case-coverage); [SPEC-SEI-007 archive OUT-05/06](../specs/archive/SPEC-SEI-007-invoice-sending-solution.md); [Spain use-case evidence UC7](../research/PRD-SEI-201-spain-use-case-evidence.md#use-cases-identified). | Earlier “credit note/corrective invoice” wording does not express C-5's ERP-label mapping precisely. Historical/generated views can carry the same wording. Preserve exact API document values; the proposed glossary and SPEC-SEI-015 own the Spain business meaning. |

## REF Source references

| ID | Original source / exact locator | Supported claim and limit |
|---|---|---|
| **PROPOSED (Solution Design: Samu Coco / Jiaxin He, 18 Nov 2026)** - SD-CANCEL01 | Solution Design input supplied for this review; attribution 18 November 2026. C-1 to C-5 are confirmed task input; P-1 to P-4 are Solution Design proposals to record, not reopen. C-2 is attributed by Samu to Ronald Lozano Manzi; C-5 reports Nestor's ERP FigJam working design, with Reject -> Cancel limited to a nonexistent operation. Four days for acceptance by silence comes from the 16 November 2026 workshop, Xavier's slides; verify the start event and calendar against SPFE-S02 Article 7. Current review clarifies state plus reason, representation-only same-number recovery and the cancellation status-update message. | Product cancellation/finality, independent rectification, eligibility, ownership and notification. No original discussion/FigJam file, legal four-day timer, new interface or deployed capability is established by this source. |
| SPFE-S02 | [Final Order HAC/1028/2026](<../context/BOE-A-2026-20587.pdf>), published 5 October 2026; Article 3.5, Article 5.5 second and final paragraphs, Annex I withdrawal table pp. 28–29 | Nonexistent-operation withdrawal of originals/copies with traceability; separate copy-to-original transition and withdrawal data. Does not select a Sage endpoint or prove safe replay. |
| ES-RD10 | [Original RD 238/2026](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-7295), published 31 March 2026; Article 10.1–10.2 | Recipient lifecycle statuses; invoice-submission withdrawal is not one of the listed statuses. |
| SPFE-S03 | [Service catalogue](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), version 0.1.0, 9 October 2026, §6.3 pp. 11–12 | Withdrawal purpose and business request/result description. Technical evidence; final legal eligibility remains governed by OUT-SPFE-R02 and its final BOE references. |
| SPFE-S08 | [Input/output formats](<../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), draft 0.1.0, 9 October 2026; §5.3 p. 14 | Cancellation section remains pending publication; not evidence of a complete executable business contract. |
| SPFE-S10 | [CancelInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/CancelInvoice.wsdl>), reviewed local PRE release 29 October 2026; documentation, `CancelInvoicePortType`, binding/action and certificate/seal ports | Exact transport contract. Opaque attachments do not establish the complete business schema, Sage API support or safe repeats. |
| FR-LIF01 | [Sage status POST OpenAPI](<../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>), API 1.0.0, received 28 October 2026; `LifecycleChange-Document`, `InvoiceStatusRequest`, `InvoiceStatusResponse` | Existing status shape and documented values. Open attributes do not prove a withdrawal command or deployed Spain support. |
| REF-GLOBAL | [SPEC013](../specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md#2-proposed-api-decision-and-alternatives), draft updated 20 October 2026, Part 1 §2 | Shared Global API direction; does not approve a withdrawal endpoint. |
| REF-SENDING | [SPEC-SEI-023](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#withdrawal-and-correction-boundaries), OUT-SPFE-R02 and OUT-SPFE-A02/03; [SPEC-SEI-024](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#24-proposed-withdrawal-interaction), §2.4 and SND-G04/05/07; drafts updated 12 November 2026 | Proposed functional boundaries, interaction and qualification checks, subject to Architecture decision; no implementation or endpoint approval. |
| REF-CONNECTOR | [SPEC011](../specs/SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding), draft updated 29 October 2026, PCN-SPFE-R01–04 | Shared transport and recovery design; implementation qualification remains open. |
