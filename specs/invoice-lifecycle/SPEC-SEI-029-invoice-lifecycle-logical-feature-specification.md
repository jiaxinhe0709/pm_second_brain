---
id: SPEC-SEI-029
title: Invoice Lifecycle Logical Feature Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-22
updated: 2026-10-27
reviewers: []
related:
  - SPEC-SEI-009
  - SPEC-SEI-028
  - SPEC-SEI-030
  - PRD-SEI-224
  - PRD-SEI-232
  - PRD-SEI-242
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# Invoice Lifecycle Logical Feature Specification

[Solution summary](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) · [API reuse assessment](SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md)

## Revision overview

This view preserves [SPEC009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) and its LCS/SPFE/AXII meanings. LCS-R14 and LCS-A26/27 cover the supplied transition-outcome rule. Release scope, authority, full/partial payment and historical routes are unchanged. These unpublished drafts do not enable customer actions.

## 1 Purpose, terms and authority

Show the buyer, seller or authorised accountant the invoice facts, action results and outstanding reports. A **transition attempt** requests a status change. Its result is separate from the invoice’s last successful status and every external report. Use the [glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). INT-LCS05; REF-PRODUCT.

Before a command or report, check the caller, represented business, actor role and invoice action. Reuse onboarding’s dataset/platform binding and credential references where qualified. A token or connection does not grant business authority. SPFE-S02 Article 11; LCS-R04.

## 2 Scenarios and safe next actions

| Trigger / actor | Required result / safe alternative | Existing coverage |
|---|---|---|
| Platform supplies evidence | Save source meaning; update only supported facts. Hold unknown/unmatched codes for review. | LCS-01–05; R01–03/09/11; A01/02/11/15 |
| Buyer records acceptance/rejection | Save the authorised decision/date and assess required communications. Missing authority/fields holds the command. Presumed acceptance stays derived. | LCS-02/04/07–09; R04–06/12; A03/05/18 |
| Buyer pays; seller records collection | Keep actor, dates, amounts and evidence. Assess full payment and each report separately; partial/bank evidence cannot prove public full payment. | LCS-02–05/07–10; A04/06/20 |
| Product requests a transition | Show its attempt result separately. Failure retains the previous successful status and corrective action. | R14; A26/27 |
| Several destinations require reporting | One owner/result per destination. Keep known successes; check the original uncertain attempt before repeating. | LCS-07–10; R05/06; A08/16/24 |
| Buyer/seller corrects a report | Preserve cancellation/replacement history. Uncertain cancellation blocks replacement; it does not withdraw the invoice. | LCS-03/07–10; SPFE-R03; A12; SPFE-A03 |
| Product misses an event | Read saved history. Query the platform separately for evidence Sage has not received. | R08/11; A10/15/23 |
| Late/conflicting evidence or provider switch | Preserve chronology and original route. Hold unsafe changes; a new route does not rebind old reports. | R07/10; A06/07/09 |
| Optional/provider-specific action requested | Check enabled scope, direction, actor and fields. Keep valid incoming evidence even when its outgoing command is disabled. | R12/13; A19/21/22/25 |

## 3 Activity order and process support

| Activity | Required result |
|---|---|
| LCS-01 Receive | Scoped platform evidence or an authorised business fact, with source/query/event identity. |
| LCS-02 Verify | Invoice, business, caller, actor, environment and original route checked. |
| LCS-03 Preserve | Raw evidence and duplicate/correction/conflict relationship saved. |
| LCS-04 Interpret | Effective country/provider rules applied; unknown values held with an owner. |
| LCS-05 Derive | Separate views with rule version, evidence age and next action. |
| LCS-06 Publish | Saved view/history readable; notification follows the saved change. |
| LCS-07 Plan obligations | Required destinations, historical actor/channel and deadlines selected. |
| LCS-08 Create obligations | One saved reporting obligation per event, destination and purpose; stable identity through recovery. |
| LCS-09 Deliver | Each attempt/result recorded; no second sender for provider-owned reporting. |
| LCS-10 Reconcile | Original uncertain result or conflict resolved before an unsafe new action. |

![Send required reports and check uncertain results](../../assets/diagrams/lifecycle-reporting-reconciliation-process.svg)

[Draw.io](../../assets/diagrams/lifecycle-reporting-reconciliation-process.drawio) · [PNG](../../assets/diagrams/lifecycle-reporting-reconciliation-process.png).

The business fact remains saved while reports complete independently. A known success stays complete when another destination fails. Check an uncertain cancellation before replacement. The [summary](SPEC-SEI-028-invoice-lifecycle-solution-summary.md#3-end-to-end-flow) shows evidence collection; SPEC030 shows proposed calls.

## 4 Functional requirements and invariants

| ID | Required behaviour | Authority |
|---|---|---|
| LCS-R01 | Preserve source code/namespace, actor, times, identity and integrity/version evidence before mapping. | PRD224 FR1–3; PRD232 LS-FR1/14 |
| LCS-R02 | Apply effective country/provider rules; unknown codes cannot advance status. | PRD232 LS-FR2/12/16 |
| LCS-R03 | Keep processing, validation, delivery, commercial, payment and reporting results separately readable; distinguish explicit/derived facts. | PRD224 FR3–4/18 |
| LCS-R04 | Before a command/report, verify actor authority, applicability and required data. | PRD224 FR1/5 |
| LCS-R05 | Select destinations/deadlines using approved rules and the invoice’s historical context. | PRD224 FR6–10 |
| LCS-R06 | Save/deliver each obligation independently; safe repetition cannot add a duplicate effect. | PRD224 FR8/11–13 |
| LCS-R07 | Keep duplicate, late, conflicting and superseding evidence; hold unsafe progression. | PRD224 FR14–17 |
| LCS-R08 | Let authorised callers read views, history, next actions and report results to recover missed notifications. | PRD224 FR18–23; PRD242 PEP-FR9 |
| LCS-R09 | Interpret Peppol transport, MLR, MLS and Invoice Response only in their source namespaces. | PRD242 PEP-FR2–6 |
| LCS-R10 | Keep original route, process and mapping context after provider change. | PRD224 FR9; PRD242 PEP-FR10 |
| LCS-R11 | Separate platform consultation, supported notifications, saved-history reads, file retrieval and reporting. | SPFE-S02 Article 10; PRD242 |
| LCS-R12 | Record mandatory/optional/correction/technical classification and destinations. Separate legal duty, provider support and enabled release. | ES-RD10; SPFE-S02; proposed control |
| LCS-R13 | Qualify provider/version, direction, actor, fields, correction and automatic reports before sending. Keep valid incoming evidence; hold unqualified commands. | PRD224 FR10; proposed control |
| LCS-R14 | Show transition attempts separately. Pending/failed attempts retain the latest successful status; save failure with `operationStatus = ERROR`. Advance only on qualified success. | INT-LCS05; proposed Spain control |

[LCS-I01–09](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#1-identity-dimensions-and-invariants) retain immutable sources, independent results, evidence limits, correction history and separate obligations. Apply business/tenant/environment/delegate checks to reads, writes, subscriptions and support. Protect payment evidence and credentials; monitor stale/unknown facts, deadlines, conflicts and uncertain reports. Targets/retention remain open.

## 5 Spain rules and Annex II

### 5.1 Destination and obligation rules

Duties depend on the invoice, actor and effective customer group. France mandatory labels do not establish Spain duties. LCS-R12/13; ES-RD10 Articles 10/12; SPFE-S02 Article 7.

| Event | Communication to issuer | Public report |
|---|---|---|
| Recipient acceptance/rejection | Mandatory when the recipient duty applies; decision and date. | `REJECTION` when applicable; no explicit acceptance code. |
| Recipient full effective payment | Mandatory when the duty applies; effective payment date. | `PAYMENT`, subject to its separate public rules/exceptions. |
| Partial decision/payment or assignment | Optional, with the selected event's required fields. | No corresponding code supplied. |
| Issuer full collection/non-payment | Private contract must establish any communication. | Optional `SETTLEMENT` / `DEFAULT`. |
| Correction | Selected provider's correction procedure. | Cancel the earlier report before a changed replacement where required. |

The [existing destination table](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#spain-events-mandatory-and-optional-reporting-by-destination) retains exact applicability, separate issuer/public calendars and special correction cases. Optional actions remain disabled until Product approves them.

Preserve the conditional presumed-acceptance view, prepaid exception, qualifying public-platform outage procedure and cancellation traceability. No explicit public acceptance code or revised rollout/deadline follows from the supplied snapshot. SPFE-S02 Articles 7.1/7.4/8.4/8.5; LCS-SPFE-R04.

### 5.2 Public event contract

Every event references the invoice’s series/number, issue date, seller NIF and seller name. The seller is not automatically the caller or represented reporting actor. `ResponseCode` uses `ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode`. SPFE-S02 Annex II; SPFE-S22.

| Actor / exact code | Required meaning / fields | Source locator |
|---|---|---|
| Recipient `PAYMENT` | Full effective payment; `EffectiveDate` and `DueDate` required. Shipment/receipt dates and correction/negative indicators are conditional. | SPFE-S22 pp. 4–6; SPFE-S03 §6.8 |
| Recipient `CANCELPAYMENT` | Cancel the earlier payment report; retain the payment fact. | SPFE-S22 p. 6; SPFE-S03 §6.8 |
| Recipient `REJECTION` | Rejection date and L1 reason `01` commercial / `02` private consumption required. Mutually exclusive with recipient PAYMENT. | SPFE-S22 p. 7/L1 p. 15; SPFE-S03 §6.8 |
| Recipient `CANCELREJECTION` | Cancel earlier rejection; do not manufacture explicit acceptance. | SPFE-S22 p. 8; SPFE-S03 §6.8 |
| Issuer `SETTLEMENT` | Full collection date required; due/financing/shipment/receipt fields conditional. | SPFE-S22 pp. 9–10; SPFE-S03 §6.9 |
| Issuer `CANCELSETTLEMENT` | Cancel the earlier collection report. | SPFE-S22 p. 11; SPFE-S03 §6.9 |
| Issuer `DEFAULT` | `EffectiveDate` means payment due date; shipment/receipt dates conditional. Mutually exclusive with issuer SETTLEMENT. | SPFE-S22 pp. 12–13; SPFE-S03 §6.9 |
| Issuer `CANCELDEFAULT` | Cancel the earlier non-payment report; retain facts/history. | SPFE-S22 p. 14; SPFE-S03 §6.9 |

Cancellation retains the four invoice-reference fields and links to the earlier report. An uncertain result holds replacement. [LCS-SPFE-R01–04/A01–04](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#public-platform-lifecycle-events-and-reporting-requirements) and the [52-row AXII matrix](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#annex-ii-event-field-traceability) retain exact paths, cardinalities and positive/negative checks. The [comparison](<../../context/Anexo II/annex-ii-review.md>) found no material field change; it does not qualify XML generation.

### 5.3 Source limits and country isolation

Literal UBL-path conflicts and optional indicator semantics remain LIF-G04/SPFE-Q16/17 gates. Do not silently repair source paths or map France reason codes to Spain `ConditionCode`. SPFE-S08/S22.

Shared behaviour preserves evidence, independent views and safe recovery. Spain rules supply actors, events, fields, duties and calendars. Prefer existing DTS for required ApplicationResponse mapping, subject to build/mapping/operations proof. Another country keeps its own rules; saved history keeps its original versions. LCS-A13/14; LIF-API-A01/04/08.

## 6 Functional acceptance

These are required checks, not executed implementation tests. The [original assurance table](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#part-4-assurance-and-traceability-view) retains detailed traceability.

| Existing checks | Required proof |
|---|---|
| LCS-A01/02/11/22 | Delivery, Peppol codes, unknown/technical/payment-processing states affect only their supported result. |
| LCS-A03/04/05/18 | Authorised rejection/full payment; bank-evidence limit; explicit versus presumed acceptance; no invented public acceptance code. |
| LCS-A06/07/12 | Duplicate, conflicting, late and corrected evidence keeps history and holds unsafe progression. |
| LCS-A08/09/24 | Independent reports, timeout recovery, historical routes and provider-owned execution avoid duplicate effects. |
| LCS-A10/15/16/17/23 | Separate source consultation/history; no reporting loops or clearing facts omitted from partial events. |
| LCS-A13/14 | Actual reused build and country rules pass isolated France/Spain checks. |
| LCS-A19/20/21/25 | Optional scope, conditional fields, partial payments, corrected totals, assignment and read/write limits retain owned results. |
| LCS-SPFE-A01–04 | Eight codes, actors, dates/reasons, uncertain cancellations, rollout/prepaid/outage conditions. SPFE-S02/S03/S22. |
| LCS-AXII-* pairs | All 52 field/group occurrences retain valid/applicable and invalid-content checks. REF-FIELDS. |

| Added check | Required result / link |
|---|---|
| LCS-A26 | Pending then failed transition retains the last successful status; history records `operationStatus = ERROR`, correlation and next action. Report failure cannot erase a saved business fact. R03/06/08/14; INT-LCS05. |
| LCS-A27 | Distinguish lifecycle Completed (`209`), operational `COMPLETED`, `ERROR` and an unknown external result. None alone creates payment, acceptance or public admission. R02/03/07/14; INT-LCS03/05. |

## REF Source references

| Source ID | Original source and version/date | Exact locator | Supported claim and limit |
|---|---|---|---|
| REF-BASE / REF-PRODUCT | [SPEC-SEI-009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md), updated 20 October; [PRD224](../../prds/PRD-SEI-224-lifecycle-rejection-payment-reporting.md), [PRD232](../../prds/PRD-SEI-232-country-lifecycle-status-mapping.md), [PRD242](../../prds/PRD-SEI-242-peppol-lifecycle-feedback.md), current repository drafts/discovery | LCS requirements/invariants/acceptance; PRD FR1–23, LS-FR and PEP-FR | Existing product/design baseline and preserved IDs; not approved architecture or runtime evidence. |
| ES-RD10 | [Original RD 238/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295), published 31 March 2026; source identity retained from baseline | Articles 8.3, 10 and 12 | Recipient/issuer and public duties remain separate; no private API catalogue supplied. |
| SPFE-S02 | [Original final order](../../context/BOE-A-2026-20587.pdf), published 5 October 2026; [official publication](https://www.boe.es/eli/es/o/2026/10/02/hac1028), checked 22 October | Articles 7–11; Annex II pp. 36–42 | Legal duties, authority and event fields; not complete wire contract. |
| SPFE-S03 | [Original catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | §§6.4–6.5 pp. 12–14; §§6.8–6.9 pp. 16–19 | Consultation, exclusivity, full payment/collection and cancellation; no tested integration. |
| SPFE-S08 | [Original formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), 0.1.0, 9 October, BORRADOR | Response description p. 14; §§5.8–5.9 pp. 14–15 | Missing complete event formats remain a gate. |
| SPFE-S22 | [New supplied Annex II](<../../context/Anexo II/A2-Proyecto-OM-FE 21-10-26.pdf>), filename dated 21 October, formal revision unknown | I.1 pp. 4–6; I.2 pp. 7–8; I.3 pp. 9–11; I.4 pp. 12–14; II/L1 p. 15 | Same reviewed field semantics and codes as baseline; no legal amendment or implementation proof. |
| REF-FIELDS | [Original field ledger](../../assets/regulatory/spain/spfe/field-traceability.json); [new comparison note](<../../context/Anexo II/annex-ii-review.md>) | All AXII traces and their source locators | Row inventory and unchanged source meaning; executable mapping and test results unverified. |
| INT-LCS01–05 | [User-supplied lifecycle evidence](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>), received 22 October, revision unknown | Named guide sections; especially INT-LCS05 | France documentation and supplied attempt-result rule. Application to Spain is a proposed control; build coverage is unknown. |
