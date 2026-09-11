---
id: PRD-SEI-213
title: Phase 2 — Private Platform Connectivity — Structured Review
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-09-11
reviewers: []
related:
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
  - PRD-SEI-216
  - PRD-SEI-217
  - PRD-SEI-218
  - PRD-SEI-219
  - PRD-SEI-220
  - PRD-SEI-235
  - https://confluence.sage.com/spaces/DNBU/pages/855183578/Platform+Transition+Management
  - https://confluence.sage.com/spaces/DNBU/pages/837610648/Public+Platform+Onboard
  - research/PRD-SEI-201-spain-use-case-evidence.md
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588792"
  page_id: "837588799"
  title: Phase 2 - Private Platform Connectivity
  layout: two_left_sidebar
  toc: true
---

# Phase 2 — Private Platform Connectivity — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-201, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-213, adds Confluence layout/navigation metadata, aligns the Phase 2 hierarchy, and recognises the Provider API, Sage adapter and approved hybrid integration modes. |
| Unchanged areas | Existing business analysis, research evidence, scenarios, requirements, acceptance criteria, risks and route principles remain based on PRD-SEI-201. |
| Decisions still open | Architecture must select the integration mode and authoritative operation owner per provider capability; provider readiness and contract details remain evidence-gated. |

## Summary

Enable a Spanish e-invoicing customer to establish supported private-platform connections alongside their public-platform registration, independently route inbound and outbound invoice flows through an eligible connection, and change those routes without losing the status, audit history, or network context of existing invoices.

This is the umbrella Phase 2 PRD. Shared routing, resilience, and provider-specific requirements are defined in the related PRDs.

## Phase 2 provider landscape

This visual shows the product boundary and common integration model. It is a portfolio view, not a commitment that every provider supports identical capabilities or uses the same network initiator. Provider readiness, authentication, registration, document exchange, status behaviour, and limitations remain governed by the relevant provider PRD and evidence gate.

The provider boundary can be implemented through the Sage-owned Provider API, a Sage-managed provider adapter, or an explicitly approved hybrid. Bidirectional invoice and lifecycle exchange is required; it does not by itself require both Sage and the provider to expose or call APIs in both directions.

<!-- confluence-html-macro:start -->
<div class="p2pl-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; padding:26px; background:#ffffff; border:1px solid #dfe1e6; border-radius:8px; box-sizing:border-box; max-width:1160px; margin:0 auto; overflow-x:auto;">
  <style>
    .p2pl-visual { --text:#172b4d; --muted:#6b778c; --border:#dfe1e6; --sage:#006644; --sage-bg:#e3fcef; --private:#6554c0; --private-bg:#eae6ff; --route:#42526e; --route-bg:#f4f5f7; --public:#0052cc; --public-bg:#deebff; --warning:#974f0c; --warning-bg:#fff7d6; }
    .p2pl-visual * { box-sizing:border-box; }
    .p2pl-visual h2 { margin:0; color:var(--text); font-size:18px; font-weight:600; }
    .p2pl-visual .p2pl-subtitle { margin:6px 0 16px; color:var(--muted); font-size:12px; line-height:1.45; }
    .p2pl-visual .p2pl-canvas { min-width:1080px; border:1px solid var(--border); border-radius:8px; background:#fcfcfd; }
    .p2pl-visual svg { display:block; width:1080px; height:580px; }
    .p2pl-visual .p2pl-title { fill:var(--text); font-size:14px; font-weight:700; }
    .p2pl-visual .p2pl-label { fill:var(--muted); font-size:9px; font-weight:700; letter-spacing:.08em; }
    .p2pl-visual .p2pl-copy { fill:#42526e; font-size:10px; }
    .p2pl-visual .p2pl-small { fill:var(--muted); font-size:9px; }
    .p2pl-visual .p2pl-sage-card { fill:var(--sage-bg); stroke:#abf5d1; stroke-width:1.5; }
    .p2pl-visual .p2pl-platform-card { fill:#ffffff; stroke:#79f2c0; stroke-width:2; }
    .p2pl-visual .p2pl-layer { fill:#f4f5f7; stroke:#dfe1e6; stroke-width:1; }
    .p2pl-visual .p2pl-route-layer { fill:var(--warning-bg); stroke:#ffe380; stroke-width:1; }
    .p2pl-visual .p2pl-adapter-card { fill:#ffffff; stroke:#c0b6f2; stroke-width:1.5; stroke-dasharray:5 4; }
    .p2pl-visual .p2pl-provider-card { fill:var(--private-bg); stroke:#c0b6f2; stroke-width:1.25; }
    .p2pl-visual .p2pl-public-card { fill:var(--public-bg); stroke:#b3d4ff; stroke-width:1.25; stroke-dasharray:5 4; }
    .p2pl-visual .p2pl-path-main { fill:none; stroke:var(--sage); stroke-width:2.2; }
    .p2pl-visual .p2pl-path-provider { fill:none; stroke:#7a869a; stroke-width:1.5; stroke-dasharray:5 4; }
    .p2pl-visual .p2pl-path-public { fill:none; stroke:var(--public); stroke-width:1.5; stroke-dasharray:5 4; }
    .p2pl-visual .p2pl-arrow-main { fill:none; stroke:var(--sage); stroke-width:2.2; }
    .p2pl-visual .p2pl-arrow-provider { fill:none; stroke:#7a869a; stroke-width:1.5; }
    .p2pl-visual .p2pl-arrow-public { fill:none; stroke:var(--public); stroke-width:1.5; }
    .p2pl-visual .p2pl-provider-title { fill:var(--private); font-size:11px; font-weight:700; }
    .p2pl-visual .p2pl-public-title { fill:var(--public); font-size:11px; font-weight:700; }
    .p2pl-visual .p2pl-sage-title { fill:var(--sage); font-size:13px; font-weight:700; }
    .p2pl-visual .p2pl-route-title { fill:var(--warning); font-size:10px; font-weight:700; }
    .p2pl-visual .p2pl-notes { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; min-width:1080px; margin-top:14px; }
    .p2pl-visual .p2pl-note { padding:11px 12px; border:1px solid var(--border); border-radius:7px; color:#42526e; background:#fff; font-size:10px; line-height:1.45; }
    .p2pl-visual .p2pl-note strong { display:block; margin-bottom:3px; color:var(--text); font-size:11px; }
    .p2pl-visual .p2pl-legend { display:flex; flex-wrap:wrap; gap:14px; min-width:1080px; margin-top:12px; color:var(--muted); font-size:10px; }
    .p2pl-visual .p2pl-key { display:inline-flex; align-items:center; gap:5px; }
    .p2pl-visual .p2pl-swatch { width:10px; height:10px; border-radius:2px; }
    .p2pl-visual .p2pl-swatch-sage { background:var(--sage); }
    .p2pl-visual .p2pl-swatch-private { background:var(--private); }
    .p2pl-visual .p2pl-swatch-public { background:var(--public); }
    .p2pl-visual .p2pl-line { width:20px; border-top:1.5px dashed #7a869a; }
  </style>

  <h2>Sage and the Phase 2 Private Provider Landscape</h2>
  <p class="p2pl-subtitle">One shared Sage platform provides connection, routing and resilience controls while each capability selects a Sage Provider API, Sage adapter or approved hybrid boundary.</p>

  <div class="p2pl-canvas">
    <svg viewBox="0 0 1080 580" role="img" aria-label="Sage ERP products connect to the Sage e-Invoicing platform, which selects a governed Provider API, provider adapter or hybrid integration boundary for B2B Router, Banqup, EDICOM, SERES or ZeroComa while retaining an optional coexisting public-platform route.">
      <text x="42" y="44" class="p2pl-label">SAGE PRODUCTS</text>
      <text x="292" y="44" class="p2pl-label">SHARED PLATFORM CAPABILITY</text>
      <text x="650" y="44" class="p2pl-label">PROVIDER BOUNDARY</text>
      <text x="872" y="44" class="p2pl-label">PRIVATE PROVIDERS</text>

      <rect x="36" y="210" width="190" height="116" rx="10" class="p2pl-sage-card"></rect>
      <text x="131" y="244" text-anchor="middle" class="p2pl-sage-title">Sage ERPs</text>
      <text x="131" y="266" text-anchor="middle" class="p2pl-copy">Authorised customer action</text>
      <text x="131" y="284" text-anchor="middle" class="p2pl-copy">Invoice and status exchange</text>
      <text x="131" y="306" text-anchor="middle" class="p2pl-small">One consistent product experience</text>

      <path d="M226 268 H278" class="p2pl-path-main"></path>
      <path d="M268 261 L278 268 L268 275" class="p2pl-arrow-main"></path>

      <rect x="280" y="118" width="310" height="300" rx="12" class="p2pl-platform-card"></rect>
      <text x="435" y="148" text-anchor="middle" class="p2pl-sage-title">Sage e-Invoicing</text>
      <text x="435" y="166" text-anchor="middle" class="p2pl-small">Shared Phase 2 product and operating model</text>

      <rect x="306" y="186" width="258" height="54" rx="7" class="p2pl-layer"></rect>
      <text x="435" y="208" text-anchor="middle" class="p2pl-title">Connection and registration</text>
      <text x="435" y="226" text-anchor="middle" class="p2pl-small">Establish capability without activating a route</text>

      <rect x="306" y="252" width="258" height="68" rx="7" class="p2pl-route-layer"></rect>
      <text x="435" y="275" text-anchor="middle" class="p2pl-route-title">Routing and transition control</text>
      <text x="435" y="293" text-anchor="middle" class="p2pl-small">Legal entity • direction • environment • effective time</text>
      <text x="435" y="307" text-anchor="middle" class="p2pl-small">Persist the selected route on every invoice</text>

      <rect x="306" y="332" width="258" height="60" rx="7" class="p2pl-layer"></rect>
      <text x="435" y="355" text-anchor="middle" class="p2pl-title">Resilience and operations</text>
      <text x="435" y="373" text-anchor="middle" class="p2pl-small">Observe • retry safely • reconcile • recover</text>

      <path d="M590 268 H638" class="p2pl-path-main"></path>
      <path d="M628 261 L638 268 L628 275" class="p2pl-arrow-main"></path>

      <rect x="640" y="118" width="176" height="300" rx="12" class="p2pl-adapter-card"></rect>
      <text x="728" y="150" text-anchor="middle" class="p2pl-title">Provider integration boundary</text>
      <text x="728" y="171" text-anchor="middle" class="p2pl-small">Mode selected per capability</text>
      <rect x="662" y="190" width="132" height="42" rx="6" class="p2pl-layer"></rect>
      <text x="728" y="215" text-anchor="middle" class="p2pl-copy">Sage Provider API</text>
      <rect x="662" y="242" width="132" height="42" rx="6" class="p2pl-layer"></rect>
      <text x="728" y="267" text-anchor="middle" class="p2pl-copy">Sage provider adapter</text>
      <rect x="662" y="294" width="132" height="42" rx="6" class="p2pl-layer"></rect>
      <text x="728" y="319" text-anchor="middle" class="p2pl-copy">Approved hybrid</text>
      <rect x="662" y="346" width="132" height="42" rx="6" class="p2pl-layer"></rect>
      <text x="728" y="371" text-anchor="middle" class="p2pl-copy">One operation owner</text>

      <path d="M816 268 H842" class="p2pl-path-provider"></path>
      <path d="M842 82 V410" class="p2pl-path-provider"></path>
      <path d="M842 82 H866" class="p2pl-path-provider"></path>
      <path d="M856 76 L866 82 L856 88" class="p2pl-arrow-provider"></path>
      <path d="M842 164 H866" class="p2pl-path-provider"></path>
      <path d="M856 158 L866 164 L856 170" class="p2pl-arrow-provider"></path>
      <path d="M842 246 H866" class="p2pl-path-provider"></path>
      <path d="M856 240 L866 246 L856 252" class="p2pl-arrow-provider"></path>
      <path d="M842 328 H866" class="p2pl-path-provider"></path>
      <path d="M856 322 L866 328 L856 334" class="p2pl-arrow-provider"></path>
      <path d="M842 410 H866" class="p2pl-path-provider"></path>
      <path d="M856 404 L866 410 L856 416" class="p2pl-arrow-provider"></path>

      <rect x="868" y="52" width="176" height="60" rx="8" class="p2pl-provider-card"></rect>
      <text x="956" y="78" text-anchor="middle" class="p2pl-provider-title">B2B Router</text>
      <text x="956" y="96" text-anchor="middle" class="p2pl-small">Provider-specific contract</text>

      <rect x="868" y="134" width="176" height="60" rx="8" class="p2pl-provider-card"></rect>
      <text x="956" y="160" text-anchor="middle" class="p2pl-provider-title">Banqup (Unifiedpost)</text>
      <text x="956" y="178" text-anchor="middle" class="p2pl-small">Provider-specific contract</text>

      <rect x="868" y="216" width="176" height="60" rx="8" class="p2pl-provider-card"></rect>
      <text x="956" y="242" text-anchor="middle" class="p2pl-provider-title">EDICOM</text>
      <text x="956" y="260" text-anchor="middle" class="p2pl-small">Provider-specific contract</text>

      <rect x="868" y="298" width="176" height="60" rx="8" class="p2pl-provider-card"></rect>
      <text x="956" y="324" text-anchor="middle" class="p2pl-provider-title">SERES (Docaposte)</text>
      <text x="956" y="342" text-anchor="middle" class="p2pl-small">Provider-specific contract</text>

      <rect x="868" y="380" width="176" height="60" rx="8" class="p2pl-provider-card"></rect>
      <text x="956" y="406" text-anchor="middle" class="p2pl-provider-title">ZeroComa</text>
      <text x="956" y="424" text-anchor="middle" class="p2pl-small">Provider-specific contract</text>

      <path d="M435 418 V470" class="p2pl-path-public"></path>
      <path d="M428 460 L435 470 L442 460" class="p2pl-arrow-public"></path>
      <rect x="306" y="472" width="258" height="70" rx="8" class="p2pl-public-card"></rect>
      <text x="435" y="500" text-anchor="middle" class="p2pl-public-title">Spanish Public Platform</text>
      <text x="435" y="520" text-anchor="middle" class="p2pl-copy">May coexist with private connections</text>
      <text x="435" y="535" text-anchor="middle" class="p2pl-small">Inbound and outbound routes remain independently controlled</text>

      <text x="682" y="455" class="p2pl-small">Dashed routes are selectable capabilities,</text>
      <text x="682" y="471" class="p2pl-small">not automatic activation or failover.</text>
    </svg>
  </div>

  <div class="p2pl-notes">
    <div class="p2pl-note"><strong>Shared Sage foundation</strong>Connections, scoped routing, invoice context, resilience and operational controls are defined once for all providers.</div>
    <div class="p2pl-note"><strong>Governed integration direction</strong>Each capability records who initiates the call and whether the provider consumes Sage's API, Sage consumes the provider contract, or an approved hybrid is used.</div>
    <div class="p2pl-note"><strong>Explicit route activation</strong>A ready provider connection becomes active only through an authorised routing decision; coexistence does not imply duplicate delivery.</div>
  </div>

  <div class="p2pl-legend" aria-label="Diagram legend">
    <span class="p2pl-key"><i class="p2pl-swatch p2pl-swatch-sage"></i>Sage-managed capability</span>
    <span class="p2pl-key"><i class="p2pl-swatch p2pl-swatch-private"></i>Private provider</span>
    <span class="p2pl-key"><i class="p2pl-swatch p2pl-swatch-public"></i>Public platform</span>
    <span class="p2pl-key"><i class="p2pl-line"></i>Selectable route or provider boundary</span>
  </div>
</div>
<!-- confluence-html-macro:end -->

## Phase 2 PRD set

| ID | Document | Purpose |
|---|---|---|
| PRD-SEI-201 | Public and Private Platform Transition | Phase 2 outcomes, scope, journeys, and delivery gates |
| PRD-SEI-202 | Private Platform Connection and Routing Foundation | Shared connection, route, registration, and transition model |
| PRD-SEI-203 | Private Platform Resilience and Operations | Cross-provider reliability, reconciliation, monitoring, and recovery |
| PRD-SEI-235 | Provider API for e-Invoicing Service | Sage-owned provider-facing contract and integration-direction decision model |
| PRD-SEI-216 | B2B Router Integration | Current B2B Router evidence, onboarding and capability-boundary decisions |
| PRD-SEI-217 | Banqup (Unifiedpost) Integration | Current Banqup evidence, onboarding and capability-boundary decisions |
| PRD-SEI-218 | EDICOM Integration | Current EDICOM discovery gates and capability-boundary decisions |
| PRD-SEI-219 | SERES (Docaposte) Integration | Current SERES discovery gates and capability-boundary decisions |
| PRD-SEI-220 | ZeroComa Integration | Current ZeroComa discovery gates and capability-boundary decisions |

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
- Per-invoice manual provider selection unless the open Phase 2 scope decision explicitly promotes it.
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

## Research and evidence

| Evidence | Confidence | Phase 2 implication | Limitation/action |
|---|---|---|---|
| Platform Transition Management draft | High internal | Transition continuity, route/offboarding distinction, audit and recoverability | Route authority, ownership and sequence remain open |
| Public Platform Onboard draft | Medium internal | Phase 1 dependency and adapter boundary | Public/private and AEAT/VeriFactu concepts require separation |
| Stakeholder confirmation on coexistence | High internal | Public/private connections may coexist | Provider mechanics still require validation |
| Stakeholder confirmation on mixed directions | High internal | Public inbound/private outbound and inverse must be representable | Route-authority mechanism remains open |
| `eInvoicing Spain Use Cases.pptx` (May 2026) | Medium internal discovery | Adds Public → Private, multiple platforms, transformation, retrieval, dual channel, corrections and accountant scenarios | Regulatory/technical claims require official/local-team validation |
| Provider API evidence packs | Mixed | Provider-specific capabilities and resilience | Technical evidence incomplete for several providers |

### Research interpretation

The PowerPoint is treated as use-case discovery evidence, not an approved regulatory specification. In particular, the following claims must not become delivery requirements until confirmed:

- absence of a central directory;
- four-day automatic acceptance timing;
- a receiver endpoint field in UBL;
- the party responsible for public-platform polling;
- trusted-copy and format-transformation responsibilities;
- the legal duration/behaviour of dual PDF and e-invoice delivery.

## Business rules and scope hypotheses

| ID | Condition | Rule/hypothesis | Status |
|---|---|---|---|
| BR1 | Public and private registrations coexist | Connection readiness and active routing remain separate | Confirmed product principle |
| BR2 | Inbound and outbound use different networks | Resolve and transition routes independently by direction | Confirmed scenario |
| BR3 | Route changes | New invoices use the effective route; existing invoices retain original context | Confirmed principle |
| BR4 | Company has multiple private providers | Model multiple connections without assuming all are active | Supported by foundation; provider selection open |
| BR5 | Specific invoice may require another provider | Do not implement override until authority, precedence and audit are approved | Open Phase 2 scope decision |
| BR6 | Provider transforms format | Preserve sufficient original/transformed context to avoid silent data loss | Proposed; evidence required |
| BR7 | PDF and e-invoice represent the same business invoice | Correlate channels and prevent duplicate business processing | Proposed adjacent requirement |
| BR8 | Accountant accesses client invoices | Delegated authority and certificate ownership must be explicit | Open identity/certificate dependency |

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

### Research and scope-decision requirements

These items require an explicit answer or related-PRD allocation before the Phase 2 delivery baseline is approved. They are not silently committed functionality.

| ID | Required decision/evidence | Result required |
|---|---|---|
| DR1 | Authoritative receiver/platform identification | Define route input, ownership and discrepancy handling |
| DR2 | Multiple private platforms and per-invoice override | Confirm initial scope, precedence, permissions and audit |
| DR3 | Public → Private retrieval responsibility | Identify who polls/retrieves and how missed invoices are detected |
| DR4 | Format transformation and trusted-copy behaviour | Define canonical/original document storage and data-loss policy |
| DR5 | Public polling and claimed auto-acceptance timing | Validate official behaviour and define alert/service targets |
| DR6 | Dual PDF + e-invoice delivery | Define correlation, customer experience and duplicate prevention |
| DR7 | Rejection, correction, credit note and payment status | Define lifecycle linkage and platform ownership after route change |
| DR8 | Accountant delegated visibility | Define authorisation, multi-certificate lifecycle and cross-product synchronisation |

## Detailed journeys

The visual summarises the Phase 2 customer and operations journeys. It does not replace the journey catalogue, business rules, lifecycle requirements, failure behaviour or consultation decisions that follow.

<!-- confluence-html-macro:start -->
<div class="p2j-visual" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; padding: 26px; background: #ffffff; border: 1px solid #dfe1e6; border-radius: 8px; box-sizing: border-box; max-width: 1120px; margin: 0 auto; overflow-x: auto;">
  <style>
    .p2j-visual { --text:#172b4d; --muted:#6b778c; --border:#dfe1e6; --public:#0052cc; --public-bg:#deebff; --private:#6554c0; --private-bg:#eae6ff; --success:#006644; --success-bg:#e3fcef; --warning:#974f0c; --warning-bg:#fff7d6; --danger:#bf2600; --danger-bg:#ffebe6; --future:#42526e; --future-bg:#f4f5f7; }
    .p2j-visual * { box-sizing:border-box; }
    .p2j-visual h2 { margin:0; color:var(--text); font-size:18px; font-weight:600; }
    .p2j-visual .p2j-subtitle { margin:6px 0 8px; color:var(--muted); font-size:12px; line-height:1.45; }
    .p2j-visual .p2j-principle { display:inline-block; margin:0 0 20px; padding:5px 9px; color:var(--text); background:#f4f5f7; border-radius:999px; font-size:10px; font-weight:700; }
    .p2j-visual .p2j-lanes { display:grid; grid-template-columns: 1fr 1fr 1fr; gap:12px; min-width:1000px; }
    .p2j-visual .p2j-lane { padding:14px; border:1px solid var(--border); border-radius:8px; background:#fcfcfd; }
    .p2j-visual .p2j-lane-head { display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:10px; }
    .p2j-visual .p2j-lane h3 { margin:0; color:var(--text); font-size:13px; }
    .p2j-visual .p2j-lane-label { color:var(--muted); font-size:9px; font-weight:700; letter-spacing:.07em; text-transform:uppercase; }
    .p2j-visual .p2j-card { position:relative; min-height:112px; margin:9px 0; padding:11px 11px 10px 34px; border:1px solid var(--border); border-radius:7px; background:#fff; color:var(--text); font-size:10px; line-height:1.4; }
    .p2j-visual .p2j-card strong { display:block; margin-bottom:4px; font-size:11px; }
    .p2j-visual .p2j-step { position:absolute; left:9px; top:10px; width:18px; height:18px; display:flex; align-items:center; justify-content:center; border-radius:50%; color:#fff; background:#7a869a; font-size:9px; font-weight:700; }
    .p2j-visual .p2j-public { border-color:#b3d4ff; background:var(--public-bg); color:var(--public); }
    .p2j-visual .p2j-public .p2j-step { background:var(--public); }
    .p2j-visual .p2j-private { border-color:#c0b6f2; background:var(--private-bg); color:var(--private); }
    .p2j-visual .p2j-private .p2j-step { background:var(--private); }
    .p2j-visual .p2j-success { border-color:#abf5d1; background:var(--success-bg); color:var(--success); }
    .p2j-visual .p2j-success .p2j-step { background:var(--success); }
    .p2j-visual .p2j-warning { border-color:#ffe380; background:var(--warning-bg); color:var(--warning); }
    .p2j-visual .p2j-warning .p2j-step { background:#ff991f; }
    .p2j-visual .p2j-danger { border-color:#ffbdad; background:var(--danger-bg); color:var(--danger); }
    .p2j-visual .p2j-danger .p2j-step { background:var(--danger); }
    .p2j-visual .p2j-arrow { height:14px; position:relative; }
    .p2j-visual .p2j-arrow::before { content:""; position:absolute; left:50%; top:0; bottom:3px; width:1.5px; background:#7a869a; }
    .p2j-visual .p2j-arrow::after { content:""; position:absolute; left:50%; bottom:1px; width:6px; height:6px; border-right:1.5px solid #7a869a; border-bottom:1.5px solid #7a869a; transform:translateX(-50%) rotate(45deg); }
    .p2j-visual .p2j-split { display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-top:7px; }
    .p2j-visual .p2j-route { padding:6px; border:1px solid; border-radius:5px; font-size:9px; font-weight:700; text-align:center; }
    .p2j-visual .p2j-route-public { color:var(--public); background:#fff; border-color:#b3d4ff; }
    .p2j-visual .p2j-route-private { color:var(--private); background:#fff; border-color:#c0b6f2; }
    .p2j-visual .p2j-continuity { margin-top:14px; display:grid; grid-template-columns:1fr auto 1fr; align-items:center; gap:12px; padding:13px; border:1px dashed #c1c7d0; border-radius:8px; background:#f7f8fa; min-width:1000px; }
    .p2j-visual .p2j-continuity div { color:var(--text); font-size:10px; line-height:1.4; text-align:center; }
    .p2j-visual .p2j-continuity strong { display:block; margin-bottom:3px; font-size:11px; }
    .p2j-visual .p2j-life-arrow { color:var(--muted); font-size:18px; }
    .p2j-visual .p2j-discovery { margin-top:14px; padding:13px; border-left:3px solid #ffab00; background:var(--warning-bg); min-width:1000px; }
    .p2j-visual .p2j-discovery h3 { margin:0 0 8px; color:var(--warning); font-size:12px; }
    .p2j-visual .p2j-chips { display:flex; flex-wrap:wrap; gap:7px; }
    .p2j-visual .p2j-chip { padding:5px 8px; border:1px solid #ffe380; border-radius:999px; color:var(--warning); background:#fff; font-size:9px; font-weight:600; }
    .p2j-visual .p2j-footer { margin-top:13px; padding:10px 12px; color:var(--text); background:#f7f8fa; border-left:3px solid var(--public); font-size:11px; line-height:1.45; min-width:1000px; }
  </style>

  <h2>Phase 2 Private Platform Journeys</h2>
  <p class="p2j-subtitle">Prepare private connectivity, activate only the intended route scope, and recover without losing historical invoice context.</p>
  <span class="p2j-principle">Connect → Validate → Activate → Observe → Recover</span>

  <section class="p2j-lanes" aria-label="Phase 2 private platform journeys grouped into prepare, activate and recover lanes">
    <article class="p2j-lane">
      <div class="p2j-lane-head"><h3>Prepare</h3><span class="p2j-lane-label">No route change</span></div>
      <div class="p2j-card p2j-private"><span class="p2j-step">A1</span><strong>Create private connection</strong>Choose provider, legal entity, environment and intended inbound/outbound capabilities.</div>
      <div class="p2j-arrow" aria-hidden="true"></div>
      <div class="p2j-card p2j-warning"><span class="p2j-step">A2</span><strong>Validate and register</strong>Check credentials, provider configuration, external registration and capability readiness.</div>
      <div class="p2j-arrow" aria-hidden="true"></div>
      <div class="p2j-card p2j-success"><span class="p2j-step">A3</span><strong>Ready but inactive</strong>Public routes remain effective until an authorised transition is confirmed.</div>
    </article>

    <article class="p2j-lane">
      <div class="p2j-lane-head"><h3>Activate</h3><span class="p2j-lane-label">Scoped transition</span></div>
      <div class="p2j-card"><span class="p2j-step">B1</span><strong>Request route change</strong>Choose inbound, outbound or both; validate authority, capability, timing and conflicts.</div>
      <div class="p2j-arrow" aria-hidden="true"></div>
      <div class="p2j-card p2j-warning"><span class="p2j-step">B2</span><strong>Prepare and cut over</strong>Schedule/confirm the effective time and reconcile any required external state.</div>
      <div class="p2j-arrow" aria-hidden="true"></div>
      <div class="p2j-card p2j-private"><span class="p2j-step">B3</span><strong>Mixed routes supported</strong>
        <div class="p2j-split"><span class="p2j-route p2j-route-public">Inbound: Public</span><span class="p2j-route p2j-route-private">Outbound: Private</span></div>
        New invoices use the effective route for their direction.
      </div>
    </article>

    <article class="p2j-lane">
      <div class="p2j-lane-head"><h3>Recover</h3><span class="p2j-lane-label">Controlled exception</span></div>
      <div class="p2j-card p2j-public"><span class="p2j-step">C1</span><strong>Cancel before activation</strong>Keep the source route active and retain the ready private connection.</div>
      <div class="p2j-arrow" aria-hidden="true"></div>
      <div class="p2j-card p2j-danger"><span class="p2j-step">C2</span><strong>Rollback after activation</strong>Run a new controlled transition; do not rewrite private-origin history.</div>
      <div class="p2j-arrow" aria-hidden="true"></div>
      <div class="p2j-card p2j-warning"><span class="p2j-step">C3</span><strong>Reconcile unknown outcome</strong>Confirm provider state before retry; escalate when automatic evidence is unavailable.</div>
    </article>
  </section>

  <section class="p2j-continuity" aria-label="Transition continuity keeps current routing separate from historical invoice lifecycle">
    <div><strong>New invoice</strong>Resolve current effective route and persist the routing decision.</div>
    <span class="p2j-life-arrow" aria-hidden="true">≠</span>
    <div><strong>Existing invoice</strong>Continue status, correction, payment and retrieval using its original network context.</div>
  </section>

  <section class="p2j-discovery" aria-label="Additional Spain use cases requiring Phase 2 scope or dependency decisions">
    <h3>Spain use cases under consultation or adjacent scope</h3>
    <div class="p2j-chips">
      <span class="p2j-chip">Public issuer → Private receiver</span>
      <span class="p2j-chip">Multiple private platforms</span>
      <span class="p2j-chip">Per-invoice provider override</span>
      <span class="p2j-chip">Format transformation</span>
      <span class="p2j-chip">Polling and auto-acceptance exposure</span>
      <span class="p2j-chip">PDF + e-invoice dual delivery</span>
      <span class="p2j-chip">Corrections and credit notes</span>
      <span class="p2j-chip">Accountant delegated visibility</span>
    </div>
  </section>

  <div class="p2j-footer">The diagram shows the committed transition backbone. The additional Spain use cases must be traced into Phase 2 requirements, related PRDs, or explicit later-scope decisions before delivery approval.</div>
</div>
<!-- confluence-html-macro:end -->

### Phase 2 journey catalogue

| ID | Journey | Phase 2 treatment | Primary requirements | Open dependency |
|---|---|---|---|---|
| J1 | Prepare private connection without switching | Core | FR1, FR2, FR4, FR9 | Provider onboarding/registration evidence |
| J2 | Switch outbound Public → Private | Core | FR3–FR8, FR13–FR20 | Route authority and cutover sequence |
| J3 | Switch inbound Public → Private | Core intent; mechanics open | FR3–FR8, FR13–FR20 | Receiver reachability and retrieval ownership |
| J4 | Public inbound + Private outbound | Core confirmed scenario | FR1–FR7, FR21–FR25 | Direction-level route authority |
| J5 | Cancel scheduled transition | Core | FR15–FR18 | Irreversible-step definition by provider |
| J6 | Roll back after activation | Core | FR7–FR10, FR21–FR25 | Public readiness and provider rollback mechanics |
| J7 | Reconcile ambiguous activation | Core | FR8, FR15, FR17, FR28–FR30 | Provider authoritative reconciliation |
| J8 | Public issuer → Private receiver | Phase 2 discovery/dependency | FR3, FR6, FR21–FR25 | Who polls public platform and how destination is identified |
| J9 | Multiple private platforms/per-invoice target | Scope decision; currently excluded from initial delivery | Extension of FR1–FR3 | Priority rules, directory and per-invoice authority |
| J10 | Format transformation/trusted public copy | Provider/document dependency | FR7, FR12, FR21–FR24 | Canonical/original format and data preservation |
| J11 | Corrections, rejection and payment status after switch | Continuity dependency | FR7, FR21–FR25 | Historical lifecycle ownership |
| J12 | Accountant cross-product visibility | Identity/certificate dependency | FR26–FR30 | Delegation and credential ownership |

### J1 — Prepare private connection without switching

1. ERP creates a connection for the selected provider, legal entity, environment and intended directions.
2. Sage returns required configuration fields and provider capability information.
3. Customer or authorised accountant supplies credentials and registration data.
4. Sage validates configuration and requests or verifies external registration.
5. Sage records provider identifiers and observed registration/capability state.
6. Connection becomes `READY` for confirmed capabilities.
7. Public routes remain active because no route transition has been requested.

**Expected result:** public and private registrations coexist; private readiness does not alter routing.

### J2/J3 — Switch an inbound or outbound route Public → Private

1. ERP requests a transition for inbound, outbound or both using a ready private connection.
2. Sage validates route authority, direction capability, legal entity, environment, effective time and conflicts.
3. Sage presents the source route, target route, affected directions, timing and historical-continuity impact.
4. Authorised actor confirms.
5. Sage performs reversible preparation and any required external steps.
6. At the effective time, Sage activates the target route only for the confirmed scope.
7. Sage reconciles the provider/network state.
8. New invoices use the new route; unaffected directions remain unchanged.
9. Existing invoices retain their original context.

**Open:** inbound switching cannot be delivery-ready until receiver reachability and retrieval ownership are confirmed.

### J4 — Use Public inbound and Private outbound

1. Customer retains public inbound registration and route.
2. Customer activates private outbound only.
3. Route resolution selects a connection by direction.
4. Received public invoices retain public context.
5. Sent private invoices retain private-provider context.

**Expected result:** the customer is represented by scoped routes, not one global public/private state.

### J5 — Cancel before activation

1. Customer cancels a scheduled transition.
2. Sage verifies irreversible provider work has not begun.
3. Target connection remains configured and ready.
4. Source route remains effective.
5. Cancellation and actor are audited.

### J6 — Roll back after activation

1. Customer or operations requests rollback because the private route is unsuitable or degraded.
2. Sage validates that public is eligible and ready for the applicable direction.
3. Sage executes a new controlled transition back to public.
4. Private-origin invoices retain private context.
5. Private connection remains present unless separately disabled/deregistered.

### J7 — Activation returns an ambiguous timeout

1. Sage sends an activation or registration mutation.
2. Provider does not return a conclusive response.
3. Transition becomes `RECONCILING`; it is not marked failed.
4. Sage queries authoritative provider state or invokes the agreed reconciliation procedure.
5. Sage completes, safely retries or raises a controlled operational exception.
6. No conflicting route is exposed while the outcome remains unknown.

### Additional Spain use-case coverage

| PowerPoint use case | Relevance to Phase 2 | Required treatment outside the visual |
|---|---|---|
| Public → Public default flow | Phase 1/public lifecycle dependency | Validate polling, status/payment reporting and claimed acceptance timing |
| Public → Private | Direct Phase 2 dependency | Define destination identification and which private platform retrieves from public |
| Multiple platforms for one company | Direct domain-model implication | Support multiple connections; decide whether selection is default-, direction- or invoice-level |
| Format transformation | Provider and document-model dependency | Preserve original/transformed documents and define canonical data responsibility |
| Invoice retrieval | Resilience/public lifecycle dependency | Define batching, rate limits, alerts and missed-invoice reconciliation |
| PDF + e-invoice dual delivery | Adjacent transition requirement | Correlate channels and prevent duplicate business processing |
| Corrections/adjustments | Historical continuity dependency | Link rejection, credit note and corrective invoice to original network context |
| Accountant visibility | Identity/certificate dependency | Define delegated authority, certificate reuse/rotation and cross-product synchronisation |

The detailed evidence and unresolved claims are recorded in `research/PRD-SEI-201-spain-use-case-evidence.md`.

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

## Consultation and open decisions

| Question/decision | Why it matters | Owner | Blocks |
|---|---|---|---|
| What authoritative source determines an invoice route? | Defines route eligibility and reconciliation | Spain local team | Production routing |
| Can routing vary by direction, document type, counterparty or individual invoice? | Defines Phase 2 granularity and precedence | Product + local team | Route contract |
| Can one company actively use multiple private platforms? | Determines connection, default and override behaviour | Product + local team | Multi-platform scope |
| Who owns retrieval for Public → Private? | Prevents invoices remaining undetected on public | Local team + providers | Inbound private journey |
| Which platform owns status, correction, cancellation and payment events for older invoices? | Determines historical access and credential retention | Local team + providers | Production transitions |
| What are the authoritative cutover, rollback and deregistration sequences? | Determines safe orchestration | Local team + architecture | Production transitions |
| How long must a previous connection remain available? | Determines continuity, cost and credential lifecycle | Compliance + product | Disablement/offboarding |
| Which formats/original artefacts must Sage retain after provider transformation? | Prevents data loss and supports audit | Product + providers | Format capability |
| Are polling, no-push and four-day auto-acceptance claims confirmed? | Drives capacity, alerts and customer response | Local team/regulatory owner | Public lifecycle dependency |
| What dual PDF/e-invoice synchronisation is required? | Prevents duplicate customer processing | Product/local team | Adjacent transition scope |
| How is accountant authority/certificate reuse managed across products? | Determines access and credential security | Identity/security/product | Accountant journey |
| Which provider should be the reference integration? | Sequences foundation validation | Product + engineering | Rollout |
| Which ERP/customer cohort enters the first rollout? | Establishes measurable pilot | Product/ERP owners | Rollout |

## Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-27 | Public and private registrations may coexist | Confirmed |
| 2026-07-27 | Inbound and outbound may use different networks | Confirmed product scenario |
| 2026-07-27 | Shared and provider-specific requirements will be maintained as separate PRDs | Confirmed |
| 2026-07-27 | Phase 2 discovery baseline may be published to the configured Confluence pages | Confirmed and executed at `phase2-prds-v0.2` |
| 2026-07-29 | PowerPoint use cases are discovery evidence, not confirmed regulatory specification | Confirmed analysis treatment |
| 2026-07-29 | Per-invoice provider selection remains an explicit Phase 2 scope decision | Open |

## Revision history

| Date | Version/revision | Change | Pull request |
|---|---|---|---|
| 2026-07-27 | `phase2-prds-v0.1` | Initial discovery draft | |
| 2026-07-27 | `phase2-prds-v0.2` | Confluence publication baseline | |
| 2026-07-29 | Draft | Added Phase 2 HTML journey visual, PowerPoint evidence coverage, business rules and structured scope decisions | |
