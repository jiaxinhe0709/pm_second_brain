---
id: PRD-SEI-240
title: E-Invoicing as a Service - Peppol Access Point Readiness
type: prd
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-09-30
updated: 2026-10-07
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-233
  - PRD-SEI-230
  - PRD-SEI-234
  - ADR-SEI-001
confluence:
  publish: false
  space_key: ""
  parent_page_id: ""
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing as a Service - Peppol Access Point Readiness

An **exchange action** is one separately tracked action, such as delivering an invoice, submitting a public copy or reporting an invoice event. Each action has its own result. See the [shared definition](../context/GLO-SEI-001-e-invoicing-terminology.md#invoices-representations-and-rules).

## Decision summary

Assess whether Sage should operate a certified Peppol Access Point (AP) as a reusable network capability for E-Invoicing as a Service. A country pack decides whether Peppol is required, permitted or useful for a particular transaction; this PRD does not select a network for every country. South Africa is a candidate for discovery, not an approved Peppol rollout or a confirmed domestic mandate. The meaning of "NE" in the request remains to be confirmed.

Operating an AP is a distinct decision from connecting to a contracted AP provider. It also does not make Sage a compliant Spanish private-platform operator, replace the Spanish public solution or resolve the Phase 3 build/partner decision in ADR-SEI-001. No decision to remove Sovos or any other provider follows from this proposal.

## Problem and goals

The shared service currently models a selected sending AP provider and an independently selected receiving AP. It does not establish that Sage itself is certified to operate either role. Without a defined ownership and readiness boundary, country teams cannot compare Sage operation with a contracted provider on capability, cost, support and exit.

- Define a testable build-versus-provider decision for the AP role, including the legal entity, certification domain, operations and economics.
- Reuse PRD-SEI-227's country-neutral invoice, route, lifecycle and evidence contracts and PRD-SEI-233's participant/discovery model.
- Allow a country pack to activate Peppol only when its own legal, participant, document/process, route and reporting evidence permits it.
- Identify South African market demand, reachable participants and applicable official rules before specifying a South Africa delivery pack.

## Non-goals

- Declaring a South African e-invoicing mandate, Peppol authority, participant scheme or tax-reporting obligation without official evidence.
- Assuming AP certification includes an SMP service, participant-management authority, invoice signing or country compliance.
- Replacing the UK country pack, Spanish private-platform requirements, a customer's chosen provider or an existing contractual service by assertion.
- Publishing to Confluence or claiming Sage is a certified AP before a named entity and certification evidence exist.

## Users and use cases

| User | Use case | Outcome |
|---|---|---|
| Sage product/customer | Send a country-eligible invoice to a buyer using another AP | Document is validated, routed once and traceable across both APs |
| Buyer/customer | Receive at an eligible Sage-operated AP | Participant authority, supported document/process and delivery evidence are established |
| Country-pack owner | Evaluate a South African or other market opportunity | Legal scope, network eligibility, profiles and reporting are evidenced independently |
| Network operations | Handle failed delivery or changed service metadata | Reconcile possible sends before retry and retain the original route |
| Decision forum | Compare operating an AP with buying AP service | Named responsibilities, cost, certification path and exit risks are comparable |

## Requirements

| ID | Requirement |
|---|---|
| AP-FR1 | Before activation, name the operating legal entity and demonstrate applicable OpenPeppol membership, agreement, certification, service-domain and production trust readiness; a candidate/test role is not production authorisation. |
| AP-FR2 | Separate Sage-operated AP, contracted AP, Peppol network, SMP service, participant registration and country policy in configuration, customer communication and exchange evidence. |
| AP-FR3 | For each exchange, evaluate country-pack eligibility, participant scheme/value, document type, process, profile/version, direction and environment before dispatch or receipt. Block when any required authority or capability is unknown. |
| AP-FR4 | Support governed outbound and inbound transport, recipient discovery and acknowledgements under the applicable certified AP specifications; record raw and canonical outcomes without treating transport acceptance as commercial acceptance. |
| AP-FR5 | Bind the sending and receiving provider roles, participant, discovered endpoint, metadata freshness, trust material, representation and correlation identities to an immutable invoice exchange action. |
| AP-FR6 | Reconcile timeouts and outcome-unknown deliveries against network evidence before retrying, changing endpoints or switching providers. Preserve access to historic evidence after a switch. |
| AP-FR7 | Maintain purpose-specific certificate/key custody, renewal, revocation, incident response, continuity, support and monitoring for each approved environment and service domain. |
| AP-FR8 | Keep AP operation separate from optional SMP operation; if Sage publishes metadata or manages participants, obtain separately evidenced authority, ownership, migration and recovery controls. |
| AP-FR9 | A country pack owns local applicability, buyer/seller identifiers, invoice profiles, reporting, retention and effective dates; an AP connection alone cannot turn a route into a compliant country offering. |

## South Africa discovery gate

South Africa is a **candidate**, not a committed country pack. The OpenPeppol country-profile index consulted on 2026-09-30 does not list South Africa; absence from that index is not proof that South African participants cannot use Peppol. Do not infer an official mandate or national profile from network availability or supplier claims.

| Gate | Evidence needed before a South Africa pack or AP route is approved |
|---|---|
| Market and scope | Named customer segment, domestic or cross-border use case, buyer participation and demand; clarify what "NE" refers to |
| Legal and tax | Current South African authority guidance on invoice/VAT obligations, any government reporting and retention; legal review of AP operation and data handling |
| Network | Applicable Peppol service domain, participant identifiers, supported BIS document/process and recipient discovery against real counterparties |
| Operating model | Sage legal entity or contracted provider, certification path, support coverage, pricing and migration/exit evidence |

## Acceptance and rollout

| ID | Acceptance condition |
|---|---|
| AP-AC1 | Given a country pack with no approved Peppol route, an eligible-looking participant ID does not enable dispatch. |
| AP-AC2 | Given Sage is only a candidate AP service provider, production onboarding and traffic remain disabled while sandbox tests can proceed with approved test credentials. |
| AP-AC3 | Given a certified Sage AP and a different buyer AP with matching participant/document/process capability, one exchange produces immutable route and acknowledgement evidence identifying both AP roles. |
| AP-AC4 | Given an ambiguous send and a new SMP endpoint, operations reconcile the original message before any new attempt or provider switch. |
| AP-AC5 | Given South African eligibility or recipient capability is not evidenced, the country pack remains inactive and presents the missing decision rather than claiming compliance. |

Discovery -> certification and sandbox evidence -> country-specific conformance -> limited pilot -> production only after legal, security, operations and country-pack approvals. Each gate needs a named owner and a rollback/exit path. No production date is committed.

## Decision and open questions

| Question | Owner / gate |
|---|---|
| Is Sage operation preferable to a contracted AP for the first eligible country, on cost, control, time and risk? | Product, engineering and finance; compare both options against the same scope |
| Which Sage legal entity, service domains and jurisdictions would seek certification? Is an SMP also needed? | Legal, network operations and security |
| What does "NE" mean in the South Africa request, and which buyers, products and transaction flows are intended? | Requesting stakeholder / South Africa product owner |
| What official South African policy and market evidence supports Peppol for those flows? | Country compliance and local product team |
| How are provider changes, participant registration, service metadata and in-flight invoices migrated? | Network operations and architecture |

## Evidence

- [OpenPeppol membership categories](https://peppol.org/join/): candidate AP providers are not authorised production providers; certified AP and SMP roles are distinct. Accessed 2026-09-30.
- [OpenPeppol country profiles](https://peppol.org/learn-more/country-profiles/): South Africa is not in the listed profile index; this does not establish legal or network unavailability. Accessed 2026-09-30.
- [PRD-SEI-233](PRD-SEI-233-peppol-multi-address-and-endpoint-routing.md): participant, SMP endpoint and AP provider are separate concepts; no Sage-operated AP decision is made there.
- [PRD-SEI-227](PRD-SEI-227-e-invoicing-as-a-service.md): the shared service separates jurisdiction, network, provider role and technical adapter.

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-09-30 | Initial discovery draft for reusable AP operation and South Africa candidate assessment | |