---
id: SPEC-SEI-052
title: Invoice Lifecycle and Reporting Error Handling
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
  - SPEC-SEI-029
  - SPEC-SEI-030
  - SPEC-SEI-041
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Invoice Lifecycle and Reporting Error Handling

## 1 Purpose and authoritative rules

Support must distinguish the invoice's business facts, transition attempts and each external reporting obligation. [SPEC029 requirements and invariants](../invoice-lifecycle/SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#4-functional-requirements-and-invariants) own the state meanings and rules. [SPEC030](../invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) and [SPEC041](../invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md) retain action/contract qualification.

Apply [SPEC048 OPS-R01–09 — common operational requirements](SPEC-SEI-048-shared-error-handling-and-operational-support.md#2-common-operational-requirements) and the stage-specific operational requirements below. ERR-S01/02.

## 2 Failure investigation and permitted recovery

| ID / condition | Evidence visible to authorised Support/Engineering | Permitted next action and owner |
|---|---|---|
| ERR-LCS-01 Unknown, conflicting or unmatched event | Show raw code/namespace, source, invoice/actor identity, event and observation times, mapping version and held reason. | Lifecycle/Integration owner applies LCS-R01/02/07/13; hold unsupported interpretation rather than guessing a new business state. |
| ERR-LCS-02 Transition attempt fails or becomes stuck | Show the relevant attempt, operationStatus/errorCode where qualified, previous successful status and current evidence. | Follow LCS-R14 and code-specific INT-ERR01 handling. A failed attempt cannot replace the last successful invoice status or fabricate business rejection. |
| ERR-LCS-03 One required report fails or times out | Show business fact, destination/purpose, original report/attempt, actor, deadline basis and each destination's outcome. | Lifecycle reporting owner recovers that obligation under LCS-R05/06. Reconcile uncertain delivery; preserve other successful reports and the business fact. |
| ERR-LCS-04 Cancellation of an earlier report is uncertain | Show the exact earlier communication, cancellation attempt and whether a replacement is blocked. | Follow SPEC029 §4.3. Original-operation reconciliation precedes replacement; report cancellation does not withdraw the invoice. |
| ERR-LCS-05 Required authority/data or supported action is missing | Show actor/direction, field/rule issues, required evidence and qualified capability. Keep legal applicability, provider support and enabled product scope separate. | Customer/Compliance/API owner resolves LCS-R04/12/13. Do not turn a technical failure or unqualified action into a report. |
| ERR-LCS-06 Events are missed or the customer changed provider | Show saved history, source-query coverage, original invoice route, retained access and unresolved obligations. | Follow LCS-R08/10/11. Recover missing evidence or reports through the qualified historical channel; OPS-R07 cannot move earlier reports to the new route. |

Use [SPEC011 — SPFE response and error matrix](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix) for source-dependent classifications. Keep exact source codes and their operation/version bindings. INT-ERR01 applies only where its selected contract is qualified. Neither a message-resource key nor an HTTP status alone proves the external effect or safe replay. ERR-S02–04.

## 3 Spain use and reuse qualification

Use in Spain covers recipient/issuer actions and separately qualified public/private reporting. Evidence history, independent obligations and guarded recovery are shared design patterns. Spain actor, event, correction and Annex II rules remain country-specific; source conflicts remain open. Build and portal coverage are unknown. Existing DTS is the preferred mapping reuse candidate where event-document transformation is needed; invoice mapping support does not prove lifecycle-document support.

## 4 Acceptance and open decisions

Exercise ERR-LCS-02/03 with a failed transition and a successful report to one destination. Exercise ERR-LCS-04 with a lost cancellation response; replacement remains blocked. Exercise ERR-LCS-01/05/06 with an unknown code, missing authority and a provider switch; preserve the historical source and existing business fact. Apply [OPS-A01–05 common checks](SPEC-SEI-048-shared-error-handling-and-operational-support.md#5-acceptance-and-open-gates), including country-rule isolation and qualification of actual implementation reuse. These are required acceptance scenarios, not executed implementation tests. ERR-S01/02.

Lifecycle/API owners must qualify Spain action bindings, transition/attempt correlation, Annex II rule execution and report reconciliation in LIF-G03 and the companion gates. Operations/Compliance own alert thresholds and applicable deadline exposure. The proposed four-day acceptance timer remains unverified in SPEC029; it cannot become a recovery success rule.

## REF Source references

| ID | Source/version and exact location | Supported claim and limit |
|---|---|---|
| ERR-S01 | Functional and API owner documents linked in §1; repository drafts read 23 November 2026; activity/requirement IDs named in §2. | Canonical stage behaviour and open gates. This view adds operational inspection, not a new external contract or lifecycle rule. |
| ERR-S02 | [SPEC048 source register](SPEC-SEI-048-shared-error-handling-and-operational-support.md#ref-source-references), OPS-S01–04; stakeholder note received 23 November 2026; PRD107/215/225 and INT-ERR01. | Product and operational evidence for support requests; stakeholder reported limitations and FR support do not prove Spain implementation. |
| ERR-S03 | [CustomerInvoiceEvents.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/CustomerInvoiceEvents.wsdl>); [SupplierInvoiceEvents.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/SupplierInvoiceEvents.wsdl>); [GetInvoices.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/GetInvoices.wsdl>); reviewed local PRE release 23 November 2026; `wsdl:portType/operation`, binding and service ports. | Exact named operations and transport evidence only. No universal replay, complete business-result or production-support claim. |
| ERR-S04 | [SPEC011 — complete business/technical mapping](../SPEC-SEI-011-public-platform-connector-solution-specification.md#business-and-technical-error-mapping); [original business messages](<../../context/Listados códigos de error/errores_negocio.properties>) and [original technical messages](<../../context/Listados códigos de error/errores_tecnicos.properties>), SPFE-S28/S29 received 23 November 2026, active message keys/templates; [release review](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026). | Message templates and proposed handling only; actual wire-code, field and operation bindings remain unqualified under SPFE-Q20/Q21. Do not copy another operation's meaning or retry rule. |
