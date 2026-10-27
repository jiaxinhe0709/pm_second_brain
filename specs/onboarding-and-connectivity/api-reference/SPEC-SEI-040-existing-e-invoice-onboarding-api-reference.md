---
id: SPEC-SEI-040
title: E-Invoice Onboarding API Reuse and Spain Changes
type: api-reference
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: '2026-10-26'
updated: '2026-10-27'
reviewers: []
related:
  - SPEC-SEI-001
  - SPEC-SEI-039
  - GLO-SEI-001
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: '837610648'
  page_id: '938804297'
  title: E-Invoice Onboarding API Reuse and Spain Changes
  layout: two_left_sidebar
  toc: true
---

# E-Invoice Onboarding API Reuse and Spain Changes

Products: **Sage 50, Sage 200, Sage Active and Sage X3** are the ERPs; **Despachos** serves accountants. Each product needs the [SXS and Tax/Connections integrations in 038](../SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules). Resolve the client's dataset and reuse required credentials before onboarding; an unavailable lookup stays pending.

[039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md) owns the sequences, product impact and GAP decisions. This page shows request/response examples and Spain changes.

<span style="color:#666666;"><strong>Grey:</strong> existing calls/fields.</span> · <span style="color:#1565C0;"><strong>Blue:</strong> proposed Spain values or additional work.</span> Examples use synthetic data and the supplied sandbox URL. Replace IDs with service-returned values. Responses are extracts. Blue values, including `es.nif`, require API-owner confirmation; they do not prove provider availability or introduce new keys.

## 1 Existing calls to reuse

**An access point identifies a platform service; a connection links the dataset to that service; addresses belong to that connection.** FR-02/03/05; INT-AP01/06.

| Customer needs | Existing call |
|---|---|
| Another supported platform, with no saved connection to it | API-01/02 identify the service and missing connection; **API-03 POST** creates that dataset/access-point connection. |
| Another address within an existing platform connection | **API-05 PUT**, `action: "add"`, using that connection's existing IDs. |

**Open decision — Engineering / Architecture:** decide whether Spain public setup uses the access-point/connection model and how existing calls apply. Record the outcome under [039 GAP-02](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#4-open-engineering-decisions). No public enrolment API is established.

| Path ID — required UUID wherever present | Where it comes from |
|---|---|
| `datasetId` | Company's SXS mapping; confirm the E-Invoice binding and accountant/client scope. |
| `accessPointId` | Service ID from API-01. |
| `connectionId` | API-02 or API-03; retain it per dataset/access-point pair. |

All five E-Invoice templates use required Bearer M2M authentication and optional `traceparent`/`tracestate`. POST/PUT bodies use `application/vnd.api+json`; API-03 also requires `Idempotency-Key`. FR-01–05.

<a id="api-01"></a>

### 1.1 API-01 — Discover services

FR-01 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

**Request — no body or path parameters:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>GET https://api-sbx.e-invoicing.sage.com/accesspoints
Authorization: Bearer {sageIdM2MToken}
traceparent: {traceparent}
tracestate: {tracestate}</code></pre>
<!-- confluence-html-macro:end -->

**Response — `200 OK`, one proposed entry:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": [
    {
      "type": "AccessPoint",
      "id": <span style="color:#1565C0;">"00000000-0000-4000-8000-000000000002"</span>,
      "attributes": {
        "name": <span style="color:#1565C0;">"B2B Router"</span>
      }
    }
  ]
}</code></pre>
<!-- confluence-html-macro:end -->

Portfolio candidates: B2B Router, Banqup (Unifiedpost), EDICOM, SERES (Docaposte) and ZeroComa. **New candidate: Sovos.** REF-PROVIDERS. <span style="color:#1565C0;">Confirm target Spain services, contracts and IDs/environments before offering them; this catalogue entry is illustrative. GAP-02/06/08.</span>

Source conflict: FR-01 declares a path `datasetId` absent from its URL.

<a id="api-02"></a>

### 1.2 API-02 — Find existing connections

FR-02 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

**Request — no body:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>GET https://api-sbx.e-invoicing.sage.com/datasets/{datasetId}/accesspoints
Authorization: Bearer {sageIdM2MToken}
traceparent: {traceparent}
tracestate: {tracestate}</code></pre>
<!-- confluence-html-macro:end -->

**Response — `200 OK`, two saved private connections:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": [
    {
      "type": "AccessPoint",
      "id": <span style="color:#1565C0;">"00000000-0000-4000-8000-000000000002"</span>,
      "attributes": {
        "name": <span style="color:#1565C0;">"B2B Router"</span>,
        "status": "CONNECTED",
        "connectionId": "00000000-0000-4000-8000-000000000003"
      }
    },
    {
      "type": "AccessPoint",
      "id": <span style="color:#1565C0;">"00000000-0000-4000-8000-000000000101"</span>,
      "attributes": {
        "name": <span style="color:#1565C0;">"Banqup (Unifiedpost)"</span>,
        "status": "CONNECTED",
        "connectionId": "00000000-0000-4000-8000-000000000005"
      }
    }
  ]
}</code></pre>
<!-- confluence-html-macro:end -->

Keep each returned `connectionId`. A disconnected entry has `DISCONNECTED` and `connectionId: null`. Reuse matching setup; only a missing connection needs API-03. More saved connections do not activate routing or enable Private A to Private B switching. REF-CONNECTIONS.

<span style="color:#1565C0;">Confirm Spain dataset mapping and concurrent provider support. Public entries depend on the GAP-02 decision. No new array key is needed for several connections. GAP-01/02/06.</span>

<a id="api-03"></a>

### 1.3 API-03 — Connect

FR-03 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

| Existing POST capability | Supported input / limit |
|---|---|
| Register initial addresses | One or more entries in `accessPointAddresses[]` for the selected connection. |
| Use supported address formats | Current, legal, or both formats in one request, as shown in the supplied France examples. |
| Set address dates | Optional `effectiveDate` and `endDate` per address. |
| Set address usage | Optional `usage`, at most one explicit value; omitted/null permits all supported operations. |
| Supply company/requester details | Existing company fields and `user` audit context. |

POST creates one dataset/access-point connection with these initial addresses. Add addresses later through [API-05 PUT](#api-05).

**Request — Sage 200 creates missing Sage setup for its customer's existing B2B Router account:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>POST https://api-sbx.e-invoicing.sage.com/connectors/{accessPointId}/datasets/{datasetId}/connect
Authorization: Bearer {sageIdM2MToken}
Idempotency-Key: {idempotencyKey}
traceparent: {traceparent}
tracestate: {tracestate}
Content-Type: application/vnd.api+json

{
  "data": {
    "type": "AccessPointConnection",
    "attributes": {
      "companyName": "Example Spain SL",
      "companyAddress": "Calle de Ejemplo 1",
      "companyPostalCode": "28000",
      "companyCountryCode": <span style="color:#1565C0;">"ES"</span>,
      "user": {
        "firstName": "Casey",
        "lastName": "Example",
        "jobTitle": null,
        "emailAddress": "user@example.invalid",
        "clientIPAddress": "192.0.2.10"
      },
      "accessPointAddresses": [
        {
          "accessPointAddressType": <span style="color:#1565C0;">"es.nif"</span>,
          "accessPointAddress": <span style="color:#1565C0;">"NIF_TBD"</span>,
          "usage": null
        }
      ]
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

**Response — `201 Created`:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "AccessPointConnection",
    "id": "00000000-0000-4000-8000-000000000003",
    "attributes": {
      "accessPointAddresses": [
        {
          "accessPointAddressType": <span style="color:#1565C0;">"es.nif"</span>,
          "accessPointAddress": <span style="color:#1565C0;">"NIF_TBD"</span>,
          "status": "IN_PROGRESS",
          "errorCode": null
        }
      ]
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

Save `data.id` as `connectionId`; setup is still in progress. Certificates use the separate calls in §2.

<span style="color:#1565C0;">Confirm ES/es.nif values, NIF/NIE formats, multi-address grouping, date/usage rules, provider binding and safe replay. France current/legal formats do not define Spain address formats. GAP-02/04/06.</span>

<a id="api-04"></a>

### 1.4 API-04 — Read connection progress

FR-04 · [039 recovery](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#25-uncertainty-and-recovery).

**Request — no body:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>GET https://api-sbx.e-invoicing.sage.com/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/
Authorization: Bearer {sageIdM2MToken}
traceparent: {traceparent}
tracestate: {tracestate}</code></pre>
<!-- confluence-html-macro:end -->

**Response — `200 OK`:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "AccessPointConnection",
    "id": "00000000-0000-4000-8000-000000000003",
    "attributes": {
      "accessPointAddresses": [
        {
          "accessPointAddressType": <span style="color:#1565C0;">"es.nif"</span>,
          "accessPointAddress": <span style="color:#1565C0;">"NIF_TBD"</span>,
          "status": "CONNECTED",
          "errorCode": null
        }
      ]
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

Read the original connection after uncertainty. An address in `RETRYING` stays under observation; do not reconnect it. An empty/failed read does not prove no earlier effect. INT-AP05/06; GAP-04.

<span style="color:#1565C0;">Confirm status/error mappings. CONNECTED alone does not prove certificate suitability, public access or route activation. GAP-05/06.</span>

<a id="api-05"></a>

### 1.5 API-05 — Update supported setup

FR-05 · [039 supported change](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#24-supported-change).

| Existing PUT capability | Supported input / limit |
|---|---|
| Add an address | `accessPointAddresses[].action: "add"` under the existing connection. |
| Change an existing address's dates | `action: "update"`; only `effectiveDate` and/or `endDate`. |
| Add and update together | Both actions in one array; see source example `mixed-actions-success`. |
| Restrict operations on a new address | Optional `usage` applies only to `add`; omitted/null permits all supported operations. |
| Edit company/requester details | Existing company name/address/postcode/country and `user` fields in `UpdateAccessPointConnectionRequest`. |

The current contract groups addresses by base SIREN. <span style="color:#1565C0;">Confirm Spain grouping and provider effects; no SIREN hierarchy is assumed for NIF. GAP-02/06/07/08.</span>

**Request — add an address to this connection:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>PUT https://api-sbx.e-invoicing.sage.com/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/
Authorization: Bearer {sageIdM2MToken}
traceparent: {traceparent}
tracestate: {tracestate}
Content-Type: application/vnd.api+json

{
  "data": {
    "type": "AccessPointConnection",
    "attributes": {
      "accessPointAddresses": [
        {
          "action": "add",
          "accessPointAddressType": <span style="color:#1565C0;">"es.nif"</span>,
          "accessPointAddress": <span style="color:#1565C0;">"NIF_TBD"</span>,
          "effectiveDate": "2026/11/01"
        }
      ]
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

**Response — `200 OK`:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "AccessPointConnection",
    "id": "00000000-0000-4000-8000-000000000003",
    "attributes": {
      "accessPointAddresses": [
        {
          "action": "add",
          "accessPointAddressType": <span style="color:#1565C0;">"es.nif"</span>,
          "accessPointAddress": <span style="color:#1565C0;">"NIF_TBD"</span>,
          "status": "IN_PROGRESS",
          "errorCode": null
        }
      ]
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

Keep the same `connectionId`; use API-04 for the address result. Routing changes require separate authorisation and a confirmed [Routing interface in 039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#24-supported-change).

## 2 Certificate management — proposed call to confirm

INT-CERT01/02 document existing ES AFL credential handling; B2B reuse remains GAP-03/06. Keep Tax credential references separate from E-Invoice connection references. Confirm `dataset_id` mapping, Tax base URL, header requiredness, authorisation format and request media type; the source lists headers without resolving these points.

### 2.1 Existing certificate provisioning

Use only for a missing required credential. **Request:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>POST {connectionsServiceBaseUrl}/datasets/{dataset_id}/connections
Authorization: {authorisationValue}
x-api-key: {apiKey}
traceparent: {traceparent}
tracestate: {tracestate}

{
  "data": {
    "type": "Connection",
    "attributes": {
      "providerId": <span style="color:#1565C0;">"B2B_CERTIFICATE_PROVIDER_TBD"</span>,
      "label": "Example business certificate",
      "credentials": {
        "type": "certificate",
        "expiresBy": "&lt;certificate expiry&gt;",
        "credentialsObject": {
          "type": "personal-certificate",
          "certificatesecret": "&lt;certificate contents&gt;",
          "password": "&lt;certificate password&gt;"
        }
      }
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

**Response extract — success code unspecified:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "Connection",
    "id": "00000000-0000-4000-8000-000000000006",
    "attributes": {
      "providerId": <span style="color:#1565C0;">"B2B_CERTIFICATE_PROVIDER_TBD"</span>,
      "label": "Example business certificate"
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

Keep `data.id` as the credential reference. `providerId` identifies the Tax credential provider, separately from a platform/account. <span style="color:#1565C0;">Confirm the B2B provider; no ID is supplied.</span> Certificate/password fields belong here; the E-Invoice connect body has no certificate field.

Source conflicts: example nesting is `credentials.credentialsObject`, field-table nesting is `certificate.credentialsObject`. `expiresBy` is declared expiry, not validation. The returned `data.links.credentialsPatchEndpoint.href` has no confirmed update method. INT-CERT01.

### 2.2 Existing internal encryption

Internal Tax/AFL flow. **Request:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>POST {connectionsServiceBaseUrl}/datasets/{dataset_id}/compliance/es-anti-fraud-legislation/encryptions
Authorization: {authorisationValue}
Idempotency-Key: {idempotencyKey}
traceparent: {traceparent}
tracestate: {tracestate}

{
  "data": {
    "type": "encrypted-certificate",
    "attributes": {
      "secret": "&lt;secret prepared by the approved credential flow&gt;"
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

**Response extract:**

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "encrypted-certificate",
    "id": "00000000-0000-4000-8000-000000000007",
    "attributes": {
      "encryptedSecret": "&lt;encrypted value&gt;"
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

The `secret` serialisation is unconfirmed. This is not an additional ERP call. INT-CERT01.

### 2.3 Credential selection and the additional onboarding result

ES AFL selects customer certificates or the Sage seal with <span style="color:#666666;"><code>Connection-Id: &lt;credential-connection-id&gt;</code></span>. INT-CERT02.

| Case | Reuse / Spain check |
|---|---|
| Suitable certificate already held | Reuse its reference after confirming client/environment/action mapping. Unavailable lookup stays pending. |
| Missing or unsuitable certificate | Provision missing material or correct expired/revoked/unsuitable material; do not request another upload for a failed lookup. |
| Sage seal | Confirm dedicated provider/type, purpose-specific agreement and B2B permission. Customers do not upload Sage's seal. |

<span style="color:#1565C0;">Confirm whether the product supplies the credential reference or the backend resolves it. Connection-Id is not a confirmed new E-Invoice API header. Readiness must cover selected reference/material version, validated expiry, trust/revocation, action suitability, reason, next action/owner and next check. No Tax response schema is supplied.</span> [SPEC001 CERT-04/05](../../SPEC-SEI-001-certificate-management-solution-specification.md#6-cert-0405-validate-trust-and-calculate-scoped-readiness).

<span style="color:#1565C0;">SPEC001 proposes NOT_REQUIRED, READY, EXPIRING, ACTION_REQUIRED, BLOCKED, UNDETERMINED; these are not confirmed Tax wire values.</span> NIF validity and business permission remain separate. The public WSDL uses certificate-authenticated HTTPS, not a certificate business-field. SPFE-S03/S16; SPEC001 G1/G9/G10.

## 3 Other additional calls to confirm

[039 §2.7](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#27-who-sends-what-and-what-comes-back) owns responsibilities. <span style="color:#1565C0;">Methods, URLs and new fields below remain unconfirmed unless named as documented.</span>

| Proposed interaction | Needed request → result | Owner / gap |
|---|---|---|
| <span style="color:#1565C0;">NIF / permission</span> | Business, caller, action → separate identity/authority findings. | Identity/Product; GAP-03/06 |
| <span style="color:#1565C0;">Public access</span> | Function, environment, credential use → access finding. No enrolment/test-invoice call established. | Public Integration; GAP-06 |
| <span style="color:#1565C0;">B2B Router account mapping</span> | Documented candidate <span style="color:#666666;"><code>GET /accounts</code></span> → visible accounts. Confirm authorised business/dataset binding, credentials and version. REF-B2BR. | Integration; GAP-02/05/06 |
| <span style="color:#1565C0;">ZeroComa setup</span> | Vendor must supply service, account fields, credentials and response. No verified onboarding payload available. REF-ZEROCOMA. | Provider Engineering; GAP-02/05/06 |
| <span style="color:#1565C0;">Allowed route change</span> | Current/target connection, start, permission → effective result or pending action/owner; preserve earlier access. | Routing; GAP-06/08 |

Keep Spain rules isolated. Actual build coverage and the supported configuration/code/contract changes remain with [039's GAP owners](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#4-open-engineering-decisions).

## REF Source references

FR-01–05 are supplied OpenAPI 3.1.0 contracts declaring API version `1.0.0`, reviewed 26 October 2026. Grey structures follow those schemas; blue values/information require confirmation. Requests show the method, sandbox URL, path inputs, headers and body where applicable. Full field constraints, audit fields and error schemas remain in the sources.

| ID | Source / exact locator | Supports / limit |
|---|---|---|
| FR-01 | [Discovery](<../../../context/FR API/Onboarding/get-accesspoints.md>), `Get-AccessPoints`; `servers`, `securitySchemes.m2m`, operation parameters. | API-01 request/catalogue; declared `datasetId` does not appear in the URL and needs correction. |
| FR-02 | [Dataset listing](<../../../context/FR API/Onboarding/get-dataset-accesspoints.md>), `Get-Dataset-AccessPoints`; `servers`, `securitySchemes.m2m`, operation parameters. | API-02 path, authentication/tracing headers and nullable connection ID. |
| FR-03 | [Connect](<../../../context/FR API/Onboarding/new-accesspoint-connection.md>), `New-AccessPoint-Connection`; `AccessPointConnectionRequest.accessPointAddresses`/`user`, response, parameters/security; examples `add-address`, `add-legal-format-address`, `add-both-formats-address`. | Initial address array, current/legal formats, dates/usage, company/requester context and required `Idempotency-Key`; no Spain enum or certificate field. |
| FR-04 | [Detail](<../../../context/FR API/Onboarding/get-accesspoint-connection.md>), `Get-AccessPoint-Connection`; parameters and security. | API-04 request and address results, not complete readiness. The guide's extra idempotency header remains a source conflict. |
| FR-05 | [Update](<../../../context/FR API/Onboarding/put-accesspoint-connection.md>), 1.0.0, `Put-AccessPoint-Connection`; `UpdateAccessPointConnectionRequest/Response.accessPointAddresses`, `action`/`usage` descriptions and request example `mixed-actions-success`. | API-05 adds addresses or updates existing dates; mixed add/update requests supported. Current base-SIREN grouping needs Spain rules. No idempotency header declared or approved route-change contract. |
| INT-AP01/06 | [Access-point guide extract](<../../../context/FR API/Onboarding/access-point-guides-evidence-extract.md>), received 22 October 2026, **Connect and channel selection / Catalogue, address mapping and environments**; revision unverified. | One connection per dataset/access point, several addresses and per-service references. Spain implementation coverage remains unknown. |
| INT-CERT01 | [Connections Service API extract](<../../../context/Tax API/Certificates/connections-service-certificate-guide-extract.md>), Confluence 467063094 v4, read 26 October 2026; **Certificate upload / Internal - Encrypt**, requests, responses and field tables. | Existing provisioning/encryption examples; nesting and syntax issues remain owner questions. No B2B provider/readiness contract. |
| INT-CERT02 | [Certificate-management extract](<../../../context/Tax API/Certificates/sage-certificate-management-guide-extract.md>), Confluence 759615024 v6, read 26 October 2026; **Current solution / Proposed solution / Final Decision Summary**. | Exact ES AFL `Connection-Id`, customer/seal selection, custody and agreement gate. Page remains UNDER REVIEW; not proof of B2B deployment. |
| REF-CERT | [SPEC001](../../SPEC-SEI-001-certificate-management-solution-specification.md), draft, 20 October 2026, CERT-04/05 and G1/G9/G10. | Proposed certificate validation/readiness meanings; no confirmed Tax wire response. |
| SPFE-S03/S16 | [Original catalogue](<../../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026, §4.3 p.8; [SendInvoice WSDL](<../../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), snapshot 13 October 2026, `SendInvoiceCertPort` / `SendInvoiceSealPort`. | Certificate-authenticated HTTPS and separate PRE access ports; no certificate property or onboarding command. |
| REF-INTEGRATION | User direction, 26–27 October 2026; [038 product precondition](../SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules) and [SXS definition](../../../context/GLO-SEI-001-e-invoicing-terminology.md#services-connections-and-routing). | Confirmed product list and requested SXS/Tax integration precondition; deployment/interface coverage still needs evidence. |
| REF-PROVIDERS | [PRD213](../../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md#phase-2-prd-set), draft, 11 September 2026, Phase 2 PRD set/provider PRDs 216–220; [040 Confluence review](https://confluence.sage.com/pages/viewpage.action?pageId=938804297), v7, read 27 October 2026, API-01 catalogue. | Five portfolio candidates; the page review adds Sovos. Candidate names and synthetic IDs do not establish Spain services, contracts or implemented integrations. |
| REF-CONNECTIONS | [PRD214](../../../prds/PRD-SEI-214-connections-registration-routing-structured-review.md#connections-registration-and-capability), draft, 7 October 2026, FR1–5/7–9; [SPEC014](../../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md#1-model-outcomes-and-invariants), draft, 20 October 2026, invariants 3–6. | Proposed concurrent public/private connections and one route per scope. Dataset binding, public access-point representation and Spain implementation remain open. |
| REF-B2BR | [B2B Router List accounts](https://developer.b2brouter.net/reference/get-accounts), read 26 October 2026, `GET /accounts`; [SPEC017](../../SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md#3-provider-operation-binding), draft, 20 October 2026, §3 **List account scope** and B2BR-Q01. | Existing provider account-list operation; proposed use to check account mapping. Contract/version selection, account mapping and Sage build remain unqualified. No response schema inferred here. |
| REF-ZEROCOMA | [PRD220](../../../prds/PRD-SEI-220-zerocoma-integration-structured-review.md#evidence-and-research-findings), draft, 11 September 2026, **Evidence and research findings**, E1/E2 and **Connection and onboarding**, FR15–17. | Public integration claim only; target private-platform product and onboarding contract remain open. No wire fields inferred. |
| REF-SPAIN-PROPOSAL | [039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md), draft, 27 October 2026, §§2.1–2.7 and GAP-01–08. | Sequence and ownership baseline for blue proposals; no deployment approval. |
