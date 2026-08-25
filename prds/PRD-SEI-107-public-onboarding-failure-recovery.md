---
id: PRD-SEI-107
title: Phase 1 — Public Onboarding Failure and Recovery
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-25
updated: 2026-08-25
reviewers: []
related:
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-105
  - PRD-SEI-106
  - PRD-SEI-215
  - PRD-SEI-225
  - PRD-SEI-226
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837610648"
  page_id: "848078012"
  title: "Retry & Error Handling Specs (Phase 1: Public Platform Onboarding)"
  layout: two_left_sidebar
  toc: true
---

# Phase 1 — Public Onboarding Failure and Recovery

## Decision summary

Phase 1 onboarding recovery is governed by operation safety, not HTTP status alone. A request may be retried automatically only when the operation is known to be read-only or the external contract provides an effective idempotency guarantee. If a mutating request may have reached the external service, the work enters `OUTCOME_UNKNOWN` and must reconcile authoritative state before retry or success.

Validation findings, authentication/authority denial, policy rejection, transient dependency failure, throttling, ambiguous mutation and internal persistence failure are separate categories with different owners and recovery actions.

Portfolio batches complete independently by client item. Exhausting a retry budget does not automatically prove permanent failure or absence of an external mutation.

> **Product principle:** Retry only what is safe; reconcile what is uncertain; never make the customer guess what happened.

This document owns onboarding-specific error contracts, operation-safety classification and recovery. Shared resilience, support and reconciliation remain in PRD-SEI-215/225.

## Source relationship

This is the canonical Git source proposed for [Retry & Error Handling Specs (Phase 1: Public Platform Onboarding)](https://confluence.sage.com/spaces/DNBU/pages/848078012/Retry+Error+Handling+Specs+Phase+1+Public+Platform+Onboarding), reviewed at version 4. It preserves error categories, correlation, retry and webhook ideas while removing unsupported provider codes, fixed timings, raw rejected identifiers and false terminal-state assumptions.

### Original draft detail disposition

| Original detail | Treatment in this canonical source |
|---|---|
| 4xx synchronous, 5xx transient and terminal categories | Preserved as transport inputs but replaced by business category plus operation-safety decision |
| Fifteen-second socket timeout | Not approved; timeout values require external contract/capacity evidence |
| Provider `429`, `503`, `504`, certificate and registration errors | Retained as scenario categories only; exact provider mapping requires technical artefacts |
| `PENDING_REGISTRATION` to `REGISTERED` | Replaced by onboarding/readiness states until an external registration contract is proven |
| Five attempts, ten-second base and fifteen-minute cap | Replaced by versioned operation/environment retry budgets with owner/baseline |
| Retry exhaustion becomes `FAILED_CRITICAL` | Replaced by an owned recoverable/escalated result; uncertain mutation remains `OUTCOME_UNKNOWN` |
| Error payload includes raw `rejected_value` | Replaced by redacted evidence reference and secure authorised detail |
| Draft endpoint path and `target_platform` | Preserved only as conceptual case/capability/environment context; transport is not approved |
| Webhook/correlation | Preserved as delivery-neutral notification/correlation capabilities with tenant/security controls |

## Outcome and operation-safety classes

| Class | Definition | Automatic retry | Reconciliation |
|---|---|---|---|
| Local deterministic | No external side effect; same input/policy yields same result | Not needed after business failure; safe after infrastructure failure | Internal durable state only |
| External read-only | Confirmed not to mutate provider state | Permitted under approved contract/budget | Optional confirmation after prolonged ambiguity |
| Idempotent mutation | Contract guarantees same idempotency scope cannot duplicate effect | Permitted with same key/correlation after approved conditions | Required when response remains ambiguous |
| Reconcilable mutation | May mutate; authoritative query/reference can prove outcome | Not until reconciliation shows absence or contract permits | Mandatory |
| Non-reconcilable/unknown | Mutation semantics or authoritative query are not evidenced | Never automatically | Manual/provider escalation; capability cannot claim success |

No public-solution onboarding mutation is assigned a safe class until official technical evidence proves the operation and its semantics.

## Error taxonomy

| Category | Examples | Responsible actor | Typical response |
|---|---|---|---|
| `VALIDATION` | Invalid NIF check character, missing subject type | Customer/product | Correct input; no retry loop |
| `AUTHENTICATION` | Invalid/expired credential | Credential custodian/security | Renew/rebind credential |
| `AUTHORITY` | Missing, denied, expired or revoked grant | Client/accountant/legal | Supply/restore valid authority |
| `POLICY` | Unsupported capability/cohort, unresolved baja/revoked rule | Product/compliance | Review rule/evidence |
| `CONFLICT` | Stale revision, concurrent overlapping change | Caller/platform | Refresh and retry deliberately |
| `THROTTLE` | Confirmed rate limit | Platform/operations | Respect provider guidance and queue |
| `TRANSIENT_DEPENDENCY` | Network/unavailable/confirmed retryable provider fault | Platform/provider | Safe bounded retry |
| `OUTCOME_UNKNOWN` | Timeout/internal loss after possible mutation | Platform/provider | Reconcile before repeat/success |
| `INTERNAL` | Persistence/queue/configuration defect | Sage engineering/operations | Recover durable intent; reconcile external state |
| `SECURITY` | Cross-client/environment attempt | Security | Deny, audit and incident handling |

## Business scenarios

| ID | Scenario | Expected outcome |
|---|---|---|
| S1 | Local validation fails | Immediate field-level correction; no external call/retry |
| S2 | Authority is denied | Capability remains action-required/denied; other authorised capabilities continue |
| S3 | Read-only census lookup times out | Safe retry only under confirmed service policy; otherwise pending/recoverable |
| S4 | Future registration-like mutation times out | `OUTCOME_UNKNOWN`; reconcile official state before retry |
| S5 | Provider throttles portfolio work | Queue and schedule within confirmed limits; preserve per-item state |
| S6 | Retry budget expires | Work is escalated/recoverable, not falsely marked absent or permanently failed |
| S7 | Internal persistence fails after external success | Recover from durable intent/correlation and query authoritative outcome |
| S8 | Duplicate client/batch request arrives | Existing logical work/result is returned; no duplicate external action |
| S9 | Batch has mixed outcomes | Safe items complete; aggregate reflects partial/action-required/unknown items |
| S10 | Customer cancels during retry | Stop scheduled safe retries; reconcile any uncertain mutation before terminal cancellation |
| S11 | Operations manually retries | Same safety, authority, environment, idempotency and audit rules apply |
| S12 | Error payload is exposed to product/webhook | Safe stable category/reason/correlation only; identifiers/secrets are redacted |

## Business rules

| ID | Condition | Rule | Status |
|---|---|---|---|
| BR1 | Error occurs | Classify fault domain, operation safety, retryability and customer action separately | Proposed shared control |
| BR2 | 4xx/5xx is received | Do not derive business permanence or retry safety from status family alone | Integration principle |
| BR3 | Business validation/authority fails | Wait for correction/evidence; do not retry unchanged request automatically | Proposed |
| BR4 | Operation is read-only/idempotent by approved evidence | Retry under versioned budget/jitter/provider guidance | Open numerical policy |
| BR5 | Mutation outcome is ambiguous | Enter `OUTCOME_UNKNOWN` and reconcile before repetition/success | PRD-SEI-215 |
| BR6 | Retry budget exhausts | Escalate/recover; do not assert mutation absence | Proposed |
| BR7 | One portfolio item fails | Preserve independent item results and continue other safe work | PRD-SEI-104 |
| BR8 | Customer cancels | Stop safe pending work; uncertain external work remains reconcilable | Proposed |
| BR9 | Error evidence is surfaced | Redact NIF/NIE, names, credentials and raw confidential payloads | PRD-SEI-226 |
| BR10 | Provider contract/version changes | Version error mapping/retry policy prospectively; preserve historical context | Historical continuity |

## Scope and non-goals

### In scope

- Onboarding error taxonomy and safe customer/operator contract.
- Operation-safety classification and retry eligibility.
- Idempotency, duplicate detection, retry budget and backoff decision surface.
- Outcome-unknown state and reconciliation requirements.
- Direct/portfolio partial outcomes, cancellation and manual recovery.
- Redaction, correlation, observability, escalation and versioning.

### Non-goals

- Inventing AEAT/public-solution endpoints, codes, retry-after behaviour, socket timeouts or SLAs.
- Setting five retries, ten-second base or fifteen-minute cap without evidence/capacity approval.
- Echoing rejected tax identifiers in error payloads.
- Owning the enterprise-wide resilience platform implementation.
- Retrying invoice submission/retrieval operations outside onboarding; those PRDs apply the shared model.

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| Confluence page 848078012 v4 | Draft 4xx/5xx/terminal taxonomy, retry/backoff, correlation and webhook behaviour | Internal discovery; provider errors/numbers unverified | Preserve intent, replace unsafe assumptions |
| PRD-SEI-215 | Operation safety, outcome unknown, reconciliation-first recovery | Shared structured-review requirements | Core safety contract |
| PRD-SEI-225 | Operations, support, evidence and reconciliation | Shared discovery requirements | Operational handoff |
| PRD-SEI-226 | Credential, identity, privacy, audit and redaction | Shared security requirements | Error/evidence safety |
| [Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238) | Technical public-solution contracts depend on ministerial order | Primary regulation; no retry/error contract in decree | External mappings/numbers remain open |

## Proposed work-item lifecycle

| State | Meaning | Exit |
|---|---|---|
| `RECEIVED` | Durable logical request exists | Validate/schedule |
| `VALIDATING` | Local/context/authority controls running | Action required, external pending or ready |
| `ACTION_REQUIRED` | Correctable business/authority/policy issue | New evidence/revision/cancel |
| `WAITING_RETRY` | Confirmed safe retry scheduled | Retry/cancel/escalate |
| `OUTCOME_UNKNOWN` | External mutation may have occurred | Reconciliation only |
| `RECONCILING` | Authoritative state is being determined | Ready/action required/still unknown |
| `READY` | Requested onboarding capability controls passed | Re-evaluate on expiry/change/suspend |
| `READY_WITH_LIMITATIONS` | Named capability limitations remain | Resolve limitation/re-evaluate |
| `SUSPENDED` | Future use blocked by policy/security/authority/credential change | Approved recovery/re-evaluation |
| `CANCELLED` | Safe work stopped and no unresolved mutation remains | Terminal for this revision |

`FAILED_CRITICAL` is not used as a catch-all. Terminal/recoverable meaning must be explicit and must not hide uncertain external state.

## Proposed error contract

Transport remains an architecture decision. A safe error/result contains:

- stable category and product reason code;
- affected case/item/capability reference;
- environment and correlation reference;
- retryability and safe next action;
- responsible actor/fault domain;
- retry/reconciliation status and next eligible time where applicable;
- redacted evidence/support reference.

It does not contain full NIF/NIE, names, credentials, certificate metadata, raw authority documents or confidential provider payloads.

## Detailed journeys

### J1 — Correctable validation

1. Local control returns a versioned validation finding.
2. Work becomes `ACTION_REQUIRED`; no unchanged automatic retry runs.
3. Product shows responsible field/actor and safe reason.
4. Correction creates a new input/evidence revision and resumes the same logical case.

### J2 — Safe transient retry

1. Approved read-only/idempotent operation returns a retryable condition.
2. Retry policy considers provider guidance, attempt budget, elapsed budget, queue/load and cancellation.
3. Same correlation/idempotency scope is preserved.
4. Success or business response completes mapping; exhaustion escalates without inventing permanence.

### J3 — Outcome unknown

1. Mutating request times out after possible transmission or internal persistence fails after response.
2. Work enters `OUTCOME_UNKNOWN` and readiness remains unconfirmed.
3. Reconciliation uses official query/reference/correlation under the same environment/authority.
4. Confirmed success is persisted; confirmed absence may allow safe retry; unresolved state escalates.

### J4 — Portfolio partial recovery

1. Batch items fail in different categories.
2. Validation/authority items await client action, safe transient items retry, unknown items reconcile and completed items remain complete.
3. Batch aggregate reflects mixed states without rolling back independent successes.
4. Accountant sees only authorised, redacted item results.

### J5 — Cancellation

1. Authorised actor requests cancellation.
2. Queued safe work and scheduled retries stop.
3. In-flight read-only work may finish/discard per policy; ambiguous mutation reconciles.
4. Case becomes `CANCELLED` only when unresolved external mutation no longer exists.

## Functional requirements

| ID | Requirement |
|---|---|
| FR1 | Every failure must carry stable category, reason, fault domain, operation-safety class, retryability and safe next action. |
| FR2 | HTTP/transport status alone must not determine business result, permanence or retry eligibility. |
| FR3 | Business validation/authority/policy failures must not retry automatically without changed input/evidence/policy. |
| FR4 | Every external operation must have an approved safety classification before automatic execution/retry. |
| FR5 | Retryable operations must preserve logical correlation and idempotency scope. |
| FR6 | Retry policy must be versioned and configurable by operation/environment/contract, including attempt and elapsed budgets, backoff/jitter and provider guidance. |
| FR7 | The service must not hard-code unsupported provider limits/timeouts/retry counts as compliance requirements. |
| FR8 | Ambiguous mutation must enter `OUTCOME_UNKNOWN` and block success/terminal failure until reconciliation or approved escalation. |
| FR9 | Reconciliation must use authoritative external state/reference where available and preserve original context. |
| FR10 | Exhausting retry budget must create an owned escalation/recoverable outcome, not assert external absence. |
| FR11 | Duplicate direct, batch and item commands must return existing logical work or conflict safely without repeating effects. |
| FR12 | Internal failure after possible external success must recover durable intent/correlation and reconcile. |
| FR13 | Concurrent conflicting revisions must be serialized/version-checked. |
| FR14 | Portfolio recovery must be independent by client item/capability and expose accurate aggregate state. |
| FR15 | Cancellation must stop safe work but retain/reconcile uncertain effects before terminal completion. |
| FR16 | Manual retry/reconcile/cancel must enforce original tenant, client, authority, environment and audit controls. |
| FR17 | Error payloads/logs/metrics/webhooks must redact sensitive identities, names, credentials and raw provider content. |
| FR18 | Products must distinguish customer-correctable, pending retry, provider fault, Sage fault and outcome unknown in plain language. |
| FR19 | Operations must see queue/retry age, attempts, next action, correlation, fault domain and redacted evidence. |
| FR20 | Error/status mappings and retry policy must be versioned so historical behaviour remains explainable. |

## Failure matrix

| Condition | Retry? | Reconcile? | Outcome/owner |
|---|---:|---:|---|
| Invalid NIF format/check character | No | No | Customer correction |
| Missing/expired authority | No | No | Client/accountant/legal evidence |
| Invalid credential before transmission | No unchanged retry | No | Credential custodian |
| Confirmed throttle on safe call | Yes, per contract | If ambiguity remains | Platform/provider |
| Connection failure before transmission | Yes if operation class allows | Usually no | Platform |
| Timeout after read-only request | Yes per contract | Optional | Platform/provider |
| Timeout after possible mutation | No blind retry | Yes | Platform/provider |
| Duplicate request | No new execution | Existing correlation | Platform |
| Internal persistence failure after external response | No blind retry | Yes | Sage operations/engineering |
| Concurrent stale update | Deliberate after refresh | No | Caller/platform |
| Security/environment violation | No | Incident review | Security |

## Non-functional requirements

- NFR1: Durable work intent and correlation must survive restart and regional failover according to approved architecture.
- NFR2: Idempotency records must have lifecycle/retention sufficient to cover retry and duplicate windows.
- NFR3: Monitoring must cover state age, retry budget, unknown outcome, reconciliation lag and aggregate partial batches.
- NFR4: Alerts must be actionable by fault domain and avoid high-cardinality personal identifiers.
- NFR5: Redacted evidence must support escalation without secrets or unnecessary personal data.
- NFR6: Environment isolation from PRD-SEI-105 applies to every retry/reconciliation/manual action.
- NFR7: Capacity/SLO targets require approved volumes, dependency contracts and baselines.
- NFR8: Customer/accountant messages must be accessible, stable and consistent across channels.

## Acceptance criteria

| ID | Given/when/then |
|---|---|
| AC1 | Given invalid local data, when validation fails, then no unchanged automatic retry/external call occurs and correction guidance is returned. |
| AC2 | Given a 500 response for an operation not classified safe, when handled, then the system does not retry solely because it is 5xx. |
| AC3 | Given an approved read-only call is throttled, when retried, then the same correlation and versioned budget/provider guidance are used. |
| AC4 | Given a mutating request times out after transmission, when handled, then it enters `OUTCOME_UNKNOWN` and cannot report success or be blindly repeated. |
| AC5 | Given reconciliation confirms external success after internal persistence failure, when recovered, then success is recorded once with the original context. |
| AC6 | Given retry budget exhaustion without known mutation, when escalated, then state remains accurately recoverable and does not assert permanent external rejection. |
| AC7 | Given a duplicate batch/item, when received, then existing work/result is returned and no duplicate effect occurs. |
| AC8 | Given mixed batch failures, when status is viewed, then completed, action-required, retrying and unknown items remain independently represented. |
| AC9 | Given cancellation while an outcome is unknown, when requested, then safe retries stop but the case is not terminal until reconciliation/approved escalation. |
| AC10 | Given an error contains a rejected identifier internally, when surfaced/logged/webhooked, then full identity and secret data are absent. |
| AC11 | Given manual retry, when operations initiates it, then original client, authority, environment, safety and audit controls are enforced. |
| AC12 | Given error mapping changes, when historical evidence is viewed, then the mapping/policy version used at the time remains explainable. |

## Measures, gates and open questions

| Measure | Purpose | Owner |
|---|---|---|
| Failures by category/fault domain | Prioritise customer/platform/provider improvements | Product/operations |
| Retry success and budget exhaustion | Tune safe recovery | Engineering/operations |
| Outcome-unknown count and age | Mutation safety | Operations |
| Reconciliation success/lag | Recovery effectiveness | Engineering/operations |
| Duplicate suppression | Idempotency effectiveness | Engineering |
| Redaction/security incidents | Evidence safety | Security/privacy |

Production is gated on official external operation/error/idempotency/rate contracts, approved safety classification, durable orchestration, reconciliation capabilities, operational ownership, redaction/security tests and measured retry/capacity policies.

| Open question | Owner | Blocks |
|---|---|---|
| Which public-solution onboarding operations exist and which mutate state? | AEAT liaison/architecture | Safety matrix |
| What official idempotency, query/reconciliation and retry-after mechanisms exist? | AEAT liaison/engineering | Automated retry/recovery |
| What attempt/elapsed budgets fit external limits and customer expectations? | Engineering/operations/product | Production policy |
| What is the escalation/support path for unresolved external outcomes? | Operations/provider liaison | Production |
| How long must idempotency, work and error evidence be retained? | Legal/privacy/architecture | Data design |

**Readiness: discovery-ready draft.** Local and shared recovery controls can be designed; provider-specific mappings remain blocked by technical artefacts.

## Decisions and change log

| Decision | Status |
|---|---|
| Retry is determined by operation safety, not HTTP family alone | Proposed for approval; shared resilience principle |
| Ambiguous mutation requires reconciliation before retry/success | Proposed for approval |
| No fixed retry count/timing is approved in this PRD | Evidence-led correction |
| Existing Confluence page remains the stable publishing target | Accepted mapping; publication disabled |

| Date | Version | Change | Evidence |
|---|---|---|---|
| 2026-08-25 | Initial canonical draft | Preserved taxonomy/retry/correlation intent; added safety classes, unknown outcomes, reconciliation, partial batches and redaction; removed invented codes/timings | Confluence v4, PRD-SEI-215/225/226, Royal Decree 238/2026 |
