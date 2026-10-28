---
id: SPEC-SEI-039
title: Customer Onboarding and Connectivity Sequence and Reuse Assessment
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: '2026-10-23'
updated: '2026-10-28'
reviewers: []
related:
- SPEC-SEI-040
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

[Summary — 037](SPEC-SEI-037-customer-onboarding-and-connectivity-solution-summary.md) · [Customer paths — 038](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md) · [API and field changes — 040](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md)

Products: **Sage 50, Sage 200, Sage Active and Sage X3** are the ERP products; **Despachos** is the accountant product. Each must meet the [SXS and Tax integration precondition](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules) before enabling e-invoicing. SXS manages the product's `datasetId` / `tenantId`.

<a id="revision-overview"></a>

## Revision overview — Phases 1–3

This view combines SPEC-SEI-021 and SPEC-SEI-036. It owns sequences, product impact and GAP decisions; 040 owns request/response examples. API/GAP IDs and predecessors are unchanged.

<a id="1-engineering-direction"></a>

## 1 Engineering direction — Phases 1–3

**What:** set up Sage access to the customer's selected e-invoicing platform. **Why:** reuse valid setup without repeated registration or an unintended provider change.

**Phase coverage:** **1 — SPFE public solution; 2 — external private providers; 3 — Sage private-platform offering.** Labels show analysis coverage, not delivery approval or confirmed API availability. REF-PHASE.

**What exists:** the shared E-Invoice API can list services, find connections, connect, read status and update supported details. **Proposal:** reuse these calls and the [Tax certificate capability](https://confluence.sage.com/spaces/CCLD/pages/759615024/Sage+certificate+management). Add Spain rules and provider support where needed. The supplied contracts establish API behaviour; they do not prove a Spain implementation is ready. FR-01–05; REF-TRUST.

| Delivery scope | Work to assess | Impact on integrating products | Phase |
|---|---|---|---|
| Public MVP | Spain service/environment settings; NIF, permission, required certificate and Sage-access checks. | Reuse saved information; show readiness, missing work and action owner. Confirm interfaces before implementing Spain inputs. | 1 |
| Public nice-to-haves | Certificate-renewal reminders and supported progress events. | Optional reminders/notifications; status checks and recovery remain MVP. | 1; optional enhancement, not MVP |
| Private platforms | Provider account connection, Spain address rules and supported changes. | Ask for missing provider inputs; retain connection IDs and earlier-invoice access. | 2; reused in 3 where qualified |
| Sage private-platform offering | Assess reuse of shared setup and provider integration; confirm delivery model and operator readiness. | Use the qualified Sage offering only after its operator and service-chain gates pass; no separate API model is selected. | 3 |
| Shared / conditional work | Business-to-dataset mapping, accountant permission, results and safe recovery. | Confirm existing approval/batch support and API compatibility; do not assume these need new services. | 1–3 |

Private A to Private B stays disabled. [038](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md) owns customer scenarios and functional behaviour. Invoice execution and transformation stay in their owning features; existing DTS remains the preferred transformation candidate there, subject to implementation checks.

<a id="4-open-engineering-decisions"></a>

<a id="2-open-engineering-decisions"></a>

## 2 Open engineering decisions — Phases 1–3

This is the authoritative GAP-01–08 register for 037–040. Owners must supply the required evidence before the affected path is enabled.

| ID | Decision / evidence needed | Owner | Phase |
|---|---|---|---|
| <a id="gap-01"></a><span style="color:#B42318;white-space:nowrap;">GAP-01</span> | <span style="color:#B42318;">Confirm SXS business/client mapping and supported resource relationships with GAP-02. Several addresses do not prove several legal entities; do not assume one dataset per NIF.</span> | API, Identity, Tax, Enablement | 1–3 |
| <a id="gap-02"></a><span style="color:#B42318;white-space:nowrap;">GAP-02</span> | <span style="color:#B42318;">**Spain connection model:** Does adding a platform require a new E-Invoice connection, allow reuse of an existing connection, or require another mapping? Architecture and Engineering must validate or replace the [BA hypothesis in 040 API-02](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-02). No option is selected. Several platform connections under one access point remain an alternative to assess, not established support. Include SPFE representation and Phase 1 API applicability. Supply the selected build/contract and a worked response example; confirm Spain service IDs/environments, address types, provider inputs, supported combinations and required configuration/code/contract changes. `fr.*` values are not Spain identifiers.</span> | Architecture and Engineering (API/Integration); Spain Product/Compliance for country rules | 1–3 |
| <a id="gap-03"></a><span style="color:#B42318;white-space:nowrap;">GAP-03</span> | <span style="color:#B42318;">Confirm accepted evidence that the caller may act for this business. Login and certificate possession are insufficient.</span> | Identity, Security, Product | 1–3 |
| <a id="gap-04"></a><span style="color:#B42318;white-space:nowrap;">GAP-04</span> | <span style="color:#B42318;">Confirm duplicate handling, safe repeats, concurrent changes and how to establish an earlier request's result.</span> | API, Integration, Operations | 1–3 |
| <a id="gap-05"></a><span style="color:#B42318;white-space:nowrap;">GAP-05</span> | <span style="color:#B42318;">Confirm what each status/event proves, including partial or missing addresses and separate activation.</span> | API, E-Invoice Service, Routing | 1–3 |
| <a id="gap-06"></a><span style="color:#B42318;white-space:nowrap;">GAP-06</span> | <span style="color:#B42318;">**Certificate reuse and ID relationships:** Can a suitable existing certificate be reused without another upload? Can the existing Tax credential connection ID be retained, or is a new one required? Can several E-Invoice connections use that credential? Validate the [BA hypothesis in 040 §2.3](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#23-credential-selection-and-the-additional-onboarding-result). Confirm certificate acceptance/permitted use and whether Tax/E-Invoice IDs are shared, mapped or independent. Require versioned contracts and a same-environment example showing certificate reuse and resulting IDs. GAP-02 owns the new platform's E-Invoice connection decision. Do not substitute IDs before confirmation. Qualify SXS/Tax binding, B2B reuse of documented AEAT provider discovery/upload, secure provisioning, `Connection-Id` selection and non-secret lookup/readiness contracts. HMRC trusted-service retrieval does not establish these. Identify identity, public/provider, approval/batch and routing interfaces. Prove independent platform access/credentials and one route per scope under the selected model; confirm operator handoff.</span> | Architecture, Tax/Connections, E-Invoice API and provider integration owners; other service owners for their interfaces; Compliance/Operations for operator duties | 1–3; operator gate in 3 |
| <a id="gap-07"></a><span style="color:#B42318;white-space:nowrap;">GAP-07</span> | <span style="color:#B42318;">Resolve guide/schema differences in usage, update/removal, retries, events and versions. Use the [existing source-difference record](../archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md#5-common-spain-changes-and-open-evidence).</span> | API, Operations | 1–3 |
| <a id="gap-08"></a><span style="color:#B42318;white-space:nowrap;">GAP-08</span> | <span style="color:#B42318;">Demonstrate Spain support, existing-product compatibility and support ownership. Product/local technical lead must decide the unlisted-provider option.</span> | Architecture, API, Integration, Operations, Spain Product | 1–3; unlisted-provider choice in 2 |

<a id="2-proposed-reuse-sequences"></a>

<a id="3-proposed-reuse-sequences"></a>

## 3 Proposed reuse sequences — Phases 1–3

<span style="color:#666666;">Grey: existing calls.</span> <span style="color:#1565C0;">Blue: proposed Spain work.</span> <span style="color:#B42318;">Red: open questions, uncertainty or assumptions requiring validation.</span> Arrows show requests/responses; lanes show responsibilities. Keep returned `datasetId`, `accessPointId` and `connectionId`; never derive them from NIF. Diagrams do not establish deployments or production readiness.

<a id="21-shared-prerequisites"></a>

<a id="31-shared-prerequisites"></a>

### 3.1 Shared prerequisites — Phases 1–3

Start after the product has integrated SXS and Tax certificate management / Connections Service, as required by 038 §4. For each company, resolve its SXS dataset/client mapping first. If confirmed missing, complete qualified channel/SXS setup before dataset-scoped calls; an unavailable lookup remains pending. Then check NIF, permission and any required credential. Keep each credential/connection reference with its source API; their ID relationship remains unconfirmed under GAP-06. Provision only a genuinely missing credential through [040 §2](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#2-certificate-management-proposed-call-to-confirm). The diagram proposes the call order, not new SXS or B2B Tax contracts. GAP-01/03/06; REF-INTEGRATION; REF-TRUST; INT-CERT01–03; SPFE-S02.

Existing API-02 returns access-point entries with connection references. INT-AP01–06 describe one connection per `datasetId` / `accessPointId` pair and several addresses inside a connection. <span style="color:#B42318;">The [040 API-02 Spain mapping](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-02) is an unvalidated BA hypothesis; [GAP-02](#gap-02) owns the decision.</span> Keep service-returned IDs; do not assume one access point or connection equals one platform. Public/private coexistence remains subject to implementation evidence under GAP-01/02/06. A saved connection does not activate a route. FR-02; INT-AP01–06; REF-CONNECTIONS.

![Shared prerequisites: product integrations are ready; resolve the SXS dataset, then check NIF, permission and any required credential](../../assets/diagrams/onboarding-setup-shared-prerequisites-sequence.svg)

<a id="22-public-readiness"></a>

<a id="32-public-readiness"></a>

### 3.2 Public readiness — Phase 1; reused in Phases 2–3

![Public setup: inspect Sage setup, check public access and return readiness](../../assets/diagrams/onboarding-setup-public-readiness-sequence.svg)

For ONB-S02, reuse saved setup and check access for the selected public function. `CONNECTED` does not prove public access. No enrolment API is supplied: `/connect` must not be assumed to register the business. Do not send a test invoice. See [040 §3](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#3-other-additional-calls-to-confirm) for the proposed access check; execution contracts remain in [SPEC011](../SPEC-SEI-011-public-platform-connector-solution-specification.md). SPFE-S03/S08/S16.

<a id="23-private-setup"></a>

<a id="33-private-setup"></a>

### 3.3 Private setup — Phases 2–3

![Private setup: find the connection, add missing setup and observe each address result](../../assets/diagrams/onboarding-setup-private-setup-sequence.svg)

For ONB-S03, find the service and connection (API-01/02). Reuse valid setup; connect only if missing (API-03), then read progress (API-04). Check permission and routing effects first. A connected address does not activate a route.

The Phase 2 portfolio names B2B Router, Banqup (Unifiedpost), EDICOM, SERES (Docaposte) and ZeroComa. [040](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-01) also records **Sovos as a new candidate** from the Confluence review. <span style="color:#B42318;">Names do not prove Spain integration readiness; provider services, contracts and inputs remain GAP-02/06.</span> REF-PROVIDERS.

The unlisted-provider decision is in [038 §3.2](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#32-decisions-and-open-questions); the separate interconnection duty is in its [operator handoff](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#operator-interconnection-handoff). Sage's operator role requires the [PRD221](../../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md) checks; customer connection success is insufficient.

<a id="24-supported-change"></a>

<a id="34-supported-change"></a>

### 3.4 Supported change — Phases 2–3, enabled changes only

![Change routing or platform: check permission, reuse or connect the target, and confirm the authorised change](../../assets/diagrams/onboarding-setup-supported-change-sequence.svg)

**Change routing or platform — ONB-S05/S06:** read existing setup first. If the chosen Spain model exposes another platform as a different `accessPointId`, API-03 is the candidate for its missing dataset connection (§3.3). <span style="color:#B42318;">Other mappings require contract assessment under GAP-02.</span> Within an existing connection, API-05 adds an address (`add`) or changes address dates (`update`), including both in one request. Confirm Spain address/grouping rules and public access-point representation. Separately authorise the routing change and confirm its effective start and earlier-invoice access. [SPEC014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns those controls. Private A to Private B stays disabled; PUT does not establish a general migration or rollback.

<a id="25-uncertainty-and-recovery"></a>

<a id="35-uncertainty-and-recovery"></a>

### 3.5 Uncertainty and recovery — Phases 1–3

Read the original connection before repeating an uncertain request. A failed or empty read does not prove no effect. While an address is `RETRYING`, observe it rather than submitting another connect. Keep unresolved work pending with an owner. INT-AP05/06. [Recovery sequence](../../assets/diagrams/onboarding-setup-uncertainty-recovery-sequence.svg).

<a id="26-existing-api-and-capability-reuse"></a>

<a id="36-existing-api-and-capability-reuse"></a>

### 3.6 Existing API and capability reuse — Phases 1–3

API links open 040's examples. [§2](#2-open-engineering-decisions) owns GAP decisions and evidence gates.

| Existing call / capability | Reuse proposal and Spain change | Gaps | Phase |
|---|---|---|---|
| Dataset: `POST /datasets` — INT-DS01 | Qualify the SXS binding to channel-specific provisioning. Reuse an existing mapping; confirm missing setup before creation. | <span style="color:#B42318;">GAP-01/02/04/06</span> | 1–3 |
| [API-01 — Discover services](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-01) — FR-01 | Reuse catalogue; qualify Spain service IDs/environments. | <span style="color:#B42318;">GAP-02/08</span> | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| [API-02 — Find connections](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-02) — FR-02 | Reuse array; confirm dataset mapping and concurrent public/private support. | <span style="color:#B42318;">GAP-01/02/06</span> | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| [API-03 — Connect](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-03) — FR-03 | Create the selected dataset/access-point connection with initial addresses, optional dates/usage and company/requester context. Confirm Spain formats/grouping, provider binding and safe repeats. | <span style="color:#B42318;">GAP-02/04/06</span> | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| [API-04 — Read progress](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-04) — FR-04 | Reuse address results; qualify readiness/status meanings and uncertain outcomes. | <span style="color:#B42318;">GAP-04/05/06</span> | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| [API-05 — Update setup](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-05) — FR-05 | Reuse address `add` and date-only `update`, including mixed requests. Confirm Spain grouping/provider support; route changes remain separate. | <span style="color:#B42318;">GAP-02/06/07/08</span> | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| Events — INT-AP01–06 | Reuse supported subscriptions/notifications; caller access and public coverage are unconfirmed. | <span style="color:#B42318;">GAP-05/06/07</span> | 1–3; support to confirm |
| Identity and Tax certificate services — REF-TRUST; INT-CERT03/04 | AEAT provider discovery/upload are documented. Qualify B2B provider use, secure provisioning and reference/readiness lookup; confirm NIF and representation separately. Trusted HMRC credential retrieval does not prove certificate readiness. | <span style="color:#B42318;">GAP-03/06</span> | 1–3; where required |
| Public connector — SPEC011 | Reuse the proposed access-check pattern; confirm actual Spain build and environment support. | <span style="color:#B42318;">GAP-02/05/06</span> | 1; reused in 2–3 |
| Setup results, approval, batches and recovery — 038 | Identify existing implementation; build only missing behaviour. | <span style="color:#B42318;">GAP-04/05/06/08</span> | 1–3 |
| Shared routing — SPEC014 | Reuse the design for authorised activation and earlier-invoice access; confirm running implementation. | <span style="color:#B42318;">GAP-06/08</span> | 2–3; enabled changes only |

Disconnection belongs to [offboarding](../archive/SPEC-SEI-003-offboarding-solution-specification.md). Do not delete/recreate a connection to repair an unknown result. Keep one product-facing API direction under [SPEC013](../SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md); provider integration mode remains an architecture decision.

<a id="27-who-sends-what-and-what-comes-back"></a>

<a id="37-who-sends-what-and-what-comes-back"></a>

### 3.7 Who sends what and what comes back — Phases 1–3

**Existing** uses supplied fields. **Proposed** identifies information needed, not an approved contract. Products call the Domain Service; its selected integration handles platform calls.

| Caller → receiver | Request / information needed | Response / what the caller keeps | Phase |
|---|---|---|---|
| ERP/product → Domain Service: public checks — **Proposed** | Business NIF, requested function, environment and known setup references, with trusted caller/permission context. Reuse saved values. | Result for each function, missing information and next action/owner. The exact interface remains GAP-05/06; no government-registration receipt is assumed. | 1; reused in 2–3 |
| ERP/product → E-Invoice API: private connect — **Existing**, Spain values unconfirmed | API-03: `datasetId`, `accessPointId`, company/requester details and addresses. [040 API-03](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-03) shows the payload; FR-03 owns the full schema. | Keep `data.id` as `connectionId`; `201` means setup started. API-04 supplies address `status` / `errorCode`, not route activation. | 2–3; <span style="color:#B42318;">SPFE use TBD</span> |
| Domain Service → Tax certificate capability — **Proposed B2B reuse** | Resolve the authorised credential connection for the SXS dataset/client. ES AFL selects it with `Connection-Id`; confirm the B2B binding. | AEAT provider discovery returns `providerId`; upload returns `201` and `data.id` as the credential reference. Validated readiness/expiry still needs a contract; see [040 §2](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#2-certificate-management-proposed-call-to-confirm). INT-CERT01–04; GAP-03/06. | 1–3; where required |
| Domain Service / public connector → Spain public platform — **Not established for onboarding** | No enrolment request is supplied. Any external access check needs a confirmed operation and accepted caller credential; do not use an invoice as a probe. | No external onboarding-response format is established. Return the supported access-check findings to the product. SPFE-S02/S03/S08/S16; GAP-06. | 1; reused in 2–3 |
| Domain Service / private integration → selected provider — **Proposed**, provider contract required | Map business/account identity and provider credentials to its contract. [040 §3](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#3-other-additional-calls-to-confirm) distinguishes the B2B Router account-check candidate from ZeroComa's missing contract. | Provider reference and mapped result/error. Provider API credentials remain separate from the Tax certificate. Exact binding remains GAP-02/05/06. | 2–3 |
| ERP/product → Domain Service / Routing: allowed change — **Proposed** | Current/target connection, requested start and permission. | Confirmed effective start and earlier-invoice access, or pending action/owner. API-05 does not define this contract. See §3.4; GAP-06/08. | 2–3; enabled changes only |

<a id="3-scenario-variations"></a>

<a id="4-scenario-variations"></a>

## 4 Scenario variations — Phases 1–3

[038's scenario table](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#31-in-scope) owns ONB-S01–08. Use the paths above; add approval, recovery or accountant batches where required.

<a id="5-acceptance-coverage"></a>

## 5 Acceptance coverage — Phases 1–3

Use [038's release checks](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#review-and-release-gates) and [API-A01–16](../archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md#6-reuse-assurance). Check contract compatibility, returned-ID handling under the selected GAP-02 model, independent credentials/readiness, recovery and client/country isolation. Confirm that Phase 1 SPFE integration does not require an unapproved private-platform model. A connection must not enable the Sage operator role or change another customer's route. These are evidence to obtain, not completed tests.

<a id="ref-source-references"></a>

## REF Source references — Phases 1–3

| ID | Source, version and exact location | Supports / limit |
|---|---|---|
| FR-01 | [Discovery contract](<../../context/FR API/Onboarding/get-accesspoints.md>), declared version 1.0.0, `Get-AccessPoints`. | API-01 discovery; not readiness. |
| FR-02 | [Dataset listing](<../../context/FR API/Onboarding/get-dataset-accesspoints.md>), 1.0.0, `Get-Dataset-AccessPoints`. | API-02 status and nullable `connectionId`. |
| FR-03 | [Connect contract](<../../context/FR API/Onboarding/new-accesspoint-connection.md>), 1.0.0, `New-AccessPoint-Connection`, request/response schemas. | API-03 and full payload example; replay/routing effects need confirmation. |
| FR-04 | [Connection detail](<../../context/FR API/Onboarding/get-accesspoint-connection.md>), 1.0.0, `Get-AccessPoint-Connection`. | API-04 per-address status/error; not activation. |
| FR-05 | [Update contract](<../../context/FR API/Onboarding/put-accesspoint-connection.md>), 1.0.0, `Put-AccessPoint-Connection`; address `action` description and `mixed-actions-success` example. | API-05 add/date-update and mixed requests; current France grouping is not a Spain default. No generic migration/replay guarantee. |
| INT-DS01 | [Dataset guide](<../../context/FR API/Onboarding/network-onboarding-create-dataset-guide-extract.md>), received 22 October 2026, ownership/channel sections and steps 1–2; revision unverified. | Conditional provisioning; Spain mapping and native linkage remain open. |
| INT-AP01–06 | [Access-point guides](<../../context/FR API/Onboarding/access-point-guides-evidence-extract.md>), received 22 October 2026, connect/update/ownership/errors/catalogue sections; revisions/builds unverified. | Existing flow guidance; source conflicts remain GAP-07. |
| REF-PHASE | [PRD213](<../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md>), Phase 2 scope; [PRD210](<../../prds/PRD-SEI-210-sage-private-platform-reuse-and-operator-expansion.md>), Phase 3 document map / phase comparison; [PRD221](<../../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md>), Phase and outcome; repository drafts. User direction, 28 October 2026. | Phase labels describe analysis coverage: SPFE, external providers, then Sage private-platform offering. They do not approve delivery, implementation or Private A to Private B switching. |
| REF-TRUST | [SPEC001](../SPEC-SEI-001-certificate-management-solution-specification.md), 20 October 2026, CERT-04/05 and G1/G9/G10. | Proposed certificate validation/readiness; not a deployed Tax response contract. |
| REF-INTEGRATION | User direction, 26–27 October 2026; [038 §4](SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#4-feature-wide-functional-requirements-and-rules). | Product SXS/Tax integration preconditions. The sequence proposes their use; SXS and B2B credential lookup contracts remain open. |
| INT-CERT01 | [Certificate API extract](<../../context/Tax API/Certificates/connections-service-certificate-guide-extract.md>), Confluence 467063094 v4, read 26 October 2026, **Certificate upload / Internal - Encrypt**. | Existing ES AFL provisioning/encryption fields. Source inconsistencies and B2B binding remain open. |
| INT-CERT02 | [Selection/custody extract](<../../context/Tax API/Certificates/sage-certificate-management-guide-extract.md>), Confluence 759615024 v6, read 26 October 2026, **Current solution / Proposed solution / Final Decision Summary**. | ES AFL `Connection-Id` selection; B2B acceptance remains open. |
| INT-CERT03 | [AEAT upload extract](<../../context/Tax API/Certificates/aeat-certificate-upload-guide-extract.md>), internal guide received 27 October 2026, revision/URL not supplied; **Environments / Obtain provider ID / Upload certificate**. | Confirmed documented GET provider catalogue/POST upload, headers and `200`/`201` for ES AFL. B2B acceptance, secure provisioning and readiness remain open. |
| INT-CERT04 | [Trusted retrieval extract](<../../context/Tax API/Certificates/connections-service-retrieval-guide-extract.md>), Confluence 484738408 v14, read 27 October 2026; **Request method / URL / headers / response**. | Trusted-service GET retrieves HMRC credentials. No demonstrated AEAT certificate shape, product permission or readiness response. |
| REF-PROVIDERS | [PRD213](../../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md#phase-2-prd-set), draft, 11 September 2026, Phase 2 PRD set, provider PRDs 216–220; [040 references](api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#ref-source-references). | Five provider candidates; contracts and Sage implementation need qualification. |
| REF-CONNECTIONS | [PRD214](../../prds/PRD-SEI-214-connections-registration-routing-structured-review.md#connections-registration-and-capability), draft, 7 October 2026, FR1–5/7–9; [SPEC014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md#1-model-outcomes-and-invariants), draft, 20 October 2026, invariants 3–6. | Proposed concurrent public/private connections, separate activation and one route per scope. Does not prove dataset binding, public access-point representation or Spain build. |
| SPFE-S02/S03/S08/S16 | [BOE HAC/1028/2026](../../context/BOE-A-2026-20587.pdf), 5 October 2026, Article 11; [catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>)/[draft formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>) 0.1.0, 9 October 2026, §§6.1–6.10/5.1–5.9; [SendInvoice WSDL](<../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), 13 October 2026, binding/ports. | Public access/operation boundary; no supplied enrolment contract or proven build. Conflicts remain in [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md). |
| REF-PRODUCT | [PRD227](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md), repository draft, FR11; [SPEC014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md), 20 October 2026, SPC-01–08; [PRD221](../../prds/PRD-SEI-221-operator-readiness-regulatory-governance.md), 6 October 2026, readiness domains/FR20. | Shared/country separation, proposed routing and operator scope; no implementation or launch approval. |
