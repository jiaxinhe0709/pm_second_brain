# Network Onboarding: Create a datasetId (tenantId) — supplied guide extract

Source: user-supplied internal copy, attached as `Pasted text.txt` on 22 October 2026. The guide describes an external partner integration. Its canonical internal URL, publication date, revision and deployed build were not supplied. The API links contain `v1.0.0`; this does not establish the guide's revision.

This technical extract retains the statements used in SPEC-SEI-020. Example company data, payload identifier values, video and navigation components are omitted. It is not the complete original guide or an OpenAPI contract. Source-dependent conclusions remain subject to owner confirmation.

## What is a dataset? / Partner tenancy model

The supplied guide states:

- A dataset is a business identity in Domain Services. One partner account can manage many datasets.
- Create one dataset for each customer legal entity. It does not represent an accounting firm, group contract, ERP instance, buyer-only role or seller-only role.
- The same dataset supports sending and receiving. Permitted operations are selected when the address is connected to an access point.
- The returned `tenantId` is the `datasetId` used in subsequent API calls. Store it against the customer in the integrating application.
- One partner account can manage its datasets through one M2M credential set.

### Ownership and access

- Datasets are scoped to the creating partner account. Calls through a different partner account cannot access that `datasetId` and return `403 Forbidden`.
- No external endpoint lists every dataset. Store the identifier when created; a global lookup cannot recover the dataset inventory.
- Dataset deletion is not currently exposed externally. Contact Sage support if required.
- Where an approved flow returns a dataset after customer consent, store the `datasetId` from the returned access-point connection. This statement does not supply that flow's contract or equate consent with action authority.

## Multi-product and existing Sage channels

- Do not assume an API-created dataset is linked to Sage Connect or an existing native Sage-product account. These are separate provisioning channels unless Sage confirms the architecture.
- Review the access-point registration plan when an address is already registered through another channel/provider. Registering the same official address can change active routing.
- Native product synchronisation and the direct E-Invoicing API are separate integration channels. A hybrid implementation needs its dataset/connection relationship confirmed with Sage Enablement before development.

## Prerequisites / Workflow summary / Steps 1–2

Prerequisites include external partner access, an M2M bearer token, a selected environment and a unique idempotency key for create and delete operations. The deletion statement conflicts with the external-deletion limit above; do not infer an available delete operation.

| Source step | Documented operation | Result and limit |
|---|---|---|
| Step 1: Create Buyer Dataset | `POST /datasets` | `202 Accepted`, no response body; provisioning has started. This is not a returned dataset ID or confirmed completion. |
| Step 2: Confirm Buyer Dataset | Repeat `POST /datasets` with identical input and the same idempotency semantics | `200 OK` when ready. The guide does not specify an operation ID, replay window, in-progress response sequence, interval, budget or complete error/recovery contract. |

Both steps document `Authorization: Bearer {jwt}`, required `X-Idempotency-Key` and `Content-Type: application/json`. The guide's `X-Idempotency-Key` is distinct from `Idempotency-Key` in the supplied FR connection-create contract. Do not silently normalise them or infer identical guarantees.

### Field reference

| Field | Supplied description |
|---|---|
| `data.type` | Required; exact value `Dataset`. |
| `platform` | Required human-readable platform/company display name, preset by Enablement. |
| `businessName` | Required business name; maximum 255 characters. |
| `businessTypeCode` | Required supported legal-entity type; case-sensitive. Only French values are supplied below. |

The success example contains `data.id` and attributes `platform`, `businessName`, `businessTypeCode`, `accountId`, `productSubscriptionId`, `productLicenceIds`, `businessId` and `tenantId`. An example does not establish a complete mandatory response schema. The example's `data.id` and `attributes.tenantId` values differ; the prose explicitly instructs consumers to use `tenantId` as `datasetId`. The owner must explain the two identifiers before client mapping is finalised.

## French business type codes

| Exact code | Source label |
|---|---|
| `FR_Soletrader` | Sole Trader |
| `FR_Smallbusiness` | Small Business |
| `FR_Partnership` | Partnership |
| `FR_Limitedco` | Limited Company |

Spain codes, mappings, eligibility, provisioning availability and channel reuse are not established by this guide. The “Buyer Dataset” step labels do not override the explicit statement that a dataset can support both sending and receiving. This does not resolve its legal-entity cardinality.


## Review clarification: dataset, entity and address scope

On 22 October 2026, the user challenged treating the guide’s one-dataset-per-legal-entity instruction as a universal France implementation rule. This is an unresolved scope question, not evidence that multiple addresses must represent multiple legal entities.

The supplied two-row observation (FR-OBS01) has the same dataset, client reference and mandate for a `fr.siren` address and a `fr.sirensiret` address with that SIREN as its prefix. The structural relationship is retained here; raw business, client, mandate and dataset values are omitted. It demonstrates multiple addresses under a dataset. It does not demonstrate multiple distinct SIRENs or establish the meaning of the client reference.

The [create contract](new-accesspoint-connection.md), [detail contract](get-accesspoint-connection.md) and [update contract](put-accesspoint-connection.md) expose `accessPointAddresses` arrays. FR-05 requires all addresses in one update array to share a base SIREN and rejects a mixed-base request. This request-level restriction does not establish whether a dataset may contain different SIRENs across connections or separate operations.

The FR owner must confirm actual dataset-to-legal-entity cardinality, accountant representation, cross-client isolation and supported operations. Keep the original guide’s provisioning instruction as a source statement; do not promote it to a universal platform constraint. France identifier hierarchy and Spain NIF findings are sourced separately in SPEC-SEI-020 section 4.4.
