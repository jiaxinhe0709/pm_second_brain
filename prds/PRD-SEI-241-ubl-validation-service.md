---
id: PRD-SEI-241
title: E-Invoicing — UBL Validation Service
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-01
updated: 2026-10-02
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-235
  - PRD-SEI-236
  - PRD-SEI-237
  - PRD-SEI-238
  - PRD-SEI-239
  - PRD-SEI-242
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588796"
  page_id: "918651070"
  title: E-Invoicing — UBL Validation Service
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — UBL Validation Service

## Decision summary

**Discovery proposal:** Provide Sage ERP products with one Domain Service capability to validate a UBL invoice before sending and return a result that both developers and customers can act on. Start with a versioned outbound UBL/Peppol BIS reference route. The service may parse and normalise invoice *facts*, but must not silently edit a supplied file. The original and any generated representation remain distinct, traceable artefacts.

This PRD owns the product-to-Domain-Service **validation and correction contract**: input modes, rule layers, result semantics, preflight versus final validation, and responsibility for correcting data. [PRD-SEI-236](PRD-SEI-236-ubl-format-profile.md) owns UBL syntax/profile detail. [PRD-SEI-242](PRD-SEI-242-peppol-lifecycle-feedback.md) separately owns feedback after sending. A validation pass establishes only that the evaluated representation passed the selected local rules at that time.

**Readiness:** consultation-ready discovery. The reference ERP, country, route, exact UBL/BIS profile, transformation permission and API shape remain open. Nothing here activates a production profile or Confluence publication.

## Outcome and problem

An ERP user should learn about a correctable invoice issue while they can still edit the invoice. An ERP developer should receive stable rule IDs, locations and versions rather than decode unrelated UBL, country and provider error formats. Operations should be able to reproduce why a document passed or failed, using the exact input, output and rule-pack versions.

Today [PRD-SEI-227](PRD-SEI-227-e-invoicing-as-a-service.md) defines shared validation principles and [PRD-SEI-236](PRD-SEI-236-ubl-format-profile.md) defines versioned UBL capability. The missing product decision is the handoff: whether products send business facts or prebuilt UBL, what “cleaning” means, when validation occurs, what comes back to the ERP, and who fixes each class of issue. Without it, a product can show “valid” for one file/profile while the final dispatched representation differs.

| Stakeholder | Needed outcome | Failure if absent |
|---|---|---|
| Seller or accountant | Understand and correct invoice issues before sending | Repeated external rejection or unexplained blockage |
| ERP developer | Integrate one stable result contract | Product-specific parsers and inconsistent issue handling |
| Domain Service | Apply exact activated profile and rule versions | Non-reproducible or contradictory checks |
| Operations/support | Inspect input, derived file and validation evidence | Inability to explain or safely recover a failure |
| Country/standards owner | Approve applicable rules, direction and route | Parser availability mistaken for country compliance |

## Phase and capability boundary

| Phase | Capability | Status |
|---|---|---|
| Discovery | Select first ERP, input mode, jurisdiction/route, document type, UBL/BIS profile and rule pack; agree correction ownership | Current |
| Reference pilot | Validate outbound UBL Invoice and/or CreditNote under separately activated versions; provide preflight result and final dispatch check | Proposed |
| Expansion | Add approved UBL profiles, other syntax adapters and inbound validation, each activated by document type, country, direction and route | Proposed, not implied by pilot |

Other files matter to the **contract design**, but this PRD does not declare CII, EDIFACT, Facturae, arbitrary XML, PDF or attachments valid for a route. Their profiles remain governed by their respective documents. Inbound validation has different trust, quarantine and recipient duties and needs separate activation.

## Terms and product principles

| Term | Required distinction |
|---|---|
| Source file | Exact bytes supplied by a product or external sender, with hash, declared type and provenance. |
| Canonical invoice facts | Parsed business meaning for comparison and mapping; neither the legal original nor proof of lossless conversion. |
| Derived representation | New bytes generated through an authorised, versioned mapping; never labelled as the unchanged source. |
| Preflight validation | Non-mutating assessment of recorded input and candidate context. It can become stale. |
| Final validation | Assessment of the exact representation, profile, route and rules selected immediately before external mutation. |
| Valid | Passed the identified local rule set at a given time. It does not mean accepted by an AP, delivered or approved by a buyer. |
| Undetermined | The service cannot give a compliance result because required profile, policy, route or evidence is missing. It must not be reported as valid. |

The Domain Service should return **one structured issue identity for two audiences**: precise rule/field/version data for an API consumer and customer-safe meaning plus a next action for the ERP UI. The ERP controls presentation and business-data edits. The service controls rule interpretation and the result contract.

## Research and evidence

Sources reviewed 2026-10-02. External specifications establish rule layers; the proposed API and ownership choices still need Sage review.

| Source | Confirmed finding | Limit / PRD consequence |
|---|---|---|
| [Peppol BIS Billing 3.0, May 2026 release](https://docs.peppol.eu/poacc/billing/3.0/bis/), section 15 | Validation has distinct syntax, EN 16931, general CIUS and country-qualified rule stages | Do not collapse all failures into “invalid XML”; exact activated release/artefact versions must be retained. |
| [Peppol BIS Billing 3.0 downloads and rules](https://docs.peppol.eu/poacc/billing/3.0/) | Published schematron, code lists and example artefacts accompany the BIS | Their existence does not approve a particular Sage country route or input format. |
| [PRD-SEI-236](PRD-SEI-236-ubl-format-profile.md) | Existing UBL discovery requires explicit syntax/profile version, original/derived separation and validation evidence | This PRD specifies the ERP handoff; it does not reselect UBL versions. |
| [PRD-SEI-227](PRD-SEI-227-e-invoicing-as-a-service.md) | Shared service must apply common and country/profile rules with stable correction guidance and block semantic loss | This is an internal product requirement, not proof of an implemented service. |
| [PRD-SEI-235](PRD-SEI-235-provider-api-for-e-invoicing-service.md) | Partner/API validation results must be actionable and distinct from delivery outcomes | The exact API and partner scope remain open. |

**Working inference:** a shared validation result can serve both customer UI and API consumers if it contains stable rule data plus separately safe, localisable guidance. Pilot usability testing must verify that inference.

## Actors, scenarios and rules

| ID | Trigger / actor | Expected outcome | Exception |
|---|---|---|---|
| S1 | ERP user validates a draft invoice | Field-level, actionable issues return before send | No external invoice mutation |
| S2 | ERP submits prebuilt UBL | Declared syntax/profile and exact bytes are assessed | Unsupported or contradictory declaration is rejected, not guessed |
| S3 | ERP sends invoice facts for UBL creation | Versioned mapper creates a distinct target file and checks semantic preservation | Loss of required meaning stops dispatch |
| S4 | ERP requests send after a successful preview | Exact final file and resolved route are checked again | Changed data, policy or capability can produce a new blocking result |
| S5 | Customer corrects invalid facts/file | New revision is validated and linked to prior result | Earlier bytes and issues remain explainable |
| S6 | A UBL file arrives through future inbound intake | Original, trust and validation are assessed before product distribution | Quarantine/rejection follows an approved inbound policy |

| ID | Condition | Business rule | Status/basis |
|---|---|---|---|
| UVAL-BR1 | A supplied file is parsed or normalised | Preserve its original bytes/hash; any changed file is a new identified representation | Existing PRD-SEI-236; proposed handoff |
| UVAL-BR2 | A preview passes | Record evaluated input, rule/profile and context; do not treat preview as send authorisation | Proposed safety rule |
| UVAL-BR3 | Send is requested | Validate the final representation and selected route before external mutation | Existing PRD-SEI-227/236 |
| UVAL-BR4 | A rule fails | Return a stable issue ID, severity, affected location, rule version, correction owner and safe guidance | Proposed product contract |
| UVAL-BR5 | A required rule cannot be evaluated | Return `undetermined` with missing evidence; never silently pass | Proposed safety rule |
| UVAL-BR6 | Another format or direction is requested | Accept only if that capability is explicitly activated for the country, route and document type | Existing format/profile governance |

## Proposed Domain Service journey

This is a **conceptual interaction**, not an approved endpoint design.

1. The authorised ERP submits invoice facts or prebuilt UBL with tenant, legal entity, actor, source invoice/revision ID, direction, document type and intended country/route. The service records the input reference/hash.
2. The service resolves an activated syntax/profile and exact schema, code-list, BIS, country and route rule artefacts. If it cannot resolve them, it returns `unsupported` or `undetermined` with the reason.
3. For a file, the service checks media/file safety, parseability, UBL schema and then applicable semantic/profile rules. For invoice facts, it maps through an approved generator and validates the resulting file, recording semantic comparison and the new bytes/hash separately.
4. The service returns a validation result with evaluated layers, profile/rule versions, overall outcome and ordered issues. Each issue includes developer detail and safe customer guidance; issues that require ERP data correction are distinguishable from service/configuration failures.
5. The ERP shows errors, permits authorised correction and submits a new revision. The service retains lineage to the previous result and source; it never silently edits the supplied file.
6. If the ERP later requests send, the service resolves the final route and exact dispatch representation, repeats applicable validation and trust/readiness checks, and binds a single idempotent send intent. A blocking failure returns a new result before external mutation.
7. If dispatch proceeds, the validation record remains attached to the send operation. Subsequent Peppol feedback belongs to [PRD-SEI-242](PRD-SEI-242-peppol-lifecycle-feedback.md).

## Conceptual result and ownership contract

| Object | Minimum information |
|---|---|
| Request | Tenant, legal entity, actor, source invoice/revision, direction, input mode, declared syntax/profile, intended country/route, source reference/hash, request identity |
| Result | Result ID/time, input hash, evaluated layers, selected profile/policy/rule versions, outcome (`pass`, `warnings`, `blocked`, `undetermined`), permitted next action, staleness context |
| Issue | Stable Sage issue ID and original rule ID, rule-set/version, stage, severity, field/path or document location, blocking effect, developer detail, safe localisable message, correction owner |
| Derived representation | Source relation, target syntax/profile, mapping version, semantic comparison, bytes/reference/hash and validation result |
| Send binding | Final representation hash, validation result, selected route/profile/rules and idempotent operation identity |

**Proposed operations:** validate/preview, get result, authorised send and get the validation evidence linked to a sent invoice. Architecture must choose transport, storage, compatibility and whether a generated representation is returned as bytes or a reference. The Domain Service must not return sensitive data or raw internal exceptions in customer guidance.

## Failure and operational behaviour

| Condition | Required behaviour |
|---|---|
| Unsupported, absent or contradictory UBL/profile declaration | Block; identify the unsupported dimension and approved alternatives where safe |
| XML is well formed but fails EN 16931, BIS or country rules | Report the actual failing layer, rule and location, with correction owner |
| Mapping loses mandatory meaning or an extension | Stop generation/dispatch; retain mapper and comparison evidence |
| File or attachment fails safety, size or content-type policy | Block or quarantine under an approved policy; return a safe issue without disclosing harmful content |
| Preview passes but file, route or rules change | Final validation evaluates current exact bytes and context; any new failure blocks mutation |
| Customer fixes an issue | New revision/result is linked; original file and result are not overwritten |
| Required rule pack unavailable | Return undetermined/service action; do not claim a customer-data error or success |
| Rule/profile version changes or is rolled back | New work uses approved effective version; historical result remains reproducible |

Support needs a redacted view of input and derived references, exact profile/rule-pack versions, issues, correction owner, result age and send binding. Operations must distinguish customer correction from missing service configuration and unsafe content. Permissions and retention follow the governing country and platform policies.

## Requirements

| ID | Functional requirement |
|---|---|
| UVAL-FR1 | When an authorised product requests validation, the service must bind tenant, legal entity, actor, source revision, direction and request identity before evaluating or storing a result. |
| UVAL-FR2 | The service must resolve the exact activated syntax, document type, profile, country/route policy and validation artefact versions, or return an explicit unsupported/undetermined outcome. |
| UVAL-FR3 | The service must preserve supplied bytes/hash and identify every derived representation separately with its source, mapper version, target profile and hash. |
| UVAL-FR4 | For UBL, the service must report syntax, EN 16931, BIS and applicable country/route rule results separately, retaining original rule IDs and versions. |
| UVAL-FR5 | Each issue must carry a stable ID, severity, location, blocking effect, rule version, developer detail, customer-safe guidance and likely correction owner. |
| UVAL-FR6 | A preview request must perform no external invoice mutation and must return enough evaluated context for a product to recognise a stale result. |
| UVAL-FR7 | An authorised send must validate the exact final representation and route against active rules before mutation; blocking or undetermined results must prevent dispatch. |
| UVAL-FR8 | A corrected input must create a linked revision/result without rewriting the original source, failed result or any previously sent representation. |
| UVAL-FR9 | If mapping loses required business meaning or target-profile validation fails, the service must stop the affected representation and identify the source-to-target discrepancy. |
| UVAL-FR10 | Another syntax, document type, direction or route must remain unsupported until its capability is separately activated with a versioned test corpus and owner approval. |
| UVAL-FR11 | A repeat send command with the same idempotency identity must return the same logical operation or an explicit conflict, without creating a second invoice effect. |
| UVAL-FR12 | A send operation must retain the final validation result, exact dispatched representation hash and versions so later feedback can be correlated without redefining validation. |

| ID | Quality constraint / gate |
|---|---|
| UVAL-NFR1 | Validation results and files require tenant-scoped authorisation; cross-tenant and delegated-access tests are pilot gates. |
| UVAL-NFR2 | Raw files, generated files and diagnostics follow approved classification, access, retention and redaction rules; secrets and private keys never appear in results or logs. |
| UVAL-NFR3 | Schema, code-list, rule, mapper and profile versions must coexist and support reproducible historical results and prospective rollback. |
| UVAL-NFR4 | Pilot readiness requires measured latency, throughput, payload-size and issue-volume baselines by product/profile; target values need named owners. |
| UVAL-NFR5 | Customer guidance must be localisable and accessible, and must distinguish customer correction from Sage/provider action. |

## Acceptance criteria

| ID | Demonstrable condition |
|---|---|
| UVAL-AC1 | Given well-formed UBL that fails a BIS business rule, the result identifies the BIS rule, field/path, version and customer-safe correction; no send occurs. |
| UVAL-AC2 | Given a prebuilt UBL with a contradictory or unactivated profile, the result is blocked/unsupported and the service does not guess a profile. |
| UVAL-AC3 | Given ERP facts are mapped to UBL, source facts, mapper version, target bytes/hash and semantic comparison remain separately inspectable. |
| UVAL-AC4 | Given preview passed but invoice content or route changed, final validation evaluates the new exact file/context and blocks an invalid send. |
| UVAL-AC5 | Given a customer corrects a failed invoice, a new linked result is returned and the failed source/result remain available to authorised support. |
| UVAL-AC6 | Given required country rules are unavailable, the service returns undetermined with Sage-owned next action and performs no external mutation. |
| UVAL-AC7 | Given the same send identity is submitted twice, no second invoice effect is created. |
| UVAL-AC8 | Given an unsupported file format or inbound direction, the service returns an explicit capability outcome even if the file is parseable. |
| UVAL-AC9 | Given a rule-pack upgrade, a historical validation remains reproducible with its original version while eligible new work uses the approved version. |

## Measures, risks and rollout

| Measure | Why | Baseline/target owner |
|---|---|---|
| First-pass validation pass rate | Shows input readiness by product/profile | ERP Product + Domain Service; baseline open |
| Correction completion and time to correction | Tests whether guidance helps customers | ERP Product/UX; baseline open |
| Preventable external validation rejection rate | Tests local conformance against receiving-side outcomes | Domain Service + AP Operations; baseline open |
| Undetermined result and stale-preview rate | Exposes profile/evidence gaps and timing problems | Domain Service Operations; baseline open |

| Risk | Mitigation / gate |
|---|---|
| “Clean” is interpreted as silent repair | Immutable source, separately identified derived representation and authorised correction path |
| Local validation differs from receiving AP rules | Versioned conformance corpus and comparison with observed external rejections; no zero-rejection promise |
| Format parser is mistaken for route approval | Capability activation by country, direction, document, profile and route |
| Customer sees a service failure as a data error | Issue owner/category plus safe next action |

**Rollout gates:** name Product Owner, Solution Designer, Engineering, Operations and reference ERP; approve pilot country/route, UBL document/profile and exact validation artefacts; verify both input modes that are in scope; agree transformation permission and customer wording; test correction, stale preview, semantic loss, idempotency and historical-version scenarios; pilot against a real AP/provider conformance environment before production approval. Rollback disables new work on the affected profile while preserving historical evidence.

## Open decisions and consultation

| Question | Owner | Blocks | Working hypothesis |
|---|---|---|---|
| Which ERP and customer segment is the reference consumer? Which input modes can it supply? | E-invoicing Product Owner + ERP owner | Pilot contract | Model facts and prebuilt UBL; activate only proven modes |
| Which country/route, UBL/BIS version, document types and extensions are first? | Country/standards owner + AP provider | Rule pack and test corpus | One approved outbound route; Invoice and CreditNote separately gated |
| What does the Domain Service have permission to transform or autofix? Who approves a new representation? | Product + Legal/Compliance + Architecture | Mapping design | Normalise facts; never silently alter source bytes |
| When should draft preflight run, and when does a result become stale? | ERP Product + Domain Service Architecture | UX and latency targets | Offer preview and always recheck final send bytes |
| Does the pilot include inbound files or only outbound validation? | Receiving Product + Security + Country owner | Inbound activation only | Defer inbound until trust/quarantine rules are agreed |
| Who owns localisation and the final customer wording? | Domain Service Product + ERP UX | Customer usability | Service supplies safe meaning; ERP presents it |
| What are retention and access periods for source, derived and failed files? | Legal/Compliance + Security | Production | Country/route policy, not a universal default |

## Decisions

No country, UBL profile, API or transformation policy is approved here. This PRD is the validation decision surface; Peppol feedback has its own PRD.
