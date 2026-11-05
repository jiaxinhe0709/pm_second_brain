---
id: PRD-SEI-210
title: Phase 3 — Sage as a Private Platform (Spain)
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-11-03
reviewers:
  - Jiaxin He
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
  - NAV-SEI-005
  - NAV-SEI-006
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
| Material changes | This revision adds the proposed OP01–OP23, CX01–CX08, VA01–VA12 and EX01–EX05 capability framework, explicit B2G capability CX09, responsibility transfer, minimum proposition, transition terms and capability gates CG1–CG7. It incorporates Jiaxin He's November 2026 product clarifications and the withdrawal, fiscal-correction, PDF and secure-transport review corrections. The former tiers map to the four layers below. |
| Unchanged areas | Retains the predecessor relationship, strategic rationale, operating-model options, business scenarios, journeys, FR1–42, NFR1–15, AC1–10 and risks. Source-dependent wording is refreshed without claiming implementation. Existing diagrams and conceptual records remain design hypotheses. No operator, investment, launch cohort, publication or lifecycle approval is granted. |
| Decisions still open | Operator and contracting entity; actual implementation and reuse fitness; launch cohort and commercial model; interconnection approach and clock interpretation; Phase 2/3 international countries, coverage and phasing; B2G coverage; optional services; support, retention and exit commitments. Earlier cross-country scope statements remain visible for review against PO-03. |

## Decision summary

This PRD defines the discovery and decision boundary for Sage to offer a Sage-branded private e-invoicing platform in Spain. The intended outcome is that eligible customers can choose Sage as their private-platform entry point, exchange compliant B2B invoices with public and private routes, see invoice and payment status inside their Sage workflow, and retain customer choice without being forced away from an existing provider.

The strategic direction is **proposed, not approved**. This document does not select build, white-label, alliance, or acquisition. It defines the minimum product and regulated operator outcomes that any route must satisfy and the evidence gates required before Sage accepts operator accountability.

> **Product principle:** A Sage-branded experience must have explicit operational and regulatory accountability. Branding a partner service as Sage must not hide who operates the platform, controls data, resolves failures, maintains interconnections, or remains responsible when the partnership changes.

The product question is: **Based on Phases 1 and 2, what additional outcomes must Sage own when the customer selects Sage as its private platform?** The capability register answers that question. It does not select components, endpoints or a delivery model. All layers, classifications, priorities and the minimum launch proposition are **proposed for review**. Product-owner scope clarifications below are confirmed inputs, not regulatory interpretations or evidence of readiness.

### Product-owner clarifications — November 2026

Source: Jiaxin He, product-owner clarifications supplied for this revision. No exact clarification day or implementation approval is asserted.

| Source ID | Confirmed product input | Application and remaining decision |
|---|---|---|
| PO-01 | When a customer onboarded to Sage as a private platform wants to connect with any other private platform, Sage must establish that interconnection within one calendar month. In Phase 2, the external private platform owns this responsibility. Phase 2 covers direct integrations with six private platforms. | OP05 owns the Phase 3 outcome. Confirm the six-provider list and actual integration readiness; six integrations in product scope do not prove six deployed integrations. CG4/CG5 must define the clock and evidence of completion. The statutory receiving-platform process and its queue exception remain separate legal rules; they do not silently qualify this product commitment. |
| PO-02 | Peppol is not mandatory, but is widely used by major organisations. Sage must determine how to support a counterparty private platform that is not on Peppol, for example through direct connection or another approach. | OP23 covers the qualified transport outcome; OP05 covers interconnection establishment. The selected network, direct/other approach and counterpart coverage remain open. Peppol participation or BIS format support alone does not prove complete Spain interconnection. |
| PO-03 | International e-invoicing and B2G are in scope for Phases 2/3. Peppol is expected for international e-invoicing. B2G is believed to be available in Sage, but coverage is unverified. | VA12 moves to Layer 2 as a Phase 2/3 capability to define; CX09 makes B2G explicit. Countries, flows, Phase 2/3 phasing and delivery approach remain open. CF01 records the conflict with the earlier future-only cross-country position. EX01–EX05 remain guardrails, not a reason to exclude international exchange. |

## Phase 3 document map

This umbrella PRD explains the complete proposition. Four category pages organise the child documents so each decision, foundation and delivery surface can be reviewed by the appropriate business, legal, engineering, security and operational owners. A detailed document can support more than one category, but it has one authoritative Confluence location and is cross-linked elsewhere rather than duplicated.

| Category | Authoritative detailed documents | Capability boundary |
|---|---|---|
| [Routing and Transmission](https://confluence.sage.com/pages/viewpage.action?pageId=876576916) | PRD-SEI-223 Exchange; PRD-SEI-224 Lifecycle | Public/private exchange, routing, transformation, faithful copy, status, rejection and payment reporting |
| [Compliance and Operator Readiness](https://confluence.sage.com/pages/viewpage.action?pageId=876576917) | ADR-SEI-001 Delivery Model; FP-SEI-001 Reuse Assessment; PRD-SEI-221 Operator Readiness | Accountable operator, reuse evidence, regulatory governance, external validation and production gates |
| [Security and Operations](https://confluence.sage.com/pages/viewpage.action?pageId=876576918) | PRD-SEI-225 Operations; PRD-SEI-226 Security | Trust, identity, certificates, data, audit, resilience, support and reconciliation |
| [Interconnection and Interoperability](https://confluence.sage.com/pages/viewpage.action?pageId=876576919) | PRD-SEI-222 Customer; cross-links to PRD-SEI-223 and PRD-SEI-225 | Entry-point onboarding, migration, public/private connectivity, platform interconnection and ecosystem recovery |
| Commercial and coverage decisions | Capability register and planned proposals | Customer value, packaging and optional services; VA12 international exchange and CX09 B2G are Phase 2/3 scope to define under PO-03, with phasing and coverage open |

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

**Earlier scope position retained for review — CF01:** the final row above conflicts with PO-03 if read as excluding international exchange from Phase 3. PO-03 is the current product input: international and B2G are in Phase 2/3 scope, with launch coverage and phasing undecided. The row is retained as the earlier position, not as a current scope exclusion. Objective G5 also retains its earlier future-path wording; EX01–EX05 preserve reuse boundaries without deferring the in-scope VA12 capability.

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

The retained visuals illustrate earlier design hypotheses. The proposed capability register below refines their reuse labels at business-outcome level. A new operator responsibility does not require a new component, and a shared design pattern does not prove a reusable implementation. Use [FP-SEI-001](../feature-proposals/FP-SEI-001-phase3-existing-capability-reuse-gap-assessment.md) for the implementation assessment.

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
| BR9 | An official technical detail or applicability interpretation remains unresolved | Keep the affected capability gated; do not assume a production contract from the published order or local PRE files | E6; REF-SPFE; replaces the earlier publication-dependent wording |

## Research and evidence register

| ID | Source | Finding | Confidence and limitation | PRD impact |
|---|---|---|---|---|
| E1 | *Spain_E-Invoicing_Strategy_Paper.070726.docx*, July 2026, supplied by the user | Strategic rationale, proposed customer segmentation, four delivery routes, survey claims and competitor comparison | Internal stakeholder evidence. Survey base/method and competitor claims were not supplied for independent verification | G1–G5, S1–S8; commercial and feature validation gates |
| E2 | [Ley 18/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818) | Mandatory B2B e-invoicing framework; free platform interconnection/interoperability; staged effect after regulatory development | Confirmed primary law | BR5; regulatory scope and timing model |
| E3 | [Real Decreto 238/2026, original publication](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295) | Defines the Spanish system, private platform, formats, interconnection, status, public-copy and operator requirements | Primary regulation; apply with the published order in E6 and operation-specific technical evidence. Product clarifications do not reinterpret it. | FR12–FR38, NFR1–NFR15, Objective G2 |
| E4 | [Ministry announcement on the approved B2B system](https://portal.mineco.gob.es/es-es/comunicacion/Paginas/Gobierno-impulsa-factura-electronica-en-pagos-de-empresas-y-profesionales-rebajar-carga-administrativa-y-morosidad.aspx) | Confirms public/private route choice and staged timing from the ministerial order | Official explanatory source; regulation prevails | Timeline and customer-choice framing |
| E5 | [European Commission ViDA adoption](https://taxation-customs.ec.europa.eu/news/adoption-vat-in-digital-age-package-2025-03-11_en) | ViDA adopted in March 2025; cross-border digital reporting changes are phased toward 2030 and beyond | Confirmed EU source; not proof that a Spain build is reusable unchanged | G5 and future extensibility |
| E6 | [Order HAC/1028/2026, original publication](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20587), published 5 October 2026; [RES-SEI-002](../context/RES-SEI-002-spain-public-platform-technical-evidence.md), current reviewed local PRE release 29 October 2026 | Final public-copy, admission, withdrawal/correction, reporting and access baseline; technical evidence is now available | Publication is established. Business schemas, authority, replay, field mappings and live qualification still have specific SPFE-Q gates. | OP12/14/20–22; OQ2; CG4/CG5 |
| E7 | PO-01–03 above, Jiaxin He, November 2026 | One-calendar-month product interconnection commitment; six Phase 2 direct integrations in scope; Peppol optional for peers and expected for international; international/B2G in Phase 2/3 | Confirmed product-owner input. Not regulatory interpretation, provider selection, country coverage, launch phasing or implementation evidence. | OP05/23; VA12; CX09; CF01–03 |
| E8 | [PPIFE_competitor_analysis.xlsx](https://sage365.sharepoint.com/sites/NWservicesforSmall/Shared%20Documents/All/EU/ES/PPIFE_competitor_analysis.xlsx?web=1), supplied workbook reviewed November 2026; precise locators in REF-COMP | Supports competitive opportunities and challenges proposition assumptions | Explicit claims, inference and conflicting cells remain distinct. The supplied local copy is the reviewed input; the linked connected copy is a locator, not a byte-equality or latest-version claim. No workbook cell establishes a Sage requirement. | Layer 3 investigation; CX08/09; VA12 qualification |

### Regulatory findings that change the strategy-paper baseline

- Real Decreto 238/2026 is now approved and defines concrete private-platform duties; Phase 3 is therefore an operator-accountability decision, not only a branding or feature decision.
- The final Order HAC/1028/2026 is published. The strategy paper's forecast dates are not a launch commitment. Compliance must bind the actual applicability periods and exceptions to each enabled scope using E6; publication itself is no longer an open question.
- Private-platform duties include admitted-syntax exchange/transformation, trust capability, public connectivity, free interconnection, continuity, support and data governance/security. The broad signing/seal wording does not approve substituting an operator seal for the required customer/delegate signature; REF-TRUST and CG5 govern that interpretation.
- The statutory requirement says support resources must be available “at all times”; the service levels, staffing model and measurable interpretation require legal and operational approval.
- Competitor capability ticks in the strategy paper remain hypotheses until source, product edition, Spain applicability and contractual availability are evidenced.

## Current state

Phase 1 and Phase 2 PRDs define public exchange and integrations to selected external private providers. Sage does not yet have an approved Spain proposition in which customers select Sage itself as their private-platform entry point. The repository also contains no approved decision for operator legal entity, delivery route, regulated accountability, launch service catalogue, pricing, support model, or exit plan.

## Proposed target capability

The target is a product-neutral Sage offering used by eligible products. Sage is answerable for the customer-visible outcome; the named operator performs or explicitly allocates the operator responsibilities. Existing conceptual records and diagrams are retained design hypotheses, not approved component or deployment boundaries. [ADR-SEI-001](../decisions/ADR-SEI-001-phase3-delivery-model-accountability.md) owns the delivery-model decision.

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

<a id="capability-framework"></a>

## Capability framework — proposed for review

This register consolidates the reviewed capability model. It adds the operator outcomes that Sage must own or explicitly allocate when selected as the private platform. It references the existing requirements and feature evidence rather than defining another invoice platform.

### Gate and objective identifiers

- G1–G5: Objectives (what Phase 3 must achieve)
- CG1–CG7: Capability evidence gates (evidence or decision needed before confirming a capability)
- Rollout G0–G7: Programme stage gates (sponsorship to general availability)

The register replaces the former three tier lists as the scope model: **Tier 0 maps to Layer 1; Tier 1 maps to Layer 2; Tier 2 maps to Layer 3. Layer 4 contains extensibility constraints.** VA12 retains its review ID but moves to Layer 2 under PO-03; it is no longer an optional future-only service. CX09 restores B2G explicitly. The layer mapping and recommended launch boundary remain proposed.

| Classification | Meaning and limit |
|---|---|
| REUSE | An evidenced Phase 1/2 foundation appears applicable, subject to actual implementation and readiness qualification. A reusable design pattern is not a production-ready build. |
| EXTEND | A relevant foundation exists in the evidence; Phase 3 adds behaviour, actors, coverage, assurance or accountability. |
| NEW RESPONSIBILITY | Sage assumes an operator outcome assigned to the external private platform in Phase 2. This does not imply new code or a new component. |
| UNKNOWN / NEEDS VALIDATION | Evidence cannot establish coverage, fitness, ownership or the required approach. Local absence alone does not prove non-existence. |

Priorities are recommendations: **LAUNCH FOUNDATION**, **LAUNCH CANDIDATE**, **POST-LAUNCH CANDIDATE**, **FUTURE CONSIDERATION**, **DECISION REQUIRED** and **EVIDENCE REQUIRED**. They indicate need or next review action, not readiness or an approved roadmap. A missing proof does not make an applicable obligation optional.

Source IDs resolve in [REF Source references](#ref-source-references). Confidence concerns documentary support for the assessment: **H** explicit, **M** supported inference, **L** weak/conflicting. None proves deployment.

### Layer 1 — Regulatory / operator core

This layer includes external duties and proposed controls needed to fulfil the supported operator outcomes safely. It does not label each internal control as a separate statutory requirement. Countries or transaction types added under VA12/CX09 need their own applicability assessment.

| ID / capability and business outcome | Classification | Recommended priority | Phase 1/2 foundation → Phase 3 delta | Evidence / confidence | Open evidence or decision gate |
|---|---|---|---|---|---|
| OP01 Operator accountability — know who answers for the offering. | NEW RESPONSIBILITY | DECISION REQUIRED | External provider operates its platform → name the operator, contracting party and allocated responsibilities. | FR5; REF-DECISION; H | CG1: entity, agreements, liability, evidence and exit rights. |
| OP02 Identity and delegated authority — act only for an authorised business and purpose. | EXTEND | LAUNCH FOUNDATION | Existing business/caller/delegate distinctions → qualify operator and peer actors without weakening isolation. | FR2/4; REF-ONB GAP-01/03; REF-TRUST; H | CG3/CG5: actual business mapping, grants, revocation and isolation. EX01. |
| OP03 Receiving entry-point publication — opted-in businesses are discoverable on Sage. | NEW RESPONSIBILITY | LAUNCH FOUNDATION | Provider-owned publication → Sage publication, consultation, change and removal outcomes. | FR6–7; REF-CUSTOMER; H | CG4: authoritative source, propagation, multiple entries and withdrawal evidence. EX02. |
| OP04 Recipient destination resolution — select an evidenced eligible destination. | UNKNOWN / NEEDS VALIDATION | EVIDENCE REQUIRED | Existing logical lookup design → qualified Spain source coverage and selection policy. Invoice consultation is not a directory. | REF-LOOKUP RLU-05–10; H on gap | CG4/CG5: sources, absence evidence, freshness, precedence and public-default cases. EX02. |
| OP05 Peer-platform interconnection — establish exchange with the requested private platform. | NEW RESPONSIBILITY | LAUNCH FOUNDATION | External provider owns interconnection; PO-01 identifies six Phase 2 direct integrations in scope → Sage fulfils PO-01 for its onboarded customer. | PO-01/02; FR21–25; J6; H | CG4/CG5/CG6: six-provider evidence, one-calendar-month clock, completion and non-Peppol counterpart approach. CF02/03; EX02. |
| OP06 Route and invoice-context continuity — new choices do not rewrite earlier work. | REUSE | LAUNCH FOUNDATION | Scoped routes, per-function readiness and original invoice context → qualify the Sage offering in the same model. | FR3/8–11; REF-ROUTE SPC-03–06; H | CG3: actual scope, effective boundaries, concurrency and historical access. EX01/02/05. |
| OP07 Outbound exchange — deliver the authorised invoice to its intended recipient. | EXTEND | LAUNCH FOUNDATION | Documented send/upload/result flow and provider integration → qualified operator delivery and independent action evidence. | J2; FR12–18; REF-SEND; H | CG3/CG4: Spain coverage, recipient result and uncertain effects. EX02/03. |
| OP08 Inbound exchange — receive the authorised invoice and deliver it to the business product. | EXTEND | LAUNCH FOUNDATION | Public collection, private intake and capture patterns → qualify Sage peer/public receipt and product handoff. | J3; REF-RECEIVE; H | CG4: source authority, public/private handoff and receipt meanings. EX02/03. |
| OP09 Meaning-preserving transformation — preserve invoice meaning across admitted syntaxes. | EXTEND | LAUNCH FOUNDATION | Existing Spain mapper and preferred DTS candidate → qualify required conversion pairs and provenance. | FR12–13; REF-DTS; H | CG3/CG4: build, source/target matrix, mappings, rule packs, semantic coverage and operations. EX03. |
| OP10 Validation — identify invalid content before dependent exchange. | EXTEND | LAUNCH FOUNDATION | Public/provider validation patterns → complete applicable profiles, Spain rules and evidenced extensions. | FR17–18; J4; SPFE-Q04/Q14; H | CG4/CG5: governing versions, field coverage and correction responsibility. EX03. |
| OP11 Authenticity and trust — use the approved signer and trust arrangements. | EXTEND | DECISION REQUIRED | Tax/certificate custody candidates → prove B2B purpose, signing authority and operator trust. | FR14; REF-TRUST; H | CG3/CG5: customer/delegate versus operator seal, actual custodian and accepted profiles. EX01–03. |
| OP12 Faithful public-copy outcome — submit required copies with separate proof. | EXTEND | LAUNCH FOUNDATION | Public submission foundation; external-provider copy remains an assumption → Sage owns execution, result and recovery. | FR19–20; REF-SEND OUT-Q03; SPFE-S02; H | CG4/CG5: issuance timing, copy indicator, acknowledgement and retry owner. EX04. |
| OP13 Counterparty lifecycle exchange — communicate authorised business states to the relevant party. | EXTEND | LAUNCH FOUNDATION | Lifecycle processing and provider feeds → qualified peer relay, authority and independent destination outcomes. | FR22/26–30; REF-LIFE; H | CG4/CG5: event meaning, actor, required destinations and missing information. EX04. |
| OP14 Public lifecycle reporting — report applicable facts without inventing a business state. | EXTEND | LAUNCH FOUNDATION | Proposed Spain mappings → supported actions, fields and public results. | REF-LIFE SPEC041 §2.1–2.2; H | CG4/CG5: three conditional reuses, five missing bindings, authority, field/date rules and cancellation recovery. EX04. |
| OP15 Unknown-outcome reconciliation — avoid unsafe duplicate action after uncertainty. | REUSE | LAUNCH FOUNDATION | Phase 2 operation-safety and reconciliation design → qualify each operator action's evidence and repeat safety. | J5; FR31–34; REF-OPS; H | CG3/CG4: authoritative result discovery, safe repeats and recovery ownership. EX02/04. |
| OP16 Historical evidence conservation — retain explainable invoices, events and action history. | EXTEND | LAUNCH FOUNDATION | Saved files, original context, raw events, derived status and failed attempts → complete operator evidence and custody. | FR35–36; REF-RECEIVE/EXIT; H | CG6: coverage, provenance, custodian, access, retention and holds. EX03/05. |
| OP17 Continuity and operational support — sustain, monitor and recover the complete service. | EXTEND | LAUNCH FOUNDATION | Provider recovery and support coordination → whole-service monitoring, controlled actions, incident ownership and continuity. | NFR7–9/13–14; REF-OPS; H | CG6: service promise, staffing, capacity, dependencies and exercise evidence. EX05. |
| OP18 Security and data assurance — evidence controls for the actual offering. | UNKNOWN / NEEDS VALIDATION | EVIDENCE REQUIRED | Existing security/certification claims → prove coverage of the selected operator and data chain. | NFR1–3/6/11/14; REF-TRUST; H on need, L on coverage | CG3/CG5/CG6: scope, transport, data roles, supplier controls and approvals. EX01/02/05. |
| OP19 Continuing obligations and controlled exit — stopping new traffic does not abandon earlier work. | EXTEND | LAUNCH FOUNDATION | Route/exit designs → supported historical processing, handover and dependency release. | J7; FR35–37; REF-EXIT; H | CG5/CG6: post-switch actors, unfinished work, records and release rules. EX05. |
| OP20 Permitted submission withdrawal — withdraw the correct public submission with traceability. | UNKNOWN / NEEDS VALIDATION | LAUNCH FOUNDATION | SPFE CancelInvoice contract; no evidenced Sage withdrawal command → qualify the customer outcome separately from report cancellation. | SPFE-S10; REF-WITHDRAW; H on external contract/gap | CG4/CG5: permitted original/copy case, authority, target references, result and unknown-outcome recovery. EX04. |
| OP21 Fiscal correction — correct an issued invoice under the applicable rectification rule. | UNKNOWN / NEEDS VALIDATION | LAUNCH FOUNDATION | ERP issuance ownership and correction design → prove product support and downstream exchange/report consequences. | REF-SEND; SPFE-S02 Articles 5.5–5.6; H on need, coverage unknown | CG3/CG4/CG5: correction case, document relationships, actor ownership and evidence. Separate from OP20 and pre-issue correction. EX03/04. |
| OP22 Transitional readable-PDF delivery — accompany the invoice when the statutory condition applies. | EXTEND | LAUNCH FOUNDATION | Local-product generation decision and attachment candidate → qualify recipient delivery, independently of structured delivery/copy. | REF-PDF; RD238-T2; H | CG4/CG5: applicability/exception evidence, exact revision, permitted channel and delivery proof. Never send the PDF to SPFE. EX03/04. |
| OP23 Qualified secure inter-platform transport — exchange with peers under evidenced transport and trust arrangements. | UNKNOWN / NEEDS VALIDATION | LAUNCH FOUNDATION | Customer/API and network candidates → qualify the operator role, required AS2/AS4 boundary and counterpart coverage. | PO-02; NFR2; RD238 Article 13.1(b); REF-ROUTE; H on need, coverage unknown | CG3/CG4/CG5/CG6: actual assets, peer/network contract, profiles, identities, invoice/status coverage and operations. Assess Peppol and non-Peppol paths without selecting either. EX02. |

### Layer 2 — Credible Sage proposition

Operator execution belongs to Layer 1. These capabilities make the outcome usable in the customer's Sage workflow. VA12 and CX09 are in-scope coverage capabilities to define under PO-03, not claims that all countries, networks or administrations launch together.

| ID / capability and customer outcome | Classification | Recommended priority | Phase 1/2 foundation → Phase 3 delta | Evidence / confidence | Open evidence or decision gate |
|---|---|---|---|---|---|
| CX01 Informed choice and activation — select Sage without accidental migration or hidden terms. | EXTEND | LAUNCH FOUNDATION | Setup/readiness separation → explain public, existing-provider and Sage options; explicitly activate selected scope. | FR1–3/8/39; J1; H | CG1/CG2/CG7: eligibility, price, entitlement, operator, scope and terms. EX01/05. |
| CX02 Embedded onboarding — complete only missing setup inside Sage. | EXTEND | LAUNCH FOUNDATION | Shared discovery, saved connection and certificate candidates → one understandable setup journey with per-function readiness. | REF-ONB GAP-01–08; J1; H | CG2/CG3: launch products, resource mapping, inputs, authority and next actor. EX01. |
| CX03 Automated ERP exchange — send and receive without routine duplicate entry or another console. | EXTEND | LAUNCH FOUNDATION | Existing sending/retrieval patterns → supported product workflows using OP07/08. | Objective CG3; J2/J3; REF-SEND/RECEIVE; H | CG2/CG4: product versions, directions and end-to-end workflow coverage. EX02/03. |
| CX04 Understandable status — distinguish delivery, copy, business state and reporting. | EXTEND | LAUNCH FOUNDATION | Existing lifecycle/history → coherent view of separate actions, freshness and uncertainty. | FR26/29/38; REF-LIFE; H | CG2/CG4: meanings and completion wording; retain OP16 source/attempt history. EX04. |
| CX05 Actionable correction and recovery — know what to fix, who acts and whether to wait. | EXTEND | LAUNCH FOUNDATION | Validation/reconciliation patterns → embedded guidance and accountable escalation. | J4/J5; FR30–34; H | CG2/CG4/CG6: correction ownership, safe actions and support handoff. OP20/21 remain distinct outcomes. EX03–05. |
| CX06 History, records access and export — inspect evidence and obtain a usable handover. | EXTEND | LAUNCH FOUNDATION | Retrieval/history/exit proposals → defined customer access and export promise, including after product cancellation. | FR36; REF-RECEIVE/EXIT; H | CG5/CG6: content, permissions, continuing access channel and completeness. EX05. |
| CX07 Accountable customer support — receive one understandable answer across the service chain. | EXTEND | LAUNCH FOUNDATION | Support coordination → Sage-led customer case ownership and incident communication. | FR33/38; REF-OPS; H | CG1/CG6: communication, escalation and service commitments. EX05. |
| CX08 Accountant, multi-entity and migration suitability — selected cohorts can act across permitted businesses and enter Sage safely. | EXTEND | LAUNCH CANDIDATE | Delegation, batch setup and transition designs → qualify the selected cohort journeys. | REF-ONB/EXIT; REF-COMP C90/C158; M | CG2/CG3/CG6: decide accountant portfolios, multi-entity administration, batch and migration separately; this is not one indivisible delivery item. EX01/05. |
| VA12 International e-invoicing — support the Phase 2/3 international proposition to be defined. Retained review ID; moved from Layer 3. | UNKNOWN / NEEDS VALIDATION | DECISION REQUIRED | Existing network/readiness candidates and earlier TBC coverage → define international flows with Peppol expected under PO-03. | PO-03; REF-INTERNATIONAL; REF-COMP C24; H on scope, coverage unknown | CG2/CG3/CG4/CG5/CG7: countries, transactions, Phase 2/3 phasing, participation, approach and economics. CF01; EX01–05. |
| CX09 B2G invoice exchange — support the Phase 2/3 public-sector proposition to be defined. | UNKNOWN / NEEDS VALIDATION | EVIDENCE REQUIRED | Product owner believes Sage capability exists; workbook claims FACe/FACeB2B → verify actual product and administration coverage without treating the networks as interchangeable. | PO-03; REF-COMP C22; H on scope, coverage unknown | CG2/CG3/CG4/CG5: product/build, supported administrations, formats, transaction scope, evidence and Phase 2/3 phasing. EX01–05. |

### Layer 3 — Optional value-added / differentiators

Only the incremental promise is optional: OP16/CX06 records access, CX04 status and OP17/CX07 support remain foundations. Competitive claims below are supporting research, not requirements. VA12 is defined only in Layer 2.

| ID / potential customer outcome | Classification | Recommended priority | Foundation → possible delta | Evidence / confidence | Open evidence or decision gate |
|---|---|---|---|---|---|
| VA01 Enhanced archiving — additional preservation assurance. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | Operational conservation; Sage archive TBC → separately defined archive service. | REF-COMP row 110; M | CG7: demand, assurance, access and cost. EX05. |
| VA02 Advanced analytics — useful cash-flow or process insights beyond status. | EXTEND | POST-LAUNCH CANDIDATE | Claimed activity reporting → validated analytical decisions. | REF-COMP C94/C100; M | CG3/CG7: data quality, decision value and permitted use. EX04/05. |
| VA03 Additional portal access — serve an actor not adequately served by embedded access. | UNKNOWN / NEEDS VALIDATION | DECISION REQUIRED | Conflicting Sage portal claims → establish the extra access need and existing fit. | REF-COMP C99 versus template C71; L | CG2/CG7: investigate for launch only for a defined actor; required records access stays CX06. EX01/05. |
| VA04 OCR/AI capture — reduce unstructured-document entry work. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | Claimed existing Sage capture → qualify reuse for a defined AP need. | REF-COMP C125; M | CG3/CG7: Spain/product coverage, quality and human review. EX03. |
| VA05 Business approvals — coordinate authorised internal decisions. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | ERP/ISV candidates → incremental workflow value without duplicating ERP ownership. | REF-COMP C25; M | CG7: actor, process, owner and demand. EX01/03. |
| VA06 Banking/reconciliation enrichment — relate invoices to evidenced bank activity. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | Claimed Banking Cloud matching → qualified invoice/payment information. | REF-COMP C114; M | CG3/CG7: coverage, matching confidence and authority; do not infer a reportable payment automatically. EX04/05. |
| VA07 Payment initiation — execute an authorised payment. | UNKNOWN / NEEDS VALIDATION | FUTURE CONSIDERATION | Workbook reports no Sage payment execution → validate existing/partner options. | REF-COMP C97/C114; L | CG7: demand, permissions, risk, ownership and economics. EX01/05. |
| VA08 Financing — obtain liquidity against eligible invoices. | UNKNOWN / NEEDS VALIDATION | FUTURE CONSIDERATION | Satago/Sage 50 claim → establish Spain applicability and value. | REF-COMP C113; L | CG7: geography, eligibility, partner and commercial case. EX05. |
| VA09 Wider business-document exchange — exchange orders and delivery documents where useful. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | Claimed ERP contacts/catalogue/quotes/documents → qualify network exchange, not another ERP suite. | REF-COMP rows 85–89; M | CG7: document/process demand and product ownership. EX03. |
| VA10 E-commerce integration — remove a demonstrated merchant handoff problem. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | Claimed ISV connectors → selected cohort and connector coverage. | REF-COMP C96; M | CG2/CG7: customer need and ecosystem support. EX02/03. |
| VA11 Sold compliance intelligence / managed service — provide additional content or delegated work. | UNKNOWN / NEEDS VALIDATION | POST-LAUNCH CANDIDATE | Internal compliance/support foundation → separate additional service promise. | REF-COMP rows 112/116; M | CG7: assess content and delegated operations separately; scope, staffing, liability and price. EX05. |

**Opportunity recommendations:** investigate VA03 only against an evidenced launch access need; retain the post-launch candidates for separate discovery; leave VA07/08 for future consideration. Exclude blockchain audit, a duplicate catalogue/quote suite and standalone general signing products from this definition unless a customer problem is evidenced. B2G and international exchange are not in that exclusion: PO-03 puts them in scope to define.

### Layer 4 — Future extensibility guardrails

EX01–EX05 are proposed design constraints for current capability decisions. Their **FUTURE CONSIDERATION** priority concerns future reuse, not postponing country-rule separation or the in-scope VA12/CX09 decisions. They do not invent another country's requirements.

| ID / boundary and protected outcome | Classification | Recommended priority | Existing foundation → constraint to preserve | Evidence / confidence | Open gate |
|---|---|---|---|---|---|
| EX01 Identity and delegated authority — preserve correct business/action scope. | REUSE | FUTURE CONSIDERATION | Party/caller/delegate distinctions → keep NIF, routing schemes and Spain representation rules local; do not make them universal identity assumptions. | REF-ONB/IDENTITY/TRUST; H | CG3/CG5: actual mappings and qualified country authority. |
| EX02 Routing, discovery, peer interconnection and transport — keep roles independently qualified. | EXTEND | FUTURE CONSIDERATION | Shared routes and connections → separate sender selection, destination evidence, peer/network support and transport. Spain default/bridge rules cannot become universal fallback. | REF-LOOKUP/ROUTE; PO-02; H | CG4: exact route/network coverage, including non-Peppol counterparties. |
| EX03 Formats, transformation and provenance — preserve source meaning and local profiles. | REUSE | FUTURE CONSIDERATION | DTS qualification and original-file patterns → version supported pairs, profiles and local rules; Spain UBL/Facturae/correction rules cannot become global defaults. | REF-DTS; FR12–18; H | CG3/CG4: build, mappings, rule versions and semantic evidence. |
| EX04 Lifecycle and country reporting — preserve facts separately from local obligations. | EXTEND | FUTURE CONSIDERATION | Shared events/history → qualify interpretations, actor/date rules, public-copy/reporting duties and destination results by country. Annex II is not a universal status model. | REF-LIFE; FR19–30; H | CG4/CG5: actual country binding and compatibility evidence. |
| EX05 Operations, retention, entitlement and exit — preserve jurisdiction and service boundaries. | EXTEND | FUTURE CONSIDERATION | Cases, history and transitions → scope support, evidence rights, retention, charging and post-switch duties by offering/operator/jurisdiction. | REF-OPS/EXIT; FR35–42; M | CG1/CG6/CG7: contracts, operating model, record disposition and commercial scope. |

## Phase 2 → Phase 3 responsibility transfer

The named operator may perform or explicitly delegate work. Sage remains answerable for the proposition it offers. Customer authority and business information remain prerequisites; Sage does not become the issuer, buyer or source of payment facts by assuming the platform role.

| Responsibility / capability | Phase 2 owner → Phase 3 accountable outcome | Sage foundation and remaining gap | Completion evidence / unresolved decision |
|---|---|---|---|
| Operator accountability / OP01 | External private platform → named operator and Sage proposition allocation. | Integration accountability exists; legal/service allocation remains open. | Entity, agreements and responsibility map; CG1. |
| Entry-point publication / OP03 | External platform → accurate Sage receiving membership. | Setup patterns; publication mechanism unqualified. | Authorised selection and reliable publication/consultation evidence; CG4. |
| Peer interconnection / OP05 | External platform → Sage fulfils PO-01 for its customer. | Phase 2 direct-integration scope; operator request/test process remains distinct. | Request/clock, peer qualification, exchange completion and escalation evidence; CG4/CG5/CG6. |
| Sending / OP07 | Provider delivers beyond Sage handoff → operator proves recipient outcome. | Sending patterns; Spain operator route coverage open. | Recipient result and accountable recovery; CG4. |
| Receiving / OP08 | Provider receives before Sage intake → operator proves receipt and product handoff. | Collection/capture; operator ingress and public/private handoff open. | Source authority, receipt and product result; CG4. |
| Transformation / OP09 | Provider supplies conversion → operator proves required coverage. | Preferred DTS candidate; complete conversion portfolio unknown. | Supported matrix and semantic/provenance evidence; CG3/CG4. |
| Validation / OP10 | Provider applies platform rules → operator applies applicable profiles and rules. | Existing patterns; complete coverage unqualified. | Rule/field coverage and correction owner; CG4/CG5. |
| Authenticity/trust/transport / OP11/23 | Provider supplies qualified arrangements → operator proves each trust and transport purpose. | Certificate/network candidates; operator fitness unknown. | Signer/delegate, custody, peer/network contract and conformance evidence; CG3/CG4/CG5. |
| Faithful copy / OP12 | Provider submission is an assumption → Sage owns copy outcome when it is the operator. | Public submission; issuance/result/retry gaps. | Independent copy result and recovery owner; CG4/CG5. |
| Counterparty lifecycle / OP13 | Provider relays states → operator proves authorised communication. | Lifecycle processing; cross-platform relay contract open. | Source fact, actor and destination evidence; CG4/CG5. |
| Public reporting / OP14 | Provider/customer allocation varies → expressly allocated authorised report outcome. | Proposed Spain mappings; execution unproven. | Mandate, applicable fields and public result; CG4/CG5. |
| Reconciliation / OP15 | Provider supplies external evidence → operator resolves or owns uncertainty. | Shared operation-safety design; source access and queries vary. | Original outcome evidence or owned unresolved case; CG4. |
| Continuity/support / OP17/CX07 | Provider restores its service → complete operating promise and Sage-led customer support. | Coordination patterns; full service coverage unapproved. | Accepted operating model and credible exercise evidence; CG6. |
| Historical evidence / OP16/CX06 | Provider holds part of the records → controlled custody, access and handover. | Saved files/history; completeness and rights open. | Coverage, custodian and usable access/export evidence; CG6. |
| Switching/exit / OP19 | Each provider controls its actions → explicit new-traffic and continuing-work ownership. | Transition design; enabled paths and former-provider actions unqualified. | Cutover, unfinished work, records and separate dependency release decisions; CG5/CG6. |

## Minimum launch capability

**Proposed for review:** an eligible business can choose Sage as its private platform, exchange invoices through its Sage workflow, understand each action's result, resolve problems with accountable support, and retain access to its records when its choices change.

| Launch boundary | Recommendation and evidence condition |
|---|---|
| Operator foundation | Fulfil the applicable Layer 1 outcomes before enabling dependent service. A small launch cohort cannot waive an operator duty. OP20/21/23 remain unproven capabilities, not assumed delivery. |
| Credible customer experience | CX01–CX07 form the smallest coherent proposed proposition. Basic status, records and support are foundations; enhanced analytics, archive assurance and sold managed services are additional promises. |
| Cohort-dependent journeys | Decide the CX08 accountant, multi-entity, batch and migration journeys independently for the selected products and customers. Existing private providers remain a valid choice. |
| Conditional legal PDF obligation | OP22 is Layer 1, not a discretionary cohort feature. Apply RD238-T2 when its statutory conditions hold; require evidence for an exception or non-applicability. Local product generation and recipient delivery are separate responsibilities. |
| International and B2G | VA12/CX09 are Phase 2/3 scope to define under PO-03. Approve countries, transaction/administration coverage, phase allocation and launch timing before commitments. Their undecided phasing is not an exclusion from Phase 3. |
| Optional services | Defer Layer 3 unless a bounded customer need and its owner, legal/data basis, service model and economics pass CG7. No feature-parity backlog is implied. |

RD238-T2 applies during the first 12 months of applicability for businesses whose preceding-calendar-year VAT volume of operations exceeded EUR 8 million, unless the recipient voluntarily and expressly accepts the original format. The readable PDF goes to the recipient, never SPFE. This is not a period starting at Sage onboarding. REF-PDF records the local-product generation decision and open delivery qualification.

## Transition terminology

These business terms distinguish outcomes; they do not add a shared glossary meaning or select an implementation. [REF-TERMS](#ref-source-references) remains authoritative for shared terminology. Use offboarding only as an umbrella with the actual outcomes named.

| Term | Meaning in this proposition |
|---|---|
| Switch into Sage | Move specified future traffic from another platform to Sage. Former-provider execution is promised only where authority and contracts support it. |
| Switch out of Sage | Move specified future traffic to another platform while assigning earlier work. |
| Traffic cutover | The evidenced boundary at which new sending/receiving changes for the authorised scope. |
| Product cancellation | End access to a Sage product; assess the platform agreement separately. |
| Platform termination | End the defined platform service scope without erasing continuing obligations. |
| Unfinished transactions | Started delivery, copy or reporting actions still awaiting resolution. |
| Historical processing | Later authorised action concerning an earlier invoice. |
| Continuing obligations | Duties still to fulfil after a change, with an identified actor and permitted path. |
| Records access | Continued authorised inspection of retained records. |
| Export | Evidenced handover of a defined records package; not proof that all obligations transfer. |
| Retention | Lawful keeping and disposition of each record class, including holds. |
| Credential release | Remove each access dependency after its final authorised need ends; incident containment has its own rules. |

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

This journey retains the receiving-platform request path. PO-01 also covers an onboarded Sage customer's request to connect with another private platform. OP05 owns that product outcome; CF02 keeps its clock and the statutory receiving-platform process distinct.

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
| FR21 | The operator must accept qualifying interconnection requests, record their order/date and make the interconnection operational within the applicable regulatory process. For Sage's customer-requested capability, apply PO-01; CF02 records the separate clock and legal interpretation gate. |
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

This is a proposed model. Architecture and legal review must confirm whether correction, cancellation, partial acceptance/payment and assignment are separate events rather than linear states. The illustration does not replace the separate processing, delivery, business-fact and reporting outcomes in REF-LIFE. OP20 withdrawal, OP21 fiscal correction and cancellation of a business report are distinct operations.

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

The existing AC IDs are retained as proposed demonstrations. AC3's “exactly once” describes the intended absence of duplicate business effect, not an evidenced exactly-once transport guarantee. The capability gates require actual contract and operating evidence; these rows are not passed tests.

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

<a id="capability-gates"></a>

## Capability evidence gates CG1–CG7

These proposed gates qualify capability decisions and reuse claims.

| Gate | Evidence or decision needed | Accountable roles from existing domain ownership | Consequence / related rollout stage |
|---|---|---|---|
| CG1 Operator and accountability | Named operator and contracting party; delivery model; responsibility, liability, delegated-control, evidence-access and exit rights. | Executive sponsor, Spain Legal, Product; REF-DECISION. | Before operator proposition approval; supports Rollout G1/G3. |
| CG2 Customer proposition and cohort | Launch products/versions, actors, volumes and valued outcomes. Decide CX08 journeys separately. Define VA12/CX09 flows and Phase 2/3 allocation without treating in-scope coverage as already delivered. | Product, Research, Commercial. | Before customer scope approval; supports Rollout G2/G3/G6. |
| CG3 Reuse qualification | Actual implementation/build, contracts, environments, consumers, owners, limits and relevant operating evidence. DTS includes source/target mappings, rule packs and operations. A service name, draft or published page is insufficient. | Existing capability owners and Engineering; REF-REUSE. | Before claiming usable reuse, capacity or savings; supports Rollout G3/G4. |
| CG4 Exchange contracts and evidence | Entry-point/discovery coverage; peer/public handoffs; secure transport; invoice, copy and status result meanings; original-outcome recovery; representative conformance evidence. Define non-Peppol counterpart coverage. | Integration/API owners and Compliance. | Before confirming supported operation; supports Rollout G4/G6. |
| CG5 Regulatory and authority interpretation | Applicable operator duties and periods; customer/delegate versus seal policy; public routing/copy rules; reporting actors and dates; withdrawal/correction; OP22 applicability; continuing obligations. Reconcile PO-01 with the separate statutory process. | Legal/Compliance, Security. | Before confirming affected coverage; supports Rollout G1/G4. |
| CG6 Operating, records and exit model | Service/support promise, staffing, capacity, incident command, continuity evidence, custody/access, retention, unfinished work and credential release. Customer and supplier commitments must be achievable together. | Operations, Legal/Records, Security. | Before customer service commitments and activation; supports Rollout G5/G6/G7. |
| CG7 Commercial and optional value | Offering terms, entitlement, price and cost-to-serve; incremental need, ownership and legal/data basis for optional services. International/B2G scope is confirmed input, while its economics and delivery details remain open. | Product, Commercial, Finance. | Before committing the proposition or optional service; supports Rollout G2/G3/G7. |

Outcomes can be proposed before readiness evidence is complete, but cannot be represented as enabled or production-ready. Optional-service details may remain open if excluded from the launch promise. Operator selection, launch cohort and commercial model remain decisions, not recommendations turned into approvals.

## Rollout and decision gates

CG1–CG7 supply evidence to the programme stages below as mapped above.

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

- Applicable published Order HAC/1028/2026, qualified official technical contracts and unresolved SPFE-Q evidence in REF-SPFE; publication itself is no longer pending.
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
| Dates assumed too early | Missed commitment or waste | Bind the published applicability baseline to the selected scope; qualify operating-model timing and open technical dependencies before a launch commitment |
| Public solution crowds out paid demand | Weak adoption/ROI | Segment research and clear non-compliance value before investment |
| Overbuilt launch | Delay and execution failure | Use the Layer 1/2 launch boundary and separately justified Layer 3 services; decide VA12/CX09 coverage and phasing under PO-03 |
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
| OQ2 | Which published applicability periods, authority rules and unresolved SPFE technical gates apply to each enabled capability? | The final order exists; exact coverage, schemas, replay, mappings and live qualification remain open | Regulatory Compliance | Rollout G1/G4; CG4/CG5 |
| OQ3 | What is the current private-platform usage by product, segment, volume and provider? | Validates the 2023 survey and migration opportunity | Research + Data | G2 |
| OQ4 | Which outcomes make customers pay rather than use the free public route? | Determines proposition and ROI | Product Marketing + Research | G2/G3 |
| OQ5 | What is the minimum launch set by segment and product? | Controls scope and schedule | Product | G2/G3 |
| OQ6 | Which route best satisfies Spain compliance, time, control, economics and exit? | Core investment decision | Executive sponsor | G3 |
| OQ7 | Can an existing Sage/Sovos agreement support Spain white-label operation and exit? | May constrain a leading option | Commercial Legal | G3 |
| OQ8 | What availability/support interpretation and service targets are required? | Regulation requires continuity and support availability | Legal + Operations | G4/G5 |
| OQ9 | Which product versions and API/connector cohorts launch first? | Determines integration and support load | Spain Product leaders | G3/G6 |
| OQ10 | Which entity reports payment/rejection and obtains the source data? | Determines API, deadline and accountability | Product + Compliance | G4 |
| OQ11 | What retention, archiving and post-termination access applies to each record? | Determines cost, privacy and exit | Legal + Records Management | G4/G5 |
| OQ12 | Which optional Layer 3 services warrant separate proposals? | Prevents unbounded scope; VA12 is instead Layer 2 under PO-03 | Portfolio Product | After Rollout G2; CG7 |

### Open capability conflicts and evidence limits

| ID | Conflict or gap | Treatment for this revision / next evidence |
|---|---|---|
| CF01 International scope | Earlier phase table and Objective G5 describe a future cross-country path; the earlier wording says “not a Spain launch commitment.” PO-03 places international and B2G in Phase 2/3 scope. | Preserve the earlier text visibly. Follow PO-03 for current product scope; review countries, flows, launch phasing and wording under CG2/CG5/CG7. EX guardrails are not a scope exclusion. |
| CF02 One-calendar-month commitment | PO-01 is Sage's customer-requested product capability. RD238 Article 9 sets a receiving-platform process, clock and queue exception. | Do not call PO-01 a legal interpretation or silently apply the queue exception to it. CG4/CG5/CG6 must establish the product clock, request evidence, completion, exception handling and operational promise. |
| CF03 Six Phase 2 integrations | PO-01 confirms six direct integrations in Phase 2 scope, but the sixth integration is unconfirmed (Yooz, Sovos or another). The competitor workbook compares B2B Router, ZeroComa, EDICOM, SERES (Docapost), Banqup (Unifiedpost) and Yooz. REF-ONB SPEC039 names five providers and Sovos as a candidate. | The workbook comparator list is not the Phase 2 integration list. Confirm the selected six, including the sixth provider, and each actual contract, country/function coverage and readiness under CG3/CG4. Do not infer selection or deployment from either list. |
| CF04 Source and API coverage | The 29 October PRE contracts and later API references establish documentary detail, not Sage runtime support. Some guide/schema statements conflict. | REF-SPFE SPFE-Q01–19, REF-ONB GAP-01–08, REF-SEND SND-G01–09 and REF-LIFE LIF-G01–08 retain their owning evidence gates. CG3/CG4 qualify selected builds; no documentary update closes them by itself. |
| CF05 Copy and routing | External-provider faithful-copy handling is an assumption; copy-result/error reporting and retry ownership are open. Public-default guidance conflicts in some no-match/private-address cases. | REF-SEND OUT-Q03, OUT-09 and SND-G09 own the detailed decisions. OP04/12 must preserve independent recipient/copy results and hold unresolved destinations; CG4/CG5. |
| CF06 Trust and lifecycle | General signature/seal wording does not establish signer equivalence. Eight report families and 52 source rows do not prove executed mappings. | REF-TRUST qualifies each signer/custody purpose. REF-LIFE distinguishes three conditional action reuses from five missing bindings. Keep CG3/CG4/CG5 open. |
| CF07 Switching versus interconnection | Existing onboarding/routing evidence keeps Private A → Private B customer switching disabled. PO-01 peer interconnection is a different outcome. | OP05 does not activate a customer route change. CG2/CG4/CG6 must qualify switch-in/out scope and each former-provider action. OP19 continuity and exit cannot be deferred with optional migration automation. |
| CF08 Status and completion language | The retained linear state illustration and AC3 wording can conceal independent action results or imply a transport guarantee. | Retain IDs, but use REF-LIFE meanings and the acceptance qualification above. Withdrawal, fiscal correction and report cancellation remain distinct. CG4 supplies actual evidence. |
| CF09 International/B2G and competitive claims | PO-03 confirms scope and expectations, not countries, certified network participation, complete B2G coverage or a delivery model. Workbook detail and summary cells sometimes conflict. | VA12/CX09 remain UNKNOWN / NEEDS VALIDATION. REF-COMP is supporting research only; CG2/CG3/CG4/CG5/CG7 establish each selected promise. |

## Decisions

| ID | Decision | Status | Owner/date |
|---|---|---|---|
| D1 | Keep the public route and existing-provider integrations as customer options | Proposed product principle | Approval required |
| D2 | Define launch requirements independently of build/partner/acquisition route | Proposed | Architecture + Product approval required |
| D3 | Do not confirm a calendar launch date until published applicability, selected operating model and dependent capability evidence are established | Proposed risk control; updates the earlier publication-trigger wording | Regulatory + Sponsor approval required |
| D4 | Treat operator accountability and exit safety as investment gates | Proposed | Legal + Sponsor approval required |

## Traceability summary

| Outcome | Evidence/rules | Scenarios | Requirements | Acceptance |
|---|---|---|---|---|
| Customer choice | E1–E4, BR1–BR3 | S1–S3 | FR1–FR11 | AC1–AC2, AC10 |
| Compliant exchange | E2–E4, BR4–BR6 | S4–S6 | FR12–FR30 | AC3–AC7 |
| Safe operation and continuity | E1, E3, BR7–BR9 | S7–S8 | FR31–FR38, NFR1–NFR15 | AC5, AC8–AC9 |
| Viable differentiated proposition | E1, E5, BR8 | S1–S2 | FR39–FR42 | AC10 |

## Readiness

**Discovery and consultation-ready.** Git remains canonical; Confluence is the publishing representation. This revision is proposed for review and has not been published. The existing publication metadata and stable page identity are unchanged; neither they nor this revision approve an investment, operating model, launch cohort or readiness claim. Rollout G1–G5 remain pilot blockers. CG1–CG7 qualify the dependent outcomes; unresolved optional Layer 3 choices do not block core discovery. VA12/CX09 scope details remain open under PO-03 rather than excluded from Phase 3.

<a id="ref-source-references"></a>

## REF Source references

Use published primary regulation and official technical material first, then approved internal decisions, current internal product evidence, proposed PRDs/specifications, official competitor information, third-party information and inference. A published internal draft is not an approved decision. PO-01–03 are product-owner clarifications, not legal interpretations. Existing detailed sources remain authoritative in their owning documents.

| Source ID | Exact source / version or locator | Supported claim and limit |
|---|---|---|
| RD238 | [Original RD 238/2026](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295), published 31 March 2026; Articles 6–13, especially Article 9 and 13.1(b); preamble on Peppol BIS | Spain entry points, interconnection, formats, transport, lifecycle and operator duties. Peppol BIS validity as UBL does not establish a universal Peppol network requirement or selected Sage route. |
| RD238-T2 | Same original regulation, transitional provision 2(1)–(2) | Conditional readable-PDF duty and recipient-only channel; not a discretionary cohort feature or period from onboarding. |
| SPFE-S02 | [Original Order HAC/1028/2026 PDF](../context/BOE-A-2026-20587.pdf); [official text](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-20587), published 5 October 2026; Articles 3–5, 7–11 and Annex II | Public-copy, admission, permitted withdrawal/correction, reporting and access rules. Does not establish an implemented Sage command or complete runtime contract. |
| SPFE-S10 | [Original CancelInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/CancelInvoice.wsdl>), reviewed local PRE release 29 October 2026; documentation, operation, binding and service ports | External withdrawal transport. Business eligibility, complete message mapping, Sage availability and repeat safety need separate evidence. |
| SPFE-S16 | [Original SendInvoice WSDL](<../context/WSDL servicios web - PRE_29_10_2026/SendInvoice.wsdl>), same reviewed release; documentation, operation and ports | Public submission transport, not proof of issuance coordination, receipt semantics or production access. |
| REF-SPFE | [RES-SEI-002](../context/RES-SEI-002-spain-public-platform-technical-evidence.md), 29 October release review and SPFE-Q01–19; [source manifest](../assets/regulatory/spain/spfe/source-manifest.json), current_wsdl_baseline | Selected original catalogue, formats, contracts, schemas and examples, with versions/hashes and limits. Current reviewed local release is 29 October 2026; neither future publication monitoring nor mapping completeness is established. |
| REF-REUSE | [FP-SEI-001](../feature-proposals/FP-SEI-001-phase3-existing-capability-reuse-gap-assessment.md), preliminary inventory, evidence pack and fitness gates | Implementation qualification method; candidate names and documented designs are not deployed reuse. |
| REF-DECISION | [ADR-SEI-001](../decisions/ADR-SEI-001-phase3-delivery-model-accountability.md), decision status and accountability matrix | Proposed operating-model decision, not a selected operator or approved route. |
| REF-GOV | [PRD-SEI-221](PRD-SEI-221-operator-readiness-regulatory-governance.md), control register; [PRD-SEI-222](PRD-SEI-222-customer-onboarding-entry-point-migration.md), customer/entry-point/transition scope | Existing operator readiness and customer foundations; retain their open decisions rather than copying controls here. |
| REF-CUSTOMER | PRD-SEI-222 above; FR6–11 and J1/J7 in this PRD | Customer setup, publication and transition outcomes. No inferred provider enrolment API or enabled migration. |
| REF-EXCHANGE | [PRD-SEI-223](PRD-SEI-223-interoperability-routing-transformation.md), BR1–14 and FR1–44; [PRD-SEI-224](PRD-SEI-224-lifecycle-rejection-payment-reporting.md), business rules and reporting scope | Existing proposed exchange/lifecycle ownership; country/provider qualification remains open. |
| REF-ONB | [SPEC-SEI-039](../specs/onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md), §§1–3 and GAP-01–08; [SPEC-SEI-040](../specs/onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md), preserved calls and Spain proposals | Shared E-Invoice setup/discovery candidates, five named providers and Sovos candidate. Neither selected sixth provider nor implementation readiness is established. |
| REF-ROUTE | [SPEC-SEI-014](../specs/SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md), invariants and SPC-01–08; [SPEC-SEI-013](../specs/SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md), integration roles | Shared routing and qualification design. Customer-provider integration does not prove peer-interconnection fitness or a required separate API. |
| REF-LOOKUP | [SPEC-SEI-012](../specs/SPEC-SEI-012-consult-public-platform-for-recipient-information.md), RLU-05–10 and RLU-SPFE-R01 | Destination evidence and absence/selection limits; AEAT invoice consultation is not a central recipient directory. |
| REF-SEND | [SPEC-SEI-022](../specs/invoice-sending/SPEC-SEI-022-invoice-sending-solution-summary.md), §§4–6; [SPEC-SEI-023](../specs/invoice-sending/SPEC-SEI-023-invoice-sending-logical-feature-specification.md), OUT-09 and OUT-SPFE-R01/02; [SPEC-SEI-024](../specs/invoice-sending/SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md), SND-G01–09; [SPEC-SEI-043](../specs/invoice-sending/api-reference/SPEC-SEI-043-invoice-sending-api-reference.md), contract issues | Existing sending design, copy assumption, routing conflict and preserved API evidence. Publication and snapshots do not prove Spain support. |
| REF-RECEIVE | [SPEC-SEI-025](../specs/invoice-receiving/SPEC-SEI-025-invoice-retrieval-solution-summary.md), §§4–7; [SPEC-SEI-026](../specs/invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md); [SPEC-SEI-027](../specs/invoice-receiving/SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md), RET-G gates | Collection, source preservation, product delivery and access are separate outcomes; current readiness unproven. |
| REF-LIFE | [SPEC-SEI-030](../specs/invoice-lifecycle/SPEC-SEI-030-invoice-lifecycle-sequence-and-reuse-assessment.md), country-pack assessment and LIF-G01–08; [SPEC-SEI-041](../specs/invoice-lifecycle/api-reference/SPEC-SEI-041-existing-e-invoice-lifecycle-api-reference.md), §§2.1–2.2 | Shared lifecycle candidate and proposed eight-action/52-row mapping. Three conditional reuses and five missing bindings do not establish execution or configuration-only delivery. |
| REF-DTS | [SPEC-SEI-008](../specs/SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md), reuse boundaries, architecture delta and UM gates | DTS is the preferred transformation candidate. Prove build, contracts, mappings, rule packs, semantic preservation and operations for each selected scope. |
| REF-TRUST | [SPEC-SEI-001](../specs/SPEC-SEI-001-certificate-management-solution-specification.md), certificate bridge and G1/G9/G10; [PRD-SEI-226](PRD-SEI-226-security-trust-identity-data-audit.md), BR3–15 | Custody/trust candidates and purpose/actor separation. Tax credentials, an operator seal and invoice-signing authority are not interchangeable. |
| REF-OPS | [PRD-SEI-225](PRD-SEI-225-operations-resilience-support-reconciliation.md), operational rules and scenarios; [PRD-SEI-215](PRD-SEI-215-resilience-recovery-reconciliation-structured-review.md), safety and reconciliation | Existing shared recovery/control design, not proof of operator-scale continuity or continuous support coverage. |
| REF-EXIT | [SPEC-SEI-031](../specs/offboarding/SPEC-SEI-031-customer-offboarding-solution-summary.md), §§2, 4–7; [SPEC-SEI-032](../specs/offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md); [SPEC-SEI-033](../specs/offboarding/SPEC-SEI-033-customer-offboarding-sequence-and-reuse-assessment.md) | Distinct transition, unfinished-work, access, export and release outcomes. Proposed support windows are not statutory periods or current service commitments. |
| REF-WITHDRAW | [FP-SEI-002](../feature-proposals/FP-SEI-002-global-api-submission-withdrawal.md), Evidence and gap / Proposed direction | External CancelInvoice evidence and missing Sage withdrawal command. No endpoint or implementation is approved. |
| REF-PDF | [PRD-SEI-246](PRD-SEI-246-spain-invoice-preparation-and-outbound-flow.md), transitional PDF product rule, recorded 22 October 2026; REF-SEND OUT-PDF-R01/02 and SND-G08 | Local-product generation allocation and open recipient delivery qualification. Source legal applicability is RD238-T2. |
| REF-IDENTITY | [PRD-SEI-231](PRD-SEI-231-country-identifiers-tenancy-and-delegated-accountants.md), country identity and delegated-accountant boundaries | Shared identity principles; Spain NIF and network addresses need purpose-specific bindings. |
| REF-INTERNATIONAL | [PRD-SEI-234](PRD-SEI-234-cross-border-and-reusable-country-capabilities.md), scope and evidence gates; [PRD-SEI-240](PRD-SEI-240-peppol-access-point-service-readiness.md), readiness and open decisions; PO-03 | Existing international/network candidates. PO-03 confirms Phase 2/3 scope and Peppol expectation, not an approved country set, access-point implementation or delivery approach. |
| REF-TERMS | [GLO-SEI-001](../context/GLO-SEI-001-e-invoicing-terminology.md), authority, route, lifecycle, retention and reuse vocabulary | Shared meanings. The transition section names distinct business outcomes without changing the glossary. |
| REF-COMP | E8 supplied workbook, Platform Providers worksheet: C22/C24/C25, rows 85–100, 110–116, 125 and 158; Inferred and Criteria worksheets; template!C71 | Competitive research only. C99 says Sage has no portal while template!C71 says Yes; J86 contradicts detailed catalogue cells; dashboard/reporting summaries contradict ZeroComa detail. Inferred protocol/status claims and global coverage do not prove Spain operator fitness. Criteria confidence is per provider/section, not every cell. Original vendor links are retained in the workbook; no parity backlog or mandatory requirement follows. |

## Change log

| Date | Change | Evidence/decision source |
|---|---|---|
| 2026-08-05 | Initial Phase 3 discovery PRD created | July 2026 strategy paper; Ley 18/2022; RD 238/2026; official Ministry and EU sources |
| 2026-08-10 | Consolidated the legacy strategic rationale and building-block navigation into the authoritative Phase 3 umbrella; renamed the Confluence topic and aligned it to four capability categories | User-approved Phase 3 information architecture; legacy Confluence pages 837588801 and 855180225 |
| 2026-11-03 | Added the proposed layered capability register, responsibility transfer, minimum proposition, transition terms, CG1–CG7, open conflicts and source references. Mapped former Tier 0/1/2 to Layers 1/2/3; added Layer 4 guardrails. Restored OP20 withdrawal, OP21 fiscal correction, OP22 conditional legal PDF delivery and OP23 secure transport. Moved VA12 to Layer 2 and added CX09 B2G under PO-03; retained the conflicting earlier cross-country text for review. Refreshed E3, BR9, OQ2, D3 and dependency/date wording because the order is published; extended FR21 by reference to PO-01 and scoped the unchanged objective/rollout gate IDs. No FR/NFR/AC ID, journey or risk was deleted. | Reviewed capability framework and corrections; Jiaxin He product-owner clarifications, November 2026; repository source review through 73d0f6c; E6 and REF sources. This replaces the earlier tier-list scope presentation and stale publication-dependent wording, not an approved delivery decision. |
