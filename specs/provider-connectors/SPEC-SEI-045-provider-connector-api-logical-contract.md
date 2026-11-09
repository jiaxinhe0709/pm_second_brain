---
id: SPEC-SEI-045
title: Provider Connector Shared API Interaction Contract
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-11-05
updated: 2026-11-09
reviewers: []
related:
  - SPEC-SEI-013
  - SPEC-SEI-014
  - SPEC-SEI-011
  - SPEC-SEI-017
  - GLO-SEI-001
  - RES-SEI-002
  - SPEC-SEI-044
  - SPEC-SEI-046
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Provider Connector Shared API Interaction Contract

[Summary](SPEC-SEI-044-provider-connector-architecture-summary.md) · [Logical contract](SPEC-SEI-045-provider-connector-api-logical-contract.md) · [Sequences and reuse](SPEC-SEI-046-provider-connector-api-sequences-and-reuse-assessment.md)

## 1 Required behaviour and acceptance

These proposed requirements apply to selected capabilities, not to every possible platform function. Owning-feature rules remain authoritative; this table defines the provider connector handoff.

| ID / condition and actor | Required result and safe next action | Acceptance evidence |
|---|---|---|
| CA-01 Feature requests an operation | Check caller, represented business, environment, role and qualified capability before execution. Deny unsupported or unauthorised combinations without an external call. | Wrong tenant, expired authority, wrong environment and unsupported operation produce no external effect. |
| CA-02 Feature requests an external mutation | Preserve operation identity, fixed input and original execution context. Repetition with the same identity/input follows the approved duplicate contract; changed input conflicts. | Concurrent duplicates produce one authorised execution owner; key reuse with changed payload is rejected. |
| CA-03 Platform returns a response or the call times out | Preserve source code, correlation and protected evidence. Return the actual known result or an unknown outcome. Reconcile a possible external effect before retry or reassignment. | Lost response after external acceptance does not cause blind resend or automatic platform failover. |
| CA-04 Platform supplies an invoice or event | Authenticate the source and hand off durable content/evidence to its feature owner. Advance acquisition progress only after the agreed durable handoff. | Duplicate notification or failed handoff causes no lost invoice and no duplicate business processing. |
| CA-05 Connection, credential or contract changes | Apply approved changes to future work. Retain original context for pending actions; revoked authority can block further external access. | Pending work is not silently rebound to another provider, role, environment or customer. |

## 2 Shared API usage and execution context

Products, authorised providers and Provider Connectors use the same Sage API contract under [044 CA-ARCH01/02](SPEC-SEI-044-provider-connector-architecture-summary.md#4-ref-source-references). This section defines logical information needed for those interactions; it does not define another Connector API. Reuse actual shared-API fields and operations. SPEC013 GPA-Q02/Q05 still govern exact wire schemas, versions and duplicate handling.

| Consumer / interaction | Shared contract use and boundary |
|---|---|
| Product → Sage | Request setup or invoice work; read permitted saved results. Use the customer's scope and operation identity. |
| Authorised provider → Sage | Submit or retrieve assigned invoices/results under the selected provider integration mode. Partner status alone does not grant all product or connector permissions. |
| Provider Connector → Sage | Use the common contract to obtain permitted work/content and submit source invoices, statuses or execution evidence. Work may arrive through notifications. |
| Provider Connector → external platform | Use that platform's separate external contract. Do not forward caller input to arbitrary endpoints. |

Caller permissions, tenant isolation and one executor per exchange action remain CA-01–05 / SPEC013 controls. Consumer-role isolation must be tested as part of CS02; sharing an API does not grant interchangeable permissions.

| Message | Minimum logical information |
|---|---|
| Accepted work / execution context | Feature operation ID; exchange-action ID where applicable; authenticated-caller reference; tenant and represented-business reference; country/environment; integration role; connection and contract-profile version; capability/operation; input reference and digest; correlation; protected credential reference. |
| Result submitted through shared API | Original operation/action and platform context; attempt identity; source request/reference; observed time; known/pending/unknown/denied-or-unsupported classification; raw source code and protected evidence reference; recovery responsibility and permitted next action. Classifications are logical, not new wire enums. |
| Source invoice/event submitted through shared API | Authenticated platform/account context; stable source event/document identity where available; original bytes or protected reference and digest; source and observed timestamps; continuation/checkpoint context where applicable. |

The owning feature determines payload readiness and business meaning. The provider connector applies the approved transport envelope and preserves external responses. DTS remains the preferred transformation candidate upstream; provider connector transport does not introduce a parallel invoice mapper, route engine or invoice store.

## 3 Capability matrix

Record support per platform, role, environment and contract version. Use **qualified**, **contract evidence only**, **unknown** or **excluded**; no provider connector-wide ready flag may imply all functions are supported.

| Capability | Private direct-provider binding | SPFE binding |
|---|---|---|
| Setup/access check | Account linking, token exchange or registration only where the provider contract requires it. Unknown for the complete six-provider set. | Qualify credentials and access for each operation. No external enrolment API is established by the supplied baseline. CA-SPFE; onboarding 038–040. |
| Send | Qualify submission, acknowledgements, duplicate behaviour and query/recovery. | `SendInvoice`; CA-SPFE / SPFE-S16. Feature owns delivery/public-copy meaning. |
| Receive/query/download | Qualify polling or push, pagination, capture and replay. | `GetRegisteredInvoice`, `GetInvoices`, `DownloadInvoicesByID`, `DownloadInvoicesByLOC`; SPFE-S12–S15. |
| Lifecycle/event reporting | Qualify source codes, event direction and reporting/query operations separately. | `CustomerInvoiceEvents`, `SupplierInvoiceEvents`; SPFE-S11/S17. Lifecycle owns interpretation. |
| Cancellation/exit | Qualify cancellation and disconnection independently. | `CancelInvoice` is not proof of customer offboarding or deletion; SPFE-S10. |
| PRE validation | Include only if supported and selected. | `ValidationInvoice`, direct SOAP rather than ebMS/MIME; SPFE-S23. Missing imported business schemas remain open. |

## 4 Scenario coverage

This is the authoritative provider connector scenario list. CA-01–05 define shared controls; the checks below apply them to observable cases. Feature-specific invoice, onboarding and lifecycle scenarios stay in their owning folders. These are acceptance checks to execute, not passed test results.

| Case / trigger | Expected evidence and safe next action | Control / sequence |
|---|---|---|
| CS01 Setup: existing private-provider customer, new private-provider customer or public access check | **Existing private customer:** link the existing provider account, verify Sage access and reuse valid setup; do not create a duplicate account or repeat completed registration. **New private customer:** support the provider-required account setup/registration and authorisation, including an external handoff where required; return pending actions until readiness is established. Test both paths for each of the six private providers. Return setup evidence to onboarding; neither path silently activates a route. **SPFE:** check operation access without inventing enrolment. | CA-01/02; operation A/B; onboarding ONB-S01/S03; CA-SPFE |
| CS02 Wrong scope, missing authority or unsupported capability/version | No external call; reason and responsible owner returned. Check wrong tenant, business, country, environment and customer-provider versus peer role separately. Test product, provider and connector caller permissions independently against the shared contract. | CA-01; operation A |
| CS03 Duplicate/concurrent request or identity reused with changed payload | Same identity/input correlates to the original operation; changed input conflicts. Test concurrent claims and worker restart before sending. | CA-02; operation A |
| CS04 Known external acceptance | Evidence and original action references persist; feature receives only the result proved by that acknowledgement. Technical acceptance does not become buyer acceptance. | CA-02/03; operation B |
| CS05 Platform rejection, malformed response or transport fault | Original fault/evidence retained with its level. A parser failure cannot be reported as invoice rejection; possible effects remain uncertain. | CA-03; operation B/C; SPEC011 public fault checks |
| CS06 Timeout or lost response after possible external acceptance | No blind resend. Qualified query reconciles the original identity; unsupported query or unresolved result holds work for its recovery owner. | CA-03; operation C |
| CS07 Save/worker failure before call or after response | Failed intent save prevents sending. Crash after external call or failed evidence save recovers the original attempt; no fresh mutation just to rebuild local evidence. | CA-02/03; operation A/C |
| CS08 Poll returns pages, empty result, duplicate item or expired cursor | Covered progress follows durable capture. Empty result is separate from outage; gaps/expired cursors require qualified rescan or owner action before claiming complete coverage. | CA-04; acquisition A–C |
| CS09 Valid, unauthenticated or replayed push | Check source/account scope and replay identity before handoff. Invalid source rejected; valid repeat cannot create duplicate business processing. SPFE push remains unqualified. | CA-01/04; acquisition A/C |
| CS10 Failure between inbound capture and acknowledgement/checkpoint | Restart replays the same saved item; committed capture deduplicates it. External acknowledgement follows the selected platform contract without losing captured work. | CA-04; acquisition B/C |
| CS11 Credential expiry, rotation or authority revocation during work | New external calls recheck effective permission. Rotation cannot change represented business/environment; blocked pending work retains its history and recovery owner. | CA-01/05; operation A/C |
| CS12 Route/provider/profile change with pending actions | New work uses only the approved new context. Earlier actions retain original context; unknown effects cannot trigger automatic failover or an alternative executor. | CA-03/05; operation C; SPEC014 |
| CS13 Batch partial result or delivery succeeds while public-copy/reporting fails | Per-item and per-action evidence remain independent. Recover only unresolved work under its original identity; a batch receipt is not whole-batch external success. | CA-02/03; operation B/C; sending/lifecycle owners |
| CS14 Wrong country rule pack, payload profile or unqualified mapping | Reject or hold before sending; country-rule isolation and DTS mapping qualification have recorded results for the selected profile. | CA-01; operation A; SPEC008/014 |
| CS15 Late or out-of-order response/event after recovery | Correlate to the original attempt/action; retain source and observation times. Stale evidence cannot overwrite newer execution ownership or directly regress lifecycle meaning. | CA-03/04; operation C, acquisition C; lifecycle owner |
| CS16 Rate limit, outage, payload limit or contract upgrade | Enforce qualified limits and backpressure. Retry timing does not override unknown-outcome checks; changed schema/version stays disabled until compatibility and recovery evidence pass. | CA-01/03/05; operation A/C; SPEC013 GPA-Q09/Q12 |

For each enabled binding, record case ID, operation/role/environment/contract version, build, source contract, result and evidence link. Mark cases **applicable**, **excluded with reason** or **blocked by evidence** before execution. Vary the feature operation across setup, send, acquisition, lifecycle and exit where selected. Add provider-specific cases from its error, paging, duplicate and trust contracts; the shared list alone cannot prove exhaustive platform coverage.

## 5 REF Source references

CA-01–05 and the logical message fields are proposed Sage controls, derived from [SPEC013](../SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md), GPA-Q03–06/Q10, and [SPEC014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md), SPC-01–08. They are not external legal requirements. CA-H01 and CA-SPFE are defined with source limits in [044 REF](SPEC-SEI-044-provider-connector-architecture-summary.md#4-ref-source-references).

| Source IDs / version | Original contracts and exact locator | Supported claim / limit |
|---|---|---|
| SPFE-S12–S15 / PRE 29 October 2026 | [DownloadInvoicesByID](<../../context/WSDL servicios web - PRE_29_10_2026/DownloadInvoicesByID.wsdl>), [DownloadInvoicesByLOC](<../../context/WSDL servicios web - PRE_29_10_2026/DownloadInvoicesByLOC.wsdl>), [GetInvoices](<../../context/WSDL servicios web - PRE_29_10_2026/GetInvoices.wsdl>), [GetRegisteredInvoice](<../../context/WSDL servicios web - PRE_29_10_2026/GetRegisteredInvoice.wsdl>), each `portType/operation`, `documentation`, `binding`, `service` | Query/download operations and transport; not complete filters, continuation rules or tested runtime coverage. |
| SPFE-S10/S11/S17 / same release | [CancelInvoice](<../../context/WSDL servicios web - PRE_29_10_2026/CancelInvoice.wsdl>), [CustomerInvoiceEvents](<../../context/WSDL servicios web - PRE_29_10_2026/CustomerInvoiceEvents.wsdl>), [SupplierInvoiceEvents](<../../context/WSDL servicios web - PRE_29_10_2026/SupplierInvoiceEvents.wsdl>), same elements | Named cancellation/event operations; not business state interpretation, offboarding or replay guarantees. |

Transport detail remains authoritative in [SPEC011, SPFE source contract binding](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-source-contract-binding). Acceptance of a selected SPFE capability must include its cited contract checks; passing CA-01–05 alone cannot qualify it.
