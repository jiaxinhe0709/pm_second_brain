---
id: PRD-SEI-237
title: Format Profile — UN/CEFACT CII
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
| [DTS local library update to CII 22B](https://confluence.sage.com/spaces/DNBU/pages/833945883) | France Domain Services already provides a DTS pattern using UBL 2.1 as its canonical transformation representation, with CII format detection, validation and bidirectional mapping described for D16B/D22B | Stakeholder input confirms DTS is implemented and reusable; this page is written as a feature proposal and does not by itself prove the deployed D22B version, service boundary or Spain readiness |
| [EN16931 artefacts and FNFE compatibility](https://confluence.sage.com/spaces/DNBU/pages/833945892) | Distinguishes the official D16B EN 16931 syntax binding from France's operational D22B/FNFE direction | French FNFE/AFNOR rules are not Spanish validation rules |
| [D16B/D22B/UBL field mapping](https://confluence.sage.com/spaces/DNBU/pages/833945888) and [structural/semantic differences](https://confluence.sage.com/spaces/DNBU/pages/833945890) | Most core business semantics are stable; key risks include namespace/schema changes, BG-3 cardinality, identifiers, code lists, datatypes and French extensions | Internal analysis requires confirmation against the exact released schema/profile artefacts and a Spain conformance corpus |
| [French CIUS mandatory/optional fields](https://confluence.sage.com/spaces/DNBU/pages/833945896) | French EXTENDED-CTC-FR adds groups, fields, cardinality and validation constraints | Reusable as a rule-pack separation example, not as a Spanish requirement |
| [XML mapping 22B (ChatGPT)](https://confluence.sage.com/spaces/DNBU/pages/757594181) | Supplies a candidate D16B-to-D22B mapping inventory and migration approach | AI-generated secondary input only; not authoritative evidence and must not be used directly as a production mapping |

## DTS reuse direction and Spain delta

**Product direction:** reuse the existing France Document Transformation Service (DTS) rather than create a second Spain-specific transformation engine, subject to a bounded Spain qualification. Reuse includes the transformation runtime, UBL-centred canonical pattern, syntax/version detection, mapping framework, validation-result model and regression-test approach where these capabilities are confirmed deployable.

Reuse does **not** mean importing French compliance policy. The following must remain versioned configuration or country/profile packs:

| Reuse candidate | Spain-specific qualification or replacement |
|---|---|
| DTS transformation runtime and APIs | Confirm tenancy, deployment model, throughput, support ownership and Spain product connectivity |
| UBL 2.1 canonical transformation pattern | Prove it preserves every required Spanish CII business term, extension, signature boundary and faithful-copy obligation |
| CII D16B/D22B detection and parsing | Activate only the exact release/profile accepted for a Spanish route; D22B availability does not prove Spanish acceptance |
| Directional CII↔UBL mappings | Run Spanish positive, negative, boundary and semantic-loss tests; explicitly test one-to-many references, identifiers, taxes, code lists and extensions |
| Schema and schematron execution framework | Replace French FNFE/AFNOR/EXTENDED-CTC-FR packs with the authoritative Spain/route pack; never combine results without provenance |
| Structured validation diagnostics | Map to Spain product/support language while retaining rule-pack, artefact and mapping versions |
| Dual-version rollout and rollback pattern | Confirm D16B/D22B coexistence, in-flight behaviour and historical replay against Spanish routes |

The first architecture task is therefore a reuse assessment and gap matrix, not a new transformer design.

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
| CII-FR11 | Use the existing DTS as the preferred transformation implementation when its confirmed capability satisfies the applicable Spain route/profile contract; record any gap requiring extension or provider ownership. |
| CII-FR12 | Keep the DTS transformation runtime, syntax artefacts, mappings and jurisdiction/profile validation packs independently versioned and identifiable in every result. |
| CII-FR13 | Prevent French FNFE, AFNOR or EXTENDED-CTC-FR rules from being applied as Spanish requirements unless an independently evidenced route profile explicitly references them. |
| CII-FR14 | Qualify every reused CII↔UBL mapping against a Spain corpus covering D16B/D22B release differences, cardinality, identifiers, code lists, tax, extensions and unrepresentable values. |
| CII-FR15 | Expose the deployed DTS build, schema pack, mapping version and validation-rule pack in operational evidence so support can reproduce a transformation decision. |
| CII-FR16 | Resolve direct, delegated, Sage-managed, provider signature/seal or Sage operator-seal mode explicitly through PRD-SEI-223/226; a generic Sage/workload/transport certificate must not satisfy invoice-signing policy. |
| CII-FR17 | Freeze the signer/seal creator, represented principal, trust-material version, signature policy and final CII bytes, and retain expiry/status/validation/preservation evidence while private keys remain in the approved custody boundary. |

## Product execution hypothesis

Current discovery input says Sage 50, Sage 200 and Despachos rely on private-platform ISVs for format/transformation capability; Sage Active and X3 ownership is open. This means the customer outcome may be supported while the native Sage product capability remains `NO` or `UNKNOWN`.

The existing France DTS materially changes the build hypothesis for shared-service products: the default should be **reuse and extend DTS**, not build a Spain-only transformer. It does not change the external-ISV hypothesis for a product unless product and architecture owners confirm that product can consume DTS in its target deployment.

## Failure and recovery

| Failure | Required response |
|---|---|
| Unrecognised release/profile | Reject before external mutation |
| Schema passes but profile fails | Reject with profile-rule diagnostics; do not report CII acceptance |
| Material mapping loss | Quarantine and require source correction or approved mapping change |
| Unsupported extension | Stop or use an explicitly approved fallback; never silently drop it |
| Outcome unknown after send | Reconcile through PRD-SEI-212 before retransmission |
| Certificate expires/revokes or signer authority changes | Block unsafe new signing; preserve historical CII evidence and require a newly approved trust plan |

## Acceptance criteria

- Given D16B syntax is valid but the required CIUS rule fails, when validation completes, then the invoice is rejected before signing/submission with separate schema and profile evidence.
- Given a later UNECE release exists, when activation is requested, then it remains a candidate until route acceptance and the conformance corpus are approved.
- Given CII is converted to UBL for delivery, when the mapping cannot preserve a required semantic value, then the exchange is quarantined rather than silently omitting it.
- Given product support is provider-owned, when capability is displayed, then native and external-provider support are distinguished.
- Given DTS can transform a French CII profile, when it is considered for Spain, then activation remains blocked until the Spanish route/profile corpus passes and French-only rules are demonstrably isolated.
- Given one input is processed through DTS, when support inspects the result, then the exact DTS build, source/target release, mapping and country/profile rule-pack versions are available with the validation evidence.
- Given UBL is the DTS canonical representation, when a Spanish CII value cannot be represented without loss, then the invoice is quarantined and the loss is reported rather than silently normalised.
- Given Sage-managed signing of final CII bytes, when evidence is stored, then the represented customer/delegate and Sage service role are distinct and a Sage workload certificate cannot be substituted.
- Given a signing certificate later expires, when archived CII is validated, then retained signing-time evidence is used without modifying the original bytes.

## Open decisions

| Question | Owner | Blocks |
|---|---|---|
| Is CII D16B in Spanish launch scope and for which private platforms/routes? | Local product/compliance | Scope |
| Which CIUS/extensions and validation artefacts are authoritative? | Local technical team | Conformance |
| Which provider will create/transform CII for each Sage product? | Product/provider owners | Delivery plan |
| What signature profile applies to CII private exchange? | Legal/security | Trust design |
| Does Sage remotely sign CII for the customer/delegate, apply an operator seal, or consume provider-created trust evidence for each route? | Business Identity / Legal / Security | Signer identity and custody |
| Which deployed DTS environment/build currently supports D16B, D22B and bidirectional UBL mapping, and what is its production support model? | DTS/Domain Services owner | Reuse readiness |
| Can the existing UBL 2.1 canonical model preserve every Spanish CII route/profile requirement and faithful-copy obligation? | Architecture/local technical team | Mapping activation |
| Which parts of the France rule-pack pipeline are configurable and which are coupled to FNFE/AFNOR behaviour? | DTS engineering | Spain isolation design |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-09-21 | Version 1 | Created CII format child and separated D16B EN 16931 evidence from later-release activation | PRD-SEI-223; EU Decision 2017/1870; UNECE artefacts |
| 2026-09-21 | Version 2 | Set DTS reuse as the preferred implementation direction while isolating French D22B/FNFE policy from Spain qualification and adding reuse evidence, requirements and acceptance gates | Stakeholder direction; France DTS and CII D16B/D22B Confluence evidence |
| 2026-09-22 | Version 3 | Added explicit signing/seal modes, prohibited generic Sage certificate use and added expiry/historic-validation evidence requirements | PRD-SEI-223/226; stakeholder direction |
