---
id: PRD-SEI-104
title: Phase 1 — Accountant and Single-Client Onboarding
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-25
updated: 2026-09-22
reviewers: []
related:
  - PRD-SEI-101
  - PRD-SEI-106
  - PRD-SEI-107
  - PRD-SEI-211
  - PRD-SEI-212
  - PRD-SEI-226
  - PRD-SEI-231
  - PRD-SEI-223
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610648"
  page_id: "848078252"
  title: "Accountant & Single Client"
  layout: two_left_sidebar
  toc: true
---

# Phase 1 — Accountant and Single-Client Onboarding

## Decision summary

Direct-customer and accountant-portfolio onboarding are two intake and orchestration modes for the same client-level controls. Every client must have an independently verified Sage access relationship, legal subject, identifier, requested capability, authority decision, environment and evidence set.

A firm API credential, accountant role, certificate or portfolio relationship authenticates or authorises access only within its approved product purpose. It does not prove that the accountant may submit, receive, consult, reject or report payment for every client. Those operations require separate, effective authority decisions under the eventual Spanish public-solution representation contract.

The same separation applies to invoice signing. An accountant may configure a client's onboarding, but may sign only where effective evidence authorises that accountant/delegate for the named client, capability, route and period. Customer-held, accountant-held, Sage-managed and provider-held signing are custody/operation modes—not shortcuts to authority—and a Sage operator seal is a different legal/technical act.

Batch acceptance proves durable receipt, not client readiness. One client failure must not fail, change or disclose another client.

> **Product principle:** Scale the orchestration, never the authority assumption.

This document owns the persona, portfolio, batch and client-isolation detail under [PRD-SEI-101](PRD-SEI-101-public-platform-onboarding.md). It does not own NIF lookup semantics, generic retry policy, invoice submission or invoice retrieval.

## Source relationship

This is the canonical Git source proposed for existing Confluence page [Accountant & Single Client](https://confluence.sage.com/spaces/DNBU/pages/848078252/Accountant+Single+Client), reviewed at version 3. It preserves the original direct/batch split and multi-tenant isolation while replacing the unsupported master-certificate and forced `SENDING_ONLY` rules with evidence-gated capability decisions.

### Original draft detail disposition

| Original detail | Treatment in this canonical source |
|---|---|
| `POST /api/v1/es/onboarding/profile` | Preserved as a proposed direct-create capability; URL/REST design is not approved |
| `POST /api/v1/es/onboarding/batch`, HTTP `202`, `batch_id` and status link | Preserved as durable asynchronous receipt behaviour; exact transport/status/link shape remains architecture-owned |
| Batch-level `accountant_firm_id` | Preserved as firm context, with current firm/user/client relationship rechecked per protected item operation |
| Batch-level `representation_type` | Replaced by per-client/per-capability authority decisions; source type remains evidence metadata |
| Batch-level `master_certificate_id` | Replaced by protected credential references applied only where official scope proves each client/capability |
| `client_nif`, `entity_type`, `role`, `effective_date` | Preserved through typed legal-subject/identifier, capability-direction and effective-time records |
| `allow_invoice_level_override` | Deferred to approved route/applicability policy; onboarding must not invent invoice routing overrides |
| “Push every NIF to AEAT via master cert” | Replaced by approved-check orchestration; no external operation/certificate is assumed |
| Forced `SENDING_ONLY` without apoderamiento | Removed as unsupported SPFE enforcement; asymmetric results remain a required capability decision |
| Example identifiers | Not reused as positive fixtures because their checksum validity was not established |

## Outcome and boundaries

| Actor/pathway | Phase 1 outcome | Not implied |
|---|---|---|
| Direct business/autónomo | One legal subject receives per-capability onboarding results | All future invoices are in scope or compliant |
| Accountant onboarding one client | Same controls under a delegated user/context | Firm membership proves statutory authority |
| Accountant portfolio | Durable batch plus isolated client work items and results | Batch-level authority or all-or-nothing rollback |
| Operations/support | Redacted aggregate and client-scoped evidence/recovery actions | Broad access to every client in a firm |

### In scope

- Direct and accountant intake differences.
- Firm/user/workspace/client relationship validation.
- Portfolio batch receipt, decomposition, scheduling, status and cancellation.
- Per-client, per-capability authority evaluation.
- Partial success, duplicate submission, correction and resumption.
- Client isolation, data minimisation, audit and safe operational recovery.

### Out of scope

- Defining the final Spanish legal mechanism for every delegated operation.
- Assuming `Colaborador Social`, generic apoderamiento or one certificate covers SPFE operations.
- Defining certificate/key custody, expiry, rotation, revocation, compromise or destruction, owned by PRD-SEI-226.
- NIF validation/AEAT census semantics, owned by PRD-SEI-106.
- Generic retry/reconciliation algorithms, owned by PRD-SEI-107 and PRD-SEI-215.
- Sending, retrieving or reporting an invoice, owned by PRD-SEI-211/212/224.

## Concepts that must remain separate

| Concept | Meaning | Does not prove |
|---|---|---|
| Firm authentication | Identity of the accountant organisation/system accessing Sage | Permission for a named client or statutory operation |
| User product role | Sage actions a firm user may request | Authority accepted by AEAT/public solution |
| Client relationship | Firm is linked to a Sage client/workspace | Submission, receipt or consultation mandate |
| Delegated authority | Effective evidence for principal, delegate and operation | Credential custody or route readiness |
| Credential reference | Protected means used to authenticate/sign where required | The legal scope of representation |
| Signing authority | Effective permission for a named natural person/delegate to sign for a named client and purpose | Firm membership, certificate possession or permission to manage onboarding |
| Signing custody mode | Customer, accountant, Sage remote-signing service or provider boundary that controls the signing operation/key | The legal signer, represented principal or authority grant |
| Sage-managed signing | Sage invokes protected signing for the explicitly represented customer/delegate | A Sage workload certificate or Sage becoming the invoice issuer |
| Sage operator seal | Electronic seal whose creator is the named Sage legal person/operator | A customer's or accountant's delegated signature |
| Batch | Envelope grouping several client requests | Shared client state, transaction or grant |
| Batch receipt | Durable acceptance for processing | Validation, authorisation or readiness success |
| Capability readiness | Client-specific decision for a named operation | Readiness for any other operation |

## Pathway comparison

| Capability | Direct/single-client pathway | Accountant portfolio pathway | Shared control |
|---|---|---|---|
| Intake | One case/request | Batch receipt and client items | Idempotent logical command |
| Immediate feedback | Envelope and local structural findings | Envelope/count/duplicate findings | No external success is implied |
| Processing | May complete synchronously only when all checks are local | Asynchronous per-client workers | Same policy and evidence contract |
| Access context | Customer workspace/user | Firm user plus client workspace relationship | Tenant/client isolation |
| Authority | Direct actor or delegated actor | Evaluated for every client/capability | No batch-level universal grant |
| Credentials | Client/approved custodian reference if required | Client-scoped or reusable reference only where official scope proves it | Separate from authority |
| Signing | Customer/direct signer or approved delegate | Evaluated per client, signer/delegate and capability; may use a protected Sage/provider service | No firm-wide master signer/certificate |
| Result | Per capability | Aggregate counts plus authorised item detail | Stable redacted reasons |
| Correction | Update/resume case | Update/resume selected items | Prior evidence retained |
| Cancellation | Cancel safe pending work | Cancel selected items or remaining batch | Unknown outcomes reconciled |

## Capability authority matrix

The matrix is a required decision surface; legal evidence and mechanisms remain open until the public-solution technical order is available.

| Capability | Product permission | Client relationship | Statutory/official authority | Credential | Decision |
|---|---|---|---|---|---|
| Manage onboarding facts | Required | Required for delegate | Contract/privacy approval as applicable | Sage authentication | May configure facts only |
| Submit invoice | Required | Required | Operation-specific evidence required | Official mechanism pending | Independent readiness |
| Receive/download invoice | Required | Required | Operation-specific evidence required | Official mechanism pending | Independent readiness |
| Consult issued invoice/status | Required | Required | Operation-specific evidence required | Official mechanism pending | Independent readiness |
| Consult received invoice/status | Required | Required | Operation-specific evidence required | Official mechanism pending | Independent readiness |
| Communicate rejection | Required | Required | Recipient-side authority required | Official mechanism pending | Independent readiness |
| Communicate payment | Required | Required | Recipient-side authority required | Official mechanism pending | Independent readiness |
| View compliance evidence | Required | Required | Purpose/access policy required | Sage authentication | Redacted and audited |
| Manage credential reference | Elevated permission | Required | Custody/administration approval | Strong authentication | Never grants other capabilities |

## Business scenarios

| ID | Scenario | Expected outcome | Isolation/exception |
|---|---|---|---|
| S1 | Business owner onboards one workspace | Direct case uses common controls and returns per-capability readiness | No accountant context is created |
| S2 | Accountant onboards one linked client | Client case records delegate and evaluates requested capabilities | Relationship alone does not make authority effective |
| S3 | Accountant submits 500 client requests | Batch is durably accepted and decomposed; capacity/rate policy schedules items | No claim that AEAT will time out at a specific count |
| S4 | Batch includes one unlinked client | That item is denied with a non-enumerating result | Other authorised items continue |
| S5 | Authority covers submission but retrieval evidence is absent | Submission and retrieval receive distinct outcomes | Do not force a universal persona role |
| S6 | Authority is revoked during a batch | Not-yet-executed affected items stop; completed evidence remains | Other clients/capabilities continue if safe |
| S7 | Same batch is resubmitted | Existing logical batch/result is returned | No duplicate client work/external call |
| S8 | Two users change the same client concurrently | Version/conflict control preserves one authoritative revision | No last-write-wins authority change |
| S9 | Accountant loses client relationship | Future reads/changes are denied; retention and client continuity remain governed | Firm cannot continue polling status |
| S10 | Customer corrects identity or mandate evidence | New revision is validated and resumed | Previous decision remains auditable |
| S11 | Accountant selects one certificate/reference for several clients | Each client is evaluated against the certificate subject, signer/delegate authority, purpose and validity | No batch-wide signing authority is inferred |
| S12 | Sage-managed signing is offered to an accountant | The client principal, authorised accountant/delegate, Sage service role and custody boundary remain separately evidenced | A Sage service identity is not labelled as the client signer |

## Business rules

| ID | Condition | Rule | Status/evidence |
|---|---|---|---|
| BR1 | Direct or accountant intake | Apply the same identity, authority and readiness policies | Accepted product model |
| BR2 | Batch envelope is valid | Acknowledge durable receipt only; do not return `READY` for unprocessed items | Proposed |
| BR3 | Delegate acts | Bind principal, client, capability, direction, environment, validity and evidence | PRD-SEI-231 |
| BR4 | Credential authenticates | Treat authentication separately from BR3 | Confirmed design principle |
| BR5 | Reusable authority/credential evidence is referenced | Re-evaluate whether its official scope includes every named client and capability | Proposed; legal contract open |
| BR6 | One item fails | Continue independent safe items and return a redacted item outcome | Proposed |
| BR7 | Caller cannot access a client | Do not reveal client existence, identifiers, state or failure detail | Security requirement |
| BR8 | Capability authority differs | Preserve asymmetric results; never coerce them into one role flag | Proposed |
| BR9 | Item changes after readiness | Create a new effective revision; do not rewrite historical evidence | PRD-SEI-101/231 |
| BR10 | External outcome is unknown | Reconcile before retry, success or cancellation completion | PRD-SEI-107/215 |
| BR11 | Accountant configures certificate readiness | Permit configuration only within product/client permission; evaluate signing authority separately | PRD-SEI-101/226 |
| BR12 | A credential/reference is reused across clients | Prove subject, purpose and authority scope independently for every client/capability | No master-certificate inference |
| BR13 | Sage manages the signing operation | Preserve the represented client, actual authorised signer/delegate, service role, trust-material version and authority snapshot | PRD-SEI-226 |
| BR14 | Sage operator seal is available | Do not present it as the client's or accountant's signature or use it as a substitute without explicit Legal approval for that route/policy | Evidence gate |

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238), Article 11.4–11.5 | Authorised intermediaries may act through the public solution under identification/authentication/representation mechanisms set by ministerial order | Primary law; detailed mechanism not yet evidenced in this review | Do not approve a certificate/grant model yet |
| [AEAT apoderamientos overview](https://sede.agenciatributaria.gob.es/Sede/colaborar-agencia-tributaria/registro-apoderamientos.html) | AEAT supports powers scoped to enabled procedures | Official general service; does not prove SPFE operation coverage | Authority record must preserve procedure/capability scope |
| Confluence page 848078252 v3 | Proposed sync direct flow, async batch and client isolation | Internal discovery; endpoints/master-certificate rules unapproved | Retain pathway intent, correct authority assumptions |
| PRD-SEI-101/231 | Common onboarding and delegated-authority model | Discovery model | Shared controls and records |
| PRD-SEI-226 | Purpose-scoped certificate, signature, seal, custody, expiry and historical-evidence model | Does not grant accountant authority by itself | Consume readiness; do not duplicate key lifecycle |

## Proposed conceptual model

| Record | Key fields | Important constraint |
|---|---|---|
| Firm | firm ID, status, product entitlements | Not a statutory principal for client invoices |
| Firm user/service principal | actor ID, roles, authentication assurance | Cannot infer client access |
| Client relationship | firm, client workspace/legal subject, product scope, validity, status | Separate from statutory authority |
| Authority evidence | principal, delegate, source/procedure, capabilities, direction, environment, validity, evidence ref | Re-evaluated per request |
| Client signing assignment | client principal, actual signer/delegate, signing mode, custody/reference, signature or seal policy, capability/route/profile, authority reference, validity, readiness and next recheck | No private key; no firm-wide authority flag |
| Batch | firm, idempotency scope, counts, state, created/cancelled times | Contains item references, not shared readiness |
| Client work item | client, requested capabilities, case revision, state, safe correlation | Isolation and independent recovery |
| Item result | capability outcomes, redacted reasons, evidence refs, timestamps | Visible only within authorised relationship |

### Proposed lifecycle

| Level | States | Meaning |
|---|---|---|
| Batch | `RECEIVED`, `PROCESSING`, `PARTIAL`, `COMPLETED`, `CANCELLING`, `CANCELLED`, `FAILED_ENVELOPE` | Aggregate orchestration only |
| Item | `QUEUED`, `VALIDATING`, `ACTION_REQUIRED`, `READY`, `READY_WITH_LIMITATIONS`, `OUTCOME_UNKNOWN`, `CANCELLED` | One client onboarding revision |
| Capability authority | `PENDING`, `EFFECTIVE`, `DENIED`, `EXPIRED`, `REVOKED`, `UNDETERMINED` | Independent official-authority decision |
| Signing readiness | `NOT_REQUIRED`, `ACTION_REQUIRED`, `DIRECT_SIGN_READY`, `DELEGATED_SIGN_READY`, `SEAL_READY`, `EXPIRING`, `SUSPENDED` | Per client/capability; certificate lifecycle remains in PRD-SEI-226 |

Batch `FAILED_ENVELOPE` is reserved for an unusable envelope. Item business failures produce `PARTIAL` or `COMPLETED` with item outcomes rather than destroying the batch.

## Detailed journeys

### J1 — Direct customer

1. Caller selects a permitted workspace/legal subject.
2. Sage creates an idempotent onboarding case.
3. Local validation returns immediate correction findings.
4. Identity, authority and capability checks run as required.
5. Caller receives independent capability outcomes and evidence.

### J2 — Accountant portfolio

1. Firm actor submits a batch with stable client references, capabilities and idempotency scope.
2. Sage validates only the envelope and caller/firm context before durable receipt.
3. Each item verifies the current client relationship without revealing unlinked client data.
4. Each capability evaluates its authority evidence and remaining onboarding controls.
5. Safe items process concurrently within approved limits.
6. Aggregate status derives from item states; permitted detail is retrievable by stable item reference.

### J3 — Correct authority evidence

1. Item reports `ACTION_REQUIRED` for a named capability with a safe reason.
2. Authorised actor adds/references new evidence.
3. Sage versions the evidence and re-evaluates only affected capabilities.
4. Unaffected completed capability decisions remain unchanged unless policy requires recheck.

### J4 — Relationship revoked mid-flight

1. Firm-client relationship becomes inactive.
2. New reads/changes are denied and queued protected work is stopped.
3. Any outcome-unknown external operation is reconciled by an authorised operational path.
4. Audit/evidence remain retained; the client may continue through its direct channel.

### J5 — Accountant establishes client signing readiness

1. The accountant selects a client and requested signing-dependent capability; Sage rechecks the active firm-client relationship and product permission.
2. The accountant selects direct customer signing, accountant/delegated signing, Sage-managed remote signing or provider-managed signing. A Sage operator seal is displayed separately and only where an approved policy permits it.
3. Sage resolves the protected trust-material reference and current PRD-SEI-226 status without importing private-key material into the product.
4. Sage evaluates the client principal, actual signer/delegate, authority scope, certificate subject/purpose, route/profile, environment and validity independently.
5. The client/capability becomes ready only for the supported mode and effective period. Other clients in the same batch remain independent.
6. Expiry, revocation, compromise, relationship loss or authority withdrawal suspends only affected future use; historical signed evidence remains available under its retention policy.

## Functional requirements

| ID | Requirement |
|---|---|
| FR1 | Direct and accountant pathways must invoke the same versioned client-level business policies. |
| FR2 | Every accountant request must bind firm actor, firm, client relationship, legal subject, environment and requested capabilities. |
| FR3 | The system must revalidate the client relationship at protected read/change time, not only at initial batch submission. |
| FR4 | Batch intake must be idempotent and durably acknowledge receipt without claiming item readiness. |
| FR5 | The service must decompose each batch into independently authorised, scheduled, observable and recoverable client items. |
| FR6 | Envelope failure must be distinguished from item validation, authority or external failure. |
| FR7 | The service must calculate batch state from item outcomes and expose counts plus authorised item detail. |
| FR8 | One item failure/cancellation must not roll back or block another independent safe item. |
| FR9 | The service must evaluate authority separately for every client and capability; a batch-level representation label is insufficient. |
| FR10 | Authentication, role, relationship and credential evidence must remain independently queryable from statutory authority. |
| FR11 | A reusable evidence reference may apply to several items only when its verified scope includes each principal and capability. |
| FR12 | The service must preserve asymmetric submission, receipt, consultation, rejection and payment-reporting outcomes. |
| FR13 | Revoked/expired authority or relationship must stop affected future protected work while retaining historical evidence. |
| FR14 | Status/error responses must not reveal an unauthorised client’s existence, identifiers or configuration. |
| FR15 | Concurrent changes to the same client/capability revision must be version-controlled or serialized. |
| FR16 | Correction must resume the same logical item with new evidence revision rather than create duplicate external work. |
| FR17 | Cancellation must stop safe pending work and reconcile outcome-unknown operations before terminal completion. |
| FR18 | Operations/manual actions must enforce the same client, authority, environment and audit controls. |
| FR19 | Capacity, concurrency, item and batch limits must be configured from measured demand and approved external constraints. |
| FR20 | Products must explain batch receipt, progress, partial completion and per-capability action required in plain language. |
| FR21 | Accountant onboarding must distinguish permission to configure certificate readiness from authority to create an invoice signature for the client. |
| FR22 | Every delegated-signing decision must bind the client principal, actual signer/delegate, capability, route/profile, environment, authority evidence, effective period and protected trust-material reference. |
| FR23 | A certificate or signing-service reference may be reused across clients only where its verified subject/purpose and the delegate's authority independently cover every client and operation. |
| FR24 | Sage-managed signing must identify the represented client, authorised signer/delegate, Sage service role and custody boundary; the Sage workload/transport identity must not be treated as the invoice signer. |
| FR25 | Sage operator sealing must have a separate readiness result and must not satisfy delegated-signature readiness unless Legal approves that exact route and policy. |
| FR26 | Batch status must expose certificate/signing action required per client without disclosing certificate secrets or another client's identity/configuration. |
| FR27 | Expiry, revocation, compromise or loss of signing authority must suspend only dependent future client capabilities and must not invalidate historical evidence solely because the certificate later expired. |

## Failure and recovery

| Failure | Behaviour | Result |
|---|---|---|
| Invalid envelope | Reject before item creation with safe structural findings | `FAILED_ENVELOPE` |
| Duplicate batch | Return existing batch/correlation | No duplicate items |
| Unknown/unlinked client | Deny item using non-enumerating result | Other items continue |
| Authority absent/undetermined | Mark affected capability action-required | No forced sender-only role |
| Relationship revoked | Stop protected future work and access | Client continuity remains independent |
| Transient safe dependency failure | Retry under PRD-SEI-107 policy | Item remains recoverable |
| Ambiguous mutation | `OUTCOME_UNKNOWN` and reconcile | No blind repeat |
| Internal failure after durable receipt | Resume from durable item state | No client resubmission required |
| Batch cancellation | Cancel safe queued work; complete/reconcile in-flight items | Accurate aggregate outcome |
| Certificate wrong owner/purpose or delegate not authorised | Block that client's signing-dependent capability and show the authorised actor a precise remediation | Other clients/capabilities continue |
| Certificate expires/revokes during a batch | Freeze new affected signing work, reconcile possible in-flight use and re-evaluate after replacement | No silent fallback to another certificate/signer |

## Non-functional requirements

- NFR1: Enforce least privilege and client isolation for every item, status, result and manual action.
- NFR2: Redact full NIF/NIE, evidence content and credential metadata from general logs/errors/metrics.
- NFR3: Encrypt sensitive records and retain only approved evidence references/content.
- NFR4: Provide durable, restart-safe batch/item processing with idempotent correlation.
- NFR5: Audit actor, firm, client, capability, environment, evidence decision and outcome.
- NFR6: Monitor queue age, partial batches, authority failures, unknown outcomes and inaccessible-client attempts.
- NFR7: Meet accessibility and consistent-message requirements across direct and accountant products.
- NFR8: Define targets only after direct/accountant volumes and external constraints are approved.

## Acceptance criteria

| ID | Given/when/then |
|---|---|
| AC1 | Given direct and accountant requests for the same client facts, when evaluated under the same policy version, then their client-level results are equivalent apart from actor/authority context. |
| AC2 | Given a valid batch envelope, when accepted, then the receipt states that item processing/readiness is pending. |
| AC3 | Given one authorised and one unlinked client, when the batch runs, then only the authorised item may change and no unlinked-client data is returned. |
| AC4 | Given firm authentication and client relationship but no effective submission authority, when submission readiness is requested, then it is denied/undetermined and audited. |
| AC5 | Given authority for submission but not retrieval, when both are requested, then distinct results are returned without coercion to `SENDING_ONLY`. |
| AC6 | Given a duplicate batch, when resubmitted in the same idempotency scope, then the existing batch is returned and no item is recreated. |
| AC7 | Given authority is revoked during processing, when the next protected step runs, then affected work stops while completed evidence remains visible to authorised actors. |
| AC8 | Given two users update one client revision, when a stale update arrives, then it cannot silently overwrite the effective revision. |
| AC9 | Given a status request after the client relationship ended, when the accountant calls it, then access is denied without disclosing current client state. |
| AC10 | Given an outcome-unknown external operation, when batch cancellation occurs, then the item remains reconcilable and is not falsely reported cancelled. |
| AC11 | Given an accountant may manage a client's onboarding but lacks signing authority, when delegated signing readiness is requested, then configuration access succeeds but signing readiness is denied/undetermined. |
| AC12 | Given one certificate reference is submitted for several clients, when only some authority scopes match, then only those client/capability combinations may become ready. |
| AC13 | Given Sage-managed signing is selected, when readiness is displayed, then the client principal, approved signer/delegate, Sage service role and custody reference are separately identifiable. |
| AC14 | Given a valid Sage workload/transport certificate, when client invoice signing is requested, then it is rejected as wrong-purpose unless a separate approved signing policy exists. |
| AC15 | Given a delegated signing certificate expires after earlier valid invoices were signed, when the next batch runs, then new affected signing is blocked while historical evidence remains attributable. |

## Measures and rollout gates

| Measure | Purpose | Owner |
|---|---|---|
| Direct/accountant conversion by capability | Compare pathway friction | Product |
| Batch receipt-to-terminal duration | Capacity and orchestration health | Operations |
| Partial-batch reasons | Identify identity, authority and dependency gaps | Product/legal/engineering |
| Authority-undetermined rate | Quantify missing Spain representation evidence | Legal/product |
| Cross-client access denials/incidents | Validate isolation | Security |
| Duplicate suppression and unknown-outcome age | Validate safe recovery | Operations |
| Signing readiness/action-required by client and mode | Identify custody, authority and expiry friction without hiding it in batch status | Product/security |

Production is gated on the official SPFE representation contract, an approved client/capability authority matrix, accountant product roles, firm-client lifecycle, privacy/retention, expected volumes, batch limits, operations runbook and security testing.

## Open questions

| Question | Owner | Blocks | Current hypothesis |
|---|---|---|---|
| Which SPFE operation may be performed through social collaboration or apoderamiento, and how is it verified/revoked? | Spain legal/AEAT liaison | Accountant production | No capability is inferred from another AEAT procedure |
| Can one official credential legitimately cover several client principals and operations? | Legal/security | Credential design | Reuse only where evidence scope proves it |
| What is the firm-client/workspace cardinality and lifecycle across products? | Product/data | API/security design | Explicit many-to-many relationship with validity |
| What are expected firms, clients per firm, batch sizes and peak concurrency? | Product/analytics | Capacity targets | Pilot measurement required |
| Which item details may accountants/support view after relationship or authority ends? | Legal/privacy/security | Retention/access | Historical access is purpose- and policy-bound |
| Which accountant/delegate mechanisms will the public and private routes recognise for each operation? | Spain legal/operator | Signing and submission readiness | Do not infer one mechanism covers all capabilities |
| May an accountant use a customer-held, accountant-held or Sage-managed remote-signing credential, and who is named as signatory in each mode? | Legal/security/Business Identity | Custody and UX design | Keep authority, signer and custodian separate |
| Which expiry horizons, renewal owners and in-flight behaviours apply to portfolio signing credentials? | Security/operations/product | Production operations | Configure by certificate class; no universal threshold |

## Decisions and readiness

| Decision | Status |
|---|---|
| Direct and accountant are orchestration variants of one control model | Accepted product direction, 2026-08-25 |
| Portfolio authority is evaluated per client and capability | Proposed for review; required safety principle |
| Original master-certificate and forced sender-only rules are not delivery requirements | Evidence-led correction |
| Existing Confluence page remains the stable publishing target | Publication approved by user on 2026-08-25, subject to merge and dry-run |

**Readiness: discovery-ready draft.** It is not approved for delivery until the representation, credential, client-relationship, volume and operations gates are closed.

## Change log

| Date | Version | Change | Evidence |
|---|---|---|---|
| 2026-08-25 | Initial canonical draft | Preserved direct/batch pathways and isolation; replaced universal credential/authority assumptions with per-client capability decisions and safe batch lifecycle | Confluence v3, PRD-SEI-101/231, Royal Decree 238/2026 |
| 2026-09-22 | Certificate/signature precision | Added per-client direct, delegated, Sage-managed, provider and operator-seal distinctions; separated accountant configuration permission from signing authority and added expiry/revocation behaviour | PRD-SEI-101/223/226; RD 238/2026 Article 7.3 |
