---
id: SPEC-SEI-007
title: Invoice sending solution
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-13
reviewers: []
related:
  - RES-SEI-002
  - GLO-SEI-001
  - PRD-SEI-104
  - PRD-SEI-212
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-231
  - PRD-SEI-236
  - PRD-SEI-241
  - PRD-SEI-244
  - PRD-SEI-246
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-005
  - SPEC-SEI-009
  - SPEC-SEI-014
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610656"
  page_id: "923861395"
  layout: two_left_sidebar
  toc: true
---

# Invoice sending solution

Terminology follows the [shared e-invoicing glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). Local terms explain this feature; exact technical IDs, fields and source codes keep their stated meanings.

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices still need review; **open** decisions still need an owner’s recorded answer. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### 1 Purpose, source authority and scope

This **proposed logical design** explains the Spain outbound invoice journey. The ERP submits a draft for checks and reviews the result. Sage qualifies the exact final candidate, recipient route, required files and action plan before the dependent issuance. The ERP owns issuance. Where Article 4 applies, the proposed handoff coordinates required public-copy submission with issuance. Recipient delivery follows the qualified plan. Recipient delivery and any required public copy have separate results. The primary business-flow source is the review draft [PRD-SEI-246](../../prds/PRD-SEI-246-spain-invoice-preparation-and-outbound-flow.md) and its [combined Draw.io diagram](../../assets/diagrams/spain-invoice-preparation-and-outbound-flow.drawio). [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md) owns shared route, transformation, trust and action principles; [PRD-SEI-212](../../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md) owns the public submission boundary. [SPEC-SEI-005](../SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) owns the UBL result and correction contract; [SPEC-SEI-001](../SPEC-SEI-001-certificate-management-solution-specification.md) owns protected trust-material use.

This spec orchestrates those contracts for one issued outbound invoice.

The diagram and PRD-SEI-246 are draft proposals. They do not approve external APIs, fields, format or profile versions, route update rules, who may sign, public-copy timing or legal correction procedures. The official public UBL version and legal copy timing are now known. Physical contracts, profile activation, route evidence and legal correction implementation remain open.

The ERP owns invoice issuance. The Domain Service may prepare and check a draft, but it cannot issue the invoice or silently change the final business data. A successful draft check cannot authorise sending changed final data.

### Public source baseline

Final Articles 3–5 now govern the public action plan: a qualifying private issuance requires a simultaneous faithful copy, while public issuance/interconnection requires no extra copy. Duplicate, copy-to-original and rejected-copy cases have distinct legal branches. The supplied SendInvoice contract confirms the operation shape; limits and profiles still require qualification.

See [REF Source references](#ref-source-references) for the original files, exact locations and source limits. The [technical evidence guide](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md) tracks shared source conflicts. The constraints below align this feature with the supplied public evidence; Sage implementation and activation remain gated.

### Shared connection and route handoff

The [shared connectivity and routing spec](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) supplies the qualified customer connection, route version, contract profile and permitted executor (SPC-03/05/06). Recipient destination evidence still comes from SPEC-SEI-012 and is a separate selection. This outbound spec owns the immutable exchange plan, representations and independent delivery/public-copy actions. Use the same foundation for external-provider integration and the proposed Sage operator role; adding that role cannot rewrite a frozen invoice plan or introduce a second executor for an uncertain action. Public protocol execution remains with SPEC-SEI-011.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Invoice revisions, plans and independent results | Keep ERP issuance separate from preparation; save final-file evidence and recover each external action independently. | Reusable unchanged | Reuse versioned intent, audit and independent-action safety patterns. ERP, exchange and lifecycle owners. |
| Actor, approval and portfolio controls | Apply the same invoice flow to a direct business, an accountant for one client and each permitted portfolio item. | Reusable design pattern with country binding; implementation unknown | Reuse the request/evidence and client-item patterns in SPEC-SEI-002 ONB-12/13. Bind invoice revisions, staff permissions and Spain authority separately. Product, Identity and Architecture must qualify the actual implementation, gaps and owners. |
| Applicability, routing, transformation and trust | Prepare the final candidate or qualified issued invoice using the selected Spain route, approved format and signer/seal policy. | Reusable with country binding | Bind local applicability, directory evidence, profiles, mapping, trust and provider contracts. Assess DTS for transformation rather than assume native ERP support. Country, exchange and DTS owners. |
| Spain recipient route and public copy | Use the Spain private/public route decision and any separate faithful public-copy obligation described in this draft. | Country-specific | Proven absence, copy duty/timing and correction rules still need the named Spain evidence gates. Do not make this route/copy topology a default elsewhere. Spain Compliance and technical owner. |
| Existing end-to-end outbound implementation | Assess ERP-native functions, shared Sage services and provider-owned operations for the selected journey. | Unknown | This flow does not prove deployed end-to-end coverage. Record the actual execution owner, build, adapter and gaps for each step. Product, Architecture and service/provider owners. |

The existing DTS reuse direction comes from [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md). It identifies a preferred candidate; it does not certify a deployed build or Spain acceptance.

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
| Internal invoice approval | A business decision that permits the specified next step for an exact invoice revision. An eligible customer or delegate may approve. Product policy decides whether manual approval or an authorised automatic rule is permitted. |
| Portfolio | An accountant's set of independently scoped client businesses. Membership does not grant sending or signing authority. |
| Accounting handoff | A separate authorised transfer of invoice information to the accountant or accounting software, with its own result. |
| Capability | A supported function, such as receiving invoices or signing them. |
| Route | The time-bound selection of platform and connection for a defined invoice scope and direction. A ready connection does not activate a route or rewrite earlier invoice plans. |
| Idempotency | Repeating the same logical request adds no effect within the contract’s defined scope and retention window. The contract binds request identity and input and defines conflict handling. |
| Reconciliation | Check the original operation against a reliable source to establish what actually happened before deciding the next action. |
| Gate | A condition, decision or evidence check that must pass before the next step can proceed. |
| Tenant | The customer account boundary used to keep one customer’s data and access separate from another’s. |
| Immutable / append-only | Immutable means a saved record cannot be changed. Append-only means later information is added as another record. Neither means indefinite retention. |
| Provenance | The record of where data came from and which versions, checks and changes produced the result. |
| Contract | The agreed inputs, outputs, behaviour and responsibilities between services or parties. |
| Durable | Saved through the agreed recovery boundary so the record survives a process restart or worker failure. Long-term retention is a separate policy. |
| ERP / Domain Service | The business software that issues the invoice; and the Sage service that prepares, validates and coordinates its exchange. |
| Preflight | A draft check. It cannot replace checking the exact final candidate or eligible issued invoice before sending. |
| Exchange action | One separately tracked action to deliver an invoice, submit a public copy, or report an invoice event. Each action has its own result. For example, invoice delivery can succeed while public-copy submission still needs attention. |
| Faithful public copy | A separate copy submitted to the public platform when the applicable Spain policy requires it. |
| Representation / hash | A specific file or form of invoice data; its calculated content fingerprint. |
| Entry point / evidence level | The published receiving destination, which need not be a raw URL; and what a result actually proves, such as platform receipt rather than buyer acceptance. |

### 2 Outcomes and handoffs

| Outcome | Observable result | Must remain distinct from |
|---|---|---|
| Draft ready for ERP review | Scoped preparation result, issues, route indication and possible generated draft representation | Issued invoice |
| Approval action required | A named business decision or authority check is missing, with the eligible approver and affected invoice/action identified | Permission to issue, sign or dispatch |
| Issued, dispatch blocked | ERP-issued identity/revision retained with an actionable validation, route, trust or policy hold | Automatic return to draft |
| Planned for dispatch | An immutable plan records the route, files, trust requirements and exchange actions; the send request is saved for recovery | External transmission success |
| Recipient delivery result known | Accepted, rejected or completed outcome for each action with evidence level | Buyer acceptance or separate public-copy completion |
| Public-copy result known | Separate faithful-copy result when required | Recipient delivery |
| Outcome unknown | One original external action is reconciled under its original route/correlation | Permission to repeat all actions |
| Customer view | Separate preparation, issuance, submission, delivery, copy/reporting and later buyer states | One global “sent” flag |

Actors are issuer/ERP; Domain Service preparation and exchange orchestration; legal-subject/authority and country policy; route/entry-point evidence owner; format/transformation, validation and trust services; private platform or public platform; operations; and product/lifecycle consumers. One legal entity, invoice and final revision are in scope per logical exchange. A portfolio coordinator invokes this flow separately for each permitted client/invoice item. This spec defines item controls and results; a new batch execution API and its physical owner remain open under OUT-Q02.

**Three operating journeys — proposed:** the client business remains the represented party. The invoice's seller, buyer and any material issuer retain their defined roles. The authenticated caller, invoice preparer, approver and signer are separately identified. An accountant can work for one client without a portfolio batch.

| Journey | Access and authority | Approval and processing | Result |
|---|---|---|---|
| Direct business customer | Bind the business user or service to the business and permitted action. | Check current authority at OUT-03/08/12. An eligible actor or authorised rule supplies any internal invoice approval at OUT-05 and the dispatch gate. | One invoice result with a named approval or correction owner. |
| Accountant for one client | Bind the firm, authenticated staff member or service, current client relationship and exact grant. | The accountant may prepare, approve, send or sign only for separately permitted actions. Missing approval returns a client action; qualified existing authority does not require a new invitation for every invoice. | The same invoice result, with client, delegate and approver separately recorded. |
| Accountant portfolio | Check the same access, authority and approval evidence for every client/invoice item. | Run independent safe items. Hold only affected items for approval, correction or reconciliation. One client's grant or decision cannot cover another client by default. | Permitted item results and aggregate progress; no portfolio-wide “sent” or “approved” result. |

**Approval boundary:** all three journeys evaluate the required approval purposes. Permission to work for a business is separate from approval of invoice content, issuance, dispatch and signing. An eligible accountant may make an internal invoice decision for the client. Permission to view or prepare invoices does not establish that eligibility. Product and Compliance must decide whether every invoice needs a manual approval, whether a qualified rule can approve automatically, and which actions the decision covers; OUT-Q01 keeps this open.

The ERP owns the invoice decision and issuance at OUT-05/06. The exchange gate at OUT-08 checks that any required dispatch approval still covers the exact final revision. OUT-12 checks current authority before each new external action. Missing evidence blocks that action and identifies the eligible customer or delegate. It does not turn an issued invoice back into a draft.

**Evidence and reuse limit:** [B2Brouter's eAccounting guide](https://docs.b2brouter.net/es/user-guide/account-settings/setting-up-your-company/) describes an accepted client connection and separate account roles. [Banqup's role guide](https://help.banqup.com/es/articles/406417-permisos-de-los-usuarios-que-hace-cada-rol) distinguishes viewing, creating and sending. These are operating-pattern references, not proof of Sage implementation or Spain legal authority. [RD 238/2026, Article 7.3](https://www.boe.es/eli/es/rd/2026/03/25/238/con) separately requires the issuer or an authorised delegate to sign invoices issued through private platforms. Qualify the actual signer, executor and representation evidence for each selected interface.

### 3 Process diagrams and text equivalent

Diagram step names use plain-language actions. The smaller activity references link to the detailed behaviour and checks below.

**Primary Spain flow:** ![Spain invoice preparation, issuance and sending](../../assets/diagrams/spain-invoice-preparation-and-outbound-flow.svg)

[Editable Draw.io](../../assets/diagrams/spain-invoice-preparation-and-outbound-flow.drawio) · [PNG preview](../../assets/diagrams/spain-invoice-preparation-and-outbound-flow.png). The diagram's numbered nodes 01–15 correspond to OUT-01–OUT-15 below. Its public recipient route and resolved private route are alternatives; the faithful public copy is a separate conditional obligation. Observation arrows into the outcome ledger do not require a synchronous join.

Text equivalent: OUT-01/02 submit draft data → OUT-03/04 return checked draft evidence → OUT-05 ERP review → OUT-07 supplies the exact final candidate → OUT-08 rechecks facts and authority → OUT-09 confirms recipient evidence → OUT-10 freezes the plan → OUT-11 prepares and validates required files and saves intent. Only then does OUT-06 ERP issuance proceed through the qualified OUT-12 boundary. Where Article 4 applies, that boundary submits the faithful public copy simultaneously with issuance. Public issuance/interconnection has no extra copy. OUT-13 records each action's raw result and reconciles unknown effects; OUT-14/15 show separate issuance, delivery and copy outcomes. Failed preparation holds the candidate before issuance. Already-issued public-original intake and late-copy recovery retain their distinct source context; they do not justify delayed copies in the normal Article 4 journey.

The diagrams show the common single-invoice process used by all three journeys. OUT-03/08 cover authority and missing approval evidence; OUT-05 covers the ERP's internal invoice decision. Portfolio coordination surrounds these steps without changing their meaning. Pending approval holds only its dependent step. Refusal is a business outcome; an uncertain submitted action follows OUT-13.

**Sending and recovery detail:** ![Prepare and send invoices; track each action](../../assets/diagrams/e-invoicing-outbound-exchange-pilot.svg)

[Editable Draw.io](../../assets/diagrams/e-invoicing-outbound-exchange-pilot.drawio) · [PNG preview](../../assets/diagrams/e-invoicing-outbound-exchange-pilot.png). This existing process makes validation correction, no-proven-route hold and outcome-unknown reconciliation explicit. It is a companion to the primary flow, not a second route policy.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Owner |
|---|---|---|
| OUT-01 Create draft | ERP holds complete business invoice data and source revision | ERP |
| OUT-02 Submit draft | Authorised preparation request and input digest accepted idempotently | ERP → Domain Service |
| OUT-03 Prepare | Entity, actor, policy, data, profile and early route indication evaluated | Domain Service + policy |
| OUT-04 Decide draft | PASS/limitations/issues with correction owner returned; no issuance/send | Validation → ERP |
| OUT-05 Review | Eligible customer/delegate reviews preparation and business content; records the required invoice decision and policy | ERP/customer or authorised accountant |
| OUT-07 Submit final candidate | Stable planned identity and exact revision bound before dependent issuance; qualified already-issued paths retain actual evidence | ERP → Domain Service |
| OUT-08 Final checks | Current authority, required approval for the exact final revision, data/representation, policy and trust checked | Exchange + Identity/validation/trust |
| OUT-09 Lookup | Current authoritative recipient evidence classifies private, proven-none/public or unresolved | Route service |
| OUT-10 Plan | Immutable route, representation, trust mode and independent actions recorded | Exchange |
| OUT-11 Prepare/send intent | Final bytes validated, trust applied if required, durable operation created | Exchange/transform/trust |
| OUT-06 ERP issuance | ERP issues only through the qualified boundary after final preparation; Article 4 copy is coordinated with issuance | ERP / exchange |
| OUT-12 Execute actions | Recipient delivery and conditional copy have separate identities for operations that change external state | Adapter/operator |
| OUT-13 Record outcomes | Each action's raw/normalised result, unknown state and reconciliation evidence retained | Exchange/operations |
| OUT-14 Derive views | Evidence-qualified technical, delivery, copy and later lifecycle statuses calculated | Lifecycle service |
| OUT-15 Show result | ERP sees known/unknown outcomes, freshness, next action and ownership | Product |

### 5 Material open decisions

| Decision / design impact | Owner and gate |
|---|---|
| Complete draft and final-data contract, issued identity, revision binding and invalidation of preflight | ERP Product + Domain Service; design/pilot |
| Draft artefact and human-readable rendering ownership | ERP Product + Architecture; design |
| Whether early lookup failure blocks ERP issuance; final route must always block dispatch when unresolved | Product/Compliance; design |
| Legal/ERP process for correcting an already issued invoice | Spain Legal/Tax + ERP Product; pilot |
| Authoritative recipient entry-point source, freshness, eligibility, bridging and observed “none” semantics | Local technical/regulatory owner + provider; route pilot |
| Public-copy representation, proof of simultaneous submission and outcome vocabulary | Spain Compliance/technical owner; external conformance |
| Signature/seal actor, trust profile and provider handoff | Legal/Security/Business Identity; trust gate |
| External idempotency, query and acknowledgement semantics per action | Provider/public owner + Operations; integration |
| OUT-Q01 Invoice approval policy: eligible customer/accountant roles, manual or automatic approval, purpose, revision binding and withdrawal rules | ERP Product + Identity + Spain Compliance; design and delegated pilot. Do not infer universal manual approval or accountant eligibility from a product login. |
| OUT-Q03 ERP issuance/public-copy coordination: final identity stability, approval, authority, trust completion, actual simultaneous submission and race/partial-failure recovery | ERP + E-Invoice + Spain Compliance; design and end-to-end release gate. Article 4 timing is fixed; no invented tolerance, reservation API or atomic distributed transaction is approved. |
| OUT-Q02 Portfolio coordinator and accounting handoff: supported client/invoice scope, limits, permission-safe progress, receipt/replay contract and implementation ownership | Product/Global API + Architecture + Operations; portfolio pilot. Qualify source design or build, Spain changes, gaps and owners before enabling bulk execution or accountant distribution. |

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Aggregate model and invariants

The proposed aggregate key is (tenant, legalSubject, environment, businessInvoiceId, issuedRevision). Preparation work is keyed separately by draftRevision. A final submission includes a stable idempotency key and fingerprint of the input in its agreed standard form; the same key/digest returns the existing exchange, while the same key with changed data conflicts. Every external action has its own operation ID, idempotency scope and result. The supplied SendInvoice and CancelInvoice WSDLs establish public PRE transport contracts. Sage-facing endpoints and records remain proposed; full public business schemas, replay safety and live activation remain gated.

| ID | Rule that must always hold |
|---|---|
| OUT-I01 | Draft preparation, ERP issuance, final validation, external admission, recipient delivery, public-copy completion and buyer acceptance are independent facts. |
| OUT-I02 | The ERP is the system of record for the issued business invoice. The service cannot change issued content or identity without a new authorised ERP revision/correction process. |
| OUT-I03 | Early lookup is guidance; final dispatch uses fresh authoritative route evidence. A failed or stale lookup is not proof of no private entry point. |
| OUT-I04 | A proven absence of a private entry point selects the Spain public recipient route under the effective policy; an observed private point still requires operational eligibility. |
| OUT-I05 | Exchange plan freezes route, profile, representation, trust actor/policy and required actions before the first external invoice mutation. |
| OUT-I06 | Transform and validate final target bytes before applicable signature/seal; no workload/transport certificate can substitute for invoice-signing authority. |
| OUT-I07 | Recipient delivery and faithful public copy have independent attempts and outcomes. One action's failure cannot repeat or erase another completed action. |
| OUT-I08 | Unknown mutation remains action-specific and reconciles against original route, payload hash and operation identity before retry. |
| OUT-I09 | Every representation and result retains source, hash, profile, mapping/trust version and external evidence; later route changes cannot rewrite original context. |
| OUT-I10 | Represented business, authenticated caller, firm/client relationship, approver and signer remain distinct. Authority is checked for each protected action. |
| OUT-I11 | Required internal invoice approval binds its purpose, business, invoice revision/hash, approver and policy. A stale or out-of-scope decision cannot authorise issuance or dispatch. |
| OUT-I12 | Portfolio items retain client-scoped authority, idempotency, approval and outcomes. Current access checks also protect item detail and aggregate counts. |
| OUT-I13 | Withdrawal or relationship loss stops affected new protected work. It preserves issued invoices, completed actions and the original evidence needed for authorised reconciliation. |

### 2 Detailed behaviour

**OUT-01/02 Draft intake.** The ERP submits complete invoice facts: issuer and recipient, type, dates, lines, quantities/prices, tax, totals, payment and applicable references/attachments, plus tenant/entity, actor, environment, source invoice/draft revision and request identity. The exact field contract is an open design item. A durable request record stores input reference/hash and authority context. The service rejects cross-tenant or unsupported cohort/capability before preparation. Duplicate request identity with same digest returns its existing result; changed digest conflicts. Intake is neither invoice issuance nor external transmission.

Resolve the direct business actor or accountant's firm, authenticated actor and current client relationship from trusted context. Check preparation permission separately from issuance, approval, submission, public-copy execution and signing. A supplied client ID or portfolio reference is not authority. Unknown and unlinked client references return a safe denial without revealing client existence.

**OUT-03/04 Prepare and decide draft.** Resolve legal subject and action-specific authority independently of login or certificate possession. Country policy evaluates applicability, selected document type, required delivery/copy duties, activated profile and supported representation path. Apply [UBL validation/correction](../SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) when UBL is selected; other syntax profiles require their own activated packs. An early recipient lookup may report private, proven no-private/public, or unknown; its source/time and limitations are displayed.

It is not frozen as the final route. Return precise blocking issues, owner and next action. A corrected draft creates a new revision; the prior result remains. Any generated electronic file is a distinct derived artefact, not a silently edited ERP source. No external invoice mutation occurs.

**OUT-05 ERP review; OUT-06 coordinated issuance.** The ERP decides whether and when to issue and records the final business invoice identity, issue time and revision under its own legal/product controls. A preparation PASS cannot issue on behalf of the ERP. The Domain Service does not infer that a changed draft or final invoice is still valid. Issued content is frozen for exchange; later content correction follows the approved legal/ERP process, potentially a new invoice or credit note, not automatic reversion to draft.

For the public profile, the supplied formats select `Invoice`, including a rectifying invoice. Where Article 4 requires a faithful copy, the ERP issuance boundary must coordinate that copy with issuance, using qualified final identity, representation, authority and readiness. Do not treat the later private-delivery result as its trigger. Prepare the required copy prerequisites before the dependent issuance handoff; bind the final issued facts and independent public operation at that handoff. The exact ERP/service coordination and proof of simultaneous submission need the copy/issuance gate in OUT-SPFE-R01. The lifecycle overview shows responsibilities; it does not approve a delayed copy after issuance or claim that the current ERP handoff already satisfies the rule.

Cancellation before issuance closes safe preparation work; cancellation after issuance cannot erase the issued record.

The ERP applies the policy selected under OUT-Q01. Where internal invoice approval is required, save its business, invoice revision/hash, purpose, eligible approver, decision, policy version and evidence reference before the dependent step. The same actor may prepare and approve only where the qualified role permits both. An accountant without approval authority requests the eligible client's decision; the Domain Service cannot approve on the client's behalf.

Reuse the request/evidence pattern in SPEC-SEI-002 ONB-12 where a decision is missing. Runtime invoice work remains owned here and by the ERP; it does not repeat onboarding automatically. Save the request before notification. Verify response eligibility, purpose, expected version and current authority before resuming the same invoice. A duplicate response returns its recorded result; refusal, expiry or a stale/conflicting response cannot release the hold. A material invoice change requires fresh evaluation of whether the decision still covers it. An authorised automatic rule records the eligible business actor who authorised it, executing service, rule/policy version and decision evidence; it cannot bypass authority, validation or trust.

**OUT-07 Final candidate or issued-data intake.** For the coordinated Article 4 journey, the ERP supplies exact final candidate facts, planned final identity/date, revision, issuer authority, route intent and request identity before issuance. The ERP and service must prove that these are the facts that will be issued. Any change invalidates the plan and affected validation/trust evidence before issuance. If the ERP allocates or changes material facts only at issuance, the journey stays gated under OUT-Q03 until its actual contract supports compliant coordination. For an already-issued public original, retain actual issuance evidence and apply its distinct interconnection rules. A late Article 4 copy is an owned nonconformance/recovery case, not the normal compliant journey. The service verifies that source revision, issued identity and hash are internally consistent and that no conflicting final submission already owns this invoice/revision. Persist final intent and operation identity before possible external mutation. Same final identity/hash resumes the existing exchange; changed bytes or issuer identity under the same key conflict and require an authorised correction/revision decision.

**OUT-08 Final checks.** Re-evaluate effective applicability, legal subject, actor/delegate authority, product entitlement, invoice identity and current profile. The exact final representation is generated or accepted, then validated under versioned syntax, semantic, country/route and attachment rules. A draft result cannot substitute for this gate. The selected signer/seal creator and represented party, protected material, purpose and policy are resolved through [certificate management](../SPEC-SEI-001-certificate-management-solution-specification.md).

Invalid or unknown policy/trust blocks the affected operation. Issues in issued content return an issued-invoice resolution state with owner; the service must not amend the invoice.

**OUT-09 Recipient lookup.** Use the reliable entry-point source for the exact recipient, environment, document and process capability, direction and effective time. Save the source, observed value, observation time, freshness and rule version.

PRIVATE_READY means a private destination is published and its route is eligible under the confirmed interconnection or bridge rule. PROVEN_NONE means the lookup succeeded and confirmed that no private receiving entry point exists. Spain policy then selects the public recipient route.

FAILED, STALE, AMBIGUOUS and UNSUPPORTED leave the route unresolved and block dispatch. Check again or obtain approved manual evidence. A timeout cannot select the public route by default. If the route changes after planning but before an external change, report a version conflict and create a new plan. Actions already sent keep their original route.

**OUT-10 Freeze exchange plan.** Record business invoice/revision/hash, issuer/recipient, selected delivery route and authoritative evidence, exact delivery and public-copy representations/profiles, required action set, trust mode/actor/policy/material references, mapping versions, source policy and effective time. Each action specifies destination, purpose, operation/idempotency ID and dependency. The public recipient route and private recipient route are alternatives; a separate faithful public copy exists only when policy requires it.

An unproven eligibility or format/signature combination cannot produce READY_TO_SEND. The plan is immutable; correction or material route/profile change creates a new plan version before mutation, with prior versions retained.

**OUT-11 Final representation and send intent.** Use an approved mapping only when evidence shows that it preserves the required business meaning. Validate each final target representation after transformation. Obtain protected signature/seal on the exact required bytes under the frozen trust plan; a signing timeout reconciles the original protected operation before a new attempt. Store signed/final bytes/hash, validation/trust evidence, external payload reference and durable send intent.

The provider adapter receives only references and authorised protocol inputs; private keys do not enter invoice events or logs. A preparation or trust failure leaves all external actions unsubmitted.

**OUT-06/12 Issue and execute independent obligations.** ERP issuance and required Article 4 copy submission share the qualified logical boundary. A saved queue intent alone does not prove that the copy duty was met. AEAT admission is a later independent fact; this design does not require admission before ERP issuance. Record actual issuance evidence against the same final identity/revision/hash and public operation. Check authority and readiness before releasing the boundary. A race, lost response or partial failure retains the issued record and reconciles the affected original action; it cannot automatically withdraw, reissue or repeat successful delivery. OUT-Q03 must qualify the physical coordination and failure handling.

For each ready exchange action, the adapter performs only the action named in the plan: deliver the invoice to the recipient (private/direct or public), or submit a required faithful public copy. Use that action's stable operation ID. Persist an attempt with payload hash, target, adapter/contract version and correlation before transmission, or use an approved recoverable external-first design. A public bridge or copy cannot be inferred simply from a private delivery result.

Before each new protected execution, recheck the effective actor/client relationship, action authority and required approval against the saved plan and final revision. Record the decision snapshot. If authority was withdrawn after planning, hold the affected unsent action and return its eligible owner. A completed action is retained. An uncertain action uses OUT-13 through an authorised client or operational path; a new actor cannot inherit the former accountant's grant.

One action may finish while another remains pending, rejected or unknown. Provider acknowledgement is recorded at its actual evidence level; no customer claim of recipient retrieval, buyer acceptance or public-copy completion is derived solely from transport success.

**OUT-13 Reconcile and retain outcomes.** For each action, add the raw provider or public-platform response, external references and normalised technical state to the record. A definite validation rejection returns a safe issue; correction follows the rules for an issued invoice. Temporary failures before any external change can retry under the versioned policy.

A timeout after a possible external change produces OUTCOME_UNKNOWN for that action only. Check the original external state using the same route and correlation before repeating it. Record proven success once. Retry after proven absence only if the contract permits it. An unresolved result opens an operations case.

Do not repeat successful recipient delivery because the public-copy result is uncertain. If external success occurs but local saving fails, rebuild the ledger from the saved intent and reliable external observation.

**OUT-14/15 Derive and present status.** [SPEC-SEI-009](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) owns the source-preserving lifecycle event and derived-view contract after exchange handoff. Show separate states for draft preparation, issuance, planning, each action’s submission or acknowledgement, delivery, public copy or reporting, and later buyer actions. Each action can be submitted, acknowledged, rejected or unknown.

Include the evidence source, time and freshness, affected action, safe next action and owner. Status information can arrive later or out of order from the public/private platform through a qualified query or supported notification. SPEC-SEI-009 owns this intake and interpretation; it also accepts separate authorised customer/ERP events. Link it to the original invoice and action; do not infer success without evidence. Limit product and support views to the permitted tenant and business, and remove confidential provider content.

Keep the original sent bytes, route, profile and trust versions, and evidence for each action under the approved retention policy.

For a portfolio, recheck current staff/client access before reads, changes and execution. Each item uses its existing invoice, revision, action and idempotency identities. A selected correction or cancellation cannot repeat another completed item. Progress and counts disclose only permitted clients; when the full aggregate would reveal inaccessible work, show a visibility limitation. An accounting handoff is a separate product operation under OUT-Q02. Its failure cannot trigger another recipient delivery, and its receipt cannot establish buyer acceptance or bookkeeping completion.

### 3 Requirements and operational controls

| ID | Requirement / source |
|---|---|
| OUT-R01 | Accept complete draft data and return preparation issues without issuing or sending; PRD-SEI-246. |
| OUT-R02 | Preserve ERP ownership of issuance and bind exact final issued identity/revision; PRD-SEI-246. |
| OUT-R03 | Revalidate final representation and current authority/profile before mutation; PRD-SEI-241/246. |
| OUT-R04 | Resolve route from authoritative fresh evidence; distinguish proven-none/public from failed lookup; PRD-SEI-223/246. |
| OUT-R05 | Freeze immutable route, representation, trust and actions in an exchange plan; PRD-SEI-223 FR1–3. |
| OUT-R06 | Transform without losing material business meaning and validate before approved signature/seal; FR7–9/31–34. |
| OUT-R07 | Execute every action with independent idempotency, correlation and outcome; FR12–16. |
| OUT-R08 | Reconcile uncertain external effects on the original action before retry; FR22–23. |
| OUT-R09 | Preserve original/derived/sent representations and raw evidence, then derive qualified views; FR25–26/30. |
| OUT-R10 | Keep public recipient delivery, public copy, technical acknowledgement and buyer lifecycle distinct; PRD-SEI-212/223/246. |
| OUT-R11 | Bind direct or delegated actor context and recheck client/action authority before protected reads and new execution; PRD-SEI-104/231 and SPEC-SEI-002. |
| OUT-R12 | Enforce the qualified internal invoice approval policy for exact revisions and purposes; save eligible decisions and safely handle missing, stale, refused or withdrawn evidence; proposed policy under OUT-Q01. |
| OUT-R13 | Isolate portfolio item authority, request identity, outcomes, recovery and permitted progress; do not infer authority or completion from batch receipt; PRD-SEI-104/231. |
| OUT-R14 | Stop affected new work on authority/relationship loss, preserve prior outcomes and separate accountant distribution from recipient delivery; PRD-SEI-231 and proposed handoff under OUT-Q02. |

Authorisation, tenant/legal-entity and TEST/production isolation apply at draft, final, plan and adapter gates. Restrict invoice payloads and authority evidence; no secrets, private keys or full tax identifiers in logs or errors safe to show to the customer. Enforce compare-and-set or equivalent lock on final invoice/revision and each action to prevent concurrent duplicate dispatch. Monitor preparation failures, stale/failing route lookup, final-check mismatches, plan conflicts, backlog and time spent in an unknown state for each action, copy lag, signature failures and evidence gaps.

Quantitative objectives and retention are design gates based on approved volumes, law/contract and pilot baselines.

### SPFE source contract binding

The source facts below govern the public binding. Recovery, storage and qualification actions are proposed Sage controls where stated. Apply them through OUT-05–08, OUT-10–13. Source conflicts stay open under copy/issuance and correction policy; SPFE-Q03/Q07/Q08/Q13/Q15/Q18; they are not resolved by a local default.

| ID | Constraint and required behaviour | Source reference |
|---|---|---|
| OUT-SPFE-R01 Bind a required copy to actual issuance | Before enabling a private-issuance journey, the ERP and E-Invoice owners qualify its copy handoff at the actual issuance boundary. Article 4 requires simultaneous copy submission; waiting for successful private recipient delivery is not the rule. Record issuer/recipient/third-party material issuance and the responsible copy sender. Public issuance/interconnection produces no redundant copy. Exact operational timing and coordination remain a Compliance/ERP release gate. | SPFE-S02 Articles 3.4 and 4.1–4.3; [REF](#ref-source-references). |
| OUT-SPFE-R02 Keep legal duplicate and withdrawal cases distinct | Preserve original/copy identity and source classification. Apply Article 5.5 rejection cases; a public original following a stored copy needs a separately authorized, traceable copy-withdrawal procedure. CancelInvoice is not used to clear a duplicate or unknown send by default. Retain the previous source, operation and legal-case evidence. | SPFE-S02 Article 5.5; SPFE-S03/SPFE-S10; [REF](#ref-source-references). |
| OUT-SPFE-R03 Correct the right representation | If the copy alone is defective, correct it while preserving correspondence to the issued original; its rejection does not invalidate that original. If the original is defective, route to the applicable governed issuance/rectification branch, including the distinct Article 5.6 cases. Never silently repair issued content or resend successful private delivery merely because public submission failed. | SPFE-S02 Article 5.6; [REF](#ref-source-references). |
| OUT-SPFE-R04 Record batch outcomes and exceptional outage evidence | SendInvoice uses the exact validated Invoice attachments and selected credential port. Enforce the qualified 1–100 batch and per-invoice authority, with the disputed size held for clarification. Save request/item results, locator and receipt evidence separately. Any Article 5.7 extension requires an SPFE-attributable outage over 24 hours and four working days after resolution; ordinary failures do not acquire that extension. | SPFE-S02 Articles 5.4/5.7; SPFE-S03/SPFE-S16; SPFE-Q03/Q15; [REF](#ref-source-references). |

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Keep the issued-invoice, exchange-plan and per-action outcome models shared. Country policy must select delivery and reporting obligations; Spain’s public recipient default and faithful-copy submission must not be hard-coded as universal rules. Record whether each operation is ERP-native, shared-service or provider-owned. DTS is a preferred transformation candidate subject to qualification, while ERP issuance and external dispatch remain separate responsibilities.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Interaction contracts

These are logical operations, not approved endpoints. Commands use requestId, tenant/legalSubject/environment, actor/authority reference, businessInvoiceId, revision, inputDigest, idempotencyKey and expectedVersion where applicable. Every response distinguishes business result, operation safety and evidence level.

| ID | Caller → logical owner | Input / output and failure contract |
|---|---|---|
| OUT-INT-01 | ERP → preparation | Submit/get/cancel draft revision; returns preparation case, stable issues and early route indication; no external invoice mutation. |
| OUT-INT-02 | Preparation → identity/country policy | Resolve legal subject, actor authority, applicability, required delivery/copy duties and activated capability; unknown blocks. |
| OUT-INT-03 | Preparation/exchange → validation/format | Validate source/candidate/final target bytes under exact activated pack; returns layered result and immutable evidence. |
| OUT-INT-04 | ERP → exchange | Submit final candidate before coordinated issuance, or actual issued evidence for a qualified already-issued path. Bind exact identity/revision/hash and later ERP issuance proof. Changed content conflicts; returns exchange reference/state. Physical coordination remains OUT-Q03. |
| OUT-INT-05 | Exchange → recipient discovery | Query authoritative entry point and operational eligibility; returns observed private, proven-none/public or unresolved with source/freshness. |
| OUT-INT-06 | Exchange → route/plan store | Compare-and-set immutable plan/version with route, representations, trust mode and action set; rejects stale route/policy. |
| OUT-INT-07 | Exchange → transform/trust | Produce final representation with comparison of business meaning; validate then sign/seal under protected operation; returns exact bytes/hash/evidence or hold. |
| OUT-INT-08 | Exchange → external adapter | Submit one specified action with stable operation ID/hash/route; returns definitive response or outcome unknown; do not repeat other actions. |
| OUT-INT-09 | Operations/exchange → adapter | Reconcile original action by correlation/external reference; returns observed state/evidence or unresolved. |
| OUT-INT-10 | Exchange → lifecycle/product | Publish committed action/result changes at least once; consumer deduplicates by eventId/version and reads authoritative ledger. |
| OUT-INT-11 | ERP/product ↔ Identity/approval owner → exchange | Resolve current actor/client permissions and required invoice decision by business, purpose, revision/hash, policy and expected version. Return qualified evidence or a scoped pending/denied/conflict result with eligible owner. A notification or recorded approval response alone does not establish effective authority. |

Proposed events are OUTBOUND_PREPARATION_CHANGED, OUTBOUND_PLAN_FROZEN, OUTBOUND_LEG_STATE_CHANGED, OUTBOUND_RECONCILIATION_REQUIRED and OUTBOUND_VIEW_CHANGED. They contain IDs, scope, state, versions and safe evidence references, not invoice XML or secrets. An event cannot prove external completion without the corresponding ledger observation.

### 2 Data inventory

| ID | Record / owner | Essential fields, handling and consumers |
|---|---|---|
| OUT-D01 | Draft preparation / ERP + preparation | Source draft ID/revision, complete-data reference/hash, actor/entity, policy/check results, early route source/time; restricted/versioned; OUT-01–05. |
| OUT-D02 | Final candidate and issued snapshot / ERP | Planned identity/date/revision/hash plus actual issue time and proof when issued. Keep candidate and issued facts distinct; changes invalidate preparation. Preserve immutable issued content and correction lineage; OUT-06–15. |
| OUT-D03 | Validation/profile result / validation | Exact input/target hash, rule/profile versions, issues, status and evidence; append-only; OUT-03/04/08/11. |
| OUT-D04 | Recipient route observation / discovery | Qualified recipient, lookup source/value/time/freshness, private eligibility, proven-none or unresolved reason; versioned; OUT-03/09/10. |
| OUT-D05 | Exchange plan / exchange | Invoice/revision, selected route, representations, mapping/trust policy, action set, authoriser, effective version; immutable; OUT-10–15. |
| OUT-D06 | Representation set / transform/trust | Source, canonical, delivery, public-copy and rendering refs/hashes, profiles, mapper, semantic/trust evidence; sensitive/immutable; OUT-08/11/15. |
| OUT-D07 | Action attempt/ledger / exchange | Action type, destination, payload hash, operation/idempotency ID, adapter/contract version, attempts, raw/normalised result, external ref; append-only; OUT-12–15. |
| OUT-D08 | Reconciliation case / operations | Original action, intended/observed state, last query, owner, unsafe actions, deadline and manual approval; restricted; OUT-13. |
| OUT-D09 | Product/lifecycle projection / lifecycle | Separate derived preparation, issuance, delivery, copy/reporting and buyer dimensions with evidence freshness/next action; rebuildable; OUT-14/15. |
| OUT-D10 | Audit/retention policy reference / records | Actor, action, scope, time, policy version, evidence location and retention/hold class; restricted; all activities. |
| OUT-D11 | Actor and approval context / Identity + ERP decision owner | Represented business, authenticated actor, firm/client relationship and grant refs, action scope, request/version, approver, invoice revision/hash, purpose, policy, decision/effective-time evidence; restricted/versioned; OUT-02/03/05/08/12/15 and INT-11. |
| OUT-D12 | Portfolio item correlation / product coordinator | Parent/submitted item refs, client-scoped invoice/action identities, result versions and visibility policy; references existing exchanges without shared authority or credentials; OUT-02/12–15. Physical coordinator and aggregate contract remain OUT-Q02. |

D02 is ERP-owned; D05/D07 are exchange-owned; D03 and trust evidence are owned by their specialist services. A plan references immutable records rather than copying credentials. Exact retention, archival and data-disposition periods are not asserted here; Legal/Privacy/Records approve them by data class.

### Annex I withdrawal field traceability

The table records all 7 source field/group occurrences for this feature. Each trace ID identifies one row in the [field ledger](../../assets/regulatory/spain/spfe/field-traceability.json). The ledger retains the original Spanish description, conditional rules, semantic type, literal UBL path and exact BOE XML row locator. Repeated source IDs remain separate occurrences. English names aid reading; the Spanish source controls the meaning.

Each listed requirement applies the source meaning, type, presence conditions, cardinality and controlled values through OUT-10–13. Cardinality is evaluated within its selected parent group, not as a universal invoice requirement. Preserve applicable content and reject unsupported mappings. For each row, the positive case uses an approved applicable fixture and tests valid content and permitted absence. The negative case violates an applicable source condition, type, cardinality or controlled value and must fail safely. These are specified acceptance cases, not executed tests. Actual ERP/API bindings, business schemas, executable rules and DTS coverage remain unqualified under SPFE-Q04/Q08/Q14 and the governed withdrawal policy. A recorded source path is not proof of a valid implementation path.

| Trace / source ID | Logical fact or group | Source cardinality | Requirement | Acceptance: positive / negative |
|---|---|---|---|---|
| `AXC-01` / `CANCELINVOICE` | Withdrawal date | `1..1` | `OUT-AXC-R01` | `OUT-AXC-A01P` / `OUT-AXC-A01N` |
| `AXC-02` / `CANCELINVOICE` | Withdrawn invoice group | `1..n` | `OUT-AXC-R02` | `OUT-AXC-A02P` / `OUT-AXC-A02N` |
| `AXC-03` / `CANCELINVOICE` | Invoice series and number | `1..1` | `OUT-AXC-R03` | `OUT-AXC-A03P` / `OUT-AXC-A03N` |
| `AXC-04` / `CANCELINVOICE` | Invoice issue date | `1..1` | `OUT-AXC-R04` | `OUT-AXC-A04P` / `OUT-AXC-A04N` |
| `AXC-05` / `CANCELINVOICE` | Seller group | `1..1` | `OUT-AXC-R05` | `OUT-AXC-A05P` / `OUT-AXC-A05N` |
| `AXC-06` / `CANCELINVOICE` | Seller NIF | `1..1` | `OUT-AXC-R06` | `OUT-AXC-A06P` / `OUT-AXC-A06N` |
| `AXC-07` / `CANCELINVOICE` | Seller name | `1..1` | `OUT-AXC-R07` | `OUT-AXC-A07P` / `OUT-AXC-A07N` |

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

| Scenario | Requirement → activities / interactions / data | Evidence and expected result |
|---|---|---|
| OUT-A01 Invalid draft | R01 → OUT-01–04, INT-01–03, D01/D03 | Customer-correctable issues; no ERP issuance or external invoice transmission by this flow. |
| OUT-A02 Final differs from preview | R02/03 → OUT-07–11/06, INT-04/03, D01–03 | Changed candidate invalidates the plan before issuance. Recheck exact final facts; stale preview cannot authorise the issue/copy boundary. If already issued, use the owned correction path. |
| OUT-A03 Private route eligible | R04–07 → OUT-09–12, INT-05–08, D04–07 | Private delivery selected from observed readiness; copy submission only if required; plan frozen before mutation. |
| OUT-A04 Proven no private entry point | R04/10 → OUT-09/10/12, INT-05/06/08, D04–07 | Successful authoritative absence selects Spain public recipient delivery with source/time. |
| OUT-A05 Lookup timeout or stale result | R04 → OUT-09, INT-05, D04 | Route unresolved and dispatch held; no public fallback by inference. |
| OUT-A06 Mapping or trust failure | R03/06 → OUT-08/11, INT-03/07, D03/D06 | No external action; exact failed representation/policy preserved with owner. |
| OUT-A07 Direct success, copy unknown | R07/08/10 → OUT-12–15, INT-08–10, D07–09 | Delivery success retained; only copy submission reconciles; no repeat delivery. |
| OUT-A08 Lost response after mutation | R08/09 → OUT-12/13, INT-08/09, D07/D08 | Original action queried; no resend or success claim before checking the original outcome. |
| OUT-A09 Issued-content correction | R02/03 → OUT-06–08, INT-04, D02/D03 | Issued original retained; ERP/Legal correction path named, no automatic draft rollback. |
| OUT-A10 Ack versus buyer status | R09/10 → OUT-13–15, INT-10, D07/D09 | Views that state what the evidence proves keep admission, recipient and buyer states separate. |
| OUT-A11 Country-bound routes and exchange actions | R03–07/09/10 → OUT-08–12/14, INT-02/03/05–08/10, D03–07/09 | Spain policy selects the evidenced recipient route and required copy submissions. Another country uses its own approved plan without inheriting Spain public fallback or copy duties. Execution owners and reused transformation evidence are recorded; a country-policy change leaves earlier plans unchanged. |
| OUT-A12 Shared route and executor handoff | R03/07–09; SPEC-SEI-014 SPC-R01/05/06 → SPC-05/06; SPC-A01/07/08 | Both integration roles use the same route/context contract; recipient lookup remains separate; a new operator profile cannot rewrite a saved invoice plan or assign a second executor after possible transmission. |
| OUT-A13 Direct business approval | R11/12 → OUT-03/05–08/12, INT-02/04/11, D02/D11; Q01 | Current business authority and the selected approval policy pass for the exact revision. A changed revision, foreign client decision or ineligible approver cannot release issuance/dispatch. |
| OUT-A14 Accountant for one client | R11/12 → OUT-02/03/05/08/12/15, INT-01/02/11, D01/D11 | A permitted accountant may prepare and, where separately authorised, approve/send for the client. View-only or preparation-only permission cannot approve, sign or send. Missing approval returns an eligible client action; verified existing evidence avoids an unnecessary new request. |
| OUT-A15 Mixed portfolio | R11–14 → OUT-02/08/12–15, INT-04/08/10/11, D07/D11/D12; Q02 | One item succeeds, another waits for approval and an unlinked client is denied. Safe items continue. Duplicate/restarted coordination retains original item/action identities; current detail and counts cannot reveal inaccessible clients. |
| OUT-A16 Withdrawal before or after transmission | R11/12/14 → OUT-08/12/13/15, INT-08/09/11, D07/D08/D11 | Withdrawal before execution blocks new use. After possible transmission, preserve the original action and reconcile through a currently authorised owner. Refusal is not retried as a technical fault; prior success is retained. |
| OUT-A17 Approval and accounting reuse boundary | R12–14 → OUT-05/08/12/15, INT-10/11, D09/D11/D12; Q01/02 | Qualify the actual approval/coordinator/handoff build, contracts, gaps and owners. Missing country approval policy holds dependent work; Spain grants do not authorise another country. Failed accountant transfer cannot resend the buyer invoice or establish buyer acceptance. |

**Actor and approval release evidence:** close OUT-Q01/02 for the selected scope. Exercise all three journeys, staff-role and client-relationship loss, revision changes, conflicting responses, mixed portfolio results and authorised reconciliation. Confirm that each required approval purpose has an eligible actor and evidence. Manual approval of every invoice remains open until Product/Compliance records the policy.

**Review gate:** validate PRD-SEI-246's six open decisions, complete draft/final contracts, route source, representation ownership, trust model and vocabulary for each action’s outcome. **Pilot gate:** test preflight/final mismatch, issued correction, private route, proven-none public default, failed lookup, conditional copy, loss of business meaning, signature failure, duplicate final request, partial action result and unknown mutation against selected providers. **Production gate:** approved Spanish profiles/public interfaces and operator terms, conformance evidence, security/retention review, operations runbooks, measured service objectives and end-to-end pilot results. The existing Draw.io is the process basis; this draft does not convert it into an approved external API design.

### SPFE evidence acceptance

The field and code-table acceptance IDs in Part 3 also form required evidence coverage. Execute them with approved fixtures and pinned rules before activation. The ledger records their current status as not executed; row coverage alone does not close implementation qualification.

These are required evidence scenarios, not executed implementation tests. The source-binding gate is copy/issuance and correction policy; SPFE-Q03/Q07/Q08/Q13/Q15/Q18. A source-backed review does not establish that this feature is ready for production.

| ID | Scenario | Required result | Requirement coverage |
|---|---|---|---|
| OUT-SPFE-A01 | Private issuance, public interconnection and recipient-issued invoice | Prove final preparation before issuance and simultaneous required copy submission at the qualified ERP boundary. Exercise identity changes, authority loss and partial/lost results. Preserve issued evidence without blind replay. No extra copy after public use and no dependence on private delivery success. | OUT-SPFE-R01; OUT-05–08, OUT-10–13; [REF](#ref-source-references). |
| OUT-SPFE-A02 | Existing copy, existing original or uncertain prior send | Classify the legal case and reconcile source evidence; no automatic withdrawal or fresh send as duplicate recovery. | OUT-SPFE-R02; OUT-05–08, OUT-10–13; [REF](#ref-source-references). |
| OUT-SPFE-A03 | Rejected public copy with a valid versus defective private original | Use the correct distinct correction branch, preserving correspondence and all issued/sent evidence. | OUT-SPFE-R03; OUT-05–08, OUT-10–13; [REF](#ref-source-references). |
| OUT-SPFE-A04 | Partial batch admission or ordinary outage versus qualifying SPFE incident | Keep item results independent and missing CSV mapping open. Apply only the qualified exceptional calendar; a failed item cannot repeat admitted items. | OUT-SPFE-R04; OUT-05–08, OUT-10–13; [REF](#ref-source-references). |

## REF Source references

For public-platform legal and external-contract facts, the original official sources below take precedence over earlier assumptions in linked PRDs and internal notes. PRDs retain product scope and are unchanged by this review. A source conflict remains an explicit gate; this spec cannot approve a local substitute.

Use the original files for the claims they establish. Final published regulation governs legal requirements; technical files supply their stated contract facts. Examples are illustrative. Missing or conflicting evidence remains a named gate. Product requirements and Sage design controls have separate authority. The English guide and extracts are reading aids.

| REF ID | Source and version | Exact location | Supported information and limit |
|---|---|---|---|
| SPFE-S02 | [BOE-A-2026-20587.pdf](<../../context/BOE-A-2026-20587.pdf>); Final order; published 5 October 2026. | Articles 3.4–3.6, 4.1–4.4 and 5.4–5.7 | Public-copy timing, duplicate/withdrawal/correction branches, admission/CSV and exceptional outage window. |
| SPFE-S03 | [CatalogoServicios.pdf](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>); 0.1.0; cover 9 October 2026. | sections 6.2–6.3; pp. 10–12 | Submission batch, per-issuer authority, disputed size and limited withdrawal. |
| SPFE-S01 | [Anexo-1-Proyecto-OM-FE.pdf](<../../context/Anexo I/20261013/Anexo-1-Proyecto-OM-FE.pdf>); Supplied 13 October 2026; SHA-256 in source manifest. | BT-ES-1 p. 4; withdrawal pp. 26–27 | CopyIndicator and invoice-reference withdrawal content. |
| SPFE-S16 | [SendInvoice.wsdl](<../../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | SendInvoice operation, SOAP binding and service ports | PRE submission transport and opaque business attachments. |
| SPFE-S10 | [CancelInvoice.wsdl](<../../context/WSDL servicios web - PRE/20261013/CancelInvoice.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | CancelInvoice operation and payload documentation | Withdrawal transport; not a general legal cancellation or retry mechanism. |
| SPFE-S06 | [RespuestaAltaFacturas.xml](<../../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/RESPUESTA/RespuestaAltaFacturas.xml>); Supplied 13 October 2026; SHA-256 in source manifest. | DocumentResponse and DocumentReference | Example request/item result, locator and response ID; CSV mapping is unconfirmed. |
| REF-PRD | [PRD-SEI-246](../../prds/PRD-SEI-246-spain-invoice-preparation-and-outbound-flow.md); [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md); [PRD-SEI-212](../../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md); [shared platform and country-pack direction](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md). | Product scope and requirement IDs cited in Parts 1–4. | Canonical product requirements. Earlier external-contract assumptions are reconciled with the supplied sources; an unresolved PRD difference needs a product decision, not silent approval. |
| REF-FIELDS | [Complete source-field ledger](../../assets/regulatory/spain/spfe/field-traceability.json); [original BOE XML](../../assets/regulatory/spain/BOE-A-2026-20587.xml). | Exact XML row locators and original cells in the ledger; trace IDs in Part 3. | Complete source-row inventory, logical controls and required acceptance cases. Actual wire/ERP mappings and execution remain unqualified. |
| REF-CONTEXT | [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md); [source manifest](../../assets/regulatory/spain/spfe/source-manifest.json); [shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). | Source register, shared conflicts and terminology. | Reading and traceability aids. Hashes identify snapshots; they do not prove live service acceptance or implementation readiness. |
