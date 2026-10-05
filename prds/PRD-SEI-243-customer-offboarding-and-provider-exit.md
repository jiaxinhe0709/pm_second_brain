---
id: PRD-SEI-243
title: Customer Offboarding and Provider Exit
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-10-05
updated: 2026-10-05
reviewers: []
related:
  - PRD-SEI-222
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-231
  - PRD-SEI-201
  - ADR-SEI-001
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "876576919"
  page_id: "918651071"
  title: Customer Offboarding and Provider Exit
  layout: two_left_sidebar
  toc: true
---

# Customer Offboarding and Provider Exit

## Decision summary

An authorised Spanish business must be able to leave the Sage e-invoicing service, move an inbound or outbound scope to another eligible route, or stop using a provider without losing invoice reachability, unfinished obligations, or evidence. The customer must see what changes for new invoices and what remains available for older ones. Sage must be able to prove the actual handover and later disposition of each connection, registration, credential, subscription, and data set.

**Product principle:** Prove the destination and account for existing invoices before releasing the previous route. Exit is complete only when every continuing obligation has an owner and every remaining access or data item has an approved purpose.

This is a **draft for consultation**, not an approved Spanish regulatory interpretation or operational runbook. In particular, who may execute post-switch Article 10 and Article 12 actions, the authoritative entry-point change sequence, and retention periods remain open.

## Relationship to existing work

This is a new, focused PRD. [PRD-SEI-222](PRD-SEI-222-customer-onboarding-entry-point-migration.md) owns route choice, onboarding, migration and its high-level switch-out journey. [PRD-SEI-224](PRD-SEI-224-lifecycle-rejection-payment-reporting.md) owns invoice events and reporting obligations. [PRD-SEI-225](PRD-SEI-225-operations-resilience-support-reconciliation.md) owns shared cases and recovery. [PRD-SEI-226](PRD-SEI-226-security-trust-identity-data-audit.md) owns authority, credentials, retention and audit controls. This PRD specifies the customer exit case and the gates connecting those capabilities; it does not replace their source-of-truth requirements.

The France experience is a reason to test exit early, but no France incident record or agreed lessons were available in the repository review. A France lessons review is a discovery input, not asserted evidence for any particular failure mode here.

## Outcome, phases and scope

| Stage | Customer outcome | Delivery boundary |
|---|---|---|
| Discovery and provider validation | The customer and Sage can identify the route, invoices, obligations, data and provider actions that exit affects | Confirm legal/provider rules, contracts, interfaces and operating ownership before automation |
| Controlled pilot | One authorised legal entity can switch out or terminate a scoped service with an observed cutover and an auditable handover | Supported route/provider combinations only; manual gates permitted when evidenced |
| Production | Repeatable scoped and full exit, recovery, export and disposition across supported providers | Expand only after route, lifecycle, security and support gates pass |

### Problem and value

An offboarding request may arrive while invoices are being delivered, counterparties still resolve an old inbound entry point, or an older invoice still needs a rejection, payment report, correction or audit response. If subscription cancellation, route deactivation and external deregistration are collapsed into one action, the customer can become unreachable or lose the means to fulfil a continuing obligation. If everything is retained indefinitely, Sage and the provider incur avoidable access, privacy and cost exposure.

The business outcome is a predictable customer exit, clear support ownership, lower lock-in risk, and evidence that Sage has neither abandoned historical work nor held access without purpose. The operational outcome is a case that can be reconciled after partial or ambiguous external actions.

### In scope

- Customer-initiated switch from Sage to the public solution or another supported private platform; switch from an external provider where Sage coordinates the exit; and full Sage service termination.
- Per-legal-entity, direction and approved scope exit, including multi-entity customers and delegated accountants.
- Inbound reachability, outbound cutover, in-flight invoices, historical lifecycle and public-reporting obligations.
- Evidence export, residual access, credential revocation, registration/entry-point withdrawal, subscription termination and data disposition gates.
- Planned, cancelled, failed, ambiguous and urgent exits, including provider unavailability.
- Product/API status, operations case, customer communication, partner obligations and audit.

### Out of scope

- Inventing a Spanish statutory deregistration, transfer or retention period where the cited law does not specify one.
- Rewriting or resending historical invoices merely because the provider changes.
- Building a universal provider endpoint or assuming every provider supports automated deregistration or cross-provider historical operations.
- Resolving commercial disputes or deciding whether a customer should cancel its wider Sage product.
- Publishing to Confluence or changing any existing PRD's lifecycle or approved policy.

## Terms and business boundaries

| Term | Meaning in this PRD | Separate from |
|---|---|---|
| Switch-out | Move a defined new-traffic scope to another route | Full customer termination |
| Offboarding | End a customer's Sage e-invoicing relationship for the defined legal entity/service | One route deactivation |
| Effective cutover | Evidenced boundary after which eligible new traffic uses the destination | Time a user clicked “cancel” |
| Entry-point withdrawal | Remove or change a publicly discoverable private receiving destination | Outbound provider selection |
| Deregistration | End a provider or network registration under its verified contract | Sage subscription cancellation |
| Historical obligation | Action or evidence still needed for an invoice created before cutover | Permission to send a new invoice on the old route |
| Disposition | Approved export, continued retention, deletion or legal hold by data class | Immediate deletion on cancellation |

## Actors and business scenarios

| Scenario | Initiator and scope | Required outcome | Special risk |
|---|---|---|---|
| Switch outbound only | Authorised business administrator; one entity | New outbound invoices use the approved destination; inbound and historical context remain | A generic “disconnect” could stop inbound |
| Switch inbound only | Authorised administrator; receiving entry point | Destination is externally reachable and publicised before old receipt is withdrawn | Counterparties keep sending to stale entry point |
| Full exit | Authorised administrator or contracted termination process | New traffic stops safely; obligations, archive, access and financial terms are handed over | Premature credential deletion |
| Accountant-managed exit | Business or validated delegate | Action is restricted to granted legal entity, capability and validity | Delegate authority may not transfer to new provider |
| Urgent provider failure | Operations with incident authority and customer communication | Preserve evidence and use an approved prospective route; unresolved history enters a case | Blind retry or unsupported historical transfer |
| Reversed request | Authorised administrator before irreversible external step | Cancel or restore last known safe state with actual invoice attribution | “Rollback” may not undo external publication |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | An exit is requested | Verify legal entity, actor authority, affected direction/scope and intended destination before mutation | Proposed control; PRD-SEI-222/231 |
| BR2 | New route will receive invoices | Do not release the last known safe receiving path until destination readiness and effective external state are evidenced, subject to confirmed Spanish and provider rules | Proposed control; RD 238/2026 Art. 6; sequence open |
| BR3 | Route changes | Preserve each invoice's original route, provider, identifiers, representation and obligation context | Established platform principle; PRD-SEI-222/224/231 |
| BR4 | Invoice or reporting obligation is unfinished | Assign a permitted executing actor and available channel before removing access needed for that obligation | Proposed control; execution authority open |
| BR5 | External mutation outcome is unknown | Reconcile observed state before retrying, claiming exit completion or releasing the previous route | Established platform principle; PRD-SEI-225 |
| BR6 | Commercial subscription ends | Route, registration, credential, historical access and data disposition change only at their own authorised gates | Established platform principle; PRD-SEI-222/226 |
| BR7 | Customer requests deletion | Apply approved retention, legal hold, privacy and contract rules by data class; record disposition outcome | Proposed control; exact periods open |
| BR8 | No eligible destination or no validated authority | Block the affected cutover, explain the reason and retain the safe route or invoke an approved incident path | Proposed control |

## Research and evidence register

| Source | What it establishes | Limit / impact |
|---|---|---|
| [Spain RD 238/2026, consolidated BOE text](https://www.boe.es/eli/es/rd/2026/03/25/238/con), reviewed 2026-10-05, Arts. 6, 9–13 and final provision 4 | Public/private route choice; private receiving entry-point publicity and operator lookup; interconnection; invoice status and public payment/rejection reporting; operator controls; staged effective application | It does not supply a complete customer/provider exit procedure, provider API or data-retention schedule. Validate the effective implementing order and technical rules before pilot. |
| [PRD-SEI-222](PRD-SEI-222-customer-onboarding-entry-point-migration.md), current Git source | Switch-out journey, separate route/registration/subscription states and open historical-ownership decisions | Discovery hypotheses require Spain local review. |
| [PRD-SEI-224](PRD-SEI-224-lifecycle-rejection-payment-reporting.md), current Git source | Article 10 and 12 obligations must be tracked independently with invoice-origin context | Permitted post-switch actor and interface remain open. |
| [PRD-SEI-225](PRD-SEI-225-operations-resilience-support-reconciliation.md) and [PRD-SEI-226](PRD-SEI-226-security-trust-identity-data-audit.md), current Git sources | Reconciliation-first operations, scoped access, evidence, credential and data governance | Do not infer approved retention duration, recovery SLA or provider capability. |
| France offboarding experience | Stakeholder concern supplied with this request | Specific incidents, causes and controls have not yet been captured; no claims are derived from it. |

**Interpretation:** The decree creates obligations that continue to matter after a route switch; the staged handover described below is a product control inferred from those obligations and existing Sage design principles. It is not presented as a statutory sequence.

## Proposed exit case and lifecycle

The **proposed** `ExitCase` records legal entity, actor and authority evidence, request type, inbound/outbound scope, old and destination routes, intended and observed external state, cutover boundary, affected invoice inventory, obligation owners, evidence-export manifest, credential/registration/subscription/data gates, communication history and approvals. Each external operation has a stable logical request ID and evidence reference. Invoice records retain their original provider context; the case references them without changing it.

The case progresses through `requested → assessed → destination_ready → cutover_pending → cutover_observed → historical_continuity → release_pending → completed`. `blocked`, `outcome_unknown`, `cancelled` and `manual_recovery` are explicit branches. State names and storage shape require architecture review; the observable gates are product requirements.

### Exit and handover visual

<!-- confluence-html-macro:start -->
<div class="p3exit-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3exit-visual *{box-sizing:border-box}.p3exit-visual h3{margin:0;color:#172b4d;font-size:18px}.p3exit-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px;line-height:1.45}.p3exit-visual svg{display:block;width:1120px;height:390px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3exit-visual .node{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3exit-visual .done{fill:#e3fcef;stroke:#00875a;stroke-width:2}.p3exit-visual .title{fill:#172b4d;font-size:12px;font-weight:700}.p3exit-visual .copy{fill:#42526e;font-size:10px}.p3exit-visual .label{fill:#6b778c;font-size:10px;font-weight:700;letter-spacing:.08em}.p3exit-visual .path{fill:none;stroke:#00875a;stroke-width:2}.p3exit-visual .arrow{fill:#00875a}.p3exit-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1120px;margin-top:12px}.p3exit-visual .note{padding:10px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:11px;line-height:1.45}.p3exit-visual .note strong{display:block;color:#172b4d;margin-bottom:3px}.p3exit-visual .hold{border-left:3px solid #de350b}.p3exit-visual .unknown{border-left:3px solid #ffab00}.p3exit-visual .history{border-left:3px solid #7a869a}
  </style>
  <h3>Prove the destination before releasing the previous route</h3>
  <p class="sub">Proposed customer-exit control flow. Each gate requires observed evidence; this is not a prescribed Spanish statutory sequence.</p>
  <svg viewBox="0 0 1120 390" role="img" aria-label="Proposed customer offboarding flow: authorise the exit, inventory invoices and obligations, prove the destination, observe the cutover, preserve historical continuity, release the previous route, decide data disposition, and complete the case. A missing destination or uncertain external result holds progress while the last safe route and original invoice evidence are preserved.">
    <text x="32" y="37" class="label">ASSESS AND CUT OVER</text><text x="32" y="225" class="label">PRESERVE, RELEASE AND CLOSE</text>
    <rect x="32" y="70" width="228" height="90" rx="9" class="node"/><text x="50" y="100" class="title">1  Authorise exit</text><text x="50" y="122" class="copy">Legal entity, actor, direction</text><text x="50" y="140" class="copy">and affected scope</text>
    <path d="M260 115 H306" class="path"/><polygon points="306,115 296,109 296,121" class="arrow"/>
    <rect x="308" y="70" width="228" height="90" rx="9" class="node"/><text x="326" y="100" class="title">2  Inventory obligations</text><text x="326" y="122" class="copy">In-flight invoices, reporting,</text><text x="326" y="140" class="copy">evidence and access</text>
    <path d="M536 115 H582" class="path"/><polygon points="582,115 572,109 572,121" class="arrow"/>
    <rect x="584" y="70" width="228" height="90" rx="9" class="node"/><text x="602" y="100" class="title">3  Prove destination</text><text x="602" y="122" class="copy">Eligibility, reachability and</text><text x="602" y="140" class="copy">effective external state</text>
    <path d="M812 115 H858" class="path"/><polygon points="858,115 848,109 848,121" class="arrow"/>
    <rect x="860" y="70" width="228" height="90" rx="9" class="node"/><text x="878" y="100" class="title">4  Observe cutover</text><text x="878" y="122" class="copy">New traffic changes only at</text><text x="878" y="140" class="copy">the evidenced boundary</text>
    <path d="M974 160 V254" class="path"/><polygon points="974,254 968,244 980,244" class="arrow"/>
    <rect x="860" y="256" width="228" height="90" rx="9" class="node"/><text x="878" y="286" class="title">5  Preserve history</text><text x="878" y="308" class="copy">Original provider, obligations</text><text x="878" y="326" class="copy">and permitted execution path</text>
    <path d="M860 301 H814" class="path"/><polygon points="814,301 824,295 824,307" class="arrow"/>
    <rect x="584" y="256" width="228" height="90" rx="9" class="node"/><text x="602" y="286" class="title">6  Release old route</text><text x="602" y="308" class="copy">Withdraw entry point and revoke</text><text x="602" y="326" class="copy">access at separate safe gates</text>
    <path d="M584 301 H538" class="path"/><polygon points="538,301 548,295 548,307" class="arrow"/>
    <rect x="308" y="256" width="228" height="90" rx="9" class="node"/><text x="326" y="286" class="title">7  Decide disposition</text><text x="326" y="308" class="copy">Export, retain or delete by</text><text x="326" y="326" class="copy">approved data-class policy</text>
    <path d="M308 301 H262" class="path"/><polygon points="262,301 272,295 272,307" class="arrow"/>
    <rect x="32" y="256" width="228" height="90" rx="45" class="done"/><text x="50" y="286" class="title">8  Complete exit</text><text x="50" y="308" class="copy">Customer and provider receive</text><text x="50" y="326" class="copy">the evidenced outcome</text>
  </svg>
  <div class="notes"><div class="note hold"><strong>Destination blocked</strong>Keep the last safe route active. Correct and retest before cutover.</div><div class="note unknown"><strong>External result unknown</strong>Observe and reconcile before retrying a mutation or claiming completion.</div><div class="note history"><strong>Historical continuity</strong>Keep a named owner and permitted channel for every unfinished obligation before removing access.</div></div>
</div>
<!-- confluence-html-macro:end -->

| Gate | Evidence required before proceeding | If missing |
|---|---|---|
| G1 Authority/scope | Legal entity, actor authority, affected direction, contract and requested action | Reject or request correction |
| G2 Inventory | In-flight invoices, unresolved delivery, Article 10/12 obligations, archive/export and credentials | Hold release; operations case |
| G3 Destination | Destination eligibility, inbound discoverability if relevant, outbound capability, test result and effective time | Keep last safe route |
| G4 Cutover | Observed external state plus internal effective boundary and customer notice | Reconcile; do not claim complete |
| G5 Historical continuity | Named owner/channel for every open obligation and access/export evidence | Maintain purpose-bound access or approved exception |
| G6 Release | Provider acknowledgement or observed withdrawal, no new traffic on old scope, credential dependency check | Release pending |
| G7 Disposition | Retention/legal hold decision, export receipt, deletion or retained-data schedule | Exit may be operationally cut over but remains open for disposition |

### Detailed journeys

**J1 — Planned switch-out.** (1) Capture request and authority per entity/direction. (2) Inventory active route, published entry point, in-flight invoices and historical obligations. (3) Configure and prove the destination without changing the old route. (4) Agree the cutover boundary, notices and fallback. (5) Change only the authorised new-traffic scope and observe external state. (6) Reconcile in-flight work on its original route. (7) Assign historical obligations, export evidence, then withdraw the old entry point/registration and revoke credentials at approved separate gates. (8) Record customer and provider acknowledgements and close only after disposition is assigned.

**J2 — Full termination without another Sage route.** Identify whether the customer will use the public solution or an external provider for future mandated traffic. Do not imply that ending the Sage subscription fulfils that receiving-route responsibility. Follow G1–G7, stop new Sage traffic at the evidenced boundary, and give the customer an export, historical-access and support statement.

**J3 — In-flight or historical invoice.** An invoice submitted before cutover keeps its original correlation and provider context. If delivery status is unknown, reconcile there before any resend. When a later commercial status, payment report or correction is due, use the confirmed actor/channel for that invoice; if unconfirmed, hold a visible operations case and escalate before removing required access. A newly issued rectifying invoice may use the then-current route only after Spain rules and interface treatment are confirmed.

**J4 — Failure, cancellation or urgent exit.** A failure before cutover leaves the previous route active. An unknown result triggers observation and reconciliation before a second mutation. After cutover, rollback uses a new evidenced transition and does not rewrite invoices already processed. An urgent provider outage preserves queues and evidence, uses an approved prospective route where possible, and handles historical work only through a legally and technically supported path. Customer and support messages distinguish requested, observed and unresolved states.

## Functional requirements

| ID | Requirement |
|---|---|
| OFR1 | On an exit request, the service must identify the legal entity, authorised actor, requested action, affected direction/scope and destination; it must reject mutation when authority or scope is unresolved. |
| OFR2 | Before cutover, the case must present an inventory of in-flight invoices, unresolved external operations, historical lifecycle/reporting obligations, registrations, credentials and retained evidence for the affected scope. |
| OFR3 | Configuring or testing the destination must leave the existing live route unchanged until an authorised cutover succeeds. |
| OFR4 | For inbound scope, activation must require evidence of destination reachability/discoverability and a documented publicity/lookup update plan; the old receiving path must remain until the approved release gate. |
| OFR5 | For outbound scope, the service must record an effective cutover boundary and route new eligible invoices accordingly without changing prior invoice-origin context. |
| OFR6 | Every in-flight invoice with an ambiguous delivery outcome must be reconciled on its original route before any resend or release decision. |
| OFR7 | The case must maintain a per-obligation owner, permitted channel and state for post-switch Article 10 and 12 actions; it must block removal of access still required by an unresolved obligation unless an approved exception names an alternative. |
| OFR8 | External deregistration, entry-point withdrawal, credential revocation, subscription termination and data disposition must be independently authorised, executed and evidenced. |
| OFR9 | A timed-out or uncertain external mutation must enter `outcome_unknown`; the service must obtain observed state or a controlled manual decision before retry or completion. |
| OFR10 | Concurrent requests for overlapping entity/direction/scope must be serialised or rejected with a visible conflict outcome. |
| OFR11 | The customer and support view must distinguish requested, destination-ready, cutover-observed, historical-continuity, release-pending and complete, with the next action and responsible party. |
| OFR12 | An export must include agreed invoice representations, identifiers, events, acknowledgements, public-copy/reporting evidence and a manifest of omissions/limitations; access must be scoped and receipt auditable. |
| OFR13 | Before closing, the case must record the approved retention/legal-hold/deletion decision for each data class and schedule later actions that cannot yet occur. |
| OFR14 | A cancelled or reversed exit must preserve the actual external state and invoice attribution; it must initiate an evidenced restoration transition rather than silently resetting the case. |
| OFR15 | A provider outage must create an owned operations case with affected invoices, deadlines, fallback route, unsafe actions, customer communication and recovery evidence. |

## Product, integration and operational contract

The customer or ERP/API consumer needs to request a scoped exit, inspect prerequisites and blockers, review the intended cutover, authorise it, follow observed progress, retrieve an export and see historical-access terms. Exact endpoints, events and UI design remain architecture/product decisions. The external provider capability record must state whether it supports independent inbound/outbound deactivation, lookup/publication change, deregistration, historical status access, export, idempotent mutation, state query, and acknowledgement. An unsupported action becomes a named manual gate; it is never silently treated as success.

Operations needs one case timeline showing intended versus observed state, source/time, invoice and obligation counts, deadline exposure, operation safety class, partner owner, customer notice, export receipt and disposition schedule. The runbook must prohibit blind replay after a timeout, and must define who can override a release gate and what evidence/approval that exception requires. Support must be able to explain what the customer can still do after subscription termination.

## Quality, security and data requirements

| ID | Requirement |
|---|---|
| ONFR1 | Every mutation and override must be attributable to an actor, legal entity, scope, request ID, timestamp, external reference, observed result and approval evidence. |
| ONFR2 | Credentials and delegated mandates must be least-privilege, purpose-bound and revoked after their confirmed dependencies end; no secret material may appear in case exports or logs. |
| ONFR3 | Exit records and exports must remain isolated by tenant, entity, environment and authorised delegate; support access must be audited. |
| ONFR4 | The design must support reconciliation after internal persistence failure following external success, without duplicate registration or invoice mutation. |
| ONFR5 | Pilot measurements must include blocked/unknown cases, stale entry points, unowned obligations, export failures and residual access; Product and Operations set targets from observed baselines before production approval. |

## Failure and recovery matrix

| Failure | Required behaviour | Exit state |
|---|---|---|
| Destination cannot be proved reachable | Preserve old route, correct and retest | Blocked at G3 |
| External publication times out | Query/observe before retry | Outcome unknown |
| Old provider accepts withdrawal but Sage persistence fails | Reconstruct from external evidence and case correlation | Manual recovery or reconciled |
| Old entry point still advertised after cutover | Keep monitored receipt/forwarding where approved; notify owner and correct publication | Release pending |
| Invoice arrives on old route after cutover | Preserve, attribute and process under approved transition rule; alert operations | Historical continuity |
| Article 10 or 12 actor is unconfirmed | Retain needed access; escalate before due date | Blocked at G5 |
| Export omits evidence | Produce manifest, repair or disclose the gap; do not claim complete export | Release/disposition pending |
| Credential revoked too early | Contain, recover through approved provider process and assess missed obligations | Incident/manual recovery |
| Two overlapping exit requests | Serialise or conflict; never create two effective cutovers | Requested/blocked |

## Acceptance criteria

- **OAC1 (OFR1–4):** Given a customer moving inbound receipt, when the destination has not been externally observed as reachable, the old inbound route remains active and the case cannot pass G3.
- **OAC2 (OFR5–6):** Given an invoice submitted before cutover whose outcome is unknown, when the destination activates, Sage does not resend that invoice via the new provider and exposes its reconciliation owner.
- **OAC3 (OFR7–8):** Given a pre-cutover invoice with a pending status or payment obligation, when subscription cancellation is requested, the case retains an approved execution path and blocks dependent credential removal until the obligation is resolved or an approved alternative is evidenced.
- **OAC4 (OFR8–9):** Given a provider deregistration request times out, the case shows `outcome_unknown` and does not issue another mutation or show completion until provider state is reconciled.
- **OAC5 (OFR10):** Given two exit requests overlap on one legal entity and direction, only one can establish the effective cutover; the other receives a conflict or queued outcome.
- **OAC6 (OFR11–13):** Given a completed customer exit, an authorised customer and support agent can retrieve the cutover evidence, export manifest, historical-access terms and data-disposition schedule without access to another entity's records.
- **OAC7 (OFR14–15):** Given a failure after cutover, recovery preserves the actual route used by each affected invoice and records customer communication, unsafe actions and approval for any restoration.

## Measures and release gates

Track completed exits by destination/scope, cutover success, stale-entry-point incidents, invoices received on an old route after cutover, unresolved historical obligations, outcome-unknown age, export completeness, time to revoke unnecessary access, and customer-reported reachability failures. Product and Operations must establish baselines and agree targets; none are invented in this draft.

| Gate | Required evidence | Owner |
|---|---|---|
| Discovery | France incident/lessons review; Spain rule and implementing-order check; provider exit capability matrix; contract and archive terms | Spain PM/PMM, Compliance/Legal/Tax, provider owner |
| Design | Confirmed route granularity, authoritative entry-point/publicity sequence, Article 10/12 post-switch actor, data classes and retention policy | Spain Compliance/Legal/Tax, local technical lead, Privacy/Security, Domain Service Product Owner |
| Pilot | Public/private and private/private switch-out drills; inbound/outbound separation; in-flight, late status/payment, timeout, rollback, export and emergency-exit tests | Engineering, provider SMEs, Operations |
| Production | Signed runbook, support and partner RACI, customer wording, measurable monitoring, contractual portability/exit rights and passed pilot evidence | Product, Operations, Legal/Security |

## Open decisions

| ID | Decision required | Why it blocks | Accountable reviewers |
|---|---|---|---|
| OD1 | Which actor/channel may deliver a later Article 10 status for an invoice exchanged through the previous provider? | Historical access and credential release | Spain Compliance/Legal, technical lead, providers |
| OD2 | Which actor/channel may send an Article 12 full-rejection or payment report after switch, and how are duplicates prevented? | Public-reporting continuity | Spain Compliance/Tax, AEAT/public-platform SME, providers |
| OD3 | What is the authoritative inbound entry-point update, observation, rollback and old-provider withdrawal sequence, including mixed routes? | Reachability and cutover promise | Local technical/regulatory team, operator SMEs |
| OD4 | Which provider actions are automated, manual or unsupported, and what contractual notice/assistance/export rights apply? | Feasible runbook and customer terms | Provider contract owner, Operations, Product |
| OD5 | What are approved retention, archive, deletion, legal-hold and credential-access periods by data/obligation class? | G5–G7 completion | Legal/Tax, Privacy, Security, Operations |
| OD6 | Can a new provider perform follow-up work on an old invoice, and which route carries a later rectifying invoice? | Historical and correction design | Spain Compliance/Tax, local technical lead, providers |
| OD7 | What specifically failed in France, and which controls or contract terms would have prevented it? | Validates the risk model and pilot tests | France service owner, Spain PM, Operations |
| OD8 | Which implementing-order and provider specifications are effective for the planned pilot date? | Regulatory and interface readiness | Spain Compliance/Tax, local technical lead |

Each decision needs a named owner, date, source and `confirmed`, `amended` or `rejected` outcome. Until then, the proposed case model must not be presented as approved policy. OD1–OD5 and OD8 block production exit automation; OD3, OD1 and OD2 block any pilot that would make those actions necessary.

## Change log

| Date | Change | Basis |
|---|---|---|
| 2026-10-05 | Added Confluence-safe HTML exit and handover visual beside the proposed case gates | User request; existing G1–G7 and failure/recovery rules |
| 2026-10-05 | Initial dedicated Spain customer offboarding and provider-exit draft | User request; PRD-SEI-222/224/225/226; RD 238/2026 |
