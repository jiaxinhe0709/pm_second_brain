# Receiving an e-invoice — supplied FR guide evidence

Source ID: **INT-RCV01**. User-supplied guide received 22 October 2026. Its sections run from subscription through invoice retrieval, querying and attachment download. The canonical page URL, revision date, OpenAPI and deployed build were not supplied. A neighbouring documentation link contains `/domain-services/docs/v1.0.0/`; this is not evidence of the API's version.

Original attachment SHA-256: `bd087283fec514678d601b7f234724620ead8a82fc3be7dcc6b3b7c6fe192c1b`.

This selective extract retains contract facts and source conflicts. Example identities, opaque tokens, presigned URLs and payloads are omitted. It is a reading aid for the supplied guide, not a verified schema or production contract.

## Prerequisites and authentication

- The dataset must be connected to the access point/address used for receiving.
- The introduction permits a Domain Services auth token obtained during Network onboarding or a Sage ID machine-to-machine token in `Authorization`. The subscription table describes a Network token from the user's Sage ID login. Confirm the supported caller/token combination per operation.
- The subscription table marks `Authorization`, `traceparent`, `Idempotency-Key` and `tracestate` required. It does not define key scope, expiry, input binding or concurrency behaviour. These requirements are not separately specified for each GET.

## 1 Subscribe to invoice received notification

- `POST /internal/events/subscriptions`; the operation card omits the initial slash. The response is labelled `201 OK` in the source. Preserve code `201`; confirm the schema rather than treating the reason phrase as normative.
- Scope uses resource `einvoice`, event type `e-invoicing.einvoice.received` and source selected by access point/environment. The example source is for production `sage.pdp.france`, not Spain.
- Scope fields include `accountId`, `datasetId` and optional case-sensitive OData `filter`. The table does not mark account/dataset/eventType required. The application still needs a qualified scope; no cross-dataset permission follows from omission.
- Attributes include `audience`, `endpoint`, `endpointType: https`, optional `opaqueToken` and `clientstate` (maximum 256 characters). The text says the token returns in `Opaque-Token`; the notification-header table only describes `clientstate`. Authentication and token validation need the missing notification contract.
- The request example uses `Data`, `Type`, `Attributes`, `Scope`; the field table and response use lowercase. `opaqueToken` and `opaquetoken` also differ. Resolve casing against the selected schema.

## 2 Invoice received event

- Store `subject` as the `e-invoiceId` for subsequent requests. Event `id`, `subscriptionid`, `accountid`, `datasetid`, `source`, `time`, `traceparent` and nullable `data.errorCode` are shown.
- The notification example uses `type: com.sage.network.e-invoicing.api.einvoice.received`, while the subscription uses `e-invoicing.einvoice.received`. The missing Events Library must establish the mapping for the selected environment/access point.
- A received notification indicates a file may be pulled. The example also allows an error. Delivery/replay, ordering, authentication, webhook response deadlines and failure semantics are not supplied.

## 3.1 Retrieve the new E-Invoice

- `GET /datasets/{datasetId}/e-invoices/{e-invoiceId}`; UUID path parameters; `200 OK` with invoice details and attachments.
- Optional `format=facturx` generates a Factur-X/ZUGFeRD 2.3 hybrid PDF from UBL/PDF files or returns an existing one without regeneration. Keep this optional representation request separate from ordinary observation and exact-source recovery.
- Attachment fields: `filename`, `mimetype`, `filetype`, `downloadUrl`. `filetype` values: `Undefined`, `UBL`, `Human_Readable`, `Original_Document`. Example MIME values: `ubl-2.1/xml`, `application/pdf`.
- Invoice fields include `eInvoiceTypeCode`, `sender`/`recipient` with `accessPointAddressType`/`accessPointAddress`, `accessPointId`, `erpInvoiceId`, `currentStatus` and `history[]`. Document codes: `AP_Invoice`, `AR_Invoice`, `AP_CreditNote`, `AR_CreditNote`.
- The example places invoice identity in `data.id`; the field table also describes `data.attributes.eInvoiceId`, absent from that example. Confirm the authoritative identifier.
- Status fields include `statusId`, `statusCode`, `status`, `notes`, `rejectionReason`; history adds `operationStatus`, `errorCode` and metadata. `operationStatus` values: `IN_PROGRESS`, `COMPLETED`, `ERROR`. The example status is `New`. It does not establish buyer acceptance or complete state mappings.

## 3.2 Query all E-Invoices

- `GET /datasets/{datasetId}/e-invoices`; `200 OK` with `data[]`, invoice IDs, metadata and attachment descriptors. The list example does not supply `downloadUrl`; use the detail operation before file download.
- The guide states a query window covering invoices created within the last **90 days**, up to **20 invoices per page**, with `meta.count`, `meta.hasMore`, `links.self` and `links.next`. Follow the returned next link for further pages.
- Filters listed: `erpInvoiceId`, `accessPointId`, `eInvoiceTypeCode`, `sender.accessPointAddress`, `sender.accessPointAddressType`, `recipient.accessPointAddress`, `recipient.accessPointAddressType`, `currentStatus/statusCode`, `createdAt`. Examples combine filters with `and` and use `ge`/`le` for dates.
- Another example uses `currentStatus/createdAt`, absent from the filter table. Its explanation claims to find any status change, but that coverage is not established by a schema or history contract. One status example also has an extra trailing quote. Verify supported syntax and change coverage before implementation.
- Results can include sent and received invoice codes; the example contains `AR_Invoice`. Listing a dataset does not by itself select received invoices. Confirm inbound direction/type selection and self-billing/credit mappings.
- Stable ordering, snapshot behaviour, late changes, boundary inclusion, continuation expiry and history beyond 90 days are not supplied. This list alone cannot prove complete recovery or records retention.

## 4 Download invoice attachments

- Perform `GET {downloadUrl}` for each required attachment from the detail response. `200 OK` returns UBL or PDF bytes.
- The guide calls the URL short-lived and presigned. It requires immediate byte capture in the consuming document system and says not to store the URL. The download needs no `Authorization` header.
- For an expired URL returning `403`, retrieve invoice details again for a fresh URL. The guide does not establish that every `403` means expiry. Preserve the invoice/file identity; qualify how to verify the renewed link still identifies the intended file.
- For a hybrid PDF, request `format=facturx` first, then download the returned `Human_Readable` attachment. This is a derived representation, not evidence of the exchanged structured original.

## Polling, formats, and extracted data

- Prefer notifications where possible. Without webhooks, list using status/date filters, then inspect an individual invoice's full `history[]`.
- No fixed interval or public rate-limit number is supplied. For `429 Too Many Requests`, honour `Retry-After`. Qualify missing/malformed-header handling with the API owner.
- The guide says receiving supplies UBL even when the supplier sent Factur-X. The supplier file is retained as `Original_Document`; a human-readable PDF is `Human_Readable`. Confirm the exact exchanged-source role for the selected provider; UBL is not necessarily the original supplier bytes.
- VAT totals and detailed tax breakdowns are not exposed as extracted response fields. Use the UBL where needed; qualify its schema, completeness and mapping to the target product.
- The regional archiving note establishes no country retention duration, historical API coverage or conservation implementation.

## Evidence still needed

Later supplied evidence: [INT-ERR01 error-handling guide](<../Shared/invoice-flow-error-handling-guide-extract.md>) clarifies history-only error/outcome fields, attempt finality and code-specific platform retry/support actions. The limits below describe what this receiving guide alone establishes; the later guide does not qualify Spain build support or event/attempt correlation.

Obtain the versioned OpenAPI, Events Library, status/error guides, caller permissions and actual build from the API owners. Qualify Spain identity, source-file roles, public/private contracts, profile/rule packs, missed-event coverage, retention and recovery independently. No Spain support or public-platform notification endpoint is established by this guide.
