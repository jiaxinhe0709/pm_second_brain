---
id: PRD-SEI-211
title: Public Platform — Invoice Consultation and Retrieval — Structured Review
type: prd
status: draft
version: 2
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-10-20
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-102
  - https://confluence.sage.com/spaces/DNBU/pages/837610648/Public+Platform+Onboard
  - https://confluence.sage.com/spaces/DNBU/pages/837610662/Public+Platform+Consult
  - https://confluence.sage.com/spaces/DNBU/pages/837610659/UBL+2.5+Invoice+Download
  - https://confluence.sage.com/spaces/DNBU/pages/837610722/SPFE+Invoice+Retrieval+Distribution
  - PRD-SEI-201
  - research/PRD-SEI-201-spain-use-case-evidence.md
  - PRD-SEI-223
  - PRD-SEI-226
  - PRD-SEI-236
  - SPEC-SEI-016
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: ""
  page_id: "837610662"
  title: Public Platform - Invoice Consultation and Retrieval
  layout: two_left_sidebar
  toc: true
---

# Public Platform — Invoice Consultation and Retrieval — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-102, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-211, adds Confluence layout/navigation metadata, and now consolidates consultation, retrieval, download artefacts and authorised product distribution. |
| Unchanged areas | Scheduling, checkpoint, idempotency, reconciliation, freshness, isolation and operational controls remain aligned with PRD-SEI-102. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-102; this successor introduces no new product decision. |

## Overview

This Phase 1 feature defines how Sage discovers, retrieves, validates and makes available invoices addressed to a customer through Spain's public e-invoicing solution.

The public solution is not expected to deliver invoices directly into each Sage ERP. Sage therefore needs a reliable consultation capability that:

- identifies legal entities eligible to receive through the public solution;
- checks for new or changed invoices without relying on a customer login;
- retrieves each invoice and its public-platform context;
- prevents duplicate business processing;
- records consultation freshness and failures;
- recovers invoices that may have been missed during outages, cursor errors or delayed availability; and
- exposes a stable result to Sage ERPs and operations.

The exact public API, notification support, query mechanism, rate limits and acceptable retrieval delay are still discovery inputs. This PRD defines the product behaviour that must hold regardless of whether the final integration uses polling alone or combines polling with a future notification mechanism.

### Retrieval, download and distribution boundary

| Term | Meaning in this PRD | Completion evidence |
|---|---|---|
| Consultation/discovery | Query or event processing that identifies candidate invoices/changes | Query scope, checkpoint/cursor and result identity |
| Retrieval | Fetch and durably retain the authoritative structured representation and public context | Exact original bytes/reference, hash, media type, format/profile/version and public reference |
| Validation/normalisation | Verify trust, syntax/profile, recipient and identity, then create canonical data where supported | Validation pack, trust evidence and mapping provenance |
| Download | Authorised delivery of a selected stored artefact to a person/product | Actor, purpose, artefact role, media type, hash and time |
| Product distribution | Exactly-once business publication of the accepted canonical/original relationship to the correct ERP/legal entity | Product acknowledgement and durable distribution identity |

The original structured representation, canonical representation and human-readable rendering are separate artefacts. A rendering or transition PDF must never be presented as the authoritative structured original. Format/profile rules remain in PRD-SEI-223 and PRD-SEI-236.

> **Consultation is complete only when Sage can prove both invoice delivery and retrieval freshness. An empty response is not, by itself, proof that nothing was missed.**

### Delivery context

| Phase | Capability | This PRD's responsibility |
|---|---|---|
| **Phase 1 — Public Platform Connection** | Public onboarding, outbound submission, inbound consultation and lifecycle | **Deliver reliable public invoice discovery and retrieval for eligible legal entities** |
| Phase 2 — Private Platform Connections | Public/private coexistence and route switching | Preserve explicit public route and invoice origin so consultation can be activated or ended safely by direction |
| Phase 3 — Platform Expansion | Private-first operation and provider switching | Reuse provider-neutral scheduling, idempotency and reconciliation patterns where appropriate |

## Product principles

1. **Scheduled retrieval is the baseline, not a user-session side effect.**
2. **Login or manual refresh may accelerate retrieval but must not be the only completeness mechanism.**
3. **Customer choice may tune an approved service policy; it must not disable mandatory retrieval or create an unsupported SLA.**
4. **Polling state and invoice lifecycle state are separate.**
5. **The scheduler must be fair across legal entities and observable at customer level.**
6. **Every retrieved invoice is idempotent by stable business and platform identity.**
7. **Reconciliation must be able to revisit a safe historical window without duplicating invoices.**

## Consultation and retrieval visual

<!-- confluence-html-macro:start -->
<div class="ppcr-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .ppcr-visual *{box-sizing:border-box}
    .ppcr-visual h2{margin:0;color:#172b4d;font-size:18px;font-weight:600}
    .ppcr-visual .ppcr-subtitle{margin:6px 0 18px;color:#6b778c;font-size:12px}
    .ppcr-visual svg{display:block;width:1080px;height:500px;background:#fafbfc;border:1px solid #ebecf0;border-radius:8px}
    .ppcr-visual .ppcr-node{fill:#fff;stroke:#36b37e;stroke-width:2}
    .ppcr-visual .ppcr-source{fill:#deebff;stroke:#0052cc;stroke-width:2}
    .ppcr-visual .ppcr-success{fill:#e3fcef;stroke:#36b37e;stroke-width:2}
    .ppcr-visual .ppcr-optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:2;stroke-dasharray:7 5}
    .ppcr-visual .ppcr-retry{fill:#fff7d6;stroke:#ff991f;stroke-width:2}
    .ppcr-visual .ppcr-alert{fill:#ffebe6;stroke:#de350b;stroke-width:2}
    .ppcr-visual .ppcr-title{fill:#172b4d;font-size:13px;font-weight:700;text-anchor:middle}
    .ppcr-visual .ppcr-copy{fill:#42526e;font-size:10px;text-anchor:middle}
    .ppcr-visual .ppcr-label{fill:#6b778c;font-size:10px;font-weight:600;text-anchor:middle}
    .ppcr-visual .ppcr-path{fill:none;stroke:#36b37e;stroke-width:2.5}
    .ppcr-visual .ppcr-path-optional{fill:none;stroke:#6b778c;stroke-width:2;stroke-dasharray:7 5}
    .ppcr-visual .ppcr-path-retry{fill:none;stroke:#ff991f;stroke-width:2.5;stroke-dasharray:7 5}
    .ppcr-visual .ppcr-path-alert{fill:none;stroke:#de350b;stroke-width:2.5;stroke-dasharray:6 5}
    .ppcr-visual .ppcr-notes{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;width:1080px;margin-top:12px}
    .ppcr-visual .ppcr-note{padding:10px 12px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;background:#fff;font-size:11px;line-height:1.4}
    .ppcr-visual .ppcr-note strong{display:block;margin-bottom:3px;color:#172b4d}
  </style>
  <h2>Public Invoice Consultation, Retrieval and Reconciliation</h2>
  <p class="ppcr-subtitle">A platform-owned schedule provides the completeness baseline; user-triggered refresh accelerates it, and reconciliation closes potential gaps.</p>
  <svg viewBox="0 0 1080 500" role="img" aria-label="Scheduled and optional user-triggered consultation of the public platform, followed by incremental query, idempotent ingestion, ERP availability, retry and reconciliation paths">
    <rect class="ppcr-node" x="30" y="178" width="170" height="88" rx="10"/>
    <text class="ppcr-title" x="115" y="210">Select due accounts</text>
    <text class="ppcr-copy" x="115" y="230">Eligible legal entities</text>
    <text class="ppcr-copy" x="115" y="245">fair scheduling + lease</text>

    <rect class="ppcr-source" x="248" y="178" width="170" height="88" rx="10"/>
    <text class="ppcr-title" x="333" y="210">Consult public solution</text>
    <text class="ppcr-copy" x="333" y="230">Incremental query</text>
    <text class="ppcr-copy" x="333" y="245">cursor + overlap window</text>

    <rect class="ppcr-node" x="466" y="178" width="170" height="88" rx="10"/>
    <text class="ppcr-title" x="551" y="210">Validate and deduplicate</text>
    <text class="ppcr-copy" x="551" y="230">Identity + content</text>
    <text class="ppcr-copy" x="551" y="245">original/copy distinction</text>

    <rect class="ppcr-node" x="684" y="178" width="170" height="88" rx="10"/>
    <text class="ppcr-title" x="769" y="210">Persist and acknowledge</text>
    <text class="ppcr-copy" x="769" y="230">Invoice + public context</text>
    <text class="ppcr-copy" x="769" y="245">advance cursor safely</text>

    <rect class="ppcr-success" x="902" y="178" width="148" height="88" rx="44"/>
    <text class="ppcr-title" x="976" y="210">Available to ERP</text>
    <text class="ppcr-copy" x="976" y="230">Invoice visible once</text>
    <text class="ppcr-copy" x="976" y="245">freshness recorded</text>

    <path class="ppcr-path" d="M200 222 L238 222"/>
    <polygon points="238,222 228,216 228,228" fill="#36b37e"/>
    <path class="ppcr-path" d="M418 222 L456 222"/>
    <polygon points="456,222 446,216 446,228" fill="#36b37e"/>
    <path class="ppcr-path" d="M636 222 L674 222"/>
    <polygon points="674,222 664,216 664,228" fill="#36b37e"/>
    <path class="ppcr-path" d="M854 222 L892 222"/>
    <polygon points="892,222 882,216 882,228" fill="#36b37e"/>

    <rect class="ppcr-optional" x="30" y="45" width="170" height="72" rx="10"/>
    <text class="ppcr-title" x="115" y="75">Refresh request</text>
    <text class="ppcr-copy" x="115" y="94">Login, user or operations</text>
    <path class="ppcr-path-optional" d="M115 117 L115 168"/>
    <polygon points="115,168 109,158 121,158" fill="#6b778c"/>
    <text class="ppcr-label" x="168" y="146">accelerates only</text>

    <polygon class="ppcr-retry" points="333,310 392,335 392,385 333,410 274,385 274,335"/>
    <text class="ppcr-title" x="333" y="354">Transient failure</text>
    <text class="ppcr-copy" x="333" y="373">retry + backoff</text>
    <path class="ppcr-path-retry" d="M333 266 L333 300"/>
    <polygon points="333,300 327,290 339,290" fill="#ff991f"/>
    <path class="ppcr-path-retry" d="M274 360 C210 360 210 285 248 244"/>
    <polygon points="248,244 237,247 246,254" fill="#ff991f"/>

    <polygon class="ppcr-alert" points="551,310 610,335 610,385 551,410 492,385 492,335"/>
    <text class="ppcr-title" x="551" y="349">Invalid or unsafe</text>
    <text class="ppcr-copy" x="551" y="368">quarantine + alert</text>
    <text class="ppcr-copy" x="551" y="383">do not advance cursor</text>
    <path class="ppcr-path-alert" d="M551 266 L551 300"/>
    <polygon points="551,300 545,290 557,290" fill="#de350b"/>

    <rect class="ppcr-optional" x="735" y="330" width="230" height="72" rx="10"/>
    <text class="ppcr-title" x="850" y="359">Reconciliation scan</text>
    <text class="ppcr-copy" x="850" y="378">Revisit safe historical window</text>
    <path class="ppcr-path-optional" d="M735 366 C675 366 665 290 684 245"/>
    <polygon points="684,245 675,252 687,257" fill="#6b778c"/>
    <path class="ppcr-path-optional" d="M965 330 C1015 310 1020 282 1000 266"/>
    <polygon points="1000,266 1011,269 1007,279" fill="#6b778c"/>
  </svg>
  <div class="ppcr-notes">
    <div class="ppcr-note"><strong>Baseline</strong>Scheduled consultation runs independently of customer activity. The final cadence is a service policy informed by volume, platform limits and required freshness.</div>
    <div class="ppcr-note"><strong>Safe progress</strong>The cursor advances only after every item in the committed page or batch is durably classified as ingested, duplicate or deliberately quarantined.</div>
    <div class="ppcr-note"><strong>Completeness</strong>Overlap windows and reconciliation scans detect late or previously missed invoices; idempotency prevents the recovery process creating duplicates.</div>
  </div>
</div>
<!-- confluence-html-macro:end -->

## Problem and business objective

The current consultation note states that receivers are not notified and that Sage will need to poll the public platform for new invoices. It offers several possible triggers: every hour, for every customer, when a customer logs in, or according to a customer-selected cadence.

Taken literally, these options leave critical product questions unanswered:

- Is the lack of notifications an approved public-platform contract or a working assumption?
- Does consultation return new invoices, changed invoices, both, or a current snapshot?
- Does reading or downloading an invoice have an external side effect?
- How is incremental progress represented across pagination and failures?
- What is the maximum acceptable time before an invoice is visible in the customer's ERP?
- How does an hourly per-customer design scale and remain fair?
- What happens to customers who rarely log in?
- Can a customer reduce polling below a compliant service level or disable it?
- How does Sage prove it recovered everything after an outage?
- How are originals distinguished from faithful copies held by the public repository?

Without a defined consultation product, Sage risks:

- invoices remaining undiscovered until a customer logs in;
- invoices being retrieved more than once and presented as duplicates;
- a failed page advancing the cursor and permanently skipping invoices;
- one high-volume customer starving other customers;
- polling every inactive or ineligible account and exhausting public-platform limits;
- customers seeing stale inboxes without an actionable freshness indicator;
- authentication or authorisation failures being retried indefinitely;
- support teams being unable to distinguish “no invoices” from “consultation has not succeeded”;
- inbound public invoices continuing after a future route change when they should not, or stopping too early while still required; and
- unverified timing assumptions becoming customer commitments.

The objective is to deliver an automated, incremental, idempotent and observable consultation capability that gives Sage reasonable evidence of inbound completeness and makes retrieved invoices available exactly once for business processing.

## Business value

| Stakeholder | Value |
|---|---|
| Customer or accountant | Receives public-platform invoices without needing to know when to refresh or sign in |
| Sage ERP | Consumes one stable inbound contract rather than implementing public polling and deduplication |
| Platform engineering | Operates a bounded scheduler with explicit progress, backoff and reconciliation |
| Operations and support | Can see last success, next due time, backlog, failure reason and affected legal entity |
| Product and compliance | Can change cadence and policy as the final specification evolves without redesigning invoice ingestion |

## Definitions and boundaries

| Term | Definition |
|---|---|
| Consultation | A read operation against the public solution to identify invoices or invoice changes available to an authorised legal entity |
| Retrieval | Obtaining the authoritative invoice payload and associated public-platform metadata required for Sage processing |
| Polling policy | The platform-owned rules that determine when a legal entity is due for consultation |
| Poll run | One traceable execution for a legal entity, query scope and environment |
| Cursor/watermark | Opaque or derived progress position used to request information after an earlier successful point |
| Overlap window | A deliberately repeated time/sequence range used to catch late or inconsistently ordered items |
| Reconciliation scan | A broader comparison or re-query used to detect gaps that routine incremental polling may miss |
| Freshness | Time since the most recent successful consultation covering the expected query scope |
| Business duplicate | The same invoice presented again under the same stable invoice identity |
| Technical duplicate | The same public result/page/event processed more than once |
| Quarantine | Durable isolation of an item that cannot safely enter the invoice lifecycle without correction or investigation |
| Eligible legal entity | A production/test legal entity whose public inbound connection, authorisation and route are ready for consultation |
| Original/copy classification | Public-platform evidence identifying whether a downloadable document is an original invoice or a faithful copy held in the universal repository |

### Consultation is not the invoice lifecycle

| Concern | Consultation responsibility | Adjacent responsibility |
|---|---|---|
| Discover an invoice | Find and retrieve it reliably | — |
| Validate technical payload | Classify safe/unsafe input | Invoice validation rules define detailed business acceptance |
| Make invoice available | Persist and publish once to the ERP-facing contract | ERP/customer workflow handles review and bookkeeping |
| Send acceptance/rejection/payment state | Preserve references and route context | Public invoice lifecycle/status feature |
| Select Public versus Private inbound | Respect the active/effective inbound route | PRD-SEI-201 and routing foundation |
| Customer public authorisation | Verify consultation eligibility and surface action required | Public Platform Onboarding |

## Scope

### In scope for Phase 1

- eligibility for public inbound consultation at legal-entity and environment level;
- a platform-owned scheduled consultation baseline;
- optional login, customer or operations-triggered refresh with controls;
- incremental query, pagination and safe progress handling;
- retrieval of invoice payload and relevant public-platform metadata;
- original/copy classification when exposed by the public solution;
- idempotent invoice ingestion and duplicate classification;
- retry, backoff, quarantine and dead-letter/exception handling;
- customer-level freshness, backlog and last-result visibility;
- operations search, retry and reconciliation;
- periodic overlap-window and broader reconciliation controls;
- audit and metrics for each poll run and retrieved item; and
- activation, pause and end behaviour linked to public inbound readiness and route.

### Shared dependencies

- public onboarding, representation and authorisation;
- legal-entity/NIF and environment identity;
- secure credential/certificate lifecycle;
- canonical invoice validation and persistence;
- ERP-facing inbound invoice contract;
- public invoice status and payment lifecycle;
- route and invoice-network context required for later Public ↔ Private transitions; and
- final AEAT service specification, sandbox and operational limits.

### Out of scope

- private-provider invoice retrieval;
- Public ↔ Private transition orchestration itself;
- customer bookkeeping or approval workflow;
- legal advice or interpretation of invoice acceptance;
- committing to an hourly cadence before volume, API limits and required freshness are agreed;
- allowing a customer to disable required public consultation;
- a claim that the public solution has no notification mechanism until confirmed;
- browser scraping or robotic use of a public web form;
- transformation into every ERP's proprietary accounting model; and
- detailed payment, rejection, correction or credit-note lifecycle requirements.

## Actors and business scenarios

| Scenario | Primary actor | Expected outcome | Exception/continuity |
|---|---|---|---|
| Activate public consultation | Sage platform after onboarding | Eligible legal entity is scheduled without waiting for login | Activation is blocked if authorisation/inbound readiness is incomplete |
| Scheduled check finds invoices | Scheduler | All new/changed invoices are retrieved and made available once | Partial page failure does not lose progress |
| Scheduled check finds nothing | Scheduler | Last-success/freshness updates; no invoice event is emitted | “No results” remains distinguishable from stale/failed consultation |
| Customer opens invoice inbox | ERP/customer | Current data is shown immediately; controlled refresh may be requested | Login does not create an unbounded synchronous wait |
| Duplicate invoice is returned | Ingestion service | Existing invoice is correlated; no duplicate business invoice is created | Conflicting content for the same identity is quarantined |
| Public platform times out | Integration service | Retry/backoff occurs and freshness degrades visibly | Other legal entities continue to receive fair service |
| Authorisation expires | Operations/customer | Consultation pauses as action-required and customer/operations are informed | No infinite retry using invalid credentials |
| Cursor becomes invalid | Operations/integration | Safe recovery or bounded re-scan restores progress | Cursor is not silently reset to “now” |
| Sage was unavailable | Reconciliation service | Historical overlap/reconciliation retrieves missed items | Idempotency absorbs repeated items |
| Public inbound route ends | Routing/operations | New public consultation follows the approved effective boundary | Historical public invoices and audit remain available |

## Evidence and research

### Evidence register

| Evidence | Confidence | What it confirms | Limitation/follow-up |
|---|---|---|---|
| [Public Platform Consult](https://confluence.sage.com/spaces/DNBU/pages/837610662/Public+Platform+Consult), revision 6 | Medium internal | Current hypothesis: receiver notifications are unavailable; regular polling is required; hourly/login/customer-selected options are under consideration | Not an API contract; each option requires local-team and engineering validation |
| Internal Spain use-case evidence, UC1 and UC5 | Medium internal | Public receiver retrieval and periodic/triggered/configurable consultation are important business scenarios | No-push, cadence and timing claims require official confirmation |
| [Real Decreto 238/2026, Article 11](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295) | High official | Public solution is an invoice repository and must provide agile manual and automatic download for issuers, recipients and authorised parties | Does not define API pagination, polling cadence, rate limits, callbacks or operational SLA |
| [Real Decreto 238/2026, Articles 5–6](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295) | High official | Public and private routes can be combined; public is the default receiving point when no private point is identified | Detailed routing/registration mechanics still depend on implementing specifications |
| [final Order HAC/1028/2026](https://www.boe.es/eli/es/o/2026/10/02/hac1028), Articles 9–11 | High official, published 5 October 2026 | Automated recovery, immediate customer availability for conservation, web-service/form consultation, and registered third-party authority | Exact discovery operations, batching, pagination, notification capability and limits still require AEAT technical documentation |

### Confirmed facts

1. Spain's public solution is intended to support both manual and automatic invoice download.
2. A recipient or its authorised intermediary can receive invoices through the public solution.
3. The public solution also acts as a universal repository and must distinguish invoices/copies in supported download behaviour.
4. Public and private mechanisms may be combined; consultation eligibility cannot be inferred from a permanent customer-wide “public” flag.
5. Final Order HAC/1028/2026 confirms automated customer-invoice recovery and immediate availability for conservation (Article 9), consultation/download channels (Article 10), and registered power of attorney for third-party recovery/consultation (Article 11). Exact API details and volumetry still depend on AEAT specifications.

### Retrieval, conservation and bulk boundary

**Confirmed:** Article 9 requires automated recovery in the applicable private-platform model and immediate availability of recovered invoices for customer conservation. This does not establish an hourly interval, absence of notifications, or a request spanning several customers. Third-party retrieval and consultation require registered power of attorney under Article 11; a valid certificate alone is insufficient.

**Proposed:** save the exact received source file and expose controlled conservation access after safe file capture, independently of completed mapping or ERP delivery. A quarantine prevents business processing and ordinary download of unsafe content; an authorised controlled export/recovery path must be agreed with Security and Compliance so conservation access is not silently lost. “Immediate” has no invented numeric target in this PRD.

**Open:** the AEAT discovery contract must establish how newly received invoices are identified, whether each call is scoped to one legal entity, and whether any multi-entity access is supported. Logical scheduling remains per authorised legal entity even if a future provider operation supports aggregation.

Automated collection of many invoices is part of required recovery. A user requesting a ZIP of several stored invoices is a separate product option, proposed outside initial scope until usage and cost evidence justify it. France's feature coverage and expected Spanish usage do not remove the automated-recovery requirement.

The proposed [combined receiving, retrieval and download specification](../specs/archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md) owns this journey, including source capture, covered progress, validation, duplicate handling, product distribution and authorised stored-file access. Its public intake path implements this PRD; private intake retains its separate scope and activation gates.

### Working hypotheses

| Hypothesis | Why it is reasonable | Validation required |
|---|---|---|
| Sage needs scheduled polling because no receiver push is available | Current Confluence and internal use-case notes | Confirm with final AEAT API/local team |
| A platform-owned default cadence is safer than customer-only triggers | Completeness cannot depend on login behaviour | Confirm freshness target and operating cost |
| Login/manual refresh should enqueue or coalesce work rather than call AEAT synchronously | Protects ERP latency and scheduler capacity | Architecture/API decision |
| Incremental polling needs an overlap window | Protects against late availability, ordering and boundary errors | Confirm query semantics and retention |
| A customer may select only from bounded cadence policies | Avoids disabling required retrieval or creating arbitrary SLAs | Product/compliance decision |

### Evidence gaps that block production design

- final automatic-download service operations and schemas;
- whether push, webhook or notification capability exists;
- accepted certificate and registered-authority verification mechanics, including legal-entity request scope and revocation;
- test/prod endpoints and sandbox data;
- query filters, ordering, pagination, cursor and retention semantics;
- whether download/consult has acknowledgement or “mark as read” effects;
- stable invoice/result identifiers and original/copy indicators;
- retry guidance, throttling, quotas and concurrency limits;
- maximum response/batch sizes and large-document handling;
- required retrieval freshness and any business/regulatory consequences of delay; and
- correction, cancellation and lifecycle-change discovery mechanism.

## Current-state and option analysis

### Option A — fixed hourly poll for every eligible customer

| Aspect | Assessment |
|---|---|
| Benefit | Simple customer expectation and initial scheduler model |
| Risk | Poll volume scales linearly even when there is no activity; hourly may be too slow or unnecessarily frequent |
| Dependency | AEAT rate limits, average response time, eligible-account count and target freshness |
| Decision | Candidate baseline, not yet a commitment |

### Option B — poll only when a customer logs in

| Aspect | Assessment |
|---|---|
| Benefit | Reduces calls for inactive customers and feels responsive during active use |
| Risk | Customers who do not log in have no reliable invoice delivery; login latency couples ERP availability to AEAT |
| Decision | Reject as the sole mechanism; retain only as an optional acceleration trigger |

### Option C — customer-selected polling interval

| Aspect | Assessment |
|---|---|
| Benefit | Gives customers control over freshness/cost preference |
| Risk | Creates inconsistent service, support expectations and potentially unsafe “off” or very slow configurations |
| Decision | Consider only as bounded service tiers/policies after compliance and capacity review |

### Option D — platform-owned adaptive scheduler

| Aspect | Assessment |
|---|---|
| Benefit | Central control, fairness, backoff, coalescing, priority and future event integration |
| Risk | More scheduling and observability complexity than a simple timer |
| Decision | Recommended product direction |

### Recommended direction

Use a platform-owned scheduler as the completeness baseline:

1. Maintain `nextPollAt` (or equivalent) per eligible legal entity and environment.
2. Lease due work so concurrent workers do not run the same scope unintentionally.
3. Apply a centrally configured default policy; exact interval remains open.
4. Allow safe acceleration from login, customer refresh or operations without generating duplicate concurrent work.
5. Apply provider-approved retry/backoff and global/per-tenant concurrency controls.
6. Query incrementally with an overlap window once supported by the API.
7. Persist each result idempotently before advancing durable progress.
8. Run periodic broader reconciliation independent of routine polling.
9. Degrade freshness and surface action-required states when consultation cannot succeed.
10. Add notifications later, if available, as an accelerator; keep scheduled reconciliation as the safety net.

## Conceptual product model

| Concept | Required attributes | Purpose |
|---|---|---|
| Consultation policy | policy ID/version, default cadence class, backoff class, reconciliation policy | Allows policy change without rewriting each customer |
| Consultation eligibility | legal entity, environment, public connection, inbound route/effective period, status, reason | Determines who may be scheduled |
| Consultation checkpoint | query scope, cursor/watermark, overlap boundary, last committed item/page, version | Provides safe incremental progress |
| Poll run | run ID, trigger, due/start/end time, query bounds, pages/items, result, error class, correlation ID | Makes each execution observable and auditable |
| External invoice observation | public identity, original/copy indicator, external timestamps, checksum/metadata, first/last seen | Correlates repeat observations |
| Ingestion outcome | invoice ID, observation ID, outcome, validation result, persisted/published time | Proves exactly-once business availability |
| Reconciliation run | scope/window, expected/observed totals where available, gaps, corrective actions | Detects missed work |

The exact storage technology and field names are solution-design decisions.

## Proposed state model

### Consultation eligibility

| State | Meaning | Scheduler behaviour |
|---|---|---|
| `NOT_READY` | Onboarding, authorisation or public inbound route is incomplete | Do not poll |
| `ACTIVE` | Eligible for baseline consultation | Schedule according to policy |
| `DEGRADED` | Recent failures; automatic recovery continues | Backoff while preserving freshness alert |
| `ACTION_REQUIRED` | Non-transient customer/configuration issue | Pause routine retries; notify owner |
| `PAUSED_OPERATIONAL` | Controlled operational pause | Preserve checkpoint and reason |
| `ENDED` | Public inbound consultation ended at approved boundary | Do not discover new work beyond boundary; retain audit/history |

### Poll run

| State | Meaning |
|---|---|
| `SCHEDULED` | Work is due or explicitly requested |
| `RUNNING` | Worker holds the lease |
| `SUCCEEDED` | Entire query scope committed, including a valid empty result |
| `PARTIAL` | Some work committed but remaining page/scope is incomplete |
| `RETRY_PENDING` | Transient failure will be retried |
| `FAILED_ACTION_REQUIRED` | Authentication, authorisation, contract or data issue needs intervention |
| `CANCELLED` | Work was safely stopped before completion |

### Retrieved item outcome

| State | Meaning |
|---|---|
| `DISCOVERED` | Result identity has been recorded |
| `RETRIEVED` | Required payload/metadata has been obtained |
| `INGESTED` | Durable invoice exists and is ready for downstream delivery |
| `DUPLICATE` | Existing invoice/observation safely correlated |
| `QUARANTINED` | Unsafe/conflicting item retained for investigation |

## Detailed journeys

### Journey 1 — activate consultation after public onboarding

1. Public onboarding confirms the legal entity, environment, authorisation and public inbound capability.
2. Routing confirms that public consultation is effective for inbound invoices in the intended scope.
3. Sage creates or activates consultation eligibility with the applicable policy version.
4. The first poll uses an approved initial-lookback rule rather than assuming “from now”.
5. Retrieved historical/current items follow the same idempotent ingestion path.
6. Sage records first-success time, checkpoint and next due time.
7. Customer/operations see `ACTIVE` only after consultation has demonstrated a successful query.

**Exception:** if initial consultation fails, the connection may remain configured but consultation is not represented as healthy.

### Journey 2 — scheduled consultation with new invoices

1. Scheduler selects a due legal entity using fair scheduling and obtains a lease.
2. Worker loads the last committed checkpoint and calculates the query/overlap bounds.
3. Public adapter authenticates for the legal entity/authorised representation.
4. Adapter retrieves a page or batch.
5. Sage records each external observation and validates identity, type, original/copy classification and payload.
6. Existing observations/invoices are correlated; new valid invoices are durably persisted.
7. Downstream availability is published idempotently.
8. Page/batch progress is committed only when every item has a durable outcome.
9. Pagination continues until the query scope is complete.
10. Poll run succeeds, freshness updates and the next due time is calculated.

### Journey 3 — scheduled consultation with no results

1. A valid query returns no invoices/changes for the requested scope.
2. Sage records query bounds, response evidence, completion time and correlation ID.
3. Checkpoint advances only according to confirmed API semantics.
4. Freshness becomes healthy and no invoice event is emitted.

The UI and operations view must distinguish this from “not yet polled”, “currently running” and “failed”.

### Journey 4 — login or manual refresh

1. ERP/customer requests a refresh or opens an experience configured to request one.
2. Sage returns current invoice data immediately.
3. If the legal entity is eligible and no sufficiently recent/run-in-progress condition applies, Sage coalesces or enqueues accelerated consultation.
4. API returns a stable refresh-operation reference and current freshness; it does not require AEAT to complete inside the user request.
5. On completion, new invoices become available through the normal ERP contract.

Rate limiting prevents repeated page refreshes from creating repeated public calls.

### Journey 5 — transient public-platform failure

1. Timeout, connection failure, throttling or approved transient response interrupts the poll.
2. Completed durable outcomes remain recorded.
3. Unsafe/uncommitted checkpoint progress is not advanced.
4. Sage classifies the failure and schedules bounded backoff using provider guidance.
5. Other legal entities continue to receive fair service.
6. Freshness and backlog indicators degrade as thresholds are crossed.
7. Recovery resumes from the last safe checkpoint/unfinished scope.

### Journey 6 — expired or invalid authorisation

1. Public solution rejects authentication/representation.
2. Sage does not retry indefinitely as a transient failure.
3. Consultation becomes `ACTION_REQUIRED` with a sanitised reason.
4. Customer/operations receive an actionable renewal/re-authorisation path.
5. Checkpoint and outstanding scope remain intact.
6. After correction, validation succeeds before scheduling resumes.

### Journey 7 — duplicate or conflicting identity

1. A repeated result matches an existing observation/invoice identity and compatible content.
2. Sage records a duplicate observation and does not create a second business invoice.
3. If the same stable identity contains materially conflicting content, Sage quarantines it.
4. Cursor/page progress follows the approved quarantine rule and cannot silently discard the conflict.
5. Operations can inspect identity, checksums and provider references without exposing unnecessary invoice content.

### Journey 8 — partial pagination failure

1. Earlier pages have been completely processed and committed.
2. A later page fails or contains an unsafe result.
3. Run becomes `PARTIAL` or `RETRY_PENDING`.
4. Recovery resumes using the last committed page/cursor or safely repeats the bounded scope.
5. Repeated earlier results are absorbed through idempotency.

### Journey 9 — reconciliation after outage or suspected gap

1. Reconciliation selects a legal entity and a safe historical window.
2. Sage re-queries invoices independent of the routine checkpoint, or compares an authoritative listing/count if the API supports it.
3. Known invoices correlate as duplicates.
4. Missing invoices are ingested through the normal path.
5. Conflicts/gaps produce traceable operational cases.
6. The routine checkpoint is changed only through an approved recovery rule.

### Journey 10 — public inbound route ends

1. A Public → Private or offboarding process establishes an effective boundary.
2. Scheduler stops creating new public consultation scope after the approved point.
3. Any poll covering the boundary completes or is safely cancelled according to the transition runbook.
4. Reconciliation confirms no required public invoice was missed before release.
5. Historical invoices, observations, checkpoints and audit remain available for continuity/retention.
6. Credentials/registration are changed only by their separate approved lifecycle.

The authoritative cutover, overlap and historical lifecycle rules remain owned by PRD-SEI-201 and local-team decisions.

## Business rules

| ID | Condition | Rule | Status |
|---|---|---|---|
| BR1 | Public inbound is not ready/effective | Consultation must not run | Proposed for approval |
| BR2 | Public inbound becomes ready | Consultation starts through platform scheduling, not customer login | Proposed for approval |
| BR3 | Customer does not log in | Scheduled consultation continues | Proposed for approval |
| BR4 | Customer requests refresh repeatedly | Requests are coalesced/rate-limited and cannot create concurrent duplicate work | Proposed for approval |
| BR5 | Poll returns no results successfully | Freshness updates; no invoice is emitted | Proposed for approval |
| BR6 | Same invoice is observed again | It must correlate without creating a duplicate business invoice | Proposed for approval |
| BR7 | Same stable identity has conflicting content | Item must be quarantined and investigated | Proposed for approval |
| BR8 | Page/run is partially processed | Progress advances only to a provably durable boundary | Proposed for approval |
| BR9 | Failure is transient | Retry/backoff applies without starving other tenants | Proposed for approval |
| BR10 | Failure requires customer/configuration action | Routine retry pauses and an actionable state is exposed | Proposed for approval |
| BR11 | Notification support becomes available | It may accelerate consultation but does not remove reconciliation without an explicit decision | Proposed for approval |
| BR12 | Customer cadence choice is offered | Choice is bounded by approved service policies and cannot disable required retrieval | Proposed for approval |
| BR13 | Public inbound route ends | Consultation follows the effective boundary without deleting historical context | Confirmed transition principle; sequence open |

## Functional requirements

### Eligibility and policy

| ID | Requirement |
|---|---|
| FR1 | Consultation must be scoped by legal entity, environment, public connection and inbound route/effective period. |
| FR2 | Only an authorised and inbound-ready legal entity may become `ACTIVE`. |
| FR3 | Activating public consultation must assign a versioned platform policy and schedule an initial query. |
| FR4 | Customer login must not be required for scheduled consultation. |
| FR5 | Ending or pausing consultation must preserve checkpoint, history and reason. |
| FR6 | Test and production credentials, checkpoints and retrieved invoices must remain isolated. |

### Scheduling and triggers

| ID | Requirement |
|---|---|
| FR7 | Sage must run a platform-owned scheduled consultation baseline for every active eligible legal entity. |
| FR8 | The scheduler must persist next-due time, trigger reason and lease/concurrency identity. |
| FR9 | Scheduling must be fair across tenants and prevent one tenant/backlog from monopolising capacity. |
| FR10 | Login, manual and operations refresh must enqueue/coalesce work through the same controlled scheduler. |
| FR11 | Duplicate or repeated refresh requests must return/reuse a stable operation where applicable. |
| FR12 | Policy changes must be centrally deployable without editing every legal entity. |
| FR13 | Global, provider and tenant-level concurrency/rate controls must be configurable. |

### Query, pagination and checkpoint

| ID | Requirement |
|---|---|
| FR14 | The public adapter must encapsulate the final automatic-download/consultation API and expose stable Sage query outcomes. |
| FR15 | Sage must record query scope, bounds, pagination and provider correlation for each poll run. |
| FR16 | Incremental progress must use confirmed API ordering/cursor semantics and must not assume timestamps are unique. |
| FR17 | The checkpoint must advance only after all items within the committed boundary have durable outcomes. |
| FR18 | Retrying or resuming a partial run must not skip or duplicate business invoices. |
| FR19 | Cursor invalidation/expiry must produce a safe recovery path; resetting directly to current time is prohibited. |
| FR20 | Query overlap/lookback must be configurable after retention and ordering behaviour are confirmed. |

### Retrieval, validation and idempotency

| ID | Requirement |
|---|---|
| FR21 | Sage must retain the stable public invoice/result identity and external references required for traceability. |
| FR22 | Retrieved documents must be classified as original or faithful copy when the public solution supplies this distinction. |
| FR23 | Each result must be durably classified as ingested, duplicate, deliberately ignored by an approved rule, or quarantined. |
| FR24 | Invoice business idempotency must use the legally/technically confirmed unique identity and must not depend only on transport event ID. |
| FR25 | Repeated compatible observations must not create duplicate invoices or duplicate downstream availability. |
| FR26 | Conflicting content under the same stable identity must be quarantined and auditable. |
| FR27 | Validation failure must retain sufficient sanitised evidence for correction without logging secret or excessive invoice data. |
| FR28 | Invoice and public-route context must be persisted before downstream ERP publication. |

### Availability and ERP/customer experience

| ID | Requirement |
|---|---|
| FR29 | Valid new invoices must be made available through the shared Sage inbound contract exactly once for business processing. |
| FR30 | Client APIs must expose current freshness, last successful consultation and action-required state without provider-specific error leakage. |
| FR31 | A refresh API must return current data and asynchronous operation/freshness context rather than block on the public platform. |
| FR32 | “No invoices found” must be distinguishable from no successful consultation, stale consultation and consultation failure. |
| FR33 | Customer-visible errors must be actionable and must not expose credentials, certificates or raw external responses. |

### Reliability, reconciliation and operations

| ID | Requirement |
|---|---|
| FR34 | Errors must be classified at least as transient, throttled, authentication/authorisation, contract/schema, invalid item and unknown. |
| FR35 | Retry/backoff must be configurable from confirmed provider guidance and must not create retry storms. |
| FR36 | A single invalid item must not permanently block unrelated legal entities; within-run continuation depends on safe API/checkpoint semantics. |
| FR37 | Sage must support a bounded historical re-scan/reconciliation independent of the routine checkpoint. |
| FR38 | Reconciliation must reuse normal validation and idempotency paths. |
| FR39 | Operations must be able to inspect active eligibility, last/next run, checkpoint freshness, run history, backlog, failure class and quarantined items. |
| FR40 | Authorised operations must be able to retry, revalidate or request reconciliation without directly editing a cursor. |
| FR41 | Every run and material state change must record actor/trigger, timestamp, scope, policy version, correlation ID and outcome. |
| FR42 | The system must alert on sustained freshness breach, growing backlog, repeated action-required failures and reconciliation gaps. |

### Artefacts, download and distribution

| ID | Requirement |
|---|---|
| FR43 | Retrieval must preserve the exact original structured representation or an approved immutable source reference before checkpoint advancement or product distribution. |
| FR44 | Every stored artefact must identify its role (`ORIGINAL`, `CANONICAL`, `PUBLIC_COPY`, `RENDERING`, `TRANSITION_COMPANION`), media type, format/profile/version, content hash, source and creation/retrieval time. |
| FR45 | Validation must resolve the activated PRD-SEI-236 UBL/public profile and retain syntax, business-rule, recipient, integrity and trust results independently. |
| FR46 | Canonical conversion and human-readable rendering must record generator/mapping versions and must not overwrite or relabel the original representation. |
| FR47 | Download must authorise the actor for the legal subject, invoice, artefact role and purpose and must record a redacted access audit. |
| FR48 | Where multiple artefacts are available, the client must be able to select or clearly distinguish original structured invoice, faithful copy, canonical data and rendering. |
| FR49 | Product distribution must occur only after durable original/context persistence and must carry a stable business distribution identity for exactly-once handling. |
| FR50 | A failed product acknowledgement must retry/reconcile distribution without re-retrieving or creating a second business invoice. |
| FR51 | Retention, access and deletion policy must be evaluated separately for original, canonical, rendering and operational evidence while preserving statutory/audit duties. |
| FR52 | Download/retrieval capability must remain independent from scheduled consultation so an authorised user can access already stored invoices even when a later poll is delayed, subject to suspension/security policy. |
| FR53 | In the applicable private-platform model, recover customer invoices automatically and make recovered source files available immediately for conservation; approve a measurable service target and controlled unsafe-file access policy before production. |
| FR54 | Third-party public recovery and consultation must check registered power of attorney for the represented subject and action separately from certificate validity; missing or revoked authority must block new public calls. |
| FR55 | Automated multi-invoice collection must not depend on a user-facing bulk export. Keep per-entity authority and progress independent of any future aggregate provider operation. |

## Proposed API and operational capabilities

| Capability | Product behaviour |
|---|---|
| Get consultation status | Returns eligibility, health, freshness, last/next consultation and sanitised action |
| Request refresh | Coalesces/enqueues accelerated work and returns a stable operation reference |
| Get refresh/run | Returns progress and summary without raw provider secrets |
| List inbound invoices | Returns invoices already accepted by the Sage ingestion boundary |
| Activate consultation | Internal/onboarding action after readiness and route checks |
| Pause/resume consultation | Controlled, authorised action with reason and audit |
| Request reconciliation | Operations action with bounded legal-entity/window scope |
| Inspect quarantine | Operations view of reason, identity and recovery action |

Endpoint paths, commands, payloads and synchronous/asynchronous response shapes require API and architecture design after the public specification is available.

## Polling policy and capacity model

The cadence decision must use evidence rather than choosing “hourly” in isolation.

### Required inputs

| Input | Owner/source |
|---|---|
| Number of eligible legal entities by launch wave | Product/commercial forecast |
| Average and peak invoices/results per legal entity | Data/market pilot |
| Required customer-visible freshness | Product/local team/compliance |
| AEAT request, concurrency and volumetry limits | Final public specification |
| Average/p95/p99 response time and pages per poll | Sandbox/load test |
| Authentication/signing cost | Engineering/security test |
| Outage duration and recovery rate | SRE capacity model |
| Reconciliation window/frequency | Architecture/risk decision |

### Sizing relationships

```text
baseline polls per day
  = eligible legal entities × (24 hours ÷ default interval)

steady-state request rate
  = polls per interval × average pages per poll ÷ interval seconds

recovery time
  = queued poll/page work after outage ÷ safe recovery throughput
```

The production design must model empty polls, high-volume legal entities, pagination, retry amplification and catch-up after the maximum supported outage. A cadence is not approved until normal and recovery demand remain within public-platform and Sage capacity.

### Policy decision table

| Policy element | Proposed default | Decision still required |
|---|---|---|
| Scheduled baseline | Enabled for all active eligible legal entities | Exact interval |
| Login-triggered refresh | Optional acceleration, coalesced | Freshness threshold and user feedback |
| Customer preference | Bounded policy only | Whether exposed in Phase 1 |
| Transient retry | Backoff with jitter/provider guidance | Attempts/time envelope |
| Reconciliation | Periodic and on-demand | Window and frequency |
| Outage recovery | Fair catch-up, not all tenants at once | Priority and capacity limits |

## Non-functional requirements

### Reliability

- Consultation, ingestion and downstream publication must be idempotent across retry, failover and replay.
- Checkpoint writes and item outcomes must be atomic or recoverably consistent.
- A worker crash must release/expire its lease safely.
- Scheduler queues and checkpoints must survive service restart.
- Reconciliation must not depend on mutable user-session state.

### Performance and scalability

- The scheduler must support forecast launch and recovery volume with measured headroom.
- High-volume customers must paginate without starving small customers.
- User refresh requests must have bounded queue and rate behaviour.
- ERP invoice reads must not wait synchronously for the public platform.
- Targets for retrieval freshness, run latency and catch-up time require baseline and approval.

### Security and privacy

- Authentication material, certificates, keys and tokens use approved secret storage and lifecycle.
- Authorisation and legal-entity isolation apply to scheduled, customer and operations triggers.
- Logs, traces and metrics minimise invoice content and personal data.
- Raw payload access is restricted and audited.
- Test data must not cross into production legal entities or ERP delivery.

### Audit and retention

- Each external observation must be traceable to poll run, public identity, query scope and ingestion outcome.
- Historical checkpoints, runs and audit must follow the approved retention policy.
- The ability to reprocess must not allow silent modification of the original invoice or audit history.

### Observability

Required dimensions include environment, policy, result class and sanitised provider error class. Legal-entity identifiers must be handled according to logging/privacy policy.

At minimum measure:

- active/due/running consultation counts;
- time since last successful consultation;
- poll success, empty, partial, retry and action-required rates;
- pages/items retrieved and duplicate/quarantine rates;
- scheduler delay and backlog age;
- public API latency and throttling;
- reconciliation gaps and recovered invoices; and
- downstream publication delay.

## Acceptance criteria

### Final-order acceptance additions

- Given a recovered invoice whose mapping or ERP delivery fails, its durably captured source remains available through the approved conservation-access policy without waiting for ERP success (FR43, FR53).
- Given a valid certificate without required registered authority, third-party retrieval and consultation are blocked and show an actionable authority issue (FR54).
- Given several authorised entities and no confirmed aggregate API, each retains its own scope, progress and outcome; collection works without a ZIP feature (FR55).


| ID | Given | When | Then |
|---|---|---|---|
| AC1 | Public inbound onboarding and route are ready | Consultation is activated | An initial scheduled query is created without requiring customer login |
| AC2 | An active legal entity has no new invoices | A valid scheduled query completes | Freshness updates and no invoice is emitted |
| AC3 | A new public invoice is available | Scheduled consultation runs | Invoice and public context are persisted and made available once |
| AC4 | The same invoice is returned again | A later/overlap/reconciliation query runs | Existing invoice is correlated with no duplicate business invoice |
| AC5 | Same stable invoice identity has conflicting content | Validation runs | Item is quarantined and an operational signal is created |
| AC6 | A multi-page query fails after committed pages | Retry occurs | Processing resumes/repeats safely without skipped or duplicate business invoices |
| AC7 | A worker fails before durable item outcome | Lease expires and work retries | Cursor has not advanced past the unsafe boundary |
| AC8 | Public platform times out | Poll runs | Classified retry/backoff occurs and freshness can degrade visibly |
| AC9 | Authorisation is invalid | Poll runs | Consultation becomes action-required rather than retrying indefinitely |
| AC10 | Customer repeatedly requests refresh | Requests arrive inside the coalescing window | At most the approved amount of public work is scheduled and callers receive stable status |
| AC11 | Customer never logs in | Scheduled cadence elapses | Consultation continues and invoices can still be retrieved |
| AC12 | Sage/public outage is recovered | Reconciliation scans the affected window | Missed invoices are recovered and repeats are absorbed |
| AC13 | High-volume customer has a large backlog | Other customers are due | Fair scheduling allows other customers to continue |
| AC14 | Public inbound route reaches its end boundary | Scheduler evaluates eligibility | New out-of-bound consultation stops while historical evidence remains |
| AC15 | Operations inspects a failed customer | Failure exists | Last success, next/retry state, checkpoint freshness and corrective action are visible without secrets |
| AC16 | A public UBL invoice is retrieved | Persistence completes | Exact original bytes/reference, hash, public reference, UBL/profile version and validation evidence are durable before checkpoint advancement |
| AC17 | A rendering is generated | User downloads both artefacts | Original structured UBL and rendering are distinctly labelled with separate hashes and provenance |
| AC18 | An unauthorised actor requests an invoice artefact | Download is attempted | Access is denied without disclosing invoice existence/content and the denied attempt is audited safely |
| AC19 | Product distribution succeeds but a later poll repeats the invoice | Deduplication runs | The same business invoice remains available once and all observations remain traceable |
| AC20 | Product acknowledgement fails after durable inbound persistence | Recovery runs | Distribution resumes/reconciles without re-fetching or duplicating the business invoice |
| AC21 | A transition PDF accompanies an invoice | Download is offered | It is labelled as `TRANSITION_COMPANION`, never as the authoritative structured invoice or public faithful copy |

## Metrics and success measures

| Metric | Target/direction | Status/owner |
|---|---|---|
| Eligible legal entities with consultation within approved freshness | Target required | Product + SRE |
| Retrieved invoices made available once | 100% | Proposed target |
| Avoidable invoice loss | 0 | Proposed target |
| Poll/item outcomes with traceable audit | 100% | Proposed target |
| Duplicate business invoices caused by replay/reconciliation | 0 | Proposed target |
| Action-required failure time to customer/operations visibility | Target required | Product + operations |
| Reconciliation gaps recovered | 100% of detectable gaps | Proposed direction; API capability dependent |
| Scheduler delay and outage catch-up time | Target required | SRE/engineering |
| Empty-poll ratio and calls per retrieved invoice | Baseline and optimise | Product/engineering |

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| No-push assumption is wrong | Unnecessary calls or missed opportunity for lower latency | Adapter supports event acceleration while scheduled reconciliation remains |
| Hourly cadence is selected without sizing | Poor freshness or rate/cost failure at scale | Evidence-based policy and load/recovery model |
| Login is the only trigger | Invoices remain undiscovered for inactive customers | Mandatory platform-owned baseline |
| Cursor advances before durable ingest | Permanent invoice loss | Commit checkpoint only after durable outcomes |
| Timestamp-only incremental query | Boundary gaps/duplicates | Confirm ordering, use stable identity and overlap |
| Download marks invoice as read/acknowledged | Retry may change external state | Confirm side effects; separate consult/retrieve/acknowledge if possible |
| Retry storm after outage | Further platform degradation | Backoff, jitter, fair catch-up and rate controls |
| Large customer starves scheduler | Other customers breach freshness | Tenant fairness, page/time slicing and prioritisation |
| Duplicate invoice identity is weak | Duplicate or overwritten invoice | Use confirmed unique code/public identity plus conflict quarantine |
| Original and faithful copy are confused | Incorrect business processing | Persist official classification and apply approved processing rule |
| Invalid authorisation retries indefinitely | Noise and stale inbox | Action-required classification and renewal flow |
| Route changes while poll is running | Wrong-boundary retrieval | Effective scope, lease/version checks and transition runbook |
| Final technical specification changes | Rework | Provider adapter and policy abstraction; explicit production gate |

## Dependencies and rollout

### Discovery and design

1. Obtain final/public AEAT automatic-download specification and change log.
2. Confirm notification support, query semantics, stable identifiers and download side effects.
3. Agree inbound freshness and customer experience with Spain local team and ERP product.
4. Produce forecast/capacity model for baseline, outage and reconciliation demand.
5. Approve consultation policy, state model, idempotency identity and checkpoint design.
6. Complete security, privacy and representation/authorisation review.

### Build and validate

1. Implement public adapter contract and sandbox authentication.
2. Implement eligibility, policy, scheduling and leasing.
3. Implement query/pagination/checkpoint and idempotent ingestion.
4. Implement customer freshness/refresh and operations controls.
5. Implement retry, quarantine, reconciliation, dashboards and alerts.
6. Test empty, high-volume, pagination, duplicate, conflict, throttling, expired authorisation and cursor-recovery cases.
7. Run outage/catch-up and tenant-fairness load tests.

### Rollout

1. Internal/sandbox legal entities.
2. Limited pilot with representative invoice volumes and accountant/multi-company cases.
3. Validate freshness, duplicate, failure and reconciliation metrics.
4. Expand cohorts behind configurable policy.
5. Retain rollback/pause capability without deleting checkpoint or invoice context.

### Production entry gates

- final automatic-download API and service terms obtained;
- public notification/no-notification behaviour confirmed;
- authentication, authorisation and legal-entity scope proven in sandbox;
- stable identity, original/copy and download side effects confirmed;
- freshness target and polling policy approved;
- rate/volumetry limits and capacity/recovery model approved;
- idempotency, partial pagination and cursor-recovery tests pass;
- reconciliation method and boundary approved;
- routing/transition interaction agreed;
- dashboards, alerts, runbook and operational ownership ready; and
- security, privacy and architecture reviews complete.

## Consultation and open decisions

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Does the public solution provide push/webhook/notification for recipients or authorised intermediaries? | Determines baseline/acceleration architecture | Spain local team + AEAT specification | Final adapter and policy | Scheduled automatic download is required; notification is unconfirmed |
| What is the authoritative automatic-download operation and response contract? | Determines implementation | AEAT specification + engineering | Build | Web-service contract will be published/confirmed separately |
| Does consult/download acknowledge or mark an invoice as read? | Determines replay safety | AEAT specification | Checkpoint/retry design | Read should be treated as potentially stateful until proven otherwise |
| Which invoices/changes can be queried: received, issued, originals, copies, statuses? | Determines scope and dedupe | Spain local team + AEAT specification | Detailed query contract | Phase 1 needs received originals; copy/status rules require confirmation |
| What identity uniquely and immutably identifies an invoice/result? | Determines business idempotency | AEAT specification + architecture | Ingestion design | Use official unique invoice code plus public reference where available |
| What ordering, pagination, cursor and retention guarantees exist? | Determines loss-free incrementality | AEAT specification | Checkpoint/reconciliation | Use overlap and stable identity; exact mechanism open |
| What retrieval freshness is required? | Determines polling policy and customer promise | Product + Spain local team/compliance | SLA/capacity | Platform-owned baseline; do not commit to hourly yet |
| Can customers choose cadence? | Determines UX and service consistency | Product + compliance + operations | Customer configuration | Bounded options only, possibly defer from Phase 1 |
| Should login always request refresh? | Determines cost and perceived freshness | ERP product + platform | Client behaviour | Only when stale and not already queued/running |
| How are customers prioritised during outage recovery? | Determines fairness and recovery SLA | SRE + product | Runbook/capacity | Oldest due with tenant fairness and controlled priority |
| What initial lookback is required on activation? | Prevents pre-activation invoice loss/duplication | Spain local team + product | Onboarding handoff | Configured boundary based on registration/effective route |
| When does public consultation end during Public → Private? | Prevents gaps/dual delivery | PRD-SEI-201 owner + Spain local team | Phase 2 cutover | Effective inbound boundary plus reconciliation |
| Who owns the customer-facing action for expired representation? | Determines recovery journey | Onboarding/product/operations | Operations readiness | Shared onboarding remediation |

## Decisions

| Date | Decision | Evidence/status |
|---|---|---|
| 2026-07-29 | Consultation/retrieval is a separate Phase 1 PRD from public onboarding | Scope decision |
| 2026-07-29 | Automatic public invoice download is a confirmed product requirement | Real Decreto 238/2026, Article 11 |
| 2026-07-29 | “No receiver notifications” remains unconfirmed rather than a committed fact | Internal note only; final AEAT contract required |
| 2026-07-29 | Platform-owned scheduling is the recommended completeness baseline | Proposed for product/architecture approval |
| 2026-07-29 | Login/manual refresh is an accelerator, not the sole mechanism | Proposed for approval |
| 2026-07-29 | Exact hourly cadence and customer-selectable interval remain open | Requires freshness, limit and capacity evidence |
| 2026-07-29 | Idempotency, safe checkpointing and reconciliation are required independent of cadence | Proposed product requirements |

## Source notes

- Official sources confirm policy and high-level capability but do not yet provide the complete production API contract.
- The [final Order HAC/1028/2026](https://www.boe.es/eli/es/o/2026/10/02/hac1028) replaces the April draft as the regulatory source. The [evidence note](../research/spain-public-platform-order-evidence.md) records the supplied XML and the remaining technical gates.
- Internal use-case evidence is summarised in `research/PRD-SEI-201-spain-use-case-evidence.md`; this PRD restates the relevant product conclusions so Confluence readers do not need repository access.
- This document is a research/proposal/solution PRD. It does not represent final legal, API or architecture approval.

## Revision history

| Date | Version/revision | Change | Pull request |
|---|---|---|---|
| 2026-07-29 | Version 1 (Draft) | Initial evidence-led Phase 1 PRD with consultation options, recommended solution, detailed journeys, requirements, visual, acceptance criteria and production gates | |
| 2026-09-21 | Version 2 (Draft) | Consolidated retrieval, download and product distribution; added representation roles, provenance, authorisation and exactly-once distribution controls | Internal Download and SPFE Retrieval/Distribution pages; PRD-SEI-223/226/236 |
