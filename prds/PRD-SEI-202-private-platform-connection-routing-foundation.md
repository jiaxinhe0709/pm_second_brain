---
id: PRD-SEI-202
title: Spain Private Platform Connection and Routing Foundation
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-07-27
updated: 2026-07-27
reviewers: []
related:
  - PRD-SEI-201
  - PRD-SEI-203
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "866126304"
  title: Private platform connection and routing foundation
---

# Spain Private Platform Connection and Routing Foundation

## Summary

Create the provider-neutral domain and API foundation for connecting Spanish customers to private e-invoicing platforms and assigning independent inbound and outbound routes while public registration remains available.

## Problem

A single customer-wide platform flag cannot represent coexisting registrations, independent sending and receiving routes, staged activation, historical invoice ownership, or recoverable transitions. Implementing provider-specific models would also make each new integration expensive and inconsistent.

## Conceptual model

```text
Customer / Legal Entity
├── Connection: Public
│   ├── External registration
│   └── Capabilities: inbound, outbound
├── Connection: Private Provider
│   ├── Credential reference
│   ├── External registration
│   └── Capabilities: provider-specific
├── Route: inbound → Public connection
├── Route: outbound → Private connection
└── Transition history
```

An invoice stores the route decision it received. It must not recalculate its original network from the customer's current routes.

## Entity definitions

### Connection

| Attribute | Purpose |
|---|---|
| connection_id | Stable Sage identifier |
| legal_entity_id | Customer/NIF scope |
| provider_id | Stable public or private provider identifier |
| environment | Test or production |
| credential_reference | Pointer to approved secure storage |
| capabilities | Supported directions and operations |
| status | Configuration and communication state |
| created/updated timestamps | Audit and concurrency |
| version | Mutation conflict control |

### External registration

| Attribute | Purpose |
|---|---|
| registration_id | Stable Sage identifier |
| connection_id | Owning connection |
| external_registration_id | Provider traceability |
| direction/scope | Registration applicability |
| observed_status | Last authoritative provider state |
| observed_at | Freshness of external state |
| requested_at/confirmed_at | Lifecycle timing |
| failure category | Actionable failure classification |

### Route

| Attribute | Purpose |
|---|---|
| route_id | Stable route identifier |
| legal_entity_id | Entity to which the route applies |
| direction | Inbound or outbound |
| connection_id | Selected connection |
| environment | Test or production |
| effective_from/effective_to | Non-overlapping validity period |
| status | Scheduled, active, retiring, or inactive |
| priority | Reserved for future extended routing |
| version | Concurrency and audit |

### Invoice routing snapshot

| Attribute | Purpose |
|---|---|
| route_id | Route selected at decision time |
| connection_id | Connection used |
| provider_id | Provider/network identity |
| direction | Inbound or outbound |
| environment | Test or production |
| decision_timestamp | Cutover-boundary evidence |
| external_reference | Provider traceability |
| protocol/version | Interpretation of provider payloads where needed |

## Goals

- Separate customer, connection, external registration, route, transition, and invoice context.
- Provide a capability-based adapter boundary for all supported providers.
- Support routing at legal-entity and direction level initially.
- Preserve extension points for document type, counterparty, network, and fallback rules.
- Prevent ambiguous or conflicting active routes.

## Non-goals

- A general-purpose routing rules engine.
- Per-invoice manual override.
- Automatic provider failover.
- Provider-specific authentication or payload mappings.
- Private-to-private switching.

## Users and use cases

- ERP teams create and inspect connections using a consistent API.
- Routing services resolve the applicable connection for a new invoice.
- Operations teams inspect the source and history of every route decision.
- Provider adapters translate shared operations into provider-specific calls.

## Requirements

### Domain model

| ID | Requirement |
|---|---|
| FR1 | A customer must be able to own multiple connection records. |
| FR2 | Each connection must identify provider, legal entity, environment, capabilities, credential reference, and status. |
| FR3 | External registration status must be represented separately from connection status. |
| FR4 | Route records must reference a connection and define direction, effective period, status, and version. |
| FR5 | Phase 2 routing must support legal entity, direction, provider, environment, and effective time. |
| FR6 | The model must be extensible to document type, counterparty, counterparty network, and fallback without schema replacement. |
| FR7 | A transition must record the source route, target route, requested scope, state, timestamps, initiator, and failure details. |
| FR8 | Every invoice must persist a routing snapshot rather than depend only on the customer's current configuration. |

### Behaviour

| ID | Requirement |
|---|---|
| FR9 | A connection may be ready without being active for any route. |
| FR10 | Only a validated, eligible connection may be activated. |
| FR11 | Conflicting active routes for the same implemented scope must be prevented. |
| FR12 | Route resolution must be deterministic and auditable. |
| FR13 | Route changes must use version or concurrency controls. |
| FR14 | Deactivating a route must not automatically disable or deregister its connection. |
| FR15 | Provider capabilities must be explicit; unsupported operations must return a consistent platform error. |

### Connection lifecycle

| State | Meaning |
|---|---|
| DRAFT | Connection exists but required configuration is incomplete |
| VALIDATING | Sage is validating credentials or provider configuration |
| PENDING_REGISTRATION | External registration is pending |
| READY | Connection is eligible for one or more declared capabilities |
| DEGRADED | Connection is usable only with a known impairment |
| ACTION_REQUIRED | Customer or operator action is required |
| DISABLING | New use is being stopped in a controlled way |
| DISABLED | Connection cannot be selected for new routes |
| FAILED | Setup did not complete and requires retry or correction |

Connection state does not identify the active invoice route.

### Route resolution

For the initial Phase 2 release, the resolution input is:

```text
legal_entity_id + direction + environment + routing_decision_timestamp
```

Resolution must:

1. retrieve routes whose effective period contains the decision timestamp;
2. exclude connections that are not eligible for the required capability;
3. return exactly one route;
4. reject or follow an explicitly approved no-route policy if none exists;
5. raise a configuration exception if multiple routes match;
6. persist the result on the invoice before provider processing begins.

Future document-type or counterparty rules must introduce explicit precedence rather than relying on database ordering.

### Proposed platform API behaviours

| Operation | Behaviour |
|---|---|
| Create connection | Creates a draft resource; never changes routing |
| Update configuration | Validates mutable metadata; secrets use a secure upload/exchange flow |
| Validate connection | Starts or returns an idempotent validation operation |
| Get connection | Returns status, capabilities, registration summaries, and credential metadata |
| Request registration | Starts provider registration where required |
| Create transition | Validates target connection and requested route scope |
| Get transition | Returns state, timestamps, failure category, and permitted actions |
| Get effective routes | Returns active and scheduled routes by direction |
| Disable route | Ends route eligibility for new invoices without implicit deregistration |
| Disable connection | Requires impact analysis for active routes and historical invoices |

Mutating operations must accept an idempotency key and return stable operation identifiers.

## Validation rules

- Legal entity and provider must be compatible with the provider's declared capability profile.
- Test credentials cannot be attached to a production connection.
- A disabled connection cannot be selected by a new route.
- A connection without the requested direction capability cannot be activated for that direction.
- Effective periods for the same implemented scope cannot overlap.
- A connection referenced by an active route cannot be disabled without first resolving route impact.
- Credential updates must not reveal or return existing secret material.
- Provider-observed state older than the agreed freshness threshold cannot be treated as current for irreversible actions.

### Initial adapter capabilities

- Validate configuration.
- Establish and inspect connection.
- Request and inspect registration.
- Check readiness.
- Submit an outbound document where supported.
- Receive or retrieve an inbound document where supported.
- Retrieve lifecycle status.
- Reconcile external state.
- Disable or deregister where supported and authorised.

## User experience

APIs and operational tools must show four distinct questions:

1. Is the connection configured?
2. Is the external registration confirmed?
3. Is the connection ready for a specific capability?
4. Is a route currently using it?

## Metrics

- 100% of provider integrations use the shared connection model.
- 100% of new invoices store their route snapshot.
- 100% of route changes have versioned audit events.
- Zero conflicting active routes within supported routing scope.

## Acceptance criteria

1. One legal entity can hold a public and multiple private connection records.
2. Each connection reports capabilities separately from status.
3. A ready connection can exist without an active route.
4. Route resolution returns different connections for inbound and outbound.
5. Overlapping routes for the same initial scope are rejected.
6. Test and production routes and credentials cannot be mixed.
7. An invoice keeps its route snapshot after the customer configuration changes.
8. Provider-specific fields can be stored without adding provider-specific logic to the routing service.
9. Disabling a route leaves the connection and registration records intact.
10. Every mutation supports concurrency control and audit history.

## Rollout

1. Agree domain terminology and identifiers.
2. Confirm the minimum routing scope with the local team.
3. Implement connection and registration lifecycle.
4. Implement deterministic route resolution and invoice snapshot.
5. Validate through the reference provider.
6. Extend only where a confirmed provider or customer need requires it.

## Risks

- Treating provider state as equivalent to Sage state.
- Building unneeded routing-rule complexity.
- Using mutable provider names rather than stable connection identifiers.
- Storing credentials directly rather than secure references.
- Assuming all providers support the same operations.

## Open questions

1. What is the authoritative routing input or directory?
2. What precedence applies if future counterparty and document-type rules overlap?
3. At what moment is the routing snapshot fixed?
4. How are invoices handled if no eligible route can be resolved?
5. Which fields constitute a legal-entity routing scope?

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | Connections and routes are separate resources | Proposed |
| 2026-07-27 | Inbound and outbound routes are independently configurable | Proposed |
| 2026-07-27 | Phase 2 implements direction-level routing before advanced rule dimensions | Proposed |

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-07-27 | Initial discovery draft | |
