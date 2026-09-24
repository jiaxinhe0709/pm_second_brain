---
id: PRD-SEI-236
title: Format Profile — UBL
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-09-21
updated: 2026-09-22
reviewers: []
related:
  - PRD-SEI-211
  - PRD-SEI-212
  - PRD-SEI-223
  - PRD-SEI-226
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "866148656"
  page_id: ""
  title: Format Profile — UBL
  layout: two_left_sidebar
  toc: true
---

# Format Profile — UBL

## Decision summary

Support UBL only through activated, versioned profiles. Do not hard-code “UBL 2.5” as the Spanish exchange format: UBL 2.5 exists, while the EU EN 16931 syntax-list decision references UBL through ISO/IEC 19845:2015, and the Spanish public solution's accepted version/profile remains an evidence gate.

This child owns UBL syntax/profile detail. PRD-SEI-223 owns cross-format transformation and representation policy; PRD-SEI-212 owns creation/submission; PRD-SEI-211 owns retrieval/download/distribution; PRD-SEI-226 owns certificates and signing trust.

## Outcome and scope

- Create or accept a UBL Invoice/CreditNote representation under an activated profile.
- Validate schema, profile/CIUS, business rules and route-specific constraints.
- Use UBL as the public-solution representation or faithful-copy representation only where the approved Spanish specification requires it.
- Preserve original, canonical, delivery, public-copy and human-readable artefacts as distinct representations.
- Support controlled version coexistence, migration and rollback.
- Treat Peppol BIS as an exact UBL/EN 16931 profile with its own version and validation artefacts, not as another syntax.

Out of scope: declaring any UBL version legally accepted without authority evidence; defining public submission transport; treating a PDF rendering as the structured invoice.

## Evidence register

| Evidence | Finding | Confidence / limitation |
|---|---|---|
| [OASIS UBL 2.5](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/UBL-2.5.html) | UBL is a versioned OASIS standard and 2.5 exists | Does not establish Spanish acceptance |
| [EU Implementing Decision 2017/1870](https://eur-lex.europa.eu/eli/dec_impl/2017/1870/oj/eng/pdf) | EN 16931 syntax list references UBL Invoice/CreditNote as ISO/IEC 19845:2015 | Country CIUS/profile and public-platform acceptance remain separate |
| [RD 238/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295) | UBL is one of four admitted syntaxes; Peppol BIS is valid in private-platform scope where it uses UBL and conforms to EN 16931; the public solution uses UBL under the ministerial technical order | Exact BIS/public UBL versions and Spanish adaptations still require activation evidence |
| [UBL 2.5 Invoice Creation](https://confluence.sage.com/spaces/DNBU/pages/837610654/UBL+2.5+Invoice+Creation?src=contextnavpagetreemode) | Internal creation context requested for consolidation | Live body unavailable during revision; validate currency before approval |
| [UBL 2.5 Invoice Submission (Send)](https://confluence.sage.com/spaces/DNBU/pages/837610656/UBL+2.5+Invoice+Submission+Send?src=contextnavpagetreemode) | Existing submission context mapped to PRD-SEI-212 | Title must not be treated as accepted-version evidence |
| [UBL 2.5 Invoice Download](https://confluence.sage.com/spaces/DNBU/pages/837610659/UBL+2.5+Invoice+Download?src=contextnavpagetreemode) | Internal download context requested for consolidation | Live body unavailable during revision |
| [SPFE Invoice Retrieval & Distribution](https://confluence.sage.com/spaces/DNBU/pages/837610722/SPFE+Invoice+Retrieval+Distribution?src=contextnavpagetreemode) | Internal retrieval/distribution context requested for consolidation | Live body unavailable during revision |
| [France DTS CII 22B initiative](https://confluence.sage.com/spaces/DNBU/pages/833945883) and [D16B/D22B/UBL mapping](https://confluence.sage.com/spaces/DNBU/pages/833945888) | Existing DTS uses UBL 2.1 as its canonical transformation representation and provides a reusable CII↔UBL mapping/versioning pattern | Stakeholder input confirms DTS reuse direction; this does not prove UBL 2.1 is the accepted Spanish public/profile version or that every Spanish field is losslessly representable |

## Versioned capability model

| Dimension | Required value |
|---|---|
| Syntax | `UBL` plus exact version |
| Document type | At minimum `Invoice` or `CreditNote`; activate independently |
| Profile | EN 16931/Spanish CIUS/public-copy/bilateral profile identifier and version |
| Extensions | Named, versioned extension set or `NONE` |
| Direction | Create, send, receive, retrieve and download activated separately |
| Route | Public submission, public copy, direct private exchange or inbound |
| Effective period | Start/end and replacement profile |
| Validation artefacts | XSD, code lists, schematron/business rules and test corpus hashes |
| Trust policy | Required signer/seal role and PRD-SEI-226 policy reference |

## Journeys

### Create and submit

1. PRD-SEI-212 receives canonical invoice data or an authorised prebuilt UBL representation.
2. The registry resolves the route's active UBL version/profile.
3. Creation or intake produces a representation and records generator/source, version and hash.
4. Schema, profile and business-rule validation complete before signing and submission.
5. Submission stores exact sent bytes, external reference and acknowledgement independently from business acceptance.

### Retrieve, download and distribute

1. PRD-SEI-211 retrieves the original UBL bytes and provider/public reference.
2. Validation and trust verification occur before canonical product delivery.
3. Original UBL, canonical data and authorised rendering remain correlated but distinguishable.
4. A download response states content type, UBL/profile version, hash and whether the artefact is original or derived.

### Upgrade

1. A new UBL/profile version enters `CANDIDATE` with evidence and conformance artefacts.
2. Existing and candidate versions run side by side for explicitly eligible routes.
3. New exchanges adopt the version only after approval; stored/in-flight representations are never silently rewritten.

## Functional requirements

| ID | Requirement |
|---|---|
| UBL-FR1 | Resolve the exact UBL syntax version, document type, profile/CIUS, extensions and validation pack before representation creation or acceptance. |
| UBL-FR2 | Validate schema, code lists, profile rules and route-specific business rules with field-level safe diagnostics. |
| UBL-FR3 | Preserve the exact input/generated and sent bytes, hashes, generator/mapping version and validation result. |
| UBL-FR4 | Reject a UBL representation whose declared version/profile is absent, contradictory or not activated for the route/direction. |
| UBL-FR5 | Treat Invoice and CreditNote support independently and preserve references between correction documents. |
| UBL-FR6 | Apply the route's approved signature/seal only after final target-profile validation and through PRD-SEI-226 controls. |
| UBL-FR7 | Generate a public faithful copy only from an approved mapping and retain its relationship to the recipient-delivery representation. |
| UBL-FR8 | Support extensions only when the extension set, agreement, validation and semantic fallback are registered. |
| UBL-FR9 | Return original UBL, canonical data and rendering as explicitly labelled artefacts subject to authorisation and retention policy. |
| UBL-FR10 | Permit multiple UBL/profile versions to coexist by effective route and date, with deterministic selection and rollback. |
| UBL-FR11 | Expose create/validate/send/receive/retrieve/download/render support separately by product and provider. |
| UBL-FR12 | Prevent “UBL 2.5” or any later version from production activation until Spanish authority/platform and recipient-route evidence is recorded. |
| UBL-FR13 | Register Peppol BIS by exact BIS/document/profile version and validate both UBL syntax and BIS/EN 16931 rules before route activation. |
| UBL-FR14 | Treat any transition-period PDF as a separately labelled readability companion, never as the UBL invoice or faithful public copy. |
| UBL-FR15 | Reuse the DTS UBL-centred canonical capability where qualified, while versioning Spain/route UBL profiles and validation packs independently from French FNFE/AFNOR rules. |
| UBL-FR16 | Resolve direct, delegated, Sage-managed, provider signature/seal or Sage operator-seal mode explicitly through PRD-SEI-223/226; a generic Sage/workload/transport certificate must not satisfy invoice-signing policy. |
| UBL-FR17 | Freeze the exact signer/seal creator, represented principal, trust-material version, signature policy and signed UBL bytes, and retain expiry/status/validation/preservation evidence without storing private keys in the product. |

## Product responsibility hypothesis

| Product | Expected input/output | Transformation owner | Status |
|---|---|---|---|
| Sage 50 | Canonical/product invoice data | Connected private platform/shared service | Validate |
| Sage 200 | Canonical/product invoice data; native format claims separate | Connected private platform/shared service | Validate |
| Sage Active | To establish | Prefer shared service | Open |
| X3 | To establish | Product/shared service split open | Open |
| Despachos | Canonical/product invoice data; native Facturae claim separate | Connected private platform/shared service | Validate |

For shared-service products, DTS is the preferred implementation candidate. Reuse remains conditional on proof that its UBL 2.1 canonical model preserves the selected Spanish UBL/CII profiles, faithful-copy content and signature boundary without silent loss.

## Failure and recovery

| Failure | Behaviour |
|---|---|
| Unsupported version/profile | Reject before mutation and show supported alternatives |
| Schema/profile failure | Preserve failed representation and diagnostics; correction creates a new attempt |
| Semantic loss during conversion | Quarantine; do not sign or submit |
| Signature failure | Stop before submission; surface PRD-SEI-226 readiness/action |
| Certificate expires/revokes or signer authority changes | Block unsafe new signing; preserve historical signed UBL evidence and require a new approved trust plan |
| Download artefact missing or hash mismatch | Quarantine/reconcile against source; do not fabricate a replacement |
| Submission outcome unknown | PRD-SEI-212 reconciles by stable identity before retry |

## Acceptance criteria

- Given UBL 2.5 exists but Spanish acceptance evidence is absent, when activation is attempted, then production activation is blocked without affecting already approved versions.
- Given a public-copy mapping, when transformation completes, then required semantic invariants pass before the final copy is signed or submitted.
- Given an inbound UBL invoice, when product distribution completes, then the original bytes, canonical representation, profile/version, validation evidence and source reference remain correlated.
- Given an authorised download request, when a rendering is returned alongside UBL, then each artefact is labelled as original or derived with its hash and media type.
- Given two profile versions are active during migration, when route planning occurs, then the selected version follows recorded eligibility/effective-date rules.
- Given a Peppol BIS message, when accepted for a private route, then the exact BIS version and its UBL/EN 16931 conformance evidence are recorded.
- Given a PDF is sent during the transition period, then the UBL representation remains the authoritative structured invoice and the PDF is labelled as a readability companion.
- Given DTS uses UBL 2.1 canonically, when a different UBL/profile version is selected for Spain, then the source, canonical and delivery versions remain explicit and transformation is blocked if required semantics cannot be preserved.
- Given Sage-managed UBL signing, when the signature is created, then the represented customer/delegate and Sage service role are separately evidenced; a Sage workload certificate cannot be substituted.
- Given a signing certificate later expires, when archived UBL is validated, then retained signing-time evidence is used and the original signed bytes remain unchanged.

## Open decisions

| Question | Owner | Blocks |
|---|---|---|
| Which UBL version/profile will the Spanish public solution accept for submission and faithful copies? | Local technical/regulatory team | Production activation |
| Which CIUS and extension identifiers apply to Spanish B2B and public-copy routes? | Legal/local product | Conformance |
| Which Peppol BIS versions and recipient/platform capabilities are in launch scope? | Product/provider partners | Private-route activation |
| Are signed UBL bytes returned by the platform or signed inside Sage? | Security/architecture | Signing design |
| For each UBL route, is Sage remotely signing for a customer/delegate, applying an operator seal, or consuming provider-created trust evidence? | Business Identity / Legal / Security | Signing identity and custody |
| Which creation/download/retrieval requirements from the internal pages remain current? | Product owner | Review completion |
| Does the DTS UBL 2.1 canonical model preserve every field, extension and trust boundary required by the selected Spanish routes? | Architecture/local technical team | DTS mapping activation |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-09-21 | Version 1 | Created UBL child profile with evidence-gated version selection and consolidated creation, submission, retrieval and download boundaries | PRD-SEI-223; OASIS UBL; EU Decision 2017/1870; linked internal discovery pages |
| 2026-09-21 | Version 2 | Added France DTS as the preferred UBL-centred reuse candidate while retaining Spain-specific version, rule-pack and semantic-preservation gates | Stakeholder direction; France DTS and D16B/D22B/UBL mapping evidence |
| 2026-09-22 | Version 3 | Added explicit signing/seal modes, prohibited generic Sage certificate use and added expiry/historic-validation evidence requirements | PRD-SEI-223/226; stakeholder direction |
