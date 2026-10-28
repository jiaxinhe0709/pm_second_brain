# Spain AEAT certificate upload — reviewed extract

Source: user-supplied internal developer guide, **Spain AEAT Certificate Upload**, received 27 October 2026. Original page URL and revision were not supplied. Attachment SHA-256: `67f792a47872a52f4b45e7835b2da6892a82afbad0b72ba14ec35eebef72afef`. This extract preserves contract names and omits source credentials, tokens, provider/dataset IDs and raw exports.

The guide covers **Spain Anti-Fraud Legislation (AFL)**. It does not establish B2B e-invoicing acceptance, deployment coverage or certificate readiness.

## Environments and prerequisites

| Environment | Base URL |
|---|---|
| Sage Network Internal Sandbox | `https://api-int.network-eng.sage.com` |
| Production | `https://api.network.sage.com` |

Enablement supplies a product- and environment-specific API key. Domain Services onboarding supplies the business dataset. B2B use and the mapping to the product's SXS/E-Invoice dataset need owner confirmation.

Both operations list required `x-api-key`, `traceparent`, `Idempotency-Key` and `Authorization` headers; `tracestate` is optional. Authorization uses a Bearer Domain Services token. The guide requires `Idempotency-Key` for GET as well as POST. It does not specify a request media type or prove replay behaviour.

## Obtain provider ID for Spain AEAT

**`GET /connections/providers` → `200 OK`.** This step is optional when the appropriate provider ID is already known.

The response contains `meta.totalPages` and `data[]` entries with `type: Provider`, `id`, `attributes` and audit metadata. Select the entry with `attributes.providerCode: es-aeat`; keep its returned `id`. Its example has `attributes.credentialType: certificate` and `attributes.categories: ["es-aeat-afl"]`.

This is a provider catalogue. It does not list a business's saved credentials. Lookup and upload examples use different provider IDs; callers must use the ID returned for their selected environment/provider.

## Upload certificate

**`POST /datasets/{datasetId}/connections` → `201 Created`.** The snippet omits the initial slash; the request example establishes this path.

| Request field | Required / meaning |
|---|---|
| `data.type` | `Connection`. |
| `data.attributes.providerId` | Required; returned AEAT provider ID. |
| `data.attributes.label` | Optional connection label. |
| `data.attributes.credentials.type` | Required; `certificate`. |
| `data.attributes.credentials.expiresBy` | Optional declared expiry; not validated expiry. |
| `data.attributes.credentials.credentialsObject.type` | Optional; example uses `personal-certificate`. |
| `data.attributes.credentials.credentialsObject.certificatesecret` | Required certificate contents; exact source spelling. |
| `data.attributes.credentials.credentialsObject.password` | Required certificate password. |

The response returns `data.type: Connection`, `data.id`, `data.attributes.label`, `data.attributes.providerId`, `data.links.credentialsPatchEndpoint.href` and audit `data.meta`. Keep `data.id` as the credential connection reference used for AFL submission. The guide does not establish whether it shares an ID with, maps to, or is independent of an E-Invoice access-point connection. Do not substitute references across the two APIs without an owner-confirmed contract.

## Source conflicts and limits

- The example uses `credentials.credentialsObject`; the field table uses `certificate.credentialsObject`. The service owner must confirm the actual nesting.
- The response example has a trailing comma and is placed under “Response Header”; its field table describes a JSON resource. Examples may correct punctuation without resolving the nesting conflict.
- A returned `credentialsPatchEndpoint.href` does not establish an update method, body or renewal behaviour.
- `201` confirms provisioning, not NIF validity, authority, validated certificate expiry, trust/revocation, action suitability or public-platform access.
- No credential-readiness lookup, B2B provider permission or B2B secure-upload boundary is established. See [SPEC001](../../../specs/SPEC-SEI-001-certificate-management-solution-specification.md), CERT-04/05 and G1/G3/G9/G10/G11.

The [earlier Connections Service page](connections-service-certificate-guide-extract.md) documents the internal encryption operation. The [certificate-management page](sage-certificate-management-guide-extract.md) documents credential selection and custody.
