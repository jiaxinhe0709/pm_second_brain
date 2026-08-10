---
id: PRD-SEI-210
title: Phase 3 — Sage as a Private Platform (Spain)
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-209
  - ADR-SEI-001
  - FP-SEI-001
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-102
  - PRD-SEI-103
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-204
  - PRD-SEI-205
  - PRD-SEI-206
  - PRD-SEI-207
  - PRD-SEI-208
  - NAV-SEI-001
  - NAV-SEI-002
  - NAV-SEI-003
  - NAV-SEI-004
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: ""
  page_id: "837588803"
  title: Phase 3 - Sage as a Private Platform (Spain)
  layout: two_left_sidebar
  toc: true
---

# Phase 3 — Sage as a Private Platform (Spain)

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-209, which remains the unchanged predecessor document. |
| Reason for this successor | Preserve the original Phase 3 draft while evaluating Phase 1 and Phase 2 component reuse as a formal Phase 3 design constraint, then consolidate the legacy *Sage as a Private Platform (Spain)* and *Private platform building blocks* Confluence pages into one authoritative Phase 3 product story. |
| Material changes | Adds the shared-platform/operator-edge architecture, the reuse/extend/new capability classification, an evidence-gated reuse decision flow, a labelled strategic-hypothesis register, the four-category Confluence structure, and explicit links to the Phase 1 submission and consultation PRDs. |
| Unchanged areas | Retains the strategic rationale, customer proposition, operating-model options, regulatory analysis, scenarios, requirements, risks, dependencies, and open questions from PRD-SEI-209. |
| Decisions still open | Actual component maturity; service ownership; reuse fitness; operator accountability; build/partner route; customer and commercial evidence; and the Phase 3 delivery investment decision. |

## Decision summary

This PRD defines the discovery and decision boundary for Sage to offer a Sage-branded private e-invoicing platform in Spain. The intended outcome is that eligible customers can choose Sage as their private-platform entry point, exchange compliant B2B invoices with public and private routes, see invoice and payment status inside their Sage workflow, and retain customer choice without being forced away from an existing provider.

The strategic direction is **proposed, not approved**. This document does not select build, white-label, alliance, or acquisition. It defines the minimum product and regulated operator outcomes that any route must satisfy and the evidence gates required before Sage accepts operator accountability.

> **Product principle:** A Sage-branded experience must have explicit operational and regulatory accountability. Branding a partner service as Sage must not hide who operates the platform, controls data, resolves failures, maintains interconnections, or remains responsible when the partnership changes.

## Phase 3 document map

This umbrella PRD explains the complete proposition. Four category pages organise the child documents so each decision, foundation and delivery surface can be reviewed by the appropriate business, legal, engineering, security and operational owners. A detailed document can support more than one category, but it has one authoritative Confluence location and is cross-linked elsewhere rather than duplicated.

| Category | Authoritative detailed documents | Capability boundary |
|---|---|---|
| [Routing and Transmission](https://confluence.sage.com/pages/viewpage.action?pageId=876576916) | PRD-SEI-223 Exchange; PRD-SEI-224 Lifecycle | Public/private exchange, routing, transformation, faithful copy, status, rejection and payment reporting |
| [Compliance and Operator Readiness](https://confluence.sage.com/pages/viewpage.action?pageId=876576917) | ADR-SEI-001 Delivery Model; FP-SEI-001 Reuse Assessment; PRD-SEI-221 Operator Readiness | Accountable operator, reuse evidence, regulatory governance, external validation and production gates |
| [Security and Operations](https://confluence.sage.com/pages/viewpage.action?pageId=876576918) | PRD-SEI-225 Operations; PRD-SEI-226 Security | Trust, identity, certificates, data, audit, resilience, support and reconciliation |
| [Interconnection and Interoperability](https://confluence.sage.com/pages/viewpage.action?pageId=876576919) | PRD-SEI-222 Customer; cross-links to PRD-SEI-223 and PRD-SEI-225 | Entry-point onboarding, migration, public/private connectivity, platform interconnection and ecosystem recovery |
| Commercial and roadmap discovery | Planned proposals | Customer value, packaging, economics, optional services and international expansion |

The detailed decision, foundation and delivery documents form the recommended technical, regulatory and operational consultation package. Commercial and roadmap discovery can progress without delaying review of the operator foundation.

## Why Phase 3 exists

Phase 1 provides the public compliance route. Phase 2 lets customers connect existing private providers while Sage retains an integrated ERP experience. Phase 3 adds a Sage private-platform proposition for customers who need more than the public route but do not want to source and integrate a separate provider themselves.

The July 2026 strategy paper argues that stopping at connectivity exposes Sage to disintermediation: a third-party platform may own onboarding, routing, status visibility, compliance perception, support, and future invoice-to-cash or procure-to-pay services while Sage remains only the accounting system of record. It also reports that a 2023 survey found existing private-platform usage among approximately 26% of Sage 50 users and 40% of Sage 200 users. Those figures are useful directional evidence but require validation against the current installed base before investment approval.

### Strategic rationale and hypotheses

The legacy *Sage as a Private Platform (Spain)* page described Phase 3 as primarily strategic rather than a baseline-compliance or immediate-revenue requirement. That distinction remains important: Phase 1 provides the public compliance route, while Phase 3 tests whether a Sage private-platform proposition is necessary to protect relevance, customer relationships and future service opportunities.

| Legacy rationale | Treatment in this PRD | Evidence status and next gate |
|---|---|---|
| Public-platform connectivity keeps customers compliant | Retain the public route as the baseline customer option across all phases | Confirmed product principle; applicable regulatory behaviour remains governed by Phase 1 evidence |
| A Sage private-platform option protects brand and compliance credibility | Treat credibility and customer ownership as strategic outcomes, not proof of customer demand | Proposed; validate with customer, market and Spain leadership research |
| Sage should maintain the strategic position it has built in Spain | Test retention, disintermediation and product-relevance exposure by customer segment | Proposed; baseline current platform usage, churn/retention risk and affected revenue |
| Owning more capability could reduce dependency on third parties | Compare build, white-label, alliance, acquisition and hybrid routes rather than assuming ownership is best | Open; ADR-SEI-001 and the reuse assessment are decision gates |
| Phase 3 may protect revenue and enable future paid services | Separate regulated core, credible Sage proposition and optional value-added services | Proposed; approve willingness-to-pay, cost-to-serve, pricing and unit economics |
| Third-party platform connectivity may create referral or partner revenue | Evaluate as one commercial model without biasing customer route guidance | Proposed; validate partner terms, demand, margin, conflicts and exit risk |
| E-invoicing could complete a wider Spanish compliance-services proposition | Treat cross-service packaging as roadmap discovery, not a Phase 3 launch requirement | Open; define customer outcome and ownership before creating further PRDs |
| Sage's existing market and authority relationships strengthen credibility | Use only as supporting context; do not treat relationships as regulatory approval or operator readiness | Evidence required; confirm claim owner, permitted use and measurable relevance |

These hypotheses explain why Phase 3 merits discovery. They do not approve a delivery route, investment, launch date or revenue forecast.

## Delivery phases and capability boundary

| Phase | Customer proposition | Sage role | Phase 3 consequence |
|---|---|---|---|
| Phase 1 — Public platform | Embedded baseline compliance | ERP/software provider connected to the public solution | Must remain available; Phase 3 cannot make the paid/private route mandatory |
| Phase 2 — Existing private providers | Keep a chosen provider and integrate it with Sage | Connector, route orchestrator, and support coordinator | Connections and historical invoice context must remain portable into Phase 3 |
| **Phase 3 — Sage private platform** | Choose Sage as the private-platform proposition and entry point | Branded proposition owner and either operator or accountable prime contractor | **Scope of this PRD** |
| Future — Cross-country network services | Reuse suitable capabilities across countries | Multi-country network and value-added service provider | Inform extensibility only; not a Spain launch commitment |

### Capability by phase

| Capability | Phase 1 | Phase 2 | Phase 3 |
|---|---:|---:|---:|
| Public solution submission and retrieval | Yes | Yes | Retained |
| Customer-owned private-provider connection | No | Yes | Retained |
| Sage-branded private-platform option | No | No | Yes |
| Private-platform entry-point publication | No | Provider-owned | Sage proposition |
| Private-to-private interconnection | Indirect/public | Provider-dependent | Required operator outcome |
| Format transformation across admitted syntaxes | Public contract | Provider-dependent | Required operator outcome |
| Platform-wide operational accountability | Public authority | External provider | Sage or named prime contractor |
| Paid value-added services | No commitment | Provider-specific | Phased commercial proposition |

## Phase 1 and Phase 2 reuse assessment

Phase 3 must extend the platform capabilities established in Phases 1 and 2 rather than create a separate invoice platform. The following visuals express the intended design constraint, the preliminary reuse boundary, and the evidence-based decision process for each candidate component.

> **Evidence caveat:** This is a PRD-level reuse hypothesis. A capability described in an approved or draft PRD is not automatically a built, deployed, scalable or production-proven component. Implementation evidence is required before a reuse decision is approved.

### One shared platform with a new operator edge

<!-- confluence-html-macro:start -->
<div class="p3reuse-suite" style="display:grid;gap:24px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
<div class="p3ra-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3ra-visual{--text:#172b4d;--muted:#6b778c;--border:#dfe1e6;--sage:#006644;--sage-bg:#e3fcef;--public:#0052cc;--public-bg:#deebff;--private:#6554c0;--private-bg:#eae6ff;--neutral:#42526e;--neutral-bg:#f4f5f7}.p3ra-visual *{box-sizing:border-box}.p3ra-visual h2{margin:0;color:var(--text);font-size:18px}.p3ra-visual .p3ra-subtitle{margin:6px 0 16px;color:var(--muted);font-size:12px;line-height:1.45}.p3ra-visual .p3ra-canvas{min-width:1080px;border:1px solid var(--border);border-radius:8px;background:#fcfcfd}.p3ra-visual svg{display:block;width:1080px;height:570px}.p3ra-visual .p3ra-label{fill:var(--muted);font-size:9px;font-weight:700;letter-spacing:.08em}.p3ra-visual .p3ra-title{fill:var(--text);font-size:13px;font-weight:700}.p3ra-visual .p3ra-copy{fill:#42526e;font-size:10px}.p3ra-visual .p3ra-small{fill:var(--muted);font-size:9px}.p3ra-visual .p3ra-product{fill:var(--sage-bg);stroke:#abf5d1;stroke-width:1.5}.p3ra-visual .p3ra-foundation{fill:#fff;stroke:#79f2c0;stroke-width:2}.p3ra-visual .p3ra-p1{fill:var(--public-bg);stroke:#b3d4ff;stroke-width:1.25}.p3ra-visual .p3ra-p2{fill:var(--private-bg);stroke:#c0b6f2;stroke-width:1.25}.p3ra-visual .p3ra-shared{fill:var(--sage-bg);stroke:#abf5d1;stroke-width:1.25}.p3ra-visual .p3ra-public{fill:var(--public-bg);stroke:#b3d4ff;stroke-width:1.5}.p3ra-visual .p3ra-provider{fill:#fff;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3ra-visual .p3ra-operator{fill:var(--private-bg);stroke:var(--private);stroke-width:2.5}.p3ra-visual .p3ra-new{fill:#fff;stroke:var(--private);stroke-width:1.25;stroke-dasharray:5 3}.p3ra-visual .p3ra-path{fill:none;stroke:var(--sage);stroke-width:2.2}.p3ra-visual .p3ra-path-public{fill:none;stroke:var(--public);stroke-width:1.6}.p3ra-visual .p3ra-path-optional{fill:none;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3ra-visual .p3ra-arrow{fill:none;stroke:var(--sage);stroke-width:2.2}.p3ra-visual .p3ra-arrow-public{fill:none;stroke:var(--public);stroke-width:1.6}.p3ra-visual .p3ra-arrow-optional{fill:none;stroke:#7a869a;stroke-width:1.5}.p3ra-visual .p3ra-notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3ra-visual .p3ra-note{padding:10px 12px;border:1px solid var(--border);border-radius:7px;color:#42526e;background:#fff;font-size:10px;line-height:1.45}.p3ra-visual .p3ra-note strong{display:block;margin-bottom:3px;color:var(--text);font-size:11px}.p3ra-visual .p3ra-legend{display:flex;flex-wrap:wrap;gap:14px;min-width:1080px;margin-top:11px;color:var(--muted);font-size:10px}.p3ra-visual .p3ra-key{display:inline-flex;align-items:center;gap:5px}.p3ra-visual .p3ra-swatch{width:10px;height:10px;border-radius:2px}.p3ra-visual .p3ra-swatch-p1{background:var(--public)}.p3ra-visual .p3ra-swatch-p2{background:var(--private)}.p3ra-visual .p3ra-swatch-shared{background:var(--sage)}.p3ra-visual .p3ra-outline{width:14px;height:10px;border:2px solid var(--private);border-radius:2px;background:#fff}
  </style>
  <h2>Phase 3 adds an operator edge—not a second invoice platform</h2>
  <p class="p3ra-subtitle">Customer products continue through the common Sage foundation. Public, external-provider and Sage-operated routes share invoice context, lifecycle, resilience and audit controls.</p>
  <div class="p3ra-canvas">
    <svg viewBox="0 0 1080 570" role="img" aria-label="Sage products use a shared Phase 1 and Phase 2 e-invoicing foundation. The foundation supports the public platform, existing private providers and a new Sage private-platform operator edge, which connects to other private platforms and sends required copies to the public solution.">
      <text x="34" y="38" class="p3ra-label">SAGE PRODUCTS</text><text x="255" y="38" class="p3ra-label">SHARED PHASE 1 + 2 FOUNDATION</text><text x="805" y="38" class="p3ra-label">NETWORK AND OPERATOR EDGES</text>

      <rect x="34" y="210" width="178" height="112" rx="10" class="p3ra-product"></rect>
      <text x="123" y="243" text-anchor="middle" class="p3ra-title">Sage ERP / API</text><text x="123" y="266" text-anchor="middle" class="p3ra-copy">Configure • send • receive</text><text x="123" y="284" text-anchor="middle" class="p3ra-copy">track • resolve</text><text x="123" y="306" text-anchor="middle" class="p3ra-small">One product-neutral contract</text>

      <path d="M212 266 H244" class="p3ra-path"></path><path d="M234 259 L244 266 L234 273" class="p3ra-arrow"></path>

      <rect x="246" y="64" width="510" height="452" rx="12" class="p3ra-foundation"></rect>
      <text x="501" y="94" text-anchor="middle" class="p3ra-title">Sage e-Invoicing shared platform</text><text x="501" y="114" text-anchor="middle" class="p3ra-small">Build once • apply consistently • retain network history</text>

      <rect x="270" y="138" width="222" height="78" rx="8" class="p3ra-p1"></rect><text x="287" y="162" class="p3ra-title">Identity and authorisation</text><text x="287" y="181" class="p3ra-copy">Legal entity • tenant • consent</text><text x="287" y="198" class="p3ra-small">Phase 1 foundation</text>
      <rect x="510" y="138" width="222" height="78" rx="8" class="p3ra-p1"></rect><text x="527" y="162" class="p3ra-title">Invoice and validation</text><text x="527" y="181" class="p3ra-copy">Canonical model • validation packs</text><text x="527" y="198" class="p3ra-small">Phase 1 foundation</text>

      <rect x="270" y="232" width="222" height="78" rx="8" class="p3ra-p2"></rect><text x="287" y="256" class="p3ra-title">Connection and readiness</text><text x="287" y="275" class="p3ra-copy">Registration • capability • health</text><text x="287" y="292" class="p3ra-small">Phase 2 foundation</text>
      <rect x="510" y="232" width="222" height="78" rx="8" class="p3ra-p2"></rect><text x="527" y="256" class="p3ra-title">Routing and transition</text><text x="527" y="275" class="p3ra-copy">Route policy • cutover • coexistence</text><text x="527" y="292" class="p3ra-small">Phase 2 foundation</text>

      <rect x="270" y="326" width="222" height="78" rx="8" class="p3ra-shared"></rect><text x="287" y="350" class="p3ra-title">Invoice network context</text><text x="287" y="369" class="p3ra-copy">Immutable route snapshot • IDs</text><text x="287" y="386" class="p3ra-small">Shared lifecycle truth</text>
      <rect x="510" y="326" width="222" height="78" rx="8" class="p3ra-shared"></rect><text x="527" y="350" class="p3ra-title">Resilience and operations</text><text x="527" y="369" class="p3ra-copy">Idempotency • reconcile • audit</text><text x="527" y="386" class="p3ra-small">Shared operational control</text>

      <rect x="270" y="420" width="462" height="70" rx="8" class="p3ra-shared"></rect><text x="501" y="447" text-anchor="middle" class="p3ra-title">Lifecycle and status orchestration</text><text x="501" y="468" text-anchor="middle" class="p3ra-copy">Preserve original network context while current customer routes evolve</text>

      <path d="M756 178 H792" class="p3ra-path-public"></path><path d="M782 171 L792 178 L782 185" class="p3ra-arrow-public"></path>
      <rect x="794" y="136" width="252" height="84" rx="9" class="p3ra-public"></rect><text x="812" y="162" class="p3ra-title">Public platform adapter</text><text x="812" y="182" class="p3ra-copy">Phase 1 submission and consultation</text><text x="812" y="200" class="p3ra-small">Retained as a valid route</text>

      <path d="M756 286 H792" class="p3ra-path-optional"></path><path d="M782 279 L792 286 L782 293" class="p3ra-arrow-optional"></path>
      <rect x="794" y="244" width="252" height="84" rx="9" class="p3ra-provider"></rect><text x="812" y="270" class="p3ra-title">External provider adapters</text><text x="812" y="290" class="p3ra-copy">Phase 2 provider-specific contracts</text><text x="812" y="308" class="p3ra-small">Retained for customer choice</text>

      <path d="M756 416 H792" class="p3ra-path"></path><path d="M782 409 L792 416 L782 423" class="p3ra-arrow"></path>
      <rect x="794" y="354" width="252" height="176" rx="10" class="p3ra-operator"></rect><text x="812" y="381" class="p3ra-title">Sage private-platform operator edge</text><text x="812" y="401" class="p3ra-copy">New external and regulated boundary</text>
      <rect x="812" y="418" width="216" height="30" rx="6" class="p3ra-new"></rect><text x="920" y="438" text-anchor="middle" class="p3ra-copy">External platform ingress / APIs</text>
      <rect x="812" y="457" width="216" height="30" rx="6" class="p3ra-new"></rect><text x="920" y="477" text-anchor="middle" class="p3ra-copy">Entry point and interconnection</text>
      <rect x="812" y="496" width="216" height="22" rx="6" class="p3ra-new"></rect><text x="920" y="511" text-anchor="middle" class="p3ra-small">Faithful copy • operator evidence</text>
    </svg>
  </div>
  <div class="p3ra-notes"><div class="p3ra-note"><strong>Reuse the platform core</strong>Identity, invoice processing, routing, historical context, resilience and audit remain shared services.</div><div class="p3ra-note"><strong>Extend before duplicating</strong>Validation, lifecycle, credentials and operations gain operator behaviour without creating parallel records.</div><div class="p3ra-note"><strong>Add one explicit boundary</strong>The new operator edge exposes regulated external capabilities while protecting internal adapter contracts.</div></div>
  <div class="p3ra-legend" aria-label="Diagram legend"><span class="p3ra-key"><i class="p3ra-swatch p3ra-swatch-p1"></i>Phase 1 capability</span><span class="p3ra-key"><i class="p3ra-swatch p3ra-swatch-p2"></i>Phase 2 capability</span><span class="p3ra-key"><i class="p3ra-swatch p3ra-swatch-shared"></i>Shared lifecycle/control</span><span class="p3ra-key"><i class="p3ra-outline"></i>New Phase 3 operator boundary</span></div>
</div>
<div class="p3rm-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3rm-visual{--text:#172b4d;--muted:#6b778c;--border:#dfe1e6;--green:#006644;--green-bg:#e3fcef;--blue:#0052cc;--blue-bg:#deebff;--purple:#6554c0;--purple-bg:#eae6ff}.p3rm-visual *{box-sizing:border-box}.p3rm-visual h2{margin:0;color:var(--text);font-size:18px}.p3rm-visual .p3rm-subtitle{margin:6px 0 16px;color:var(--muted);font-size:12px;line-height:1.45}.p3rm-visual .p3rm-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;min-width:1080px}.p3rm-visual .p3rm-column{padding:14px;border:1px solid var(--border);border-radius:9px;background:#fcfcfd}.p3rm-visual .p3rm-column h3{margin:0 0 4px;font-size:14px}.p3rm-visual .p3rm-column p{margin:0 0 12px;color:var(--muted);font-size:10px;line-height:1.4}.p3rm-visual .p3rm-column-reuse{border-top:4px solid var(--green)}.p3rm-visual .p3rm-column-extend{border-top:4px solid var(--blue)}.p3rm-visual .p3rm-column-new{border-top:4px solid var(--purple)}.p3rm-visual .p3rm-column-reuse h3{color:var(--green)}.p3rm-visual .p3rm-column-extend h3{color:var(--blue)}.p3rm-visual .p3rm-column-new h3{color:var(--purple)}.p3rm-visual .p3rm-card{margin-top:8px;padding:10px 11px;border-radius:7px;font-size:10px;line-height:1.35}.p3rm-visual .p3rm-card strong{display:block;margin-bottom:2px;color:var(--text);font-size:11px}.p3rm-visual .p3rm-reuse{background:var(--green-bg);border:1px solid #abf5d1}.p3rm-visual .p3rm-extend{background:var(--blue-bg);border:1px solid #b3d4ff}.p3rm-visual .p3rm-new{background:var(--purple-bg);border:1px solid #c0b6f2}.p3rm-visual .p3rm-rule{min-width:1080px;margin-top:14px;padding:11px 13px;color:var(--text);background:#f4f5f7;border-left:3px solid var(--purple);font-size:11px;line-height:1.45}
  </style>
  <h2>Reuse, extend, or add new operator capability</h2>
  <p class="p3rm-subtitle">The classification is preliminary until implementation maturity and technical fit are evidenced. “New” should be limited to regulated operator capabilities or boundaries that do not exist in Phases 1 and 2.</p>
  <section class="p3rm-grid" aria-label="Three-column preliminary classification of Phase 3 capabilities into reuse, extend and new operator capability">
    <article class="p3rm-column p3rm-column-reuse"><h3>Reuse as shared capability</h3><p>Preserve the contract and implementation where evidence proves fitness.</p><div class="p3rm-card p3rm-reuse"><strong>Legal entity and tenant</strong>One customer identity across every route</div><div class="p3rm-card p3rm-reuse"><strong>Canonical invoice and validation engine</strong>Common processing foundation</div><div class="p3rm-card p3rm-reuse"><strong>Connection, readiness and routing model</strong>Add Sage as another supported connection type</div><div class="p3rm-card p3rm-reuse"><strong>Immutable invoice route snapshot</strong>Keep provider and lifecycle history stable</div><div class="p3rm-card p3rm-reuse"><strong>Idempotency, reconciliation and audit</strong>One operational safety model</div></article>
    <article class="p3rm-column p3rm-column-extend"><h3>Extend the shared capability</h3><p>Keep the core, then add Phase 3 scale, trust or workflow behaviour.</p><div class="p3rm-card p3rm-extend"><strong>Authorisation and credentials</strong>Add operator certificates, seals and external trust</div><div class="p3rm-card p3rm-extend"><strong>Submission and consultation</strong>Add private ingress, event acceleration and public copies</div><div class="p3rm-card p3rm-extend"><strong>Formats and validation packs</strong>Add admitted syntaxes and transformation evidence</div><div class="p3rm-card p3rm-extend"><strong>Lifecycle and status</strong>Fan out status without contradictory history</div><div class="p3rm-card p3rm-extend"><strong>Operations and support</strong>Add operator-wide incidents, BCP and statutory evidence</div></article>
    <article class="p3rm-column p3rm-column-new"><h3>Add the Phase 3 operator edge</h3><p>Create only the externally consumable and regulated responsibilities that are genuinely absent.</p><div class="p3rm-card p3rm-new"><strong>Operator accreditation and governance</strong>Approval, control ownership and regulatory evidence</div><div class="p3rm-card p3rm-new"><strong>Published Sage entry point</strong>Discoverable destination for inbound invoices</div><div class="p3rm-card p3rm-new"><strong>External platform API</strong>Stable ingress and egress contract for other PPIFEs</div><div class="p3rm-card p3rm-new"><strong>Interconnection management</strong>Requests, tests, activation, timing and evidence</div><div class="p3rm-card p3rm-new"><strong>Commercial and exit controls</strong>Subscription, accountability and portability</div></article>
  </section>
  <div class="p3rm-rule"><strong>Design rule:</strong> provider-specific adapters may be reused behind the platform boundary, but their internal interfaces must not become Sage's external private-platform API.</div>
</div>
<div class="p3rd-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3rd-visual{--text:#172b4d;--muted:#6b778c;--border:#dfe1e6;--green:#006644;--green-bg:#e3fcef;--red:#bf2600;--red-bg:#ffebe6;--amber:#974f0c;--amber-bg:#fff7d6;--blue:#0052cc;--blue-bg:#deebff;--purple:#6554c0;--purple-bg:#eae6ff}.p3rd-visual *{box-sizing:border-box}.p3rd-visual h2{margin:0;color:var(--text);font-size:18px}.p3rd-visual .p3rd-subtitle{margin:6px 0 16px;color:var(--muted);font-size:12px;line-height:1.45}.p3rd-visual .p3rd-canvas{min-width:1080px;border:1px solid var(--border);border-radius:8px;background:#fcfcfd}.p3rd-visual svg{display:block;width:1080px;height:500px}.p3rd-visual .p3rd-label{fill:var(--muted);font-size:9px;font-weight:700;letter-spacing:.08em}.p3rd-visual .p3rd-title{fill:var(--text);font-size:12px;font-weight:700}.p3rd-visual .p3rd-copy{fill:#42526e;font-size:9.5px}.p3rd-visual .p3rd-node{fill:#fff;stroke:#c1c7d0;stroke-width:1.5}.p3rd-visual .p3rd-check{fill:var(--red-bg);stroke:var(--red);stroke-width:1.5}.p3rd-visual .p3rd-research{fill:var(--red-bg);stroke:var(--red);stroke-width:1.5;stroke-dasharray:5 4}.p3rd-visual .p3rd-gate{fill:var(--amber-bg);stroke:#ffab00;stroke-width:1.5}.p3rd-visual .p3rd-reuse{fill:var(--green-bg);stroke:#36b37e;stroke-width:1.5}.p3rd-visual .p3rd-extend{fill:var(--blue-bg);stroke:#4c9aff;stroke-width:1.5}.p3rd-visual .p3rd-wrap{fill:#f4f5f7;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:5 4}.p3rd-visual .p3rd-new{fill:var(--purple-bg);stroke:var(--purple);stroke-width:1.5}.p3rd-visual .p3rd-path{fill:none;stroke:var(--green);stroke-width:2.1}.p3rd-visual .p3rd-loop{fill:none;stroke:var(--red);stroke-width:1.6;stroke-dasharray:6 4}.p3rd-visual .p3rd-branch{fill:none;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:5 4}.p3rd-visual .p3rd-arrow{fill:none;stroke:var(--green);stroke-width:2.1}.p3rd-visual .p3rd-arrow-loop{fill:none;stroke:var(--red);stroke-width:1.6}.p3rd-visual .p3rd-arrow-branch{fill:none;stroke:#7a869a;stroke-width:1.5}.p3rd-visual .p3rd-yes{fill:var(--green);font-size:9px;font-weight:700}.p3rd-visual .p3rd-no{fill:var(--red);font-size:9px;font-weight:700}.p3rd-visual .p3rd-notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3rd-visual .p3rd-note{padding:10px 12px;border:1px solid var(--border);border-radius:7px;color:#42526e;background:#fff;font-size:10px;line-height:1.45}.p3rd-visual .p3rd-note strong{display:block;margin-bottom:3px;color:var(--text);font-size:11px}
  </style>
  <h2>Prove reuse before committing Phase 3 architecture</h2>
  <p class="p3rd-subtitle">Each candidate moves from documented intent to implementation evidence, fit assessment and an explicit architecture decision. Missing evidence returns to discovery rather than becoming an assumed dependency.</p>
  <div class="p3rd-canvas">
    <svg viewBox="0 0 1080 500" role="img" aria-label="A Phase 3 reuse decision starts with a Phase 1 or Phase 2 capability inventory, checks for implementation evidence, returns missing evidence to discovery, assesses Phase 3 fit and records one of four outcomes: reuse, extend, wrap or build new.">
      <text x="40" y="38" class="p3rd-label">CANDIDATE</text><text x="270" y="38" class="p3rd-label">EVIDENCE GATE</text><text x="535" y="38" class="p3rd-label">FIT AND GAP</text><text x="790" y="38" class="p3rd-label">RECORDED DECISION</text>

      <rect x="38" y="180" width="190" height="90" rx="10" class="p3rd-node"></rect><text x="133" y="211" text-anchor="middle" class="p3rd-title">Inventory capability</text><text x="133" y="233" text-anchor="middle" class="p3rd-copy">PRD source • service owner</text><text x="133" y="250" text-anchor="middle" class="p3rd-copy">consumer • dependency</text>

      <path d="M228 225 H286" class="p3rd-path"></path><path d="M276 218 L286 225 L276 232" class="p3rd-arrow"></path>

      <polygon points="360,150 434,225 360,300 286,225" class="p3rd-check"></polygon><text x="360" y="213" text-anchor="middle" class="p3rd-title">Implementation</text><text x="360" y="230" text-anchor="middle" class="p3rd-title">evidence?</text><text x="360" y="249" text-anchor="middle" class="p3rd-copy">Built • deployed • tested</text>

      <text x="446" y="213" class="p3rd-yes">YES</text><path d="M434 225 H508" class="p3rd-path"></path><path d="M498 218 L508 225 L498 232" class="p3rd-arrow"></path>

      <text x="348" y="321" class="p3rd-no">NO</text><path d="M360 300 V348" class="p3rd-loop"></path><path d="M353 338 L360 348 L367 338" class="p3rd-arrow-loop"></path>
      <rect x="273" y="350" width="174" height="66" rx="9" class="p3rd-research"></rect><text x="360" y="377" text-anchor="middle" class="p3rd-title">Discovery / proof</text><text x="360" y="397" text-anchor="middle" class="p3rd-copy">Inspect, test or prototype</text>
      <path d="M273 383 H174 V280" class="p3rd-loop"></path><path d="M167 280 L174 270 L181 280" class="p3rd-arrow-loop"></path>

      <polygon points="600,150 692,225 600,300 508,225" class="p3rd-gate"></polygon><text x="600" y="207" text-anchor="middle" class="p3rd-title">Fit for Phase 3?</text><text x="600" y="228" text-anchor="middle" class="p3rd-copy">Contract • scale • security</text><text x="600" y="245" text-anchor="middle" class="p3rd-copy">regulation • operations</text>

      <path d="M692 225 H730 V190 H764" class="p3rd-branch"></path><path d="M754 183 L764 190 L754 197" class="p3rd-arrow-branch"></path><rect x="766" y="154" width="266" height="70" rx="9" class="p3rd-reuse"></rect><text x="786" y="181" class="p3rd-title">Reuse unchanged</text><text x="786" y="201" class="p3rd-copy">Existing contract and component remain fit</text>
      <path d="M692 225 H730 V268 H764" class="p3rd-branch"></path><path d="M754 261 L764 268 L754 275" class="p3rd-arrow-branch"></path><rect x="766" y="233" width="266" height="70" rx="9" class="p3rd-extend"></rect><text x="786" y="260" class="p3rd-title">Extend shared capability</text><text x="786" y="280" class="p3rd-copy">Keep core; add operator behaviour</text>
      <path d="M692 225 H720 V347 H764" class="p3rd-branch"></path><path d="M754 340 L764 347 L754 354" class="p3rd-arrow-branch"></path><rect x="766" y="312" width="266" height="70" rx="9" class="p3rd-wrap"></rect><text x="786" y="339" class="p3rd-title">Wrap behind a new boundary</text><text x="786" y="359" class="p3rd-copy">Reuse internally; protect external contract</text>
      <path d="M600 300 V425 H764" class="p3rd-branch"></path><path d="M754 418 L764 425 L754 432" class="p3rd-arrow-branch"></path><rect x="766" y="391" width="266" height="70" rx="9" class="p3rd-new"></rect><text x="786" y="418" class="p3rd-title">Build or source new</text><text x="786" y="438" class="p3rd-copy">No safe reusable capability exists</text>
    </svg>
  </div>
  <div class="p3rd-notes"><div class="p3rd-note"><strong>Evidence, not PRD status</strong>Record repository/service ownership, deployment, tests, limits and production history.</div><div class="p3rd-note"><strong>Assess the whole fit</strong>Functional similarity is insufficient if scale, security, regulatory or operational characteristics differ.</div><div class="p3rd-note"><strong>Keep the decision durable</strong>Record owner, rationale, required changes, dependencies and verification evidence for every outcome.</div></div>
</div>
</div>
<!-- confluence-html-macro:end -->

## Strategic transition visual

<!-- confluence-html-macro:start -->
<div class="p3sp-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1160px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3sp-visual *{box-sizing:border-box}.p3sp-visual h2{margin:0;color:#172b4d;font-size:18px}.p3sp-visual p{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3sp-visual svg{display:block;width:1080px;height:430px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3sp-visual .lane{fill:#f4f5f7;stroke:#dfe1e6}.p3sp-visual .sage{fill:#e3fcef;stroke:#36b37e;stroke-width:2}.p3sp-visual .external{fill:#fff;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3sp-visual .public{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3sp-visual .decision{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3sp-visual .title{fill:#172b4d;font-size:13px;font-weight:700}.p3sp-visual .copy{fill:#42526e;font-size:10px}.p3sp-visual .label{fill:#6b778c;font-size:10px;font-weight:700;letter-spacing:.08em}.p3sp-visual .path{fill:none;stroke:#00875a;stroke-width:2.2}.p3sp-visual .optional{fill:none;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3sp-visual .arrow{fill:#00875a}.p3sp-visual .arrow-optional{fill:#7a869a}.p3sp-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3sp-visual .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.45}.p3sp-visual .note strong{display:block;color:#172b4d;font-size:11px;margin-bottom:3px}
  </style>
  <h2>Phase 3: Sage becomes the customer-facing private-platform option</h2>
  <p>The customer sees one Sage experience; the operating model behind it remains an explicit decision and accountability boundary.</p>
  <svg viewBox="0 0 1080 430" role="img" aria-label="Sage products connect to a Sage private-platform proposition which exchanges invoices with the Spanish public solution and other private platforms. Build, white-label, alliance, or acquisition is a gated operating-model decision behind the Sage proposition.">
    <text x="36" y="35" class="label">CUSTOMER AND PRODUCT</text><text x="330" y="35" class="label">SAGE PRIVATE-PLATFORM PROPOSITION</text><text x="790" y="35" class="label">SPANISH NETWORK</text>
    <rect x="35" y="65" width="230" height="88" rx="10" class="sage"/><text x="55" y="92" class="title">Sage customer and ERP</text><text x="55" y="114" class="copy">Configure, send, receive, track</text><text x="55" y="132" class="copy">and resolve exceptions in Sage</text>
    <rect x="330" y="65" width="350" height="88" rx="10" class="sage"/><text x="350" y="92" class="title">Sage private-platform experience</text><text x="350" y="114" class="copy">Identity, entry point, routing, transformation,</text><text x="350" y="132" class="copy">status, audit, support and customer choice</text>
    <rect x="785" y="55" width="250" height="65" rx="10" class="public"/><text x="805" y="82" class="title">AEAT public solution</text><text x="805" y="101" class="copy">Copy, public exchange and payment data</text>
    <rect x="785" y="145" width="250" height="65" rx="10" class="external"/><text x="805" y="172" class="title">Other private platforms</text><text x="805" y="191" class="copy">Free interconnection and status exchange</text>
    <path d="M265 109 H322" class="path"/><polygon points="322,109 312,103 312,115" class="arrow"/><path d="M680 95 H777" class="path"/><polygon points="777,95 767,89 767,101" class="arrow"/><path d="M680 125 C730 125 730 178 777 178" class="optional"/><polygon points="777,178 767,172 767,184" class="arrow-optional"/>
    <rect x="330" y="245" width="350" height="125" rx="10" class="decision"/><text x="350" y="272" class="title">Operating-model decision gate</text><text x="350" y="296" class="copy">Build • white-label • alliance • acquisition</text><text x="350" y="318" class="copy">Select using compliance evidence, time, control,</text><text x="350" y="336" class="copy">service accountability, investment and exit safety</text><text x="350" y="356" class="copy">Decision not yet approved</text>
    <path d="M505 245 V163" class="optional"/><polygon points="505,163 499,173 511,173" class="arrow-optional"/>
  </svg>
  <div class="notes"><div class="note"><strong>Choice remains</strong>Public and existing-provider routes remain valid customer options.</div><div class="note"><strong>Brand implies accountability</strong>Sage must be able to explain who operates, supports and controls every regulated capability.</div><div class="note"><strong>History remains stable</strong>A platform or route change must not rewrite an invoice's original network context.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Problem and opportunity

### Customer problem

The public solution provides a free compliance route, but customers with higher volumes, multiple entities, complex formats, existing trading networks, or richer workflow expectations may need routing, transformation, status visibility, exception handling, and integrated support. Today they may have to select and operate a third-party platform outside the Sage relationship.

### Business problem

If Sage offers only ERP connectivity, platform operators may become the visible owner of compliance onboarding, exchange, status, and adjacent services. Sage then bears ERP integration cost while another provider owns the expansion path. Conversely, becoming the platform operator introduces regulated, security, interoperability, availability, support, and commercial obligations beyond ordinary ERP connectivity.

### Strategic opportunity

A credible Sage option could protect product relevance, offer a consistent multi-product proposition, create a controlled path to paid services, and give Sage more influence over future invoice-to-cash and procure-to-pay experiences. These benefits are hypotheses until the addressable segment, willingness to pay, unit economics, and route feasibility are validated.

## Objectives

| ID | Objective | Evidence of success |
|---|---|---|
| G1 | Protect customer choice while adding Sage as a credible private-platform option | Customers can choose public, an existing provider, or Sage without forced migration |
| G2 | Meet the Spanish regulated operator outcomes before launch | Legal, security, interoperability and operational gates pass with evidence |
| G3 | Keep invoice exchange and exception handling inside the Sage workflow | Pilot users can complete and understand primary and recovery journeys without a separate platform console for routine work |
| G4 | Establish a viable operating and commercial model | Approved business case covers ownership, cost-to-serve, pricing, partner economics and exit |
| G5 | Preserve a future cross-country capability path without delaying Spain | Spain design separates reusable platform services from country-specific obligations |

## Non-goals

- Forcing existing private-platform customers to migrate to Sage.
- Removing the free public-platform option.
- Approving build, white-label, alliance, or acquisition through this PRD.
- Claiming that every competitor feature in the strategy paper is verified.
- Launching every value-added capability—OCR, financing, banking, procurement, payments or analytics—on day one.
- Replacing the ERP as the accounting system of record.
- Defining provider endpoint contracts before official technical specifications and implementation evidence exist.
- Committing a launch date solely from the strategy paper's forecast.

## Definitions and accountability

| Term | Meaning in this PRD | Not equivalent to |
|---|---|---|
| Sage private-platform proposition | The Sage-branded service sold, configured and supported as a private e-invoicing option | Proof that Sage owns every underlying component |
| Private platform operator | The legal/operational entity responsible for a platform meeting Spanish system requirements | A reseller or UI brand by itself |
| Fronting/white-label | Sage presents a branded experience over partner-operated capabilities | Transfer of accountability without contract and evidence |
| Entry point | Publicly discoverable destination chosen by a business for receiving invoices | A default outbound route |
| Connection | Technical and contractual context enabling exchange with a platform | Registration, readiness or active route |
| Route | Current selection used for a defined invoice direction/scope | Ownership of historical invoices |
| Interconnection | Platform-to-platform ability to exchange invoices and mandatory statuses | A bespoke customer integration |
| Faithful copy | UBL representation sent to the public solution when required | A second commercial invoice |
| Value-added service | Optional capability beyond the regulated exchange core | A prerequisite for legal compliance |

## Actors

| Actor | Need or responsibility |
|---|---|
| Spanish business/customer | Choose an appropriate route, remain compliant and understand invoice outcomes |
| Accountant or finance user | Review inbound/outbound status, correct failures and report payment/rejection information |
| Sage ERP product | Create or receive invoice intent, preserve accounting truth and show meaningful status |
| Sage platform service | Orchestrate identity, routing, exchange, audit, reconciliation and product-neutral capabilities |
| Legal private-platform operator | Meet regulated platform requirements and accept interconnection obligations |
| Underlying partner | Supply contracted capabilities when the route is white-label or alliance |
| Counterparty platform | Exchange invoices and mandatory statuses through direct or public interconnection |
| AEAT public solution | Receive required copies/data and provide the public exchange/repository functions defined by regulation |
| Sage operations and support | Monitor intended/observed state, recover safe failures and coordinate incidents |
| Security, privacy, legal and compliance | Approve control design, accountability, certification, contracts and data handling |
| Product and commercial leadership | Approve proposition, route, investment, pricing, cohort and success measures |

## Customer segments and proposition

| Segment | Default proposition | Phase 3 relevance | Evidence status |
|---|---|---|---|
| Very small business without invoicing software | Public portal | No default paid proposition | Proposed in strategy paper |
| Small business using Sage invoicing | Embedded public route | Offer Sage private option only where needs justify it | Proposed |
| Sage customer with an existing private provider | Preserve provider and integrate through Phase 2 | Do not force migration; offer opt-in transition if valuable | Confirmed product principle |
| Medium business without a private provider | Public baseline plus Sage private option | Primary discovery segment | Proposed |
| Accounting-only customer | Connector/API proposition | Validate whether Phase 3 increases retention or adoption | Proposed |
| Developer or ISV | API access | Later cohort unless business case and support model justify launch | Open |

## Business scenarios

| ID | Trigger and actor | Expected outcome | Exception/continuity rule |
|---|---|---|---|
| S1 | New customer needs more than the public route | Customer compares public and Sage options in plain language and activates only after eligibility/readiness checks | No dark pattern or forced paid upgrade |
| S2 | Existing Sage customer already uses Provider A | Customer keeps Provider A with Phase 2 integration | Phase 3 launch does not change active routes |
| S3 | Customer opts into Sage for outbound and inbound | Sage publishes/uses the selected entry point and routes new invoices through the Sage proposition | Historical Provider A invoices retain Provider A context |
| S4 | Sage customer sends to a counterparty on another private platform | Platforms exchange the invoice and required statuses directly or through the public interconnection route | Customer is not required to join the counterparty platform |
| S5 | Counterparty has no published private entry point | Exchange uses the public solution according to the regulated default | Outcome remains visible in Sage |
| S6 | Customer pays or rejects an invoice | Required state reaches the relevant issuer and public solution within the applicable rule | Duplicate or delayed events do not create contradictory history |
| S7 | Underlying partner is unavailable | Sage shows degraded state, preserves invoice safety and reconciles ambiguous outcomes | Retry occurs only when operation safety is known |
| S8 | Partner contract ends or Sage changes operating model | Customers and historical invoices remain accessible through a controlled transition | Exit plan is required before launch, not after termination |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Customer has not agreed a private receipt platform | Treat the public solution as the receipt entry point | Confirmed: RD 238/2026 Article 6 |
| BR2 | Customer already has a private provider | Phase 3 must not change that route without explicit customer authorisation | Confirmed product decision |
| BR3 | Sage is presented as the private option | The UI, contract and support model must name the operator and Sage's accountability | Proposed governance rule |
| BR4 | Private-platform invoice is issued | Produce/send the required faithful UBL copy to the public solution unless the public solution itself is the exchange/interconnection medium | Confirmed: RD 238/2026 Articles 6 and 11 |
| BR5 | Another qualifying private platform requests interconnection for a client | Accept and operationalise the request under the statutory process; do not charge the requesting platform for interconnection | Confirmed: Articles 8–9 |
| BR6 | No bilateral syntax agreement exists | Use the syntax/specifications required for the public solution | Confirmed: Article 7 |
| BR7 | Current route or operator changes | Never rewrite invoice-origin provider, identifiers, syntax, signature evidence or status history | Confirmed product continuity principle |
| BR8 | A value-added feature is not needed for regulated exchange | Package it separately from baseline compliance and disclose price/limits | Proposed commercial rule |
| BR9 | A regulatory technical detail depends on the ministerial order | Treat it as an open implementation gate, not an assumed contract | Confirmed dependency |

## Research and evidence register

| ID | Source | Finding | Confidence and limitation | PRD impact |
|---|---|---|---|---|
| E1 | *Spain_E-Invoicing_Strategy_Paper.070726.docx*, July 2026, supplied by the user | Strategic rationale, proposed customer segmentation, four delivery routes, survey claims and competitor comparison | Internal stakeholder evidence. Survey base/method and competitor claims were not supplied for independent verification | G1–G5, S1–S8; commercial and feature validation gates |
| E2 | [Ley 18/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818) | Mandatory B2B e-invoicing framework; free platform interconnection/interoperability; staged effect after regulatory development | Confirmed primary law | BR5; regulatory scope and timing model |
| E3 | [Real Decreto 238/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295) | Defines the Spanish system, private platform, formats, interconnection, status, public-copy and operator requirements | Confirmed primary regulation. Some technical details still depend on a ministerial order | FR12–FR38, NFR1–NFR15, G2 |
| E4 | [Ministry announcement on the approved B2B system](https://portal.mineco.gob.es/es-es/comunicacion/Paginas/Gobierno-impulsa-factura-electronica-en-pagos-de-empresas-y-profesionales-rebajar-carga-administrativa-y-morosidad.aspx) | Confirms public/private route choice and staged timing from the ministerial order | Official explanatory source; regulation prevails | Timeline and customer-choice framing |
| E5 | [European Commission ViDA adoption](https://taxation-customs.ec.europa.eu/news/adoption-vat-in-digital-age-package-2025-03-11_en) | ViDA adopted in March 2025; cross-border digital reporting changes are phased toward 2030 and beyond | Confirmed EU source; not proof that a Spain build is reusable unchanged | G5 and future extensibility |

### Regulatory findings that change the strategy-paper baseline

- Real Decreto 238/2026 is now approved and defines concrete private-platform duties; Phase 3 is therefore an operator-accountability decision, not only a branding or feature decision.
- The effective dates are relative to the ministerial order governing the public solution. The strategy paper's May and October 2027 dates are not treated as confirmed dates in this PRD.
- Private platforms must support the admitted structured syntaxes and transformation, advanced electronic signing/sealing, public-solution connectivity, free interconnection, business continuity, continuous support availability, and data governance/security.
- The statutory requirement says support resources must be available “at all times”; the service levels, staffing model and measurable interpretation require legal and operational approval.
- Competitor capability ticks in the strategy paper remain hypotheses until source, product edition, Spain applicability and contractual availability are evidenced.

## Current state

Phase 1 and Phase 2 PRDs define public exchange and integrations to selected external private providers. Sage does not yet have an approved Spain proposition in which customers select Sage itself as their private-platform entry point. The repository also contains no approved decision for operator legal entity, delivery route, regulated accountability, launch service catalogue, pricing, support model, or exit plan.

## Proposed target capability

The target is a product-neutral Sage platform layer used by eligible Sage products. It owns the customer-visible lifecycle and delegates only through explicit, observable contracts.

### Conceptual responsibility model

| Responsibility | Required owner | Route-dependent question |
|---|---|---|
| Customer proposition, consent and route choice | Sage | Which Sage entity contracts with the customer? |
| Legal private-platform operation | Named operator | Sage entity, acquired entity or partner? |
| ERP/accounting truth | Sage product | Which product versions and APIs are launch scope? |
| Invoice exchange and transformation | Platform operator | Built service or contracted partner capability? |
| Public-solution copy and payment/rejection communication | Accountable service named in design | Which party transmits, proves and reconciles it? |
| Interconnection onboarding and tests | Platform operator | Who accepts requests and maintains the test bank? |
| Customer support and incident command | Sage-led | What is the partner escalation and evidence contract? |
| Historical access and exit | Sage accountable to customer | How is data/service continuity protected if the route changes? |

### Core conceptual records

- **Legal entity:** immutable tax identity, jurisdiction and product tenancy.
- **Platform subscription:** commercial plan, operator, contract, service set and effective dates.
- **Registration/entry point:** external registration, published endpoint and evidence.
- **Connection:** credentials, certificates, environment, capabilities and health.
- **Route policy:** direction, scope, priority, authoriser and effective interval.
- **Invoice network context:** original route/operator, external IDs, syntax/profile, signature evidence, public-copy reference and timestamps.
- **Interconnection:** requesting/responding platform, client basis, request date, test state, effective date and evidence.
- **Operational case:** fault domain, safe next action, reconciliation status, owner and redacted evidence.

## Delivery-route decision

| Route | Potential advantage | Material exposure | Evidence required before recommendation |
|---|---|---|---|
| Build | Highest design control and reuse potential | Time, new operator capability, certifications, format/interconnection complexity and cost | Architecture estimate, capability gap, certification path, operating model and credible schedule |
| White-label | Potentially fastest branded route | Sage brand absorbs failures while control and local fit may remain with partner | Spain regulatory mapping, product fit, service levels, data/exit rights, unit economics and tested integration |
| Alliance/powered-by | Faster capability and visible specialist | Split journey, weaker differentiation and continuing commercial dependency | Customer proposition, accountability map, co-support model, margin and termination plan |
| Acquisition | Immediate people, capability and market position | Capital, diligence, integration time, country concentration and contract liabilities | Corporate development case, regulatory/technical diligence and integration plan |

**Working hypothesis:** a partner-enabled route may offer the fastest path, but it must not be recommended until Spain fit, operator compliance, customer experience, economics and exit safety are evidenced. A build-versus-partner decision must be made at the first investment gate.

## Minimum launch capability

### Tier 0 — Regulatory operator core

Identity and tenant isolation; entry-point publication and lookup; public-solution connectivity; admitted syntax receipt, validation and transformation; signature/seal handling; outbound and inbound exchange; mandatory status exchange; faithful-copy submission; payment/rejection communication; free interconnection; security certification; continuity, support, audit and reconciliation.

### Tier 1 — Credible Sage customer proposition

Embedded onboarding, transparent route choice, invoice/status timeline, actionable error messages, correction and safe retry, operations-assisted recovery, migration from/to Phase 2 providers, role-based access, service health and exportable history.

### Tier 2 — Differentiating services

Legal archiving, OCR/capture, portals, approvals, payment services, reconciliation, financing, banking, data and insights. Each requires separate demand, legal, risk, data and commercial validation; none is assumed in launch scope.

## Journeys

### J1 — Compare and activate the Sage option

1. An authorised customer sees public, existing-provider and Sage options with price, capability, operator and data-use differences.
2. Sage validates legal entity, product eligibility, required authority and contracted service.
3. The platform provisions the customer without changing any active route.
4. Readiness checks verify operator, entry point, certificates, public connectivity, formats and support visibility.
5. The customer explicitly activates inbound, outbound or both.
6. Sage records the authoriser and effective interval and confirms the old route remains attached to historical invoices.

### J2 — Outbound invoice to another private platform

1. The ERP creates an approved invoice and idempotency key.
2. Sage snapshots customer, route, syntax and operator context.
3. The platform determines the recipient entry point and agreed syntax.
4. It validates, transforms where required, applies or verifies required signature evidence, and transmits once.
5. It submits the faithful copy to the public solution when required.
6. Sage records technical, commercial and payment status events without conflating them.
7. The ERP and operations views show the same authoritative outcome.

### J3 — Inbound invoice and status

1. A public or private platform resolves the customer's Sage entry point.
2. Sage authenticates the source, validates/deduplicates the invoice and preserves the original payload/evidence according to retention policy.
3. The ERP receives a canonical representation plus original network context.
4. An authorised finance user accepts, rejects or later records payment.
5. Sage sends required status to the issuer route and public solution and reconciles acknowledgements.

### J4 — Correctable validation failure

1. Validation rejects an invoice before transmission and identifies field, rule, source and correction owner.
2. Sage does not create an external-success state or send a misleading faithful copy.
3. The user corrects the invoice in the system of record.
4. Resubmission uses a new or retained identity according to the approved correction rule and keeps the failed attempt in audit history.

### J5 — Timeout with unknown external outcome

1. Transmission times out after the mutation may have reached the external system.
2. Sage records `outcome unknown`, blocks blind resubmission and exposes the affected route/reference.
3. Automated reconciliation queries available evidence; operations escalates if no safe query exists.
4. Retry occurs only after absence or idempotent replay is proven.
5. Late responses are correlated without producing duplicate invoices or contradictory terminal states.

### J6 — Interconnection request

1. A qualifying platform requests interconnection on behalf of a client.
2. The operator validates eligibility, records receipt order/date and supplies the required specifications and test facility.
3. Until direct interconnection is ready, invoices use the public solution where the regulation requires that interim route.
4. Test evidence confirms invoice and mandatory-status exchange in agreed/default syntaxes.
5. Activation is auditable and free to the requesting platform for the regulated interconnection.

### J7 — Switch out or operating-model exit

1. An authorised customer selects another entry point or Sage initiates a controlled service transition.
2. New route activation is coordinated without deleting the Sage connection prematurely.
3. In-flight and historical invoices retain original operator, identifiers, evidence and recovery path.
4. The customer can export required records and see responsibilities after termination.
5. Credentials and data are retained, revoked or deleted only under the approved legal and continuity policy.

## Functional requirements

### Proposition, identity and governance

| ID | Requirement |
|---|---|
| FR1 | Sage must present public, existing-provider and Sage private-platform options with capabilities, price, operator identity and material limitations before selection. |
| FR2 | Only an authorised actor may contract, provision, activate, change or terminate the Sage platform for a legal entity; every action must record actor, timestamp and scope. |
| FR3 | Provisioning or validating the Sage platform must not change an active inbound or outbound route. |
| FR4 | The service must isolate legal entities, products and environments and prevent a user or credential from accessing another tenant. |
| FR5 | The platform must maintain a versioned responsibility map naming Sage, operator and partner ownership for every regulated and customer-facing capability. |

### Entry point, connection and routing

| ID | Requirement |
|---|---|
| FR6 | The platform must create and maintain a discoverable entry-point record for each opted-in legal entity and supported scope. |
| FR7 | Entry-point activation must require verified readiness for receipt, status return, public connectivity, support and audit. |
| FR8 | Inbound and outbound routes must be independently selectable where legally and technically permitted. |
| FR9 | A route change must apply prospectively and preserve the network context and recovery path of existing invoices. |
| FR10 | When no customer private entry point is published, the platform must apply the public-solution default required by regulation. |
| FR11 | The service must detect conflicting concurrent route or entry-point changes and require the actor to retry against current state. |

### Invoice formats, exchange and authenticity

| ID | Requirement |
|---|---|
| FR12 | The operator capability must receive, validate, exchange and transform every syntax admitted by the applicable Spanish regulation. |
| FR13 | Transformation must preserve semantic content, authenticity/integrity evidence and an auditable link between source and transformed representations. |
| FR14 | Private-platform issuance must apply or verify the required advanced electronic signature/seal before exchange. |
| FR15 | Every invoice must carry and preserve the unique identity components required by regulation plus Sage and external correlation identifiers. |
| FR16 | A duplicate request or inbound invoice must return the existing outcome or be quarantined; it must not create a second commercial invoice. |
| FR17 | The platform must validate required fields and agreed extensions before transmission and return actionable correction information. |
| FR18 | Customer-specific extra data may be required only when its prior contractual communication and applicable scope are evidenced. |

### Public solution and private interconnection

| ID | Requirement |
|---|---|
| FR19 | When required, the platform must send a faithful UBL copy to the public solution simultaneously with private issuance and retain acknowledgement/reconciliation evidence. |
| FR20 | The platform must not send a duplicate faithful copy when the public solution already acted as the invoice or interconnection medium. |
| FR21 | The operator must accept qualifying interconnection requests, record their order/date and make the interconnection operational within the applicable regulatory process. |
| FR22 | The interconnection capability must exchange at least invoices and mandatory commercial/payment statuses. |
| FR23 | The operator must supply required technical specifications and a test facility to the requesting qualifying platform. |
| FR24 | Regulated interconnection must not charge the requesting platform prohibited fees. Commercial customer services must be separately identifiable. |
| FR25 | Where direct interconnection is pending, the system must support the required public-solution interim path and reconcile the later cutover. |

### Status and payment lifecycle

| ID | Requirement |
|---|---|
| FR26 | The system must distinguish technical receipt, validation, delivery, commercial acceptance/rejection, payment, correction and cancellation events. |
| FR27 | Mandatory status events must be communicated to the applicable issuer/operator and public solution within the legally applicable period. |
| FR28 | Duplicate, late or out-of-order events must be correlated and retained without rolling a terminal business state backward. |
| FR29 | Payment/rejection communication must identify the invoice, event time, reporting actor, source system and acknowledgement. |
| FR30 | If Sage lacks the information required to report a status, the product must identify the responsible user/system and escalate before the deadline rather than inventing a state. |

### Operations, recovery and exit

| ID | Requirement |
|---|---|
| FR31 | Each operation must be classified as safe to retry, reconcile-before-retry, or manual-only. |
| FR32 | A mutating timeout with an ambiguous outcome must enter an explicit unknown state and prevent blind duplication. |
| FR33 | Operations must see intended and observed state, fault domain, safe next action, deadlines and redacted evidence in one case view. |
| FR34 | The service must support reconciliation across Sage, operator/partner, counterparty and public-solution records. |
| FR35 | Platform or route disablement must be controlled by direction/scope and must not remove historical access or evidence prematurely. |
| FR36 | The launch contract and product must provide an executable partner/service exit path covering customer notice, route transition, data export, in-flight work and historical retrieval. |
| FR37 | A partner change must not require Sage products to adopt a new customer-facing lifecycle when the regulated semantics remain unchanged. |
| FR38 | Customer-visible health and incident communications must identify impact and safe user action without exposing sensitive operational data. |

### Commercial and value-added services

| ID | Requirement |
|---|---|
| FR39 | Regulated core capabilities, paid value-added services and partner-supplied features must be separately itemised in catalogue, entitlement and billing. |
| FR40 | Sage must measure adoption, service cost and value-added conversion by cohort without using invoice content beyond approved purposes. |
| FR41 | A value-added service may launch only after its product owner, legal basis, data boundary, operational owner, price and acceptance criteria are approved. |
| FR42 | Referral or revenue-share arrangements must not bias route recommendations presented as compliance guidance. |

## Proposed state model

### Platform readiness

`requested → provisioning → validating → ready → active → degraded → suspended → terminating → terminated`

- `ready` means regulated and operational checks pass but no route is changed.
- `active` is scoped by legal entity and direction; it is not a single global customer flag.
- `degraded` permits only operations proven safe under the incident mode.
- `terminated` prevents new exchange but does not erase historical invoice context.

### Invoice exchange

`created → validating → ready-to-send → transmitting → acknowledged | rejected | outcome-unknown → reconciling → delivered → commercially-accepted | commercially-rejected → paid`

This is a proposed model. Architecture and legal review must confirm whether correction, cancellation, partial acceptance/payment and assignment are separate events rather than linear states.

## Failure and recovery matrix

| Failure | Required behaviour | Forbidden behaviour |
|---|---|---|
| Invalid identity, entry point or configuration | Block activation; identify correction owner | Activate and rely on runtime failure |
| Certificate/signing failure | Stop affected transmission; alert before expiry/failure | Send unsigned where signature is required |
| Provider/operator unavailable | Queue only within approved limits; show degradation and reconcile | Promise delivery or retry without bounds |
| Validation rejection | Return field/rule/source and preserve attempt | Convert rejection into generic technical error |
| Timeout after mutation | Record outcome unknown and reconcile | Blindly resubmit |
| Duplicate invoice/event | Return existing outcome or quarantine conflict | Create parallel invoice history |
| Out-of-order status | Retain event and apply approved precedence | Roll back a later authoritative state silently |
| Public-copy failure after private acceptance | Keep invoice context; retry/reconcile the copy with deadline alert | Resend the commercial invoice |
| Internal persistence failure after external success | Reconcile using correlation evidence | Tell customer the invoice definitely failed |
| Concurrent route change | Reject stale write and show current configuration | Last-write-wins without audit |
| Interconnection not ready | Use required interim public route and track the one-month process | Drop or indefinitely hold customer invoices |
| Partner termination | Execute approved transition and retention plan | Delete credentials/data before historical obligations end |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | The accountable operator must hold ISO/IEC 27001 or legally accepted equivalent evidence covering the operating scope before production. |
| NFR2 | Platform interconnection must support the secure protocols required by the applicable regulation, currently AS2 or AS4. |
| NFR3 | Keys, certificates, tokens and secrets must use approved vaulting, least privilege, rotation, expiry alerting and non-production separation. |
| NFR4 | Every mutating API and event consumer must support idempotency and durable correlation. |
| NFR5 | Audit records must be tamper-evident and capture actor/service, time, legal entity, action, before/after state and evidence reference. |
| NFR6 | Invoice data must be minimised, purpose-limited, encrypted in transit/at rest and retained/deleted under an approved Spain policy. |
| NFR7 | The service must define measurable availability, recovery, support and capacity objectives before pilot; targets require operational and commercial approval. |
| NFR8 | Business continuity and disaster recovery tests must cover exchange, public copy, status deadlines, reconciliation and partner dependency. |
| NFR9 | Monitoring must distinguish Sage product, Sage platform, operator/partner, counterparty and public-solution faults. |
| NFR10 | Logs, alerts and support bundles must redact secrets and unnecessary invoice/customer content. |
| NFR11 | Production, sandbox/test and partner environments must use separate identities, credentials, data and routing controls. |
| NFR12 | Customer-facing setup, status and recovery experiences must meet Sage accessibility and localisation standards, including Spanish language content. |
| NFR13 | Capacity models must cover invoice volume, payload size, transformation, signature operations, event bursts and statutory reporting deadlines by cohort. |
| NFR14 | Supplier/partner controls must be contractually auditable and mapped to the same service objectives customers receive from Sage. |
| NFR15 | Data portability and exit procedures must be tested before general availability and after material operator changes. |

## Product, API and operational experience

### Customer and ERP experience

- Explain “public,” “your existing provider,” and “Sage private platform” using outcomes rather than infrastructure jargon.
- Show direction-specific readiness, active route, operator, service health and effective date.
- Use one invoice timeline while preserving distinct technical, commercial and payment events.
- Put correction in the accounting system of record where possible; link to specialist handling only when necessary.
- Provide export and termination information before purchase and while active.

### API/client contract

The proposed API boundary must support: eligibility; quote/entitlement; provision; validate; activate by scope; resolve entry point; submit; receive/retrieve; report status/payment; inspect timeline; reconcile; suspend; transition; export; and terminate. Endpoint shapes and protocols are architecture decisions, not approved by this PRD.

Each mutation must accept a caller identity, legal-entity scope, idempotency key and expected current version. Responses must distinguish accepted, rejected, pending and outcome-unknown. Polling/webhook behaviour must preserve ordering and replay evidence.

### Operations experience

Operations need portfolio health, certificate/credential expiry, interconnection request ageing, public-copy exceptions, status deadline risk, reconciliation backlog, partner incidents, tenant impact, and a case-level safe action. Manual actions require permission, reason, preview where feasible, dual control for high-risk changes, and immutable audit.

## Acceptance criteria

| ID | Demonstration |
|---|---|
| AC1 | Given a customer with an active Provider A route, provisioning the Sage option leaves all routes and existing invoice context unchanged. Covers FR2–FR9. |
| AC2 | Given an eligible customer with passed readiness checks, explicit inbound activation publishes/resolves the Sage entry point without changing outbound. Covers FR6–FR11. |
| AC3 | Given an outbound invoice whose recipient uses another qualifying private platform, Sage exchanges the agreed/default structured syntax, retains signature/transformation evidence and produces the required public copy exactly once. Covers FR12–FR25. |
| AC4 | Given the same submission or inbound event twice, only one commercial invoice exists and both calls/events resolve to one auditable outcome. Covers FR15–FR16 and NFR4–NFR5. |
| AC5 | Given a timeout after transmission, the invoice becomes outcome-unknown, blind retry is blocked, and reconciliation resolves the state without duplication. Covers FR31–FR34. |
| AC6 | Given a payment or rejection, the required issuer and public communications are correlated, acknowledged and visible with deadline evidence. Covers FR26–FR30. |
| AC7 | Given a qualifying interconnection request, the operator records receipt, provides specifications/test access, supports the required interim path and demonstrates invoice/status exchange without prohibited charges. Covers FR21–FR25. |
| AC8 | Given a partner or route transition, new invoices use the new route while old invoices retain original identifiers, evidence, status access and support ownership. Covers FR35–FR37 and NFR15. |
| AC9 | Security review can trace every production operator control to certification scope, protocol, secret, tenant, audit, continuity and supplier evidence. Covers NFR1–NFR14. |
| AC10 | A customer can identify which capabilities are regulated core, paid add-ons or partner-supplied before purchase and on an invoice. Covers FR1 and FR39–FR42. |

## Measures and baselines

No numeric targets are approved. Owners must establish baselines and target dates before pilot.

| Measure | Why it matters | Baseline/target owner |
|---|---|---|
| Eligible customers choosing public, existing-provider or Sage route | Validates segmentation and customer choice | Spain Product + Commercial |
| Activation completion and time by product/cohort | Tests onboarding usability and operational effort | Product Operations |
| Invoice exchange success without manual intervention | Tests core reliability | Platform Engineering |
| Outcome-unknown and duplicate prevention rate | Tests exchange safety | SRE/Operations |
| Public-copy and mandatory-status deadline compliance | Tests regulated operation | Compliance + Operations |
| Interconnection request age and pass rate | Tests operator readiness | Platform Operations |
| Support contacts and cost per active customer | Tests commercial viability | Customer Services + Finance |
| Paid add-on attach, retention and margin | Tests value hypothesis | Commercial + Finance |
| Route transition completion and historical-access defects | Tests customer choice and exit safety | Product + Operations |

## Rollout and decision gates

| Gate | Evidence required | Blocks |
|---|---|---|
| G0 — Strategic sponsorship | Named executive sponsor, outcome, budget envelope and decision owners | Route selection |
| G1 — Regulatory interpretation | Legal mapping of RD 238/2026 and the ministerial order; operator entity and accountability | Contract/design commitment |
| G2 — Customer and proposition | Current installed-base research, segment demand, willingness to pay and minimum competitive set | Business case |
| G3 — Route recommendation | Comparable build/white-label/alliance/acquisition evidence on time, control, compliance, service, economics and exit | Investment approval |
| G4 — Technical and security feasibility | Reference architecture, official technical artefacts, sandbox/test evidence, certification and supplier controls | Pilot build |
| G5 — Operational readiness | Support model, service objectives, monitoring, reconciliation, continuity and incident exercises | External pilot |
| G6 — Pilot | Limited product/customer cohort; end-to-end, failure, interconnection and exit tests; agreed success/kill criteria | General availability |
| G7 — General availability | Legal, security, operations, finance and product sign-off; capacity and rollback evidence | Scaled launch |

Recommended delivery sequence: internal discovery → route due diligence → technical proof → employee/test tenants → limited design partners → controlled production pilot → product-by-product rollout. Public and Phase 2 routes remain fallback options throughout.

## Dependencies

- Ministerial order and official technical specifications for the public solution.
- Legal interpretation of platform/operator requirements and accountable Sage entity.
- Phase 1 public connectivity and Phase 2 connection/routing/resilience contracts.
- Official sandbox/test facilities and interconnection specifications.
- Identity, entitlement, billing, consent, certificate, signature/seal and support capabilities.
- Partner technical, security, service, data, audit and exit evidence for non-build routes.
- Current customer research and validated commercial model.

## Risks and mitigations

| Risk | Consequence | Mitigation/gate |
|---|---|---|
| Brand without control | Sage owns customer harm but cannot resolve it | Responsibility map, back-to-back controls, operational access and exit rights |
| Dates assumed too early | Missed commitment or waste | Plan relative to ministerial-order trigger; maintain scenarios |
| Public solution crowds out paid demand | Weak adoption/ROI | Segment research and clear non-compliance value before investment |
| Overbuilt launch | Delay and execution failure | Separate Tier 0/1 launch from Tier 2 services |
| Underpowered white-label proposition | Low differentiation and margin | Spain fit, capability and economics proof before selection |
| Interconnection/format complexity | Failed exchange or non-compliance | Official artefacts, conformance suite and staged interconnection testing |
| Existing providers see Sage as hostile | Partner/referral harm | Preserve customer choice and separate Phase 2 from opt-in Phase 3 |
| Partner or acquisition transition fails | Customer lock-in and historical-data loss | Tested exit/portability plan and immutable invoice context |
| Support demand is underestimated | Service and margin failure | Pilot cost-to-serve, operational simulation and capacity gate |
| Competitor matrix is inaccurate | Wrong feature/pricing decision | Source every claim by Spain product/edition and date |
| Value-added data use exceeds purpose | Privacy/trust harm | Separate consent, legal basis, minimisation and service-level governance |

## Open questions and decision owners

| ID | Question | Why it matters | Proposed owner | Blocks |
|---|---|---|---|---|
| OQ1 | Which legal entity will be the operator/customer contracting party? | Determines regulatory, tax, liability and support accountability | Spain Legal + Compliance | G1 |
| OQ2 | Has the ministerial order been published, and what technical/date triggers apply? | Sets exact contract and effective timeline | Regulatory Compliance | G1/G4 |
| OQ3 | What is the current private-platform usage by product, segment, volume and provider? | Validates the 2023 survey and migration opportunity | Research + Data | G2 |
| OQ4 | Which outcomes make customers pay rather than use the free public route? | Determines proposition and ROI | Product Marketing + Research | G2/G3 |
| OQ5 | What is the minimum launch set by segment and product? | Controls scope and schedule | Product | G2/G3 |
| OQ6 | Which route best satisfies Spain compliance, time, control, economics and exit? | Core investment decision | Executive sponsor | G3 |
| OQ7 | Can an existing Sage/Sovos agreement support Spain white-label operation and exit? | May constrain a leading option | Commercial Legal | G3 |
| OQ8 | What availability/support interpretation and service targets are required? | Regulation requires continuity and support availability | Legal + Operations | G4/G5 |
| OQ9 | Which product versions and API/connector cohorts launch first? | Determines integration and support load | Spain Product leaders | G3/G6 |
| OQ10 | Which entity reports payment/rejection and obtains the source data? | Determines API, deadline and accountability | Product + Compliance | G4 |
| OQ11 | What retention, archiving and post-termination access applies to each record? | Determines cost, privacy and exit | Legal + Records Management | G4/G5 |
| OQ12 | Which Tier 2 services warrant separate proposals? | Prevents unbounded Phase 3 scope | Portfolio Product | Post-G2 |

## Decisions

| ID | Decision | Status | Owner/date |
|---|---|---|---|
| D1 | Keep the public route and existing-provider integrations as customer options | Proposed product principle | Approval required |
| D2 | Define launch requirements independently of build/partner/acquisition route | Proposed | Architecture + Product approval required |
| D3 | Do not confirm a calendar launch date until the ministerial-order trigger and chosen route are evidenced | Proposed risk control | Regulatory + Sponsor approval required |
| D4 | Treat operator accountability and exit safety as investment gates | Proposed | Legal + Sponsor approval required |

## Traceability summary

| Outcome | Evidence/rules | Scenarios | Requirements | Acceptance |
|---|---|---|---|---|
| Customer choice | E1–E4, BR1–BR3 | S1–S3 | FR1–FR11 | AC1–AC2, AC10 |
| Compliant exchange | E2–E4, BR4–BR6 | S4–S6 | FR12–FR30 | AC3–AC7 |
| Safe operation and continuity | E1, E3, BR7–BR9 | S7–S8 | FR31–FR38, NFR1–NFR15 | AC5, AC8–AC9 |
| Viable differentiated proposition | E1, E5, BR8 | S1–S2 | FR39–FR42 | AC10 |

## Readiness

**Discovery and consultation-ready.** This PRD is the authoritative Confluence umbrella for strategic, regulatory, customer, commercial and architecture discovery. Publication communicates the proposal and open decisions; it does **not** mean the investment, operating model, delivery scope or production launch is approved. G1–G5 are blockers to a production pilot; unresolved Tier 2 choices do not block core discovery.

## Change log

| Date | Change | Evidence/decision source |
|---|---|---|
| 2026-08-05 | Initial Phase 3 discovery PRD created | July 2026 strategy paper; Ley 18/2022; RD 238/2026; official Ministry and EU sources |
| 2026-08-10 | Consolidated the legacy strategic rationale and building-block navigation into the authoritative Phase 3 umbrella; renamed the Confluence topic and aligned it to four capability categories | User-approved Phase 3 information architecture; legacy Confluence pages 837588801 and 855180225 |
