---
id: SPEC-SEI-053
title: Customer Offboarding Error Handling
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
  - SPEC-SEI-032
  - SPEC-SEI-033
  - SPEC-SEI-014
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Customer Offboarding Error Handling

## 1 Purpose and authoritative rules

Support must explain which part of a disconnect or exit is unfinished and preserve required historical work. [SPEC032 exit checks](../offboarding/SPEC-SEI-032-customer-offboarding-logical-feature-specification.md#2-state-invariants-and-workflow) own OFF-01–08. [SPEC038 switch journey](../onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#switch-platform-one-customer-journey) owns the combined customer request; [SPEC033](../offboarding/SPEC-SEI-033-customer-offboarding-sequence-and-reuse-assessment.md) owns API reuse qualification.

Apply [SPEC048 OPS-R01–09 — common operational requirements](SPEC-SEI-048-shared-error-handling-and-operational-support.md#2-common-operational-requirements) and the stage-specific operational requirements below. ERR-S01/02.

## 2 Failure investigation and permitted recovery

| ID / condition | Evidence visible to authorised Support/Engineering | Permitted next action and owner |
|---|---|---|
| ERR-OFF-01 Planned stop lacks scope, authority or destination evidence | Show selected business/direction/services, requested cutoff, failed gate and continuing-work decision. | Customer/Onboarding/Operations resolves OFF-01–03. Incident containment follows OFF-S10 separately and cannot wait for planned-exit approval. |
| ERR-OFF-02 Cutover/disconnection response is lost | Show original operation, requested and observed route/cutoff, provider confirmation and affected traffic. | Routing/Integration owner applies OFF-04/08 before another change. A working new connection cannot prove that the old service ended. |
| ERR-OFF-03 Earlier invoices or late events need old access | Show original invoice route, pending reports, retained credential/access purpose, due dates and accepted handover owner. | Operations/Compliance resolves OFF-05 and cutoff rules. Do not delete the configuration or revoke shared access while dependent work lacks a safe path. |
| ERR-OFF-04 Credential, contract or service removal partly fails | Show each separate release result and remaining uses of the selected connection/credential. | Security/provider/contract owner applies OFF-06. Do not repeat completed release steps or remove another retained business/direction. |
| ERR-OFF-05 Export, historical access or records handover fails | Show package scope/version, missing/failed files, authorised recipient, expiry and receipt evidence. | Records/Operations owner recovers OFF-07 and SPEC032 §5. A failed download is not an accepted export; retention/disposal follows the approved policy. |
| ERR-OFF-06 Many exits or an incident require recovery | Show item-level gate status, unsafe actions, incident owner and unfinished handovers. | OPS-R07 applies only to qualified OFF-08 actions. Private A to Private B remains subject to enabled scope; bulk action cannot enable a disabled switch or close unresolved duties. |

Use [SPEC011 — SPFE response and error matrix](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix) for source-dependent classifications. Keep exact source codes and their operation/version bindings. INT-ERR01 applies only where its selected contract is qualified. Neither a message-resource key nor an HTTP status alone proves the external effect or safe replay. ERR-S02–04.

## 3 Spain use and reuse qualification

Use in Spain covers stopping selected Sage access and enabled exits, including historical duties. Scoped release, evidence-led cutover and handover recovery are shared design patterns. Spain public access, copy/reporting and country records rules require Spain binding; external agreements need provider-specific handling. Actual exit automation and support-tool coverage are unknown. Existing DTS does not own exit/route actions; any export-format transformation needs its own qualified mapping.

## 4 Acceptance and open decisions

Exercise ERR-OFF-02/04 with a lost disconnect result and a credential shared by retained services. Exercise ERR-OFF-03/05 with outstanding historical reports and a failed export; show distinct progress and owners. Exercise ERR-OFF-01/06 with urgent security containment and mixed bulk eligibility; do not claim completed planned exit. Apply [OPS-A01–05 common checks](SPEC-SEI-048-shared-error-handling-and-operational-support.md#5-acceptance-and-open-gates), including country-rule isolation and qualification of actual implementation reuse. These are required acceptance scenarios, not executed implementation tests. ERR-S01/02.

OFF-Q01–06 remain open for periods, provider/public access changes, continuity and export implementation. Onboarding/Routing/Integration qualify external observation and partial removal; Security/Records qualify shared credentials and handover; Operations qualifies runbooks and bulk scope. No SPFE deregistration endpoint or fixed support/retention period is introduced.

## REF Source references

| ID | Source/version and exact location | Supported claim and limit |
|---|---|---|
| ERR-S01 | Functional and API owner documents linked in §1; repository drafts read 23 November 2026; activity/requirement IDs named in §2. | Canonical stage behaviour and open gates. This view adds operational inspection, not a new external contract or lifecycle rule. |
| ERR-S02 | [SPEC048 source register](SPEC-SEI-048-shared-error-handling-and-operational-support.md#ref-source-references), OPS-S01–04; stakeholder note received 23 November 2026; PRD107/215/225 and INT-ERR01. | Product and operational evidence for support requests; stakeholder reported limitations and FR support do not prove Spain implementation. |
| ERR-S03 | [SPEC033 §3.3 Spain public evidence](../offboarding/SPEC-SEI-033-customer-offboarding-sequence-and-reuse-assessment.md#33-spain-public-evidence), reviewed local PRE WSDL set 23 November 2026. | No named SPFE offboarding operation is evidenced. Internal access removal and external representation changes still need qualification. |
| ERR-S04 | [SPEC011 — complete business/technical mapping](../SPEC-SEI-011-public-platform-connector-solution-specification.md#business-and-technical-error-mapping); [original business messages](<../../context/Listados códigos de error/errores_negocio.properties>) and [original technical messages](<../../context/Listados códigos de error/errores_tecnicos.properties>), SPFE-S28/S29 received 23 November 2026, active message keys/templates; [release review](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026). | Message templates and proposed handling only; actual wire-code, field and operation bindings remain unqualified under SPFE-Q20/Q21. Do not copy another operation's meaning or retry rule. |
