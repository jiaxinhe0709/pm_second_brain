# Connections Service certificate API — reviewed extract

Source: [1.2.1. Connection Service](https://confluence.sage.com/spaces/CCLD/pages/467063094/1.2.1.+Connection+Service), page 467063094, version 4; read 26 October 2026. This curated extract records field names and behaviour only. Original credential values, tokens, provider IDs and raw page exports are omitted.

## Certificate upload

The page documents `POST /datasets/{dataset_id}/connections` under **Certificate upload → Request**.

| Example field | Supplied value / meaning |
|---|---|
| `data.type` | `Connection`. |
| `data.attributes.providerId` | AEAT credential provider ID obtained from `/connections/providers`; actual provider ID omitted. The lookup method/response and a B2B provider are not established here. |
| `data.attributes.label` | Connection label. |
| `data.attributes.credentials.type` | `certificate`. |
| `data.attributes.credentials.expiresBy` | When the certificate expires. An input value is not proof that the certificate has been validated. |
| `data.attributes.credentials.credentialsObject.type` | Example uses `personal-certificate`. |
| `data.attributes.credentials.credentialsObject.certificatesecret` | Certificate contents. Preserve this exact field spelling. |
| `data.attributes.credentials.credentialsObject.password` | Certificate password. |

The request header table lists `x-api-key`, `traceparent`, `tracestate` and `Authorization`; no credential/header values are retained here.

Under **Certificate upload → Response**, the example returns `data.type: Connection`, `data.id`, `data.attributes.providerId`, `data.attributes.label`, `data.links.credentialsPatchEndpoint.href` and audit `data.meta` fields. The field table describes `data.id` as the connection ID needed for submission. It does not establish a certificate-readiness or validated-expiry response.

### Source inconsistencies

- The request example nests `credentialsObject` below `credentials`. The field table instead labels paths below `data::attributes::certificate::credentialsObject`. The owner must confirm the actual contract.
- The response example contains JSON punctuation errors. A readable example may normalise those punctuation errors, but must not silently resolve the nesting conflict.
- HTTP success codes, a credential lookup/readiness response, and B2B acceptance are not established by this page's examples.

## Internal encryption

Under **Internal - Encrypt**, the page documents `POST /datasets/{dataset_id}/compliance/es-anti-fraud-legislation/encryptions`.

| Direction | Fields |
|---|---|
| Request | `data.type: encrypted-certificate`; `data.attributes.secret`. |
| Response | `data.type: encrypted-certificate`; `data.id`; `data.attributes.encryptedSecret`. |

The header table lists `traceparent`, `tracestate`, `Idempotency-Key` and `Authorization`. The source does not establish the certificate/password serialisation inside `secret` or an external product permission to call this internal operation.

## Scope

These are ES AFL design/documentation facts, not proof of deployed B2B support. Certificate connection IDs must not be assumed equal to E-Invoice access-point connection IDs. Use the [certificate-management extract](sage-certificate-management-guide-extract.md) for credential selection and custody.
