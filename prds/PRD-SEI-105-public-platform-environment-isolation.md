---
id: PRD-SEI-105
title: Phase 1 — Public Platform Environment Isolation
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-25
updated: 2026-08-25
reviewers: []
related:
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-107
  - PRD-SEI-212
  - PRD-SEI-215
  - PRD-SEI-226
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837610648"
  page_id: "848078351"
  title: "Environment Routing (TEST vs PRO)"
  layout: two_left_sidebar
  toc: true
---

# Phase 1 — Public Platform Environment Isolation

## Decision summary

TEST and production are separate trust and evidence boundaries. The target environment must be resolved from trusted deployment, account, credential and configuration context; a caller-controlled header or payload must not silently redirect a request or default an ambiguous request to TEST.

No official SPFE sandbox, homologation behaviour, simulation certificate or production onboarding endpoint is treated as confirmed until the ministerial technical order and provider artefacts identify it. Sage may still provide an internal test mode, but it must be labelled as simulation and must not claim AEAT/public-solution acceptance.

Test records are retained under an approved non-production policy and isolated from production. They are not promoted as production identity, authority, credential, registration or readiness evidence.

> **Product principle:** Environment is a trusted execution boundary, not a convenience parameter.

This document owns environment selection and isolation for Phase 1 onboarding. Generic security is owned by PRD-SEI-226 and retry/reconciliation by PRD-SEI-107/215.

## Source relationship

This is the canonical Git source proposed for [Environment Routing (TEST vs PRO)](https://confluence.sage.com/spaces/DNBU/pages/848078351/Environment+Routing+TEST+vs+PRO), reviewed at version 2. It retains the original intent to distinguish testing from live compliance while removing unsupported environment contracts and unsafe request-driven routing.

### Original draft detail disposition

| Original detail | Treatment in this canonical source |
|---|---|
| `X-Environment` plus payload `target_environment` | May be accepted only as a checked hint; trusted server context owns the effective environment |
| Missing environment defaults to TEST | Replaced by explicit rejection of missing/ambiguous context |
| TEST uses AEAT sandbox/homologation | Retained as an open official-environment question; internal mode is labelled simulation |
| TEST accepts simulation certificate and only checks X.509 | Removed as unverified; credential policy requires official/security approval |
| TEST records do not persist | Replaced by isolated retention under an approved non-production policy |
| Production permanently registers the business | Removed until an official registration operation/acknowledgement is evidenced |
| Live compliance locks identity for a calendar cycle | Removed as unsupported; identity/profile changes are effective-dated |
| Fake NIF values such as `ERR...` inject errors | Replaced by authorised scenario controls and synthetic valid/invalid fixtures outside identity fields |

## Outcome and environment classes

| Environment class | Purpose | External claim permitted | Evidence use |
|---|---|---|---|
| Internal simulation | Exercise Sage validation, personas, state and failures without AEAT | None; clearly labelled simulated | Engineering/QA only |
| Official TEST/homologation | Exercise confirmed public-solution test contract when available | Only acknowledgements defined by that contract | Test certification/pilot evidence; never production readiness by itself |
| Production | Execute approved live public-solution operations | Only confirmed authoritative outcomes | Production compliance evidence |

The implementation may have more deployment stages, but every stage must resolve to a named environment class and trust policy.

## Concepts that must remain separate

| Concept | Meaning | Must not be confused with |
|---|---|---|
| Deployment environment | Sage runtime/account boundary | External provider environment |
| External target | Confirmed endpoint/account/service class | A string supplied by a client request |
| Simulation | Sage-generated deterministic behaviour | AEAT sandbox result |
| Homologation | Official conformance/test process if supplied | General development environment |
| Production readiness | Approved identity, authority, credentials, contract and operational gates | Successful simulation/test request |
| Test evidence | Trace of non-production behaviour | Legal invoice, production registration or compliance evidence |
| Failure injection | Controlled scenario facility | Fake NIF embedded in customer identity fields |

## Business scenarios

| ID | Scenario | Expected outcome |
|---|---|---|
| S1 | Developer exercises onboarding before an official sandbox exists | Sage simulation tests local behaviour and is explicitly labelled non-authoritative |
| S2 | Official TEST contract becomes available | Environment profile is versioned with endpoint, credentials, capabilities and evidence semantics |
| S3 | Production user sends a TEST selector | Trusted production context wins or mismatch is rejected before external access |
| S4 | Environment context is absent/ambiguous | Request is rejected with safe configuration guidance; no silent default |
| S5 | Test credential is supplied to production | Request is rejected; credential is not copied or promoted |
| S6 | Same legal subject exists in TEST and production | Records remain environment-qualified and cannot overwrite one another |
| S7 | Operations injects timeout/rejection scenario | Scenario control is authorised and isolated; official identity fields stay valid/synthetic |
| S8 | Production endpoint is unavailable | Production retry/recovery policy applies; request never fails over to TEST |
| S9 | Customer completes TEST onboarding | Production case starts/re-evaluates required controls independently |
| S10 | External contract version changes | New environment profile becomes effective prospectively; historical evidence preserves prior version |

## Business rules

| ID | Condition | Rule | Status |
|---|---|---|---|
| BR1 | Request targets an external service | Resolve environment through trusted server-side context | Proposed security control |
| BR2 | Caller supplies an environment hint | Validate against trusted context; never use it as sole route authority | Proposed |
| BR3 | Required context is missing/conflicting | Reject before credential use or external call | Proposed |
| BR4 | TEST and production exist | Separate endpoints, accounts, credentials, storage, queues, audit, monitoring and access | Proposed |
| BR5 | Official sandbox is not evidenced | Describe testing as Sage simulation only | Evidence rule |
| BR6 | Test execution completes | Do not set production readiness or registration | Product boundary |
| BR7 | Failure scenario is requested | Use an authorised scenario mechanism/fixture, not reserved-looking tax identity values | Data-quality/security rule |
| BR8 | Production dependency fails | Never route to TEST as fallback | Compliance/safety rule |
| BR9 | Evidence is retained | Include environment and contract/version in every decision and event | Historical continuity |
| BR10 | Test data is deleted | Apply approved non-production retention, not an assumption that no test evidence persists | Privacy/operations gate |

## Scope and non-goals

### In scope

- Trusted environment resolution and mismatch rejection.
- Internal simulation, official test/homologation and production classifications.
- Endpoint/account/credential/data/queue/monitoring isolation.
- Environment-qualified onboarding identity, authority, verification and readiness.
- Synthetic data and fault-injection controls.
- Contract/version changes and historical evidence.
- Promotion rules, release gates, kill controls and production fallback prohibition.

### Non-goals

- Inventing AEAT sandbox URLs, certificates, behaviours, SLAs or error triggers.
- Defining invoice-submission payloads.
- Treating TEST as free-form customer demo mode with production data.
- Automatically copying credentials, authority or verification results between environments.
- Setting exact retention or availability targets without owners/baselines.

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238), Article 11 and final provision 3 | Public-solution technical, authentication, representation and communication details depend on ministerial order | Primary law; no environment contract established by the decree | Sandbox/production bindings remain delivery gates |
| Confluence page 848078351 v2 | Proposed TEST/PRO split, header selection, test certificates and error identifiers | Internal discovery; external claims unverified | Preserve split; replace routing/default/test-data assumptions |
| PRD-SEI-226 | Trust, credential, data and audit principles | Shared discovery requirements | Security and isolation baseline |
| PRD-SEI-107/215 | Operation safety, retry and reconciliation | Shared requirements | Production failure behaviour |

## Proposed environment profile

**Proposed model; architecture and security approval required.**

| Field | Purpose |
|---|---|
| `environmentProfileId` | Stable reference to a versioned execution boundary |
| `class` | `SIMULATION`, `OFFICIAL_TEST`, `PRODUCTION` |
| `sageDeployment/account` | Trusted internal boundary |
| `externalService/endpointRef` | Approved provider target reference, not a client URL |
| `credentialPolicyRef` | Allowed credential types/custodian/rotation for this environment |
| `capabilityMatrixVersion` | Confirmed operations supported in this environment |
| `contract/schemaVersion` | External contract used by evidence and mapping |
| `dataClassification/retentionRef` | Environment-specific data controls |
| `effectiveFrom/effectiveTo/status` | Version lifecycle and disablement |

Every onboarding case, work item, verification finding, authority decision, credential reference and readiness decision must carry the environment profile or immutable snapshot.

## Detailed journeys

### J1 — Internal simulation

1. Authorised tester uses a non-production Sage deployment and synthetic client fixture.
2. Trusted configuration resolves `SIMULATION`; the caller cannot elevate it.
3. Local validators/state/failure paths run without public-solution access.
4. Results are labelled simulated and retained in isolated test evidence.

### J2 — Official test

1. Release process selects an approved official-test environment profile.
2. Test-specific account and credential policy are applied.
3. Only capabilities evidenced by the test contract are called.
4. Acknowledgements retain test/contract context and satisfy named release gates only.

### J3 — Production

1. Production deployment resolves the approved production profile server-side.
2. Product/client/environment/credential relationships are revalidated.
3. Mismatched request hints or credentials are rejected before transmission.
4. Approved production operation runs and its evidence is marked production.

### J4 — Contract/environment change

1. New endpoint/schema/capability configuration is staged as a new profile version.
2. Simulation and official test gates run as available.
3. Controlled activation selects the new profile for future work.
4. In-flight and historical work retains its original profile/contract context.

## Functional requirements

| ID | Requirement |
|---|---|
| FR1 | The system must resolve the effective environment from trusted deployment/account/configuration context. |
| FR2 | A client header or payload must not be the sole authority for selecting an external environment. |
| FR3 | Missing, ambiguous or conflicting environment context must be rejected before credential retrieval or external access. |
| FR4 | Production must never fall back to TEST/simulation after failure. |
| FR5 | Simulation, official TEST and production must be distinguishable in cases, events, evidence, logs and customer/operator views. |
| FR6 | Each environment must have independently governed endpoint, account, credential, data, queue, audit and monitoring resources. |
| FR7 | A credential must be bound to permitted environment/purpose and rejected outside that binding. |
| FR8 | Test identity, authority, verification and readiness outcomes must not automatically satisfy production controls. |
| FR9 | Promotion must create/re-evaluate production context rather than copy mutable test state as production evidence. |
| FR10 | Simulation must not emit public-solution acknowledgements or claim official acceptance. |
| FR11 | Official-test behaviour must be limited to confirmed contract capabilities and documented evidence meaning. |
| FR12 | Failure injection must use authorised scenario controls/fixtures, not magic production identifier values. |
| FR13 | Test data must be synthetic or approved/masked under environment-specific privacy policy. |
| FR14 | Environment profile/version must be captured in every external request, result and readiness decision. |
| FR15 | Profile changes must apply prospectively and preserve context for in-flight/historical work. |
| FR16 | Operations must be able to disable an environment/capability/cohort without deleting evidence or affecting unrelated environments. |
| FR17 | Manual recovery must not cross environment boundaries. |
| FR18 | The service must expose safe diagnostics for environment mismatch, profile version, external target reference and credential policy without exposing secrets. |

## Failure and recovery

| Failure | Behaviour | Prohibited behaviour |
|---|---|---|
| Missing environment context | Reject and identify configuration owner | Default to TEST |
| Conflicting header/payload/context | Reject and audit mismatch | Choose caller value |
| Wrong-environment credential | Reject before external call | Copy/convert credential |
| TEST endpoint unavailable | Apply test policy and report test failure | Route to production |
| Production endpoint unavailable | Apply production retry/reconciliation | Route to TEST |
| Unknown external environment outcome | Reconcile within same profile/contract | Query another environment |
| Profile changed mid-flight | Complete/reconcile using original snapshot where safe | Rewrite work to new profile |
| Test-data leak attempt | Deny/quarantine and security audit | Persist in production |

## Non-functional requirements

- NFR1: Enforce network, identity/access, secret, data and observability isolation between environment classes.
- NFR2: Encrypt credentials and data; never log secret material or full personal identifiers.
- NFR3: Audit environment resolution inputs, effective profile, actor, operation and result.
- NFR4: Monitor cross-environment mismatches and attempts as security signals.
- NFR5: Retain test/production evidence under independently approved schedules.
- NFR6: Support repeatable simulation fixtures without customer or production data.
- NFR7: Derive performance/capacity targets per environment from approved contracts and load profiles.
- NFR8: Make environment labels unambiguous and accessible in customer/developer/operations experiences.

## Acceptance criteria

| ID | Given/when/then |
|---|---|
| AC1 | Given production trusted context and a TEST request hint, when intake occurs, then it is rejected before credential retrieval/external access. |
| AC2 | Given no resolvable environment, when a request arrives, then it fails explicitly and does not default to TEST. |
| AC3 | Given a test credential in production, when an external operation is requested, then it is rejected and audited. |
| AC4 | Given a completed simulation, when status is displayed, then it is labelled non-authoritative and production readiness is unchanged. |
| AC5 | Given successful official TEST onboarding, when production begins, then production identity, authority, credential and external controls are independently evaluated. |
| AC6 | Given a production outage, when retry policy exhausts, then work remains production/recoverable and is never sent to TEST. |
| AC7 | Given failure injection, when an error scenario is requested, then the control is outside official identity fields and restricted to authorised test context. |
| AC8 | Given an environment profile change, when old evidence is viewed, then its original profile/contract version remains visible. |
| AC9 | Given support accesses a case, when diagnostics are shown, then the effective environment is clear while endpoint secrets/credentials remain hidden. |
| AC10 | Given environment disablement, when invoked, then affected future work stops without deleting historical evidence or disabling other environments. |

## Measures, gates and open questions

| Measure | Purpose | Owner |
|---|---|---|
| Environment mismatch attempts | Detect integration/security defects | Security/engineering |
| Credential-environment rejection | Validate binding and onboarding UX | Security/product |
| Test-to-production escaped defects | Measure release quality | QA/engineering |
| Production calls reaching non-production | Must remain zero | Security/operations |
| Evidence with complete environment/version | Audit completeness | Compliance/QA |

| Open question | Owner | Blocks |
|---|---|---|
| What official SPFE test/homologation environments and contracts exist? | AEAT liaison | External test/pilot |
| Which credentials and identity data are permitted in official TEST? | Security/legal/AEAT liaison | Test design |
| What data/retention policy applies to simulation and homologation evidence? | Privacy/security | Operations approval |
| Which products/deployments/accounts are trusted to resolve each environment? | Architecture/platform | Build |
| What release, rollback and kill criteria apply to profile changes? | Engineering/operations/product | Production |

**Readiness: discovery-ready draft.** External TEST and production integration remain blocked by official artefacts and approved environment/security design.

## Decisions and change log

| Decision | Status |
|---|---|
| Environment is trusted server-side context, not caller-controlled routing | Proposed for approval |
| Missing/conflicting context is rejected; there is no silent TEST default | Proposed for approval |
| Test evidence is isolated and retained under policy, never promoted as production evidence | Proposed for approval |
| Existing Confluence page remains the stable publishing target | Accepted mapping; publication disabled |

| Date | Version | Change | Evidence |
|---|---|---|---|
| 2026-08-25 | Initial canonical draft | Preserved TEST/PRO separation; replaced header/default, simulation-certificate, no-retention and magic-NIF assumptions with trusted environment profiles and evidence gates | Confluence v2, Royal Decree 238/2026, PRD-SEI-101/107/226 |
