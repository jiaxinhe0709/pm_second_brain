---
id: PRD-SEI-237
title: Format Profile — UN/CEFACT CII
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
  page_id: "907248301"
  title: Format Profile — UN/CEFACT CII
  layout: two_left_sidebar
  toc: true
---

# Format Profile — UN/CEFACT CII

## Decision summary

Treat UN/CEFACT Cross Industry Invoice (CII) as a separately governed format. The EN 16931 syntax-list evidence points to the XML Schemas 16B SCRDM-CII binding; later UN/CEFACT releases must not be inferred as automatically accepted by Spain, a recipient or a connected platform.

PRD-SEI-223 owns common transformation and representation controls. This child owns CII version/profile detail; PRD-SEI-211/212 own retrieval/submission and PRD-SEI-226 owns trust.

## Scope

- Receive, validate, transform and send CII where route and party evidence permits.
- Govern D16B SCRDM-CII/EN 16931 bindings and any later candidate release independently.
- Preserve CII originals and semantic lineage through canonical and delivery representations.
- Support CIUS/extension constraints only through explicit versioned agreement.

Out of scope: assuming base CII schema conformance is sufficient for EN 16931, Spanish acceptance or bilateral interoperability.

## Evidence register

| Evidence | Finding | Limitation |
|---|---|---|
| [EU Implementing Decision 2017/1870](https://eur-lex.europa.eu/eli/dec_impl/2017/1870/oj/eng/pdf) | EN 16931 syntax list references UN/CEFACT CII XML Schemas 16B (SCRDM-CII) | Does not define Spain-specific routing or extensions |
| [UNECE supply-chain standards](https://unece.org/trade/standards/trade-and-uncefact/uncefact/supply-chain-management) | UNECE publishes CII artefacts and later releases | A later release is not automatically an activated EN 16931/Spanish profile |
| Internal requirement 40 | CII 16B requested as a mandatory format capability | Product/route ownership and launch scope remain discovery inputs |

## Capability contract

| Dimension | Required evidence |
|---|---|
| Syntax/release | `CII`, SCRDM-CII release and schema package hash |
| Profile | EN 16931/CIUS/bilateral profile identifier and version |
| Extensions | Named extension set and agreement |
| Operation | Create, validate, transform, send, receive, retrieve and download separately |
| Route | Private direct, public bridge or inbound route eligibility |
| Mapping | Directional source/target mapping, semantic assertions and loss policy |
| Trust | Signature policy reference where applicable |

## Functional requirements

| ID | Requirement |
|---|---|
| CII-FR1 | Resolve the exact CII release, profile/CIUS, extension set and validation artefacts before processing. |
| CII-FR2 | Validate schema and profile/business rules separately and retain both results. |
| CII-FR3 | Activate D16B SCRDM-CII only for routes whose legal, recipient and platform evidence supports it. |
| CII-FR4 | Treat later CII releases as candidates requiring independent conformance and acceptance evidence. |
| CII-FR5 | Preserve exact original/sent bytes, payload hash, validation pack, mapping version and route evidence. |
| CII-FR6 | Prove required semantic invariants for each CII↔canonical and CII↔delivery-format transformation. |
| CII-FR7 | Quarantine unsupported extensions or values that cannot be represented without material loss. |
| CII-FR8 | Transform and validate the final delivery representation before any route-required signature/seal. |
| CII-FR9 | Expose operation-level product/provider capability rather than a single “supports CII” flag. |
| CII-FR10 | Support controlled coexistence and rollback of CII/profile versions without rewriting stored artefacts. |

## Product execution hypothesis

Current discovery input says Sage 50, Sage 200 and Despachos rely on private-platform ISVs for format/transformation capability; Sage Active and X3 ownership is open. This means the customer outcome may be supported while the native Sage product capability remains `NO` or `UNKNOWN`.

## Failure and recovery

| Failure | Required response |
|---|---|
| Unrecognised release/profile | Reject before external mutation |
| Schema passes but profile fails | Reject with profile-rule diagnostics; do not report CII acceptance |
| Material mapping loss | Quarantine and require source correction or approved mapping change |
| Unsupported extension | Stop or use an explicitly approved fallback; never silently drop it |
| Outcome unknown after send | Reconcile through PRD-SEI-212 before retransmission |

## Acceptance criteria

- Given D16B syntax is valid but the required CIUS rule fails, when validation completes, then the invoice is rejected before signing/submission with separate schema and profile evidence.
- Given a later UNECE release exists, when activation is requested, then it remains a candidate until route acceptance and the conformance corpus are approved.
- Given CII is converted to UBL for delivery, when the mapping cannot preserve a required semantic value, then the exchange is quarantined rather than silently omitting it.
- Given product support is provider-owned, when capability is displayed, then native and external-provider support are distinguished.

## Open decisions

| Question | Owner | Blocks |
|---|---|---|
| Is CII D16B in Spanish launch scope and for which private platforms/routes? | Local product/compliance | Scope |
| Which CIUS/extensions and validation artefacts are authoritative? | Local technical team | Conformance |
| Which provider will create/transform CII for each Sage product? | Product/provider owners | Delivery plan |
| What signature profile applies to CII private exchange? | Legal/security | Trust design |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-09-21 | Version 1 | Created CII format child and separated D16B EN 16931 evidence from later-release activation | PRD-SEI-223; EU Decision 2017/1870; UNECE artefacts |
