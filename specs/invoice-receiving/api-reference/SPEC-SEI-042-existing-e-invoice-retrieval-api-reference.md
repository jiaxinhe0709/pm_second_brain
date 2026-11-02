---
id: SPEC-SEI-042
title: E-Invoice Retrieval API Reuse and Spain Changes
type: api-reference
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-30
updated: 2026-11-02
reviewers: []
related:
  - SPEC-SEI-016
  - SPEC-SEI-025
  - SPEC-SEI-026
  - SPEC-SEI-027
  - SPEC-SEI-011
  - SPEC-SEI-039
  - SPEC-SEI-040
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610662"
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# E-Invoice Retrieval API Reuse and Spain Changes

[Summary and walkthrough](../SPEC-SEI-025-invoice-retrieval-solution-summary.md) · [Required behaviour](../SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md) · [Sequences, product impact and gates](../SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md)

## Purpose and evidence

**View is required for public and private platforms. SPFE user download is required; private user download is TBD.** SPEC026 §1 owns this decision. A private provider's source-file fetch can still be necessary for intake and viewing. It is separate from a user downloading a saved file. REF-SCOPE.

This reference follows the [onboarding API analysis](../../onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md): existing calls, request/result fields, Spain changes and open evidence. SPEC027 owns RET-G01–10 and the reuse decisions. This page does not create another gate register.

**Evidence reviewed:** INT-RCV01, INT-ERR01 and the supplied Query/Retrieve OpenAPI definitions (INT-RCV02/03, received 2 November 2026), the SPFE catalogue/formats and the four original query/download WSDLs selected by the manifest: **PRE release 29 October 2026**. A canonical guide URL and deployed-build version remain missing. The supplied REST contracts do not prove Spain support. The WSDLs establish transport, not complete business schemas or a running Spain integration. REF-EVIDENCE.

<span style="color:#666666;">Grey: documented existing calls/fields.</span> · <span style="color:#1565C0;">Blue: proposed Spain reuse or additional work.</span> · <span style="color:#B42318;">Red: open evidence.</span> Examples use synthetic IDs and placeholders. Response snippets are field extracts, not complete schemas or executed requests. INT-RCV02/03 list production and sandbox servers; no Spain environment is qualified by their presence.

## 1 Existing product-facing calls

**Query supplies the invoice list. Retrieve supplies one invoice's details, status history and attachment download links.** Downloading an attachment follows its returned link as part of the retrieval flow. These are two Sage invoice operations; the file transfer uses a further HTTP request to the returned URL.

| Product action | API name / existing ID | Input → result |
|---|---|---|
| Open or filter the invoice list | **Query e-invoices — RET-API-01** | `datasetId`, optional `filter` and `page[after]` → paginated `data[]`, invoice information, current status and attachment links. No status history is declared. INT-RCV02. |
| Open one selected invoice and access its attachments | **Retrieve e-invoice — RET-API-02** | `datasetId` and one `e-invoiceId` UUID → one `data` object, invoice details, current status, `history[]` including operation results/error codes, and attachment download links. Follow a link to obtain the file. INT-RCV03; INT-RCV01 §4. |

The usual screen flow is **Query → select invoice → Retrieve → follow an attachment link if needed**. RET-API-03 retains the file-transfer rules under their existing ID; it does not define a third Sage invoice endpoint. A caller that already has a qualified invoice ID can retrieve directly. Query already includes invoice information and file links; a detail call is needed only when the caller needs additional information or a renewed link. Qualify the list-to-detail ID mapping below before using it. INT-RCV02/03; RET-G01/04.

| ID / operation or flow step | Use in this feature | Spain qualification | Functional link |
|---|---|---|---|
| [RET-API-01 — Query e-invoices / list](#ret-api-01) | Supply invoices for the required public/private list view; recover missed notifications within qualified query coverage. | Inbound/source selection, business mapping and historical coverage. RET-G01/03. | SPEC026 §2; RSD-03; RRI-A04 |
| [RET-API-02 — Retrieve e-invoice / detail](#ret-api-02) | Supply selected invoice information, status/history and file descriptors. | Public/private support, source identity and role mapping. Metadata alone is not a readable document. RET-G01/04/07. | SPEC026 §2; RSD-07; RCV-02 |
| [RET-API-03 — Follow attachment link (file-transfer step)](#ret-api-03) | Obtain bytes using a link returned by Retrieve or Query; assess reuse for SPFE user download from saved files. | Prove that the link returns the selected captured file under current authority. Private user download remains TBD. RET-G04/05/10. | RSD-04/07; RRI-A05/08 |
| [RET-API-04 — Subscription/event](#ret-api-04) | Accelerate discovery where supported. Required view does not depend on webhook availability. | Selected source/environment, permissions, event contract and missed-event recovery. RET-G02/03. | PRI-02; RRI-A02/04/09 |
| [RET-API-05 — Optional readable file](#ret-api-05) | Assess an optional readable representation. | Factur-X generation is not selected by the required view outcome. Spain need and existing rendering options remain RET-G08. | RRI-A06; RCV-I05 |

Resolve `datasetId` from the qualified SXS/onboarding binding. Keep the business, caller, source and environment explicit. Obtain invoice IDs from qualified list/event results. Neither a known ID nor an existing connection grants permission. [Onboarding GAP-01/02/06](../../onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#2-open-engineering-decisions) remains authoritative for setup/resource relationships. Do not create another dataset or connection to read an invoice. REF-TERMS.

### Shared request and recovery rules

INT-RCV02/03 declare Sage ID M2M bearer JWT authentication for both GETs. `traceparent` and `tracestate` are optional; neither GET declares `Idempotency-Key`. INT-RCV01 permits Domain Services or Sage ID M2M tokens in its introduction but describes Network-token login in the subscription table. Confirm accepted caller/token scope per operation and resolve guide differences; do not copy subscription headers to GETs. RET-G01/02.

For `429`, honour valid `Retry-After`; no fixed quota or polling interval is supplied. Preserve history `operationStatus` values `IN_PROGRESS`, `COMPLETED`, `ERROR`. Read the correlated attempt's `history[].errorCode`; `currentStatus` has neither field. A final attempt error is not a failed business invoice or an instruction to recapture. Keep the code-specific platform retry/support owner from INT-ERR01. RET-G02/09.

<a id="ret-api-01"></a>

### 1.1 RET-API-01 — Query e-invoices (list)

`GET /datasets/{datasetId}/e-invoices` · INT-RCV02; INT-RCV01 §3.2.

| Contract element | Documented result / limit |
|---|---|
| Request | Required `datasetId`; optional OData `filter` and `page[after]`. INT-RCV02 examples cover `erpInvoiceId`, `createdAt`, `customizationId`, `recipient/accessPointAddress` and `currentStatus/statusCode`. Additional guide filters and conflicting dot/slash examples need runtime qualification. |
| Response | `200`; `data[]` with `attributes.documents[]`. Each document can contain `eInvoiceId`, parties, totals, current status and `attachments[].downloadUrl`. No `history[]` is declared. The older guide list example omits URLs; that omission does not require a detail call before every download. INT-RCV02 `GetInvoicesResponse` / `InvoicesResponse`. |
| Page / range | `meta.count`, `meta.hasMore`, `links.self`, `links.next` are in INT-RCV02. Up to 20 items/page and a 90-day creation window are guide statements, not specified limits in the supplied OpenAPI. Qualify them against the selected build. Neither establishes retention or complete historical coverage. |
| Invoice identity | The list example has different outer `data[].id` and nested `documents[].eInvoiceId` values. Neither contract explains this relationship. Confirm which value binds the detail path and how multiple documents map to the list before activation. RET-G01. |
| Direction | Both sent and received codes can appear. Qualify `AP_Invoice`, `AR_Invoice`, `AP_CreditNote`, `AR_CreditNote`, self-billing and the selected source. Do not present every dataset result as received. |

**Request — documented path, synthetic dataset ID:**

```http
GET /datasets/00000000-0000-4000-8000-000000000001/e-invoices
```

<span style="color:#1565C0;">Reuse for the public/private list view; preserve the returned invoice IDs and source context. Supply SPFE freshness/collection results through a qualified existing or extended product contract.</span> <span style="color:#B42318;">The guide does not define that freshness contract, stable ordering, snapshot behaviour, continuation expiry or older-than-90-day access. Do not infer an empty complete history from this call. RET-G01/03/05.</span>

### 1.2 RET-API-02 — Retrieve e-invoice (detail)

<a id="ret-api-02"></a>

`GET /datasets/{datasetId}/e-invoices/{e-invoiceId}` · UUID path parameters · INT-RCV03; INT-RCV01 §3.1.

```http
GET /datasets/00000000-0000-4000-8000-000000000001/e-invoices/00000000-0000-4000-8000-000000000002
```

| Response field / group | Use / limit |
|---|---|
| `data.id` | INT-RCV03 declares one `data` object with `id`; invoice fields sit directly in `data.attributes`. The older guide field table also lists `data.attributes.eInvoiceId`; the supplied detail schema does not. Resolve the Query document-ID mapping under RET-G01. |
| `eInvoiceTypeCode`, `sender`, `recipient`, `accessPointId`, `erpInvoiceId` | Invoice type, parties and source/product references. `erpInvoiceId` is not a universal duplicate key. |
| `currentStatus`, `history[]`, `data.meta` | INT-RCV03 adds `currentStatus.statusAttributes` and declares history fields `operationStatus`, `errorCode`, `statusAttributes` and attempt metadata. `data.meta` is required. Neither history ordering nor full attempt correlation is supplied. Viewing does not create buyer acceptance. |
| File descriptors | `filename`, `mimetype`, `filetype`, `downloadUrl`. INT-RCV03 includes `Undefined`, `UBL`, `Human_Readable`, `Original_Document`, `FacturX`; map these values to saved business file roles. |
| Tax detail | VAT totals and tax breakdowns are not exposed as extracted fields in the guide. Use the qualified structured representation and inbound mapping where the product view needs them. RET-G07. |

**Response `200` — one attachment descriptor extract; container/schema not asserted:**

```json
{
  "filename": "synthetic-original.xml",
  "mimetype": "ubl-2.1/xml",
  "filetype": "Original_Document",
  "downloadUrl": "{shortLivedDownloadUrl}"
}
```

The MIME string above is a guide example, not the Spain public format. <span style="color:#1565C0;">Qualify public UBL 2.5 and the original/public-copy/derived mapping. Use detail information to build the required view for both source types.</span> <span style="color:#B42318;">A detail GET supplies data and links; it does not prove document rendering, saved-record storage or Spain service support. RET-G01/04/05/07.</span>

<a id="ret-api-03"></a>

### 1.3 RET-API-03 — Follow attachment link (file-transfer step)

`GET {downloadUrl}` · INT-RCV01 §4.

This step follows an attachment link returned by Retrieve or Query. The existing ID records transfer and recovery rules; the supplied OpenAPI definitions do not define a separate Sage attachment-download endpoint. The Retrieve response is JSON with links; following a link returns the actual file.

```http
GET {shortLivedDownloadUrl}
```

`200` returns bytes. The guide says the URL is short-lived and presigned; send **no `Authorization` header** to the file host. Capture bytes promptly. Do not retain the URL in durable records, logs or events. An expired link can return `403`; only confirmed expiry justifies reading detail again for a fresh link. Other refusals need their own cause/action.

<span style="color:#1565C0;">For SPFE user download, reuse this call only if it returns the selected captured file with current actor/file permission, correct role and integrity. Preserve good files when a required file is missing. Keep ordinary saved reads independent of SPFE availability and downstream mapping/product receipt.</span>

<span style="color:#B42318;">The guide does not establish immutable attachment identity/version/hash, allowed host/redirect rules, byte-range resume, storage ownership or historical saved-read access. A presigned link alone does not close these gaps. Identify an existing records contract before proposing an endpoint extension. Private user download remains TBD; this does not prevent a qualified backend source fetch. RET-G04/05/10.</span>

<a id="ret-api-04"></a>

### 1.4 RET-API-04 — Subscribe and receive an event

`POST /internal/events/subscriptions` → `201` · INT-RCV01 §§1–2. The guide labels the result `201 OK`; only code `201` is retained here.

| Supplied information | Use / unresolved point |
|---|---|
| Scope | Resource `einvoice`, event `e-invoicing.einvoice.received`, `accountId`, `datasetId`, selected source/environment and optional OData filter. Do not copy France source `sage.pdp.france` to Spain. |
| Callback | `audience`, `endpoint`, `endpointType: https`, optional `opaqueToken` and `clientstate` (maximum 256 characters). Caller access and notification authentication remain unqualified. |
| Event | `subject` supplies the invoice ID; context includes `id`, `subscriptionid`, `accountid`, `datasetid`, `source`, `time`, `traceparent` and nullable `data.errorCode`. Verify scope/authenticity and errors before detail retrieval. |
| Source conflicts | Request `Data/Type/Attributes/Scope` versus lowercase; `opaqueToken` versus `opaquetoken`; subscription event name differs from notification example `com.sage.network.e-invoicing.api.einvoice.received`. |

<span style="color:#B42318;">No safe complete subscription payload, webhook response deadline, replay contract or versioned event schema can be selected from these conflicts. Obtain the Events Library and selected schema. A public SPFE webhook is not established. RET-G02.</span> Notification receipt does not prove source capture or authorize a destructive source acknowledgement. RRI-A02/04/09.

<a id="ret-api-05"></a>

### 1.5 RET-API-05 — Optional readable representation

`GET /datasets/{datasetId}/e-invoices/{e-invoiceId}?format=facturx` · INT-RCV03 `parameters.format`; INT-RCV01 §§3.1/4.

INT-RCV03 says `format=facturx` generates and persists a Factur-X/ZUGFeRD 2.3 hybrid from UBL/PDF attachments, or returns an existing `FacturX` attachment without regeneration. INT-RCV01 describes `Human_Readable`; confirm the selected build's file-role mapping. This is a derived representation. The supplier's Factur-X can separately be `Original_Document`; returned UBL is not necessarily the supplier's original bytes.

<span style="color:#1565C0;">Required invoice viewing can reuse qualified product detail displays or readable representations.</span> <span style="color:#B42318;">Do not select this France generation option as the Spain viewer by default. Confirm actual renderer/build, required content, unsupported formats and independent rendering errors under RET-G08. Ordinary detail/saved-file access does not request generation.</span>

## 2 Spain public source calls

These backend SPFE SOAP operations support RSD-03 discovery/source acquisition and RSD-04–06 capture/progress. Each uses HTTP POST at the selected WSDL service address. The catalogue establishes business purpose and limits; missing formats remain open. Keep `QUERYBYFILTER` and other ebMS actions separate from HTTP `soapAction` URIs. SPFE-S03/S08/S12–15.

The supplied SPFE baseline establishes no webhook or WebSocket interface. These operations require Sage-initiated calls. Product-facing Query/Retrieve calls do not define a trigger for fresh SPFE collection. [SPEC027 §3.1](../SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#31-query-coverage-and-recovery) owns the France comparison, scheduled baseline, proposed list-open refresh and Architecture's cadence/rate-limit decisions. REF-EVIDENCE; RET-G03/06.

| ID / exact operation | Request → result / evidenced limit | Remaining Spain binding |
|---|---|---|
| RET-SPFE-01 — `GetRegisteredInvoice` | `QUERYBYFILTER`: recipient/issuer role and presentation-date filters in `MessageProperties` → `DocumentStatus`; maximum 1000 results, pagination key `SECUENCE_ID`. | Exact property names/types, date boundaries, ordering, complete continuation and recipient authority. The singular operation name is exact. |
| RET-SPFE-02 — `GetInvoices` | `QUERYBYID`: role and invoice identities → invoice metadata/final issuer/recipient states in `DocumentStatus`; maximum 1000 identifiers. | Identity encoding and response mapping. This is not date discovery, a source file or a full lifecycle-history contract. |
| RET-SPFE-03 — `DownloadInvoicesByLOC` | `DOWNLOADBYLOC`: one `ApplicationResponse` with locator-based `DocumentReference` entries → `InvoiceType` files. Catalogue prefers this route. | Locator/NIU encoding and certificate/representation checks. No LOC batch limit is supplied; do not copy the ID limit. |
| RET-SPFE-04 — `DownloadInvoicesByID` | `DOWNLOADBYID`: one `ApplicationResponse` with invoice `DocumentReference` entries → `InvoiceType` files; maximum 100 invoices. Failed references have distinct errors. | Exact ID/role binding, item/file correlation, partial outcomes and read effects. The ID is issuer NIF + series/number + issue date, not a Sage UUID. |

### 2.1 Transport and address selection

SPFE-S12–15 define certificate ports under `https://prewww1.aeat.es/wlpl/SPFE-FACT/ws/` and seal ports under `https://prewww10.aeat.es/wlpl/SPFE-FACT/ws/`. Append the exact suffix below. These are supplied PRE addresses; neither runtime access nor a production address is qualified.

| Operation | Exact suffix | HTTP action URI |
|---|---|---|
| `GetRegisteredInvoice` | `GetRegisteredInvoiceSOAP` | `https://www.agenciatributaria.gob.es/spfe/ns/services/GetRegisteredInvoice/v1/GetRegisteredInvoice` |
| `GetInvoices` | `GetInvoicesSOAP` | `https://www.agenciatributaria.gob.es/spfe/ns/services/GetInvoices/v1/GetInvoices` |
| `DownloadInvoicesByLOC` | `DownloadInvoicesByLOCSOAP` | `https://www.agenciatributaria.gob.es/spfe/ns/services/DownloadInvoicesByLOC/v1/DownloadInvoicesByLOC` |
| `DownloadInvoicesByID` | `DownloadInvoicesByIDSOAP` | `https://www.agenciatributaria.gob.es/spfe/ns/services/DownloadInvoicesByID/v1/DownloadInvoicesByID` |

Use SOAP 1.2, an empty SOAP body and `eb3:Messaging` in the header. The SOAP part uses `application/soap+xml` with `action` equal to the selected `soapAction`. With attachments, it sits in `multipart/related`, `type="application/soap+xml"`. Match each `PartInfo/@href="cid:..."` to its MIME `Content-ID`; the WSDL declares no generic `payload` part. Zero-to-many transport attachments do not override operation-specific business minima/limits. SPFE-S12–15; [SPEC011 transport rules](../../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding).

Standard SOAP 1.2 faults use `env:Code/env:Value` and `env:Reason/env:Text`, no service-specific `env:Detail`, HTTP 400 or 500. Catalogue download-error wording and business result levels still need reconciliation. Do not use removed custom fault fields or treat HTTP success as proof that every requested file was captured. RET-G06; SPFE-S03/S08/S12–15.

### 2.2 Deliberately incomplete business binding

SPFE-S08 §§5.4–5.7 mark query/download formats pending. The WSDLs treat business attachments as opaque; they do not define the missing filter names, full `DocumentReference` structure, locator encoding, item-error payloads or continuation guarantees. Therefore this reference supplies **no executable XML business payload**. Obtain the original business schemas/examples and qualify them before enabling collection. RET-G06.

For recipient work, check representation separately from certificate validity. Issuer/social-collaborator and locator/certificate branches cannot be reused as proof of recipient permission. Qualify the selected role and operation before making calls. RSD-R01; SPFE-S02 Articles 9–11; SPFE-S03 §§6.4–6.7.

## 3 Reuse decisions and additional work

| Capability / pattern | Reuse direction and local change | Owner / evidence gate |
|---|---|---|
| Public/private invoice view | Prefer existing E-Invoice list/detail and product display capabilities. Add only missing Spain source/role/freshness bindings. | API, Product, Identity: selected build/schema, authorised same-environment examples and historical-view coverage. RET-G01/03/05. |
| SPFE user download | Prefer existing file/records capability. Prove that selected links return captured, labelled files under current authority. | Records, API, Security: actual build, saved-file binding, restore/history and access evidence. RET-G04/05. |
| Private user download | **TBD:** do not turn a backend provider fetch or an existing France file endpoint into a product commitment. | Product/Compliance with Records and provider owners: decision and affected roles/use cases. RET-G10. |
| Public collection | Reuse the shared capture/progress/recovery design, with the qualified Spain SOAP binding. Actual implementation reuse remains unknown. | Connector/API/Identity: current client build, missing business contracts, authority, partial results and recovery proof. RET-G06. |
| Private intake | Prefer proven notification/fetch or supplied-file handling. Product-facing RET-API calls do not establish a provider-owned download contract. | Integration/provider: selected provider operation, bytes/role provenance, authority and acknowledgement/history. RET-G01/02/04. |
| Inbound mapping / readable display | Assess existing DTS first for the required input/output pair and tax/extension meaning. Keep rendering as a separately qualified capability. | DTS, Format, Product: actual build, Spain UBL/profile mappings, fixtures, loss checks and run owner. RET-G07/08. |

No source establishes a new product view, freshness, refresh, saved-read or rendering endpoint. Architecture/API owners must identify existing coverage, then specify only the required extension. Demonstrate country-rule isolation and existing-country compatibility; Spain identity, public-copy, authority and UBL rules must not become shared defaults. SPEC027 RET-API-A01–10 owns qualification acceptance.

## REF Source references

| REF ID | Original source / version | Exact location | Supported claims and limits |
|---|---|---|---|
| REF-SCOPE | [SPEC026](../SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#1-purpose-actors-and-boundary), draft, 30 October 2026 | Scope table; REF-SCOPE | Recorded user decision: public/private view required, SPFE user download required, private user download TBD. Not external legal evidence. |
| REF-PRODUCT | [PRD211](../../../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md), draft, updated 20 October 2026; [PRD223](../../../prds/PRD-SEI-223-interoperability-routing-transformation.md), updated 7 October 2026 | PRD211 FR30–33/43–55; PRD223 FR17–20/43–44 | Public freshness, exact source capture, authorised access and distribution; shared receiving/DTS direction. Not a wire contract. |
| INT-RCV01 | [Supplied receiving guide extract](<../../../context/FR API/Receiving/receive-e-invoice-guide-extract.md>), received 22 October 2026; revision/build unknown | Prerequisites; §§1–4; Polling, formats, and extracted data | Guide call paths, IDs, query limits, temporary-file and optional Factur-X flow. Original attachment hash retained. Reconcile with INT-RCV02/03; no source URL or Spain support established. |
| INT-RCV02 | [Supplied Query e-invoices OpenAPI](<../../../context/FR API/Receiving/query-e-invoices.openapi.json>), OpenAPI 3.1.0, info.version 1.0.0; received 2 November 2026 | `GET /datasets/{datasetId}/e-invoices`; `parameters.filterQuery/pageAfter`; `GetInvoicesResponse`; `InvoicesResponse`; 200 example | Paginated list, nested documents, current status and file links. Example ID relationship is unresolved. No deployed build, exhaustive filter support, page-size/window limit or Spain readiness established. |
| INT-RCV03 | [Supplied Retrieve e-invoice OpenAPI](<../../../context/FR API/Receiving/retrieve-e-invoice.openapi.json>), OpenAPI 3.1.0, info.version 1.0.0; received 2 November 2026 | `GET /datasets/{datasetId}/e-invoices/{e-invoiceId}`; `parameters.format`; `GetInvoiceResponse`; `InvoiceResponse`; `invoiceCurrentStatus`; `invoiceHistoryItem` | Single detail object, history/error fields, file links and optional persisted Factur-X generation. Original JSON bodies retained from supplied fenced text; no canonical publication URL, deployed build or Spain support established. |
| INT-ERR01 | [Supplied error guide extract](<../../../context/FR API/Shared/invoice-flow-error-handling-guide-extract.md>), received 22 October 2026; revision/build unknown | Processing and error fields; receiving dictionaries; Recovery interpretation | Attempt outcomes, history/error locations and platform-owned retry/support guidance. Not AEAT errors or universal retry timing. |
| SPFE-S02 | [Final Order HAC/1028/2026](../../../context/BOE-A-2026-20587.pdf), published 5 October 2026 | Articles 9–11, PDF pp. 9–11; Annex I BT-23/24 | Recovery, access, representation and profile baseline. Not product endpoint, retention duration or missing business schemas. |
| SPFE-S03 | [Original catalogue](<../../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), v0.1.0, 9 October 2026 | §§6.4–6.7, PDF pp. 12–15 | Exact ebMS actions, business purposes, role branches, date/identity/LOC limits and source result descriptions. Locator path has a duplicated `ws/`; WSDL supplies exact address. Business error semantics need reconciliation. |
| SPFE-S08 | [Original formats](<../../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), v0.1.0, 9 October 2026, BORRADOR | §5.1.1 p. 8; §§5.4–5.7 pp. 14–15 | UBL 2.5 InvoiceType/ApplicationResponse/DocumentStatus selection; query/download formats pending. Not complete payload schemas. |
| SPFE-S12 | [DownloadInvoicesByID.wsdl](<../../../context/WSDL servicios web - PRE_29:10:2026/DownloadInvoicesByID.wsdl>), PRE 29 October 2026 | `documentation`, messages, portType/binding operation, SOAP action and service ports | Exact ID-download transport. Does not establish missing business payload or live acceptance. |
| SPFE-S13 | [DownloadInvoicesByLOC.wsdl](<../../../context/WSDL servicios web - PRE_29:10:2026/DownloadInvoicesByLOC.wsdl>), PRE 29 October 2026 | Same named elements for `DownloadInvoicesByLOC` | Exact locator-download transport; no inferred LOC batch limit or recipient permission. |
| SPFE-S14 | [GetInvoices.wsdl](<../../../context/WSDL servicios web - PRE_29:10:2026/GetInvoices.wsdl>), PRE 29 October 2026 | Same named elements for `GetInvoices` | Exact identity-query transport. Opaque attachments do not complete business schema. |
| SPFE-S15 | [GetRegisteredInvoice.wsdl](<../../../context/WSDL servicios web - PRE_29:10:2026/GetRegisteredInvoice.wsdl>), PRE 29 October 2026 | Same named elements for singular `GetRegisteredInvoice` | Exact filter-query transport, header-only messages and MIME documentation. Filter/continuation guarantees remain open. |
| REF-TERMS | [Glossary](../../../context/GLO-SEI-001-e-invoicing-terminology.md); [SPEC039](../../onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md), draft, updated 29 October 2026 | Invoice view/source-file/stored-file terms; GAP-01/02/06 | Shared meanings and setup mapping gates. No new dataset/entity or credential relationship inferred. |
| REF-EVIDENCE | [Source manifest](../../../assets/regulatory/spain/spfe/source-manifest.json); [release review](../../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-release-reviewed-29-october-2026) | `current_wsdl_baseline`; PRE review; SPFE-Q04/05/06/09/12–14/17 | Reviewed local release, hashes and remaining schemas/runtime/business gates. Not monitoring of later publications or production readiness. |
