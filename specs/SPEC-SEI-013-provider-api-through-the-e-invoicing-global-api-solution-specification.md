---
id: SPEC-SEI-013
title: Provider API through the E-Invoicing Global API Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-06
reviewers: []
related:
  - PRD-SEI-213
  - PRD-SEI-214
  - PRD-SEI-215
  - PRD-SEI-235
  - PRD-SEI-223
  - PRD-SEI-226
  - PRD-SEI-227
  - PRD-SEI-231
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-003
  - SPEC-SEI-006
  - SPEC-SEI-007
  - SPEC-SEI-008
  - SPEC-SEI-009
  - SPEC-SEI-011
  - SPEC-SEI-012
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Provider API through the E-Invoicing Global API Solution Specification

## Part 1 Feature Solution Summary

### Reader guide and design status

**Proposed direction: products and authorised partners use one E-Invoicing Global API contract. Provider API describes the provider-facing capabilities of that contract; it does not require a second API product.** Product and partner permissions, customer authority and supported operations remain different. Provider-owned interfaces may still need Sage-managed adapters.

This is a **reviewable logical proposal**, not an approved API contract or proof of an existing implementation. **Confirmed** means a source-supported product requirement or the user's design brief. **Proposed** means a design choice requiring review. **Open** means missing evidence or an unresolved decision. **Out of scope** means another feature owns the behaviour. Operation, field, state and component names below are logical design identifiers; they do not assert deployed endpoints, schemas or services.

Part 1 explains the decision and journey. [Part 2](#part-2-logical-feature-specification) defines behaviour. [Part 3](#part-3-logical-service-interactions-and-data-inventory) defines the contract and data. [Part 4](#part-4-assurance-and-traceability-view) identifies acceptance, owners and evidence gates.

### 1 Purpose and source authority

The design responds to the user's brief: both products and partners should be able to use the same single E-Invoicing Global API to reduce development and ongoing maintenance. It turns the existing provider requirements into a shared contract proposal, while retaining the connection, routing and historical-continuity controls in the Phase 2 review.

| Source | Authority for this design | Limit or decision required |
|---|---|---|
| User's Provider API brief, 6 October 2026 | Confirms the request to challenge a separate API and assess one shared Global API. | Does not approve an architecture, cost saving, endpoint or production launch. |
| [PRD-SEI-213 — Private Platform Connectivity](../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md), FR1–30 and DR1–8 | Connections remain separate from routes; directions are independent; changes are controlled; existing invoices keep original network context. | Umbrella PRD, not a provider HTTP contract. Per-invoice provider selection and some inbound transition mechanics remain open. |
| [Complete explorer](../work/e-invoice-complete-explorer.html), connection view and `fields.connect`, `fields.send`, `fields.receive` | Illustrates reused legal-entity/authority context, independent connection checks, final exchange evidence and separate lifecycle outcomes. | Prototype and field catalogue, not approved API or legal evidence. Its selectable provider in Send cannot close PRD-SEI-213 DR2. |
| [PRD-SEI-235 — Provider API](../prds/PRD-SEI-235-provider-api-for-e-invoicing-service.md), PA-FR1–20 and PA-NFR1–5 | Provider identity, customer authority, single/batch exchange, retrieval, status/history, events, reconciliation, interconnection and exit controls. | Its Sage-owned provider-facing contract can be implemented as part of the Global API; deployment separation is not established. |
| [Shared platform PRD](../prds/PRD-SEI-227-e-invoicing-as-a-service.md), [routing/transformation PRD](../prds/PRD-SEI-223-interoperability-routing-transformation.md) | Shared capabilities with country/network bindings and preferred DTS transformation assessment. | Does not qualify an existing Global API, DTS build or provider integration for Spain. |
| [Connection/routing review](../prds/PRD-SEI-214-connections-registration-routing-structured-review.md), [resilience review](../prds/PRD-SEI-215-resilience-recovery-reconciliation-structured-review.md) | Owning domains for route transitions and provider recovery. | This API exposes those capabilities; it does not introduce a second route engine. |

No existing Global API contract, deployed build, partner-access policy or conformance results were supplied or identified in these sources. Design review must compare the proposal with the actual service contract. Spain legal claims, time limits, permitted formats and external technical codes remain owned evidence gates; this document does not establish new regulatory facts.

### 2 Proposed API decision and alternatives

| Option | Result and tradeoff | Proposed treatment |
|---|---|---|
| One Global API contract for products and partners | Common invoice identity, operation receipts, errors, lifecycle, versioning and support. Partner-only capabilities need scoped permissions and external conformance. | Preferred starting point, subject to API/security/compatibility qualification. |
| Separate product and provider API products | Independent releases and exposure policies, but risk duplicate models, mapping, documentation, testing and operation ownership. | Require a demonstrated constraint that the shared contract cannot meet safely or compatibly. |
| One contract with distinct exposure or deployment controls | Shared semantics and version ownership; gateways, credentials, quotas or runtimes may be separated where justified. | Permitted implementation choice under GPA-Q02; one API contract does not require one deployment or host. |

**Proposed decision rule:** add a second API product only after documenting the exact security, compatibility, legal or operational constraint; the shared-contract alternatives considered; the cost; and the accountable owner. Do not infer a second API solely from the word “provider”. Do not promise savings until the baseline and incremental partner work are measured.

The integration modes in PRD-SEI-235 still apply per capability:

| Source mode | Meaning under the Global API proposal | Ownership rule |
|---|---|---|
| `PROVIDER_API` | Provider consumes authorised capabilities of the Sage Global API. | Sage owns API resources; the provider may own an assigned external delivery action. |
| `SAGE_ADAPTER` | Sage calls an evidenced provider-owned API, mailbox, callback or file interface. | Adapter executes the named operation through the shared domain services. |
| `HYBRID` | Different capabilities use different boundaries. | Each mutation has one execution owner and one reconciliation owner. Both paths cannot send the same delivery leg. |

Bidirectional invoice exchange describes business direction. It does not require both parties to host APIs or initiate calls. Partner pull plus partner submission can provide both directions; callbacks and adapter calls are separate, qualified choices.

### 3 Scope, outcomes and terms

In scope: consumer onboarding and capability readiness; scoped customer access; provider connections; authorised single/batch invoice intake; partner delivery work where selected; inbound ingestion and authorised retrieval; lifecycle evidence and history; events and reconciliation; permissioned route-transition access; Spain interconnection case tracking; suspension, exit, versioning and operational controls.

Out of scope: building or deploying the API; defining provider-specific endpoints; ERP issuance; transformation/signing implementation; a new invoice store or route engine; unrestricted directory search; approving Spain legal rules; automatic failover; Private A → Private B transition; final retention/deletion policy; and enabling per-invoice route override before DR2 approval. These remain in their owning features.

| Term | Plain-language meaning |
|---|---|
| Consumer / principal | A product application or partner service calling the API; the principal is its trusted identity. |
| Provider / partner | Provider operates an invoice-network capability. Other partners may act as delegates or product integrators; partner status alone does not give provider execution rights. |
| Authority grant | Recorded permission for a named principal to perform a capability for a legal entity, scope and time. Login or a certificate does not supply this permission. |
| Connection / registration / route | Configuration to communicate; external enrolment/reachability; and the time-bound selection used for new invoice work. |
| Delivery leg | One independently tracked recipient delivery, public copy or reporting action. |
| Idempotency / reconciliation | Repeating the same logical request adds no effect; checking authoritative evidence to find what happened after an uncertain result. |
| Work item / execution owner | An assigned external action and the party allowed to execute it. Retrieval of an invoice is not permission to transmit it. |
| Representation / provenance | A specific invoice file or data form; evidence of its source, transformations and versions. |
| Durable receipt | Confirmation that Sage saved the operation for recovery; it does not prove delivery or buyer acceptance. |

| Observable outcome | Meaning and boundary |
|---|---|
| Consumer ready for a named capability | Qualified identity, contract and sandbox/production evidence; no automatic customer or route access. |
| Connection ready for a direction/profile | That capability is available for the customer; active routes remain unchanged. |
| Operation accepted or rejected | Saved receipt/per-item result, or safe error with owner; asynchronous acceptance is not external success. |
| Invoice available within permitted scope | Stable identity, original/derived representation references and history; retrieval/acknowledgement is not buyer acceptance. |
| Delivery/lifecycle evidence recorded | Original source and independent leg/state outcome retained; unknown outcome is a recovery state. |
| Access suspended/ended | New protected actions stop under policy; unresolved work and historical evidence have explicit continuity owners. |

### 4 Spain use and reuse qualification

| Capability/source | Intended Spain use | Reuse classification and local changes | Gap, owner and activation evidence |
|---|---|---|---|
| Global API | Products and approved partners share resources and operation semantics. | Existing implementation reuse candidate; coverage unknown. Add partner permissions/operations only where actual gaps exist. | API owner + Architecture: deployed contract/build, current consumers, identity model, compatibility and external exposure proof. |
| Receipts, authority, audit and event recovery | Isolate consumers/entities and recover repeats or missed outcomes. | Reusable proposed design pattern; no deployed coverage claimed. | Service owners + Security: actual store/outbox, concurrency, revoke-race, replay and isolation tests. |
| [Outbound SPEC-SEI-007](SPEC-SEI-007-spain-invoice-preparation-and-outbound-solution-specification.md), [inbound SPEC-SEI-006](SPEC-SEI-006-inbound-invoice-receiving-solution-specification.md), [lifecycle SPEC-SEI-009](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) | Reuse the proposed invoice, leg, representation and evidence boundaries. | Shared design patterns requiring country/provider binding. API delegates to these owners. | Domain owners: actual contracts/builds and gaps; qualify profile, execution owner, mapping and acknowledgement meaning. |
| Existing DTS; [SPEC-SEI-008](SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) | Preferred transformation candidate when an authorised exchange needs a supported source/target representation. | Existing implementation candidate plus proposed Spain mapper migration pattern. No blanket inbound, four-syntax or signed-document support assumed. | DTS + Spain mapping owners: build, input/output contracts, mappings, rule packs, semantic preservation, custody, limits and on-call evidence for each selected pair. |
| Provider adapters and public connector | Execute capabilities not owned by a partner through the shared API. | Implementation coverage unknown; each provider/network needs its own adapter or contract qualification. | Provider owners + [SPEC-SEI-011](SPEC-SEI-011-public-platform-connector-solution-specification.md): exact interface, initiator, credentials, registration, query/replay and operations evidence. |
| Identity, routing and lifecycle/reporting policy | Apply approved Spain rules for the selected entity, network and capability. | Shared services with country rules; Spain-specific identifiers, route/public-copy/reporting duties and interconnection calendar remain local. | Spain Product/Compliance: approved rule/version and applicability evidence; no Spain default in another country. |

A reusable design pattern is not an existing implementation. Every candidate needs the actual source capability/build, local changes, missing coverage, accountable owner and acceptance evidence before activation. GPA-A17/A18 test country isolation and reuse qualification.

### 5 Process diagrams and lifecycle

![Global API access, connection and route control](../assets/diagrams/global-api-access-and-route-process.svg)

[Editable Draw.io](../assets/diagrams/global-api-access-and-route-process.drawio) · [PNG preview](../assets/diagrams/global-api-access-and-route-process.png).

Text equivalent: GPA-01 qualifies the product or partner consumer → GPA-02 associates existing legal-entity authority and tests a connection by capability → GPA-03 authorises each request through the common API. Ready connection leaves current routes unchanged. A separate GPA-09 transition checks authority, direction, conflicts and effective time; uncertain external activation reconciles before commit. GPA-10 records an interconnection case where required. GPA-11 independently controls suspension, grants, routes and continuity; GPA-12 owns recovery/version changes.

![Global API invoice exchange and reconciliation](../assets/diagrams/global-api-exchange-and-reconciliation-process.svg)

[Editable Draw.io](../assets/diagrams/global-api-exchange-and-reconciliation-process.drawio) · [PNG preview](../assets/diagrams/global-api-exchange-and-reconciliation-process.png).

Text equivalent: GPA-03 checks trusted identity and current authority → GPA-04 validates operation intent and saves one durable receipt per accepted invoice/item → GPA-05 delegates customer send or inbound receipt to its owning service. A final exchange plan assigns each leg to an adapter or partner executor. GPA-06 records source evidence and independent outcomes. A possible external mutation with no result is held for GPA-08 reconciliation before replay. GPA-07 supplies authorised retrieval/history and separate acknowledgements. GPA-08 publishes durable events and supports missed-event recovery. GPA-12 resolves faults without changing original route or business data.

| Activity / actor and trigger | Preconditions, operation and postcondition | Exception and recovery owner |
|---|---|---|
| GPA-01 Consumer administrator requests access | Contract, identity, environment and capability reviewed; save qualification and consumer state. | API/Security: incomplete or incompatible consumer stays action-required; no route activation. |
| GPA-02 Customer/product/delegate associates provider | Existing legal subject and authority verified; store connection and independent readiness evidence. | Identity/provider owner: missing grant or profile holds only the affected capability. |
| GPA-03 Product/partner calls API | Trusted principal, current grant, country/environment, action and object scope checked. | API/Identity: deny and audit without exposing another entity or provider. |
| GPA-04 Caller submits invoice(s) | Declared intent, exact revision/source, scope and repeat identity validated; durable per-item acceptance or rejection. | API/intake: changed-key conflict, invalid input or incomplete durable acceptance; recover original receipt. |
| GPA-05 Domain executes accepted intent | Receiving ingests; outbound fixes final route/profile/legs; exactly one executor selected per external leg. | Domain/executor: blocked readiness, unknown result or conflicting claim held; no fallback send. |
| GPA-06 Provider/adapter supplies outcome | Correlate authorised evidence to original invoice/leg; append raw event and derive views. | Lifecycle: unknown reference quarantined for reconciliation; duplicates/reordering do not regress state. |
| GPA-07 Consumer retrieves or acknowledges | Authorised current/historical invoice, representation and cursor access; acknowledgement saved separately. | Records/distribution: missing object, cursor expiry or revoked grant has a scoped recovery path. |
| GPA-08 Event worker/consumer observes change or gap | Durable publication, bounded delivery/replay and authoritative read; close only evidenced gaps. | Events/Operations: retry notification safely; uncertain business mutation reconciles before repetition. |
| GPA-09 Authorised actor requests route transition | Qualified target and direction, expected route version and effective time; owning route service controls cutover. | Route owner: cancel pre-irreversible work; uncertain activation reconciles; rollback is a new controlled transition. |
| GPA-10 Authorised actor requests interconnection | Record parties, entity scope, evidence, responsible owner and approved Spain deadline rule if available. | Spain/Operations: unresolved clock/capability blocks claimed readiness, not hidden as connected. |
| GPA-11 Owner changes or ends access | Classify credential, grant, capability, subscription, route or registration action; preserve approved continuity. | Security/domain/Operations: outstanding work receives a named recovery owner; revocation never silently widens access. |
| GPA-12 Support/release owner acts | Permissioned reconciliation, correction, migration or rollback with evidence and version checks. | API/domain owner: no unsafe replay, retroactive reroute or unapproved compatibility break. |

### 6 Ownership, dependencies and risks

The Domain Service Product Owner owns the shared product/partner proposition and scope. The Global API owner owns contract, external documentation and compatibility. Identity/Security owns consumer identity and customer-authority checks. Connection/Routing owns readiness and transitions. Exchange/Receiving owns invoice processing and leg assignment. Lifecycle owns evidence interpretation. DTS/Trust owns qualified transformations and protected signing. Provider owners own interface evidence; Operations owns support and reconciliation; Spain Product/Compliance owns local policy and interconnection evidence. Named individuals remain GPA-Q01.

The main risks are role confusion, exposing another customer's data, duplicate transmission across API/adapter paths, callbacks treated as truth, shared-model changes breaking products, and Spain rules becoming global defaults. Gates in Part 4 must resolve them before pilot or production.

## Part 2 Logical Feature Specification

### 1 Shared contract and permission model

**Proposed:** one API contract catalogue, shared resource identities, error vocabulary and version policy. Products and partners call only operations permitted to their principal and current customer grant. Separate credentials, quotas, access policies and documentation views may be needed. A common contract does not make all consumers trusted equally.

| Capability | Product application | Delegated partner | Qualified provider executor |
|---|---|---|---|
| Consumer onboarding/configuration | Product administration under approved control-plane policy. | Partner administration of its own identity/subscriptions. | Same partner administration, plus provider conformance. |
| Customer connection/readiness | Named customer-admin permission. | Explicit customer-admin delegation only. | May supply account/capability evidence; cannot grant itself customer authority. |
| Draft preparation/final customer send | Issuer/customer authority; ERP retains issuance ownership. | Explicit issuer/delegate authority and qualified input contract. | Same rule if acting as issuer delegate; execution assignment alone is insufficient. |
| Inbound invoice ingest | An approved product ingestion role, if needed; not implicit in send permission. | Only if expressly qualified for source delivery. | Named receiving/source capability, matched entity and origin connection. |
| Retrieve invoice/status/history | Granted product/dataset/entity scope. | Granted customer/direction/history scope. | Own assigned work or approved retrieval scope; not every invoice for the customer. |
| Claim delivery work/report network evidence | Denied unless separately registered as executor. | Denied unless separately qualified as executor. | Explicit leg assignment, direction/profile and environment qualification. |
| Report buyer rejection/payment | Explicit business-actor authority. | Explicit relevant delegation. | Network evidence permission alone cannot invent buyer decisions. |
| Route change/interconnection case | Separate administration permission. | Explicit administration delegation. | Own technical evidence only, unless separately granted administration. |
| Route/readiness read and recipient lookup | Approved entity/purpose scope. | Explicit lookup/read delegation. | Approved country/provider lookup scope; no unrestricted directory access. |
| Audit/support/recovery | Separately permissioned safe view. | Own scoped view, where approved. | Own scoped view; broad Operations access is separately controlled. |

Do not implement a single role test that grants every provider all partner operations. Capability and customer authority are independent dimensions. An accountant's portfolio login is evaluated per client; neither a portfolio mandate nor a provider certificate supplies universal invoice access/signing rights.

Direction is relative to the represented legal entity: OUTBOUND means the entity is issuer; INBOUND means it is recipient. Network origin and the calling application's location do not define business direction. Where a provider also represents another party, that is a separate authority context.

### 2 Invariants and state boundaries

| ID | Required rule |
|---|---|
| GPA-R01 | A provider-facing capability belongs to the proposed Global API contract; any separate API needs a recorded justification and decision. |
| GPA-R02 | Authenticate principal/environment and independently authorise customer, action, direction, object and effective time on every protected operation. |
| GPA-R03 | Consumer readiness, grant, connection, registration and route are separate records; no general CONNECTED flag or implicit route switch. |
| GPA-R04 | Same scoped request identity and digest resume one logical operation; changed content/intent conflicts; no duplicate effect across execution paths. |
| GPA-R05 | Acceptance, validation, recipient delivery, public copy, buyer acceptance, payment and notification acknowledgement have separate outcomes. |
| GPA-R06 | Exactly one execution owner and reconciliation owner are bound to each external mutation; possible mutation with unknown outcome cannot be blindly repeated. |
| GPA-R07 | Original bytes/evidence, revisions, source and final route/profile/contract versions remain explainable after later changes. |
| GPA-R08 | Retrieval, paging, product distribution and executor work claims have distinct purposes; reads do not authorise delivery. |
| GPA-R09 | Evidence/events are scoped, deduplicated and provenance-preserving; notification is recoverable through authoritative reads. |
| GPA-R10 | Route transitions use the owning route service, direction scope and concurrency checks; existing invoices keep original context. |
| GPA-R11 | Customer data, credentials, environments, countries and consumer workloads remain isolated with permissioned audit. |
| GPA-R12 | Spain rules and provider capabilities are explicit versioned bindings, not global defaults or inferred production readiness. |
| GPA-R13 | Suspension, credential/grant removal, route deactivation, deregistration, subscription termination and retention are independent controlled actions. |
| GPA-R14 | Partner extension/version rollout preserves supported product contracts; service limits and compatibility targets need measured evidence and owners. |

Proposed consumer states are DRAFT → VALIDATING → READY_FOR_CAPABILITY, with ACTION_REQUIRED, SUSPENDED or REVOKED as applicable. Connection readiness is a matrix of capability/direction/profile/environment and evidence validity. A disabled capability does not erase an independently ready one.

Operation state is distinct from invoice state: RECEIVED is local intake; ACCEPTED means a recoverable operation was committed; PROCESSING, BLOCKED or OUTCOME_UNKNOWN describe subsequent work; COMPLETED or REJECTED require evidence for the specific operation. Unknown is not rejection. Events and receipts include the stage and leg they describe. Cancellation stops only work that can still be safely stopped; already executed or uncertain external work follows its original recovery path.

### 3 Lifecycle behaviour

**GPA-01 Qualify a consumer.** A product administrator or partner requests sandbox access with organisational identity, requested capability set, contract version, environment and support responsibility. API/Security verifies identity and permissions; Engineering records conformance results separately for submissions, retrieval, executor work, evidence, events and reconciliation. Production activation requires its own evidence. Store protected credential references; do not return private keys or reuse a product secret for a partner. Authentication protocol, trust material and exposure topology are GPA-Q02/Q03. Credential rotation supports only an approved overlap; revocation stops use immediately under the agreed enforcement target. The API exposes safe configuration/readiness metadata, not secrets. Consumer onboarding does not create a customer or select a route.

**GPA-02 Bind customer authority and connection readiness.** An authorised product/customer administrator or delegate associates the consumer/provider with an existing tenant, legal subject, environment and intended directions. Reuse the verified identity and authority context from onboarding; do not onboard the company again merely to add a provider. Verify the proposed grant against its evidence and effective interval. A provider cannot approve its own grant. Connection checks separately record account/registration, authentication, format/mapping, signing where required, direction, reachability, callback if selected, and reconciliation support. A provider without callbacks can qualify a pull/reconciliation mode if approved; callback readiness is not a universal requirement. Store limitations and observed time. Missing profile, failed credential or insufficient signer authority holds only the affected scope. Changes use an expected configuration version and audit. A successful connection check leaves public routes unchanged. Registration mutations with unclear results reconcile through the selected provider owner before repetition.

**GPA-03 Authorise every operation.** Resolve trusted consumer identity, environment and allowed contract version. Resolve the requested tenant/legal subject, grant, country/network binding, action/direction and object visibility from server-owned records. Caller-supplied tenant, provider, role or grant IDs are selectors, not proof. Check actor authority separately from service authentication and certificate/trust readiness. Check revoked/suspended/effective state both at intake and before a protected execution/read disclosure. Pagination, work claim, event replay, acknowledgement, download and manual recovery undergo the same scope checks. Denied requests return a safe error/correlation without confirming another customer's object existence. Log safe audit metadata with no bearer tokens, full invoice bodies or raw restricted provider diagnostics.

**GPA-04 Accept a single or bounded batch invoice operation.** The caller declares a qualified intent: prepare draft, send an issued invoice, or ingest a received invoice. These are distinct capabilities sharing common resources. A provider delivering an inbound invoice cannot accidentally invoke an issuer send that creates a routing loop. Draft/final issuance behaviour delegates to SPEC-SEI-007; intake does not issue the invoice. Preserve caller source identity, exact revision/content digest, representation/profile, authority context and idempotency identity. Source files use an approved bounded upload/reference mechanism; arbitrary caller URLs are not fetched.

Scope idempotency by environment, consumer, entity, logical operation/intent and caller key; store request digest and receipt. A same-key same-digest retry returns the existing operation; same-key changed content, intent or entity conflicts where it addresses the existing scope. A new key is not permission to resend the same business invoice: domain duplicate checks include stable source invoice/revision, origin/provider references and content evidence under the owning duplicate policy. Cross-consumer duplicate handling cannot disclose an invoice to a consumer without access. Distinct credit/correction documents remain distinct and carry links required by the owning lifecycle policy.

Commit accepted operation, idempotency result and durable work/event intent as one recoverable acceptance boundary. An incomplete commit cannot return ACCEPTED. The storage/outbox implementation is GPA-Q05. If the client times out before seeing acceptance, it resumes the original key/receipt; it does not invent another invoice identity. Batch limits are GPA-Q09. Structural invalidity may reject the batch envelope; a valid envelope produces independent per-item authority, digest, receipt and outcome, including partial acceptance. Replaying a batch resumes accepted items and does not erase failed-item evidence. Corrected rejected items need a new linked request/revision; changing an accepted item under its old key is prohibited.

**GPA-05 Process intent and assign execution.** Received invoice intake delegates to SPEC-SEI-006, retaining original/source evidence, identity, duplicate/quarantine result and product distribution context. Final issued sends delegate to SPEC-SEI-007, including final validation, recipient evidence from SPEC-SEI-012, trust and a fixed plan. The plan records route/connection/provider/direction, rule/profile/mapping versions, exact artefact references and independent recipient/public-copy/reporting legs where applicable. The Global API does not introduce another transformation or signing engine; qualify DTS and Trust for the selected scope.

For each external leg select `SAGE_ADAPTER` or qualified partner execution under `PROVIDER_API`; a hybrid splits capabilities explicitly. **Proposed pull execution:** a provider queries assigned work, then claims a work item using a current version and a bounded claim token. Only the claimant may obtain execution content and report results for that generation. Retrieval alone cannot claim work or invoke another send. Save durable ownership/send intent before external transmission. The provider must support original-reference queries or evidence-based reconciliation of its execution. Exact claim, renewal, expiry and cancellation contracts are GPA-Q04/Q05.

A claim timeout or worker crash after possible transmission creates unknown outcome. Lease expiry must not automatically give another worker permission to retransmit. Mark the original action for reconciliation; issue another execution permission only after evidence establishes non-execution or the provider's proven idempotency contract makes it safe. Callback/push execution, if selected instead of pull, needs equivalent durable ownership and receipt semantics. The adapter path follows the same rule. Never allow adapter failover to duplicate a partner-owned leg. Successful recipient delivery does not repeat when a separate copy/reporting leg fails. Authority is rechecked before first execution; if it is revoked after transmission, preserve the outstanding action and assign an authorised reconciliation path.

**GPA-06 Record source evidence and lifecycle.** A provider executor or adapter supplies source event identity, invoice/leg/correlation, external reference, raw state/code, occurrence/observation time, evidence reference and contract/mapping version. Verify the source's permission for that invoice and original operation. Persist evidence before projection/publication; repeats return the original receipt. Same event identity with changed evidence is a conflict requiring investigation. Unknown invoice/reference, unsupported code or unmatched leg is held in a restricted reconciliation record, not matched by invoice number alone. Retain raw evidence with safe public views under policy.

SPEC-SEI-009 owns interpretation into technical, validation, delivery, commercial and payment/reporting dimensions. Late/out-of-order evidence cannot blindly move a view backward. Corrected evidence is appended with an explicit supersession link; it does not overwrite history. A provider's transport receipt does not establish buyer acceptance/payment. Business rejection or payment reporting requires its own actor authority and country rule. A post-switch event resolves through the invoice's original provider/connection, not today's default route.

**GPA-07 Retrieve, download and acknowledge.** Authorised consumers query invoices, status/history and scoped operation/work outcomes. Query filters include entity, direction, environment, source and updated/change position where qualified. Use stable, opaque cursors bound to consumer/access scope, filters and snapshot/change position. Order by a deterministic position with a stable tie-breaker; the exact paging model is GPA-Q06. Preserve source event time separately from change position so a late event remains discoverable. Re-evaluate authority on every page and artefact access; an expired/revoked cursor cannot widen rights.

Empty authorised results mean no matching records in that query scope; they do not mean global absence, denied access or source unavailability. Expose coverage/freshness and cursor expiry safely. Read paths include historical invoices visible under an explicit grant, independently of the currently active route. Grant history scope needs a decision; route continuity does not grant a former provider perpetual access. Download provides an approved, bounded reference to the permitted original/derived representation, or a safe unavailable/quarantined outcome. No secret or unrestricted evidence reference is returned.

Product distribution acknowledgement, provider work claim/completion, notification receipt and buyer business response are separate operations. Persist the named acknowledgement and return it on duplicate; its meaning/version and authorised actor remain visible. Advancing a consumer checkpoint requires all covered items to have durable acknowledged outcomes or explicit durable exception records. A provider without permission for an item cannot obtain it by acknowledging an adjacent page. Cursor expiry returns a controlled restart/reconciliation action that preserves deduplication identity.

**GPA-08 Notify and reconcile.** Save a publishable event with the domain change or through a recoverable outbox boundary. Each event contains stable event ID, type/version, invoice or operation reference, entity/environment, leg where applicable, source occurrence time, publication/change position and authorised safe payload. Event types include operation result, invoice availability, lifecycle change, work availability and capability/transition change. Delivery-attempt IDs are distinct from the stable event ID. Subscribe only to permitted capabilities/entity scope; event delivery does not widen invoice access.

Callbacks, if selected, use the approved authenticated transport and endpoint validation policy; reject arbitrary endpoints and unapproved redirects. Recheck subscription/grant/revocation before disclosure. Consumers deduplicate and tolerate reordering, record a durable receipt before acknowledgement, and query authoritative state/history for gaps. Notification receipt is not processing success or buyer acceptance. Bounded retries use the approved retention/backoff/rate policy; exhausted delivery goes to an owned operational queue while source history remains available under policy. No numeric interval or indefinite retention is assumed.

Missed-event recovery uses an authorised change cursor plus current object/history reads, with overlap/deduplication and an explicit expired-window outcome. Unknown external mutations query the original executor/provider reference and evidence. Confirmed success records the result; evidenced non-execution permits a controlled retry; a still-unknown result stays held and escalates. Manual closure needs evidence and an authorised actor. Neither a stale callback nor a missing notification permits re-executing business work.

**GPA-09 Expose controlled route transitions.** A separately authorised actor requests the legal entity, direction, source/target, expected route version and effective time. The owning route service checks readiness, grant, conflicting transitions and historical-continuity impact. It performs reversible preparation, tracks the irreversible boundary, reconciles external changes and atomically records the effective route for the selected scope. Cancel only before the safe cancellation boundary; rollback after activation is a new qualified transition. Unknown activation cannot expose conflicting active routes. Invoice planning at cutover uses one deterministic decision/version and preserves it. Do not rewrite existing plans, automatically deregister the old connection, or broaden inbound permission because outbound is ready. Per-invoice selection illustrated in the explorer stays disabled unless PRD-SEI-213 DR2 closes with precedence, permission and audit rules.

Authorised products/partners may also read their permitted connections and effective routes, and request scoped recipient lookup where the country/provider capability is approved. Delegate lookup to SPEC-SEI-012. Return source, scope, observed time, rule version, freshness and private/public-supported/unresolved classification; never expose another customer's credentials or private configuration. An early lookup is advisory and cannot replace final exchange evidence. Missing, stale, partial or competing results remain unresolved rather than selecting an arbitrary provider or proving public fallback.

**GPA-10 Track Spain interconnection requests.** Record requester, participating platforms, represented entity/scope, capability/profile, evidence, request/effective/observed times, assigned owner, current case state, actions and escalation. Apply only a Compliance-approved deadline rule with trigger, calendar, pause/extension behaviour and evidence. Until that rule is approved, expose missing-rule/action-required rather than a compliant deadline. Tracking a case does not assert that technical interconnection is ready, that Sage has an approved operator role, or that a provider has completed it. The case links provider conformance and route-readiness evidence without changing routes itself.

**GPA-11 Suspend, revoke and exit safely.** Administrative requests identify whether they affect consumer credentials, a customer grant, capability, subscription, route, connection or registration. Check expected version, effective time, authority and reason; record separate outcomes. Credential compromise can require immediate block without waiting for business drain. Stop new protected reads/mutations/execution under the suspension/revocation rule; classify accepted but unexecuted, executed, unknown, and historical work separately. Cancellation/compensation depends on the original activity and external evidence; no deletion or automatic retransmission follows revocation.

Preserve minimum required evidence and outstanding reconciliation. Select an authorised continuity owner or hold with explicit support action. Historical consumer access requires a remaining grant and policy; revoked authority cannot be bypassed by old links/cursors. Terminate event disclosure under its independent policy. Do not disable/deregister a connection needed by non-terminal invoices unless an approved continuity exception exists. [SPEC-SEI-003](SPEC-SEI-003-offboarding-solution-specification.md) owns final customer offboarding; record its dependencies without implementing retention/deletion here.

**GPA-12 Recover, evolve and operate.** Support actions are scoped, permissioned and audited with expected state/version, reason and evidence. Reconciliation, failed-notification redelivery and a proven-safe business retry are separate actions. Correct input through a linked new request/revision under the original domain rules; never alter an issued invoice in place. Contract versions pin accepted operations/events; configuration/country-rule updates apply prospectively. A supported old product consumer continues to work while partner extensions are piloted. Deprecation requires a qualified consumer inventory, compatibility decision, approved notice/window and exercised migration/rollback. Rollback changes new work; it does not move in-flight operations to another executor or erase history. Capacity controls isolate provider/customer backlogs; degraded behaviour exposes its fault owner instead of silent fallback.

Permissioned audit/health reads return only the consumer's approved scope and safe operational data: capability health/limitations, applicable limits, pending/unknown operation age, event/reconciliation freshness and action owner. Broader Operations access is a separate entitlement. Restricted audit, raw diagnostic or other-provider/customer data is not returned through the partner view.

### 4 Error and recovery contract

Logical error categories are proposed; exact HTTP mapping, public codes and message schemas require GPA-Q02. Each safe response includes category, stage, correlation/operation reference where authorised, retry/reconcile/correct action and responsible owner. Detailed diagnostics remain restricted. No error tells a client to retry an uncertain mutation blindly.

| Category | Effect and safe next action | Owner |
|---|---|---|
| Authentication/authority denied | No protected operation/disclosure; renew identity or obtain approved scoped authority. | Consumer admin / Identity. |
| Contract/input/profile invalid | No unsupported processing; correct through linked request/revision. | Consumer / API / country/profile owner. |
| Idempotency/version conflict | Preserve original result; query it or submit an approved distinct operation. | Consumer / API / domain. |
| Not ready/unresolved route | Hold affected work with failed gate/evidence; no automatic route substitution. | Connection / Routing / provider owner. |
| Limit/backpressure | Indicate bounded delay/retry guidance; retain accepted receipt; a rejected request creates no accepted work. | API Operations / consumer. |
| Unavailable before effect proven | Controlled retry under operation policy, original identity retained. | Service/executor owner. |
| Outcome unknown | Preserve original intent/correlation and reconcile authoritative state before replay. | Original reconciliation owner. |
| Cursor/event window expired | Rebuild authorised checkpoint with overlap/current history and deduplication; expose remaining coverage limits. | Records / Events / consumer. |
| Evidence mismatch or security concern | Restricted hold/investigation; safe reason to the authorised consumer. | Lifecycle / Security / Operations. |

### 5 Security, service quality and audit

**Required:** least privilege; encrypted approved transport/storage; separate sandbox/production principals, credentials, data and subscriptions; qualified secret custody; tenant/entity/provider/country isolation; protected original/derived documents; audit access that omits secrets and unnecessary business data. Work claims are bound to principal, operation and generation. Download references and callbacks cannot bypass current authority. Apply bounded upload/parser checks and quarantine unsafe content under the receiving owner; exact file/profile/security controls require qualification. Provider administrators cannot create customer grants or promote their own production readiness.

Audit actor/principal, action/scope, source/expected/new version, safe outcome, reason, policy/contract version, event/operation/leg correlation and recovery evidence. Keep authoritative invoice/evidence stores as their systems of record; API caches and notifications are views. Legal retention, deletion, audit and idempotency/event recovery windows are separate policies and require GPA-Q10. Loss of retained bytes/versions under an approved policy means recovery may become unavailable; do not promise permanent replay.

| Measure / control | Definition and approval gate |
|---|---|
| Contract/maintenance effort | Baseline existing API/adapters, new partner-only work, duplicated models/tests, support and release effort; API Product owns comparison before claiming savings. |
| Service quality | Measure API durable-acceptance latency separately from domain validation, each delivery leg and lifecycle freshness. API/domain Operations set targets by capability. |
| Capacity/fairness | Bound payload, batch, page, concurrency, backlog and provider/customer quotas; prove one noisy consumer does not starve others. |
| Recovery | Measure oldest unknown operation, event gap, retry backlog and reconciliation age; accountable owner and alerts before production. |
| Security/continuity | Measure revocation enforcement, stale-authority disclosure prevention and historical grant coverage; Security/domain owners approve thresholds. |
| Compatibility | Consumer inventory, conformance pass rate, migration completion and rollback evidence; API owner approves supported versions and deprecation window. |

Numeric limits, latency, service levels, retention and statutory clocks remain open. Required evidence is measured capacity, selected partner/product workloads and approved operating objectives, not assumed global values.

## Part 3 Logical Service Interactions and Data Inventory

### 1 Logical operation catalogue

These are capability names for contract review, not invented production URL paths. GPA-Q02 will map them to the actual Global API resource/schema catalogue and produce a versioned API definition. Extend existing equivalent operations before creating duplicates. Admin operations may use a separately secured control-plane exposure under the same contract ownership.

| Interaction / lifecycle | Caller → owner; logical input → output | Authority, repeat and recovery |
|---|---|---|
| GPA-INT-01 / GPA-01 | Consumer administrator → API registry; identity, environment, capability/version and conformance → consumer/readiness reference. | Admin role; versioned/idempotent configuration; incomplete evidence stays unready. |
| GPA-INT-02 / GPA-02/03/11 | API/domain → Identity; principal, entity, action, direction, environment and time → grant/decision/version. | Trusted service context; no credential-as-authority substitution; deny revoked or stale scope. |
| GPA-INT-03 / GPA-02 | Authorised administrator → Connection; legal subject, provider account/secure references, direction/profile/environment → connection and readiness matrix. | Customer-admin grant; request/config version; reconcile uncertain registration, no implicit route change. |
| GPA-INT-04 / GPA-04 | Product/partner → API intake; declared invoice intent, exact revision/source/artefact, scope and key → durable operation/receipt or per-item errors. | Intent-specific grant; scoped key/digest and domain duplicate policy; recover original receipt after timeout. |
| GPA-INT-05 / GPA-05 | API worker → Exchange/Receiving; accepted receipt and pinned scope/input → intake result or plan with legs/executors. | Service plus current action authority; repeat original operation; domain hold/unknown keeps original context. |
| GPA-INT-06 / GPA-05 | Exchange → qualified DTS/Validation/Trust; source/target profile, rule/mapping/trust versions and references → qualified representation/evidence. | Protected service/custody scope; version-pinned transform/request identity; no unqualified default mapping or signing. |
| GPA-INT-07 / GPA-05 | Assigned provider → Work service; scoped query, claim/version and operation → permitted work, claim and exact content reference. | Qualified executor/leg assignment; generation-controlled claim; expiry after possible effect requires reconciliation. |
| GPA-INT-08 / GPA-05/08 | Exchange/reconciler → Sage adapter/provider contract; original leg/reference/profile → external receipt, query evidence or unknown result. | Selected execution/reconciliation owner only; proven provider repeat contract or authoritative query; no automatic second executor. |
| GPA-INT-09 / GPA-06 | Provider/adapter → Lifecycle evidence intake; event/source/leg/reference/state/time/evidence → durable evidence receipt and later projection. | Original-invoice source scope; event identity/digest; mismatched/unknown evidence held. |
| GPA-INT-10 / GPA-07 | Product/partner → Records/Lifecycle; permitted filters, invoice/operation and cursor → scoped page, history, representation or outcome. | Recheck grant per read/page/download; deterministic cursor; expiry gives bounded restart, not unrestricted history. |
| GPA-INT-11 / GPA-07 | Permitted consumer → Distribution/Work/Events owner; named receipt purpose, object/version and evidence → acknowledgement result. | Purpose-specific authority; deduplicate acknowledgement; no implied buyer decision or external transmission. |
| GPA-INT-12 / GPA-08 | Events → qualified callback / authorised consumer → Events change read; scoped subscription/change cursor → stable events, delivery receipt or gap/expiry. | Subscription/grant check before disclosure; durable event, attempt identity, replay/overlap; current object/history remains authoritative. |
| GPA-INT-13 / GPA-08/12 | Reconciler → original operation owner; invoice/leg/external reference, event gap or receipt key → evidenced outcome/retry permission/held case. | Recovery role plus original scope; no changed identity or blind replay; append decision evidence. |
| GPA-INT-14 / GPA-09 | Authorised product/partner → Routing/Lookup; scoped route/readiness read or recipient lookup → evidence/version/freshness/decision; separately, expected route, target, effective time or cancel/rollback intent → transition result. | Read/lookup and route-admin grants differ; country/source scope, owning concurrency/reconciliation contract; old invoice context retained. |
| GPA-INT-15 / GPA-10 | Authorised actor/Operations → Spain case service; parties, scope, request/evidence, rule reference → case/action/deadline status. | Case-admin scope; versioned updates; absent approved rule does not produce a compliant clock. |
| GPA-INT-16 / GPA-11/12 | Security/domain/release administrator → relevant control owner; revoke/suspend/exit/version action, expected version, reason/evidence → independent result and continuity actions. | Separate administrative permissions; idempotent/versioned; unresolved work remains owned and audited. |
| GPA-INT-17 / GPA-12 | Authorised consumer/Operations → Audit/Health; permitted consumer/entity/capability and operation scope → safe audit, health, limits, unknown/pending age and freshness. | Scope-specific audit/health entitlement; no mutation, secret, restricted diagnostic or cross-consumer data; stale/unavailable health is explicit. |

All protected interactions carry trusted principal/environment context and safe correlation. The API façade routes to the existing owning service where qualified; the logical inventory does not prescribe separate services.

### 2 Shared request, receipt and event semantics

Proposed request envelope includes request correlation, declared operation intent, legal-subject/access context, environment/country, idempotency key for mutations, expected object version where required and payload/profile references. Caller assertions are verified against trusted identity and server records. Required fields and permitted defaults vary by operation; no silent Spain default fills a missing country rule.

Receipt includes stable operation ID, request identity/digest reference, accepted/rejected/pending state, accepted time, authorised result reference and per-item outcomes for batches. Evidence responses distinguish stage, leg, source event time, observed time, contract/rule/mapping version and safe action owner. Status views expose independent dimensions with provenance; they do not flatten all progress to SENT.

Proposed event envelope includes stable event ID/type/schema version, change position, safe entity/environment and resource references, operation/leg correlation, source/observed/published times and permitted evidence/state summary. Full invoices, credentials and raw restricted evidence are not embedded by default. Schema evolution and whether references use signed access links are GPA-Q02/Q03/Q06 decisions. Replay uses the same event identity with a new delivery attempt identity.

### 3 Data inventory and systems of record

Logical records below may belong to existing stores. Creating another API invoice ledger or another authority database is not implied. Retention periods and permitted deletion depend on GPA-Q10 and the owning legal/security policy; versioned records preserve only the evidence that policy allows.

| Data ID / owner | Contents and classification | Lifecycle consumers and persistence controls |
|---|---|---|
| GPA-D01 Consumer registry / API | Principal/organisation/product-or-partner role, environment, contract/capabilities, support/readiness and secure credential reference; restricted operational data. | GPA-01/03/11/12; versioned state and qualification; protected credentials remain in secret custody. |
| GPA-D02 Authority/access association / Identity | Tenant, legal subject, principal/delegate, grant evidence, capability/direction/country/environment/history scope, interval/revocation and version; restricted legal/access evidence. | GPA-02/03/05/07–12; authoritative grants referenced, not duplicated; effective state rechecked. |
| GPA-D03 Connection/readiness and execution binding / Connection/Exchange | Provider/account, protected trust refs, direction/profile, mode, executor/reconciler, capability checks/evidence validity; restricted configuration. | GPA-02/05/08–12; versioned by capability; route separate; original bindings retained on invoices/legs. |
| GPA-D04 Acceptance/idempotency/batch journal / Intake | Scope/key/digest/intent, source invoice/revision, operation/item/receipt, acceptance/outbox repair status; restricted operational evidence. | GPA-04/05/08/12; recoverable atomic acceptance; retention covers approved retry/reconciliation window. |
| GPA-D05 Invoice/representations/provenance / Records + owning domain | Stable invoice/revision/source, original/exact sent/derived refs and hashes, profile/mapping/trust versions, context and evidence; sensitive business data. | GPA-04–09/11/12; immutable bytes/revisions; download/quarantine/access policy; retention owned by Records. |
| GPA-D06 Delivery work and leg outcomes / Exchange | Original plan/route/connection, independent leg IDs, owner, claim/generation/send intent, external refs and known/unknown outcomes; restricted. | GPA-05/06/08/09/11/12; conditional ownership; expired claim never proves non-execution. |
| GPA-D07 Lifecycle evidence/history / Lifecycle | Stable source event, raw code/status, mapping version, source/observed time, correlation and derived dimensions; sensitive evidence. | GPA-06–09/11/12; append-only correction links, source provenance and safe projections. |
| GPA-D08 Retrieval/distribution/checkpoints / Records/Distribution | Scope/filter-bound cursor, change/snapshot position, representation entitlement, receipt purpose/version and gaps; restricted consumer data. | GPA-07/08/11/12; re-authorise each page/action; independent consumer checkpoints and durable exception outcomes. |
| GPA-D09 Event/outbox/subscription / Events | Stable event/change position, safe payload, subscription scope, delivery attempts, acknowledgement and replay limits; restricted. | GPA-04/06/08/11/12; durable source/outbox recovery; current access check before disclosure; no indefinite replay promise. |
| GPA-D10 Route transition / Routing | Source/target, entity/direction/environment/time, expected/current version, external steps, conflict and activation evidence; restricted control record. | GPA-02/05/09/11/12; owning transition service; historical plans are unchanged. |
| GPA-D11 Interconnection case / Spain owner | Parties, scope/request/effective time, rule/calendar, evidence, owner, state/deadline/escalation; restricted case evidence. | GPA-02/09/10/11/12; approved rule required for clock; versioned updates, no implicit readiness. |
| GPA-D12 Audit/recovery and compatibility qualification / respective control owners | Safe actor/action/state versions/correlation, evidence/owner/next action, build/contract/consumer inventory, conformance and gate decisions; restricted operational records. | GPA-01–12; immutable audit and controlled release records; no secrets/customer raw exports in repository evidence. |

## Part 4 Assurance and Traceability View

### 1 Acceptance and source traceability

These are **future acceptance scenarios**, not claims that implementation tests have run. IDs in abbreviated columns share the `GPA-` prefix. A design review needs both a product consumer and a partner reference consumer; success for one role does not qualify the other.

| Acceptance ID / scenario | Source and requirements | Activity; interactions; data | Required observable evidence |
|---|---|---|---|
| GPA-A01 Shared product/partner contract | User brief; R01/14 | 01/03/12; INT-01/02/16; D01/12 | Both reference consumers use one supported resource/receipt/error model; permitted differences are explicit; separate API exception justified if required. |
| GPA-A02 Cross-customer/object denial | PA-FR1/3/5/15; R02/11 | 02/03/07/08; INT-02/10/12; D01/02/08/09/12 | Valid provider credentials cannot submit, enumerate, download, replay or acknowledge for an ungranted entity; no existence/data leakage. |
| GPA-A03 Independent capability readiness | PA-FR2; 213 FR1–4; R03 | 01/02/09; INT-01/03/14; D01/03/10 | Outbound ready/inbound unready is visible; no route activation on consumer/connection readiness; optional callback does not block approved pull mode. |
| GPA-A04 Repeat, conflict and restart | PA-FR4/7/8; R04/06 | 04/05/08; INT-04/05/13; D04/06/12 | Same key/digest returns original receipt; changed request conflicts; restart/acceptance timeout recovers durable work; alternate keys/paths do not duplicate effects. |
| GPA-A05 Partial batch | PA-FR6/7; R02/04/05 | 03/04/05; INT-02/04/05; D02/04/05 | Valid envelope with permitted, denied and invalid items yields independent outcomes; replay preserves accepted items; corrected item cannot replace accepted input. |
| GPA-A06 Intent and direction separation | PA-FR3/10; R02/05/08 | 03–05; INT-02/04/05; D02/04/05 | Inbound provider delivery cannot issue an outbound send or loop; issuer/delegate send authority differs from executor/source evidence permission. |
| GPA-A07 One executor under race/crash | PA-FR8; R04/06 | 05/08/12; INT-07/08/13; D03/06/12 | Competing claims/API/adapter paths cannot transmit one leg twice; expiry after possible send stays held until authoritative reconciliation. |
| GPA-A08 Independent delivery/copy outcomes | PA-FR7/10/11; R05/07 | 05/06/08; INT-05/08/09/13; D05/06/07 | Recipient success and separate copy/reporting failure remain distinct; recovery of failed leg does not resend the successful one; API receipt is not buyer acceptance. |
| GPA-A09 Source evidence integrity | PA-FR11–13; R05/07/09 | 06/08; INT-09/12/13; D06/07/09 | Duplicate/out-of-order evidence does not regress view; same event ID changed payload conflicts; unknown refs held; transport event cannot manufacture buyer/payment state. |
| GPA-A10 Retrieval, paging and historical grants | PA-FR9/10/12; 213 FR7/22/23; R07/08/11 | 07/09/11; INT-10/11/14; D02/05/07/08/10 | Stable paging/change position finds late updates; purpose-specific acknowledgements; empty/denied/unavailable differ; old invoice remains available only to currently authorised history scope. |
| GPA-A11 Notification loss and replay | PA-FR13/14; R09 | 06–08; INT-09/10/12/13; D07/08/09 | Duplicate/lost callback, restart and expired cursor have bounded recovery with durable event/original history; event receipt is separate from business processing. |
| GPA-A12 Cutover, conflict, cancel and rollback | 213 FR3/5–8/11/13–24; R03/10 | 05/09/12; INT-05/14/16; D03/05/06/10/12 | Cutover freezes one deterministic route; overlapping transition rejected; safe pre-boundary cancellation; uncertain activation reconciles; rollback affects new work only. |
| GPA-A13 Explorer scope guard | 213 DR2/J9; R10/12 | 03/05/09; INT-02/05/14; D02/03/10 | Unapproved per-invoice provider override is rejected/disabled despite prototype selector; approved future binding proves precedence, scope and audit. |
| GPA-A14 Revocation and outstanding work | PA-FR20; 213 FR9/25/30; R02/06/13 | 03/05/07/08/11; INT-02/07/10/12/16; D02/03/06/08/09/12 | Revocation races with read/page/download/dispatch disclose or execute no newly forbidden work; already transmitted/unknown work gets an authorised continuity owner. |
| GPA-A15 Interconnection rule missing/approved | PA-FR17; R12 | 02/09/10; INT-03/14/15; D03/10/11 | Missing approved Spain clock is action-required; qualified rule records trigger/calendar/evidence and escalation; case closure alone cannot activate a route. |
| GPA-A16 Compatibility, limits and support | PA-FR15/18/19; PA-NFR2/4/5; R11/14 | 01/04/08/12; INT-01/04/12/16/17; D01/04/09/12 | Old supported product works after partner extension; bounded workloads and noisy-consumer isolation proved; scoped audit/health reads omit secrets and other-consumer data; version rollback and incident runbook exercised. |
| GPA-A17 Country-rule isolation | Shared-platform direction; R11/12 | 02–06/09/10; INT-02–06/09/14/15; D02/03/05/07/10/11 | Synthetic second-country binding cannot inherit Spain identity, public-route/copy/reporting or deadline rules; missing country policy holds work; Spain change leaves other binding unaffected. |
| GPA-A18 Implementation reuse qualification | PRD-SEI-223/227; R07/12/14 | 01/02/05/12; INT-01/03/05/06/16; D01/03/05/12 | Actual API/domain/DTS build/contracts and gaps recorded; selected mapping/profile/operations pass; absent inbound/four-syntax/signing coverage is explicit and cannot activate by assumption. |
| GPA-A19 Scoped route/discovery access | PA-FR16; 213 FR26/27; R02/03/10/12 | 03/09; INT-02/03/14; D02/03/10/12 | Authorised route/connection reads expose no secrets; lookup retains rule/source/time/freshness and unresolved outcomes; an advisory result cannot authorise final dispatch or expand provider access. |

Security evidence also covers principal/role tampering, provider self-grant, forged work claim, callback endpoint abuse, unsafe file/reference input, evidence replay, unrestricted audit access and sandbox/production crossover under GPA-A02/06/07/09/14/16. Findings need owners and closure evidence before production.

### 2 Open decisions and accountable gates

Owners below are accountable roles awaiting named individuals. Do not close a question merely by choosing a value in an API draft.

| Decision ID | Question and proposed direction | Owner / gate | Consequence if unresolved |
|---|---|---|---|
| GPA-Q01 | Who owns the common API and which product/partner capability forms the reference cohort? Prefer one contract owner with domain/provider owners. | Domain Service Product Owner + Global API owner / design | Cannot approve scope, maintenance comparison or conformance responsibility. |
| GPA-Q02 | What existing Global API build/resources/schemas exist; which extensions, exposure topology, HTTP/error mapping and API definition are needed? Prefer equivalent existing operations and one contract. | API Architecture/Engineering + consumer owners / design | Cannot promise implementation reuse or issue a build-ready endpoint specification. A required separate API must document its constraint. |
| GPA-Q03 | What authentication/trust protocol, organisation verification, customer grant evidence, revocation enforcement and external data policy apply? | Security/Identity + Privacy/Compliance / sandbox exit | Partner access, callbacks/downloads and credential rotation cannot activate. |
| GPA-Q04 | Which capabilities use partner pull/push or Sage adapters; who executes/reconciles each leg; which provider is actually ready? Proposed pull work is a candidate, not a commitment. | Architecture + provider/domain owners / design/pilot | Cannot enable provider execution or hybrid delivery; retain only qualified paths. |
| GPA-Q05 | What acceptance/outbox, idempotency retention, claim/lease, concurrency and unknown-outcome contracts are proven? | API/Exchange Engineering + provider owners / sandbox exit | Durable acceptance, duplicate prevention and safe retry are unqualified. |
| GPA-Q06 | What paging/change/replay model, history scope, acknowledgement meanings, event versions and cursor expiry limits are supported? | Records/Lifecycle/Events + consumer owners / pilot | Retrieval and missed-event recovery cannot claim complete coverage. |
| GPA-Q07 | Which Spain scopes/profiles, authority/signing roles, transformation pairs, route/copy/reporting rules and interconnection clock have primary evidence and approval? | Spain Product/Compliance + provider/Trust/DTS owners / Spain production | Keep country-dependent capabilities disabled or held; no legal time/format assumptions. |
| GPA-Q08 | Does PRD-SEI-213 DR2 permit per-invoice provider selection; what are precedence, granularity, authority and transition mechanics? Keep initial scope within the PRD. | Spain Product + Routing/Architecture / affected scope approval | Explorer selector cannot become an implementation requirement; unresolved inbound switching stays gated. |
| GPA-Q09 | What payload/batch/page/concurrency/rate limits, service levels, measured targets, backpressure and support responsibilities are affordable? | API/domain Operations + Product / production | No numeric commitments or unbounded workloads; isolate pilots within approved limits. |
| GPA-Q10 | What retention/deletion, audit, idempotency/event windows, grant history scope and revocation/exit continuity policy apply? | Records + Security/Privacy/Compliance + Operations / production | Cannot promise indefinite history/replay; suspended/revoked work needs explicit handling. |
| GPA-Q11 | Which actual DTS/API/domain/adapter implementations can be reused; what local changes/gaps and on-call contracts remain? | Architecture + service/DTS/provider owners / pilot | A proposed pattern cannot certify production readiness; unsupported profile/mapping remains disabled. |
| GPA-Q12 | What contract compatibility/deprecation policy, product/partner inventory, migration and rollback evidence supports one API? | Global API Product/Engineering + consumer owners / production/expansion | Partner launch cannot break supported products or retire interfaces without an approved migration. |

### 3 Readiness and review result

**Design review:** agree the shared-contract decision, reference consumers, existing API inventory and logical operation ownership (GPA-Q01/Q02/Q04). Resolve or explicitly exclude per-invoice selection and unsupported transition scope. Publish a versioned contract definition for review only after actual API/schema evidence is available.

**Sandbox exit:** prove identity/authority isolation, intent separation, durable single/batch acceptance, duplicate/concurrency safety, original-executor reconciliation and independent capability readiness (GPA-A02–09; GPA-Q03/Q05).

**Pilot:** use a qualified product and partner cohort with retrieval, events, missed-event recovery, country bindings, selected transformation/profile evidence and compatibility (GPA-A01/10–13/17/18; GPA-Q04/Q06/Q08/Q11).

**Production/expansion:** require approved Spain policies/interconnection evidence; measured limits/service objectives; on-call/runbooks and incident/exit recovery; retention/access policy; and consumer compatibility/migration evidence (GPA-A14–18; GPA-Q07/Q09/Q10/Q12). Additional providers and countries need their own qualification rather than inheriting the pilot's readiness.

Current result: **reviewable logical proposal for provider capabilities through one E-Invoicing Global API**. PRD-SEI-213 supplies the routing/control foundation; PRD-SEI-235 supplies provider-facing exchange requirements. The explorer informs the journey while its open scope choices remain identified. Existing source documents are preserved; no implementation, lifecycle approval or Confluence publication is implied.
