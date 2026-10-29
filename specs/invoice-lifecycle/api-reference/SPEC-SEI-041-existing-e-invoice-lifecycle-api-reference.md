---
id: SPEC-SEI-041
title: E-Invoice Lifecycle API Reuse and Spain Changes
type: api-reference
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-28
updated: 2026-10-29
reviewers: []
related:
  - SPEC-SEI-028
  - SPEC-SEI-029
  - SPEC-SEI-030
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

# E-Invoice Lifecycle API Reuse and Spain Changes

[SPEC030](../SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md) owns sequences, product impact and LIF-G01–08. This reference owns product-call details and examples. [SPEC029](../SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md) owns required behaviour and exact Spain event meanings.

**Evidence:** FR-LIF01 is the supplied OpenAPI 3.1.0 document, declared API version `1.0.0`, received 28 October 2026. It defines one status POST. Subscription, webhook and history details come from INT-LCS02/05 and INT-ERR01; their full contracts are not supplied. No source proves deployed Spain support.

<span style="color:#666666;">Grey: existing calls and fields.</span> · <span style="color:#1565C0;">Blue: proposed Spain work.</span> · <span style="color:#B42318;">Red: unresolved evidence or decisions.</span> Section 1 uses documented France statuses. Section 2 proposes Spain bindings and payloads. Examples use synthetic IDs; response extracts omit metadata. No example is an executed test.

## 1 Existing calls and results

| ID / caller → receiver | Purpose / evidence | Functional link |
|---|---|---|
| [LIF-API-01](#lif-api-01) — product → E-Invoice API | Request a status transition. FR-LIF01 defines method, path, envelope and HTTP responses. | LCS-R04/13/14 |
| [LIF-API-02](#lif-api-02) — authorised subscriber → Events | Subscribe to status-processing notifications. Guide evidence only. | LCS-R08 |
| [LIF-API-03](#lif-api-03) — Events → product | Prompt a read after processing; success or failure is possible. Guide evidence only. | LCS-R08/14 |
| [LIF-API-04](#lif-api-04) — product → E-Invoice API | Read saved status/history, including the matching attempt. Guide/error evidence only. | LCS-R03/08/14 |

Use service-returned `datasetId` and `e-invoiceId`. Confirm the represented business, actor, environment and invoice's original route before a command. Onboarding's connection result does not grant lifecycle authority. LCS-R04/10; LIF-G01/07.

<a id="lif-api-01"></a>

### 1.1 LIF-API-01 — Request a status transition

`POST /datasets/{datasetId}/e-invoices/{e-invoiceId}/status` · `operationId: LifecycleChange-Document` · FR-LIF01.

| Contract element | Supplied definition / limit |
|---|---|
| Server | Production `https://api.e-invoicing.sage.com`; sandbox-production `https://api-sbx.e-invoicing.sage.com`. These do not prove Spain enablement. |
| Authentication | Required Sage ID M2M bearer JWT (`securitySchemes.m2m`). The guide also mentions Domain Services tokens; accepted issuers/scopes need confirmation. |
| Path parameters | Both required UUIDs. |
| Headers | Required `Idempotency-Key`; optional `traceparent` and `tracestate`. INT-LCS01 calls both tracing headers required; resolve under LIF-G03. |
| Body | Required; `application/vnd.api+json`. Required `data.type = e-InvoiceStatus`, `data.attributes` and `data.attributes.statusCode` UUID. |
| `statusAttributes` | Optional object with `additionalProperties: true`. Descriptions name status-specific data; nested fields, required values and country rules are not enforced by this schema. |
| Occurrence time | INT-LCS01 documents optional `statusAttributes.lifecycleMetadata.statusDateTime`, UTC date-time. FR-LIF01 does not type this nested field. It cannot replace distinct Spain legal dates. |
| `201 Created` | JSON:API lifecycle-change task. `data.id` is the operation UUID. `data.attributes` describes the requested status; `data.meta` carries creation/modification metadata. No attempt outcome or destination-report result is defined here. |
| Follow-up timing | `Retry-After` is documented on `201` and `429`, in seconds. It supplies timing, not permission to repeat a mutation. |

**Request — existing France Approved example:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>POST https://api-sbx.e-invoicing.sage.com/datasets/{datasetId}/e-invoices/{e-invoiceId}/status
Authorization: Bearer {sageIdM2MToken}
Content-Type: application/vnd.api+json
Idempotency-Key: {originalRequestKey}

{
  "data": {
    "type": "e-InvoiceStatus",
    "attributes": {
      "statusCode": "00000000-0000-0000-0000-500000000000"
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

**Response — `201 Created`, extract:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-InvoiceStatus",
    "id": "00000000-0000-4000-8000-000000000041",
    "attributes": {
      "statusCode": "00000000-0000-0000-0000-500000000000",
      "status": "Approved",
      "statusAttributes": {}
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

Save the operation ID. The returned `Approved` label does not establish that processing succeeded. Follow LIF-API-03/04. LCS-R14; INT-LCS05.

### 1.2 Documented status inputs

FR-LIF01 supplies these nine request examples. UUIDs and shapes below are existing France evidence. INT-LCS01 supplies the field requirements; FR-LIF01 does not define nested validation schemas.

[SPEC029's general / France / Spain comparison](../SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#general-status-comparison) owns the business meanings and country differences. This table retains exact request UUIDs and payload constraints.

| Exact example name / UUID `statusCode` | `statusAttributes` / guide constraint |
|---|---|
| `inHand` — `00000000-0000-0000-0000-400000000000` | No status-specific attributes. |
| `approved` — `00000000-0000-0000-0000-500000000000` | No status-specific attributes. |
| `partiallyApproved` — `00000000-0000-0000-0000-600000000000` | `partiallyApprovedData[]`: required `motifCode`; optional `motifNote`, `approvedNetAmount`, `approvedTotalAmount`, `nonApprovedNetAmount`, `nonApprovedTotalAmount`, `currencyCode`. |
| `disputed` — `00000000-0000-0000-0000-700000000000` | `disputeData[]`: required `reasonCode`; optional `notes`, `requestedActionCode`, `requestedAction`. |
| `suspended` — `00000000-0000-0000-0000-800000000000` | `suspendedData` object; optional `reasonCode`, `reasonText`. |
| `completed` — `00000000-0000-0000-0000-140000000000` | Optional `completedData[]`; supplied items require `fieldId`, `fieldValue`. |
| `refused` — `00000000-0000-0000-0000-120000000000` | `rejectionData[]`: required `reasonCode`; optional `notes`. |
| `paymentSent` — `00000000-0000-0000-0000-900000000000` | `paymentData[]`: required `netAmount`, `currencyCode`; optional `vatRate`. |
| `paymentReceived` — `00000000-0000-0000-0000-110000000000` | Same payment shape; the guide allows partial or full collection. |

**Payment Sent request body — supplied example:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-InvoiceStatus",
    "attributes": {
      "statusCode": "00000000-0000-0000-0000-900000000000",
      "statusAttributes": {
        "paymentData": [
          { "netAmount": 800, "vatRate": 20, "currencyCode": "EUR" },
          { "netAmount": 200, "vatRate": 5.5, "currencyCode": "EUR" }
        ]
      }
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

<span style="color:#B42318;">These amounts do not establish full effective payment, Spain legal dates or a completed report. The response enum also includes `Submitted`; that alone does not establish another writable command. Sample reasons `PA-001`, `DIS-001`, `SUP-001` and `REASON-CODE` are not qualified reason fixtures. LIF-G03/04/05.</span>

<a id="lif-api-02"></a>

### 1.3 LIF-API-02 — Subscribe

`POST /internal/events/subscriptions` · INT-LCS02.

The guide names `resource = einvoice`, `eventType = e-invoicing.einvoice.statusupdated`, dataset/source/audience scope and an HTTPS endpoint. France source examples do not establish a Spain source. <span style="color:#B42318;">Full request/response, subscriber access, webhook security and replay contracts remain LIF-G01/05; no complete payload is inferred.</span>

<a id="lif-api-03"></a>

### 1.4 LIF-API-03 — Receive notification

INT-LCS02 gives type `com.sage.network.api.e-invoicing.einvoice.statusupdated`. `subject` is the invoice ID; `data.id` is the status UUID. Neither is the POST operation ID. The top-level notification `id` has unconfirmed uniqueness/correlation semantics.

Read the matching history attempt after the event. Finished processing can mean `ERROR`. <span style="color:#B42318;">Do not deduplicate separate attempts by status UUID or treat receipt as buyer acceptance. Exact correlation remains LIF-G05.</span>

<a id="lif-api-04"></a>

### 1.5 LIF-API-04 — Read status and history

`GET /datasets/{datasetId}/e-invoices/{e-invoiceId}` · INT-LCS02/05; INT-ERR01.

| Exact response path / value | Meaning / limit |
|---|---|
| `data.attributes.currentStatus` | Current snapshot. It has no `operationStatus` or `errorCode`. |
| `data.attributes.history[].operationStatus` | `IN_PROGRESS`, `COMPLETED`, `ERROR`: outcome of that processing attempt. |
| `data.attributes.history[].errorCode` | Nullable processing error code; not a Spain external rejection reason. |

Use saved history to recover a missed notification. Keep the latest successful status after failure. Operational `COMPLETED` differs from lifecycle `Completed` and from each destination's report outcome. <span style="color:#B42318;">Full history schema, ordering, pagination, freshness and operation correlation remain LIF-G02/05. This GET cannot recover platform evidence Sage never received; public consultation is separate.</span>

## 2 Spain changes to qualify

**Proposed country binding:** assess this mapping as a Spain lifecycle country pack behind the existing API and qualified connectors. Reuse the platform's native action/attribute/rule mechanism where available. The `data.attributes.statusAttributes.spfe` object below illustrates required inputs; it is not an established pack format. Resolve the Spain binding, business authority and historical destination from trusted invoice/setup context. The caller's `eventCode` does not grant authority or select an arbitrary country. France payload validation stays unchanged. FR-LIF01; LCS-R04/10/13; LIF-G01/04/07.

[SPEC030's country-pack assessment](../SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md#country-pack-assessment) owns the architecture evidence, proposed shared/country/connector split and qualification. Its [contract-fit analysis](../SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md#contract-fit-analysis) identifies semantic, input and result gaps. A gap may be resolved through existing pack configuration or country/connector code; it is not automatically a shared API change.

The [row mapping](../../../assets/mappings/spfe-lifecycle-api-mapping.json) covers all **eight actions and 52 Annex II field/group occurrences**. It retains source cardinalities, conditions, literal paths and existing acceptance IDs. Its API keys and XML interpretations are proposals. The [logical event rules](../SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#52-public-event-contract) remain authoritative for required behaviour. SPFE-S02/S22.

<a id="spfe-action-mapping"></a>

### 2.1 Action and destination mapping

The three existing UUIDs below are **conditional reuse candidates**. Their France meaning does not prove a valid Spain command. For the other five actions, the API owner must register a supported action binding or select an approved contract extension. No new UUID is assigned by this proposal. FR-LIF01; INT-LCS01/03; LIF-G04.

| SPFE `eventCode` / authorised actor | Proposed Sage action / `statusCode` | SPFE operation / XML `ResponseCode` | Mapping condition |
|---|---|---|---|
| `PAYMENT` / recipient | `PaymentSent` — `00000000-0000-0000-0000-900000000000` | `CustomerInvoiceEvents` / `PAYMENT` | Full effective payment evidence and applicable country rules; partial payments cannot trigger this report. |
| `CANCELPAYMENT` / recipient | New action binding required; UUID unassigned. | `CustomerInvoiceEvents` / `CANCELPAYMENT` | Link to the earlier recipient `PAYMENT` report. |
| `REJECTION` / recipient | `Refused` — `00000000-0000-0000-0000-120000000000` | `CustomerInvoiceEvents` / `REJECTION` | Authorised business rejection with reason `01` or `02`; never technical `Rejected`. |
| `CANCELREJECTION` / recipient | New action binding required; UUID unassigned. | `CustomerInvoiceEvents` / `CANCELREJECTION` | Link to the earlier recipient `REJECTION` report. |
| `SETTLEMENT` / issuer | `PaymentReceived` — `00000000-0000-0000-0000-110000000000` | `SupplierInvoiceEvents` / `SETTLEMENT` | Full collection evidence and enabled optional issuer scope. |
| `CANCELSETTLEMENT` / issuer | New action binding required; UUID unassigned. | `SupplierInvoiceEvents` / `CANCELSETTLEMENT` | Link to the earlier issuer `SETTLEMENT` report. |
| `DEFAULT` / issuer | New action binding required; UUID unassigned. | `SupplierInvoiceEvents` / `DEFAULT` | Authorised issuer non-payment declaration; enabled optional scope. |
| `CANCELDEFAULT` / issuer | New action binding required; UUID unassigned. | `SupplierInvoiceEvents` / `CANCELDEFAULT` | Link to the earlier issuer `DEFAULT` report. |

The connector maps recipient actions to ebMS `Action = ACCOUNTINGCUSTOMERPARTYACTION` and issuer actions to `ACCOUNTINGSUPPLIERPARTYACTION`. Each selected `eventCode` becomes `ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode`. Do not mix recipient and issuer actions in one public message. Catalogue §6.8 permits up to 100 recipient states; §6.9 supplies no numeric issuer limit. The product POST remains one command for one invoice. SPFE-S03 §§6.8–6.9; SPFE-S11/S17.

The five new bindings also need defined response `status` values or an approved response shape; the supplied response enum has no DEFAULT or cancellation values. Check existing consumers before extending it. A cancellation action changes the report result/history; it cannot erase the saved payment/decision fact or withdraw the invoice. LCS-R03/06/07; LIF-G02/03/04.

Use [SPEC029's comparison](../SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md#general-status-comparison) for statuses with no direct public event. An allowed private communication uses its separate contract. LCS-R02/03/12/13.

<a id="spfe-field-mapping"></a>

### 2.2 Input and XML field mapping

**Invoice context:** resolve the following facts from the invoice addressed by `datasetId` / `e-invoiceId`. The logical names below are not confirmed ERP or GET response field names. If a required fact is missing, obtain it through a qualified correction/input path before reporting; do not substitute caller identity or current company-master data. These four fields occur in all eight actions: **32 mapped occurrences**. SPFE-S02 Annex II; SPFE-S22 I.1–4.

| Saved invoice fact | Logical XML target under `DocumentResponse/DocumentReference` |
|---|---|
| `invoiceNumber` — exact series and number | `cbc:ID` |
| `issueDate` — original invoice business date | `cbc:IssueDate` |
| `sellerNif` — seller stated on that invoice | `cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` |
| `sellerName` — seller stated on that invoice | `cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName` |

Construct the referenced-invoice group for PAYMENT, REJECTION, SETTLEMENT and DEFAULT from those facts: **four mapped group occurrences**. It is not another caller field. Cancellation messages retain their four required references. The source's cancellation seller-name level differs from adjacent identifiers; qualify the actual hierarchy under SPFE-Q16.

**Event inputs:** every API key below is proposed under `data.attributes.statusAttributes.spfe`. Dates are business-date strings in `YYYY-MM-DD` form. Obtain them from an authorised product fact or qualified saved evidence. Do not derive them from creation/webhook time. **Sixteen mapped occurrences** complete the 52-row coverage. `R` means `ApplicationResponse/cac:DocumentResponse/cac:Response`. XML targets below express the source meaning; they are not executable XPath. Exact literal paths remain in the row mapping.

| Trace ID / action | Proposed API key / type | Presence | Logical XML target / mapping |
|---|---|---|---|
| AXII-PAYMENT-01 | `effectivePaymentDate` / date | `1..1` | `R/cbc:EffectiveDate` — full effective payment date. |
| AXII-PAYMENT-02 | `paymentDueDate` / date | `1..1` | `R/cac:Status/cbc:ReferenceDate`, selected by `Condition/AttributeID=DueDate`. |
| AXII-PAYMENT-03 | `goodsOrServicesReceiptDate` / date | `0..1`; include when relevant | `ReferenceDate`, selector `ShipmentDate`; malformed source path remains SPFE-Q16. |
| AXII-PAYMENT-04 | `invoiceReceiptDate` / date | `0..1`; include when relevant | `ReferenceDate`, selector `ReceptionDate`. |
| AXII-PAYMENT-05 | `correctedInvoice` / boolean | `0..1`; source condition | Source `R/cac:Status/cbc:StatusReason=CorrectedInvoice`. Logical boolean; XML representation remains gated. |
| AXII-PAYMENT-06 | `negativeAmountInvoice` / boolean | `0..1`; source condition | Source `StatusReason=NegativeAmountInvoice`. Apply the negative corrective-invoice/no-payment condition; XML representation remains gated. |
| AXII-REJECTION-01 | `rejectionDate` / date | `1..1` | `R/cbc:EffectiveDate` — recipient decision date. |
| AXII-REJECTION-02 | `rejectionReasonCode` / string | `1..1` | `R/cac:Status/cbc:ConditionCode`: exact `"01"` commercial rejection or `"02"` private consumption/not related to business activity. |
| AXII-SETTLEMENT-01 | `effectiveCollectionDate` / date | `1..1` | `R/cbc:EffectiveDate` — full collection date. |
| AXII-SETTLEMENT-02 | `paymentDueDate` / date | `0..1` | `ReferenceDate`, selector `DueDate`; PAYMENT's requiredness does not apply. |
| AXII-SETTLEMENT-03 | `financingArrangement` / boolean | `0..1`; source condition | Source `R/cac:Status/cac:Condition/cbc:AttributeID=FinancingArrangement`; XML value representation remains gated. |
| AXII-SETTLEMENT-04 | `goodsOrServicesReceiptDate` / date | `0..1`; include when relevant | `ReferenceDate`, selector `ShipmentDate`. |
| AXII-SETTLEMENT-05 | `invoiceReceiptDate` / date | `0..1`; include when relevant | `ReferenceDate`, selector `ReceptionDate`. |
| AXII-DEFAULT-01 | `paymentDueDate` / date | `1..1` | `R/cbc:EffectiveDate` — due date, not the non-payment observation date. |
| AXII-DEFAULT-02 | `goodsOrServicesReceiptDate` / date | `0..1`; include when relevant | `ReferenceDate`, selector `ShipmentDate`. |
| AXII-DEFAULT-03 | `invoiceReceiptDate` / date | `0..1`; include when relevant | `ReferenceDate`, selector `ReceptionDate`. |

SPFE-S02 Annex II pp. 36–42 / SPFE-S22 pp. 4–14 support these field meanings and cardinalities. The proposed boolean keys do not settle indicator serialization or mean that `false` must be written to XML. Omit non-applicable indicators; hold serialization until the selected schema/fixtures resolve SPFE-Q16. No generic prepaid field is introduced.

Two proposed control inputs sit outside the 52 source rows:

| Proposed key | Mapping / check |
|---|---|
| `eventCode` / string, required | One of §2.1's eight exact codes. It must agree with the qualified `statusCode`, country binding and authorised actor before mutation. It maps to `R/cbc:ResponseCode`. |
| `originalReportId` / opaque string, required for `CANCEL*` | Resolve the saved report for the same invoice, actor, destination and original event. Keep it internally; Annex II does not establish a wire field for this Sage reference. Check the original result before cancellation/replacement. LCS-R06/07; LIF-G06. |

For Spain, validate the selected `spfe` shape and reject mismatched or unsupported fields. France `paymentData[]` and `rejectionData[]` remain France contract fields. Do not fabricate net amounts, VAT rows or French reasons to pass shared validation. Public reports carry no partial-payment amount. Separate full-payment/collection evidence and country exceptions must pass SPEC029's rules; supplied dates alone do not prove them. LCS-A20/25; LIF-G03/04/08.

<a id="spfe-payload-examples"></a>

### 2.3 Proposed payload examples

Use the existing POST path, content type, authentication and idempotency header from §1.1. The blue object is new proposed input. These bodies illustrate a country binding; the supplied OpenAPI does not establish that a deployed build processes them.

**Recipient PAYMENT — conditional reuse of PaymentSent:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-InvoiceStatus",
    "attributes": {
      "statusCode": "00000000-0000-0000-0000-900000000000",
      "statusAttributes": {
        <span style="color:#1565C0;">"spfe": {
          "eventCode": "PAYMENT",
          "effectivePaymentDate": "2026-10-27",
          "paymentDueDate": "2026-10-20"
        }</span>
      }
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

The invoice references come from saved context. Add receipt dates/indicators only when their source conditions apply. The full-payment fact and reporting obligation must already be established.

**Recipient REJECTION — conditional reuse of Refused:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-InvoiceStatus",
    "attributes": {
      "statusCode": "00000000-0000-0000-0000-120000000000",
      "statusAttributes": {
        <span style="color:#1565C0;">"spfe": {
          "eventCode": "REJECTION",
          "rejectionDate": "2026-10-27",
          "rejectionReasonCode": "01"
        }</span>
      }
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

**Recipient CANCELPAYMENT — non-executable until its action binding is registered:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-InvoiceStatus",
    "attributes": {
      "statusCode": <span style="color:#B42318;">"{registeredCancelPaymentStatusUuid}"</span>,
      "statusAttributes": {
        <span style="color:#1565C0;">"spfe": {
          "eventCode": "CANCELPAYMENT",
          "originalReportId": "saved-payment-report-001"
        }</span>
      }
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

The red placeholder is not a UUID or an assigned API value. Cancellation sends the selected cancellation code and the same invoice references; it does not copy the earlier payment date/amount into unsupported XML fields. Keep the local cancellation link and preserve the business fact.

### 2.4 Results, recovery and qualification

| Result / information | Mapping decision |
|---|---|
| POST operation `data.id` | Existing operation reference. Retain it through notification/history recovery; it is not the external report reference. |
| Saved report identity and destination | Proposed read/result coverage: expose a stable report reference that `originalReportId` can resolve, with its invoice, event, actor and destination. The exact GET response fields remain LIF-G02/05. |
| SPFE `DocumentStatus` and receipt | Retain exact source/per-item outcomes and external references against that report. Do not invent success/error enums or infer event-response structure from an invoice-submission example. SPFE-S08/S11/S17; LIF-G04/06. |
| Cancellation/replacement | Keep separate attempts/results. An uncertain cancellation holds replacement; known success at another destination stays complete. LCS-A12/24; LIF-API-A06. |

Public operations stay under [SPEC011](../../SPEC-SEI-011-public-platform-connector-solution-specification.md). Existing DTS is the preferred ApplicationResponse transformation candidate; qualify its actual build, contracts, mappings, rules and operations. API owners must demonstrate the native country-extension mechanism before selecting the namespace/action registry. Validate typed input, response compatibility, retained pack/rule versions and France/Spain isolation. SPFE-S08's pending formats, literal-path defects and indicator serialization remain gates. The proposal does not establish tested XML or production integration. LIF-G01–08; LIF-API-A01/04/06/08.

## 3 Errors and safe follow-up

FR-LIF01 lists HTTP errors below. Error bodies use `application/vnd.api+json` and `errors[]`; `400` uses the detailed schema, `413`/`415` include `source.header`, and the other listed errors use the simple schema. HTTP intake errors differ from later `history[].errorCode` and external reporting results.

| Response / condition | Product action / qualification needed |
|---|---|
| `400`, `405`, `413`, `415` | Correct the request, method, size or media type. The contract gives no numeric payload limit or complete business validation rules. |
| `401`, `403` | Resolve authentication or authority; do not change the business or route to bypass denial. |
| `404` | Check resource identity and access. It does not prove an earlier request had no effect. |
| `429` | Observe `Retry-After`, then apply qualified repeat rules. |
| `500`, `502`, `503`, `504`, timeout | Preserve original request/key/context; reconcile possible effects before an unsafe resend. |
| Same key / changed content / concurrency | Key scope, retention, conflict response and concurrent-transition rules are unspecified. Do not infer them from the header name or invent a documented `409`. LIF-G06. |

<span style="color:#B42318;">Source-quality gaps: the response schema does not require top-level `data`; its attribute fields are not required either. The `400` example uses `links: []` while its schema defines an object. API owners must confirm the intended schema and fixtures under LIF-G03.</span> Qualification checks remain [LIF-API-A01–08](../SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md#5-api-qualification-acceptance).

## REF Source references

| ID | Original source / version / exact location | Supports / limit |
|---|---|---|
| FR-LIF01 | [Supplied OpenAPI](<../../../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>), received 28 October 2026; OpenAPI `3.1.0`, `info.version: 1.0.0`; `paths` status POST, `operationId: LifecycleChange-Document`; `components.parameters`, `.securitySchemes.m2m`, `.schemas.PostInvoiceStatusRequest/Response`, `.schemas.InvoiceStatusRequest/Response`, `.responses`. | Exact POST contract and examples. Retained from the user's paste with JSON content unchanged; original URL/revision/build unverified. No GET, subscription, Spain action or deployed-support proof. |
| INT-LCS01–05 | [Supplied lifecycle guides](<../../../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>), received 22 October 2026, revision unknown; named send, receive/history, catalogue, reason and outcome sections. | Nested-field guidance, notifications and attempt semantics; linked API `1.13.0` does not establish equivalence to FR-LIF01 `1.0.0`. |
| INT-ERR01 | [Supplied error guide](<../../../context/FR API/Shared/invoice-flow-error-handling-guide-extract.md>), received 22 October 2026, revision/build unknown; processing/error fields and status-change recovery. | Exact currentStatus/history/error paths and guide recovery; no full read or correlation schema. |
| SPFE-S02/S22 | [Final BOE order](../../../context/BOE-A-2026-20587.pdf), published 5 October 2026, Annex II pp. 36–42; [supplied Annex II](<../../../context/Anexo II/A2-Proyecto-OM-FE 21-10-26.pdf>), formal revision unknown, I.1–4 pp. 4–14 and L1 p. 15. | Spain field/code comparison baseline; legal authority remains final BOE. No complete executable mapping or POST extension established. |
| SPFE-S03 | [Original catalogue](<../../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), `0.1.0`, 9 October 2026; §§6.8–6.9, pp. 16–19. | Action/actor routing, full payment/collection, correction and recipient batch limit. Does not establish Sage command bindings. |
| SPFE-S08 | [Original formats](<../../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), `0.1.0`, 9 October 2026, BORRADOR; §§5.8–5.9 p. 15. | Detailed issuer/recipient event formats are pending in this snapshot. |
| SPFE-S11/S17 | [CustomerInvoiceEvents WSDL](<../../../context/WSDL servicios web - PRE_29:10:2026/CustomerInvoiceEvents.wsdl>); [SupplierInvoiceEvents WSDL](<../../../context/WSDL servicios web - PRE_29:10:2026/SupplierInvoiceEvents.wsdl>), PRE release 29 October 2026; named operations, messages, bindings and ports. | PRE SOAP/ebMS transport with opaque UBL attachments. No complete event business schema, deployed Spain API or live acceptance proof. |
| REF-MAP | [Proposed API/XML row mapping](../../../assets/mappings/spfe-lifecycle-api-mapping.json), 28 October 2026; `actions`, `additional_proposed_inputs`, all 52 `rows`; based on [canonical source ledger](../../../assets/regulatory/spain/spfe/field-traceability.json), AXII rows. | Source-to-input-to-logical-XML proposal, preserved cardinalities/conditions/paths and existing acceptance IDs. New API keys and XML interpretations require engineering qualification; no executed mapper or fixtures. |
| REF-PACK | [SPEC030 country-pack assessment](../SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md#country-pack-assessment), draft, 28 October 2026, §3.5 and ARCH-LCS01/02 source rows. | Preferred Spain pack/connector direction based on supplied architecture; exact native pack interfaces and deployed coverage remain unqualified. Does not approve the illustrative `spfe` format. |
| REF-DESIGN | [SPEC030](../SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md), draft, 28 October 2026, §§1–5/LIF-G01–08; [SPEC029](../SPEC-SEI-029-invoice-lifecycle-logical-feature-specification.md), draft, §§4–6. | Canonical proposed requirements, reuse gates and acceptance; not approved implementation or a new external contract. |
