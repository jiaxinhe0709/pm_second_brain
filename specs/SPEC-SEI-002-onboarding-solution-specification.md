---
id: SPEC-SEI-002
title: Customer Onboarding Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-06
reviewers: []
related:
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-107
  - PRD-SEI-202
  - PRD-SEI-222
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-231
  - SPEC-SEI-001
  - SPEC-SEI-004
  - ADR-SEI-001
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Customer Onboarding Solution Specification

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices still need review; **open** decisions still need an owner’s recorded answer. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### 1 Purpose, authority and boundaries

This is a **proposed logical design** for setting up one Spanish business to use e-invoicing. It covers two stages with separate checks and approvals. **Phase 1** checks readiness for functions that use the public solution. **Later phases** configure a private platform, check the published receiving destination, and activate or change the route.

Public readiness alone does not mean that the business is registered externally, a private route is active, or invoices can be exchanged. The source requirements are [public onboarding](../prds/PRD-SEI-101-public-platform-onboarding.md), [direct and accountant onboarding](../prds/PRD-SEI-104-accountant-and-single-client-onboarding.md), [recovery](../prds/PRD-SEI-107-public-onboarding-failure-recovery.md), and [private onboarding and migration](../prds/PRD-SEI-222-customer-onboarding-entry-point-migration.md). The [certificate spec](SPEC-SEI-001-certificate-management-solution-specification.md) supplies the conditional trust-readiness contract.

The logical services, state names, interaction shapes and records below are **proposed**. The PRDs establish customer outcomes and safety constraints. Spanish external interfaces, entry-point publication sequence, representation rules, operator model, signing policy, measurable service targets and ownership of the implemented services remain **open**. This document is one canonical Markdown source and one intended Confluence page; it is unpublished.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Work items and portfolio isolation | Track each Spanish business separately, recognise repeated requests and show partial portfolio results. | Reusable unchanged | Reuse the work-item, version and independent-client patterns. Validate tenant and client isolation. Onboarding and Product. |
| Readiness and route transition | Assess public readiness, then separately configure and activate a private route where supported. | Reusable with country binding | Bind the local identity, authority, entitlement, provider and entry-point policies. Product, Identity and route owner. |
| Spain onboarding rules | Use Spain identity/representation checks and the confirmed public/private entry-point and migration sequence. | Country-specific | Do not make Spanish NIF/NIE rules or the public/private sequence defaults for other countries. Spain technical owner and Compliance. |
| Existing onboarding implementation | Assess identity, trust, work-item, connection and routing services for the Spain journey. | Unknown | No deployed end-to-end onboarding implementation is established here. Record existing owners, contracts and gaps first. Architecture and service owners. |

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
| Capability | A supported function, such as receiving invoices or signing them. |
| Route | The platform and connection used to send or receive an invoice. |
| Idempotency | A repeat of the same request has no additional effect. The contract must define how the system recognises that request. |
| Reconciliation | Check the original operation against a reliable source to establish what actually happened before deciding the next action. |
| Gate | A condition, decision or evidence check that must pass before the next step can proceed. |
| Tenant | The customer account boundary used to keep one customer’s data and access separate from another’s. |
| Immutable / append-only | A saved item cannot be changed; new information is added as a new record instead of overwriting earlier records. |
| Provenance | The record of where data came from and which versions, checks and changes produced the result. |
| Contract | The agreed inputs, outputs, behaviour and responsibilities between services or parties. |
| Durable | Saved so the record remains available after a service restart. |
| Readiness | Evidence that the required checks for a specific function have passed. The result may expire or have limitations. |
| Entry point | The published address or destination used to reach a business for invoice receipt. |
| Cutover / rollback | Switch new work to a different route; or make a controlled change back. Earlier invoices keep their actual route history. |
| Portfolio | An accountant’s set of client businesses. Each client is checked separately. |
| Input digest / hash | A calculated fingerprint used to detect a change in the submitted data. |

### 2 Endpoints and handoffs

| Outcome | Observable result | Boundary |
|---|---|---|
| Public capability ready | Entity/capability is ready or ready with stated limitations, with evidence, expiry/recheck and next action | No claim of external registration, invoice compliance, delivery or private route activation |
| Private route active | Explicitly authorised direction/scope has matching intended and observed external readiness and an effective new-traffic boundary | Earlier invoices retain original route and operator |
| Action required / blocked | Exact entity, capability or direction is held with stable reason and owner | Other portfolio items and unaffected directions continue |
| Cancelled before activation | Pending work is closed under policy and live routing is unchanged | Externally completed actions still require reconciliation and separate reversal |
| Recovery or rollback case | Actual external and invoice state is preserved; restoration is a new evidenced transition | No silent state reset or historical rewrite |

Actors are the customer administrator or validated delegate; Sage product/API; onboarding orchestration; legal-subject and authority services; conditional trust service; operator/connection and route services; external public platform or provider; evidence store; and operations. Each performs only its authorised action for one tenant, legal entity, environment, capability, direction and route scope. An accountant portfolio is a collection of isolated client work items, not one shared mandate or credential.

### 3 Process diagrams and text equivalent

**Public readiness:** ![Public onboarding readiness process](../assets/diagrams/onboarding-public-readiness-process.svg)

[Editable Draw.io source](../assets/diagrams/onboarding-public-readiness-process.drawio) · [PNG preview](../assets/diagrams/onboarding-public-readiness-process.png). The existing [customer and service readiness overview](../assets/diagrams/e-invoicing-customer-service-readiness.drawio) provides cross-service context; this diagram isolates the Phase 1 process.

Customer/delegate starts ONB-01 for one entity/capability → ONB-02 resolves legal subject and authority → ONB-03 checks applicable external identity/representation evidence and conditional certificate readiness → ONB-04 records readiness for each required check. Missing authority or uncertain policy yields an owned action; an ambiguous external mutation yields ONB-08 reconciliation. For a portfolio, repeat per client and return partial outcomes without promoting failed clients.

**Private onboarding and migration:** ![Private onboarding and migration process](../assets/diagrams/onboarding-private-route-process.svg)

[Editable Draw.io source](../assets/diagrams/onboarding-private-route-process.drawio) · [PNG preview](../assets/diagrams/onboarding-private-route-process.png). The existing [route transition and offboarding overview](../assets/diagrams/e-invoicing-route-transition-offboarding.drawio) gives the wider lifecycle.

ONB-05 records the chosen legal entity, direction, scope, operator and commercial/authority terms while existing traffic continues → ONB-06 validates connection and publishes/observes any required entry point → ONB-07 activates only after readiness, authorisation and effective boundary are recorded → ONB-09 preserves prior-route in-flight/history and releases dependencies at separate gates. Failure before cutover leaves the old route. Unknown external outcome goes to ONB-08. A post-cutover failure opens a controlled restoration case that keeps each invoice's actual origin.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Owner / consumer |
|---|---|---|
| ONB-01 Open work item | Authenticated request creates one scoped, versioned work item; duplicate key returns same result | Product → onboarding |
| ONB-02 Establish subject and authority | Verified entity, principal/delegate, action and validity; missing grant is visible | Identity/authority → onboarding |
| ONB-03 Assess prerequisites | Applicability, environment, external checks and conditional trust assessed separately | Onboarding → identity/trust/external |
| ONB-04 Publish public readiness | Result for each capability, evidence and recheck; no route mutation | Onboarding → product |
| ONB-05 Configure private choice | Explicit option, subscription/connection intent and scope stored without new traffic | Customer/product → onboarding/route |
| ONB-06 Prove private readiness | Operator, transport, profile and required external entry point observed ready | Connection/adapter → onboarding |
| ONB-07 Cut over new traffic | Serialised scope transition records authorised effective boundary | Route service → exchange/product |
| ONB-08 Reconcile/recover | Unknown result or discrepancy has owner, observed state and safe next action | Operations/external adapter |
| ONB-09 Preserve and release | Original invoice context persists; previous dependencies released only after approved gates | Route/records/operations |

### 5 Key decisions and risks

| Decision | Design impact | Owner and gate |
|---|---|---|
| Official public-solution identity, representation, certificate and API contract | Determines which ONB-03 checks or mutations are real | Spain regulatory/technical owner; public pilot |
| Private operator, supported directions/scope granularity and activation mechanism | Determines ONB-05–07 command and lock key | Product, architecture, operator; design |
| Entry-point publish/observe/withdraw order and propagation evidence | Determines inbound cutover and rollback safety | Local technical/regulatory owner, provider; pilot |
| Post-switch historical status/reporting actor and route | Determines how prior-provider access is retained | Compliance/Tax, provider; migration pilot |
| Provider idempotency, state query and correction support | Determines whether automation or manual reconciliation is safe | Provider owner, operations; integration |
| Trust/signature and retention policies | Determines conditional readiness and expiry/record schedules | Security, Legal/Tax; design |

The main risks are an accountant acting without the required client permission, treating public readiness as route activation, losing inbound reachability, repeating an external change after a timeout, or losing access needed for earlier invoices.

The controls below pause the affected scope, show the intended and observed states, and keep the last safe route until the required checks pass.

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Scope model and invariants

The proposed work-item key is (tenant, legalSubject, environment, capability, direction, scope, onboardingIntent). Each request includes an idempotency key and a fingerprint of the input in its agreed standard form.

Changes affecting the same business, direction and scope run one at a time. Independent clients and directions that do not overlap can proceed separately. TEST and production use separate identities, evidence, credentials, route state and keys.

| ID | Rule that must always hold |
|---|---|
| ONB-I01 | Authentication, legal-subject identity, representation authority, credential possession, commercial entitlement, external registration and active route are independent facts. |
| ONB-I02 | Public readiness is per entity and capability, with limitations and evidence. It cannot activate a private route or prove invoice compliance. |
| ONB-I03 | An accountant grant is checked per client, capability, action and effective time; portfolio batch success cannot mask a failed item. |
| ONB-I04 | New eligible traffic changes route only after an explicit authorised cutover; every invoice freezes its actual origin route, operator and identifiers. |
| ONB-I05 | An unknown external mutation is neither success nor safe retry. Observe/reconcile the original operation before repeating it. |
| ONB-I06 | Subscription, connection, entry-point registration, route, transition and historical access have separate state and separate release gates. |
| ONB-I07 | No private key or reusable secret enters a product response, work item, audit event or support view. |

### 2 Activities and state transitions

**ONB-01 Intake.** The product submits the business reference, requested capabilities and directions, actor, environment and any portfolio batch reference. Onboarding checks the request format, tenant access and whether the requested capability is supported, then saves a work item.

The same key and input fingerprint return the existing item. Reusing the key with different content returns a conflict. Cancellation stops pending steps but does not erase an external change that may already have happened. A portfolio parent shows overall progress; each client item keeps its own permission, state and error.

**ONB-02 Identity and authority.** The legal-subject service resolves Spanish identity and product/tenant mapping without treating a user login as the legal entity. Authority evaluates direct administrator or delegate/mandate for the exact capability, direction, action and time. Missing, expired, revoked or ambiguous authority blocks that child item. Grant correction creates a new decision snapshot; an in-flight external operation retains the snapshot used at submission and is reconciled before replacement. Recheck authority immediately before ONB-07 and other external mutations.

**ONB-03 Prerequisites.** Resolve a versioned capability policy for phase, operator, environment, route, direction and effective date. Check required legal identity/representation evidence, product entitlement, external verification where an approved contract exists, and certificate readiness only when the policy says it is required. Record NOT_REQUIRED as an evidenced policy result; UNDETERMINED is a policy block. The trust service returns readiness for the specific purpose and evidence reference per [SPEC-SEI-001](SPEC-SEI-001-certificate-management-solution-specification.md), without exposing key material.

External reads may be retried under a bounded policy; an external mutation requires operation safety classification and reconciliation support. Onboarding does not invent a registration call where no official interface is confirmed.

**ONB-04 Public readiness.** Save the result and evidence source for each required check before calculating the overall capability result. Proposed states are NOT_STARTED, CHECKING, ACTION_REQUIRED, READY_WITH_LIMITATIONS, READY, SUSPENDED and OUTCOME_UNKNOWN.

READY means the approved Phase 1 checks for that capability passed at the recorded time. Expired or revoked dependencies can change the result; show the reason and when to check again. Product and support receive a result with sensitive values removed. The user sees who must act next. A public-readiness event cannot activate a route.

**ONB-05 Private choice/configuration.** Present supported public/current-provider/Sage options with operator, direction, supported scope, price and support boundary. Record explicit customer/delegate choice and action authority. Create proposed subscription and connection configurations independently from active route state. If there is an existing provider or public route, inventory current directions and historical obligations. A configuration failure or cancellation before cutover leaves the old route. Unsupported mixed-scope combinations are blocked with a product explanation rather than silently widened.

**ONB-06 Private readiness.** Validate operator/contract/cohort approval, credentials and conditional trust, transport/profile conformance, external-provider capabilities and (for inbound) required entry-point publication/discoverability. Store intended value, external operation ID, independently observed value, source, observed time and freshness. Connection configured is distinct from external observed ready. If publication times out, mark OUTCOME_UNKNOWN and invoke ONB-08. A provider without reliable observation requires a documented manual gate with named evidence and approver. Existing route remains selected throughout.

**ONB-07 Activation/cutover.** Check the actor’s permission again and confirm that readiness evidence is still current. Lock the affected scope and record the expected current route version. The cutover plan records the approved time and sequence, entry-point publication evidence, rollback trigger and customer notice.

Change the route only if its current version still matches the expected version (compare-and-set). The change applies only to the authorised direction and scope, for invoices accepted after the agreed boundary. If the external and internal states do not match, do not report ACTIVE; open ONB-08.

When accepting an invoice, the exchange service saves its route version so the provider cannot change while that invoice is being processed. After success, save the actual cutover time and return status for each direction. A single ONBOARDED flag must not hide different route states.

**ONB-08 Recovery.** Onboarding owns the affected capability and route outcome; [SPEC-SEI-004](SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md) owns the detailed failure classification, retry, correction, cancellation and reconciliation contract. Reconcile unknown external effects using the original correlation/operation ID before repeating a mutation or claiming readiness. A mismatch keeps the transition blocked and opens an owned case. After cutover, restoration is a new authorised transition, subject to current external state and inbound discoverability; invoice origins remain unchanged.

**ONB-09 Continuity and release.** Keep old-route access for in-flight delivery, statuses, rejection/payment reporting, corrections and audit according to confirmed actor/channel rules. Release old entry point, registration, credentials and commercial relationship at independent approved gates. [Offboarding SPEC-SEI-003](SPEC-SEI-003-offboarding-solution-specification.md) governs a later full exit. Lack of a confirmed historical execution path blocks release, not the already evidenced new-traffic cutover.

### 3 Logical requirements and quality controls

| ID | Requirement and PRD source |
|---|---|
| ONB-R01 | Resolve legal subject, tenant, environment and exact capability before any mutation; PRD-SEI-101/222. |
| ONB-R02 | Verify direct or per-client delegate authority for each action and recheck before activation; PRD-SEI-104/231. |
| ONB-R03 | Maintain independent, evidenced readiness dimensions; conditional certificate need follows policy; PRD-SEI-101/226. |
| ONB-R04 | Return partial portfolio results and isolate correction, cancellation and failure per client; PRD-SEI-104/107. |
| ONB-R05 | Allow private configuration and tests while live route stays unchanged; PRD-SEI-222. |
| ONB-R06 | Require observed external inbound readiness and explicit scope-specific authority before cutover; PRD-SEI-222. |
| ONB-R07 | Serialise overlapping cutovers and freeze route origin for each invoice; PRD-SEI-222/202. |
| ONB-R08 | Reconcile outcome-unknown external mutations before retry or success; PRD-SEI-107/222/225. |
| ONB-R09 | Preserve historical actor, route and evidence; release previous dependencies separately; PRD-SEI-222/224. |
| ONB-R10 | Audit intent, decision, mutation, observation, correction and override with actor, scope, time and source; PRD-SEI-225/226. |

Authorisation uses least privilege and delegation limited to the approved purpose; support override must be attributable and cannot bypass external-observation or legal-policy gates. Encrypt sensitive evidence, isolate tenant/entity/environment, redact diagnostics, and use reference-only credentials. Define service objectives after volumes, external propagation and recovery baselines are measured. Monitor age/count of pending, blocked, unknown and discrepant items, expiring grants/trust, stale entry points and failed cutovers; each alert has an operations owner.

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Reuse one work-item and readiness contract while resolving country rules through versioned policies and provider adapters. The Spain public-readiness result must remain separate from private-route activation. Another country needs its own identity, representation, certificate and receiving-address evidence; it cannot inherit Spain’s readiness or transition sequence.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Interaction contracts

These are logical contracts, not approved endpoints or physical service allocations. Every command carries requestId, correlationId, actor, tenant, legalSubject, environment, action, scope, expectedVersion and inputDigest as applicable. An error includes stable category, affected scope, safe retry class and responsible action; never a credential.

| ID | Caller → logical owner | Input / output and safety |
|---|---|---|
| ONB-INT-01 | Product → onboarding | Open/get/cancel work item; idempotency key and digest; returns item/version and child outcomes; conflict on changed duplicate. |
| ONB-INT-02 | Onboarding → identity/authority | Resolve legal subject and scoped decision snapshot; returns grant evidence, validity and reason; fail closed on unknown. |
| ONB-INT-03 | Onboarding → capability/trust | Evaluate phase/operator/capability policy and conditional trust; returns READY, limited, action, not-required or undetermined plus evidence/recheck. |
| ONB-INT-04 | Onboarding → external verification adapter | Perform approved read/check or mutation only under a versioned contract; record operation ID, safety class, external reference and observed result. |
| ONB-INT-05 | Onboarding → subscription/connection | Store proposed commercial and technical context; returns independent states; cannot select active route. |
| ONB-INT-06 | Onboarding → entry-point/provider adapter | Publish or inspect supported entry point; intent and observed state remain distinct; unknown result invokes ONB-INT-08. |
| ONB-INT-07 | Onboarding → route/exchange | Compare-and-set cutover for exact direction/scope and effective boundary; route version returned and bound to new invoices. |
| ONB-INT-08 | Operations/onboarding → adapter | Query/reconcile original external operation; returns confirmed, absent-safe-to-retry or unresolved with evidence; no duplicate mutation. |
| ONB-INT-09 | Onboarding → product/operations | Emit state-changed/case-opened notification after durable commit; consumers deduplicate by eventId and version. |

Events are proposed ONBOARDING_ITEM_CHANGED, PUBLIC_READINESS_CHANGED, PRIVATE_READINESS_CHANGED, ROUTE_CUTOVER_OBSERVED and ONBOARDING_RECOVERY_OPENED. Delivery is at least once, so the same event may arrive again; consumers recognise repeats and read the authoritative work-item version. A notification is never the sole proof of an external side effect. External adapter capabilities (query, idempotency, publication, revocation, acknowledgement) are registered per provider and environment; unsupported operations become explicit manual gates.

### 2 Data inventory

| ID | Record / owner | Essential fields and handling | Consumers |
|---|---|---|---|
| ONB-D01 | Onboarding work item / onboarding | Immutable request scope/digest; mutable state/version, phase, owner, deadline, child links, reason; restricted | Product, operations |
| ONB-D02 | Legal subject and authority snapshot / identity | Tenant/entity key, verified identity reference, actor, mandate, action, scope, valid interval, evidence reference; versioned/restricted | ONB-02, ONB-07 |
| ONB-D03 | Capability policy and readiness / policy/onboarding | Policy version, phase, dimension, result, source, observedAt, validUntil, next action; append decision history | ONB-03/04/06 |
| ONB-D04 | Trust reference / trust | Purpose, material reference/version, readiness, next recheck; never key bytes | ONB-03/06 |
| ONB-D05 | Subscription and connection / respective owner | Operator, terms/entitlement, environment, transport/profile, independent state, credential reference | ONB-05/06 |
| ONB-D06 | Entry-point intent/observation / operator adapter | Direction/scope, intended value, external reference, observed value/source/time, safety class, operation ID | ONB-06/08 |
| ONB-D07 | Route transition / route | From/to route, expected version, effective boundary, approval, observed state, rollback case and outcome | ONB-07/09 |
| ONB-D08 | Invoice origin / exchange/records | Invoice ID, original operator/route/profile, route version, accepted time and external correlations; immutable | ONB-07/09, offboarding |
| ONB-D09 | Recovery/evidence case / operations | Fault class, original operation, intended/observed state, owner, safe action, evidence with sensitive values removed and audit timeline | ONB-08 |

Retention and deletion periods are set by approved legal, privacy, contract and evidence policy per data class; none are inferred here. D02/D04/D05 references are access controlled. D08 remains available to explain later statuses and reports after route change. All records include tenant/entity/environment partition keys and audit attribution.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

### 1 Verification matrix

| Scenario | Requirement → activities / contracts | Evidence and expected result |
|---|---|---|
| ONB-A01 Direct public readiness | R01–03 → ONB-01–04 / INT-01–04, D01–04 | One entity/capability returns evidenced readiness or precise limitation; no private route changes. |
| ONB-A02 Accountant partial portfolio | R01–04 → ONB-01–04 / INT-01–03, D01–03 | One invalid client remains blocked; authorised clients continue; no shared grant or credential inference. |
| ONB-A03 Corrected NIF or grant | R01–03, R10 → ONB-02/03 / INT-02–04 | New evidence revision is checked; earlier decision and external operation remain auditable. |
| ONB-A04 Configure private without activation | R05 → ONB-05/06 / INT-05/06, D05–07 | Existing inbound/outbound routing is unchanged through tests and failure. |
| ONB-A05 Scoped cutover | R06/07/09 → ONB-06/07/09 / INT-06/07, D06–08 | Only authorised direction changes after evidenced boundary; earlier invoices retain origin. |
| ONB-A06 Publication timeout | R08/10 → ONB-08 / INT-08, D06/09 | Outcome unknown is visible; no second mutation until observed or manually resolved. |
| ONB-A07 Overlapping transitions | R07 → ONB-07 / INT-07, D07 | Only one transition passes the expected-version check. The other receives a conflict or waits in the queue; both cannot activate overlapping routes. |
| ONB-A08 Rollback after live invoices | R07–10 → ONB-08/09 / INT-07–09, D07–09 | Restoration has new evidence; invoices on each side keep actual route. |
| ONB-A09 Country-bound onboarding reuse | R01–03/06/10 → ONB-02/03/06, INT-02–04/06, D02/03/06 | The same workflow selects separate approved country policies. Spain identity and entry-point rules do not run for another country; missing local policy blocks readiness or activation. Existing Spain evidence remains unchanged. |

### 2 Review and release gates

**Reviewable now:** logical separation, lifecycle, failure model and proposed contracts. **Public pilot gate:** approved capability/representation and external API policy; authority and conditional trust policy; per-client isolation, cancellation and unknown-outcome drills. **Private pilot gate:** selected operator and provider capability matrix; verified entry-point mechanism/sequence; observed readiness and scoped route granularity; historical obligations decision table; rollback and concurrent-cutover drills. **Production gate:** approved legal/operator terms, threat review, conformance evidence, support runbooks and ownership, measured service objectives and monitoring, retention policy, and passed end-to-end pilot evidence.

Open decisions in Part 1 must be recorded with owner, source, date and accepted outcome before their dependent paths are enabled. Where the official interface or legal actor is unknown, the product exposes a blocked/manual gate and does not assert that onboarding is complete.
