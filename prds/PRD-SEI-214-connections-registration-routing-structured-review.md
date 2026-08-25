---
id: PRD-SEI-214
title: Foundation — Connections, Registration and Routing — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-24
reviewers: []
related:
  - PRD-SEI-202
  - PRD-SEI-201
  - PRD-SEI-203
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
  - PRD-SEI-231
  - PRD-SEI-233
  - https://confluence.sage.com/spaces/DNBU/pages/855183578/Platform+Transition+Management
  - https://confluence.sage.com/spaces/DNBU/pages/837610648/Public+Platform+Onboard
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588799"
  page_id: "866126304"
  title: Foundation — Connections, Registration and Routing
  layout: two_left_sidebar
  toc: true
---

# Foundation — Connections, Registration and Routing — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-202, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-214, adds Confluence layout/navigation metadata, and strengthens the connection/route contract with separate legal-subject, establishment, identifier, endpoint, credential and delegated-authority bindings. |
| Unchanged areas | Connection, registration, readiness, route and historical invoice-context separation remains based on PRD-SEI-202. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-202; this successor introduces no new product decision. |

## Overview

This feature provides the shared Phase 2 foundation that allows a Spanish e-invoicing customer to connect to public and private platforms at the same time and to use the appropriate connection for each supported invoice flow.

Phase 1 establishes public-platform onboarding. Phase 2 adds private-provider connectivity and Public ↔ Private route transitions. This foundation prevents each provider integration from inventing its own customer, connection, registration, route, credential, invoice-context, and transition model.

> **Connect a platform once, prove that it is ready, and activate it only for the invoice scope the customer intends to change.**

### Delivery context

| Phase | Routing capability | Foundation responsibility |
|---|---|---|
| Phase 1 — Public Platform Connection | Public routing for supported invoice flows | Persist explicit public route and invoice-network context |
| **Phase 2 — Private Platform Connections** | Public and private registrations coexist; inbound and outbound may use different routes | **Deliver shared connections, registrations, capability readiness, deterministic routing, and invoice snapshots** |
| Phase 3 — Platform Expansion | Private-first and Private A ↔ Private B switching | Extend route dimensions and provider interoperability without replacing the Phase 2 model |

## Product principle

> **A connection describes where Sage can communicate; a route describes when Sage should use that connection.**

Creating, validating, or retaining a private connection must not silently change invoice routing. Likewise, changing the route for new invoices must not rewrite the platform context of invoices already processed.

## Connection and routing visual

<!-- confluence-html-macro:start -->
<div class="pcrf-visual" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; padding: 24px; background: #ffffff; border: 1px solid #dfe1e6; border-radius: 8px; box-sizing: border-box; max-width: 1050px; margin: 0 auto; overflow-x: auto;">
  <style>
    .pcrf-visual { --text:#172b4d; --muted:#6b778c; --border:#dfe1e6; --public:#0052cc; --public-bg:#deebff; --private:#6554c0; --private-bg:#eae6ff; --route:#974f0c; --route-bg:#fff7d6; --ok:#006644; --ok-bg:#e3fcef; }
    .pcrf-visual * { box-sizing:border-box; }
    .pcrf-visual h2 { margin:0; color:var(--text); font-size:18px; }
    .pcrf-visual .subtitle { margin:6px 0 18px; color:var(--muted); font-size:12px; }
    .pcrf-visual .layout { display:grid; grid-template-columns:220px 40px 330px 40px 300px; align-items:center; min-width:930px; }
    .pcrf-visual .card { padding:14px; border:1px solid var(--border); border-radius:8px; background:#fff; }
    .pcrf-visual .card h3 { margin:0 0 10px; color:var(--text); font-size:13px; }
    .pcrf-visual .node { margin:7px 0; padding:9px; border:1px solid var(--border); border-radius:6px; color:var(--text); background:#f4f5f7; font-size:11px; line-height:1.35; }
    .pcrf-visual .public { color:var(--public); background:var(--public-bg); border-color:#b3d4ff; }
    .pcrf-visual .private { color:var(--private); background:var(--private-bg); border-color:#c0b6f2; }
    .pcrf-visual .route { color:var(--route); background:var(--route-bg); border-color:#ffe380; }
    .pcrf-visual .ready { color:var(--ok); background:var(--ok-bg); border-color:#abf5d1; }
    .pcrf-visual .arrow { position:relative; height:2px; background:#7a869a; }
    .pcrf-visual .arrow::after { content:""; position:absolute; right:-1px; top:50%; width:7px; height:7px; border-top:2px solid #7a869a; border-right:2px solid #7a869a; transform:translateY(-50%) rotate(45deg); }
    .pcrf-visual .split { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
    .pcrf-visual .label { color:var(--muted); font-size:9px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; }
    .pcrf-visual .context { margin-top:16px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:9px; min-width:930px; }
    .pcrf-visual .context .node { margin:0; text-align:center; }
    .pcrf-visual .principle { margin-top:16px; padding:10px 12px; color:var(--text); background:#f7f8fa; border-left:3px solid var(--public); font-size:11px; line-height:1.4; min-width:930px; }
  </style>
  <h2>Connection, Registration, Route and Invoice Context</h2>
  <p class="subtitle">A customer may be connected to multiple networks while each invoice flow has one deterministic route.</p>
  <section class="layout" aria-label="Customer legal entity has public and private connections that feed independent inbound and outbound routes">
    <article class="card">
      <span class="label">Business scope</span>
      <h3>Customer legal entity</h3>
      <div class="node">NIF / legal entity</div>
      <div class="node">Test or production</div>
      <div class="node">Authorised ERP / accountant</div>
    </article>
    <div class="arrow" aria-hidden="true"></div>
    <article class="card">
      <span class="label">Available capability</span>
      <h3>Connections and registrations</h3>
      <div class="split">
        <div class="node public">Public connection<br><small>REGISTERED</small></div>
        <div class="node private">Private provider<br><small>READY</small></div>
      </div>
      <div class="node ready">Validated capabilities: inbound / outbound / status</div>
    </article>
    <div class="arrow" aria-hidden="true"></div>
    <article class="card">
      <span class="label">Effective behaviour</span>
      <h3>Independent routes</h3>
      <div class="node public">Inbound → Public</div>
      <div class="node private">Outbound → Private</div>
      <div class="node route">Effective time + audit version</div>
    </article>
  </section>
  <section class="context" aria-label="Invoice route decision is persisted for historical continuity">
    <div class="node">Resolve one eligible route</div>
    <div class="node route">Persist route decision</div>
    <div class="node">Retain provider and lifecycle context</div>
  </section>
  <div class="principle">Changing the customer's current route changes future routing decisions. It does not change the original connection, provider reference, or lifecycle context of existing invoices.</div>
</div>
<!-- confluence-html-macro:end -->

## Problem and business objective

The Phase 2 provider portfolio includes B2B Router, Banqup, EDICOM, SERES, and ZeroComa. Each provider will expose different account structures, credentials, registration steps, invoice directions, status models, and operational limitations.

Without a shared foundation:

- each provider adapter may model the same customer differently;
- completing provider onboarding could accidentally become equivalent to activating a route;
- one customer-wide `PUBLIC_ACTIVE` or `PRIVATE_ACTIVE` state could not represent public inbound with private outbound;
- two overlapping routes could both appear eligible for the same invoice;
- current configuration could overwrite the evidence required to service historical invoices;
- ERP teams would receive provider-specific behaviours instead of a stable Sage contract;
- operations would be unable to explain why a particular connection was selected;
- later Private A ↔ Private B transitions would require redesign rather than extension.

The business objective is to provide a single, auditable and provider-neutral way to answer:

1. Which networks is this legal entity connected to?
2. What external registrations are confirmed?
3. What can each connection currently do?
4. Which connection should handle a new inbound or outbound invoice?
5. Why was that connection selected?
6. Which connection remains responsible for an existing invoice?

## Business value

| Stakeholder | Value |
|---|---|
| Customer or accountant | Prepare private connectivity without an unexpected route change and use different networks for sending and receiving |
| Sage ERP product | Consume one stable connection and routing contract rather than implement five provider models |
| Platform engineering | Add provider adapters behind consistent capability and lifecycle boundaries |
| Operations and support | Explain route decisions, distinguish configuration from provider failure, and recover exceptions safely |
| Product and compliance | Preserve evidence of routing and registration decisions through regulatory change |

## Definitions and concept boundaries

| Term | Definition |
|---|---|
| Legal entity | The customer business or sole trader to which the Spanish NIF and routing scope apply |
| Establishment/presence | Seat, fixed establishment, branch/site or domicile/residence fact relevant to applicability or operation scope |
| Official identifier | Scheme-qualified identifier issued/recognised by an authority for a named subject and purpose; Spanish NIF is not a universal endpoint or credential |
| Participant/entry-point address | Scheme-qualified destination used for directory lookup or routing |
| Delegated authority | Effective evidence that a delegate may perform a named operation for a client, direction, country/route and time |
| Credential reference | Secret/certificate/token reference used to authenticate or secure an operation; possession does not itself prove delegated authority |
| Connection | Sage configuration and secure credential reference used to communicate with one network/provider in one environment |
| External registration | The provider or network's record that the legal entity is enrolled or reachable |
| Capability | An operation a connection is confirmed to support, such as outbound submission, inbound receipt, status retrieval, or reconciliation |
| Readiness | Evidence that a connection can perform a declared capability; readiness does not mean the connection is an active route |
| Route | A time-bound selection of one eligible connection for a defined invoice scope |
| Route scope | The business dimensions to which a route applies; initially legal entity, direction, environment, and effective time |
| Routing decision | The deterministic selection recorded for one invoice |
| Invoice routing snapshot | The immutable route, connection, provider and decision context stored on the invoice |
| Transition | A controlled change from a source route to a target route |
| Deregistration | Ending an external provider/network registration; not the same as route deactivation or customer offboarding |

### Connection versus registration versus route

| Scenario | Connection | Registration | Route |
|---|---|---|---|
| Customer has entered private-provider credentials but validation failed | Exists, not ready | Unknown/not confirmed | Unchanged |
| Private provider is registered and tested before cutover | Ready | Confirmed | Public may remain active |
| Private outbound is activated while public inbound continues | Ready | Confirmed | Outbound private; inbound public |
| Private outbound route is ended | May remain ready | May remain confirmed | No longer selected for new outbound invoices |
| Customer fully deregisters private provider | Disabled/retained for audit | Ended | Must already be inactive or safely transitioned |

## Actors and business scenarios

| Scenario | Primary actor | Expected outcome | Continuity/exception |
|---|---|---|---|
| Prepare private connection | ERP/customer/accountant | Private capability becomes ready without changing public routes | Correct configuration until validation succeeds |
| Activate private outbound | Authorised ERP/customer | New outbound invoices use private; inbound may remain public | Existing public-origin invoices retain public context |
| Activate private inbound | Authorised ERP/customer | New inbound invoices are associated with private connection | Provider reachability/registration must be confirmed |
| Schedule a route change | Authorised ERP/customer | Route becomes effective at agreed time | Conflicting transition is rejected |
| Provider credentials expire | Customer/operations | Connection becomes action-required; unsafe operations stop | Existing work remains visible and recoverable |
| Disable unused connection | Operations/authorised customer | Connection cannot be selected for new routes | Block or warn if active/historical work depends on it |
| Investigate invoice routing | Support/operations | Route selection and historical context can be explained | No secret or unnecessary invoice content exposed |
| Accountant configures several clients | Accountant/client admin | Each connection/route action is evaluated for the named client and operation | Portfolio membership or authentication does not grant access to another client |
| Same NIF has several published entry points/scopes | Customer/platform | Each scheme-qualified destination and effective scope remains separately observable and selectable only under approved precedence | NIF is not used as the participant address by implication |

## Business rules

| ID | Condition | Rule | Rationale/evidence | Status |
|---|---|---|---|---|
| BR1 | Customer is registered with public and private platforms | Registrations may coexist | Confirmed stakeholder decision | Confirmed |
| BR2 | Customer sends and receives invoices | Inbound and outbound routes may use different connections | Confirmed stakeholder scenario | Confirmed |
| BR3 | A connection becomes ready | Readiness must not automatically activate a route | Prevent unintended routing change | Proposed for approval |
| BR4 | A route changes | Only future routing decisions use the new route | Platform Transition Management principle | Confirmed |
| BR5 | Existing invoice requires lifecycle activity | Use its original connection/network context unless an approved rule says otherwise | Transition continuity | Confirmed principle; ownership details open |
| BR6 | Route is deactivated | Connection, registration, credentials, and data are not automatically deleted | Transition is not offboarding | Confirmed principle |
| BR7 | More than one route matches implemented scope | Sage must not choose arbitrarily | Deterministic and auditable routing | Proposed for approval |
| BR8 | Provider capability is unconfirmed | Connection cannot be activated for that capability | Avoid unsupported routing | Proposed for approval |
| BR9 | Connection/route is created | Bind it to a Sage legal subject and, where relevant, establishment/presence and official-identifier references; never use a bare NIF as the global connection key | PRD-SEI-231 identity model | Proposed for approval |
| BR10 | Network destination is required | Store participant/entry-point scheme and value separately from legal/tax identifiers and from provider resource IDs | PRD-SEI-231/233 | Proposed for approval |
| BR11 | Credential successfully authenticates | Treat authentication as connection evidence only; require a separate effective authority decision for protected customer operations | PRD-SEI-231 | Proposed for approval |
| BR12 | Accountant/delegate performs an operation | Grant must cover client, capability, direction, route/country, environment and effective time | PRD-SEI-231 | Proposed for approval |
| BR13 | Identifier, authority or credential changes | Apply the new record prospectively to eligible work; retain the snapshot/evidence used by historical external mutations | Audit and historical-continuity principle | Proposed for approval |

## Scope by capability

| Capability | Phase 2 foundation | Provider PRD | Later phase |
|---|---|---|---|
| Customer/legal-entity connection model | Deliver | Map provider resource | Extend if required |
| Public/private registration coexistence | Deliver | Confirm provider constraints | — |
| Independent inbound/outbound routes | Deliver | Declare capability | — |
| Effective-time route activation | Deliver | Support provider preparation | Extend scheduling policies |
| Invoice routing snapshot | Deliver | Supply provider reference | — |
| Connection/readiness lifecycle | Deliver | Map provider states | — |
| Provider adapter capability contract | Deliver | Implement supported operations | Extend capabilities |
| Document-type/counterparty routing | Model extension point | Evidence use case | Potential later delivery |
| Per-invoice manual override | Exclude | — | Potential later delivery |
| Private A ↔ Private B | Preserve extensibility | — | Phase 3 |
| Automatic failover/route optimisation | Exclude | — | Future decision |

## Goals

- Represent multiple public/private connections and registrations for one legal entity.
- Make inbound and outbound routing independently configurable.
- Establish and validate a provider connection without activating it.
- Resolve one deterministic route for each new invoice.
- Preserve immutable invoice-network context for historical lifecycle continuity.
- Expose a stable, capability-based contract to all Sage ERPs and provider adapters.
- Prevent conflicting routes and unsafe connection disablement.
- Give operations an explainable and auditable view of current and historical routing.

## Non-goals

- A general-purpose routing rules engine.
- Per-invoice caller-selected provider override.
- Automatic failover between private providers.
- Provider-specific authentication or payload mappings.
- Private Provider A ↔ Provider B switching.
- Final customer offboarding, retention deletion, or legal advice.
- Approval of the final technical architecture or persistence technology.

## Research and evidence

| Evidence | Confidence | What it informs | Limitation/follow-up |
|---|---|---|---|
| Platform Transition Management Confluence draft | High internal | Explicit route, historical context, transition/offboarding distinction | Local-team answers still required |
| Public Platform Onboard Confluence draft | Medium internal | Phase 1 onboarding and adapter boundary | Contains public/private and AEAT/VeriFactu concepts that require separation |
| Stakeholder confirmation: public/private coexist | High internal | BR1 and multi-connection model | External/provider mechanics remain to be confirmed |
| Stakeholder scenario: different inbound/outbound networks | High internal | BR2 and direction-level routing | Other route dimensions remain open |
| Provider API evidence packs | Mixed by provider | Capability-based adapter boundary | EDICOM/SERES/ZeroComa endpoint evidence incomplete |

### Research contradictions and gaps

1. The Phase 1 onboarding draft presents private-provider selection inside a public-platform journey. Phase 2 must not assume that flow is an approved contract.
2. The authoritative source of an invoice route remains open with the local team.
3. Historical lifecycle ownership after a route change remains open.
4. Final cutover, rollback and deregistration sequences remain open.
5. Provider-specific capability/readiness evidence differs materially across the five integrations.

These gaps block production route activation, but they do not block defining the shared conceptual foundation or running provider discovery.

## Current-state analysis

Phase 1 is expected to establish public onboarding and invoice lifecycle. The current documentation does not yet demonstrate that all of the following are present in the implemented contract:

- stable connection/route identifiers;
- independent inbound and outbound scope;
- provider-neutral capability readiness;
- immutable invoice routing snapshot;
- effective-time route history;
- explicit external registration observations;
- safe concurrent transition control.

Phase 2 must validate these dependencies before treating the Phase 1 implementation as reusable.

## Proposed solution overview

> **Solution maturity: proposed conceptual model. Architecture approval is required before delivery commitment.**

The foundation separates ten responsibilities:

1. **Legal entity:** owns the Spanish routing scope.
2. **Connection:** stores provider/environment configuration and secure credential references.
3. **External registration:** records intended and last-observed provider/network enrolment state.
4. **Capability readiness:** states what the connection is currently eligible to do.
5. **Route:** selects a ready connection for a time-bound invoice scope.
6. **Invoice routing snapshot:** preserves the decision and provider context used by an invoice.
7. **Legal subject/establishment:** identifies the business/presence for which a connection or route is authorised.
8. **Official/participant identifiers:** keep legal/tax identity and network destination in separate scheme-qualified records.
9. **Delegated authority:** proves that the actor may perform the named operation for this client and time.
10. **Credential reference:** authenticates/secures the boundary without becoming authority by implication.

Provider adapters translate the shared capability contract into provider-specific operations. The routing service does not call a provider synchronously to decide every invoice route; it resolves from validated internal state and then records that decision.

## Conceptual information model

### Connection

| Attribute | Business purpose |
|---|---|
| `connection_id` | Stable Sage identity independent of mutable provider/customer names |
| `legal_entity_id` | Sage legal-subject scope; not a raw NIF |
| `establishment_reference` | Relevant seat/fixed-establishment/branch/presence scope where the connection or external registration requires it |
| `official_identifier_references` | Scheme-qualified subject identifiers with role, validity and verification evidence |
| `provider_id` | Public or private network/provider |
| `environment` | Prevent test/production mixing |
| `credential_reference` | Pointer to approved secret storage; never the secret itself |
| `authority_policy_reference` | Required authority shape for protected provisioning/routing operations; the per-operation decision is bound at execution |
| `capabilities` | Inbound, outbound, status, reconciliation and other confirmed operations |
| `status` | Configuration/communication lifecycle |
| `version` | Concurrency and audit |

### External registration

| Attribute | Business purpose |
|---|---|
| `registration_id` | Stable Sage identity |
| `connection_id` | Owning connection |
| `external_registration_id` | Provider/network traceability |
| `scope/direction` | Registration applicability |
| `participant_address` | Network/directory scheme and value, kept separate from NIF and provider resource ID |
| `subject/establishment_reference` | Legal subject/presence represented by the external registration |
| `intended_status` | State Sage is trying to establish |
| `observed_status` | Last authoritative external observation |
| `observed_at` | Freshness and reconciliation evidence |
| `failure_category` | Actionable ownership and recovery |

### Route

| Attribute | Business purpose |
|---|---|
| `route_id` | Stable route identity |
| `legal_entity_id` | Customer scope |
| `establishment_reference` | Optional approved presence scope; absence must not be inferred from NIF |
| `direction` | Inbound or outbound in initial delivery |
| `connection_id` | Selected eligible connection |
| `environment` | Test or production |
| `effective_from/effective_to` | Historical and scheduled validity |
| `status` | Scheduled, active, retiring or inactive |
| `version` | Conflict prevention and audit |

### Invoice routing snapshot

| Attribute | Business purpose |
|---|---|
| `route_id` | Explain the rule selected |
| `connection_id` | Preserve the connection used |
| `provider_id` | Preserve network/provider identity |
| `direction` and scope | Explain selection context |
| `decision_timestamp` | Resolve cutover-boundary disputes |
| `external_reference` | Continue provider lifecycle operations |
| `protocol/schema_version` | Interpret historical provider data where required |
| `identifier_snapshot` | Legal/tax/participant identifiers actually used and their verification/version evidence |
| `authority_decision_reference` | Actor, client, capability, direction, route/environment and effective grant used for the routing mutation |

## Proposed connection lifecycle

| State | Meaning | Customer/route impact |
|---|---|---|
| `DRAFT` | Required configuration is incomplete | Cannot become active |
| `VALIDATING` | Credentials/configuration are being tested | Existing routes unchanged |
| `PENDING_REGISTRATION` | External registration is not yet confirmed | Cannot activate affected capability |
| `READY` | One or more capabilities are eligible | May be selected by an authorised transition |
| `DEGRADED` | Known impairment exists | Use depends on approved capability/operation policy |
| `ACTION_REQUIRED` | Customer or operator must correct configuration | Unsafe new operations stop |
| `DISABLING` | Impact is being checked and new use is ending | No implicit deregistration |
| `DISABLED` | Cannot be selected for new routes | Historical context remains |
| `FAILED` | Setup could not complete | Correct/retry; routes unchanged |

Connection lifecycle and route lifecycle must remain separate.

## Route resolution

### Initial Phase 2 scope

```text
legal_entity_id + direction + environment + routing_decision_timestamp
```

The model preserves extension points for document type, counterparty, counterparty network and fallback, but Phase 2 does not implement a general rules engine without confirmed need.

### Resolution behaviour

1. Retrieve routes whose effective period contains the decision timestamp.
2. Exclude connections not ready for the required capability.
3. Return exactly one eligible route.
4. If none match, apply only an approved no-route policy; never invent a fallback.
5. If multiple routes match, raise a configuration conflict rather than use database order.
6. Persist the routing snapshot before provider processing starts.
7. Use the stored snapshot for later lifecycle activity.

## Detailed journeys

### Journey A — Prepare private connection without changing routing

1. ERP creates a draft connection for provider, legal entity and environment.
2. Sage returns provider-required configuration and capability expectations.
3. Customer/accountant supplies credentials through a secure flow.
4. Provider adapter validates the configuration and obtains registration evidence.
5. Sage records capability-specific readiness.
6. Connection becomes `READY`.
7. No route changes because no authorised transition was requested.

**Expected outcome:** public routes remain active while private connectivity is prepared.

### Journey B — Activate private outbound while retaining public inbound

1. Authorised actor selects the ready private connection for outbound.
2. Sage validates legal entity, environment, capability, effective time and conflicts.
3. Sage shows current and proposed route impact.
4. Actor confirms.
5. At the effective time, private outbound becomes active.
6. Public inbound remains active.
7. New outbound invoices store private context.
8. Existing public-origin invoices retain public context.

### Journey C — Correct invalid connection configuration

1. Validation rejects credentials, registration data or provider configuration.
2. Connection becomes `ACTION_REQUIRED` or `FAILED` with stable error category.
3. Sage identifies the responsible actor and correction.
4. Actor updates only permitted configuration.
5. Validation is repeated idempotently.
6. No active route changes during correction.

### Journey D — Prevent conflicting route

1. A second activation request overlaps an existing or scheduled route for the same implemented scope.
2. Sage detects the conflict using effective period and version.
3. Request is rejected with existing route/transition reference.
4. No route is activated by arbitrary priority.

### Journey E — Disable connection with historical dependencies

1. Authorised actor requests connection disablement.
2. Sage identifies active routes, scheduled transitions and historical non-terminal invoices.
3. Unsafe disablement is blocked or escalated according to approved policy.
4. Route deactivation/transition occurs separately.
5. External deregistration and credential revocation occur only when explicitly authorised and safe.

## Functional requirements

### Connections, registration and capability

| ID | Requirement |
|---|---|
| FR1 | A legal entity must be able to hold multiple public and private connection records concurrently. |
| FR2 | Each connection must identify legal entity, provider, environment, credential reference, capabilities, lifecycle status and version. |
| FR3 | External registration observations must be represented separately from connection status and active routes. |
| FR4 | Readiness must be declared per supported capability where inbound, outbound, status or reconciliation differ. |
| FR5 | Creating or validating a connection must not activate or change a route. |
| FR6 | Test credentials and resources must not be attached to a production connection. |

### Routing

| ID | Requirement |
|---|---|
| FR7 | Initial route scope must support legal entity, direction, environment and effective time. |
| FR8 | A route must reference one eligible connection and preserve its effective period and audit version. |
| FR9 | Overlapping active/scheduled routes for the same implemented scope must be prevented. |
| FR10 | Route resolution must be deterministic, explainable and independent of mutable provider display names. |
| FR11 | A disabled or capability-ineligible connection must not be selected for a new route. |
| FR12 | Route changes must use concurrency/version controls. |
| FR13 | Deactivating a route must not automatically disable or deregister its connection. |

### Invoice context and continuity

| ID | Requirement |
|---|---|
| FR14 | Every new invoice must persist route, connection, provider, direction, environment and decision timestamp before provider processing. |
| FR15 | External references and protocol/schema context must be added when provider processing supplies them. |
| FR16 | Later configuration changes must not rewrite an existing invoice routing snapshot. |
| FR17 | Historical lifecycle operations must use the original context unless an approved ownership rule requires another behaviour. |
| FR18 | An unresolved historical-ownership case must be surfaced for reconciliation rather than silently rerouted. |

### Adapter and platform contract

| ID | Requirement |
|---|---|
| FR19 | Provider capabilities must be explicit and discoverable through the shared contract. |
| FR20 | Unsupported provider operations must return a stable Sage capability error. |
| FR21 | Provider-specific identifiers and fields must remain within adapter/connection boundaries and not alter shared route semantics. |
| FR22 | Mutating connection, registration and transition operations must accept an idempotency identity and return a stable operation reference. |
| FR23 | Read APIs must distinguish intended Sage state from last-observed provider state and observation freshness. |

### Operations and audit

| ID | Requirement |
|---|---|
| FR24 | Operations must be able to inspect connection, registration, capability, route, transition and invoice-context relationships. |
| FR25 | Every mutation must record actor, reason, timestamp, previous/new state, correlation ID and version. |
| FR26 | Disablement must show active-route and historical-invoice impact before execution. |
| FR27 | Secrets and certificate material must never be returned through client or operations APIs. |

### Identity, establishment and delegated authority

| ID | Requirement |
|---|---|
| FR28 | Connections, registrations and routes must reference stable Sage legal-subject identities and scheme-qualified external identifiers rather than using a bare NIF as a global key. |
| FR29 | The model must support a relevant establishment/presence reference with type, jurisdiction and validity where applicability, registration or route scope depends on it. |
| FR30 | Participant/entry-point scheme and value must be stored separately from legal/tax identifiers, provider resource IDs and credential references. |
| FR31 | Every protected create, validate, register, activate, transition, disable or deregister operation must bind an authority decision covering actor, client, capability, direction/scope, route/country, environment and effective time. |
| FR32 | Authentication or valid credential use must not bypass FR31 or imply accountant/client authority. |
| FR33 | Identifier, establishment, authority and credential snapshots used for an external mutation must remain historically reproducible after later correction, expiry, revocation or route change. |
| FR34 | Accountant bulk processing must evaluate each client/item independently and return per-item authority and routing outcomes without leaking another client's existence or data. |
| FR35 | Product and operations views must distinguish legal subject, official identifier, participant address, provider registration, credential health and delegated-authority status. |

## Proposed client/API capabilities

| Operation | Business behaviour |
|---|---|
| Create connection | Creates `DRAFT`; does not change routing |
| Update connection configuration | Updates permitted metadata or secure credential reference |
| Validate connection | Starts/returns idempotent validation and capability evidence |
| Get connection | Returns status, capabilities, registration summaries and credential metadata |
| Request/inspect registration | Manages external registration where provider requires it |
| List effective routes | Shows active and scheduled inbound/outbound routes |
| Request route transition | Validates target readiness, scope, timing and conflict |
| Resolve route | Internal deterministic selection for a new invoice |
| Disable route | Ends new selection without implicit provider deregistration |
| Disable connection | Runs dependency impact and controlled lifecycle |

Endpoint shapes and technical state names require architecture review.

## Validation and failure rules

| Scenario | Expected behaviour |
|---|---|
| Invalid credentials/configuration | Keep connection non-ready; return actionable correction |
| Registration pending | Preserve pending state; do not activate capability |
| Provider observation stale | Do not use as evidence for irreversible action beyond approved freshness |
| No eligible route | Apply approved no-route behaviour; never silently choose another provider |
| Multiple routes match | Raise configuration conflict and operational signal |
| Duplicate create/transition request | Return existing operation for idempotency identity |
| Concurrent configuration change | Reject stale version and require refresh |
| Disable active connection | Block until route impact is resolved |
| Historical non-terminal invoices exist | Retain required context/access or follow approved exception |

## Non-functional requirements

### Security and privacy

- Credentials, tokens, certificates and PINs must use approved secret storage.
- Connection APIs return metadata and expiry only, never secret values.
- Mutations require authenticated and authorised actors.
- Legal-entity isolation must apply to accountant and multi-company use.
- Logs and audit data must minimise invoice/customer content.

### Reliability and performance

- Normal route resolution must not require a synchronous provider call.
- Route and invoice-snapshot persistence must be atomic or recoverably consistent.
- Connection/route mutations must be idempotent and concurrency-controlled.
- Configuration propagation target and route-resolution latency require engineering baseline and owner.

### Audit and retention

- Historical route periods and invoice snapshots must remain explainable for the applicable retention period.
- Credential lifecycle, data retention and deregistration must remain separately controllable.
- Audit records must be immutable according to approved policy.

## Product and operational experience

### Customer/ERP

Clients must clearly distinguish:

1. configuration complete;
2. external registration confirmed;
3. capability ready;
4. route active;
5. action required.

The customer must be able to prepare a connection without an unexpected invoice-routing change.

### Operations

Operations must be able to answer:

- What did Sage intend?
- What did the provider last report, and when?
- What route is active/scheduled for each direction?
- Why was this connection selected for this invoice?
- Which invoices depend on a connection before disablement?
- Which actor changed the state and why?

## Acceptance criteria

1. One legal entity can hold public and multiple private connections concurrently.
2. A private connection can become ready while public inbound/outbound routes remain unchanged.
3. Public inbound and private outbound can be active at the same time.
4. A connection without outbound readiness cannot be activated for outbound.
5. Overlapping routes for the same implemented scope are rejected.
6. A route resolves deterministically at the cutover boundary using the decision timestamp.
7. An invoice created before and after cutover retains the correct, different routing snapshot.
8. Test and production credentials, registrations and routes cannot be mixed.
9. Disabling a route leaves connection/registration records and historical invoice context intact.
10. Disabling a connection shows and protects active/historical dependencies.
11. Provider-specific fields do not change the shared route contract.
12. Every mutation and route decision is auditable without exposing secrets.
13. A connection using a valid credential cannot activate a route when the actor lacks an effective client- and operation-specific authority grant.
14. Two scheme-qualified entry points associated with the same NIF remain separate destinations and are not collapsed into one route by value matching.
15. Changing a current identifier, credential or delegated grant does not rewrite the snapshot used by an existing invoice or completed route mutation.
16. An accountant bulk request containing one authorised and one unauthorised client produces independent item outcomes and exposes no unauthorised client data.

## Metrics

| Metric | Target/direction | Evidence status |
|---|---|---|
| New invoices with complete routing snapshot | 100% | Proposed target |
| Audited connection and route mutations | 100% | Proposed target |
| Conflicting active routes in implemented scope | 0 | Proposed target |
| Provider integrations using shared connection model | 100% of Phase 2 portfolio | Proposed target |
| Route resolution latency | Baseline and target required | Open — engineering owner |
| Configuration-to-readiness time | Measure by provider and journey | Open — product/provider baseline |
| Support cases where route cannot be explained | 0 | Proposed direction |

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Provider states are forced into one generic lifecycle | Loss of provider meaning and recovery options | Shared capability model plus raw provider evidence |
| One global customer state is retained | Cannot represent independent inbound/outbound routes | Separate connection, registration and route |
| Advanced rules are built before evidence | Delivery delay and ambiguous precedence | Implement direction-level scope first; preserve extension points |
| Route resolution depends on live provider call | Availability and latency risk | Resolve from reconciled internal readiness |
| Current route overwrites historical context | Broken status/audit continuity | Immutable invoice routing snapshot |
| Connection disabled too early | Historical lifecycle failure | Dependency impact and separate deregistration |
| NIF is used as tenant, endpoint and credential key | Cross-client access, wrong route and unexplainable history | Separate Sage subject, scheme-qualified identifier, participant address and credential records |
| Authentication is treated as authority | Accountant or integration performs an unauthorised client operation | Operation-specific authority evaluation and audited denial |
| Proposed model is treated as approved architecture | Premature implementation constraint | Architecture decision gate and explicit labels |

## Dependencies and rollout

1. Confirm Phase 1 invoice/network fields and migration needs.
2. Agree terminology and business rules with product, local team and architecture.
3. Confirm initial route scope and no-route behaviour.
4. Implement connection, registration and capability lifecycle.
5. Implement route history, deterministic resolution and invoice snapshot.
6. Validate with one reference provider.
7. Integrate resilience/operations controls from PRD-SEI-203.
8. Pilot with one ERP/customer cohort.
9. Enable further providers only after capability and readiness mapping passes.

### Production entry gates

- Route authority confirmed by the local team.
- Historical lifecycle ownership confirmed.
- Cutover, rollback and deregistration sequences approved.
- Phase 1 dependency/migration assessment complete.
- Architecture and security reviews complete.
- Reference provider passes sandbox, reconciliation and continuity tests.
- Operations runbook, dashboards and ownership agreed.

## Consultation and open decisions

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| What is the authoritative routing input/directory? | Determines eligibility and reconciliation | Spain local team | Production routing | Sage configuration must be checked against authoritative source |
| At what moment is invoice route fixed? | Determines cutover-boundary behaviour | Product + architecture | Detailed design | Before provider processing, using persisted decision timestamp |
| Who owns historical lifecycle after route change? | Determines connection/credential retention | Spain local team/provider | Production transition | Original provider context remains authoritative |
| What happens when no route is eligible? | Determines customer/API and queue behaviour | Product + operations | API contract | Fail explicitly; do not invent fallback |
| Which additional route dimensions are required? | Determines schema/precedence | Product/local team | Later scope, not initial foundation | Direction-level initial delivery |
| How fresh must provider state be before activation/disablement? | Determines safe irreversible actions | Architecture + provider | Operational design | Provider-specific threshold |
| Which Spain evidence proves authority for registration, route activation, invoice retrieval, lifecycle reporting and deregistration? | Prevents one broad accountant/platform grant from authorising every operation | Local legal/identity/security | Production activation | Use operation-specific grants; evidence matrix required |
| When does a Spanish seat/fixed establishment/branch become part of route scope rather than transaction-only applicability? | Determines connection cardinality without inventing a SIRET-like hierarchy | Local legal/product/architecture | Detailed model/pilot | Keep optional establishment reference and activate only confirmed granularity |
| What authoritative source and scheme identify each public/private entry point? | Prevents NIF from becoming an assumed network address | Local technical team/providers | Production routing | Scheme-qualified address plus observed evidence |

## Decisions

| Date | Decision | Evidence/status |
|---|---|---|
| 2026-07-27 | Public and private registrations may coexist | Confirmed stakeholder decision |
| 2026-07-27 | Inbound and outbound may use different networks | Confirmed stakeholder scenario |
| 2026-07-27 | Connections, registrations and routes require separate concepts | Proposed solution principle |
| 2026-07-27 | Direction-level routing precedes advanced rule dimensions | Proposed delivery boundary |
| 2026-07-28 | PRD explicitly separates business rules, research and proposed solution analysis | Draft improvement |

## Revision history

| Date | Version/revision | Change | Pull request |
|---|---|---|---|
| 2026-07-27 | `phase2-prds-v0.1` | Initial discovery draft | |
| 2026-07-27 | `phase2-prds-v0.2` | Confluence publication baseline | |
| 2026-07-28 | Draft | Deepened business analysis, research, solution, visual, traceability and readiness gates | |
| 2026-08-24 | Working revision | Separated legal subject, establishment, official identifier, participant address, credential and delegated authority; added historical snapshots and accountant-isolation acceptance coverage | PRD-SEI-231/233; Spain solution-design brief comparison | |
