---
id: SPEC-SEI-006
title: Invoice receiving solution
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
  - PRD-SEI-104
  - PRD-SEI-102
  - PRD-SEI-211
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-227
  - PRD-SEI-231
  - PRD-SEI-236
  - PRD-SEI-241
  - PRD-SEI-244
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-005
  - SPEC-SEI-008
  - SPEC-SEI-009
  - SPEC-SEI-010
  - SPEC-SEI-014
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "918651328"
  page_id: "923861394"
  layout: two_left_sidebar
  toc: true
---

# Invoice receiving solution

> **Historical specification.** This document is retained for historical reference. For the current combined receiving, retrieval and download design, use [SPEC-SEI-016](SPEC-SEI-016-invoice-receiving-retrieval-and-download-solution-specification.md). Earlier content and history are preserved. Publication is disabled; this notice does not approve implementation or activation.

Terminology follows the [shared e-invoicing glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). Local terms explain this feature; exact technical IDs, fields and source codes keep their stated meanings.

## Part 1 Feature Solution Summary

### Retrieval and storage handoff

[SPEC-SEI-010](SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md) proposes public discovery, exact source capture, safe checkpointing and authorised conservation download. This receiving spec consumes the captured artefact reference and owns validation and product distribution. Recovered source availability does not wait for ERP processing; unsafe content follows the controlled quarantine-access policy. The retrieval service commits progress only after every covered item has a durable outcome.

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices still need review; **open** decisions still need an owner’s recorded answer. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### Design depth and scope

[SPEC-SEI-007](SPEC-SEI-007-invoice-sending-solution.md) provides the comparison for version binding, durable operation intent, separate outcomes and recovery. Receiving needs equivalent control over source evidence, identity, mapping, product delivery and acknowledgements. ERP issuance, outbound signing and public-copy submission remain outside this receiving journey.

All state names and contract details below are **proposed**. The source PRDs establish product requirements; they do not prove that a receiving implementation, provider acknowledgement contract or DTS inbound mapping is deployed and qualified.

### 1 Purpose, authority and boundary

This **proposed logical design** explains how Sage could receive invoices through an approved private platform or retrieve them from the public platform. The service checks the source, recipient and original file, recognises duplicates, and makes one invoice available to the correct Sage product. [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md) owns exchange/routing requirements; [PRD-SEI-211](../../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md) owns scheduled public discovery, checkpoints and freshness; [PRD-SEI-244](../../prds/PRD-SEI-244-e-invoicing-process-flow-specification.md) supplies the inbound process boundary. [SPEC-SEI-005](../SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) owns the outbound UBL validation/correction contract; this spec calls an activated inbound validation profile with separate trust and quarantine policy. [SPEC-SEI-009](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) owns lifecycle interpretation after durable receipt.

The service starts when an external invoice is available. Public consultation decides **whether and when to fetch it**. Receiving decides **what to do with the fetched invoice**.

Transport, download, technical acknowledgement, product availability, buyer acceptance and payment or rejection reporting have separate results. The supplied public catalogue and WSDLs now establish the named query/download operations and initial response levels. Exact payload/correlation, accepted profile rules, representation authority, retention, deadlines and live behavior still need qualification. See the public source binding and REF section below.

### Public source baseline

Public discovery, consultation and file download now have distinct supplied operations. Retrieval owns the public calls and durable source capture. Receiving uses those captured bytes, profile and copy classification without treating a query result or download as buyer acceptance.

See [REF Source references](#ref-source-references) for the original files, exact locations and source limits. The [technical evidence guide](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md) tracks shared source conflicts. The constraints below align this feature with the supplied public evidence; Sage implementation and activation remain gated.

### Shared connection and route handoff

The [shared connectivity and routing spec](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns role-qualified source connections, receiving-route context and permitted historical bindings (SPC-03/05/06/08). Use that context for RCV-02 recipient matching and RCV-03 trust checks; do not create a second connection registry or route engine when Sage adds its private-platform role. This receiving spec continues to own source validation, duplicate/conflict handling, original files and product delivery. A new operator profile does not qualify an existing customer-provider interface for interconnection or authorise late delivery by itself.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Intake, evidence and one business invoice | Preserve source observations, identify repeats, quarantine problems and deliver one invoice to the permitted product. | Reusable unchanged | Reuse receipt, audit and repeat-handling patterns. Receiving, Records and Product. |
| Actor, approval and accounting handoff | Let the direct business or an authorised accountant work with each client's received invoices. Keep portfolio results separate. | Reusable design pattern with country binding; implementation unknown | Reuse SPEC-SEI-002 ONB-12/13 request/evidence and client-item patterns. Product and Identity qualify actual access, approval and accounting connectors, local changes, gaps and owners. Spain public representation remains country-specific. |
| Recipient, trust, mapping and acknowledgement | Check the Spain recipient and route interval, approved inbound rules and source contract. | Reusable with country binding | Bind local identity, invoice-key rules, trust/profile packs and provider acknowledgement timing. Routing, Security and integration owner. |
| Spain receipt channels | Join public-platform retrieval and approved private receipt, preserving original/copy classification and source history. | Country-specific | Public checkpoints, bridge behaviour and Spain invoice identity need their own evidence. Do not assume the same topology elsewhere. Spain technical owner and consultation owner. |
| Existing receiving and transformation services | Assess adapters, receiving storage, product delivery and DTS mapping/validation functions. | Unknown | No complete reusable receiving implementation is proven here. DTS is a transformation candidate, not proof of retrieval or delivery support. Architecture and receiving/DTS owners. |

The existing DTS reuse direction comes from [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md). It identifies a preferred candidate; it does not certify a deployed build or Spain acceptance.

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
| Internal invoice approval | A business decision that permits a specified next step for an exact invoice revision. An eligible customer or delegate may approve. It is separate from receipt, technical acknowledgement and buyer acceptance. |
| Portfolio | An accountant's set of separately scoped client businesses. Membership does not share authority, credentials or outcomes. |
| Accounting handoff | An authorised transfer of invoice information or files to the accountant or accounting software, with its own result. |
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
| Source observation | A record of an invoice arriving or being retrieved from a particular platform. |
| Quarantine | Hold an item in restricted storage until an authorised owner resolves a trust, content or routing problem. |
| Canonical representation | The common data form used by Sage products. It is derived from the received invoice and does not replace the original. |
| Technical acknowledgement | A response defined by the platform contract. It does not by itself prove buyer approval or product availability. |
| Outbox / checkpoint | A saved record of an event waiting to be delivered; a saved position showing how far retrieval has progressed. |
| Hash / SLA | A calculated content fingerprint; and a service-level agreement. Service targets still need approval. |

### 2 Outcomes and responsibility

| Outcome | Meaning | Not implied |
|---|---|---|
| Available to product | Original and canonical references and one owning-product delivery intent are durable; product receipt is tracked separately | Product consumption, buyer approval or bookkeeping completion |
| Internal invoice approval pending | The product holds a specified business action for the eligible customer or accountant under its approval policy | Failure to capture the source or permission to delay required conservation access |
| Accountant access or handoff held | The affected client access, authority, review decision or connector needs action by its named owner | Failure of an independently authorised client receiving service |
| Processing or delivery pending | Saved source and operation identify the blocked check, mapping or product delivery and its owner | Lost invoice or permission to create a new business identity |
| Duplicate linked | Another source observation maps to an existing business invoice with its own route/reference evidence | A second product invoice |
| Quarantined | Untrusted, invalid, conflicting or unrouteable item is preserved safely with owner and reason | Trusted receipt or business delivery |
| Pending external outcome | Acknowledgement or source operation is uncertain and being reconciled | Permission to send a new acknowledgement blindly |
| No public result | A successful consultation found no new item and updated freshness | A receiving failure or proof that all historical gaps are closed |

External operator/public adapter supplies source evidence; receiving owns source classification, security gate, duplicate decision, original preservation and product publication; identity/routing owns recipient match; trust and validation services own their decisions; operations owns quarantine/recovery; the ERP owns buyer workflow after availability.

**Three operating journeys — proposed:** the client business remains the invoice recipient. The authenticated receiving service, customer user, accountant staff member and business approver are separately identified. An accountant can work for one client without a batch.

| Journey | Access and authority | Approval and processing | Result |
|---|---|---|---|
| Direct business customer | Qualify the business's receiving connection and actual service caller. Check user permission before protected access or action. | Capture and process under the receiving controls. An eligible business actor or authorised rule supplies any later internal invoice approval. | The business sees receipt, processing, product delivery and review as separate facts. |
| Accountant for one client | Bind firm, authenticated staff/service, current client relationship and separately granted viewing, download, review or reporting actions. | The accountant may approve an internal invoice step only where its grant covers that purpose. Otherwise return the action to an eligible client approver. | The same client invoice and source evidence, with permitted accountant access or a separately tracked accounting handoff. |
| Accountant portfolio | Apply the same checks independently to each client, invoice and requested action. | Collect permitted client work and show scoped progress. Missing authority or approval holds only affected access/actions; other independently authorised work continues. | Permitted per-client results and counts. Portfolio membership does not share grants, credentials or invoice outcomes. |

**Where approval belongs:** all three journeys check current authority and the applicable approval policy. Approval to set up access and act for a business is separate from approval of an individual invoice.

| Approval purpose or stage | Required boundary | Owner |
|---|---|---|
| Receive/retrieve for the business | Qualify the connection, actual caller and action authority before protected retrieval. Reuse current verified evidence where it covers the action; do not request manual approval for each source file by default. | Identity/connection owner and SPEC-SEI-010 retrieval owner |
| Capture, safety checks and conservation access | Preserve exact source files and run technical checks under RCV-01–06. Pending internal invoice approval does not delay source capture, safe checkpointing or required authorised conservation access. Unsafe files retain their controlled-access policy. | Receiving/Records and SPEC-SEI-010 |
| Internal invoice approval | After receipt, the product may require an eligible customer or delegated accountant to approve a named step, such as accounting or onward sharing. Manual, trusted-source or automatic policy choices remain open under RCV-Q12. | ERP/Product, with Identity |
| Buyer acceptance, rejection or payment reporting | These are separately authorised business decisions and reports owned by SPEC-SEI-009. Technical receipt or an internal workflow approval cannot create them automatically. | Authorised buyer/delegate and lifecycle owner |
| Accounting handoff | Check current client access, sharing purpose, target binding and any required invoice decision. Track transfer separately from source receipt and product availability. | Product/accounting connector under RCV-Q13 |

**Confirmed Spain boundary:** [Order HAC/1028/2026, Articles 9–11](https://www.boe.es/eli/es/o/2026/10/02/hac1028) requires automated public recovery by the relevant private platforms and immediate availability of recovered invoices for conservation. A third party accessing public recovery or consultation requires registered power of attorney, including automated/web-service access. Identify whether Sage, the provider or the accountant actually performs that access. A product invitation or permission to view an already stored invoice is not evidence of that public-platform authority.

**Provider evidence and limit:** [B2Brouter eAccounting](https://docs.b2brouter.net/es/user-guide/account-settings/setting-up-your-company/) describes a client-approved accountant connection. [Banqup's accounting application](https://help.banqup.com/es/articles/406403-que-es-la-aplicacion-de-contabilidad) describes a separate transfer after purchase-invoice acceptance/archive or sales-invoice sending/direct archive. These support a proposed accounting handoff pattern. They do not establish mandatory approval of every invoice, Sage implementation coverage or the meaning of a Spain commercial/reporting event.

### 3 Process diagrams

Diagram step names use plain-language actions. The smaller activity references link to the detailed behaviour and checks below.

**Inbound intake and delivery:** ![Receive, check and deliver an invoice to the product](../../assets/diagrams/receiving-intake-and-delivery-process.svg)

[Editable Draw.io](../../assets/diagrams/receiving-intake-and-delivery-process.drawio) · [PNG](../../assets/diagrams/receiving-intake-and-delivery-process.png). The existing [inbound exchange overview](../../assets/diagrams/e-invoicing-inbound-exchange.drawio) shows the same cross-service route at a broader level.

Text equivalent: RCV-01 accepts one public-retrieved or private-arrived item with saved source reference → RCV-02 authenticates channel and resolves the exact recipient/route interval → RCV-03 verifies file safety, trust, integrity and replay → RCV-04 claims identity and classifies exact repeat/conflict or a candidate for equivalence checks → RCV-05 validates activated syntax/profile and preserves exact original → RCV-06 maps approved canonical semantics → RCV-07 saves one business invoice and publishes to the authorised product → RCV-08 issues only the acknowledgement allowed by the confirmed source contract. Wrong recipient, untrusted, invalid or conflicting content is quarantined with an owner; qualified duplicate observations are linked without a second business invoice. A candidate link is finalised only after the required validation and equivalence checks. Product consumption and any conditional acknowledgement have separate evidence; RCV-08 uses the approved source milestone, not a universal after-delivery rule.

All three operating journeys use this technical receipt process. Actor access checks apply at RCV-02/07/09 and at the protected product/file operation. Internal invoice approval belongs to the product's later business workflow; it does not introduce a manual wait before RCV-01. Missing accountant authority holds that actor's access or handoff. It cannot stop a separate, valid client receiving path or turn RCV-08 into buyer acceptance.

**Retrieve public invoices and check for missing items:** ![Retrieve public invoices and check for missing items](../../assets/diagrams/e-invoicing-public-consultation-reconciliation.svg)

[Editable Draw.io](../../assets/diagrams/e-invoicing-public-consultation-reconciliation.drawio) · [PNG](../../assets/diagrams/e-invoicing-public-consultation-reconciliation.png). This existing process is owned by PRD-SEI-211. The intake handoff occurs only after a retrieved item and source context are durable. A public cursor advances under that PRD's committed-page rule, not merely because RCV-01 accepted a notification.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Owner |
|---|---|---|
| RCV-01 Register observation | Source channel, external reference, original bytes/hash and receipt time are durable | Adapter/receiving |
| RCV-02 Match recipient | Authenticated operator/public context and exact tenant/legal entity/route interval established | Identity/routing |
| RCV-03 Assess safety/trust | File, transport, signature/integrity, replay and environment result evidenced | Trust/security |
| RCV-04 Resolve identity | Claim scoped identity; decide exact repeat/conflict or hold candidate until qualification and required equivalence checks complete | Receiving/records |
| RCV-05 Validate original | Exact activated inbound syntax/profile/rules applied; invalid item quarantined | Validation |
| RCV-06 Map semantics | Approved transform produces distinct canonical representation with loss check | Transformation |
| RCV-07 Publish once | Original, context and canonical record commit; authorised product receives one business event | Receiving/product |
| RCV-08 Acknowledge/reconcile | Contractual technical response or uncertain outcome is recorded separately | Adapter/operations |
| RCV-09 Recover | Quarantine, missed delivery, cursor gap or unknown external effect has owner and safe action | Operations |

### 5 Decisions and risks

| ID / decision and design impact | Owner and evidence needed | Gate |
|---|---|---|
| RCV-Q01 Source contract: ingress, identity, retries, public read effects and query support | Integration/Spain technical owners and providers; approved contracts. Public discovery/download details stay with SPEC-SEI-010. | Integration; unverified adapter disabled |
| RCV-Q02 Recipient and effective route: late arrivals, suspension and mixed receipt | Routing/Compliance; qualified identity schemes, route history and approved late-arrival policy. | Design/pilot; uncertain match held |
| RCV-Q03 Accepted syntax/profile and inbound trust policy | Country/standards and Security; activated receive/validate capability, signature policy and conformance corpus per route. | Activation; parser success insufficient |
| RCV-Q04 Business identity and representation equivalence | Spain technical/Legal and Records; exact identity components, original/copy relation and material-conflict rules. | Design; ambiguous matches quarantined |
| RCV-Q05 Acknowledgement meaning, timing and recovery | Provider owner, Compliance and Operations; milestones, negative responses, deadline, idempotency and reliable outcome query. | Contract; no invented response promise |
| RCV-Q06 Retention, conservation access and provider exit | Legal/Privacy/Records; role-specific retention, holds, safe quarantine access and verified export. SPEC-SEI-010 owns public file access. | Production; historical evidence protected |
| RCV-Q07 Canonical and target-product contract | Receiving/Product; schema/version, supported document types and extensions, owning product and any explicit multi-product distribution policy. | Design/pilot; ambiguous target held |
| RCV-Q08 Receiving-to-product commit and delivery proof | Receiving/Architecture/Product; recoverable commit protocol, deduplication persistence, receipt query and crash evidence. | Pilot; event publication cannot prove consumption |
| RCV-Q09 DTS or alternative inbound implementation | DTS/Transformation/Validation owners; actual build, mapping direction, packs, async completion, storage handoff and operational qualification. | Activation; outbound generation does not qualify inbound parsing |
| RCV-Q10 Reprocessing and conflict resolution authority | Operations/Security/Records; permitted actions, policy selection, approvals and controls for delivered invoices. | Pilot; unsupported repair remains manual-only |
| RCV-Q11 Service objectives and capacity | Product/Operations/adapter owners; provider limits, volume baselines, retry budgets, alert thresholds and named support owners. | Production; no numeric SLA asserted |
| RCV-Q12 Actor authority and internal invoice approval policy | Product/Identity/Spain Compliance; direct and accountant staff roles, actual public caller and registered representation, eligible approvers, manual/automatic policy, decision purposes and withdrawal rules. | Delegated design/pilot; manual approval of every invoice is open. Missing required action authority blocks that action, not independently authorised capture. |
| RCV-Q13 Portfolio and accounting handoff contract | Product/Global API/Records/Architecture; supported targets, client sharing scope, connector schema, handoff identity/receipt/replay, permission-safe counts, volumes and named implementation/run owners. | Accountant/portfolio pilot; classify actual reuse, changes and gaps. Shared access or batch receipt cannot establish invoice transfer or bookkeeping completion. |

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Scope model and invariants

The source observation key includes (sourceNetwork, operator, environment, externalReference, retrieval/arrival identity). Business identity uses the approved country components plus seller, buyer, document type and issuer reference where required; no single raw field is assumed universally unique. Every record is partitioned by tenant, legal subject and environment. Source route and effective route interval are frozen when observed; a later onboarding/offboarding transition cannot rewrite them.

| ID | Rule that must always hold |
|---|---|
| RCV-I01 | Public retrieval and private arrival are alternative intake paths; both preserve their own source references and original bytes. |
| RCV-I02 | Channel authentication does not prove recipient match, legal invoice validity or buyer acceptance. |
| RCV-I03 | Wrong-tenant or unrouteable content is never exposed to another tenant/product; it is denied or quarantined with evidence with sensitive values removed. |
| RCV-I04 | Qualified network observations can attach to one business invoice; changed bytes under one observation key or conflicting business facts are not silently merged. |
| RCV-I05 | Original, derived canonical form, faithful copy and rendering are separately labelled, hashed and retained under policy. |
| RCV-I06 | Product delivery is business-idempotent: a retry or public/private duplicate cannot create another business invoice. |
| RCV-I07 | A technical acknowledgement is distinct from durable product availability and any later lifecycle status. |
| RCV-I08 | An uncertain external acknowledgement or consultation effect is reconciled before repeating an unsafe mutation. |
| RCV-I09 | A different hash proves different bytes, not necessarily a different business invoice. A private original and public faithful copy require evidenced identity and business-meaning equivalence before linking. |
| RCV-I10 | Capture, processing, product availability, product consumption, source acknowledgement and buyer lifecycle are separate facts. Failure in one does not erase evidence in another. |
| RCV-I11 | Reprocessing retains source bytes and prior decisions, fixes policy/mapping versions for that attempt, and cannot silently change an invoice already delivered to a product. |
| RCV-I12 | A duplicate candidate cannot bypass recipient, safety, trust or profile checks on the new observation. Activation is required for the exact receiving and mapping direction. |
| RCV-I13 | The represented recipient, actual receiving caller and accountant actor remain distinct. Each protected read, download, decision or handoff checks its own current client/action authority. |
| RCV-I14 | Pending internal invoice approval does not block source capture or required authorised conservation access. Technical acknowledgement and buyer acceptance keep separate meanings. |
| RCV-I15 | Accounting handoff has its own authorised target, stable identity, approval evidence where required and receipt. Failure cannot repeat external capture or create another client invoice. |
| RCV-I16 | Portfolio work and result visibility are scoped per client. Revocation stops affected future access/actions while preserving history and independently authorised client receiving work. |

### 1.1 Separate state dimensions

These are proposed logical states, not provider response codes. Each dimension has its own timestamp, evidence reference, record version and safe next action. SPEC-SEI-009 owns later commercial/payment states.

| Dimension / record | Example states | Transition and evidence rule |
|---|---|---|
| Source capture / D01 | REGISTERED, CAPTURE_VERIFIED, CAPTURE_INCOMPLETE | Only durable bytes/reference and matching hash satisfy capture; a saved notification is insufficient. |
| Receiving checks / D03/D05/D09 | CHECKS_PENDING, PROCESSING_HELD, QUALIFIED, QUARANTINED | Unavailable services hold work for retry; invalid or undetermined required results prevent qualification. Owned quarantine is a durable classification, not validation success. |
| Identity / D04 | CANDIDATE, NEW, DUPLICATE_LINKED, CONFLICT | Qualification and any required equivalence evidence precede a final duplicate link or business commit. |
| Product / D06/D07 | NOT_READY, BUSINESS_AVAILABLE, DELIVERY_PENDING, PRODUCT_RECEIVED, DELIVERY_HELD | BUSINESS_AVAILABLE follows recoverable record/outbox commit; PRODUCT_RECEIVED needs an authenticated product receipt. Event publication proves neither consumption nor accounting. |
| Source acknowledgement / D08 | NOT_REQUIRED, NOT_DUE, INTENT_SAVED, CONFIRMED, REJECTED, OUTCOME_UNKNOWN | The source contract selects the due milestone and meaning. Keep original operation identity through reconciliation. |

Public conservation access and checkpoint state remain with SPEC-SEI-010. A classification receipt may precede mapping/product completion only when its source evidence, saved processing state and recovery owner satisfy the agreed durable-outcome contract. A pending handoff is not a final classification.

Internal invoice approval and accounting handoff are additional product-owned facts under RCV-Q12/13. They do not reuse CHECKS_PENDING, BUSINESS_AVAILABLE or source acknowledgement as a business approval state. A product may show “awaiting review” after technical availability without claiming buyer acceptance or accounting completion.

### 2 Detailed behaviour

**RCV-01 Register observation.** An approved adapter supplies source network/operator, environment, authenticated channel reference, external item ID, arrival/retrieval time, declared document/profile, exact payload bytes/reference/hash and available public original/copy classification. Persist a durable intake receipt and correlation before downstream processing or any irreversible acknowledgement. Same observation key/hash returns prior state; same key with changed hash preserves a distinct conflicting attempt linked to the prior observation and enters RCV-09. Public consultation may provide a checkpoint/page identity, but cursor ownership remains with PRD-SEI-211.

A successful empty public query creates freshness evidence there, not an invoice here.

Verify that the artefact reference is accessible only to intended services, immutable under the required policy and consistent with the declared hash and file role. For public capture, reference the existing SPEC-SEI-010 record; do not create a second archive or fetch again because processing is delayed. Private receipt needs the same durable-capture controls. A metadata/object mismatch stays CAPTURE_INCOMPLETE with a Records-owned repair action; it cannot become a trusted receipt or completed public classification.

**RCV-02 Match recipient.** Verify source operator/channel and effective inbound capability, then resolve the addressed legal entity using scheme-qualified identifiers, tenant/product binding, route direction/scope and effective interval. Do not infer recipient from a user session, unqualified identifier or current route alone when the invoice was observed under an earlier interval. A wrong or ambiguous match is denied/quarantined without revealing another tenant. Delegate access is separate from receiving eligibility.

Resolve the actual service caller and its client/action authority separately from any accountant user requesting a view or refresh. Public retrieval consumes SPEC-SEI-010's qualified authority context. Staff membership, portfolio membership and certificate possession cannot substitute for an effective client grant.

Keep claimed recipient and resolved recipient separate. Check trusted adapter context against invoice identifiers; disagreement opens a restricted case. Select the owning product under an explicit binding. Do not broadcast to all products with the same tax identifier. Recheck effective binding before product commit; a concurrent route/product change creates a version conflict for Routing/Product to resolve. Suspension or offboarding preserves history but does not automatically authorise new late delivery or historical file access.

**RCV-03 Assess safety and trust.** Apply file/content-type/size/attachment safety, transport identity, signature or seal/integrity policy, status/time evidence and replay checks according to route/profile. [Certificate management](../SPEC-SEI-001-certificate-management-solution-specification.md) owns purpose-specific trust validation. A failed or undetermined required check quarantines the item; no product event or trusted acknowledgement is issued. Retain safe evidence of the original and exact trust policy version, not private keys or raw confidential content in logs.

XML parsing disables external entity and network resolution and enforces approved resource limits. Reject or quarantine unsafe attachments, expansion attacks and misleading content types under Security policy. Evaluate exact received bytes before mapping; a derived representation cannot inherit the source signature. Distinguish an unavailable trust service from a definite invalid signature while preventing trusted product availability in both cases. Restricted technical receipt evidence is allowed only under a source contract that does not imply trusted acceptance.

**RCV-04 Resolve identity.** First compare the identity of the source observation. Then compare the approved business invoice identity, content and source history. A repeated observation with the same content links to its existing result.

If the same business invoice arrives through both a private platform and the public bridge, link both source records to one business invoice only after the new observation passes its required checks. Keep each source's route, artefact role and evidence. Different syntax, signatures or a faithful public copy may produce different hashes without changing business facts. Hash comparison alone cannot approve or reject this relationship.

Where comparison is needed, keep a candidate identity link until RCV-05/06 establish profile validity and business-meaning equivalence. Compare approved identity plus required facts such as parties, document type, amounts, tax, currency and correction references under a versioned country rule. Preserve both representations. Material differences or unproven equivalence quarantine the new observation; never overwrite or silently amend the earlier invoice. Identical bytes cannot justify linking across tenant/entity/environment boundaries.

Use a unique business key and transaction, or another approved concurrency control, so simultaneous requests cannot create conflicting identity decisions.

An approved correction/credit document is a separate business document linked by its correction reference. A sender replacement is a new observation whose relationship must be decided; using the same issuer number is not permission to replace a delivered invoice. RCV-Q04 defines exact keys and equivalence rules.

**RCV-05 Validate original.** Resolve exact activated inbound syntax, document type, country, route, profile and rule pack. Validate the received original, not an unlabelled canonical substitute; record parse/schema, business/profile and route outcomes separately. Inbound validation also requires trust, recipient and quarantine policy beyond outbound preflight. An unsupported or missing profile is UNSUPPORTED/UNDETERMINED, not accepted because a parser can read it. Invalid content is preserved under restricted quarantine with a safe reason and responsible source/customer/operations actor.

Fix syntax/schema, country/profile, extension and validator versions for the attempt. Service acceptance or an asynchronous task ID is a pending result, not PASS. Resume/query the same accepted operation after timeout; record terminal evidence before continuing. Keep unsupported profile, invalid invoice and unavailable validator as separate actionable reasons. No automatic repair of source XML occurs.

**RCV-06 Map semantics.** Transform only through an approved versioned mapping into facts in the agreed common data form for the product. Store source/target hashes, mapper and comparison of business meaning. Missing required meaning or unsupported extension blocks business delivery while preserving original evidence. An authorised rendering is derived and labelled as such; it cannot replace the exchanged original. If mapping fails due to service configuration, operations owns repair and replay from the original without creating a second business invoice.

Validate canonical output against its own agreed schema and product rules, including document type, currencies, decimal precision, tax/totals, references and required extensions. Source-profile PASS does not prove canonical validity. Record retained, transformed or unsupported required meaning; silently dropping material meaning is prohibited. Consume only the result belonging to the saved source hash, scope and mapping operation/version. An expired temporary DTS result cannot substitute for durable source or output storage; resume or regenerate under the approved recovery contract.

**RCV-07 Publish once.** Save the original reference, validation and trust decisions, common data representation, business identity and product-delivery outbox together, either atomically or through a coordinated process that can recover from partial completion.

The ERP-facing event identifies the tenant and business, invoice ID, original source route, file references, status and correlation. It excludes secrets. The product uses stable event and invoice IDs to recognise repeats and acknowledge delivery.

If the product is unavailable, keep delivery pending with visible retry status. Do not report the invoice as absent or retrieve it externally again without a reason. The ERP separately manages review, acceptance, accounting and later rejection or payment actions.

Define delivery identity from business invoice, owning product/binding and approved delivery version. Concurrent workers use a unique claim and record-version check or equivalent protection. Publish from the saved outbox after commit. The product saves its deduplication key and invoice effect recoverably before returning an authenticated receipt; message receipt alone cannot prove the business effect. If the receipt is lost, query the same delivery identity or redeliver under a proven idempotency contract. Do not create a fresh invoice/event identity to bypass a timeout.

Product schema rejection is DELIVERY_HELD with a Product/Receiving owner. Consumer inbox and outbox records remain available for the approved replay window. Product transfer or additional distribution requires an explicit authority/binding decision and preserved prior delivery evidence. A crash after business commit is recovered from D06/D07 rather than restarting public retrieval.

The product applies its selected internal invoice approval policy after the technical handoff. Identify the permitted next action and eligible approver. An accountant may approve only for a currently authorised client/purpose. When a decision is required, bind it to invoice ID/revision/hash, business, purpose, approver, policy and evidence version. Reuse the request/evidence pattern in SPEC-SEI-002 ONB-12; this does not create a second onboarding case or official mandate. Pending, refused, expired, withdrawn or stale evidence holds only the dependent business action. Verify any corrected response against the current request/version and authority before resuming. An authorised automatic rule records the eligible business actor who authorised it, executing service, rule/policy version and decision evidence.

Accounting handoff uses an explicitly permitted accountant/connector target under RCV-Q13. Record a stable handoff identity tied to the existing invoice and target binding, the shared artefact roles, authority/approval evidence and target receipt. Send only permitted content. A lost receipt is queried or replayed under the same proven idempotent identity. Do not retrieve the invoice again, create another business invoice, or interpret accounting transfer as commercial acceptance. The product/connector owns this downstream work; receiving references its result.

**RCV-08 Acknowledge/reconcile.** Send a technical response only at the point allowed by the confirmed provider or public-platform contract and supported by the saved state. Record the acknowledgement kind, operation identity, content and meaning, provider reference and observed response. Keep these separate from invoice validation and buyer status.

A timeout after a possible acknowledgement produces OUTCOME_UNKNOWN. Check the original operation before another external change, unless an effective idempotency guarantee is proven. A transport acknowledgement alone cannot establish delivery to the buyer.

RCV-08 is conditional on the source's required milestone; the diagram's order does not require every source to wait for ERP delivery. Save acknowledgement intent, destination, observation, response kind, payload hash and contract version before a possible external effect. Duplicate arrival returns the existing response state under that contract. Negative/quarantine responses use approved meanings; technical rejection is not buyer commercial rejection. Public retrieval has no acknowledgement mutation unless its confirmed contract requires one. Without a safe query or repeat contract, retain OUTCOME_UNKNOWN and assign a manual-only case.

**RCV-09 Recover.** Quarantines retain safe original and source context, fault category, owner, deadline and allowed action. A corrected replacement from sender is a new observation linked to the old one; the original is not edited. Reprocess after rule/mapper repair from preserved bytes under explicit current or historically frozen policy as appropriate, recording which version yielded the new result. For public retrieval, incomplete pages/cursors and historical gap scans follow PRD-SEI-211; receiving returns saved classification for each item (ingested, duplicate, quarantined/conflict) for its safe progress decision.

Route switching preserves old invoice history and late-arrival handling.

Inspection, quarantine release, reprocessing, redelivery and retention/export are different permissions. Record actor, scope, reason, expected version, selected policies/mappings and before/after outcome. Ordinary support views use safe metadata; controlled source access follows Records/Security policy. Rule repair may qualify an undelivered item but cannot skip recipient/trust checks. Reprocessing a delivered invoice adds evidence without replacing product facts; business correction needs an explicit Product/Legal contract. Customer views show source, processing and delivery states, safe issue, owner and next action without confidential provider content.

Recheck current firm/staff/client access before accountant reads, downloads, approval responses and handoffs. Relationship or grant loss stops those affected future actions. It does not delete the client invoice or stop a receiving service whose own authority remains effective. If that service's authority is also lost, stop its affected protected calls and assign an eligible client/operational recovery owner. Preserve earlier authority and result evidence; do not transfer the old accountant's grant to a new actor.

Portfolio coordination uses separately scoped client/invoice items and the same RCV-01–09 process. One blocked review or handoff cannot stop another permitted item. Correct or replay only the affected item. Current staff/client access also filters detail, progress and counts; show a visibility limitation where an aggregate would reveal inaccessible work. Receipt or discovery for one client cannot advance another client's progress.

### 2.1 Failure and recovery decisions

| Failure / operation safety | Saved result and safe next action | Owner |
|---|---|---|
| Capture inconsistency / safe resume | CAPTURE_INCOMPLETE; reconcile object/metadata using original capture identity. No final classification or product delivery. | Records/adapter |
| Required service unavailable / idempotent resume | PROCESSING_HELD; resume saved check/transform identity and versions. Timeout is not PASS. | Validation/Trust/Transformation |
| Wrong recipient, unsafe file or material conflict / manual-only | Restricted quarantine with source, fault and owner; authorised evidence-based resolution only. | Routing/Security/Records |
| Concurrent identity claim / idempotent resume | Losing worker reads winning committed decision; changed facts enter conflict, not another invoice. | Receiving/Records |
| Partial business record/outbox commit / safe resume | Recover saved commit protocol; block publication until references and intent agree. | Receiving/Architecture |
| Product applied invoice, receipt lost / reconcile-first or proven idempotent resume | Query original delivery identity or redeliver it; retain one product business effect. | Product/Receiving |
| Source acknowledgement possibly applied / reconcile-first | Keep original operation, route and hash; query authoritative outcome. Without safe contract, manual resolution. | Adapter/Operations |
| Policy/mapper repair / authorised new attempt | Preserve source and prior results; select versions explicitly; no replacement of delivered invoice. | Operations/specialist owner |
| Route switch or provider exit / policy-bound action | Preserve source/route history and delivery/acknowledgement identities; apply approved late-arrival and historical-access rules. | Routing/Records/Compliance |

### 3 Requirements and quality controls

| ID | Requirement / source |
|---|---|
| RCV-R01 | Authenticate/authorise inbound platform and exact environment/capability; PRD-SEI-223 FR17. |
| RCV-R02 | Verify recipient, trust/integrity, syntax/profile and identity before product delivery; FR18. |
| RCV-R03 | Deduplicate private, retry and public-bridge observations to one business invoice with all evidence; FR19. |
| RCV-R04 | Deliver durably to correct entity/product once at business level; FR20. |
| RCV-R05 | Preserve original and versioned transformation/validation evidence; FR7–10. |
| RCV-R06 | Quarantine invalid, untrusted, conflicting or unrouteable content with owner; FR24. |
| RCV-R07 | Classify retry/idempotent resume/reconcile-first/manual-only and expose state; FR22–26. |
| RCV-R08 | Return durable classification for each item to public consultation and preserve freshness/gap recovery; PRD-SEI-211. |
| RCV-R09 | Keep transport, validation, product availability and lifecycle/buyer status distinct; PRD-SEI-223/224. |
| RCV-R10 | Qualify exact inbound and canonical profiles, directional mapping and required extensions before activation; PRD-SEI-223 FR7/11/27–28/31/34/43–44. |
| RCV-R11 | Preserve original/copy/derived roles and evidenced equivalence without merging material conflicts; PRD-SEI-223 FR19/30/35 and SPEC-SEI-010. |
| RCV-R12 | Recover partial commit and lost product receipt under original delivery identity; distinguish consumption from publication; PRD-SEI-223 FR20/22/25–26. |
| RCV-R13 | Authorise/audit reprocessing, restrict source access, preserve prior evidence and prevent silent changes to delivered content; PRD-SEI-223 FR10/24–26/39 and PRD-SEI-226. |
| RCV-R14 | Bind shared behaviour to country rules and qualify reused implementation for the inbound contract; PRD-SEI-223 FR27–28/43–44 and PRD-SEI-227. |
| RCV-R15 | Bind direct and accountant actors to the represented client and check current action-specific authority for receiving, access, approval and handoff; PRD-SEI-104/231 and SPEC-SEI-002. |
| RCV-R16 | Apply the selected internal approval policy after receipt, with eligible decision/version evidence; preserve capture, conservation access and technical/commercial outcome separation; Order HAC/1028/2026 Articles 9–11 and proposed RCV-Q12. |
| RCV-R17 | Track authorised accounting handoff independently with stable target identity, receipt and safe replay; approval or transfer cannot imply buyer acceptance or repeat capture; proposed RCV-Q13. |
| RCV-R18 | Isolate portfolio work, recovery and permitted visibility; on authority loss stop affected future actions while preserving history and independently authorised client receipt; PRD-SEI-104/231. |

Protect source documents, credentials and recipient data with encryption, least privilege and tenant/environment isolation. Support access is audited and redacted. Monitor receipt-to-availability latency, quarantine age, duplicate/conflict rate, product backlog, stale public freshness, time spent with an unknown acknowledgement result and wrong-recipient attempts. Objectives require provider contracts, volume baselines and Product/Operations approval; no cadence or SLA is invented here.

### SPFE source contract binding

The source facts below govern the public binding. Recovery, storage and qualification actions are proposed Sage controls where stated. Apply them through RCV-01–07, RCV-09. Source conflicts stay open under inbound profile and identity qualification; SPFE-Q04/Q06/Q09/Q13/Q14; they are not resolved by a local default.

| ID | Constraint and required behaviour | Source reference |
|---|---|---|
| RCV-SPFE-R01 Consume a captured file rather than query metadata | RCV-01 accepts the durable file reference/hash from SPEC-SEI-010. GetInvoices or GetRegisteredInvoice metadata and final source states are separate lifecycle observations. Missing file capture keeps receiving incomplete; do not synthesize an invoice from query success. | SPFE-S03/SPFE-S13; [REF](#ref-source-references). |
| RCV-SPFE-R02 Validate the new observation before linking it | RCV-02–06 verify recipient, exact UBL 2.5 public profile, source CopyIndicator and applicable fields before deduplication can complete. Keep a public copy and private original as separate artefacts. The supplied conflicting ProfileID is an owned qualification issue, not a reason to silently change bytes. | SPFE-S02/SPFE-S08/SPFE-S09; [REF](#ref-source-references). |
| RCV-SPFE-R03 Preserve source access through downstream failure | Captured source conservation access remains independent of mapping, internal approval and ERP delivery. A download retry or repeated locator observation must not create another business invoice. An ambiguous item remains an owned restricted result. | SPFE-S02/SPFE-S03; proposed receipt/deduplication control; [REF](#ref-source-references). |

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Keep the source-observation, original-file, duplicate and product-delivery contracts shared. Country/route policies determine recipient identity, business duplicate keys, accepted profiles, trust and acknowledgements. Public consultation stays a separate source adapter with its own checkpoint rules. Qualify any reused DTS mapping or validation function for the exact inbound contract; it does not own receipt or buyer workflow.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Interaction contracts

Resolve country and policy context from trusted references; do not trust a caller-supplied country/profile to activate a capability. File access is scoped to the service, tenant/entity/environment and artefact role. Responses carry operationId, outcome, evidenceRef, recordVersion, safe error category, owner and next action where relevant. These are logical fields, not an approved message schema.

Distinguish DENIED, CONFLICT, UNSUPPORTED, INVALID, PENDING, TEMPORARY_FAILURE and OUTCOME_UNKNOWN. Validation failure is not a transport failure; accepted async work is not a final result. Query/resume the same operation after a timeout unless the contract proves that no operation was accepted. Errors and product events exclude invoice bodies, secrets and unrestricted file links.

These are logical operations, not approved endpoints. Each command/event carries tenant/entity/environment, source, external reference, observationId, correlationId, payload hash, route/profile version and expected record version where applicable.

| ID | Caller → owner | Contract and safety |
|---|---|---|
| RCV-INT-01 | Private adapter/public retrieval → receiving | Register source observation and immutable payload reference; duplicate key returns prior outcome, changed hash conflicts. |
| RCV-INT-02 | Receiving → identity/routing | Resolve operator/source and recipient at observation effective time; returns scoped entity/product or ambiguous/denied. |
| RCV-INT-03 | Receiving → trust/security | Verify channel, file, integrity, signature/status and replay under effective policy; returns evidence reference or quarantine reason. |
| RCV-INT-04 | Receiving → identity index | Claim scoped technical/business identity with expected version; returns candidate, new, duplicate or conflict. Final link requires qualified observation and any equivalence evidence. |
| RCV-INT-05 | Receiving → inbound validation | Validate exact original under activated profile/rules; returns layered outcome and issues; no silent repair. |
| RCV-INT-06 | Receiving → transformation | Submit/query directional mapping with fixed versions and source hash; returns pending or terminal canonical reference/hash, target validation and business-meaning comparison; loss blocks delivery. |
| RCV-INT-07 | Receiving → product | Publish at least once with stable invoice/event/delivery IDs and schema/binding version; product deduplicates business effect and returns/query exposes authenticated receipt. Lost receipt reuses original identity. |
| RCV-INT-08 | Receiving → adapter | Issue/query technical acknowledgement under approved contract; unknown outcome reconciles before unsafe repeat. |
| RCV-INT-09 | Receiving → public consultation | Return durable classification for each item and evidence reference; consultation alone owns checkpoint/freshness. |
| RCV-INT-10 | Operations → receiving | Inspect/reprocess quarantine or delivery backlog under action-specific authority, expected version and audit; delivered content is protected from silent replacement. |
| RCV-INT-11 | Receiving/specialists → audit/records | Save scoped action, decision, attempt/version and evidence references; approved hold/retention policy governs disposal. Audit persistence failure holds actions requiring that evidence. |
| RCV-INT-12 | Product/file access/receiving ↔ Identity/approval owner | Check actual caller, represented client, firm/staff relationship, action grant and required decision purpose/version. Return effective scope/evidence or pending/denied/conflict with eligible owner. Local invitation acceptance cannot establish registered public representation. |
| RCV-INT-13 | Product → accountant/accounting connector | Transfer permitted invoice/file references under explicit target binding, stable handoff identity and qualified access/approval policy; return or query durable receipt. Lost response uses that identity and proven replay safety. Physical API, target schema and implementation remain RCV-Q13. |

Proposed events are INBOUND_ITEM_CLASSIFIED, INBOUND_INVOICE_AVAILABLE, INBOUND_QUARANTINE_OPENED and INBOUND_DELIVERY_RECOVERED. Notifications follow durable commit, are at least once, and cannot stand in for original bytes or provider evidence. Consumers deduplicate eventId/version; late events cannot regress a newer state. INBOUND_DELIVERY_RECOVERED needs product receipt evidence, not merely another publish attempt. Lifecycle consumers receive source-preserving receiving facts under SPEC-SEI-009, without inventing commercial acceptance.

| Interaction group | Persisted inputs and result evidence | Timeout/recovery boundary |
|---|---|---|
| INT-01/09 intake and public classification | Capture ID, observation key/hash, artefact role, page/item reference; saved classification/version and processing or quarantine owner. | Return prior saved receipt after crash. Pending handoff cannot complete public coverage; durable classification may precede mapping/ERP success. |
| INT-02–04 recipient, trust and identity | Qualified claimed/resolved parties, source/route interval, exact bytes, trust policy and scoped business key; versioned decision/evidence. | Dependency outage holds qualification. Concurrent claim loser reads committed state; no alternate tenant fallback. |
| INT-05/06 validation and mapping | Source/target contract, hashes, selected capability bundle and operation ID; terminal layered checks, target validation and equivalence evidence. | Resume/query accepted operation; reject mismatched or stale completion; capture output before temporary expiry. |
| INT-07 product delivery | Stable delivery/event/invoice identity, schema/product binding and protected file references; product receipt/version. | Recover commit/outbox and original delivery; no new business identity after receipt loss. |
| INT-08 acknowledgement | Approved milestone/meaning, source observation, original operation/route/hash and intent; response/query evidence. | Reconcile unknown external effect; manual-only if safe query/repeat unsupported. |
| INT-10/11 recovery and audit | Action permission, expected record version, reason, selected attempt versions and prior delivery state; immutable audit/result reference. | Reject stale or unauthorised action; keep owned held state if required evidence cannot be saved. |
| INT-12/13 actor approval and accounting handoff | Current client/action authority, decision purpose, invoice revision/hash, request/policy/target versions and stable handoff/receipt refs. | Stale or conflicting approval cannot release a hold. Recheck authority before a new protected action; reconcile/query or replay only the original permitted handoff. Capture and client receiving stay independent. |

### 2 Data inventory

| ID | Record / owner | Essential fields and handling | Consumer |
|---|---|---|---|
| RCV-D01 | Source observation / receiving; source artefact / Records | Source/operator/environment, external ref, arrival time, immutable capture/bytes reference, hash algorithm/value, artefact role and classification evidence, correlation; sensitive/immutable | RCV-01–09; public capture references SPEC-SEI-010 RSD-D04 |
| RCV-D02 | Recipient/route decision / identity/routing | Entity/tenant/product, qualified identifiers, route interval/version, source/freshness, decision reason; restricted/versioned | RCV-02/07 |
| RCV-D03 | Trust/safety result / trust | Channel, file, replay, signature/status policy/result/evidence; restricted/append-only | RCV-03/05/08 |
| RCV-D04 | Identity link / receiving | Scoped observation IDs, business key/rule version, candidate/final link, invoice ID, hashes, equivalence evidence, duplicate/conflict reason and expected version; concurrency protected | RCV-04–07/09 |
| RCV-D05 | Validation/representation / validation + transformation | Exact source/canonical references/hashes, source and target schema/profile/rules, extensions, layered results/issues, mapper/direction and equivalence evidence, rendering labels; sensitive/append-only | RCV-04–07/09 |
| RCV-D06 | Business inbound invoice / records | Stable invoice ID, buyer/seller, source route, original/canonical refs, product delivery state; restricted | RCV-07/09 |
| RCV-D07 | Product outbox / receiving; receipt / product | Event/invoice/delivery IDs, target scope/product/binding/schema version, attempts, product receipt/evidence/version and delivery state; restricted/replayable with persistent consumer deduplication | RCV-07/09 |
| RCV-D08 | External acknowledgement / adapter | Intent, due milestone/meaning, operation/observation, route/hash/contract version, attempts, response, query evidence, external ref, observed state and safety class; restricted/append-only | RCV-08/09 |
| RCV-D09 | Quarantine/recovery case / operations | Fault, original reference, owner, deadline, allowed action, evidence with sensitive values removed and audit; restricted | RCV-09 |
| RCV-D10 | Public consultation checkpoint / consultation | Cursor/window/page classification/freshness; owned by PRD-SEI-211 and SPEC-SEI-010, referenced here only | RCV-01/09 |
| RCV-D11 | Action audit and retention/hold reference / audit + Records | Actor/service, action permission, scope, time, reason, versions, before/after outcome, evidence location, country/artefact retention class and hold; restricted/append-only | RCV-01–09; INT-10/11 |
| RCV-D12 | Processing attempt / receiving + specialists | Attempt/operation IDs, source hash, fixed validator/mapper/runtime and country/profile versions, pending/terminal result reference, superseding attempt link and owner; restricted/append-only | RCV-03–07/09; INT-03/05/06/10 |
| RCV-D13 | Actor authority context / Identity | Actual receiving service or user, represented business, firm/staff/client relationship, grant refs, action/purpose/direction/environment, validity, decision snapshot and denial reason; restricted/versioned | RCV-02/07/09; INT-12/13 |
| RCV-D14 | Internal approval/accounting handoff reference / Product + connector | Existing invoice/revision/hash, decision request/version/purpose, eligible approver, policy/evidence, target/binding, stable handoff ID, permitted file roles and receipt/recovery result; restricted/versioned; no new invoice archive | RCV-07/09 downstream handoff; INT-12/13 |

Retention and deletion follow approved legal/privacy/contract policy. The original received bytes and provenance must remain explainable after canonical mapping, route change or provider exit. D10 cannot advance merely because a product event was emitted; consultation applies its own committed-page and reconciliation rules.

### 3 Reuse qualification and historical continuity

Assess existing DTS first where transformation or validation is needed. [SPEC-SEI-008](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) proposes migration of Spain UBL generation; it does not establish an inbound UBL-to-canonical contract. An outbound mapping cannot simply be reversed. No actual receiving/DTS deployment has been inspected for this spec.

| Source capability / reuse type | Retained behaviour and Spain changes | Gap, owner and evidence before activation |
|---|---|---|
| Shared intake, records and outbox / design pattern; build unknown | Reuse durable capture, scoped identity and recoverable delivery; bind Spain recipient and original/copy rules. | Receiving/Records/Product: build/version, tenant/environment isolation, commit failure and lost-receipt evidence. |
| Existing DTS / implementation candidate | Reuse qualified runtime, task completion and common format functions; supply exact inbound source-to-canonical mapping, local packs and product schema. | DTS/Validation owners: deployed contract, input/output direction, async correlation, XML access, expiry/capture, equivalence corpus and support/capacity evidence. |
| Provider/public adapters / implementation coverage unknown | Use confirmed ingress, source classification and acknowledgement/query contracts. Spain adapter remains local. | Integration/Spain technical owners: provider contract/version, conformance and timeout/duplicate drills; no inferred acknowledgement from retrieval. |
| SPEC-SEI-002 ONB-12/13 and provider accounting examples / proposed design patterns; runtime build unknown | Reuse purpose-bound approval evidence, isolated client items and separate accounting transfer. Bind receiving actors, invoice revisions, target permissions and Spain public representation. | Product/Identity/Architecture/Records: actual relationship, approval, portfolio and connector builds/contracts, gaps, owners, authority withdrawal, access isolation and lost-receipt evidence under RCV-Q12/13. |

Record retained behaviour, local changes, gaps, named build/run owner and evidence for each selected implementation. Unsupported capability stays inactive or held; another country's approved implementation does not activate Spain rules. Profile/mapper rollout affects only selected new attempts. Historical source, invoice, route and delivery identities remain fixed. Controlled reprocessing uses D12 and cannot create a new business delivery for an invoice already applied by the product. Recovery may redeliver the original delivery identity under its proven idempotency contract. Rollback restores the qualified capability for eligible work without deleting newer evidence or losing pending operations.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

| Scenario | Requirement → activity / interaction / data | Expected evidence |
|---|---|---|
| RCV-A01 Direct private invoice | R01–05 → RCV-01–07, INT-01–07, D01–07 | Authenticated source, exact original/trust/profile, correct entity and one product invoice. |
| RCV-A02 Public retrieved invoice | R02–05/08 → RCV-01–07/09, INT-01/09, D01/D10 | Durable item classification; cursor/freshness remains consultation-owned. |
| RCV-A03 Wrong recipient | R02/06 → RCV-02/09, INT-02/10, D02/09 | No cross-tenant disclosure or product event; redacted owned case. |
| RCV-A04 Invalid trust or file | R02/06 → RCV-03/09, INT-03/10, D03/09 | Quarantine; no trusted ack or product delivery. |
| RCV-A05 Same invoice via two paths | R03/04 → RCV-04/07, INT-04/07, D04/06/07 | One business invoice, both source observations retained. |
| RCV-A06 Changed observation or material identity conflict | R03/06/11 → RCV-01/04–06/09, INT-01/04–06/10, D01/D04/D05/D09 | Same observation key with changed bytes, or same business identity with materially different facts, quarantines the new attempt; prior evidence/invoice not overwritten. |
| RCV-A07 Transformation loses meaning | R05/06 → RCV-06/09, INT-06/10, D05/09 | Original preserved; no product event until approved repair. |
| RCV-A08 Product outage | R04/07 → RCV-07/09, INT-07/10, D06/07 | Durable invoice/outbox; repeated event delivery creates one product business effect after recovery. |
| RCV-A09 Ack timeout | R07/09 → RCV-08/09, INT-08, D08/09 | Unknown result reconciled; no repeated acknowledgement without checking the original outcome. |
| RCV-A10 Public gap or late item | R07/08 → RCV-09, INT-09, D01/D10 | Revisit window without duplicate invoice; freshness truthful. |
| RCV-A11 Country-bound receipt and identity | R01–03/05/06/09 → RCV-02–06/08, INT-02–06/08, D02–05/08 | Shared intake uses the selected country’s recipient, invoice-key, trust, profile and acknowledgement rules. Spain bridge observations do not define another country’s receipt model. Missing local policy quarantines or blocks the affected item without changing another country’s records. |
| RCV-A12 Original and faithful copy differ in bytes | R03/05/10/11 → RCV-03–07, INT-03–07, D01/D03–07/D12 | Qualified representations with same approved identity and equivalent facts link to one invoice while preserving roles/hashes. Changed amount, party or unproven equivalence quarantines the new observation. |
| RCV-A13 Concurrent private/public arrival | R03/04/12 → RCV-04–07, INT-04/07, D04/D06/D07 | Two workers race: one business identity and product effect; losing worker reads saved decision, with both observations retained. |
| RCV-A14 Product applies invoice, receipt lost | R04/07/12 → RCV-07/09, INT-07/10, D06/D07/D11 | Query/redelivery uses original delivery identity; deduplication survives product restart; one invoice effect and authenticated receipt. |
| RCV-A15 Crash at source or business commit | R04/05/08/12 → RCV-01/07/09, INT-01/07/09, D01/D06/D07 | Missing object/hash mismatch cannot complete capture/classification. Crash before/after business/outbox commit recovers without missing or duplicate publication; public progress does not skip an unresolved item. |
| RCV-A16 Async mapping delayed or wrong completion | R05/07/10 → RCV-05/06/09, INT-05/06/10, D05/D12 | Task acceptance remains pending; wrong scope/hash/version result is refused. Resume uses saved operation; expired temporary output is recovered under approved contract. |
| RCV-A17 Source valid, canonical invalid | R02/05/06/10 → RCV-05–07/09, INT-05/06/10, D05/D09/D12 | Source passes but target schema, tax precision, totals or required extension fails; no business availability; exact original and issues retained. |
| RCV-A18 Reprocess before and after delivery | R04/05/13 → RCV-05–07/09, INT-05–07/10/11, D05–07/D09/D11/D12 | Authorised repair records new versions and old outcomes. Undelivered item may qualify; delivered invoice cannot be silently overwritten or reissued. |
| RCV-A19 Offboarding, late arrival and product transfer | R01/04/05/13 → RCV-02/07/09, INT-02/07/10/11, D02/D06/D07/D11 | Historical route evidence retained; late receipt/transfer follows explicit approved binding. Race with binding change is held; no broadcast or loss of old history. |
| RCV-A20 Acknowledgement milestone and duplicate | R07/09 → RCV-01/08/09, INT-01/08, D01/D08/D09 | Contract permits raw technical receipt or requires later qualification: only its milestone/meaning is used. Duplicate returns saved response; no buyer rejection implied. Unknown outcome without safe query/repeat remains manual-only. |
| RCV-A21 Unsafe XML, attachment and support access | R01/02/06/13 → RCV-03/09, INT-03/10/11, D03/D09/D11 | External entity/network resolution and resource abuse blocked; unsafe content not displayed/executed. Unauthorised support read/release/reprocess denied and audited without raw payload in logs. |
| RCV-A22 Reuse activation and version rollback | R05/10/14 → RCV-03–07/09, INT-03/05–07/10, D03/D05/D06/D12 | Actual build, inbound mapping and country packs qualified; outbound generation alone insufficient. Missing country binding blocks activation. Rollout/rollback preserves historical and pending attempt identities. |
| RCV-A23 Conservation independent of processing | R05/06/08/11 → RCV-01/05–07/09, INT-01/09, D01/D05/D09/D10 | Saved source remains available under SPEC-SEI-010 access policy during mapping/product failure. Unsafe source follows controlled access. Receiving classification and public checkpoint remain distinct from ERP consumption. |
| RCV-A24 Retention hold and provider exit | R05/13 → RCV-01/09, INT-10/11, D01/D05/D06/D11 | Approved role/country retention and hold protect source/provenance; export/restore checks keep historic identities and access policy. No disposal based solely on route suspension. |
| RCV-A25 Shared source qualification across roles | R01/02/13/14; SPEC-SEI-014 SPC-R01–03/05/08 → SPC-03/05/06/08; RCV-02/03; SPC-A01/02/09 | Adding an operator role preserves existing receiving connections and invoice history; incoming trust/recipient checks use the qualified role and historical interval, with no inherited interconnection readiness or widened authority. |
| RCV-A26 Direct business awaiting invoice review | R15/16 → RCV-01–07, INT-01/07/12, D01/D06/D13/D14; Q12 | Effective receiving authority allows capture and qualified product availability. A pending internal decision holds its named accounting/reporting step, not source recovery, safe checkpointing or required authorised conservation access. |
| RCV-A27 Accountant for one client | R15/16 → RCV-02/07/09, INT-12/13, D13/D14 | An eligible accountant can approve the named internal step for the client. View/download-only access cannot approve or report rejection/payment. Missing approval identifies the eligible client actor; an invitation alone cannot enable public retrieval. |
| RCV-A28 Mixed accountant portfolio | R15/17/18 → RCV-02/07/09, INT-12/13, D13/D14; Q13 | One authorised item transfers, another waits for review and an unlinked client is denied. Items retain independent identities and results. Current counts/detail do not reveal inaccessible clients; a selected correction cannot replay other items. |
| RCV-A29 Relationship or authority withdrawn | R15/18 → RCV-02/07/09, INT-12/13, D11/D13/D14 | New affected accountant access, decisions and handoffs stop. Client files and earlier results remain. Independently authorised receipt continues; loss of the receiving service's own authority stops its affected protected calls and requires authorised recovery. |
| RCV-A30 Approval purpose, revision and country isolation | R14–16 → RCV-02/07/09, INT-12, D13/D14; Q12 | Foreign-client, stale-revision, ineligible or conflicting approval cannot release a business hold or unsafe quarantine. Qualify an automatic rule before use. Spain representation cannot authorise another country; an internal decision cannot create a buyer acceptance/reporting event. |
| RCV-A31 Accountant applies transfer, receipt lost | R17/18 → RCV-07/09, INT-13, D06/D14; Q13 | Query or proven idempotent replay uses the original invoice/target/handoff identity. No second business invoice or source retrieval. Transfer success remains separate from bookkeeping completion, buyer acceptance and statutory reporting. |

### Readiness and release evidence

| Gate | Required decision and evidence | Accountable owners |
|---|---|---|
| Design review | RCV-Q01–Q05/07–Q10/12/13: source/recipient and original/copy contracts, activation matrix, canonical/product schema, commit/receipt model, acknowledgement safety, recovery permissions, actor/approval policy, accounting handoff and selected implementation assessment. Review traceability R01–R18 and A01–A31. | Receiving, Architecture, Routing, Security, Identity, Product, Records, DTS and integration owners |
| Pilot | Qualify each selected private/public path and document/profile pair. Exercise cross-tenant denial, malicious/invalid files, mixed-route equivalence/conflict, concurrency, partial commit, lost product receipt, async completion, acknowledgement uncertainty, late arrival and authorised replay. Verify SPEC-SEI-010 capture/checkpoint handoff and SPEC-SEI-009 factual status handoff. | Integration, Receiving/Product, Security and Operations |
| Production | Resolve RCV-Q06/11; supply retention/hold, restore/export, named support, action runbooks, provider conformance, measured capacity and agreed monitoring/retry/service targets. Record evidence for each reused build and country policy; unresolved capabilities remain disabled or held. | Legal/Privacy/Records, Product, Operations and service owners |

For the accountant/portfolio pilot, close RCV-Q12/13 and exercise all three journeys, current staff/client permissions, eligible approvals, pending review during automatic capture, withdrawal, mixed item results and lost handoff receipts. Qualify the actual reused relationship, approval and connector implementations. Manual approval of every invoice remains an open Product/Compliance decision; internal invoice approval and commercial acceptance are separate purposes.

Monitor separate capture, qualification, business availability, product receipt and acknowledgement times. Alert on incomplete capture, aged quarantine, stale public freshness, delivery backlog, unknown external effects, integrity failures and absent audit evidence. Runbooks identify the original operation, permitted action, owner/escalation path and evidence needed to close the case. RCV-Q11 supplies actual thresholds and retry limits; no new deadlines or SLA are approved here.

The present readiness is **reviewable logical proposal**. The acceptance scenarios specify evidence to obtain; they do not claim that implementation tests have passed. Approved external contracts, country rules, implementation qualification and release evidence remain necessary before activation.

### SPFE evidence acceptance

These are required evidence scenarios, not executed implementation tests. The source-binding gate is inbound profile and identity qualification; SPFE-Q04/Q06/Q09/Q13/Q14. A source-backed review does not establish that this feature is ready for production.

| ID | Scenario | Required result | Requirement coverage |
|---|---|---|---|
| RCV-SPFE-A01 | A successful public query arrives without downloaded invoice bytes | Update only the evidenced metadata/lifecycle observation; no source-capture, receiving or ERP success is fabricated. | RCV-SPFE-R01; RCV-01–07, RCV-09; [REF](#ref-source-references). |
| RCV-SPFE-A02 | The same invoice is observed again as a copy or with a conflicting profile | Preserve source roles and each observation, enforce trust/profile checks and hold conflicts without rewriting source or double delivery. | RCV-SPFE-R02; RCV-01–07, RCV-09; [REF](#ref-source-references). |
| RCV-SPFE-A03 | Source capture succeeds but mapping or ERP delivery fails | Keep authorized conservation access and retry the existing downstream work without refetching or creating another invoice. | RCV-SPFE-R03; RCV-01–07, RCV-09; [REF](#ref-source-references). |

## REF Source references

For public-platform legal and external-contract facts, the original official sources below take precedence over earlier assumptions in linked PRDs and internal notes. PRDs retain product scope and are unchanged by this review. A source conflict remains an explicit gate; this spec cannot approve a local substitute.

Use the original files for the claims they establish. Final published regulation governs legal requirements; technical files supply their stated contract facts. Examples are illustrative. Missing or conflicting evidence remains a named gate. Product requirements and Sage design controls have separate authority. The English guide and extracts are reading aids.

| REF ID | Source and version | Exact location | Supported information and limit |
|---|---|---|---|
| SPFE-S02 | [BOE-A-2026-20587.pdf](<../../context/BOE-A-2026-20587.pdf>); Final order; published 5 October 2026. | Articles 3–4 and 9–11; Annex I BT-23/24 | Conservation access, authority and original/copy/profile meaning. |
| SPFE-S03 | [CatalogoServicios.pdf](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>); 0.1.0; cover 9 October 2026. | sections 6.4–6.7; pp. 12–15 | Status queries versus invoice downloads; locator download is preferred for platforms. |
| SPFE-S08 | [FormatosEntradaSalida.pdf](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>); 0.1.0; cover 9 October 2026. | section 5.1.1 and response description; pp. 8, 14 | Invoice attachments and structured response meanings; incomplete formats. |
| SPFE-S13 | [DownloadInvoicesByLOC.wsdl](<../../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByLOC.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | DownloadInvoicesByLOC operation and payload documentation | Downloaded invoice attachments; no automatic business or ERP completion. |
| SPFE-S09 | [factura.xml](<../../context/Ejemplos/20261013/factura.xml>); Supplied 13 October 2026; SHA-256 in source manifest. | cbc:ProfileID and cbc:CopyIndicator | Original example and profile conflict; no faithful-copy conformance example. |
| REF-PRD | [PRD-SEI-223](../../prds/PRD-SEI-223-interoperability-routing-transformation.md); [PRD-SEI-211](../../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md); [PRD-SEI-244](../../prds/PRD-SEI-244-e-invoicing-process-flow-specification.md); [shared platform and country-pack direction](../../prds/PRD-SEI-227-e-invoicing-as-a-service.md). | Product scope and requirement IDs cited in Parts 1–4. | Canonical product requirements. Earlier external-contract assumptions are reconciled with the supplied sources; an unresolved PRD difference needs a product decision, not silent approval. |
| REF-CONTEXT | [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md); [source manifest](../../assets/regulatory/spain/spfe/source-manifest.json); [shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md). | Source register, shared conflicts and terminology. | Reading and traceability aids. Hashes identify snapshots; they do not prove live service acceptance or implementation readiness. |
