---
id: RES-SEI-011
title: UK Peppol readiness and open decisions
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-008
  - RES-SEI-009
  - RES-SEI-010
  - PRD-SEI-230
  - PRD-SEI-245
confluence:
  publish: false
  page_id: ""
---

# UK Peppol readiness and open decisions

The research baseline supports product preparation and consultation. It does not establish UK delivery readiness. The next decision is which customer/product cohort to assess first and whether the reported Sage AP can serve it under a qualified operating contract.

[RES-SEI-009](RES-SEI-009-policy-and-source-evidence.md) owns UK policy findings. [RES-SEI-008](../global/RES-SEI-008-operations-and-commercial-assessment.md) owns the global operating assessment. This document owns the proposed UK evidence backlog and decision sequence. Roles below are suggested responsibilities; named accountable owners and reviewers remain open.

## Evidence and decision gates

| Gate | Decision and evidence needed | Proposed accountable role | Baseline and next safe action |
|---|---|---|---|
| UKG-01 Cohort | First Sage product, customer segment, directions, document/process and voluntary/current-contract/future-mandate purpose | UK product owner | Open. Select a bounded assessment cohort; avoid a universal “UK ready” claim. |
| UKG-02 Legal scope | Applicable original law, commencement, geography, parties, exclusions and transaction scope | UK compliance/legal owner | Policy direction evidenced; detailed legal qualification open. Resolve UK05 retrieval and assess the selected context. |
| UKG-03 Profile | Official applicable profile, process, syntax, code lists, versions and effective dates | UK compliance and format owner | Global candidates exist; final future-mandate selection not established. Prepare mapping analysis without choosing a statutory default. |
| UKG-04 Identity and registration | Allowed schemes, identity checks, delegated authority, existing-registration handling, metadata operator and migration rules | Network product owner | Current code-list evidence is available; final UK policy and selected provider contract need qualification. |
| UKG-05 AP eligibility | Actual Sage asset, legal entity, agreement, service domains, accepted conformance, certificates and operational scope | AP engineering with legal/security | Stakeholder-reported asset; production evidence unverified. Follow PRD-SEI-245's existing gates. |
| UKG-06 Product and reuse | Current product gaps, data mappings, DTS/validation evidence and implemented send/receive contracts | Product engineering and platform owner | Coverage unverified. Exercise the selected RES-SEI-010 scenarios and record local changes. |
| UKG-07 Feedback and recovery | Process response expectations, supported evidence sources, correlation, reconciliation and safe correction | Lifecycle and operations owner | Product requirements exist; provider/counterparty capability needs proof. Qualify PRD-SEI-242 mappings. |
| UKG-08 Service and economics | Security, retention, support, incident ownership, capacity, comparable cost and exit evidence | Operations, security and commercial owner | Open. Complete RES-SEI-008 for the cohort. |
| UKG-09 Activation | Approved purpose/scope, acceptance evidence, rollout, monitoring and rollback decisions | UK product owner with compliance/security/operations | Not approved. No live statutory claim follows from research or network certification alone. |

There are no fabricated completion dates or pass-rate targets. A gate closes only when its applicable evidence is reviewed by a named owner. A future-mandate gate may remain open while a separately qualified voluntary or current-contract assessment progresses; its approval must state that narrower purpose.

## Immediate evidence requests

| Priority | Request | Why it is needed | Gate |
|---|---|---|---|
| First | Name UK product, network, AP, security and operations owners; choose the first assessment cohort | Turns broad discovery into accountable decisions | UKG-01/05/08 |
| First | Inventory the reported AP and its agreement, environment and certificate metadata | Determines the actual conformance and production critical path | UKG-05 |
| First | Obtain existing participant-management and AP customer API contracts | Establishes what can be inspected, created, migrated and reconciled | UKG-04/07 |
| First | Inspect one product's current outbound and inbound flows using synthetic examples | Shows real data and journey gaps | UKG-06 |
| Next | Reconcile UK policy sources and obtain the original relevant legal text | Separates current obligations from future policy | UKG-02 |
| Next | Complete a candidate profile mapping and validation assessment | Exposes missing fields, document variants and DTS changes | UKG-03/06 |
| Next | Obtain comparable internal cost and contracted-service inputs | Enables an operating recommendation after asset qualification | UKG-08 |

These are requests to be handled by the project owners; no messages to other people or external systems have been sent.

## Proposed acceptance evidence

| Demonstration | Evidence and limit | Gates |
|---|---|---|
| Country-rule isolation | Run selected synthetic cases in two qualified country/profile configurations; prove one country's rule change does not alter the other. Global Billing/PINT sources P06/P08 define candidate artefacts, not UK law. | UKG-03/06 |
| Implementation reuse | Identify source capability, deployed version, contract, local changes, gaps, owner and test evidence. Assess DTS first where transformation is needed. | UKG-06 |
| Client and capability isolation | Exercise UKR-03/04 from RES-SEI-010; one client's authority and one direction's readiness do not imply the others. | UKG-04/06 |
| Qualified response process | Exercise UKR-08 against the selected process and registration; P07 establishes that billing-with-response requires a separate registration. | UKG-03/07 |
| Uncertain delivery and failed import | Exercise PG-04 and UKR-09; reconcile original exchange evidence and recover import without duplicate sending. | UKG-07 |
| Safe provider/authority change | Exercise UKR-10 and PG-06/07; prove historical access, in-flight handling and removal of revoked rights. | UKG-04/07/08 |
| Trust incident | Demonstrate expiry, revocation or rotation handling against PRD-SEI-245's acceptance checks. | UKG-05/08 |

Source IDs are defined in [RES-SEI-003](../RES-SEI-003-peppol-source-register.md). These are proposed acceptance evidence for qualification. They add no unauthorised component boundaries or new external API contract.

## Delivery sequence

1. **Research baseline:** source register, global analysis, UK scenarios and explicit gates. Available in this folder; subject to review.
2. **Consultation and asset qualification:** assign owners, choose the cohort and collect current-state evidence. Produces a grounded gap assessment.
3. **Requirements review:** propose targeted changes to the existing owning PRDs. Preserve permanent IDs and existing sources; request separate successors only when needed.
4. **Solution design:** after the relevant product decisions, define the selected interactions, contracts, data and operational controls in solution specifications.
5. **Qualified pilot and expansion:** proceed only with applicable approvals and acceptance evidence. Each new country/process/cohort needs its own qualification.

## Review decisions still open

- Which product and customer cohort should lead, and is the immediate purpose current-contract exchange, voluntary exchange or future-mandate preparation?
- Who holds each accountable role and who reviews the evidence?
- What does the reported Sage AP include today, and which dependencies remain contracted?
- Which profile/country comparisons most reduce UK design uncertainty?
- Which findings justify PRD changes now, and which depend on forthcoming official artefacts?

Research creation does not change existing PRD statuses, stable Confluence mappings or publication settings.
