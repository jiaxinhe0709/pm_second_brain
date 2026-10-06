---
id: SPEC-SEI-001
title: Certificate Management Solution Specification
type: solution-spec
status: draft
owner: TBD — Trust Service Solution Designer
product: spain-e-invoicing
created: 2026-10-05
updated: 2026-10-06
reviewers: []
related:
  - PRD-SEI-226
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-202
  - PRD-SEI-222
  - PRD-SEI-223
  - PRD-SEI-225
  - PRD-SEI-231
  - ADR-SEI-001
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Certificate Management Solution Specification

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices still need review; **open** decisions still need an owner’s recorded answer. Technical IDs and state names are kept so engineering, testing and stakeholders can refer to the same item.

### 1 Purpose and reading route

This draft explains how Sage could manage certificates and keys used by onboarding, connections, invoice exchange and operations. For each requested use, the service checks whether the approved policy and current evidence allow it. It also protects private keys, manages replacement or compromise, and preserves evidence for earlier operations.

[PRD-SEI-226](../prds/PRD-SEI-226-security-trust-identity-data-audit.md) remains the source of product and security requirements. The interfaces, records and state names in this spec are **proposed**. They are not an approved architecture.

The four views below form one canonical document and one intended Confluence page. The supplied templates guide its structure; they do not establish certificate policy or approve this design:

1. This summary: scope, parties, workflow, lifecycle and decision gates.
2. [Part 2 Logical Feature Specification](#part-2-logical-feature-specification): complete behaviour, invariants, transitions, errors and acceptance scenarios.
3. [Part 3 Logical Service Interactions and Data Inventory](#part-3-logical-service-interactions-and-data-inventory): logical operations, events, records and contracts.
4. [Part 4 Assurance and Traceability View](#part-4-assurance-and-traceability-view): requirement coverage, verification and unresolved gates.

This document is for Product, Business Identity, Security, Legal, Spain Compliance, engineering, operations and integration teams. Start with Part 1 for the scope and decisions. Part 2 explains behaviour, Part 3 describes interfaces and data, and Part 4 shows how to verify the design. Open questions remain in the source PRDs until an approved decision record replaces them.

### Spain use and reuse boundaries

This is a **Spain reference design**. The classifications below describe proposed reuse of behaviour, not proof that existing code is ready for use. **Reusable unchanged** means the design pattern can stay the same. **Reusable with country binding** means the shared behaviour needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** means implementation fitness or coverage still needs evidence.

This follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot or production use still depends on this spec’s approval and evidence gates. Reuse in another country needs that country’s own assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Versioned inventory and evidence | Keep certificate versions, operation references and historical proof for Spain. | Reusable unchanged | Reuse the record and audit pattern; check storage, access and recovery fitness. Trust owner and Records. |
| Readiness, protected use and rotation | Check the purpose, actor, route/profile and current authority before Spain operations. | Reusable with country binding | Bind approved Spain certificate, signer/seal, trust-source, custody and retention policies. Business Identity, Security and Spain Legal. |
| Spain trust requirements | Resolve public-solution authentication, representation and signing requirements for each supported Spain route. | Country-specific | Keep these rules in the Spain policy. Do not carry them into another country by default. Spain technical owner and Legal. |
| Existing trust-service implementation | Assess which inventory, custody, validation and signing functions can serve Spain. | Unknown | This spec does not establish a deployed service or approved custodian. Confirm owner, build, interfaces and gaps before committing reuse. Business Identity and Architecture. |

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
| Capability | A supported function, such as receiving invoices or signing them. |
| Route | The platform and connection used to send or receive an invoice. |
| Idempotency | A repeat of the same request has no additional effect. The contract must define how the system recognises that request. |
| Reconciliation | Check the original operation against a reliable source to establish what actually happened before deciding the next action. |
| Gate | A condition, decision or evidence check that must pass before the next step can proceed. |
| Tenant | The customer account boundary used to keep one customer’s data and access separate from another’s. |
| Immutable / append-only | A saved item cannot be changed; new information is added as a new record instead of overwriting earlier records. |
| Provenance | The record of where data came from and which versions, checks and changes produced the result. |
| Contract | The agreed inputs, outputs, behaviour and responsibilities between services or parties. |
| Durable | Saved so the record remains available after a service restart. |
| Custodian / custody | The party or protected system that holds and uses a private key. |
| Principal / delegate | The business or person represented, and the person authorised to act for them. |
| Signature / seal | Different cryptographic proofs associated with a signer or an organisation. Their permitted use must be approved separately. |
| Rotation / cutover | Prepare a replacement certificate or key, then switch future work to it at an approved point. |
| PKI / HSM | Public key infrastructure manages certificates and keys. A hardware security module is a device that protects cryptographic keys. |
| CA / RTO / RPO | Certificate authority; target time to restore a service; and maximum acceptable loss of recent data. Values remain subject to approval. |
| LFS | Logical Feature Specification: Part 2 of this document. |

### 2 Terms used

| Term | Meaning |
|---|---|
| Trust material | A certificate, certificate chain, key reference or external validation identity. Its subject, custodian, permitted purpose and lifecycle must be defined. |
| Material version | One saved version of the certificate or key reference. Renewal creates a new version and keeps the earlier record. |
| Trust policy | A rule valid for a stated period. It defines who may use which material, for what purpose and route/profile, and the required checks and evidence. |
| Readiness | The current result of checks for one capability, actor, business, environment and route/profile. Permission to act and invoice delivery are checked separately. |
| Protected operation | Use of a key inside the approved protected system operated by the customer, Sage, a provider or a trust service. |
| Operation binding | The fixed link between one attempt and its policy version, material version, authority snapshot and exact input hash. |
| Evidence package | Saved references to the exact signed file, signature or seal, certificate chain, status and time evidence, policy and source history. These allow later verification. |

### 3 Feature purpose and scope

The process starts when an authorised owner requests, selects or registers trust material, or when another service asks to use it. The trust service records the material and its permitted purpose, checks custody and trust, and returns readiness for the requested use. It monitors dependent services and manages replacement, retirement and retained evidence.

Direct customer signing, delegated accountant signing, Sage-managed remote signing, provider signing or sealing, Sage operator sealing, workload identity, transport authentication and inbound validation are **different policy classes**. Each class needs its own approved policy.

Policy activation for an individual class requires legal/security approval.

The process can finish with an active version approved for the requested use, a retired or destroyed private key with historical evidence retained, or a verified reference to material held externally. Denied or inapplicable requests are closed with a reason and an audit record.

`VALIDATION_UNKNOWN`, uncertain key creation or use, and failed replacement remain recovery cases. The service must show who owns the next action; it must not report success or close them silently.

The first design slice covers inventory, versioning, readiness, expiry monitoring, rotation and dependency impact for approved certificate classes; onboarding and exchange consume the service through explicit interfaces. Physical PKI/HSM selection, final Spanish certificate profiles, public-solution authentication details, exact retention periods, and the legal permissibility of an operator seal are outside this draft's authority. No universal certificate-upload step is assumed.

### 4 Parties and responsibility boundary

| Party | Responsibility | Handoff |
|---|---|---|
| Customer or accountant | Identifies intended legal subject and direct/delegated signing mode; completes approved proof or customer-held setup | Supplies authority evidence to onboarding/identity; never grants authority by presenting a certificate alone |
| Onboarding service | Resolves requested capability/route/profile, asks for certificate need and readiness, displays remediation | Stores scoped readiness reference, not a private key; [PRD-SEI-101](../prds/PRD-SEI-101-public-platform-onboarding.md) owns customer onboarding |
| Identity and authority service | Resolves legal subject, principal, delegate, scope and effective authority | Supplies independently versioned authority decision; [PRD-SEI-231](../prds/PRD-SEI-231-country-identifiers-tenancy-and-delegated-accountants.md) owns identity/delegation model |
| Trust service owner | Owns material inventory, policy evaluation, protected-operation orchestration, lifecycle and evidence contract | Returns purpose-specific readiness, operation result and audit/evidence references |
| Custodian or provider | Holds/operates the protected key or supplies external trust/status evidence under an approved agreement | Returns attested result and evidence; custody and export rules are approved per class |
| Exchange/connection service | Freezes trust plan per operation and enforces runtime readiness | Does not substitute signer, seal or transport credential; [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md) owns exchange |
| Security, Legal and Operations | Approve policy and high-risk actions; monitor expiry, compromise and historical proof | Control suspension, incident and restoration; [PRD-SEI-225](../prds/PRD-SEI-225-operations-resilience-support-reconciliation.md) owns shared operations |

### 5 Key open solution decisions

| Decision | Current position and design impact | Owner / gate |
|---|---|---|
| Which service physically owns inventory, remote signing, validation and preservation? | Logical boundary is proposed; integration/ownership cannot be fixed until Business Identity and architecture review | Business Identity, architecture / design |
| Who may sign, and when may a Sage operator seal be used? | Keep direct, delegated, remote-service and seal modes separate; seal cannot substitute for issuer/delegate signature by default | Spain Legal, Security / trust-policy activation |
| Which classes may import/export keys, and which custodians are approved? | Reference-only product boundary; non-exportability is preferred where applicable | Security, Legal / custody design |
| Which CA/trust lists, status sources, freshness, signature profiles and preservation evidence apply? | Parameterise by country/route/profile; no guessed defaults | Spain technical owner, Security / conformance |
| Which expiry horizon, overlap, retention and destruction rules apply per class? | Versioned policy fields with no universal duration | Security, Operations, Legal / production |
| What is the public-solution authentication and representation contract? | Do not claim external registration or certificate need without official technical evidence | Spain regulatory/technical owner / external design |

### 6 End-to-end workflow

Three process diagrams cover setup, protected use and lifecycle control. Each uses the existing `assets/diagrams` convention: horizontal responsibility lanes, phase bands, black/grey shapes, short branch labels and a version-controlled Draw.io source. Solid arrows are the selected process; dashed arrows are exception or conditional paths. The diagrams show logical responsibility, not a physical deployment or approved certificate policy.

#### Process 1 Certificate setup and onboarding readiness

![Certificate setup and onboarding readiness process](../assets/diagrams/certificate-setup-onboarding-process.svg)

**Editable source:** [Certificate setup and onboarding Draw.io](../assets/diagrams/certificate-setup-onboarding-process.drawio). **Preview:** [PNG](../assets/diagrams/certificate-setup-onboarding-process.png). This is the certificate-specific detail of the broader [customer and service readiness Draw.io](../assets/diagrams/e-invoicing-customer-service-readiness.drawio). The broader diagram's route activation belongs to Phase 2/3; Phase 1 public onboarding returns capability readiness without activating a private route.

```text
Customer or accountant requests one capability for one legal subject
  → CERT-01 resolves the effective route/profile policy and certificate need
  → CERT-02 checks principal/delegate authority independently
      └─ missing or expired grant → customer/accountant obtains the scoped grant
  → evaluate the certificate-need decision for the authorised capability
      ├─ NOT_REQUIRED → CERT-05 records an evidenced no-certificate result
      └─ UNKNOWN or conflicting policy → hold for a named policy decision
      └─ REQUIRED → CERT-03 establishes an approved protected version or external reference
          → CERT-04 checks owner, purpose, environment, chain, validity and status
              └─ invalid or unknown trust → remediation or original-operation reconciliation
  → CERT-05 returns scoped readiness, next recheck and responsible action
  → onboarding displays the result without exposing a private key
```

The direct and accountant paths share the same trust controls. A portfolio item is assessed per client and capability; one accountant certificate does not grant authority across the portfolio. A `READY` decision does not register the customer externally or activate a route.

#### Process 2 Protected use and evidence

![Protected certificate use and evidence process](../assets/diagrams/certificate-protected-use-process.svg)

**Editable source:** [Protected use Draw.io](../assets/diagrams/certificate-protected-use-process.drawio). **Preview:** [PNG](../assets/diagrams/certificate-protected-use-process.png).

```text
Exchange supplies final exact representation bytes and input hash
  → CERT-06 freezes actor, authority snapshot, policy and material version
  → use-time checks re-evaluate current scope, status and suspension
      └─ failed check → block only affected new use; no key operation
  → INT-06 invokes the protected custodian using one operation ID and input hash
      ├─ definitive rejection → return safe rejected result with audit evidence
      ├─ outcome unknown → CERT-09 queries/reconciles the original operation
      │   └─ if still unproven → hold; do not start a fresh signing attempt
      └─ confirmed result → CERT-07 durably stores exact object and trust evidence
  → return an evidence reference and customer-safe trust result
```

A confirmed cryptographic result is not invoice delivery or buyer acceptance. Reconciliation may establish a confirmed signature or definitive rejection; it must preserve the original operation identity and cannot silently change the representation or signer.

#### Process 3 Renewal, containment and retirement

![Certificate renewal, containment and retirement process](../assets/diagrams/certificate-renewal-recovery-process.svg)

**Editable source:** [Renewal and recovery Draw.io](../assets/diagrams/certificate-renewal-recovery-process.drawio). **Preview:** [PNG](../assets/diagrams/certificate-renewal-recovery-process.png).

```text
Monitoring detects approaching expiry, revocation or compromise
  → CERT-08 maps active workloads, routes, policies and in-flight attempts
      └─ compromise/revocation → CERT-09 contains affected new use and opens case
  → for planned renewal, CERT-08 creates a new protected material version
  → CERT-04 validates it and tests the required counterpart/profile
      └─ failed or unknown test → hold; old version remains usable only if safe
  → approved effective cutover selects the new version for future work
  → frozen in-flight attempts retain their original binding or reconcile
  → CERT-10 retires/destroys old key material after dependency and hold gates
  → historical signed bytes, certificate and validation evidence remain available
```

The route, certificate and trust-policy versions used by an earlier operation remain part of its historical evidence. Key destruction and evidence retention follow separate approved schedules.

The lifecycle below follows setup, permitted use, evidence storage, replacement and retirement (`CERT-01`–`CERT-10`). Inbound validation uses `CERT-04` and `CERT-07` without signing. When an external result is unknown, check the original operation before requesting another change.

### 7 One feature lifecycle

| Activity | Result that must be visible | Responsible party | Detailed reference |
|---|---|---|---|
| CERT-01 Classify | Material class, intended purpose, environment and owner are explicit | Trust service | LFS §3, INT-01 |
| CERT-02 Authorise | Principal/delegate/operator and effective policy are resolved independently of authentication | Identity/authority and trust | LFS §4, INT-02 |
| CERT-03 Establish custody | Key is protected or externally referenced; version is inventoried | Custodian and trust | LFS §5, INT-03 |
| CERT-04 Validate | Chain, scope, validity and status produce evidenced result or unknown | Trust | LFS §6, INT-04 |
| CERT-05 Decide readiness | Scoped result and next recheck/remediation are returned | Trust; onboarding consumes | LFS §6, INT-05 |
| CERT-06 Bind and use | Approved actor/policy/material/input are frozen before protected use | Exchange and trust | LFS §7, INT-06 |
| CERT-07 Preserve | Exact output and evidence references are durable | Trust/evidence store | LFS §7, INT-07 |
| CERT-08 Rotate | Replacement passes validation and dependency cutover before old new-use is disabled | Trust and operations | LFS §8, INT-08 |
| CERT-09 Contain | Affected purposes stop; incident and unknown outcomes remain reconcilable | Security and operations | LFS §9, INT-09 |
| CERT-10 Retire | Key-use ends; approved historical evidence remains available | Trust and records owner | LFS §10, INT-10 |

### 8 Cross-cutting controls and risks

Tenant, environment, legal subject, actor, purpose and route/profile are explicit in every decision; no bare certificate ID authorises use. Protected APIs require least privilege and action-specific authorisation. Every mutation is auditable and designed to handle repeats safely. The system retains prior material and policy versions so a route change or certificate expiry cannot rewrite the original signing conclusion. Capacity, latency, alert thresholds, retention and recovery targets require baselines and approval; this draft specifies the measurement points rather than inventing values.

The main risks are using material for the wrong purpose, acting for a client without permission, silently replacing a signer or seal, an outage caused by expiry, signing twice after a timeout, and losing historical evidence. Part 2 explains when to block work and how to recover.

This draft is **ready for solution review**. The decisions in §5 and the assurance gates must be resolved before production activation.

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Authority, status and design boundary

This is a **proposed logical design** for the certificate/key lifecycle in [PRD-SEI-226](../prds/PRD-SEI-226-security-trust-identity-data-audit.md), including the conditional onboarding consumer in [PRD-SEI-101](../prds/PRD-SEI-101-public-platform-onboarding.md) and exchange consumer in [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md). It does not approve a PKI/HSM product, cryptographic algorithm, certificate authority, signer model, Spanish legal interpretation, cloud boundary, or physical API. The [Part 1](#part-1-feature-solution-summary) provides the lifecycle map; the [Part 3](#part-3-logical-service-interactions-and-data-inventory) defines logical contracts; [Part 4](#part-4-assurance-and-traceability-view) tracks verification.

**Confirmed product constraints from the PRDs:** certificate need is capability/route/profile dependent; authority is independent of certificate possession; different trust purposes are not interchangeable; key material remains inside approved custody; invalid/currently unknown trust blocks new dependent operations; old signed evidence persists independently of private-key lifecycle; ambiguous external mutations reconcile before repetition. **Proposed design:** the records, state vocabulary, commands/events, concurrency model and operation-binding protocol below. **Open:** the policy content, accountable service owner, custody implementation, trust/status sources, legal signature/seal modes and service objectives.

### 2 Actors, scope and invariants

Actors are customer/delegate, product/onboarding, identity/authority service, trust-policy approver, trust service, custody provider, exchange/connection service, security operations and evidence/archive service. An external certificate subject or provider is evidence, not a Sage-authorised user. Logical tenancy is `(tenant, legalSubject, environment)`; every material/policy/decision additionally has purpose, permitted actor/mode, capability, route and profile where applicable.

**Invariants**

| ID | Rule that must always hold |
|---|---|
| CM-I01 | A material reference never confers business authority. An effective authority decision is checked for the requested principal/delegate/action and time. |
| CM-I02 | Every material version has exactly one class, custodian, owner, environment and version identity. A new certificate/key is a new version; historical rows are append-only. |
| CM-I03 | A trust policy explicitly lists permitted uses. Authentication, direct signature, delegated signature, Sage-managed remote signature, provider signature/seal, operator seal, validation and timestamp are distinct purposes. |
| CM-I04 | No product API, queue, log, support view, audit event or document carries an exportable private key or reusable secret. Custody APIs may receive protected material only inside an approved secure boundary. |
| CM-I05 | `ACTIVE` material is usable only after policy, chain/status, authority, custody and environment checks for that exact operation. Inventory state alone cannot authorise use. |
| CM-I06 | A protected operation is bound to immutable `operationId`, `materialVersionId`, `policyVersion`, `authoritySnapshotId`, `inputHash`, legal subject and environment before execution. A material/policy switch does not silently change an in-flight attempt. |
| CM-I07 | A timeout after a possibly executed protected operation creates `OUTCOME_UNKNOWN`. No fresh attempt is issued until the original is reconciled or the custodian's effective idempotency guarantee is evidenced. |
| CM-I08 | Rotation and route change affect future operations that meet the policy. They never rewrite prior signed bytes, actor, material/policy binding or historical conclusion. |
| CM-I09 | Revocation, compromise, wrong purpose/owner/environment or stale/unknown validation blocks affected *new* use. Containment targets the narrowest proven dependency set. |
| CM-I10 | Private-key destruction and evidence disposition are separate governed actions. Evidence cannot be deleted merely because material retires or a provider exits. |

### 3 CERT-01 Classify request and applicability

**Trigger:** onboarding requests a capability; connection/exchange needs trust; an owner requests issuance/import/reference; or monitoring detects changed material. **Preconditions:** caller identity, trusted environment and one legal subject/operator are resolved. The trust service looks up an effective, approved policy by country, capability, direction, route, format/profile, actor mode and time. A policy can return `NOT_REQUIRED`, `REQUIRED`, `PROHIBITED` or `UNDETERMINED`; `NOT_REQUIRED` is an evidenced decision, not a default caused by missing configuration. `UNDETERMINED` blocks the dependent capability and creates a policy decision case.

The request names a class from the PRD taxonomy (direct issuer, accountant/delegate, Sage-managed remote signing, Sage operator seal, provider signing/sealing, workload, transport, external validation or timestamp). The service rejects a generic “Sage certificate” or “signing certificate” with no legal actor/purpose. The selected policy version and rule reason are stored in `D-02`; no material is provisioned from a policy lookup alone.

Duplicate logical requests return the same classification for the same idempotency key and immutable input digest. A changed input creates a new assessment revision. `INT-01` serves the lookup.

| Class | Decision inputs that cannot be inherited from another class | Consumer boundary |
|---|---|---|
| Direct issuer signature | Issuer/signatory identity, approved representation profile, key usage and direct authority | Outbound exchange; onboarding checks conditional readiness |
| Accountant/delegated signature | Client-by-client mandate, delegate, permitted action, effective time and route | Accountant onboarding and outbound exchange |
| Sage-managed remote signing | Actual customer/delegate signatory, Sage's custody/service role and approved remote-signing authority | Trust service performs protected use; ERP receives no key |
| Sage operator seal | Named operator legal person, permitted document/route and Legal-approved seal policy | Exchange; never silently satisfies customer signature |
| Provider signing/sealing | Provider's actual actor and attested returned evidence, authority defined by the contract and approved adapter | Provider adapter and trust verification |
| Workload / transport | Endpoint or service identity, channel protocol, environment and counterpart trust | Connection/transport; cannot imply invoice signature |
| External validation / timestamp | Trust-list, status/time source, evidence freshness and preservation profile | Inbound and historical validation |

The activated format profiles in [PRD-SEI-236](../prds/PRD-SEI-236-ubl-format-profile.md), [237](../prds/PRD-SEI-237-cii-format-profile.md), [238](../prds/PRD-SEI-238-un-edifact-format-profile.md) and [239](../prds/PRD-SEI-239-facturae-format-profile.md) may require different representation and signature policy. The policy lookup must bind an exact profile/version rather than treating UBL, CII, EDIFACT and Facturae as interchangeable.

### 4 CERT-02 Resolve subject and authority

The caller supplies tenant/workspace context, legal subject reference, requested acting person/service, represented principal, capability and direction. The identity/authority owner independently verifies the tenant-to-subject relationship and an effective grant for the requested action, route/profile and environment. The decision includes evidence source/version, effective interval, revocation check and result; it is not inferred from login, portfolio membership, certificate subject, possession, or provider access.

A direct signer must be distinguished from a delegate; a Sage-operated signing service is the custodian/operator and not automatically the signatory. An operator seal identifies the operator legal person and requires its own policy approval.

`DENIED`, `REVOKED`, `EXPIRED` or `UNDETERMINED` authority blocks the affected scoped action, records a reason with sensitive values removed and leaves unrelated clients/capabilities unchanged. An authority change emits invalidation for dependent readiness and future operations, while preserving prior snapshots. `INT-02` returns a versioned authority reference; no raw mandate is copied into the material inventory.

### 5 CERT-03 Establish custody and material version

An authorised owner requests one of: generate/issue in an approved protected boundary; register a customer-held or provider-held reference; or import only when the class-specific custody policy permits it. The request requires owner, custodian, subject, class, purpose, scope, environment, policy, renewal owner and change reason. High-risk actions require independently attributable approval and separation of duties under the effective corporate policy. The trust service records a `REQUESTED` inventory item before any external mutation, then `APPROVED` and `PROVISIONING`/`PROVISIONED` according to observed custodian evidence.

`PROVISIONING_OUTCOME_UNKNOWN` means the custodian may have created material; reconcile by request reference before issuing another command.

The custodian returns a non-secret handle and public certificate/attestation metadata. The trust service verifies the returned subject, issuer/chain, public-key fingerprint, key usage/extended usage, validity, custodian attestation and environment against the approved request. It records an immutable material version, including source and observation time. It never stores the private key in an application database or emits it in an event. A customer-held key may never be copied to Sage just to satisfy readiness.

If an external reference cannot provide the necessary evidence, readiness stays `UNDETERMINED`. `INT-03` is the logical command; `D-03` is the inventory record.

### 6 CERT-04/05 Validate trust and calculate scoped readiness

**Validation inputs:** material version, trust policy version, owner/principal/delegate, authority decision, capability, route/profile, environment and checked time. Validation evaluates: (1) exact subject/owner and permitted purpose; (2) custody and key availability/attestation; (3) current validity interval and algorithm/profile policy; (4) chain/trust-list status and approved issuer; (5) current revocation/status evidence and freshness; (6) dependency or incident suspension; and (7) per-operation authority where the class requires it. The source and version of each check are retained. Failure in one dimension cannot be hidden by a passing dimension.

**Proposed readiness outcomes:** `NOT_REQUIRED`, `READY`, `EXPIRING`, `ACTION_REQUIRED`, `BLOCKED`, `UNDETERMINED`. `EXPIRING` can remain usable only until the approved horizon/policy says otherwise; it always creates a renewal action. `VALIDATION_UNKNOWN` yields `UNDETERMINED` and blocks new protected use by default. The result includes scope, material/policy/authority versions, evaluation time, next mandatory check, expiry, evidence reference, reason code, responsible remediation actor, and a non-secret dependency summary.

The customer-facing label maps to `TRANSPORT_READY`, `DIRECT_SIGN_READY`, `DELEGATED_SIGN_READY`, `SEAL_READY` or `VALIDATION_READY`; it cannot collapse all purposes into one “certificate valid” flag. Onboarding stores only the readiness result/reference and rechecks before later use. A batch evaluates each legal subject and capability independently, including shared accountant material.

`INT-04` validates material; `INT-05` returns readiness. Cache use, if approved, may not outlive the shortest applicable authority, certificate, status-source, policy or incident validity. Cache invalidation is driven by version change or revocation/suspension events; an unavailable status source is not a reason to assume validity. Exact freshness targets are open by class/profile.

### 7 CERT-06/07 Bind protected use and preserve evidence

Before exchange uses a key, it finalises the representation under the approved transform/validate order, calculates the exact input hash and freezes a trust plan. The plan names the represented principal, actual signer/delegate or seal creator, custody service role, material version, policy version, authority snapshot, route/profile, environment and correlation. The trust service rechecks current authority, status and dependency suspension **at use time**; an onboarding `READY` result is not a perpetual grant.

A workload or transport certificate cannot fill a missing invoice-signature policy. A Sage operator seal remains blocked for a signature duty until the legal/policy decision explicitly permits that use.

`INT-06` invokes the protected operation with an idempotency/correlation reference. The custodian must either guarantee one result per reference or expose authoritative operation lookup before automatic retry can be enabled. A definitive success returns signature/seal or channel proof, actual material version, observed time and custodian evidence. The trust service verifies that the result binds to the same input hash and approved actor/policy.

`INT-07` commits the immutable signed object/reference, hash, signature/seal, public chain, revocation/status and trusted-time evidence, authority snapshot, validation policy/conclusion, transformation provenance and retention class before reporting the operation as complete. If persistence fails after possible key use, outcome remains unknown and reconciliation searches by original operation ID; the system does not sign a new revision silently.

Inbound validation takes the same evidence principle but has no Sage signing actor: it verifies external channel/platform identity, replay controls, exact received bytes, signature/seal, recipient and profile. Untrusted content enters quarantine with reason with sensitive values removed; no trusted product delivery or success assertion occurs. This follows the boundary in PRD-SEI-226 and exchange behaviour in PRD-SEI-223.

### 8 CERT-08 Monitor, renew and rotate

Monitoring evaluates every active version against its class-specific expiry horizon, revocation/status freshness, chain/trust-list and algorithm policy, plus authority and owner changes. It produces a dependency graph covering workloads, connections, routes, signing policies, queued/in-flight operations and historic obligations. A renewal case names an owner, deadline derived from approved policy, replacement source and affected capabilities. No universal fixed warning period is assumed.

Rotation creates a **new** version, validates it in the correct environment and tests counterpart acceptance where required. The owner approves an effective-dated cutover. New operations select the new version after cutover; in-flight operations retain their frozen binding and either complete on the old version while valid or enter controlled reconciliation/restart under an explicit policy. Overlap is permitted only where the protocol and trust policy allow it.

An unsuccessful cutover leaves the old version usable only if still valid and safe, records rollback and blocks unsafe new use; it does not erase the failed replacement. Old private-key use ends after dependency checks, then revocation/retirement/destruction follow approved gates. `INT-08` coordinates the change and emits `EVT-03`/`EVT-04`.

### 9 CERT-09 Revoke, compromise and reconcile

Confirmed revocation or compromise immediately marks the affected version and its dependent capabilities unavailable for new use. Security/operations classify the incident, preserve forensic and signing-time evidence, identify affected attempts/representations and evaluate whether historical conclusions require new review. The trust service sends scoped invalidation to onboarding, connection and exchange consumers; it does not globally suspend unrelated tenant/environment/purpose combinations without evidence. Support sees the impacted scope and next authorised action, with no secret exposure.

An unknown external provisioning, signing, revocation or deletion outcome opens a case with `intendedState`, `observedState`, original request ID, last authoritative query, owner and next safe action. Reconciliation queries the custodian/external system if the contract supports it. If the contract lacks safe lookup/idempotency, the case requires manual, dual-controlled resolution; a blind duplicate mutation is prohibited. Recovery completion records the source of truth, preserves all attempted versions, and requires revalidation before resumption. The generic incident/reconciliation owner is PRD-SEI-225; this spec owns trust-specific facts and controls.

### 10 CERT-10 Retire, destroy and prove history

Retirement requires dependency checks for new and in-flight use, unresolved outcomes, legal hold, historical access and provider exit obligations. `RETIRED` removes new-use eligibility; `DESTROYED` applies only after custodian evidence that private-key material is destroyed or inaccessible under approved policy. Public certificate, chain, signature/seal, exact signed bytes or immutable hash/object reference, time/status/authority/policy and preservation evidence remain according to their separate legal schedule.

An approved historical verification re-evaluates the signed object against the **signing-time** and preservation evidence under the applicable validation policy; present-day certificate expiry alone does not invalidate the past result. Revalidation/augmentation events are append-only and do not alter the original signing time or signed bytes.

### 11 State machines and concurrency

**Material version (proposed):** `REQUESTED → APPROVED → PROVISIONING → PROVISIONED → ACTIVE → EXPIRING → ROTATION_PENDING → RETIRED → DESTROYED`. Exceptions are `PROVISIONING_OUTCOME_UNKNOWN`, `SUSPENDED`, `EXPIRED`, `REVOKED`, `COMPROMISED`, `VALIDATION_UNKNOWN`. `REVOKED` and `COMPROMISED` cannot return to `ACTIVE`; replacement requires a new version. State transitions use expected version/compare-and-swap and record actor, reason, source and time. An incident-suspension overlay can coexist with a lifecycle state; the service must not replace evidence of compromise with a generic `SUSPENDED` label.

**Readiness (derived, not manually set):** input/version changes create a new decision. The current view points to the latest valid scoped decision, but old decisions remain immutable. Concurrent requests with the same logical scope and input digest deduplicate; different input revisions are serialised or compared by revision so an older asynchronous response cannot overwrite a newer result. Authority revocation, policy withdrawal and material events invalidate affected cached decisions immediately as far as the event contract permits; use-time evaluation is still required.

**Protected operation:** `PREPARED → SUBMITTED → CONFIRMED | REJECTED | OUTCOME_UNKNOWN → RECONCILED_CONFIRMED | RECONCILED_REJECTED | MANUAL_REVIEW`. Only a confirmed/evidenced result may become complete. A retry uses the same operation ID only when the custody contract proves idempotency; changing input hash, actor or material version requires a different logical operation and an explicit correction decision.

### 12 Security, operations and service qualities

Authorisation is action-specific for view, create, approve, activate, rotate, revoke, destroy, use, validate and audit. High-risk actions follow approved separation of duties. Every service-to-service call authenticates workload and environment independently of customer authority. Non-production and production use isolated keys, endpoints, identities, policies, stores and monitoring data. Evidence/audit stores are append-only or tamper evident; support/customer projections redact subject identifiers as policy requires and never expose private keys, reusable tokens, raw cert-import packages or uncontrolled invoice contents.

Data residency, retention, deletion and access policies are external approval inputs, not inferred here.

Observability records counts/age for expiry within policy horizon, unowned dependencies, failed validation by reason, blocked wrong-purpose/attempts outside the permitted scope, rotation outcomes, protected operations with unknown outcomes and missing evidence packages. Each event carries trace/correlation and a safe material reference. Alerts route to the named renewal/incident owner. Capacity and latency must be measured by material class, custody provider and peak operation rate in pilot; no target is set without baseline and operator commitment.

Disaster recovery must preserve inventory/evidence integrity and reconcile possible external key uses before traffic resumes.

### 13 Requirements and acceptance

| ID | Testable logical requirement | Source |
|---|---|---|
| CM-R01 | The service returns certificate applicability for an exact capability/route/profile/actor/environment, including evidenced `NOT_REQUIRED` and blocking `UNDETERMINED`. | PRD-226 FR30/45; PRD-101 FR39 |
| CM-R02 | Provisioning records class, owner, custodian, purpose, environment and immutable version before it can become active. | PRD-226 FR31/36 |
| CM-R03 | Protected key material remains in approved custody; product/service outputs contain only approved references/public metadata. | PRD-226 FR36/37 |
| CM-R04 | Authority is checked independently from possession/authentication for every direct/delegated/Sage-managed use. | PRD-226 FR33; PRD-101 FR41/42 |
| CM-R05 | Readiness and use reject wrong-purpose, wrong-owner, wrong-environment, expired, revoked, compromised, suspended and validation-unknown material for affected new operations. | PRD-226 FR39/45 |
| CM-R06 | A protected operation freezes material, policy, authority and exact input hash and cannot silently substitute a signer or seal. | PRD-226 FR32/33/40 |
| CM-R07 | A possible external mutation with unknown result reconciles by original reference before a new attempt. | PRD-226 J8; PRD-225 |
| CM-R08 | Rotation activates a validated new version through approved effective time and preserves in-flight and historical bindings. | PRD-226 FR38/40 |
| CM-R09 | Revocation/compromise invalidates scoped new use, preserves forensic history and requires reapproval before resumption. | PRD-226 FR39/41 |
| CM-R10 | Evidence supports historic validation after expiry, rotation, key destruction or provider exit without changing original signed bytes. | PRD-226 FR42–44 |
| CM-R11 | Onboarding receives readiness for each client and capability and remediation without key data; later use rechecks current state. | PRD-101 FR39–50 |
| CM-R12 | All protected actions emit audit that identifies the actor, hides sensitive values and shows signs of tampering with operation/policy/material version and outcome. | PRD-226 FR17/18 |

Acceptance scenarios `CM-AC01`–`CM-AC16` and evidence gates are in [Part 4](#part-4-assurance-and-traceability-view). No feature is production-ready until the decisions there are resolved and test evidence exists.

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Keep the shared operation and evidence model separate from Spain trust policy. Each decision must retain the selected country/route/profile policy version and actual signer or seal actor. A shared service must not apply another country’s certificate or signing defaults to Spain. The implementation owner remains open under G1; Security and Legal must approve each policy before activation.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Contract status and common envelope

All interactions below are **proposed logical interfaces**, not approved HTTP routes, event topics or database tables. The [Part 2](#part-2-logical-feature-specification) owns behaviour. Each command/query carries `correlationId`, trusted `environment`, authenticated caller identity, `tenantId` or operator scope as applicable, `legalSubjectId` where applicable, `requestId`/idempotency key for mutation, and an explicit `reason`. No caller-supplied tenant or environment value overrides trusted credentials/deployment context. The service rejects mismatches before data lookup or mutation.

Responses identify `decisionId`/`operationId`, evidence reference, version and safe reason code. All times are recorded with offset/UTC and source clock; exact encoding is an architecture choice.

The caller must not send or receive private keys through these application contracts. Any authorised import is a separately approved secure custody workflow. For asynchronous operations, accepted means **durably received**, never “external operation succeeded.” Error categories are `INVALID_INPUT`, `UNAUTHORISED_SCOPE`, `POLICY_UNDETERMINED`, `AUTHORITY_DENIED`, `TRUST_INVALID`, `DEPENDENCY_SUSPENDED`, `CONFLICT`, `TRANSIENT_UNAVAILABLE`, `OUTCOME_UNKNOWN` and `INTERNAL_FAILURE`; internal/provider details are retained only in controlled evidence. A mutating `TRANSIENT_UNAVAILABLE` is retryable only when it is proven not to have reached custody or the contract provides effective idempotency.

### 2 Logical service interactions

| ID | Caller → owner | Purpose and logical result | Safety / authorisation |
|---|---|---|---|
| INT-01 | Onboarding/exchange → trust policy | Resolve applicability for country, capability, direction, route/profile, actor mode, environment, effective time. Returns `NOT_REQUIRED/REQUIRED/PROHIBITED/UNDETERMINED`, policy version and reason. | Read-only; access scoped to legal subject/operator and product capability. Unknown policy blocks dependent use. |
| INT-02 | Trust → identity/authority | Resolve legal subject and effective authority for principal/delegate, operation, capability, route and time. Returns versioned decision/evidence reference. | Read-only but sensitive; no mandate body copied to product or logs. Revocation forces re-evaluation. |
| INT-03 | Owner/trust → approved custodian | Request issue/generate/register/import under class policy; returns protected handle, public certificate metadata, observed state and custodian reference. | Mutating; durable request/idempotency and authoritative lookup required before automatic retry. High-risk approval/dual control as policy requires. |
| INT-04 | Trust → validator/status sources | Validate chain, subject, usage, period, issuer/trust list, revocation/status freshness and profile. Returns each check, source/version/time and aggregate. | Read-only; failure/unknown does not become valid by fallback. External query limits/freshness need approved policy. |
| INT-05 | Onboarding/connection/exchange → trust | Evaluate scoped readiness from policy, material, authority, status and incident overlays. Returns purpose-specific result, reason, next recheck, owner and evidence reference. | Read-only derived decision; tenant/subject isolation; not a perpetual authorisation token. |
| INT-06 | Exchange/connection → trust/custodian | Prepare and invoke protected signing, sealing or channel operation for frozen actor/policy/material/input. Returns operation state and attested result. | Mutating; same `operationId`/input digest deduplicates. Unknown reconciles via INT-09 before a new attempt. |
| INT-07 | Trust → evidence/archive | Persist exact signed object/reference, output, chain, status/time, authority/policy, provenance and validation conclusion; return immutable package reference. | Mutating; append-only by operation/version, no secret payload. Completion is not returned before required evidence is durable. |
| INT-08 | Owner/operations → trust/custodian | Create replacement version, validate/test it, approve effective cutover, stop old new-use, retire/revoke/destroy at separate gates. | Mutating staged workflow; compare-and-swap on inventory version and explicit approvals; no blind rollback of in-flight work. |
| INT-09 | Operations/trust → custodian/external source | Query original request/operation status for unknown provisioning, key use, revocation or destruction; return authoritative evidence or manual-review need. | Read-only query first; reconciliation case owns next mutation. Lack of query/idempotency blocks automatic replay. |
| INT-10 | Records/operations → trust/custodian | Retire or destroy private-key version after dependency/hold checks, retaining separate historic evidence. | Irreversible action; privileged approval, custodian proof and audit required. |
| INT-11 | Onboarding/operations → trust | List safe inventory/dependency/readiness summary for authorised scope. | Read-only and redacted; no cross-tenant enumeration or key contents. |
| INT-12 | Audit/legal/support → evidence service | Retrieve a permitted historic validation package or initiate versioned revalidation/augmentation. | Role and purpose checked; original signed bytes/evidence immutable; sensitive content masked by role. |

**Consumer handoffs:** `INT-01` and `INT-05` are the onboarding boundary. `INT-02` remains independently owned by identity/authority. `INT-06` and `INT-07` are exchange-time, and `INT-08`–`INT-12` are trust/operations controls. A product must never activate a route from `INT-05` alone; route authority and external observation belong to PRD-SEI-202/222.

### 3 Events and delivery semantics

Events are proposed notifications of committed source state. Consumers must tolerate duplicate, delayed and out-of-order delivery by event ID, aggregate ID and monotonic version. A missing event cannot be the only protection against unsafe use: `INT-06` performs a current check.

| ID | Producer | Meaning and minimum payload | Consumer action |
|---|---|---|---|
| EVT-01 `MaterialVersionRecorded` | Trust | material ID/version, class, owner scope, environment, custody reference, state, event/version/time | Refresh inventory/readiness without treating created as active |
| EVT-02 `ReadinessChanged` | Trust | scope, purpose, old/new result, reason, policy/material/authority versions, next recheck, event/version/time | Onboarding/connection update their projection; maintain old decision history |
| EVT-03 `RotationPlanned` | Trust | old/new version refs, affected dependencies, planned effective time, approval ref | Exchange/operations prepare and test; do not switch early |
| EVT-04 `RotationEffective` | Trust | effective time, new selected version, old new-use disposition, reconciliation ref | New work chooses new version; in-flight work keeps frozen binding |
| EVT-05 `TrustUseBlocked` | Trust | scoped material/purpose, reason class, observed time, incident/case ref | Stop affected new use, notify owner; no secret data |
| EVT-06 `OperationOutcomeChanged` | Trust | operation ID, source, state, evidence ref, version/time | Reconcile original attempt; never infer invoice delivery from signature success |
| EVT-07 `EvidencePreservationChanged` | Evidence service | package ID, preservation/revalidation version, result, time | Update historic evidence view without changing original signed bytes/time |

### 4 Data inventory

| ID | Record and owner | Required logical fields | Classification, versioning and disposition |
|---|---|---|---|
| D-01 | Trust policy — Security/Legal-approved trust owner | policy ID/version, jurisdiction, route/profile, direction, actor/mode, material class, required checks, signer/seal rule, custody rule, effective interval, approvers/evidence | Sensitive configuration; immutable version, effective-dated. Retain prior versions referenced by operations. |
| D-02 | Applicability/readiness decision — trust service | decision ID, subject/operator scope, capability, purpose, material/policy/authority versions, checks and evidence, outcome/reason, evaluated/next-check times, remediation owner | Sensitive metadata; append-only decisions; current pointer derived. Product gets safe projection only. |
| D-03 | Material/version inventory — trust service | stable material ID, version ID, class, subject/owner, custodian/ref, public certificate fingerprint/chain ref, issuer, key usage, environment, validity, lifecycle state, owner, dependency refs | Restricted security data; no private key. Immutable version plus audited lifecycle events; public material retained for historic proof as policy requires. |
| D-04 | Authority snapshot — identity/authority owner | principal, delegate/signatory, legal subject, capability/route/environment, effective period, source/version, revocation result and evidence reference | Restricted personal/business authority data; trust stores reference or approved snapshot, not unrestricted mandate. |
| D-05 | Dependency edge — trust service | material version, workload/connection/route/policy, queued or in-flight operation, historical obligation, owner and effective interval | Restricted operational metadata; versioned edges; needed for scoped rotation and containment. |
| D-06 | Protected-operation binding — trust service | operation ID, request digest, input hash, principal/signer/seal creator, material/policy/authority versions, route/profile, environment, state, custodian ref and timestamps | Restricted immutable operation plan; corrections use a new version/operation. No key material. |
| D-07 | Evidence package — evidence/archive owner | signed object or immutable object ref, exact hash, signature/seal, chain, status/trust-list/time, authority snapshot, policy/version, validation conclusion, provenance, preservation events, retention class | Highly restricted business/security evidence; append-only and independently retained from private-key version. |
| D-08 | Rotation/incident/reconciliation case — trust/operations | case ID, trigger, intended/observed states, dependencies, owner, approvals, original external refs, next safe action, evidence and closure | Restricted operations record; full history, no secret payload; case closure requires evidenced outcome. |
| D-09 | Audit event — security audit owner | actor/workload, scope, action, reason, request/operation ID, policy/material refs, source/result/time, evidence with sensitive values removed ref | Tamper-evident and access controlled; retention/hold policy separate from application logs. |

### 5 Proposed payload examples

These are illustrative logical payloads for discussion; names and types are **not an approved API**. Identifiers are synthetic and contain no customer data.

```json
{
  "interaction": "INT-05",
  "requestId": "req-synthetic-01",
  "environment": "TEST",
  "legalSubjectRef": "subject-synthetic-01",
  "capability": "SUBMIT_INVOICE",
  "routeProfileRef": "profile-synthetic-01",
  "actorMode": "AUTHORISED_DELEGATE",
  "purpose": "DELEGATED_SIGNING",
  "atTime": "2026-10-05T12:00:00Z"
}
```

```json
{
  "decisionRef": "decision-synthetic-01",
  "result": "ACTION_REQUIRED",
  "reason": "AUTHORITY_EXPIRED",
  "materialVersionRef": "material-version-synthetic-01",
  "policyVersionRef": "policy-synthetic-01",
  "authorityDecisionRef": "authority-synthetic-01",
  "checkedAt": "2026-10-05T12:00:00Z",
  "nextRecheckAt": null,
  "remediationOwner": "ACCOUNTANT_OR_CUSTOMER"
}
```

The response deliberately has no private key, raw mandate or claim that the customer is registered with an external platform. `ACTION_REQUIRED` affects only the named capability/scope.

### 6 Contract decisions before physical design

The Business Identity/trust owner and architecture must select the actual service boundary and physical API/event transport. Security/Legal must approve custody and signer/seal policies. The Spain technical owner must provide issuer/trust-list/status, public-authentication and format/signature profiles. Custodians/providers must prove lookup/idempotency and returned evidence for each protected mutation. Privacy/records owners must approve retention, access and residency by record class. Performance/error budgets require measured volume and service commitments. Until those decisions are recorded, the fields above are a design proposal and the external adapters remain abstract.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

### 1 Review purpose and status

This view links the [Part 1](#part-1-feature-solution-summary), [Part 2](#part-2-logical-feature-specification) and [Part 3](#part-3-logical-service-interactions-and-data-inventory) to observable verification. This document is a **reviewable logical proposal**. All scenarios below are proposed acceptance tests; their external certificates, profiles, legal permissions and service objectives must be selected and evidenced before a design for implementation is approved.

### 2 Lifecycle coverage

| Activity | Requirements | Interactions / records | Acceptance and evidence |
|---|---|---|---|
| CERT-01 Classify | CM-R01 | INT-01; D-01, D-02 | CM-AC01, CM-AC02; approved policy catalogue and negative policy fixtures |
| CERT-02 Authorise | CM-R04, CM-R11 | INT-02; D-04, D-09 | CM-AC03, CM-AC04; authority decision matrix and revocation test |
| CERT-03 Establish custody | CM-R02, CM-R03 | INT-03; D-03, D-09 | CM-AC05; custody/attestation and secret-leak tests |
| CERT-04 Validate | CM-R05 | INT-04; D-01–D-03 | CM-AC06, CM-AC07; chain/status/profile corpus |
| CERT-05 Decide readiness | CM-R01, CM-R05, CM-R11 | INT-05; D-02, EVT-02 | CM-AC02, CM-AC08; per-scope projections |
| CERT-06 Bind and use | CM-R04, CM-R06, CM-R07 | INT-06, INT-09; D-06 | CM-AC09, CM-AC10, CM-AC11; custodian idempotency/lookup proof |
| CERT-07 Preserve | CM-R10, CM-R12 | INT-07, INT-12; D-07, D-09 | CM-AC12; signed-object and evidence integrity checks |
| CERT-08 Rotate | CM-R08 | INT-08; D-03, D-05, D-08; EVT-03/04 | CM-AC13; counterpart and in-flight cutover test |
| CERT-09 Contain | CM-R05, CM-R07, CM-R09 | INT-09; D-05, D-08; EVT-05/06 | CM-AC07, CM-AC10, CM-AC14; scoped incident drill |
| CERT-10 Retire | CM-R10 | INT-10, INT-12; D-03, D-07 | CM-AC15; destruction proof and historic revalidation |

CM-AC16 also checks the country-policy boundary for CERT-01/02/04/06, CM-R01/04/05/06, INT-01/02/04/06 and D-01/D-02/D-06.

Every `CM-R` appears in the matrix. `INT-11` is the safe operational projection used across CERT-05, CERT-08 and CERT-09; its authorisation/redaction is covered by CM-AC08 and CM-AC14. `EVT-01` supports CERT-03, `EVT-07` supports CERT-10. Detailed event delivery and replay tests remain part of the architecture and integration gate.

### 3 Acceptance scenarios

| ID | Given / when | Required result |
|---|---|---|
| CM-AC01 | A route/profile has approved `NOT_REQUIRED` policy; onboarding asks for readiness | It receives a versioned, reasoned no-certificate decision and no upload/provisioning step. |
| CM-AC02 | The policy is missing, conflicting or not effective for the requested actor/route | Readiness is `UNDETERMINED`, dependent activation is blocked and a named policy owner/action is returned. |
| CM-AC03 | An accountant holds a valid certificate but lacks effective authority for one client/capability | Only that client/capability is blocked; other authorised client items continue without data leakage. |
| CM-AC04 | A prior grant is revoked after onboarding was ready | Future dependent use fails at runtime; old decision and previously signed evidence stay unchanged. |
| CM-AC05 | An approved custody flow provisions material | Inventory records one immutable version and public metadata; product responses, logs, events and audit contain no private key or reusable secret. |
| CM-AC06 | A valid workload or transport certificate is offered for invoice signing | The request fails for wrong purpose even though transport authentication could independently remain ready. |
| CM-AC07 | Chain, revocation, status freshness, owner or environment fails/is unknown | New affected use is blocked or undetermined with the exact safe reason; no automatic pass/fallback occurs. |
| CM-AC08 | Two onboarding items share a delegate material reference but have different principals/grants | Each gets its own scoped decision and remediation; a support query cannot enumerate the other item without authority. |
| CM-AC09 | A remote-signing request passes preflight, then its authority/material changes before key use | Use-time recheck prevents the operation or requires a new approved binding; no stale signature is reported. |
| CM-AC10 | Custody times out after possible signing/provisioning | Original operation enters `OUTCOME_UNKNOWN`; reconciliation queries original reference and does not issue a fresh mutation blindly. |
| CM-AC11 | A caller repeats the same operation ID with identical digest, then with a changed input hash | Identical request deduplicates under proven contract; changed input conflicts and requires a new authorised operation. |
| CM-AC12 | An outbound representation is signed/sealed successfully | Exact bytes/hash, actor, material/policy/authority versions, validation/time and provenance are durable before success is exposed. |
| CM-AC13 | A material version approaches expiry and replacement is cut over | Replacement is validated and accepted by affected counterpart; new work uses the effective version while in-flight attempts retain their frozen binding. |
| CM-AC14 | One material version is compromised | Affected new use stops, dependencies and forensic evidence are visible to authorised operators, unaffected isolated scopes continue where safe, and resumption requires reapproval. |
| CM-AC15 | A retired private key is destroyed and its certificate later expires | Authorised historic verification uses retained signed bytes, chain, status/time/policy and preservation evidence; destruction and current expiry alone do not erase the past result. |
| CM-AC16 | The same trust capability is evaluated for Spain and another country with different approved policies | CM-R01/04/05/06: CERT-01/02/04/06 and INT-01/02/04/06 select the correct policy and actor. D-01/D-02/D-06 retain each decision and operation version. Changing one country’s policy does not change the other country’s readiness or earlier evidence. |

Additional negative tests must cover tenant and TEST/production crossover, revoked signer versus valid transport, seal substitution, unauthorised approval/destroy, out-of-order events, duplicate event delivery, stale cache, lost evidence write after key use, invalid inbound trust, replay and provider exit. They are grouped into the corresponding scenarios above; test fixtures and exact expected codes require approved physical contracts.

### 4 Security and operational assurance

| Control claim | Evidence required before pilot or production | Owner |
|---|---|---|
| Material cannot cross tenant, legal-subject, operator or environment boundaries | Negative authorisation tests at every interaction; trusted context enforcement; audit of blocked attempts | Security and engineering |
| Key operations are protected and attributable | Custodian/HSM or remote-service design review, access policy, non-exportability/backup proof as applicable, dual-control and key-use audit | Trust owner and Security |
| A signer, delegate and operator seal are not confused | Approved legal/authority matrix, policy fixtures, API labels, actor evidence and negative substitution tests | Spain Legal, Business Identity and Product |
| Rotation does not cause outage or change in-flight work silently | Dependency inventory, expiry alerts, counterpart conformance, cutover/rollback and queue tests | Operations and exchange owner |
| Unknown outcomes are recoverable without duplicate use | Custodian lookup/idempotency contract, fault-injection, reconciliation runbook and unresolved-case dashboard | Trust owner and Operations |
| Historical proof survives expiry, key destruction and provider exit | Evidence-package completeness test, restore/export test, independent verification and retention/hold policy | Records, Legal and Security |
| Service can operate at launch scale | Measured class/provider volumes, latency, queue/backlog, alert and recovery baselines; approved target and capacity test | Product and Operations |

### 5 Decision and evidence gates

| Gate | Decision or missing evidence | Accountable owner | Effect if unresolved |
|---|---|---|---|
| G1 Trust owner | Which Sage Business Identity/service team owns inventory, key operations, validation and preservation? | Business Identity and architecture | Blocks service boundary, API ownership and delivery plan |
| G2 Legal actor | Which direct/delegated/Sage-managed signing and operator-seal modes are permitted for each Spain route/profile? | Spain Legal, Compliance and Security | Blocks trust-policy activation and signing design |
| G3 Custody | Which key classes may be customer/provider/Sage held; what import/export and dual-control rules apply? | Security and trust owner | Blocks provisioning implementation |
| G4 External profiles | Official public/AS2/AS4/signature profiles, accepted issuers/trust lists, status source and freshness | Spain technical owner and external parties | Blocks conformance and production validation |
| G5 Failure contract | Custodian/provider idempotency or authoritative lookup for each protected mutation | Trust owner and supplier | Blocks automatic retry and recovery automation |
| G6 Retention | Evidence, key destruction, residency, legal hold and access schedules by class | Legal, Privacy and Records | Blocks production data handling and exit |
| G7 Operations | Per-class warning/overlap thresholds, owners, coverage, RTO/RPO and response commitments | Security, Product and Operations | Blocks production runbooks and service objectives |
| G8 Regulatory/public | Public-solution authentication/representation technical contract and exact certificate requirement | Spain regulatory/technical owner | Blocks public-route certificate-dependent activation |

These gates are drawn from the open questions in [PRD-SEI-226](../prds/PRD-SEI-226-security-trust-identity-data-audit.md), [PRD-SEI-101](../prds/PRD-SEI-101-public-platform-onboarding.md) and [PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md). The source PRDs remain the authoritative open-question records until approved ADRs replace individual decisions.

### 6 Readiness judgement

This document is ready for a Product, Business Identity, Security, Legal, Spain technical and Operations solution review. It is **not approved for implementation or external activation**. The first review should resolve G1–G3 and select one concrete certificate class/route as the reference slice; G4–G8 then determine conformance, pilot and production gates. No document status or Confluence publication is changed by this review view.
