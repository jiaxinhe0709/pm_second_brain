---
id: PRD-SEI-221
title: Foundation — Operator Readiness and Regulatory Governance
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
  - PRD-SEI-102
  - PRD-SEI-103
  - PRD-SEI-201
  - PRD-SEI-202
  - PRD-SEI-203
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: ""
  title: Foundation — Operator Readiness and Regulatory Governance
  layout: two_left_sidebar
  toc: true
---

# Foundation — Operator Readiness and Regulatory Governance

## Decision summary

Phase 3 must not enter customer pilot or production until the named private-platform operator and the end-to-end Sage proposition can demonstrate the applicable legal, technical, security, operational and customer-support controls.

This PRD defines a product and business-analysis readiness framework. It converts the current regulatory findings into evidence domains, journeys, requirements and gates. It does not provide legal advice, certify compliance, or assume that Sage will be the legal operator. The selected delivery model in ADR-SEI-001 determines which entity supplies each control, but Sage must retain enough evidence and operational authority to support the proposition it presents to customers.

> **Product principle:** Operator readiness is an evidenced operating condition, not a feature-complete claim or a one-time legal review.

## Phase and outcome

| Phase | Relevant outcome | Readiness implication |
|---|---|---|
| Phase 1 — Public connection | Sage products use the public solution | Public route remains a valid baseline and fallback according to approved rules |
| Phase 2 — Existing private providers | Customers connect a selected external provider | Provider readiness is connection-specific; Sage is not assumed to operate that provider |
| **Phase 3 — Sage private-platform proposition** | Customers can choose Sage as their private-platform experience | **Named operator and full service chain must pass the controls in this PRD** |
| Future expansion | Additional countries and value-added services | Inform extensibility only; each jurisdiction/service requires separate readiness evidence |

## Problem and objective

### Problem

A Sage-branded private-platform proposition creates expectations beyond a normal ERP integration. Customers and counterparties depend on the operator to receive, transform, exchange, sign or seal, interconnect, submit required public information, communicate lifecycle events, preserve evidence, maintain continuity and provide support.

Readiness can fail even when the happy-path API works. Examples include:

- no confirmed legal entity is authorised or accountable to operate the platform;
- entry-point lookup or interconnection cannot be proven end to end;
- transformation loses mandatory business information;
- operator signatures, seals or certificates are not governed;
- a faithful copy reaches the public solution but cannot be correlated or reconciled;
- Sage and a partner disagree about an ambiguous outcome or incident owner;
- support and continuity claims are not backed by capacity, staffing or exercises;
- regulatory or audit evidence is inaccessible after partner termination;
- the ministerial order changes an assumed technical contract.

### Objective

Create one authoritative readiness control register that:

- maps official obligations and approved interpretations to product/service controls;
- identifies the accountable and responsible entity for every control;
- distinguishes evidence missing, designed, implemented, externally validated and operational states;
- blocks pilot or production when critical evidence is absent;
- supports recurring review after launch and controlled suspension when readiness degrades;
- links Phase 1/2 reuse decisions to the additional Phase 3 operator gap.

## Scope and non-goals

### In scope

- Spain private-platform operator readiness for the Phase 3 Sage proposition.
- Legal/accountability, registration, entry point, interoperability, public connectivity, lifecycle, security, continuity, support, evidence and exit domains.
- Sage-operated, partner-operated and hybrid delivery routes.
- Discovery, external validation, pilot, production, recurring review and suspension gates.
- Evidence that spans Sage products, shared platform services and the named operator.

### Non-goals

- Selecting the delivery model; see ADR-SEI-001.
- Giving legal advice or replacing approval from Sage legal/compliance teams.
- Reproducing legislation or unpublished/confidential technical specifications.
- Defining final endpoint payloads before official technical specifications are available.
- Certifying every value-added service or future country.
- Setting invented service levels, legal retention periods or launch dates.
- Treating the public route as unavailable because Phase 3 exists.

## Definitions

| Term | Meaning | Important distinction |
|---|---|---|
| Legal operator | Entity responsible for operating a qualifying private platform | Not automatically the Sage brand or customer-contracting entity |
| Proposition owner | Sage entity accountable for the customer offer and experience | May rely on a different legal operator under an approved model |
| Control | Policy, process or technical behaviour used to satisfy a requirement or risk | A control statement is not evidence that it operates effectively |
| Evidence | Current artefact or observable result proving design, implementation or operation | A supplier assertion without verification has limited confidence |
| Readiness | Approved evidence that the scoped service can operate safely at a stated gate | Not a permanent status; it can expire or be suspended |
| External validation | Test, approval or review involving the public solution, another platform, authority or independent assessor | Internal testing alone may not demonstrate interoperability |
| Waiver | Time-bound approval to accept a defined non-critical gap with compensating control | Cannot override law or a critical production blocker |
| Suspension | Controlled removal of new traffic or availability after readiness degrades | Historical access and reconciliation may still be required |

## Regulatory evidence and confidence

This section records product implications, not legal conclusions. The official publication and Sage legal/compliance interpretation take precedence.

| ID | Source | Confirmed product-relevant finding | Confidence/limitation | Control impact |
|---|---|---|---|---|
| E1 | [Ley 18/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818) | Establishes the mandatory B2B e-invoicing framework and interoperability/interconnection direction | Primary law; implementation depends on later regulation | Legal scope, customer coverage, timing and interoperability register |
| E2 | [Real Decreto 238/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), Articles 5–13 | Defines the Spanish public/private system, entry points, syntaxes, interconnection, public solution and private-platform requirements | Primary regulation; formal legal interpretation still required | Most readiness domains in this PRD |
| E3 | Real Decreto 238/2026, Article 7 | Admitted structured syntaxes include CII, UBL, EDIFACT invoice and Facturae; private platforms require exchange/transformation capability | Confirmed at regulation level; profiles and technical detail may be expanded | Format, transformation and conformance controls |
| E4 | Real Decreto 238/2026, Articles 5–6 | Businesses may publish private receipt entry points; absent a published entry point, the public solution is the default | Confirmed at regulation level | Directory/lookup, route authority and coexistence controls |
| E5 | Real Decreto 238/2026, Articles 8–9 | Private-platform interconnection and associated process/conditions are mandatory system outcomes | Confirmed at regulation level; operational details require interpretation/specification | Interconnection request, testing, activation, support and evidence |
| E6 | Real Decreto 238/2026, Article 13 | Private-platform requirements include public-solution connectivity, ISO/IEC 27001 or equivalent, AS2/AS4 secure transport, advanced signature/seal capability, all admitted syntaxes and transformation, BCP, service/support availability, data governance/confidentiality and free interoperability | Confirmed regulation-level requirements; scope/equivalence and measurable operation need formal approval | Security certification, protocol, trust, transformation, BCP, support and data controls |
| E7 | Real Decreto 238/2026, Article 9 | Operators must accept qualifying interconnection requests; the regulation defines a one-month operating period subject to queueing rules, a test-bank/resource duty, public-solution bridging before direct interconnection, and no charge to the requesting platform | Confirmed regulation-level process; detailed technical execution remains to be evidenced | Request queue, deadline, test bank, bridging, evidence and commercial controls |
| E8 | Real Decreto 238/2026, Articles 11–12 | The public solution is managed by AEAT; its UBL, authentication, download and payment/rejection services depend in part on ministerial-order specifications | Confirmed regulation-level design with an open technical dependency | Public-copy, consultation, payment/status and authorisation controls |
| E9 | Real Decreto 238/2026, final provisions | Effective application is tied to the ministerial order for the public solution, with staged periods | Confirmed dependency; do not infer a calendar date until the order status is verified | Regulatory-change monitoring and launch gate |
| E10 | PRD-SEI-210 strategy context | Sage seeks a credible private-platform proposition while retaining public and existing-provider choice | Internal product hypothesis/decision context | Customer proposition and delivery-model controls |

### Evidence caveats

- BOE consolidated pages state that consolidated text is informative; legal review should use the official publication and current amendments.
- The detailed public technical contract, conformance process and some operational interpretation may depend on the ministerial order and subsequent official material.
- “Resources of support available at all times” must be translated into measurable coverage by legal and operations; this PRD does not equate the phrase to an invented SLA.
- A partner's existing operator status or certification does not prove that the Sage-branded service, data flow, countries, environments and support chain are covered.

## Actors and accountability

| Actor | Readiness responsibility |
|---|---|
| Executive/Phase 3 sponsor | Accepts investment and residual risk; appoints decision authority |
| Sage proposition owner | Owns customer outcome, scope, eligibility and gate recommendation |
| Legal operator | Demonstrates platform controls and accepts defined statutory/operational responsibilities |
| Sage product/platform teams | Implement and evidence shared product, routing, lifecycle, security and operational controls |
| Local legal/compliance | Interpret official obligations, approve control applicability and track regulatory change |
| Security/privacy | Approve trust boundary, data roles, threats, access, certificates, incidents and evidence |
| Operations/support | Prove monitoring, runbooks, staffing, reconciliation, incident and customer communication |
| Partner/procurement | Convert partner claims into enforceable service, evidence, audit and exit commitments |
| QA/conformance | Maintain test corpus and demonstrate internal/external validation |
| Customer/pilot participant | Provides authorised configuration and validates understandable outcomes and recovery |
| Counterparty platform/public solution | Supplies external interoperability and conformance evidence |

## Proposed readiness state model

The names are proposed; the behavioural distinctions are required.

| State | Meaning | Permitted next states |
|---|---|---|
| `EVIDENCE_MISSING` | Control applies but required evidence or owner is absent | `ASSESSED` |
| `ASSESSED` | Applicability, owner, risk and evidence plan are agreed | `DESIGN_APPROVED`, `EVIDENCE_MISSING` |
| `DESIGN_APPROVED` | Control design and responsibility are approved | `IMPLEMENTED` |
| `IMPLEMENTED` | Control exists in the scoped environment with internal evidence | `EXTERNALLY_VALIDATED`, `DESIGN_APPROVED` |
| `EXTERNALLY_VALIDATED` | Required external/conformance evidence has passed | `PILOT_READY`, `IMPLEMENTED` |
| `PILOT_READY` | All pilot-critical controls pass for the named cohort and operating model | `PRODUCTION_READY`, `SUSPENDED` |
| `PRODUCTION_READY` | Production-critical controls, operations and approvals pass | `SUSPENDED` |
| `SUSPENDED` | New activity is disabled or restricted because readiness degraded | Prior approved state only after recovery/re-approval |

Readiness must be scoped by operator, environment, capability, direction, syntax/profile, Sage product/cohort and effective period. A single global boolean is insufficient.

## Readiness domains and control register

| Domain | Required outcome | Minimum evidence | Critical gate |
|---|---|---|---|
| Legal entity and accountability | Operator, proposition owner, customer contract and liability are unambiguous | Legal opinion/approval, entity/contract map, ADR responsibility matrix | Before implementation commitment/pilot |
| Regulatory applicability/change | Current obligations, exclusions, dependencies and effective dates are monitored | Source register, legal interpretations, change owner and impact process | Every gate |
| Operator registration/qualification | Named operator can participate for the scoped service | Authority/process evidence or approved route to qualification | Before external pilot |
| Customer authority/eligibility | Customer selection and data processing are authorised and auditable | Eligibility rules, consent/authority record, terms and revocation journey | Before activation |
| Entry point and lookup | Customer receipt choice is published, discoverable and reconciled | Lookup API/process evidence, authoritative source, propagation and rollback tests | Before inbound pilot |
| Formats/transformation | All scoped admitted syntaxes are received, emitted and transformed without material loss | Versioned profiles, mapping, conformance corpus, round-trip/loss analysis | Before relevant syntax activation |
| Trust/signature/seal | Origin/integrity controls and credentials are governed | Approved trust model, custody, rotation, revocation and validation evidence | Before invoice exchange |
| Public connectivity/copy | Required information reaches the public solution and can be proved/reconciled | Contract/spec version, correlation, idempotency, unknown-outcome and reconciliation tests | Before outbound pilot |
| Platform interconnection | Requests, testing, activation, exchange and failure escalation work with other platforms | Process, test bank, counterpart evidence, directory and operational contacts | Before general availability |
| Lifecycle/payment reporting | Required statuses reach the right parties in order without corrupting history | Authority/mapping rules, dedupe/order tests, public/counterparty acknowledgements | Before lifecycle activation |
| Security/privacy/data | Data, credentials, access, retention and incidents are controlled across parties | Threat model, DPIA/assessment, roles, controls, test and approval evidence | Before pilot/production |
| BCP/availability/support | Service degradation, continuity and customer support are operational | Capacity model, BCP, exercises, staffing, SLAs/OLAs, runbooks and incident command | Before pilot/production |
| Observability/reconciliation | Intended and observed state can be compared and repaired safely | Metrics, traces, cases, redacted evidence, safe actions and reconciliation tests | Before pilot |
| Supplier/partner assurance | Delegated controls are enforceable and continuously evidenced | Due diligence, contract, audit rights, reporting, subcontractor and change controls | Before partner commitment/pilot |
| Retention/audit/exit | Evidence and historical lifecycle survive route/model change and termination | Retention approvals, export, transition assistance, credential revocation and exit test | Before production |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Sage presents the service as its private-platform option | Name the legal operator and Sage accountability in product, contract and support material | Proposed governance rule; ADR decision required |
| BR2 | No private receipt entry point is publicly identified | Treat the public solution as the default receipt entry point | Regulation-level finding; implementation authority to confirm |
| BR3 | Customer selects a private receipt route | Activation requires authorised selection plus confirmed external readiness | Proposed control derived from entry-point duties |
| BR4 | A current route changes | Existing invoices keep original provider/network, syntax, signature and lifecycle context | Existing product continuity principle |
| BR5 | A mutating external request has an ambiguous outcome | Reconcile observed state before unsafe resubmission | Existing resilience requirement |
| BR6 | A partner supplies an operator control | Sage requires current evidence, operational access and enforceable audit/exit rights | Proposed governance rule |
| BR7 | An official technical dependency is unresolved | Do not invent a production contract or declare the affected control ready | Confirmed dependency |
| BR8 | A critical control fails or expires | Prevent new affected activity and enter a controlled suspended/degraded mode | Proposed safety rule |
| BR9 | A waiver is requested | Legal obligations and critical safety controls cannot be waived; other waivers are scoped, time-bound and approved | Proposed governance rule |
| BR10 | Operator or partner changes | Re-run applicable readiness controls and preserve customer/history continuity | Proposed governance rule |
| BR11 | A qualifying private-platform interconnection request is received | Accept, queue and make the interconnection operational within the applicable statutory process; provide the required test capability and do not charge the requesting platform for the interconnection | Regulation-level finding; operational interpretation required |

## Detailed readiness journeys

### J1 — Establish the control register

1. Local legal/compliance records the official source, article/topic, applicability and interpretation owner.
2. Product maps the obligation or risk to a customer/operational outcome.
3. The delivery model assigns one accountable and one operationally responsible party.
4. Control owner records design, implementation, test, evidence location, expiry and review trigger.
5. Independent reviewers approve or return the control with explicit gaps.

**Expected result:** every material obligation and readiness risk is traceable to an owned, reviewable control.

### J2 — Validate a customer entry point

1. An authorised customer selects the Sage private route for a defined direction/scope.
2. Eligibility, operator subscription, credentials and endpoint readiness are validated without changing the active route.
3. The entry point is published/registered through the authoritative mechanism.
4. Sage independently observes the published state and records evidence and propagation time.
5. Only after observed readiness matches intended state does route activation occur.

**Expected result:** new inbound traffic is enabled only after externally observable readiness; failure leaves the previous route intact.

### J3 — Prove format transformation and exchange

1. QA selects a versioned test invoice for each scoped admitted syntax/profile and edge case.
2. The operator validates origin, integrity and business rules.
3. Where transformation is required, the service records input/output syntax, mapping version and any controlled loss decision.
4. The receiving platform validates the output and returns correlated evidence.
5. Semantic comparison proves mandatory information and identifiers remain intact.

**Expected result:** transformation is demonstrably interoperable, explainable and versioned—not inferred from a successful HTTP response.

### J4 — Reconcile an ambiguous public-copy outcome

1. The operator transmits a required public copy and times out after transmission.
2. The operation enters `OUTCOME_UNKNOWN`; no blind duplicate is sent.
3. Reconciliation queries or correlates the public state using stable identifiers.
4. If found, Sage records success and evidence; if absent and safe, the same idempotent operation resumes.
5. If state remains unknown, an operational case is raised with redacted evidence and customer-safe messaging.

**Expected result:** public evidence becomes consistent without duplicate or contradictory invoice history.

### J5 — Complete external interconnection validation

1. The authorised platform-to-platform request is recorded with customer basis and named contacts.
2. Parties exchange supported syntax/profile, security, endpoint and test information.
3. Positive, rejection, duplicate, out-of-order, unavailable and recovery scenarios are tested.
4. Intended and observed readiness is recorded by both parties.
5. Activation occurs for the approved scope; the support and suspension path is communicated.

**Expected result:** interconnection is an operational capability with evidence, not a bilateral happy-path demonstration.

### J6 — Handle a control gap or waiver

1. A reviewer records the failed/missing evidence, affected scope and customer/regulatory risk.
2. Legal/compliance decides whether the control is legally mandatory or critical.
3. Mandatory/critical gaps block the relevant gate.
4. A non-critical gap may receive a time-bound waiver with compensating control, approver and expiry.
5. Expiry without closure automatically removes the waiver and re-evaluates readiness.

**Expected result:** gaps remain visible and cannot be converted into indefinite acceptance.

### J7 — Suspend and recover service readiness

1. Monitoring, regulatory change or an incident identifies that a critical control is no longer effective.
2. The affected operator/environment/capability enters `SUSPENDED` or a controlled degraded state.
3. New affected activity stops or follows an explicitly approved safe route; historical access and reconciliation continue where required.
4. Operations communicates impact, owns recovery and preserves evidence.
5. Independent re-validation and approval are required before traffic resumes.

**Expected result:** readiness degradation is controlled without deleting history or silently rerouting traffic.

## Functional requirements

### Governance and evidence

| ID | Requirement |
|---|---|
| FR1 | Maintain a versioned control register linking official source or approved risk to outcome, control, owner, evidence, scope, state, expiry and review trigger. |
| FR2 | Identify the legal operator, proposition owner, responsible service owner and approver for every production-critical control. |
| FR3 | Distinguish supplier assertion, documented design, implemented control, internal test, contractual commitment and external validation. |
| FR4 | Prevent a readiness state from advancing when mandatory evidence, owner or approval is absent. |
| FR5 | Record every waiver with scope, rationale, compensating control, approver and automatic expiry. |
| FR6 | Maintain an auditable history of control, evidence, approval, waiver, suspension and reactivation changes. |

### Customer and route readiness

| ID | Requirement |
|---|---|
| FR7 | Validate customer eligibility, authority, subscription and direction/scope before establishing a private-platform entry point. |
| FR8 | Separate configured, externally observed and active route state. |
| FR9 | Activate a route only when required internal and external readiness controls pass. |
| FR10 | Preserve the previous safe route when new entry-point publication or validation fails. |
| FR11 | Reconcile discrepancies between Sage intent and the authoritative external entry-point/lookup state. |
| FR12 | Preserve invoice-origin context and required historical lifecycle when a route, operator or partner changes. |

### Exchange and interoperability

| ID | Requirement |
|---|---|
| FR13 | Maintain versioned capability coverage by direction, document type, syntax/profile, operator, environment and counterparty route. |
| FR14 | Validate admitted input and output syntaxes against the approved versioned specifications. |
| FR15 | Record transformation provenance, mapping version, input/output syntax and validation evidence for every transformed invoice. |
| FR16 | Prevent activation of a syntax/profile until semantic preservation and required external conformance tests pass. |
| FR17 | Govern operator certificates, signatures and seals with approved ownership, storage, use, rotation, revocation and audit controls. |
| FR18 | Correlate private exchange, public copy, interconnection and lifecycle evidence using stable identifiers. |
| FR19 | Support idempotent or reconciliation-first handling for every mutating external operation according to its proven safety classification. |
| FR20 | Maintain a tested platform-interconnection process covering request, receipt timestamp, queue position, statutory deadline, authentication, test-bank access, conformance, public-solution bridging, activation, incident, suspension, termination and evidence that no prohibited interconnection charge was applied. |

### Lifecycle and operations

| ID | Requirement |
|---|---|
| FR21 | Define authoritative sources, ordering, deduplication and conflict behaviour for technical, rejection, acceptance and payment events. |
| FR22 | Show intended and observed state for customer route, operator connection, public copy and interconnection. |
| FR23 | Provide redacted correlation and evidence sufficient to distinguish Sage, customer, operator, public-platform and counterparty faults. |
| FR24 | Permit only authorised, safe and audited manual recovery actions. |
| FR25 | Enter controlled suspension/degradation when a critical control expires or fails, without deleting historical evidence. |
| FR26 | Continue required reconciliation and historical lifecycle work during suspension or operating-model transition. |
| FR27 | Revalidate affected controls before resuming activity after suspension. |
| FR28 | Test partner and operating-model exit while preserving customer configuration, history, evidence and a viable transition route. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | Encrypt credentials, certificates and invoice data in transit and at rest using approved controls. |
| NFR2 | Enforce least privilege, separation of duties and environment/tenant isolation for configuration, evidence and recovery actions. |
| NFR3 | Keep production credentials and customer data out of PRDs, repositories, test fixtures and support exports. |
| NFR4 | Establish performance, capacity, queue/backpressure and recovery targets from an approved volume model; do not infer them from pilot traffic. |
| NFR5 | Make every external operation observable through stable correlation without exposing invoice content unnecessarily. |
| NFR6 | Define retention, residency, access, deletion and legal-hold rules with legal/privacy approval and partner alignment. |
| NFR7 | Exercise BCP, disaster recovery, incident command and reconciliation at a frequency approved for the service risk. |
| NFR8 | Provide accessible, plain-language customer states that distinguish pending, rejected, degraded and action-required outcomes. |
| NFR9 | Version external specifications, mappings, controls and evidence so an invoice outcome remains historically explainable. |
| NFR10 | Monitor control/evidence expiry and regulatory-source change with named escalation. |
| NFR11 | Ensure partner dependencies provide equivalent telemetry, evidence timeliness and escalation sufficient for Sage's accountable role. |
| NFR12 | Define measurable availability and support coverage only after legal interpretation, risk assessment and operating-model approval. |

## Failure and recovery matrix

| Failure | Expected system/operational response | Gate implication |
|---|---|---|
| Operator identity/accountability unresolved | Stop decision/pilot; escalate to ADR decision owner | Blocks pilot and production |
| Official technical specification unavailable | Maintain dependency; use no irreversible production assumption | Blocks affected external validation/production |
| Entry point published but not observable | Keep previous route; reconcile and raise case | Blocks inbound activation |
| Transformation validation loses material data | Quarantine test/traffic; correct mapping/version; repeat conformance | Blocks syntax/profile |
| Certificate expires or is revoked | Stop affected signing/exchange; alert; use approved rotation/recovery | May suspend affected service |
| Timeout after public-copy mutation | Enter outcome unknown; reconcile before retry | Blocks readiness if untested |
| Duplicate/out-of-order lifecycle event | Dedupe/order by stable identity; retain audit and conflict evidence | Blocks lifecycle activation if unsafe |
| Counterparty platform unavailable | Queue/degrade according to approved policy; communicate and reconcile | Requires tested BCP/support path |
| Partner cannot provide evidence during incident | Invoke contractual escalation; restrict/suspend affected activity | Material supplier-control failure |
| Critical control evidence expires | Automatically re-evaluate and suspend affected scope if not renewed | Blocks continued readiness |
| Sage/partner observed state diverges | Open reconciliation case; prevent unsafe mutation; preserve both observations | Blocks activation/resumption |
| Partner/model exit begins | Execute transition plan; preserve historical lifecycle and evidence | Must be tested before production |

## Product and operational experience

### Customer/product experience

The Sage product should expose only meaningful readiness outcomes: configured, validation required, ready, activation pending, active, degraded, suspended or action required. It should explain which direction/scope is affected and whether existing invoices continue. It must not expose internal control jargon or imply that “connected” means externally reachable.

### Operations experience

Operations requires:

- operator/environment health and control-expiry view;
- intended versus observed entry point, route and interconnection state;
- correlated invoice/public-copy/status evidence;
- safe retry/reconcile/disable actions with permissions and audit;
- supplier/public/counterparty fault classification;
- runbooks, incident command and customer communication templates;
- evidence export that is redacted and access-controlled;
- regulatory change and readiness review queue.

## Rollout and readiness gates

| Gate | Required evidence | Exit condition |
|---|---|---|
| R0 — Discovery governed | Sponsor, legal/compliance owner, operator candidates, source register and control template | Owners accept the assessment plan |
| R1 — Model feasible | ADR option shortlist, preliminary accountability, FP-SEI-001 gaps and regulatory interpretations | No unresolved fatal operating-model contradiction |
| R2 — Design approved | Architecture/security/privacy/operations designs and supplier contracts map to all critical controls | Critical designs approved; evidence plan funded |
| R3 — Internally implemented | Scoped capabilities, environments, test corpus, observability, runbooks and BCP exist | Internal happy/failure/recovery tests pass |
| R4 — Externally validated | Required public/counterparty/interconnection/conformance evidence passes | External evidence attached and approved |
| R5 — Pilot ready | Named cohort, support cover, kill criteria, fallback, customer terms and incident plan approved | Pilot authority granted for explicit scope |
| R6 — Production ready | Production capacity, security, legal, operational, commercial and exit approvals pass | Production authority granted for explicit scope |
| R7 — Ongoing assurance | Evidence remains current; incidents, changes and exercises are reviewed | Readiness retained or affected scope suspended |

## Acceptance criteria

- Given a proposed operator, when the pilot gate is reviewed, then the legal operator, Sage proposition owner, customer-contracting entity and incident accountabilities are named and approved.
- Given a customer configuring private inbound, when entry-point publication cannot be externally observed, then the current route remains unchanged and an actionable reconciliation case is created.
- Given each activated syntax/profile, when the conformance corpus is run, then validation and transformation preserve required semantic information and record mapping provenance.
- Given a timeout after a public-copy submission, when recovery runs, then the service reconciles the external outcome before any unsafe retry and preserves correlated evidence.
- Given an interconnection candidate, when external validation occurs, then happy, rejection, duplicate, unavailable and recovery scenarios pass for the approved scope.
- Given a critical certificate or control expires, when monitoring detects it, then new affected activity is stopped or safely degraded, customers/operations are informed and historical evidence remains accessible.
- Given a partner-operated control, when Sage requests incident or audit evidence, then the evidence is available within the approved contractual/operational process and is sufficient to explain the customer outcome.
- Given a partner/model exit exercise, when the transition is executed, then customer configuration, invoice history, audit evidence and the approved alternative route remain usable.
- Given an unresolved ministerial-order dependency, when production readiness is reviewed, then affected controls remain blocked rather than relying on an assumed endpoint or date.

## Measures

Targets and measurement windows require owners after the pilot baseline is defined.

| Measure | Purpose | Target owner |
|---|---|---|
| Critical controls with current approved evidence | Core readiness completeness | Compliance/product |
| Controls by readiness state and expiry horizon | Shows progress and emerging risk | Programme governance |
| External conformance scenarios passed | Demonstrates interoperability breadth | QA/operator |
| Entry-point intent/observed discrepancies | Measures routing control health | Platform operations |
| Outcome-unknown cases and age | Measures external mutation/reconciliation safety | Operations/engineering |
| Time to detect, classify and recover operator incidents | Measures operating effectiveness | Operations |
| Supplier evidence exceptions | Measures delegated-control health | Supplier assurance |
| BCP/exit exercises passed | Demonstrates continuity and portability | Operations/product |
| Customer support contacts by readiness/failure category | Identifies confusing journeys and control gaps | Product/support |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Readiness becomes a checklist without effective evidence | Require observable tests, expiry, independent approval and recurring review |
| Partner qualification is assumed to cover Sage's proposition | Scope evidence by service, data flow, environment, product and responsibilities |
| Regulation changes during delivery | Maintain official source register, change triggers and re-assessment workflow |
| “At all times” support is translated into an arbitrary SLA | Obtain formal legal/operations interpretation, then contract and test measurable coverage |
| Public/counterparty external test access arrives late | Treat external validation as an early programme dependency and gate |
| Reuse assessment underestimates operator gaps | Link FP-SEI-001 decisions to every relevant readiness domain |
| Customer route is activated before external state propagates | Separate configured, observed and active state; keep previous route until validated |
| Data/evidence becomes inaccessible through a partner | Contract audit/export/retention rights and test exit before production |
| Suspension creates invoice loss | Preserve queues/history, apply safe routing policy and continue reconciliation |
| A single global readiness flag hides partial coverage | Scope state by operator, environment, direction, syntax/profile and cohort |

## Dependencies

- Approved owner and decision forum for Phase 3.
- ADR-SEI-001 delivery-model and accountability decision.
- FP-SEI-001 evidence-backed reuse and gap assessment.
- Current official ministerial order and public technical specifications when published/applicable.
- Named legal/compliance interpretation owners.
- Operator/partner sandbox, conformance, security and operational evidence.
- Public solution and counterparty platform test access.
- Approved customer segment, Sage product cohort and volume model.
- Security, privacy, supplier assurance, operations and commercial approvals.

## Open questions and consultation owners

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Which entity will be the legal private-platform operator? | Determines most responsibilities and evidence | Executive/legal sponsor | R1 onward | Open via ADR-SEI-001 |
| What process evidences operator qualification/registration? | Defines external readiness path | Local legal/compliance | R4/pilot | Official confirmation required |
| What is the authoritative entry-point publication/lookup mechanism and propagation model? | Controls inbound activation and reconciliation | Local technical/regulatory team | R3/R4 | Open |
| Which technical profiles, APIs and test suites will the ministerial order define? | Determines implementation and conformance | Local technical/regulatory team | R3/R4/production | Track official publication |
| How should “support resources available at all times” be measured? | Drives staffing, partner SLA and cost | Legal/operations | R2/R5 | Formal interpretation required |
| Which lifecycle/payment event is authoritative when platforms disagree? | Prevents contradictory history | Local team/legal/product | R3/R4 | Preserve source observations; approved precedence required |
| What are the statutory/contractual evidence and invoice retention periods? | Drives data model and exit | Legal/privacy | R2/production | Do not invent duration |
| Can both public and private receipt registrations coexist, and at what granularity? | Determines route/entry-point model | Local technical/regulatory team | R2/R4 | Product model should support coexistence pending confirmation |
| Which party owns older invoices and lifecycle after an operator switch? | Determines credential/evidence continuity | Legal/product/operator | R2/production | Preserve original operator context; responsibility requires approval |
| What are the authoritative cutover, rollback and deregistration sequences? | Prevents unreachable customers and lost traffic | Local team/operator/architecture | Pilot | Validate new observed state before releasing prior route where permitted |
| Which controls may a partner evidence on demand versus Sage retaining directly? | Affects audit, incident and exit | Security/legal/operations | Contract/R5 | Sage needs reliable access for customer-facing accountability |

## Recommended next actions

1. Assign the Phase 3 compliance product owner and legal interpretation owner.
2. Convert the readiness-domain table into the governed control register with evidence links and expiry.
3. Confirm the current status of the ministerial order and official technical/conformance material.
4. Map every ADR-SEI-001 option to the accountability and supplier-control rows.
5. Select one outbound/public-copy and one inbound/interconnection reference journey for early external validation.
6. Define pilot-critical versus production-critical controls only after legal, security and operations review.
7. Schedule a BCP and partner/model exit tabletop before commercial commitment.

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial discovery PRD for Phase 3 operator readiness and regulatory governance | Official BOE sources, PRD-SEI-210 and Phase 1/2 foundations |
