# Sending an e-invoice — supplied FR guide evidence

Source ID: **INT-SND01**. User-supplied guide received 22 October 2026, beginning with the sending video and ending with Get invoice details. The guide uses documentation paths under `/domain-services/docs/v1.0.0/`; its canonical page URL, revision date, OpenAPI and deployed build were not supplied. The documentation path is not proof of an API version or current deployment.

Original attachment SHA-256: `4c0dd498414f358cc86f00daeb978da37cbb9fad85477b962e20ceac7d836bba`.

This technical extract omits example tokens, webhook secrets, company identifiers, operational IDs and full payloads. It preserves the claims and conflicts needed for reuse assessment. This guide describes France and Demo PA behaviour. It does not establish Spain support or a complete contract.

## Prerequisites and submission design requirements

- The dataset must have a completed access-point connection. The guide requires `CONNECTED` before submission. It says asynchronous POST intake can accept a request during `IN_PROGRESS` or `ERROR`, then fail during processing. `SENDER_NOT_ONBOARDED` identifies incomplete sender setup.
- Supply `sender.accessPointAddressType`, `recipient.accessPointAddressType` and `eInvoiceTypeCode`, even if an earlier schema marks them optional.
- `sender` and `recipient` are routing addresses, separate from seller and buyer inside the invoice. The sender belongs to the calling dataset. One submission has one recipient. Self-billing routes buyer to seller. An additional recipient needs a separate submission under this guide.
- Documented codes: `AR_Invoice`, `AR_CreditNote` and `AP_CreditNote`. The guide associates `AR_CreditNote` with UBL type `381`. It does not define a complete Spain document-type mapping or self-billing code selection.
- Sage PA France accepts UBL 2.1 XML with an optional PDF, or one Factur-X hybrid PDF. Factur-X contains structured CII data and needs no separate UBL attachment. Demo PA requires both UBL and PDF for its test flow.
- ERP-to-UBL field mapping must be documented. No mapping, transformation API or semantic-preservation evidence is supplied here.

## Step 1 — Subscribe to invoice status updated event

- Operation card: `POST internal/events/subscriptions`; overview sequence: `POST /internal/events/subscriptions`. The leading-slash and API base/access surface require confirmation.
- Subscription scope names resource `einvoice`, `e-invoicing.einvoice.statusupdated`, dataset and environment/access-point-specific source. The guide includes audience, HTTPS endpoint, optional opaque token and `clientstate` (maximum 256 characters).
- The guide says the notification means processing for the attempt has finished, with either success or `ERROR`. It is not evidence of buyer acceptance.
- The JSON example uses `Data`, `Type`, `Attributes`, `Scope`, `Resource`, `EventType`, `DatasetId`, `Endpoint` and `EndpointType`, alongside lower-case keys. The field table uses lower-case `data` and lower-camel-case names. Do not derive a serializer from this inconsistent example.

## Step 2 — Send an e-invoice

- `POST /datasets/{datasetId}/e-invoices` returns `201 Created`, an e-invoice ID and per-attachment `uploadUrl` values.
- The header table marks `Authorization`, `traceparent`, `Idempotency-Key` and `tracestate` required. It does not define key scope, lifetime, body binding, conflict responses or lost-response recovery. Do not substitute onboarding's `X-Idempotency-Key` without the selected contract.
- The guide's authentication section permits a Domain Services auth token or Sage ID M2M token in `Authorization`; the operation header text describes a Network token. Confirm accepted tokens, scopes and audiences per operation. Authentication is separate from authority for the represented business.
- Request uses `data.type: "e-Invoice"`; `data.attributes` includes `attachments[].filename`, `attachments[].mimetype`, sender/recipient address types and values, `accessPointId`, `eInvoiceTypeCode`, and optional `erpInvoiceId`.
- Declared filename length: 1–128; routing address value length: 1–50. MIME values: `ubl-2.1/xml` and `application/pdf`. The guide does not define Spain address types, UBL 2.5 MIME support or attachment limits.
- The response example identifies the resource in `data.id`. Its table also lists `attributes.eInvoiceId`. `currentStatus` is variously an object, string or empty object across examples/tables. Confirm the selected schema.

## Step 3 — Upload attachments; Factur-X subsection

- PUT binary content to each returned `uploadUrl`, one file per request; documented success is `200 OK`. No stable upload host/path is defined.
- The general instruction says upload both UBL and PDF. Supported document choices makes PDF optional for real Sage PA France and requires one hybrid file for the Factur-X path. Use a qualified provider-specific manifest; do not universalise the Demo rule.
- For `MALICIOUS_ATTACHMENTS`, the guide advises removing the local file reference and re-uploading from a fresh local file, then inspecting status. It supplies no invoice amendment/removal endpoint, scan policy, upload renewal or safe retry contract.
- A Factur-X/ZUGFeRD 2.3 hybrid PDF is declared as `application/pdf`. Retrieval can generate and persist a hybrid file from separate UBL/PDF attachments; an existing hybrid is returned without regeneration. This does not prove DTS coverage, original-file equivalence or Spain acceptance.

## Step 4 — Receive invoice sent event

- Example event `type`: `com.sage.network.api.e-invoicing.einvoice.statusupdated`; prefix and `source` vary by environment/access point. This differs from the subscription's unprefixed `EventType`; qualify the event library rather than equate them.
- `subject` is the e-invoice ID. The example includes event `id`, `subscriptionid`, `accountid`, `datasetid`, time, trace context, `data.id` status identifier and nullable `data.errorCode`. Optional `clientstate` is returned as a header.
- The example repeats `specversion`. Step 4 calls this an invoice-sent event, while step 1 allows final `ERROR`. Completion of processing is not a universal success signal.
- Webhook authentication, delivery guarantees, replay/order/version handling and Spain event support are not established by this example.

## Step 5 — Get invoice details

- Operation card: `GET /datasets/{datasetId}/e-invoices/{e-invoiceId}` returns `200 OK`. The overview sequence instead shows the collection path; use the detail card for this evidenced operation and confirm the schema.
- The response exposes `currentStatus`, `history[]`, `statusId`, `statusCode`, `status`, `operationStatus`, `errorCode`, `notes`, `rejectionReason` and history metadata. `operationStatus` values are `IN_PROGRESS`, `COMPLETED`, `ERROR`. Status IDs/codes and their mapping need the missing Invoice Statuses guide.
- Attachment details include `filename`, `mimetype`, `downloadUrl` and `filetype`: `Undefined`, `UBL`, `Human_Readable`, `Original_Document`.
- Optional `format=facturx` can generate and persist a Factur-X/ZUGFeRD 2.3 file. This is a potentially state-changing representation request despite its GET method. It is not required for status observation.
- Status freshness, post-error handling, file retention, URL expiry and original-operation discovery after a lost POST response are not defined here.

## Evidence still needed

Later supplied evidence: [INT-ERR01 error-handling guide](<../Shared/invoice-flow-error-handling-guide-extract.md>) clarifies history-only error/outcome fields, attempt finality and code-specific platform retry/support actions. The limits below describe what this sending guide alone establishes; the later guide does not qualify Spain build support or event/attempt correlation.

Obtain the selected OpenAPI, event library, status/error guides, provider/environment matrix and actual build from the API owner. Qualify every Spain field, representation, authority rule, public action and recovery path separately. The generic archiving note establishes no country retention duration or conservation implementation.
