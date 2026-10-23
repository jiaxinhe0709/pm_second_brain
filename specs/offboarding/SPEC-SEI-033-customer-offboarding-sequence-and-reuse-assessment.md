---
id: SPEC-SEI-033
title: Customer Offboarding Sequence and Reuse Assessment
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-22
updated: 2026-10-22
reviewers: []
related:
  - SPEC-SEI-003
  - SPEC-SEI-031
  - SPEC-SEI-032
  - PRD-SEI-243
  - SPEC-SEI-014
  - SPEC-SEI-016
  - SPEC-SEI-021
  - SPEC-SEI-027
  - SPEC-SEI-030
  - SPEC-SEI-008
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: ""
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# Customer Offboarding Sequence and Reuse Assessment

[Solution Summary](SPEC-SEI-031-customer-offboarding-solution-summary.md) · [Logical Feature Specification](SPEC-SEI-032-customer-offboarding-logical-feature-specification.md) · [Feature folder](README.md)

## Revision overview

This separate draft assesses how the proposed OFF journey in [SPEC-SEI-003](../archive/SPEC-SEI-003-offboarding-solution-specification.md) could use existing APIs and shared capabilities. It adds saved FR disconnection evidence, Spain/provider differences, export dependencies and engineering qualification gates. The predecessor remains unchanged and selected for stable Confluence page `923861391`.

Existing OFF-INT-01–10 and OFF-D01–09 remain proposed logical operations/records in the predecessor. They are not newly approved endpoints or deployment boundaries. Support periods, historical authority, archive terms and production implementation coverage remain open. No new API is designed here.

## 1 Engineering direction and product impact

**Assess the existing connection-update, disconnection, observation, routing, lifecycle and retrieval capabilities before building another exit interface.** A connection DELETE is only one candidate action within OFF-06. A complete exit still needs authority, inventory, destination proof, historical ownership, export and disposition. REF-PRODUCT; INT-AP03.

| Scope | Reuse or change to assess | Effect on integrating products |
|---|---|---|
| Sage private-platform departure | Retain shared OFF gates and qualify the actual Sage connector's address/direction removal. | Present requested versus observed outcome and stop only selected new traffic. Do not label `202` as completed exit. |
| External private-platform departure | Bind each operator's contract, authority, notice, export and observation behaviour. | Show provider-owned/manual steps and blockers. No promise of universal automated removal. |
| Product-only cancellation | Separate product entitlement from platform agreement and historical/archive access. | Establish a usable post-cancellation login/request path and scope. Current implementation unknown. |
| Historical processing | Reuse invoice origin, lifecycle obligations, reports and case recovery. | Permit only confirmed historical operations after cutoff; preserve unselected scope. |
| Export and disposition | Reuse records/retrieval and secure delivery where qualified. | Expose scope, snapshot, omissions, readiness, retrieval and acceptance separately. No evidenced complete offboarding export API is supplied. |
| Public destination or direct recovery | Reuse qualified public access/retrieval where the actor is authorised. | Public technical readiness is not permission to deregister another provider or replace all private records. |

The scope is Spain. Shared gates, case patterns and audit controls are design-reuse candidates. Spain identity, publication, public-copy/reporting and data-policy bindings remain local. Existing implementation coverage is unknown until the selected build, contract and operations pass the gates below. Terms follow the [glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md).

## 2 High-level sequences

These tables describe proposed logical sequences, not an approved allocation to services. Actors and shared capabilities can map to existing components after engineering review. A country/provider boundary represents the relevant rules and external contract.

### 2.1 Planned private-platform departure

| Step | Interaction | Evidence or branch |
|---|---|---|
| 1 | Authorised customer/product → existing case/authority capabilities: request exact scope and terms. | OFF-01/02, R12: authority, dependency inventory and exit statement; no external mutation. |
| 2 | Transition owner → destination operator and routing capabilities: qualify destination and record intended boundary. | OFF-03: observe supported direction, destination and receiving-publication conditions; block if unproved. |
| 3 | Transition owner → shared routing and country/provider action: commit and observe one scoped cutoff. | OFF-04: expected/actual route version and independently observed provider state. Unknown effects enter OFF-08. |
| 4 | Historical owner → original invoice/lifecycle capabilities: finish or hand over earlier work. | OFF-05: original identifiers, due dates, actor/channel and accepted handover. No automatic replay via destination. |
| 5 | Release owner → qualified update/disconnect operation; notification/detail observation confirms result. | OFF-06: choose address, direction or whole-connection action only after dependency checks. INT-AP02/03; address absence alone is insufficient. |
| 6 | Records/customer → qualified export/archive capabilities: validate package and record delivery/disposition. | OFF-07, R13: export can begin earlier. Completion evidence and later schedules are separate from disconnect. |

For external → Sage adoption, the destination steps follow [onboarding SEI021](../onboarding/SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md). The previous operator's release is independently evidenced. Do not create competing route commits in onboarding and offboarding. REF-PRODUCT; SPEC-SEI-014 SPC-04/08.

### 2.2 Unknown disconnection or late provider evidence

| Step | Interaction | Evidence or branch |
|---|---|---|
| 1 | Product/operations receives timeout, `202`, event or incomplete detail. | Keep original action/correlation and selected scope. An event is a prompt to observe, not proof of every exit gate. |
| 2 | Recovery owner → qualified state/detail query or provider support: observe original result. | INT-AP03/05/06 do not supply a universal original-operation reconciliation guarantee. Missing query coverage is GAP-02. |
| 3 | Recovery owner compares intended action with observed addresses/provider records and remaining invoices. | Absent address may follow failed creation as well as removal. Correlate action history and provider evidence. |
| 4 | Recovery owner resumes, conflicts or holds the same transition under evidenced safety rules. | No blind DELETE/recreate, no reset of prior invoice origin and no dependent credential deletion. |

INT-AP06's platform-managed retry horizon and INT-AP05's seven-day error observations are source-specific. Neither defines this feature's support period, retry permission or audit retention. Capture required evidence before a source observation expires. Conflicting guide retry/escalation wording stays unqualified.

### 2.3 Export and historical handover

| Step | Interaction | Evidence or branch |
|---|---|---|
| 1 | Records owner → invoice, lifecycle and exit sources: inventory and authorise a snapshot. | OFF-D03/06/08; distinguish held records, obtainable external evidence and gaps. |
| 2 | Qualified retrieval → original provider/public download where authorised. | Fetch missing allowed files using the actual contract. Preserve source-original versus public-copy classification. SPFE-S02/03/12/13. |
| 3 | Export capability → authorised recipient: deliver validated package/manifest through a scoped channel. | OFF-R13/14; no supplied endpoint establishes this whole operation. GAP-04. |
| 4 | Customer/destination → exit case: acknowledge received version; accept historical obligations separately where applicable. | Download receipt does not prove import, legal authority or operational handover. |
| 5 | Historical processing → Records: supply later deltas and disposition evidence. | Keep ongoing duties and data-class schedules owned after general access ends. OFF-R12/13. |

## 3 Existing API and capability reuse

### 3.1 Saved FR contracts and guide evidence

| Source capability and exact evidenced operation | Reuse assessment and Spain/provider changes | Gap, owner and release evidence |
|---|---|---|
| INT-AP02; `PUT /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/`. Saved FR-05 OpenAPI `1.0.0`. | Candidate for scoped date/address changes. The later guide describes `remove` from API v1.1.0 and usage changes; do not silently add those to the saved schema. Spain address identity and granularity need binding. | GAP-01; FR API and provider owners: pin OpenAPI/build, action enum, usage semantics, dates and partial effects. Test OFF-A20/23. |
| INT-AP03 guide; `DELETE /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}`; response `202` with no success body. | Whole-connection disconnection candidate. Guide sequence includes a trailing slash while the operation card does not. It cannot safely implement partial exit unless the full affected scope is proven. | GAP-01/02; connector owner: actual signature, provider coverage, authority, acknowledgement and recovery. No saved complete DELETE OpenAPI was supplied. |
| INT-AP03/06; `e-invoicing.accesspointconnection.updated`, followed by detail read. | Reuse notification/observation pattern. Guide states no separate offboarding event. Do not create a fictional DEACTIVATED status; removed/expired addresses disappear. | GAP-02; API/Operations owners: event/correlation, duplicate/out-of-order delivery, address-specific outcomes and authoritative external confirmation. |
| FR-04; `GET /connectors/{accessPointId}/datasets/{datasetId}/connections/{connectionId}/`; OpenAPI `1.0.0`. | Candidate for saved connection/address observation; does not alone prove correct legal entity mapping or original action outcome. INT-AP05 has failed-absent-address evidence. | GAP-02/03; API/Identity owners: freshness, history, missing resource semantics, shared scope and source reconciliation. |
| INT-AP06; `GET /datasets/{datasetId}/accesspoints`. | Recover known dataset connector/connection references. Dataset CONNECTED/DISCONNECTED is too coarse to establish selected-address release or complete customer exit. | GAP-03; dataset owner: actual dataset/entity/address cardinality and isolation. Do not assume one dataset always means one entity. |
| Dataset provisioning/deletion, INT-DS01. | Saved guide says external dataset deletion is unavailable and points to support; its prerequisite wording also mentions delete. Treat deletion availability as unresolved. | GAP-03; dataset owner: contract and manual process. Dataset deletion is not a substitute for connection removal, record disposition or mandate withdrawal. |

Keep exact source field names and provider statuses. INT-AP05's upstream error strings must not become Spain errors or public invoice-report states. A supported request can still have partial, unknown or provider-rejected results.

### 3.2 Shared capability and implementation qualification

| Source capability | Retained design / local change | Unknown coverage, owner and evidence gate |
|---|---|---|
| SPEC-SEI-003 OFF-INT-01–03/10, D01–03/09: case, authority and inventory | Reuse scoped request, audit, blockers and original-operation recovery patterns. Bind actual authority and customer access after product cancellation. | GAP-03/05; Identity/Operations/Product owners: existing builds, entitlement/retention behaviour, multi-client isolation and runbook. Design reuse only until demonstrated. |
| SPEC-SEI-014 SPC-04/07/08; OFF-INT-04/05, D04/05: routing | Reuse one route transition and preserved invoice context. Bind Spain receiving publication and each operator's sequence. | GAP-01/06; Routing/provider owners: transaction boundary, concurrency, staged cutoff and external observations. |
| SPEC-SEI-009 and lifecycle SEI030; OFF-INT-06, D06: earlier obligations | Reuse event provenance, independent reporting results and cases. Bind post-switch actor/channel and purpose-limited access. | GAP-05; Legal/Tax, lifecycle and provider owners: authority, actual old-invoice operations, recipient/issuer distinction, duplicates and deadlines. |
| SPEC-SEI-016 and retrieval SEI027; OFF-INT-08, D08: records/download | Reuse authorised stored-file retrieval and preservation patterns. Add exit snapshot, manifest, deltas and post-cancellation access only where missing. | GAP-04; Records/Product owners: original coverage, package completeness, size/resume limits, delivery and accepted custody. Existing full export implementation unknown. |
| SPEC-SEI-008 DTS | Preferred transformation candidate where an additional export syntax or readable representation is required. Preserve source files as separate evidence. | GAP-04; DTS/Records owners: deployed build, accepted contracts, exact mappings, country rule packs, fidelity and operations. No transformation is needed merely to copy unchanged source bytes. |
| Existing security/credential and commercial capabilities; OFF-INT-07, D07 | Reuse independent release, least privilege and shared-dependency checks. Bind scope/entitlement/mandate to actual provider contracts. | GAP-03/05; Security/Commercial/provider owners: post-exit restricted mode, revocation, incident exceptions and contract separation. |

### 3.3 Spain public evidence

SPFE-S02 Articles 9–11 establish recovery/download and access context. The supplied service catalogue and WSDLs establish particular query, download and event operations. They supply no named platform-offboarding or archive-transfer operation. This is a limit of the supplied snapshot, not proof that no later capability exists. OFF-Q04 requires current contract qualification.

| Evidence | Relevance to offboarding | Limit to preserve |
|---|---|---|
| SPFE-S15 `GetRegisteredInvoice`; SPFE-S14 `GetInvoices` | Candidate inventory discovery and identifier consultation under qualified authority. | Metadata consultation does not supply invoice files or a complete private-provider history. Query coverage/checkpoints need proof. |
| SPFE-S12 `DownloadInvoicesByID`; SPFE-S13 `DownloadInvoicesByLOC` | Candidate file acquisition for an authorised evidence package. | Downloaded public original/copy must keep its classification. Batch limits and authorization differ; do not infer a complete exit export from a successful batch. |
| SPFE-S11 `CustomerInvoiceEvents`; SPFE-S17 `SupplierInvoiceEvents` | Candidate continued reporting through an authorised channel. | Contracts do not assign the post-switch actor or grant a new platform authority over old invoices. OFF-Q02 remains open. |
| SPFE-S08 formats and referenced XSDs | Bind the selected public operation's transport/schema when reused. | Formats v0.1.0 is draft with pending sections; header XSDs are not a complete business/exit schema. Existing SPFE conflicts remain gates. |

The detailed public retrieval/reporting contracts stay in their owning feature specs. No new public endpoint, country default or country-neutral copy/reporting rule is introduced by this set.

## 4 Engineering gaps and acceptance evidence

| Gap | Decision/evidence needed | Accountable roles / consequence |
|---|---|---|
| GAP-01 Removal scope and provider sequence | Pin the actual version/build and country/provider contract; qualify address/direction/whole-connection removal, notice, dates, receiving propagation and shared dependencies. | Connector/Routing/provider owners; blocks affected automated cutoff/release. OFF-Q04. |
| GAP-02 Completion and reconciliation | Demonstrate action correlation, state freshness, asynchronous completion, timeouts, absent-address ambiguity, partial effects and retry safety. | API/Operations/provider owners; no `202`-to-complete shortcut. OFF-A05/23. |
| GAP-03 Entity, relationship and post-exit access | Qualify dataset/entity/address mapping, delegate authority, platform versus product contract, independent credentials and actual restricted login/access. | Identity, dataset, Product/Commercial/Security owners; blocks unsupported partial release or historical/export access promise. OFF-A13/20. |
| GAP-04 Export and accepted custody | Demonstrate inventory coverage, exact originals/copies, events/receipts, secure resumable delivery, manifest integrity, delta generation, destination import and data disposition. | Records, retrieval, DTS and destination owners; blocks complete-export or transferred-custody claim. OFF-Q05; OFF-A18/19/25. |
| GAP-05 Earlier duties and time periods | Resolve OFF-Q01/02/03/06 with product terms, legal roles, applicable rights, retention schedules, permitted actors/channels and operational escalation. | Product/Operations/Legal/Tax/Privacy/Security/providers; blocks dependent expiry, credential release or deletion. OFF-A16/17/21/22. |
| GAP-06 Current Spain evidence and isolation | Qualify authoritative receiving change sequence, public access/representation, cross-provider work and applicable effective dates. Keep all local rules out of another country's defaults. | Spain Compliance and platform owners; blocks affected activation. OFF-A10/24. |

For each gap, record a named owner, source/version, tested build/environment, date and accepted result before passing its gate. A missing automated capability can use a controlled manual step only where the contract and authority permit it.

| API qualification check | Required evidence and functional trace |
|---|---|
| Partial disconnect compatibility | Run selected-address/direction removal against the pinned build while another address/entity/direction remains active. Check observations and event payloads. OFF-A12/20/23; GAP-01/03. |
| Unknown effect and duplicate recovery | Simulate timeout after provider acceptance, repeated/out-of-order events and lost internal persistence. Observe the original action; no duplicate removal/recreate or historical resend. OFF-A03/05/14/23; GAP-02. |
| Post-cancellation authorisation | End the product entitlement, exercise permitted historical/export/copy paths, reject new-traffic and revoked-delegate attempts, then revoke only dependencies that have ended. OFF-A13/16/17/20/22; GAP-03/05. |
| Export completeness and handover | Compare source inventory to package/manifest, open all parts, validate relationships/hashes, simulate missed/late records and expired links, and distinguish receipt from accepted obligations. OFF-A18/19/21/25; GAP-04. |
| Country and provider regression | Show that Spain bindings do not change FR address/status meanings or another provider's removal rules. An unqualified provider cannot pass through a shared default. OFF-A10/24; GAP-06. |

These checks are evidence requirements, not executed tests. API documentation alone does not establish availability, conformance, export coverage or production readiness.

## REF Source references

| Source ID | Original source, version/date and exact locator | Supported claims and limits |
|---|---|---|
| REF-PRODUCT | [PRD-SEI-243](../../prds/PRD-SEI-243-customer-offboarding-and-provider-exit.md), draft 5 October 2026, OFR1–15/OD1–8; [SPEC-SEI-003](../archive/SPEC-SEI-003-offboarding-solution-specification.md), updated 8 October, Parts 2–4; [SPEC-SEI-014](../SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md), SPC-04/07/08. | Product scope and proposed interaction/reuse boundaries. Not an approved API. |
| INT-AP02/03/05/06 | [Saved source guide extract](<../../context/FR API/Onboarding/access-point-guides-evidence-extract.md>), received 22 October 2026; Update addresses safely, Remove accesspoint connection, Accesspoint connection updated event, Retention window and Status sections under the matching IDs. | The available saved guide evidence. Original standalone offboarding guide/OpenAPI not supplied. v1.1.0 removal, 0.1.7 disconnect link and 1.10.0 error link are unaligned. |
| FR-04 | [Saved detail OpenAPI](<../../context/FR API/Onboarding/get-accesspoint-connection.md>), `info.version: 1.0.0`; `Get-AccessPoint-Connection`, path and response `accessPointAddresses`. | Exact saved detail contract; deployment/provider support untested. |
| FR-05 | [Saved update OpenAPI](<../../context/FR API/Onboarding/put-accesspoint-connection.md>), `info.version: 1.0.0`; `Put-AccessPoint-Connection`, address-action schema, examples and usage restrictions. | Saved schema differs from later guide claims. Resolve the selected version before implementing removal. |
| INT-DS01 | [Saved dataset guide extract](<../../context/FR API/Onboarding/network-onboarding-create-dataset-guide-extract.md>), received 22 October 2026; What is a dataset?, Ownership and access, Prerequisites / Workflow summary / Steps 1–2, and Review clarification sections. | Dataset deletion availability conflict and unconfirmed cardinality. Does not prove dataset deletion or universal entity mapping. |
| SPFE-S02 | [Original BOE PDF](../../context/BOE-A-2026-20587.pdf), Order HAC/1028/2026, published 5 October 2026; Articles 8–11; [official text](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-20587). | Public report responses, recovery/download and access framework; no private full-exit contract. |
| SPFE-S03 | [Original service catalogue PDF](<../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), v0.1.0, 9 October 2026; sections 6.4–6.9, pp. 12–19. | Specific query/download/event descriptions and limits. No complete export/inventory or original-operation safety guarantee. |
| SPFE-S08 | [Original input/output formats PDF](<../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), v0.1.0, 9 October 2026; sections 4–5. | Draft transport/format evidence. Pending sections and source conflicts remain unresolved. |
| SPFE-S12/13 | [DownloadInvoicesByID.wsdl](<../../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByID.wsdl>) and [DownloadInvoicesByLOC.wsdl](<../../context/WSDL servicios web - PRE/20261013/DownloadInvoicesByLOC.wsdl>), supplied snapshot `20261013`; named operations, bindings and certificate ports. | Exact configured file-download operations, not tested availability or complete archive transfer. |
| SPFE-S14/15 | [GetInvoices.wsdl](<../../context/WSDL servicios web - PRE/20261013/GetInvoices.wsdl>) and [GetRegisteredInvoice.wsdl](<../../context/WSDL servicios web - PRE/20261013/GetRegisteredInvoice.wsdl>), snapshot `20261013`; named operations/bindings. | Consultation operations, not invoice files or universal recipient-directory queries. |
| SPFE-S11/17 | [CustomerInvoiceEvents.wsdl](<../../context/WSDL servicios web - PRE/20261013/CustomerInvoiceEvents.wsdl>) and [SupplierInvoiceEvents.wsdl](<../../context/WSDL servicios web - PRE/20261013/SupplierInvoiceEvents.wsdl>), snapshot `20261013`; named operations/bindings. | Event submission contracts. No post-switch authority allocation. |

The original-file inventory and authority limits remain in [RES-SEI-002](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md). The local examples and English extracts are reading aids, not proof of field-mapping completeness or implementation readiness. Copy-right and privacy sources, with their limits, are in SPEC-SEI-032 REF beside the owning behaviour.
