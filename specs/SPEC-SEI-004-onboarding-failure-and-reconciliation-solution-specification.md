---
id: SPEC-SEI-004
title: Onboarding Failure and Reconciliation Solution Specification
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
  - PRD-SEI-105
  - PRD-SEI-107
  - PRD-SEI-215
  - PRD-SEI-225
  - PRD-SEI-226
  - SPEC-SEI-002
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Onboarding Failure and Reconciliation Solution Specification

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices still need review; **open** decisions still need an owner’s recorded answer. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### 1 Purpose and design status

This **proposed logical design** explains what happens when public-platform onboarding fails or its result is uncertain. It covers identifying the problem, correcting data, retrying safely, cancelling work and checking what the external system actually did. [PRD-SEI-107](../prds/PRD-SEI-107-public-onboarding-failure-recovery.md) owns the product requirements. [SPEC-SEI-002](SPEC-SEI-002-onboarding-solution-specification.md) owns the parent onboarding journey and capability readiness; this spec owns what happens when one of its operations fails or may have succeeded without a reliable response. [PRD-SEI-225](../prds/PRD-SEI-225-operations-resilience-support-reconciliation.md) supplies shared operations principles.

This design does not assign any unverified public-platform operation a safe retry class or assert an external endpoint, timeout, rate limit or retry count.

Each business and capability gets an accurate status and a clear next action. A network or HTTP status alone cannot prove success, failure or whether retry is safe. An accountant’s portfolio shows mixed results, while each client recovers independently.

If an external change may have happened, the result stays unresolved until a reliable source confirms it or an authorised person makes an approved decision supported by evidence.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Capture, classify and hold unknown results | Record the original attempt, separate problem category from retry safety, and show each client’s actual result. | Reusable unchanged | Reuse the evidence and safety patterns; an unknown external effect stays unresolved. Recovery owner and Operations. |
| Retry and reconciliation | Retry safe Spain onboarding operations or check the original external result before repeating a change. | Reusable with country binding | Bind the exact provider operation, idempotency guarantee, query support, budgets and approved error mapping. Integration owner and Operations. |
| Spain public-platform recovery | Map the confirmed public-solution errors, authority corrections and cancellation rules. | Country-specific | Official operation and response semantics remain an evidence gate. Spain technical owner, Compliance and Product. |
| Existing recovery implementation | Assess scheduler, error catalogue, case handling and adapter observation support. | Unknown | This spec establishes logical behaviour, not a proven deployed recovery service. Check interfaces and failure evidence first. Architecture and integration owner. |

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
| External mutation | An operation that changes another system, such as registering a business. A timeout may leave its result unknown. |
| Retry budget / backoff / jitter | Limits on retry attempts and elapsed time; waiting between attempts; and varying that wait to avoid many retries at once. |
| Portfolio item | One client’s work item. Other clients do not share its permission, retry limits or result. |
| Correlation / input digest | A reference linking related requests and results; a fingerprint used to detect changes in the input. |

### 2 Endpoints and responsibility

| Outcome | Meaning | Owner |
|---|---|---|
| Corrected and ready | A new input/evidence revision passes the parent onboarding gates | Customer/delegate corrects; onboarding decides |
| Waiting safe retry | Approved read-only or contractually idempotent operation is scheduled under a versioned budget | Recovery scheduler |
| Outcome unknown / reconciling | Original mutation may have occurred; readiness is unconfirmed and repetition blocked | Integration + operations |
| Action required | Validation, authority, authentication or policy issue has a specific actor and action | Customer, credential custodian or policy owner |
| Escalated recoverable | Retry budget exhausted or authoritative state unavailable, with owned case and preserved intent | Operations/provider |
| Cancelled | Pending safe work stopped and no unresolved external mutation is hidden | Onboarding + recovery |

### 3 Process diagrams

**Classify and recover:** ![Onboarding failure classification process](../assets/diagrams/onboarding-failure-classification-process.svg)

[Editable Draw.io](../assets/diagrams/onboarding-failure-classification-process.drawio) · [PNG](../assets/diagrams/onboarding-failure-classification-process.png). Text equivalent: OFR-01 records the failed operation and durable intent → OFR-02 classifies fault and operation safety separately → correctable findings go to OFR-03, approved safe retries to OFR-04, uncertain mutations to OFR-05, and security violations to an incident. Exhausted safe retries go to an owned escalation, never to a false permanent rejection.

**Reconcile an uncertain effect:** ![Onboarding reconciliation process](../assets/diagrams/onboarding-uncertain-outcome-process.svg)

[Editable Draw.io](../assets/diagrams/onboarding-uncertain-outcome-process.drawio) · [PNG](../assets/diagrams/onboarding-uncertain-outcome-process.png). Text equivalent: OFR-05 freezes the original operation and blocks repeats → OFR-06 queries an authoritative source using the original correlation and environment → proven success is committed once, proven absence may permit OFR-04 under the approved contract, and unresolved state becomes OFR-07 with owner, evidence and deadline → OFR-08 updates only the affected client/capability and the portfolio aggregate.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Primary owner |
|---|---|---|
| OFR-01 Capture | Operation intent, attempt, correlation and input digest are durable before possible side effect | Onboarding/integration |
| OFR-02 Classify | Stable fault category, operation safety, business result and safe action are distinct | Recovery policy |
| OFR-03 Correct | New customer/authority/policy evidence revision is linked; unchanged input is not retried | Product + relevant actor |
| OFR-04 Retry safely | Same logical identity under approved contract, budget and cancellation check | Scheduler/adapter |
| OFR-05 Hold unknown | Possible mutation is marked OUTCOME_UNKNOWN; no duplicate mutation or readiness claim | Integration |
| OFR-06 Reconcile | Authoritative observed state is linked to original attempt | Adapter/operations |
| OFR-07 Escalate | Unresolved or exhausted work gets owner, evidence, deadline and manual gate | Operations |
| OFR-08 Publish | Item and parent aggregate reflect actual mixed outcomes; notification with sensitive values removed follows commit | Onboarding/product |

### 5 Open decisions

| Decision and effect | Owner / gate |
|---|---|
| Official public-solution operations, idempotency scope, state query and response semantics determine the safety class | Spain technical/regulatory owner; integration design |
| Approved attempt and elapsed budgets, provider guidance, concurrency and freshness targets determine scheduling | Platform Operations + provider; pilot |
| Legal/authority rules for correction and cancellation after an external effect determine terminal handling | Spain Legal/Compliance + Product; design |
| Which client-visible reasons and support diagnostics are safe determine the error catalogue | Product, Privacy/Security, Support; UX/security review |
| Manual proof and approval threshold where no authoritative query exists determine whether a capability can be automated | Operations + Compliance; pilot |

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Scope model and invariants

The recovery key is (tenant, legalSubject, environment, onboardingCase, capability, operationKind, inputRevision). A portfolio batch is only an aggregate; it cannot lend authority, credentials, retry budget or success to another client. Proposed operation safety classes are LOCAL_DETERMINISTIC, EXTERNAL_READ_ONLY, CONTRACT_IDEMPOTENT_MUTATION, RECONCILABLE_MUTATION and UNKNOWN_MUTATION. Only an approved, versioned external contract can place an operation in the latter three classes.

| ID | Rule that must always hold |
|---|---|
| OFR-I01 | A 4xx/5xx, timeout or closed socket is evidence about transport, not a complete business outcome. |
| OFR-I02 | Automatic retry requires a proven safety class, unchanged logical identity, current authority/environment and an approved policy budget. |
| OFR-I03 | A possible external mutation remains OUTCOME_UNKNOWN until original-state observation or approved manual disposition; no fresh mutation or READY state is inferred. |
| OFR-I04 | Correcting data/authority creates a new revision; original request, attempt and decision remain reproducible. |
| OFR-I05 | Cancellation stops queued safe work but cannot erase an uncertain external side effect. |
| OFR-I06 | One client/capability failure cannot roll back or promote another portfolio item. |
| OFR-I07 | Error payloads, metrics, logs and notifications contain no full tax identifiers, names, credentials or raw confidential provider body. |

### 2 Detailed behaviour

**OFR-01 Capture durable intent.** Before calling an external system, save the case and item, tenant, business, environment, capability, actor and authority snapshot. Also save the operation kind, safety-policy version, request fingerprint, idempotency key and correlation reference.

If saving fails before transmission, classify INTERNAL with no external effect only when a control proves that the request could not have been sent. If transmission may have happened, recover the saved intent, outbox or adapter correlation and enter OFR-05. A duplicate request returns the existing item. The same key with a different fingerprint returns a conflict.

**OFR-02 Classify.** Classify two things separately: the problem and whether the operation can safely be repeated. Problem categories are VALIDATION, AUTHENTICATION, AUTHORITY, POLICY, CONFLICT, THROTTLE, TRANSIENT_DEPENDENCY, OUTCOME_UNKNOWN, INTERNAL and SECURITY.

Keep the original provider code in controlled storage with the mapping version. Return a stable Sage reason, responsible actor and safe next action. A definite validation or authority problem produces ACTION_REQUIRED. An unclassified provider result must not be treated as safe to retry. Deny and audit a security or environment mismatch; do not queue it.

**OFR-03 Correct.** A customer or validated delegate can amend only their own entity/capability item. New subject data, mandate, credential reference or policy evidence increments inputRevision and triggers the relevant parent onboarding gate again. Unchanged invalid data cannot enter an automatic loop. If old revision has an uncertain external effect, it remains under OFR-05/06 while the new revision is held from conflicting mutation. Preserve the original failure and correction lineage for support.

**OFR-04 Retry safely.** Eligible reads or contractually idempotent mutations use the same operation identity/key and approved adapter semantics. The scheduler checks cancellation, current authority, environment, provider guidance, attempt/elapsed budget, load and temporary lock for the affected scope before dispatch. Bounded backoff/jitter values are configuration, not guessed compliance constants. An exhausted budget creates OFR-07; it does not prove external absence. Manual retry is subject to the same checks and audit.

**OFR-05 Hold unknown.** A timeout after possible mutation, lost response, uncertain provider code or persistence failure after possible success records OUTCOME_UNKNOWN on that operation and blocks dependent readiness or terminal cancellation. Freeze original request hash, operation ID, provider reference if known, policy/adapter version and transmission timing. A lock prevents concurrent correction/retry from creating a second effect for overlapping scope.

**OFR-06 Reconcile.** Check reliable provider or public-platform state using the same business, environment and original correlation reference. Compare the intended and observed values under the applicable contract.

CONFIRMED_SUCCESS records the original effect once and resumes onboarding checks. CONFIRMED_ABSENT permits a controlled retry only when the provider contract accepts that evidence as sufficient proof of absence. CONFLICT and UNRESOLVED stay on hold, with evidence and an escalation owner.

An empty or failed query does not prove that nothing happened. Save a versioned reconciliation result and ensure repeated checks do not create an additional effect.

**OFR-07 Escalate.** Open a case when a safe budget expires, no authoritative query exists, observed state conflicts or age breaches the approved objective. Include affected item, fault domain, deadline exposure, original operation, last observation, unsafe actions, provider contact and message safe to show to the customer. An authorised manual decision must cite evidence and approver; it cannot overwrite actual external state. Security incidents use the incident path.

**OFR-08 Publish.** Persist state before emitting item-change notification. The customer sees ACTION_REQUIRED, WAITING_RETRY, OUTCOME_UNKNOWN/RECONCILING, READY_WITH_LIMITATIONS or READY with next action, without raw identifiers. A portfolio aggregate counts each state and never collapses unknown into failed or complete. Notification consumers deduplicate by item version; loss of notification is repaired by querying the authoritative item.

### 3 Requirements and quality controls

| ID | Requirement / source |
|---|---|
| OFR-R01 | Classify business category and operation safety separately; PRD-SEI-107 FR1–4. |
| OFR-R02 | Version retry policy and preserve idempotency/correlation across safe attempts; FR5–7. |
| OFR-R03 | Hold and reconcile ambiguous mutations before retry/success; FR8–9/12. |
| OFR-R04 | Escalate exhausted/unresolvable work without false terminal conclusion; FR10. |
| OFR-R05 | Deduplicate requests and version concurrent revisions; FR11/13. |
| OFR-R06 | Isolate portfolio recovery and cancellation by item; FR14–15. |
| OFR-R07 | Apply tenant, authority, environment, security and audit controls to manual action; FR16–17. |
| OFR-R08 | Provide stable safe customer/support status, correlation and policy version; FR18–20. |

Durable intent and idempotency records must survive restart and cover the approved duplicate window. Monitoring covers unknown age, retries, reconciliation lag, partial batches and missing owners without high-cardinality personal identifiers. Targets and retention follow approved operational/legal policy and measured pilot baselines.

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Share the error categories, original-operation record and recovery-state model. Select retry safety, code mapping, budgets and observation support by the approved external contract, country and environment. A read or mutation proven safe for one provider does not establish safety for another. Keep an unverified operation on hold or under a named manual gate.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Interaction contracts

These are logical operations, not approved endpoints. Commands carry caseId, itemId, tenant/entity/environment, actor, inputRevision, operationId, idempotencyKey, expectedVersion and correlation as applicable. Results include stable category, safety class, state, owner, next action, evidence reference and mapping/policy version.

| ID | Caller → owner | Contract and meaning of failures and recovery rules |
|---|---|---|
| OFR-INT-01 | Onboarding → recovery | Register intent/attempt before side effect; return durable operation identity or reject dispatch. |
| OFR-INT-02 | Adapter → recovery | Report transport/provider result with original code, transmission phase and safety evidence; mapping produces classified result. |
| OFR-INT-03 | Product → onboarding/recovery | Submit corrected input/evidence revision or cancel; expected-version and authority enforced; uncertain old effect remains held. |
| OFR-INT-04 | Scheduler → adapter | Retry only under approved safety/budget with same idempotency scope; return definitive/unknown result. |
| OFR-INT-05 | Recovery → adapter | Query original mutation state by operation/reference; return observed value, source, time and confidence. |
| OFR-INT-06 | Operations → recovery | Record manual reconciliation or escalation decision with approver, evidence and constrained action. |
| OFR-INT-07 | Recovery → onboarding/product | Publish committed item/aggregate change; at-least-once event, consumer deduplicates by item/version. |

Proposed events are ONBOARDING_ATTEMPT_CLASSIFIED, ONBOARDING_RECONCILIATION_REQUIRED, ONBOARDING_ITEM_RECOVERED and ONBOARDING_RECOVERY_ESCALATED. An event is a notification, not evidence that an external mutation completed.

### 2 Data inventory

| ID | Record / owner | Key fields, classification and consumers |
|---|---|---|
| OFR-D01 | Recovery item / onboarding | Tenant/entity/environment, capability, state/version, parent batch, owner, next action; restricted; OFR-01–08. |
| OFR-D02 | Operation intent/attempt / recovery | Immutable operation ID, input hash, authority snapshot, safety class/policy, adapter version, transmission phase, timestamps; restricted; OFR-01/04–06. |
| OFR-D03 | Error catalogue/mapping / policy | Stable Sage code, provider code mapping, fault domain, safe guidance, version/effective period; controlled; OFR-02/08. |
| OFR-D04 | Retry schedule / recovery | Same idempotency scope, attempt/elapsed budget, next eligibility, lease, cancellation flag; restricted; OFR-04/07. |
| OFR-D05 | Reconciliation observation / adapter | Original operation, authoritative source, observed value, time, reference, conclusion and evidence; append-only; OFR-05/06. |
| OFR-D06 | Correction lineage / onboarding | Prior/new input revision, changed evidence reference, actor, authority, reason; restricted; OFR-03. |
| OFR-D07 | Escalation case / operations | Fault, owner, deadline, unsafe actions, provider contact, manual approval and audit; restricted; OFR-07. |
| OFR-D08 | Aggregate/notification / onboarding | Child counts/versions and redacted event ID; derived/rebuildable; OFR-08. |

Exact retention periods are open; preserve D02/D05/D06 sufficiently to explain outcomes and avoid duplicate effects under the approved legal/operational policy. Store references rather than credentials or raw provider bodies in user-facing records.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

| Scenario | Requirement → activity / interaction / data | Expected evidence |
|---|---|---|
| OFR-A01 Local invalid data | R01/07 → OFR-02/03, INT-02/03, D03/06 | No external call or unchanged retry; safe correction action. |
| OFR-A02 Safe read throttled | R01/02 → OFR-02/04, INT-02/04, D02/04 | Same correlation; approved budget/provider guidance; other clients fair. |
| OFR-A03 Mutation timeout | R03 → OFR-05/06, INT-05, D02/05 | OUTCOME_UNKNOWN, no repeat or READY claim until observed. |
| OFR-A04 External success, local persistence failure | R03 → OFR-01/05/06, INT-01/05, D02/05 | Original effect committed once from durable intent/observation. |
| OFR-A05 Budget exhausted | R04 → OFR-07, INT-06, D04/07 | Owned recoverable case, no false external absence. |
| OFR-A06 Duplicate and stale revision | R05 → OFR-01/03, INT-01/03, D01/06 | Existing result or explicit conflict; no second effect. |
| OFR-A07 Mixed accountant portfolio | R06/08 → OFR-08, INT-07, D01/08 | Independent child outcomes and accurate aggregate. |
| OFR-A08 Cancel while unknown | R03/06 → OFR-05/06/08, INT-03/05, D01/05 | Safe queued work stops; case remains reconcilable. |
| OFR-A09 Manual retry and redaction | R07/08 → OFR-07/08, INT-06/07, D03/07 | Authority/environment enforced; support view lacks raw identity/secrets. |
| OFR-A10 Provider and country safety isolation | R01–03/07/08 → OFR-02/04–06, INT-02/04/05, D02–05 | A safe retry class for one approved contract is not inherited by another country or provider. Missing local safety evidence prevents automatic repeat; the original operation remains traceable and the next action has an owner. |

**Review gate:** confirm operation inventory, safety classes, external state-query evidence and error catalogue. **Pilot gate:** prove correction, safe retry, uncertain mutation, persistence loss, cancellation, partial portfolio and manual-action drills against the selected integration. **Production gate:** approved budgets, monitoring/ownership, redaction, retention and measurable recovery objectives. Until official semantics are proven, mutation automation stays disabled or uses a named manual gate.
