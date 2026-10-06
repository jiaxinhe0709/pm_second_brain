---
id: SPEC-SEI-010
title: Public Platform Invoice Retrieval, Storage and Download Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-06
reviewers: []
related:
  - GLO-SEI-001
  - PRD-SEI-211
  - PRD-SEI-223
  - PRD-SEI-226
  - PRD-SEI-236
  - SPEC-SEI-001
  - SPEC-SEI-002
  - SPEC-SEI-006
  - SPEC-SEI-009
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610662"
  page_id: "912540298"
  layout: two_left_sidebar
  toc: true
---

# Public Platform Invoice Retrieval, Storage and Download Solution Specification

Terminology follows the [shared e-invoicing glossary](../context/GLO-SEI-001-e-invoicing-terminology.md). Local terms explain this feature; exact technical IDs, fields and source codes keep their stated meanings.

## Part 1 Feature Solution Summary

### Reader guide and design status

This is a **proposed logical design**, ready for review of its boundaries and decisions. Part 1 explains the outcome and scope. Part 2 describes behaviour. Part 3 describes the information and service contracts. Part 4 links requirements to acceptance checks and production gates.

**Confirmed** means supported by the source evidence. **Proposed** means a design choice still needing approval. **Open** means information or a decision is missing. **Out of scope** means excluded from this initial proposal. Service names and record names below are logical responsibilities, not approved deployments or public API endpoints.

### Outcome and authority

Sage should find invoices received through AEAT/SPFE, preserve the exact recovered file, make it available to the authorised customer for conservation, and pass a stable source reference to inbound processing. A later mapping or ERP failure must not lose the source invoice or force public retrieval to start again.

[PRD-SEI-211](../prds/PRD-SEI-211-public-platform-invoice-consultation-structured-review.md), FR1–FR55, is the current product authority. [SPEC-SEI-006](SPEC-SEI-006-inbound-invoice-receiving-solution-specification.md) owns validation, business duplicates, transformation and product distribution after capture. [SPEC-SEI-009](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) owns commercial/payment status interpretation. File access is not an acceptance event.

The [final Order HAC/1028/2026](https://www.boe.es/eli/es/o/2026/10/02/hac1028), Articles 9–11, confirms automated recovery, immediate availability for conservation, consultation/download channels and third-party representation requirements. The [source snapshot and evidence note](../research/spain-public-platform-order-evidence.md) records provenance and limits. The order does not provide the complete new-invoice discovery API or establish UBL 2.5 acceptance.

### Scope and important distinctions

| Capability | Initial proposed scope | Evidence or limit |
|---|---|---|
| Automatic discovery and retrieval | Scheduled collection for every active, authorised public receiving scope; manual refresh joins the same queue. | Required recovery in the applicable operating model; cadence and API mechanics open. |
| Source storage | Exact recovered bytes, identity, classification, hash and source context in durable protected storage. | Physical storage service and retention values open. An external immutable reference is acceptable only after its access, integrity, retention and exit guarantees are approved. |
| Customer conservation access | Authorised download of a stored structured invoice or faithful copy, clearly labelled. | Available independently of mapping/ERP completion; unsafe content follows a separately approved controlled access path. |
| Multiple recovered invoices | Collect multiple results safely over successive requests/pages. | Automated collection is distinct from a user export feature. |
| Single call across customers | Open; no dependency on such an operation. | AEAT must confirm whether this exists. Each represented entity keeps separate authority and progress. |
| Multi-file ZIP/export | Out of scope for the initial proposal. | Product must validate demand and cost. France coverage and expected Spanish usage are unverified stakeholder inputs. |
| Rendering or canonical representation | Optional derived artefacts linked to their generator/version. | No derived file is labelled as the recovered original. |
| Business processing and lifecycle reporting | Delegated to SPEC-SEI-006 and SPEC-SEI-009. | Download does not imply technical validation, ERP delivery, commercial acceptance or payment. |

**Conservation** means keeping invoices available for the required records period. **Durable** means saved so the information survives a process restart or worker failure. A **canonical representation** is a shared internal format used for processing; it does not replace the source file. A **faithful copy** is the public UBL copy of an invoice exchanged through another route. Preserve its retrieved bytes as a source artefact with role `PUBLIC_COPY`; do not call it the original invoice from the private route. A **checkpoint** is saved retrieval progress. A **quarantine** is restricted storage for a file requiring investigation. A **lease** gives one worker temporary authority to handle a scope; a replacement worker must reject the old worker's commits.

### Spain use and reuse boundaries

Reuse labels follow the [shared e-invoicing glossary](../context/GLO-SEI-001-e-invoicing-terminology.md#reuse-vocabulary). **Reusable unchanged** describes a design pattern; **Unknown** records unverified implementation fitness. Scope exclusions are marked **Out of scope**.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Queue fairness, resumable progress, durable capture, access audit | Support reliable public retrieval and downloads. | Reusable unchanged; proposed design pattern | Actual shared implementation coverage is unknown. Platform Owner must demonstrate contracts, isolation, failure behaviour and operational readiness. |
| Stored-file roles, hashing, conservation access | Keep recovered UBL distinct from copies and derived files. | Reusable with country binding | Records/Security Owners must bind retention, authority, safe-file rules and deletion policy to each country. |
| AEAT adapter and registered representation | Retrieve for the correct represented Spanish entity. | Country-specific | Spain Technical Owner and Compliance must supply the exact API and power-of-attorney procedure. |
| Public invoice code, copy indicator and UBL profile | Preserve Spanish identity and public-source classification. | Country-specific | Format Owner must bind final annexes to the published technical schema. No default for other countries. |
| DTS transformation/validation | Produce or validate a derived representation where required by receiving. | Unknown; existing implementation reuse candidate | DTS Owner must prove the exact inbound profile and lossless mapping. DTS temporary staging is not the permanent invoice archive. |
| France collection or download implementation | Possible source of platform patterns. | Unknown | Record capability, required local changes, gaps, owner and test evidence before activation. Do not infer Spain availability from France. |

### Actors and responsibility

Customer/product initiates a refresh or file read. Retrieval Owner owns eligibility, scheduling, provider calls and progress. Records Owner owns durable file capture, integrity, retention and retrieval after route changes. Receiving Owner owns classification and downstream processing. Security owns file-access enforcement and unsafe-file handling. Compliance owns legal representation, conservation duties and applicability. Operations owns bounded recovery and incident evidence. Named individuals and support targets remain open.

### Process and continuity

![Public consultation and reconciliation](../assets/diagrams/e-invoicing-public-consultation-reconciliation.svg)

[Editable Draw.io](../assets/diagrams/e-invoicing-public-consultation-reconciliation.drawio) · [PNG preview](../assets/diagrams/e-invoicing-public-consultation-reconciliation.png). This existing process diagram is reused. Its “check scope”, “schedule and lease”, “query”, “classify and persist”, “boundary durable” and “commit progress” steps map to RSD-01, RSD-02, RSD-03, RSD-04/05 and RSD-06 below. “Publish availability” separates conservation file access from the later business-invoice view. Download activity RSD-07 reads saved files without starting another public query.

The proposed sequence is: check scope → collect a bounded page → recover and save each source → record each item's durable outcome → commit covered progress. Customer file access becomes possible after safe durable capture. Receiving and ERP delivery continue independently. An incomplete page resumes from saved evidence; it never resets progress to the current time.

## Part 2 Logical Feature Specification

### Activity lifecycle

All activities use the tenant, represented legal entity, country, environment, route/version and correlation context. Missing authority blocks new public calls. Stored-file reads have their own records entitlement; onboarding suspension does not automatically settle historical access rights.

| ID / trigger and actor | Preconditions and decision inputs | Operation and postcondition | Error and recovery owner |
|---|---|---|---|
| RSD-01 Check eligibility / scheduler, refresh or recovery request | Active inbound public scope; accepted credential reference; registered authority for entity/action; effective policy. | Record eligible scope and policy version, or hold it with an actionable reason. Recheck before calls and commit if scope changed. | Retrieval/Authority Owners: expired credentials, absent/revoked authority or suspension hold new calls; preserve history and checkpoint. |
| RSD-02 Schedule / eligible due scope | RSD-01 passes; provider/tenant capacity available; no current effective lease. | Coalesce triggers; take a lease with a generation number; save run ID, trigger, bounds and policy. Fair scheduling prevents one backlog taking all capacity. | Retrieval/Operations: busy scope returns current operation; worker loss permits takeover after lease expiry; stale generation cannot commit. |
| RSD-03 Discover and fetch / worker with current lease | Confirmed adapter contract and authority; saved checkpoint or approved initial bounds. | Query a bounded page/window; save provider correlation and continuation evidence. Fetch exact files if discovery and file recovery are separate. No result is distinct from failure. | Adapter Owner: throttle/backoff per contract; invalid cursor opens bounded gap recovery; uncertain provider-side read/ack effect requires reconciliation before repeat. |
| RSD-04 Capture source / each recovered item | Scope matches expected entity/environment; size/type policy; source identity and available classification. | Persist exact bytes or approved immutable reference, hash, file role, media/profile, source and retrieval time. Publish a recoverable capture receipt only after file and metadata agree. Safe source can become available for conservation before business processing. | Records/Security: partial write, mismatch or unsafe content cannot become an ordinary downloadable file. Preserve restricted evidence and retry from saved item identity; do not advance past missing capture. |
| RSD-05 Register durable outcome / captured item | RSD-04 receipt; stable observation key/hash; intake service available or durable handoff intent. | Save intake receipt/classification or an owned pending handoff. Receiving returns ingested, duplicate, approved ignored or quarantined outcome. A pending handoff is retriable but is not a completed page classification. | Receiving/Records: same key/hash returns prior receipt; changed content or ambiguous original/copy relation enters quarantine. A mapping/ERP error after durable classification does not undo capture. |
| RSD-06 Commit covered progress / completed boundary | Current lease generation; every covered item has saved source and durable classification, or approved ignore evidence; no unresolved hole. | Atomically or through a proven recoverable protocol commit page/item outcome coverage and checkpoint. Save successful consultation time. ERP delivery acknowledgement is not a checkpoint condition. | Retrieval Owner: a crash before/after commit replays saved receipts; stale worker commit rejected; incomplete page retains prior committed boundary. |
| RSD-07 Read stored file / customer, authorised ERP or operator | Current subject/action entitlement; invoice and file role match scope; retention and safe-access policy permit read. | Return the selected labelled file with safe content handling; audit actor, role, purpose, result and correlation. A download attempt is not proof that the customer conserved the file. | Access/Records Owners: deny unauthorised or unsafe ordinary read; missing/hash-mismatched file opens integrity incident. Controlled quarantine export requires approved elevated policy and audit. |
| RSD-08 Reconcile gaps / authorised operations or recovery policy | Bounded entity/time scope; authority; separate recovery progress; approved limits. | Re-scan via RSD-03–06, reuse capture/intake identities, compare coverage and record resolved/remaining gaps. Preserve routine checkpoint. | Operations/Adapter: data outside provider retention requires an explicit recovery case and customer impact assessment; never silently report completeness. |
| RSD-09 Retain, transfer or delete / records policy event | Versioned policy, retention basis, applicable hold, ownership and approved action. | Preserve historical downloads through route/provider changes when entitled. Verify export before exit; record deletion evidence only when allowed. | Records/Compliance: hold blocks deletion; incomplete export blocks disposal; restoration and integrity failures open a records incident. |

### Invariants and state separation

- A retrieved file has a source-observation identity; a business invoice has its own receiving identity. Two routes or two polls can observe the same business invoice. Capture must not cause another business invoice or ERP delivery.
- Provider identity and issuer NIF/series/number/issue date are preserved. The exact public-code encoding is an API/profile gate, not an invented string concatenation rule in Sage.
- Every page item has an explicit saved outcome. Approved ignore rules require policy version and reason. Quarantine is a durable outcome only when source/evidence, owner and recovery action are preserved.
- `DISCOVERED`, `CAPTURED`, `QUARANTINED`, `CLASSIFIED` and `PROGRESS_COMMITTED` are proposed retrieval states. `CONSERVATION_ACCESSIBLE` is a separate access property; `BUSINESS_AVAILABLE` and `ERP_DELIVERED` belong to receiving. Their timestamps and failure reasons remain distinct.
- A faithful copy stays `PUBLIC_COPY`. If the private-route original later arrives, receiving decides the business link; neither artefact is overwritten. Unknown classification remains restricted pending evidence.
- XML parsing disables external entity/network resolution. Resource limits, file name/header handling and safe XML serving are required controls; exact limits and implementation need Security approval.
- Changing a credential, route, mapper or country policy does not rewrite the saved source or historical evidence. New attempts record the newly selected policy/version.
- A download is a read. Whether AEAT recovery also changes provider state is open. If a call has a possible mutation, save intent and reconcile the authoritative result before an unsafe repeat.

### Requirements and failure handling

| ID | Observable requirement | Source |
|---|---|---|
| RSD-R01 | Automated retrieval checks entity/action authority separately from valid transport credentials. | PRD211 FR1–6, FR54; order Article 11. |
| RSD-R02 | Scheduled baseline and coalesced refresh use bounded, fair, resumable work with stale-worker protection. | FR7–20. |
| RSD-R03 | Exact recovered source and context are durable before advancing progress; original/copy/derived roles remain explicit. | FR21–28, FR43–46. |
| RSD-R04 | Every committed boundary has durable item classification and recoverable coverage evidence. | FR17–18, FR23, FR36–38. |
| RSD-R05 | Safe source-file conservation access remains independent of ERP success; download enforces current authority and records audit. | FR47–53; order Article 9. |
| RSD-R06 | Business identity, quarantined conflicts and failed downstream delivery reuse receiving contracts. | FR24–29, FR49–50. |
| RSD-R07 | Retention, holds, restore, exit and deletion are bound to artefact role and country; suspension does not erase historical source evidence. | FR5, FR51–52. |
| RSD-R08 | Automated multi-invoice collection works without a ZIP/export; aggregated provider scopes are enabled only with confirmed support and separate entity authority. | FR55. |
| RSD-R09 | Spain-specific identity, profile, representation and public routing cannot become another country's defaults. | Reuse boundaries; PRD-SEI-226/236. |

| Failure | Required saved outcome and safe action |
|---|---|
| Public API timeout, throttle or unavailability | Run failure class and provider correlation; bounded backoff. No fabricated empty result or freshness success. |
| File recovered but storage failed | Item remains incomplete; retry capture or refetch under confirmed read semantics. Prior checkpoint remains. |
| Metadata saved but object absent, or orphan object | Recover using capture identity/hash and incomplete receipt; object is not downloadable until verified. Records Owner reconciles/cleans orphans under policy. |
| Receiving service unavailable | Durable pending handoff; retry without refetching source. Do not claim final item classification or completed page. |
| Unsafe or malformed file | Restricted quarantine; owned investigation and approved conservation-access procedure. Do not execute or display raw content in the product. |
| Changed bytes under the same identity | Preserve both observations and restrict conflicting files. Receiving/Records reconcile; no silent overwrite. |
| Worker crashes around progress commit | Resume from saved item outcomes and lease generation; reconcile commit result, avoiding lost coverage. |
| Route switched or authority revoked during run | Stop further public calls; re-evaluate any commit against saved scope version. Preserve captured evidence and use approved historical access rights. |
| Product distribution fails | SPEC-SEI-006 retries its existing distribution identity. Retrieval/source file remains available under its policy. |
| Expired provider history or storage loss | Records/Operations recovery case; restore/reconcile against trustworthy evidence where available. Mark the gap until proved repaired. |

## Part 3 Logical Service Interactions and Data Inventory

### Contracts

These are proposed logical contracts. Physical endpoints, payload schemas, transaction boundaries and service ownership require architecture review. Each result carries scope, correlation, version and safe outcome/error categories. Credentials remain protected references, never request logs.

| ID / direction | Request and result | Activity |
|---|---|---|
| RSD-INT01 Product/Operations → Retrieval | Refresh/recovery scope and actor; returns saved current freshness plus stable queued operation or actionable denial. No synchronous AEAT dependency. | RSD-01/02/08 |
| RSD-INT02 Retrieval → Authority/Credentials | Entity/action/environment, credential and authority references; returns effective eligibility/version. Provider representation is separate from local subscription. | RSD-01/03/06 |
| RSD-INT03 Retrieval → AEAT adapter | Explicit represented scope, bounds and continuation evidence; returns discovery items/files and provider correlation or classified failure. Exact contract open. | RSD-03/08 |
| RSD-INT04 Retrieval → Records | Capture identity, exact bytes or approved reference, classification and context; returns durable verified receipt or incomplete capture. | RSD-04 |
| RSD-INT05 Retrieval → Receiving | Durable source reference/hash, observation and public-route/page context; returns stable intake receipt and durable classification, or pending/error. | RSD-05/06 |
| RSD-INT06 Worker → Progress store | Lease generation, scope version and complete item-outcome coverage; returns committed boundary or conflict. Idempotent commit/recovery required. | RSD-06 |
| RSD-INT07 Product/ERP → File access → Records | Actor, invoice, entity, artefact role and purpose; returns authorised labelled bytes or safe denial. If temporary access links are chosen, restrict scope/expiry and redact bearer values. | RSD-07 |
| RSD-INT08 Records → Audit/Operations | Capture, access, gap, integrity, export and deletion outcomes with evidence references; durable/auditable notification and recovery ownership. | RSD-04/07/08/09 |

### Data and ownership

All invoice and identity data is sensitive. Audit uses identifiers/references rather than full invoice bodies. Encryption, least privilege, environment separation and approved storage locations apply. No customer invoice files belong in this repository.

| ID / record and system of record | Minimum logical information | Policy / consumer |
|---|---|---|
| RSD-D01 Eligibility / Authority service | Tenant, entity, country, environment, route/version, actions, registered-authority reference/status, credential reference and effective period. | Restricted; authority retention/revocation policy. RSD-01/03/06. |
| RSD-D02 Run / Retrieval | Run/operation ID, trigger/actor, scope, lease generation/expiry, bounds, provider correlation, attempts and safe failure class. | Operational retention open. RSD-02/03/08. |
| RSD-D03 Coverage/checkpoint / Retrieval | Committed bounds/continuation evidence, page identity, item-outcome references, scope/policy version, last successful query and recovery gap state. | Never silently overwritten by rescan. RSD-03/06/08. |
| RSD-D04 Source artefact / Records | Immutable object/reference, capture ID, hash algorithm/value, bytes/size, media type, source and retrieval time, public identity, invoice components, role/copy indicator, profile and integrity evidence. | Sensitive immutable source; approved role/country retention and holds. RSD-04/05/07/09. |
| RSD-D05 Observation/intake link / Receiving with Retrieval reference | Observation key/hash, artefact ID, page/item identity, intake receipt, business link if known, durable classification, rule version and quarantine owner. | Receiving owns business deduplication; Retrieval owns coverage. RSD-05/06/08. |
| RSD-D06 Derived artefact / Receiving or rendering owner | Source link, canonical/rendered role, generator/mapping/profile version, hash and creation time. | Separate retention and access; cannot replace D04. RSD-07/09. |
| RSD-D07 File access audit / Audit | Actor, represented entity, invoice/artefact role, purpose, time, policy version, correlation and allowed/denied/read outcome. | No credentials, bearer links or raw invoice bodies. RSD-07. |
| RSD-D08 Recovery/records case / Operations and Records | Gap/integrity evidence, affected scope, hold/retention/export decision, owner, permitted actions and resolution references. | Preserve until approved resolution and retention action. RSD-08/09. |

### Spain and reuse boundary in contracts

Shared contracts carry country and environment explicitly. Adapter policy supplies AEAT representation, public identity encoding, copy classification, schema and recovery semantics. Records policy supplies country/role retention and historical-access rules. An aggregate query, if confirmed later, must return entity-bound results; ambiguous entity attribution is quarantined rather than distributed.

Qualify reused implementations with a record of existing capability, Spain changes, missing controls, accountable owner and acceptance evidence. DTS is a candidate for derived-file transformation/validation only; its staging lifetime must not define invoice conservation. Physical storage, file streaming versus protected links, and cross-service commit protocols remain open decisions.

## Part 4 Assurance and Traceability View

### Acceptance scenarios

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

### Open decisions and production gates

| ID | Decision/evidence needed | Owner | Effect and required gate |
|---|---|---|---|
| RSD-G01 | New-invoice discovery, request-per-entity or aggregation, filters, ordering, pagination, notification capability, identifiers, history and read/ack side effects. | Spain Public Platform Technical Owner | Blocks physical adapter design and complete recovery tests. Obtain official AEAT artefacts; SII/VERI*FACTU APIs are not substitutes. |
| RSD-G02 | Accepted certificate contract and registered representation procedure/code, verification, expiry/revocation and action scope. | Compliance, Security and Spain Technical Owner | Blocks live customer retrieval; integrate onboarding/certificates. |
| RSD-G03 | Meaning and measurable target for immediate availability; safe conservation access for failed/unsafe files. | Compliance, Product, Security and Records Owner | Blocks production availability promise. Cannot defer access until ERP success by default. |
| RSD-G04 | Durable storage implementation or approved immutable reference, retention by role/country, holds, historic access, deletion, restore and provider exit. | Records Owner, Legal and Security | Blocks production storage/access. No retention duration invented. |
| RSD-G05 | Exact UBL profile/version, Annex I field binding, copy indicator and public-code encoding. | Format Owner and Spain Technical Owner | Blocks profile activation and exact identity/classification tests. |
| RSD-G06 | Capture/outcome/checkpoint commit protocol, stale-worker protection and crash consistency. | Retrieval, Receiving and Architecture Owners | Blocks implementation baseline until failure tests prove no gaps or duplicate business delivery. |
| RSD-G07 | Fairness, throughput, provider quotas, freshness targets, backlog alerting and recovery limits. | Product, Adapter Owner and Operations | Blocks load/pilot approval; establish targets from customer/provider evidence. |
| RSD-G08 | Reuse assessment and named build/run owners for collector, records, access and DTS-derived processing. | Platform and DTS Owners | Blocks claims of existing implementation readiness; record gaps and local changes. |
| RSD-G09 | Evidence for user multi-file export: customer scenarios, demand, cost and security design. | Product Owner | Blocks adding ZIP/export to scope; does not block automated recovery. |

### Operational evidence and readiness

Track successful consultation age separately from the age of recovered files and the time until conservation access. Observe per-entity pending pages, capture failures, intake backlog, quarantine age, access denial/failure, integrity incidents and unrepaired gaps. Provider rate limits, support targets and alert thresholds are open in G07; no numeric SLA is asserted.

Operations may request bounded retry, rescan or restore through audited workflows. They cannot edit a checkpoint directly, overwrite original bytes, bypass registered authority, or release an unsafe file through an ordinary product read. Escalation follows the owner named for the affected gate and record.

**Readiness:** reviewable logical proposal with the final-order evidence incorporated. Physical adapter contracts, records policy, measurable conservation-access target and reuse evidence remain production gates. Intended future Confluence location is a child of **Public Platform - Invoice Consultation and Retrieval** (page `837610662`), with links from the UBL Download and inbound-receiving topics. Publication is authorised for this single draft pilot page. The other solution specs remain unpublished pending validation of this page.
