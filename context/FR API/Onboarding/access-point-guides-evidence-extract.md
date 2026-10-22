# Access-point guides — supplied technical evidence extract

Source: user-supplied guides and inline access-point material, received 22 October 2026. Canonical guide URLs, publication dates and deployed builds were not supplied. Ownership and error-handling attachments were each supplied twice with identical content; each pair is one source.

This extract retains technical claims used in SPEC-SEI-020. Example tokens, webhook secrets, personal/company data, operational identifiers and full payloads are omitted. The original five FR OpenAPI snapshots remain unchanged. These guides add evidence; they do not silently amend a selected contract or establish Spain support.

| Source ID | Supplied material | Version evidence and limit |
|---|---|---|
| INT-AP01 | Connect guide beginning with the onboarding video; sections Choose the right connection model, Direct API or Embedded UI, Consent and audit data, Partner routing and lifecycle constraints, and numbered steps 0–5 | Describes the France flow. No guide revision or deployed build supplied. |
| INT-AP02 | Update guide; Overview, steps 1–4, Update addresses safely | Safe-update text names API v1.1.0 for `remove`; its field table still describes older restrictions. No complete version-specific OpenAPI supplied. |
| INT-AP03 | Offboarding guide; Overview, Remove accesspoint connection, Accesspoint connection updated event | Links an API specification labelled 0.1.7. This does not prove DELETE support for every current provider/version. |
| INT-AP04 | Address-ownership guide; Transfer Scenarios, Implementation Steps, Confirm connection details | Links an API specification labelled 0.1.9. Contains last-one-wins guidance, not a universal conflict-resolution guarantee. |
| INT-AP05 | Error-handling guide; Retention window, Error Object, Error Codes Dictionary, Unknown error codes | Its endpoint link contains 1.10.0. Version alignment with the other guides is unverified. |
| INT-AP06 | Inline message: Retrieve dataset access points; access-point catalogue/environments; address types/design; permitted operations; statuses/retry behaviour; status notifications | No revision supplied. Includes facts and conflicts requiring selected-contract qualification. |

## INT-AP01 Connect and channel selection

- One dataset connects to a selected access point once. Subsequent address changes use the existing connection. This is a dataset/access-point constraint, not proof of one legal entity per dataset.
- Connect can register multiple addresses. The guide says to include SIREN plus other required address types; this additional requirement is not established by the saved schema's `minItems: 1` alone.
- The documented operation is `POST /connectors/{accessPointId}/datasets/{datasetId}/connect`. The guide's overview sequence contains a malformed path placeholder; use the saved FR-03 signature as the baseline until the owner confirms the canonical contract.
- A pre-registered portal address can be linked to a product dataset using the same address; additional addresses may be included.
- The integrating product owns the address/dataset/client mapping and its ongoing management. Enablement and Engineering advise. The product must operate within supported platform, authority and country constraints.
- An official SIREN/SIRET address has one active directory route. A registration through another dataset/provider can replace that route. A production handover needs Enablement planning; do not rely on delete-and-recreate.
- Direct `/connect` and Embedded UI are alternative registration experiences. Embedded UI needs partner enablement; its short-lived launch URL remains on the server. No full Embedded UI contract is supplied.
- The partner obtains and retains customer authority. Company and `user` fields record current audit context; they can be updated and do not independently prove authority.
- The guide describes Domain Services tokens and Sage ID M2M tokens. The saved OpenAPI snapshots declare M2M; actual caller/surface support needs qualification.
- The guide shows `POST /internal/events/subscriptions`, then the completed event and a connection detail read. The documented subscription path does not grant access to unrelated internal-only directory APIs; qualify the correct surface and credentials.

## INT-AP02 Update and removal

- Update an existing connection with `PUT /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/`. The update guide requires the product to retain dataset, access-point and connection references.
- The main field table describes address actions such as `add`/`remove`; it limits `usage` to `add`. The later **Update addresses safely** text says `action: "update"` can change `usage` or `endDate` and says to omit `usage` to restore all supported operations. These statements need a version-specific owner decision.
- The later text says address `remove` requires API v1.1.0 and recommends pinning the intended OpenAPI. It says no `GET /version` endpoint exists. This is address removal, not dataset deletion.
- The response field table mentions `COMPLETED`; the saved schema and status guide use `CONNECTED`. Preserve the source discrepancy rather than rename states.
- The guide describes `e-invoicing.accesspointconnection.updated` for completed amendments and disconnection. An address-removal result has `action: "remove"`; retrieve detail to confirm the resulting address list.

## INT-AP03 Connection disconnection

- The guide documents `DELETE /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}` with `202 Accepted` and no success body. The sequence diagram includes a trailing slash; the operation card does not. Confirm the selected signature and provider support.
- `202` means the request was accepted; the guide later uses the updated event and a detail read to confirm processing. There is no separate offboarding event in this flow.
- The guide's final instruction is to confirm address removal and stop sending as required. It does not establish dataset deletion, safe rollback, legal-authority withdrawal, release of earlier invoice obligations or a complete exit process.
- Its legacy whole-connection deletion flow needs reconciliation with INT-AP01's France handover constraints and INT-AP02's versioned address removal. It is not universal permission to disconnect/recreate a production route.

## INT-AP04 Address ownership transfer

- Scenario A links a pre-registered address to the product dataset. Scenario B describes a product taking an address currently mapped to another product dataset; the example is an accountant product followed by the customer's own product.
- Implementation Steps describe the latest product calling connect as taking ownership. Treat this as a potentially routing-changing operation, not a harmless local account link.
- The guide uses `Content-Type: application/json` for connect, while FR-03 declares JSON:API media type. Its connect header table omits the FR-03 required idempotency header; omission from a guide is not proof that the header is optional.
- The guide puts a required `Idempotency-Key` in the GET-detail header table; FR-04 does not. Confirm that discrepancy.
- Its “if subscribed” notification language also allows tracking with a detail read. Source error codes, provider constraints and operation results still need checking; this guide does not establish that every duplicate address can be taken over.

## INT-AP05 Error handling and retry ownership

Errors are per address in `data.attributes.accessPointAddresses[]`. The guide says onboarding errors remain available in status responses for **7 days**. This is source-observation availability, not Sage audit/retention policy.

The `{scope}` suffix means `0` Create/Update Connection, `1` GetToken, `2` CreateCompany, `3` CreateInboundEndpoint, `4` CreateOutboundEndpoint, `5` UpdateEndpoint. Retain the exact code and its upstream stage. These are source responsibilities, not new required Spain components.

| Code or class | Supplied guidance | Reuse limit |
|---|---|---|
| `ERR-408-{scope}`, `ERR-401-{scope}`, `ERR-403-{scope}`, `ERR-429-{scope}`, `ERR-500-{scope}`, `ERR-502-{scope}`, `ERR-503-{scope}`, `ERR-504-{scope}` | Platform retry; monitor or contact support. `ERR-408` says contact support if unchanged after 6 days. | Embedded upstream codes differ from the caller's HTTP 401/403. Platform retries do not authorise another product connect request. Resolve horizon conflicts with INT-AP06. |
| `ERR-400-{scope}`, `ERR-FR004-{scope}`, `ERR-PPL001-{scope}` | Platform retry/investigation for unexpected or upstream retrieval/service errors. | France/Sovos/Peppol-specific classification; no automatic Spain mapping follows. |
| `ERR-ADDRESS-0` / `ERR-ADDRESS-1` | Duplicate within a connection / duplicate in the system; source advises skipping an already connected address or correcting a duplicate. | Reconcile with INT-AP04 takeover guidance. Do not replace a genuine official identity with an invented unique value to bypass a conflict. |
| `ERR-ADDRESS-2`, `ERR-ADDRESS-3`, `ERR-ADDRESS-4` | Company/inbound/outbound endpoint already exists, possibly after partial persistence; support reconciliation before resubmission. | Keep the original effect and operation. Duplicate errors can be evidence of earlier effects. |
| `ERR-FR001-{scope}`, `ERR-FR002-{scope}`, `ERR-FR003-{scope}` | Directory/date or mandate-scope issues; support or client/compliance correction before resubmission. | Preserve France source codes; Spain needs its own authority and provider rules. |
| `ERR-PPL002-{scope}` | Existing SML endpoint; offboard the other PA first or obtain a confirmed workaround. | Do not generalise last-one-wins to this case or enable a previously gated migration. |
| `ERR-USAGE-{scope}` | Usage/company/endpoint collision; first successful usage wins; manual remediation may be needed. | Reconcile with update-usage and takeover claims for the selected provider/build. |
| `ERR-INTERNAL` | Support guidance before resubmission. | No assumed automatic recovery. |

The unknown-error note says to tell users that automatic retries are occurring. This needs reconciliation with actual status/retry evidence and the no-automatic-resubmit rows above. A Spain product must not claim a retry that is not established.

The guide's `ERR-PPL002-3` example says a connection can appear connected while the failed address is absent from `accessPointAddresses`. That address is not ready to receive. Absence alone is therefore insufficient proof of successful removal, no earlier effect or receiving readiness; use correlated action/result evidence.

## INT-AP06 Catalogue, address mapping and environments

- `GET /datasets/{datasetId}/accesspoints` returns access-point `id`, name, dataset-level CONNECTED/DISCONNECTED and nullable `connectionId`. It can recover a known dataset's resource references. It is not a global dataset inventory or an original-operation reconciliation contract.
- The access-point ID represents a service route shared across clients/products. The connection ID is dataset-specific. Actual country/provider/environment binding still needs qualification.
- The real Sage PA France connector uses Sovos UAT in INT/SBX and Sovos Production in PROD. The supplied environment table shows no France directory in INT/SBX, France PPF in PROD, Peppol test in INT/SBX and Peppol production in PROD. No load/stress testing is available under the guide's stated limits.
- Sage PA France Demo has no Sovos, directory or Peppol integration in the supplied environment table. It supports mock/basic flows with reduced validation and error fidelity, even though a PROD environment row is listed. It does not qualify real submission, directory effects or Spain support.
- Prefer one dataset and one official address registration per legal entity **wherever possible**. This is product integration guidance, not an enforced universal one-to-one limit. Independently registering the same official address can redirect traffic to the last successful registration.
- `fr.siren_suffix` and `fr.sirensiret_routing` are partner-defined internal routes. They do not replace official directory registration or establish additional legal entities. Hybrid/provider architecture needs Enablement confirmation.

### Address types and lengths

Both internal and legal address formats are documented; the guide recommends legal formats for new integrations.

| Type | Guide representation | Declared field length / limit |
|---|---|---|
| `fr.siren` | SIREN | 9 |
| `fr.sirensiret` | SIRET; legal representation includes SIREN and SIRET separated by `_` | 14; the longer legal representation needs clarification against this figure. |
| `fr.siren_suffix` | SIREN plus user-defined non-geographical suffix; legal representation uses `_` | 110 |
| `fr.sirensiret_routing` | Establishment plus internal routing code; legal representation includes SIREN, SIRET and routing code separated by `_` | 125; differs from FR-03/05 input max 114 and FR response max 50. |

The supplied internal-format description for the final row and its example also need owner clarification on whether SIREN is repeated. Do not derive a validator from examples alone.

### Permitted operations

The inline guide lists omitted usage as all supported operations, plus `SEND`, `RECEIVE` and `EREPORTING`. FR-03/04/05 and other supplied guide field tables list only SEND/EREPORTING with at most one explicit value. Confirm `RECEIVE` and combined restricted modes against the selected contract/build; do not silently extend the saved enum.

### Status, retries and notifications

- The status guide lists IN_PROGRESS, RETRYING, CONNECTED and ERROR. RETRYING is platform-managed for up to **24 hours**, then ERROR. It tells products not to submit duplicate connect requests and to poll/process notifications; unresolved work beyond 24 hours goes to support.
- It says no DEACTIVATED status exists; removed or expired addresses disappear from detail. This does not remove the need for evidence of the original action or erase the failed-absent-address case in INT-AP05.
- A completed notification occurs when an individual address reaches CONNECTED or ERROR. One connect request can produce several notifications and a partial address result.
- Exact source strings vary: guide prose uses `e-invoicing.accesspointconnection.completed` / `.updated`; CloudEvent examples use `com.sage.network.api.e-invoicing.accesspointconnection.completed` / `.updated`; the inline illustration uses `accesspointconnection.completed`. Source URLs, casing and subscription fields also vary. Qualify the event library and actual environment-specific contract; do not assume these are interchangeable aliases.
- Event `subject` is described as `connectionId`. Deduplication, ordering, authentic delivery, current access and authoritative read behaviour still need qualification. A completion event is not blanket customer readiness or an activation decision.
