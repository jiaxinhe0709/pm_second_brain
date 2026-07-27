---
id: PRD-SEI-203
title: Spain Private Platform Resilience and Operations
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-07-27
updated: 2026-07-27
reviewers: []
related:
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
---

# Spain Private Platform Resilience and Operations

## Summary

Provide consistent reliability, reconciliation, monitoring, audit, and operational recovery across all Spanish private-platform integrations.

## Problem

Private providers will differ in availability, idempotency, webhook delivery, status semantics, and recovery facilities. A timeout may leave the external outcome unknown, while duplicate retries can create duplicate registrations or invoices. Without shared resilience rules, each adapter will expose different operational risks.

## Reliability principles

1. Retry safety is determined per operation, not per provider.
2. A transport timeout does not prove that an external mutation failed.
3. Provider webhooks are notifications, not automatically trusted state.
4. Reconciliation compares intended, recorded, and externally observed state.
5. Customer-facing messages identify the responsible actor without exposing provider secrets.
6. Manual recovery is a controlled product capability, not an undocumented database correction.

## Goals

- Prevent invoice loss and avoidable duplication.
- Reconcile ambiguous outcomes before unsafe retries.
- Standardise provider health and error classification.
- Give operations actionable recovery tools and audit history.
- Make degraded provider conditions visible without leaking sensitive data.

## Non-goals

- Contractual provider SLA negotiation.
- Automatic switching between private providers.
- Customer offboarding and retention policy.
- Provider-specific recovery endpoints.

## Users and use cases

- Customers receive accurate, actionable degraded-service information.
- ERP products receive stable retryable and non-retryable errors.
- Operations identify provider incidents and recover individual work items.
- Engineering compares provider health using common measures.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | Provider operations must use idempotency controls where supported. |
| FR2 | Ambiguous timeouts must enter an `outcome unknown` state and reconcile before an unsafe retry. |
| FR3 | Retry policies must distinguish transient, permanent, throttling, authentication, validation, and unknown-outcome errors. |
| FR4 | Asynchronous work must support durable queues, bounded retry, and dead-letter handling. |
| FR5 | Webhooks must support authentication, deduplication, ordering tolerance, and replay protection. |
| FR6 | Polling or reconciliation must recover missed webhook events where provider capabilities allow. |
| FR7 | Circuit breaking or equivalent protection must limit cascading provider failures. |
| FR8 | Credential expiry and authentication failures must be detected and surfaced before avoidable outages. |
| FR9 | Operations must be able to inspect, retry, reconcile, and escalate failed work using controlled actions. |
| FR10 | Every recovery action must record actor, reason, time, previous state, and result. |
| FR11 | Logs and operational views must redact secrets, certificate material, and unnecessary invoice content. |
| FR12 | Provider health must be measurable by environment and operation type. |

### Error taxonomy

| Category | Example | Default treatment |
|---|---|---|
| VALIDATION | Unsupported or malformed customer data | Do not retry; return actionable correction |
| AUTHENTICATION | Invalid or expired credentials | Stop affected work; request credential action |
| AUTHORISATION | Account lacks required provider permission | Do not retry until permission changes |
| THROTTLED | Provider rate limit | Retry using provider guidance and bounded backoff |
| TRANSIENT_PROVIDER | Temporary 5xx or service degradation | Retry where operation is safe |
| NETWORK | Connection failure before response | Retry or reconcile according to operation safety |
| OUTCOME_UNKNOWN | Timeout after a mutating request may have been accepted | Reconcile before retry |
| CONFLICT | Provider state conflicts with requested mutation | Inspect/reconcile; do not overwrite blindly |
| PERMANENT_PROVIDER | Provider rejects a supported operation permanently | Stop and escalate/marshal stable error |
| INTERNAL | Sage processing or persistence failure | Recover from durable state; protect against duplicate provider calls |

### Operation safety classification

Every provider operation must be classified:

- **Read-only retryable:** safe to repeat.
- **Idempotent mutation:** safe to repeat with the same provider or Sage idempotency identity.
- **Reconcile-before-retry mutation:** may have succeeded externally; query state first.
- **Manual-decision mutation:** insufficient provider capability for automatic recovery.

The classification, retry limit, reconciliation method, and terminal treatment must be recorded in each provider PRD.

## Failure-mode matrix

| Scenario | Required response |
|---|---|
| Provider unavailable before request is sent | Queue or fail as transient according to operation SLA |
| Connection drops after request is sent | Mark outcome unknown and reconcile |
| Duplicate webhook | Detect provider event identity or semantic duplicate; process once |
| Out-of-order webhook | Compare event version/time and prevent lifecycle regression |
| Webhook authentication fails | Reject, audit, and monitor security signal |
| Webhook never arrives | Poll/reconcile where supported; otherwise raise aged-work exception |
| Provider reports unknown customer | Compare registration state; do not automatically recreate |
| Credential expires | Stop unsafe work, notify responsible actor, preserve queued items |
| Rate limit reached | Respect retry-after/provider policy and protect shared capacity |
| Sage persistence fails after provider success | Recover using correlation/idempotency identity and reconcile |
| Manual retry requested | Show impact and operation safety; require reason and authorisation |

## Operational experience

### Work item view

Operations must be able to see:

- Sage operation and correlation IDs;
- legal entity and provider without unnecessary customer data;
- operation type and environment;
- current Sage state and last known provider state;
- attempt count and next retry time;
- error category and redacted diagnostic;
- whether the outcome is known;
- permitted recovery actions;
- related route, transition, connection, and invoice references;
- complete recovery history.

### Controlled actions

| Action | Guardrail |
|---|---|
| Retry | Allowed only for operations classified safe or after successful reconciliation |
| Reconcile | Read-only where possible; record observed provider state and freshness |
| Cancel queued work | Require impact display and reason |
| Mark resolved | Require evidence/reference and restricted permission |
| Roll back transition | Invoke transition workflow; never directly rewrite route history |
| Disable connection | Show active-route and historical-invoice impact |
| Escalate | Produce a redacted support bundle with correlation references |

## Observability requirements

- Metrics must be segmented by provider, environment, operation, outcome, and error category.
- Alerts must identify sustained provider degradation separately from individual customer misconfiguration.
- Distributed correlation must cover client request, Sage orchestration, adapter call, webhook/event, and reconciliation.
- Dashboards must show backlog age, retry volume, dead-letter volume, unknown outcomes, credential expiry, and state discrepancies.
- Provider payload logging must be allow-listed and redacted.
- Health status must not be derived from a single failed customer request.

## User experience

Customer-facing status should distinguish:

- action required by customer;
- temporary provider delay;
- Sage retry in progress;
- outcome being reconciled;
- operations investigation;
- completed or permanently failed.

Raw provider messages should be retained securely for diagnosis but translated into stable Sage error categories.

## Metrics

| Metric | Initial direction |
|---|---|
| Avoidable duplicate external operations | 0 |
| Avoidable invoice loss | 0 |
| Dead-letter items with owner and reason | 100% |
| Provider incidents detected within agreed monitoring interval | 100% |
| Manual recovery actions with audit event | 100% |
| Credential expiries detected before expiry where metadata is available | 100% |

Additional measures:

- p50/p95/p99 provider operation latency;
- retry recovery rate;
- unknown-outcome age;
- webhook delay and duplicate rate;
- reconciliation discrepancy rate;
- dead-letter backlog age;
- mean time to acknowledge and resolve provider incidents.

## Acceptance criteria

1. A duplicate webhook does not create a second lifecycle event.
2. An out-of-order event cannot regress a terminal invoice state without an explicit allowed transition.
3. A timed-out mutation enters `OUTCOME_UNKNOWN` and is not blindly repeated.
4. A successful reconciliation can complete an operation without resubmitting it.
5. Invalid credentials stop affected calls and create an actionable customer/operations state.
6. Rate-limit responses use bounded provider-aware retry.
7. Dead-lettered work has an owner, reason, correlation identifier, and permitted action.
8. Manual actions are permission-controlled and audited.
9. Logs and support bundles exclude credentials and prohibited invoice data.
10. A provider outage is visible by provider and operation without requiring individual case inspection.

## Rollout

1. Define common error taxonomy and operation states.
2. Implement correlation, audit, idempotency, and retry primitives.
3. Validate unknown-outcome reconciliation with the reference provider.
4. Add provider health dashboards and alerts.
5. Add controlled operational recovery.
6. Apply readiness checks to every subsequent provider.

## Risks

- Retrying a successful but timed-out request.
- Provider webhooks being delayed, duplicated, or reordered.
- Recovery controls causing unauthorised state changes.
- Excessive logging of sensitive invoice or credential data.
- Applying one retry policy to operations with different safety characteristics.

## Open questions

1. What operational SLA applies to ambiguous outcomes and dead-letter items?
2. Which recovery actions may support teams perform without engineering involvement?
3. What customer-visible provider status is commercially acceptable?
4. What evidence and retention are required for operational audit?
5. Which providers offer authoritative reconciliation endpoints?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | Resilience is a shared Phase 2 capability, not a provider-specific afterthought | Proposed |
| 2026-07-27 | Unknown external outcomes must be reconciled before unsafe retry | Proposed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
