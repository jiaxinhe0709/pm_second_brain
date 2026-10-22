---
id: SPEC-SEI-018
title: Customer Onboarding Solution Summary
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-21
updated: 2026-10-21
reviewers: []
related:
  - SPEC-SEI-002
  - SPEC-SEI-019
  - SPEC-SEI-020
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-107
  - PRD-SEI-222
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

# Customer Onboarding Solution Summary

[Logical Feature Specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) · [API Reuse Assessment](SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md) · [Feature landing page](README.md)

## Revision overview

This is the summary companion to [SPEC-SEI-019](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md), based on [SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md). The split gives stakeholders a shorter end-to-end view and gives Engineering and QA a separate behaviour specification. Detailed fields and technical analysis remain linked supporting material.

The predecessor is unchanged. Business scope, phase boundaries, ONB/OFR IDs and safety controls are retained. The split does not approve implementation, close existing decisions or change the publication source. The stable onboarding page still selects SPEC-SEI-002. The [proposed page hierarchy](README.md#confluence-presentation) keeps summary, logical behaviour and API design as separate views. Publication and the final delivery-feature breakdown remain pending.

## 1 Purpose

Help a Spanish business set up, connect, confirm or extend supported e-invoicing functions through Sage. A direct customer or authorised accountant must understand what is ready, what is active and who must act next. An existing customer should complete only missing or invalidated work.

Directors and Product can review the outcome, boundaries and material decisions here. Engineering and QA use the [logical specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) for activity requirements and acceptance, and the [API assessment](SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md) for existing coverage, Spain tailoring by platform and reuse gaps. The [feature landing page](README.md) links the canonical PRDs.

Customer onboarding is the Master Feature journey for this review. This grouping does not establish new delivery-feature boundaries or a deployed capability. **Confirmed** identifies a sourced fact or recorded ownership direction. The solution behaviour remains **proposed**; **open** decisions require the named owner's evidence and approval.

## 2 Terms used

Use the [shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). These distinctions are essential to the summary.

| Term | Meaning |
|---|---|
| Represented business | The business whose setup or invoice function is affected. It is separate from the authenticated caller. |
| Authority | Current permission for a specific action for that business. A login, client relationship or certificate alone is insufficient. |
| Readiness | An evidenced check result for a stated function, actor and environment, with limitations and recheck conditions. |
| Activation | An evidenced start of authorised use for the exact function, direction and scope. Connection and readiness are separate results. |
| Recovery | Correct or establish the result of affected work, then return to its blocked check. |

## 3 Master Feature purpose and scope

The journey starts when an authorised actor requests a setup outcome for one business or a supported set of independent businesses. It ends with a recorded result for each requested function, including any remaining action and its owner. These entry situations share the activity model in section 7.

| Customer situation | Intended outcome |
|---|---|
| First-time setup | Select a supported option and establish the required checks. |
| Existing public service | Establish Sage access for selected functions without assuming new public enrolment (SPFE-S03). |
| Existing private provider | Keep the provider and connect its qualified account to Sage. |
| Public and private services | Qualify the function assigned to each service and return independent results. |
| Existing Sage setup | Confirm unchanged valid setup or add only requested functions. |
| Platform change | Change supported future work at an authorised boundary; preserve earlier obligations. |
| Existing B2G use | Assess B2B separately and retain the B2G setup. |
| Unsupported or uncertain setup | Explain the limitation or missing evidence and give an owned next action. |

The logical specification defines these situations as ONB-S01–08. Actor choice is independent: a direct customer, an accountant for one client, or an accountant portfolio can use the applicable journey. A single delegated client does not require a batch.

**Phase 1** returns public readiness. **Later phases** may qualify private setup and route activation. Private A to Private B changes remain disabled pending the shared routing decision. A summary or diagram cannot enable them.

| Outcome or endpoint | Meaning |
|---|---|
| Selected work complete | Each function has a supported, evidenced result. Public readiness and later activation retain separate meanings. |
| Final rejection or withdrawal | The requested work has a recorded final disposition. Existing service remains subject to its own state and obligations. |
| Cancellation complete | Safe pending work is stopped and every possible external effect has sufficient evidence-backed resolution for closure. |
| Action pending or outcome unknown | Not an endpoint. Retain the owner and recovery path; do not infer completion from escalation. |

Invoice creation, sending, retrieval, status reporting and full offboarding belong to their owning features. Their dependencies remain in scope for setup checks and handoffs. Physical APIs, deployment design and detailed field mappings are supporting engineering material.

## 4 Parties and responsibility boundary

| Party | Responsibility and handoff |
|---|---|
| Business or authorised accountant | Select the requested outcome and supported option; provide missing information or a purpose-specific decision. |
| ERP or product | Present choices and client actions; show the current permitted per-function result through the Global API. |
| E-Invoice Service | Own setup and recovery coordination. This recorded direction does not establish a separate onboarding service. |
| Identity, trust and connection owners | Supply qualified identity, authority, protected access and connection evidence. Keep their decisions separate. |
| Routing and invoice-operation owners | Qualify activation, preserve invoice origins and apply runtime checks for their own operations. |
| Provider or public connector | Execute only the selected qualified contract and provide operation evidence. |
| Operations | Own assigned unresolved work and evidence-backed manual action; assignment alone does not prove success. |

## 5 Key open solution decisions

The full [decision record in SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md#5-key-decisions-and-risks) remains the reference for existing wording, ownership and gates. These groups identify the decisions that can change the end-to-end journey.

| References | Impact | Owner and gate |
|---|---|---|
| ONB-Q01/02 and OFR-Q01/02 | Supported observations, public/private combinations, receiving reachability and exact recovery checkpoints. | Integration, Routing, Product and Operations; selected-provider pilot. |
| ONB-Q04/09 | Actual ERP/API results, customer inputs, scheduling, timezones and receiving-history coverage. | API, ERP Product, Routing and Receiving; contract review and cohort pilot. |
| ONB-Q06/07 and OFR-Q04 | Protected-source operations, accepted representation evidence, eligible approvers and action channel. | Trust, Identity, Spain Compliance and Security; selected-function and delegated pilots. |
| ONB-Q08 | Batch permissions, limits, fair processing and access-filtered progress. | Accountant Product, API, Identity and Operations; portfolio pilot. |
| ONB-Q05 and OFR-Q03 | Existing implementation coverage and gaps within the E-Invoice Service. | Service owner and Architecture; before build. |
| Unnumbered transition and operational decisions | Operator approval, publication sequence, historical access, safe retry budgets and manual closure evidence. | Provider, Routing, Compliance and Operations; before the affected path is enabled. |

## 6 End to end workflow

Capture the request, verify the represented business and acting party, then assess existing setup. Run the required public or private branch for each function. Missing approval enters ONB-12; supported portfolio intake enters ONB-13. Unknown effects enter ONB-08 and resume the exact affected check after resolution.

![Set up, connect or review e-invoicing through Sage](../../assets/diagrams/onboarding-scenario-selection-process.svg)

Figure 1. Onboarding paths for ONB-S01–08. [Editable Draw.io](../../assets/diagrams/onboarding-scenario-selection-process.drawio) · [PNG](../../assets/diagrams/onboarding-scenario-selection-process.png).

Solid arrows show work or a result. Dashed arrows show selected or conditional work. The columns identify paths, not service boundaries. A combined setup can use several branches. Recovery and approval remain conditional activities, not alternative delivery routes.

## 7 Master Feature lifecycle

| Activity | Outcome | Accountable party or handoff |
|---|---|---|
| ONB-13 Manage portfolio batch | Saved receipt and independent item mapping, where batch mode applies. | E-Invoice Service; current per-client permission. |
| ONB-01 Capture requested functions | Scoped request recorded or duplicate/conflict returned. | Product to E-Invoice Service. |
| ONB-02 Check business identity and authority | Separate identity and action-authority findings. | Identity and authority owners. |
| ONB-10 Assess current setup | Plan for missing, unchanged, stale or unsupported work. | E-Invoice Service with evidence owners. |
| ONB-12 Coordinate client approval and evidence | Missing decision resolved or owned client action retained. | Eligible approver and evidence owner. |
| ONB-03 Assess prerequisites | Required access and trust checks established. | Policy, Identity and trust owners. |
| ONB-04 Publish public readiness | Evidenced result for each selected public function. | E-Invoice Service to product. |
| ONB-05 Configure private choice | Explicit supported choice and missing configuration recorded. | Customer, product and connection owner. |
| ONB-06 Prove private readiness | Selected function and required external state qualified. | Connection and provider owners. |
| ONB-07 Cut over new traffic | Authorised future-work boundary evidenced. | Routing owner. |
| ONB-08 Reconcile and recover | Original effect resolved or kept on an owned hold. | Operation owner and Operations. |
| ONB-09 Preserve and release | Earlier invoice access retained; dependency release separately gated. | Routing, records and Operations. |
| ONB-11 Return results and required actions | Current permitted results, limitations and next actions. | E-Invoice Service through Global API to product. |

The [logical activity blocks](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md#6-feature-activities) are authoritative for behaviour. The order above is a reading route: approval and recovery can interrupt a check, and independent items can proceed separately.

## 8 Cross cutting solution considerations

This design is intended for Spain. Shared work-item, approval, portfolio and recovery patterns are reuse candidates. Identity, representation, trust, provider operations and route rules need country bindings. Spain rules must not become another country's defaults.

Actual implementation coverage remains unknown. The E-Invoice Service, Identity, trust and Routing owners must identify the source build, retained behaviour, local changes, gaps and qualification evidence. Existing Tax/certificate capability is a selected-purpose reuse candidate. Existing DTS is the preferred transformation candidate where relevant; its build, contracts, mappings, rule packs and operations require qualification under [SPEC-SEI-008](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md). Onboarding does not prove either capability ready.

## 9 Dependencies and risks

| Dependency or risk | Consequence and response |
|---|---|
| Authority or trust evidence is missing | Hold dependent work and return the eligible action owner. |
| An external change has an unknown outcome | Preserve the original operation and check actual state before repetition. |
| A receiving change affects reachability | Routing decides hold or continuation from evidence, even before local activation. |
| Earlier invoices still need the previous path | Retain required access until the historical-continuity gate passes. |
| Capacity and service targets are unqualified | Set measurable limits and objectives from approved contracts and pilot evidence. |

## 10 Features within this Master Feature

For this pilot, one [Logical Feature Specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) covers ONB-01–13 and integrated OFR-01–08 recovery. Public setup, private setup, approval and portfolio processing are activity groups; this split does not approve them as separate delivery Features.

Shared certificate, connection/routing, public-execution and invoice-operation specs retain their existing boundaries. Section 7 of the logical specification links those handoffs. Product and Engineering can agree a finer delivery-feature breakdown if independent review or ownership requires it.

## 12 Assurance and completion checks

Before approval, confirm that ONB-S01–08 and each applicable actor path have acceptance coverage; each enabled function has qualified authority, trust and operation evidence; and each unresolved decision has an owner and gate. Test unknown effects, correction, cancellation, concurrent changes, portfolio visibility and historical continuity.

The [logical specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md#7-traceability-and-supporting-artefacts) defines the acceptance route. Neither document establishes production readiness.

## REF Source references

| REF ID | Source and version | Exact location | Supported claim and limit |
|---|---|---|---|
| REF-BASE | [SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md), snapshot 20 October 2026 | Parts 1–4 and REF | Predecessor scope, IDs, recorded ownership direction, proposed behaviour and open gates. Not implementation evidence. |
| REF-PRODUCT | [PRD-SEI-101](../../prds/PRD-SEI-101-public-platform-onboarding.md), [104](../../prds/PRD-SEI-104-accountant-and-single-client-onboarding.md), [107](../../prds/PRD-SEI-107-public-onboarding-failure-recovery.md), [222](../../prds/PRD-SEI-222-customer-onboarding-entry-point-migration.md) | Decision summaries, scope and functional requirements | Canonical product scope; unresolved differences require an owner decision. |
| REF-COUNTRY | [PRD-SEI-227](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md) | Shared platform and country-pack direction | Reuse direction; not deployment qualification. |
| SPFE-S03 | [Original catalogue](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | Sections 6.1–6.10, pp. 9–20 | Supplied public operations; no onboarding enrolment contract in this bundle. Supports the S02 boundary. Does not prove live availability. |
| REF-EVIDENCE | [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md) and [logical REF](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md#ref-source-references) | Source register, exact contracts and open conflicts | Original-source route for Spain-dependent rules and acceptance. The guide is a reading aid. |
