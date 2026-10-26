---
id: SPEC-SEI-039
title: Customer Onboarding and Connectivity Sequence and Reuse Assessment
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: '2026-10-23'
updated: '2026-10-26'
reviewers: []
related:
- SPEC-SEI-037
- SPEC-SEI-038
- SPEC-SEI-021
- SPEC-SEI-036
- SPEC-SEI-020
- SPEC-SEI-018
- SPEC-SEI-019
- SPEC-SEI-001
- SPEC-SEI-003
- SPEC-SEI-008
- SPEC-SEI-014
- SPEC-SEI-016
- PRD-SEI-227
- GLO-SEI-001
- RES-SEI-002
- SPEC-SEI-034
- SPEC-SEI-035
- SPEC-SEI-011
- SPEC-SEI-013
- SPEC-SEI-017
- PRD-SEI-210
- PRD-SEI-221
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: '837610648'
  page_id: '936509735'
  title: Onboarding and Connectivity API Reuse Assessment
  layout: two_left_sidebar
  toc: true
---

# Customer Onboarding and Connectivity Sequence and Reuse Assessment

[Summary — 037](SPEC-SEI-037-customer-onboarding-and-connectivity-solution-summary.md) · [Customer paths — 038](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md)

## Revision overview

This view combines SPEC-SEI-021 and SPEC-SEI-036. It assesses reuse; it does not design a new API. Existing API/GAP IDs retain their meanings. Payloads and detailed contract checks remain in their linked sources. The predecessors are unchanged.

## 1 Engineering direction

**What:** set up Sage access to the customer's selected e-invoicing platform. **Why:** reuse valid setup without repeated registration or an unintended provider change.

**What exists:** the shared E-Invoice API can list services, find connections, connect, read status and update supported details. **Proposal:** reuse these calls and the Tax certificate capability. Add Spain rules and provider support where needed. The supplied contracts establish API behaviour; they do not prove a Spain implementation is ready. FR-01–05; REF-TRUST.

| Delivery scope | Work to assess | Impact on integrating products |
|---|---|---|
| Public MVP — Phase 1 | Spain service/environment settings; NIF, permission, required certificate and Sage-access checks. | Reuse saved information; show readiness, missing work and action owner. Confirm interfaces before implementing Spain inputs. |
| Public nice-to-haves | Certificate-renewal reminders and supported progress events. | Optional reminders/notifications; status checks and recovery remain MVP. |
| Private platforms — later phase | Provider account connection, Spain address rules and supported changes. | Ask for missing provider inputs; retain connection IDs and earlier-invoice access. |
| Shared / conditional work | Business-to-dataset mapping, accountant permission, results and safe recovery. Sage's own platform offer also requires operator approval. | Confirm existing approval/batch support and API compatibility; do not assume these need new services. |

Private A to Private B stays disabled. [038](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md) owns customer scenarios and functional behaviour. Invoice execution and transformation stay in their owning features; existing DTS remains the preferred transformation candidate there, subject to implementation checks.

## 2 Proposed reuse sequences

Grey / **Existing** shows existing E-Invoice API calls. Blue / **To confirm** shows Spain changes or an interface needing confirmation; it does not mean a new API. Arrows show requests and responses. Lanes show responsibilities, not approved deployments. Keep the returned `datasetId`, `accessPointId` and `connectionId` for later calls; never derive them from NIF.

### 2.1 Shared prerequisites

Check the business NIF, caller permission and a suitable in-date certificate where required. Reuse the Tax service's protected reference. Find the existing dataset mapping; create a dataset only when the channel requires a missing one. Mapping and service interfaces remain GAP-01/03/06. REF-TRUST; SPFE-S02.

[Shared-check sequence](../../assets/diagrams/onboarding-setup-shared-prerequisites-sequence.svg).

### 2.2 Public readiness

![Public setup: inspect Sage setup, check public access and return readiness](../../assets/diagrams/onboarding-setup-public-readiness-sequence.svg)

For ONB-S02, use existing Sage records where applicable, then check access for the selected public function. `CONNECTED` alone does not prove public access. The supplied public contracts provide no enrolment API; do not assume `/connect` registers the business or send a test invoice. Public execution contracts remain in [SPEC011](../SPEC-SEI-011-public-platform-connector-solution-specification.md). SPFE-S03/S08/S16.

### 2.3 Private setup

![Private setup: find the connection, add missing setup and observe each address result](../../assets/diagrams/onboarding-setup-private-setup-sequence.svg)

For ONB-S03, find the selected service and connection (API-01/02). Reuse valid setup; connect only when required (API-03), then read progress (API-04). Save the returned connection ID. Check permission and routing effects before connecting. Spain provider inputs remain GAP-02; a connected address does not itself activate a customer route.

The unlisted-provider decision is in [038 §3.2](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#32-decisions-and-open-questions); the separate interconnection duty is in its [operator handoff](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#operator-interconnection-handoff). Sage's operator role requires the [PRD221](../../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md) checks; customer connection success is insufficient.

### 2.4 Supported change

![Change routing or platform: check permission, reuse or connect the target, and confirm the authorised change](../../assets/diagrams/onboarding-setup-supported-change-sequence.svg)

**Change routing or platform — ONB-S05/S06:** read existing setup first. If an allowed platform change needs a target connection, use the private setup in §2.3. Use API-05 only for supported connection edits. Separately authorise and confirm the route change and its effective start; preserve access to earlier invoices. [SPEC014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns these routing controls. Private A to Private B stays disabled; an update is not a general migration or rollback.

### 2.5 Uncertainty and recovery

Read the original connection before repeating an uncertain request. A failed or empty read does not prove no effect. While an address is `RETRYING`, observe it rather than submitting another connect. Keep unresolved work pending with an owner. INT-AP05/06. [Recovery sequence](../../assets/diagrams/onboarding-setup-uncertainty-recovery-sequence.svg).

### 2.6 Existing API and capability reuse

**Reuse** selects a candidate, not a proven Spain build. The gap IDs point to the owner checks in §4. Exact schemas, headers and status definitions belong to the linked API contracts.

| Existing call / capability | Reuse proposal and Spain change | Gaps |
|---|---|---|
| Dataset: `POST /datasets` — INT-DS01 | Reuse conditional creation. Confirm Spain business inputs and business/client mapping. | GAP-01/02/04 |
| API-01: `GET /accesspoints` — FR-01 | Reuse discovery; add confirmed Spain services and environments. | GAP-02/08 |
| API-02: `GET /datasets/{datasetId}/accesspoints` — FR-02 | Reuse connection lookup and returned IDs. | GAP-01/05 |
| API-03: `POST /connectors/{accessPointId}/datasets/{datasetId}/connect` — FR-03 | Reuse private connection setup with confirmed Spain addresses/provider inputs. Public applicability is unconfirmed. | GAP-02/03/04 |
| API-04: `GET /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/` — FR-04 | Reuse per-address status reads; confirm Spain result meanings. | GAP-04/05 |
| API-05: `PUT /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/` — FR-05 | Reuse supported updates; confirm Spain fields and route effects. | GAP-04/07 |
| Events — INT-AP01–06 | Reuse supported subscriptions/notifications; caller access and public coverage are unconfirmed. | GAP-05/06/07 |
| Identity and Tax certificate services — REF-TRUST | Reuse existing checks and protected references; confirm NIF, representation and certificate acceptance. | GAP-03/06 |
| Public connector — SPEC011 | Reuse the proposed access-check pattern; confirm actual Spain build and environment support. | GAP-02/05/06 |
| Setup results, approval, batches and recovery — 038 | Identify existing implementation; build only missing behaviour. | GAP-04/05/06/08 |
| Shared routing — SPEC014 | Reuse the design for authorised activation and earlier-invoice access; confirm running implementation. | GAP-06/08 |

Disconnection belongs to [offboarding](../archive/SPEC-SEI-003-offboarding-solution-specification.md). Do not delete/recreate a connection to repair an unknown result. Keep one product-facing API direction under [SPEC013](../SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md); provider integration mode remains an architecture decision.

### 2.7 Who sends what and what comes back

This table describes onboarding only. **Existing** uses supplied API fields. **Proposed** describes information to exchange, not approved JSON fields or a new endpoint. Products call the Domain Service; the selected integration handles platform calls.

| Caller → receiver | Request / information needed | Response / what the caller keeps |
|---|---|---|
| ERP/product → Domain Service: public checks — **Proposed** | Business NIF, requested function, environment and known setup references, with trusted caller/permission context. Reuse saved values. | Result for each function, missing information and next action/owner. The exact interface remains GAP-05/06; no government-registration receipt is assumed. |
| ERP/product → E-Invoice API: private connect — **Existing**, Spain values unconfirmed | API-03 path IDs: `datasetId`, `accessPointId`. Body: `companyName`, `companyAddress`, `companyPostalCode`, `companyCountryCode`, `user` and `accessPointAddresses`. Use the full FR-03 schema for required nested fields and headers. | `201` connection resource: keep `data.id` as `connectionId`. Read each address's `status` and `errorCode` through API-04. This is connection progress, not route activation. |
| Domain Service → Tax certificate capability — **Proposed**, interface unconfirmed | Business reference, selected action and environment; locate suitable existing material. | Certificate-check result and protected reference where available. Keep private keys inside the trusted service. REF-TRUST; GAP-03/06. |
| Domain Service / public connector → Spain public platform — **Not established for onboarding** | No enrolment request is supplied. Any external access check needs a confirmed operation and accepted caller credential; do not use an invoice as a probe. | No external onboarding-response format is established. Return the supported access-check findings to the product. SPFE-S02/S03/S08/S16; GAP-06. |
| Domain Service / private integration → selected provider — **Proposed**, provider contract required | Provider-required business/account identifiers, addresses and authorised credential use. Map the E-Invoice request to that provider's contract; do not assume the same body is forwarded. | Provider account/connection reference and setup result or error, mapped to the E-Invoice result. Exact endpoints, required fields and codes remain GAP-02/05/06. |
| ERP/product → Domain Service / Routing: allowed change — **Proposed** | Existing connection, target platform, requested change/start and permission for that change. | Confirmed effective start and earlier-invoice access, or pending action/owner. API-05 alone does not establish this routing contract. See §2.4; GAP-06. |

## 3 Scenario variations

Use the [single scenario table in 038](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#31-in-scope). ONB-S01–04 select the shared/public/private paths. ONB-S05/S06 add the change checks; ONB-S07 preserves B2G; ONB-S08 returns a limitation. Approval, recovery and accountant batches are conditional steps in that same journey.

## 4 Open engineering decisions

Each owner must identify existing code, missing changes and evidence before the affected path is enabled. Documentation alone does not establish production support.

| ID | Decision / evidence needed | Owner |
|---|---|---|
| GAP-01 | Confirm `datasetId` mapping for NIFs, multiple addresses, accountant clients and native-product channels. Do not assume one dataset per NIF. | API, Identity, Tax, Enablement |
| GAP-02 | Supply Spain service IDs, environments, business/address types and provider inputs. Classify each change as configuration, code or API contract. `fr.*` values are not Spain identifiers. | Spain Product/Compliance, API, Integration |
| GAP-03 | Confirm accepted evidence that the caller may act for this business. Login and certificate possession are insufficient. | Identity, Security, Product |
| GAP-04 | Confirm duplicate handling, safe repeats, concurrent changes and how to establish an earlier request's result. | API, Integration, Operations |
| GAP-05 | Confirm what each status/event proves, including partial or missing addresses and separate activation. | API, E-Invoice Service, Routing |
| GAP-06 | Identify actual Tax/identity, public/provider, approval/batch and route interfaces. Confirm operator-process handoff where applicable. | Architecture and service owners; Compliance/Operations for operator duties |
| GAP-07 | Resolve guide/schema differences in usage, update/removal, retries, events and versions. Use the [existing source-difference record](../archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md#5-common-spain-changes-and-open-evidence). | API, Operations |
| GAP-08 | Demonstrate Spain support, existing-product compatibility and support ownership. Product/local technical lead must decide the unlisted-provider option. | Architecture, API, Integration, Operations, Spain Product |

## 5 Acceptance coverage

Use [038's release checks](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#review-and-release-gates) and the existing [API-A01–16](../archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md#6-reuse-assurance). Check contract compatibility, safe recovery, client isolation and country isolation. A customer connection must not enable the Sage operator role or change another customer's route. These are evidence to obtain, not completed tests.

## REF Source references

| ID | Source, version and exact location | Supports / limit |
|---|---|---|
| FR-01 | [Discovery contract](<../../context/FR API/Onboarding/get-accesspoints.md>), declared version 1.0.0, `Get-AccessPoints`. | API-01 discovery; not readiness. |
| FR-02 | [Dataset listing](<../../context/FR API/Onboarding/get-dataset-accesspoints.md>), 1.0.0, `Get-Dataset-AccessPoints`. | API-02 status and nullable `connectionId`. |
| FR-03 | [Connect contract](<../../context/FR API/Onboarding/new-accesspoint-connection.md>), 1.0.0, `New-AccessPoint-Connection`, request/response schemas. | API-03 and full payload example; replay/routing effects need confirmation. |
| FR-04 | [Connection detail](<../../context/FR API/Onboarding/get-accesspoint-connection.md>), 1.0.0, `Get-AccessPoint-Connection`. | API-04 per-address status/error; not activation. |
| FR-05 | [Update contract](<../../context/FR API/Onboarding/put-accesspoint-connection.md>), 1.0.0, `Put-AccessPoint-Connection`. | API-05; no generic migration/replay guarantee. |
| INT-DS01 | [Dataset guide](<../../context/FR API/Onboarding/network-onboarding-create-dataset-guide-extract.md>), received 22 October 2026, ownership/channel sections and steps 1–2; revision unverified. | Conditional provisioning; Spain mapping and native linkage remain open. |
| INT-AP01–06 | [Access-point guides](<../../context/FR API/Onboarding/access-point-guides-evidence-extract.md>), received 22 October 2026, connect/update/ownership/errors/catalogue sections; revisions/builds unverified. | Existing flow guidance; source conflicts remain GAP-07. |
| REF-TRUST | [SPEC001](../SPEC-SEI-001-certificate-management-solution-specification.md), 20 October 2026, CERT-04/05 and G1/G9/G10; [Sage certificate management](https://confluence.sage.com/spaces/CCLD/pages/759615024/Sage+certificate+management), supplied context, content/version unverified. | Proposed certificate reuse; no confirmed Tax API or Spain acceptance. |
| SPFE-S02/S03/S08/S16 | [BOE HAC/1028/2026](../../context/BOE-A-2026-20587.pdf), 5 October 2026, Article 11; [catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>)/[draft formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>) 0.1.0, 9 October 2026, §§6.1–6.10/5.1–5.9; [SendInvoice WSDL](<../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), 13 October 2026, binding/ports. | Public access/operation boundary; no supplied enrolment contract or proven build. Conflicts remain in [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md). |
| REF-PRODUCT | [PRD227](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md), repository draft, FR11; [SPEC014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md), 20 October 2026, SPC-01–08; [PRD221](../../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md), 6 October 2026, readiness domains/FR20. | Shared/country separation, proposed routing and operator scope; no implementation or launch approval. |
