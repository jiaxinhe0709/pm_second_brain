---
id: PRD-SEI-106
title: Phase 1 — Spain NIF/NIE Verification and Census Lookup
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
  - PRD-SEI-108
  - PRD-SEI-226
  - PRD-SEI-231
  - PRD-SEI-235
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610648"
  page_id: "855187086"
  title: "NIF/NIE Verification & Lookup API -DRAFT"
  layout: two_left_sidebar
  toc: true
---

# Phase 1 — Spain NIF/NIE Verification and Census Lookup

## Decision summary

Spain uses NIF as the tax-identity role required for supplier and recipient mentions in the public e-invoicing solution. The value and validation family depend on the subject:

- a Spanish natural person’s DNI generally serves as NIF;
- a foreign natural person’s NIE generally serves as NIF;
- legal persons and entities use an assigned entity NIF;
- exceptional assigned NIF cases, including natural persons without DNI/NIE, must be represented explicitly rather than forced into the common formats.

NIE is not a Spanish equivalent of SIRET. It does not identify an establishment under a legal entity. Establishment/presence, invoice-party identity, delegated actor and network destination remain separate records.

Verification has distinct layers: normalization, structural/check-character validation, census identity matching, applicability, authority and routing. Passing one layer must not imply success in another.

The AEAT “Comprobación de un NIF de terceros a efectos censales” service is an identity-data quality check. `IDENTIFICADO` does not prove that a party may trade, is in mandatory B2B scope, has selected a route or has authorised an accountant.

> **Product principle:** Preserve the official response, but never give it a stronger meaning than its source.

## Source relationship

This is the canonical Git source proposed for [NIF/NIE Verification & Lookup API -DRAFT](https://confluence.sage.com/spaces/DNBU/pages/855187086/NIF+NIE+Verification+Lookup+API+-DRAFT), reviewed at version 7. It preserves local and external verification use cases while correcting the identity taxonomy, result meanings, batch-limit interpretation, privacy and hard-block assumptions.

### Original draft detail disposition

| Original detail | Treatment in this canonical source |
|---|---|
| Local validation, AEAT lookup and future directory as three layers | Preserved, but renamed structural validation, census identity matching and separate routing discovery |
| DNI/NIF/NIE all use one modulo-23 rule | Replaced by approved subject/identifier-class validator selection |
| Entity `CIF` uses one modulo-11 rule | Legacy terminology removed from canonical scheme; entity-class controls require approved catalogue/tests |
| AEAT confirms “active and permitted to trade” | Corrected to the official census identity-quality response semantics |
| Sage uses “our Qualified FNMT certificate” | Removed as an approved design; access/authentication/custody require service/security evidence |
| `IDENTIFICADO` maps to `VALID`; baja/revoked hard-block invoice | Split into official response, identity decision and separate country capability policy |
| Future national directory returns `SPFE` or `PDP_ID` from October 2027 | Retained only as an open routing research question; no date or directory contract is approved |
| REST single/batch endpoints | Preserved as conceptual capabilities; URL/payload/transport remains architecture-owned |
| Batch maximum 10,000 | Corrected: official interactive CSV guidance currently says 20,000; neither number is an approved Sage API limit |
| `<50ms`, `<800ms`, VALID 30-day and invalid 24-hour cache | Retained as target categories only; numeric targets/TTL require contract, baseline and owner |
| Named NuGet packages | Removed as requirements; implementation dependency needs existence, security, licence and maintenance assessment |

## Identity catalogue

| Subject | Official identity treatment | Model requirement |
|---|---|---|
| Spanish natural person/autónomo | DNI generally serves as NIF | `scheme=ES:NIF`, natural-person subject, `sourceDocumentType=DNI` |
| Foreign natural person/autónomo | NIE generally serves as NIF | `scheme=ES:NIF`, foreign-natural-person subject, `sourceDocumentType=NIE` |
| Natural person without DNI/NIE where AEAT assigns another NIF | Assigned NIF, including relevant provisional/special cases | Explicit source/assignment type and evidence; do not pretend it is DNI/NIE |
| Spanish legal person/entity | Entity NIF assigned by tax administration | Entity subject/identifier-class rules |
| Foreign/non-resident entity or permanent establishment | Assigned NIF where required | Separate non-resident/presence facts; no SIRET-like hierarchy inferred |
| Establishment/branch/site | Separate presence record | No universal subordinate identifier derived from NIF/NIE |
| Network destination | Scheme-qualified participant/address record | Never inferred solely from NIF/NIE |

## Verification layers

| Layer | Question answered | Typical result | Must not imply |
|---|---|---|---|
| Normalization | Can input be represented consistently without changing legal value? | normalized/display forms | Validity |
| Structural validation | Does value match the approved class and check-character rules? | valid/invalid/rule version | Census existence |
| Census identity matching | Do submitted identifier/name data match AEAT census semantics? | official response mapping | E-invoicing scope, trading permission or route |
| Applicability | Does the mandate apply to this subject/transaction/time? | required/exempt/not applicable/undetermined | Identity match |
| Delegated authority | May this actor perform this capability for the subject? | effective/denied/undetermined | Credential or census validity |
| Invoice mapping | Which supplier/recipient field and identity role apply? | party/field mapping | Network address |
| Routing discovery | Where must the invoice be delivered? | scheme-qualified destination/route | Tax identity alone |

## AEAT census response semantics

The currently reviewed AEAT guidance distinguishes natural-person and entity responses.

| Official response | Subject | Source meaning | Product treatment |
|---|---|---|---|
| `IDENTIFICADO` | Natural person | NIF and supplied name data identify the taxpayer | Record matched identity data; no broader conclusion |
| `NO IDENTIFICADO-SIMILAR` | Natural person | Minor name differences; AEAT returns census name data | Correct/review personal data under privacy controls |
| `NO IDENTIFICADO` | Natural person | Supplied data do not identify the taxpayer | Correct/review; do not label nonexistent universally |
| `IDENTIFICADO` | Entity | NIF identifies entity; current NIF and business name returned | Record identity match/current value |
| `NO IDENTIFICADO` | Entity | NIF does not identify under supplied request semantics | Correct/review |
| `IDENTIFICADO-BAJA` | Entity | Entity identified and census state is baja | Apply separately approved Spain policy/manual review |
| `IDENTIFICADO-REVOCADO` | Entity | Entity identified and NIF is revoked | Apply separately approved Spain policy/manual review |
| `NO PROCESADO` | Applicable technical contract | Item was beyond processing or not handled | Retry/resubmit only under confirmed safe contract |

The product must preserve raw official code, mapped category, source/version/time and a plain-language explanation. It must not turn `BAJA` or `REVOCADO` into a universal invoice-creation prohibition without an approved legal/business rule for the relevant capability.

## Business scenarios

| ID | Scenario | Expected outcome |
|---|---|---|
| S1 | Spanish company NIF is entered | Entity-class format/check rules run; legal subject is separate from workspace |
| S2 | Spanish autónomo enters DNI | DNI-derived value is represented as NIF for the natural-person subject |
| S3 | Foreign autónomo enters NIE | NIE-derived value is represented as NIF; no establishment is created |
| S4 | Natural person has an assigned non-DNI/NIE NIF | Explicit exceptional class/evidence is captured |
| S5 | Format passes but check character fails | Local validation rejects before external lookup with rule-specific correction |
| S6 | Census returns similar name | Product asks an authorised actor to review/correct and minimises returned personal data |
| S7 | Entity returns current NIF after legal-form change | New/current identifier relationship is recorded with effective evidence; history remains |
| S8 | Entity returns baja/revoked | Policy/manual review decides capability effect; result is not overstated |
| S9 | Accountant portfolio requires verification | Each client is independently authorised and checked; limits follow approved integration contract |
| S10 | External lookup is unavailable | Structural result remains available and external verification is pending/unavailable, not falsely valid |
| S11 | Same value is proposed as route | Routing is rejected/undetermined until a separate scheme-qualified address is evidenced |
| S12 | Verification cache has expired or identity changed | Recheck policy applies prospectively; historical decision keeps original evidence |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Identifier is captured | Store scheme, normalized value, subject, source-document type, purpose, issuer, validity and evidence | PRD-SEI-231 |
| BR2 | Natural-person NIF is processed | Apply the correct DNI/NIE/assigned-NIF class, not a universal regex/modulo rule | AEAT identity model |
| BR3 | Entity NIF is processed | Use current approved entity-prefix/check-character rules and terminology; do not use legacy CIF as canonical scheme | AEAT identity model |
| BR4 | Local validation passes | It proves only structural validity under the recorded validator version | Confirmed logic boundary |
| BR5 | Census check is used | State its data-quality purpose and preserve official semantics | AEAT service documentation |
| BR6 | Census result is baja/revoked | Apply an approved capability policy or manual review; do not infer universal prohibition | Open Spain policy |
| BR7 | Interactive/CSV limit is documented | Do not treat it as an API limit unless the approved integration contract says so | Evidence boundary |
| BR8 | Verification result is reused | Apply approved freshness, identity-change and purpose rules; no invented 30/24-day TTLs | Open policy |
| BR9 | Personal name data is returned | Minimise access/display/retention and audit viewing | Privacy requirement |
| BR10 | Identifier participates in invoice/routing | Use explicit role mappings; NIF identity does not become participant address by implication | PRD-SEI-108/231/233 |

## Scope and non-goals

### In scope

- Spain NIF identity taxonomy for natural persons and entities.
- Normalization and local structural/check-character validation.
- Versioned validator rules, fixtures and negative cases.
- Proposed AEAT census verification adapter and result mapping.
- Direct and portfolio verification orchestration.
- Correction, re-verification, current/previous identifier and historical evidence.
- Privacy, caching/freshness decision surface, audit and operations.

### Non-goals

- Determining transaction applicability, tax treatment or place of supply.
- Proving a party is permitted to trade or is ready for e-invoicing.
- Establishing delegated authority.
- Resolving an invoice network destination.
- Approving a REST endpoint, NuGet library or specific implementation package.
- Treating the AEAT 20,000-record interactive CSV limit as Sage API capacity.
- Defining final public-solution supplier/recipient field mappings, owned with PRD-SEI-108/212.

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [AEAT — NIF for natural persons](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/alta-modelo-036/casilla-110-solicitud-numero-identificacion-036/personas-fisicas.html) | DNI generally serves as NIF for Spanish natural persons; NIE generally serves as NIF for foreign natural persons; assigned NIF cases exist | Primary official guidance | Identity catalogue and validator selection |
| [AEAT — NIF for legal persons/entities](https://sede.agenciatributaria.gob.es/Sede/censos-nif-domicilio-fiscal/solicitar-nif/nif-juridica.html) | Entities use NIF and its prefix carries entity/legal-form information | Primary official guidance | Entity class and subject mapping |
| [AEAT — third-party NIF check](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-030/comprobacion-nif-terceros-efectos-censales.html) | Identity-data quality purpose; unit/list/CSV; official response meanings; CSV UI limit 20,000 | Primary operational guidance; UI is not integration contract | Result semantics and limit boundary |
| [AEAT identification-quality web service manual](https://sede.agenciatributaria.gob.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Modelos_y_formularios/Declaraciones/Modelos_01_al_99/030_036_037/WS_Masivo/Manual_Tecnico_WS_Masivo_Calidad_Datos_Identificativos.pdf) | SOAP structures and response categories | Official technical manual v1.8/2021; current availability/auth/limits require confirmation | Adapter evidence gate |
| [Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238), Article 11.3 | Public-solution invoice requires correctly informed supplier and recipient NIF mentions | Primary law; syntax/order detail pending | Invoice-role handoff |
| Confluence page 855187086 v7 | Draft layers, results, batch and API proposals | Internal discovery; several meanings/limits/SLAs/packages unsupported | Preserve intent, correct details |

## Proposed data and capability model

| Record/capability | Minimum contract |
|---|---|
| Identifier | identifier ID, `ES:NIF`, normalized/display values, subject ID/type, source-document type, purpose, validity |
| Validator result | validator/rule version, identifier class, result/reasons, checked time |
| Verification request | subject/identifier/name evidence reference, purpose, environment, actor/authority, correlation |
| Official response | raw code/value reference, mapped category, returned-current-identifier/name handling, source contract/version/time |
| Verification decision | result, confidence/scope, freshness/recheck, policy version, evidence reference |
| Identifier relationship | previous/current identifier, relationship reason/effective time/source |

Proposed client capabilities are: normalize, validate locally, request approved external verification, retrieve redacted status/evidence and re-verify. URL shapes and sync/async transport remain architecture decisions.

## Detailed journeys

### J1 — Local validation

1. Caller supplies legal subject, subject type, claimed identity/source type and value.
2. Service normalizes presentation without changing legal value.
3. Validator selects the approved class/rule version.
4. Format and check-character rules run.
5. Result returns safe correction reasons and stores the validator version.

### J2 — Census verification

1. Authorised purpose/actor submits a structurally valid identifier and required name/business-name data.
2. Adapter uses approved environment/authentication/service contract.
3. Official response is preserved and mapped without semantic inflation.
4. Personal returned data is minimised and protected.
5. Onboarding/applicability/authority components consume only the specific result they need.

### J3 — Correct and re-verify

1. Mismatch/similar result creates an action-required finding.
2. Authorised actor corrects identity evidence or confirms the current official value.
3. New verification revision runs.
4. Prior request/result remains historically auditable.

### J4 — Entity identifier changes

1. Official response returns a current NIF for an entity after an eligible change.
2. Service records previous-to-current relationship and effective evidence.
3. Future contexts use the approved current identity.
4. Historical invoices/decisions retain the identifier snapshot originally used.

## Functional requirements

| ID | Requirement |
|---|---|
| FR1 | The service must identify legal subject separately from Sage tenant/workspace and from the identifier value. |
| FR2 | Every identifier must store scheme, subject, purpose, source-document/assignment class, normalized value, validity and evidence. |
| FR3 | The model must treat DNI/NIE as sources/classes through which a natural person’s NIF is represented, not establishment or routing IDs. |
| FR4 | Exceptional assigned NIF cases must be representable without mislabelling them DNI/NIE/entity NIF. |
| FR5 | Local validation must select an approved rule set using subject and identifier class. |
| FR6 | Local validation must test check-character/control rules as well as format and record validator version. |
| FR7 | Documentation/tests must label examples synthetic-positive or synthetic-negative and verify expected outcome. |
| FR8 | The service must distinguish normalized, structurally valid, census matched and policy-ready states. |
| FR9 | External census verification must require an approved purpose, caller authority, environment and service contract. |
| FR10 | The adapter must preserve official response code/semantics and source/version/time. |
| FR11 | `IDENTIFICADO` must not be mapped to trading permission, mandate applicability, route or delegated authority. |
| FR12 | Similar/mismatch results must support correction without exposing returned personal data beyond approved purpose. |
| FR13 | Baja/revoked results must invoke a separately approved Spain policy/manual-review result rather than an undocumented universal hard block. |
| FR14 | `NO PROCESADO`, throttle, timeout and technical error must remain distinct from identity mismatch. |
| FR15 | Direct and batch verification must produce the same per-subject semantics. |
| FR16 | Batch processing must preserve per-client authority/isolation and return independent outcomes. |
| FR17 | Capacity/limits must derive from the approved technical contract and measured demand; UI CSV limits must be labelled separately. |
| FR18 | Cache/freshness/recheck policy must be versioned by purpose/result and approved; no hard-coded unsupported TTL is allowed. |
| FR19 | Identity or official current-value changes must create effective-dated relationships and new decisions without rewriting history. |
| FR20 | NIF/NIE values and returned names must be redacted from logs, URLs, metrics and general error payloads. |
| FR21 | Access to raw/returned personal data must be purpose-bound, least-privilege and audited. |
| FR22 | Verification evidence retention/deletion must follow approved legal/privacy schedules. |
| FR23 | The service must expose safe operations evidence including correlation, source, time, mapped result and next action. |
| FR24 | Invoice and routing consumers must use explicit identifier-role/address mappings rather than infer them from raw value. |

## Failure and recovery

| Failure | Classification | Behaviour |
|---|---|---|
| Unsupported class/ambiguous subject | Correctable | Request subject/source evidence; no guessed validator |
| Format/check failure | Correctable local | Stop before external call; safe field reasons |
| Similar/mismatch | Business verification | Correct/review; preserve official semantics |
| Baja/revoked | Policy review | Apply approved rule/manual review; no semantic inflation |
| Auth/authority failure | Security | Deny external check; audit without exposing subject |
| External timeout/read failure | Technical/transient | Retry only under approved safe contract |
| `NO PROCESADO` | Capacity/technical | Resume under confirmed contract; not identity invalid |
| Duplicate request | Duplicate | Return existing result within idempotency/freshness scope |
| Internal persistence failure | Recoverable/unknown | Reconcile request/result correlation; no blind repeat if contract unsafe |
| Concurrent identity correction | Conflict | Version-check and preserve one effective revision |

## Non-functional requirements

- NFR1: Apply privacy classification and least privilege to NIF/NIE/name/evidence data.
- NFR2: Encrypt sensitive data and use tokenised/redacted display outside approved identity views.
- NFR3: Keep validator rules deterministic, versioned and covered by positive/negative/property tests.
- NFR4: Make external verification idempotent/correlation-addressable under its approved contract.
- NFR5: Monitor validation outcome distribution, external health, stale evidence and policy-review age using safe dimensions.
- NFR6: Separate TEST/production credentials, data and evidence under PRD-SEI-105.
- NFR7: Establish latency, cache, batch and availability targets from contract/baselines before delivery approval.
- NFR8: Provide accessible, actionable correction messages without presenting tax/legal conclusions beyond evidence.

## Acceptance criteria

| ID | Given/when/then |
|---|---|
| AC1 | Given a foreign natural-person sole trader with NIE, when captured, then the identifier is represented as `ES:NIF` with NIE source type and no establishment ID is inferred. |
| AC2 | Given an entity NIF, when validated, then entity-class rules are used and the canonical scheme is not `CIF`. |
| AC3 | Given a value matching regex but failing check character, when validated, then it fails before external lookup with rule/version evidence. |
| AC4 | Given `IDENTIFICADO`, when mapped, then the result states census identity match only and does not mark e-invoicing eligibility or route readiness. |
| AC5 | Given `NO IDENTIFICADO-SIMILAR`, when displayed, then correction is possible and returned personal data is restricted/audited. |
| AC6 | Given `IDENTIFICADO-BAJA` or `IDENTIFICADO-REVOCADO`, when onboarding consumes it, then the approved policy/manual-review outcome is used rather than an undocumented universal invoice block. |
| AC7 | Given the public UI documents 20,000 CSV rows, when product batch limits are configured, then that number is not used as an API limit without matching technical-contract evidence. |
| AC8 | Given an unavailable external service, when local validation passed, then the profile shows structural success plus external pending/unavailable, not `VALID` overall. |
| AC9 | Given an entity’s current NIF is returned, when adopted, then future contexts use it while historical evidence retains the prior value. |
| AC10 | Given a raw identifier in an error condition, when logs/status/webhooks are generated, then the full value is absent outside approved secure evidence. |
| AC11 | Given the same NIF value is proposed as a network route, when routing evaluates it, then a separate eligible scheme/address is required. |
| AC12 | Given a cached result outside approved freshness, when readiness is evaluated, then it is rechecked or marked stale according to policy. |

## Measures, gates and open questions

| Measure | Purpose | Owner |
|---|---|---|
| Structural failure by rule/version | Improve data capture/validator quality | Product/data |
| Census match/similar/mismatch by subject class | Measure identity-data quality | Product/compliance |
| Baja/revoked policy-review age | Avoid unresolved onboarding cases | Spain compliance/operations |
| External verification latency/availability | Adapter health | Engineering/operations |
| Stale verification rate | Evidence quality | Product/operations |
| Personal-data access/redaction incidents | Privacy effectiveness | Security/privacy |

Production external lookup is gated on current official service artefacts, Sage access entitlement/purpose, authentication, environment, limits, privacy/legal basis, cache/freshness, result policy and operational support.

| Open question | Owner | Blocks |
|---|---|---|
| Which current AEAT integration is authorised for Sage and under what purpose/authentication? | AEAT liaison/security/privacy | External lookup |
| What exact validator catalogue and exceptional NIF cases are required for Phase 1? | Spain tax/data | Local validator approval |
| What onboarding/capability treatment applies to baja/revoked results? | Spain legal/product | Readiness policy |
| What freshness and recheck policy applies by result and use? | Product/legal/operations | Cache/decision design |
| Which invoice/profile fields carry supplier/recipient identifiers under final SPFE syntax? | Spain semantic-profile owner | PRD-SEI-108/212 delivery |

**Readiness: discovery-ready draft.** Local validation can progress after catalogue approval; external census integration is not delivery-ready.

## Decisions and change log

| Decision | Status |
|---|---|
| NIF is the identity role; DNI/NIE/entity assignment describe subject/value class | Evidence-led proposed decision |
| NIE is not an establishment identifier or SIRET equivalent | Confirmed correction |
| Census match does not prove e-invoicing eligibility, authority or routing | Evidence-led control |
| Existing Confluence page remains the stable publishing target | Publication approved by user on 2026-08-25, subject to merge and dry-run |

| Date | Version | Change | Evidence |
|---|---|---|---|
| 2026-08-25 | Initial canonical draft | Corrected NIF/NIE model, verification layers, official response semantics, 20,000 UI-limit context, privacy and evidence gates; removed invented SLAs/TTL/packages | Confluence v7, AEAT identity/census guidance, Royal Decree 238/2026, PRD-SEI-231 |
