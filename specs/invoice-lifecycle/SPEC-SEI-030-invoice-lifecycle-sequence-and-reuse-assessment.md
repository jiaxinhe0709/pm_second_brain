---
id: SPEC-SEI-030
title: Invoice Lifecycle Sequence and Reuse Assessment
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
  - SPEC-SEI-029
  - PRD-SEI-224
  - PRD-SEI-232
  - PRD-SEI-242
  - SPEC-SEI-008
  - SPEC-SEI-011
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

# Invoice Lifecycle Sequence and Reuse Assessment

[Solution summary](SPEC-SEI-028-invoice-lifecycle-solution-summary.md) · [Logical specification](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md)

## Revision overview

This view assesses the existing E-Invoice API against [SPEC009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md), which stays unchanged and remains the Confluence source. The supplied France guides establish reuse candidates; they do not prove Spain support, new status UUIDs or a configurable country implementation. No new endpoint or breaking change is approved.

## 1 Reuse decision and product impact

Assess the existing status POST → notification → invoice GET/history pattern first. Products may retain that pattern if the selected build supports the Spain action, actor, fields and reporting results. Variable `statusAttributes` does not prove arbitrary-field support. INT-LCS01/02/05. [SPEC029](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) owns required behaviour.

| Delivery scope | Reuse / Spain work | Product impact / gates |
|---|---|---|
| Public consultation — Phase 1 | Map qualified public evidence to saved invoice views. | Reuse invoice reads if fields suffice; no AEAT webhook is established. LIF-G01/02/05. |
| Private mapping — Phase 2 | Qualify each provider’s status, actor, direction, original route and automatic reports. | Keep common calls where supported; expose separate reporting results. LIF-G02/07. |
| Recipient actions/reporting — Phase 3 | Qualify Spain action UUIDs, dates/reasons, report ownership and cancellation. | Products supply the selected action fields and retain operation/report results. LIF-G04/06. |
| Optional issuer/customer actions | Select enabled scope and qualify collection/default/cancellation. | Read support does not imply a writable command. LIF-G04/08. |
| Shared history and recovery | Correlate exact attempts, notifications and destination results; prove safe replay. | Recover missed events through reads. No confirmed breaking change. LIF-G02/05/06. |

PRD224 retains these phases. The guide uses status POST for payment facts, not a separate payment endpoint or revised invoice UBL. Whether its payload covers Spain reporting is still open.

<a id="2-operation-assessment"></a>

## 2 Proposed reuse sequences

Grey shows documented existing E-Invoice calls. Blue shows Spain binding or proposed work to confirm. Each diagram explains the request, result and action still needing evidence.

<a id="21-french-request-notification-and-history-read"></a>

### 2.1 Existing request, notification and history read

![Existing E-Invoice API: request a status change and read its result](../../assets/diagrams/invoice-lifecycle-fr-update-sequence.svg)

[Draw.io](../../assets/diagrams/invoice-lifecycle-fr-update-sequence.drawio) · [PNG](../../assets/diagrams/invoice-lifecycle-fr-update-sequence.png).

Save the returned operation ID. The completion event prompts a result read; it cannot prove transition success. A missed event uses qualified history recovery. LIF-G02/05/06.

### 2.2 Spain business event and independent public reporting

![Spain business fact and separate public/private report results](../../assets/diagrams/invoice-lifecycle-spain-reporting-sequence.svg)

[Draw.io](../../assets/diagrams/invoice-lifecycle-spain-reporting-sequence.drawio) · [PNG](../../assets/diagrams/invoice-lifecycle-spain-reporting-sequence.png).

Save the authorised fact, select required destinations and execute each report through its qualified contract. Public and private results stay independent; correlate provider-owned reporting instead of sending it again. Responsibility lanes do not approve new services.

### 2.3 Failed transition and uncertain cancellation

![Keep the successful status and check an uncertain cancellation](../../assets/diagrams/invoice-lifecycle-recovery-sequence.svg)

[Draw.io](../../assets/diagrams/invoice-lifecycle-recovery-sequence.drawio) · [PNG](../../assets/diagrams/invoice-lifecycle-recovery-sequence.png).

A failed transition retains the last successful status. A timeout/local error does not prove external rejection or non-execution. Hold replacement while checking the original cancellation; without a qualified lookup, keep an owned manual case. LCS-R14; LIF-G06.

## 3 Contract details that affect reuse

| Existing operation / source | Request → result | Reuse / Spain gap |
|---|---|---|
| `POST /internal/events/subscriptions` — INT-LCS01/02 | `resource = einvoice`, scoped `eventType = e-invoicing.einvoice.statusupdated` → subscription. | Qualify service/environment, dataset, webhook security, delivery and replay. LIF-G01/05. |
| `POST /datasets/{datasetId}/e-invoices/{e-invoiceId}/status` — INT-LCS01 | `data.type = e-InvoiceStatus`; UUID `statusCode`, selected `statusAttributes` → `201 Created`, operation `data.id`. | Reuse envelope/attempt pattern; Spain UUIDs, fields, actors and corrections remain unconfirmed. LIF-G04/06. |
| Status-updated webhook — INT-LCS02 | Example type `com.sage.network.api.e-invoicing.einvoice.statusupdated`; `subject` = invoice, `data.id` = status UUID. | Finished processing may mean `ERROR`. Prove event-to-operation/history correlation. LIF-G05. |
| `GET /datasets/{datasetId}/e-invoices/{e-invoiceId}` — INT-LCS02/INT-ERR01 | Existing IDs → `data.attributes.currentStatus` and `history`. | Read the relevant attempt’s outcome/error from history. Prove full schema, completeness and freshness. LIF-G02/05. |
| `GetInvoices` / `GetRegisteredInvoice` — SPFE-S03/S14/S15 | Identity or presentation-date query → public observations. | Separate external discovery from saved-history reads. Qualify fields, scope and continuation. LIF-G01/02. |
| `CustomerInvoiceEvents` — SPFE-S11 | Recipient PAYMENT, REJECTION or cancellation → public result. | Supplied SOAP transport; body/envelope, actor/fields and result correlation still gated. LIF-G04/06. |
| `SupplierInvoiceEvents` — SPFE-S17 | Issuer SETTLEMENT, DEFAULT or cancellation → public result. | Qualify contract and enabled optional scope. LIF-G04/08. |

SOAP operations belong to the public connector boundary in [SPEC011](../SPEC-SEI-011-public-platform-connector-solution-specification.md). Their supplied PRE WSDLs do not prove production support, complete event schemas or batch limits.

### 3.1 Identifiers, payloads and outcome domains

| Existing element | Reuse rule / gap |
|---|---|
| Dataset/invoice and historical route | Reuse saved IDs; verify current business/action authority. A route change cannot rebind old reports. LIF-G01/07. |
| `statusCode` | UUID required. France numeric `200` identifies three different UUIDs; AEAT `PAYMENT` is a separate external code. Country selection remains LIF-G02/04. |
| `statusAttributes` | Use only the selected action’s fields. The [guide](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md#int-lcs01-send-a-status-update>) retains array/object shapes. Spain schema/unknown-field behaviour is open. LIF-G04. |
| Occurrence time | Optional `lifecycleMetadata.statusDateTime` is UTC. Creation/webhook timestamps cannot replace legal event dates. LIF-G04. |
| Operation/event/history IDs | POST `data.id` is an operation; webhook `data.id` is a status UUID; `subject` is the invoice. Notification top-level `id` is ambiguous. Prove correlation; never deduplicate distinct attempts by status UUID. LIF-G05. |
| Attempt result | `history[].operationStatus` = `IN_PROGRESS`, `COMPLETED` or `ERROR`; nullable `history[].errorCode`. `currentStatus` has neither. Prove entry schema/order/correlation. INT-ERR01; LIF-G02/05. |
| Lifecycle Completed | France `209`, UUID `00000000-0000-0000-0000-140000000000`, concerns information supplied after suspension. It differs from operational `COMPLETED`, payment and report completion. LCS-A27. |

Detailed LCS-D01–10 and interaction inventories remain in [SPEC009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#1-interaction-contracts). Qualify existing fields before proposing additions.

### 3.2 Spain field coverage against the French guide

These are reuse candidates, not approved transformations. [SPEC029 §5.2](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#52-public-event-contract) and the AXII ledger own exact Spain fields/cardinalities.

| Spain need | Existing candidate / change to qualify |
|---|---|
| Four invoice-reference fields | Derive from saved invoice context only after proving exact seller NIF/name, series/number and date. Dataset owner need not be the seller. |
| Recipient `PAYMENT` | France Payment Sent `211`/`paymentData` does not prove full effective payment. Obtain due/payment dates and conditional fields. |
| Issuer `SETTLEMENT` | France Payment Received `212` includes partial payments; qualify full collection, occurrence date and conditional fields. |
| `REJECTION`, L1 `01`/`02` | France Refused `210`/`rejectionData[].reasonCode` needs an explicit actor/reason/date mapping; similar labels are insufficient. |
| Explicit acceptance | France Approved `205` may inform qualified private communication. No supplied public acceptance report exists. |
| `DEFAULT` | No matching writable command is supplied. A calculated overdue view cannot automatically assert issuer non-payment. |
| Four `CANCEL*` actions | Missing command evidence. Preserve report cancellation/replacement lineage; invoice withdrawal differs. |
| Several dates/indicators | France `paymentData[]` has required `netAmount`/`currencyCode`, optional `vatRate`; it lacks the distinct Spain date/indicator fields. One lifecycle timestamp cannot replace them. |
| Several destinations | Existing POST/history pattern needs proof of independent obligations/results and provider-report correlation. |

Assess existing DTS first for ApplicationResponse generation. Qualify its actual build, contract, mappings, rules, country versions and operations. Transformation cannot provide missing event facts or authority. LIF-G04.

### 3.3 Authentication, retries and completion

INT-LCS01 documents Domain Services or Sage ID M2M tokens and required `Authorization`, `traceparent`, `tracestate`, `Idempotency-Key` for status POST. Qualify public certificate authentication/representation separately; a product bearer token is not a provider credential. SPFE-S02 Article 11; SPFE-S11/S17.

| Condition | Required handling / gate |
|---|---|
| Repeated command | Keep original identity/content; a changed correction is a linked action. Prove key scope, retention, conflicts and concurrency. LIF-G06. |
| `201` or completion notification | Save/correlate the operation and read the result. Neither proves business/public success. LIF-G05. |
| Confirmed transition `ERROR` | Retain successful status and failed history; expose correction/owner. A report’s external result remains separate. LCS-R14/A26/27. |
| Timeout or uncertain cancellation | Check the original effect before unsafe replay, new key, replacement or route fallback. LIF-G06. |
| `429`, missing event or concurrent changes | Honour `Retry-After`; still apply mutation-safety rules. Read qualified history or consult uncaptured source evidence. LIF-G02/05/06. |

[INT-ERR01](<../../context/FR API/Shared/invoice-flow-error-handling-guide-extract.md>) retains `ERR-SENDING-STATUS-*` actions for mapping, unsupported status, update and notification failures. Platform retries do not authorise product resends. Its code-specific six-day support guidance is not a Spain deadline.

## 4 Source conflicts and qualification gates

| Gate / owner | Required evidence before the affected capability is enabled |
|---|---|
| LIF-G01 — API/Architecture, Integration | Actual build/API version, country extension points, access-point mapping and Spain entitlement. |
| LIF-G02 — Lifecycle/API | Separate views, latest successful status, exact attempt/history schema, per-destination work, concurrency and retained rule versions. |
| LIF-G03 — API owner | Resolve France Payment Received terminal/nonterminal, Disputed → Refused, blocked Submitted → Rejected and Completed/Rejected actor conflicts against the selected matrix/schema/tests. No Spain default inferred. |
| LIF-G04 — Spain, DTS, API, Legal/Tax | Spain command identifiers, eight actor/code bindings, 52 fields, complete schema, literal-path/indicator decisions, cancellation and result fixtures. Preserve incoming facts while holding unsupported commands. |
| LIF-G05 — Notifications/API | Event security/identity, operation/history correlation, replay and complete reads. Resolve sample `DIS-001`, `SUP-001`, `PA-001` against closed reason lists. |
| LIF-G06 — API, Connector, Operations | Key/retry/mutation-safety rules, original-result reconciliation, uncertain cancellation and owned manual fallback. |
| LIF-G07 — Identity/Spain, provider owners | Represented business/actor authority, original provider/channel and selected private contract. Retain LCS-Q-PROVIDER. |
| LIF-G08 — Product/Spain | Enabled release/optional actions, legal applicability and calendars. Retain LCS-Q-OPTIONAL and valid incoming optional evidence. |

[Existing provider assessments](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#lifecycle-statuses-and-actions-by-provider) retain B2B Router, Banqup, SERES, EDICOM and ZeroComa evidence limits. No new private contract is established. The [Annex II comparison](<../../context/Anexo II/annex-ii-review.md>) does not close runtime gaps.

## 5 API qualification acceptance

These checks supplement LCS-A01–27; none is claimed as executed implementation testing.

| Check | Required proof / functional link |
|---|---|
| LIF-API-A01 | Common calls select separate France/Spain rules without changing codes, reasons, duties, authority or saved history. LCS-A13/14; G01/02/04. |
| LIF-API-A02 | POST, events and history correlate the exact attempt despite repeated UUIDs/missed events; pending/failure preserves success. LCS-A10/26; G02/05. |
| LIF-API-A03 | Separate lifecycle Completed, operational COMPLETED, technical Rejected, business Refused and external unknown; resolve guide conflicts. LCS-A01/22/27; G03/05. |
| LIF-API-A04 | Eight codes/52 fields cover actors, full/partial payment, reasons, dates, indicators and cancellations; invalid input holds before mutation. LCS-SPFE-A01/02; AXII pairs; G04. |
| LIF-API-A05 | Same-key replay, changed content, concurrent commands, timeout and `429` follow qualified safe rules without duplicate effects. LCS-A06–08; G06. |
| LIF-API-A06 | Independent destination results and provider-owned reports avoid duplicates; uncertain cancellation holds replacement. LCS-A08/12/24; SPFE-A03; G04/06. |
| LIF-API-A07 | Wrong client/actor/environment denied; historical invoice reports retain their permitted route without automatic fallback. LCS-A09/15/19; G07. |
| LIF-API-A08 | Record actual build, schema, DTS/rules, positive/negative fixtures and operations owner for enabled scope. Unqualified actions remain held. LCS-A14/25; G01–08. |

## REF Source references

| Source ID | Original source and version/date | Exact locator | Supported claims and limits |
|---|---|---|---|
| REF-BASE | [SPEC-SEI-009](../archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md), updated 20 October 2026; [functional successor view](SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md), draft 22 October | LCS-INT-01–11; D01–10; provider catalogues; LCS requirements/acceptance | Canonical draft requirements and logical contracts; no physical allocation approval. |
| INT-LCS01 | [Supplied send-status guide extract](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md#int-lcs01-send-a-status-update>), received 22 October, revision unknown | §1 request/response, headers and per-status examples; linked API `1.13.0` | Exact product POST and documented payloads; not Spain schema or deployed build evidence. |
| INT-LCS02 | [Supplied receive/history guide extract](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md#int-lcs02-receive-notifications-and-read-history>), same receipt/version limit | §§1–3; linked Notifications `6.3.0`; webhook example; invoice GET | Completion event and history read; full correlation/history contract absent. |
| INT-LCS03/04/05 | [Supplied status, reason and outcome evidence](<../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>), same receipt/version limit | Status list; blocked table; status-specific reasons; user transition note | Exact France UUIDs, conflicts and attempt outcomes. Matrix/Schematron not independently verified; no Spain defaults. |
| INT-ERR01 | [Existing supplied FR error-guide extract](<../../context/FR API/Shared/invoice-flow-error-handling-guide-extract.md>), received 22 October 2026; revision/build unknown | Processing and error fields; Processing status change; Recovery interpretation | Exact history/currentStatus/error paths and code-specific actions. No complete correlation contract, Spain error mapping or product-side resend permission. |
| SPFE-S02 | [Final BOE order](../../context/BOE-A-2026-20587.pdf), published 5 October 2026; [official publication](https://www.boe.es/eli/es/o/2026/10/02/hac1028), checked 22 October | Articles 7–11; Annex II pp. 36–42 | Legal/event/authority baseline; not proof of an activated wire contract. |
| SPFE-S03 | [Original catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | §§6.4–6.5 and 6.8–6.9, pp. 12–14 and 16–19 | Query/report names, actor/event meaning, exclusivity and correction; not complete request formats. |
| SPFE-S08 | [Original formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), 0.1.0, 9 October, BORRADOR | §§5.4–5.5/5.8–5.9, pp. 14–15 | Pending business formats; source-response levels need qualification. |
| SPFE-S11/S17 | [CustomerInvoiceEvents.wsdl](<../../context/WSDL servicios web - PRE/20261013/CustomerInvoiceEvents.wsdl>); [SupplierInvoiceEvents.wsdl](<../../context/WSDL servicios web - PRE/20261013/SupplierInvoiceEvents.wsdl>), supplied 13 October | Corresponding operations, SOAP bindings, certificate/seal service ports | Recipient/issuer PRE transport contracts; no production or complete event-body claim. |
| SPFE-S14/S15 | [GetInvoices.wsdl](<../../context/WSDL servicios web - PRE/20261013/GetInvoices.wsdl>); [GetRegisteredInvoice.wsdl](<../../context/WSDL servicios web - PRE/20261013/GetRegisteredInvoice.wsdl>), supplied 13 October | Operations and ports; catalogue QUERYBYID/QUERYBYFILTER | Consultation transport; does not prove every required event or recovery lookup is exposed. |
| SPFE-S22 | [Supplied Annex II](<../../context/Anexo II/A2-Proyecto-OM-FE 21-10-26.pdf>), filename dated 21 October, formal revision unknown | I.1–4 pp. 4–14; II/L1 p. 15; [review](<../../context/Anexo II/annex-ii-review.md>) | Source fields, dates, cardinalities and codes; existing path ambiguities remain. |
| REF-FIELDS / REF-DTS | [Original AXII ledger](../../assets/regulatory/spain/spfe/field-traceability.json); [DTS specification](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md); [shared evidence baseline](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md) | AXII rows and SPFE-Q gates; DTS reuse/qualification | Preferred transformation candidate and source inventory; neither proves ApplicationResponse implementation readiness. |
