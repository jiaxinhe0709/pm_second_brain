---
id: SPEC-SEI-019
title: Customer Onboarding Logical Feature Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-21
updated: 2026-10-21
reviewers: []
related:
  - SPEC-SEI-002
  - SPEC-SEI-018
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-107
  - PRD-SEI-222
  - PRD-SEI-225
  - PRD-SEI-227
  - PRD-SEI-231
  - SPEC-SEI-001
  - SPEC-SEI-008
  - SPEC-SEI-011
  - SPEC-SEI-013
  - SPEC-SEI-014
  - SPEC-SEI-016
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

# Customer Onboarding Logical Feature Specification

## Revision overview

This separate draft is based on [SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md) and accompanies [SPEC-SEI-018 Solution Summary](SPEC-SEI-018-customer-onboarding-solution-summary.md). It follows the Logical Feature Specification template: scope, shared rules, quality requirements, activity blocks and supporting references.

The predecessor remains unchanged. ONB-S01–08, ONB-01–13, OFR-01–08 and existing requirement and acceptance IDs retain their meanings. Required behaviour is stated here; detailed physical proposals, field inventories and existing decision records stay linked to the predecessor. The split does not change phase gates, enable a provider, approve an architecture or establish production readiness.

Open decisions retain their existing owners and gates. The stable Confluence page `923861390` still selects SPEC-SEI-002; neither companion is selected for publication.

## 1 Purpose and authority

Define how an authorised customer or accountant establishes or confirms selected e-invoicing functions through Sage. For each activity, identify required information, observable results, important failures and the safe next action.

This is a **proposed logical design**. Product scope comes from REF-PRODUCT. Exact Spain public rules and supplied contract facts come from the SPFE source IDs in [REF](#ref-source-references). Internal states, coordination and qualification controls are Sage design proposals. Recorded ownership direction is identified in section 7. Proposed source-derived refinements remain subject to Product review; a document split cannot approve them.

## 2 Terms used

Use the [shared e-invoicing glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). Terms below retain its meanings.

| Term | Meaning in this feature |
|---|---|
| Represented business | The business whose setup is affected. It is separate from the authenticated caller. |
| Authority | Current permission for the exact action, business, scope and period. Product access and a client relationship are separate. |
| Readiness | An evidenced capability-check result for an actor, business, environment and selected profile, with limitations and recheck conditions. |
| Route and cutover | The selected platform/connection for a direction and scope; the authorised boundary for changing future work. |
| Entry point | A published receiving destination. A local configuration does not prove external reachability. |
| Reconciliation | Establish what happened to the original operation from reliable evidence before deciding the next action. |
| Idempotency | Repetition of the same logical request adds no effect within the qualified contract's scope and duplicate window. |
| Approval evidence | A purpose-specific decision bound to the business, scope and request or plan version. It is separate from effective authority. |
| Batch receipt | Saved acceptance of a manifest of independently scoped requests. It does not establish client readiness. |

## 3 Scope

### 3.1 In scope

Assess the requested outcome and current setup; verify identity and action authority; establish conditional access and trust; confirm public readiness; configure supported private connections; coordinate separately authorised activation; preserve earlier invoice obligations; and return per-function results. Missing approval, portfolio processing, correction, cancellation and recovery use the same activity controls.

These scenarios are authoritative for entry selection. Apply actor and processing mode separately.

| ID | Starting situation | Required plan and result |
|---|---|---|
| ONB-S01 | No established e-invoicing setup | Present qualified choices, establish missing prerequisites and return results for selected functions. |
| ONB-S02 | Existing public service outside Sage | Establish Sage access and qualified function evidence; do not infer external registration or active exchange. |
| ONB-S03 | Existing private provider retained | Bind the existing account and add only missing Sage setup. An initial Sage route still needs separate authority where required. |
| ONB-S04 | Public and private services used together | Plan functions separately, preserve valid independent results and identify dependencies. Do not create overlapping delivery executors. |
| ONB-S05 | Existing Sage setup confirmed or extended | Return valid unchanged references without mutation; recheck stale evidence or add only the requested functions. |
| ONB-S06 | Supported platform change requested | Qualify the new plan and future-work boundary. Preserve earlier invoice context. Keep unapproved transitions blocked. |
| ONB-S07 | B2G service used before B2B setup | Assess B2B access independently and retain the existing B2G service. |
| ONB-S08 | Provider/function unsupported or setup unknown | Return the precise limitation, missing evidence and owner. Do not force a provider change or infer absence. |

### 3.2 Out of scope

Invoice issuance, delivery, retrieval, lifecycle reporting and full exit belong to their owning features. Onboarding supplies their setup evidence and checks relevant dependencies. Physical endpoints, schemas, storage design, deployment and detailed field mapping are outside this logical specification; section 7 links their supporting analysis.

### 3.3 Outcomes and end states

Return a recorded outcome for each function: readiness, independently evidenced activation, unchanged setup, a limitation or an owned action. Readiness, activation, request completion, approval-request status and batch coordination remain separate dimensions.

Pending prerequisites, retry waits, unknown external effects and unresolved manual cases remain open work. Cancellation is final only after the ONB-08 closure gate passes. No whole-customer ONBOARDED flag substitutes for these results.

### 3.4 Assumptions and dependencies

| Dependency | Owner and boundary |
|---|---|
| Identity, direct/delegated access and evidence | Identity and Product; current per-business action checks. |
| Protected credentials and operations | SPEC-SEI-001 owner; qualify the actual Tax/Connections/AFL source and selected purpose. |
| Connections, route versions and historical context | SPEC-SEI-014 owner; independent configuration, readiness and route gates. |
| Global API and public execution | SPEC-SEI-013 and SPEC-SEI-011 owners; qualified contracts rather than invented setup operations. |
| Receiving history and progress | SPEC-SEI-016 owner; available history, source-date meaning, authority and saved checkpoints. |
| Existing implementation coverage | E-Invoice Service and Architecture; build, contract, local-change and gap evidence under ONB-Q05/OFR-Q03. |

### 3.5 Decisions and open questions

Use the existing [decision record](../SPEC-SEI-002-onboarding-solution-specification.md#5-key-decisions-and-risks); do not create parallel decision statuses. ONB-Q01–09 and OFR-Q01–04 cover discovery, combinations, scope, API/ERP fields, implementation, protected operations, approval, portfolio limits and recovery. Unnumbered decisions cover operator/transition sequencing, historical access, retry budgets, manual evidence, retention and service objectives. Missing qualification blocks only dependent work.

## 4 Feature wide functional requirements and rules

The IDs below preserve the predecessor's controls. Activity blocks reference them and add activity-specific behaviour. Source scope is REF-PRODUCT/REF-BASE unless a SPFE source ID is given. No draft design becomes approved through this restatement.

| ID | Requirement or rule | Applies to |
|---|---|---|
| ONB-R01 | Before any external change, Sage must resolve the authorised tenant, represented business, environment and exact function/scope. | All protected work. |
| ONB-R02 | Sage must verify direct or per-client delegated authority for each action and recheck it before activation or another protected execution. | Identity, setup, activation and use. |
| ONB-R03 | Sage must keep readiness dimensions and their evidence separate. A certificate check applies only where the selected policy requires it. | Public/private readiness and results. |
| ONB-R04 | Sage must isolate each client's result, correction, cancellation and failure; other safe clients can continue. | Portfolio processing. |
| ONB-R10 | Sage must retain who requested, decided, changed, observed, corrected or overrode the work, with scope, time and source. | All activities. |
| ONB-R12 | Sage must reuse only matching valid evidence. Unchanged setup requires no external change; extension affects only requested functions. | Planning and checks. Proposed scenario refinement. |
| ONB-R14 | Sage must retain B2G/B2B distinctions, phase limits, unsupported functions and gated transitions. Invoice owners decide transaction applicability. | Scenario planning and execution. |
| ONB-R16 | Sage must reuse suitable protected references under SPEC-SEI-001. Failed lookup remains unknown and cannot trigger an assumed missing-certificate upload. Authentication and signing require separate qualification. | Public/private trust checks and recovery. |
| ONB-R17 | Before readiness, Sage must verify the business NIF and action authority, plus a suitable certificate where required. A policy-backed NOT_REQUIRED removes only the certificate condition. | ONB-02/03/04/06. |
| ONB-R18 | Sage must distinguish intake, readiness, activation and later use. Each actual actor/contract must qualify authentication, signing, retrieval and reporting separately. | Setup and runtime handoff; SPFE-S02 Article 11. |
| ONB-R19 | Sage must check current firm role, client relationship and action permission independently at protected reads, changes and execution. | Direct/delegated access and portfolio results. |
| ONB-R24 | Sage must prefill qualified current information and ask only for missing, changed or unverified information required by selected functions. A missing/conflicting value returns the affected function, reason and correction owner. | Intake, assessment and client action. Proposed field refinement. |
| OFR-R01 | Sage must classify the business problem separately from whether the operation can safely repeat. | Every failed operation. |
| OFR-R02 | For a permitted retry, Sage must preserve operation identity and correlation and apply an approved, versioned policy and budget. | Automatic and manual retry. |
| OFR-R03 | After a possible external effect with no definitive result, Sage must hold dependent work and reconcile before retry or success. | Unknown changes. |
| OFR-R05 | Sage must return an existing result for an unchanged duplicate and reject conflicting input or stale revisions without another effect. | Requests, corrections and concurrent decisions. |
| OFR-R06 | Sage must isolate recovery and cancellation by client item. | Portfolio processing. |
| OFR-R07 | Manual actions must enforce current authority, environment, security and audit controls. An override cannot bypass evidence or legal-policy gates. | Support and manual recovery. |
| OFR-R08 | Sage must return stable safe status, correlation, relevant policy version, action and owner without exposing protected data. | Product and support results. |
| OFR-R09 | Sage must bind recovery to the original scenario, plan, provider/role, direction, scope and blocked check. Preserve independent valid functions and enforce dependencies. | Failed checks and external effects. |
| OFR-R10 | Corrected or reconciled work must return to its parent checks. Recovery cannot force migration, repeat enrolment, commit a route or infer absence from failed discovery. | Recovery completion. |
| OFR-R12 | Sage must keep NIF, required-certificate and authority findings independent and use qualified protected references and original-source observations. | Trust correction and recovery. |

**Phase rule:** Phase 1 performs public readiness checks without route mutation. Private setup and activation need later-phase qualification. Private A to Private B remains disabled until the shared-foundation decision is approved.

**Isolation rule:** TEST and production evidence, credentials and routes remain separate. Spain identity, representation, routing and recovery rules are selected explicitly; they cannot become another country's defaults.

## 5 Cross cutting quality and operational requirements

These NFR IDs group existing controls; they introduce no numeric service commitment.

| NFR ID | Category | Requirement and acceptance target | Position |
|---|---|---|---|
| ONB-NFR01 | Security and privacy | Isolate tenant/business/environment access. Return no private keys, reusable secrets, raw confidential provider bodies or full tax identifiers in logs, metrics and notifications. Retain only safe protected references in setup results. | Proposed control; negative access/redaction tests required. |
| ONB-NFR02 | Recoverability | A restart must retain accepted intent, duplicate detection, batch manifests and unresolved original effects. Recover without creating an additional effect. | Proposed control; persistence-loss/restart evidence required. |
| ONB-NFR03 | Audit and retention | Keep reproducible decision, correction and operation histories. Apply approved retention and deletion by data class; do not invent a duration. | Policy schedule open with Security, Privacy and Compliance. |
| ONB-NFR04 | Capacity and support | Bound retry attempts and elapsed time, observe provider guidance and schedule independent clients fairly. Monitor pending/unknown age, missing owners, approval expiry, queue age and failed transitions. | Numeric limits, objectives and alert thresholds open with Operations; ONB-Q07/08. |
| ONB-NFR05 | Usability and accessibility | Show the affected function, current outcome and permitted next action with its owner. Do not rely on colour alone to distinguish status or client actions. | Proposed control; ERP review under ONB-Q04/09. |

## 6 Feature activities

Activity references below also refer to the [summary lifecycle](SPEC-SEI-018-customer-onboarding-solution-summary.md#7-master-feature-lifecycle). Interaction and data IDs link to the [supporting inventories](#supporting-inventories); they preserve traceability without defining fields or storage here. Activity-specific requirements below remain proposed unless an external-source statement is explicitly identified.

### 6.1 ONB-01 Capture requested functions

**Outcome:** One saved, scoped request or an explicit duplicate/conflict result. **Parties:** customer/accountant, product and Sage. **Precondition:** authenticated product context and current permission to prepare the selected business.

The request identifies the business, intent, selected functions, directions and environment, with a batch reference where applicable. A case can open while NIF or certificate checks are pending. It cannot execute dependent platform work before its prerequisites pass. Unsupported requests return a limitation without external work.

The same request key and input fingerprint returns the existing item after current access checks. Changed content conflicts. Before an external change, **OFR-01 Capture durable intent** records the original operation, input revision, authority snapshot and recovery checkpoint. If local failure cannot prove non-transmission, ONB-08 handles the possible effect.

**Rules:** ONB-R01/19/24, OFR-R05; ONB-NFR01/02. **Relationships:** ONB-INT-01; OFR-INT-01/03; ONB-D01; OFR-D02/09.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A26 | Given an authorised case with pending identity/trust checks, when saved, then intake succeeds without default upload, readiness, activation or dependent platform execution. |
| OFR-A06 | Given an existing request, when repeated or changed under the same key/stale version, then return the recorded result or conflict without another effect. |
| OFR-A04 | Given possible external success followed by persistence loss, when recovering, then establish the original result once from retained intent/observation. |

### 6.2 ONB-02 Check business identity and authority

**Outcome:** Independent business-identity, caller and action-authority findings. **Parties:** direct customer/delegate, Sage and Identity. **Precondition:** authorised business context from ONB-01.

Verify the business NIF against the represented subject and environment; retain the approved NIF/NIE mapping for an individual business. Verify the caller separately. For a delegate, check the firm's role, client relationship and exact action grant. An unknown evidence source leaves authority undetermined. Missing decisions enter ONB-12; corrected evidence creates a new decision revision. An already submitted uncertain operation retains its original snapshot and uses ONB-08.

**Rules:** ONB-R02/17/19, OFR-R12. **Relationships:** ONB-INT-02; ONB-D02; OFR-D06.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A03 | Given corrected NIF/grant evidence, when checked, then evaluate the new revision and retain earlier decisions and operations. |
| ONB-A25; OFR-A20 | Given independent NIF, required-certificate and authority findings, when one fails, then another passing finding cannot produce readiness; recovery resumes only the affected check. NOT_REQUIRED retains NIF/authority checks. |
| ONB-A29 | Given one delegated client without batch mode, when access is checked, then enforce client/action permission; unrelated or unknown client references receive the same safe denial. |
| ONB-SPFE-A03 | Given a valid certificate but missing required registered retrieval authority, when public retrieval readiness is checked, then hold that function; preserve independent results. SPFE-S02 Article 11; SPFE-S03 operation authorisation. |

### 6.3 ONB-12 Coordinate client approval and evidence

**Outcome:** Qualified evidence or a specific pending client action. **Parties:** requester, eligible approver, product, Sage and evidence owner. **Precondition:** a gate identifies a missing purpose-specific decision.

![Obtain missing approval and verify authority before resuming](../../assets/diagrams/onboarding-client-approval-process.svg)

Figure 1. Approval and evidence flow. [Draw.io](../../assets/diagrams/onboarding-client-approval-process.drawio) · [PNG](../../assets/diagrams/onboarding-client-approval-process.png). Solid arrows show handoffs; dashed arrows show conditional work and recovery. Existing qualified evidence bypasses a new request. Refusal or missing authority retains the blocked check.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R20 | First check current evidence for the exact purpose/scope. If insufficient, Sage must save and present a request to an eligible approver. Keep terms acceptance, delegated operation, route change and signing decisions separate. |
| ONB-R21 | Sage must bind the request/response to business, delegate where relevant, purpose, scope, environment, plan/digest, policy/terms version and expiry. Reject stale/conflicting responses. Withdrawal stops affected future use and preserves earlier snapshots. |

Proposed request states are REQUESTED, APPROVED, DECLINED, EXPIRED, WITHDRAWN and SUPERSEDED. Only REQUESTED accepts an initial decision. APPROVED records a response; Identity must separately verify effective authority and required official evidence. An approved request may later be withdrawn or superseded. Grant expiry is evaluated separately from pending-request expiry.

Identical responses return the recorded acknowledgement after current access checks; they cannot restore expired/withdrawn permission. Save a response or withdrawal only against its current expected version. Material changes require revalidation and a replacement request where needed. Invitation/reminder delivery is not approval. The action channel, approvers and expiry rules remain ONB-Q07 decisions.

**Information exchanged:** business, purpose, proposed effect and request version to the approver; a bound decision and protected evidence reference back. **Relationships:** ONB-INT-12; ONB-D12. **Quality:** ONB-NFR01/03/05.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A30 | Given matching qualified evidence, when the gate is reached, then omit a new request; otherwise return ACTION_REQUIRED and the eligible owner for only dependent work. |
| ONB-A31 | Given an approved response, when eligibility and official evidence are checked, then missing/wrong authority cannot become readiness; terms cannot substitute for delegation. SPFE-S02 Article 11 where applicable. |
| ONB-A32 | Given refusal, expiry, changed terms/plan or competing responses, when processed, then apply the current version/effective-time rules; no stale decision authorises work or enters a technical retry loop. |
| ONB-A33 | Given withdrawal or staff/client-relationship loss, when effective, then stop affected future execution and unauthorised reads; reconcile in-flight effects. A new eligible actor needs fresh checks, without transferred grants/credentials. |
| ONB-A39 | Given accountant-selected companies and a client action, when presented, then trusted firm/actor context cannot be entered manually and an invitation cannot establish approver eligibility. |

### 6.4 ONB-10 Assess current setup

**Outcome:** A versioned plan for each requested function. **Parties:** customer/accountant, Sage and qualified evidence owners. **Precondition:** current access to the business.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R11 | Sage must assess current public/private/Sage setup and the requested outcome before planning missing work. Keep customer declarations separate from observed evidence, including source, time, environment and version. |

Use authorised records and qualified external reads; do not assume a universal directory. Failed or empty lookup does not prove no setup. Plan unchanged confirmation, a refreshed check, missing configuration, supported activation or an owned limitation. A changed scenario/plan rechecks affected dependencies; it cannot replay a completed or uncertain operation.

**Rules:** ONB-R12/14/24. **Information exchanged:** existing functions, selected service/account, observations and missing evidence. **Relationships:** ONB-INT-10; ONB-D10.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A11 | Given ONB-S01, when supported public/private choices are selected, then use their separate phase and activation gates; make no silent platform selection. |
| ONB-A12 | Given ONB-S02, when Sage authority is absent or matching evidence exists, then return the missing action or omit repeated valid work, respectively. |
| ONB-A15; OFR-A14 | Given ONB-S05, when confirming/extending or a read fails, then preserve valid unchanged references and route version; refresh only affected checks and add only requested work. |
| ONB-A17; OFR-A18 | Given ONB-S07/08, when B2G evidence or unsupported functions are assessed, then retain service distinctions and return an owned limitation without a transient retry loop or business-wide applicability decision. |
| ONB-A18 | Given unsupported/unknown setup, when assessed, then do not substitute a provider, force migration or perform unsupported mutation; possible effects enter ONB-08. |
| ONB-A38 | Given each ONB-S01–08 and the selected ERP, when information is needed, then prefill valid matches and ask only for necessary corrections; unchanged S05 requires no new input or mutation. |

### 6.5 ONB-03 Assess prerequisites

**Outcome:** Required access, policy and trust checks for the exact public/private purpose. **Parties:** Sage, Identity, trust owner and qualified integration. **Precondition:** current selected-function plan.

![Check public setup and return readiness](../../assets/diagrams/onboarding-public-readiness-process.svg)

Figure 2. ONB-02–04 public checks. [Draw.io](../../assets/diagrams/onboarding-public-readiness-process.drawio) · [PNG](../../assets/diagrams/onboarding-public-readiness-process.png). Responsibility lanes group logical roles. Failed checks return to their correction/recovery owner; a recovered check must pass before readiness is recorded. Lane labels do not approve deployment boundaries.

Resolve the applicable policy for country, phase, operator, role, environment, function and effective time. Required certificates use purpose-qualified protected references under SPEC-SEI-001. Confirmed missing/expired/revoked/unsuitable material returns the correction owner. Unavailable/stale/ambiguous lookup remains unknown. NOT_REQUIRED needs policy evidence; UNDETERMINED blocks dependent progress. Establish access credentials before the first dependent platform call.

| Requirement ID | Public source constraint and proposed Sage control |
|---|---|
| ONB-SPFE-R02 | Use only supplied qualified checks for public-only setup. Do not invent enrolment, receiving-point publication, onboarding `effectiveDate` or a test invoice. The supplied operation inventory has no such setup payload. SPFE-S03 sections 6.1–6.10; SPFE-S08 sections 5.1–5.9; SPFE-S16. |
| ONB-SPFE-R03 | Verify the represented business independently from the certificate caller and require current action authority. Local approval or an existing credential alone cannot satisfy official representation. SPFE-S02 Article 11; SPFE-S03 operation authorisation. |

The public rules establish certificate-based access and specified web-form Cl@ve options. They do not establish Cl@ve access for an automated ERP contract. Third-party recovery/consultation requires registered authority as stated in Article 11. Authentication, invoice signing and action authority remain separate checks. SPFE-S02; REF-PRIVATE Article 7(3).

**Rules:** ONB-R03/16/17/18, OFR-R12. **Relationships:** ONB-INT-03/04; OFR-INT-09; ONB-D03/04. A lookup cannot qualify authentication/signing execution; ONB-Q06 must identify the actual source and contract.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A22 | Given an existing suitable protected reference, when all purpose/subject/role/environment/version checks pass, then reuse it without another upload or credential copy. |
| ONB-A23; OFR-A21 | Given missing material or an unavailable lookup, when classified, then distinguish owned correction from unknown observation; retry only a proven safe read within budget, otherwise escalate. |
| ONB-A24 | Given certificate-status feedback or tax-only validity, when enabling a function, then require the actual qualified protected-execution contract; status alone cannot enable authentication/signing. |
| ONB-A27; OFR-A23 | Given an unmet prerequisite or web-form access, when setup/recovery runs, then do not invent an unknown mutation or qualify automated authentication, signing, retrieval or reporting from that evidence. SPFE-S02 Article 11. |
| ONB-SPFE-A02 | Given public-only setup and no registration contract, when checking readiness, then perform no enrolment, receiving-point publication or invoice mutation. SPFE-S03/S08/S16. |

### 6.6 ONB-04 Publish public readiness

**Outcome:** Evidenced readiness for each selected public function. **Parties:** Sage and product. **Precondition:** required checks have recorded results.

| Requirement ID | Activity requirement |
|---|---|
| ONB-SPFE-R01 | Qualify submission, consultation, retrieval and event reporting independently for contract, credential and authority. A network connection or one accepted operation cannot prove all functions ready. SPFE-S03; SPFE-S16 establishes submission ports only. |

Proposed readiness states remain NOT_STARTED, CHECKING, ACTION_REQUIRED, READY_WITH_LIMITATIONS, READY, SUSPENDED and OUTCOME_UNKNOWN. READY means the selected checks passed at the recorded time; expiry or revocation can change the result. Pending prerequisites do not imply an uncertain external change. Readiness notifications cannot activate routes.

**Information exchanged:** function result, evidence/freshness, limitations, recheck condition and action owner. **Relationships:** ONB-INT-09/11; ONB-D03/11. **Rules:** ONB-R03/18; ONB-NFR05.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A01 | Given one authorised public capability, when checks finish, then return evidenced readiness or a precise limitation without changing a private route. |
| ONB-SPFE-A01 | Given sending and receiving requested but only submission qualified, when results are returned, then receiving stays separately limited/pending. SPFE-S03/S16. |

### 6.7 ONB-05 Configure private choice

**Outcome:** Explicit supported choice and only missing configuration recorded. **Parties:** customer/delegate, product, Sage and connection owner. **Precondition:** later-phase scope and selected-provider contract are qualified.

![Connect a private provider and activate only when required](../../assets/diagrams/onboarding-private-route-process.svg)

Figure 3. ONB-05–09 private setup and activation. [Draw.io](../../assets/diagrams/onboarding-private-route-process.drawio) · [PNG](../../assets/diagrams/onboarding-private-route-process.png). Configure/check first; decide separately whether an authorised route change is required. Failed/unknown work returns to its blocked gate. Historical obligations continue after a qualified change.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R05 | Sage must allow private configuration and checks without changing the active route. Record explicit operator, scope, direction and supported commercial/support boundary. |

For an existing provider, bind its current account and reuse valid matching setup. Reopening setup cannot cause duplicate enrolment, subscription, credential replacement or receiving publication. A contract-required external change needs separate authority and saved intent. Before any possible effect, failure/cancellation leaves the old route unchanged; after a possible effect, ONB-08 decides the evidence-based hold.

**Information exchanged:** chosen service/account and terms/entitlement evidence. **Relationships:** ONB-INT-05; ONB-D05. **Rules:** ONB-R12/14; ONB-12 for missing decisions.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A04 | Given private setup without activation, when configured/tested or locally failed, then the active route is unchanged. |
| ONB-A13; OFR-A12 | Given ONB-S03 and failed/uncertain account binding, when recovered, then retain the provider and original operation; create no second account or duplicate enrolment and resume ONB-05/06. |

### 6.8 ONB-06 Prove private readiness

**Outcome:** Evidence for each selected private function and required external state. **Parties:** Sage, trust/connection owners and provider. **Precondition:** qualified plan, access, operator and customer scope.

Check the contract, credentials, purpose-specific trust, transport and profile. Inspect existing receiving-point evidence before publishing anything. If publication/change is required, retain intended value, original operation and independent observation with source/time/freshness. A configured connection or successful transport alone cannot prove receiving or public reporting ready.

If a change might have affected reachability, hold unsafe dependent traffic even before local cutover. The previous route remains selected but may no longer be safe. Missing reliable observation requires a qualified manual-evidence gate, not presumed success.

**Rules:** ONB-R03/16/17/18, OFR-R03/09. **Relationships:** ONB-INT-03/06/08; ONB-D04/06; OFR-D05/09. **Recovery owner:** provider/Integration with Routing for reachability.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A14; OFR-A13 | Given ONB-S04 with a failed function, when results/recovery are composed, then preserve independent valid functions, enforce actual dependencies and retain one delivery executor per action. |
| ONB-A06; OFR-A03 | Given publication may have succeeded before timeout, when the result is lost, then retain OUTCOME_UNKNOWN and original evidence; do not repeat mutation or infer safe previous-route reachability. |

### 6.9 ONB-07 Cut over new traffic

**Outcome:** An evidenced authorised boundary for eligible new work, or a conflict/hold. **Parties:** authorised actor, Sage and Routing. **Precondition:** supported transition, current authority/readiness and observed required external state.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R06 | Before activation, Sage must require explicit authority for the exact direction/scope and observed required inbound readiness. |
| ONB-R07 | Sage must process overlapping scope changes one at a time and preserve each invoice's actual origin route. A stale expected route version cannot overwrite a concurrent change. |
| ONB-R25 | Sage must distinguish the requested start from the confirmed effective boundary. Unknown historical start alone cannot reset unchanged setup or receiving progress. Scheduling/timezone support remains ONB-Q09. |

Bind current/target platforms, plan version, approved time/sequence, customer notice and restoration trigger. Change only the qualified scope after an expected-version check. New eligible invoices retain the route version selected at acceptance; do not reassign in-flight work by invoice date. Disagreement between internal/external state cannot return ACTIVE. An unchanged valid route omits commit. Restoration needs a new authorised transition and fresh reachability evidence.

**Relationships:** ONB-INT-07; ONB-D07/08; SPEC-SEI-014. **Rules:** phase rule, OFR-R09/10; ONB-NFR03.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A05 | Given a qualified transition, when committed, then only the authorised direction changes at its evidenced boundary and earlier invoices retain their origins. |
| ONB-A07; OFR-A17 | Given overlapping plans or changed provider/direction/scenario, when execution competes, then a stale version conflicts and original operation identities remain separate. |
| ONB-A08; OFR-A15 | Given uncertainty before/after cutover, when restoring, then Routing decides hold/continuation from actual reachability and uses a separately authorised transition; invoice history is preserved. |
| ONB-A10; ONB-A16 | Given unchanged setup or a gated change, when evaluated, then confirm without unnecessary commit or block the unapproved transition. Private A to Private B is not enabled by this spec. |
| ONB-A40 | Given immediate/scheduled/unchanged setup, when determining start, then preserve unknown historical start, distinguish pending from confirmed activation and test the agreed timezone and both sides of the boundary. |

### 6.10 ONB-08 Reconcile and recover

**Outcome:** Resolved original work returned to its exact check, or an owned unresolved hold. **Parties:** Sage, original operation owner, customer/delegate for correction and Operations. **Precondition:** failed check, inconsistent state or possible external effect.

| Recovery activity | Required behaviour and safe next action |
|---|---|
| OFR-01 Capture durable intent | Use the original record from ONB-01; preserve input, policy, authority and operation identity before dispatch. |
| OFR-02 Classify | Separate problem category from repeat safety. Preserve original source reason and mapping version; return a safe reason/owner. Security/environment mismatch is denied and audited. |
| OFR-03 Correct | Accept authorised scoped correction as a new revision; keep prior decisions. Hold conflicting new changes while an earlier effect is unknown. Resume the affected check. |
| OFR-04 Retry safely | Retry only a proven safe read or contractually idempotent change, with the same identity. Check current authority, cancellation, environment, provider guidance, scope conflict and attempt/elapsed budget. |
| OFR-05 Hold unknown | After a possible effect, retain OUTCOME_UNKNOWN, original input/operation/provider reference, version and transmission timing. Block conflicting repeat, dependent readiness and final cancellation. |
| OFR-06 Reconcile | Query reliable original state. CONFIRMED_SUCCESS records the effect once and returns to parent checks. CONFIRMED_ABSENT permits retry only if that contract accepts the proof. CONFLICT/UNRESOLVED stays held. |
| OFR-07 Escalate | Assign an owner with original evidence, deadline exposure, last observation, unsafe actions and customer-safe message. Manual disposition needs approver/evidence; it cannot rewrite external facts. |
| OFR-08 Publish | Commit the result before notification; ONB-11 composes the per-function view. Repeated/lost notifications are repaired by reading the current permitted version. |

Problem categories remain VALIDATION, AUTHENTICATION, AUTHORITY, POLICY, CONFLICT, THROTTLE, TRANSIENT_DEPENDENCY, OUTCOME_UNKNOWN, INTERNAL and SECURITY. An HTTP/SOAP error alone does not determine the business result or repeat safety. Generic catalogue resend guidance does not prove a mutation safe to repeat. SPFE-S03 section 5.1; SPFE-S08 sections 4.3 and 5.2–5.9.

| Requirement ID | Additional constraint |
|---|---|
| ONB-R08 | Before retry or success, Sage must reconcile an external change whose result is unknown. An empty/failed query is not proof of absence. |
| OFR-R04 | Exhausted budgets or missing reliable observation must produce an owned unresolved case, without false success, absence or final cancellation. |
| OFR-SPFE-R01 | Recover the failed setup check through its qualified owner; do not use SendInvoice/CancelInvoice as an onboarding probe or rollback. Proposed Sage control; SPFE-S03/S16 identify invoice operations. |
| OFR-SPFE-R02 | Preserve transport, SOAP, request and per-item results separately. Resume only with proven repeat safety or authoritative reconciliation. SPFE-S03/S08. |

**Cancellation closure gate:** stop safe queued work. Every possible effect needs evidenced resolution or an approved evidence-backed disposition sufficient for closure. An open unknown effect or assigned escalation alone cannot close cancellation.

**Relationships:** ONB-INT-08; OFR-INT-01–09; OFR-D01–09. **Quality:** ONB-NFR01–04. The route/trust owner retains the original effect and execution controls; recovery does not execute signing or activate a route.

| Acceptance ID | Given / When / Then |
|---|---|
| OFR-A01 | Given invalid local data with proven non-transmission, when classified, then return correction without an unchanged automatic retry or external call. |
| OFR-A02 | Given a throttled safe read, when retried, then preserve correlation, approved budget/provider guidance and fair client processing. |
| OFR-A05 | Given exhausted retries or no reliable observation, when escalated, then retain the unresolved owner/evidence without inferring absence. |
| OFR-A09 | Given manual retry/support access, when performed, then enforce current authority/environment and redact protected material. |
| OFR-A16 | Given CONFIRMED_SUCCESS for an original effect, when recovered, then return to fresh parent gates without route commit or an active-use claim. |
| OFR-A22 | Given corrected credentials or an uncertain protected operation, when recovered, then use the original source/purpose/version and qualified correction owner; do not issue credentials, change signer or repeat possible effects. |
| OFR-SPFE-A01 | Given a public check failure and catalogue resend guidance, when recovering, then retry only a proven repeat-safe check; introduce no invoice/route mutation. SPFE-S03/S08. |
| OFR-SPFE-A02 | Given a lost owning-feature mutation result, when onboarding receives it, then retain the original feature/connector operation and recovery owner; do not fabricate setup success. SPFE-S03/S16. |

### 6.11 ONB-09 Preserve and release

**Outcome:** Earlier invoice obligations retain qualified access; old dependencies release only at separate gates. **Parties:** Sage, Routing, records, provider and Operations. **Precondition:** earlier/in-flight work or a transition exists.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R09 | Sage must preserve original actor, route and evidence for earlier invoices and release previous dependencies separately after their approved continuity gates. |

Retain the required path for delivery completion, status/payment reports, rejection, correction and audit. Unconfirmed historical execution blocks release, without automatically blocking an independently qualified new-traffic change. Full exit follows SPEC-SEI-003. Receiving-owned history choices must preserve saved progress and suppress duplicate intake during overlap; unknown coverage returns an action, not an invented default date.

**Information exchanged:** historical access evidence and receiving coverage/checkpoint. **Relationships:** ONB-D08; ONB-INT-07/11; SPEC-SEI-016.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A41 | Given a supported earlier-invoice retrieval choice, when coverage is set, then qualify source-date meaning, authority and available history, preserve progress and prevent duplicate intake. Unknown coverage has an owner. |

### 6.12 ONB-11 Return results and required actions

**Outcome:** The current authorised result for each function, with its limitation/action owner. **Parties:** Sage, Global API, ERP/product and support. **Precondition:** result and evidence committed.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R13 | Sage must return setup, readiness and independently evidenced activation separately for each selected function through the common API. |

Return the business/environment, function/direction/scope, selected connection/profile, independent check findings, conditional route/effective boundary, freshness and safe next action. These are logical information groups; actual fields remain ONB-Q04/09. Missing activation evidence means pending/unknown, even if connection checks pass. Keep public copy/reporting separate from delivery and receiving; setup cannot claim invoice acceptance, payment or legal-report completion.

A notification follows saved state and may repeat. Consumers deduplicate by version and read the authoritative permitted result after loss/out-of-order delivery. Runtime owners recheck authority, revocation and required credential validity before new protected use; setup is not indefinite permission.

**Relationships:** ONB-INT-09/11; OFR-INT-07; ONB-D11; OFR-D08. **Rules:** ONB-R18/19; OFR-R08; ONB-NFR01/05.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A20 | Given concurrent changes or lost/duplicate notifications, when the product reads again, then return the authoritative permitted version without repeating external work or treating readiness/recovery as activation. |
| ONB-A42 | Given ERP result and later public transport mapping, when produced, then separate business/caller, independent results and owned actions; emit no credentials, invented SPFE onboarding fields or test invoice. SPFE-S02 Article 11; SPFE-S03 sections 6.1–6.10; SPFE-S08 sections 5.1.2–5.2; SPFE-S16/S18. |

### 6.13 ONB-13 Manage portfolio batch

**Outcome:** Saved receipt and independent client work with permitted progress. **Parties:** authorised submitter, product, Sage, Identity and Operations. **Precondition:** qualified batch permission and contract under ONB-Q08.

![Receive a portfolio batch and isolate every client outcome](../../assets/diagrams/onboarding-portfolio-batch-process.svg)

Figure 4. Portfolio intake and independent client processing. [Draw.io](../../assets/diagrams/onboarding-portfolio-batch-process.drawio) · [PNG](../../assets/diagrams/onboarding-portfolio-batch-process.png). Reject an invalid envelope before client work. Save valid intake before receipt, check each client independently and stop only unsafe/unauthorised work. Dashed paths show correction, cancellation and uncertain-effect recovery.

| Requirement ID | Activity requirement |
|---|---|
| ONB-R22 | Sage must save a batch manifest before receipt, map each logical client item once and resume incomplete decomposition after restart. An invalid envelope/conflicting duplicate item reference creates no client work. |
| ONB-R23 | Sage must expose only currently permitted progress/actions and allow authorised selected correction/cancellation without repeating completed independent work or hiding unknown effects. |

Bind batch identity to trusted submitting organisation/product, environment and command purpose. Same key/digest returns the existing receipt after current access checks; changed input conflicts. Count identical repeated entries separately from unique logical work. Overlapping accepted batches can attach identical authorised commands; changed/stale work cannot duplicate effects.

Receipt does not freeze permission. Recheck each client before protected execution and result access. Unknown/unlinked references receive the same safe denial. Relationship/staff-role loss stops affected new work and current detail access; an eligible replacement actor needs fresh checks and inherits no prior grant or credential.

| Proposed coordination state | Meaning |
|---|---|
| RECEIVED | Receipt and manifest saved; item creation/processing not started. |
| PROCESSING | Work advances without an unresolved approval, correction or uncertain effect. |
| PARTIAL | At least one item needs such action/resolution; other safe items can continue. |
| COMPLETED | Every requested item has a recorded final disposition; no pending action/uncertain effect remains. Not a readiness result. |
| CANCELLING | Remaining-batch cancellation recorded; safe pending work stops and submitted effects await resolution. |
| CANCELLED | Remaining-batch work stopped and ONB-08's closure gate passed. Retain completed item results. |
| FAILED_ENVELOPE | Rejected before client items or external work. Failure after receipt is recoverable work. |

CANCELLING takes precedence during unresolved remaining-batch cancellation; otherwise unresolved item action produces PARTIAL. Selected-item cancellation does not make the whole batch CANCELLED. Progress counts/details include only clients currently accessible; a parent state that reveals withheld progress is replaced by a visibility limitation. Receipt counts describe submitted requests, not current client progress. Filtering, pagination and notifications enforce the same access boundary.

**Information exchanged:** batch key/digest, scoped submitted references, receipt/unique counts, item mapping and permitted progress/actions. **Relationships:** ONB-INT-13; ONB-D13. **Rules:** ONB-R04/19; OFR-R05/06; ONB-NFR01/02/04.

| Acceptance ID | Given / When / Then |
|---|---|
| ONB-A02; OFR-A07 | Given mixed client outcomes, when processing/aggregating, then each client keeps its permission/result and counts derive from committed versions; unknown work is not complete/failed. |
| ONB-A34 | Given repeated intake or restart during decomposition, when resumed, then create/attach each logical item once; preserve received/unique counts and reject conflicting envelope entries before work. |
| ONB-A35; OFR-A08 | Given mixed ready/pending/invalid/unknown clients, when selected work is corrected/cancelled, then safe items continue and completed results remain; unknown effects prevent final cancellation. |
| ONB-A36 | Given loss of access to submitted clients, when reading/filtering/notifying, then withhold current details/counts and any revealing parent state; retain only safe submitted references. |

## 7 Traceability and supporting artefacts

### Supporting inventories

| Reference | Purpose and authority |
|---|---|
| [Feature landing page](README.md) | Navigation to canonical PRDs, companions and unchanged predecessor. |
| [Solution Summary](SPEC-SEI-018-customer-onboarding-solution-summary.md) | End-to-end outcome, workflow, boundaries and material decisions. |
| [SPEC-SEI-002 interaction contracts](../SPEC-SEI-002-onboarding-solution-specification.md#1-interaction-contracts) | ONB-INT-01–13 and OFR-INT-01–09 logical/technical analysis. Proposed service allocations and field names require qualification. |
| [SPEC-SEI-002 data inventory](../SPEC-SEI-002-onboarding-solution-specification.md#2-data-inventory) | ONB-D01–13 and OFR-D01–09 supporting records; no new duplicate stores are required by this split. |
| [SPEC-SEI-002 customer fields](../SPEC-SEI-002-onboarding-solution-specification.md#3-customer-and-accountant-fields-by-scenario) and [system/results fields](../SPEC-SEI-002-onboarding-solution-specification.md#4-system-fields-dates-and-erp-results) | Proposed field-level analysis under ONB-Q04/09, including start dates and receiving history. |
| [SPEC-SEI-002 public field boundary](../SPEC-SEI-002-onboarding-solution-specification.md#5-sage-spfe-field-boundary) | Exact transport elements and source limits. Does not define an onboarding payload. |
| [SPEC-SEI-002 original verification matrix](../SPEC-SEI-002-onboarding-solution-specification.md#1-verification-matrix) | Detailed PRD-to-interaction/data mappings for existing acceptance IDs. The compact scenarios here retain their observable outcomes. |
| [SPEC-SEI-002 technical sequences](../SPEC-SEI-002-onboarding-solution-specification.md#onboarding-technical-sequences) | Supporting public/private sequence examples. Physical contracts and deployment remain unqualified. |
| [SPEC-SEI-001](../SPEC-SEI-001-certificate-management-solution-specification.md), [013](../SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md), [014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md), [011](../SPEC-SEI-011-public-platform-connector-solution-specification.md), [016](../SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md), [003](../SPEC-SEI-003-offboarding-solution-specification.md) | Owning trust, API, route, public-execution, receiving and exit boundaries. |

### Solution ownership and reuse qualification

**ONB-R15 and OFR-R11 preserve recorded ownership direction:** the E-Invoice Service coordinates setup and recovery. There is no separately approved onboarding service. An internal component, physical record mapping, scheduler and deployment remain proposed under ONB-Q05/OFR-Q03. Dependency owners retain their own controls. This allocation is technical analysis rather than a new business requirement.

| Reuse area | Spain use, local changes and gaps | Owner and activation evidence |
|---|---|---|
| Shared work-item, version, approval, batch and recovery patterns | Reuse proposed logical patterns; bind Spain authority and disclosure rules. Actual implementation coverage is unknown. | Product, Identity, E-Invoice Service and Architecture: source capability/build, contracts, retained behaviour, local changes, gaps and restart/access evidence. ONB-Q05/07/08; OFR-Q03. |
| Country/provider policies and adapters | Bind NIF/NIE, representation, credential purposes, receiving-point sequences, repeat safety and result meanings for Spain. None becomes a default for another country/provider. | Spain policy, Integration and Routing: approved local rules, selected contracts, error mapping, original-state observation and cross-country isolation evidence. ONB-Q01/02/06/07; OFR-Q01/02/04. |
| Existing Tax/certificate capability | Existing implementation reuse candidate; lookup/readiness feedback does not establish protected authentication/signing coverage. | Tax Service, Connections Service, AFL and Security: actual build/source/contract, safe reference/version, purpose qualification, correction owner and original-operation observation under SPEC-SEI-001. |
| Existing DTS transformation | Preferred reuse candidate where exchange needs transformation; onboarding itself performs no invoice conversion. | DTS and exchange owners: build, mappings, rule packs, selected input/output contracts, operations and Spain acceptance under [SPEC-SEI-008](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md). |

| Acceptance ID | Required cross-feature evidence |
|---|---|
| ONB-A09; OFR-A10 | Given another country/provider, when the shared flow runs, then select its approved rules and retry contract. Missing local evidence blocks dependent work; do not inherit Spain rules or modify prior Spain evidence. |
| ONB-A19; OFR-A11 | Given a reuse candidate, when qualifying it, then record source build/contracts, local changes, gaps, owner and selected-purpose evidence. Changed role/purpose/environment/version prevents unsupported evidence reuse. |
| ONB-A21; OFR-A19 | Given the proposed workflow, when reviewing implementation, then retain recorded E-Invoice Service coordination and identify actual component coverage; do not treat a proposed internal boundary as a deployed service. |
| ONB-A28; OFR-A24 | Given process and technical-sequence views, when reviewed/injected with representative faults, then IDs and meanings agree. Missing prerequisites, failed safe reads, unknown policy and possible effects select their own correction/recovery checkpoints. |
| ONB-A37 | Given shared approval/portfolio patterns, when used for another country or implementation, then require local approver, representation, disclosure and build/contract qualification before enabling them. |

### Review and release gates

The activity scenarios describe evidence to obtain, not executed implementation tests. Before approval or enabling a scope, the owners must close its relevant gates in the [existing release-gate record](../SPEC-SEI-002-onboarding-solution-specification.md#2-review-and-release-gates).

| Scope | Evidence needed |
|---|---|
| Design | Scenario/function dependencies, original-operation identity, safe repeat/observation semantics, exact recovery checkpoints and accountable owners. |
| Public pilot | Qualified function contracts, caller/representation, conditional trust, independent results and SPFE acceptance above. Resolve relevant SPFE-Q01/09/12 conflicts with the source owner. |
| Private/migration pilot | Qualified provider/operator, receiving-point sequence/reachability, authorised boundary, concurrent-change/restoration tests and historical access. |
| Delegated/portfolio pilot | Eligible approvers, accepted evidence and actual action channel; durable receipt, restart, selected recovery/cancellation and current-visibility tests. |
| ERP/cohort pilot | Actual field mappings, missing-input actions, timezone/scheduling support and receiving-history coverage. Measure existing-use assumptions. |
| Production | Approved security, retention, support ownership/runbooks, conformance and measured capacity, service/recovery objectives and retry limits. |

## REF Source references

Final published law establishes legal duties. A technical file establishes only its own stated contract facts. Examples cannot close missing field/profile/operation coverage. The supplied formats document is draft; conflicting transport and unfinished service formats remain qualification gates. English guides and text extracts are reading aids.

| REF ID | Original source and version | Exact location | Supported claims and limits |
|---|---|---|---|
| REF-BASE | [SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md), updated 20 October 2026 | ONB/OFR activities, requirements, verification matrix and decisions | Predecessor IDs, recorded ownership and proposed behaviour. Does not prove implementation. |
| REF-PRODUCT | [PRD-SEI-101](../../prds/PRD-SEI-101-public-platform-onboarding.md), [104](../../prds/PRD-SEI-104-accountant-and-single-client-onboarding.md), [107](../../prds/PRD-SEI-107-public-onboarding-failure-recovery.md), [222](../../prds/PRD-SEI-222-customer-onboarding-entry-point-migration.md), [225](../../prds/PRD-SEI-225-operations-resilience-support-reconciliation.md), [231](../../prds/PRD-SEI-231-country-identifiers-tenancy-and-delegated-accountants.md) | Product scope/FRs; PRD-104 FR2–8/13–20 and NFR4; PRD-107 FR1–20; PRD-231 ID-FR9–12. Individual source versions remain in their front matter. | Canonical product needs for readiness, authority, portfolio, recovery and continuity. Earlier external assumptions cannot override final sources. |
| SPFE-S02 | [BOE-A-2026-20587.pdf](../../context/BOE-A-2026-20587.pdf); Order HAC/1028/2026, published 5 October 2026; [official original](https://www.boe.es/eli/es/o/2026/10/02/hac1028) checked 21 October 2026 | Article 11(1)–(2) | Certificate access, specified web-form options and representation rules including registered third-party recovery/consultation authority. Does not prove Sage API support. |
| REF-PRIVATE | [RD 238/2026 official original](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-7295), published 31 March 2026; checked 21 October 2026 | Article 7(3) | Signature boundary for covered private-platform invoices. Separate from connection authentication; no universal customer-upload requirement follows. |
| SPFE-S03 | [CatalogoServicios.pdf](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), 0.1.0, 9 October 2026 | Sections 4.1–4.3, 5.1 and 6.1–6.10, pp. 7–20 | Operation inventory, authorisation and fault/resend guidance. No supplied onboarding enrolment contract; no blanket repeat-safety guarantee. |
| SPFE-S08 | [FormatosEntradaSalida.pdf](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), 0.1.0, 9 October 2026, marked draft | Sections 4.3 and 5.1.2–5.9, pp. 7–15 | Caller/destination/message structure and distinct response levels. No onboarding payload; transport conflict and pending formats limit qualification. |
| SPFE-S16 | [SendInvoice.wsdl](<../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), supplied 13 October 2026 | Request documentation, SOAP binding, fault and service/port elements | Submission contract and certificate-class PRE ports; no onboarding mutation, live-availability evidence or guarantee that repetition is safe. |
| SPFE-S18 | [ebms-header-3_0-200704.xsd](<../../context/WSDL servicios web - PRE/20261013/xsd/ebms/ebms-header-3_0-200704.xsd>), supplied 13 October 2026 | MessageInfo, PartyInfo/From/To, CollaborationInfo and PayloadInfo/PartInfo | Exact header structure used by ONB-A42's supporting mapping; generic schema does not establish business values, authority or replay safety. |
| REF-CONTEXT | [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md), [source manifest](../../assets/regulatory/spain/spfe/source-manifest.json), [glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md) | Source register, snapshot hashes, shared conflicts and terminology | Traceability and reading aids. Inventory completeness and hashes do not prove field-map or implementation completeness. |
