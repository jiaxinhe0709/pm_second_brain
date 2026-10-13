---
id: SPEC-SEI-016
title: Invoice receiving, retrieval and download solution specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-13
updated: 2026-10-13
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
  - SPEC-SEI-006
  - SPEC-SEI-010
  - PRD-SEI-213
  - PRD-SEI-216
  - SPEC-SEI-014
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# Invoice receiving, retrieval and download solution specification

## Revision overview

This draft combines the current repository versions of [SPEC-SEI-006 — Invoice receiving](SPEC-SEI-006-invoice-receiving-solution.md) and [SPEC-SEI-010 — Public retrieval and download](SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md). Both predecessor files remain unchanged. Their snapshot hashes are recorded under REF-BASE-006 and REF-BASE-010.

**Reason:** stakeholders need one feature that obtains received invoices from an eligible public or private source, preserves the actual source file, processes it and permits authorised file download. Separate source contracts remain visible within that feature. The user approved a combined draft on 13 October 2026 (REF-SCOPE).

**Changes:** this document joins retrieval, receiving and stored-file access in one four-part specification. It adds private full-file intake, notification followed by fetch, and qualified private polling. It separates source-file download from customer download of a saved file. It identifies B2B Router, Sovos Spain and Sovos France as qualification contexts. France remains a reuse assessment, outside this Spain activation scope.

**Preserved:** the RCV and RSD technical IDs, public evidence, tenant/entity isolation, source roles, duplicate controls, durable progress, validation, DTS assessment, product delivery, actor authority, accountant journeys, internal approval, recovery and records controls retain their meanings. Common controls are joined through references to one source record. No second archive or product invoice is introduced.

**Open:** provider file contracts, selected source formats, build coverage, acknowledgement effects, operating targets, records policies, DTS inbound mappings, rollout scope and future publication selection still require recorded decisions. This draft does not approve implementation, activation or publication.

The new draft has no Confluence page ID. The current publishing configuration still selects SPEC-SEI-006 for receiving page `923861394` and SPEC-SEI-010 for public retrieval page `912540298`. After explicit publication approval, the combined draft can be selected for the stable receiving topic page. The owner must agree how the existing public detail page links to it. No additional page is requested by this draft, and neither predecessor is marked superseded.

Terminology follows the [shared e-invoicing glossary](../context/GLO-SEI-001-e-invoicing-terminology.md). Exact contract fields, source codes and existing activity IDs retain their meanings.

## Part 1 Feature Solution Summary

### One feature and its service handoffs

This specification owns the logical journey from source discovery or arrival to durable capture, receiving, product delivery and authorised stored-file download. Retrieval and receiving are stages of one feature. Logical service owners can remain separate; Architecture must qualify the actual service boundaries.

The public collector uses RSD-01–06/08. Private intake uses PRI-01–04. Both use the RSD-04/05 capture-and-classification controls and RCV-01–09 receiving controls. RSD-07/09 govern proposed common stored-file access and records handling, under the selected country and source policy. A saved invoice remains available through downstream mapping or product-delivery failure. Unsafe files follow a separately approved access path.

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Confirmed** means supported by the cited source within its stated limits. **Proposed** choices still need review. **Open** decisions need an owner’s recorded answer. **Out of scope** identifies work excluded from this proposal or owned by another feature. Technical IDs and state names let engineering, testing and stakeholders refer to the same item. Logical service names do not establish approved endpoints or deployed service boundaries.

### Design depth and scope

[SPEC-SEI-007](SPEC-SEI-007-invoice-sending-solution.md) provides the comparison for version binding, durable operation intent, separate outcomes and recovery. Receiving needs equivalent control over source evidence, identity, mapping, product delivery and acknowledgements. ERP issuance, outbound signing and public-copy submission remain outside this receiving journey.

All state names and contract details below are **proposed**. The source PRDs establish product requirements; they do not prove that a receiving implementation, provider acknowledgement contract or DTS inbound mapping is deployed and qualified.

### 1 Purpose, authority and boundary

This **proposed logical design** explains how Sage obtains invoices for a represented business through an eligible public or private source. Sage preserves the actual source file, checks the recipient and file, recognises repeats, maps approved business meaning and delivers one business invoice to the permitted product. An authorised user or service can also download the saved source file (RRI-R01/02/06; REF-SCOPE/REF-PRD).

The feature starts with a scheduled or requested source check, a notification, or a delivered file. A source adapter decides how to obtain the file under its qualified contract. Receiving decides what to do with the captured invoice. Customer download reads saved content. Lifecycle consultation refreshes source states. Each operation has its own evidence and result.

[PRD-SEI-211](../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md) supplies public collection requirements. Its Phase 1 exclusion of private retrieval remains unchanged. [PRD-SEI-213](../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md) and [PRD-SEI-216](../prds/PRD-SEI-216-b2b-router-integration-structured-review.md) supply private connectivity and the B2B Router discovery context. [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md) supplies exchange and receiving requirements. [PRD-SEI-244](../prds/PRD-SEI-244-e-invoicing-process-flow-specification.md) supplies the inbound process boundary. Combining the design does not select both sources for the same release; Product owns that decision under RRI-Q02.

[SPEC-SEI-005](SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) owns outbound UBL validation/correction. Inbound validation needs its own activated profile, trust and quarantine policy. [SPEC-SEI-009](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) owns public/private status consultation, interpretation, buyer decisions and payment reporting. [SPEC-SEI-014](SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns connections, role-qualified routes and historical bindings. This feature consumes those controls.

Viewing, downloading, technical acknowledgement, source capture, product availability, internal approval, buyer acceptance and payment reporting remain separate facts. A public or private query result does not prove that Sage holds the invoice file. Exact contracts, profiles, representation, retention and production behaviour remain gated.

### Source intake and download scope

| Path or action | Proposed behaviour | Evidence and boundary |
|---|---|---|
| Spain public platform | Consult/discover, download the actual invoice through the qualified ID/locator operation, capture and classify it, then commit covered progress. | SPFE-S02/S03/S12–S15 and RSD-SPFE-R01–03. Pagination, authority and complete formats remain open. |
| Private platform delivers the complete file | Authenticate the source and scope. Capture the supplied exact bytes and pass their reference to receiving. Fetch again only for a documented missing-file or integrity/recovery reason. | Proposed PRI-01–03 controls. Provider support and the exchanged source representation require RRI-Q01 evidence. |
| Private platform supplies a notification, metadata or file reference | Save the scoped observation. Fetch the exact invoice through the qualified provider contract. Keep file acquisition pending until durable capture succeeds. | A notification ID, successful query, status or temporary URL cannot stand in for the file. Acknowledgement effects and recovery need RRI-Q01 evidence. |
| Private source supports polling | Use qualified received-invoice selection, scoped limits and stable item identities. Capture and classify all covered items before claiming complete collection. | No common cursor, cadence, batch limit or notification support is assumed. PRI-02/04 and RRI-Q01/02. |
| Authorised customer, accountant or ERP downloads a saved file | Check current client/action authority, role, retention and file safety. Return clearly labelled saved bytes and audit the result. | RSD-07/09 and RRI-R06. This operation does not start another external query or assert product receipt, buyer acceptance or conservation completion. |
| Multiple invoice collection | Process many items with independent entity authority, complete item outcomes and bounded recovery. | Automated collection is in scope. A single cross-customer provider request requires specific contract evidence. |
| ZIP or customer batch export | Remains outside the initial proposed scope. | RSD-G09: Product must assess demand, cost, records access and security. This does not prevent required automated collection or single-file download. |
| Rendered PDF or canonical data | Preserve as a distinct derived representation where approved. | A rendering or metadata record cannot replace the exact structured source required by the selected contract. Source formats are qualified per provider/country. UBL 2.5 is the supplied public binding, subject to SPFE-S08 and RSD-G05/RCV-Q03 profile gates. |

**Provider contexts:** B2B Router and Sovos Spain identify Spain private-source assessments. Sovos France identifies a possible source of reusable design or implementation. These names establish no uniform API, production support, source-file format or Spain authority. Provider and country qualification remain separate under RRI-Q01/03 and RCV-Q03/09 (REF-SCOPE/REF-PRIVATE).

**External legal baseline:** final Order HAC/1028/2026, Articles 9–11, supports automated public recovery, conservation availability and registered third-party access within its stated operating model (SPFE-S02). Apply those requirements to the selected Spain scope. They do not establish a private-provider wire contract or another country's records rules.

### Public source baseline

Public discovery, consultation and file download now have distinct supplied operations. RSD-01–06/08 own public calls and durable progress within this combined feature. Receiving uses those captured bytes, profile and copy classification without treating a query result or download as buyer acceptance.

See [REF Source references](#ref-source-references) for the original files, exact locations and source limits. The [technical evidence guide](../context/RES-SEI-002-spain-public-platform-technical-evidence.md) tracks shared source conflicts. The constraints below align this feature with the supplied public evidence; Sage implementation and activation remain gated.

### Shared connection and route handoff

The [shared connectivity and routing spec](SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns role-qualified source connections, receiving-route context and permitted historical bindings (SPC-03/05/06/08). Use that context for RCV-02 recipient matching and RCV-03 trust checks; do not create a second connection registry or route engine when Sage adds its private-platform role. This receiving spec continues to own source validation, duplicate/conflict handling, original files and product delivery. A new operator profile does not qualify an existing customer-provider interface for interconnection or authorise late delivery by itself.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Intake, evidence and one business invoice | Preserve source observations, identify repeats, quarantine problems and deliver one invoice to the permitted product. | Reusable unchanged | Reuse receipt, audit and repeat-handling patterns. Receiving, Records and Product. |
| Actor, approval and accounting handoff | Let the direct business or an authorised accountant work with each client's received invoices. Keep portfolio results separate. | Reusable design pattern with country binding; implementation unknown | Reuse SPEC-SEI-002 ONB-12/13 request/evidence and client-item patterns. Product and Identity qualify actual access, approval and accounting connectors, local changes, gaps and owners. Spain public representation remains country-specific. |
| Recipient, trust, mapping and acknowledgement | Check the Spain recipient and route interval, approved inbound rules and source contract. | Reusable with country binding | Bind local identity, invoice-key rules, trust/profile packs and provider acknowledgement timing. Routing, Security and integration owner. |
| Spain receipt channels | Join public-platform retrieval and approved private receipt, preserving original/copy classification and source history. | Country-specific | Public checkpoints, bridge behaviour and Spain invoice identity need their own evidence. Do not assume the same topology elsewhere. Spain technical owner and consultation owner. |
| Capture, stored-file access, progress and recovery | Reuse the RSD-04/05/07/09 controls for every qualified Spain intake path. | Reusable design patterns with country/source binding; build coverage unknown | Records/Retrieval/Receiving/Security must prove actual capture, access, retention, progress and failure contracts. |
| B2B Router and Sovos Spain intake | Assess the exact Spain source interface, file representation, discovery/arrival and fetch/recovery contract. | Shared intake design with provider/country binding; implementation unknown | Integration Owner records contracted interface/version, local changes, gaps, build/run owner and acceptance evidence under RRI-Q01/03. |
| Sovos France collection/download | Assess a possible implementation or pattern to reuse for Spain. | Unknown; reuse candidate | France/Spain integration owners identify the actual source build, retained behaviour, country changes and gaps. France use cannot activate Spain identity, representation or records rules. |
| Existing receiving and transformation services | Assess adapters, receiving storage, product delivery and DTS mapping/validation functions. | Unknown | No complete reusable receiving implementation is proven here. DTS is a transformation candidate, not proof of retrieval or delivery support. Architecture and receiving/DTS owners. |

The existing DTS reuse direction comes from [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md). It identifies a preferred candidate; it does not certify a deployed build or Spain acceptance.

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
| Retrieval / file acquisition | Obtaining the actual invoice file from a source. A source query or notification is a separate discovery fact. |
| Source-file download / stored-file download | A source-file download transfers a file from an external source. A stored-file download returns already captured bytes to an authorised actor. Qualify which operation is meant. |
| Notification-only intake | A source event or reference saved for later file acquisition. It does not establish durable invoice-file capture or business delivery. |
| Source observation | A record of an invoice arriving or being retrieved from a particular platform. |
| Quarantine | Hold an item in restricted storage until an authorised owner resolves a trust, content or routing problem. |
| Canonical representation | The common data form used by Sage products. It is derived from the received invoice and does not replace the original. |
| Technical acknowledgement | A response defined by the platform contract. It does not by itself prove buyer approval or product availability. |
| Outbox / checkpoint | A saved record of an event waiting to be delivered; a saved position showing how far retrieval has progressed. |
| Hash / SLA | A calculated content fingerprint; and a service-level agreement. Service targets still need approval. |

### 2 Outcomes and responsibility

| Outcome | Meaning | Not implied |
|---|---|---|
| Source observed; file pending | A scoped notification or query item is saved for acquisition, with an operation, owner and next action | Verified invoice capture, completed collection, receiving success or downloadable content |
| Source file captured | Exact bytes/reference, hash, role and metadata are durable and verified under RSD-04 | Profile validity, product delivery, internal approval or buyer acceptance |
| Stored-file access result | RSD-07 records allowed, denied, failed or completed access at the qualified transfer boundary, with integrity and audit evidence | External refetch, product receipt, buyer acceptance or proof of completed conservation |
| Available to product | Original and canonical references and one owning-product delivery intent are durable; product receipt is tracked separately | Product consumption, buyer approval or bookkeeping completion |
| Internal invoice approval pending | The product holds a specified business action for the eligible customer or accountant under its approval policy | Failure to capture the source or permission to delay required conservation access |
| Accountant access or handoff held | The affected client access, authority, review decision or connector needs action by its named owner | Failure of an independently authorised client receiving service |
| Processing or delivery pending | Saved source and operation identify the blocked check, mapping or product delivery and its owner | Lost invoice or permission to create a new business identity |
| Duplicate linked | Another source observation maps to an existing business invoice with its own route/reference evidence | A second product invoice |
| Quarantined | Untrusted, invalid, conflicting or unrouteable item is preserved safely with owner and reason | Trusted receipt or business delivery |
| Pending external outcome | Acknowledgement or source operation is uncertain and being reconciled | Permission to send a new acknowledgement blindly |
| No new source result | A qualified public or private query found no new item within its stated scope and updated source freshness | A receiving failure or proof that all historical gaps are closed |

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
| Receive/retrieve for the business | Qualify the connection, actual caller and action authority before protected retrieval. Reuse current verified evidence where it covers the action; do not request manual approval for each source file by default. | Identity/connection owner and Retrieval/Adapter Owner under RSD-01 and PRI-01 |
| Capture, safety checks and conservation access | Preserve exact source files and run technical checks under RCV-01–06. Pending internal invoice approval does not delay source capture, safe checkpointing or required authorised conservation access. Unsafe files retain their controlled-access policy. | Receiving/Records under RSD-04/07/09 |
| Internal invoice approval | After receipt, the product may require an eligible customer or delegated accountant to approve a named step, such as accounting or onward sharing. Manual, trusted-source or automatic policy choices remain open under RCV-Q12. | ERP/Product, with Identity |
| Buyer acceptance, rejection or payment reporting | These are separately authorised business decisions and reports owned by SPEC-SEI-009. Technical receipt or an internal workflow approval cannot create them automatically. | Authorised buyer/delegate and lifecycle owner |
| Accounting handoff | Check current client access, sharing purpose, target binding and any required invoice decision. Track transfer separately from source receipt and product availability. | Product/accounting connector under RCV-Q13 |

**Confirmed Spain boundary:** [Order HAC/1028/2026, Articles 9–11](https://www.boe.es/eli/es/o/2026/10/02/hac1028) requires automated public recovery by the relevant private platforms and immediate availability of recovered invoices for conservation. A third party accessing public recovery or consultation requires registered power of attorney, including automated/web-service access (SPFE-S02). Identify whether Sage, the provider or the accountant actually performs that access. A product invitation or permission to view an already stored invoice is not evidence of that public-platform authority.

**Accounting pattern and limit:** the predecessor records accountant access and separate accounting transfer as proposed patterns (REF-BASE-006). Product and Identity must qualify actual relationship, approval and accounting connector contracts under RCV-Q12/13. These patterns do not prove mandatory approval of each invoice, deployed Sage support or a commercial/reporting result.

### 3 Process diagrams

Diagram step names use plain-language actions. The smaller activity references link to the detailed behaviour and checks below.

**Combined source intake, capture and download:** ![Obtain public or private invoice files, capture them and provide separate receiving and download paths](../assets/diagrams/receiving-retrieval-and-download-intake-process.svg)

[Editable Draw.io](../assets/diagrams/receiving-retrieval-and-download-intake-process.drawio) · [PNG](../assets/diagrams/receiving-retrieval-and-download-intake-process.png).

The diagram starts with an authorised source check or arrival. The public path uses RSD-01–03. The private path uses PRI-01–03 and checks whether the event already contains the file. Both join at verified source capture (RSD-04), then classification and receiving (RSD-05/RCV-01–09). Source progress uses RSD-06 or PRI-04 only after complete durable outcomes. Authorised stored-file access (RSD-07/09) runs independently of mapping or product delivery. Missing bytes, an unsafe file or an unknown external effect follows its owned hold/recovery path. File download cannot imply buyer acceptance.

The detailed diagrams below are reused unchanged from the predecessors. Their links open those base designs. The same RCV and RSD IDs are defined in this combined document; the predecessor diagrams do not prove implementation readiness.

**Inbound intake and delivery:** ![Receive, check and deliver an invoice to the product](../assets/diagrams/receiving-intake-and-delivery-process.svg)

[Editable Draw.io](../assets/diagrams/receiving-intake-and-delivery-process.drawio) · [PNG](../assets/diagrams/receiving-intake-and-delivery-process.png). The existing [inbound exchange overview](../assets/diagrams/e-invoicing-inbound-exchange.drawio) shows the same cross-service route at a broader level.

Text equivalent: RCV-01 accepts one captured item from the public or qualified private path with a saved source reference → RCV-02 authenticates channel and resolves the exact recipient/route interval → RCV-03 verifies file safety, trust, integrity and replay → RCV-04 claims identity and classifies exact repeat/conflict or a candidate for equivalence checks → RCV-05 validates activated syntax/profile and preserves exact original → RCV-06 maps approved canonical semantics → RCV-07 saves one business invoice and publishes to the authorised product → RCV-08 issues only the acknowledgement allowed by the confirmed source contract. Wrong recipient, untrusted, invalid or conflicting content is quarantined with an owner; qualified duplicate observations are linked without a second business invoice. A candidate link is finalised only after the required validation and equivalence checks. Product consumption and any conditional acknowledgement have separate evidence; RCV-08 uses the approved source milestone, not a universal after-delivery rule.

All three operating journeys use this technical receipt process. Actor access checks apply at RCV-02/07/09 and at the protected product/file operation. Internal invoice approval belongs to the product's later business workflow; it does not introduce a manual wait before RCV-01. Missing accountant authority holds that actor's access or handoff. It cannot stop a separate, valid client receiving path or turn RCV-08 into buyer acceptance.

**Retrieve public invoices and check for missing items:** ![Retrieve public invoices and check for missing items](../assets/diagrams/e-invoicing-public-consultation-reconciliation.svg)

[Editable Draw.io](../assets/diagrams/e-invoicing-public-consultation-reconciliation.drawio) · [PNG](../assets/diagrams/e-invoicing-public-consultation-reconciliation.png). This existing process is owned by PRD-SEI-211. The intake handoff occurs only after a retrieved item and source context are durable. A public cursor advances under that PRD's committed-page rule, not merely because RCV-01 accepted a notification.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Owner |
|---|---|---|
| RSD-01–03 Public intake | Check represented scope and authority, schedule a bounded run, discover and download the actual file. | Public Retrieval/Adapter |
| PRI-01–03 Private intake | Qualify caller/source, save discovery or arrival evidence, and obtain the actual file where it was not delivered. | Private Adapter/Integration |
| RSD-04 Capture source | Exact bytes, source role and metadata are durable and their hash agrees before a verified capture receipt. | Records |
| RCV-01 Register observation | Source channel, external reference, original bytes/hash and receipt time are durable | Adapter/receiving |
| RCV-02 Match recipient | Authenticated operator/public context and exact tenant/legal entity/route interval established | Identity/routing |
| RCV-03 Assess safety/trust | File, transport, signature/integrity, replay and environment result evidenced | Trust/security |
| RCV-04 Resolve identity | Claim scoped identity; decide exact repeat/conflict or hold candidate until qualification and required equivalence checks complete | Receiving/records |
| RCV-05 Validate original | Exact activated inbound syntax/profile/rules applied; invalid item quarantined | Validation |
| RCV-06 Map semantics | Approved transform produces distinct canonical representation with loss check | Transformation |
| RCV-07 Publish once | Original, context and canonical record commit; authorised product receives one business event | Receiving/product |
| RCV-08 Acknowledge/reconcile | Contractual technical response or uncertain outcome is recorded separately | Adapter/operations |
| RSD-05/06 or PRI-04 Source progress | Save receiving classification and complete covered outcomes. Mapping or product receipt is not a prerequisite where an owned durable processing state exists. | Retrieval/Adapter/Receiving |
| RSD-07/09 Read and retain files | Apply current authority, safety, retention, holds and historical access independently of downstream success. | Access/Records |
| RCV-09 Recover | Quarantine, missed delivery, cursor gap or unknown external effect has owner and safe action | Operations |

### 5 Decisions and risks

| ID / decision and design impact | Owner and evidence needed | Gate |
|---|---|---|
| RCV-Q01 Source contract: ingress, identity, retries, public read effects and query support | Integration/Spain technical owners and providers; approved contracts. RSD-01–06/08 specify public collection. PRI-01–04 specify private intake under RRI-Q01. | Integration; unverified adapter disabled |
| RCV-Q02 Recipient and effective route: late arrivals, suspension and mixed receipt | Routing/Compliance; qualified identity schemes, route history and approved late-arrival policy. | Design/pilot; uncertain match held |
| RCV-Q03 Accepted syntax/profile and inbound trust policy | Country/standards and Security; activated receive/validate capability, signature policy and conformance corpus per route. | Activation; parser success insufficient |
| RCV-Q04 Business identity and representation equivalence | Spain technical/Legal and Records; exact identity components, original/copy relation and material-conflict rules. | Design; ambiguous matches quarantined |
| RCV-Q05 Acknowledgement meaning, timing and recovery | Provider owner, Compliance and Operations; milestones, negative responses, deadline, idempotency and reliable outcome query. | Contract; no invented response promise |
| RCV-Q06 Retention, conservation access and provider exit | Legal/Privacy/Records; role-specific retention, holds, safe quarantine access and verified export. RSD-07/09 specify file access under the selected source/country records policy. | Production; historical evidence protected |
| RCV-Q07 Canonical and target-product contract | Receiving/Product; schema/version, supported document types and extensions, owning product and any explicit multi-product distribution policy. | Design/pilot; ambiguous target held |
| RCV-Q08 Receiving-to-product commit and delivery proof | Receiving/Architecture/Product; recoverable commit protocol, deduplication persistence, receipt query and crash evidence. | Pilot; event publication cannot prove consumption |
| RCV-Q09 DTS or alternative inbound implementation | DTS/Transformation/Validation owners; actual build, mapping direction, packs, async completion, storage handoff and operational qualification. | Activation; outbound generation does not qualify inbound parsing |
| RCV-Q10 Reprocessing and conflict resolution authority | Operations/Security/Records; permitted actions, policy selection, approvals and controls for delivered invoices. | Pilot; unsupported repair remains manual-only |
| RCV-Q11 Service objectives and capacity | Product/Operations/adapter owners; provider limits, volume baselines, retry budgets, alert thresholds and named support owners. | Production; no numeric SLA asserted |
| RCV-Q12 Actor authority and internal invoice approval policy | Product/Identity/Spain Compliance; direct and accountant staff roles, actual public caller and registered representation, eligible approvers, manual/automatic policy, decision purposes and withdrawal rules. | Delegated design/pilot; manual approval of every invoice is open. Missing required action authority blocks that action, not independently authorised capture. |
| RCV-Q13 Portfolio and accounting handoff contract | Product/Global API/Records/Architecture; supported targets, client sharing scope, connector schema, handoff identity/receipt/replay, permission-safe counts, volumes and named implementation/run owners. | Accountant/portfolio pilot; classify actual reuse, changes and gaps. Shared access or batch receipt cannot establish invoice transfer or bookkeeping completion. |

### Combined intake decisions

| ID / decision and design impact | Owner and evidence needed | Gate |
|---|---|---|
| RRI-Q01 Private source file and collection contract | Integration/Provider Owner and Security; exact contracted country/interface/version, actual caller/entity, full-file versus notification delivery, source-file role/profile, fetch permissions/limits, acknowledgement effects, stable identity, coverage and missed-event recovery. | Source activation; incomplete evidence keeps the affected mode disabled or pending. |
| RRI-Q02 One-feature rollout and user entry points | Product/ERP/Global API/Operations; release cohorts, enabled public/private modes, request/refresh/file-download meanings, freshness and capacity evidence. | Pilot; the combined draft does not add private retrieval to PRD-SEI-211 Phase 1 or establish a numeric cadence/SLA. |
| RRI-Q03 Provider and country implementation reuse | Platform/Integration/DTS/Records owners; source capability/build, retained behaviour, Spain changes, gaps, accountable build/run owners and qualification results for B2B Router or selected Sovos interface. | Dependent activation; another country's support, an outbound mapping or a proposed pattern cannot qualify the selected Spain path. |

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Scope model and invariants

The source observation key includes (sourceNetwork, operator, environment, externalReference, retrieval/arrival identity). Business identity uses the approved country components plus seller, buyer, document type and issuer reference where required; no single raw field is assumed universally unique. Every record is partitioned by tenant, legal subject and environment. Source route and effective route interval are frozen when observed; a later onboarding/offboarding transition cannot rewrite them.

| ID | Rule that must always hold |
|---|---|
| RCV-I01 | Public retrieval, qualified private polling, notification followed by fetch, and complete-file arrival are intake variants of one feature. Each preserves its own source references and exact bytes. Metadata-only arrival cannot satisfy capture. |
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

RSD-07/09 govern stored-file access under the selected policy. RSD-06 governs public checkpoints; PRI-04 governs private source progress. A classification receipt may precede mapping/product completion only when its source evidence, saved processing state and recovery owner satisfy the agreed durable-outcome contract. A pending handoff is not a final classification.

Internal invoice approval and accounting handoff are additional product-owned facts under RCV-Q12/13. They do not reuse CHECKS_PENDING, BUSINESS_AVAILABLE or source acknowledgement as a business approval state. A product may show “awaiting review” after technical availability without claiming buyer acceptance or accounting completion.

### 2 Retrieval, private intake and stored-file access

All intake paths check the tenant, represented business, actual caller, country, environment and effective source binding before protected work. Credential possession does not establish authority. Source roles and limits come from the selected contract. Public automatic collection remains the completeness baseline for its applicable Spain scope. A customer login or manual refresh alone cannot replace that requirement (SPFE-S02; RSD-R01/02).

### 2.1 Private intake lifecycle — proposed

The table defines provider-neutral controls. It does not assert support for any particular delivery mode. Qualify the selected provider/country/interface under RRI-Q01 before activation.

| ID / trigger and actor | Preconditions and decision inputs | Operation and required result | Error and recovery owner |
|---|---|---|---|
| PRI-01 Qualify private intake / arrival, due check or refresh | Current source connection, receiving capability, represented scope, caller authority and contracted interface/version are qualified. | Recheck scope and selected full-file, notification/fetch or polling mode. Save authority, route, profile and contract evidence. | Adapter/Identity: deny or hold unauthorised/unsupported work. Keep prior records; provider credential validity alone cannot permit capture/access for another entity. |
| PRI-02 Record discovery or arrival / qualified source mode | PRI-01 passes. Event authenticity/replay or query scope/limits are qualified. | Save the stable source item/event identity, correlation, time and available metadata. If complete bytes arrived, pass them to RSD-04. Otherwise save FETCH_PENDING and invoke PRI-03. A successful empty query saves only scoped freshness. | Adapter: duplicate events attach to prior item state. A failed query cannot be reported as empty. Save incomplete/gap evidence and retry/reconcile under the source contract. |
| PRI-03 Obtain source file / pending item | Trusted provider identity/ref, current file-access authority, selected source-file role/profile and contract are available. | Fetch the exact file through the qualified operation, or validate the supplied full-file payload/reference. RSD-04 verifies durable capture; RSD-05/RCV-01 attach the same source record to receiving. Keep metadata, structured source, copies, attachments and renderings separately labelled. | Adapter/Records: a timeout, expired link, unsupported format, incomplete body, unsafe content or missing object has its own saved reason/owner. Hold file-dependent work and collection completion. Resume the same item/operation; reconcile possible external effects before unsafe repetition. |
| PRI-04 Record covered progress and reconcile / saved item outcomes or detected gap | Every covered item has a verified source and durable receiving classification, or an approved ignore outcome with reason/policy. The scope/version and worker claim remain valid. | Save provider-specific coverage/continuation only under its qualified contract. A notification receipt is not collection completion. Recover missed events through qualified listing/history/replay, with separately bounded recovery progress and the same item/receiving identities. | Adapter/Operations: partial pages or unavailable history remain visible gaps. Do not import AEAT filters, cursor spelling, limits or read effects. Stop affected future calls when source authority is lost; preserve saved files and historical evidence. |

If an event acknowledgement only confirms durable notification receipt, the contract may permit it before file capture. Record that narrow meaning. If acknowledgement consumes the source file or ends its recoverability, require verified capture or a proven lossless recovery boundary before sending it. Acknowledgement timing, effects and repeat safety remain RCV-Q05/RRI-Q01. A saved event cannot be reported as a downloaded invoice.

Ordinary stored-file access uses RSD-07 after safe capture and current permission checks. Mapping, ERP receipt and internal invoice review cannot delay required authorised access. Unsafe content uses the approved quarantine-access path. Private-country retention and access rules require their own binding; the public order does not silently set them (RRI-R06; RSD-G03/04).

### 2.2 Public collection and common records lifecycle

RSD-01–03/06/08 retain the Spain public collector meanings from REF-BASE-010. RSD-04/05/07/09 also provide **proposed shared records and handoff controls** for qualified private sources. Their country/source binding remains mandatory. Reusing these controls does not create a second archive or approve a physical Records service.

Every activity records the tenant, represented legal entity, country, environment, route/version and correlation context. Missing authority stops new calls to the public platform. Reading a previously stored file needs a separate check of current records-access permission. Suspending onboarding does not by itself decide whether the customer may still access historical files.

| ID / trigger and actor | Preconditions and decision inputs | Operation and postcondition | Error and recovery owner |
|---|---|---|---|
| RSD-01 Check eligibility / scheduler, refresh or recovery request | The public inbound scope is active. Credential references and registered authority are valid for the legal entity/action; the policy is effective. | Save the eligible scope and policy version, or a reason and next action. Recheck before calls and before saving progress if the scope changed. | Retrieval/Authority Owners: expired credentials, missing/revoked authority or suspension stop new calls. Keep history and the checkpoint. |
| RSD-02 Schedule / eligible due scope | RSD-01 passes; provider and tenant capacity is available; no worker holds a valid lease. | Combine identical triggers into one run. Take a numbered lease and save the run ID, trigger, limits and policy. Give other tenants a fair share of capacity. | Retrieval/Operations: return the current run for a busy scope. After worker loss, take over only under lease-expiry rules; the previous worker cannot save stale progress. |
| RSD-03 Discover and fetch / worker with current lease | The adapter contract and authority are confirmed. Use the saved checkpoint or approved starting limits. | Query a page or time window within approved limits. Save the provider correlation and continuation evidence. Fetch exact files separately if the contract requires it. An empty result is different from a failed request. | Adapter Owner: follow approved throttling and retry waits. An invalid cursor opens a limited gap-recovery case. Check uncertain read/ack effects before repeating the call. |
| RSD-04 Capture source / each recovered item | The entity and environment match the requested scope. Check size/type policy, source identity and available file classification. | Save exact bytes or an approved immutable reference, hash, role, media/profile, source and retrieval time. Return a capture receipt only after the file and metadata agree. A safe saved file can become available for conservation before business processing. | Records/Security: incomplete writes, mismatches and unsafe content cannot be offered as ordinary downloads. Keep restricted evidence and retry using the saved item identity. Do not skip an item whose source has not been saved. |
| RSD-05 Register durable outcome / captured item | RSD-04 returned a receipt. The observation key/hash is stable. Receiving is available, or a recoverable handoff request can be saved. | Save the receiving receipt and classification, or a pending handoff with an owner. Receiving classifies the item as ingested, duplicate, approved ignored or quarantined. A pending handoff can be retried but does not complete the page. | Receiving/Records: the same key/hash returns the previous receipt. Changed content or an uncertain original/copy relationship enters quarantine. Later mapping or ERP failure does not undo saved capture and classification. |
| RSD-06 Commit covered progress / completed boundary | The worker still owns the current lease. Every covered item has a saved source and classification, or approved evidence explaining why it was ignored. No item is missing. | Save page/item coverage and the checkpoint together, or use a proven recovery protocol. Record the successful consultation time. ERP acknowledgement is not required to advance this retrieval checkpoint. | Retrieval Owner: after a crash, reuse saved receipts and check whether the save completed. Reject an old worker’s update. An incomplete page keeps the previous checkpoint. |
| RSD-07 Read stored file / customer, authorised ERP or operator | Current permission covers the legal entity, action, invoice and file role. Retention and safe-access rules permit the read. | Return the selected, clearly labelled file with safe content handling. Audit actor, role, purpose, result and correlation. A download attempt does not prove the customer kept the file. | Access/Records Owners: deny unauthorised or unsafe ordinary reads. A missing file or hash mismatch opens an integrity incident. Quarantine export needs approved elevated permission and audit. |
| RSD-08 Reconcile gaps / authorised operations or recovery policy | The entity/time range, authority and recovery limits are approved. Recovery has separate progress from routine retrieval. | Repeat RSD-03–06 for that range. Reuse capture and receiving identities, compare covered items and record resolved or remaining gaps. Keep the routine checkpoint. | Operations/Adapter: unavailable provider history needs an explicit recovery case and customer-impact assessment. Do not claim completeness without evidence. |
| RSD-09 Retain, transfer or delete / records policy event | Check the policy version, retention basis, holds, record owner and permission for the action. | Keep authorised historical downloads available through route/provider changes. Verify export before exit. Record deletion evidence only when deletion is allowed. | Records/Compliance: a hold prevents deletion; incomplete export prevents disposal. Restore or integrity failures open a records incident. |

### 2.3 Retrieval invariants and state separation

- A retrieved file has a source-observation identity; a business invoice has its own receiving identity. Two routes or two polls can observe the same business invoice. Capture must not cause another business invoice or ERP delivery.
- For the Spain public binding, provider identity and issuer NIF/series/number/issue date are preserved (SPFE-S02, Article 6). The exact public-code encoding is an API/profile gate, not an invented string concatenation rule in Sage.
- Every page item has an explicit saved outcome. Approved ignore rules require policy version and reason. Quarantine is a durable outcome only when source/evidence, owner and recovery action are preserved.
- `DISCOVERED`, `CAPTURED`, `QUARANTINED`, `CLASSIFIED` and `PROGRESS_COMMITTED` are proposed retrieval states. `CONSERVATION_ACCESSIBLE` is a separate access property; `BUSINESS_AVAILABLE` and `ERP_DELIVERED` belong to receiving. Their timestamps and failure reasons remain distinct.
- A faithful copy stays `PUBLIC_COPY`. If the private-route original later arrives, receiving decides the business link; neither artefact is overwritten. Unknown classification remains restricted pending evidence.
- XML parsing disables external entity/network resolution. Resource limits, file name/header handling and safe XML serving are required controls; exact limits and implementation need Security approval.
- Changing a credential, route, mapper or country policy does not rewrite the saved source or historical evidence. New attempts record the newly selected policy/version.
- A stored-file download is a Sage records read. Whether an external recovery/download operation changes provider state is a source-contract gate. If a call has a possible mutation, save intent and reconcile the authoritative result before an unsafe repeat.

**State alignment:** RSD `CAPTURED` and RCV `CAPTURE_VERIFIED` reference the same verified capture receipt. They do not cause two writes of the source file. RSD `CLASSIFIED` requires the saved receiving classification and owner; a pending handoff cannot satisfy it. The inherited RSD label `ERP_DELIVERED` needs the qualified RCV product-receipt evidence under RCV-Q08. Event publication alone cannot set that result. Architecture must bind these logical views to the actual schema under RRI-Q02; the state names do not approve new physical fields.

### 3 Receiving behaviour

**RCV-01 Register observation.** PRI-02 discovery or notification receipts are separate from invoice-file capture. A metadata-only event stays in PRI-D01 until PRI-03 and RSD-04 return a verified source reference. Receiving qualification and product delivery require that reference.

**Captured observation registration.** An approved adapter supplies source network/operator, environment, authenticated channel reference, external item ID, arrival/retrieval time, declared document/profile, exact payload bytes/reference/hash and available public original/copy classification. Persist a durable intake receipt and correlation before downstream processing or any irreversible acknowledgement. Same observation key/hash returns prior state; same key with changed hash preserves a distinct conflicting attempt linked to the prior observation and enters RCV-09. Public consultation may provide a checkpoint/page identity, but cursor ownership remains with PRD-SEI-211.

A successful empty source query creates scoped freshness/coverage evidence in its collector. It does not create an invoice in receiving.

Verify that the artefact reference is accessible only to intended services, immutable under the required policy and consistent with the declared hash and file role. For every source, reference the verified RSD-04 source artefact; do not create a second archive or fetch again because processing is delayed. Apply the same proposed durable-capture controls to qualified private receipt. A metadata/object mismatch stays CAPTURE_INCOMPLETE with a Records-owned repair action; it cannot become a trusted receipt or completed public classification.

**RCV-02 Match recipient.** Verify source operator/channel and effective inbound capability, then resolve the addressed legal entity using scheme-qualified identifiers, tenant/product binding, route direction/scope and effective interval. Do not infer recipient from a user session, unqualified identifier or current route alone when the invoice was observed under an earlier interval. A wrong or ambiguous match is denied/quarantined without revealing another tenant. Delegate access is separate from receiving eligibility.

Resolve the actual service caller and its client/action authority separately from any accountant user requesting a view or refresh. Public retrieval consumes RSD-01/INT02 qualified authority context; private intake consumes PRI-01 context. Staff membership, portfolio membership and certificate possession cannot substitute for an effective client grant.

Keep claimed recipient and resolved recipient separate. Check trusted adapter context against invoice identifiers; disagreement opens a restricted case. Select the owning product under an explicit binding. Do not broadcast to all products with the same tax identifier. Recheck effective binding before product commit; a concurrent route/product change creates a version conflict for Routing/Product to resolve. Suspension or offboarding preserves history but does not automatically authorise new late delivery or historical file access.

**RCV-03 Assess safety and trust.** Apply file/content-type/size/attachment safety, transport identity, signature or seal/integrity policy, status/time evidence and replay checks according to route/profile. [Certificate management](SPEC-SEI-001-certificate-management-solution-specification.md) owns purpose-specific trust validation. A failed or undetermined required check quarantines the item; no product event or trusted acknowledgement is issued. Retain safe evidence of the original and exact trust policy version, not private keys or raw confidential content in logs.

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

### 3.1 Receiving failure and recovery decisions

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

### 4 Receiving requirements and quality controls

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
| RCV-R11 | Preserve original/copy/derived roles and evidenced equivalence without merging material conflicts; PRD-SEI-223 FR19/30/35 and RSD-04/05/07/09. |
| RCV-R12 | Recover partial commit and lost product receipt under original delivery identity; distinguish consumption from publication; PRD-SEI-223 FR20/22/25–26. |
| RCV-R13 | Authorise/audit reprocessing, restrict source access, preserve prior evidence and prevent silent changes to delivered content; PRD-SEI-223 FR10/24–26/39 and PRD-SEI-226. |
| RCV-R14 | Bind shared behaviour to country rules and qualify reused implementation for the inbound contract; PRD-SEI-223 FR27–28/43–44 and PRD-SEI-227. |
| RCV-R15 | Bind direct and accountant actors to the represented client and check current action-specific authority for receiving, access, approval and handoff; PRD-SEI-104/231 and SPEC-SEI-002. |
| RCV-R16 | Apply the selected internal approval policy after receipt, with eligible decision/version evidence; preserve capture, conservation access and technical/commercial outcome separation; SPFE-S02, Order HAC/1028/2026 Articles 9–11, and proposed RCV-Q12. |
| RCV-R17 | Track authorised accounting handoff independently with stable target identity, receipt and safe replay; approval or transfer cannot imply buyer acceptance or repeat capture; proposed RCV-Q13. |
| RCV-R18 | Isolate portfolio work, recovery and permitted visibility; on authority loss stop affected future actions while preserving history and independently authorised client receipt; PRD-SEI-104/231. |

Protect source documents, credentials and recipient data with encryption, least privilege and tenant/environment isolation. Support access is audited and redacted. Monitor receipt-to-availability latency, quarantine age, duplicate/conflict rate, product backlog, stale public freshness, time spent with an unknown acknowledgement result and wrong-recipient attempts. Objectives require provider contracts, volume baselines and Product/Operations approval; no cadence or SLA is invented here.

### 4.1 Public retrieval requirements and failure handling

| ID | Observable requirement | Source |
|---|---|---|
| RSD-R01 | Automated retrieval checks entity/action authority separately from valid transport credentials. | PRD-SEI-211 FR1–6, FR54; SPFE-S02 Article 11. |
| RSD-R02 | Scheduled retrieval and combined refresh requests use approved limits, fair capacity and saved progress. Old workers cannot save stale results. | PRD-SEI-211 FR7–20. |
| RSD-R03 | Exact recovered source and context are durable before advancing progress; original/copy/derived roles remain explicit. | PRD-SEI-211 FR21–28, FR43–46. |
| RSD-R04 | Every committed boundary has durable item classification and recoverable coverage evidence. | PRD-SEI-211 FR17–18, FR23, FR36–38. |
| RSD-R05 | Safe source-file conservation access remains independent of ERP success; download enforces current authority and records audit. | PRD-SEI-211 FR47–53; SPFE-S02 Article 9. |
| RSD-R06 | Business identity, quarantined conflicts and failed downstream delivery reuse receiving contracts. | PRD-SEI-211 FR24–29, FR49–50. |
| RSD-R07 | Retention, holds, restore, exit and deletion are bound to artefact role and country; suspension does not erase historical source evidence. | PRD-SEI-211 FR5, FR51–52. |
| RSD-R08 | Automated multi-invoice collection works without a ZIP/export; aggregated provider scopes are enabled only with confirmed support and separate entity authority. | PRD-SEI-211 FR55. |
| RSD-R09 | Spain-specific identity, profile, representation and public routing cannot become another country's defaults. | Reuse boundaries; PRD-SEI-226/236. |

| Failure | Required saved outcome and safe action |
|---|---|
| Public API timeout, throttle or unavailability | Run failure class and provider correlation; bounded backoff. No fabricated empty result or freshness success. |
| Recovery call may change provider state and its response is lost | Preserve the original connector operation as outcome unknown. Check its authoritative result before a repeat, unless the qualified contract proves that repeating the same request is safe. Keep the prior checkpoint until every covered item has a saved outcome; an unknown call does not prove an empty page or completed recovery. |
| File recovered but storage failed | Item remains incomplete; retry capture or refetch under confirmed read semantics. Prior checkpoint remains. |
| Metadata saved but object absent, or orphan object | Recover using capture identity/hash and incomplete receipt; object is not downloadable until verified. Records Owner reconciles/cleans orphans under policy. |
| Receiving service unavailable | Durable pending handoff; retry without refetching source. Do not claim final item classification or completed page. |
| Unsafe or malformed file | Restricted quarantine; owned investigation and approved conservation-access procedure. Do not execute or display raw content in the product. |
| Changed bytes under the same identity | Preserve both observations and restrict conflicting files. Receiving/Records reconcile; no silent overwrite. |
| Worker crashes around progress commit | Resume from saved item outcomes and lease generation; reconcile commit result, avoiding lost coverage. |
| Route switched or authority revoked during run | Stop further public calls; re-evaluate any commit against saved scope version. Preserve captured evidence and use approved historical access rights. |
| Product distribution fails | RCV-07/09 retries the existing distribution identity. Retrieval/source file remains available under its policy. |
| Expired provider history or storage loss | Records/Operations recovery case; restore/reconcile against trustworthy evidence where available. Mark the gap until proved repaired. |

### 4.2 Combined feature requirements

These are proposed Sage controls supporting the user-approved combined scope and canonical public/private requirements. They are not external provider API claims (REF-SCOPE/REF-PRD/REF-PRIVATE).

| ID | Observable requirement | Control and evidence |
|---|---|---|
| RRI-R01 | Provide one receiving feature with qualified public and private intake variants. Obtain and preserve the actual invoice before file-dependent processing or delivery. | PRI-01–03; RSD-01–05; RCV-01–07. RRI-Q01/02 select the supported modes and rollout. |
| RRI-R02 | Record discovery/notification, source-file acquisition, durable capture, receiving, stored-file download and lifecycle status as distinct facts. | PRI-D01; RSD-D04/07; RCV-D01/D06. A metadata-only response cannot satisfy capture or mark a file as downloadable. |
| RRI-R03 | Qualify the selected provider, country, interface/version, source representation, authority and acknowledgement meaning before activation. | RRI-Q01/03; RCV-Q01/03/05. A provider name or a generated PDF cannot qualify the exchanged structured source. |
| RRI-R04 | Recover private missed events and partial collection under stable source identities. Claim complete progress only after durable item outcomes and qualified coverage. | PRI-02/04; PRI-D01/02; RCV-01/04/09. No fabricated cursor or borrowed public limit. |
| RRI-R05 | Record source build/capability, retained behaviour, local changes, gaps, owner and qualification evidence for each selected reused capability. Assess existing DTS first for relevant inbound transformation. | PRI-D03; RRI-Q03; RCV-Q09. France support and outbound DTS generation do not qualify Spain intake or inbound mapping. |
| RRI-R06 | Permit authorised single-file access to the captured source, with role labelling, safe handling, integrity checks, access-result audit and source/country records policy. Keep access independent of mapping/ERP success. An interrupted read can resume or repeat only under current authority and the qualified transfer contract. | RSD-04/07/09; RSD-INT07; RCV-INT-12. An ordinary read does not refetch externally or report buyer acceptance. ZIP remains RSD-G09. |

### 5 SPFE receiving contract binding

The source facts below govern the public binding. Recovery, storage and qualification actions are proposed Sage controls where stated. Apply them through RCV-01–07, RCV-09. Source conflicts stay open under inbound profile and identity qualification; SPFE-Q04/Q06/Q09/Q13/Q14; they are not resolved by a local default.

| ID | Constraint and required behaviour | Source reference |
|---|---|---|
| RCV-SPFE-R01 Consume a captured file rather than query metadata | RCV-01 accepts the durable file reference/hash from RSD-04/05 in this spec. GetInvoices or GetRegisteredInvoice metadata and final source states are separate lifecycle observations. Missing file capture keeps receiving incomplete; do not synthesize an invoice from query success. | SPFE-S03/SPFE-S13; [REF](#ref-source-references). |
| RCV-SPFE-R02 Validate the new observation before linking it | RCV-02–06 verify recipient, exact UBL 2.5 public profile, source CopyIndicator and applicable fields before deduplication can complete. Keep a public copy and private original as separate artefacts. The supplied conflicting ProfileID is an owned qualification issue, not a reason to silently change bytes. | SPFE-S02/SPFE-S08/SPFE-S09; [REF](#ref-source-references). |
| RCV-SPFE-R03 Preserve source access through downstream failure | Captured source conservation access remains independent of mapping, internal approval and ERP delivery. A download retry or repeated locator observation must not create another business invoice. An ambiguous item remains an owned restricted result. | SPFE-S02/SPFE-S03; proposed receipt/deduplication control; [REF](#ref-source-references). |

### 5.1 SPFE discovery and download contract binding

The source facts below govern the public binding. Recovery, storage and qualification actions are proposed Sage controls where stated. Apply them through RSD-01, RSD-03–06, RSD-08. Source conflicts stay open under RSD-G01/G02/G05/G06; SPFE-Q06/Q09/Q12/Q17; they are not resolved by a local default.

| ID | Constraint and required behaviour | Source reference |
|---|---|---|
| RSD-SPFE-R01 Discover by presentation date and consult by identity | RSD-03 uses GetRegisteredInvoice/QUERYBYFILTER for presentation-date discovery and GetInvoices/QUERYBYID for identity/final-status consultation. Do not use issue date as presentation date. Catalogue maxima are 1000 results/identifiers respectively; preserve raw SECUENCE_ID spelling until wire semantics are qualified. Missing filters, page ordering or continuation evidence blocks a completeness claim. | SPFE-S03/SPFE-S15/SPFE-S14; [REF](#ref-source-references). |
| RSD-SPFE-R02 Fetch the exact file through a separate download | Prefer DownloadInvoicesByLOC/DOWNLOADBYLOC where its authority contract is qualified. Retain locator separately from invoice code and MessageId. DownloadInvoicesByID/DOWNLOADBYID is the qualified alternative, with catalogue maximum 100 invoices. Do not invent a locator limit or infer file bytes from query success. Missing/failed items remain incomplete. | SPFE-S03/SPFE-S12/SPFE-S13; [REF](#ref-source-references). |
| RSD-SPFE-R03 Preserve authority, capture and complete progress | Recheck the selected issuer/recipient role and represented entity before each call. Locator/certificate and social-collaboration authorization need Article 11 reconciliation. Save exact files and item outcomes before advancing progress; no page, locator or batch shares another entity's authority or hides a failed item. | SPFE-S02/SPFE-S03; proposed durable-progress control; [REF](#ref-source-references). |

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Keep the source-observation, original-file, duplicate and product-delivery contracts shared. Country/route policies determine recipient identity, business duplicate keys, accepted profiles, trust and acknowledgements. Public consultation stays a source adapter with its own RSD-06 checkpoint rules; private coverage uses PRI-04. Logical service separation remains an Architecture decision. Qualify any reused DTS mapping or validation function for the exact inbound contract; it does not own receipt or buyer workflow.

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

### 1.1 Retrieval, capture and stored-file interactions

These contracts describe the information services exchange and the expected behaviour. They are **proposed**. Architecture must still agree the API endpoints, payload schemas, how related records are saved together, and service ownership. Each result identifies its scope, correlation, version and safe outcome or error. Pass protected credential references; never put credentials in request logs.

| ID / direction | Request and result | Activity |
|---|---|---|
| RSD-INT01 Product/Operations → Retrieval | Refresh/recovery scope and actor; returns saved current freshness plus stable queued operation or actionable denial. No synchronous AEAT dependency. | RSD-01/02/08 |
| RSD-INT02 Retrieval → Authority/Credentials | Entity/action/environment, credential and authority references; returns effective eligibility/version. Provider representation is separate from local subscription. | RSD-01/03/06 |
| RSD-INT03 Retrieval → AEAT adapter | Explicit represented scope, bounds and continuation evidence; returns discovery items/files and provider correlation or classified failure. Bind GetRegisteredInvoice/GetInvoices and the distinct download operation; exact filter, continuation and response shapes remain open. | RSD-03/08 |
| RSD-INT04 Retrieval → Records | Capture identity, exact bytes or approved reference, classification and context; returns durable verified receipt or incomplete capture. | RSD-04 |
| RSD-INT05 Retrieval → Receiving | Durable source reference/hash, observation and public-route/page context; returns stable intake receipt and saved item classification, or pending/error. | RSD-05/06 |
| RSD-INT06 Worker → Progress store | Lease generation, scope version and complete item-outcome coverage; returns committed boundary or conflict. Idempotent commit/recovery required. | RSD-06 |
| RSD-INT07 Product/ERP → File access → Records | Actor, invoice, entity, artefact role and purpose; returns authorised labelled bytes or safe denial. If temporary access links are chosen, restrict scope/expiry and redact bearer values. | RSD-07 |
| RSD-INT08 Records → Audit/Operations | Capture, access, gap, integrity, export and deletion outcomes with evidence references; durable/auditable notification and recovery ownership. | RSD-04/07/08/09 |

### 1.2 Private source interactions

All operations below are proposed logical contracts. Exact endpoints, message schemas, limits and service ownership remain RRI-Q01/02. Never log credentials, raw invoice bodies or unrestricted file links.

| ID / caller → owner | Request and result | Activity and safety |
|---|---|---|
| PRI-INT01 Private collector/adapter ↔ provider | Qualified scope, source item or event/ref, contracted interface/version and bounds; returns full-file bytes/reference, discovery evidence or classified failure. | PRI-01–03/04. Preserve source operation identity. Notification-only success remains file acquisition pending. Reconcile possible provider-state effects before unsafe retry. |
| PRI-INT02 Private adapter → Records/Receiving | Exact file and context use the same RSD-INT04 capture contract, then RSD-INT05/RCV-INT-01 registration and classification. Return existing capture/intake receipt or owned pending/error. | PRI-03; RSD-04/05; RCV-01/09. This is a traceability alias to shared contracts, not a new archive/API or second business invoice. |
| PRI-INT03 Private collector → progress/Operations | Qualified source scope/version, event/page/item identities and saved outcomes; returns coverage/continuation or an owned gap/recovery case. | PRI-02/04. No progress completion from a notification receipt, pending fetch or unresolved classification. Lease/version and partial-commit recovery require qualification. |

### 1.3 Shared contract and record ownership

| Boundary | Single record/contract | Rule |
|---|---|---|
| Source storage | RSD-D04; RSD-INT04 | Records owns one exact source artefact per source observation/content. Public identity fields apply only to the public binding. Private fields/profile/roles come from its qualified contract. |
| Receiving observation | RCV-D01 and RSD-D05; RCV-INT-01/RSD-INT05/PRI-INT02 | Receiving owns the observation/classification link. Both ID families identify views of that link, not separately saved invoice files. |
| Public progress | RSD-D03; RCV-D10 reference; RSD-INT06 | The public collector owns committed coverage. Receiving supplies classification. Product delivery is a separate result. |
| Private progress | PRI-D01/02; PRI-INT03 | The private collector owns notified/pending items and qualified coverage. Its contract does not inherit AEAT continuation or batch limits. |
| Saved-file access | RSD-INT07; RSD-D07; RCV-INT-12 authority | Access reads the selected stored role after current permission and integrity checks. Historical provider context remains preserved; a current route cannot rewrite it. |
| Business invoice/product delivery | RCV-D04/D06/D07; RCV-INT-04/07 | Receiving and the product enforce one approved business identity/effect. More source observations or customer downloads do not create another delivery. |

### 2 Data inventory

| ID | Record / owner | Essential fields and handling | Consumer |
|---|---|---|---|
| RCV-D01 | Source observation / receiving; source artefact / Records | Source/operator/environment, external ref, arrival time, immutable capture/bytes reference, hash algorithm/value, artefact role and classification evidence, correlation; sensitive/immutable | RCV-01–09; public capture references RSD-D04 in this spec |
| RCV-D02 | Recipient/route decision / identity/routing | Entity/tenant/product, qualified identifiers, route interval/version, source/freshness, decision reason; restricted/versioned | RCV-02/07 |
| RCV-D03 | Trust/safety result / trust | Channel, file, replay, signature/status policy/result/evidence; restricted/append-only | RCV-03/05/08 |
| RCV-D04 | Identity link / receiving | Scoped observation IDs, business key/rule version, candidate/final link, invoice ID, hashes, equivalence evidence, duplicate/conflict reason and expected version; concurrency protected | RCV-04–07/09 |
| RCV-D05 | Validation/representation / validation + transformation | Exact source/canonical references/hashes, source and target schema/profile/rules, extensions, layered results/issues, mapper/direction and equivalence evidence, rendering labels; sensitive/append-only | RCV-04–07/09 |
| RCV-D06 | Business inbound invoice / records | Stable invoice ID, buyer/seller, source route, original/canonical refs, product delivery state; restricted | RCV-07/09 |
| RCV-D07 | Product outbox / receiving; receipt / product | Event/invoice/delivery IDs, target scope/product/binding/schema version, attempts, product receipt/evidence/version and delivery state; restricted/replayable with persistent consumer deduplication | RCV-07/09 |
| RCV-D08 | External acknowledgement / adapter | Intent, due milestone/meaning, operation/observation, route/hash/contract version, attempts, response, query evidence, external ref, observed state and safety class; restricted/append-only | RCV-08/09 |
| RCV-D09 | Quarantine/recovery case / operations | Fault, original reference, owner, deadline, allowed action, evidence with sensitive values removed and audit; restricted | RCV-09 |
| RCV-D10 | Public consultation checkpoint / consultation | Cursor/window/page classification/freshness; owned by the RSD collector under PRD-SEI-211; points to RSD-D03 here | RCV-01/09 |
| RCV-D11 | Action audit and retention/hold reference / audit + Records | Actor/service, action permission, scope, time, reason, versions, before/after outcome, evidence location, country/artefact retention class and hold; restricted/append-only | RCV-01–09; INT-10/11 |
| RCV-D12 | Processing attempt / receiving + specialists | Attempt/operation IDs, source hash, fixed validator/mapper/runtime and country/profile versions, pending/terminal result reference, superseding attempt link and owner; restricted/append-only | RCV-03–07/09; INT-03/05/06/10 |
| RCV-D13 | Actor authority context / Identity | Actual receiving service or user, represented business, firm/staff/client relationship, grant refs, action/purpose/direction/environment, validity, decision snapshot and denial reason; restricted/versioned | RCV-02/07/09; INT-12/13 |
| RCV-D14 | Internal approval/accounting handoff reference / Product + connector | Existing invoice/revision/hash, decision request/version/purpose, eligible approver, policy/evidence, target/binding, stable handoff ID, permitted file roles and receipt/recovery result; restricted/versioned; no new invoice archive | RCV-07/09 downstream handoff; INT-12/13 |

Retention and deletion follow approved legal/privacy/contract policy. The original received bytes and provenance must remain explainable after canonical mapping, route change or provider exit. D10 cannot advance merely because a product event was emitted; consultation applies its own committed-page and reconciliation rules.

### 2.1 Retrieval and records data inventory

All invoice and identity data is sensitive. Audit uses identifiers/references rather than full invoice bodies. Encryption, least privilege, environment separation and approved storage locations apply. No customer invoice files belong in this repository.

| ID / record and system of record | Minimum logical information | Policy / consumer |
|---|---|---|
| RSD-D01 Eligibility / Authority service | Tenant, entity, country, environment, route/version, actions, registered-authority reference/status, credential reference and effective period. | Restricted; authority retention/revocation policy. RSD-01/03/06. |
| RSD-D02 Run / Retrieval | Run/operation ID, trigger/actor, scope, lease generation/expiry, bounds, provider correlation, attempts and safe failure class. | Operational retention open. RSD-02/03/08. |
| RSD-D03 Coverage/checkpoint / Retrieval | Committed bounds/continuation evidence, page identity, item-outcome references, scope/policy version, last successful query and recovery gap state. | Never silently overwritten by rescan. RSD-03/06/08. |
| RSD-D04 Source artefact / Records | Immutable object/reference, capture ID, hash algorithm/value, bytes/size, media type, source and retrieval time, public identity, invoice components, role/copy indicator, profile and integrity evidence. | Sensitive immutable source; approved role/country retention and holds. RSD-04/05/07/09. |
| RSD-D05 Observation/intake link / Receiving with Retrieval reference | Observation key/hash, artefact ID, page/item identity, intake receipt, business link if known, saved item classification, rule version and quarantine owner. | Receiving owns business deduplication; Retrieval owns coverage. RSD-05/06/08. |
| RSD-D06 Derived artefact / Receiving or rendering owner | Source link, canonical/rendered role, generator/mapping/profile version, hash and creation time. | Separate retention and access; cannot replace D04. RSD-07/09. |
| RSD-D07 File access audit / Audit | Actor, represented entity, invoice/artefact role, purpose, time, policy version, correlation and allowed/denied/read outcome. | No credentials, bearer links or raw invoice bodies. RSD-07. |
| RSD-D08 Recovery/records case / Operations and Records | Gap/integrity evidence, affected scope, hold/retention/export decision, owner, permitted actions and resolution references. | Preserve until approved resolution and retention action. RSD-08/09. |

### 2.2 Private collection and reuse records

| ID / record and owner | Minimum logical information | Consumer and policy |
|---|---|---|
| PRI-D01 Source event/collection item / Private collector | Tenant/entity/country/environment, provider/account/interface/version, event/item/ref, source time, selected file role/profile, acquisition operation and NOTIFIED/FETCH_PENDING/FILE_FETCHED or owned error; capture/intake references after verification. | PRI-01–04; PRI-INT01–03. NOTIFIED is metadata, not captured invoice content. Stable source-item identity relates repeat events; scope isolation and approved event retention apply. |
| PRI-D02 Private coverage/gap / Private collector and Operations | Qualified bounds/continuation where available, worker/scope version, covered item/classification refs, last successful check, independent recovery range, unresolved gap/history and owner. | PRI-02/04; PRI-INT03. Completeness requires evidence. Raw event sequence or latest observed timestamp alone cannot prove coverage. |
| PRI-D03 Capability/reuse qualification / Platform and Integration owners | Source country/provider/interface/build/version, retained behaviour, Spain changes, unsupported modes, gaps, accountable build/run owners, contract and test evidence, approved scope and requalification trigger. | PRI-01; RRI-Q01/03; RCV-03/05/06. Versioned/restricted. Candidate names and document completeness do not prove production readiness. |

### 3 Reuse qualification and historical continuity

Assess existing DTS first where transformation or validation is needed. [SPEC-SEI-008](SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md) proposes migration of Spain UBL generation; it does not establish an inbound UBL-to-canonical contract. An outbound mapping cannot simply be reversed. No actual receiving, private collector or DTS deployment has been inspected for this spec. Qualify the deployed contracts, selected Spain input/profile, inbound mapping, rule packs, async completion, durable storage and operating evidence before activation.

| Source capability / reuse type | Retained behaviour and Spain changes | Gap, owner and evidence before activation |
|---|---|---|
| Shared intake, records and outbox / design pattern; build unknown | Reuse durable capture, scoped identity and recoverable delivery; bind Spain recipient and original/copy rules. | Receiving/Records/Product: build/version, tenant/environment isolation, commit failure and lost-receipt evidence. |
| Existing DTS / implementation candidate | Reuse qualified runtime, task completion and common format functions; supply exact inbound source-to-canonical mapping, local packs and product schema. | DTS/Validation owners: deployed contract, input/output direction, async correlation, XML access, expiry/capture, equivalence corpus and support/capacity evidence. |
| B2B Router or selected Sovos Spain/France intake / design or implementation candidate; coverage unknown | Reuse only evidenced collection, capture, access or receiving controls. Bind Spain scope, actual source file, grants, trust and records rules. | Integration/Platform/Records: PRI-D03 records exact source build/contract, retained behaviour, country changes, gaps, owner and full-file, notification/fetch, missed-event and failed-download evidence. Each named context is assessed independently. |
| Provider/public adapters / implementation coverage unknown | Use confirmed ingress, source classification and acknowledgement/query contracts. Spain adapter remains local. | Integration/Spain technical owners: provider contract/version, conformance and timeout/duplicate drills; no inferred acknowledgement from retrieval. |
| SPEC-SEI-002 ONB-12/13 and provider accounting examples / proposed design patterns; runtime build unknown | Reuse purpose-bound approval evidence, isolated client items and separate accounting transfer. Bind receiving actors, invoice revisions, target permissions and Spain public representation. | Product/Identity/Architecture/Records: actual relationship, approval, portfolio and connector builds/contracts, gaps, owners, authority withdrawal, access isolation and lost-receipt evidence under RCV-Q12/13. |

Record retained behaviour, local changes, gaps, named build/run owner and evidence for each selected implementation. Unsupported capability stays inactive or held; another country's approved implementation does not activate Spain rules. Profile/mapper rollout affects only selected new attempts. Historical source, invoice, route and delivery identities remain fixed. Controlled reprocessing uses D12 and cannot create a new business delivery for an invoice already applied by the product. Recovery may redeliver the original delivery identity under its proven idempotency contract. Rollback restores the qualified capability for eligible work without deleting newer evidence or losing pending operations.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

The retained short references in the RCV acceptance table use the RCV namespace: `R01` means `RCV-R01`, `INT-01` means `RCV-INT-01`, and `D01` means `RCV-D01`. The RSD table below uses its own RSD namespace. The two families retain their predecessor meanings. RRI requirements join their shared outcomes; PRI IDs identify the added private intake controls.

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
| RCV-A23 Conservation independent of processing | R05/06/08/11 → RCV-01/05–07/09, INT-01/09, D01/D05/D09/D10 | Saved source remains available under RSD-07/09 access policy during mapping/product failure. Unsafe source follows controlled access. Receiving classification and public checkpoint remain distinct from ERP consumption. |
| RCV-A24 Retention hold and provider exit | R05/13 → RCV-01/09, INT-10/11, D01/D05/D06/D11 | Approved role/country retention and hold protect source/provenance; export/restore checks keep historic identities and access policy. No disposal based solely on route suspension. |
| RCV-A25 Shared source qualification across roles | R01/02/13/14; SPEC-SEI-014 SPC-R01–03/05/08 → SPC-03/05/06/08; RCV-02/03; SPC-A01/02/09 | Adding an operator role preserves existing receiving connections and invoice history; incoming trust/recipient checks use the qualified role and historical interval, with no inherited interconnection readiness or widened authority. |
| RCV-A26 Direct business awaiting invoice review | R15/16 → RCV-01–07, INT-01/07/12, D01/D06/D13/D14; Q12 | Effective receiving authority allows capture and qualified product availability. A pending internal decision holds its named accounting/reporting step, not source recovery, safe checkpointing or required authorised conservation access. |
| RCV-A27 Accountant for one client | R15/16 → RCV-02/07/09, INT-12/13, D13/D14 | An eligible accountant can approve the named internal step for the client. View/download-only access cannot approve or report rejection/payment. Missing approval identifies the eligible client actor; an invitation alone cannot enable public retrieval. |
| RCV-A28 Mixed accountant portfolio | R15/17/18 → RCV-02/07/09, INT-12/13, D13/D14; Q13 | One authorised item transfers, another waits for review and an unlinked client is denied. Items retain independent identities and results. Current counts/detail do not reveal inaccessible clients; a selected correction cannot replay other items. |
| RCV-A29 Relationship or authority withdrawn | R15/18 → RCV-02/07/09, INT-12/13, D11/D13/D14 | New affected accountant access, decisions and handoffs stop. Client files and earlier results remain. Independently authorised receipt continues; loss of the receiving service's own authority stops its affected protected calls and requires authorised recovery. |
| RCV-A30 Approval purpose, revision and country isolation | R14–16 → RCV-02/07/09, INT-12, D13/D14; Q12 | Foreign-client, stale-revision, ineligible or conflicting approval cannot release a business hold or unsafe quarantine. Qualify an automatic rule before use. Spain representation cannot authorise another country; an internal decision cannot create a buyer acceptance/reporting event. |
| RCV-A31 Accountant applies transfer, receipt lost | R17/18 → RCV-07/09, INT-13, D06/D14; Q13 | Query or proven idempotent replay uses the original invoice/target/handoff identity. No second business invoice or source retrieval. Transfer success remains separate from bookkeeping completion, buyer acceptance and statutory reporting. |

### Retrieval and file-access acceptance

In this table, `R01` means `RSD-R01` and `G01` means `RSD-G01`. Each scenario retains its RSD requirement and gate references from the public retrieval predecessor. Shared capture/access controls apply to private intake only under its qualified country/source binding.

| ID | Scenario and expected evidence | Requirement |
|---|---|---|
| RSD-A01 | Valid certificate, missing registered customer authority: public calls are blocked; saved reason names the required action without exposing credentials. | R01 |
| RSD-A02 | Login and scheduled refresh coincide: one scoped operation continues; another tenant still receives capacity. | R02 |
| RSD-A03 | Page has three items; the second cannot be stored: committed progress does not skip it. Restart resumes saved outcomes without another business invoice. | R03/R04 |
| RSD-A04 | Source capture succeeds but mapping or ERP delivery fails: permitted conservation download succeeds and remains distinct from business availability. | R05/R06 |
| RSD-A05 | Public faithful copy and private original represent one invoice: artefact roles and bytes remain separate; receiving creates one business identity. | R03/R06 |
| RSD-A06 | Same observation has changed bytes: both source observations remain traceable; conflict is restricted and owned. | R03/R06 |
| RSD-A07 | Worker takeover occurs before commit: old lease generation cannot advance progress; new worker resumes/reconciles safely. | R02/R04 |
| RSD-A08 | Wrong tenant, entity, role or environment requests a file: no bytes are returned and denial is audited without revealing invoice details. | R05/R09 |
| RSD-A09 | Unsafe file is quarantined: ordinary access and ERP processing stop; an approved authorised conservation/recovery procedure remains available and audited. | R05 |
| RSD-A10 | Cursor expires or history is missing: bounded rescan preserves routine progress; unresolved loss is visible rather than reported as empty/successful. | R02/R04 |
| RSD-A11 | Provider/route changes or retention hold applies: historical access follows approved entitlement; held files cannot be deleted; exit export is verified before disposal. | R07 |
| RSD-A12 | No multi-entity API and no ZIP feature exist: automated collection still retrieves multiple invoices with independent entity authority and progress. | R08 |
| RSD-A13 | Another country uses the shared collector/store: Spain identity, UBL/copy rules and representation are selected only for Spain; missing country binding blocks activation. | R09 |
| RSD-A14 | Object is missing or hash mismatch is detected during file read: no corrupted file is served; integrity incident and restore/reconciliation evidence are recorded. | R03/R07 |
| RSD-A15 | For each reused collector, records, file-access or selected DTS capability, record the source build, Spain changes, gaps, owner and qualification evidence. Prove capture/checkpoint recovery, retained-file access and any selected inbound mapping for the actual Spain scope. Missing evidence blocks the dependent capability; France support or a proposed pattern does not prove Spain readiness. | R03–R07/R09; G06/G08 |
| RSD-A16 | A qualified recovery operation may change provider state, and its response is lost after possible transmission: the original connector operation is held for reconciliation. No unsafe repeat, successful freshness claim or checkpoint advance occurs. A repeat requires authoritative evidence or the contract's proven repeat-safety guarantee. | R02–R04; G01/G06 |

### Combined intake and download acceptance

These scenarios define qualification evidence to obtain. They are not executed implementation tests. RRI-Q01–03, RCV-Q01/03/05/09 and RSD-G03/04/06/08 apply to the selected scope.

| ID / scenario | Requirement → activity / interaction / data | Required evidence |
|---|---|---|
| RRI-A01 Private source supplies complete bytes | RRI-R01/02/03 → PRI-01–03, RSD-04/05, RCV-01–07; PRI-INT01/02; RSD-D04/RCV-D01 | Qualified source/file role and one verified capture. No redundant fetch solely because downstream processing is delayed. Same receiving controls and one business delivery apply. |
| RRI-A02 Private notification arrives before the file | RRI-R01–04 → PRI-02–04, RSD-04/05; PRI-INT01–03; PRI-D01/02 | Saved notification is FETCH_PENDING. Query success/event acknowledgement cannot create capture, file availability or completed collection. Qualified fetch supplies the exact file and scoped context before receiving continues. |
| RRI-A03 Fetch expires, times out or returns incomplete bytes | RRI-R01–04 → PRI-03/04, RSD-04, RCV-09; PRI-INT01/03; PRI-D01/02 | Preserve the item and original operation, reason/owner and coverage gap. Resume/refetch only under the qualified recovery/read contract. No synthetic source file or checkpoint skip. Unknown external effects reconcile before unsafe repeat. |
| RRI-A04 Missed, duplicate or reordered private notifications | RRI-R03/04 → PRI-02/04, RCV-01/04/09; PRI-INT01–03; PRI-D01/02, RCV-D04 | Contract-qualified listing/history/replay recovers the gap. Repeat observations reuse item/business identities. No second product invoice or regression from an older observation. Unsupported history remains an owned visible gap. |
| RRI-A05 Customer/accountant downloads the saved file during ERP failure | RRI-R02/06 → RSD-07/09, RCV-07/09; RSD-INT07/RCV-INT-12; RSD-D04/07 | Current authority permits the labelled safe file. Bytes/hash match the saved source. An interrupted transfer records failure and may resume/repeat an authorised stored read under the qualified contract. No external refetch or new business delivery. Product failure, download, internal approval and buyer acceptance remain separate facts. |
| RRI-A06 Source offers only metadata or a derived PDF for a required structured invoice | RRI-R01–03 → PRI-03, RSD-04, RCV-05; PRI-INT01/02; PRI-D01, RCV-D05 | Hold the required source role/profile. A rendering can remain a separately labelled derived artefact; it cannot be renamed as the missing exchanged original or bypass contract/profile qualification. |
| RRI-A07 France reuse candidate selected for Spain | RRI-R03/05/06 → PRI-01, RCV-02–06, RSD-07/09; PRI-D03 | Record source build/contract, Spain changes, gaps, owners and evidence. Spain identity, representation, routing, profile and records rules apply only to Spain. Missing country binding blocks activation. France/Sovos support alone does not pass the gate. |
| RRI-A08 Source authority or accountant grant is revoked | RRI-R03/06; RCV-R15/18 → PRI-01/03, RSD-01/07, RCV-02/09; PRI-D01/RCV-D13 | Stop affected protected source/file actions; preserve prior evidence. Recheck current historical-file access independently. Other independently authorised client receiving continues. New routes do not rewrite saved source context. |
| RRI-A09 Notification receipt and destructive acknowledgement differ | RRI-R02/03/04 → PRI-02–04, RCV-08/09; PRI-INT01/RCV-INT-08; PRI-D01/RCV-D08 | A permitted early event receipt states only durable event intake. An acknowledgement that ends source recoverability requires verified capture or a proven lossless recovery boundary. Lost possible mutations reconcile before unsafe repetition. |
| RRI-A10 Provider, Records or DTS reuse evidence is missing | RRI-R03/05 → PRI-01, RCV-03/05/06, RSD-04/07; PRI-D03/RCV-D12 | Dependent mode/profile remains disabled or held. Record actual contracts, source/output mapping, rule packs, async handling, storage and run owner before activation. Complete source inventory or an outbound mapper cannot establish inbound readiness. |

### Readiness and release evidence

| Gate | Required decision and evidence | Accountable owners |
|---|---|---|
| Design review | RRI-Q01–03 and RCV-Q01–Q05/07–Q10/12/13: source/recipient and original/copy contracts, activation matrix, canonical/product schema, commit/receipt model, acknowledgement safety, recovery permissions, actor/approval policy, accounting handoff and selected implementation assessment. Review RCV-R01–18/RCV-A01–31, RSD-R01–09/RSD-A01–16 and RRI-R01–06/RRI-A01–10. Close the source-binding gates for the selected modes. | Receiving, Architecture, Routing, Security, Identity, Product, Records, DTS and integration owners |
| Pilot | Qualify each selected private/public path and document/profile pair. Exercise cross-tenant denial, malicious/invalid files, mixed-route equivalence/conflict, concurrency, partial commit, lost product receipt, async completion, acknowledgement uncertainty, late arrival and authorised replay. Verify RSD-04–06 capture/checkpoint handoff and PRI-02–04 private capture/coverage and SPEC-SEI-009 factual status handoff. | Integration, Receiving/Product, Security and Operations |
| Production | Resolve RCV-Q06/11; supply retention/hold, restore/export, named support, action runbooks, provider conformance, measured capacity and agreed monitoring/retry/service targets. Record evidence for each reused build and country policy; unresolved capabilities remain disabled or held. | Legal/Privacy/Records, Product, Operations and service owners |

For the accountant/portfolio pilot, close RCV-Q12/13 and exercise all three journeys, current staff/client permissions, eligible approvals, pending review during automatic capture, withdrawal, mixed item results and lost handoff receipts. Qualify the actual reused relationship, approval and connector implementations. Manual approval of every invoice remains an open Product/Compliance decision; internal invoice approval and commercial acceptance are separate purposes.

Monitor separate capture, qualification, business availability, product receipt and acknowledgement times. Alert on incomplete capture, aged quarantine, stale public freshness, delivery backlog, unknown external effects, integrity failures and absent audit evidence. Runbooks identify the original operation, permitted action, owner/escalation path and evidence needed to close the case. RCV-Q11 supplies actual thresholds and retry limits; no new deadlines or SLA are approved here.

The present readiness is **reviewable logical proposal**. The acceptance scenarios specify evidence to obtain; they do not claim that implementation tests have passed. Approved external contracts, country rules, implementation qualification and release evidence remain necessary before activation.

### Public retrieval and records production gates

| ID | Decision/evidence needed | Owner | Effect and required gate |
|---|---|---|---|
| RSD-G01 | GetRegisteredInvoice date discovery, GetInvoices identity/status query and separate downloads are documented. Qualify exact request-per-entity filters, ordering, SECUENCE_ID continuation, history, notifications and read/ack side effects. | Spain Public Platform Technical Owner | Blocks physical adapter design and complete recovery tests. Obtain official AEAT artefacts; SII/VERI*FACTU APIs are not substitutes. |
| RSD-G02 | Accepted certificate contract and registered representation procedure/code, verification, expiry/revocation and action scope. | Compliance, Security and Spain Technical Owner | Blocks live customer retrieval; integrate onboarding/certificates. |
| RSD-G03 | Meaning and measurable target for immediate availability; safe conservation access for failed/unsafe files. | Compliance, Product, Security and Records Owner | Blocks production availability promise. Cannot defer access until ERP success by default. |
| RSD-G04 | Durable storage implementation or approved immutable reference, retention by role/country, holds, historic access, deletion, restore and provider exit. | Records Owner, Legal and Security | Blocks production storage/access. No retention duration invented. |
| RSD-G05 | Exact UBL profile/version, Annex I field binding, copy indicator and public-code encoding. | Format Owner and Spain Technical Owner | Blocks profile activation and exact identity/classification tests. |
| RSD-G06 | Capture/outcome/checkpoint commit protocol, stale-worker protection and crash consistency. | Retrieval, Receiving and Architecture Owners | Blocks implementation baseline until failure tests prove no gaps or duplicate business delivery. |
| RSD-G07 | Fairness, throughput, provider quotas, freshness targets, backlog alerting and recovery limits. | Product, Adapter Owner and Operations | Blocks load/pilot approval; establish targets from customer/provider evidence. |
| RSD-G08 | Reuse assessment and named build/run owners for collector, records, access and DTS-derived processing. | Platform and DTS Owners | Blocks claims of existing implementation readiness; record gaps and local changes. |
| RSD-G09 | Evidence for user multi-file export: customer scenarios, demand, cost and security design. | Product Owner | Blocks adding ZIP/export to scope; does not block automated recovery. |

### Retrieval and file-access operational evidence

Track successful consultation age separately from the age of recovered files and the time until conservation access. Observe per-entity pending pages, capture failures, intake backlog, quarantine age, access denial/failure, integrity incidents and unrepaired gaps. Provider rate limits, support targets and alert thresholds are open in G07; no numeric SLA is asserted.

Operations may request bounded retry, rescan or restore through audited workflows. They cannot edit a checkpoint directly, overwrite original bytes, bypass registered authority, or release an unsafe file through an ordinary product read. Escalation follows the owner named for the affected gate and record.

### SPFE receiving evidence acceptance

These are required evidence scenarios, not executed implementation tests. The source-binding gate is inbound profile and identity qualification; SPFE-Q04/Q06/Q09/Q13/Q14. A source-backed review does not establish that this feature is ready for production.

| ID | Scenario | Required result | Requirement coverage |
|---|---|---|---|
| RCV-SPFE-A01 | A successful public query arrives without downloaded invoice bytes | Update only the evidenced metadata/lifecycle observation; no source-capture, receiving or ERP success is fabricated. | RCV-SPFE-R01; RCV-01–07, RCV-09; [REF](#ref-source-references). |
| RCV-SPFE-A02 | The same invoice is observed again as a copy or with a conflicting profile | Preserve source roles and each observation, enforce trust/profile checks and hold conflicts without rewriting source or double delivery. | RCV-SPFE-R02; RCV-01–07, RCV-09; [REF](#ref-source-references). |
| RCV-SPFE-A03 | Source capture succeeds but mapping or ERP delivery fails | Keep authorized conservation access and retry the existing downstream work without refetching or creating another invoice. | RCV-SPFE-R03; RCV-01–07, RCV-09; [REF](#ref-source-references). |

### SPFE discovery and download evidence acceptance

These are required evidence scenarios, not executed implementation tests. The source-binding gate is RSD-G01/G02/G05/G06; SPFE-Q06/Q09/Q12/Q17. A source-backed review does not establish that this feature is ready for production.

| ID | Scenario | Required result | Requirement coverage |
|---|---|---|---|
| RSD-SPFE-A01 | Issue date differs from SPFE presentation date and the result is paginated | Use presentation-date selection, the exact qualified continuation contract and all-item coverage. Do not guess a filter field or skip page boundaries. | RSD-SPFE-R01; RSD-01, RSD-03–06, RSD-08; [REF](#ref-source-references). |
| RSD-SPFE-A02 | Query success followed by partial ID/locator downloads | Only downloaded, verified items gain capture receipts. No query-only invoice file, borrowed LOC limit or all-success result is fabricated. | RSD-SPFE-R02/RSD-SPFE-R03; RSD-01, RSD-03–06, RSD-08; [REF](#ref-source-references). |
| RSD-SPFE-A03 | A valid locator or submitter certificate lacks the recipient's qualified authority | Hold the affected download and checkpoint; independently authorized entity runs retain their own progress. | RSD-SPFE-R03; RSD-01, RSD-03–06, RSD-08; [REF](#ref-source-references). |

## REF Source references

Use the original files for the claims they establish. Final published regulation governs legal requirements; technical files supply their stated contract facts. Examples are illustrative. Missing or conflicting evidence remains a named gate. Product requirements and Sage design controls have separate authority. The English guide and extracts are reading aids.

REF-BASE entries preserve design provenance. They do not qualify a runtime build. REF-SCOPE records the user’s functional/document direction; it does not approve provider contracts or legal interpretations. REF-PRIVATE records canonical private requirements and discovery limits.

| REF ID | Source and version | Exact location | Supported information and limit |
|---|---|---|---|
| SPFE-S02 | [BOE-A-2026-20587.pdf](<../context/BOE-A-2026-20587.pdf>); final Order HAC/1028/2026; published 5 October 2026. | Articles 3–4, 6 and 9–11; Annex I BT-23/24 | Public invoice/copy scope, public invoice identity, automated recovery, conservation availability and registered third-party access. Apply within the order’s scope. It does not define every wire field, provider contract or another country’s obligations. |
| SPFE-S03 | [CatalogoServicios.pdf](<../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>); 0.1.0; cover 9 October 2026. | sections 6.4–6.7; pp. 12–15 | GetInvoices by identity, GetRegisteredInvoice by presentation-date filter and two download paths. |
| SPFE-S15 | [GetRegisteredInvoice.wsdl](<../context/WSDL servicios web - PRE/20261013/GetRegisteredInvoice.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | GetRegisteredInvoice operation, binding and payload documentation | Exact singular operation name and PRE addresses; generic payload description does not complete the filter contract. |
| SPFE-S14 | [GetInvoices.wsdl](<../context/WSDL servicios web - PRE/20261013/GetInvoices.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | GetInvoices operation and service ports | Identity/status-query transport. |
| SPFE-S12 | [DownloadInvoicesByID.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByID.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | DownloadInvoicesByID operation | Invoice-file download by identity. |
| SPFE-S13 | [DownloadInvoicesByLOC.wsdl](<../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByLOC.wsdl>); Supplied 13 October 2026; SHA-256 in source manifest. | DownloadInvoicesByLOC operation | Locator-based file download. |
| SPFE-S08 | [FormatosEntradaSalida.pdf](<../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>); 0.1.0; cover 9 October 2026; marked BORRADOR. | Section 5.1.1 and response description, pp. 8, 14; sections 5.4–5.7, pp. 14–15 | Supplied UBL 2.5 binding, invoice attachments and response levels. Query/download formats remain pending. This file and inventory completeness do not qualify full field mappings or live conformance. |
| SPFE-S09 | [factura.xml](<../context/Ejemplos/20261013/factura.xml>); Supplied 13 October 2026; SHA-256 in source manifest. | cbc:ProfileID and cbc:CopyIndicator | Original example and profile conflict; no faithful-copy conformance example. |
| REF-BASE-006 | [SPEC-SEI-006-invoice-receiving-solution](./SPEC-SEI-006-invoice-receiving-solution.md); current repository snapshot used 13 October 2026; SHA-256 `c66247ffd2ceef0d7500c3bbb13363f317ebc36b7f49af5e1be871f4286014b6`. | Four parts, RCV/RSD controls and REF source tables. | Receiving design foundation and stable technical IDs. Original retained unchanged. Snapshot includes existing local edits; it is not a claim of a committed or deployed baseline. |
| REF-BASE-010 | [SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received](./SPEC-SEI-010-consult-and-download-ubl-from-public-platform-for-einvoices-received.md); current repository snapshot used 13 October 2026; SHA-256 `1f7d663c98c1406e1ceb73006866d519a3766ea38ef1d5b0fbd4b96fe054ec37`. | Four parts, RCV/RSD controls and REF source tables. | Public retrieval and download design foundation and stable technical IDs. Original retained unchanged. Snapshot includes existing local edits; it is not a claim of a committed or deployed baseline. |
| REF-PRD | [PRD-SEI-211](../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md); [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md); [PRD-SEI-244](../prds/PRD-SEI-244-e-invoicing-process-flow-specification.md); [PRD-SEI-227](../prds/PRD-SEI-227-e-invoicing-as-a-service.md); current repository baselines used 13 October 2026. | PRD211 FR1–55 and Phase 1 scope; PRD223 FR7–11/17–20/22–31/34–35/39/43–44; inbound process and shared-country boundaries. | Canonical product requirements and proposed platform direction. Public Phase 1 still excludes private retrieval. Source-dependent claims need the original SPFE evidence; unresolved scope differences remain Product decisions. |
| REF-PRIVATE | [PRD-SEI-213](../prds/PRD-SEI-213-private-platform-connectivity-structured-review.md); [PRD-SEI-216](../prds/PRD-SEI-216-b2b-router-integration-structured-review.md); current repository baselines used 13 October 2026. | Private connection/capability boundaries; PRD216 FR26–30, Receive invoice journey, source E3/E5/E6 limits and open contract questions. | Canonical private requirements and B2B Router discovery context. This combined draft does not reassert current public API guarantees. Contracted received-file operations, full-file/event semantics, historical coverage and selected interface remain RRI-Q01. No Sovos production contract is supplied. |
| REF-SCOPE | User-supplied stakeholder discussion and task direction, supplied/confirmed in this chat 13 October 2026; discussion’s original date and independent file link unavailable. | Common retrieval outcome across public/private sources; question about downloading B2B Router/Sovos invoices; instruction to create one draft from both predecessors without changing them; clarification that download is included. | Functional and document scope only. Supports RRI-R01/02/06 and the provider/country assessment contexts. No raw chat export is stored; this record does not establish external API support, legal approval or implementation readiness. |
| REF-CONTEXT | [RES-SEI-002](../context/RES-SEI-002-spain-public-platform-technical-evidence.md); [source manifest](../assets/regulatory/spain/spfe/source-manifest.json); [shared glossary](../context/GLO-SEI-001-e-invoicing-terminology.md); current repository aids used 13 October 2026. | Source register, original-file versions and hashes, SPFE-Q04/Q06/Q09/Q12–14/Q17 conflicts, and shared terminology. | Reading and traceability aids. The original files establish only their stated evidence. English guides/text extracts, complete inventory and file hashes do not establish full field mapping, service acceptance or runtime readiness. |
