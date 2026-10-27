"""Build the API-by-API grey/blue review; no network calls or publication."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'specs/onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md'
GREY = '#666666'
BLUE = '#1565C0'
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
    base = '{connectionsServiceBaseUrl}' if tax else 'https://api-sbx.e-invoicing.sage.com'
    auth = '{authorisationValue}' if tax else 'Bearer {sageIdM2MToken}'
    lines = [f'{method} {base}{path}', f'Authorization: {auth}']
    lines.extend(extra_headers)
    lines.extend(['traceparent: {traceparent}', 'tracestate: {tracestate}'])
    if body is not None and not tax:
        lines.append('Content-Type: application/vnd.api+json')
    code = html.escape('\n'.join(lines), quote=False)
    if body is not None:
        code += '\n\n' + coloured_json(body, changed)
    return code_block(code)

def path_inputs(*names):
    meanings = {
        'datasetId': 'Company dataset resolved through SXS; confirm the E-Invoice binding.',
        'accessPointId': 'Selected service ID returned by API-01.',
        'connectionId': 'Saved connection ID for this dataset/access-point pair, returned by API-02 or API-03.',
    }
    if not names:
        return '**Path parameters:** none for the shown URL.'
    rows = ['| Path parameter | Required / type | Value to supply |', '|---|---|---|']
    rows.extend(f'| `{name}` | Yes / UUID | {meanings[name]} |' for name in names)
    return '\n'.join(rows)

def call(value):
    return f'<span style="color:{GREY};"><code>{html.escape(value)}</code></span>'

def connection(status, update=False):
    address = {'accessPointAddressType': SPAIN_TYPE, 'accessPointAddress': NIF,
               'status': status, 'errorCode': None}
    if update:
        address = {'action': 'update', **address}
    return {'data': {'type': 'AccessPointConnection', 'id': CONNECTION_ID,
                     'attributes': {'accessPointAddresses': [address]}}}

discovery = {'data': [{'type': 'AccessPoint', 'id': identifier,
                       'attributes': {'name': name}}
                      for name, identifier in PRIVATE_PROVIDERS]}
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
update = {'data': {'type': 'AccessPointConnection', 'attributes': {
    'accessPointAddresses': [{'action': 'update', 'accessPointAddressType': SPAIN_TYPE,
                              'accessPointAddress': NIF, 'effectiveDate': '2026/11/01',
                              'endDate': '2027/11/01'}]}}}
CERT_PROVIDER = 'B2B_CERTIFICATE_PROVIDER_TBD'
credential_create = {'data': {'type': 'Connection', 'attributes': {
    'providerId': CERT_PROVIDER, 'label': 'Example business certificate',
    'credentials': {'type': 'certificate', 'expiresBy': '<certificate expiry>',
                    'credentialsObject': {'type': 'personal-certificate',
                        'certificatesecret': '<certificate contents>',
                        'password': '<certificate password>'}}}}}
credential_result = {'data': {'type': 'Connection',
    'id': '00000000-0000-4000-8000-000000000006',
    'attributes': {'providerId': CERT_PROVIDER, 'label': 'Example business certificate'}}}
encryption_request = {'data': {'type': 'encrypted-certificate',
    'attributes': {'secret': '<secret prepared by the approved credential flow>'}}}
encryption_result = {'data': {'type': 'encrypted-certificate',
    'id': '00000000-0000-4000-8000-000000000007',
    'attributes': {'encryptedSecret': '<encrypted value>'}}}

old = DOC.read_text()
front = old.split('---', 2)[1]
if '  - SPEC-SEI-001\n' not in front:
    front = front.replace('related:\n', 'related:\n  - SPEC-SEI-001\n')
body = f'''# E-Invoice Onboarding API Reuse and Spain Changes

Products: **Sage 50, Sage 200, Sage Active and Sage X3** are the ERP products; **Despachos** is the accountant product.

**Product precondition:** each must integrate **SXS** for `datasetId` / `tenantId` management and **Tax certificate management / Connections Service** for credential setup and protected use before enabling e-invoicing. See the [shared rule in 038](../SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules); accountant mappings remain client-specific.

For each company, resolve its SXS dataset first, then reuse/check any required credential. Provision only missing setup; unavailable lookup remains pending. [039 §2.1](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#21-shared-prerequisites) shows the proposed order. The product integrations are not repeated for every customer. SXS and B2B credential lookup contracts remain to confirm.

[039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md) owns the sequences, product impact and GAP decisions. This companion shows API-01–05 request/response examples and certificate calls. Dataset creation, events, approvals and batches remain in 039's linked sources. No diagrams.

<span style="color:{GREY};"><strong>Grey — existing:</strong> reuse the current call, keys and status values.</span> · <span style="color:{BLUE};"><strong>Blue — Spain proposal:</strong> changed country values or additional information/calls to confirm.</span>

Response extracts show selected fields; full schemas are linked. All sample business details and UUIDs are synthetic. Use service-returned IDs in an integration. Blue values are proposals, not approved Spain enums or evidence of a live provider connection. Existing keys with blue values are not new fields.

## 1 Existing calls to reuse

Request templates use the supplied **sandbox** URL; they do not prove Spain availability. Replace placeholders with authorised values. Each template includes the optional tracing headers. FR-01–05, `servers`, `securitySchemes.m2m` and operation parameters.

| Shared request header | Required / value |
|---|---|
| `Authorization` | Required: `Bearer {{sageIdM2MToken}}`, using the supplied Sage ID M2M security scheme. |
| `traceparent`, `tracestate` | Optional tracing values. |
| `Content-Type` — POST/PUT bodies | `application/vnd.api+json`, as declared in the supplied request contracts. |

| Product / example | What happens during onboarding |
|---|---|
| Sage 200 customer already uses B2B Router | SXS supplies the dataset ID. API-02 finds saved Sage setup; API-03 is used only if that setup is missing. Keep the customer's B2B Router account. Confirm its account/credential mapping under GAP-02/06. |
| Despachos acts for a client using ZeroComa | Resolve that client's dataset and permission. Provider Engineering must confirm the contracted ZeroComa service and onboarding API before setup can proceed. Do not treat the catalogue example as an available integration. REF-ZEROCOMA. |
| Sage 50 customer selects the public platform | Resolve saved SXS/Tax setup, check NIF, permission and required certificate readiness. No public enrolment API is established; do not assume API-03 performs one. See [039 public readiness](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#22-public-readiness). |

<a id="api-01"></a>

### 1.1 API-01 — Discover services

{call('GET /accesspoints')} — FR-01 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

{path_inputs()}

**Request — no body:**

{request('GET', '/accesspoints')}

**Proposed private-provider catalogue — existing `200 OK` response shape:**

{payload(discovery, [value for provider in PRIVATE_PROVIDERS for value in provider])}

The five provider names come from the Phase 2 portfolio, not an existing Spain API response. REF-PROVIDERS. This example assumes one service entry per provider; Engineering must confirm the contracted services and environments. Public readiness is separate; no public catalogue entry is established.

{blue('Spain: configure only qualified service entries. API/Integration must supply actual service IDs and prove environment support before offering a provider. GAP-02/08.')}

Source issue: FR-01 declares a path `datasetId` absent from `/accesspoints`; the API owner must resolve it.

<a id="api-02"></a>

### 1.2 API-02 — Find existing connections

{call('GET /datasets/{datasetId}/accesspoints')} — FR-02 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

{path_inputs('datasetId')}

**Request — no body:**

{request('GET', '/datasets/{datasetId}/accesspoints')}

**Proposed example: two saved private connections under one dataset — existing `200 OK` response shape:**

{payload(listing, [value for provider in PRIVATE_PROVIDERS[:2] for value in provider])}

One company's dataset can have several platform connections. Reuse that dataset when adding a supported platform. The array can represent several access points. Each connected entry has its own `connectionId`; an unconnected entry can return `DISCONNECTED` with `connectionId: null`. Retain IDs by dataset/access-point pair, not one connection ID for the whole dataset. FR-02; INT-AP01/06; REF-CONNECTIONS.

These are synthetic saved-connection examples, not evidence that both providers are available. For Sage 200's matching B2B Router connection, skip API-03. If that connection is missing, use the alternative below. An additional saved connection does not activate it or enable Private A to Private B switching.

| Same dataset: proposed Spain use | Representation / qualification needed |
|---|---|
| Public setup plus B2B Router | Retain qualified public access while preparing/using the private connection. Engineering must confirm whether public setup appears as an access point; no public catalogue ID is invented. |
| More than one saved private connection | Use a distinct connection ID per access point. Confirm the permitted provider combination; readiness/credential checks remain separate and each route scope selects one eligible connection. |

{blue('Spain: confirm business/client mapping, dataset/access-point cardinality, supported public/private combinations and public representation. No new array or response key is needed to represent multiplicity. Do not assume one dataset per NIF. GAP-01/02/06; owners in 039 §4.')} REF-CONNECTIONS.

<a id="api-03"></a>

### 1.3 API-03 — Connect

{call('POST /connectors/{accessPointId}/datasets/{datasetId}/connect')} — FR-03 · [039 private setup](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#23-private-setup).

**Alternative: Sage setup is missing for the existing B2B Router customer.**

{path_inputs('accessPointId', 'datasetId')}

**Additional required header:** `Idempotency-Key: {{idempotencyKey}}` — FR-03. Qualify its replay guarantees under GAP-04.

**Request with body for review:**

{request('POST', '/connectors/{accessPointId}/datasets/{datasetId}/connect', create, ['ES', SPAIN_TYPE, NIF], extra_headers=['Idempotency-Key: {idempotencyKey}'])}

{blue('Spain proposal: es.nif identifies the business tax-ID scheme in these examples. The API owner must confirm the enum and supported NIF/NIE formats; no Spain enum is defined in the supplied contracts. Confirm the country value, provider account binding and safe repeats. Other company/requester fields remain reuse candidates. API/Spain Product/Integration — GAP-02/04/06.')}

**Response extract — `201 Created`:**

{payload(connection('IN_PROGRESS'), [SPAIN_TYPE, NIF])}

Keep `data.id` as `connectionId`. `201` does not mean setup is complete. Certificate management is the separate call/result in §2; the existing connect contract has no certificate field.

<a id="api-04"></a>

### 1.4 API-04 — Read connection progress

{call('GET /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/')} — FR-04 · [039 recovery](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#25-uncertainty-and-recovery).

{path_inputs('accessPointId', 'datasetId', 'connectionId')}

**Request — no body:**

{request('GET', '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/')}

**Response extract — `200 OK`:**

{payload(connection('CONNECTED'), [SPAIN_TYPE, NIF])}

{blue('Spain: confirm provider status/error mappings. No new response key is confirmed. Public access, certificate readiness and route activation need separate findings; CONNECTED alone does not prove them. API/Integration — GAP-05/06.')}

Follow [039 recovery](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#25-uncertainty-and-recovery): read the original connection before repeating an uncertain request. While an address is `RETRYING`, keep observing it; do not reconnect. A failed/empty read does not prove no effect. GAP-04.

<a id="api-05"></a>

### 1.5 API-05 — Update supported setup

{call('PUT /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/')} — FR-05 · [039 supported change](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#24-supported-change).

{path_inputs('accessPointId', 'datasetId', 'connectionId')}

**Request with body extract — date update:**

{request('PUT', '/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/', update, [SPAIN_TYPE, NIF])}

**Response extract — `200 OK`:**

{payload(connection('IN_PROGRESS', update=True), [SPAIN_TYPE, NIF])}

{blue('Spain: confirm supported address edits, grouping rules and routing effects. An allowed platform change may also require the Routing call in §3; PUT does not establish that contract. API/Integration/Routing — GAP-02/06/07/08.')}

## 2 Certificate management — proposed call to confirm

The [Connections Service source](<../../../context/Tax API/Certificates/connections-service-certificate-guide-extract.md>) now gives specific ES AFL fields. Grey below is documented ES AFL behaviour; blue is the B2B reuse proposal. This credential connection is not assumed equal to the E-Invoice access-point `connectionId`. INT-CERT01.

For both Tax requests, `dataset_id` is the path parameter; confirm its binding to the company's SXS dataset. `{{connectionsServiceBaseUrl}}` is a configuration placeholder. The source lists the shown headers but does not establish requiredness, the `Authorization` value format or request media type; the Tax owner must confirm them. Tracing optionality above applies only to FR-01–05. INT-CERT01, **Certificate upload / Internal - Encrypt**.

### 2.1 Existing certificate provisioning

{call('POST /datasets/{dataset_id}/connections')} — Connections Service. Use only when the required customer credential does not already exist.

**Request example for review — source-listed headers and body:**

{request('POST', '/datasets/{dataset_id}/connections', credential_create, [CERT_PROVIDER], tax=True, extra_headers=['x-api-key: {apiKey}'])}

{blue('Confirm whether an existing credential provider is eligible for B2B or another is needed. The source obtains providerId from /connections/providers, but supplies no B2B ID. Certificate/password fields belong to this credential-provisioning flow, not the E-Invoice connect body.')}

Here `providerId` identifies the **Tax credential provider**. It is not the E-Invoice `accessPointId` or a private-platform account ID. B2B Router API credentials are separate from the Tax-managed certificate.

**Response extract — success code not specified in the source:**

{payload(credential_result, [CERT_PROVIDER])}

Keep `data.id` as the credential connection reference. The source also returns `data.links.credentialsPatchEndpoint.href`; its update method/contract needs confirmation. The response does not return a validated-expiry or readiness result.

The request example uses `credentials.credentialsObject`; its field table instead says `certificate.credentialsObject`. The example above follows the code nesting. The API owner must resolve this conflict. `expiresBy` is declared input expiry, not proof of validation.

### 2.2 Existing internal encryption

{call('POST /datasets/{dataset_id}/compliance/es-anti-fraud-legislation/encryptions')} — internal Connections Service/AFL flow, not an extra ERP call.

**Request extract:**

{request('POST', '/datasets/{dataset_id}/compliance/es-anti-fraud-legislation/encryptions', encryption_request, tax=True, extra_headers=['Idempotency-Key: {idempotencyKey}'])}

**Response extract:**

{payload(encryption_result)}

Reuse the protected flow where qualified. The source does not define how certificate/password contents are serialised inside `secret`; do not invent that format.

### 2.3 Credential selection and the additional onboarding result

Existing ES AFL selection header: {call('Connection-Id: <credential-connection-id>')}. The [certificate-management source](<../../../context/Tax API/Certificates/sage-certificate-management-guide-extract.md>) documents this for customer certificates and the Sage seal. INT-CERT02.

| Customer case | Existing mechanism / B2B work |
|---|---|
| Customer certificate already held | Reuse its credential connection ID. {blue('Confirm the business/client/environment mapping and B2B suitability before use.')} |
| Customer certificate missing | Use the separate provisioning flow in §2.1. {blue('Confirm its B2B provider and accepted certificate class.')} |
| Sage seal selected | ES AFL uses a dedicated provider and credential type. {blue('Confirm their actual values, the stored purpose-specific agreement and permission for B2B use. No customer upload of the Sage seal.')} |

{blue('For B2B, propose reusing Connection-Id selection inside the authorised service integration. Engineering must confirm whether the product supplies the reference or the backend resolves it from existing setup. It is not a confirmed new header on the E-Invoice APIs.')}

| Additional onboarding response information | What is still missing |
|---|---|
| {blue('Credential reference actually selected; certificate/material version.')} | Confirm how a credential lookup/validation interface returns these values. The creation response supplies only the new connection reference. |
| {blue('Validated expiry, trust/revocation and suitability findings for the selected action/environment.')} | `expiresBy` alone is insufficient; no validation response schema is supplied by the Connections Service page. |
| {blue('Purpose-specific readiness, reason and next action/owner; next mandatory check.')} | Map actual Tax results to [SPEC001 CERT-04/05](../../SPEC-SEI-001-certificate-management-solution-specification.md#6-cert-0405-validate-trust-and-calculate-scoped-readiness); response field names remain to confirm. |

{blue('Use SPEC001’s proposed readiness meanings: NOT_REQUIRED, READY, EXPIRING, ACTION_REQUIRED, BLOCKED or UNDETERMINED. Tax response fields must be mapped to these meanings; they are not confirmed Tax wire values.')}

The public connector uses an accepted certificate for authenticated HTTPS. The supplied WSDL separates certificate and seal ports; it does not define a certificate field in the business request/response. These ports do not supply an onboarding call. SPFE-S03/S16.

Reuse suitable in-date material; expired/revoked/unsuitable material needs action. Unavailable lookup remains pending, not a request for another upload. NIF and permission remain independent. Tax/Connections/AFL owners must confirm lookup/readiness contracts and B2B binding under GAP-03/06 and SPEC001 G1/G9/G10.

## 3 Other additional calls to confirm

{blue('These are proposed interactions to qualify against existing services. HTTP methods, URLs and new wire-field names remain unconfirmed.')} [039 §2.7](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#27-who-sends-what-and-what-comes-back) retains the full responsibility boundaries.

| Call to assess | Request → response needed | Owner / 039 gap |
|---|---|---|
| {blue('NIF / permission check')} | {blue('Business, caller and action → separate identity/authority findings or correction needed.')} | Identity/Product — GAP-03/06 |
| {blue('Public access check')} | {blue('Selected function, environment and authorised credential use → access finding. No enrolment call or test invoice is established.')} | Public Integration — GAP-06 |
| {blue('B2B Router account check / setup mapping')} | Documented candidate: {call('GET /accounts')} → visible provider accounts. {blue('Bind only the authorised business account to the SXS dataset and private connection; confirm credentials, version and setup operations. No account-creation call is assumed.')} REF-B2BR. | Integration — GAP-02/05/06; documented provider API, Sage implementation unknown. |
| {blue('ZeroComa setup mapping')} | {blue('Vendor must supply its target service, business/account fields, credentials and setup response. No verified onboarding payload is available to show.')} REF-ZEROCOMA. | Provider Engineering — GAP-02/05/06; contract required before implementation. |
| {blue('Allowed route change')} | {blue('Current/target connection, requested start and permission → confirmed effective start, earlier-invoice access or pending action.')} | Routing — GAP-06/08. Private A to Private B stays disabled. |

For blue items, engineering must identify existing support, configuration/country rules, code changes or API-contract changes. Use [039’s GAP owners](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#4-open-engineering-decisions). Keep Spain rules separate from other countries.

## REF Source references

FR-01–05 are supplied OpenAPI 3.1.0 contracts declaring API version `1.0.0`, reviewed 26 October 2026. Grey structures follow those schemas; blue values/information require confirmation. Requests show the method, sandbox URL, path inputs, headers and body where applicable. Full field constraints, audit fields and error schemas remain in the sources.

| ID | Source / exact locator | Supports / limit |
|---|---|---|
| FR-01 | [Discovery](<../../../context/FR API/Onboarding/get-accesspoints.md>), `Get-AccessPoints`; `servers`, `securitySchemes.m2m`, operation parameters. | API-01 request/catalogue; declared `datasetId` does not appear in the URL and needs correction. |
| FR-02 | [Dataset listing](<../../../context/FR API/Onboarding/get-dataset-accesspoints.md>), `Get-Dataset-AccessPoints`; `servers`, `securitySchemes.m2m`, operation parameters. | API-02 path, authentication/tracing headers and nullable connection ID. |
| FR-03 | [Connect](<../../../context/FR API/Onboarding/new-accesspoint-connection.md>), `New-AccessPoint-Connection`; parameters, security, request media type and `AccessPointConnectionRequest/Response`. | API-03 request, required `Idempotency-Key` and payload; no Spain enum or certificate field. |
| FR-04 | [Detail](<../../../context/FR API/Onboarding/get-accesspoint-connection.md>), `Get-AccessPoint-Connection`; parameters and security. | API-04 request and address results, not complete readiness. The guide's extra idempotency header remains a source conflict. |
| FR-05 | [Update](<../../../context/FR API/Onboarding/put-accesspoint-connection.md>), `Put-AccessPoint-Connection`; parameters, security, request media type and `UpdateAccessPointConnectionRequest/Response`. | API-05 request and add/update actions; no idempotency header declared, and no approved route-change contract. |
| INT-AP01/06 | [Access-point guide extract](<../../../context/FR API/Onboarding/access-point-guides-evidence-extract.md>), received 22 October 2026, **Connect and channel selection / Catalogue, address mapping and environments**; revision unverified. | One connection per dataset/access point, several addresses and per-service references. Spain implementation coverage remains unknown. |
| INT-CERT01 | [Connections Service API extract](<../../../context/Tax API/Certificates/connections-service-certificate-guide-extract.md>), Confluence 467063094 v4, read 26 October 2026; **Certificate upload / Internal - Encrypt**, requests, responses and field tables. | Existing provisioning/encryption examples; nesting and syntax issues remain owner questions. No B2B provider/readiness contract. |
| INT-CERT02 | [Certificate-management extract](<../../../context/Tax API/Certificates/sage-certificate-management-guide-extract.md>), Confluence 759615024 v6, read 26 October 2026; **Current solution / Proposed solution / Final Decision Summary**. | Exact ES AFL `Connection-Id`, customer/seal selection, custody and agreement gate. Page remains UNDER REVIEW; not proof of B2B deployment. |
| REF-CERT | [SPEC001](../../SPEC-SEI-001-certificate-management-solution-specification.md), draft, 20 October 2026, CERT-04/05 and G1/G9/G10. | Proposed certificate validation/readiness meanings; no confirmed Tax wire response. |
| SPFE-S03/S16 | [Original catalogue](<../../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026, §4.3 p.8; [SendInvoice WSDL](<../../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), snapshot 13 October 2026, `SendInvoiceCertPort` / `SendInvoiceSealPort`. | Certificate-authenticated HTTPS and separate PRE access ports; no certificate property or onboarding command. |
| REF-INTEGRATION | User direction, 26–27 October 2026; [038 product precondition](../SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules) and [SXS definition](../../../context/GLO-SEI-001-e-invoicing-terminology.md#services-connections-and-routing). | Confirmed product list and requested SXS/Tax integration precondition; deployment/interface coverage still needs evidence. |
| REF-PROVIDERS | [PRD213](../../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md#phase-2-prd-set), draft, 11 September 2026, Phase 2 PRD set; provider PRDs 216–220. | Five named provider candidates. Does not establish available services, catalogue IDs or completed integrations. |
| REF-CONNECTIONS | [PRD214](../../../prds/PRD-SEI-214-connections-registration-routing-structured-review.md#connections-registration-and-capability), draft, 7 October 2026, FR1–5/7–9; [SPEC014](../../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md#1-model-outcomes-and-invariants), draft, 20 October 2026, invariants 3–6. | Proposed concurrent public/private connections and one route per scope. Dataset binding, public access-point representation and Spain implementation remain open. |
| REF-B2BR | [B2B Router List accounts](https://developer.b2brouter.net/reference/get-accounts), read 26 October 2026, `GET /accounts`; [SPEC017](../../SPEC-SEI-017-b2b-router-provider-adapter-binding-solution-specification.md#3-provider-operation-binding), draft, 20 October 2026, §3 **List account scope** and B2BR-Q01. | Existing provider account-list operation; proposed use to check account mapping. Contract/version selection, account mapping and Sage build remain unqualified. No response schema inferred here. |
| REF-ZEROCOMA | [PRD220](../../../prds/PRD-SEI-220-zerocoma-integration-structured-review.md#evidence-and-research-findings), draft, 11 September 2026, **Evidence and research findings**, E1/E2 and **Connection and onboarding**, FR15–17. | Public integration claim only; target private-platform product and onboarding contract remain open. No wire fields inferred. |
| REF-SPAIN-PROPOSAL | [039](../SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md), draft, 27 October 2026, §§2.1–2.7 and GAP-01–08. | Sequence and ownership baseline for blue proposals; no deployment approval. |
'''
DOC.write_text('---' + front + '---\n\n' + body)
print(json.dumps({'file': str(DOC.relative_to(ROOT)), 'e_invoice_response_extracts': 5,
                  'e_invoice_request_examples': 5, 'e_invoice_request_body_examples': 2,
                  'credential_encryption_request_examples': 2, 'credential_encryption_examples': 4,
                  'certificate_management': True,
                  'diagrams': 0, 'published': False}, indent=2))
