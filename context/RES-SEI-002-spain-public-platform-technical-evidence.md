---
id: RES-SEI-002
title: Spain public platform technical evidence guide
type: research
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-13
updated: 2026-10-20
reviewers: []
related:
  - RES-SEI-001
  - GLO-SEI-001
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-004
  - SPEC-SEI-005
  - SPEC-SEI-006
  - SPEC-SEI-007
  - SPEC-SEI-008
  - SPEC-SEI-009
  - SPEC-SEI-010
  - SPEC-SEI-011
  - SPEC-SEI-012
  - SPEC-SEI-014
  - SPEC-SEI-015
  - SPEC-SEI-016
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Spain public platform technical evidence guide

The supplied AEAT technical bundle supports initial offline work on the Spain public platform POC. It describes submission, consultation, download, cancellation and invoice events. It does not establish a complete or tested production contract. The input/output formats document is marked **BORRADOR**, meaning **draft**, and contains seven service sections pending publication.

The original supplied files are the **source evidence baseline** for external Spain public-platform behaviour. The final BOE order governs legal requirements. The catalogue, formats, WSDLs and XSDs govern the technical facts each establishes. Examples illustrate particular messages. Earlier product assumptions must be reconciled with this evidence. Sage architecture, internal states, recovery controls and product scope remain proposed choices. A conflict between source files remains an open gate; this guide does not resolve it by preference.

This English guide links all 21 supplied files: four PDFs, eight WSDLs, four XSDs and five XML examples. The PDFs contain 112 pages. Their Spanish text is searchable in the [extracted source folder](../assets/regulatory/spain/spfe/). The original files remain authoritative. This guide translates key findings; it is not a complete or official English translation.

Use the [existing legal evidence note](../research/spain-public-platform-order-evidence.md) for the published order and the [shared glossary](GLO-SEI-001-e-invoicing-terminology.md) for project terminology. The technical release adds evidence to those sources. It does not approve the current PRDs, solution specs, country rules or implementation.

## How to use this context

Keep the complete sources in the repository. Start a Spain review with this guide, then read the pages and contracts relevant to that feature. Do not paste all 112 pages into every chat. Files in `context/` are persistent evidence; they are not automatically loaded into every conversation.

| Task | Read next |
|---|---|
| Legal scope, public-copy duties or dates | Existing legal evidence note, the final BOE order and the official calendar linked below. |
| Connector or transport POC | Service catalogue sections 3–6; formats sections 4–5; the selected WSDL and its XSD imports. |
| Invoice mapping or validation | Invoice Annex I; final BOE Annex I; formats section 5.1.1; the two invoice examples. |
| Retrieval and download | Catalogue sections 6.4–6.7; `GetRegisteredInvoice`, `GetInvoices` and download WSDLs. |
| Status and payment reporting | Final BOE Annex II; catalogue sections 6.8–6.9; both event WSDLs. |
| Credentials or delegated authority | Final order Articles 9–11; catalogue authorization text for the selected operation; the WSDL certificate ports. |

**Confirmed in supplied evidence** means that a statement appears in the local source. It does not mean that the operation has been tested. **Confirmed legal evidence** means that the statement is supported by the published regulation. **Proposed** identifies a POC or review choice. **Open** identifies missing or conflicting evidence.

## Source authority and release status

| Source | Identity and date | Authority and limit |
|---|---|---|
| Final ministerial order | `BOE-A-2026-20587`, Order `HAC/1028/2026`; dated 2 October, published 5 October 2026; 42 pages. | Final legal source. Publication identity and entry into force were checked against the [official BOE text](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20587) on 13 October 2026. No byte-equality claim is made for the local PDF. |
| Separate invoice Annex I | `Anexo-1-Proyecto-OM-FE.pdf`; 34 pages; no explicit release version identified in the text. | AEAT-labelled invoice field and code tables. Its filename still contains `Proyecto`, meaning draft/project. Compare each relevant rule with the final BOE annex before binding it. The filename does not change the final order's legal status. |
| Service catalogue | `CatalogoServicios.pdf`; cover date 9 October 2026; version `0.1.0`; 21 pages. | Initial technical description of nine services, including a PRE-only validation service. Contains conflicts and incomplete details listed below. |
| Input/output formats | `FormatosEntradaSalida.pdf`; cover date 9 October 2026; version `0.1.0`; 15 pages. | Cover explicitly marks the initial version `BORRADOR`. Sections 5.3–5.9 are pending publication. |
| WSDL/XSD and XML examples | Files supplied in folders named `20261013`. | Contract and example evidence for the supplied snapshot. Folder date and the stakeholder update indicate receipt on 13 October; they do not prove each file's official publication date. |

The user supplied these files from the internal technical-documentation collection. The technical PDFs identify AEAT as author. Their public download provenance has not been independently verified. Do not label the entire bundle as a final production release. The [source manifest](../assets/regulatory/spain/spfe/source-manifest.json) records paths, sizes, SHA-256 hashes, page counts, WSDL ports and local schema references.

The supplied stakeholder update says technical documentation was released on 13 October 2026 and that pre-production availability remains TBC. Its older statement that technical specifications were pending describes the earlier legal-publication update. The actual files establish that technical material is now present; environment availability remains open.

## Implementation calendar

The [official AEAT calendar](https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html), checked on 13 October 2026, confirms the following dates. The invoice duty and reporting duty have different transitions.

| Obligation and group | Date |
|---|---|
| Ministerial order enters into force and starts the staged periods | 6 October 2026 |
| Issue and receive invoices: prior-year VAT volume of operations exceeds EUR 8 million | 6 October 2027 |
| Issue and receive invoices: remaining businesses and professionals, including exactly EUR 8 million | 6 October 2028 |
| Status/payment reporting: group above EUR 8 million | 6 October 2027 |
| Status/payment reporting: remaining legal persons/entities, subject to the special row below | 6 October 2028 |
| Status/payment reporting: remaining natural persons and income-attribution entities | 6 October 2029 |
| Specific private-platform obligations | 6 October 2027 |

The threshold uses the VAT volume-of-operations measure and the preceding calendar year. It is not simply any current turnover figure. Compliance must bind the correct group and exceptions to each customer. The [Royal Decree, final provision 4 and transitional provisions 2–3](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-7295), supplies the underlying rules. The large-business transition also requires a readable PDF for 12 months, unless the recipient expressly accepts the original format. That PDF must not be sent to SPFE.

## English guide to the transport contract

These findings come from the [catalogue](../assets/regulatory/spain/spfe/service-catalogue.es.txt), [formats document](../assets/regulatory/spain/spfe/input-output-formats.es.txt), WSDLs and supplied XML examples.

| Contract item | Meaning in this snapshot | Evidence and qualification |
|---|---|---|
| HTTPS and certificate access | Applications authenticate with a recognized qualified electronic certificate. | Catalogue section 4.3, p. 8. WSDLs expose separate certificate and electronic-seal ports. Certificate acceptance does not establish authority for the represented party. |
| SOAP | The service uses an XML request/response envelope. The WSDLs bind SOAP 1.2. | Catalogue p. 8 and sample envelope namespace agree. Formats p. 7 says SOAP 1.1; resolve this conflict. |
| ebMS 3.0 / ebXML | The SOAP header carries message identity, caller/receiver information, action and payload references. | Formats sections 5.1.2–5.2 and WSDL documentation. The WSDLs describe an empty SOAP body. |
| MIME `multipart/related` | Business XML documents travel as separate parts of the HTTP message. | The ebMS `PartInfo/@href` refers to the part's `Content-ID` through `cid:`. This is transport packaging, separate from prohibited files embedded inside an invoice. |
| UTF-8 | XML uses UTF-8 encoding. | Both technical PDFs, section 4.1. |
| UBL 2.5 | The formats document selects UBL version 2.5 business documents. | Formats p. 8: `InvoiceType` for invoices, including rectifications; `ApplicationResponse` for cancellation, actions and queries/download requests; `DocumentStatus` for responses other than invoice downloads. This is supplied technical evidence, not a successful conformance test. |
| Synchronous response | Each sent message receives a synchronous response. | Both technical PDFs, section 3. The response still requires per-document interpretation. It does not establish buyer acceptance or payment. |
| WSDL payload typing | Business attachments are opaque at the WSDL layer. | The WSDL imports the ebMS schema, not the UBL business schemas. One illustrative `payload` part does not restrict the actual message to one attachment. Validate business documents separately. |
| AS4 reference | The formats document describes a minimal ebMS/AS4-compatible approach without a cryptographic message signature. | Formats p. 9. This statement does not qualify full AS4/Peppol conformance or settle invoice-signing duties and security controls. |

All eight WSDLs expose these PRE address patterns:

```text
Electronic certificate, excluding electronic seal:
https://prewww1.aeat.es/wlpl/SPFE-FACT/ws/{Operation}SOAP

Electronic seal certificate:
https://prewww10.aeat.es/wlpl/SPFE-FACT/ws/{Operation}SOAP
```

`{Operation}` is an explanatory placeholder. Use the exact address and port from the selected WSDL. These addresses establish configured contract locations, not connectivity, credentials, live acceptance or production addresses.

## Service inventory

The names and actions below are exact technical values. `N` means several business documents; it does not mean an unlimited number. Each row uses catalogue sections 6.2–6.10, pp. 10–20, and the matching WSDL where supplied.

| Operation | ebMS `Action` | Request and response | Purpose and documented limit |
|---|---|---|---|
| `SendInvoice` | `SUBMITINVOICE` | N `InvoiceType` attachments → one `DocumentStatus`. | Submit originals or faithful copies. Catalogue: 1–100 invoices. Mixed issuers are described, with representation evaluated for each invoice. |
| `CancelInvoice` | `CANCELINVOICE` | One `ApplicationResponse` → one `DocumentStatus`. | Withdraw a previously submitted invoice in a permitted case. It is not a general substitute for a rectifying invoice. Exact multi-reference behavior needs confirmation. |
| `GetInvoices` | `QUERYBYID` | N `ApplicationResponse` attachments → one `DocumentStatus`. | Consult by invoice identity and issuer/recipient role. Maximum 1,000 invoice identifiers. Includes final issuer/recipient states. It does not return the invoice files. |
| `GetRegisteredInvoice` | `QUERYBYFILTER` | ebMS `MessageProperties` filters → one `DocumentStatus`. | Discover by SPFE presentation-date range and issuer/recipient role. Maximum 1,000 results, with pagination key spelled `SECUENCE_ID` in the catalogue. |
| `DownloadInvoicesByID` | `DOWNLOADBYID` | One `ApplicationResponse` with N `DocumentReference` entries → N `InvoiceType` attachments. | Download by invoice identity. Maximum 100 invoices. Catalogue recommends locator download for platforms. |
| `DownloadInvoicesByLOC` | `DOWNLOADBYLOC` | One `ApplicationResponse` with N locator references → N `InvoiceType` attachments. | Download by locator. Certificate/locator authorization is described separately. No separate numeric limit is stated in section 6.7; do not copy the ID-download limit without confirmation. |
| `CustomerInvoiceEvents` | `ACCOUNTINGCUSTOMERPARTYACTION` | One `ApplicationResponse` → one `DocumentStatus`. | Recipient payment/rejection reports and their cancellation. Maximum 100 states in one request. Do not mix supplier and customer events. |
| `SupplierInvoiceEvents` | `ACCOUNTINGSUPPLIERPARTYACTION` | One `ApplicationResponse` → one `DocumentStatus`. | Issuer collection/non-payment reports and their cancellation. Section 6.9 does not give a numeric batch limit. |
| `InvoiceValidation` | Not applicable | Direct XML `InvoiceType` → direct XML `DocumentStatus`. | Catalogue describes one-invoice PRE-only validation. No matching WSDL is supplied. It does not register or admit the invoice and is unavailable in production under this description. |

The catalogue's ninth service uses path `ws/InvoiceValidationSOAP`. Its exact HTTP/SOAP request packaging and certificate ports need evidence. Do not derive them from the eight attachment-based WSDLs.

`GetRegisteredInvoice` is singular in the WSDL, operation and endpoint. Preserve this spelling. The stakeholder update uses a plural name. `GetInvoices` is the identifier query; `GetRegisteredInvoice` is the date-filter query. Their names alone are insufficient to choose the discovery operation.

## Invoice fields and validation

The separate [invoice annex](../assets/regulatory/spain/spfe/invoice-annex.es.txt) records EN 16931 business terms (`BT`), groups (`BG`) and Spain extensions (`BT-ES`, `BG-ES`). It gives cardinality, meaning, semantic type and selected UBL paths. Conditional groups still have required fields when the group is used. Preserve exact IDs and code values in a mapping.

| Finding | Supplied evidence | Use and limit |
|---|---|---|
| Faithful-copy marker | Annex p. 4, `BT-ES-1`, `/in:Invoice/cbc:CopyIndicator`: `True` is a copy; `False` or absence is an original. | Preserve the source classification. The examples contain `false`; they do not supply a complete faithful-copy example. Use valid XML boolean serialization in the qualified profile. |
| Invoice identity | Catalogue sections 6.2–6.6: issuer NIF + series/invoice number + issue date. Final order Article 6 uses the same business elements. | Treat these as identity components. No complete separator/escaping/normalization contract is established by a plus sign in prose. `MessageId`, invoice identity and locator are different values. |
| Invoice document type | Formats p. 8 selects `InvoiceType`, not `CreditNote`. Annex pp. 27–28 lists invoice codes `380`, `384`, `388`, `389`, `471`. | Include the required rectification data for the selected invoice code. Do not convert every rectification into `CreditNote` from generic UBL assumptions. |
| Example `CustomizationID` | `urn:cen.eu:en16931:2026#conformant#urn:aeat.es:spfe:1.0.0:extended` | Exact value in both invoice examples. Preserve it as example evidence; qualify the accepted profile and its version. |
| Example `ProfileID` | `urn:aeat:names:specification:schema:profile:B2B` | Both examples omit `ubl:` from the value required by final Annex I BT-23: `urn:aeat:names:specification:ubl:schema:profile:B2B`. The separate annex agrees with the final order. Preserve the examples as supplied; SPFE-Q13 gates sample use and profile activation. |
| Validation layers | Catalogue pp. 10–11 and 19–20: XML syntax, EN 16931 semantics, then SPFE business rules. | The four supplied XSDs cover messaging/envelopes. They are not an invoice validator or a complete Spain rule pack. |
| Invoice size | Catalogue p. 11 states **5120 bytes per invoice**. | Preserve this exact published value as a disputed limit. The supplied invoice files are 5,376 and 5,390 bytes; even changing CRLF to LF leaves them above 5,120. Do not silently change the unit to KB or implement the limit as settled. |
| Embedded files and URL references | Catalogue p. 11 prohibits binary content in `cbc:EmbeddedDocumentBinaryObject` and `cbc:EmbeddedDocument`; it permits external URL references. | Separate invoice content restrictions from MIME business-document transport. Qualify URL/security policy and compare the final legal rule. Do not assume Sage should fetch external URLs. |

Annex coverage includes invoice data, supplier and recipient data, third parties, payments, tax breakdowns, allowances/charges, totals, invoice lines, supporting references, rectification data, withdrawal fields and code lists. The extracted text preserves all pages. Original tables are required for exact path and cardinality review because text extraction can split or interleave cells.

The separate invoice annex does not replace **Annex II**. The final BOE PDF includes Annex II for payment, rejection, collection, non-payment and cancellation communications. Use that annex together with the catalogue for lifecycle mapping.

## Raw event codes and outcome meanings

The following codes appear in final BOE Annex II and catalogue sections 6.8–6.9, pp. 16–19. Keep them unchanged in source records. These are communication codes; cancellation of a communication is separate from invoice withdrawal.

| Actor | `ResponseCode` | English meaning |
|---|---|---|
| Recipient | `PAYMENT` | Reports effective payment in full. |
| Recipient | `CANCELPAYMENT` | Cancels a previously reported payment. |
| Recipient | `REJECTION` | Reports commercial rejection. |
| Recipient | `CANCELREJECTION` | Cancels a previously reported commercial rejection. |
| Issuer | `SETTLEMENT` | Reports collection in full. |
| Issuer | `CANCELSETTLEMENT` | Cancels a previously reported collection. |
| Issuer | `DEFAULT` | Reports non-payment. |
| Issuer | `CANCELDEFAULT` | Cancels a previously reported non-payment. |

The catalogue does not allow partial payment or partial collection reports. The full-payment/collection report omits an amount. This restriction applies to SPFE reporting; it does not forbid Sage from recording partial payments internally.

Recipient payment and commercial rejection are mutually exclusive. Issuer collection and non-payment are mutually exclusive. The catalogue requires cancellation before correcting an earlier payment or collection report. Recover an uncertain cancellation result before sending its replacement. Issuer collection/non-payment is optional information; apply the confirmed country rules and customer transition to recipient reporting.

The final order describes presumed acceptance when there is no rejection or later rectifying invoice. The catalogue describes invoices as initially accepted. Preserve that legal/source view separately from explicit buyer acceptance, technical admission, delivery and payment. No four-day acceptance timer is established by these files.

The formats document, p. 14, gives request-level `ResponseCode` values: `200` for all correct, `406` for partial success and `400` for complete rejection. It also describes one `DocumentReference` per submitted invoice, with item identity, result and locator. The sample uses `ReferencedDocumentInternalAddress` for the locator and `DocumentStatusCode` for an item result.

Those XML business-response codes are not automatically HTTP status codes. Catalogue section 6.6 separately mentions an HTTP `400` download case when a locator is unavailable. Retain transport, SOAP fault, request result and item result independently. The supplied sample's `200` means technical admission under that response; it does not mean that the buyer paid or explicitly accepted the invoice.

## Identity and authorization

The formats document, pp. 9 and 12, says ebMS `From/PartyId` identifies the sender from the certificate. Invoice supplier/recipient fields identify business parties. A platform caller and its represented customer can therefore differ. Do not copy the authenticated-caller NIF into every issuer field.

| Operation group | Catalogue authorization description | Qualification required |
|---|---|---|
| Submission, invoice withdrawal and events | Power of attorney (`apoderamiento`) and social collaboration (`colaborador social`). Section 4.1 also describes the taxpayer acting directly. | Confirm the procedure, caller role, represented party and per-invoice authorization, including mixed-issuer submission. |
| Identifier/date queries and ID downloads | Direct use or power of attorney; social collaboration is described with limits to issuer-side access by the original submitter. | Compare the catalogue with final order Article 11. Confirm permitted authority for each operation; do not extend submission authority to recipient retrieval. |
| Locator downloads | Check the platform certificate against the locator's `NIUs`; if negative, check power of attorney. | The supplied material does not fully define `NIUs`, issuance/binding rules or revocation behavior. Compliance and the technical owner must reconcile this path with legal representation requirements. A locator is not proven to be an unrestricted bearer token. |
| All calls | Recognized qualified certificate; NIFs must be validated against AEAT's centralized database according to section 4.1. | Exact certificate acceptance, NIF-validation responsibility and integration contract remain open. This does not prove a separate available identity-quality endpoint. |

## Conflicts and missing evidence

| ID | Finding and source | Owner and next evidence |
|---|---|---|
| SPFE-Q01 | Formats p. 7 says SOAP 1.1. Catalogue p. 8, WSDL bindings and XML envelope examples use SOAP 1.2. Catalogue p. 9 still describes SOAP 1.1 fault names. | Public Platform Technical Owner: confirm transport and fault profile. Proposed offline POC baseline: SOAP 1.2 from the supplied WSDLs, with the conflict recorded. |
| SPFE-Q02 | Formats pp. 14–15 mark sections 5.3–5.9 pending publication. | AEAT liaison and Technical Owner: obtain exact query, pagination, download, cancellation and event request/response shapes. Catalogue descriptions alone do not close this gap. |
| SPFE-Q03 | Catalogue p. 11 states a 5,120-byte invoice limit, but both supplied invoice examples exceed it. | AEAT liaison: confirm number, unit, byte-measurement basis, envelope/batch limits and conformance examples. |
| SPFE-Q04 | No UBL 2.5 business XSD set, complete EN 16931/Spain rules or referenced validation/error document is supplied. | Format/Validation Owner: qualify the actual schemas, extensions, code lists and rule versions. Do not assert invoice schema validation from XML parsing. |
| SPFE-Q05 | Catalogue describes `InvoiceValidationSOAP`, but its WSDL and exact packaging are absent. | Technical Owner: obtain its contract and access evidence. Do not rely on it for production preflight validation. |
| SPFE-Q06 | Header-only date-query request in the catalogue differs from the WSDL's generic payload part. Filter names, formats and continuation semantics are incomplete. `SECUENCE_ID` is the source spelling. | Retrieval Owner: obtain official examples and boundary tests, including pagination and presentation-date semantics. |
| SPFE-Q07 | Catalogue p. 9 recommends resending after some failures or missing responses. No complete idempotency or same-content duplicate contract is supplied. | Connector/Outbound Owners: qualify replay behavior and reconciliation. `MessageId` alone is not proof of idempotency. Never withdraw an existing invoice merely to retry an uncertain send. |
| SPFE-Q08 | Catalogue cancellation language includes removal and identifier reuse. The final order preserves traceability and restricts permissible withdrawal cases. | Compliance and Outbound Owner: approve withdrawal versus rectification policy, audit behavior and historical identity handling. |
| SPFE-Q09 | Catalogue social-collaboration and locator-certificate paths need reconciliation with final order Article 11 authority requirements. | Compliance/Security/Technical Owners: approved operation-specific authority and credential matrix. |
| SPFE-Q10 | Catalogue p. 21 points to a `tikeV1.0/.../SistemaFacturacion.wsdl` reference. Its relationship to this SPFE bundle is not established. | AEAT liaison: obtain the correct SPFE publication link. Do not use that reference as the source for these eight contracts. |
| SPFE-Q11 | Formats operation-key list omits `DOWNLOADBYID`, although the catalogue and corresponding WSDL describe the service. Catalogue locator path repeats `ws/`. | Technical Owner: retain exact WSDL operation/address and catalogue action values; obtain corrected reference material. |
| SPFE-Q12 | WSDL addresses exist, but PRE service availability, Sage access, accepted test identities and authorization are not demonstrated. Production endpoints, quotas and service targets are absent. | AEAT liaison and Security/Operations: confirm access and environment rules, then record authorized live test results. |
| SPFE-Q13 | Both invoice examples use a `ProfileID` without `ubl:`, while final BOE Annex I BT-23 and the separate annex require the value with `ubl:`. | Format/Validation and AEAT liaison: qualify the governing value and accepted examples. Preserve originals; do not activate an example profile solely because it was supplied. |
| SPFE-Q14 | The full source-row inventory and logical acceptance matrix are recorded in the owning specs and field ledger. Actual ERP/API/UBL bindings and executable coverage are not yet qualified. Annex I includes conditional groups, 29 Spain-specific BT fields, repeated BG-24 meanings and code lists. SPEC-SEI-015 identifies three-versus-five corrective amount cardinality and buyer-identity wording/path issues. | Creation/Format/DTS and Compliance: record each supported field/group, source locator, condition, target path, rule, exception and test. Hold unsupported applicable content. |
| SPFE-Q15 | Articles 5.4 and 8.3 require receipt evidence with a secure verification code (`CSV`). The sample `DocumentStatus/ID` is not explicitly mapped to that code by the supplied formats. | Connector/Records and AEAT liaison: confirm CSV representation, scope and retrieval/verification. Keep response ID, locator, message ID and CSV distinct. |
| SPFE-Q16 | Annex II defines mandatory dates and source paths. Catalogue payment prose mentions a prepaid indicator; Annex II uses `CorrectedInvoice` and `NegativeAmountInvoice`, and Article 7.4 defines a separate prepaid-invoice reporting exception. | Lifecycle/Compliance/Format: reconcile each field and condition; do not invent a prepaid wire field or reuse one date meaning for every event. |
| SPFE-Q17 | Locator-download and supplier-event sections have no explicit numeric batch limit. Ordering, mixed-item failure shapes and complete error codes remain incomplete across services. | Connector/Retrieval/Lifecycle owners: obtain each operation's limits and response examples. A limit for one operation cannot qualify another. |
| SPFE-Q18 | Final legal rules establish public-copy timing, duplicate cases, correction branches and exceptional outage windows. Their operational calendars and exact implementation coverage are unqualified. | Compliance/Outbound/Lifecycle/Operations: approve country-rule bindings, issuance handoff, incident evidence, working-day calendar and acceptance corpus. |

No recipient directory, external customer-registration mutation or webhook interface is established by this bundle. The invoice discovery operations do not identify a recipient's chosen receiving platform. Absence here does not prove that no such capability can exist elsewhere; keep the owning spec's evidence gate open.

## Legal behaviour that the feature review must preserve

These rows use the original final BOE order, source **SPFE-S02**. They add rules that an API-name inventory alone cannot cover. The cited articles govern even when an example or catalogue summary omits the distinction.

| Evidence ID | Source location | Required behaviour and review consequence |
|---|---|---|
| SPFE-E01 | Article 3.4 | Public issuance or interconnection already makes the invoice available to the administration. Do not create another faithful-copy obligation for that same public use. |
| SPFE-E02 | Article 4.1–4.3 | Where the public solution is not used for issuance or interconnection, send the faithful UBL copy simultaneously with issuance. Recipient/third-party material issuance assigns the copy to the platform used by that actor. Pin `CopyIndicator` and actor separately from private recipient delivery. |
| SPFE-E03 | Article 5.5 | Duplicate copies and copies of public originals are rejected. Public interconnection after a copy requires prior copy withdrawal. This is a controlled legal case, not a retry mechanism. Preserve withdrawal traceability. |
| SPFE-E04 | Article 5.6 | A rejected copy does not by itself invalidate an original already delivered privately. Correct a defective copy while preserving correspondence. A defect in the original has a separate issuance/correction branch; do not repair the copy alone or silently edit issued bytes. |
| SPFE-E05 | Articles 5.7 and 8.4 | For an SPFE-attributable technical outage lasting more than 24 hours, the affected invoice/copy or state/payment submission may occur within four working days after resolution. Record attribution, duration, resolution and the working-day calendar. This is not a general retry budget or retrieval deadline. |
| SPFE-E06 | Article 7.4; Annex I BT-ES-2 | The recipient payment-report duty can be fulfilled by the invoice/copy's payment date only when the specified issue/operation-date conditions hold. An explicit recipient payment communication overrides that exception. An arbitrary `PrepaidPayment` field is insufficient. |
| SPFE-E07 | Articles 5.4 and 8.3 | Keep invoice/event admission and receipt evidence, including the secure verification code (`CSV`), independently. Exact code placement remains SPFE-Q15. |
| SPFE-E08 | Annex II, PDF pp. 36–42 | All eight event codes identify an invoice by series/number, issue date and seller NIF, with the stated seller-name fields. Apply event-specific dates and rejection reasons, not a generic amount-bearing payment message. |
| SPFE-E09 | Annex I BT-23/24, PDF p. 14; separate annex p. 6 | Final `ProfileID` includes `ubl:`. `CustomizationID` uses the exact final extended-profile value. The examples' conflicting `ProfileID` remains visible under SPFE-Q13. |
| SPFE-E10 | Annex I, PDF pp. 13–34 | Qualify all applicable core fields, conditional groups, Spain extensions and code lists. Corrective types 384/471 still use `Invoice`, with `RECT:TIPO`, `RECT:MODALIDAD` and applicable `RECT:IMPORTES` references. The detailed field inventory is in SPEC-SEI-015. |

## Annex II field review

This table records source meaning and field locators. It is not a completed wire schema. Preserve literal source paths; qualify ambiguous formatting and cardinality against the actual schema. The original PDF tables govern visual interpretation.

| Communication | Required or conditional content | Original source location |
|---|---|---|
| All eight codes | Invoice `DocumentReference`: `cbc:ID`, `cbc:IssueDate`, `cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID`, and the stated seller `RegistrationName`. Cancellation messages keep invoice references; do not assume an event ID alone is sufficient. | SPFE-S02, Annex II pp. 36–42. |
| `PAYMENT` | Payment `cbc:EffectiveDate` and due date under `cac:Status/cbc:ReferenceDate` with `AttributeID=DueDate` are required. Conditional receipt dates use `ShipmentDate` and `ReceptionDate`. Source indicators use `cbc:StatusReason=CorrectedInvoice` or `NegativeAmountInvoice`. | SPFE-S02, pp. 36–37. |
| `REJECTION` | Rejection `cbc:EffectiveDate` and `cac:Status/cbc:ConditionCode` are required. L1: `01` commercial rejection; `02` private consumption or not related to the business activity. | SPFE-S02, pp. 38–39 and 42. |
| `SETTLEMENT` | Collection `cbc:EffectiveDate` is required. Due date and relevant receipt dates are conditional. The source names financing indicator `AttributeID=FinancingArrangement`; exact indicator serialization needs qualification. | SPFE-S02, pp. 39–40. |
| `DEFAULT` | `cbc:EffectiveDate` means the **payment due date**, not a generic non-payment observation time. Relevant receipt dates are conditional. | SPFE-S02, pp. 41–42. |
| `CANCELPAYMENT`, `CANCELREJECTION`, `CANCELSETTLEMENT`, `CANCELDEFAULT` | Preserve the invoice identity and source cancellation meaning. Retain Sage correction/cancellation lineage separately. Do not add unsupported wire fields by analogy with an initial report. | SPFE-S02, pp. 37–42; catalogue pp. 17–19. |

## Completeness and review closure

All supplied files and PDF pages are indexed. That establishes source coverage. It does not establish a complete field mapping, executable country rule pack, approved product scope or working integration.

| Review domain | Closure evidence required | Accountable owner |
|---|---|---|
| Every catalogue service | Exact operation/action, request, response, role, authority, limits, errors, duplicate and uncertain-result handling. Include the PRE validator and services whose format sections are pending. | Connector and feature owners. |
| Every applicable Annex I field/group and code list | Source row and condition → product/source field → qualified UBL path/rule → acceptance example. Explicitly mark unsupported applicable content and preserve all required meaning. | Creation, Format, DTS, Validation and Compliance. |
| Every Annex II communication | Actor, invoice identity, mandatory/conditional fields, raw codes, legal applicability, cancellation sequence and independent reporting result. | Lifecycle, Format and Compliance. |
| Every legal branch above | Issuance/public-copy timing; existing copy/original cases; copy versus original correction; prepaid exception; outage and CSV evidence. | Outbound, Lifecycle, Records and Compliance. |
| Every represented scope and environment | Direct/delegated caller, certificate versus seal, source authorization, current grants, source date/version and permitted operation. | Identity, Certificates, Onboarding and Security. |
| Every reuse claim | Actual build/contracts, local mapping/rules, gaps, named build/run owner and evidence. Prove country-rule isolation. | Architecture, DTS and service owners. |
| Current phase boundary | Public technical alignment covers public operations and their creation, validation, receiving, authority and recovery dependencies. Offboarding and private-provider API design are deferred. No public offboarding API is inferred. | Product and feature owners. |

Review completion below means that source-backed behaviour, acceptance scenarios and REF entries are recorded. Implementation and conformance gates remain open where the source or build evidence is incomplete.

## POC work supported by this evidence

**Proposed offline work:** build the SOAP 1.2/ebMS/MIME envelope from the supplied contracts; preserve exact invoice XML; parse request and item outcomes separately; exercise mixed success, SOAP faults, missing attachments and response correlation with synthetic data. These tests establish local handling only.

**Open live-test gate:** confirm PRE availability, the accepted certificate and operation-specific authority. Confirm the invoice-size conflict and approved submission profile before relying on a live admission result. Use only permitted synthetic test identities and invoices.

**Proposed initial live sequence after the gate:** submit one qualified original; consult its result by identity; discover by presentation date once the filter contract is available; retrieve the exact invoice through its locator. Add faithful-copy and event tests after their schemas, authority and country rules are qualified. Test uncertain results and reconcile before repeating a mutation.

For transformation, assess existing **DTS** first. Qualify its build, input/output contracts, UBL 2.5 mapping, `CopyIndicator`, Spain extensions, rectification rules and operating controls. The release does not establish that DTS already supports this profile. Reuse shared parsing, evidence storage, correlation and recovery patterns where proven; keep Spain identity, public-copy, event and authorization rules in the Spain adapter or country rule pack. Test that these rules do not become defaults for another country.

## Targeted review map

This pass reviews the ten original targets and three public dependencies: creation, receiving and setup recovery. Each reviewed spec links its original sources in `REF Source references`; `*-SPFE-R*` and `*-SPFE-A*` identify the added requirements and acceptance scenarios. The map also records two deferred specs so absence from this pass is explicit. Offboarding is not needed for the current public-platform phase; SPEC-SEI-003 remains unchanged. The private/provider-facing scope of SPEC-SEI-013 is also unchanged. Existing document lifecycle and publication status are preserved.

Strikethrough in **Applied source reconciliation** marks completed document-review work for the supplied snapshot. It does not close the **Remaining owner and gate** column or mean that acceptance tests passed. Original source files remain unchanged. PRDs are unchanged. The two deferred rows are not struck through.

The completed field inventory covers 176 invoice rows, 7 withdrawal rows, 52 event rows and 15 code tables. [SPEC-SEI-015](../specs/SPEC-SEI-015-invoice-creation-solution-specification.md#annex-i-invoice-field-traceability), [SPEC-SEI-007](../specs/SPEC-SEI-007-invoice-sending-solution.md#annex-i-withdrawal-field-traceability) and [SPEC-SEI-009](../specs/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#annex-ii-event-field-traceability) own the readable matrices. The [field ledger](../assets/regulatory/spain/spfe/field-traceability.json) preserves every original Spanish row and exact locator. Actual field bindings, approved fixtures and test execution remain open. Outbound and creation diagrams now place final preparation before the dependent ERP issue/copy boundary; OUT-Q03 still gates physical coordination.

Current receiving, retrieval and download design is consolidated in [SPEC-SEI-016](../specs/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md). The SPEC-SEI-006 and SPEC-SEI-010 rows below retain the original review record and link to archived predecessors. Their RCV/RSD controls and open gates are carried into SPEC-SEI-016. This navigation change does not record new source checks or executed tests.

| Canonical feature | Applied source reconciliation | Original REF evidence | Acceptance coverage | Remaining owner and gate |
|---|---|---|---|---|
| [SPEC-SEI-011 Public connector](../specs/SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding) | ~~Eight WSDL operations plus PRE validator, message envelope, response levels and uncertain effects. `PCN-SPFE-R01`–`R04`.~~ | SPFE-S02, SPFE-S03, SPFE-S08, SPFE-S16, SPFE-S18, SPFE-S04, SPFE-S06; original file, version and locator in feature REF. | `PCN-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: PCN-Q01/Q02/Q03/Q07; SPFE-Q01–Q12/Q15/Q17. |
| [SPEC-SEI-010 Retrieval](../specs/archive/SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md#spfe-source-contract-binding) | ~~Presentation-date discovery, identity consultation, locator/ID download and safe complete progress. `RSD-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S03, SPFE-S15, SPFE-S14, SPFE-S12, SPFE-S13, SPFE-S08; original file, version and locator in feature REF. | `RSD-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: RSD-G01/G02/G05/G06; SPFE-Q06/Q09/Q12/Q17. |
| [SPEC-SEI-009 Lifecycle](../specs/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md#spfe-source-contract-binding) | ~~Eight raw event codes, Annex II fields, cancellation, prepaid exception and legal calendar. `LCS-SPFE-R01`–`R04`.~~ | SPFE-S02, SPFE-S03, SPFE-S11, SPFE-S17, SPFE-S08; original file, version and locator in feature REF. | `LCS-SPFE-A01`–`A04`; required evidence scenarios, not executed tests. | Feature and source owner: country event/field/calendar and correction gates; SPFE-Q07/Q13/Q15/Q16/Q17/Q18. |
| [SPEC-SEI-007 Outbound](../specs/SPEC-SEI-007-invoice-sending-solution.md#spfe-source-contract-binding) | ~~Copy at issuance, no redundant public copy, duplicate/withdrawal/correction and outage branches. `OUT-SPFE-R01`–`R04`.~~ | SPFE-S02, SPFE-S03, SPFE-S01, SPFE-S16, SPFE-S10, SPFE-S06; original file, version and locator in feature REF. | `OUT-SPFE-A01`–`A04`; required evidence scenarios, not executed tests. | Feature and source owner: OUT-Q03 physical issue/copy coordination and correction policy; SPFE-Q03/Q07/Q08/Q13/Q15/Q18. |
| [SPEC-SEI-005 Validation](../specs/SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md#spfe-source-contract-binding) | ~~UBL 2.5 Invoice, final identifiers, business rules and PRE-validator limit. `UV-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S01, SPFE-S03, SPFE-S08, SPFE-S09; original file, version and locator in feature REF. | `UV-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: profile activation; SPFE-Q03/Q04/Q05/Q13/Q14. |
| [SPEC-SEI-008 DTS mapping](../specs/SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md#spfe-source-contract-binding) | ~~Final public target and complete applicable field preservation and DTS qualification requirements. `UM-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S01, SPFE-S08, SPFE-S09; original file, version and locator in feature REF. | `UM-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: UM-Q01/Q03/Q04/Q09; SPFE-Q04/Q13/Q14. |
| [SPEC-SEI-001 Certificates](../specs/SPEC-SEI-001-certificate-management-solution-specification.md#spfe-source-contract-binding) | ~~Public certificate/seal ports, caller versus represented party and distinct signing purpose. `CM-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S03, SPFE-S16, SPFE-S08; original file, version and locator in feature REF. | `CM-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: G4/G8/G10/G11; SPFE-Q01/Q09/Q12. |
| [SPEC-SEI-002 Onboarding](../specs/SPEC-SEI-002-onboarding-solution-specification.md#spfe-source-contract-binding) | ~~Public readiness by operation; no invented enrolment; current representation evidence. `ONB-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S03, SPFE-S16, SPFE-S08; original file, version and locator in feature REF. | `ONB-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: ONB-Q04/Q06/Q07; SPFE-Q09/Q12. |
| [SPEC-SEI-012 Recipient lookup](../specs/SPEC-SEI-012-consult-public-platform-for-recipient-information.md#spfe-source-contract-binding) | ~~Invoice consultation cannot supply recipient-directory evidence or prove absence. `RLU-SPFE-R01`–`R02`.~~ | SPFE-S03, SPFE-S14, SPFE-S15; original file, version and locator in feature REF. | `RLU-SPFE-A01`–`A02`; required evidence scenarios, not executed tests. | Feature and source owner: RLU-Q01/Q03/Q05; source adapter remains unqualified. |
| [SPEC-SEI-014 Shared public connection binding](../specs/SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md#spfe-source-contract-binding) | ~~Public role/profile qualification requirements and owning-feature action rules; private scope is unchanged. `SPC-SPFE-R01`–`R02`.~~ | SPFE-S02, SPFE-S03, SPFE-S16; original file, version and locator in feature REF. | `SPC-SPFE-A01`–`A02`; required evidence scenarios, not executed tests. | Feature and source owner: SPC-Q02/Q03/Q04; SPFE-Q09/Q12. |
| [SPEC-SEI-015 Creation](../specs/SPEC-SEI-015-invoice-creation-solution-specification.md#spfe-source-contract-binding) | ~~Five public Invoice types, conflicting sample identifiers and complete conditional field inventory and coverage requirements. `IC-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S01, SPFE-S08, SPFE-S03, SPFE-S09; original file, version and locator in feature REF. | `IC-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: IC-Q01/Q02/Q04/Q05/Q06; SPFE-Q03/Q04/Q13/Q14. |
| [SPEC-SEI-006 Receiving](../specs/archive/SPEC-SEI-006-invoice-receiving-solution.md#spfe-source-contract-binding) | ~~Captured file versus metadata; profile/copy roles and conserved access. `RCV-SPFE-R01`–`R03`.~~ | SPFE-S02, SPFE-S03, SPFE-S08, SPFE-S13, SPFE-S09; original file, version and locator in feature REF. | `RCV-SPFE-A01`–`A03`; required evidence scenarios, not executed tests. | Feature and source owner: inbound profile and identity qualification; SPFE-Q04/Q06/Q09/Q13/Q14. |
| [SPEC-SEI-004 Setup recovery](../specs/SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md#spfe-source-contract-binding) | ~~Qualified public setup checks; separate fault levels and no blanket resend. `OFR-SPFE-R01`–`R02`.~~ | SPFE-S03, SPFE-S08, SPFE-S16; original file, version and locator in feature REF. | `OFR-SPFE-A01`–`A02`; required evidence scenarios, not executed tests. | Feature and source owner: OFR-Q01/Q04 and retry-safety decision; SPFE-Q01/Q07/Q12. |
| [SPEC-SEI-003 Offboarding](../specs/SPEC-SEI-003-offboarding-solution-specification.md) | Deferred by current public-only scope. Product disconnection and Sage private-platform exit need their own product/provider evidence; no public offboarding operation is supplied. | No current-phase source mandate for this feature. | Not reviewed in this pass; source file unchanged. | Product owner defines a later phase and its evidence before review. |
| [SPEC-SEI-013 Provider-facing Global API](../specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md) | Deferred private/provider-facing design. Public calls continue through the qualified feature and connector boundaries; this bundle does not establish partner/private contracts. | No current-phase source mandate for this feature. | Not reviewed in this pass; source file unchanged. | Product owner defines a later phase and its evidence before review. |


## REF Source references

Use the stable `SPFE-S*` source IDs below in the reviewed specs. Each feature's REF table states the exact article, page, section or XML/WSDL element supporting its claims. Source-dependent constraints cite those IDs beside the behaviour. Product requirements, proposed Sage controls and unresolved evidence have separate authority.

### Complete source register

The register below is generated from the supplied file inventory. The source manifest contains a SHA-256 hash for every original file and extracted text. Hashes identify this local snapshot; they do not establish publication authority or successful integration.

| Source | Original file | Coverage |
|---|---|---|
| SPFE-S01 | [Anexo-1-Proyecto-OM-FE.pdf](<../context/Anexo I/20261013/Anexo-1-Proyecto-OM-FE.pdf>); [Spanish text](../assets/regulatory/spain/spfe/invoice-annex.es.txt) | 34 PDF pages |
| SPFE-S02 | [BOE-A-2026-20587.pdf](<../context/BOE-A-2026-20587.pdf>); [Spanish text](../assets/regulatory/spain/spfe/public-platform-order.es.txt) | 42 PDF pages |
| SPFE-S03 | [CatalogoServicios.pdf](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>); [Spanish text](../assets/regulatory/spain/spfe/service-catalogue.es.txt) | 21 PDF pages |
| SPFE-S04 | [Peticion_ebXML- SUBMITINVOICE.xml](<../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/PETICIÓN/Peticion_ebXML- SUBMITINVOICE.xml>) | XML |
| SPFE-S05 | [altaFacturas.xml](<../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/PETICIÓN/altaFacturas.xml>) | XML |
| SPFE-S06 | [RespuestaAltaFacturas.xml](<../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/RESPUESTA/RespuestaAltaFacturas.xml>) | XML |
| SPFE-S07 | [Respuesta_ebXML- SUBMITINVOICE.xml](<../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/RESPUESTA/Respuesta_ebXML- SUBMITINVOICE.xml>) | XML |
| SPFE-S08 | [FormatosEntradaSalida.pdf](<../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>); [Spanish text](../assets/regulatory/spain/spfe/input-output-formats.es.txt) | 15 PDF pages |
| SPFE-S09 | [factura.xml](<../context/Ejemplos/20261013/factura.xml>) | XML |
| SPFE-S10 | [CancelInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/CancelInvoice.wsdl>) | CancelInvoice |
| SPFE-S11 | [CustomerInvoiceEvents.wsdl](<../context/WSDL servicios web - PRE/20261013/CustomerInvoiceEvents.wsdl>) | CustomerInvoiceEvents |
| SPFE-S12 | [DownloadInvoicesByID.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByID.wsdl>) | DownloadInvoicesByID |
| SPFE-S13 | [DownloadInvoicesByLOC.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByLOC.wsdl>) | DownloadInvoicesByLOC |
| SPFE-S14 | [GetInvoices.wsdl](<../context/WSDL servicios web - PRE/20261013/GetInvoices.wsdl>) | GetInvoices |
| SPFE-S15 | [GetRegisteredInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/GetRegisteredInvoice.wsdl>) | GetRegisteredInvoice |
| SPFE-S16 | [SendInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>) | SendInvoice |
| SPFE-S17 | [SupplierInvoiceEvents.wsdl](<../context/WSDL servicios web - PRE/20261013/SupplierInvoiceEvents.wsdl>) | SupplierInvoiceEvents |
| SPFE-S18 | [ebms-header-3_0-200704.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/ebms/ebms-header-3_0-200704.xsd>) | XSD |
| SPFE-S19 | [soap-envelope.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/w3/soap-envelope.xsd>) | XSD |
| SPFE-S20 | [xml.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/w3/xml.xsd>) | XSD |
| SPFE-S21 | [envelope.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/xmlsoap/envelope.xsd>) | XSD |
