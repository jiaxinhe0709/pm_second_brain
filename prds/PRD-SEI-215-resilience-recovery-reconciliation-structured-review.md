---
id: PRD-SEI-215
title: Operations — Resilience, Recovery and Reconciliation — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-203
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
  - research/provider-apis/README.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "837611183"
  title: Operations — Resilience, Recovery and Reconciliation
  layout: two_left_sidebar
  toc: true
---

# Operations — Resilience, Recovery and Reconciliation — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-203, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-215, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-203. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-203; this successor introduces no new product decision. |

## Overview

This feature defines the shared reliability and operational controls required to run all Phase 2 Spanish private-platform connections safely.

The provider portfolio will not behave uniformly. Providers may use different authentication, synchronous/asynchronous responses, webhooks, polling, acknowledgements, status models, idempotency mechanisms and support processes. Sage therefore needs one product-level resilience model that protects invoices and registrations without hiding meaningful provider differences.

> **Retry only when the outcome is known to be safe; reconcile when the outcome is uncertain.**

### Delivery context

| Layer | Responsibility |
|---|---|
| Shared routing foundation — PRD-SEI-202 | Connection, registration, capability readiness, route and invoice context |
| **Shared resilience and operations — PRD-SEI-203** | **Error ownership, operation safety, retry, reconciliation, monitoring, audit and controlled recovery** |
| Provider PRDs — PRD-SEI-204–208 | Provider-specific evidence, mappings, limits and reconciliation mechanisms |

## Product principle

> **A transport error describes what Sage observed; it does not necessarily describe what the provider did.**

A timeout after a mutating request may mean failure, success or an unknown outcome. Treating all three as failure can create duplicate registrations, duplicate invoice submissions or contradictory route state.

## Resilience and recovery visual

<!-- confluence-html-macro:start -->
<div class="ppro-visual" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; padding:24px; background:#fff; border:1px solid #dfe1e6; border-radius:8px; box-sizing:border-box; max-width:1060px; margin:0 auto; overflow-x:auto;">
  <style>
    .ppro-visual { --text:#172b4d; --muted:#6b778c; --border:#dfe1e6; --green:#006644; --green-bg:#e3fcef; --amber:#974f0c; --amber-bg:#fff7d6; --red:#bf2600; --red-bg:#ffebe6; --blue:#0052cc; --blue-bg:#deebff; }
    .ppro-visual * { box-sizing:border-box; }
    .ppro-visual h2 { margin:0; color:var(--text); font-size:18px; }
    .ppro-visual .subtitle { margin:6px 0 18px; color:var(--muted); font-size:12px; }
    .ppro-visual .flow { display:grid; grid-template-columns:190px 34px 210px 34px 210px 34px 230px; align-items:center; min-width:940px; }
    .ppro-visual .node { min-height:84px; padding:12px; border:1px solid var(--border); border-radius:8px; color:var(--text); background:#f4f5f7; font-size:11px; line-height:1.35; text-align:center; }
    .ppro-visual .node strong { display:block; margin-bottom:5px; font-size:12px; }
    .ppro-visual .blue { color:var(--blue); background:var(--blue-bg); border-color:#b3d4ff; }
    .ppro-visual .green { color:var(--green); background:var(--green-bg); border-color:#abf5d1; }
    .ppro-visual .amber { color:var(--amber); background:var(--amber-bg); border-color:#ffe380; }
    .ppro-visual .red { color:var(--red); background:var(--red-bg); border-color:#ffbdad; }
    .ppro-visual .arrow { position:relative; height:2px; background:#7a869a; }
    .ppro-visual .arrow::after { content:""; position:absolute; right:-1px; top:50%; width:7px; height:7px; border-top:2px solid #7a869a; border-right:2px solid #7a869a; transform:translateY(-50%) rotate(45deg); }
    .ppro-visual .branches { display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-top:16px; min-width:940px; }
    .ppro-visual .branches .node { min-height:74px; }
    .ppro-visual .control { margin-top:16px; padding:10px 12px; color:var(--text); background:#f7f8fa; border-left:3px solid var(--amber); font-size:11px; line-height:1.4; min-width:940px; }
  </style>
  <h2>Safe Operation Outcome and Recovery</h2>
  <p class="subtitle">Classify the operation and observed outcome before deciding whether to retry.</p>
  <section class="flow" aria-label="Sage classifies a provider operation, executes it, assesses the outcome and applies safe completion or recovery">
    <div class="node blue"><strong>1. Classify operation</strong>Read-only, idempotent mutation, reconcile-before-retry, or manual decision</div>
    <div class="arrow" aria-hidden="true"></div>
    <div class="node"><strong>2. Execute safely</strong>Correlation ID, idempotency identity, bounded timeout and durable state</div>
    <div class="arrow" aria-hidden="true"></div>
    <div class="node amber"><strong>3. Assess outcome</strong>Known success, known failure, or outcome unknown</div>
    <div class="arrow" aria-hidden="true"></div>
    <div class="node green"><strong>4. Complete or recover</strong>Persist status, retry safely, reconcile provider state, or escalate</div>
  </section>
  <section class="branches" aria-label="Three outcome branches">
    <div class="node green"><strong>Known success</strong>Complete once and continue lifecycle</div>
    <div class="node red"><strong>Known failure</strong>Correct, retry within policy, or stop permanently</div>
    <div class="node amber"><strong>Outcome unknown</strong>Do not repeat mutation until reconciliation determines safety</div>
  </section>
  <div class="control">Operations can inspect intended Sage state, last-observed provider state, evidence freshness and permitted recovery actions. Manual recovery must never become an undocumented database correction.</div>
</div>
<!-- confluence-html-macro:end -->

## Problem and business objective

Private-provider operations will fail in materially different ways:

- a malformed invoice is rejected and must be corrected;
- credentials expire and require customer or operator action;
- a provider returns a rate limit and work must wait;
- a network connection fails before the request is sent and may be safely retried;
- a connection drops after a provider may have accepted the mutation;
- a webhook is duplicated, delayed, reordered or never received;
- Sage persists provider success incompletely;
- Sage and provider registration/route state diverge;
- an operator retries an unsafe operation without understanding its impact.

Without shared resilience and operations behaviour:

- invoices or registrations may be duplicated;
- invoices may be lost or remain indefinitely unprocessed;
- provider incidents may be confused with customer misconfiguration;
- every adapter may expose different error messages and retry semantics to ERPs;
- operations may require engineering or direct data corrections for routine recovery;
- credentials, invoice content or provider diagnostics may be exposed unnecessarily;
- audit evidence may be incomplete when investigating compliance or customer impact.

The business objective is to preserve invoice and routing continuity while giving customers, ERP products and operations an accurate, actionable and secure view of failures and recovery.

## Business value

| Stakeholder | Value |
|---|---|
| Customer/accountant | Understand whether to correct data, renew credentials, wait for provider recovery or contact support |
| Sage ERP | Receive stable error categories and operation states independent of provider |
| Operations/support | Recover known cases through controlled actions with evidence and audit |
| Engineering/SRE | Detect provider degradation, protect shared capacity and diagnose distributed failures |
| Product/compliance | Demonstrate that invoices, credentials and route transitions are protected from unsafe retry and silent loss |

## Definitions and concept boundaries

| Term | Definition |
|---|---|
| Operation | A discrete Sage or provider action such as validate connection, register entity, submit invoice, retrieve status or deregister |
| Attempt | One execution of an operation; an operation may have multiple safe attempts |
| Idempotency identity | Stable identity that allows repeated delivery without repeating the business effect |
| Known success | Evidence confirms the requested effect occurred |
| Known failure | Evidence confirms the requested effect did not occur |
| Outcome unknown | Sage cannot determine whether the provider performed the mutation |
| Retry | Repeat an operation or attempt according to an approved safety policy |
| Reconciliation | Compare intended Sage state, recorded processing state and authoritative provider evidence |
| Dead-letter item | Work that exhausted automatic recovery or requires a decision |
| Provider degradation | Sustained impairment affecting provider/environment/operation beyond isolated customer errors |
| Manual recovery | Permission-controlled operation such as reconcile, safe retry, cancel, roll back or escalate |

### Retry versus reconciliation

| Situation | Retry | Reconcile | Why |
|---|---|---|---|
| Read-only provider lookup times out | Usually safe | Optional if reads disagree | No external mutation |
| Provider rejects malformed invoice | No unchanged retry | No | Customer/ERP must correct |
| Provider rate limits a safe operation | Bounded delayed retry | Optional | Provider confirms no completion |
| Invoice submission times out after send | Not until safety known | Required | Provider may already have accepted it |
| Webhook is missing | No submission retry | Retrieve/reconcile status | Missing notification does not prove missing effect |
| Manual operator suspects mismatch | Only after evidence | Required first | Protect against duplicate/contradictory state |

## Actors and business scenarios

| Scenario | Actor | Expected outcome | Control |
|---|---|---|---|
| Correct validation error | Customer/ERP | Actionable field/business error; no automatic retry | Stable category and responsible actor |
| Renew expired credential | Customer/operations | Unsafe calls pause; queued work remains visible | Credential metadata/expiry and secure rotation |
| Recover provider outage | Platform/SRE | Safe work retries within bounded policy | Provider health, circuit protection and backlog monitoring |
| Resolve unknown invoice outcome | Platform/operations | Provider state determines completion or safe retry | Correlation, idempotency and reconciliation |
| Process duplicate webhook | Platform | Event applied once | Authentication and deduplication |
| Recover dead-letter item | Operations | Permitted action, reason and result are audited | Role-based controls |
| Communicate degraded service | Product/support | Customer sees accurate responsibility and next action | Stable status without sensitive diagnostics |

## Business rules

| ID | Condition | Rule | Rationale/evidence | Status |
|---|---|---|---|---|
| BR1 | Operation has external side effects | Retry policy must be defined per operation, not generically per provider | Duplicate prevention | Proposed for approval |
| BR2 | Transport timeout follows a mutation | Do not classify as failure solely from timeout | Provider effect may be unknown | Proposed for approval |
| BR3 | Outcome is unknown | Reconcile before unsafe retry | Core product principle | Proposed for approval |
| BR4 | Provider sends duplicate/out-of-order event | Process idempotently and prevent invalid lifecycle regression | Common async behaviour | Proposed for approval |
| BR5 | Recovery requires manual action | Action must be permission-controlled, reasoned and audited | Operational governance | Proposed for approval |
| BR6 | Provider diagnostic contains sensitive data | Translate/redact before customer or general operations display | Security/privacy | Proposed for approval |
| BR7 | One customer request fails | Do not infer provider-wide outage from the isolated event | Avoid misleading health status | Proposed for approval |
| BR8 | Provider-specific recovery capability is absent | Use explicit manual-decision path; do not simulate certainty | Evidence limitations | Proposed for approval |

## Scope

### In scope

- shared error and responsibility taxonomy;
- per-operation safety classification;
- idempotency and correlation requirements;
- bounded retry/backoff and throttling behaviour;
- unknown-outcome reconciliation;
- webhook/event authentication, deduplication, ordering and replay controls;
- durable queues and dead-letter handling;
- provider health, dashboards and alerting;
- credential-expiry/action-required handling;
- controlled operations recovery and audit;
- customer/ERP status translation;
- provider-readiness checks for resilience.

### Out of scope

- Negotiating contractual provider SLAs.
- Automatic route switching to another private provider.
- Customer offboarding and final data-retention policy.
- Provider-specific endpoints, retry values or webhook secrets.
- A replacement for enterprise incident management.
- Direct database correction as an approved recovery workflow.

## Research and evidence

| Evidence | Confidence | What it informs | Limitation/follow-up |
|---|---|---|---|
| Platform Transition Management | High internal | Recoverable/idempotent transitions, reconciliation, audit | Exact SLAs/continuity durations open |
| B2B Router public documentation | Medium/high public | Async send, retrieval and webhook capability | Exact guarantees/idempotency/contract limits require confirmation |
| Banqup public documentation | Medium/high public | OAuth, sales/purchase journeys and API surface | Event/reconciliation and Spain product details open |
| EDICOM evidence pack | Low technical | Vendor artefacts required | No confirmed public endpoint-level evidence |
| SERES public product material | Medium product/low technical | API integration and lifecycle product claims | Endpoint/event guarantees unconfirmed |
| ZeroComa public product material | Medium product/low technical | Issuance/receipt/traceability claims | Private-platform API role unconfirmed |

### Research gaps

- provider-specific idempotency guarantees;
- authoritative reconciliation endpoints or operational procedures;
- webhook signing, event identity, ordering and retry guarantees;
- rate, batch, payload and maintenance limits;
- provider incident/support and escalation models;
- operational retention and audit requirements;
- target SLAs for unknown outcomes, dead-letter work and customer communication.

These gaps must be completed in each provider PRD before production readiness.

## Current-state analysis

The provider PRDs currently apply a common resilience checklist, but the available evidence is uneven. Without a shared implementation and operations contract, individual adapters could:

- retry the same HTTP category differently;
- expose raw provider messages;
- implement incompatible dead-letter states;
- omit reconciliation where webhooks are missing;
- use different meanings for `FAILED`, `RETRYING` or `PENDING`;
- provide no consistent operations control or metric.

Phase 2 should establish shared primitives and governance before scaling from the reference provider to all five integrations.

## Proposed solution overview

> **Solution maturity: proposed conceptual resilience model. Exact technologies, retry values and provider mappings require engineering/provider approval.**

Each externally observable operation follows:

1. Create stable Sage operation and correlation identities.
2. Classify operation safety.
3. Persist intent before external mutation where required.
4. Execute with bounded timeout and provider-aware controls.
5. Classify known success, known failure or outcome unknown.
6. Persist evidence and current state.
7. Retry only when safe.
8. Reconcile when events/effects are ambiguous or missing.
9. Move exhausted/decision-required work to controlled operations recovery.
10. Record every automated and manual action.

## Error and responsibility taxonomy

| Category | Default responsible actor | Example | Default treatment |
|---|---|---|---|
| `VALIDATION` | Customer/ERP | Unsupported or malformed business data | Do not retry unchanged; return correction |
| `AUTHENTICATION` | Customer/operations | Invalid/expired credentials | Pause unsafe work; rotate credentials |
| `AUTHORISATION` | Customer/provider admin | Missing permission/consent | Stop until access changes |
| `THROTTLED` | Sage/provider | Rate limit | Respect provider guidance and bounded backoff |
| `TRANSIENT_PROVIDER` | Provider/Sage platform | Temporary service failure | Retry only safe operation |
| `NETWORK` | Sage/network/provider | Connection failure | Determine whether request was transmitted |
| `OUTCOME_UNKNOWN` | Sage operations/platform | Timeout after possible mutation | Reconcile before retry |
| `CONFLICT` | Product/operations | Sage/provider state disagreement | Inspect and reconcile; no blind overwrite |
| `PERMANENT_PROVIDER` | Provider/product | Unsupported/rejected operation | Stop and map stable error |
| `INTERNAL` | Sage engineering/platform | Persistence/processing failure | Recover from durable state and prevent duplicate external effect |

Provider-specific raw codes remain available to authorised diagnosis but must map to one stable category and ownership.

## Operation safety classification

| Class | Definition | Retry rule | Required evidence |
|---|---|---|---|
| Read-only retryable | No external business effect | Bounded retry allowed | Request/correlation and error |
| Idempotent mutation | Provider or Sage identity guarantees one effect | Repeat with same identity | Idempotency guarantee and stored identity |
| Reconcile-before-retry mutation | Mutation may have occurred | Query/confirm state first | Provider lookup or agreed reconciliation |
| Manual-decision mutation | No safe automatic proof/recovery | Operator decision only | Impact, evidence and authorised reason |

Every provider PRD must classify at least:

- connection validation;
- legal-entity/account creation;
- external registration;
- invoice create/import;
- invoice send/submit;
- status update;
- correction/cancellation;
- disablement/deregistration.

## Proposed work-item lifecycle

| State | Meaning | Permitted next action |
|---|---|---|
| `ACCEPTED` | Sage accepted operation intent | Execute/queue |
| `IN_PROGRESS` | Attempt is running | Complete, fail or unknown |
| `RETRY_SCHEDULED` | Safe retry is planned | Retry/cancel under policy |
| `RECONCILING` | External evidence is being obtained | Complete, safe retry or exception |
| `ACTION_REQUIRED` | Customer/operator correction required | Correct and resume/cancel |
| `COMPLETED` | Effect confirmed and recorded | Terminal |
| `PERMANENTLY_FAILED` | Confirmed failure cannot be automatically recovered | Terminal/escalate |
| `DEAD_LETTER` | Automatic policy exhausted or decision required | Controlled manual action |
| `CANCELLED` | Work intentionally stopped before unsafe effect | Terminal |

Technical names may change, but known failure and unknown outcome must remain distinct.

## Detailed journeys

### Journey A — Correct validation failure

1. ERP submits an operation with invalid business data.
2. Provider or Sage returns validation evidence.
3. Sage maps error to stable fields/category and responsible actor.
4. Work becomes `ACTION_REQUIRED`; unchanged payload is not retried.
5. ERP/customer corrects data and submits a new/idempotently related operation.
6. Audit links correction to original failure.

### Journey B — Retry known transient failure

1. Safe operation receives confirmed transient provider failure.
2. Policy checks attempt limit, provider guidance and backlog capacity.
3. Work becomes `RETRY_SCHEDULED`.
4. Retry uses the same correlation/idempotency identity where required.
5. Success completes once; exhaustion becomes dead-letter or permanent failure.

### Journey C — Reconcile unknown invoice submission

1. Sage persists intent and sends invoice.
2. Connection times out after transmission.
3. Work becomes `OUTCOME_UNKNOWN/RECONCILING`, not failed.
4. Sage queries provider using correlation, invoice identity or provider-supported lookup.
5. If provider accepted it, Sage records success without resubmission.
6. If provider confirms no effect, Sage safely retries.
7. If evidence remains unavailable, work becomes controlled manual decision.

### Journey D — Process duplicate/out-of-order webhook

1. Sage authenticates provider event.
2. Event identity or semantic fingerprint is checked.
3. Duplicate event is acknowledged without duplicate effect.
4. Event version/time is compared with recorded lifecycle.
5. Older event cannot regress state unless the provider mapping explicitly permits it.
6. Missed gap triggers retrieval/reconciliation where available.

### Journey E — Credential expires

1. Expiry metadata or authentication error indicates invalid credential.
2. Connection becomes action-required for affected capability.
3. Unsafe new calls stop; queued work remains visible.
4. Customer/operations rotates credential through secure flow.
5. Connection is revalidated.
6. Queued work resumes according to operation safety.

### Journey F — Operations recover dead-letter item

1. Operator opens work item and sees intended state, observed provider evidence and operation safety.
2. UI exposes only permitted actions.
3. Operator records reason/evidence.
4. System performs reconcile, safe retry, cancel, rollback workflow or escalation.
5. Result and actor are appended to immutable audit history.

## Functional requirements

### Operation safety and execution

| ID | Requirement |
|---|---|
| FR1 | Every external operation must have a documented safety classification before production enablement. |
| FR2 | Mutating operations must use provider idempotency or Sage duplicate protection where technically possible. |
| FR3 | A transport timeout after possible mutation must enter outcome-unknown treatment rather than confirmed failure. |
| FR4 | Retry policy must distinguish validation, authentication, authorisation, throttling, transient, network, conflict, permanent and internal categories. |
| FR5 | Retry limits, backoff and terminal treatment must be defined per operation/provider capability. |
| FR6 | Asynchronous work must persist intent and progress durably across process restarts. |

### Events and reconciliation

| ID | Requirement |
|---|---|
| FR7 | Provider webhooks/events must be authenticated, deduplicated, replay-protected and tolerant of reordering. |
| FR8 | Lifecycle processing must prevent invalid state regression from older events. |
| FR9 | Missed events must be recoverable by polling/reconciliation where provider capability exists. |
| FR10 | Reconciliation must record intended Sage state, observed provider state, observation time, evidence source and discrepancy. |
| FR11 | A provider without authoritative automatic reconciliation must use an explicit manual-decision procedure. |

### Queue, capacity and provider protection

| ID | Requirement |
|---|---|
| FR12 | Retry and queue behaviour must respect provider rate/batch limits and protect shared Sage capacity. |
| FR13 | Circuit breaking or equivalent controls must limit cascading failure during sustained provider degradation. |
| FR14 | Dead-letter work must retain owner, reason, correlation, operation safety and permitted actions. |
| FR15 | Backlog age and capacity must be observable by provider, environment and operation. |

### Customer and ERP experience

| ID | Requirement |
|---|---|
| FR16 | Client errors must expose stable Sage category, responsible actor, retry/action guidance and correlation reference. |
| FR17 | Raw provider errors must not be the only customer-facing explanation. |
| FR18 | Customer-visible status must distinguish correction required, temporary delay, retrying, reconciling, operations investigation and permanent failure. |
| FR19 | Provider degradation messaging must not be inferred from a single customer error. |

### Operations and audit

| ID | Requirement |
|---|---|
| FR20 | Operations must inspect operation, attempts, invoice/connection/route references, intended/observed state, freshness and recovery history. |
| FR21 | Retry, reconcile, cancel, resolve, rollback and escalation actions must be permission-controlled. |
| FR22 | Every manual action must record actor, reason, evidence, time, previous state and result. |
| FR23 | Recovery must invoke approved domain workflows rather than direct route/invoice state rewriting. |
| FR24 | Support bundles and operational views must redact secrets and unnecessary invoice/customer content. |

### Health and observability

| ID | Requirement |
|---|---|
| FR25 | Metrics must be segmented by provider, environment, operation, outcome and error category. |
| FR26 | Distributed correlation must cover client request, orchestration, adapter call, event and reconciliation. |
| FR27 | Credential expiry/authentication failure must be detected and surfaced before or at first avoidable failure. |
| FR28 | Alerts must distinguish provider degradation from individual customer configuration errors. |

## Failure-mode matrix

| Scenario | Required response |
|---|---|
| Provider unavailable before request is sent | Queue/fail transiently according to operation SLA |
| Connection drops after mutation is sent | Outcome unknown; reconcile |
| Duplicate webhook | Authenticate and process once |
| Out-of-order webhook | Prevent invalid regression; reconcile gaps |
| Webhook authentication fails | Reject, audit and monitor security signal |
| Webhook never arrives | Retrieve/reconcile or age into exception |
| Provider reports unknown customer | Compare registration; do not automatically recreate |
| Credential expires | Pause unsafe work and request secure rotation |
| Rate limit reached | Respect provider guidance and bounded backoff |
| Sage persistence fails after provider success | Recover using correlation/idempotency and reconcile |
| Manual retry requested | Show safety/impact; require permission and reason |
| Provider and Sage route/registration disagree | Reconcile and invoke domain transition; do not overwrite blindly |

## Operational experience

### Work-item view

Operations must see:

- operation and correlation IDs;
- provider, environment and operation type;
- legal entity using minimised identification;
- current state, attempt count and next action/time;
- intended Sage state and last-observed provider state;
- whether the outcome is known;
- error category and redacted diagnostic;
- operation-safety class;
- related connection, route, transition and invoice references;
- permitted actions and complete recovery history.

### Controlled actions

| Action | Guardrail |
|---|---|
| Retry | Only safe classification or completed reconciliation |
| Reconcile | Prefer read-only evidence; record source/freshness |
| Cancel queued work | Show customer/lifecycle impact and require reason |
| Mark resolved | Restricted permission and evidence reference |
| Roll back transition | Invoke PRD-SEI-201/202 workflow; no direct history rewrite |
| Disable connection | Show active-route/historical dependency |
| Escalate | Generate redacted support bundle and provider correlation |

## Security and non-functional requirements

### Security/privacy

- Secrets, certificates, tokens and signed webhook material must use approved secure handling.
- Provider payload logging must be allow-listed and redacted.
- Operational roles must follow least privilege and separation of duties where required.
- Manual actions require strong actor identity and immutable audit.

### Reliability/capacity

- Queues and orchestration must survive restarts without duplicate business effects.
- Retry storms must be prevented through jitter/backoff, rate controls and circuit protection.
- Provider outage must not exhaust capacity required by healthy providers.
- Recovery point/time objectives require engineering/SRE ownership and evidence.

### Audit/retention

- Operation, attempt, event, reconciliation and manual-action evidence must be linked.
- Retention duration and legal/audit requirements remain open and must be approved before production.

## Acceptance criteria

1. A duplicate webhook does not create a second lifecycle event.
2. An out-of-order event cannot regress terminal state unless explicitly allowed by provider mapping.
3. A timed-out mutation enters outcome-unknown/reconciliation and is not blindly repeated.
4. Reconciliation can complete a successful provider operation without resubmission.
5. Provider-confirmed no-effect allows a safe retry with preserved identity.
6. Invalid credentials stop affected unsafe calls and create actionable status.
7. Validation errors identify correction and are not retried unchanged.
8. Rate-limit responses use bounded provider-aware delay.
9. Dead-letter items show owner, reason, safety, correlation and permitted action.
10. Manual recovery is permission-controlled and fully audited.
11. Logs/support bundles exclude credential material and prohibited invoice data.
12. Provider degradation is visible by provider/environment/operation.
13. One provider outage does not prevent processing through a healthy provider beyond shared-capacity limits.
14. Each provider passes an operation-safety and reconciliation readiness review before production.

## Metrics

| Metric | Target/direction | Evidence status |
|---|---|---|
| Avoidable duplicate external operations | 0 | Proposed target |
| Avoidable invoice loss | 0 | Proposed target |
| Manual recovery actions with complete audit | 100% | Proposed target |
| Dead-letter items with owner/reason/safety | 100% | Proposed target |
| Credential expiries detected before expiry where metadata exists | 100% | Proposed target |
| Unknown outcome maximum age | Target required by operation/provider | Open — operations/product |
| Dead-letter maximum age | Target required | Open — operations |
| Provider incident detection/acknowledgement | Target required | Open — SRE |
| Retry recovery rate | Measure by provider/operation | Baseline required |
| Webhook delay/duplicate rate | Measure by provider | Baseline required |

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Successful mutation is retried after timeout | Duplicate invoice/registration | Outcome-unknown state and reconciliation |
| One generic retry policy is applied | Unsafe or ineffective recovery | Per-operation safety classification |
| Webhook is trusted as complete/ordered truth | Missing or regressed lifecycle | Deduplication, ordering controls and reconciliation |
| Provider raw error is exposed | Poor UX or sensitive leakage | Stable taxonomy and redaction |
| Manual recovery bypasses domain workflows | Corrupt route/invoice history | Controlled actions invoking approved workflow |
| Provider outage creates retry storm | Shared platform degradation | Bounded retry, jitter, rate control and circuit protection |
| Operational SLA remains undefined | Aged invisible customer impact | Named decision gates and backlog-age metrics |
| Provider lacks reconciliation API | Persistent ambiguity | Manual-decision procedure and commercial/provider escalation |

## Rollout

1. Approve shared error taxonomy and operation-safety model.
2. Implement correlation, durable intent, idempotency and audit primitives.
3. Classify reference-provider operations.
4. Validate known failure, timeout-after-send, duplicate event, missing event and persistence-after-success scenarios.
5. Implement dashboards, alerts and dead-letter work view.
6. Pilot controlled recovery with operations/support.
7. Define customer communication and operational SLAs.
8. Require resilience readiness for every subsequent provider.

### Provider production gate

- Every mutating operation classified.
- Idempotency or reconcile-before-retry evidence recorded.
- Webhook/polling/reconciliation behaviour tested.
- Limits and provider outage controls configured.
- Credential expiry/rotation journey tested.
- Dead-letter ownership and support escalation agreed.
- Security/redaction review complete.
- Operational/customer SLAs approved.

## Consultation and open decisions

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| What SLA applies to unknown outcomes? | Limits customer ambiguity and operational backlog | Product + operations | Production support model | Provider/operation-specific |
| What SLA applies to dead-letter work? | Defines ownership and staffing | Operations | Production readiness | Severity/operation-specific |
| Which recovery actions can support perform? | Defines roles and controls | Operations + security | Operations tooling | Reconcile and safe retry with guardrails |
| What provider degradation is customer-visible? | Avoids misleading or commercially sensitive messaging | Product/support | UX | Stable Sage status, provider detail only where appropriate |
| How long is operational evidence retained? | Audit/privacy/cost | Compliance + security | Production data design | Follow approved invoice/audit policy |
| Which providers have authoritative reconciliation? | Determines automatic versus manual recovery | Provider owners | Provider readiness | B2B Router/Banqup to validate; others open |
| What availability/capacity targets apply? | Drives architecture and SRE controls | Product + SRE | NFR approval | Baseline through reference provider |

## Decisions

| Date | Decision | Evidence/status |
|---|---|---|
| 2026-07-27 | Resilience is a shared Phase 2 capability | Proposed product boundary |
| 2026-07-27 | Unknown external outcomes must be reconciled before unsafe retry | Proposed product principle |
| 2026-07-28 | Provider PRDs must classify operation safety and reconciliation readiness | Draft improvement |
| 2026-07-28 | Manual recovery must invoke controlled domain workflows | Draft improvement |

## Revision history

| Date | Version/revision | Change | Pull request |
|---|---|---|---|
| 2026-07-27 | `phase2-prds-v0.1` | Initial discovery draft | |
| 2026-07-27 | `phase2-prds-v0.2` | Confluence publication baseline | |
| 2026-07-28 | Draft | Deepened business analysis, research, solution model, recovery visual and operational gates | |
