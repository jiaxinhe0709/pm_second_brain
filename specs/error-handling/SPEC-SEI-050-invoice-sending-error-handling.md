---
id: SPEC-SEI-050
title: Invoice Sending Error Handling
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
  - SPEC-SEI-023
  - SPEC-SEI-024
  - SPEC-SEI-043
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Invoice Sending Error Handling

## 1 Purpose and authoritative rules

Support must identify which sending action failed, establish its actual effect and recover only that action. [SPEC023 activities OUT-08–15](../invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md#3-process-and-activity-order) own execution, outcomes and recovery. [SPEC024](../invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md) and [SPEC043](../invoice-sending/api-reference/SPEC-SEI-043-invoice-sending-api-reference.md) retain contract qualification.

Apply [SPEC048 OPS-R01–09 — common operational requirements](SPEC-SEI-048-shared-error-handling-and-operational-support.md#2-common-operational-requirements) and the stage-specific operational requirements below. ERR-S01/02.

## 2 Failure investigation and permitted recovery

| ID / condition | Evidence visible to authorised Support/Engineering | Permitted next action and owner |
|---|---|---|
| ERR-SND-01 Validation, route or trust check blocks sending | Show exact invoice revision, selected sender/recipient platforms, failed prerequisite, validation issues and whether external execution started. | Customer, Trust or Routing owner resolves the named check under OUT-08–11. A corrected issued invoice follows the owning correction rule. |
| ERR-SND-02 Submission times out or local result is lost | Show original action/attempt, identifiers, payload hash, route, transmission evidence, response levels and current reconciliation. Do not display an unevidenced “not sent”. | API/Integration owner applies OUT-13 using original-operation evidence; unsafe repeat remains unavailable. |
| ERR-SND-03 Delivery succeeds; public copy or PDF fails | Show independent recipient-delivery, copy and PDF results, each executor and missing report/error evidence. | Recover only the outstanding action under OUT-12–15/OUT-PDF-R02. Where the private provider owns the copy, escalate there; Sage must not add a second sender. |
| ERR-SND-04 Attempt ends in ERROR or notification is missed | Show the matching history attempt, operationStatus/errorCode where supported, current invoice status and evidence freshness. | Follow the qualified code-specific owner in INT-ERR01/SPEC024. A missing callback or failed attempt cannot itself justify a fresh invoice submission. |
| ERR-SND-05 Invoice cancellation is refused or uncertain | Show exact earlier invoice/action, original/copy role, eligibility evidence, response and any unresolved attempt. | Apply SPEC023 withdrawal/correction boundaries and cancellation eligibility. Sending owner reconciles the exact cancellation; do not repeat sending or a lifecycle report as repair. |
| ERR-SND-06 Incident affects a batch or automatic sending | Search by dataset, route, time, invoice/error status and external reference. Preserve per-invoice and per-action progress. | Operations uses OPS-R07 on eligible failed actions only; completed invoices/actions stay outside the recovery selection. |

Use [SPEC011 — SPFE response and error matrix](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix) for source-dependent classifications. Keep exact source codes and their operation/version bindings. INT-ERR01 applies only where its selected contract is qualified. Neither a message-resource key nor an HTTP status alone proves the external effect or safe replay. ERR-S02–04.

## 3 Spain use and reuse qualification

Use in Spain covers public delivery and enabled private routes. Independent results and original-attempt recovery are shared design patterns. Spain routing, public-copy and cancellation rules need Spain binding; provider retry/report contracts need local qualification. Actual support-tool and sending-build coverage is unknown. Existing DTS remains the preferred transformation candidate under SPEC049; sending recovery cannot silently regenerate or replace issued bytes.

## 4 Acceptance and open decisions

Exercise ERR-SND-02/03 with accepted private delivery and lost public-copy evidence; verify that only the outstanding action is eligible. Exercise ERR-SND-04 with ERROR on a history attempt while the invoice snapshot remains Submitted. Exercise ERR-SND-05/06 with an uncertain cancellation, a completed invoice and revoked authority in a bulk selection. Apply [OPS-A01–05 common checks](SPEC-SEI-048-shared-error-handling-and-operational-support.md#5-acceptance-and-open-gates), including country-rule isolation and qualification of actual implementation reuse. These are required acceptance scenarios, not executed implementation tests. ERR-S01/02.

SND-G04/05/07/09 remain open for replay/reconciliation semantics, provider-owned copy errors, original-attempt correlation and the selected connection model. API/Integration and provider owners supply evidence; Operations qualifies runbooks and bulk actions. Cancellation wire support remains unqualified. Portal controls cannot close these gates.

## REF Source references

| ID | Source/version and exact location | Supported claim and limit |
|---|---|---|
| ERR-S01 | Functional and API owner documents linked in §1; repository drafts read 23 November 2026; activity/requirement IDs named in §2. | Canonical stage behaviour and open gates. This view adds operational inspection, not a new external contract or lifecycle rule. |
| ERR-S02 | [SPEC048 source register](SPEC-SEI-048-shared-error-handling-and-operational-support.md#ref-source-references), OPS-S01–04; stakeholder note received 23 November 2026; PRD107/215/225 and INT-ERR01. | Product and operational evidence for support requests; stakeholder reported limitations and FR support do not prove Spain implementation. |
| ERR-S03 | [SendInvoice.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/SendInvoice.wsdl>); [CancelInvoice.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/CancelInvoice.wsdl>); reviewed local PRE release 23 November 2026; `wsdl:portType/operation`, binding and service ports. | Exact named operations and transport evidence only. No universal replay, complete business-result or production-support claim. |
| ERR-S04 | [SPEC011 — complete business/technical mapping](../SPEC-SEI-011-public-platform-connector-solution-specification.md#business-and-technical-error-mapping); [original business messages](<../../context/Listados códigos de error/errores_negocio.properties>) and [original technical messages](<../../context/Listados códigos de error/errores_tecnicos.properties>), SPFE-S28/S29 received 23 November 2026, active message keys/templates; [release review](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026). | Message templates and proposed handling only; actual wire-code, field and operation bindings remain unqualified under SPFE-Q20/Q21. Do not copy another operation's meaning or retry rule. |
