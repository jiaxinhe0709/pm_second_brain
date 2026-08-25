---
id: PRD-SEI-101
title: Phase 1 — Public Platform Onboarding
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-25
updated: 2026-08-25
reviewers: []
related:
  - PRD-SEI-104
  - PRD-SEI-105
  - PRD-SEI-106
  - PRD-SEI-107
  - PRD-SEI-108
  - PRD-SEI-211
  - PRD-SEI-212
  - PRD-SEI-213
  - PRD-SEI-214
  - PRD-SEI-215
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-231
  - PRD-SEI-233
  - PRD-SEI-235
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: ""
  page_id: "837610648"
  title: Public Platform - Onboarding
  layout: two_left_sidebar
  toc: true
---

# Phase 1 — Public Platform Onboarding

## Decision summary

Phase 1 onboarding prepares a Spanish business or professional to use Sage capabilities that interact with the public e-invoicing solution. It establishes the Sage access context, legal subject, Spanish tax identity, transaction-scope facts, operation-specific authority, requested capabilities, environment and evidence needed to decide whether the customer is ready.

Onboarding does **not** by itself prove that an invoice is compliant, delivered or reported. It produces a versioned readiness decision that later document, delivery and reporting operations consume.

The Phase 1 completion state is `READY_FOR_PUBLIC_SOLUTION` or `READY_WITH_LIMITATIONS`, not `REGISTERED_FOR_PUBLIC_PLATFORM`, unless an official external registration contract and authoritative acknowledgement are subsequently evidenced. Royal Decree 238/2026 makes the public solution the default when no private receipt platform has been expressly agreed, but leaves its detailed identification, authentication and representation mechanisms to a ministerial order.

> **Product principle:** Identify the right subject, prove the right authority, enable only the evidenced capabilities, and retain why readiness was granted.

This document is a discovery and consultation contract. Proposed entities, states and client operations are not approved physical architecture or evidence of an available AEAT API.

## Source consolidation overview

This PRD creates the previously missing canonical Git source for the stable Confluence topic `837610648`. It consolidates the useful content from the existing parent and five child pages without treating their draft endpoints, certificate assumptions, dates, limits or status mappings as approved facts.

| Existing page | Detail preserved here | Material correction |
|---|---|---|
| [Public Platform — Onboarding](https://confluence.sage.com/spaces/DNBU/pages/837610648/Public+Platform+-+Onboarding) | Phase 1 boundary, central onboarding capability, business/accountant personas, preflight and readiness | Public use is not an exclusive universal network; VeriFactu is separate; no registration handshake is assumed |
| [Accountant & Single Client](https://confluence.sage.com/spaces/DNBU/pages/848078252/Accountant+Single+Client) | Direct and portfolio pathways, asynchronous bulk processing, per-client isolation | A shared credential or accountant role does not prove portfolio-wide authority; send/receive asymmetry remains an evidence question |
| [Environment Routing — TEST vs PRO](https://confluence.sage.com/spaces/DNBU/pages/848078351/Environment+Routing+TEST+vs+PRO) | Environment separation, non-production testing and production gates | Environment is not selected by an untrusted header with a silent default; official sandbox behaviour remains unconfirmed |
| [NIF/NIE Verification & Lookup API — DRAFT](https://confluence.sage.com/spaces/DNBU/pages/855187086/NIF+NIE+Verification+Lookup+API+-DRAFT) | Local validation, census verification and direct/batch use cases | NIF is the umbrella identity; NIE generally serves as NIF for a foreign natural person; census matching is not e-invoicing eligibility |
| [Retry & Error Handling Specs](https://confluence.sage.com/spaces/DNBU/pages/848078012/Retry+Error+Handling+Specs+Phase+1+Public+Platform+Onboarding) | Error categories, correlation, partial outcomes and recovery | Retry values and external errors must come from official contracts; ambiguous mutations require reconciliation |
| [Seller NIF vs Buyer NIF/NIE](https://confluence.sage.com/spaces/DNBU/pages/837610770/Seller+NIF+vs+Buyer+NIF+NIE) | Supplier/recipient identity roles and invoice-field intent | Regex is not complete validation; NIE is not a SIRET-like establishment ID; invoice identity is separate from routing |

No detail in those pages is approved solely because it is retained as an input here. Their Confluence history remains available while this PRD becomes the proposed canonical source for the parent topic.

## Outcome, phase and future direction

### Phase 1 outcome

A direct customer or delegated accountant can establish one or many independently controlled customer profiles and obtain an explainable readiness result for each requested public-solution capability.

| Capability | Phase 1 | Later phase or owning PRD |
|---|---|---|
| Legal-subject and Spanish tax-identity capture | In scope | Shared country model in PRD-SEI-231 |
| Transaction-scope facts and applicability preconditions | In scope | Per-transaction decision in PRD-SEI-235 |
| Direct customer onboarding | In scope | — |
| Accountant portfolio intake | In scope | — |
| Per-client, per-capability authority evaluation | In scope, subject to Spain evidence | Shared authority model in PRD-SEI-231 |
| Local NIF structural/check-character validation | In scope | Validator implementation requires approved rules/tests |
| AEAT census identity-quality check | Proposed, gated on approved access and service contract | Provider specification if integration is approved |
| Public-solution access/readiness evidence | In scope conceptually | Technical binding requires ministerial order/provider artefacts |
| Public invoice submission | Out of scope | PRD-SEI-212 |
| Public invoice consultation/retrieval | Out of scope | PRD-SEI-211 |
| Invoice rejection and payment reporting | Out of scope | PRD-SEI-224 |
| Private-platform connection, publication or switching | Out of scope | PRD-SEI-213, PRD-SEI-214 and PRD-SEI-222 |
| Generic resilience and reconciliation platform | Reused, not redefined | PRD-SEI-215 and PRD-SEI-225 |
| VeriFactu/RRSIF configuration or record submission | Out of scope | Separate fiscal-recording capability |

### Future direction

The onboarding engine should be reusable across public and private routes, but Phase 1 must not make private-platform configuration a mandatory step. Later phases may reuse the same legal subject, identifier, authority, credential reference, environment and evidence records while adding independently governed connections and routes.

## Compliance relationship

Onboarding prepares a reusable compliance context; it does not collapse the compliance outcomes into one status.

| Outcome | What onboarding must establish | What later execution must prove |
|---|---|---|
| Document compliance | Correct legal subjects, identifier roles, applicable policy/profile and permitted issuing actor | Structured representation passed the applicable semantic, syntax and business validation |
| Delivery compliance | Authorised sender/receiver capabilities and eligible public-route context | Intended recipient was resolved and the required destination acknowledged delivery |
| Reporting compliance | Authorised reporting actor and applicable status/payment duties | Required authority data was accepted or reconciled within the applicable deadline |
| Evidence compliance | Policy, identity, authority, environment and readiness decision are versioned | Each execution result and acknowledgement is bound to its immutable context |

## Definitions and boundaries

| Term | Meaning in this PRD | Must not be confused with |
|---|---|---|
| Onboarding | Establishing the customer context and readiness for named capabilities | Issuing, delivering, receiving or reporting an invoice |
| Public solution | The public e-invoicing solution managed by AEAT under Royal Decree 238/2026 | VeriFactu, SII, FACe or every AEAT electronic service |
| Legal subject | The business, professional or other person/entity bearing the relevant rights and obligations | Sage tenant, workspace, user or raw NIF value |
| NIF | Spanish tax-identification number and umbrella identity role | A single subject type or universal routing address |
| DNI | Identity document number that generally serves as NIF for a Spanish natural person | Separate business-establishment number |
| NIE | Foreigner identity number that generally serves as NIF for a foreign natural person | A legal-entity identifier, establishment identifier or SIRET equivalent |
| Entity NIF | NIF assigned to a legal person or entity | Historic `CIF` terminology or a natural-person document type |
| Establishment/presence | Seat, fixed establishment, branch/site, domicile or residence fact relevant to later applicability | A NIF/NIE-derived sub-identifier |
| Census verification | AEAT identity-data matching for a NIF and name/business name | Proof of mandate scope, trading permission, route or e-invoicing eligibility |
| Authentication | Evidence establishing who is accessing a service | Authority to act for a client or capability |
| Delegated authority | Effective evidence permitting a delegate to perform named operations for a principal | Accountant role, API key, certificate possession or portfolio membership |
| Credential reference | Reference to a protected authentication/signing credential and its custodian | The delegated-authority grant itself |
| Channel decision | Recorded use/default/combination of public and private routes | Technical connection or invoice-level routing result |
| Readiness | Sage decision that required onboarding controls passed for named capabilities | External registration, delivery success or legal compliance of all future invoices |
| Environment | Isolated test or production execution boundary | A request field that callers may freely switch |

## Actors and responsibilities

| Actor | Need and responsibility |
|---|---|
| Business owner or authorised administrator | Identify the correct legal subject, supply evidence, request capabilities and correct failures |
| Sole trader/autónomo | Complete the same controls with heightened personal-data protection for DNI/NIE-derived identity |
| Accountant or asesoría user | Onboard only linked clients and request only capabilities supported by effective authority |
| Accountant-firm administrator | Manage firm users and client relationships without granting statutory authority by implication |
| Sage ERP/API consumer | Submit stable onboarding commands, display per-capability results and avoid inventing legal conclusions |
| Onboarding service | Orchestrate validation, authority, verification, readiness and evidence without executing invoices |
| Identity/authority service | Maintain scheme-qualified identities, authority grants and historical snapshots |
| Country-policy owner | Version scope, identifier, authority and evidence rules; resolve regulatory uncertainty |
| Security/privacy | Approve credential custody, personal-data handling, access controls and retention |
| Operations/support | Reconcile pending/unknown states, explain failures and recover only safe operations |
| AEAT/public solution | External authority/service whose confirmed contracts constrain verification and readiness |

## Onboarding control visual

<!-- confluence-html-macro:start -->
<div class="esponb-flow" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .esponb-flow *{box-sizing:border-box}.esponb-flow h2{margin:0;color:#172b4d;font-size:18px}.esponb-flow .sub{margin:6px 0 15px;color:#6b778c;font-size:12px}.esponb-flow svg{display:block;width:1120px;height:510px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.esponb-flow .node{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.esponb-flow .gate{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.esponb-flow .fail{fill:#ffebe6;stroke:#ff5630;stroke-width:1.6}.esponb-flow .optional{fill:#f4f5f7;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:7 5}.esponb-flow .done{fill:#dff7eb;stroke:#00875a;stroke-width:2}.esponb-flow .title{fill:#172b4d;font-size:11px;font-weight:700}.esponb-flow .copy{fill:#42526e;font-size:9px}.esponb-flow .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.07em}.esponb-flow .path{fill:none;stroke:#00875a;stroke-width:2}.esponb-flow .retry{fill:none;stroke:#de350b;stroke-width:1.7;stroke-dasharray:6 4}.esponb-flow .pending{fill:none;stroke:#ff991f;stroke-width:1.7;stroke-dasharray:6 4}.esponb-flow .arrow{fill:#00875a}.esponb-flow .arrow-red{fill:#de350b}.esponb-flow .arrow-amber{fill:#ff991f}.esponb-flow .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1120px;margin-top:12px}.esponb-flow .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.esponb-flow .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Two intake modes, one evidence-led readiness decision</h2>
  <p class="sub">Direct and accountant pathways differ in orchestration only. Every legal subject passes the same identity, scope, authority and capability controls.</p>
  <svg viewBox="0 0 1120 510" role="img" aria-label="Direct customers and accountant portfolio batches create isolated onboarding cases. Each case passes access-context, identity and scope validation, operation-specific authority, capability and environment checks, and confirmed external checks when available. Correctable failures return for correction, ambiguous external outcomes wait for reconciliation, and successful cases become ready or ready with limitations with immutable evidence.">
    <text x="28" y="32" class="label">INTAKE</text><text x="258" y="32" class="label">SHARED CONTROLS</text><text x="844" y="32" class="label">DECISION AND EVIDENCE</text>
    <rect x="28" y="72" width="188" height="76" rx="9" class="node"/><text x="46" y="99" class="title">Direct customer</text><text x="46" y="120" class="copy">One legal subject / workspace</text><text x="46" y="136" class="copy">Immediate structural feedback</text>
    <rect x="28" y="205" width="188" height="76" rx="9" class="node"/><text x="46" y="232" class="title">Accountant portfolio</text><text x="46" y="253" class="copy">Asynchronous batch receipt</text><text x="46" y="269" class="copy">Independent client work items</text>
    <path d="M216 110 H256" class="path"/><polygon points="256,110 246,104 246,116" class="arrow"/><path d="M216 243 H236 V110 H256" class="path"/><polygon points="256,110 246,104 246,116" class="arrow"/>
    <rect x="258" y="72" width="174" height="76" rx="9" class="node"/><text x="276" y="99" class="title">Context and identity</text><text x="276" y="120" class="copy">Tenant • subject • NIF role</text><text x="276" y="136" class="copy">presence and verification</text>
    <path d="M432 110 H464" class="path"/><polygon points="464,110 454,104 454,116" class="arrow"/>
    <rect x="466" y="72" width="174" height="76" rx="9" class="node"/><text x="484" y="99" class="title">Scope and authority</text><text x="484" y="120" class="copy">Policy • principal • delegate</text><text x="484" y="136" class="copy">capability • validity • evidence</text>
    <path d="M640 110 H672" class="path"/><polygon points="672,110 662,104 662,116" class="arrow"/>
    <rect x="674" y="62" width="174" height="96" rx="9" class="gate"/><text x="692" y="89" class="title">Readiness controls</text><text x="692" y="110" class="copy">Direction • environment</text><text x="692" y="128" class="copy">Credential reference</text><text x="692" y="146" class="copy">Official checks when confirmed</text>
    <path d="M848 110 H882" class="path"/><polygon points="882,110 872,104 872,116" class="arrow"/>
    <rect x="884" y="62" width="204" height="96" rx="12" class="done"/><text x="902" y="89" class="title">Capability readiness</text><text x="902" y="110" class="copy">READY or READY_WITH_LIMITATIONS</text><text x="902" y="128" class="copy">per client and capability</text><text x="902" y="146" class="copy">policy and evidence snapshot retained</text>
    <rect x="466" y="242" width="174" height="82" rx="9" class="fail"/><text x="484" y="269" class="title">Correctable failure</text><text x="484" y="290" class="copy">Invalid/mismatched facts or evidence</text><text x="484" y="307" class="copy">No external mutation; correct and resume</text>
    <path d="M553 148 V234" class="retry"/><polygon points="553,234 547,224 559,224" class="arrow-red"/><path d="M466 283 H345 V156" class="retry"/><polygon points="345,156 339,166 351,166" class="arrow-red"/>
    <rect x="674" y="242" width="174" height="82" rx="9" class="gate"/><text x="692" y="269" class="title">Outcome unknown</text><text x="692" y="290" class="copy">External request may have changed state</text><text x="692" y="307" class="copy">Reconcile before retry or success</text>
    <path d="M761 158 V234" class="pending"/><polygon points="761,234 755,224 767,224" class="arrow-amber"/><path d="M848 283 H906 V166" class="pending"/><polygon points="906,166 900,176 912,176" class="arrow-amber"/>
    <rect x="258" y="394" width="830" height="62" rx="9" class="optional"/><text x="276" y="419" class="title">Independent evidence rail</text><text x="276" y="439" class="copy">Access context • subject and identifier snapshot • applicability inputs • authority decision • capability • environment • source/version/time • findings • actor • correlation</text>
  </svg>
  <div class="notes"><div class="note"><strong>Batch is transport</strong>A batch receipt never grants authority; each client becomes an isolated work item.</div><div class="note"><strong>No invented registration</strong>Readiness does not claim AEAT registration unless an authoritative contract and acknowledgement exist.</div><div class="note"><strong>Capability-specific</strong>Submission, retrieval, rejection and payment reporting may reach different results for the same client.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Business scenarios

| ID | Trigger/context | Expected outcome | Exception or continuity requirement |
|---|---|---|---|
| S1 | Business administrator onboards one company | One isolated profile is validated and receives per-capability readiness | Existing invoice processing is unchanged until later capabilities are activated |
| S2 | Autónomo onboards directly | DNI/NIE-derived NIF is processed under personal-data controls and subject-appropriate validation | Raw identity is not exposed in URLs, logs or broad support views |
| S3 | Accountant submits a portfolio | Batch is accepted for processing and decomposed into independently authorised client work items | One invalid or unauthorised client does not fail or expose another |
| S4 | Accountant is linked to a workspace but lacks statutory authority for retrieval | Workspace configuration may proceed only within product permission; retrieval readiness remains denied/undetermined | Authentication and portfolio membership do not expand authority |
| S5 | Client requests sending and receiving | Each direction/capability is evaluated separately | Failure of retrieval authority must not silently force or imply submission authority |
| S6 | NIF passes structural validation but AEAT census name does not match | Profile records a verification finding and correction path | Do not describe the party as unable to trade or universally unable to invoice |
| S7 | Entity census response indicates baja or revoked NIF | Country policy and compliance owner determine the permitted next action; onboarding does not invent a universal invoice block | Evidence and customer explanation are retained |
| S8 | Customer has explicitly selected a private platform | Record the fact and avoid overriding it during public onboarding | Private connection/publication/switching remains outside Phase 1 |
| S9 | Official public access mechanism is not yet confirmed | Complete all internal controls possible and return `ACTION_REQUIRED_EXTERNAL_SPEC` or equivalent limitation | Do not request certificate upload or claim external registration |
| S10 | External verification times out after transmission | Work item enters outcome-unknown/reconciliation state | No blind duplicate external call |
| S11 | TEST onboarding succeeds | Test readiness and evidence stay confined to TEST | No promotion or reuse of test credentials/outcomes in production |
| S12 | Customer changes name, legal form, NIF, authority or credential | New effective-dated records drive future readiness; prior evidence remains immutable | Existing invoice contexts are not rewritten |
| S13 | Duplicate direct or batch request is submitted | Same logical request is recognised and returns the existing work/result | No duplicate external mutation or profile |
| S14 | Customer cancels before readiness | Pending work is safely cancelled where no external mutation is uncertain | Audit and required evidence remain under retention policy |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | No private receipt platform has been expressly agreed | Treat the public solution as the default under Royal Decree 238/2026 | Confirmed regulatory rule; detailed mechanics remain open |
| BR2 | Customer uses or may use a combination of public/private routes | Record the customer/channel facts without making private connection a Phase 1 step | Confirmed legal possibility; exact route policy is outside this PRD |
| BR3 | Onboarding completes | Report capability readiness, not universal compliance or delivery success | Product boundary |
| BR4 | External registration is not evidenced | Do not create a `REGISTERED_FOR_PUBLIC_PLATFORM` assertion | Evidence-control rule |
| BR5 | Identifier is captured | Bind scheme, value, subject, purpose, issuer country, validity and verification evidence; do not use a bare NIF as tenant or route | PRD-SEI-231 |
| BR6 | Subject is a foreign natural person | Treat NIE as a source document/number that generally serves as NIF; do not create an establishment hierarchy from it | AEAT identity guidance |
| BR7 | Presence facts are captured | Store them separately from NIF/NIE and defer invoice-specific applicability to effective policy | PRD-SEI-231/235 |
| BR8 | AEAT census check returns a result | Interpret it as identity-data quality/census state only | AEAT service purpose |
| BR9 | Accountant or other delegate acts | Evaluate authority for principal, client, capability, direction, country/route, environment and effective time | PRD-SEI-231; Spain mechanism open |
| BR10 | Credential authenticates successfully | Treat it as authentication evidence only, not proof of BR9 | Security/authority separation |
| BR11 | Portfolio batch is accepted | Acceptance confirms only durable receipt and structural eligibility for processing | Proposed orchestration rule |
| BR12 | One batch item fails | Continue safe independent items and return a redacted per-item result | Proposed portfolio rule |
| BR13 | Environment is selected | Resolve it from trusted deployment/credential/configuration context and reject conflicts | Proposed security control |
| BR14 | TEST is used | Isolate data, credentials, endpoints, evidence and monitoring from production | Proposed security control |
| BR15 | External operation may be mutating | Classify operation safety and require idempotency or authoritative reconciliation before automatic retry | PRD-SEI-215/225 |
| BR16 | Readiness inputs change | Re-evaluate affected future capabilities and preserve the prior decision snapshot | Historical-continuity rule |
| BR17 | Customer requests unsupported capability | Return an explicit unavailable/undetermined result with owner and required evidence | No silent downgrade |
| BR18 | Invoice identity is captured | Keep supplier/recipient invoice roles separate from network destination and from delegated actor | PRD-SEI-231/233 |

## Scope and non-goals

### In scope

- Direct business and autónomo onboarding for a single Sage workspace/legal subject.
- Accountant portfolio intake with independent per-client processing and results.
- Sage tenant/workspace/product/dataset context and client-link verification.
- Legal-subject, NIF/DNI/NIE/entity identity and presence capture.
- Local identifier validation using approved, versioned rules.
- Optional AEAT census verification when access, purpose and service contract are approved.
- Spain applicability inputs required to decide customer/capability readiness.
- Operation-specific delegated-authority evidence and decision.
- Public-solution channel/default context and capability request.
- Credential references and custody controls once the official mechanism is confirmed.
- TEST/production separation, correction, cancellation, retry and reconciliation.
- Per-capability readiness, evidence, audit, product and operations visibility.

### Non-goals

- Submitting, receiving, consulting, rejecting, correcting or reporting payment for an invoice.
- Treating onboarding as proof that every future transaction is within scope.
- Implementing or configuring VeriFactu/RRSIF.
- Creating a private-platform connection, publishing a private entry point or switching provider.
- Defining the final public-solution endpoint, authentication or certificate workflow before official evidence.
- Replacing AEAT census registration processes such as models 030/036.
- Determining VAT, place of supply or legal advice for the customer.
- Using a NIF/NIE as an invoice-routing destination without a separate approved routing scheme.
- Approving physical API endpoints, databases, queues or vendor libraries in this PRD.

## Research and evidence register

| ID | Source | Finding used | Confidence and limitation | Requirement impact |
|---|---|---|---|---|
| E1 | [Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238) Articles 3, 5, 6 and 11 | Mandate scope is between entrepreneurs/professionals; public/private routes or a combination are possible; public is the default absent an express private receipt agreement; public invoices carry supplier and recipient NIF | Primary regulation. Technical order still required | BR1–BR4; FR20–FR24; delivery gates |
| E2 | Royal Decree 238/2026 Article 11.4–11.5 and final provision 3 | Public identification, authentication and representation are to be specified by ministerial order; authorised intermediaries may act under those future terms | Primary regulation; exact credential/grant contract unresolved | FR15–FR19; blocks production access design |
| E3 | [AEAT — NIF for natural persons](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/alta-modelo-036/casilla-110-solicitud-numero-identificacion-036/personas-fisicas.html) | DNI generally serves as NIF for Spanish natural persons and NIE generally serves as NIF for foreign natural persons; exceptional assigned NIF cases exist | Primary tax-authority guidance; detailed edge cases need country catalogue | BR5–BR7; FR5–FR10 |
| E4 | [AEAT — NIF for legal persons/entities](https://sede.agenciatributaria.gob.es/Sede/censos-nif-domicilio-fiscal/solicitar-nif/nif-juridica.html) | Legal persons/entities use an assigned NIF; identity and legal-form data are distinct from Sage tenancy | Primary tax-authority guidance | FR5–FR10 |
| E5 | [AEAT — third-party NIF checking](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-030/comprobacion-nif-terceros-efectos-censales.html) | Service supports unit/list/CSV identity-quality checks; CSV UI limit is 20,000; results differ for natural persons and entities | Primary operational guidance. UI limit is not an integration/API contract | BR8; FR11–FR14; removes unsupported 10,000 assumption |
| E6 | [AEAT — identification-quality web service manual](https://sede.agenciatributaria.gob.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Modelos_y_formularios/Declaraciones/Modelos_01_al_99/030_036_037/WS_Masivo/Manual_Tecnico_WS_Masivo_Calidad_Datos_Identificativos.pdf) | Documents SOAP results including identified, similar, not identified, baja, revoked and not processed | Official technical document, version 1.8 dated 2021; current access/limits/security must be reconfirmed | Proposed adapter/status mapping; production gate |
| E7 | Existing Confluence parent and five child pages listed in the source consolidation | Provide personas, draft flows, API examples, environment/error proposals and identity questions | Internal discovery input only; many claims lack official evidence | Scenarios and proposed requirements, not provider facts |
| E8 | PRD-SEI-231 | Separates access context, legal subject, presence, official identifier, network address, authority and credential | Shared discovery model | FR1–FR19 |
| E9 | PRD-SEI-235 | Applicability requires transaction facts beyond B2B/B2C/B2G label | Shared discovery model | FR8, FR20 and readiness limits |
| E10 | PRD-SEI-211/212 | Public consultation and submission need immutable identity/authority context and their own operation lifecycles | Detailed discovery PRDs; external interfaces still gated | Capability handoff and evidence |
| E11 | PRD-SEI-215/225/226 | Shared reconciliation, security, trust, data and audit controls | Shared discovery/draft requirements | Failure, NFR and operations requirements |

### Evidence contradictions resolved in this draft

| Draft claim | Evidence-led treatment |
|---|---|
| Every business must transition entirely through the AEAT public network | The mandate is scoped to qualifying B2B operations; public/private routes or a combination are permitted |
| Onboarding registers the customer with AEAT and receives registration confirmation | No such contract is assumed; readiness is internal unless official evidence proves an external operation |
| Business uploads its certificate and accountant uses one master certificate for all clients | Credential and representation mechanism is open pending the ministerial order; authority remains per client/capability |
| Social collaborator can send but cannot retrieve without individual apoderamiento | Retained as a research question, not an enforcement rule for SPFE |
| `NIF` and `NIE` are peer identifier schemes | NIF is the invoice/tax identity role; NIE generally supplies that NIF for a foreign natural person |
| All DNI/NIF/NIE use the same modulo-23 rule and entities use legacy CIF handling | Validation is selected by subject/identifier class and implemented from approved rules/tests; historical terminology is not the canonical model |
| AEAT `IDENTIFICADO` proves active and permitted to trade | It proves the supplied identity data matched the census response contract |
| AEAT batch limit is 10,000 | The current public UI guidance says 20,000 CSV records; no Sage integration limit is approved |
| Environment comes from `X-Environment` and missing means TEST | Trusted environment boundaries select the target; ambiguity or mismatch is rejected |
| TEST records need not persist | Test evidence is retained under an approved non-production policy and isolated from production |
| Five retries with fixed timings are compliant | Retry policy depends on operation safety and confirmed external limits; numbers remain configuration decisions |

## Current-state analysis

The current Confluence hierarchy is detailed but fragmented. The parent provides the product story, while child pages independently define identity, portfolio, environment and failure behaviour. That creates five problems:

1. A reader can implement a child-page assumption without seeing the parent phase boundary.
2. One readiness flag hides independent identity, authority, credential and capability states.
3. Draft endpoint shapes and retry numbers appear equivalent to provider facts.
4. Accountant authentication, credential custody and statutory authority are conflated.
5. GitHub has no canonical source for the stable onboarding page, so review and publishing lineage are incomplete.

The proposed target keeps the detailed scenarios but places each claim behind an explicit evidence status and capability boundary.

## Proposed conceptual solution

**Proposed model; architecture decision required.** The onboarding capability has six responsibilities:

1. **Intake** — receive a direct request or durable accountant batch and create isolated work items.
2. **Context** — bind Sage access context to one legal subject and its effective identifiers/presence facts.
3. **Decision** — evaluate policy, requested capabilities and operation-specific authority.
4. **Verification** — execute local checks and only approved external checks, recording source and confidence.
5. **Readiness** — produce independent capability outcomes without claiming invoice or delivery success.
6. **Evidence/operations** — retain explainable decisions and provide correction/reconciliation actions.

### Conceptual records

| Record | Minimum fields | Ownership/boundary |
|---|---|---|
| Onboarding case | case ID, intake mode, environment, status, created/updated time, requested actor, correlation | Orchestration; no authority implied |
| Access context | tenant, workspace, dataset, product, environment, verified relationship | Shared tenancy/security model |
| Legal subject | stable subject ID, subject type, legal name, jurisdiction, status and effective dates | PRD-SEI-231 |
| Presence | presence ID/type/address, parent subject, evidence, validity | PRD-SEI-231/235; not inferred from NIF |
| Official identifier | scheme, normalized value, source-document type, subject/purpose, issuer, validity, verification | PRD-SEI-231 |
| Channel context | public default/selected, known private choice/combination, source and effective time | Does not create a private connection |
| Capability request | client, capability, direction, effective request time and requested route | Evaluated independently |
| Authority decision | principal, delegate/user, capability, direction, environment, evidence, validity, result/reason | Separate from authentication/credential |
| Credential reference | owner, custodian, purpose, environment, expiry/rotation/status | Secret remains in approved vault |
| Verification finding | check type/source/version/time, input subject, outcome, reason, evidence reference | Result meaning cannot exceed source contract |
| Readiness decision | capability, result, limitation/reason, policy version, evidence snapshot and expiry/recheck | Consumed by later operation |
| Batch | batch ID, submitting firm, counts, status and item references | No client details leaked across item boundaries |

### Readiness dimensions

Do not represent the customer with one `onboarded` flag.

| Dimension | Example values | Meaning |
|---|---|---|
| Profile | `DRAFT`, `VALIDATING`, `ACTION_REQUIRED`, `COMPLETE`, `CANCELLED` | Progress of the onboarding case |
| Identity | `UNVERIFIED`, `STRUCTURALLY_VALID`, `VERIFIED`, `MISMATCH`, `REVIEW_REQUIRED` | Identity evidence only |
| Authority | `NOT_REQUIRED`, `PENDING`, `EFFECTIVE`, `DENIED`, `EXPIRED`, `REVOKED`, `UNDETERMINED` | Per capability and client |
| Credential | `NOT_YET_REQUIRED`, `PENDING`, `VALID`, `EXPIRING`, `INVALID`, `REVOKED` | Authentication/custody readiness |
| External check | `NOT_REQUIRED`, `NOT_ATTEMPTED`, `PENDING`, `CONFIRMED`, `NOT_CONFIRMED`, `OUTCOME_UNKNOWN` | Only for a confirmed external operation |
| Capability readiness | `NOT_REQUESTED`, `ACTION_REQUIRED`, `READY_WITH_LIMITATIONS`, `READY_FOR_PUBLIC_SOLUTION`, `SUSPENDED` | Final onboarding result per capability |

### Capability catalogue

Initial capabilities are identifiers, not promises that the public solution already exposes each operation:

- `SUBMIT_INVOICE`
- `RECEIVE_INVOICE`
- `CONSULT_ISSUED_INVOICE`
- `CONSULT_RECEIVED_INVOICE`
- `COMMUNICATE_REJECTION`
- `COMMUNICATE_PAYMENT`
- `VIEW_COMPLIANCE_EVIDENCE`
- `MANAGE_ONBOARDING`
- `MANAGE_CREDENTIAL_REFERENCE`

Each capability must carry `CONFIRMED`, `PROPOSED`, `UNKNOWN` or `UNSUPPORTED` evidence status for the selected external contract version.

## Detailed journeys

### J1 — Direct customer readiness

1. An authenticated product user selects the Spanish legal subject/workspace.
2. Sage verifies product permission and binds immutable access context.
3. The user supplies subject type, official identity and required presence/applicability facts.
4. Sage performs immediate structural validation with a rule version and returns field-level corrections without exposing sensitive values.
5. The user requests named public-solution capabilities rather than a universal sender/receiver role.
6. Sage determines whether the user acts directly or as a delegate and evaluates authority per capability.
7. Approved external checks run asynchronously when required and supported; otherwise the result records the missing external specification/control.
8. The service produces per-capability readiness and retains the decision/evidence snapshot.
9. The product explains what is ready, limited, unavailable or still required and which later invoice capability consumes the result.

**Result:** internal readiness is explainable; no invoice is sent and no AEAT registration is claimed.

### J2 — Accountant portfolio batch

1. An authorised accountant-firm user submits a batch with an idempotency key and client references.
2. Sage authenticates the firm context, validates the envelope and durably records the batch.
3. Sage returns an asynchronous receipt; acceptance does not mean any client is ready.
4. Each client becomes an isolated work item bound to its own workspace/legal subject relationship.
5. For each requested capability, Sage evaluates product permission, statutory authority evidence and environment independently.
6. Safe work continues for other clients when one item is invalid, unauthorised or awaiting evidence.
7. The accountant can retrieve only redacted results for clients they remain authorised to view.
8. Batch status derives from item outcomes and exposes counts without leaking another client’s identity.

**Result:** scale is achieved without a master grant or cross-client state.

### J3 — NIF correction and census mismatch

1. Local validation selects rules using subject type and claimed identifier/source-document type.
2. A structural/check-character failure stops before external lookup and returns a correctable finding.
3. After correction, an approved census check may compare the identifier and name/business name.
4. The service maps the official response without adding a trading/eligibility interpretation.
5. Similar/mismatch/baja/revoked results route to the country-policy decision and, where needed, manual review.
6. Corrected verification creates a new finding; prior findings remain auditable.

### J4 — Missing representation specification

1. A delegate requests a capability whose official SPFE representation mechanism is not confirmed.
2. Sage may complete tenant, identity and structural controls.
3. The authority result remains `UNDETERMINED` and capability readiness remains `ACTION_REQUIRED` or `READY_WITH_LIMITATIONS` as policy permits.
4. The customer is told which evidence/official specification is missing; no certificate workflow is invented.

### J5 — Transient external failure

1. An approved read-only verification call fails before a response.
2. The service applies the versioned safe retry policy and records attempts/correlation.
3. If retry budget is exhausted, the item remains pending/action-required with fault ownership.
4. Other client items continue.

### J6 — Ambiguous external mutation

1. A future confirmed mutating operation times out after transmission.
2. The operation enters `OUTCOME_UNKNOWN` and onboarding cannot claim readiness from that mutation.
3. The service queries or otherwise reconciles authoritative state using the original correlation/idempotency mechanism.
4. Only confirmed absence permits resubmission; confirmed success is persisted without duplicating the mutation.

### J7 — Cancellation and change

1. Customer cancels a case or changes identity, authority, capability or environment.
2. Sage prevents new work for the superseded context and safely cancels non-mutating pending steps.
3. Any outcome-unknown external work is reconciled rather than forgotten.
4. A new effective-dated decision governs future operations; historical invoice/onboarding evidence remains unchanged.

## Functional requirements

### Intake, tenancy and isolation

| ID | Requirement |
|---|---|
| FR1 | The service must create a correlation-addressable onboarding case for one legal subject and one environment without treating the Sage tenant, workspace or user as that legal subject. |
| FR2 | The service must verify the caller’s permitted tenant/workspace/client relationship before returning or changing onboarding data. |
| FR3 | Direct and accountant intake must invoke the same business controls even where their orchestration and response timing differ. |
| FR4 | Portfolio intake must durably acknowledge the batch, create independently controlled items and expose aggregate plus authorised per-item status. |
| FR5 | A failure, cancellation or authority denial for one client must not change another client or expose its identity/configuration. |

### Identity and applicability inputs

| ID | Requirement |
|---|---|
| FR6 | The service must bind a stable legal subject to scheme-qualified identifiers and must record subject type, source-document type, purpose, validity and verification evidence. |
| FR7 | The service must represent DNI/NIE/entity NIF treatment without modelling NIE as an establishment identifier or as a peer routing scheme. |
| FR8 | The service must capture presence and applicability facts separately from identifiers and must not permanently classify all transactions during onboarding. |
| FR9 | Local validation must select approved rules by identifier and subject class, expose the rule version and test check characters as well as format. |
| FR10 | Examples, fixtures and documentation must use explicitly synthetic identifiers that pass the intended validator or are labelled as negative test cases. |

### Verification

| ID | Requirement |
|---|---|
| FR11 | The service must distinguish structural validation, census identity matching, scope eligibility, delegated authority and routing discovery as separate checks/results. |
| FR12 | An AEAT census adapter, if approved, must map official response semantics without asserting trading permission, mandate applicability, route or capability authority. |
| FR13 | External verification must retain source, contract/version, checked time, outcome, evidence reference and any recheck/expiry policy. |
| FR14 | Batch size, caching, latency, throttling and retry controls must come from approved service evidence and measured capacity, not copied from an interactive UI or draft page. |

### Authority and credentials

| ID | Requirement |
|---|---|
| FR15 | The service must evaluate an effective authority decision for each client, capability, direction, country/route, environment and time when a delegate acts. |
| FR16 | Authentication, accountant-firm role, portfolio membership, API credential or certificate possession must not satisfy FR15 by implication. |
| FR17 | Authority evidence must record source/type, principal, delegate, permitted operations, validity, status, evidence reference and revocation history. |
| FR18 | Revoked, expired, denied or undetermined authority must block only the affected future capabilities and preserve historical evidence. |
| FR19 | Credential workflows must remain abstract references until the official SPFE authentication/representation contract and Sage custody design are approved. |

### Public-solution context and readiness

| ID | Requirement |
|---|---|
| FR20 | The service must record whether public use is a customer selection, regulatory default, part of a known combination or undetermined, with source and effective time. |
| FR21 | Phase 1 must not create, publish or switch a private-platform connection or route. |
| FR22 | The service must evaluate readiness independently for every requested capability and must not infer receipt/consultation/reporting readiness from submission readiness. |
| FR23 | The service must not emit an external-registration success unless an approved official operation and acknowledgement prove it. |
| FR24 | A completed onboarding case must provide a versioned readiness decision and immutable evidence snapshot for later public submission, consultation or reporting operations. |
| FR25 | Later operations must re-evaluate expired/revoked authority and materially changed policy rather than relying indefinitely on onboarding completion. |

### Environment, lifecycle and recovery

| ID | Requirement |
|---|---|
| FR26 | Trusted deployment, credential and configuration context must select TEST or production; a caller-provided mismatch or missing required context must be rejected. |
| FR27 | TEST and production must use separate credentials, external endpoints, storage partitions, evidence labels, observability and access controls. |
| FR28 | Test outcomes and credentials must never automatically promote into production; production readiness must be separately evaluated. |
| FR29 | Every logical direct request, batch and external operation must support duplicate detection through an approved idempotency/correlation mechanism. |
| FR30 | Automatic retries must be limited to operations classified safe; ambiguous external mutations must reconcile before repetition. |
| FR31 | Cancellation must stop safe pending work while retaining or reconciling any uncertain external outcome and preserving required audit. |
| FR32 | Changed identity, authority, credential, environment or policy must create new effective context without rewriting prior decisions or invoice history. |

### Product and operations experience

| ID | Requirement |
|---|---|
| FR33 | Products must display case, identity, authority, external-check and capability-readiness results separately in plain language. |
| FR34 | Correctable failures must identify the responsible actor and remediation without revealing full sensitive identifiers or credential data. |
| FR35 | Operations must see intended versus observed state, correlation, age, fault domain, safe next action and redacted evidence. |
| FR36 | Manual actions must enforce the same tenant, authority, environment, evidence and audit controls as automated actions. |
| FR37 | Every protected read/change must record actor, client, capability, environment, reason and result in a tamper-evident audit trail. |
| FR38 | The service must support controlled suspension of a capability or cohort without deleting identity, authority or historical evidence. |

## Proposed client/API capability surface

This table defines behaviours, not approved URLs or transport choices.

| Capability | Direct behaviour | Portfolio behaviour | Key safety control |
|---|---|---|---|
| Create/update case | Immediate receipt plus synchronous structural findings where possible | Durable asynchronous batch receipt and item creation | Idempotency and tenant/client binding |
| Validate identity | Local immediate result; approved external checks may be pending | Independent per-item checks under rate/capacity control | Result meaning limited to source contract |
| Submit authority evidence | Per client/capability | Reusable evidence reference only where its legal scope covers each named client/capability | No batch-level universal grant |
| Evaluate readiness | Per capability with reasons | Per-item/per-capability with aggregate counts | No cross-client leakage or silent downgrade |
| Correct/resume | Resume same logical case with new evidence revision | Resume selected authorised items | Prior findings retained |
| Cancel | Cancel safe work; reconcile ambiguity | Cancel selected authorised items/batch remainder | Does not erase audit or uncertain mutations |
| View status/evidence | Redacted subject-scoped view | Aggregate plus authorised item views | Least privilege and personal-data controls |

## Failure and recovery matrix

| Failure/condition | Classification | Required behaviour | Customer/operations outcome |
|---|---|---|---|
| Invalid identifier format/check character | Correctable validation | Stop before external call; return rule-specific field finding | Customer corrects and resumes |
| NIF/name census mismatch or similar result | Business verification finding | Preserve official result; apply country-policy/manual-review rule | No invented “cannot trade” message |
| Entity baja/revoked result | Policy/legal review | Do not map automatically to universal invoice prohibition | Explain evidence and required owner decision |
| Unknown client or unauthorised accountant | Security/authority | Deny with non-enumerating response and audit | No client existence/data leakage |
| Authority expired/revoked during processing | Authority | Stop affected future capability; leave other authorised items independent | Action required with evidence owner |
| Credential invalid/expired | Authentication/configuration | Block affected external step; do not change authority record | Credential custodian remediates |
| Environment mismatch | Security/configuration | Reject before external call | Explicit correction; no silent TEST default |
| External validation/throttle/unavailability | Transient where contract permits | Retry only under approved budget; otherwise retain pending/recoverable state | Fault domain and next action visible |
| Timeout after confirmed read-only call | Transient | Retry safely with correlation as contract permits | No duplicate mutation risk |
| Timeout after possible mutation | Outcome unknown | Reconcile authoritative state before retry/success | Operations alert if unresolved |
| Duplicate request or batch | Duplicate | Return/attach to existing logical case; do not repeat external work | Stable result/correlation |
| Internal persistence failure after external success | Outcome unknown/internal | Recover from durable intent/correlation and reconcile | Do not ask customer to resubmit blindly |
| Concurrent conflicting update | Conflict | Serialize or reject stale version; preserve one effective revision | Caller refreshes and retries deliberately |
| Partial portfolio failure | Mixed | Complete independent safe items and report aggregate/permitted item outcomes | Failed item does not roll back others |
| Cancellation with work in flight | Cancellation | Stop safe operations; reconcile uncertain work; retain audit | Accurate final item state |

## Security, privacy and non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Apply least privilege and tenant/client isolation to every direct, batch, status, evidence and manual operation. |
| NFR2 | Treat DNI/NIE-derived NIFs, names, authority evidence and credential metadata according to approved personal/confidential-data classification. |
| NFR3 | Never place full NIF/NIE values, certificate material, secrets or raw authority documents in URLs, logs, metrics, general errors or webhook payloads. |
| NFR4 | Encrypt sensitive data in transit and at rest; store secret material only in the approved credential system with access/rotation audit. |
| NFR5 | Maintain tamper-evident audit and immutable decision snapshots sufficient to explain readiness at the time it was used. |
| NFR6 | Define retention and deletion separately for profile data, verification findings, authority evidence, credentials, batches and historical compliance evidence. |
| NFR7 | Make direct/batch orchestration and external work recoverable after process restart without duplicate mutation. |
| NFR8 | Monitor queue age, verification latency, authority failures, outcome-unknown age, environment mismatch and evidence completeness by safe dimensions. |
| NFR9 | Establish performance, batch-size, concurrency and availability targets from approved volumes, official external limits and measured baselines before production. |
| NFR10 | Make status/correction experiences accessible and consistent across customer-facing and accountant products. |
| NFR11 | Version policy, validator, external contract, mapping and customer-message rules so historical outcomes remain explainable. |
| NFR12 | Support a kill/disable control by environment, cohort and external capability without deleting completed evidence or disabling unrelated clients. |

## Acceptance criteria

| ID | Given/when/then |
|---|---|
| AC1 | Given a direct user with workspace permission, when a Spanish legal subject is onboarded, then the case binds a separate legal-subject record and does not treat the workspace ID as its official identity. |
| AC2 | Given a foreign natural-person sole trader, when identity is captured, then the NIE is represented as the source number generally serving the person’s NIF and no establishment ID is inferred. |
| AC3 | Given a structurally invalid synthetic NIF, when validation runs, then the failure occurs before external lookup and reports the versioned validation rule. |
| AC4 | Given an AEAT census response of `IDENTIFICADO`, when the result is stored, then it is labelled as census identity matching and does not assert e-invoicing scope, route or authority. |
| AC5 | Given an entity result of baja or revoked, when onboarding evaluates it, then the configured country-policy/manual-review rule is applied and no undocumented universal invoice block is created. |
| AC6 | Given an accountant authenticated to a firm but not linked to a client, when status or onboarding is requested, then access is denied without disclosing the client’s existence or data. |
| AC7 | Given an accountant linked to a client but lacking effective retrieval authority, when submission and retrieval are requested, then each capability receives its own authority/readiness result. |
| AC8 | Given a batch with authorised, invalid and unauthorised clients, when processing completes, then safe authorised items complete independently and returned detail is limited to permitted clients. |
| AC9 | Given the official SPFE representation contract remains unknown, when a delegate requests external readiness, then the capability is not reported as registered or fully ready and the missing gate is explicit. |
| AC10 | Given a caller supplies a production payload to a TEST deployment or conflicting environment context, when intake occurs, then the request is rejected before external access. |
| AC11 | Given TEST onboarding succeeded, when production onboarding starts, then no TEST credential, verification or readiness decision is promoted as production evidence. |
| AC12 | Given a duplicate direct or batch request with the same idempotency scope, when it is retried, then the existing logical case/result is returned and external work is not duplicated. |
| AC13 | Given a future mutating external request timed out after transmission, when recovery runs, then it reconciles authoritative state before resubmission or readiness success. |
| AC14 | Given a customer has expressly selected a private platform, when Phase 1 public onboarding records that fact, then no private connection or route is created or overwritten. |
| AC15 | Given identity or authority changes after readiness, when a later operation begins, then expired/revoked controls are re-evaluated while the earlier decision remains historically explainable. |
| AC16 | Given a customer is ready to submit but retrieval is not evidenced, when the product displays status, then it shows the capability difference rather than a single `ONBOARDED` flag. |
| AC17 | Given an operator inspects a failed case, when evidence is displayed, then correlation, fault owner and safe action are visible while full identifiers and secrets remain redacted. |
| AC18 | Given onboarding completes, when PRD-SEI-212 or PRD-SEI-211 consumes readiness, then it receives subject, capability, authority, environment, policy and evidence references without mutable customer-master substitution. |

## Measures

Targets require baselines and owners before production approval.

| Measure | Purpose | Dimensions/guardrail | Owner |
|---|---|---|---|
| Started-to-ready conversion | Identify onboarding friction | Direct/accountant, subject type, capability, environment; no raw IDs | Product |
| Time in each case/readiness state | Find customer, Sage or external bottlenecks | Fault domain and capability | Product/operations |
| Correction rate by validation rule | Improve data quality and messages | Validator/rule version | Product/data |
| Authority undetermined/denied rate | Quantify accountant capability gaps | Capability and evidence type | Legal/product |
| Portfolio partial-failure rate | Measure scalable accountant experience | Safe batch-size bands and fault domain | Product/operations |
| External verification success/latency | Measure confirmed adapter health | Contract version/environment | Engineering/operations |
| Outcome-unknown count and age | Measure mutation/reconciliation safety | Operation/environment | Operations |
| Evidence completeness | Confirm every readiness result is explainable | Policy, identity, authority, source and actor references | Compliance/QA |
| Cross-client access violations | Security control effectiveness | Must be zero; security incident process applies | Security |
| Support contacts by onboarding stage | Identify unclear correction/authority experience | Stage and persona | Support/product |

## Dependencies and rollout gates

| Gate | Evidence/decision required | Blocks |
|---|---|---|
| Canonical review | Product, Spain regulatory, security, architecture, operations and accountant-product reviewers assigned | In-review status |
| Policy | Approved Phase 1 customer/transaction cohort, effective dates, exclusions and public/default interpretation | Customer eligibility |
| Identity | Approved Spain identifier catalogue, validator rules/test fixtures, data classification and census-result policy | Identity implementation |
| Representation | Ministerial order/provider artefacts plus approved per-capability accountant authority matrix | Delegate production readiness |
| External contract | Current official WSDL/OpenAPI/schema, authentication, environments, limits, idempotency, status/error and support evidence | External integration design |
| Design | State/record boundaries, API/client contract, privacy, retention and threat model approved | Build |
| Non-production | Environment isolation, synthetic data, fault injection, idempotency and reconciliation tests pass | Pilot |
| Pilot | Named direct and accountant cohorts, volumes, support model, success/kill criteria and manual recovery approved | Production |
| Production | Security, capacity, observability, operations runbook, retention and evidence-completeness controls pass | General availability |

Publication to the six existing stable Confluence pages was explicitly approved on 2026-08-25. Merge and a successful dry-run remain required before the live update; global automatic publication remains disabled.

## Risks and mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| “Registered” is asserted without an official registration contract | False customer/compliance promise | Use capability readiness and evidence states; gate external assertion |
| VeriFactu is conflated with B2B e-invoicing | Wrong credentials, workflow and scope | Keep separate definitions and PRD boundary |
| One accountant credential is treated as universal authority | Unauthorised client actions/access | Per-client, per-capability authority decision independent of authentication |
| NIF/NIE is used as tenant, establishment and route | Collision, privacy and incorrect delivery | Scheme/role-qualified identity plus separate tenant/presence/network records |
| Census match is treated as eligibility | Incorrect blocking/activation | Preserve official semantics and apply separate policy decisions |
| Environment header silently redirects traffic | Production/test leakage | Trusted environment boundary and mismatch rejection |
| Bulk scale causes cross-client disclosure | Regulatory/security incident | Item isolation, non-enumerating errors, least privilege and audit |
| Blind retry duplicates external mutation | Conflicting external state | Operation-safety classification and reconciliation-first recovery |
| Draft limits/SLAs become production commitments | Unreliable design and customer promise | Evidence register, baselines and delivery gates |
| Confluence and Git diverge | Unreviewed requirements are implemented/published | Git canonical source, controlled current-source mapping and explicit publish approval |

## Open questions and decision owners

| Question | Why it matters | Owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Has the ministerial technical order for the public solution been published, and which version governs delivery? | Defines authentication, representation, UBL and service contracts | Spain regulatory/legal | External design/production | Treat as unavailable until primary evidence is registered |
| Does the public solution require customer registration, or only authenticated access/use? | Determines whether any external onboarding mutation exists | AEAT/provider liaison | State/API design | No registration assertion without explicit contract |
| Which official mechanisms authorise submission, receipt, consultation, rejection, payment reporting and evidence access? | Prevents one grant from becoming universal | Spain legal/identity/security | Accountant pilot/production | Per-capability matrix; no inferred send/receive asymmetry |
| Can social collaboration or a recorded apoderamiento be used for each SPFE operation, and with what evidence/revocation check? | Determines accountant experience and enforcement | Spain legal/AEAT liaison | Delegate production | Open; VeriFactu/SII precedent is not automatically transferable |
| Which AEAT identity-quality service may Sage use, for what purpose and authentication model? | Determines lawful/technical census verification | AEAT liaison/security/privacy | External identity check | Use local validation until approved |
| What should `IDENTIFICADO-BAJA` and `IDENTIFICADO-REVOCADO` mean for onboarding and later invoices? | Avoids unsupported universal block or unsafe activation | Spain tax/legal/product | Identity policy/pilot | Manual/policy review until decided |
| What is the official TEST or homologation environment and synthetic-data contract? | Determines safe external testing | AEAT liaison/engineering | External test/pilot | No production-like assumptions without evidence |
| Which exact product/dataset maps to a legal subject, and can one workspace contain several subjects? | Determines tenancy/cardinality | Product/data/architecture | Data/API design | Explicit relationship, never equality by assumption |
| Which customer cohorts and transaction directions are Phase 1? | Determines eligibility and volume | Spain product/regulatory | Journey/rollout | Use PRD-SEI-235 applicability contract after approval |
| What are expected direct customers, accountant firms, clients per firm, concurrent batches and peak checks? | Determines capacity and operational model | Product/analytics | NFR targets/pilot | Measure pilot and set reviewed limits |
| What evidence and retention periods apply to identity, authority, credentials and readiness decisions? | Determines privacy, audit and deletion | Legal/privacy/security | Production | Separate configurable schedules pending approval |
| Should the five current child pages remain published as generated children or become anchors/redirects to the consolidated parent? | Prevents duplicate sources and broken navigation | Product/document owner | Publication plan only | Preserve links until explicit migration plan is approved |

## Decisions

| ID | Decision | Status | Owner/date |
|---|---|---|---|
| D1 | Phase 1 onboarding is a public-solution readiness capability, not private-platform onboarding | Accepted product direction | User, 2026-08-25 |
| D2 | Consolidate the parent and five child-page subjects into one canonical PRD while preserving their detail and evidence lineage | Accepted product direction | User, 2026-08-25 |
| D3 | Model direct and accountant pathways as different intake/orchestration modes using the same client-level controls | Proposed for review | TBD |
| D4 | Do not infer accountant authority from authentication, certificate possession or portfolio membership | Proposed for review; consistent with PRD-SEI-231 | TBD |
| D5 | Use per-capability readiness rather than one onboarding/registered flag | Proposed for review | TBD |
| D6 | Publish this canonical source to the existing stable parent page only after merge and a successful dry-run | Approved by user | 2026-08-25 |

## Readiness

**Status: discovery-ready draft; not consultation-ready or approved for delivery.**

The document is ready for structured review of scope, identity and proposed controls. Production design remains blocked by the public-solution technical order/contracts, operation-specific representation evidence, customer/data cardinality, environment definition and approved capacity/security/retention decisions.

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-25 | Initial canonical draft | Consolidated the Public Platform onboarding parent and five child subjects; separated readiness from registration, NIF from NIE source identity, authority from authentication, TEST from production and safe retry from reconciliation | User approval; internal Confluence pages; Royal Decree 238/2026; AEAT identity guidance; PRD-SEI-211/212/215/225/226/231/235 |
