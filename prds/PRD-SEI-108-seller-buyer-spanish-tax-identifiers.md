---
id: PRD-SEI-108
title: Phase 1 — Seller and Buyer Spanish Tax Identifiers
type: prd
status: draft
owner: TBD
product: spain-e-invoicing
created: 2026-08-25
updated: 2026-08-25
reviewers: []
related:
  - PRD-SEI-101
  - PRD-SEI-103
  - PRD-SEI-106
  - PRD-SEI-212
  - PRD-SEI-231
  - PRD-SEI-233
  - PRD-SEI-235
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610648"
  page_id: "837610770"
  title: "Seller NIF vs Buyer NIF/NIE"
  layout: two_left_sidebar
  toc: true
---

# Phase 1 — Seller and Buyer Spanish Tax Identifiers

## Decision summary

The Spanish public solution requires correctly informed NIF mentions for the invoice issuer and recipient. “Seller NIF versus buyer NIF/NIE” is therefore principally a **party-role and subject-class mapping**, not a choice between peer schemes.

NIF is the tax-identity role. For natural persons, the value commonly comes from DNI or NIE; legal persons/entities use an assigned entity NIF. The model must preserve subject type and source-document/assignment class while exposing the appropriate invoice-party NIF.

Buyer identity does not by itself establish that the transaction is mandatory B2B, that the buyer’s Spanish presence receives the transaction, or where the invoice must be routed. Applicability and routing are separate decisions.

> **Product principle:** Identify the invoice parties by role; decide applicability and destination with separate evidence.

This document owns seller/issuer and buyer/recipient identifier-role mapping. PRD-SEI-106 owns identifier validation/census matching, PRD-SEI-235 owns transaction applicability, PRD-SEI-233 owns network addresses and PRD-SEI-212 owns final public-solution payload mapping.

## Source relationship

This is the canonical Git source proposed for [Seller NIF vs Buyer NIF/NIE](https://confluence.sage.com/spaces/DNBU/pages/837610770/Seller+NIF+vs+Buyer+NIF+NIE), reviewed at version 1. It retains the supplier/recipient distinction while correcting the NIF/NIE hierarchy, B2B scope, regex-only validation and routing/unique-code assumptions.

### Original draft detail disposition

| Original detail | Treatment in this canonical source |
|---|---|
| Seller NIF always and buyer NIF/NIE by party | Preserved as issuer/recipient roles, but NIF is the identity role and DNI/NIE/entity assignment are subject classes |
| `taxIdentifierType = NIF | NIE` | Replaced by scheme, subject, source-identifier class, purpose and invoice-party role |
| Regex examples described as production-ready | Retained only as incomplete format ideas; production validation requires class-specific check rules/tests |
| Company “CIF” regex | Legacy label removed from the canonical scheme; use entity NIF class |
| Buyer is a foreign resident/taxpayer with NIE | Corrected: buyer must satisfy the applicable entrepreneur/professional and geographic/transaction tests |
| Seller BT-32 and buyer BT-48 mappings | Retained as unconfirmed mapping hypotheses; final Spain semantic/UBL profile must approve exact fields |
| Buyer identifier contributes to unique invoice linkage | Removed as a confirmed rule; unique-code composition needs official source and is separate from recipient identity |
| NIF/NIE can identify destination | Corrected: route requires a separate eligible scheme-qualified participant/address record |

## Party and identity treatment

| Invoice party | Subject | Identity treatment | Additional decision required |
|---|---|---|---|
| Issuer/seller | Spanish legal person/entity | Entity NIF in issuer role | Which legal subject/presence supplies the transaction |
| Issuer/seller | Spanish natural person/autónomo | DNI generally serves as NIF | Confirm business/professional capacity and scope |
| Issuer/seller | Foreign natural person/professional | NIE generally serves as NIF where assigned/required; exceptional assigned NIF cases possible | Confirm Spanish scope/presence and applicable identity |
| Recipient/buyer | Spanish legal person/entity | Entity NIF in recipient role | Confirm recipient is entrepreneur/professional and transaction addressed to Spanish seat/presence |
| Recipient/buyer | Spanish natural person | DNI generally serves as NIF | Distinguish business/professional recipient from consumer |
| Recipient/buyer | Foreign natural person | NIE generally serves as NIF where relevant; exceptional assigned NIF cases possible | Distinguish professional recipient and relevant Spanish presence/residence |
| Recipient/buyer | Non-Spanish/out-of-scope party | Country/transaction policy selects applicable identity | Do not force NIE merely because party is foreign |

## Concepts that must remain separate

| Concept | Question | Example outcome |
|---|---|---|
| Legal subject | Who bears seller/buyer rights and obligations? | Company or autónomo |
| Presence/establishment | Which seat/fixed establishment/domicile/residence is relevant? | Spanish fixed establishment receives operation |
| Official identifier | What scheme/value identifies that subject for the purpose? | `ES:NIF` with entity/DNI/NIE source class |
| Invoice role | How is the subject represented in this invoice? | Issuer or recipient |
| Applicability | Does mandatory Spanish B2B e-invoicing apply to this transaction/time? | Required/exempt/undetermined |
| Invoice field/profile | Where does the identifier appear in approved syntax/profile? | Final semantic mapping, versioned |
| Network address | Where is the structured invoice delivered? | Scheme-qualified participant/destination |
| Delegated actor | Who materially performs submission/receipt? | Accountant/platform under authority |

No equality is assumed between these records even when values share characters.

## B2B and geographic boundary

Royal Decree 238/2026 applies mandatory electronic invoicing where the supplier and relevant recipient are entrepreneurs/professionals and the recipient has its business seat, fixed establishment, domicile or habitual residence in Spain, subject to the detailed conditions/exceptions. A buyer with DNI/NIE is not automatically B2B; a foreign party with no NIE is not automatically out of every e-invoicing/reporting obligation.

Onboarding may capture reusable identity and presence facts, but each invoice must consume the effective applicability decision from PRD-SEI-235.

## Business scenarios

| ID | Scenario | Expected identity treatment | Separate decision |
|---|---|---|---|
| S1 | Company sells to Spanish company | Issuer entity NIF and recipient entity NIF | Applicable profile/route/time |
| S2 | Autónomo sells B2B service | Issuer DNI-derived NIF | Business capacity and transaction scope |
| S3 | Foreign natural-person professional with NIE sells | Issuer NIE-derived NIF where applicable | Spanish establishment/scope |
| S4 | Company sells to individual consumer with DNI/NIE | Identity may exist but mandatory B2B classification is not inferred | B2C/document/reporting policy |
| S5 | Company sells to foreign professional | Applicable country identifier may not be Spanish NIE/NIF | Geographic/cross-border policy |
| S6 | Buyer has Spanish fixed establishment | Legal subject and presence are linked separately | Whether operation is addressed to that presence |
| S7 | Accountant submits seller’s invoice | Seller remains issuer/tax subject; accountant is delegated actor | Operation-specific authority |
| S8 | Self-billing/third-party issuance | Supplier duty/identity remains explicit; performing actor differs | Approved arrangement/authority |
| S9 | Same NIF appears in directory/address scheme | Store separate network-address record and evidence | Eligibility/route authority |
| S10 | Seller or buyer NIF changes | New effective identity used prospectively | Historical invoice retains snapshot |

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Public-solution invoice is created | Include correctly informed issuer and recipient NIF mentions under the final approved profile | RD 238/2026 Article 11.3 |
| BR2 | Natural person is a party | Represent NIF with DNI/NIE/assigned-NIF source class appropriate to subject | AEAT guidance |
| BR3 | Buyer possesses DNI/NIE | Do not infer entrepreneur/professional status or B2B applicability | PRD-SEI-235 |
| BR4 | Foreign party lacks NIE | Do not infer invalid transaction; apply country/scope/identity policy | PRD-SEI-235/234 |
| BR5 | Presence affects scope | Store presence separately and decide invoice-specific relationship | PRD-SEI-231/235 |
| BR6 | Accountant/platform performs operation | Seller/buyer invoice identity remains principal-party identity; actor is separate and authorised | PRD-SEI-231 |
| BR7 | Raw value passes regex | Do not call it valid until subject-class check-character and policy controls pass | PRD-SEI-106 |
| BR8 | NIF value is available for routing | Require explicit eligible address scheme, purpose and directory/route evidence | PRD-SEI-233 |
| BR9 | Semantic field mapping changes | Version mapping/profile prospectively and retain historical profile | Evidence continuity |
| BR10 | Identifier changes | Preserve effective-dated identity relationships and invoice snapshots | PRD-SEI-231 |

## Scope and non-goals

### In scope

- Seller/issuer and buyer/recipient party-role identity model.
- Natural-person and entity NIF treatment including DNI/NIE source classes.
- Relationship to B2B/B2C, geographic applicability and Spanish presence.
- Delegated actor and self-billing separation.
- Proposed invoice-field mapping contract and historical snapshots.
- Validation handoff, error behaviour, privacy and acceptance scenarios.

### Non-goals

- Reimplementing validation/census lookup from PRD-SEI-106.
- Deciding VAT treatment or transaction applicability.
- Defining network participant schemes or route precedence.
- Claiming final EN 16931/UBL/Spanish semantic field mapping before the ministerial profile is approved.
- Defining unique invoice code composition beyond confirmed official rules.
- Treating regex examples as production-ready validators.

## Evidence register

| Source | Finding | Confidence/limitation | Impact |
|---|---|---|---|
| [Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238), Articles 3 and 11.3 | B2B scope depends on entrepreneur/professional and Spanish seat/presence context; public invoices require issuer and recipient NIF mentions | Primary law; detailed syntax/profile comes through ministerial order | Party roles and delivery gate |
| [AEAT — NIF for natural persons](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/alta-modelo-036/casilla-110-solicitud-numero-identificacion-036/personas-fisicas.html) | DNI/NIE generally serve as NIF for their respective natural-person populations; exceptions exist | Primary official guidance | Natural-person modelling |
| [AEAT — legal-person/entity NIF](https://sede.agenciatributaria.gob.es/Sede/censos-nif-domicilio-fiscal/solicitar-nif/nif-juridica.html) | Entities use assigned NIF | Primary official guidance | Entity modelling |
| Confluence page 837610770 v1 | Proposed seller NIF/buyer NIF-NIE distinction and field/regex examples | Internal discovery; scope/validation/field claims incomplete | Preserve party intent, correct model |
| PRD-SEI-231/233/235 | Identity, routing and applicability separation | Shared discovery models | Cross-document contract |

## Proposed invoice-party identity record

| Field | Purpose |
|---|---|
| `invoicePartyRole` | `ISSUER`, `RECIPIENT` and future legally distinct roles |
| `legalSubjectId` | Stable Sage subject bearing the invoice role |
| `presenceId` | Optional relevant seat/fixed-establishment/presence selected by applicability |
| `identifierId` | Reference to verified/versioned official identifier |
| `identifierScheme` | `ES:NIF` or other policy-approved scheme |
| `sourceIdentifierClass` | `DNI`, `NIE`, `ENTITY_NIF`, assigned/exception class |
| `mappingProfile/version` | Approved semantic/syntax mapping used |
| `snapshot` | Immutable value/subject/role/profile context used for invoice |
| `applicabilityDecisionRef` | Explains why Spanish obligation/profile applies |

The physical representation may differ, but these distinctions must remain queryable and historically explainable.

## Detailed journeys

### J1 — Resolve issuer identity

1. Invoice references a Sage legal subject and supplying presence facts.
2. Applicability selects relevant country/profile and required issuer role.
3. Identity service selects an effective verified identifier permitted for issuer use.
4. Mapping profile writes the identifier to the approved invoice field.
5. Invoice stores an immutable identity/profile snapshot.

### J2 — Resolve recipient identity

1. Recipient legal subject, subject type and relevant presence are established.
2. Applicability determines whether Spanish mandatory B2B rules apply.
3. Effective recipient identity is selected and validated for the profile.
4. Route resolution separately selects a destination; it may reuse characters only under an explicit scheme.
5. Invoice snapshot preserves both identity and route context separately.

### J3 — Correct identity

1. Missing/invalid/mismatched identifier stops before external submission.
2. Product identifies party role and responsible actor without exposing unnecessary personal data.
3. Corrected identity is revalidated/versioned.
4. New invoice revision uses corrected snapshot; prior evidence remains.

### J4 — Delegated issuance

1. Accountant/platform acts for seller under a named capability grant.
2. Invoice issuer remains the seller legal subject/NIF.
3. Performing actor/authority evidence is retained separately.
4. Submission route/authentication follows its approved contract without replacing seller identity.

## Functional requirements

| ID | Requirement |
|---|---|
| FR1 | The system must represent issuer and recipient as explicit invoice-party roles linked to stable legal subjects. |
| FR2 | The system must reference verified scheme-qualified identifiers rather than raw untyped `sellerNif`/`buyerNie` strings. |
| FR3 | Natural-person identifier records must preserve whether NIF is represented through DNI, NIE or an assigned exceptional class. |
| FR4 | Entity and natural-person identifiers must use their approved class-specific validation through PRD-SEI-106. |
| FR5 | The presence relevant to a transaction must remain separate from legal subject and NIF/NIE. |
| FR6 | Buyer identity must not determine B2B/B2C or geographic applicability by itself. |
| FR7 | The system must consume an explainable applicability decision before applying mandatory Spain B2B profile behaviour. |
| FR8 | A foreign party must not be forced to supply NIE solely because it is foreign; country/scope policy selects the permitted identity. |
| FR9 | Delegated actor/authentication/authority must remain separate from seller/issuer and buyer/recipient identity. |
| FR10 | Self-billing/third-party issuance must preserve the supplier’s legal duty/identity and record the performing actor/arrangement separately. |
| FR11 | Final invoice-field mapping must be versioned and approved against the official Spanish semantic/syntax profile. |
| FR12 | Draft BT/UBL field assumptions must not become delivery requirements without profile evidence and conformance tests. |
| FR13 | The service must reject missing/invalid party identity with party-role-specific correction before external submission. |
| FR14 | Identifier correction/change must create a new effective identity/snapshot without rewriting historical invoices. |
| FR15 | Invoice identity and network destination must remain separate even where a network scheme reuses a NIF value. |
| FR16 | Route resolution must require an eligible scheme-qualified address and source/lookup evidence under PRD-SEI-233. |
| FR17 | Raw NIF/NIE and names must be minimised/redacted in errors, logs, URLs and metrics. |
| FR18 | Products/operations must explain whether a failure concerns issuer identity, recipient identity, applicability, authority or destination. |
| FR19 | Conformance tests must cover legal entity, Spanish autónomo, foreign professional, B2C exclusion, cross-border, delegated issuance and identity change. |
| FR20 | Every submitted invoice must retain immutable seller/buyer identity, applicability and mapping-profile context sufficient for audit/reconciliation. |

## Validation and failure matrix

| Condition | Owner | Behaviour |
|---|---|---|
| Issuer identifier missing | Seller/product | Block submission; identify required role/profile |
| Recipient identifier missing | Buyer data/customer | Apply approved profile/applicability rule; no invented universal fallback |
| Identifier structurally invalid | Customer/data | Correct through PRD-SEI-106 |
| Identifier census mismatch | Customer/data/compliance | Preserve census semantics; correction/review |
| Buyer is consumer | Applicability policy | Do not classify mandatory B2B solely from identity |
| Relevant Spanish presence unresolved | Customer/tax policy | `UNDETERMINED`; no silent scope/route selection |
| Delegated authority missing | Delegate/client | Block affected operation, not party identity record |
| No eligible route | Routing/product | Keep valid invoice identity; delivery remains unresolved |
| Mapping profile unknown/outdated | Compliance/platform | Block external submission until approved version |
| Identifier changes after issue | Lifecycle/data | Historical invoice keeps original snapshot; future invoices use new effective identity |

## Non-functional requirements

- NFR1: Protect natural-person identifiers/names with least privilege, encryption, redaction and purpose limitation.
- NFR2: Version identity, applicability and semantic mapping decisions for historical explanation.
- NFR3: Prevent high-cardinality/full identifier data in logs and metrics.
- NFR4: Make validation/mapping deterministic and covered by profile conformance tests.
- NFR5: Preserve identity snapshots immutably for approved invoice/audit retention.
- NFR6: Monitor identity-role failures and unresolved applicability/route separately.
- NFR7: Support accessible role-specific correction messages across products.
- NFR8: Meet performance targets only after profile rules, volumes and dependencies are approved.

## Acceptance criteria

| ID | Given/when/then |
|---|---|
| AC1 | Given a Spanish company seller, when issuer identity resolves, then an entity-class `ES:NIF` identifier is linked to the issuer role. |
| AC2 | Given a foreign natural-person professional with NIE, when identity resolves, then NIE is the source class for `ES:NIF` and no establishment is inferred. |
| AC3 | Given a buyer with DNI/NIE but classified as consumer, when applicability runs, then mandatory B2B is not inferred solely from the identifier. |
| AC4 | Given a foreign business without Spanish NIE, when processed, then country/applicability policy selects the identity treatment rather than forcing NIE. |
| AC5 | Given an accountant submits for a client, when invoice identity is produced, then the seller remains issuer and the accountant is stored separately as authorised actor. |
| AC6 | Given valid seller/buyer NIFs but no eligible destination, when delivery is planned, then identity remains valid while route is unresolved. |
| AC7 | Given the same NIF characters are used in a network participant address, when stored, then tax identifier and scheme-qualified address remain distinct records. |
| AC8 | Given a regex match but invalid check character, when validated, then the party identity fails through PRD-SEI-106 before submission. |
| AC9 | Given no approved Spanish semantic mapping version, when invoice submission is attempted, then the system blocks rather than use a draft BT/UBL assumption. |
| AC10 | Given an identifier changes after issue, when the old invoice is reviewed, then its original seller/buyer identity and profile snapshot remain unchanged. |
| AC11 | Given an identity error is surfaced, when logged/displayed, then party role and correction are clear but full personal identifier is redacted outside approved view. |
| AC12 | Given a recipient fixed establishment may be relevant, when onboarding stores it, then each invoice still evaluates whether the operation is addressed to that presence. |

## Measures, gates and open questions

| Measure | Purpose | Owner |
|---|---|---|
| Issuer/recipient identity failure by class/profile | Improve master data and mapping | Product/data |
| Applicability-undetermined due to party/presence | Find scope-data gaps | Product/compliance |
| Valid identity but no route | Separate data from delivery problems | Routing/operations |
| Mapping-profile conformance pass rate | Delivery readiness | Engineering/QA |
| Historical snapshot completeness | Audit quality | Compliance/QA |
| Personal-data exposure incidents | Privacy effectiveness | Security/privacy |

Production is gated on the ministerial Spanish semantic/syntax profile, approved field mappings, identity catalogue/validator, B2B/applicability policy, address/routing authority and profile conformance fixtures.

| Open question | Owner | Blocks |
|---|---|---|
| Which exact semantic/UBL fields and code lists carry issuer/recipient NIF under the final SPFE order? | Spain semantic-profile owner | Submission mapping |
| Which recipient identity is permitted/required for exceptional natural-person/non-resident cases? | Spain tax/legal | Coverage |
| How is the relevant Spanish seat/fixed establishment selected for each operation? | Spain tax/product | Applicability |
| What official unique invoice code composition must be stored/generated, and which party fields participate? | Spain regulatory/technical | Identifier/coding implementation |
| Which directory/address schemes may reuse NIF and under what route authority? | Spain routing owner | Delivery |

**Readiness: discovery-ready draft.** The role model is decision-useful; final invoice mapping is blocked by the official profile and country-policy decisions.

## Decisions and change log

| Decision | Status |
|---|---|
| Seller/buyer are invoice roles; NIF is the tax-identity role and DNI/NIE describe natural-person source class | Evidence-led proposed decision |
| Buyer identity does not determine B2B applicability or route | Proposed for approval |
| Regex-only examples and draft field mappings are not production contracts | Evidence-led correction |
| Existing Confluence page remains the stable publishing target | Publication approved by user on 2026-08-25, subject to merge and dry-run |

| Date | Version | Change | Evidence |
|---|---|---|---|
| 2026-08-25 | Initial canonical draft | Preserved issuer/recipient intent; corrected NIF/NIE hierarchy, B2B/geographic scope, delegated actor, validation and routing separation | Confluence v1, Royal Decree 238/2026, AEAT identity guidance, PRD-SEI-106/231/233/235 |
