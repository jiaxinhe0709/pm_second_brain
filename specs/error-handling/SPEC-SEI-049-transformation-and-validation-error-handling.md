---
id: SPEC-SEI-049
title: Transformation and Validation Error Handling
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-11-23
updated: 2026-11-23
reviewers: []
related:
  - SPEC-SEI-048
  - PRD-SEI-215
  - PRD-SEI-225
  - SPEC-SEI-005
  - SPEC-SEI-008
  - SPEC-SEI-015
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Transformation and Validation Error Handling

## 1 Purpose and authoritative rules

Support must find a transformation by dataset or a reference known to the ERP/customer, identify its failed checkpoint and recover qualified processing. Validation failures must return owned corrections. This view adds operational inspection and action requirements; [SPEC008 Part 2](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md#part-2-logical-feature-specification) owns UM-01–09 and its recovery semantics. [SPEC005](../SPEC-SEI-005-ubl-validation-and-correction-solution-specification.md) owns validation/correction; [SPEC015](../SPEC-SEI-015-invoice-creation-solution-specification.md) owns invoice preparation and issued-content correction.

Apply [SPEC048 OPS-R01–09 — common operational requirements](SPEC-SEI-048-shared-error-handling-and-operational-support.md#2-common-operational-requirements) and the stage-specific operational requirements below. ERR-S01/02.

## 2 Failure investigation and permitted recovery

| ID / condition | Evidence visible to authorised Support/Engineering | Permitted next action and owner |
|---|---|---|
| ERR-TRF-01 Request missing or stuck | Find by dataset, caller file/reference, task/transformation ID and time; show intake, dispatch, processing, validation and result-access checkpoints where evidenced. Separate failed lookup from proven absence. | Consumer/DTS owner investigates the original acceptance under UM-02/03/09 before creating more work. |
| ERR-TRF-02 Mapping/resource or business validation fails | Show all rule/field issues, source/target format, input revision/hash, mapper, rule-pack, DTS/build and profile versions; identify missing provenance. | Customer corrects business input through a linked revision; DTS/Format owner repairs technical resources. Apply UM-04/05/09 and SPEC005 correction rules. |
| ERR-TRF-03 Original processing needs replay | Show original task, terminal/pending outcome, pinned bundle, output/hash, downstream handoff and prior replay attempts. | Offer UM-09 replay only when the original effect and pinned resources are qualified. Do not silently select newer rules or resend downstream invoices. DTS owner. |
| ERR-TRF-04 Output download expires or custody transfer fails | Show generation result, artefact identity/hash, expiry evidence and consumer receipt separately. | Consumer recovers UM-07/08 file access or handoff. A download failure alone does not require generation again. Missing exact bytes go to DTS/Records owner. |
| ERR-TRF-05 Result, notification or task links disagree | Show observations, timestamps, original task/transformation links and notification attempts. | DTS owner reconciles UM-06/07/09 and repairs the failed handoff. No invented terminal state or second authoritative result. |
| ERR-TRF-06 Several transformations are affected | Filter failed/stuck work by dataset, capability and version; list item-level eligibility. | Use OPS-R07 only for qualified UM-09 actions. One successful or blocked item cannot authorise replay of another. DTS/Operations. |

Use [SPEC011 — SPFE response and error matrix](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix) for source-dependent classifications. Keep exact source codes and their operation/version bindings. INT-ERR01 applies only where its selected contract is qualified. Neither a message-resource key nor an HTTP status alone proves the external effect or safe replay. ERR-S02–04.

## 3 Spain use and reuse qualification

Existing DTS is the preferred implementation reuse candidate. UM-Q01–Q07 retain build, contract, mapping, rules and operations gaps; reuse is not qualified by this document. Search and pinned-attempt investigation are reusable patterns. Spain mappings/profile rules remain country-specific. For incoming conversion, [SPEC026 RCV-06](../invoice-receiving/SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#32-receiving-handoff) limits DTS to Phase 3 non-UBL 2.5 input; this error view does not broaden that scope.

## 4 Acceptance and open decisions

Verify ERR-TRF-01/05 with lost intake acknowledgement and missing task links; preserve the original identity. Exercise ERR-TRF-02/03 with a repaired mapper and a newer default: show the exact selected version and keep corrected-input work linked. Exercise ERR-TRF-04/06 with expired access and a mixed batch; generated success must not imply downstream invoice delivery. Apply [OPS-A01–05 common checks](SPEC-SEI-048-shared-error-handling-and-operational-support.md#5-acceptance-and-open-gates), including country-rule isolation and qualification of actual implementation reuse. These are required acceptance scenarios, not executed implementation tests. ERR-S01/02.

DTS/Format owners must prove selected build, source/target contracts, mapper/ruleset provenance, saved input/output access, replay safety and known-error mappings. Operations/Product must set historical access and stuck-work thresholds. Missing retained input or pinned resources blocks exact replay; assign a named recovery alternative without claiming identical regeneration.

## REF Source references

| ID | Source/version and exact location | Supported claim and limit |
|---|---|---|
| ERR-S01 | Functional and API owner documents linked in §1; repository drafts read 23 November 2026; activity/requirement IDs named in §2. | Canonical stage behaviour and open gates. This view adds operational inspection, not a new external contract or lifecycle rule. |
| ERR-S02 | [SPEC048 source register](SPEC-SEI-048-shared-error-handling-and-operational-support.md#ref-source-references), OPS-S01–04; stakeholder note received 23 November 2026; PRD107/215/225 and INT-ERR01. | Product and operational evidence for support requests; stakeholder reported limitations and FR support do not prove Spain implementation. |
| ERR-S03 | [ValidationInvoice.wsdl](<../../context/WSDL servicios web - PRE_23_11_26/ValidationInvoice.wsdl>); reviewed local PRE release 23 November 2026; `wsdl:portType/operation`, binding and service ports. | Exact named operations and transport evidence only. No universal replay, complete business-result or production-support claim. |
| ERR-S04 | [SPEC011 — complete business/technical mapping](../SPEC-SEI-011-public-platform-connector-solution-specification.md#business-and-technical-error-mapping); [original business messages](<../../context/Listados códigos de error/errores_negocio.properties>) and [original technical messages](<../../context/Listados códigos de error/errores_tecnicos.properties>), SPFE-S28/S29 received 23 November 2026, active message keys/templates; [release review](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026). | Message templates and proposed handling only; actual wire-code, field and operation bindings remain unqualified under SPFE-Q20/Q21. Do not copy another operation's meaning or retry rule. |
