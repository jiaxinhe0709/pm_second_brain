---
id: PRD-SEI-223
title: Exchange — Interoperability, Routing and Transformation
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-09-22
reviewers: []
related:
  - PRD-SEI-210
  - FP-SEI-001
  - ADR-SEI-001
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-224
  - PRD-SEI-103
  - PRD-SEI-202
  - PRD-SEI-203
  - PRD-SEI-211
  - PRD-SEI-212
  - PRD-SEI-226
  - PRD-SEI-236
  - PRD-SEI-237
  - PRD-SEI-238
  - PRD-SEI-239
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "876576916"
  page_id: "866148656"
  title: Exchange — Interoperability, Routing and Transformation
  layout: two_left_sidebar
  toc: true
---

# Exchange — Interoperability, Routing and Transformation

## Decision summary

Phase 3 must exchange an invoice from a Sage customer to the recipient's authoritative entry point—Sage private platform, another private platform or the public solution—while preserving business meaning, authenticity/integrity evidence, immutable route context and the required public copy.

Routing, transformation, signing and public-copy submission are related but distinct decisions. The platform should establish an immutable exchange plan before the first external mutation, then execute each required leg idempotently and reconcile ambiguous outcomes.

“Sage signing” must never be a generic exchange option. The plan must distinguish a customer/direct signature, an accountant or other authorised delegated signature, a Sage-operated remote-signing service acting for that identified principal/delegate, provider signing/sealing, a Sage operator seal, and Sage workload/transport authentication. PRD-SEI-226 owns the trust-material lifecycle; this PRD freezes and executes the approved purpose-specific choice for each representation.

This PRD is the parent capability contract. It owns shared format governance, representation lineage, transformation, route-aware signing and cross-format controls. Format-specific versions, profiles, extensions, validation artefacts and conformance gates are owned by the child PRDs listed below. Submission and retrieval journeys consume those contracts through PRD-SEI-212 and PRD-SEI-211 respectively.

> **Product principle:** Choose the route from authoritative evidence, transform before the applicable signature/seal, and preserve one traceable identity across every network representation.

## Phase and outcome

| Phase | Exchange capability | Phase 3 implication |
|---|---|---|
| Phase 1 | Submit/retrieve through public solution | Reuse where evidence proves fitness; public remains a valid route and required repository/copy boundary |
| Phase 2 | Route through configured external provider adapters | Reuse routing, adapter, context and resilience patterns |
| **Phase 3** | Operate Sage private-platform exchange and interconnection | Add external ingress, admitted-syntax transformation, trust, direct/public bridging and operator evidence |

### Format portfolio and document ownership

As of 21 September 2026, Article 7.1 of Real Decreto 238/2026 names four structured syntaxes for the Spanish system: CII, UBL, an EDIFACT invoice message and Facturae. The preamble also treats Peppol BIS messages as valid where they use UBL and conform to EN 16931; Peppol BIS is therefore governed as a UBL profile, not a fifth syntax. A transitional PDF readability companion is not an electronic-invoice syntax. Additional syntaxes require a future ministerial order under the third final provision and then a new child profile or an explicit extension of an existing child.

| Document | Ownership | Does not own |
|---|---|---|
| **PRD-SEI-223 (this parent)** | Shared representation model, format registry, transformation policy, semantic preservation, signing order and portfolio activation | Country/profile-specific schemas or implementation-guide detail |
| PRD-SEI-236 — UBL | UBL invoice/credit-note versions, Spanish/EU profiles, validation artefacts and public-copy representation | Generic submission/retrieval orchestration |
| PRD-SEI-237 — CII | UN/CEFACT CII syntax/profile/version and EN 16931 binding | UBL or Facturae rules |
| PRD-SEI-238 — UN/EDIFACT | ISO 9735 syntax, directory/message/subset agreement and EDIFACT mapping controls | Treating EDIFACT as an automatically accepted EN 16931 syntax |
| PRD-SEI-239 — Facturae | Spanish Facturae versions, B2G/FACe use and XAdES profile evidence | General private-platform signature policy |
| PRD-SEI-212 | Creation of an exchange-ready representation and outbound submission | Format-specific rules |
| PRD-SEI-211 | Retrieval, download artefacts and authorised product distribution | Format-specific rules |
| PRD-SEI-226 | Certificate, key and trust lifecycle | Format transformation |

### Product execution hypothesis

The following is discovery input, not a delivery commitment. “External private-platform ISV” means the customer outcome may be supported by the connected platform even when the Sage product has no native format/transformation implementation.

| Product | Native transform/format claim | Private-exchange signing claim | Current ownership hypothesis | Evidence state |
|---|---|---|---|---|
| Sage 50 | No; external private-platform ISV | Yes, certificate-based | Product supplies invoice data; platform owns mapping/transport; signing boundary to confirm | Internal input; validate |
| Sage 200 | Facturae claimed; other transforms external | Yes, certificate-based | Product may create Facturae; platform owns other delivery forms | Internal input; validate |
| Sage Active | To be established | To be established | Shared services preferred | Open |
| X3 | To be established | To be established | Product/platform split to be established | Open |
| Despachos | Facturae claimed; other transforms external | Yes, certificate-based | Product may create Facturae; platform owns other delivery forms | Internal input; validate |

The France Domain Services Document Transformation Service (DTS) is the preferred reuse candidate for shared transformation capability. Stakeholder input confirms it exists and can be reused; the linked CII D22B material describes its UBL-centred architecture and planned/implemented evolution but is not, alone, deployment evidence. Spain must therefore start with a reuse-and-gap assessment, retaining DTS platform capability while replacing or isolating French jurisdictional rule packs.

## Problem and objective

### Problem

A business invoice may be created in one Sage/product format, exchanged in a syntax agreed by trading parties, transformed by an operator, signed or sealed, delivered through a direct private interconnection or the public solution, and copied to the public repository in UBL. Each representation must remain attributable to the same business invoice without losing required content or obscuring which platform performed each action.

Failure risks include:

- routing from stale customer configuration rather than authoritative entry-point evidence;
- sending privately when the recipient must be reached through the public solution;
- transforming after signature and invalidating authenticity/integrity evidence;
- semantic loss between CII, UBL, EDIFACT or Facturae representations;
- duplicate delivery or public copy after a timeout;
- treating successful transport as recipient acceptance;
- allowing direct and public-bridge paths to create competing invoice histories;
- failing to retrieve an invoice deposited in the public solution during interconnection setup;
- exposing partner or country-specific contracts directly to Sage products.

### Objective

Define a product-neutral exchange capability that plans, validates, transforms, signs/seals, submits, receives, acknowledges and reconciles every required exchange leg with stable identities, evidence and operational control.

## Scope and non-goals

### In scope

- Outbound and inbound exchange through Sage, other private platforms and the public solution.
- Recipient entry-point resolution and route decision evidence.
- Admitted syntax/profile negotiation, validation and transformation.
- Advanced signature/seal orchestration and evidence boundaries.
- Required faithful UBL public copy and correlation.
- Direct private interconnection and public-solution bridging.
- Idempotency, duplicate detection, outcome-unknown reconciliation and quarantine.
- Product-neutral API/event capability and operations experience.

### Non-goals

- Final endpoint names, schemas or authentication before official/architecture approval.
- Customer onboarding and route activation; see PRD-SEI-222.
- Full lifecycle/payment business behaviour; see PRD-SEI-224.
- Deciding build/partner/acquisition.
- Supporting proprietary syntax as a launch commitment without approved scope/evidence.
- Tax/legal validation beyond the approved invoice rule packs.
- Recreating provider-specific adapter detail from Phase 2 PRDs.

## Definitions

| Term | Meaning | Not equivalent to |
|---|---|---|
| Business invoice identity | Stable identity of the commercial invoice across representations | One provider's transmission ID |
| Representation | Versioned syntax/profile instance of the invoice | A new commercial invoice |
| Exchange plan | Immutable decision record for required route, transformations, trust and public-copy legs | Current customer route configuration |
| Entry-point evidence | Authoritative observed information used to determine receipt destination | A cached preference without freshness/provenance |
| Direct interconnection | Exchange between qualifying private platforms | A customer-specific ERP API |
| Public bridge | Use of the public solution as the transport/interconnection route | The faithful copy alone |
| Faithful copy | Required UBL copy marked/treated as a copy in the public solution | The recipient-delivered original representation |
| Transport acknowledgement | Evidence that a network accepted a message | Business acceptance of the invoice |
| Transformation provenance | Input/output syntax, mapping/rule version, actor and validation evidence | A generic “converted” flag |
| Outcome unknown | Mutation may have succeeded externally but acknowledgement is absent | Confirmed failure |
| Format | A named electronic-invoice representation family, such as UBL, CII, UN/EDIFACT or Facturae | A version or trading-party profile |
| Syntax version | A released version of the underlying schema/message standard | Proof that Spain or a recipient accepts it |
| Profile / CIUS | A constrained usage specification for a syntax, including business rules | The base syntax alone |
| Extension | Additional agreed content outside or on top of a profile | An ungoverned custom field |
| Transformation mapping | Versioned, directional rules from one representation/profile to another | Display rendering |
| Document Transformation Service (DTS) | Existing France Domain Services capability and local-library pattern for version-aware parsing, validation and CII↔UBL transformation; preferred reuse candidate for Spain | Proof that a French profile/version is accepted on a Spanish route |
| Rendering | Human-readable presentation derived from a representation | The legally exchanged structured artefact |
| Signature profile | Versioned rules for signer, algorithm, certificate, signed object and verification evidence | Possession of a certificate |
| Direct signature | Signature created by the issuer/authorised signatory under the applicable policy | A platform seal or transport credential |
| Delegated signature | Signature created by an explicitly authorised delegate for the represented issuer | A firm role, client relationship or certificate possession alone |
| Sage-managed signing | Protected remote-signing operation orchestrated by Sage for an identified issuer/delegate and authority | A generic Sage service certificate or Sage operator seal |
| Operator seal | Electronic seal whose creator is the named platform legal person | The issuer's/direct or delegated signature unless explicitly approved by Legal |
| Trust-material readiness | Purpose-specific PRD-SEI-226 result for the exact actor, route, profile, environment and time | One global certificate-ready flag |

## Exchange route visual

<!-- confluence-html-macro:start -->
<div class="p3xchg-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3xchg-visual *{box-sizing:border-box}.p3xchg-visual h2{margin:0;color:#172b4d;font-size:18px}.p3xchg-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3xchg-visual svg{display:block;width:1080px;height:520px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3xchg-visual .sage{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3xchg-visual .decision{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3xchg-visual .private{fill:#eae6ff;stroke:#6554c0;stroke-width:1.5}.p3xchg-visual .public{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3xchg-visual .error{fill:#ffebe6;stroke:#ff5630;stroke-width:1.5}.p3xchg-visual .title{fill:#172b4d;font-size:11px;font-weight:700}.p3xchg-visual .copy{fill:#42526e;font-size:9px}.p3xchg-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3xchg-visual .path{fill:none;stroke:#00875a;stroke-width:2}.p3xchg-visual .private-path{fill:none;stroke:#6554c0;stroke-width:1.8}.p3xchg-visual .public-path{fill:none;stroke:#0052cc;stroke-width:1.8}.p3xchg-visual .retry{fill:none;stroke:#de350b;stroke-width:1.5;stroke-dasharray:6 4}.p3xchg-visual .arrow{fill:#00875a}.p3xchg-visual .arrow-p{fill:#6554c0}.p3xchg-visual .arrow-b{fill:#0052cc}.p3xchg-visual .arrow-r{fill:#de350b}.p3xchg-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3xchg-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3xchg-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>One exchange plan, multiple evidenced legs</h2>
  <p class="sub">The recipient route and public-copy duty are planned once. Direct private delivery and public bridging remain traceable to the same invoice identity.</p>
  <svg viewBox="0 0 1080 520" role="img" aria-label="A Sage product creates invoice intent. The shared platform validates and establishes an immutable exchange plan, transforms to the agreed syntax before applying signature or seal, then routes either directly to another private platform, through the public solution as a bridge, or to a Sage recipient. A separate correlated faithful UBL copy is sent to the public solution where required. Ambiguous outcomes enter reconciliation rather than blind retry.">
    <text x="34" y="34" class="label">PRODUCT INTENT</text><text x="235" y="34" class="label">SHARED EXCHANGE CORE</text><text x="710" y="34" class="label">NETWORK LEGS</text>
    <rect x="34" y="82" width="166" height="84" rx="9" class="sage"/><text x="52" y="109" class="title">Invoice intent</text><text x="52" y="130" class="copy">Legal entity • recipient</text><text x="52" y="147" class="copy">canonical business data</text>
    <path d="M200 124 H232" class="path"/><polygon points="232,124 222,118 222,130" class="arrow"/>
    <rect x="234" y="72" width="184" height="104" rx="9" class="sage"/><text x="252" y="99" class="title">Validate and identify</text><text x="252" y="120" class="copy">Business rules • unique identity</text><text x="252" y="138" class="copy">route snapshot inputs</text><text x="252" y="156" class="copy">reject before mutation if invalid</text>
    <path d="M418 124 H450" class="path"/><polygon points="450,124 440,118 440,130" class="arrow"/>
    <rect x="452" y="62" width="206" height="124" rx="9" class="decision"/><text x="470" y="89" class="title">Immutable exchange plan</text><text x="470" y="110" class="copy">Authoritative entry point and route</text><text x="470" y="128" class="copy">syntax/profile and transformation</text><text x="470" y="146" class="copy">signature/seal and public copy</text><text x="470" y="164" class="copy">idempotency and evidence keys</text>
    <path d="M658 124 H698" class="path"/><polygon points="698,124 688,118 688,130" class="arrow"/>
    <rect x="700" y="72" width="166" height="104" rx="9" class="sage"/><text x="718" y="99" class="title">Transform then trust</text><text x="718" y="120" class="copy">Agreed admitted syntax</text><text x="718" y="138" class="copy">semantic validation</text><text x="718" y="156" class="copy">apply signature / seal</text>
    <path d="M866 104 H902 V78" class="private-path"/><polygon points="902,78 896,88 908,88" class="arrow-p"/>
    <rect x="904" y="48" width="142" height="64" rx="8" class="private"/><text x="922" y="74" class="title">Direct private</text><text x="922" y="94" class="copy">Other platform / Sage</text>
    <path d="M866 142 H902 V194" class="public-path"/><polygon points="902,194 896,184 908,184" class="arrow-b"/>
    <rect x="904" y="196" width="142" height="64" rx="8" class="public"/><text x="922" y="222" class="title">Public bridge</text><text x="922" y="242" class="copy">Recipient retrieval route</text>
    <path d="M555 186 V320 H902" class="public-path"/><polygon points="902,320 892,314 892,326" class="arrow-b"/>
    <rect x="904" y="288" width="142" height="64" rx="8" class="public"/><text x="922" y="314" class="title">Faithful UBL copy</text><text x="922" y="334" class="copy">Correlated public record</text>
    <rect x="452" y="286" width="268" height="84" rx="9" class="sage"/><text x="470" y="313" class="title">Persist evidence and lifecycle handoff</text><text x="470" y="334" class="copy">Transport results • external IDs • representations</text><text x="470" y="352" class="copy">route context • status correlation • audit</text>
    <path d="M975 112 V278 H720 V328" class="private-path"/><polygon points="720,328 714,318 726,318" class="arrow-p"/>
    <path d="M975 260 V278" class="public-path"/>
    <path d="M975 352 V400 H720" class="public-path"/><polygon points="720,400 730,394 730,406" class="arrow-b"/>
    <rect x="452" y="392" width="268" height="82" rx="9" class="error"/><text x="470" y="419" class="title">Outcome unknown / conflicting evidence</text><text x="470" y="440" class="copy">Freeze unsafe retry • reconcile each external leg</text><text x="470" y="458" class="copy">resume, quarantine or escalate with redacted evidence</text>
    <path d="M586 370 V384" class="retry"/><polygon points="586,384 580,374 592,374" class="arrow-r"/>
  </svg>
  <div class="notes"><div class="note"><strong>Route and copy differ</strong>The recipient delivery leg and required public copy are independently evidenced.</div><div class="note"><strong>Transform before signing</strong>Every representation records mapping, validation and trust provenance.</div><div class="note"><strong>Reconcile by leg</strong>A successful private delivery does not imply that the public copy succeeded, or vice versa.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors and responsibilities

| Actor | Responsibility |
|---|---|
| Sage ERP/API consumer | Submit canonical invoice intent and consume stable lifecycle outcomes |
| Sage exchange core | Validate, identify, plan, orchestrate, persist context and reconcile |
| Sage private-platform operator | Perform or govern external ingress/egress, transformation, trust and interconnection |
| Sender/recipient platform | Exchange invoice and required statuses using agreed/required syntax |
| Public solution | Public receipt route, bridge and repository/copy services according to regulation/specification |
| Operations/support | Diagnose each exchange leg and perform only safe recovery |
| Security/compliance | Approve protocols, certificates, transformations, evidence and data controls |

## Business scenarios

| ID | Scenario | Expected route/behaviour | Exception/continuity |
|---|---|---|---|
| S1 | Sage sender and Sage private recipient | Internal/operator exchange using the approved representation | Still produce required public copy and evidence |
| S2 | Sage sender to another private platform with direct interconnection | Deliver through direct platform route in agreed syntax | Public copy remains a separate correlated leg |
| S3 | Direct interconnection not yet operational | Deposit/deliver through public solution bridging according to approved rules | Recipient platform must retrieve; history records bridge route |
| S4 | Recipient has no public private entry point | Use public solution as default receipt route | Do not assume a private destination from stale data |
| S5 | Input syntax differs from recipient syntax | Transform before applicable signature and validate semantic preservation | Quarantine on material loss/invalid mapping |
| S6 | Private delivery succeeds but public copy times out | Preserve private success; reconcile copy independently | Do not redeliver the private invoice |
| S7 | Duplicate inbound representation arrives | Resolve by business identity/network identifiers and retain evidence | Do not create a second business invoice |
| S8 | Status/event arrives before invoice persistence completes | Buffer/reconcile by stable identifiers | Preserve event source/order evidence |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Exchange plan is created | Freeze route, syntax/profile, mapping, trust and copy decisions for that exchange attempt | Proposed safety rule |
| BR2 | Recipient private entry point is authoritative and ready | Use the selected private route for eligible traffic | Entry-point authority details open |
| BR3 | No private receipt entry point is identified | Use public solution as default receipt route | RD 238/2026 Article 6 |
| BR4 | Parties have an approved syntax/specification agreement | Use that agreement when supported and evidenced | RD 238/2026 Article 7 |
| BR5 | No bilateral syntax agreement exists | Use the syntax/specifications required for the public solution | RD 238/2026 Article 7 |
| BR6 | Transformation is required between private platforms | Sender-side platform transforms before the invoice is signed for exchange | RD 238/2026 Article 7; legal/technical review required |
| BR7 | Invoice is not emitted through the public solution | Send the required faithful UBL copy simultaneously as defined by the approved specification | RD 238/2026 Article 6; exact transaction semantics open |
| BR8 | Direct interconnection is unavailable during setup | Use the public solution bridge according to the statutory process | RD 238/2026 Article 9 |
| BR9 | One external leg succeeds and another is unknown | Preserve successful evidence and reconcile only the unknown leg | Proposed resilience rule |
| BR10 | Representation changes | Preserve business identity plus input/output syntax, mapping and trust provenance | Proposed audit rule |
| BR11 | Private-platform invoice is signed under Article 7.3 | Use the approved direct or authorised-delegated signer model and preserve who is represented, who signs and who operates the service | RD 238/2026 Article 7.3; implementation profile open |
| BR12 | Sage operates remote signing | Treat Sage as service operator/custodian while preserving the approved customer/delegate as signer; never substitute a workload certificate | PRD-SEI-226 |
| BR13 | Sage/provider operator seal is proposed | Keep it separate from the customer/delegate signature and block substitution unless the applicable route/trust policy has explicit Legal approval | Evidence gate |
| BR14 | Certificate expires, rotates or is revoked | Freeze the exact trust-material version on existing attempts; block unsafe new use and preserve historic validation evidence | PRD-SEI-226 |

## Research and evidence register

| Source | Finding | Confidence/limitation | Requirement impact |
|---|---|---|---|
| [RD 238/2026 Articles 5–7](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295) | Public/private system, entry-point default, four admitted syntaxes, Peppol BIS as a UBL/EN 16931 profile, all-format transformation, advanced signature for private-platform issuance and UBL public copy | Primary regulation; ministerial technical order and exact profiles/specifications still required | Routing, formats, copy and trust |
| RD 238/2026 Articles 8–9 | Direct interconnection, public bridge, invoice/status scope and operational procedure | Primary regulation; detailed interfaces open | Interconnection routing and fallback |
| RD 238/2026 Articles 11–13 | Public UBL boundary, authentication dependency, operator AS2/AS4 and capability requirements | Primary regulation; ministerial-order detail open | Protocol, public adapter and readiness |
| PRD-SEI-103 | Public submission validation, idempotency and evidence patterns | Product intent/implementation fitness unassessed | Reuse candidate via FP-SEI-001 |
| PRD-SEI-202/203 | Route snapshot, adapter boundary, outcome-unknown and reconciliation | Product intent/implementation fitness unassessed | Shared exchange/resilience behaviour |
| Internal format-capability requirements 36–44 | Receive/send/transform, agreed delivery format, exchange signing, UBL/CII/EDIFACT/Facturae, CIUS/extensions and contractually agreed formats | Discovery input; product claims and legal interpretation need owner validation | Parent/child capability split and traceability |
| OASIS UBL specifications | UBL is versioned; UBL 2.5 exists as a 2026 specification | Existence does not prove acceptance by the Spanish public solution | UBL child uses an evidence-gated version registry; no hard-coded 2.5 |
| EU Implementing Decision (EU) 2017/1870 | EN 16931 syntax list references UBL as ISO/IEC 19845:2015 and UN/CEFACT CII XML Schemas 16B | Spanish implementation profiles and later version support still require confirmation | UBL and CII child baselines |
| UNECE UN/CEFACT artefacts | CII and UN/EDIFACT are separately versioned standards; EDIFACT needs directory/message/subset context | Base syntax alone is insufficient for bilateral interoperability | CII and EDIFACT child controls |
| Spanish Facturae portal | Public-administration invoicing uses Facturae 3.2.x and XAdES; portal lists 3.2.2 artefacts | B2B private-platform applicability and exact signature policy remain separate decisions | Facturae child baseline |
| PRD-SEI-226 | Shared certificate, key, signing/sealing and trust lifecycle | Does not decide invoice-format acceptance | Trust readiness and runtime signing dependency |
| [eIDAS Regulation, consolidated](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02014R0910-20240520) | Separates signatures, seals, qualified certificates, trust services, timestamps, validation and preservation services | Exact Spanish route/signature profile still requires approval | Do not collapse signature, seal and custody roles |
| [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.00_20/en_31910201v010400a.pdf) | Defines signature validation procedures and long-term validation evidence concepts | Retention profile and exact signature format remain policy decisions | Runtime validation and durable evidence |
| [France DTS CII 22B initiative](https://confluence.sage.com/spaces/DNBU/pages/833945883) | Existing DTS uses a UBL 2.1 canonical pattern and describes version detection, schema/schematron validation, bidirectional CII transformation and dual-version operation | Stakeholder input confirms reuse direction; page wording does not establish deployed D22B production readiness | Preferred implementation candidate; qualify rather than rebuild |
| [D16B/D22B compatibility and mapping analyses](https://confluence.sage.com/spaces/DNBU/pages/833945892) | Official EN 16931 CII binding remains D16B while France targets D22B; mapping risks concentrate in schema/namespace, cardinality, identifiers, code lists and extensions | France-specific FNFE/AFNOR conclusions are not Spain policy; linked field analysis needs exact-artefact verification | Version-aware registry, semantic-loss tests and country rule-pack separation |
| [French CIUS/EXTENDED-CTC-FR analysis](https://confluence.sage.com/spaces/DNBU/pages/833945896) | Shows how jurisdictional requirements add fields, groups, cardinality and validation rules above the common semantic model | Reusable design pattern only | Isolate jurisdiction/profile packs from shared transformation runtime |

## Proposed conceptual model

| Record | Required information |
|---|---|
| Business invoice | Legal parties, invoice number/series/date, canonical content/version and internal identity |
| Representation | Syntax/profile/version, payload hash, source, transform mapping, validation result and trust evidence |
| Entry-point observation | Recipient, direction/scope, destination, source, observed time, validity/freshness and evidence |
| Exchange plan | Immutable recipient route, legs, representation plan, trust actor, copy duty, rule versions and created time |
| Exchange leg | Type (`PRIVATE_DIRECT`, `PUBLIC_BRIDGE`, `PUBLIC_COPY`, `INTERNAL`), destination, request/idempotency ID and state |
| External evidence | Platform reference, acknowledgement, timestamp, protocol/certificate evidence and redacted diagnostic |
| Reconciliation case | Intended/observed state, safe actions, owner, attempts, result and audit |
| Format profile | Format, syntax version, profile/CIUS, extension set, direction, route, effective period and activation state |
| Transformation mapping | Source/target profiles, mapping version, semantic assertions, loss policy, tests and effective period |
| Signature/seal profile | Route/format, trust mode (`DIRECT_SIGNATURE`, `DELEGATED_SIGNATURE`, `SAGE_MANAGED_SIGNATURE`, `PROVIDER_SIGNATURE_OR_SEAL`, `SAGE_OPERATOR_SEAL`), represented principal, actual signer/delegate or seal creator, service operator/custodian, authority reference, certificate purpose/version, signed object/container, algorithm/policy constraints, timestamp/status/validation/preservation rules and effective period |
| Representation set | Original, canonical, delivery, public-copy and rendering artefacts correlated to one business invoice |

### Proposed exchange-leg states

`PLANNED → VALIDATED → READY_TO_SEND → SUBMITTED → ACKNOWLEDGED → COMPLETED`

Recoverable branches: `REJECTED_CORRECTABLE`, `RETRY_PENDING`, `OUTCOME_UNKNOWN`, `RECONCILING`, `QUARANTINED`, `FAILED_TERMINAL`.

Transport acknowledgement and business lifecycle state remain separate.

## Detailed journeys

### J1 — Outbound direct private exchange

1. Product submits canonical invoice intent with legal entity and recipient.
2. Sage validates business identity and resolves current authoritative entry-point evidence.
3. An immutable exchange plan selects direct private delivery and required public-copy leg.
4. Sage transforms to the agreed admitted syntax, validates semantics, resolves purpose-specific PRD-SEI-226 readiness and applies the approved direct/delegated/Sage-managed/provider signature or explicitly approved seal process to the final bytes.
5. Direct delivery and public copy execute as separately correlated idempotent legs.
6. Evidence and lifecycle handoff are persisted before success is reported.

### J2 — Outbound through public bridge

1. Route resolution finds no direct operational interconnection or the public solution is the applicable route.
2. Exchange plan identifies public bridge/recipient behaviour and UBL representation.
3. Sage validates and submits once using a stable idempotency identity.
4. The receiving platform/customer retrieves through the public route.
5. Sage correlates transport and later lifecycle evidence without creating a duplicate copy leg.

### J3 — Correct a transformation failure

1. Validation identifies unsupported value, mapping loss or profile violation before external mutation.
2. The invoice is rejected to product/user with field-level safe diagnostics and mapping/rule version.
3. The source is corrected or an approved mapping change is versioned.
4. A new representation is generated under the same business invoice with a new attempt identity.
5. The original failed representation remains auditable but is never transmitted.

### J4 — Reconcile a partial/ambiguous outcome

1. Direct private delivery is acknowledged, but public-copy submission times out.
2. Sage records direct success and marks only the copy leg `OUTCOME_UNKNOWN`.
3. Reconciliation queries the public solution using stable correlation/identity.
4. If present, copy succeeds; if absent and resubmission is safe, the same logical copy resumes.
5. The private recipient delivery is never repeated because of copy uncertainty.

### J5 — Inbound direct private exchange

1. A qualifying platform authenticates and submits an admitted signed representation.
2. Sage validates sender platform, transport, signature/integrity, syntax/profile and unique identity.
3. Duplicate detection checks business and external identifiers before product delivery.
4. Sage transforms into canonical form while retaining the original representation/evidence.
5. The invoice is delivered once to the correct legal entity/product and acknowledged according to the approved contract.

### J6 — Inbound retrieved from public bridge

1. Consultation/event trigger identifies an invoice addressed to a Sage private-platform customer.
2. Sage retrieves using an idempotent checkpoint and validates recipient route/effective interval.
3. Original public representation and reference are retained.
4. Canonical invoice is delivered once; checkpoint advances only after durable persistence.
5. Late/direct duplicate is reconciled to the existing business invoice.

## Functional requirements

### Planning and routing

| ID | Requirement |
|---|---|
| FR1 | Resolve recipient route from approved authoritative evidence with source, freshness and scope. |
| FR2 | Create an immutable exchange plan before any external mutation. |
| FR3 | Record the exact route/rule version and effective observation used for the decision. |
| FR4 | Support direct private, public bridge, public copy and internal Sage legs without merging their outcomes. |
| FR5 | Refuse or quarantine exchange when no eligible, explainable route exists. |

### Identity, validation and transformation

| ID | Requirement |
|---|---|
| FR6 | Assign/preserve a stable business invoice identity and the applicable statutory unique-code components. |
| FR7 | Validate canonical content and every external representation against versioned syntax/profile/business rules. |
| FR8 | Transform between activated admitted syntaxes without material semantic loss and with recorded provenance. |
| FR9 | Apply the approved signature/seal only after the required transformation for the selected representation. |
| FR10 | Retain original received representation and evidence according to approved retention rules. |
| FR11 | Prevent a syntax/profile from activation until conformance and semantic-preservation tests pass. |

### Outbound and public copy

| ID | Requirement |
|---|---|
| FR12 | Execute every mutating exchange leg with a stable logical idempotency/correlation identity. |
| FR13 | Generate and submit the faithful UBL public copy where required, marked and correlated as a copy. |
| FR14 | Persist internal invoice/plan state before external mutation or provide a proven recovery mechanism for external-first success. |
| FR15 | Treat each leg's acknowledgement, rejection and unknown outcome independently. |
| FR16 | Never repeat a completed recipient-delivery leg solely because another leg is incomplete. |

### Inbound and interconnection

| ID | Requirement |
|---|---|
| FR17 | Authenticate and authorise inbound platform traffic by operator, environment and capability. |
| FR18 | Validate transport, signature/integrity, syntax/profile, recipient and unique identity before product delivery. |
| FR19 | Deduplicate direct, retried and public-bridge representations to one business invoice while retaining all source evidence. |
| FR20 | Deliver an accepted inbound invoice durably to the correct legal entity/product exactly once at the business level. |
| FR21 | Support the approved interconnection request/test/activation and public-bridge transition defined by PRD-SEI-221. |

### Resilience and operations

| ID | Requirement |
|---|---|
| FR22 | Classify operations as safe retry, idempotent resume, reconcile-first or manual-only. |
| FR23 | Reconcile `OUTCOME_UNKNOWN` against the relevant external leg before retransmission. |
| FR24 | Quarantine invalid, untrusted, conflicting or unrouteable inbound content with redacted operational evidence. |
| FR25 | Expose intended/observed state, correlation, representation, external reference, safe action and owner per leg. |
| FR26 | Preserve a complete audit chain from product intent through every representation, route leg and outcome. |

### Format portfolio and representation governance

| ID | Requirement |
|---|---|
| FR27 | Maintain a governed registry of formats, syntax versions, profiles/CIUS, extensions, directions, routes, products, providers, effective periods and activation state. |
| FR28 | Evaluate create, receive, validate, transform, sign, submit, retrieve, download and render capabilities independently; support for one operation must not imply support for another. |
| FR29 | Select the agreed delivery representation from regulation, recipient capability and evidenced trading-party agreement, with deterministic precedence and decision evidence. |
| FR30 | Preserve and correlate the source/original, canonical, delivery, public-copy and human-readable representations required for the route. |
| FR31 | Demonstrate semantic preservation for every activated transformation with positive, negative, boundary and round-trip or invariant tests appropriate to the mapping. |
| FR32 | Complete transformation and target-profile validation before applying the signature or seal required for that delivery representation. |
| FR33 | For invoices issued through a private platform, require the advanced electronic signature mandated by RD 238/2026 Article 7.3; resolve exact signature policy, format/profile, legal subject, direct/delegated signer role and effective date through PRD-SEI-226, and never treat certificate possession alone as authority. |
| FR34 | Prevent activation of an unapproved format/profile/version, mapping, extension or signature combination. |
| FR35 | Make authorised original, canonical and human-readable artefacts available to retrieval/download consumers with content type, profile/version, hash and provenance. |
| FR36 | Require explicit contractual and technical evidence before activating a CIUS extension or additional bilateral format, including validation and fallback behaviour. |
| FR37 | Require each additional format to have an owned child profile, conformance corpus, supported-operation matrix and lifecycle policy before production activation. |
| FR38 | Expose whether an operation is performed natively by the Sage product, by a shared Sage service or by a connected private-platform provider. |
| FR39 | Support coexistence and controlled migration between format/profile versions without silently rewriting stored or in-flight representations. |
| FR40 | Treat Peppol BIS as a governed UBL/EN 16931 profile, not a fifth syntax, and activate only the exact BIS version and route after conformance evidence. |
| FR41 | Distinguish any transition-period PDF readability companion from the authoritative structured invoice and never submit it as the public faithful copy. |
| FR42 | Add a new syntax only after the applicable ministerial order, open specifications, cross-format receive/transform evidence and an owned child profile are recorded. |
| FR43 | Use the existing DTS as the preferred shared transformation implementation where a recorded capability assessment proves it meets the selected Spain product, route, format and operational contract. |
| FR44 | Version and deploy the transformation runtime, syntax/schema artefacts, directional mappings and jurisdiction/profile validation packs as independently identifiable components. |
| FR45 | Prevent French FNFE, AFNOR and EXTENDED-CTC-FR rules from becoming Spain defaults; activate only the authoritative rule pack selected by the immutable exchange plan. |
| FR46 | Before Spain activation, qualify reused DTS mappings with Spanish positive, negative, boundary, semantic-loss, version-coexistence and rollback tests and retain the exact DTS/mapping/rule-pack evidence. |

### Signature, seal and certificate execution

| ID | Requirement |
|---|---|
| FR47 | Every exchange plan must select a purpose-specific trust mode and PRD-SEI-226 readiness result; `Sage certificate`, `certificate ready` or `signed by platform` is insufficient. |
| FR48 | For direct or delegated signature, the plan must identify the represented issuer, actual authorised signer/delegate, authority reference, service operator/custodian, certificate/trust-material version and exact signed object. |
| FR49 | Sage-managed signing must preserve the customer/delegate signer model while recording Sage's remote-signing service role and protected operation reference; a Sage workload or transport certificate must never be substituted. |
| FR50 | Sage/operator sealing must name the seal creator and use a distinct policy/readiness result; it must not satisfy Article 7.3 delegated-signature execution unless Legal approves that exact route and model. |
| FR51 | Before signing/sealing, the runtime must recheck purpose, owner/subject, authority, environment, validity, revocation/status freshness, algorithm/profile and representation hash under the frozen policy. |
| FR52 | The runtime must block new use of expired, revoked, compromised, suspended, wrong-purpose, wrong-owner, wrong-environment or validation-unknown trust material without silently falling back to another signer, certificate or seal. |
| FR53 | Each signed/sealed representation must retain signed bytes/hash, signature/seal, public certificate chain, signer/seal creator and represented-principal evidence, authority/policy snapshot, trusted time/status evidence, validation conclusion and preservation provenance required by PRD-SEI-226. |
| FR54 | A signing/sealing timeout after possible execution must enter `OUTCOME_UNKNOWN` and reconcile by immutable operation/reference before retry; a new signature or differently signed representation must not be created blindly. |

### Source requirement traceability

| Source ref | Source capability | Parent requirement | Child/consumer |
|---|---|---|---|
| 36 | Receive, send and transform while preserving authenticity/integrity | FR27–FR35 | All format children; PRD-SEI-211/212/226 |
| 37 | Transform to agreed delivery format | FR29–FR32 | All format children |
| 38 | Sign private-platform exchange representation | FR32–FR34 | Confirmed high-level duty in RD 238/2026 Article 7.3; PRD-SEI-226 plus applicable format child owns implementation |
| 39 | UBL | FR27, FR34, FR37, FR39 | PRD-SEI-236 |
| 40 | CII 16B/SCRDM-CII | FR27, FR34, FR37, FR39 | PRD-SEI-237 |
| 41 | UN/EDIFACT / ISO 9735 | FR27, FR34, FR37, FR39 | PRD-SEI-238 |
| 42 | Facturae | FR27, FR32–FR34, FR37, FR39 | PRD-SEI-239 |
| 43 | CIUS and agreed extensions | FR27, FR29, FR34, FR36 | Relevant format child |
| 44 | Other contractually agreed formats | FR27, FR29, FR34, FR36–FR37 | New child PRD before activation |

## Conceptual API/event capabilities

Names and payloads are proposed boundaries, not approved endpoints.

| Capability | Minimum contract behaviour |
|---|---|
| Submit invoice intent | Accept canonical identity/content plus legal entity; return stable request/invoice identity and asynchronous state |
| Get exchange plan/outcome | Return route snapshot, representation/leg states and customer-safe failure information |
| Receive invoice event | Notify product after durable canonical persistence with source network context |
| Retrieve original/evidence | Authorised retrieval of original representation and redacted exchange evidence |
| Correct/resubmit | Create a new attempt/representation without changing the original failed evidence |
| Reconcile operation | Operations-only action to compare intended/observed external state without blind mutation |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Use approved AS2/AS4 and/or official public-solution protocols according to the activated boundary. |
| NFR2 | Protect signing/sealing keys and credentials using approved custody, rotation, revocation and separation of duties. |
| NFR3 | Derive throughput, payload, latency, queue and recovery targets from an approved volume/format model. |
| NFR4 | Apply backpressure and fair scheduling so one tenant/platform cannot starve others. |
| NFR5 | Encrypt invoice content/evidence and minimise sensitive data in logs, metrics and support artefacts. |
| NFR6 | Isolate tenant, operator, environment and certificate contexts. |
| NFR7 | Version schemas, profiles, mappings and route rules with backward/rollout controls. |
| NFR8 | Provide end-to-end correlation and immutable audit sufficient to reconstruct each exchange plan and leg. |
| NFR9 | Make customer/product status accessible and distinguish transport, validation and business outcomes. |

## Failure and recovery matrix

| Failure | Required response |
|---|---|
| Stale/missing entry-point evidence | Refresh or stop as unrouteable; do not guess private destination |
| Unsupported syntax/profile | Reject before mutation with supported alternatives |
| Semantic transformation loss | Quarantine and require corrected mapping/source |
| Signature/certificate invalid | Reject/quarantine; never deliver as trusted |
| Trust material expires/revokes after planning but before signing | Stop the affected operation, preserve the frozen plan and require re-plan/re-authorisation under an audited policy |
| Sage workload/transport certificate selected for invoice signature | Reject as wrong purpose and require an approved direct/delegated/seal profile |
| Sage operator seal selected where delegated signature is required | Block until the exact Legal/trust-policy gate is approved; do not relabel the seal |
| Signing request times out after possible key use | Record outcome unknown and reconcile the immutable signing-operation reference before any retry |
| Recipient validation rejection | Preserve rejection evidence; allow corrected new attempt according to business rules |
| Throttle/transient outage before mutation | Backoff/resume safely according to contract |
| Timeout after mutation | Mark only affected leg outcome unknown; reconcile first |
| Internal persistence failure after external success | Recover via correlation and external evidence; prevent duplicate leg |
| Duplicate direct/public inbound | Merge to one business invoice; retain all delivery evidence |
| Out-of-order status before invoice | Buffer/reconcile; never invent invoice state |
| Direct interconnection unavailable | Apply approved public bridge without rewriting route history |
| Conflicting representations for same identity | Quarantine, preserve both and escalate |

## Acceptance criteria

- Given a recipient with an observed-ready private entry point and direct interconnection, when a valid invoice is submitted, then the exchange plan records direct delivery plus any required public-copy leg before transmission.
- Given no published private entry point, when route resolution runs, then the public solution is selected and the decision source/time is auditable.
- Given transformation from EDIFACT to UBL, when conformance runs, then required semantic content, business identity and provenance are preserved before signing.
- Given direct delivery succeeds and the public copy is outcome-unknown, when reconciliation runs, then the copy is resolved independently and direct delivery is not repeated.
- Given the same invoice arrives directly and through public bridge, when deduplication runs, then one business invoice is delivered while both network references remain auditable.
- Given a certificate is invalid, when inbound validation runs, then the invoice is quarantined and no product delivery or trusted acknowledgement occurs.
- Given interconnection is not operational, when the approved bridge applies, then exchange through the public solution remains traceable to the same invoice identity and route decision.
- Given a product can create a format but cannot transform it, when route planning runs, then the selected external/shared transformation owner is explicit and the product is not shown as natively capable.
- Given a syntax version exists but has not been accepted by the Spanish profile or recipient, when activation is attempted, then the format registry blocks it and reports the missing evidence gate.
- Given a transformation changes the delivery representation, when signing is requested, then target-profile validation completes first and the signature references the final exchanged bytes.
- Given an authorised user downloads an invoice, when multiple representations exist, then the response identifies original/canonical/rendered artefacts, hashes, format/profile versions and provenance without presenting a rendering as the exchanged original.
- Given a contractually agreed extension, when it is activated, then the agreement, validation artefacts, mapping behaviour and fallback are versioned and auditable.
- Given a Peppol BIS invoice, when the format registry evaluates it, then it is classified as an exact UBL/EN 16931 profile rather than a separate syntax.
- Given a transition-period PDF companion, when representations are stored or downloaded, then the PDF is labelled as a readability companion and the structured invoice remains authoritative.
- Given a proposed fifth syntax, when no ministerial order has admitted it, then production activation is blocked even if a bilateral provider can technically process it.
- Given Sage-managed signing, when a private-platform representation is signed, then evidence identifies the customer principal, approved signer/delegate, Sage service role, authority snapshot, trust-material version and exact signed bytes separately.
- Given a valid Sage workload or mTLS certificate, when it is selected as the invoice-signing credential, then policy resolution rejects it as wrong purpose.
- Given a Sage operator seal is technically available, when the route requires a direct/delegated signature and no explicit Legal approval permits substitution, then exchange remains blocked and the UI does not label the seal as the customer's signature.
- Given a certificate expires after an invoice was validly signed, when the invoice is retrieved or revalidated, then historic validity is evaluated from retained signing-time evidence rather than failed solely because the certificate is now expired.
- Given a signing request times out after possible execution, when recovery runs, then the original signing reference is reconciled and no second signature is created blindly.

## Measures

| Measure | Purpose | Owner |
|---|---|---|
| Exchange success by route/leg/syntax | Reliability and coverage | Product/operations |
| Transformation rejection and semantic-loss cases | Mapping quality | Engineering/local compliance |
| Duplicate rate and dedupe conflicts | Identity quality | Engineering |
| Outcome-unknown count/age by external leg | Reconciliation health | Operations |
| Route-resolution failures/stale observations | Entry-point health | Platform operations |
| Public-copy completeness/correlation | Regulatory evidence | Compliance/operations |
| End-to-end and queue latency percentiles | Capacity/customer experience | Engineering/product |

## Rollout gates

| Gate | Requirement |
|---|---|
| Discovery | Official profiles, public contract, entry-point authority and launch syntax/route scope confirmed |
| Design | Exchange plan, identity, trust, transformation, adapter and evidence boundaries approved |
| Internal conformance | Positive, negative, duplicate, timeout, persistence and semantic-loss corpus passes |
| DTS reuse qualification | Deployed capability/build, ownership, Spain connectivity, D16B/D22B/UBL coverage, country-rule isolation, operational support and gap backlog are evidenced |
| External conformance | Public and at least one counterparty platform validate each launch route/syntax |
| Pilot | PRD-SEI-221 controls, monitoring, operations and bridge/fallback criteria approved |
| Production | Capacity, BCP, certificate rotation, reconciliation and version rollout tests pass |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| One invoice becomes multiple business records | Stable identity, representation/leg model and cross-route dedupe |
| Transformation corrupts business meaning | Versioned mappings, semantic comparison and quarantine |
| Signature applied at wrong point | Exchange-plan trust sequence and conformance tests |
| Public copy and delivery become coupled retries | Independent leg state and reconciliation |
| Generic “Sage certificate/signature” hides the legal actor | Purpose-specific modes, explicit represented principal/signer/seal creator and PRD-SEI-226 policy |
| Certificate expiry breaks future exchange or historic proof | Dependency monitoring, runtime recheck, frozen trust versions and retained validation/preservation evidence |
| Stale directory data misroutes invoices | Source/freshness evidence, refresh and no-guess rule |
| Partner adapter leaks into Sage products | Product-neutral capability contract and controlled wrapper |
| Protocol/certificate operations underestimated | PRD-SEI-221 security and readiness controls |
| French validation policy leaks into Spanish exchange | Separate runtime/mapping/rule-pack versions, exchange-plan selection and Spain-specific conformance tests |
| DTS is assumed production-ready from design documentation alone | Verify deployed build, service boundary, ownership, capacity and operations before committing the Spain delivery plan |

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Hypothesis |
|---|---|---|---|---|
| What is the authoritative entry-point query and freshness model? | Route correctness | Local technical/regulatory team | Design/external test | Record source/freshness and refresh before plan |
| Which syntax profiles and mapping rules are launch scope? | Transformation/test effort | Local compliance/product | Design | Minimum legally required scope, subject to evidence |
| What exactly makes the public UBL copy “faithful”? | Mapping/evidence | Local legal/technical team | Conformance | Semantic equivalence plus required marking/reference |
| What are official idempotency/query capabilities for the public solution? | Unknown-outcome safety | Public technical team | Pilot | Reconcile-first wrapper required |
| How is bilateral syntax agreement discovered and evidenced? | Route/transform decision | Legal/product/operator | Design | Explicit trading agreement record |
| Who signs: issuer, delegated operator or platform? | Trust model and transform order | Legal/security/operator | Design | Support approved modes with explicit evidence |
| Can direct and bridge deliveries coexist during interconnection cutover? | Duplicate/reachability risk | Local/operator | External test | Dedupe and effective intervals required |
| Which statuses must interconnection exchange? | Boundary with PRD-SEI-224 | Local team | Lifecycle design | Article 10 minimum plus approved extensions |
| Which Spanish authority/profile accepts which UBL versions, including UBL 2.5? | Prevent unsupported public submissions | Local technical/regulatory team | UBL activation | Keep version configurable until evidenced |
| Which technical advanced-signature profile and direct/delegated signer evidence implement Article 7.3 for each syntax/route? | Trust and delegated-authority design | Legal/security | Design | The duty is confirmed; exact implementation remains an evidence gate |
| Is a qualified signature required for B2G invoices above €5,000, and in which route/profile? | Prevent incorrect Facturae policy | Legal/local compliance | Facturae activation | Confirm against current official policy |
| Which Business Identity capability will own advanced signatures, hashes and evidence storage? | Avoid duplicate key/signing services | Business Identity owner (Sam Reid) | Architecture | PRD-SEI-226 remains lifecycle boundary |
| Does the proposed Sage capability perform remote signing for the named customer/delegate, apply a Sage operator seal, or offer both as separately contracted services? | Determines signer identity, custody, liability and evidence wording | Business Identity owner / Legal / Security | Trust architecture | Treat as separate capabilities until approved |
| Which certificate classes, expiry horizons, renewal owners and rotation-overlap rules apply to each route and signing mode? | Prevents outage and unsafe generic thresholds | Security/operations/provider owners | Production readiness | PRD-SEI-226 controls per-class policy |
| What examples and legal evidence support the proposed signature requirements? | Conformance and audit defensibility | Local SME (Ronald) / legal | Design | Capture as evidence before approval |
| For each Sage product, which operations are native, shared-service or provider-owned? | Scope, UX and support ownership | Product owners | Delivery planning | Validate the product execution hypothesis |
| Which internal Confluence UBL pages remain current and can be exported into Git evidence? | Creation/submission/download alignment | Product owner | UBL child review | Pages are linked but their live bodies were unavailable during this revision |
| Which DTS build and deployment boundary are production-ready for reuse by Spain, and who owns its roadmap and operations? | Determines whether reuse is a library, shared service or product integration | DTS/Domain Services owner | Architecture and delivery plan | Reuse DTS; extend only evidenced gaps |
| Can the DTS UBL 2.1 canonical model preserve all Spanish route/profile semantics, public-copy requirements and trust boundaries? | A canonical-model gap can create silent loss or invalid signatures | Architecture/local compliance | Mapping activation | Retain the pattern, prove invariants per mapping |
| How are France FNFE/AFNOR packs isolated from Spain and route-specific rule packs in build, configuration and evidence? | Prevents jurisdictional policy contamination | DTS engineering/security | Spain production readiness | Independently version runtime, schema, mapping and rule packs |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 interoperability, routing and transformation PRD | PRD-SEI-210, Phase 1/2 foundations and RD 238/2026 |
| 2026-09-21 | Version 2 | Established parent/child format governance, operation-level capability, product ownership hypotheses, requirements 36–44 traceability and evidence-gated signing/version rules; verified the four-format set, Peppol BIS classification, transitional PDF distinction and future-syntax mechanism | Internal format-capability input; RD 238/2026; OASIS, EU, UNECE and Facturae official sources; PRD-SEI-226 |
| 2026-09-21 | Version 3 | Set France DTS as the preferred reuse candidate and added Spain qualification, country-rule isolation, versioned evidence and operational readiness gates | Stakeholder direction; France DTS/CII D16B-D22B/FNFE Confluence evidence |
| 2026-09-22 | Version 4 | Separated direct, delegated, Sage-managed, provider and operator-seal execution; added purpose-specific certificate checks, expiry/revocation blocking, signing outcome reconciliation and historic validation evidence | Stakeholder direction; PRD-SEI-226; RD 238/2026 Article 7.3; eIDAS; ETSI EN 319 102-1 |
