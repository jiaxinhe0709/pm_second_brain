"""Build the API-by-API grey/blue review; no network calls or publication."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'specs/onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md'
GREY = '#666666'
BLUE = '#1565C0'
RED = '#B42318'
AP_ID = '00000000-0000-4000-8000-000000000002'
CONNECTION_ID = '00000000-0000-4000-8000-000000000003'
SPAIN_TYPE = 'es.nif'
NIF = 'NIF_TBD'
PRIVATE_PROVIDERS = [
    ('B2B Router', AP_ID),
    ('Banqup (Unifiedpost)', '00000000-0000-4000-8000-000000000101'),
    ('EDICOM', '00000000-0000-4000-8000-000000000102'),
    ('SERES (Docaposte)', '00000000-0000-4000-8000-000000000103'),
    ('ZeroComa', '00000000-0000-4000-8000-000000000104'),
]

def blue(value):
    return f'<span style="color:{BLUE};">{value}</span>'

def red(value):
    return f'<span style="color:{RED};">{value}</span>'

def coloured_json(value, changed=()):
    code = html.escape(json.dumps(value, indent=2, ensure_ascii=False), quote=False)
    for item in changed:
        token = html.escape(json.dumps(item, ensure_ascii=False), quote=False)
        code = code.replace(token, blue(token))
    return code

def code_block(code):
    return ('<!-- confluence-html-macro:start -->\n'
            f'<pre style="color:{GREY};background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{code}</code></pre>\n'
            '<!-- confluence-html-macro:end -->')

def payload(value, changed=()):
    return code_block(coloured_json(value, changed))

def request(method, path, body=None, changed=(), *, tax=False, extra_headers=()):
    base = 'https://api-int.network-eng.sage.com' if tax else 'https://api-sbx.e-invoicing.sage.com'
    auth = 'Bearer {domainServicesToken}' if tax else 'Bearer {sageIdM2MToken}'
    lines = [f'{method} {base}{path}', f'Authorization: {auth}']
    if tax:
        lines.extend(['x-api-key: {productEnvironmentApiKey}', 'Idempotency-Key: {idempotencyKey}'])
    lines.extend(extra_headers)
    lines.extend(['traceparent: {traceparent}', 'tracestate: {tracestate}'])
    if body is not None and not tax:
        lines.append('Content-Type: application/vnd.api+json')
    code = html.escape('\n'.join(lines), quote=False)
    if body is not None:
        code += '\n\n' + coloured_json(body, changed)
    return code_block(code)

def call(value):
    return f'<span style="color:{GREY};"><code>{html.escape(value)}</code></span>'

def connection(status, action=None):
    address = {'accessPointAddressType': SPAIN_TYPE, 'accessPointAddress': NIF,
               'status': status, 'errorCode': None}
    if action:
        address = {'action': action, **address}
    return {'data': {'type': 'AccessPointConnection', 'id': CONNECTION_ID,
                     'attributes': {'accessPointAddresses': [address]}}}

discovery = {'data': [{'type': 'AccessPoint', 'id': identifier,
                       'attributes': {'name': name}}
                      for name, identifier in PRIVATE_PROVIDERS[:1]]}
listing = {'data': [{'type': 'AccessPoint', 'id': AP_ID,
                     'attributes': {'name': 'B2B Router', 'status': 'CONNECTED',
                                    'connectionId': CONNECTION_ID}},
                    {'type': 'AccessPoint', 'id': PRIVATE_PROVIDERS[1][1],
                     'attributes': {'name': 'Banqup (Unifiedpost)', 'status': 'CONNECTED',
                                    'connectionId': '00000000-0000-4000-8000-000000000005'}}]}
create = {'data': {'type': 'AccessPointConnection', 'attributes': {
    'companyName': 'Example Spain SL', 'companyAddress': 'Calle de Ejemplo 1',
    'companyPostalCode': '28000', 'companyCountryCode': 'ES',
    'user': {'firstName': 'Casey', 'lastName': 'Example', 'jobTitle': None,
             'emailAddress': 'user@example.invalid', 'clientIPAddress': '192.0.2.10'},
    'accessPointAddresses': [{'accessPointAddressType': SPAIN_TYPE,
                              'accessPointAddress': NIF, 'usage': None}]}}}
add_address = {'data': {'type': 'AccessPointConnection', 'attributes': {
    'accessPointAddresses': [{'action': 'add', 'accessPointAddressType': SPAIN_TYPE,
                              'accessPointAddress': NIF, 'effectiveDate': '2026/11/01'}]}}}
CERT_PROVIDER = '00000000-0000-4000-8000-000000000008'
provider_result = {'meta': {'totalPages': 1}, 'data': [{'type': 'Provider',
    'id': CERT_PROVIDER, 'attributes': {'providerCode': 'es-aeat',
    'credentialType': 'certificate', 'categories': ['es-aeat-afl']}}]}
credential_create = {'data': {'type': 'Connection', 'attributes': {
    'providerId': CERT_PROVIDER, 'label': 'AEAT AFL Certificate',
    'credentials': {'type': 'certificate', 'expiresBy': '<certificate expiry>',
                    'credentialsObject': {'type': 'personal-certificate',
                        'certificatesecret': '<certificate contents>',
                        'password': '<certificate password>'}}}}}
credential_result = {'data': {'type': 'Connection',
    'id': '00000000-0000-4000-8000-000000000006',
    'attributes': {'providerId': CERT_PROVIDER, 'label': 'AEAT AFL Certificate'}}}

old = DOC.read_text()
front = old.split('---', 2)[1]
if '  - SPEC-SEI-001\n' not in front:
    front = front.replace('related:\n', 'related:\n  - SPEC-SEI-001\n')
body = f'''# E-Invoice Onboarding API Reuse and Spain Changes

Products: **Sage 50, Sage 200, Sage Active and Sage X3** are the ERPs; **Despachos** serves accountants. Each product needs the [SXS and Tax/Connections integrations in 038](../SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules). Resolve the client's dataset and reuse required credentials before onboarding; an unavailable lookup stays pending.

[039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md) owns the sequences, product impact and GAP decisions. This page shows request/response examples and Spain changes.

**Phase coverage:** **1 — SPFE public solution; 2 — external private providers; 3 — Sage private-platform offering.** Labels show analysis coverage, not delivery approval or confirmed API availability. REF-PHASE.

<span style="color:{GREY};"><strong>Grey:</strong> existing calls/fields.</span> · <span style="color:{BLUE};"><strong>Blue:</strong> proposed Spain values or additional work.</span> · <span style="color:{RED};"><strong>Red:</strong> open questions, uncertainty or assumptions requiring validation.</span> Examples use synthetic data and documented sandbox URLs. Replace IDs with service-returned values. Responses are extracts. Blue values, including `es.nif`, require API-owner confirmation; they do not prove provider availability or introduce new keys.

<a id="1-existing-calls-to-reuse"></a>

## 1 Existing calls to reuse — Phases 1–3

**Existing contract:** calls use dataset, access-point and connection IDs; addresses belong to a connection. The supplied guide describes one connection per dataset/access-point pair. This does not select how Spain maps platforms to those resources. FR-02/03/05; INT-AP01/06.

| Customer needs | Existing call | Phase |
|---|---|---|
| Another supported platform, with no saved setup | If it maps to a separate access point, API-01/02 find the service and **API-03 POST** creates its dataset connection. Other mappings need GAP-02 assessment. | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| Another address within an existing platform connection | **API-05 PUT**, `action: "add"`, using that connection's existing IDs. | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |

<span style="color:#B42318;">**Open decision — Architecture / Engineering:** confirm the Spain dataset/access-point/connection/platform relationship, including whether platforms use separate access points, several connections under one access point, or another supported mapping. No option is selected. SPFE representation and use of these calls in Phase 1 are part of [039 GAP-02](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#4-open-engineering-decisions). No public enrolment API is established.</span>

| Path ID — required UUID wherever present | Where it comes from |
|---|---|
| `datasetId` | Company's SXS mapping; confirm the E-Invoice binding and accountant/client scope. |
| `accessPointId` | Service ID from API-01. |
| `connectionId` | API-02 or API-03; retain the returned resource associations. Spain relationships remain GAP-02. |

All five E-Invoice templates use required Bearer M2M authentication and optional `traceparent`/`tracestate`. POST/PUT bodies use `application/vnd.api+json`; API-03 also requires `Idempotency-Key`. FR-01–05.

<a id="api-01"></a>

<a id="11-api-01-discover-services"></a>

### 1.1 API-01 — Discover services — Phases 2–3; <span style="color:#B42318;">SPFE use TBD</span>

FR-01 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

**Request — no body or path parameters:**

{request('GET', '/accesspoints')}

**Response — `200 OK`, one proposed entry:**

{payload(discovery, PRIVATE_PROVIDERS[0])}

Portfolio candidates: B2B Router, Banqup (Unifiedpost), EDICOM, SERES (Docaposte) and ZeroComa. **New candidate: Sovos.** REF-PROVIDERS. {red('Confirm target Spain services, contracts and IDs/environments before offering them; this catalogue entry is illustrative. GAP-02/06/08.')}

<span style="color:#B42318;">Source conflict: FR-01 declares a path `datasetId` absent from its URL.</span>

<a id="api-02"></a>

<a id="12-api-02-find-existing-connections"></a>

### 1.2 API-02 — Find existing connections — Phases 2–3; <span style="color:#B42318;">SPFE use TBD</span>

FR-02 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

**Request — no body:**

{request('GET', '/datasets/{datasetId}/accesspoints')}

{red('BA working hypothesis: one company dataset can connect to B2B Router and Banqup, with a separate access point and E-Invoice connection ID for each platform. This is an unvalidated BA proposal, not an observed Spain API result or an agreed design. Architecture and Engineering must validate or replace this mapping against the supported build and contract, then decide when adding a platform requires a new connection. GAP-02.')}

**Illustrative response using the existing `200 OK` structure — BA hypothesis, not a validated Spain response:**

{payload(listing, [value for provider in PRIVATE_PROVIDERS[:2] for value in provider])}

Keep each returned `connectionId`. A disconnected entry has `DISCONNECTED` and `connectionId: null`. Under this hypothesis, API-03 creates a missing dataset/access-point connection; the actual Spain call depends on GAP-02. More saved connections do not activate routing or enable Private A to Private B switching. REF-CONNECTIONS.

{red('Confirm Spain dataset mapping and concurrent provider support. Public entries depend on the GAP-02 decision. The existing array is a reuse candidate, not proof that the selected Spain model needs no contract change. GAP-01/02/06.')}

<a id="api-03"></a>

<a id="13-api-03-connect"></a>

### 1.3 API-03 — Connect — Phases 2–3; <span style="color:#B42318;">SPFE use TBD</span>

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

{request('POST', '/connectors/{accessPointId}/datasets/{datasetId}/connect', create, ['ES', SPAIN_TYPE, NIF], extra_headers=['Idempotency-Key: {idempotencyKey}'])}

**Response — `201 Created`:**

{payload(connection('IN_PROGRESS'), [SPAIN_TYPE, NIF])}

Save `data.id` as `connectionId`; setup is still in progress. Certificates use the separate calls in §2.

{red('Confirm ES/es.nif values, NIF/NIE formats, multi-address grouping, date/usage rules, provider binding and safe replay. France current/legal formats do not define Spain address formats. GAP-02/04/06.')}

<a id="api-04"></a>

<a id="14-api-04-read-connection-progress"></a>

### 1.4 API-04 — Read connection progress — Phases 2–3; <span style="color:#B42318;">SPFE use TBD</span>

FR-04 · [039 recovery](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#25-uncertainty-and-recovery).

**Request — no body:**

{request('GET', '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/')}

**Response — `200 OK`:**

{payload(connection('CONNECTED'), [SPAIN_TYPE, NIF])}

Read the original connection after uncertainty. An address in `RETRYING` stays under observation; do not reconnect it. An empty/failed read does not prove no earlier effect. INT-AP05/06; GAP-04.

{red('Confirm status/error mappings. CONNECTED alone does not prove certificate suitability, public access or route activation. GAP-05/06.')}

<a id="api-05"></a>

<a id="15-api-05-update-supported-setup"></a>

### 1.5 API-05 — Update supported setup — Phases 2–3; <span style="color:#B42318;">SPFE use TBD</span>

FR-05 · [039 supported change](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#24-supported-change).

| Existing PUT capability | Supported input / limit |
|---|---|
| Add an address | `accessPointAddresses[].action: "add"` under the existing connection. |
| Change an existing address's dates | `action: "update"`; only `effectiveDate` and/or `endDate`. |
| Add and update together | Both actions in one array; see source example `mixed-actions-success`. |
| Restrict operations on a new address | Optional `usage` applies only to `add`; omitted/null permits all supported operations. |
| Edit company/requester details | Existing company name/address/postcode/country and `user` fields in `UpdateAccessPointConnectionRequest`. |

The current contract groups addresses by base SIREN. {red('Confirm Spain grouping and provider effects; no SIREN hierarchy is assumed for NIF. GAP-02/06/07/08.')}

**Request — add an address to this connection:**

{request('PUT', '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/', add_address, [SPAIN_TYPE, NIF])}

**Response — `200 OK`:**

{payload(connection('IN_PROGRESS', action='add'), [SPAIN_TYPE, NIF])}

For this existing-connection example, keep `connectionId`; use API-04 for the address result. Routing changes require separate authorisation and a confirmed [Routing interface in 039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#24-supported-change).

<a id="2-certificate-management-proposed-call-to-confirm"></a>

## 2 Certificate management — proposed call to confirm — Phases 1–3, where required

INT-CERT01–03 document existing **ES AFL** credential handling. {red('Qualify B2B reuse, dataset binding and secure provisioning before activation. GAP-03/06; SPEC001 G1/G3/G9/G10/G11.')} No certificate field is added to API-03.

| Reference | Documented purpose |
|---|---|
| E-Invoice API-03 `data.id`; API-02 `connectionId` | Identifies an `AccessPointConnection`. Used by API-04/05. FR-02/03. |
| Tax certificate upload `data.id`; ES AFL `Connection-Id` | Identifies a `Connection` used to select stored credentials. INT-CERT01–03. |

{red('ID relationship unconfirmed: the sources do not establish whether these IDs are shared, mapped or independent. Until the Tax/Connections and E-Invoice API owners confirm the contract, retain each reference with its source and do not substitute one for the other. See 039 GAP-06.')} Different synthetic IDs in these examples do not prove separate ID namespaces.

<a id="21-existing-certificate-provisioning"></a>

### 2.1 Existing certificate provisioning — Phases 1–3, where required

The AEAT guide supplies both calls below. Internal Sandbox uses `https://api-int.network-eng.sage.com`; production uses `https://api.network.sage.com`. Enablement supplies each product/environment's API key. Both calls require Bearer Domain Services authentication, `x-api-key`, `traceparent` and `Idempotency-Key`; `tracestate` is optional. <span style="color:#B42318;">Request media type is not specified.</span> INT-CERT03.

**Find the provider — skip if its correct environment-specific ID is already known. No body:**

{request('GET', '/connections/providers', tax=True)}

**Response extract — `200 OK`:**

{payload(provider_result)}

Select `providerCode: "es-aeat"` and keep its `data[].id` as `providerId`. This catalogue does not list saved customer credentials. {red('The documented category is es-aeat-afl; confirm whether B2B can use this provider. Do not invent a B2B provider ID.')}

**Upload only a confirmed missing required credential — request:**

{request('POST', '/datasets/{datasetId}/connections', credential_create, tax=True)}

**Response extract — `201 Created`:**

{payload(credential_result)}

Keep `data.id` as the credential reference. `201` confirms provisioning, not validated certificate readiness. `expiresBy` is optional declared expiry. The response also supplies `data.links.credentialsPatchEndpoint.href`; <span style="color:#B42318;">it does not define an update method/body.</span> INT-CERT03.

<span style="color:#B42318;">Source conflict: the example uses `credentials.credentialsObject`; the field table uses `certificate.credentialsObject`. Tax/Connections must confirm nesting.</span> {red('Confirm the B2B secure-provisioning path; the AFL certificate/password example does not establish that boundary.')} SPEC001 G3/G11.

<a id="22-existing-internal-encryption"></a>

### 2.2 Existing internal encryption — Phases 1–3, if AFL reuse is qualified

Connections Service invokes AFL encryption internally. This is not an additional ERP call. The [source extract](<../../../context/Tax API/Certificates/connections-service-certificate-guide-extract.md#internal-encryption>) owns its payload; <span style="color:#B42318;">secret serialisation remains unconfirmed.</span> INT-CERT01/02.

<a id="23-credential-selection-and-the-additional-onboarding-result"></a>

### 2.3 Credential selection and the additional onboarding result — Phases 1–3, where required

ES AFL selects customer certificates or the Sage seal with {call('Connection-Id: <credential-connection-id>')}. INT-CERT02. {red('Confirm product-supplied versus backend-resolved selection for B2B; this is not a confirmed E-Invoice API header.')}

| Case | Reuse / Spain check |
|---|---|
| Suitable certificate already held | Reuse its reference after confirming client/environment/action mapping. Failed lookup stays pending; it does not justify another upload. |
| Add another platform that requires a certificate | {red('BA working hypothesis: reuse suitable protected certificate material without another upload. Tax/Connections and the provider integration owners must confirm acceptance and permitted use. Can the existing Tax credential connection ID be reused, or is a new one required? Can several E-Invoice connections use that credential? These remain open under GAP-06; the E-Invoice connection decision belongs to GAP-02.')} |
| Missing or unsuitable certificate | Provision missing material or correct expired/revoked/unsuitable material through the qualified flow. |
| Sage seal | <span style="color:#B42318;">Confirm dedicated provider/type, B2B permission and stored purpose-specific agreement.</span> Customers do not upload Sage's seal. |

The [trusted-service retrieval contract](<../../../context/Tax API/Certificates/connections-service-retrieval-guide-extract.md>) documents GET/`200` for **HMRC access tokens**. Its response exposes credentials; it is not an ERP onboarding call. <span style="color:#B42318;">AEAT certificate shape, B2B permission and safe reference/readiness lookup remain unconfirmed.</span> INT-CERT04.

{blue('Readiness must identify the selected reference/material version, validated expiry, trust/revocation, action suitability and next action/owner.')} {red('No certificate-readiness response schema is supplied.')} [SPEC001 CERT-04/05](../../SPEC-SEI-001-certificate-management-solution-specification.md#6-cert-0405-validate-trust-and-calculate-scoped-readiness) proposes `NOT_REQUIRED`, `READY`, `EXPIRING`, `ACTION_REQUIRED`, `BLOCKED`, `UNDETERMINED`; <span style="color:#B42318;">these are not Tax wire values.</span> NIF validity and business permission remain separate. Public WSDLs use certificate-authenticated HTTPS, not a certificate business-field. SPFE-S03/S16.

<a id="3-other-additional-calls-to-confirm"></a>

## 3 Other additional calls to confirm — Phases 1–3

[039 §2.7](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#27-who-sends-what-and-what-comes-back) owns responsibilities. {red('Methods, URLs and new fields below remain unconfirmed unless named as documented.')}

| Proposed interaction | Needed request → result | Owner / gap | Phase |
|---|---|---|---|
| {blue('NIF / permission')} | Business, caller, action → separate identity/authority findings. | Identity/Product; GAP-03/06 | 1–3 |
| {blue('Public access')} | Function, environment, credential use → access finding. No enrolment/test-invoice call established. | Public Integration; GAP-06 | 1; reused in 2–3 |
| {blue('B2B Router account mapping')} | Documented candidate {call('GET /accounts')} → visible accounts. Confirm authorised business/dataset binding, credentials and version. REF-B2BR. | Integration; GAP-02/05/06 | 2; reused in 3 where qualified |
| {blue('ZeroComa setup')} | <span style="color:#B42318;">Vendor must supply service, account fields, credentials and response. No verified onboarding payload available.</span> REF-ZEROCOMA. | Provider Engineering; GAP-02/05/06 | 2; reused in 3 where qualified |
| {blue('Allowed route change')} | Current/target connection, start, permission → effective result or pending action/owner; preserve earlier access. | Routing; GAP-06/08 | 2–3; enabled changes only |

Keep Spain rules isolated. Actual build coverage and the supported configuration/code/contract changes remain with [039's GAP owners](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#4-open-engineering-decisions).

<a id="ref-source-references"></a>

## REF Source references — Phases 1–3

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
| INT-CERT03 | [AEAT upload extract](<../../../context/Tax API/Certificates/aeat-certificate-upload-guide-extract.md>), internal guide received 27 October 2026; revision/URL not supplied. **Environments / Obtain provider ID / Upload certificate**, headers, fields and responses. | GET provider catalogue, ES AFL provider code/category and POST upload, URLs, required headers, `200`/`201`. Nesting conflict remains; no B2B acceptance or readiness contract. |
| INT-CERT04 | [Trusted retrieval extract](<../../../context/Tax API/Certificates/connections-service-retrieval-guide-extract.md>), Confluence 484738408 v14, read 27 October 2026; **Request method / URL / headers / response**. | Internal GET/`200` for HMRC tokens. Not evidence of AEAT certificate shape, validated expiry or product permission. |
| REF-PHASE | [PRD213](<../../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md>), Phase 2 scope; [PRD210](<../../../prds/PRD-SEI-210-sage-private-platform-reuse-and-operator-expansion.md>), Phase 3 document map / phase comparison; [PRD221](<../../../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md>), Phase and outcome; repository drafts. User direction, 28 October 2026. | Phase labels describe analysis coverage: SPFE, external providers, then Sage private-platform offering. They do not approve delivery, implementation or Private A to Private B switching. |
| REF-CERT | [SPEC001](../../SPEC-SEI-001-certificate-management-solution-specification.md), draft, 20 October 2026, CERT-04/05 and G1/G9/G10. | Proposed certificate validation/readiness meanings; no confirmed Tax wire response. |
| SPFE-S03/S16 | [Original catalogue](<../../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026, §4.3 p.8; [SendInvoice WSDL](<../../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), snapshot 13 October 2026, `SendInvoiceCertPort` / `SendInvoiceSealPort`. | Certificate-authenticated HTTPS and separate PRE access ports; no certificate property or onboarding command. |
| REF-INTEGRATION | User direction, 26–27 October 2026; [038 product precondition](../SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules) and [SXS definition](../../../context/GLO-SEI-001-e-invoicing-terminology.md#services-connections-and-routing). | Confirmed product list and requested SXS/Tax integration precondition; deployment/interface coverage still needs evidence. |
| REF-PROVIDERS | [PRD213](../../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md#phase-2-prd-set), draft, 11 September 2026, Phase 2 PRD set/provider PRDs 216–220; [040 Confluence review](https://confluence.sage.com/pages/viewpage.action?pageId=938804297), v7, read 27 October 2026, API-01 catalogue. | Five portfolio candidates; the page review adds Sovos. Candidate names and synthetic IDs do not establish Spain services, contracts or implemented integrations. |
| REF-CONNECTIONS | [PRD214](../../../prds/PRD-SEI-214-connections-registration-routing-structured-review.md#connections-registration-and-capability), draft, 7 October 2026, FR1–5/7–9; [SPEC014](../../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md#1-model-outcomes-and-invariants), draft, 20 October 2026, invariants 3–6. | Proposed concurrent public/private connections and one route per scope. Dataset binding, public access-point representation and Spain implementation remain open. |
| REF-B2BR | [B2B Router List accounts](https://developer.b2brouter.net/reference/get-accounts), read 26 October 2026, `GET /accounts`; [SPEC017](../../SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md#3-provider-operation-binding), draft, 20 October 2026, §3 **List account scope** and B2BR-Q01. | Existing provider account-list operation; proposed use to check account mapping. Contract/version selection, account mapping and Sage build remain unqualified. No response schema inferred here. |
| REF-ZEROCOMA | [PRD220](../../../prds/PRD-SEI-220-zerocoma-integration-structured-review.md#evidence-and-research-findings), draft, 11 September 2026, **Evidence and research findings**, E1/E2 and **Connection and onboarding**, FR15–17. | Public integration claim only; target private-platform product and onboarding contract remain open. No wire fields inferred. |
| REF-SPAIN-PROPOSAL | [039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md), draft, 28 October 2026, §§2.1–2.7 and GAP-01–08. | Sequence and ownership baseline for blue proposals; no deployment approval. |
'''
DOC.write_text('---' + front + '---\n\n' + body)
print(json.dumps({'file': str(DOC.relative_to(ROOT)), 'e_invoice_response_extracts': 5,
                  'e_invoice_request_examples': 5, 'e_invoice_request_body_examples': 2,
                  'certificate_product_request_examples': 2, 'certificate_product_response_extracts': 2,
                  'certificate_management': True,
                  'diagrams': 0, 'published': False}, indent=2))
