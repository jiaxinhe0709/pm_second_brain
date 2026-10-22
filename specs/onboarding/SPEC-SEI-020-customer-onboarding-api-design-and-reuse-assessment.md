---
id: SPEC-SEI-020
title: Customer Onboarding API Reuse Assessment
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-21
updated: 2026-10-22
reviewers: []
related:
  - SPEC-SEI-002
  - SPEC-SEI-018
  - SPEC-SEI-019
  - SPEC-SEI-001
  - SPEC-SEI-008
  - SPEC-SEI-011
  - SPEC-SEI-013
  - SPEC-SEI-014
  - SPEC-SEI-016
  - PRD-SEI-227
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# Customer Onboarding API Reuse Assessment

[Solution Summary](SPEC-SEI-018-customer-onboarding-solution-summary.md) · [Logical Feature Specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) · [Feature landing page](README.md)

## Revision overview

This companion to [SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md) assesses existing FR capabilities, Spain changes, product impact and coverage gaps by public and private platform. Business requirements, phase gates and ONB/OFR meanings remain in SPEC-SEI-019. The predecessor, source contracts and publication selection remain unchanged.

## 1 Engineering decision summary

**Agreed direction, 22 October 2026: reuse the existing FR APIs and tailor Spain through the country pack.** API design and call sequences are outside this assessment. Engineering must establish whether each Spain difference needs configuration, a country/provider binding, a shared capability change or a contract extension. REF-REUSE; REF-COUNTRY.

The intended Spain use is to confirm or establish selected public/private functions for a business through Sage. Phase 1 remains public readiness. Later private setup and activation retain their existing gates; Private A to Private B remains disabled. REF-LOGICAL sections 3 and 6.

### Product impact by delivery scope

| Scope | Existing reuse starting point | Spain change or consideration | Product integration impact |
|---|---|---|---|
| Public platform MVP | Discovery and existing-connection inspection: API-01/02/04; Tax Service certificate capability is the intended supporting source. | Qualify Spain service availability, valid NIF, current authority, in-date suitable certificate and per-function readiness. Decide whether an internal connection record is needed; external public enrolment is not established. Section 4.1. | Keep the discovery/read approach. Use available business evidence; ask only for missing or invalid inputs. Show the affected function and action owner. Exact caller changes remain open. |
| Public platform nice-to-haves | Existing reads can support progress displays. Notification/reminder coverage is not supplied. | Assess existing progress, reminder and guidance capabilities before adding work. Section 4.2. | Optional richer guidance. Actionable failure/recovery information remains part of MVP. |
| Private platforms | API-01–05 cover discovery and connection resource operations. | Qualify each selected provider's new/existing account setup, Spain identifiers, credentials, terms, sending/receiving evidence and separate activation. Section 4.3. | Retain supported provider accounts. Request only provider-required information; show setup, readiness and activation separately. |
| Other shared changes | M2M access, resource references, create key, source statuses and errors appear in FR-01–05. | Qualify business/client isolation, country rules, result interpretation and recovery. Approval/portfolio coverage is unknown. Sections 2 and 5. | Reuse existing integration conventions where compatible. Assess actual required input/result changes before committing product work. |

**Evidence basis:** FR-01–05 document existing operations. Tax/Connections/AFL are implementation reuse candidates under SPEC-SEI-001. The shared onboarding flow is a proposed design pattern. Deployed builds, provider coverage and Spain compatibility remain **Unknown** until qualified.

## 2 Shared capabilities and reuse boundaries

Use the [shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). Shared behaviour is **Reusable with country binding** unless the evidence establishes otherwise. Spain rules are **Country-specific**. Implementation fitness remains **Unknown** until the owner supplies evidence.

| Capability already described | Reuse assessment and Spain consideration | Evidence / owner |
|---|---|---|
| M2M bearer authentication; optional `traceparent`/`tracestate`; JSON:API media type | Retain established integration conventions. Application authentication does not establish permission for a represented business or delegated client. | FR-01–05; Identity/API; GAP-03. |
| UUID `datasetId`, `accessPointId`, `connectionId` | Retain resource references. Qualify their tenant, ERP company, represented-business, provider and environment mappings. Do not assume the FR dataset is automatically the Tax Service dataset. | FR-01–05; API/Identity and Tax Service; GAP-01. |
| Status, error and metadata observations | Reuse available observations, subject to section 5's meaning and freshness checks. Credentials, raw sensitive errors and private keys stay outside product results and logs. | FR-02/04/05; REF-LOGICAL ONB-NFR01–03; GAP-05. |
| Approval, portfolio and recovery patterns | Reuse the proposed behaviour in SPEC-SEI-019. User fields, address arrays and a create key do not establish existing implementation coverage for these functions. | REF-LOGICAL ONB-08/12/13; E-Invoice Service and dependency owners; GAP-04/06/08. |
| Transformation for later invoice operations | Existing DTS remains the preferred reuse candidate where relevant. Onboarding connection APIs provide no evidence of format readiness. Selected builds, mappings, Spain rule packs and operations still need qualification. | [SPEC-SEI-008](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md); DTS/exchange owners. Outside onboarding API changes. |

## 3 Existing operation reuse assessment

The supplied method/path and operation IDs are the reuse baseline. Source contracts hold field definitions and examples.

| ID / source operation | Existing method and path | Existing documented capability | Public-platform reuse | Private-platform reuse |
|---|---|---|---|---|
| API-01 / FR-01 `Get-AccessPoints` | GET `/accesspoints` | Lists access-point IDs and names. | Candidate for offering the Spain public option. Country filtering, availability and capabilities are not established. | Candidate for offering qualified private providers. Listing alone does not establish provider support for Spain. |
| API-02 / FR-02 `Get-Dataset-AccessPoints` | GET `/datasets/{datasetId}/accesspoints` | Lists dataset access points, CONNECTED/DISCONNECTED and nullable `connectionId`. | Inspect existing Sage setup where applicable. Does not prove NIF, certificate, authority or public readiness. | Find existing Sage connections before new setup. Does not prove an account outside Sage is absent or receiving is active. |
| API-03 / FR-03 `New-AccessPoint-Connection` | POST `/connectors/{accessPointId}/datasets/{datasetId}/connect` | Creates an AccessPointConnection; requires company/user/address inputs and `Idempotency-Key`. | **Applicability open:** use only if public access needs an internal connection record. This is not evidence of an external public registration operation. | Reuse candidate for missing setup. FR address/usage/date rules need the Spain/provider assessment in section 5. Qualify whether it links an account, creates one or has other effects. |
| API-04 / FR-04 `Get-AccessPoint-Connection` | GET `/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/` | Reads connection/address details, source status, errors and creation/modification metadata. | Inspect internal setup where it exists. Certificate/readiness evidence still comes from its qualified owner. | Inspect setup and provider observations within their proven scope. A read is not automatically a fresh external readiness or original-operation check. |
| API-05 / FR-05 `Put-AccessPoint-Connection` | PUT `/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/` | Updates supported connection/address details; source describes date-limited address updates. | **Applicability open:** only for a confirmed internal configuration need. | Candidate for supported setup changes. It does not establish general migration, withdrawal, disconnection or route activation coverage. |

API-01/02/04 support assessment under ONB-10/11. API-03/05 may support missing setup under ONB-05/06 after their actual effects are qualified. Existing valid unchanged setup should need no mutation. REF-LOGICAL ONB-A15/38.

## 4 Spain tailoring by platform

### 4.1 Public platform MVP

Required behaviour: REF-LOGICAL ONB-02–04.

| Spain need | What we already have or can assess for reuse | What must change or be considered for Spain | Coverage / owner |
|---|---|---|---|
| Public service choice and existing setup | API-01/02/04 provide discovery and inspection. | Qualify the Spain public service choice and test/production availability. Establish whether public-only setup needs an internal connection; do not require API-03/05 merely because private setup uses them. | Unknown public binding; API/Integration and Product; GAP-02/06/08. |
| Valid business NIF | Existing business context can avoid repeated entry; Identity is the owning capability in REF-LOGICAL ONB-02. The five FR contracts do not prove NIF verification. | Qualify the business NIF and applicable NIF/NIE mapping, evidence source and correction owner. Keep the represented business separate from the certificate caller. A certificate or populated identifier cannot substitute for this check. | Country-specific identity rules; Identity/Spain Product; GAP-01/02/03/06; ONB-A03/25. |
| In-date, suitable certificate | **Intended source: existing Tax Service certificate capability**, following REF-TRUST. Reuse eligible protected material without another upload. REF-SAGE-CERT is the internal supporting reference. | Qualify actual Tax/Connections/AFL custody and lookup/readiness coverage. Establish current validity interval, revocation, subject, purpose, environment and evidence freshness. Expired/unsuitable material needs correction; unavailable/stale feedback remains unknown. Later protected authentication/signing needs separate qualification. | Existing implementation candidate; coverage Unknown. Tax Service, trust and Security; SPEC-SEI-001 G1/G9/G10; GAP-06/08; ONB-A22–25. |
| Direct/delegated action authority | M2M and request `user` are available, but do not establish effective authority. Reuse the Identity/authority capability where qualified. | Apply the selected Spain action's representation rules. Third-party recovery/consultation needs the registered-authority evidence in SPFE-S02 Article 11. Do not carry tax-only authority or certificate possession into public B2B use without validation. | Country-specific rules; Identity/Spain Compliance; GAP-03/06; ONB-SPFE-A03. |
| Per-function readiness and safe correction | Existing status/error observations can contribute; they do not cover all readiness findings. | Establish which owner supplies each finding and whether existing product results can express readiness, limitation, correction owner and recheck needs. NIF, certificate and authority remain independent. Failed/unknown prerequisites hold dependent work. | Result coverage Unknown; E-Invoice Service/API and dependency owners; GAP-05/06; ONB-A25/42. |
| Evidence of public access | Supplied public catalogue and formats describe invoice operations, not an onboarding enrolment command. | Qualify only supported access checks. Do not assume a customer-enrolment operation, invent its fields or use invoice submission/cancellation as an onboarding probe. Web-form access does not establish automated ERP access. | Spain technical binding; Integration/connector owner; SPFE-S02/S03/S08; ONB-SPFE-R02/03, ONB-A27. |

Public readiness does not activate a route or prove invoice exchange/reporting readiness. REF-LOGICAL ONB-04/11. NIF and certificate checks above also apply to private functions when the selected policy requires them; private credentials and signing arrangements remain provider-specific.

### 4.2 Public platform nice-to-haves

These are reuse candidates for optional product improvements, not added MVP commitments.

| Capability | Existing evidence | Spain consideration and owner |
|---|---|---|
| Progress notifications and renewal/remediation reminders | Reads exist; no notification or reminder contract is supplied. | Product and the owning service must confirm available events, expiry evidence, permissions and coverage before selecting work. Do not infer a new subscription API. |
| Richer setup guidance and prefilled correction | SPEC-SEI-019 ONB-R24 already requires use of qualified current information and only necessary input. | ERP Product can assess additional local guidance and help content. Core owned actions and safe recovery remain MVP requirements; richer presentation is optional. |

### 4.3 Private platforms

Assess **each selected provider**. No provider-specific Spain onboarding contract is supplied with FR-01–05, so provider support and local effects remain Unknown. Requirements stay in REF-LOGICAL ONB-05–09.

| Spain need / scenario | Existing reuse starting point | What must change or be considered for Spain | Coverage / owner |
|---|---|---|---|
| New private setup, ONB-S01 | API-01–05 cover provider discovery and connection resources. | Qualify supported provider, customer eligibility, required account/terms/entitlement information, Spain identity and actual setup effects. Apply the common FR differences in section 5. | Unknown provider binding; Product/API/Integration; GAP-02/03/08. |
| Keep an existing provider, ONB-S03 | API-02/04 can identify a known Sage connection; API-03 may support missing Sage setup. | Establish how to bind an existing external account. Distinguish account linking from account creation; avoid duplicate enrolment, subscription or credential replacement. An absent Sage connection does not prove no provider account exists. | Unknown linking coverage; provider/API owner; GAP-04/06/08; ONB-A13. |
| Provider credentials and trust | Existing Tax Service capability may provide reusable material for a qualified purpose; FR connection fields are not proof of credential fitness. | Confirm the provider's credential, authentication and signing arrangements separately. Tax-valid material cannot automatically satisfy private B2B use. A customer certificate upload is conditional on the selected arrangement. | Unknown selected-purpose coverage; trust/provider and Security; REF-TRUST G9/G10; ONB-A22/24. |
| Sending and receiving readiness | API-04 exposes connection/address status and errors. | Qualify evidence separately for sending, receiving and any required receiving destination. Determine which observation proves actual provider state and its freshness. Local CONNECTED or successful transport is insufficient by itself. | Unknown readiness/observation coverage; Integration/provider owner; GAP-05/06; ONB-06. |
| Public and private together, ONB-S04 | Connection resources can identify separate setups; common assessment can reuse valid evidence. | Qualify independent public access, public-copy and reporting dependencies for selected functions through their owning specs. Private setup cannot imply public readiness or create a second delivery executor. | Country/provider binding; Product/Integration and invoice-operation owners; ONB-A14. |
| Activation or supported platform change, ONB-S06 | API-03/05 offer setup changes; route capability is outside the supplied five contracts. | Confirm separate route authority, sending/receiving scope, effective boundary and earlier-invoice access under SPEC-SEI-014/016. A connection date edit is not a migration or rollback. Private A to Private B stays gated. | Unknown route implementation coverage; Routing/Receiving and Product; GAP-06/08; ONB-A05/08/16. |

For confirmed or extended existing Sage setup (ONB-S05), preserve valid matching references and recheck only affected evidence. Unsupported or unknown provider coverage returns an owned limitation (ONB-S08); it cannot force a provider switch. Existing B2G use is assessed independently for B2B (ONB-S07).

## 5 Common Spain changes and open evidence

### Country and contract differences

This is the shared tailoring list for the platform assessments above. **Required tailoring** identifies a known FR/Spain difference. It does not select an API design or prove a breaking change.

| What is documented today | Spain change or consideration | Assessment / owner |
|---|---|---|
| FR-03 requires company details, `user` and at least one `accessPointAddresses` entry. | Confirm which existing business inputs each Spain public/private path actually needs. Identify any conflict between required FR inputs and public-only setup before choosing configuration or contract work. | Applicability/extension open; Product/API; GAP-02/06. |
| FR-03/04/05 address types: `fr.siren`, `fr.sirensiret`, `fr.siren_suffix`, `fr.sirensiret_routing`; FR-05 groups by the same base SIREN. | **Required tailoring:** bind approved Spain business identifiers, provider addresses and grouping rules. Do not substitute NIF into an FR address type. Exact Spain contract representation remains open. | Country-specific rules; Identity/API/Integration; GAP-02. |
| FR-04/05 `mandateNumber` is described as generated per France opt-in form. | **Required tailoring:** keep the French opt-in meaning local. Identify the separate Spain authority/terms evidence; a connection field cannot create legal representation. | Country-specific authority binding; Identity/Compliance; GAP-02/03. |
| FR-03/04/05 `usage` permits SEND/EREPORTING; omitted/null permits all operations; at most one explicit value. | **Required tailoring:** assess Spain functions and permissions separately. The FR default cannot establish receiving, public reporting or signing permission. Whether the shared contract needs extension remains open. | Country/function binding; Product/API/Identity; GAP-02/05. |
| FR date format `YYYY/MM/DD`, next-day effective-date minimum and end-date constraints. | **Required tailoring:** qualify Spain/provider date rules, business timezone and requested versus confirmed start. Do not inherit France's next-day rule or treat a connection date as a statutory date or route activation. | Country/provider binding; Product/API/Routing; GAP-02/07; ONB-Q09. |
| Dataset status CONNECTED/DISCONNECTED; address states IN_PROGRESS/RETRYING/CONNECTED/DISCONNECTED/ERROR; `errorCode` and creation/modification metadata. | Qualify source meanings, observation freshness and what the product can already display. Preserve raw evidence; do not rename CONNECTED to overall READY/ACTIVE. | Coverage/mapping open; API/E-Invoice Service; GAP-05. |
| FR-03 requires `Idempotency-Key`; FR-05 declares no equivalent or expected-version parameter. Common errors include 401/403/429/5xx; 429 documents `Retry-After`. | Qualify duplicate scope, update safety, concurrent changes and recovery of original effects. An uncertain change cannot be repeated merely because a read fails or the HTTP method appears repeatable. Existing capability evidence is needed before any extension decision. | Shared safety coverage Unknown; API/Integration/Operations; GAP-04. |
| FR-01 declares path `datasetId` without a placeholder; address lengths differ between input (114) and output (50); FR-05 prose/schema differ on editable fields. | Resolve source inconsistencies with the FR owner before reuse. Do not treat these as Spain requirements or silently change existing clients. | Source clarification; API owner; GAP-07. |

France requests, source meanings and country rules must remain compatible. Country-pack changes may leave caller contracts unchanged. New required inputs or unsupported result meanings may require product or shared-contract work; that impact needs evidence rather than assumption. REF-COUNTRY; API-A07/13.

### Evidence gates

Existing gate IDs and ONB-Q/OFR-Q ownership remain. Each outcome must identify the reused capability, local change, remaining gap and evidence.

| Gate | Evidence needed to finish the assessment | Owner / existing reference |
|---|---|---|
| GAP-01 Dataset and resource identity | Actual tenant/business/client/environment mappings, including FR dataset versus Tax Service dataset, and access isolation. | API/Identity/Tax Service; ONB-Q01/04/08. |
| GAP-02 Country binding | Approved Spain rules and selected public/private provider coverage for section 5's differences; identify configuration, country/provider work or a possible contract gap. | Spain Product/Compliance/API/Integration; ONB-Q02/03/09. |
| GAP-03 Actor and authority | Existing direct/delegated access, firm/client checks, eligible approvals and accepted Spain authority evidence. | Identity/Security/Product; ONB-Q06/07/08. |
| GAP-04 Mutation safety | Actual create/update duplicate, concurrency, partial-effect and original-operation observation guarantees; safe recovery evidence. | API/Integration/Operations; OFR-Q01/02. |
| GAP-05 Result meanings | Source-to-function mapping, freshness and independent activation evidence; existing product result coverage and any gap. | API/E-Invoice Service/Routing; ONB-Q04/09. |
| GAP-06 Companion capabilities | Existing NIF evidence, Tax Service certificate lookup/readiness and protected-use coverage; case, approval, batch and route capabilities where selected scope needs them. | E-Invoice Service/Architecture/dependency owners; ONB-Q04–08, OFR-Q03/04; SPEC-SEI-001 G1/G9/G10. |
| GAP-07 Source inconsistencies | Owner-confirmed signatures, lengths, supported edits and actual validation/error behaviour in the FR source. | FR API owner; before build/client reuse. |
| GAP-08 Selected implementation qualification | Named reused build, retained behaviour, Spain/provider changes, known gaps, tests, monitoring and support ownership. | Architecture/API/Integration/Operations; ONB-Q05, OFR-Q03. |

## 6 Reuse assurance

These checks assess reuse against existing behaviour. Acceptance IDs retain their meanings; detailed scenarios remain in REF-LOGICAL.

| Check | Evidence required | Trace |
|---|---|---|
| API-A01 Resource access | Dataset/connection and client isolation, including removed relationships and safe denials. | ONB-A29/33/36; GAP-01/03. |
| API-A02 Unchanged setup | Valid matching setup is reused without create/update or a new route version. | ONB-A15/38. |
| API-A03 Create duplicates | Evidence of actual same-key replay, conflicting input, in-flight behaviour and duplicate window. | OFR-A04/06; GAP-04/08. |
| API-A04 Lost create response | Original operation can be recovered or held as unknown without another account/connection effect. | ONB-A06; OFR-A03/05. |
| API-A05 Update concurrency and uncertainty | Existing change controls prevent stale overwrite and blind repeat/rollback after possible effects. | ONB-A07/08; OFR-A15/17. |
| API-A06 Status interpretation | Resource status and HTTP completion do not become blanket readiness or activation. | ONB-A20/24/42; GAP-05. |
| API-A07 Country isolation | Spain identifier, authority, usage and date rules remain isolated from France and other countries. | ONB-A09/19/37; OFR-A10; GAP-02. |
| API-A08 Retry classification | Actual retry guarantees and provider guidance support the selected safe retry; failure/404 cannot establish absence. | OFR-A01/02/09/21; GAP-04. |
| API-A09 Missing companion coverage | An uncovered trust, authority, batch or route need remains a named gap with an owner, not presumed FR coverage. | ONB-A25/31/34/35; GAP-03/06. |
| API-A10 Public boundary | No invented public enrolment, test-invoice setup check or automatic activation; automated access is separately qualified. | ONB-SPFE-A01–03; OFR-SPFE-A01/02; SPFE-S02/S03/S08. |
| API-A11 Source correlation | All five operation IDs and exact paths match FR-01–05; reuse conclusions remain traceable to documented capabilities. | Source snapshots; GAP-07. |
| API-A12 Reuse and operations | Actual build, scope, local changes, gaps, operations and recovery evidence are recorded before enabling a function. | ONB-A19/21; OFR-A11/19; GAP-08. |
| API-A13 Existing product compatibility | FR regressions pass; any required Spain caller change is evidenced against the section 1 impact assessment. | REF-REUSE/COUNTRY; GAP-02/05/07/08. |
| API-A14 NIF and certificate result composition | Independent findings survive invalid NIF, expired/revoked/wrong-purpose material and unavailable Tax Service feedback. Verify protected-reference reuse and later-use rechecks. | ONB-A22–25; OFR-A20/21; REF-TRUST; GAP-03/05/06. |

## 7 Confluence presentation

Keep one engineering view alongside the summary and logical specification. Lead with platform-specific reuse and the common tailoring table. Link source contracts for schema detail. The [local preview](../../work/onboarding-api-review/index.html) reflects this focus. The [landing page](README.md#confluence-presentation) retains the publication boundary.

## REF Source references

FR files are supplied OpenAPI 3.1.0 snapshots, each declaring `info.version: 1.0.0`, reviewed 21 October 2026. No contract publication date, actual build version or completeness of the wider service is established. Source files remain unchanged. JSON names and paths below are exact; review excludes generated code samples and sample personal data.

| Source ID | Original file | Exact contract element | Supported claim and limit |
|---|---|---|---|
| REF-REUSE | Product/architecture review feedback recorded in [section 1](#1-engineering-decision-summary), 22 October 2026 | Direction to reuse FR APIs and tailor Spain through country packs; focus this assessment on existing coverage and Spain changes | Confirms the reuse choice. Does not approve exact schema changes, release priorities or production fitness. |
| REF-COUNTRY | [PRD-SEI-227](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md), canonical product proposal | Shared core and country-pack boundary; FR11; country-pack governance | Source design pattern for isolating local rules and preserving product contracts. Its broader proposal status is unchanged by this onboarding reuse decision. |
| FR-01 | [get-accesspoints.md](<../../context/FR API/Onboarding/get-accesspoints.md>) | `paths["/accesspoints"].get`, `GetAccessPointsResponse`, `AccessPointsResponse`, `parameters.datasetId` | Discovery path, response and signature inconsistency. No capability/readiness contract or Spain deployment proof. |
| FR-02 | [get-dataset-accesspoints.md](<../../context/FR API/Onboarding/get-dataset-accesspoints.md>) | `paths["/datasets/{datasetId}/accesspoints"].get`, `DatasetAccessPointsResponse` | Dataset listing, binary status and nullable connection reference; no proven original-operation recovery semantics. |
| FR-03 | [new-accesspoint-connection.md](<../../context/FR API/Onboarding/new-accesspoint-connection.md>) | `paths["/connectors/{accessPointId}/datasets/{datasetId}/connect"].post`; `Idempotency-Key` parameter; `AccessPointConnectionRequest/Response` | Create contract, required inputs, FR constraints and 201/address states. Key scope/retention/replay and external effects remain unqualified. |
| FR-04 | [get-accesspoint-connection.md](<../../context/FR API/Onboarding/get-accesspoint-connection.md>) | `paths["/connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/"].get`; `AccessPointConnectionResponse`; `Assigned-Keys` | Detail read, address states/metadata and FR mandate description. Does not establish fresh authoritative external observation or authority. |
| FR-05 | [put-accesspoint-connection.md](<../../context/FR API/Onboarding/put-accesspoint-connection.md>) | Same connection path `.put`; `PutAccessPointConnectionRequest`; `UpdateAccessPointConnectionRequest/Response` | Update actions, country grouping/date/usage rules and response shape. No supplied idempotency/version header; actual repeat/atomicity semantics need qualification. |
| REF-LOGICAL | [SPEC-SEI-019](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md), draft 21 October 2026 | ONB/OFR requirements, activity blocks, NFRs and acceptance | Canonical proposed behaviour for assessing reuse. This assessment does not change scope or allocate new APIs. |
| REF-BASE | [SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md), updated 20 October 2026 | Interaction/data inventories and decision/release-gate record | Original technical analysis and existing open decisions. Preserved unchanged; not implementation evidence. |
| REF-TRUST | [SPEC-SEI-001](../SPEC-SEI-001-certificate-management-solution-specification.md), draft, updated 20 October 2026 | Part 2 section 6 CERT-04/05; Part 3 INT-04/05; Part 4 G1/G9/G10 | Canonical proposed certificate validation, scoped readiness and source/operation qualification. Logical handoffs do not establish deployed Tax Service endpoints or B2B compatibility. |
| REF-SAGE-CERT | [Sage certificate management](https://confluence.sage.com/spaces/CCLD/pages/759615024/Sage+certificate+management), internal Confluence page; version/date unverified | CCLD page ID 759615024; exact content/section not verified because access was unavailable on 22 October 2026 | User-supplied internal certificate-management reference, also recorded in SPEC-SEI-001. Does not independently establish NIF validation, live Tax Service contracts, Spain legal requirements or public-platform acceptance. |
| SPFE-S02 | [BOE-A-2026-20587.pdf](../../context/BOE-A-2026-20587.pdf), Order HAC/1028/2026, published 5 October 2026 | Article 11(1)–(2); source baseline in REF-SPAIN | Certificate access and representation, including registered third-party recovery/consultation authority. Does not establish a Sage implementation or Tax Service contract. |
| SPFE-S03 | [Original public service catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | Sections 4.3, 5.1 and 6.1–6.10, pp. 8–20 | Public operation inventory and fault guidance; no supplied external onboarding registration command or blanket safe-retry guarantee. |
| SPFE-S08 | [Original input/output formats](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), 0.1.0, 9 October 2026, draft | Sections 5.1–5.9, pp. 8–15 | Operation/request/item response distinctions and supplied formats; no onboarding payload. Pending formats/conflicts remain gates. |
| REF-SPAIN | [SPEC-SEI-019 REF](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md#ref-source-references), [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md), [glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md) | Original legal/contract locators, shared conflicts and qualified identity/outcome terms | Existing Spain evidence route. This engineering assessment introduces no new legal rule; final BOE evidence retains its authority. |
