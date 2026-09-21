---
id: PRD-SEI-238
title: Format Profile — UN/EDIFACT
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
  title: Format Profile — UN/EDIFACT
  layout: two_left_sidebar
  toc: true
---

# Format Profile — UN/EDIFACT

## Decision summary

Support UN/EDIFACT only through a complete bilateral implementation profile. “ISO 9735” alone is not an executable invoice contract: route activation must identify the directory/release, message type, subset/implementation guide, code lists, separators/character encoding and trading-party agreement.

Do not describe UN/EDIFACT as an automatically accepted EN 16931 syntax. Where the Spanish route requires another representation, PRD-SEI-223 governs the evidenced transformation.

## Scope

- Receive/send an agreed UN/EDIFACT invoice message through an eligible private route.
- Validate envelope, syntax, directory/message/subset and business rules.
- Transform between the activated EDIFACT profile and canonical/delivery representations with loss controls.
- Preserve exact interchange/message bytes, acknowledgement evidence and business-invoice correlation.

Out of scope: generic “all EDIFACT” support; assuming an `INVOIC` label identifies a compatible directory/subset; public-platform acceptance without evidence.

## Evidence register

| Evidence | Finding | Limitation |
|---|---|---|
| [UNECE UN/EDIFACT message design guidelines](https://unece.org/fileadmin/DAM/trade/edifact/untdid/d424_s1.htm) | UN/EDIFACT uses ISO 9735 syntax and versioned directories/messages | A syntax standard is not a bilateral implementation guide |
| [UNECE D16B INVOIC](https://service.unece.org/trade/untdid/d16b/trsd/trsdi1.htm) | `INVOIC` is a defined message type in a named directory | D16B is an example, not a selected Spanish launch profile |
| Internal requirement 41 | EDIFACT per ISO 9735 requested as mandatory capability | Exact profile, route and provider ownership are open |

## Activation profile

| Dimension | Required value |
|---|---|
| Syntax | ISO 9735 edition/version and service-segment rules |
| Directory/message | Exact directory release and message type/version |
| Subset/guide | Bilateral or industry implementation guide and version |
| Encoding/envelope | Character set, separators, interchange/message envelope and control references |
| Parties | Sender/recipient identifiers and qualifier rules |
| Acknowledgement | Technical/functional acknowledgement type and correlation |
| Mapping | Directional semantic mapping and non-representable-value policy |
| Agreement | Contract/trading-party evidence, effective dates and fallback |

## Functional requirements

| ID | Requirement |
|---|---|
| EDI-FR1 | Refuse route activation unless the complete activation profile and bilateral agreement are recorded. |
| EDI-FR2 | Validate interchange/envelope, syntax, directory/message, subset and business rules as distinct layers. |
| EDI-FR3 | Preserve interchange and message control references without using either as the sole business-invoice identity. |
| EDI-FR4 | Retain exact received/sent bytes, hashes, encoding, delimiters, profile and validation evidence. |
| EDI-FR5 | Prove semantic invariants for each EDIFACT↔canonical or EDIFACT↔delivery-format mapping. |
| EDI-FR6 | Block or quarantine values/segments that cannot be mapped without an approved loss/fallback policy. |
| EDI-FR7 | Distinguish technical acknowledgement, functional acceptance and invoice business lifecycle. |
| EDI-FR8 | Apply signing/sealing only when required by the selected route/profile and after final transformation. |
| EDI-FR9 | Expose EDIFACT capability per directory/message/subset, operation, product and provider. |
| EDI-FR10 | Version agreements and profiles so trading-party changes do not alter historical exchanges. |

## Product execution hypothesis

Discovery input says Sage 50, Sage 200 and Despachos expect private-platform ISVs to provide EDIFACT format/transformation. Sage Active and X3 remain open. Native product support must therefore not be inferred from end-to-end provider support.

## Failure and recovery

| Failure | Required response |
|---|---|
| Unknown directory/message/subset | Reject before business processing |
| Envelope/control-reference conflict | Quarantine as duplicate/conflict and retain evidence |
| Unsupported segment/value | Apply only registered fallback; otherwise reject/quarantine |
| Functional negative acknowledgement | Preserve separately from transport result and permit correction flow |
| Timeout after transmission | Reconcile using route correlation; do not generate a new business invoice |

## Acceptance criteria

- Given an invoice is labelled `INVOIC` without a directory and implementation guide, when route activation is attempted, then activation is refused.
- Given an interchange validates syntactically but violates the bilateral subset, when processing runs, then it is rejected before transformation/signing.
- Given EDIFACT is transformed to UBL, when a mandatory value lacks an approved mapping, then the representation is quarantined and no public/private submission occurs.
- Given a technical acknowledgement succeeds and a functional acknowledgement rejects, then transport and business/functional outcomes remain separate.

## Open decisions

| Question | Owner | Blocks |
|---|---|---|
| Which directory, INVOIC version and industry/bilateral subsets are launch scope? | Product/provider partners | Scope |
| Which private platforms accept each profile? | Partner team | Routing |
| Which acknowledgement messages are required? | Architecture/provider partners | Lifecycle design |
| Is EDIFACT always provider-transformed for the first product cohort? | Product owners | Delivery plan |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-09-21 | Version 1 | Created EDIFACT format child with complete bilateral-profile and transformation controls | PRD-SEI-223; UNECE UN/EDIFACT artefacts; internal requirement 41 |
