---
id: PRD-SEI-239
title: Format Profile — Facturae
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-09-21
updated: 2026-09-22
reviewers: []
related:
  - NAV-SEI-004
  - PRD-SEI-211
  - PRD-SEI-212
  - PRD-SEI-223
  - PRD-SEI-226
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "876576919"
  page_id: "907248303"
  title: Format Profile — Facturae
  layout: two_left_sidebar
  toc: true
---

# Format Profile — Facturae

## Decision summary

Govern Facturae as a Spanish format profile with route-specific version and XAdES controls. Official Spanish material supports Facturae 3.2.x for public-administration invoicing and lists 3.2.2 artefacts; this must not be generalised into a universal B2B private-platform requirement.

This child owns Facturae schemas, XAdES object/container/policy coupling and route-specific validation. PRD-SEI-226 owns certificate/key custody and lifecycle, signer/seal authority, expiry/rotation and long-term evidence; PRD-SEI-212/211 own submission and retrieval.

## Scope

- Create, validate, sign, submit, receive and download activated Facturae representations.
- Distinguish B2G/FACe requirements from private B2B platform exchange.
- Apply the exact approved XAdES signature policy after final representation creation.
- Preserve signed original bytes, validation/signature evidence and canonical lineage.
- Support controlled Facturae version coexistence.

Out of scope: asserting every B2B invoice needs Facturae or XAdES specifically; assuming a certificate grants signing authority; confirming the proposed €5,000 qualified-signature rule without official evidence. RD 238/2026 Article 7.3 does require an advanced electronic signature for invoices issued through private platforms, but the exact technical signature profile remains route/format specific.

## Evidence register

| Evidence | Finding | Limitation |
|---|---|---|
| [Official Facturae format portal](https://www.facturae.gob.es/formato) | Spanish public-administration invoices use Facturae 3.2.x with XAdES | Does not establish all B2B private-platform rules |
| [RD 238/2026 Article 7](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295) | Facturae is one of four admitted syntaxes and private-platform invoices require an advanced signature | Does not by itself select the exact XAdES profile for every Facturae route |
| [Latest Facturae version](https://www.facturae.gob.es/formato/ultima-version) | Portal lists Facturae 3.2.2 schema/documentation artefacts | Route acceptance and migration dates still require confirmation |
| [Facturae signature policies](https://www.facturae.gob.es/formato/politicas-firma-electronica) | Official signature-policy material is published | Exact current profile/policy must be selected and versioned |
| [eIDAS Regulation, consolidated](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02014R0910-20240520) | Distinguishes electronic signatures, seals, certificates, validation, timestamps and preservation services | Does not select a Facturae/XAdES route policy by itself |
| [Spanish electronic-signature and certificate policy catalogue](https://administracionelectronica.gob.es/ctt/politicafirma/descargas) | Publishes policy and implementation material relevant to Spanish administrative signatures | Exact applicable artefact/version must be frozen per route |
| [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.00_20/en_31910201v010400a.pdf) | Provides validation and long-term-validation evidence concepts | Exact preservation profile remains a product/legal decision |
| Internal requirements 38 and 42 | Product signing and Facturae support claims | Claims and legal interpretations need validation |

## Route/profile model

| Dimension | Required value |
|---|---|
| Version | Exact Facturae version and schema hash |
| Route | B2G/FACe, private B2B or inbound source |
| Profile/rules | Applicable administrative, contractual and code-list rules |
| Signature/seal | XAdES form/container/policy identifier, direct/delegated/Sage-managed/provider/seal mode, represented principal, actual signer/delegate or seal creator, service operator/custodian, certificate purpose/version, signed object, timestamp/status and validation/preservation pack |
| Operation | Create, validate, sign, send, receive, retrieve, download and render independently |
| Product/provider | Native, shared Sage service or connected-platform owner |
| Effective period | Activation, coexistence and retirement dates |

## Functional requirements

| ID | Requirement |
|---|---|
| FCT-FR1 | Resolve the exact Facturae version, route/profile and validation pack before creation or acceptance. |
| FCT-FR2 | Validate schema, code lists and route-specific business rules before signature. |
| FCT-FR3 | Resolve the XAdES profile/policy, signer role and certificate purpose through an effective, approved trust policy. |
| FCT-FR4 | Apply the signature to final Facturae bytes and preserve signature, certificate-chain, timestamp/revocation and verification evidence as required. |
| FCT-FR5 | Never infer signer authority from certificate possession; use PRD-SEI-226 authority and lifecycle controls. |
| FCT-FR6 | Keep B2G/FACe and private B2B capabilities separate in route and product capability records. |
| FCT-FR7 | Preserve exact signed original bytes and hash; derived canonical/rendered artefacts must be labelled. |
| FCT-FR8 | Version Facturae transformations and prove required semantic invariants before signing/submission. |
| FCT-FR9 | Expose native versus provider-owned Facturae capability by operation and product. |
| FCT-FR10 | Support coexistence/rollback of approved versions without modifying archived signed invoices. |
| FCT-FR11 | Distinguish direct customer signature, accountant/other delegated signature, Sage-managed remote signature, provider signature/seal and Sage operator seal; `Sage signature` must not be stored as an undifferentiated mode. |
| FCT-FR12 | For Sage-managed signing, preserve the represented customer, actual authorised signer/delegate, Sage service role, custody/operation reference and authority snapshot; do not use a Sage workload/transport certificate as the invoice-signing credential. |
| FCT-FR13 | A Sage or provider operator seal must name the legal-person seal creator and must not satisfy a direct/delegated private-platform signature policy unless Legal approves that exact route/policy. |
| FCT-FR14 | Resolve and freeze the exact XAdES form, signature-policy identifier/hash, canonicalisation/digest/signature algorithms, certificate/trust-material version, signed nodes/object, container/embedding rules and validation pack before signing. |
| FCT-FR15 | Recheck certificate purpose, subject/owner, authority, environment, validity, revocation/status freshness and algorithm/profile policy immediately before signing; unsafe status must block new use. |
| FCT-FR16 | Retain the exact signed Facturae bytes plus signature, public certificate chain, trusted time/status evidence, policy/validation conclusion and preservation provenance; private keys must remain in the PRD-SEI-226 protected custody boundary. |
| FCT-FR17 | Certificate expiry or rotation must not alter archived Facturae bytes or automatically invalidate an earlier signing-time conclusion; later validation must use retained evidence and approved preservation policy. |

## Product responsibility hypothesis

| Product | Current claim | Evidence state |
|---|---|---|
| Sage 50 | Signing via certificates; format/transform through private-platform ISV | Validate |
| Sage 200 | Facturae and certificate-based signing available | Validate exact versions, routes and ownership |
| Sage Active | To establish | Open |
| X3 | To establish | Open |
| Despachos | Facturae and certificate-based signing available | Validate exact versions, routes and ownership |

## Certificate readiness dependency

Where the selected Facturae route requires signing, onboarding must show the conditional certificate-readiness stage from PRD-SEI-101. The user must select the explicit signing/custody mode rather than a generic “Sage certificate”. Readiness requires a protected certificate/trust-material reference, represented principal, actual authorised signer/delegate or seal creator, service operator/custodian, permitted purpose, route/profile, environment, chain, validity and current status/revocation evidence. Products store only the reference and approved public metadata; private keys/signing operations remain in the PRD-SEI-226 custody boundary. Expiry, renewal, rotation, revocation, compromise, destruction and historic validation/preservation remain owned by PRD-SEI-226.

## Failure and recovery

| Failure | Required response |
|---|---|
| Unsupported Facturae version | Reject before signing/submission |
| Schema/business-rule failure | Return safe diagnostics and retain failed attempt |
| Certificate not ready/expired/revoked | Block signing and surface the precise readiness action |
| Wrong certificate purpose/subject or missing delegate authority | Block the Facturae signature; do not infer authority from possession or product role |
| Sage workload certificate or unapproved operator seal selected | Reject policy resolution and require the approved signer/seal mode |
| Signing timeout after possible execution | Reconcile the immutable signing-operation reference before retry; do not create a second signature blindly |
| Historic certificate now expired | Validate from retained signing-time/status/policy evidence; do not alter the archived signed bytes |
| Signature verification failure | Quarantine; do not distribute as trusted |
| FACe/private route confusion | Stop route plan and require corrected route evidence |
| Outcome unknown after send | Reconcile via PRD-SEI-212 before retry |

## Acceptance criteria

- Given a B2G/FACe route, when Facturae is selected, then the approved schema and XAdES policy are resolved and validated before submission.
- Given a private B2B route, when no Facturae requirement/agreement exists, then the system does not force Facturae merely because the product can create it.
- Given a valid certificate without verified signer authority, when signing is requested, then the action is blocked.
- Given an expired/revoked certificate, when onboarding or runtime readiness runs, then the route is not ready and the remediation is explicit.
- Given a signed Facturae invoice is downloaded, then the exact signed original is distinguishable from any rendering or canonical representation.
- Given Sage-managed signing, when Facturae is signed, then the evidence separately identifies the customer principal, authorised signer/delegate, Sage service role, custody reference, certificate version and exact signed object.
- Given a Sage workload/transport certificate, when it is selected for the Facturae XAdES signature, then the request is rejected as wrong-purpose.
- Given a Sage operator seal is available but the approved route requires a direct/delegated signature, when signing is planned, then the route remains blocked and the seal is not labelled as the customer's signature.
- Given a certificate later expires, when an archived signed Facturae invoice is validated, then the original bytes and retained signing-time validation/preservation evidence are used rather than current expiry alone.

## Open decisions

| Question | Owner | Blocks |
|---|---|---|
| Which Facturae versions are accepted for each B2G/FACe and private route? | Local technical/compliance team | Activation |
| Which direct/delegated advanced-signature and XAdES profile implements Article 7.3 for each private B2B Facturae route? | Legal/security | Private-route design |
| Is a qualified signature required above €5,000 for any B2G route? | Legal/local compliance | Signature policy |
| Which XAdES profile/policy and validation evidence apply per route? | Security/local technical team | Conformance |
| Does Sage's proposed service remotely sign for the customer/delegate, apply a Sage operator seal, or support both through separately approved policies? | Business Identity owner / Legal / Security | Signer identity, UX and architecture |
| Which expiry horizon, renewal owner, status source, timestamp and long-term preservation evidence apply to each Facturae route? | Security/operations/local technical team | Production lifecycle |
| Which Sage 200/Despachos capabilities are native and production-ready? | Product owners | Delivery plan |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-09-21 | Version 1 | Created Facturae child profile and separated official B2G/XAdES evidence from unconfirmed B2B and threshold claims | PRD-SEI-223; official Facturae portal; internal requirements 38 and 42 |
| 2026-09-22 | Version 2 | Added explicit direct, delegated, Sage-managed, provider and operator-seal modes; detailed XAdES policy freezing, protected custody, expiry/runtime checks and historic validation evidence | Stakeholder direction; PRD-SEI-101/223/226; eIDAS; ETSI EN 319 102-1; Spanish policy catalogue |
