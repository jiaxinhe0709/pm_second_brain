---
id: PRD-SEI-222
title: Customer — Onboarding, Entry Point and Migration
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-210
  - FP-SEI-001
  - ADR-SEI-001
  - PRD-SEI-221
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-223
  - PRD-SEI-224
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: ""
  title: Customer — Onboarding, Entry Point and Migration
  layout: two_left_sidebar
  toc: true
---

# Customer — Onboarding, Entry Point and Migration

## Decision summary

Phase 3 should let an eligible Spanish business compare its available routes, configure the Sage private-platform proposition without changing live traffic, prove external entry-point readiness, and then activate or migrate an explicitly authorised direction and scope. Public and existing-provider routes remain valid choices.

The customer must never become unreachable because configuration, publication and activation were treated as one step. A route change affects new invoices within the authorised scope; it does not rewrite the network context or lifecycle ownership of older invoices.

> **Product principle:** Configure first, prove externally, activate deliberately, and release the previous route only when continuity is safe.

## Phase and customer outcome

| Customer starting point | Phase 3 outcome | Continuity principle |
|---|---|---|
| Uses the public solution | May adopt Sage private inbound, outbound or both if supported | Public history remains public-origin; unselected directions remain unchanged |
| Uses an external private provider | May keep it, add Sage for another scope, or migrate an authorised scope | Existing-provider history remains accessible through its original context |
| New to Spain e-Invoicing | Can compare public, existing-provider and Sage options before activation | No private route is silently selected |
| Multiple legal entities/products | Each authorised legal entity is assessed and activated independently | One entity's change must not affect another |

## Problem and objective

### Problem

Onboarding a private-platform customer is not only account creation. Sage must identify the correct legal entity, establish authority, explain route choice, configure the operator relationship, validate capabilities and credentials, publish or register the receipt entry point, observe that external state, and cut over traffic without losing invoices.

If those concerns are collapsed into a single “connected” flag:

- a customer may believe inbound is active when counterparties still see the public route;
- an outbound change may unintentionally change inbound;
- a failed publication may leave two systems claiming different active states;
- credentials or registrations may be removed while old invoices still need lifecycle access;
- a retry after timeout may create duplicate subscriptions or route mutations;
- Sage may be unable to explain who authorised a change and when it took effect.

### Objective

Provide an auditable onboarding and migration capability that separates commercial enrolment, connection configuration, external readiness and active routing; supports coexistence where the authoritative Spanish model permits it; and provides recoverable cutover, rollback and switch-out behaviour.

## Scope and non-goals

### In scope

- Eligibility, proposition comparison and explicit customer choice.
- Legal-entity identity, authority and operator subscription.
- Direction/scope-specific connection and route configuration.
- Entry-point publication/lookup and intended-versus-observed readiness.
- Public-to-Sage, external-provider-to-Sage and Sage-to-other-route transitions.
- Correction, retry, ambiguous outcome, cancellation, rollback and historical continuity.
- Product/API and operations visibility for onboarding cases.

### Non-goals

- Selecting the legal operator or delivery model.
- Finalising the authoritative route granularity before local confirmation.
- Defining detailed external endpoint contracts before official specifications.
- Automatically migrating all existing-provider customers.
- Transforming or reissuing historical invoices through the new route.
- Deleting retained invoice data during route deactivation.
- Commercial packaging beyond the subscription/entitlement information required for onboarding.

## Definitions and distinctions

| Concept | Meaning | Must not be confused with |
|---|---|---|
| Eligibility | Customer/entity meets product, legal and operator conditions | Readiness of a configured connection |
| Subscription | Commercial/contractual relationship for the Sage proposition | External entry-point registration |
| Connection | Technical and authority context for an operator/environment | Active route |
| Entry point | Published/discoverable destination used for receipt | Default outbound route |
| Configured | Required information has been captured | Externally reachable or active |
| Observed ready | Sage has confirmed the relevant external state | Customer authorisation to activate |
| Route activation | New eligible traffic begins using the selected route | Migration of historical invoices |
| Deactivation | Stops new traffic on a route | Deregistration, offboarding or deletion |
| Migration | Controlled change of active route/operator for a defined scope | A hard disconnect from the previous route |
| Rollback | Restore the last known safe route after a failed cutover | Blindly reversing external mutations |

## Onboarding and migration visual

<!-- confluence-html-macro:start -->
<div class="p3onb-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3onb-visual *{box-sizing:border-box}.p3onb-visual h2{margin:0;color:#172b4d;font-size:18px}.p3onb-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3onb-visual svg{display:block;width:1080px;height:470px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3onb-visual .node{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3onb-visual .gate{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3onb-visual .failure{fill:#ffebe6;stroke:#ff5630;stroke-width:1.5}.p3onb-visual .optional{fill:#fff;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3onb-visual .done{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3onb-visual .title{fill:#172b4d;font-size:11px;font-weight:700}.p3onb-visual .copy{fill:#42526e;font-size:9px}.p3onb-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3onb-visual .path{fill:none;stroke:#00875a;stroke-width:2}.p3onb-visual .retry{fill:none;stroke:#de350b;stroke-width:1.6;stroke-dasharray:6 4}.p3onb-visual .switch{fill:none;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3onb-visual .arrow{fill:#00875a}.p3onb-visual .arrow-red{fill:#de350b}.p3onb-visual .arrow-grey{fill:#7a869a}.p3onb-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3onb-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3onb-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Configure, prove, then activate the selected route</h2>
  <p class="sub">The previous safe route continues until both external readiness and customer activation succeed. Correction and rollback do not rewrite historical invoices.</p>
  <svg viewBox="0 0 1080 470" role="img" aria-label="A customer compares routes, establishes identity and authority, configures the Sage private platform, validates external entry-point readiness, explicitly activates a scoped route, and then uses Sage for new invoices. Validation failures loop back for correction and a failed cutover restores the previous safe route while historical invoices retain their original network context.">
    <text x="34" y="34" class="label">CHOOSE</text><text x="265" y="34" class="label">CONFIGURE WITHOUT TRAFFIC CHANGE</text><text x="650" y="34" class="label">PROVE AND ACTIVATE</text><text x="930" y="34" class="label">OPERATE</text>
    <rect x="34" y="76" width="180" height="82" rx="9" class="node"/><text x="52" y="103" class="title">Compare routes</text><text x="52" y="124" class="copy">Public • existing provider • Sage</text><text x="52" y="141" class="copy">direction and scope explained</text>
    <path d="M214 117 H254" class="path"/><polygon points="254,117 244,111 244,123" class="arrow"/>
    <rect x="256" y="76" width="190" height="82" rx="9" class="node"/><text x="274" y="103" class="title">Prove identity and authority</text><text x="274" y="124" class="copy">Legal entity • entitlement • consent</text><text x="274" y="141" class="copy">no route changes yet</text>
    <path d="M446 117 H486" class="path"/><polygon points="486,117 476,111 476,123" class="arrow"/>
    <rect x="488" y="76" width="170" height="82" rx="9" class="node"/><text x="506" y="103" class="title">Configure connection</text><text x="506" y="124" class="copy">Operator • credentials • capability</text><text x="506" y="141" class="copy">desired route recorded</text>
    <path d="M658 117 H698" class="path"/><polygon points="698,117 688,111 688,123" class="arrow"/>
    <rect x="700" y="66" width="188" height="102" rx="9" class="gate"/><text x="718" y="93" class="title">External readiness gate</text><text x="718" y="114" class="copy">Publish / register entry point</text><text x="718" y="132" class="copy">observe authoritative state</text><text x="718" y="150" class="copy">validate inbound and/or outbound</text>
    <path d="M888 117 H922" class="path"/><polygon points="922,117 912,111 912,123" class="arrow"/>
    <rect x="924" y="76" width="122" height="82" rx="9" class="done"/><text x="942" y="103" class="title">Activate scope</text><text x="942" y="124" class="copy">New invoices use</text><text x="942" y="141" class="copy">the chosen route</text>
    <rect x="650" y="245" width="238" height="82" rx="9" class="failure"/><text x="668" y="272" class="title">Validation or publication fails</text><text x="668" y="293" class="copy">Correct evidence/configuration and retry safely</text><text x="668" y="310" class="copy">previous active route is unchanged</text>
    <path d="M794 168 V237" class="retry"/><polygon points="794,237 788,227 800,227" class="arrow-red"/><path d="M650 286 H574 V166" class="retry"/><polygon points="574,166 568,176 580,176" class="arrow-red"/>
    <rect x="924" y="245" width="122" height="82" rx="9" class="optional"/><text x="942" y="272" class="title">Rollback / switch</text><text x="942" y="293" class="copy">Restore safe route</text><text x="942" y="310" class="copy">or controlled handover</text>
    <path d="M985 158 V237" class="switch"/><polygon points="985,237 979,227 991,227" class="arrow-grey"/>
    <rect x="256" y="380" width="790" height="54" rx="8" class="optional"/><text x="274" y="404" class="title">Continuity rail</text><text x="274" y="423" class="copy">Existing invoices retain original provider, identifiers, syntax, evidence and lifecycle route throughout configuration, cutover, rollback and switch-out.</text>
  </svg>
  <div class="notes"><div class="note"><strong>Independent dimensions</strong>Commercial subscription, connection, external readiness and route activation are separate.</div><div class="note"><strong>Scoped choice</strong>Inbound, outbound and future permitted granularity are changed only with explicit authority.</div><div class="note"><strong>Safe continuity</strong>The last known safe route remains until the new state is externally proven.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors and needs

| Actor | Need/responsibility |
|---|---|
| Business owner/authorised administrator | Understand options, authorise the legal entity and select the intended route |
| Accountant/finance user | Know when inbound/outbound is active and how existing invoices continue |
| Sage ERP/API consumer | Configure and track onboarding through stable product-neutral operations |
| Sage proposition owner | Apply eligibility, pricing/entitlement and customer-choice rules |
| Legal operator | Provision the platform relationship and prove external readiness |
| Existing/public platform | Preserve or release route state according to the approved transition sequence |
| Sage operations/support | Reconcile intended/observed state, recover cases and explain customer impact |
| Legal/security/compliance | Approve authority, terms, credentials, data roles and activation controls |

## Business scenarios

| ID | Trigger | Expected outcome | Continuity/exception |
|---|---|---|---|
| S1 | New customer compares routes | Plain-language comparison of public, external-provider and Sage choices | No private subscription or route is preselected |
| S2 | Public customer configures Sage private outbound | Configuration and validation occur without changing public inbound | Public inbound and all history remain unchanged |
| S3 | Public customer migrates both directions | New private routes activate only after observed readiness and authority | Previous route retained until safe release |
| S4 | Existing-provider customer adopts Sage inbound only | Sage becomes inbound route for approved scope; outbound remains with provider | Provider-origin invoices continue through provider context |
| S5 | Entry-point publication fails | Customer receives actionable pending/failure state | Existing route continues; correction is safe to retry |
| S6 | Activation times out after external mutation | Sage records outcome unknown and reconciles authoritative state | No blind second activation |
| S7 | Customer cancels before activation | Draft/configured resources are removed or retained by policy | Live routes remain unchanged |
| S8 | Cutover produces unacceptable failures | Controlled rollback restores last known safe route where permitted | New-route invoices retain their actual origin; no history rewrite |
| S9 | Customer switches out of Sage | New traffic moves after destination readiness; historical access and evidence continue | Credentials/registration removed only when no longer required |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Customer chooses Sage private platform | Capture explicit authority for legal entity, direction, scope and effective action | Proposed control |
| BR2 | Private route is being configured | Do not change live routing until readiness and activation gates pass | Confirmed product principle |
| BR3 | Public/private routes coexist | Model direction and scope independently to the maximum supported granularity; final authoritative granularity requires local confirmation | User decision plus open local question |
| BR4 | No private receipt entry point is published | Public solution remains the default receipt point | RD 238/2026 Articles 5–6 |
| BR5 | External observed state differs from Sage intent | Treat onboarding/transition as incomplete and reconcile; do not claim active | Proposed safety rule |
| BR6 | Current route changes | Only new eligible invoices after the effective cutover use the new route | Confirmed continuity principle |
| BR7 | Historical invoice exists | Preserve original route/operator and required lifecycle access | Confirmed continuity principle |
| BR8 | Activation outcome is ambiguous | Reconcile before retry or rollback | Phase 2 resilience principle |
| BR9 | Customer cancels before activation | Live route remains unchanged; configured resources follow retention/security policy | Proposed rule |
| BR10 | Previous registration/credential may be released | Release only after approved safety checks and continuity ownership are satisfied | Open sequence; conservative hypothesis |

## Evidence and open research

| Source | What it supports | Confidence/limitation | Impact |
|---|---|---|---|
| PRD-SEI-201/202 | Route independence, transition continuity, invoice-origin context and recoverable switching | Product requirements; local route authority remains open | BR3, BR6–BR10 and migration journeys |
| PRD-SEI-221 | Readiness states, entry-point validation and operator gates | Discovery proposal | Activation and pilot gating |
| RD 238/2026 Articles 5–6 | Public/private combination, private entry-point publication, open lookup and public default | Primary regulation; detailed technical mechanism requires confirmation | Entry-point/route requirements |
| RD 238/2026 Articles 8–9 | Interconnection and public bridging during setup | Primary regulation; implementation specification open | Migration continuity and external readiness |
| ADR-SEI-001 | Legal operator and delivery-model decision | Proposed, not selected | Subscription, authority and support ownership |

## Proposed conceptual model

**Architecture decision required:** record boundaries and APIs remain to be approved. The behavioural distinctions below are required.

| Record | Required information |
|---|---|
| Legal entity | NIF/tax identity, Sage tenant/product context, jurisdiction and verification evidence |
| Customer authority | Authoriser, role, legal entity, allowed direction/scope, action, timestamp and evidence |
| Platform subscription | Proposition, operator, contract/entitlement, start/end and commercial state |
| Connection | Operator/environment, credentials/certificates, capability, configured state and health |
| Entry-point registration | Direction/scope, intended value, observed value, source, external reference and timestamps |
| Route policy | Direction/scope, selected route, priority, effective interval, authoriser and decision reason |
| Transition | From/to route, requested/validated/activated times, state, checkpoints, rollback and case |
| Invoice network context | Original route/operator, identifiers, syntax, evidence and lifecycle history |

### Independent state dimensions

| Dimension | Proposed states |
|---|---|
| Subscription | `NOT_STARTED`, `PENDING_TERMS`, `ACTIVE`, `SUSPENDED`, `ENDED` |
| Connection | `DRAFT`, `VALIDATING`, `READY`, `DEGRADED`, `REVOKED` |
| External registration | `NOT_REQUESTED`, `PENDING`, `OBSERVED_READY`, `FAILED`, `REMOVAL_PENDING`, `REMOVED`, `OUTCOME_UNKNOWN` |
| Route | `UNCHANGED`, `ACTIVATION_PENDING`, `ACTIVE`, `ROLLBACK_PENDING`, `INACTIVE` |
| Transition case | `REQUESTED`, `VALIDATING`, `CUTOVER_PENDING`, `COMPLETED`, `FAILED_RECOVERABLE`, `OUTCOME_UNKNOWN`, `ROLLED_BACK`, `CANCELLED` |

No single `ONBOARDED` flag should replace these dimensions.

## Detailed journeys

### J1 — Compare and configure without activation

1. Sage identifies the legal entity and eligible product/cohort.
2. The customer sees public, current-provider and Sage options, costs and responsibility boundaries.
3. An authorised administrator selects direction/scope and accepts applicable terms.
4. Sage creates subscription and connection records in non-active states.
5. Configuration validation returns actionable missing/invalid fields.

**Result:** the customer can prepare the Sage route without changing live invoice traffic.

### J2 — Publish, observe and activate

1. Sage validates internal operator, credential and capability readiness.
2. The operator publishes/registers the private entry point through the approved mechanism.
3. Sage independently observes the authoritative external state.
4. Customer confirmation or approved effective-time rule authorises activation.
5. Sage atomically makes the new route effective for new eligible invoices and records the cutover evidence.

**Result:** active state is supported by matching intended, observed and authorised state.

### J3 — Correct a validation/publication failure

1. A validation or external publication fails with a stable category and safe customer message.
2. Sage preserves valid configuration and identifies the corrective action and owner.
3. The customer or operations corrects only the affected information.
4. The same logical request resumes idempotently.
5. The prior active route remains unchanged until success.

### J4 — Resolve an ambiguous activation

1. External mutation times out after transmission.
2. Transition enters `OUTCOME_UNKNOWN` and prevents concurrent route changes.
3. Sage queries/reconciles the external state using correlation and idempotency identifiers.
4. If the new state exists, validation continues; if absent and safe, the operation resumes.
5. If unresolved, operations handles a controlled case; Sage does not claim active.

### J5 — Migrate from an existing private provider

1. Sage captures the exact direction/scope and inventories in-flight/historical dependencies.
2. The Sage connection and entry point become observed-ready while Provider A remains active.
3. Cutover selects Sage for new eligible invoices.
4. Provider A access/credentials remain for required historical lifecycle and reconciliation.
5. Provider A registration is released only after the approved responsibility and safety conditions pass.

### J6 — Roll back after cutover

1. A defined kill condition identifies material failure after activation.
2. Sage determines invoices already created/received on each route and freezes unsafe new changes.
3. Where authoritative external rules permit, the last safe route is restored and observed.
4. Invoices already processed on Sage retain Sage origin; previous invoices retain prior origin.
5. The incident, customer communication and corrective plan are audited.

### J7 — Switch out/offboard

1. Customer selects a supported destination or terminates the service with explicit authority.
2. Destination readiness and effective handover are confirmed before stopping new Sage traffic.
3. New activity stops according to the approved sequence.
4. Historical read/status/export access continues for the approved period.
5. Entry point, credentials and subscription are removed/revoked only at their separate safe gates.

## Functional requirements

### Identity, choice and authority

| ID | Requirement |
|---|---|
| FR1 | Resolve and verify the legal entity independently of the Sage user or product tenant. |
| FR2 | Present public, current-provider and Sage route choices with price, scope, operator and support responsibility before consent. |
| FR3 | Record explicit authority by legal entity, direction, scope and requested action. |
| FR4 | Prevent unauthorised users from creating, activating, rolling back or removing a route. |
| FR5 | Support multiple legal entities without sharing credentials, authority or route state across tenants. |

### Configuration and readiness

| ID | Requirement |
|---|---|
| FR6 | Allow subscription and connection configuration without changing an active route. |
| FR7 | Validate commercial, legal, credential, capability, security and operator prerequisites separately. |
| FR8 | Maintain intended and observed external entry-point/registration state with source and timestamps. |
| FR9 | Expose actionable, non-sensitive validation failures and their responsible actor. |
| FR10 | Classify mutating external operations by idempotency/reconciliation safety. |

### Activation, migration and continuity

| ID | Requirement |
|---|---|
| FR11 | Activate only the explicitly authorised direction/scope after required readiness gates pass. |
| FR12 | Ensure concurrent activation requests for overlapping scope cannot create conflicting active routes. |
| FR13 | Record an effective cutover point sufficient to determine the route for every new invoice. |
| FR14 | Preserve previous live routing when validation, publication or pre-cutover steps fail. |
| FR15 | Preserve immutable invoice-origin context and historical lifecycle through every route change. |
| FR16 | Keep previous credentials/access only for the approved continuity need and revoke them when no longer required. |
| FR17 | Support controlled rollback with actual-route attribution for invoices processed during the cutover window. |
| FR18 | Separate route deactivation, entry-point removal, credential revocation, subscription termination and data retention/deletion. |
| FR19 | Reconcile `OUTCOME_UNKNOWN` external mutations before retrying or presenting active state. |
| FR20 | Produce a complete audit of who requested, approved, executed, observed and recovered each transition. |

### Product and operations

| ID | Requirement |
|---|---|
| FR21 | Provide product/API operations to create configuration, validate, view readiness, request activation/cancellation/rollback and view transition history subject to permissions. |
| FR22 | Give operations intended/observed state, correlation, fault domain, safe next action and redacted evidence. |
| FR23 | Provide customer messages that identify affected direction/scope and whether existing invoices continue. |
| FR24 | Prevent manual actions that bypass mandatory readiness, authority or audit controls. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Protect credentials, authority evidence and personal data through encryption, least privilege and environment/tenant isolation. |
| NFR2 | Make all logical onboarding and transition requests idempotent and correlation-addressable. |
| NFR3 | Define capacity and propagation targets from approved customer/entity volumes and authoritative external behaviour. |
| NFR4 | Monitor pending, failed, outcome-unknown and intent/observed discrepancies with age and owner. |
| NFR5 | Keep customer-facing status accessible, plain-language and consistent across Sage products. |
| NFR6 | Retain transition and authority evidence for the approved legal/audit period without storing secrets in logs. |
| NFR7 | Version route rules and external contracts so historical decisions remain explainable. |
| NFR8 | Support controlled feature/route disablement by operator, product, cohort, direction and scope. |

## Failure and recovery matrix

| Failure | Behaviour | Customer/operations outcome |
|---|---|---|
| Identity/NIF mismatch | Stop before external mutation | Correct legal-entity evidence |
| Authority revoked | Prevent new privileged actions; assess pending transition | Current safe route remains unless separately suspended |
| Credentials invalid | Connection not ready | Actionable credential owner shown |
| Entry-point publication rejected | Preserve prior route | Correct and resume same logical request |
| Timeout after publication | `OUTCOME_UNKNOWN`; query external state | No blind duplicate mutation |
| Observed state differs | Block activation and reconcile | Do not show active |
| Concurrent overlapping transition | Serialise/reject conflict | One authoritative transition proceeds |
| Internal failure after external success | Persist/recover from correlation and observed state | Reconcile before activation/rollback |
| Cutover quality failure | Trigger approved rollback/kill process | Preserve actual origin of affected invoices |
| Previous provider removal fails | Keep removal pending; do not corrupt new route | Operations case and continued audit |

## Acceptance criteria

- Given a public inbound route and a requested Sage outbound route, when the customer configures Sage outbound, then public inbound and all active routing remain unchanged until explicit outbound activation.
- Given a private entry point that Sage has requested but cannot observe externally, when activation is attempted, then activation is blocked and the prior route remains active.
- Given two authorised requests for overlapping route scope, when they execute concurrently, then only one may establish the effective route and the other receives a conflict outcome.
- Given an activation timeout after external transmission, when recovery runs, then Sage reconciles external state before retry or customer success is reported.
- Given migration from Provider A to Sage, when cutover completes, then new eligible invoices use Sage while Provider A invoices retain Provider A identifiers and lifecycle context.
- Given rollback after some Sage invoices were exchanged, when the prior route is restored, then Sage-origin invoices remain Sage-origin and their lifecycle remains accessible.
- Given switch-out, when new-route readiness is not proven, then Sage does not remove the current entry point or stop the safe route.

## Measures

| Measure | Purpose | Target owner |
|---|---|---|
| Eligible-to-configured and configured-to-active conversion | Identifies proposition and onboarding friction | Product |
| Time in each onboarding/transition state | Identifies process and external bottlenecks | Product/operations |
| Intent/observed discrepancies | Measures entry-point control | Platform operations |
| Activation failures and outcome-unknown age | Measures mutation safety | Engineering/operations |
| Rollbacks and invoices affected | Measures cutover quality | Product/operations |
| Historical-context completeness | Protects audit and continuity | Data/QA |
| Support contacts by onboarding step | Identifies unclear customer experience | Support/product |

## Rollout gates

| Gate | Requirement |
|---|---|
| Discovery | Authoritative route granularity, entry-point mechanism, authority model and ownership questions assigned |
| Design | Independent state/data model, API contract, security, failure and transition sequence approved |
| Sandbox | Configuration, validation, idempotency, discrepancy and rollback cases pass without live traffic |
| External validation | Entry-point publication/lookup and public/counterparty behaviour proven |
| Pilot | Named cohort, support, previous-route continuity and kill criteria approved under PRD-SEI-221 |
| Production | Capacity, monitoring, retention, switch-out and operational/model exit tests pass |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| “Connected” is mistaken for active | Separate and expose subscription, connection, observed registration and route state |
| Customer loses inbound reachability | Validate externally before cutover; keep previous safe route until approved release |
| Direction/scope granularity is assumed incorrectly | Model independently and gate final behaviour on local decision |
| Duplicate external registrations | Idempotent logical requests and reconciliation-first timeout handling |
| Old credentials retained indefinitely | Connection-aware continuity purpose, expiry and revocation control |
| Rollback rewrites history | Immutable invoice network context and actual effective intervals |
| Partner model obscures responsibility | ADR accountability and PRD-SEI-221 evidence gates |

## Open questions and decision owners

| Question | Why it matters | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| What precisely determines an invoice's route? | Defines authoritative selection and reconciliation | Local technical/regulatory team | Design/pilot | Explicit route policy plus external entry-point observation |
| What route granularity is legally and technically supported? | Determines independent inbound/outbound/entity/supplier behaviour | Local team | Design | Model extensibly; activate only confirmed scopes |
| Can public and private registrations coexist, and how are multiple private entry points represented? | Controls migration safety | Local team/operator | External validation | Coexistence is supported conceptually; exact mechanics open |
| Who owns older invoice lifecycle after switching? | Determines credential/evidence continuity | Local/legal/operator | Pilot/production | Original-network context remains; responsibility requires approval |
| What is the authoritative cutover, rollback and deregistration sequence? | Prevents reachability and duplicate risk | Local team/architecture/operator | Pilot | Prove new state before release where permitted |
| Is activation immediate, scheduled or externally effective after propagation? | Determines customer promise and route timestamp | Local team/product | Design | Separate requested and observed effective time |
| Which roles can bind each legal entity? | Prevents unauthorised registration | Legal/product | Pilot | Approved business administrator with audit evidence |
| How long must historical access and credentials remain? | Drives retention/security | Legal/privacy/operator | Production | Configurable until approved |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 customer onboarding, entry-point and migration PRD | PRD-SEI-210, Phase 2 transition foundations and RD 238/2026 |
