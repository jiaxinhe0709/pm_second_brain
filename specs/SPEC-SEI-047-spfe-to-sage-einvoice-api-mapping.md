---
id: SPEC-SEI-047
title: SPFE SOAP to Sage E-Invoice API Mapping
type: api-reference
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-11-17
updated: 2026-11-18
reviewers: []
related:
  - RES-SEI-002
  - GLO-SEI-001
  - SPEC-SEI-005
  - SPEC-SEI-008
  - SPEC-SEI-011
  - SPEC-SEI-040
  - SPEC-SEI-041
  - SPEC-SEI-042
  - SPEC-SEI-043
  - SPEC-SEI-024
  - FP-SEI-002
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# SPFE SOAP to Sage E-Invoice API Mapping

An authorised business needs to send, find, view and download Spain invoices, report buyer or seller actions, and recover failed or uncertain requests. This reference maps the nine SPFE SOAP services to the existing Sage E-Invoice API surface. It links to the owning specifications for detailed fields, rules and acceptance checks.

**Proposed reuse direction:** retain the common Send, Query, Retrieve and status APIs, with qualified Spain rules and SPFE transport. Submission withdrawal has no documented equivalent in the supplied E-Invoice contracts. Service 09 is available only in sandbox/PRE and is excluded from the live production flow. Existing France contracts establish reuse candidates; deployed Spain implementation coverage remains unknown. REF-SND, REF-RCV, REF-LIF, REF-WITHDRAWAL; SPFE-S03 §6.10.

## 1 Service mapping

In the table, `{invoices}` means `/datasets/{datasetId}/e-invoices`. Sage calls are product-facing. SPFE calls communicate with AEAT. A mapping does not mean that each Sage call triggers one SOAP call, or that a saved read refreshes SPFE data.

| SPFE service / source | Actor and observable outcome | Existing Sage API or interaction | Spain mapping and authoritative detail |
|---|---|---|---|
| **01 — `SendInvoice`**; SPFE-S16 | Authorised sender submits the invoice or applicable public copy. | `POST {invoices}`; then `PUT {uploadUrl}` for each declared file. | [SPEC-SEI-043 §1.2](invoice-sending/api-reference/SPEC-SEI-043-invoice-sending-api-reference.md#12-proposed-per-invoice-identities-and-platforms) owns request fields and platform-selection semantics; its [contract baseline and reuse assessment](invoice-sending/api-reference/SPEC-SEI-043-invoice-sending-api-reference.md#contract-baseline-and-reuse-assessment) owns sending-specific API changes and gaps. [SPEC-SEI-024 §2.2](invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#22-spain-final-plan-and-independent-actions) owns delivery/copy interactions. |
| **02 — `CancelInvoice`**; SPFE-S10 | Authorised actor withdraws an eligible earlier SPFE submission. | **No documented equivalent.** | A distinct issuer action on the existing resource is proposed; endpoint, payload and result remain undecided. [FP-SEI-002 analysis and proposed direction](../feature-proposals/FP-SEI-002-global-api-submission-withdrawal.md#analysis-and-proposed-direction). |
| **03 — `GetInvoices`**; SPFE-S14 | Authorised issuer or recipient queries SPFE metadata and states by invoice identity. | `GET {invoices}/{e-invoiceId}` exposes the saved invoice and history. | Qualify external-to-Sage identity and state mapping. SPFE consultation does not establish full lifecycle history. [SPEC-SEI-042 public source calls](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#2-spain-public-source-calls) and [Retrieve contract](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#ret-api-02). |
| **04 — `GetRegisteredInvoice`**; SPFE-S15 | Authorised issuer or recipient discovers registered invoices using role/date filters. | `GET {invoices}` with qualified `filter` and `page[after]` values. | Reuse the list view after source collection. Qualify date meanings, freshness, coverage and independent SPFE continuation. [SPEC-SEI-042 Query contract](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#ret-api-01) and [public source calls](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#2-spain-public-source-calls). |
| **05 — `DownloadInvoicesByID`**; SPFE-S12 | Authorised actor obtains source invoice XML using external invoice identity. | Query or Retrieve returns `attachments[].downloadUrl`; `GET {downloadUrl}` returns bytes. | Source acquisition and user download are separate steps. Qualify file capture, invoice association, permissions and file role. [SPEC-SEI-042 file-transfer step](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#ret-api-03). |
| **06 — `DownloadInvoicesByLOC`**; SPFE-S13 | Authorised actor obtains source invoice XML using an SPFE locator. | Same Query/Retrieve and download-link flow as service 05. | The locator selects the SPFE source file; it is not a Sage UUID or download URL. [SPEC-SEI-042 public source calls](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#2-spain-public-source-calls). |
| **07 — `CustomerInvoiceEvents`**; SPFE-S11 | Buyer reports payment or commercial rejection, or retracts its earlier report. | `POST {invoices}/{e-invoiceId}/status`. | Conditional reuse of buyer lifecycle actions. [SPEC-SEI-041 action and destination mapping](invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#spfe-action-mapping) owns all buyer event codes, UUID candidates and gaps. |
| **08 — `SupplierInvoiceEvents`**; SPFE-S17 | Seller reports collection or non-payment, or retracts its earlier report. | `POST {invoices}/{e-invoiceId}/status`. | Conditional reuse of seller lifecycle actions for enabled scope. [SPEC-SEI-041 action and destination mapping](invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#spfe-action-mapping) owns all seller event codes, UUID candidates and gaps. |
| **09 — `ValidationInvoice` (sandbox/PRE only)**; SPFE-S23; SPFE-S03 §6.10 | Caller checks one UBL invoice in sandbox/PRE without registering it. | **No live production mapping: SPFE does not provide this service in production.** | Optional sandbox/PRE conformance aid; never a live production dependency. Sage final-file validation remains separate. [SPEC-SEI-005 SPFE source contract binding](SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md#spfe-source-contract-binding), UV-SPFE-R03, owns its use and limits. |

## 2 Customer and supplier roles

For normal sales and purchase flows, an ERP **supplier/purchase invoice** places the connected business in the buyer role and maps to `CustomerInvoiceEvents`. An ERP **customer/sales invoice** places it in the seller role and maps to `SupplierInvoiceEvents`. The service names identify the reporting party, not the ERP's invoice category. REF-EXAMPLES; REF-LIF.

For self-billing, preserve seller, buyer and material issuer separately under the [GLO-SEI-001 invoice definitions](../context/GLO-SEI-001-e-invoicing-terminology.md#invoices-representations-and-rules). The authenticated caller can represent a business; authentication alone does not grant buyer or seller authority.

Use [SPEC-SEI-041 input and XML field mapping](invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#spfe-field-mapping) for saved invoice references and event dates, reasons and indicators. It also defines the conditions for full-payment reporting. Its eight-action table remains the single mapping authority; the supplied API leaves five action bindings unassigned. Open `statusAttributes` proves JSON schema flexibility, not Spain execution support. REF-LIF.

## 3 Shared interactions and reuse qualification

| Area | Reuse direction, country change or gap | Accountable roles and existing acceptance |
|---|---|---|
| Setup | Access-point discovery and dataset connection APIs support setup; none of the nine SOAP services is an onboarding equivalent. Spain resource mapping and public readiness remain qualified separately. | API/Identity/Integration: [SPEC-SEI-040 existing calls and Spain limits](onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#1-existing-calls-to-reuse--phases-13). |
| Results and recovery | Reuse request receipts, notifications and invoice history where compatible. `POST /internal/events/subscriptions` is guide evidence, with access/schema gaps. A notification prompts a result read; neither Sage `201` nor HTTP success proves an SPFE business result. No SPFE webhook is established. | API/Events/Integration: [SPEC-SEI-041 existing calls and results](invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md#1-existing-calls-and-results) and [SPEC-SEI-042 subscription/event](invoice-receiving/api-reference/SPEC-SEI-042-existing-e-invoice-retrieval-api-reference.md#ret-api-04). |
| Spain transport and results | The reviewed WSDLs use SOAP 1.2. Services 01–08 carry UBL business documents as MIME attachments referenced by ebMS headers; service 09 uses direct SOAP bodies. Preserve transport faults, business response codes and per-invoice results separately. Exact transport/result rules stay in the connector specification. | Public Integration: [SPEC-SEI-011 source contract binding](SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding) and [response and error matrix](SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix). SPFE-S10–S17/S23. |
| Transformation | Assess existing DTS first for Spain invoice and event XML generation where transformation is needed. Qualify its actual build, contracts, executable mappings, rule packs and operations. Saved UBL 2.5 viewing does not itself require conversion. | DTS/Format: [SPEC-SEI-008 DTS specification](SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) and [SPEC-SEI-030 field coverage and DTS qualification](invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md#32-spain-field-coverage-against-the-french-guide). |
| Activation and country isolation | Demonstrate Spain identity, route, file, action and result bindings without changing France rules. Resolve withdrawal and missing action contracts before enabling them. Record the selected build and positive, negative and recovery evidence for each enabled service. | API/Architecture/Spain/Integration: [SPEC-SEI-024 sending checks](invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#5-api-qualification-checks), [SPEC-SEI-027 retrieval checks](invoice-receiving/SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#5-api-qualification-checks) and [SPEC-SEI-030 lifecycle acceptance](invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md#5-api-qualification-acceptance). |

## 4 Evidence status

The manifest selects the locally reviewed **29 October 2026 PRE WSDL release**. The source check currently fails because registered paths SPFE-S04–S08 are absent after local example/formats moves. The supplied examples at REF-EXAMPLES are not registered local snapshots in that manifest. This draft does not qualify a new release or production implementation. REF-BASELINE.

The example conflicts remain in [RES-SEI-002 specification impact](../context/RES-SEI-002-spain-public-platform-technical-evidence.md#spfe-example-review-and-specification-impact): buyer `PAYMENT` paired with seller wording, SOAP 1.1 event requests against SOAP 1.2 WSDLs, inconsistent dates, and download identity/correlation mismatches. Public Integration and the AEAT liaison need corrected fixtures and governing business schemas before executable conformance can be claimed. REF-EXAMPLES; REF-BASELINE.

## REF Source references

| Source ID | Original file and version/date | Exact locator, supported claim and limit |
|---|---|---|
| REF-BASELINE | [Source manifest](../assets/regulatory/spain/spfe/source-manifest.json), `current_wsdl_baseline`, reviewed 29 October 2026; [RES-SEI-002 release review](../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-release-reviewed-29-october-2026), updated 11 November 2026. | Selected local transport release, known missing schemas and example conflicts. Does not monitor later AEAT releases or prove runtime access. SPFE-S04–S08 registered paths are currently missing. |
| SPFE-S03 | [Original service catalogue](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), version 0.1.0, 9 October 2026. | §§6.10.2–6.10.3, pp. 19–20: validation is available only in PRE, is unavailable in production and does not register the invoice. The catalogue's older `InvoiceValidationSOAP` spelling does not replace SPFE-S23's reviewed operation name. |
| SPFE-S16 / SPFE-S10 | [SendInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/SendInvoice.wsdl>); [CancelInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/CancelInvoice.wsdl>), reviewed PRE release 29 October 2026. | Named `portType` operations, input/output messages, SOAP 1.2 documentation, bindings/actions and certificate/seal ports. Opaque business attachments do not establish a complete business schema or Sage support. |
| SPFE-S14 / SPFE-S15 | [GetInvoices WSDL](<../context/WSDL servicios web - PRE_29_10_2026/GetInvoices.wsdl>); [GetRegisteredInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/GetRegisteredInvoice.wsdl>), same reviewed release. | Named operations, messages, binding/actions and ports. Business purpose and unresolved field semantics are maintained in SPEC-SEI-042 §2 against its catalogue sources. |
| SPFE-S12 / SPFE-S13 | [DownloadInvoicesByID WSDL](<../context/WSDL servicios web - PRE_29_10_2026/DownloadInvoicesByID.wsdl>); [DownloadInvoicesByLOC WSDL](<../context/WSDL servicios web - PRE_29_10_2026/DownloadInvoicesByLOC.wsdl>), same reviewed release. | Named download operations, ebMS/MIME transport, faults and ports. Neither establishes Sage saved-file access or complete identity/locator encoding. |
| SPFE-S11 / SPFE-S17 | [CustomerInvoiceEvents WSDL](<../context/WSDL servicios web - PRE_29_10_2026/CustomerInvoiceEvents.wsdl>); [SupplierInvoiceEvents WSDL](<../context/WSDL servicios web - PRE_29_10_2026/SupplierInvoiceEvents.wsdl>), same reviewed release. | Named event operations, messages, transport and ports. Business event/action and field mapping remain in SPEC-SEI-041 against its Annex II sources. |
| SPFE-S23 | [ValidationInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/ValidationInvoice.wsdl>), same reviewed release. | `ValidationInvoiceRequest` part `ubl:Invoice`, response part `ublds:DocumentStatus`, direct-body documentation and SOAP binding. Referenced UBL business schemas remain missing locally. PRE use is bounded by SPEC-SEI-005 UV-SPFE-R03. |
| REF-SND | [Supplied Send OpenAPI](<../context/FR API/Sending/send-e-invoice-openapi.md>), OpenAPI 3.1.0, API 1.0.0; [supplied sending guide extract](<../context/FR API/Sending/send-e-invoice-guide-extract.md>), received 22 October 2026. | `Send-Document`, POST request/response; guide steps 2–5 establish upload, events and reads. France-oriented evidence; Spain values, runtime and file support need qualification. SPEC-SEI-043 owns detailed reuse proposals. |
| REF-RCV | [Query OpenAPI](<../context/FR API/Receiving/query-e-invoices.openapi.json>); [Retrieve OpenAPI](<../context/FR API/Receiving/retrieve-e-invoice.openapi.json>), OpenAPI 3.1.0, API 1.0.0; snapshots received 13 November 2026. | `Query-Invoices`, `Retrieve-Invoice`, filters, pagination, attachment links and detail history. No implicit fresh SPFE collection or deployed Spain support. SPEC-SEI-042 owns field mappings and conflicts. |
| REF-LIF | [Status OpenAPI](<../context/FR API/Lifecycle/update-e-invoice-status.openapi.json>), OpenAPI 3.1.0, API 1.0.0, received 28 October 2026; [lifecycle guide extract](<../context/FR API/Lifecycle/lifecycle-api-guides-evidence-extract.md>), received 22 October 2026. | `LifecycleChange-Document`, `InvoiceStatusRequest`, `InvoiceStatusResponse`; guide INT-LCS01–05. Existing status shape, event/read pattern and France actor catalogue; not executable Spain action bindings. SPEC-SEI-041 owns the proposed eight-action mapping. |
| REF-WITHDRAWAL | [FP-SEI-002 analysis and proposed direction](../feature-proposals/FP-SEI-002-global-api-submission-withdrawal.md#analysis-and-proposed-direction), draft updated 12 November 2026. | Canonical proposed withdrawal direction and Architecture decision boundary. No approved endpoint, payload or delivery commitment. |
| REF-EXAMPLES | [Supplied service examples 01–09](<../context/Descripción servicios web/Ejemplos de peticiones y respuestas de SW/>), local collection inspected 17 November 2026; publication version unverified. | Numbered request/response folders illustrate invoice submission, cancellation, query, download, buyer `Pagar.xml`, seller `Cobrada.xml` and validation. Examples are not complete contracts; local snapshots are not registered in the source manifest. |
