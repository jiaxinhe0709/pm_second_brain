---
id: PRD-SEI-201
title: Spain Public and Private Platform Transition
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-07-27
updated: 2026-07-27
reviewers: []
related:
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
  - https://confluence.sage.com/spaces/DNBU/pages/855183578/Platform+Transition+Management
  - https://confluence.sage.com/spaces/DNBU/pages/837610648/Public+Platform+Onboard
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
---

# Spain Public and Private Platform Transition

## Summary

Enable a Spanish e-invoicing customer to establish supported private-platform connections alongside their public-platform registration, independently route inbound and outbound invoice flows through an eligible connection, and change those routes without losing the status, audit history, or network context of existing invoices.

This is the umbrella Phase 2 PRD. Shared routing, resilience, and provider-specific requirements are defined in the related PRDs.

## Phase 2 PRD set

| ID | Document | Purpose |
|---|---|---|
| PRD-SEI-201 | Public and Private Platform Transition | Phase 2 outcomes, scope, journeys, and delivery gates |
| PRD-SEI-202 | Private Platform Connection and Routing Foundation | Shared connection, route, registration, and transition model |
| PRD-SEI-203 | Private Platform Resilience and Operations | Cross-provider reliability, reconciliation, monitoring, and recovery |
| PRD-SEI-204 | B2B Router Integration | B2B Router provider adapter and onboarding |
| PRD-SEI-205 | Banqup (Unifiedpost) Integration | Banqup provider adapter and onboarding |
| PRD-SEI-206 | EDICOM Integration | EDICOM provider adapter and onboarding |
| PRD-SEI-207 | SERES (Docaposte) Integration | SERES provider adapter and onboarding |
| PRD-SEI-208 | ZeroComa Integration | ZeroComa provider adapter and onboarding |

## Problem

Customers may be registered with both public and private platforms and may use different routes for inbound and outbound invoices. A route can change while invoices created or received through a previous connection still require status updates, corrections, cancellation, audit, or retrieval.

Without explicit connection and route management, Sage risks incorrect delivery, lost lifecycle events, premature deregistration, inconsistent provider state, and an inability to recover safely from partial transitions.

### Why Phase 1 is not sufficient

Phase 1 establishes the public connection and invoice lifecycle. Phase 2 introduces several conditions that the Phase 1 customer-level platform selection cannot represent:

- public and private registrations can coexist;
- inbound and outbound invoices can use different networks;
- a private connection can be configured before it becomes an active route;
- a route can change at a scheduled time;
- old invoices can remain active on their original network;
- an external transition operation can succeed even when Sage receives a timeout;
- route deactivation, connection disablement, deregistration, and customer offboarding are different events.

### Product principles

1. **Connections are not routes.** A customer may be connected to a provider without routing invoices through it.
2. **Routing is scoped.** A route applies to a defined legal entity, direction, environment, and effective period.
3. **New routing does not rewrite history.** Existing invoices retain their original network context.
4. **Activation is explicit.** Completing provider onboarding does not automatically change invoice routing.
5. **Deregistration is explicit.** Removing an active route does not automatically remove a provider registration.
6. **Unknown is a real state.** A timeout must not be treated as confirmation of failure.

## Definitions

| Term | Definition |
|---|---|
| Connection | Sage configuration and credentials that enable communication with a public or private platform. |
| Registration | The external platform's record that a legal entity is enrolled or reachable through that platform. |
| Route | A time-bound rule selecting a connection for a defined invoice scope. |
| Route scope | The dimensions to which a route applies, initially legal entity, direction, environment, and effective time. |
| Transition | A controlled change from one effective route to another. |
| Routing decision | The recorded selection of a route and connection for an invoice. |
| Invoice network context | Immutable information identifying the connection and provider originally used for an invoice. |
| Route deactivation | Ending a route so it is no longer selected for new invoices. |
| Connection disablement | Preventing new operations through a connection while retaining its record and history. |
| Deregistration | Removing or ending an external platform registration. |
| Offboarding | Ending the customer's Sage Spain e-invoicing relationship; outside this PRD. |

## Goals

- Support coexistence of public and private registrations.
- Allow inbound and outbound routes to be configured independently.
- Establish and validate a private connection without activating it.
- Support controlled Public → Private and Private → Public route changes.
- Preserve the original network context and lifecycle of existing invoices.
- Give customers and operations teams clear transition status.
- Provide a shared foundation for the five planned provider integrations.

## Non-goals

- Private Provider A → Private Provider B transitions.
- Sage operating as a private e-invoicing platform.
- Per-invoice manual provider selection in the first Phase 2 release.
- Dynamic cost, performance, or weighted routing.
- Automatic failover between private providers.
- Final customer offboarding, data deletion, or retention policy.
- Provider-specific protocol requirements, which belong in provider PRDs.

## Users and use cases

### Sage ERP product

- Establish a private connection for a customer.
- Check whether the connection is ready.
- Request an inbound or outbound route change.
- Show progress and actionable failures.
- Retrieve invoices regardless of their original network.

### Business or accountant

- Connect an eligible private provider.
- Keep public registration while preparing or using private routing.
- Use different networks for sending and receiving.
- Understand which route is active and from when.
- Continue working with invoices created before a route change.

### Operations and support

- Inspect connections, registrations, routes, and transitions.
- Detect discrepancies between Sage and providers.
- Retry, reconcile, roll back, or escalate failed transitions.
- Inspect a complete audit history.

## Requirements

| ID | Requirement |
|---|---|
| FR1 | A customer may hold public and private registrations concurrently. |
| FR2 | The system must represent connections separately from active routes. |
| FR3 | The system must support independent inbound and outbound routes. |
| FR4 | A private connection must be validated and marked ready before route activation. |
| FR5 | Route changes must support an effective date and time. |
| FR6 | New invoices must use the applicable active route at the routing-decision time. |
| FR7 | Existing invoices must retain their original connection, provider, external reference, direction, and status history. |
| FR8 | Route activation must be recoverable and auditable. |
| FR9 | A connection must not be automatically deregistered merely because it is no longer the active route. |
| FR10 | Customers and operations must be able to see transition progress and failure states. |
| FR11 | The system must prevent conflicting route transitions for the same scope. |
| FR12 | Provider-specific behaviour must be isolated behind a shared capability-based adapter contract. |

### Route lifecycle

| ID | Requirement |
|---|---|
| FR13 | A transition request must identify legal entity, direction, source route, target connection, requested effective time, and initiator. |
| FR14 | Sage must validate target connection readiness and scope eligibility before accepting activation. |
| FR15 | Sage must expose whether a transition is scheduled, preparing, activating, reconciling, completed, failed, or rolled back. |
| FR16 | A scheduled transition must be cancellable until the point at which irreversible external work begins. |
| FR17 | The transition must be idempotent for repeated requests carrying the same idempotency key. |
| FR18 | A completed transition must identify the exact time from which the new route became effective. |
| FR19 | Sage must not create a period with two conflicting active routes for the same implemented scope. |
| FR20 | Sage must not create an unintended period with no route; where unavoidable, the state must be explicit and operationally visible. |

### Invoice continuity

| ID | Requirement |
|---|---|
| FR21 | Route resolution for a new invoice must store the resolved route ID, connection ID, provider, direction, environment, external reference when available, and decision timestamp. |
| FR22 | Subsequent status, correction, cancellation, retrieval, and reconciliation operations must use the invoice's original context unless an approved lifecycle rule says otherwise. |
| FR23 | Historical invoice access must not depend only on the customer's currently active route. |
| FR24 | If ownership of an older lifecycle operation is not known, Sage must prevent silent rerouting and surface the case for reconciliation. |
| FR25 | A previous connection must not be disabled or deregistered while it is required by non-terminal invoices, unless an approved exception process exists. |

### Customer and operations control

| ID | Requirement |
|---|---|
| FR26 | Customer-facing clients must be able to retrieve current inbound and outbound routes and their effective times. |
| FR27 | Clients must be able to retrieve configured connections without receiving secrets or raw credentials. |
| FR28 | Transition errors must identify whether the customer, Sage, provider, or local operations team must act. |
| FR29 | Operations must be able to compare intended Sage state with observed provider state. |
| FR30 | Manual retry, reconciliation, rollback, disablement, and deregistration must be permission-controlled and audited. |

## Detailed journeys

### Journey A — Prepare private outbound connection without switching

1. ERP creates a connection for the selected provider and legal entity.
2. Sage returns required configuration fields and provider capability information.
3. Customer or authorised accountant supplies credentials and registration data.
4. Sage validates configuration and requests or verifies external registration.
5. Sage records provider identifiers and observed registration state.
6. Connection becomes `READY` for outbound invoices.
7. Public outbound remains active because no route transition has been requested.

Expected result: the customer holds both public and private registrations, with no invoice-routing change.

### Journey B — Switch outbound from public to private

1. ERP requests a route transition using the ready private connection.
2. Sage verifies route authority, connection readiness, direction capability, effective time, and absence of conflicting transitions.
3. Sage presents the proposed source route, target route, direction, timing, and continuity implications.
4. Authorised client confirms.
5. Sage prepares any required external work.
6. At the effective time, Sage activates the private outbound route and ends the public outbound route.
7. Sage reconciles the target provider state.
8. New outbound invoices use private; inbound remains unchanged.
9. Existing public-origin invoices retain public context.

### Journey C — Use public inbound and private outbound

1. Customer retains public inbound registration and route.
2. Customer activates the private outbound route.
3. Route lookup resolves by direction.
4. Received public invoices retain public context.
5. Sent private invoices retain provider-specific private context.

Expected result: the customer is not described by one global public/private state.

### Journey D — Roll back before activation

1. Customer cancels a scheduled transition.
2. Sage verifies that irreversible provider work has not begun.
3. Target connection remains configured and ready.
4. Source route remains effective.
5. Cancellation is audited.

### Journey E — Roll back after activation

1. Customer or operations requests rollback because the private route is unsuitable or degraded.
2. Sage validates that public is eligible and ready for the applicable direction.
3. Sage executes a new transition back to public.
4. Private-origin invoices retain private context.
5. Private connection remains present unless separately disabled or deregistered.

### Journey F — Activation returns an ambiguous timeout

1. Sage sends an activation or registration request.
2. Provider does not return a conclusive response.
3. Transition becomes `RECONCILING`; it is not marked failed.
4. Sage queries authoritative provider state or invokes the agreed reconciliation process.
5. Sage either completes the transition, safely retries, or raises an operational exception.
6. No conflicting route is exposed while the outcome is unknown.

## Transition state model

| State | Meaning | Permitted next states |
|---|---|---|
| REQUESTED | Request accepted but not fully validated | VALIDATING, CANCELLED |
| VALIDATING | Eligibility, readiness, and conflicts are being checked | SCHEDULED, PREPARING, REJECTED |
| SCHEDULED | Valid request waiting for effective time | PREPARING, CANCELLED |
| PREPARING | Reversible external and internal preparation is underway | ACTIVATING, FAILED, CANCELLED |
| ACTIVATING | Route cutover is in progress | RECONCILING, COMPLETED, FAILED |
| RECONCILING | External outcome or state is being confirmed | COMPLETED, FAILED, ROLLBACK_REQUIRED |
| COMPLETED | Target route is effective | Terminal |
| REJECTED | Request was invalid or ineligible | Terminal |
| FAILED | Transition did not complete and source route remains authoritative | Retry or terminal according to failure |
| ROLLBACK_REQUIRED | Safe automatic resolution is not possible | ROLLED_BACK, COMPLETED, FAILED |
| ROLLED_BACK | Source route has been restored through a controlled transition | Terminal |
| CANCELLED | Transition ended before activation | Terminal |

Final technical names may change during solution design, but the distinct behaviours must remain represented.

## Failure and edge-case behaviour

| Scenario | Expected behaviour |
|---|---|
| Target credentials invalid | Reject preparation; leave source route unchanged |
| Target registration pending | Keep target connection non-active; show pending state |
| Effective time arrives while provider is unavailable | Follow approved cutover policy; do not claim target is active without evidence |
| Duplicate transition request | Return the existing transition for the same idempotency key |
| Concurrent inbound and outbound changes | Allow only where their scopes do not conflict |
| Invoice submitted exactly at cutover | Use a deterministic decision timestamp and persist selected route |
| Public connection later disabled | Continue private routing; identify affected public-origin lifecycle operations |
| Provider says active but Sage says failed | Enter reconciliation; prevent unsafe duplicate activation |
| Customer requests deregistration with open invoices | Block, warn, or require approved override according to consultation decision |
| No eligible route | Reject or queue according to approved policy; never silently choose an unapproved provider |

## Non-functional requirements

### Security and privacy

- Credentials and certificate material must be held in approved secure storage.
- APIs and logs must expose credential metadata only, never secret values.
- Route and connection mutations must require authenticated, authorised actors.
- Operations access must follow least privilege.
- Audit records must not contain unnecessary invoice content or personal data.

### Reliability

- Transition orchestration must survive process restarts.
- Mutating requests must support idempotency.
- Provider calls must have bounded timeouts and operation-specific retry policies.
- The system must support reconciliation after missed events and ambiguous outcomes.

### Performance

- Normal route resolution must not require a synchronous provider call.
- Route configuration changes must become visible within an agreed internal propagation target.
- Bulk onboarding and accountant-managed customers must not create conflicting transitions.

### Auditability

- All connection, route, registration, and transition state changes must record actor, time, reason, previous value, new value, and correlation identifier.
- The route decision used by an invoice must remain explainable after later configuration changes.

## Acceptance criteria

1. A customer can have public inbound, public outbound, private inbound, and private outbound connections represented concurrently.
2. Public inbound and private outbound can be active at the same time.
3. Preparing a private connection does not alter an active public route.
4. A route cannot activate until its target connection is ready for the required direction.
5. A new invoice created before and after a cutover receives the correct, persisted route context.
6. A public-origin invoice remains queryable after outbound switches to private.
7. Repeating a transition request with the same idempotency key does not create a second transition.
8. An ambiguous provider timeout results in reconciliation rather than blind retry.
9. Route deactivation does not automatically deregister the underlying connection.
10. Every route change and manual recovery action appears in the audit history.

## User experience

The common journey is:

1. Select a supported private provider.
2. Supply configuration and credentials through an approved secure flow.
3. Validate the connection and external registration.
4. Show the connection as ready but inactive.
5. Select inbound, outbound, or both route scopes.
6. Review the proposed effective time and impact.
7. Activate the route and show transition progress.
8. Confirm the effective route and retain previous connections as required.

The experience must distinguish `connection ready` from `route active`.

## Metrics

| Metric | Initial target |
|---|---|
| Successful route transitions | >99% excluding confirmed provider outages |
| Avoidable invoice loss during transitions | 0 |
| Invoices with complete routing context | 100% |
| Audited connection and route changes | 100% |
| Unreconciled internal/provider discrepancies | 0 beyond agreed operational SLA |
| Transition failures with actionable status | 100% |

## Rollout

1. Confirm the shared connection and routing model.
2. Select one reference provider using customer priority, sandbox readiness, API coverage, and provider support.
3. Deliver the reference provider end to end.
4. Validate resilience and operational recovery.
5. Add remaining providers in prioritised waves.
6. Enable production route switching only after consultation entry gates are met.

### Entry gates for production switching

- The local team confirms the authoritative route-determination mechanism.
- Historical lifecycle ownership is documented for each supported operation.
- Cutover, rollback, and deregistration sequences are approved.
- The reference provider passes sandbox and resilience testing.
- Phase 1 persists required invoice network context.
- Security, privacy, support, and operational readiness reviews are complete.

## Risks

| Risk | Mitigation |
|---|---|
| Route authority remains undefined | Keep it as a delivery gate and do not embed an unconfirmed authority rule |
| Provider adapters diverge | Require the shared foundation and capability contract |
| Old invoices lose lifecycle access | Persist invoice origin and retain required connection access |
| External success is reported as a timeout | Reconcile before retrying non-idempotent operations |
| Five providers are attempted simultaneously | Establish a reference adapter before scaling |
| Overly granular routing delays delivery | Implement legal entity, direction, provider, environment, and effective time first |

## Open questions

1. What authoritative source determines an invoice route?
2. Can routing vary by document type, counterparty, or regulatory scenario?
3. Which platform owns status, correction, cancellation, and retrieval for older invoices after a route change?
4. What are the authoritative cutover, rollback, and deregistration sequences?
5. How long must a previous connection remain available?
6. Which provider should be the reference integration?
7. Which ERP and customer cohorts enter the first rollout?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | Public and private registrations may coexist | Confirmed |
| 2026-07-27 | Inbound and outbound may use different networks | Confirmed product scenario |
| 2026-07-27 | Shared and provider-specific requirements will be maintained as separate PRDs | Confirmed |
| 2026-07-27 | Confluence publication remains disabled pending review | Confirmed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
