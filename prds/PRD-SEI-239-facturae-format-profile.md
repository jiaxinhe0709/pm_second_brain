---
id: PRD-SEI-239
title: Format Profile — Facturae
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-09-21
updated: 2026-09-21
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
  page_id: ""
  title: Format Profile — Facturae
  layout: two_left_sidebar
  toc: true
---

# Format Profile — Facturae

## Decision summary

Govern Facturae as a Spanish format profile with route-specific version and XAdES controls. Official Spanish material supports Facturae 3.2.x for public-administration invoicing and lists 3.2.2 artefacts; this must not be generalised into a universal B2B private-platform requirement.

This child owns Facturae schemas, profile and signature coupling. PRD-SEI-226 owns certificate/key lifecycle and signer authority; PRD-SEI-212/211 own submission and retrieval.

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
| Internal requirements 38 and 42 | Product signing and Facturae support claims | Claims and legal interpretations need validation |

## Route/profile model

| Dimension | Required value |
|---|---|
| Version | Exact Facturae version and schema hash |
| Route | B2G/FACe, private B2B or inbound source |
| Profile/rules | Applicable administrative, contractual and code-list rules |
| Signature | XAdES profile/policy identifier, signer role, certificate purpose and verification pack |
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

## Product responsibility hypothesis

| Product | Current claim | Evidence state |
|---|---|---|
| Sage 50 | Signing via certificates; format/transform through private-platform ISV | Validate |
| Sage 200 | Facturae and certificate-based signing available | Validate exact versions, routes and ownership |
| Sage Active | To establish | Open |
| X3 | To establish | Open |
| Despachos | Facturae and certificate-based signing available | Validate exact versions, routes and ownership |

## Certificate readiness dependency

Where the selected Facturae route requires signing, onboarding must show a conditional certificate-readiness stage from PRD-SEI-101. Readiness requires a valid certificate reference, verified owner/legal subject, permitted signing purpose, environment, chain, validity, status/revocation evidence and authorised signer/delegation. Rotation, expiry and revocation remain owned by PRD-SEI-226.

## Failure and recovery

| Failure | Required response |
|---|---|
| Unsupported Facturae version | Reject before signing/submission |
| Schema/business-rule failure | Return safe diagnostics and retain failed attempt |
| Certificate not ready/expired/revoked | Block signing and surface the precise readiness action |
| Signature verification failure | Quarantine; do not distribute as trusted |
| FACe/private route confusion | Stop route plan and require corrected route evidence |
| Outcome unknown after send | Reconcile via PRD-SEI-212 before retry |

## Acceptance criteria

- Given a B2G/FACe route, when Facturae is selected, then the approved schema and XAdES policy are resolved and validated before submission.
- Given a private B2B route, when no Facturae requirement/agreement exists, then the system does not force Facturae merely because the product can create it.
- Given a valid certificate without verified signer authority, when signing is requested, then the action is blocked.
- Given an expired/revoked certificate, when onboarding or runtime readiness runs, then the route is not ready and the remediation is explicit.
- Given a signed Facturae invoice is downloaded, then the exact signed original is distinguishable from any rendering or canonical representation.

## Open decisions

| Question | Owner | Blocks |
|---|---|---|
| Which Facturae versions are accepted for each B2G/FACe and private route? | Local technical/compliance team | Activation |
| Is an advanced signature mandatory for all B2B private-platform invoices? | Legal/security | Private-route design |
| Is a qualified signature required above €5,000 for any B2G route? | Legal/local compliance | Signature policy |
| Which XAdES profile/policy and validation evidence apply per route? | Security/local technical team | Conformance |
| Which Sage 200/Despachos capabilities are native and production-ready? | Product owners | Delivery plan |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-09-21 | Version 1 | Created Facturae child profile and separated official B2G/XAdES evidence from unconfirmed B2B and threshold claims | PRD-SEI-223; official Facturae portal; internal requirements 38 and 42 |
