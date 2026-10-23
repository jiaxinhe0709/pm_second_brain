---
id: SPEC-SEI-011
title: Public Platform Connector Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-20
reviewers: []
related:
  - RES-SEI-002
  - GLO-SEI-001
  - PRD-SEI-101
  - PRD-SEI-105
  - PRD-SEI-211
  - PRD-SEI-212
  - PRD-SEI-214
  - PRD-SEI-224
  - PRD-SEI-226
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-007
  - SPEC-SEI-008
  - SPEC-SEI-009
  - SPEC-SEI-016
  - SPEC-SEI-012
  - SPEC-SEI-014
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "902988120"
  page_id: "923861399"
  layout: two_left_sidebar
  toc: true
---

# Public Platform Connector Solution Specification

Terminology follows the [shared e-invoicing glossary](../context/GLO-SEI-001-e-invoicing-terminology.md). Local terms explain this feature; exact technical IDs, fields and source codes keep their stated meanings.

An **exchange action** is one separately tracked action to deliver an invoice, submit a public copy, or report an invoice event. Each action has its own result. For example, invoice delivery can succeed while public-copy submission still needs attention.

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. [Part 2](#part-2-logical-feature-specification) gives the detailed behaviour and rules. [Part 3](#part-3-logical-service-interactions-and-data-inventory) describes service interactions and data. [Part 4](#part-4-assurance-and-traceability-view) links requirements to the checks and evidence needed before release.

The design remains a draft. **Confirmed** means supported by the cited source, within its stated limits. **Proposed** choices still need review. **Open** decisions still need an owner’s recorded answer. **Out of scope** identifies work excluded from this proposal or handled by another feature. Service names describe logical responsibilities; they do not establish deployed services or approved API endpoints. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### 1 Purpose, authority and boundaries

This **proposed logical design** gives Sage services a controlled way to call Spain’s public platform (SPFE), operated by AEAT. The connector handles the platform’s communication protocol. It is separate from invoice retrieval and recipient lookup.

For each call, it checks the customer, represented legal entity, permitted action and environment. It selects an approved contract and credentials for that purpose, then performs only an enabled operation. It saves the request and response evidence and returns a result that clearly says whether the outcome is known, pending or unknown. The service that requested the call decides what that result means for its feature.

The supplied PRD describes the wider integration. The capability mapping below shows how this connector supports it and where related services retain responsibility.

[PRD-SEI-214](../prds/PRD-SEI-214-connections-registration-routing-structured-review.md), FR2–6/19–23/27, separates connections, registration, capability readiness and routes. [PRD-SEI-105](../prds/PRD-SEI-105-public-platform-environment-isolation.md), FR1–18, owns environment isolation. [PRD-SEI-211](../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md) and [PRD-SEI-212](../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md) supply retrieval and submission safety requirements. These are canonical product requirements, not evidence of a deployed public adapter.

| Evidence | Supported fact | Limit |
|---|---|---|
| [User-supplied Public Platform API Integration PRD](https://confluence.sage.com/spaces/DNBU/pages/902988120/Spain+Public+Platform+API+Integration+AEAT+Public+Electronic+Invoicing+Solution) | Defines the requested integration capabilities: connectivity, faithful-copy submission, invoice identification, status/payment communication, retrieval, authentication, monitoring and audit. | Refers to a draft ministerial order. Its exact timing, attachment restrictions, event labels, certificate requirements and SLA need current evidence and the relevant owners' approval. It is product context, rather than proof of an available AEAT API or approved technical design. |
| [Order HAC/1028/2026, Articles 9–11](https://www.boe.es/eli/es/o/2026/10/02/hac1028), checked 6 October 2026 | Public recovery/consultation access and authentication/representation requirements exist. Third-party recovery and Article 10 consultation require registered representation. | Exact operations, credential profiles, limits and technical access are governed by AEAT specifications. Do not extend one action's authority automatically to another. |
| [Existing evidence note](../research/spain-public-platform-order-evidence.md) | Records the supplied order snapshot and limits of the retrieval evidence. | Does not supply a production transport contract or prove a central recipient directory. |
| SPEC-SEI-001/002 | Trust, onboarding and uncertain onboarding-operation designs. | Draft logical contracts; qualification and external evidence remain necessary. |

### Public source baseline

Eight supplied WSDLs now establish PRE operation names, SOAP 1.2 bindings, certificate/seal ports and ebMS/MIME packaging. The catalogue adds a ninth PRE-only validation service. Earlier claims that no public operation evidence exists are replaced by this supplied baseline. Protocol conflicts, business schemas, replay safety and actual access remain open.

See [REF Source references](#ref-source-references) for the original files, exact locations and source limits. The [technical evidence guide](../context/RES-SEI-002-spain-public-platform-technical-evidence.md) tracks shared source conflicts. The constraints below align this feature with the supplied public evidence; Sage implementation and activation remain gated.

### Shared foundation and public protocol boundary

The [shared connectivity and routing spec](SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns the shared connection/profile qualification and route context across customer-provider integration and Sage platform interconnection. This connector remains the public-platform protocol and operation-evidence owner. It consumes a qualified connection/profile and owning feature action; it cannot activate a route, create invoice/reporting obligations or replace the shared route engine. Reuse public execution controls where proven, while checking exact role, represented-party authority, credential purpose and operation contract independently. Shared foundation reuse does not imply that public and private platforms expose the same interface.

### How the connector supports the supplied PRD

The PRD describes the full public-platform integration in the **Sage Global e-Invoicing Platform**. This spec describes the connector within that integration. The platform contains the shared invoicing capabilities; the Global API is the contract through which products and partners access them. The connector supports the business capabilities below without taking over invoice issuance, transformation or lifecycle decisions from their responsible services.

| PRD capability | Connector responsibility | Related feature and evidence needed |
|---|---|---|
| Submit faithful invoice copies | Transmit the exact prepared file through a supported public operation. Save acknowledgement, rejection and error evidence separately from recipient delivery. | SPEC-SEI-007 owns the copy obligation and issuance trigger. SPEC-SEI-005/008 own qualified validation/transformation; SPEC-SEI-001 owns protected signing where required. Exact timing, UBL profile, metadata and attachment restrictions remain contract/country-rule checks. |
| Generate and store the Spain invoice identifier | Carry the approved identifier and preserve the supplied invoice identity in requests and responses. Do not invent its encoding. | The PRD lists supplier NIF, number, series and date. Format/Spain owners must confirm the final encoding and contract; invoice and records services own generation and storage. |
| Communicate invoice and payment status | Send an authorised report and save its independent response. Preserve raw external codes rather than assigning business meaning in the connector. | SPEC-SEI-009 owns actor authority, lifecycle interpretation and reporting rules. The PRD's Rejected, Fully Paid, Collected, Not Paid/Non-Payment and cancellation labels need an approved external mapping. Accepted applies only if the AEAT contract exposes it. |
| Retrieve invoices, messages and statuses | Execute supported discovery/read calls, including authorised status/payment queries, and return raw source responses within the correct entity scope. Distinguish an empty result from an outage. | SPEC-SEI-016 owns automated retrieval, source-file capture, covered progress and delivery to products; SPEC-SEI-009 owns status interpretation. Article 10 establishes status/payment consultation; GetRegisteredInvoice, GetInvoices and the two downloads now have supplied operation evidence. Exact filter/continuation/business shapes remain incomplete; no automatic public notification interface is supplied. Keep source correlation and observation time, distinguish status consultation from file download, and prevent duplicate business processing. |
| Authenticate and use credentials | Apply the selected AEAT authentication contract using protected credential references for the approved action and environment. | SPEC-SEI-001 owns credential custody and qualification. Customer certificate procurement remains out of scope. One accepted certificate does not establish authority for every operation. |
| Handle cancellation requests | Execute cancellation only where the confirmed contract supports the specific action and the responsible feature authorises it. Save request and result evidence. | PCN-Q01/Q03 must distinguish invoice cancellation, communication cancellation and cancellation of unsent local work. None automatically deletes an issued invoice or undoes an external effect. |
| Monitor, audit and recover failures | Record timestamps, acknowledgements, rejections, errors and retrieval activity. Detect uncertain outcomes and assign recovery to an owner. | Operations and feature owners agree service targets, retry safety, retention and support. Schema, authentication, duplicate/already-existing invoice, status and availability errors retain their actual source meaning. |

| Responsibility | Owner and handoff |
|---|---|
| Customer identity, authority and readiness | [Onboarding](archive/SPEC-SEI-002-onboarding-solution-specification.md) and identity/authority services; connector checks effective evidence before each operation. |
| Certificate custody and purpose-specific use | [Certificate management](SPEC-SEI-001-certificate-management-solution-specification.md); connector receives protected references and results, not private keys. |
| Public discovery, polling, source archive and checkpoint | [Receiving, retrieval and download](archive/SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md); connector returns correlated source responses and files. |
| Issued invoice, validation, exchange plan and independent actions | [Outbound](archive/SPEC-SEI-007-invoice-sending-solution.md) and PRD-SEI-212; connector executes one approved public operation. |
| Status consultation and commercial/payment interpretation | [Lifecycle](archive/SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md); lifecycle requests source refresh and interprets the result; connector executes qualified public queries and preserves source observations without deriving buyer acceptance. |
| Recipient receiving destination | [Recipient lookup](SPEC-SEI-012-consult-public-platform-for-recipient-information.md); uses this connector only if an approved public lookup contract exists. |

The connector does not issue invoices, change customer routes, interpret absence of a private destination, create public-copy duties, own statutory archive retention, or provide a generic proxy to arbitrary URLs. Onboarding/registration mutations, if required by the final contract, remain owned by their feature service and must use this same operation-safety boundary.

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
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
| Readiness | The current result of capability checks for a stated legal entity, actor, environment and route/profile, with evidence, limitations and a recheck condition. Readiness is separate from authority, route activation and invoice outcomes. |
| Public platform / SPFE / AEAT | SPFE is the Spain public e-invoicing platform. AEAT is the authority operating it. Each platform operation needs its own approved contract. |
| Connection / contract profile | Configuration for communication; the selected operation, protocol and schema, environment and safety rules. A connection does not activate a route. |
| Durable intent / execution claim | A saved request identity and fixed input before a possible external effect; permission for one worker to execute that work. An expired claim does not prove the earlier worker did nothing. |
| External effect / outcome unknown | A change in the public platform; a result for which that change may have happened but reliable evidence is missing. Check the original operation before repeating it. |
| Lease generation / version check | A number identifying the current worker’s claim; a check that a record still has the version expected by the caller. These prevent old workers or stale updates from replacing newer work. |
| Outbox / circuit breaker | A saved event waiting to be delivered; a control that temporarily stops calls after defined failures. Neither changes the invoice route. |
| Scope / evidence / cohort | The customer, legal entity, environment and action covered by a call; saved facts and references showing what happened; the group of consumers selected for activation. |

### 2 Outcomes and handoffs

| Outcome | Meaning | Does not prove |
|---|---|---|
| Capability qualified | Exact operation, environment, contract and evidence are enabled for a defined cohort. | Every public function is supported or a customer route is active. |
| Known result | Correlated response/evidence durably recorded at its actual meaning. | Buyer acceptance, ERP consumption or completion of unrelated invoice exchange actions. |
| Pending | Work is saved and waiting for capacity, a response, local evidence recovery or owner action. | External success or invoice absence. |
| Outcome unknown | External effect may have happened; original operation must be reconciled. | Permission to create a fresh operation or switch environment. |
| Denied/unsupported | Scope, authority, capability or contract is insufficient; no new external effect is initiated. | Permanent business ineligibility. |

### Spain use and reuse boundaries

This is a **Spain reference design**. **Reusable unchanged** means the proposed design pattern can stay the same. **Reusable with country binding** means shared behaviour needs approved country rules or adapters. **Country-specific** rules stay in the Spain country pack. **Unknown** means that the existing implementation’s suitability or coverage still needs evidence. These labels do not prove production readiness. Another country needs its own assessment. See the [shared e-invoicing glossary](../context/GLO-SEI-001-e-invoicing-terminology.md#reuse-vocabulary).

| Area | Intended Spain use | Reuse classification | Condition and owner |
|---|---|---|---|
| Operation ledger, correlation and recovery | Preserve intent, evidence and safe retries for public operations. | Reusable unchanged; proposed design pattern | Connector/Architecture: qualify actual implementation and crash recovery. |
| Environment, credentials, capacity and diagnostics | Isolate operations and protect material. | Reusable with country binding | Security/Operations: bind endpoint, trust, quotas, error catalogue and retention policy. |
| AEAT protocol and representation | Call the selected SPFE service for the authorised business/action. | Country-specific; adapter and rules | Spain technical/Compliance owners: final contract, registered authority and conformance evidence. |
| Existing public adapter | Reuse any proven Sage connector functions. | Unknown; existing implementation coverage | Record build, contracts, gaps and build/run owner before activation. |
| DTS | No invoice transformation within connector. | Out of scope; preferred candidate upstream where transformation is required | Outbound/Receiving and DTS owners qualify exact mapping under [SPEC-SEI-008](SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) or the owning feature. DTS is not the public transport or archive. |

### 3 Process and ordered lifecycle

![Public platform connector process](../assets/diagrams/public-platform-connector-process.svg)

[Editable Draw.io](../assets/diagrams/public-platform-connector-process.drawio) · [PNG preview](../assets/diagrams/public-platform-connector-process.png).

Step names describe the action in plain language. The smaller PCN references link each step to the detailed behaviour and acceptance checks below.

Text equivalent: Receive the service request (PCN-01) → Check customer and environment (PCN-02) → Check permission and credentials (PCN-03) → Check platform support (PCN-04) → Save the request before sending (PCN-05) → Call the public platform (PCN-06) → Save the response and evidence (PCN-07) → Return the result to the service (PCN-08). If permission is denied or the action is unsupported, hold the request without sending a call. If the external outcome is unknown or evidence is missing, check what happened before retrying (PCN-09), using the original request identity and context. Update settings for future requests (PCN-10) while preserving pending work and history.

| Activity / trigger and actor | Required result | Failure owner and safe handoff |
|---|---|---|
| PCN-01 Receive the service request / owning feature service | Save a stable feature operation, input reference/digest and correlation. | Connector/feature: the same key with changed input returns a conflict. |
| PCN-02 Check customer and environment / connector | Resolve tenant, represented entity, country and environment from trusted records. | Identity/Security: deny ambiguous context before any access. |
| PCN-03 Check permission and credentials / connector and specialist services | Check current authority for the action and credentials for its purpose and environment. | Authority/Trust: missing or revoked permission holds new calls. |
| PCN-04 Check platform support / connector | Select the enabled operation, exact contract/version, retry-safety class and readiness evidence. | Integration owner: keep unsupported combinations disabled. |
| PCN-05 Save the request before sending / connector | Save the request and claim execution once, with fixed input and target context. | Connector/Records: a failed save prevents a new external change. |
| PCN-06 Call the public platform / adapter | Call within approved limits using the correct credential, contract and quota. | Adapter/Operations: record whether transmission may have happened. Check uncertain outcomes before repeat. |
| PCN-07 Save the response and evidence / connector | Save protected raw evidence, a safe normalised result and links to each item. | Records/connector: recover the original response without making a fresh external change. |
| PCN-08 Return the result to the service / connector | Return a result within scope and send a recoverable notification to the requesting feature. | Feature/connector: recognise repeated notifications and do not apply them twice. |
| PCN-09 Check what happened before retrying / operations or approved policy | Establish the original outcome, or keep an unresolved case with a responsible owner. | Operations/adapter: use manual recovery when safe query or retry is unproven. |
| PCN-10 Update settings for future requests / authorised integration owner | Record profile/group changes for future work, their impact and audit evidence. | Integration/Security: keep current work/history and other environments separate. |

### 4 Material decisions

Open decisions PCN-Q01–Q08 in Part 4 gate exact APIs, custody/authority, operation safety, evidence durability, service targets, deployment and rollout. A successful connection check is not blanket readiness. No live platform configuration is changed by this document.

## Part 2 Logical Feature Specification

### 1 Model and invariants

Logical operation identity includes tenant, legal entity, country, environment, capability, owning feature operation and idempotency identity. Every attempt freezes contract profile, endpoint reference, credential binding, authority decision, payload digest and expected record version. Idempotency retention and scope must be agreed with each consumer/provider.

| ID | Rule that must always hold |
|---|---|
| PCN-I01 | Trusted environment and credential binding must agree; production cannot fail over to simulation or TEST. |
| PCN-I02 | Authentication, business authority, capability readiness, registration and route activation are separate facts. |
| PCN-I03 | Only a qualified operation/profile may execute; one successful call does not qualify all capabilities. |
| PCN-I04 | Same scoped key and digest returns/resumes the original operation; changed input conflicts. |
| PCN-I05 | Save immutable intent before any possible external effect; uncertainty uses original identity and context. |
| PCN-I06 | Successful transport or a successful request does not supply missing business results for individual items. |
| PCN-I07 | Evidence and notification follow a recoverable commit; local save failure cannot justify fresh submission. |
| PCN-I08 | Contract/credential changes keep historical context and apply only to eligible future work. |
| PCN-I09 | Retry is controlled at one external execution owner; feature and connector retries cannot multiply public effects. |
| PCN-I10 | Credentials, raw invoices and bearer access values never appear in client events or diagnostic logs. |

### 2 Behaviour by activity

**PCN-01 Accept the feature request.** The calling Sage service asks the connector to perform a named platform action. Authenticate that service and check its permitted capability. Accept the feature operation reference, legal entity and action, fixed payload or query reference, digest and idempotency key. The caller cannot choose an arbitrary URL or protocol command.

Save a stable connector operation. A repeat with the same identity and input returns its current saved state. Changed input or context returns a conflict. A feature may cancel work before execution. Once an external change may have happened, cancellation cannot erase the history or claim that the change was undone.

**PCN-02 Resolve the customer and environment.** Check that the caller’s scope matches the connection’s legal entity, country and trusted deployment/account environment. Select the environment profile and approved destination from protected configuration. Reject missing, cross-tenant or conflicting context before accessing credentials.

Simulation uses clearly labelled synthetic test data. Official TEST access requires its confirmed contract. Neither simulation nor a TEST response proves production readiness or acceptance by the live public platform.

**PCN-03 Check authority and credentials.** Check local permission and external authority to act for the represented legal entity. Article 9/10 access uses its own registered-authority checks. Other actions use the authority rules approved for that action; one permission does not automatically cover another.

Obtain protected credential references through SPEC-SEI-001. Check purpose, environment, expiry/status and represented party under the current policy. If authority or credential versions change while the request waits, check again before execution. Hold new calls when required authority evidence is unavailable. A certificate alone cannot supply that authority, and the connector does not require private-key export.

**PCN-04 Select the supported operation.** Select an enabled registry entry for the requested action, country, environment and consumer group. It must identify the protocol and schema version, approved destination, request/response limits and response meaning. It must also identify possible external changes, provider idempotency/query support, timeout/retry rules and the evidence owner. Missing information blocks activation; do not borrow assumptions from another AEAT service. SII, VERI*FACTU and FACe contracts do not prove SPFE support.

Use approved readiness checks that do not change external state, or conformance evidence for the selected contract. Never send a real or empty invoice to test a connection. DNS/TLS/network checks show only that communication is possible. Show configuration, authentication/authority, operation support and current service health separately. Registration remains UNKNOWN/NOT_APPLICABLE unless the confirmed operating model provides a registration fact. A successful ping does not establish enrolment, and this design does not invent an enrolment endpoint.

**PCN-05 Save the request and assign one worker.** Save the operation, fixed input reference, exact scope/profile, feature correlation and retry-safety class. One execution owner claims the work through a numbered lease or equivalent concurrency control. A stale worker cannot save a result or initiate another attempt. Before sending, save the attempt identity and the point at which transmission may begin. Save queue work and operation records through a recoverable outbox or equivalent protocol. Missing payload, object or hash prevents execution.

An expired lease does not prove that the previous worker stopped transmitting. If a worker loses its lease or another worker takes over after a possible external effect, hold the original operation for reconciliation or a provider-proven idempotent resume. Do not start another change just because the local lease expired. Test claim checks immediately before transmission, rejection of stale saves and external retry safety together.

Combine only identical operations under the approved consumer contract. Limit queued work and share capacity fairly across tenants and capabilities. Submission backlog must not prevent retrieval or reconciliation. Exact quotas and priorities remain PCN-Q05 decisions.

**PCN-06 Call the public platform.** Build the request from the qualified contract and the checked feature request. Enforce resource limits, verify the remote transport identity, handle XML safely and use only approved destinations. Redirects or returned URLs cannot bypass destination or credential rules. The connector must not change signed invoice bytes or repair invoice facts.

Record whether failure happened before transmission, after possible transmission or after a response matched to the request. A call proven to have no external effect may repeat under its approved read/retry contract; “consult” in its name is not proof. A lost response after a possible change becomes OUTCOME_UNKNOWN. Throttling or an outage must not appear as an empty result or successful freshness check. A circuit breaker pauses affected calls; it does not switch route, environment or invoice exchange action. Exact waits and limits remain open.

**PCN-07 Save response evidence.** Save the protected response bytes or reference, digest, received time, external request/item references, contract/error catalogue version and what the response proves. Match each item result to the request. Keep partial or missing results visible; request-level success does not mean every item was admitted. Preserve unknown external error codes in restricted evidence and notify the catalogue owner. The caller receives a safe category and responsible owner.

Before temporary streamed files expire, obtain confirmation that the responsible service saved and verified them. SPEC-SEI-016 owns permanent invoice capture; connector staging is temporary. If the external result is known but saving its evidence fails, hold the operation for evidence recovery. Recover the original response or query the original operation instead of repeating a change. The implementation must prove that this recovery survives worker loss.

**PCN-08 Return the result and notify the feature.** The service that requested the call can read the saved result within its authorised scope. Notifications include connector/feature IDs, event ID, version, known/pending/unknown state and safe evidence references. A notification may arrive more than once or out of order, so consumers check identity and version before applying it.

The feature service decides what admission, freshness, retrieval progress, lifecycle status and customer wording mean. The connector cannot advance a retrieval checkpoint or mark the buyer as having accepted an invoice.

**PCN-09 Establish the original outcome before retry.** One recovery owner selects SAFE_RETRY, IDEMPOTENT_RESUME, RECONCILE_FIRST or MANUAL_ONLY from evidence about the operation. Do not choose from the error name alone. Query the original operation/reference with its payload digest, contract and environment. A failed query leaves the outcome unknown. Repeat only when the approved contract and evidence of non-execution permit it.

Changing a route or credential does not resolve an earlier outcome. A replacement credential needs an approved link to the original represented party, action and environment, with evidence for the new attempt. If neither reliable query nor proven idempotency is available, open a manual case with an owner and hold unsafe repeats. Reusing the same local key cannot bypass that hold.

Inspection, recovery and profile activation require separate audited permissions. Cancellation after transmission is a separate external operation, if supported by a qualified contract, and remains the feature service’s responsibility.

**PCN-10 Change configuration safely.** Check that the current profile/endpoint version matches the expected version before applying a change. Record the actor, reason, impact and approval evidence. Deploy the capability disabled, obtain correctly labelled TEST/simulation evidence, then enable only the approved production group.

Credential rotation keeps earlier attempts unchanged. Disablement stops new affected calls and assesses queued work, work already running and unresolved operations. Keep their evidence and leave other capabilities/environments separate. Rollback restores a qualified profile for eligible future work; it must not repeat completed or outcome-unknown operations.

### 3 Requirements and operational controls

| ID | Observable requirement / source |
|---|---|
| PCN-R01 | Enforce trusted tenant/entity/country/environment and qualified credential binding before calls; PRD105 FR1–9/14/17, PRD214 FR6. |
| PCN-R02 | Check action authority separately from authentication and readiness; PRD101 FR22/24, PRD211 FR54, PRD226. |
| PCN-R03 | Activate exact operation contracts independently; no probe may issue an invoice or change routes; PRD214 FR3–5/19–21. |
| PCN-R04 | Persist idempotent intent, immutable payload and controlled attempt ownership; PRD212 FR22–28, PRD214 FR22. |
| PCN-R05 | Classify external-effect uncertainty and reconcile original operation before unsafe repeat; PRD212 FR25–27/36–40. |
| PCN-R06 | Preserve correlated raw/item evidence and safe errors without overclaiming success; PRD212 FR29–35, PRD214 FR23/27. |
| PCN-R07 | Recover local evidence/handoff failure and deliver versioned deduplicated notifications; PRD212 FR34/37, PRD211 adapter/checkpoint requirements. |
| PCN-R08 | Bound fair capacity and expose health, backlog, unknown outcomes and safe actions; PRD211 scheduling, PRD212 FR38–39. |
| PCN-R09 | Preserve in-flight/history through credential/profile change, suspension and rollback; PRD105 FR15–16, PRD214 FR16–18/25–26. |
| PCN-R10 | Isolate Spain rules and qualify reused implementation before activation; PRD214 FR19–21 and repository reuse controls. |

Encryption, least privilege and purpose-bound source access protect PCN-D01–D09. Metrics distinguish attempts before/after transmission, provider and local latency, throttle, authority denial, evidence gaps, unknown-operation age and notification backlog. Avoid legal-subject identifiers as public metric labels. Security owns destination restrictions and XML/resource limits; Operations/Product approve service objectives from provider terms and measured volumes. No numeric SLA or retention period is invented.

### SPFE source contract binding

The supplied operation catalogue below is the external contract baseline. An operation remains disabled for live use until its listed gaps, authority and environment checks pass. The names identify SPFE operations, not new Sage API endpoints.

| SPFE operation / ebMS Action | Business request → response | Documented constraint and remaining qualification | REF |
|---|---|---|---|
| `SendInvoice` / `SUBMITINVOICE` | N `Invoice` attachments → one `DocumentStatus`. | 1–100 invoices; evaluate authority per issuer. Originals/copies retain their role. The 5120-byte invoice limit conflicts with examples. | SPFE-S03 pp. 10–11; SPFE-S16. |
| `CancelInvoice` / `CANCELINVOICE` | One `ApplicationResponse` → one `DocumentStatus`. | Previously submitted invoice and legally permitted withdrawal case; exact reference/cardinality binding remains open. Not a replay/duplicate-clear operation. | SPFE-S02 Article 5.5; SPFE-S03 pp. 11–12; SPFE-S10. |
| `GetInvoices` / `QUERYBYID` | N `ApplicationResponse` attachments → one `DocumentStatus`. | Up to 1000 invoice identifiers, with issuer/recipient role. Consults invoice metadata and final states; no invoice-file download. | SPFE-S03 pp. 12–13; SPFE-S14. |
| `GetRegisteredInvoice` / `QUERYBYFILTER` | ebMS `MessageProperties` filters → one `DocumentStatus`. | Presentation-date discovery; up to 1000 results and `SECUENCE_ID` pagination. Exact filter/continuation contract and header-only request need qualification against the generic WSDL payload. | SPFE-S03 pp. 13–14; SPFE-S15. |
| `DownloadInvoicesByID` / `DOWNLOADBYID` | One `ApplicationResponse` with N `DocumentReference` entries → N `Invoice` attachments. | Up to 100 invoices; issuer/recipient role; retain failed references independently. | SPFE-S03 pp. 14–15; SPFE-S12. |
| `DownloadInvoicesByLOC` / `DOWNLOADBYLOC` | One `ApplicationResponse` with locator references → N `Invoice` attachments. | Preferred platform-download path. Catalogue locator/certificate authority needs legal reconciliation; no distinct numeric limit is supplied. | SPFE-S03 pp. 15–16; SPFE-S13. |
| `CustomerInvoiceEvents` / `ACCOUNTINGCUSTOMERPARTYACTION` | One `ApplicationResponse` → one `DocumentStatus`. | Up to 100 recipient states; no supplier-state mixing; complete Annex II field/wire and item-result binding remain gated. | SPFE-S03 pp. 16–17; SPFE-S11. |
| `SupplierInvoiceEvents` / `ACCOUNTINGSUPPLIERPARTYACTION` | One `ApplicationResponse` → one `DocumentStatus`. | Issuer collection/non-payment communications and their cancellation; numeric batch limit is not supplied. | SPFE-S03 pp. 17–19; SPFE-S17. |
| Catalogue `InvoiceValidation`, path `ws/InvoiceValidationSOAP` / no ebMS Action | Direct `Invoice` XML → direct `DocumentStatus` XML. | PRE-only; one invoice; no registration/admission. No WSDL supplied; exact HTTP/SOAP packaging and ports remain unqualified. | SPFE-S03 pp. 19–20; SPFE-Q05. |

The source facts below govern the public binding. Recovery, storage and qualification actions are proposed Sage controls where stated. Apply them through PCN-02–09. Source conflicts stay open under PCN-Q01/Q02/Q03/Q07; SPFE-Q01–Q12/Q15/Q17; they are not resolved by a local default.

| ID | Constraint and required behaviour | Source reference |
|---|---|---|
| PCN-SPFE-R01 Register the exact supplied operations | The registry pins the eight WSDL names, action, environment, certificate class and business meaning independently. Include catalogue InvoiceValidation as PRE-only and disabled until its missing contract is qualified. No recipient directory, enrolment, public offboarding or webhook is inferred from this inventory. | SPFE-S03/SPFE-S16; REF-WSDL; [REF](#ref-source-references). |
| PCN-SPFE-R02 Build and correlate the public message | For the eight WSDLs, use the supplied SOAP 1.2 binding, ebMS Messaging header, empty SOAP body and MIME multipart/related business attachments referenced by cid. Preserve caller PartyId, MessageId/RefToMessageId, ConversationId and item references independently. Resolve SOAP/fault conflicts under SPFE-Q01 before activation; do not put a business Invoice directly in the empty body. | SPFE-S08/SPFE-S16/SPFE-S18/SPFE-S04; [REF](#ref-source-references). |
| PCN-SPFE-R03 Preserve each response level and receipt | PCN-07 keeps HTTP status, SOAP fault, ebMS signal, structured ResponseCode and per-invoice DocumentStatusCode separate. XML values 200/406/400 are business response codes, not automatically HTTP success/failure. Retain response ID, locator, invoice identity and CSV separately; an unknown mapping remains open. | SPFE-S08/SPFE-S06/SPFE-S02; SPFE-Q15; [REF](#ref-source-references). |
| PCN-SPFE-R04 Qualify limits, authority and uncertain effects | Use each operation's documented limits and authority, holding conflicts and missing limits rather than copying defaults. The WSDL base64Binary payload declaration is not an instruction to rewrite or inline invoice bytes. MessageId and a local idempotency key do not prove provider repeat safety. Catalogue resend guidance cannot authorize a fresh mutation after an unknown result. | SPFE-S03/SPFE-S16; SPFE-Q03/Q07/Q09/Q17; [REF](#ref-source-references). |

## Part 3 Logical Service Interactions and Data Inventory

### 1 Interaction contracts

These are logical operations, not endpoint names. Commands carry requestId, connector/feature operation IDs, trusted scope, capability, contractProfileRef, payload/query reference and digest, idempotency key, correlation and expectedVersion as appropriate. Protected values stay references. Responses distinguish known outcome, pending work, denial, unsupported capability, conflict, temporary failure, outcome unknown and evidence-recovery hold.

| ID / caller → owner | Inputs, result and authority | Correlation, failure and evidence | Activities |
|---|---|---|---|
| PCN-INT-01 Feature → connector | Submit/query/cancel unsent intent; permitted workload and scope. | Scoped key/digest returns prior operation; conflict on change; D03/D09. | PCN-01/08/09 |
| PCN-INT-02 Connector → identity/authority | Resolve entity/action permission and effective version. | Denied/undetermined holds new calls; decision reference D02. | PCN-02/03/06 |
| PCN-INT-03 Connector → protected trust service | Obtain/use credential handle for purpose/environment/principal. | No key export; invalid binding denied; protected evidence D02/D04. | PCN-03/06/09 |
| PCN-INT-04 Connector → profile/connection registry | Resolve activated capability, destination and safety contract. | Versioned profile/readiness; unsupported held; D01. | PCN-02/04/05/10 |
| PCN-INT-05 Connector → public adapter → AEAT | Execute exact approved operation with fixed intent and credential handle. | Save attempt boundary; known/item results or unknown; D03–D06. | PCN-05–07 |
| PCN-INT-06 Connector/Operations → reconciliation adapter | Query original external operation under approved authority. | Query evidence/absence/unresolved; no invented endpoint; D04/D05/D07. | PCN-09 |
| PCN-INT-07 Connector → Records/owning feature | Save response and file capture receipt; publish versioned result event. | Verify scoped hash/ref before completion; recover save/notification failure; D05/D06/D08. | PCN-07/08 |
| PCN-INT-08 Authorised owner → connector/audit | Inspect/recover/disable/update profile with reason and expected version. | Reject stale/unauthorised action; preserve original operation and audit D07/D09. | PCN-09/10 |

Proposed events: PUBLIC_CONNECTOR_RESULT_RECORDED, PUBLIC_CONNECTOR_RECOVERY_REQUIRED and PUBLIC_CONNECTOR_CAPABILITY_CHANGED. Each follows durable evidence and carries eventId/version, affected scope/capability, state and safe references. A capability-change event is not route activation.

### 2 Data inventory and systems of record

| ID / record and owner | Minimum logical information and handling | Consumers |
|---|---|---|
| PCN-D01 Connection/capability profile / registry | Stable connection, country/environment, operation/protocol and schema, governed destination, activation/cohort, read/mutation semantics, idempotency/query rules, limits, source/effective version; restricted/versioned. | PCN-02/04–10 |
| PCN-D02 Eligibility snapshot / authority/trust owners | Entity/action, actor/workload, policy/authority and credential references, principal/environment/purpose, validity/check time; restricted/append-only evidence. No credentials copied. | PCN-02/03/05/06/09 |
| PCN-D03 Operation intent / connector | Scoped key, feature/connector IDs, digest, immutable payload/query reference, safety class, cancellation and current operation version; restricted, immutable input. | PCN-01/05–09 |
| PCN-D04 Execution attempt / connector | Attempt/lease generation, fixed profile/destination/bindings, pre/post-transmission markers, correlation/times and safe result; append-only. | PCN-05–09 |
| PCN-D05 External response / connector + Records | Raw protected reference/hash, per-item correlations, external codes/references, observed state and evidence meaning, catalogue version; sensitive/immutable. | PCN-07–09 |
| PCN-D06 File handoff / connector + Records | Temporary source/reference/hash/expiry, durable capture receipt and owner; sensitive, bounded staging. Permanent archive belongs to feature/Records. | PCN-06–09 |
| PCN-D07 Recovery case / Operations | Original operation, reason/safety, evidence/last query, owner, approved next action and escalation; restricted/versioned. | PCN-09/10 |
| PCN-D08 Notification outbox / connector | Event ID, operation/result version, target owner, delivery attempts/receipt and evidence refs; restricted/replayable. | PCN-07/08/09 |
| PCN-D09 Action audit / audit owner | Actor, scope/action/reason/time, versions and before/after state, evidence references and retention/hold class; restricted/append-only. | PCN-01–10 |

The public platform is authoritative for its external results; connector records are authoritative for Sage intent/attempts. Feature services own business interpretation. Retention, idempotency windows, evidence holds and staging expiry are PCN-Q04 decisions by data class; connector cleanup cannot dispose of a feature's archived invoice or unresolved-case evidence.

### 3 Reuse qualification

Assess existing Sage public transport, credential access, operation/outbox and monitoring capabilities. Record source build/design pattern, retained behaviour, Spain changes, missing operations, accountable owner and qualification evidence. The same adapter library, gateway or service deployment are alternative physical choices under PCN-Q06; whichever is selected must have one execution/idempotency owner and durable recovery. Capability selection must not copy Spain authority, error or routing rules into another country. No DTS transformation is introduced in this contract.

## Part 4 Assurance and Traceability View

### Acceptance and traceability

These scenarios specify evidence to obtain; they are not executed implementation tests.

| ID / scenario | Requirements → activities / interactions / data | Required result |
|---|---|---|
| PCN-A01 Wrong tenant/environment or untrusted override | R01 → PCN-01–03, INT-01–04, D01/D02/D09 | Denial before credential/public access; no production-to-TEST fallback. |
| PCN-A02 Valid certificate, missing/revoked action authority | R02 → PCN-03/06, INT-02/03, D02/D04/D09 | New call held; represented subject/action evidenced; other grants not inferred. |
| PCN-A03 Network check succeeds, operation unqualified | R03 → PCN-04, INT-04, D01 | Capability stays unsupported; no invoice probe or route activation. |
| PCN-A04 Duplicate and changed intent | R04 → PCN-01/05, INT-01/05, D03/D04 | Same key/digest resumes original; changed context conflicts; concurrent workers produce one effective execution claim. |
| PCN-A05 Pre-send failure versus lost response | R04/05 → PCN-05/06/09, INT-05/06, D03/D04/D07 | Proven pre-send retry permitted; possible effect becomes unknown and reconciles original operation. |
| PCN-A06 No reliable query/idempotency contract | R05 → PCN-09, INT-06/08, D03–D05/D07/D09 | Manual-only hold; repeated feature request cannot bypass it. |
| PCN-A07 Partial response/unknown error | R06 → PCN-07/08, INT-05/07, D04/D05/D08 | Missing items remain unresolved; protected source code retained; safe message does not claim blanket admission. |
| PCN-A08 External success, local persistence failure | R05/07 → PCN-07/09, INT-06/07, D03–D07 | Original outcome/evidence reconstructed without fresh mutation; crash evidence proves recovery. |
| PCN-A09 Capture/notification delayed | R07 → PCN-07–09, INT-07, D05/D06/D08 | Temporary file durably handed off before expiry; repeated/out-of-order events do not regress consumer state. |
| PCN-A10 Throttle/outage and competing tenants | R08 → PCN-05/06/09, INT-05/08, D01/D03/D04/D07 | Bounded fair backlog and circuit breaker with approved rules; no false empty result, freshness or route switch. |
| PCN-A11 Rotation/disablement/rollback during work | R09 → PCN-03/05/09/10, INT-03/04/06/08, D01–D04/D07/D09 | Original context preserved; stale worker rejected; replacement authority checked; unaffected cohorts continue. |
| PCN-A12 Unsafe content/destination and support access | R01/06/09 → PCN-02/06/09/10, INT-05/08, D04–D07/D09 | XML/resource and destination controls enforced; no credentials/raw bodies in errors/logs; unauthorised recovery denied. |
| PCN-A13 Country isolation and reuse qualification | R10 → PCN-02–06/10, INT-02–05/08, D01/D02/D04/D09 | Selected build/contracts proved; missing country binding blocks activation; Spain authority/error rules do not affect another country. |
| PCN-A14 Shared foundation handoff | R01–03/10 → PCN-02–06/09; SPEC-SEI-014 SPC-02/03/06/07, SPC-A02/08 | Public operations consume the qualified role/profile and original action, retain one execution owner and cannot activate routes or inherit private-interface readiness. |

### Open decisions and release gates

| ID / decision | Owner | Effect, evidence and gate |
|---|---|---|
| PCN-Q01 Qualify the supplied eight PRE WSDLs and ninth catalogue service, resolving SOAP/fault conflicts, missing business formats/schemas and actual PRE access | Spain Technical/Integration owners | Supports an offline adapter design from the supplied contracts. Live activation remains blocked by per-operation conflicts, missing schemas/semantics and access evidence. Recipient directory support is not assumed. |
| PCN-Q02 Action authority and accepted credential contracts | Compliance/Identity/Security | Blocks represented-business calls; bind procedure, verification/revocation and credential purpose/principal to every capability. |
| PCN-Q03 Side effects, idempotency scope/window, outcome queries and cancellation | Adapter/Operations/feature owners | Blocks automatic retry/reconciliation rules; absent evidence means manual-only after possible effect. |
| PCN-Q04 Ledger/evidence/capture durability, retention/holds and consumer replay windows | Architecture/Records/Security | Blocks implementation baseline/production; prove crash recovery and custody, especially external success with local save failure. |
| PCN-Q05 Quotas, fairness, retry budgets, breaker policy and measured objectives | Product/Operations/adapter owners | Blocks capacity/pilot sign-off; use provider terms and measured cohort volumes. |
| PCN-Q06 Physical deployment and existing implementation fit | Architecture/Connector owner | Choose library/gateway/service and single execution owner; record source build, gaps, owners and isolation/recovery evidence before reuse. |
| PCN-Q07 Safe error catalogue, per-item correlation and feature handoffs | Integration/feature owners | Blocks conformance; preserve external semantics, source hashes and durable capture/result receipts. |
| PCN-Q08 Activation, rotation/disablement and operational support | Security/Operations/Connector owner | Blocks production; named on-call, audited actions, cohort/rollback drills and pending-work handling. |

**Design review:** agree boundaries and PCN-Q01–Q04/06/07, leaving unavailable interfaces explicit. **Pilot:** activate only qualified operations and exercise A01–A13 against the selected test contract and owning features. **Production:** resolve Q05/Q08, custody/retention and outstanding action-specific contracts; require conformance, security, crash/recovery evidence and measured support objectives. This is a **reviewable logical proposal**, not an approved design or live connector deployment.

### SPFE evidence acceptance

These are required evidence scenarios, not executed implementation tests. The source-binding gate is PCN-Q01/Q02/Q03/Q07; SPFE-Q01–Q12/Q15/Q17. A source-backed review does not establish that this feature is ready for production.

| ID | Scenario | Required result | Requirement coverage |
|---|---|---|---|
| PCN-SPFE-A01 | Build each supplied WSDL request and a PRE validation request | Verify exact operation/action/port and attachment correlation. Hold the validator until its separate contract is qualified; do not infer body packaging or a registration/directory API. | PCN-SPFE-R01/PCN-SPFE-R02; PCN-02–09; [REF](#ref-source-references). |
| PCN-SPFE-A02 | Structured 200/406/400, SOAP fault, missing item and unknown CSV binding | Retain each response level and unresolved item independently; no blanket invoice admission, buyer acceptance or substituted CSV. | PCN-SPFE-R03; PCN-02–09; [REF](#ref-source-references). |
| PCN-SPFE-A03 | Same MessageId after a lost mutation response or missing operation limit | Hold/reconcile original work unless provider repeat safety is proven; retain limit conflict and authority evidence instead of borrowing defaults. | PCN-SPFE-R04; PCN-02–09; [REF](#ref-source-references). |

## REF Source references

For public-platform legal and external-contract facts, the original official sources below take precedence over earlier assumptions in linked PRDs and internal notes. PRDs retain product scope and are unchanged by this review. A source conflict remains an explicit gate; this spec cannot approve a local substitute.

Use the original files for the claims they establish. Final published regulation governs legal requirements; technical files supply their stated contract facts. Examples are illustrative. Missing or conflicting evidence remains a named gate. Product requirements and Sage design controls have separate authority. The English guide and extracts are reading aids.

| REF ID | Source and version | Exact location | Supported information and limit |
|---|---|---|---|
| SPFE-S02 | [BOE-A-2026-20587.pdf](<../context/BOE-A-2026-20587.pdf>); Final order; published 5 October 2026. | Articles 5, 8 and 11 | Submission/event receipt/CSV, legal outcomes and authority. |
| SPFE-S03 | [CatalogoServicios.pdf](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>); 0.1.0; cover 9 October 2026. | sections 4–6; pp. 7–20 | Operation/action semantics, limits, faults and ninth validation service. |
| SPFE-S08 | [FormatosEntradaSalida.pdf](<../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>); 0.1.0; cover 9 October 2026. | sections 4.3 and 5.1–5.9; pp. 7–15 | Draft formats, UBL 2.5, envelope, response codes and pending operation formats. |
| SPFE-S16 | [SendInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | types, messages, portType, SOAP binding and service ports | SendInvoice shape, opaque UBL attachment and exact PRE ports. |
| SPFE-S18 | [ebms-header-3_0-200704.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/ebms/ebms-header-3_0-200704.xsd>); Supplied 13 October 2026; SHA-256 in source manifest. | Messaging, UserMessage, PayloadInfo and imported schemas | Messaging/envelope schema; not a UBL business validator. |
| SPFE-S04 | [Peticion_ebXML- SUBMITINVOICE.xml](<../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/PETICIÓN/Peticion_ebXML- SUBMITINVOICE.xml>); Supplied 13 October 2026; SHA-256 in source manifest. | Messaging/UserMessage and PartInfo/@href | Example header, empty SOAP body and MIME cid reference. |
| SPFE-S06 | [RespuestaAltaFacturas.xml](<../context/Descripción servicios web/Ejemplos y peticiones de repuesta/20261013/01 - SendInvoicesSOAP/RESPUESTA/RespuestaAltaFacturas.xml>); Supplied 13 October 2026; SHA-256 in source manifest. | DocumentResponse/Response and DocumentReference | Example request/item result and locator; no confirmed CSV binding. |
| REF-WSDL | SPFE-S10: [CancelInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/CancelInvoice.wsdl>), SPFE-S11: [CustomerInvoiceEvents.wsdl](<../context/WSDL servicios web - PRE/20261013/CustomerInvoiceEvents.wsdl>), SPFE-S12: [DownloadInvoicesByID.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByID.wsdl>), SPFE-S13: [DownloadInvoicesByLOC.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByLOC.wsdl>), SPFE-S14: [GetInvoices.wsdl](<../context/WSDL servicios web - PRE/20261013/GetInvoices.wsdl>), SPFE-S15: [GetRegisteredInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/GetRegisteredInvoice.wsdl>), SPFE-S16: [SendInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/SendInvoice.wsdl>), SPFE-S17: [SupplierInvoiceEvents.wsdl](<../context/WSDL servicios web - PRE/20261013/SupplierInvoiceEvents.wsdl>); supplied PRE snapshot. | Each portType operation, binding and service port. | Eight exact public transport contracts. Business schemas, full action payloads and replay guarantees remain unqualified. |
| SPFE-S18 | [ebms-header-3_0-200704.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/ebms/ebms-header-3_0-200704.xsd>); supplied PRE snapshot. | xsd:schema targetNamespace `http://docs.oasis-open.org/ebxml-msg/ebms/v3.0/ns/core/200704/`; imports/types. | Messaging or SOAP/XML transport schema. Not a UBL Invoice, ApplicationResponse or DocumentStatus business schema; no country rule validation. |
| SPFE-S19 | [soap-envelope.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/w3/soap-envelope.xsd>); supplied PRE snapshot. | xsd:schema targetNamespace `http://www.w3.org/2003/05/soap-envelope`; imports/types. | Messaging or SOAP/XML transport schema. Not a UBL Invoice, ApplicationResponse or DocumentStatus business schema; no country rule validation. |
| SPFE-S20 | [xml.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/w3/xml.xsd>); supplied PRE snapshot. | xsd:schema targetNamespace `http://www.w3.org/XML/1998/namespace`; imports/types. | Messaging or SOAP/XML transport schema. Not a UBL Invoice, ApplicationResponse or DocumentStatus business schema; no country rule validation. |
| SPFE-S21 | [envelope.xsd](<../context/WSDL servicios web - PRE/20261013/xsd/xmlsoap/envelope.xsd>); supplied PRE snapshot. | xsd:schema targetNamespace `http://schemas.xmlsoap.org/soap/envelope/`; imports/types. | Messaging or SOAP/XML transport schema. Not a UBL Invoice, ApplicationResponse or DocumentStatus business schema; no country rule validation. |
| SPFE-S10 | [CancelInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/CancelInvoice.wsdl>); supplied PRE snapshot. | `CancelInvoice` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| SPFE-S11 | [CustomerInvoiceEvents.wsdl](<../context/WSDL servicios web - PRE/20261013/CustomerInvoiceEvents.wsdl>); supplied PRE snapshot. | `CustomerInvoiceEvents` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| SPFE-S12 | [DownloadInvoicesByID.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByID.wsdl>); supplied PRE snapshot. | `DownloadInvoicesByID` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| SPFE-S13 | [DownloadInvoicesByLOC.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByLOC.wsdl>); supplied PRE snapshot. | `DownloadInvoicesByLOC` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| SPFE-S14 | [GetInvoices.wsdl](<../context/WSDL servicios web - PRE/20261013/GetInvoices.wsdl>); supplied PRE snapshot. | `GetInvoices` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| SPFE-S15 | [GetRegisteredInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/GetRegisteredInvoice.wsdl>); supplied PRE snapshot. | `GetRegisteredInvoice` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| SPFE-S17 | [SupplierInvoiceEvents.wsdl](<../context/WSDL servicios web - PRE/20261013/SupplierInvoiceEvents.wsdl>); supplied PRE snapshot. | `SupplierInvoiceEvents` portType operation, SOAP binding, service ports and soap:address. | Exact PRE transport contract; business payload fields, replay and full result semantics need the catalogue/format qualifications. |
| REF-PRD | [PRD-SEI-214](../prds/PRD-SEI-214-connections-registration-routing-structured-review.md); [PRD-SEI-105](../prds/PRD-SEI-105-public-platform-environment-isolation.md); [PRD-SEI-211](../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md); [PRD-SEI-212](../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md). | Product scope and requirement IDs cited in Parts 1–4. | Canonical product requirements. Earlier external-contract assumptions are reconciled with the supplied sources; an unresolved PRD difference needs a product decision, not silent approval. |
| REF-CONTEXT | [RES-SEI-002](../context/RES-SEI-002-spain-public-platform-technical-evidence.md); [source manifest](../assets/regulatory/spain/spfe/source-manifest.json); [shared glossary](../context/GLO-SEI-001-e-invoicing-terminology.md). | Source register, shared conflicts and terminology. | Reading and traceability aids. Hashes identify snapshots; they do not prove live service acceptance or implementation readiness. |
