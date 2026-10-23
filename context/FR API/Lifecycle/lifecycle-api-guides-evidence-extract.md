# French lifecycle API guide evidence

Received from the user on 22 October 2026. This curated extract records four supplied guides and the transition-outcome note pasted in chat. It omits video embeds, UI markup, example tokens and webhook credentials. Guide revision and deployed build are unknown. Linked API paths display E-Invoicing `1.13.0` and Notifications `6.3.0`; those links do not prove the running version.

## INT-LCS01 Send a status update

Prerequisites: a company dataset connected to an access point, an invoice already posted to that access point and its e-invoice ID. The guide documents Domain Services or Sage ID M2M authentication. Authentication does not establish represented-business authority for a Spain action.

| Contract element | Supplied guide evidence |
|---|---|
| Operation | `POST /datasets/{datasetId}/e-invoices/{e-invoiceId}/status` |
| Required headers | `Authorization`, `traceparent`, `tracestate`, `Idempotency-Key` |
| Envelope | `data.type = e-InvoiceStatus`; `data.attributes.statusCode` is a UUID. |
| Variable data | `data.attributes.statusAttributes` contains only the selected status's documented fields. |
| Occurrence time | Optional `statusAttributes.lifecycleMetadata.statusDateTime`, UTC date-time. |
| Response | `data.id` identifies the status-change operation; response includes `statusCode`, resolved `status`, echoed `statusAttributes` and creation metadata. Example shows `201 Created`. |
| Rate response | `Retry-After` gives seconds before retry on `429`; the guide does not define mutation safety, key retention or conflict handling. |

| Status payload | Documented shape |
|---|---|
| In Hand / Approved | No status-specific attributes required. |
| Partially Approved | `statusAttributes.partiallyApprovedData[]`; required `motifCode`; optional `motifNote`, `approvedNetAmount`, `approvedTotalAmount`, `nonApprovedNetAmount`, `nonApprovedTotalAmount`, `currencyCode`. |
| Disputed | `statusAttributes.disputeData[]`; required `reasonCode`; optional `notes`, `requestedActionCode`, `requestedAction`. |
| Suspended | `statusAttributes.suspendedData` is one object; optional `reasonCode`, `reasonText`. |
| Completed | Optional `statusAttributes.completedData[]`; each supplied item needs `fieldId` and `fieldValue`. |
| Refused | `statusAttributes.rejectionData[]`; required `reasonCode`; optional `notes`. |
| Payment Sent / Payment Received | `statusAttributes.paymentData[]`; required `netAmount`, `currencyCode`; optional `vatRate`. One item per VAT rate. |

The guide supplies no separate payment/settlement endpoint. It uses lifecycle codes `211` and `212`, with UUIDs in the request. It says not to resubmit revised UBL merely to add payment data. It describes Payment Received as partial or full payment and calls it terminal.

## INT-LCS02 Receive notifications and read history

| Element | Supplied guide evidence |
|---|---|
| Subscribe | `POST /internal/events/subscriptions`; the snippet's path omits the leading slash. |
| Subscription | `resource = einvoice`; `eventType = e-invoicing.einvoice.statusupdated`; dataset, source, audience and HTTPS endpoint scope. |
| France source example | `https://api.e-invoicing.network.sage.com` for production `sage.pdp.france`. Resolve other access points/environments from the Events Library; no Spain source is supplied. |
| Notification | Example type `com.sage.network.api.e-invoicing.einvoice.statusupdated`; `subject` is the e-invoice ID. `data.id` is the workflow status UUID. `datasetid`, `accountid`, `subscriptionid`, `data.accessPointId` carry context. |
| Completion meaning | Notification follows finished processing, including `ERROR`. It is not proof of a successful transition. |
| Read | `GET /datasets/{datasetId}/e-invoices/{e-invoiceId}`; inspect `data.attributes.history`. Full history-entry schema is delegated to another guide, not supplied here. |

The example's top-level `id` is annotated as a resource/status ID; its uniqueness and relationship to POST operation `data.id` are not established. Do not substitute `data.id`, `subject`, notification `id` or operation `data.id` for each other. Delivery guarantees, webhook authentication, replay, pagination and operation correlation remain unqualified.

## INT-LCS03 Status catalogue and blocked transitions

The numeric code is display/catalogue evidence. The POST `statusCode` field takes the exact UUID.

| Numeric code | Guide status | UUID | Set by |
|---|---|---|---|
| 200 | New | `00000000-0000-0000-0000-170000000000` | Domain Services |
| 200 | File Uploaded | `00000000-0000-0000-0000-180000000000` | Domain Services |
| 200 | Submitted | `00000000-0000-0000-0000-100000000000` | Seller PA |
| 201 | Issued by platform | `00000000-0000-0000-0000-150000000000` | Seller PA |
| 202 | Received by platform | `00000000-0000-0000-0000-160000000000` | Buyer PA |
| 203 | Made Available | `00000000-0000-0000-0000-300000000000` | Buyer PA |
| 204 | In Hand | `00000000-0000-0000-0000-400000000000` | Buyer |
| 205 | Approved | `00000000-0000-0000-0000-500000000000` | Buyer |
| 206 | Partially Approved | `00000000-0000-0000-0000-600000000000` | Buyer |
| 207 | Disputed | `00000000-0000-0000-0000-700000000000` | Buyer |
| 208 | Suspended | `00000000-0000-0000-0000-800000000000` | Buyer |
| 209 | Completed | `00000000-0000-0000-0000-140000000000` | Buyer in list; supplier in explanation |
| 210 | Refused | `00000000-0000-0000-0000-120000000000` | Buyer |
| 211 | Payment Sent | `00000000-0000-0000-0000-900000000000` | Buyer |
| 212 | Payment Received | `00000000-0000-0000-0000-110000000000` | Seller |
| 213 | Rejected | `00000000-0000-0000-0000-130000000000` | PA |

Mandatory labels in this catalogue describe France. They do not establish Spain obligations or enabled actions. New, File Uploaded and Submitted share numeric `200` but have different UUIDs.

The guide calls Refused and Rejected terminal. Its blocked-transition table marks Payment Received nonterminal. That conflicts with INT-LCS01. It blocks Refused from Disputed, whereas INT-LCS01 explicitly permits Disputed → Refused. It also blocks Rejected from Submitted. Rejected is assigned Buyer in the blocked table but PA in the status list. The linked matrix workbook was not supplied or reviewed; its rules and precedence remain an evidence gate.

## INT-LCS04 French reason-code guide

The supplied guide attributes closed lists to FNFE CDAR rule `BR-FR-CDV-CL-09`. Its linked Schematron was not independently verified in this review. Lists are status-specific; additional B2G Refused reasons must not enter standard B2B defaults.

Business reasons use `rejectionData[].reasonCode`, `partiallyApprovedData[].motifCode`, `disputeData[].reasonCode` or `suspendedData.reasonCode`, as specified by INT-LCS01. These fields are distinct. The guide lists `NON_TRANSMISE` as a Deposited/Submitted outcome rather than rejection; it describes technical Rejected and Inadmissible separately. Inadmissible numeric `501` has no published Sage UUID in the supplied catalogue. No UUID or writable action can be inferred for it.

Sample values `DIS-001`, `SUP-001` and `PA-001` in INT-LCS01 are absent from the corresponding closed lists. Do not use them as approved validation fixtures. French reasons such as `DEST_ERR` and `CMD_ERR` are not Spain rejection reasons `01` and `02`.

## INT-LCS05 Transition outcome note

The user supplied these outcome rules separately from the four guides:

- The invoice remains on its latest successful status.
- A failed transition is recorded in `history` with `operationStatus = ERROR`.
- `IN_PROGRESS` means a transition is underway.
- `COMPLETED` means that transition succeeded.
- `ERROR` means the transition failed and the previous successful status remains.

`operationStatus = COMPLETED` differs from lifecycle status Completed (`209`). The note supplies no exact field path for the current status or full history-entry schema. A transport timeout does not establish `ERROR` at the external destination.

## Evidence limits

The guides support a common endpoint, status-specific payloads, asynchronous completion and history as implementation reuse candidates. They do not prove a configurable country registry, plugin architecture, Spain event UUIDs, arbitrary `statusAttributes`, independent reporting-destination results or deployed Spain support. Qualify those claims against the selected schema, build and tests.

The separately available [FR error-handling evidence, INT-ERR01](<../Shared/invoice-flow-error-handling-guide-extract.md>) supplies the paths `data.attributes.history[].operationStatus`, nullable `history[].errorCode` and `data.attributes.currentStatus`. The snapshot object has no attempt outcome/error fields. That source adds field evidence; the complete history schema, attempt correlation and runtime coverage still need qualification.
