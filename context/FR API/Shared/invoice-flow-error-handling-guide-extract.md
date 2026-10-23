# Invoice-flow error handling — supplied FR guide evidence

Source ID: **INT-ERR01**. Received 22 October 2026. Original attachment SHA-256: `db1584ba56f6d7236ca34a03e1301862ee25e61e2317d6096e8ecf1c6ec4e44a`.

The original guide's revision, canonical page URL and deployed build were not supplied. It links a development-hosted retrieve-invoice reference whose path contains `1.13.0`; that link does not establish the supported runtime version. This selective extract omits example identities and payloads. The dictionary below preserves the supplied 45 codes, descriptions and recommended actions. These are FR flow codes, not AEAT response codes or proof of Spain support.

## Processing and error fields

- The guide says a status notification is sent after handling the invoice/status-change attempt. Processing is complete for that attempt; `ERROR` is final for that attempt. It does not mean all business obligations are complete or the invoice is successfully delivered.
- Processing outcome is `data.attributes.history[].operationStatus`: `IN_PROGRESS`, `COMPLETED`, `ERROR`. Nullable troubleshooting code is `data.attributes.history[].errorCode`.
- `data.attributes.currentStatus` is the latest status snapshot. It does **not** contain `operationStatus` or `errorCode`. The example retains `Submitted` while the associated history item has `operationStatus: ERROR` and `ERR-SENDING-DOC-004`.
- The guide marks `data.meta` required in the retrieve response. Correlate the relevant history item/attempt using the qualified identifiers and metadata. Neither history ordering nor a complete correlation contract is supplied.

## Error codes dictionary

Descriptions and recommended actions in the following four tables are supplied source wording. Internal implementation names identify the guide's context; they do not allocate Spain requirements to those components.

### Sending a document (`ERR-SENDING-DOC`)

| Error code            | Description                                               | Recommended action                                                                                                    |
| --------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ERR-SENDING-DOC-001` | Failure getting document from the eInvoicing Service.     | Temporary processing issue. Retry is handled by the platform flow. If unchanged after 6 days, contact support.        |
| `ERR-SENDING-DOC-002` | Failure to send the notification back.                    | Temporary delivery issue. Retry is handled by the platform flow. If unchanged after 6 days, contact support.          |
| `ERR-SENDING-DOC-003` | Failure getting attachments from the eInvoicing Service.  | Temporary retrieval issue. Retry is handled by the platform flow. If unchanged after 6 days, contact support.         |
| `ERR-SENDING-DOC-004` | Failure sending document to the provider.                 | Temporary provider delivery issue. Retry is handled by the platform flow. If unchanged after 6 days, contact support. |
| `ERR-SENDING-DOC-005` | Failure storing sender tracking data.                     | Internal tracking persistence issue. Contact support if status remains unchanged.                                     |
| `ERR-SENDING-DOC-006` | Unexpected exception.                                     | Internal unexpected issue. Contact support and include identifiers.                                                   |
| `ERR-SENDING-DOC-007` | Failure to retrieve the idempotency key for this request. | Verify that the request includes a valid idempotency key. Contact support if the error persists.                      |

### Receiving event `einvoice.received` (`ERR-RECEIVING-DOC`)

| Error code              | Description                                               | Recommended action                                                                                               |
| ----------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `ERR-RECEIVING-DOC-001` | Failure to send the notification back.                    | Temporary notification issue. Retry is handled by the platform flow. If unchanged after 6 days, contact support. |
| `ERR-RECEIVING-DOC-002` | Failure to retrieve the idempotency key for this request. | Verify that the request includes a valid idempotency key. Contact support if the error persists.                 |

### Processing status change (`ERR-SENDING-STATUS`)

| Error code                | Description                                               | Recommended action                                                                                 |
| ------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `ERR-SENDING-STATUS-001`  | Failure getting the event type (not recognized).          | Treat as a general status-processing error. Contact support if unchanged after 6 days.             |
| `ERR-SENDING-STATUS-002`  | Failure to send the notification back.                    | Temporary delivery issue. Retry is handled by the platform flow.                                   |
| `ERR-SENDING-STATUS-003`  | Failure getting document from the eInvoicing Service.     | Temporary retrieval issue. Retry is handled by the platform flow.                                  |
| `ERR-SENDING-STATUS-004`  | Failure getting attachments from the eInvoicing Service.  | Temporary attachment retrieval issue. Retry is handled by the platform flow.                       |
| `ERR-SENDING-STATUS-0010` | Failure in extracting data from UBL.                      | Temporary workaround path; expected to be removed when extraction moves to the eInvoicing Service. |
| `ERR-SENDING-STATUS-005`  | Failure to map invoice status context.                    | Mapping issue. Contact support.                                                                    |
| `ERR-SENDING-STATUS-006`  | Failure to update invoice status.                         | Internal status update issue. Contact support if unchanged after 6 days.                           |
| `ERR-SENDING-STATUS-007`  | Unexpected exception.                                     | Internal unexpected issue. Contact support and include identifiers.                                |
| `ERR-SENDING-STATUS-008`  | Status not supported.                                     | Confirm that the value is an invoice status and that the receiving partner supports it.            |
| `ERR-SENDING-STATUS-009`  | Failure to store transaction information in DynamoDB.     | Internal transaction persistence issue. Contact support.                                           |
| `ERR-SENDING-STATUS-0011` | Failure to retrieve the idempotency key for this request. | Verify that the request includes a valid idempotency key. Contact support if the error persists.   |

### Receiving SVIX notification (`ERR-RECEIVING-NOT`)

| Error code              | Description                                              | Recommended action                                                                                                     |
| ----------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `ERR-RECEIVING-NOT-001` | Failure verifying webhook request.                       | Verify webhook setup and signature configuration. Contact support if unresolved.                                       |
| `ERR-RECEIVING-NOT-002` | Failure mapping handler based on partner status code.    | Internal mapping issue. Contact support.                                                                               |
| `ERR-RECEIVING-NOT-003` | Failure to process the notification.                     | Internal processing issue. Retry is handled by the platform flow.                                                      |
| `ERR-RECEIVING-NOT-004` | Failure to send SQS to Webhook Handler.                  | Internal queue handoff issue. Contact support if status remains unchanged.                                             |
| `ERR-RECEIVING-NOT-005` | Failure to mark notification as failed.                  | Internal state update issue. Contact support.                                                                          |
| `ERR-RECEIVING-NOT-006` | Failure to get the notification from Sovos.              | Temporary upstream retrieval issue. Retry is handled by the platform flow.                                             |
| `ERR-RECEIVING-NOT-007` | Notification content is empty.                           | Upstream payload issue. Contact support and provide payload metadata.                                                  |
| `ERR-RECEIVING-NOT-008` | Failure identifying address type.                        | Data classification issue. Contact support.                                                                            |
| `ERR-RECEIVING-NOT-009` | Failure to create invoice on eInvoicing service.         | Internal creation issue. Retry is handled by the platform flow.                                                        |
| `ERR-RECEIVING-NOT-010` | Failure to update attachments on eInvoicing service.     | Internal attachment update issue. Retry is handled by the platform flow.                                               |
| `ERR-RECEIVING-NOT-011` | Failure in extracting data from UBL.                     | Temporary workaround path. This is expected to be removed when extraction is moved into the eInvoicing Service.        |
| `ERR-RECEIVING-NOT-012` | Failure getting tracking record from DynamoDB.           | Internal tracking lookup issue. Contact support.                                                                       |
| `ERR-RECEIVING-NOT-013` | Failure adding recipient tracking record to DynamoDB.    | Internal tracking persistence issue. Contact support.                                                                  |
| `ERR-RECEIVING-NOT-014` | Failure getting the CDAR extractor function.             | Not used currently. Keep for reference only.                                                                           |
| `ERR-RECEIVING-NOT-015` | Failure getting the lifecycle URI from CDAR.             | Internal lifecycle retrieval issue. Contact support.                                                                   |
| `ERR-RECEIVING-NOT-016` | Failure downloading lifecycle document from provider.    | Temporary provider retrieval issue. Retry is handled by the platform flow.                                             |
| `ERR-RECEIVING-NOT-017` | Failure extracting attributes from CDAR.                 | Internal extraction issue. Contact support.                                                                            |
| `ERR-RECEIVING-NOT-018` | Failure building the notification.                       | Internal notification build issue. Contact support.                                                                    |
| `ERR-RECEIVING-NOT-019` | Failure sending notification to the eInvoicing Service.  | Temporary delivery issue. Retry is handled by the platform flow.                                                       |
| `ERR-RECEIVING-NOT-020` | Error extracting attachment for recipient.               | Not used currently. Keep for reference only.                                                                           |
| `ERR-RECEIVING-NOT-021` | Unexpected exception.                                    | Internal unexpected issue. Contact support and include identifiers.                                                    |
| `ERR-RECEIVING-NOT-22`  | Error getting the Lifecycles of lifecycles (LoL) record. | Confirm that a transaction exists for the document and transaction identifiers. Contact support if the error persists. |
| `ERR-RECEIVING-NOT-23`  | Error getting the transaction ID from the transaction.   | Internal transaction lookup issue. Contact support and include the document and transaction identifiers.               |
| `ERR-RECEIVING-NOT-24`  | Error adding a transaction to the transactions table.    | Internal transaction persistence issue. Contact support.                                                               |
| `ERR-RECEIVING-NOT-25`  | Transaction is duplicated.                               | The transaction may already have been processed. Confirm the existing transaction before retrying.                     |

## Recovery interpretation and limits

| Source fact | Required assessment before reuse |
|---|---|
| Selected temporary errors say retry is handled by the platform flow | Do not turn them into product-side fresh invoice POST, renewed idempotency key or whole-flow resend. Establish the platform retry/attempt identity and observable result. Other codes instead request support or data/configuration correction. |
| `ERROR` is final for an attempt, while some rows describe platform retry | The retry trigger, timing, new-attempt relationship and eventual completion contract remain unqualified. A failed attempt cannot later be silently overwritten as success; retain each result. |
| Some rows say contact support if unchanged after 6 days | This is code-specific guidance in this FR source, not a universal retry duration, SLA, monitoring threshold or Spain legal reporting allowance. It does not justify waiting on security, missing data or a statutory obligation. |
| Idempotency-key errors | Confirm where the original key comes from and who owns it, especially on a received-event flow. The guide does not define a new GET header or give permission to create another invoice/key. |
| `ERR-RECEIVING-NOT-25` | Check the existing transaction before retry. A duplicate transaction does not alone establish verified file capture or product business receipt. |
| `ERR-RECEIVING-NOT-014` and `ERR-RECEIVING-NOT-020` | Source says not currently used. Preserve for reference; do not require a new runtime branch without selected-build evidence. |
| `ERR-SENDING-STATUS-0010`, `ERR-SENDING-STATUS-0011`, `ERR-RECEIVING-NOT-22` through `-25` | Preserve the exact inconsistent zero padding. Do not normalize code strings. |
| Lifecycle-document failures | `ERR-RECEIVING-NOT-016` concerns downloading a lifecycle document. This is distinct from downloading the original invoice or its attachments. CDAR/LoL, provider transaction and Spain ApplicationResponse mappings remain to qualify. |

This dictionary does not establish HTTP errors, source-file URL expiry/range behaviour, AEAT error meanings, notification authentication details, retention or complete provider recovery. Read it with INT-SND01 and INT-RCV01, then qualify the selected Spain build, owner and contract. Unknown external effects still require reconciliation before unsafe repetition.
