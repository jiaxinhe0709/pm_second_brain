---
id: RES-SEI-008
title: Peppol operations and commercial assessment
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-003
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-240
  - PRD-SEI-245
confluence:
  publish: false
  page_id: ""
---

# Peppol operations and commercial assessment

Sage needs an evidence-based decision on how to operate Peppol reliably and at an acceptable cost. [PRD-SEI-245](../../../prds/PRD-SEI-245-peppol-access-point-validation-and-certification.md#decision-summary-and-readiness) records the stakeholder report that Sage has an AP implementation or entitlement, with certification and production readiness unverified. Begin by qualifying that asset. Do not treat this as an empty build-versus-buy exercise or assume the reported asset is a certified live service.

## Current capability evidence

| Capability | Baseline position | Evidence to request and proposed role |
|---|---|---|
| AP asset and hosting | Reported; exact asset and contract open | Engineering: software/build, environment, hosting, dependencies and operator |
| Legal network eligibility | Unverified in this research | Legal/network: entity, agreement, authority, membership category and service domains |
| Test and production credentials | State unverified | Security: certificate purpose, issuer, subject, environment, validity and custody references |
| Accepted conformance | Completion unverified | AP owner: required suite/version, results, defects and authority acceptance |
| Participant management and metadata | Operating model open | Network product: operator, management contract, ownership and migration evidence |
| Send/receive and feedback | Requirements exist; actual coverage unverified | Engineering: supported process matrix and representative end-to-end traces |
| Support and recovery | Operational acceptance unverified | Operations: on-call model, dependency escalation, runbooks and recovery exercises |

Only non-secret metadata and evidence references belong in the assessment. PRD-SEI-245 owns the AP release gates. P11 in the [source register](../RES-SEI-003-peppol-source-register.md#global-network-sources) provides public accreditation guidance; it does not establish Sage's test results or the exact current authenticated suite.

## Options to compare after asset qualification

The following are proposed options, not a provider selection.

| Option | Responsibilities to investigate | Main decision exposure |
|---|---|---|
| Qualify and operate the reported Sage AP | Software, hosting, network obligations, trust, capacity, on-call and customer support | Control and reuse benefit must justify continuing operating cost and readiness work |
| Contract a certified AP service | Sage product integration and customer obligations; provider network operations | Contract scope, service evidence, data access, dependency and exit |
| Sage AP with contracted metadata service | AP operations plus an external participant-management dependency | Split ownership, cutover and escalation must be explicit |
| Retain more than one qualified route | Per-route capability, contracts, evidence and support | Additional flexibility has cost; it does not make automatic failover safe |

For a possibly transmitted message, reconcile the original exchange before changing route; see PG-04 in RES-SEI-005. A secondary provider is not a general retry mechanism.

## Operational assessment

These are proposed evidence checks. Contractual limits and targets remain open until agreed.

| Concern | Demonstration needed | Business effect if missing |
|---|---|---|
| Trust rotation and revocation | Correct environment and identity; rotation exercise; expiry/revocation response | Affected new exchanges can fail or become ineligible |
| Dependency failure | Distinguish metadata, AP, receiving-product and product-API failures | Support may resend an invoice that is already delivered |
| Evidence and observability | Correlate product request, route, message, raw response and recovery case | No reliable answer to the customer's delivery question |
| Capacity | Expected peaks, document/attachment limits, queues and receiving backlogs | Delayed invoicing or lost customer visibility |
| Callback loss and replay | Durable history retrieval, authentication, replay handling and reconciliation | Missed results or duplicate accounting work |
| Incident ownership | Named accountable service owner and escalations for each dependency | Customers cannot obtain a safe next action |
| Privacy and retention | Data locations, processors, access purposes, retention and deletion rules | Country approval or customer evidence obligations may be unmet |
| Change management | Release qualification for network, profile, rule and provider changes | Previously valid documents can fail after an unnoticed update |
| Reporting duties | Applicable network statistics duties assessed separately from national tax reporting | An operating obligation may be missed or incorrectly shown as invoice tax compliance |
| Exit | Export, receiving continuity, migration, pending cases and historical access | Provider change may interrupt customer obligations |

Country-rule isolation must be demonstrated across at least two qualified configurations. The assessment must identify whether each capability is implemented, proposed or unavailable, and name its owner.

## Cost model inputs

Compare options for the same country, directions, supported profiles, traffic and support coverage. Collect vendor quotes and internal cost estimates; no price, SLA or savings target is asserted here.

| Cost group | Inputs needed |
|---|---|
| Initial qualification | Agreements, due diligence, test work, integration, migration and security assessment |
| Recurring fixed | Membership/accreditation fees where applicable, hosting, licences, minimum commitments and support |
| Usage | Outbound/inbound volumes, chargeable responses, registration/lookup charges, storage and network transfer |
| Operations | Monitoring, on-call, certificates, upgrades, incident effort and reconciliation |
| Product/country extension | Mapping, validation, localisation, support training and regression |
| Exit and concentration | Export/migration charges, transition overlap and a dependency-failure scenario |

Use a sensitivity analysis for low, expected and peak volumes once real inputs exist. Include failed and retried work if chargeable. Avoid comparing a managed-service quote with hosting cost alone.

## Decision evidence and next action

AP engineering should assemble the asset inventory first. Legal/network, security and operations then qualify their respective evidence. Platform and country product owners can compare operating options against the first real cohort. Finance/procurement supplies comparable cost inputs.

An operating recommendation needs the supported-capability matrix, unresolved obligations, cost ranges and acceptance owners. A pilot additionally needs the country-specific gates in RES-SEI-011. This research approves neither production use nor a provider change.
