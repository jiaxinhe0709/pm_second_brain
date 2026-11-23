---
id: SPEC-SEI-051
title: Invoice Receiving and Retrieval Error Handling
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-11-23
updated: 2026-11-23
reviewers: []
related:
  - SPEC-SEI-048
  - PRD-SEI-215
  - PRD-SEI-225
  - SPEC-SEI-026
  - SPEC-SEI-027
  - SPEC-SEI-042
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Invoice Receiving and Retrieval Error Handling

## 1 Purpose and authoritative rules

Support must distinguish collection, source-file capture, original recovery, safe viewing/download and ERP delivery. [SPEC026 §3](../invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#3-process-and-activity-order) owns their behaviour and selected copy-only policy. [SPEC027](../invoice-receiving/SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md) and [SPEC042](../invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md) retain contracts and coverage gaps.

Apply [SPEC048 OPS-R01–09 — common operational requirements](SPEC-SEI-048-shared-error-handling-and-operational-support.md#2-common-operational-requirements) and the stage-specific operational requirements below. ERR-S01/02.

## 2 Failure investigation and permitted recovery

| ID / condition | Evidence visible to authorised Support/Engineering | Permitted next action and owner |
|---|---|---|
| ERR-RCV-01 Collection or status read fails | Show source, requested range/page, saved progress, last successful observation and any coverage gap. Distinguish no results from failed/incomplete collection. | Retrieval owner follows SPEC026 §3.3 and RSD-03/06/08; a failed page cannot advance completed progress. |
| ERR-RCV-02 File is missing, partial or inaccessible | Show file/source role, available verified bytes, refusal/expiry evidence and unfinished capture. | Integration/Records owner recovers the missing file or authorised link under RSD-04/PRI-01–03. Do not refetch complete files because later ERP processing failed. |
| ERR-RCV-03 Only a faithful copy is available | Show original-recovery status, recipient setup/access, attempted source, copy label and unresolved matching evidence. | Follow SPEC026 original-file retrieval: restore recipient access, check the receiving provider, then request sender help if needed. ERP delivery remains governed by the selected original-file policy; safe copy access stays separate. |
| ERR-RCV-04 Wrong recipient, unsafe file, validation or duplicate conflict | Show restricted diagnostic references, identity/role conflict and failed checks without revealing another client's content. | Receiving/Security/Format owner resolves RCV-02–05/09. Retry cannot override access, safety or conflicting business identity. |
| ERR-RCV-05 Conversion or ERP handoff fails | Show saved source, processing revision, conversion applicability, delivery ID and ERP acknowledgement separately. | Resume the affected RCV-06/07/09 checkpoint. Transformation recovery uses SPEC049. ERP-specific bookkeeping/import failures belong to the local product; do not repeat source capture or create duplicate ERP invoices. |
| ERR-RCV-06 Download, event or source-confirmation result is lost | Show exact file/download, event, source acknowledgement and original attempt evidence; distinguish invoice files from lifecycle-document failures. | Owner follows RSD-07/RCV-08/09 and qualified INT-ERR01 handling. Bulk recovery under OPS-R07 selects the exact failed read, capture or handoff, not all processing for an invoice. |

Use [SPEC011 — SPFE response and error matrix](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix) for source-dependent classifications. Keep exact source codes and their operation/version bindings. INT-ERR01 applies only where its selected contract is qualified. Neither a message-resource key nor an HTTP status alone proves the external effect or safe replay. ERR-S02–04.

## 3 Spain use and reuse qualification

Use in Spain covers public collection and enabled private receipt/view/download. Capture checkpoints, protected file access and stable ERP delivery are reusable design patterns. Spain original/copy policy and provider transfer/acknowledgement semantics need separate binding. Actual build and support-tool coverage is unknown. Existing DTS is the preferred conversion candidate only within SPEC026 RCV-06: Phase 3 non-UBL 2.5 input. This document adds no conversion to Phases 1–2.

## 4 Acceptance and open decisions

Exercise ERR-RCV-01 with a failed middle page and an empty successful query. Exercise ERR-RCV-02/03 with a saved copy, failed private original retrieval and later restored access; reapply intake/matching checks. Exercise ERR-RCV-04–06 with another-client content, a lost ERP acknowledgement and expired download access without repeating completed capture. Apply [OPS-A01–05 common checks](SPEC-SEI-048-shared-error-handling-and-operational-support.md#5-acceptance-and-open-gates), including country-rule isolation and qualification of actual implementation reuse. These are required acceptance scenarios, not executed implementation tests. ERR-S01/02.

RET-G01/04/07/09/10 retain identity, file-role, mapping, repeat-handling and provider download evidence. Receiving/API owners must qualify original recovery triggers, copy/original matching and source acknowledgements. Local ERP owners must define journal/supplier-invoice/delivery-note import diagnostics. Operations/Product decide portal recovery scope and collection thresholds.

## REF Source references

| ID | Source/version and exact location | Supported claim and limit |
|---|---|---|
| ERR-S01 | Functional and API owner documents linked in §1; repository drafts read 23 November 2026; activity/requirement IDs named in §2. | Canonical stage behaviour and open gates. This view adds operational inspection, not a new external contract or lifecycle rule. |
| ERR-S02 | [SPEC048 source register](SPEC-SEI-048-shared-error-handling-and-operational-support.md#ref-source-references), OPS-S01–04; stakeholder note received 23 November 2026; PRD107/215/225 and INT-ERR01. | Product and operational evidence for support requests; stakeholder reported limitations and FR support do not prove Spain implementation. |
| ERR-S03 | [GetRegisteredInvoice.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/GetRegisteredInvoice.wsdl>); [GetInvoices.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/GetInvoices.wsdl>); [DownloadInvoicesByID.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/DownloadInvoicesByID.wsdl>); [DownloadInvoicesByLOC.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/DownloadInvoicesByLOC.wsdl>); reviewed local PRE release 23 November 2026; `wsdl:portType/operation`, binding and service ports. | Exact named operations and transport evidence only. No universal replay, complete business-result or production-support claim. |
| ERR-S04 | [SPEC011 — complete business/technical mapping](../SPEC-SEI-011-public-platform-connector-solution-specification.md#business-and-technical-error-mapping); [original business messages](<../../context/Listados códigos de error/errores_negocio.properties>) and [original technical messages](<../../context/Listados códigos de error/errores_tecnicos.properties>), SPFE-S28/S29 received 23 November 2026, active message keys/templates; [release review](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026). | Message templates and proposed handling only; actual wire-code, field and operation bindings remain unqualified under SPFE-Q20/Q21. Do not copy another operation's meaning or retry rule. |
