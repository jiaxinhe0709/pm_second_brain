---
id: PRD-SEI-245
title: E-Invoicing — Peppol Access Point Validation and Certification
type: prd
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-05
updated: 2026-10-05
reviewers: []
related:
  - PRD-SEI-240
  - PRD-SEI-227
  - PRD-SEI-233
  - PRD-SEI-241
  - PRD-SEI-242
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: ""
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Peppol Access Point Validation and Certification

## Revision overview

This separately readable successor builds on [PRD-SEI-240](PRD-SEI-240-peppol-access-point-service-readiness.md). It exists because the stakeholder now reports that Sage **has a Peppol Access Point**, while validation and certificates are still outstanding. It changes the immediate decision from whether to obtain an AP to how to prove the existing AP and its operating entity are ready for the intended service domain and production use. The predecessor's distinctions between AP, SMP, country compliance, routing, and historical evidence remain valid. The meaning of “has an AP”, the responsible legal entity, agreement and test-certificate state, exact test scope, and first country/customer cohort remain open. The predecessor file is unchanged.

## Decision summary and readiness

**Stakeholder-reported current state:** Sage has an AP implementation or entitlement. This has not yet been evidenced as an OpenPeppol-certified production service. **Current delivery phase: validation and accreditation preparation.** Keep production traffic and customer claims of certified Sage AP service disabled until the applicable authority accepts the evidence and the production certificate and operational gates are complete.

The product outcome is a Sage-operated Peppol send/receive capability whose network eligibility, security, supported documents, customer scope, and recovery behaviour can be demonstrated before a limited pilot. AP certification is a network operating gate. It does not by itself authorise a country-specific e-invoicing offer, an SMP service, participant registration, tax reporting, or buyer commercial acceptance.

| Phase | Capability and decision | Status |
|---|---|---|
| Confirm asset and authority | Identify AP software/hosting, operating legal entity, applicable Peppol Authority, service domain, agreement and existing certificates | Current; evidence requested |
| Validate in test | Obtain/confirm AP test PKI certificate, configure isolated AS4 endpoint, run required OpenPeppol testbed suite and obtain acceptance of test report | Required before production PKI request; completion unconfirmed |
| Establish production trust | Request and securely deploy AP production PKI certificate after accepted tests; separately validate HTTPS server certificate and key operations | Pending |
| Pilot | Exercise approved directions, documents, participants and end-to-end lifecycle with a named country pack and limited cohort | Proposed, subject to gates |
| Scale | Activate more countries, profiles and participants through separate eligibility and operational approval | Future |

## Why this matters

An AP that Sage owns but cannot yet prove ready creates a gap between a technical asset and a sellable service. An ERP may create a valid invoice while the AP cannot legally or technically exchange it. Premature route activation could cause failed or ambiguous deliveries; premature marketing could imply certification that has not been granted. Conversely, a clear evidence path lets product and operations reuse the AP without repeating country-independent readiness work for every market.

| Actor | Needed outcome |
|---|---|
| Sage product and country owner | Know which country/document/process/direction may use the AP and when |
| ERP/API consumer and customer | Receive truthful availability, validation, send and feedback states |
| AP engineering and network operations | Prove conformance, maintain keys, detect failures, reconcile unknown outcomes |
| Security/legal/compliance | Verify entity, agreement, service domain, certificate custody and country obligations |
| OpenPeppol / relevant Peppol Authority | Receive the required onboarding evidence and approve network participation |

## Terms and business rules

| Term | Meaning for this PRD |
|---|---|
| AP asset | Implemented or procured AP software/service; ownership and hosting must be evidenced. Its existence is not certification. |
| AP test PKI certificate | OpenPeppol-issued credential for the AP test environment and testbed; not a production credential. |
| AP production PKI certificate | Network credential requested after accepted onboarding tests; distinct from the AP HTTPS server certificate. |
| HTTPS server certificate | Certificate securing the AS4 endpoint's web connection; not issued by OpenPeppol according to its AP setup guide. |
| Certified AP service | A legal entity authorised for the applicable service domain/jurisdiction and operating with accepted network tests and production credentials. |
| Country offering | Additional product/legal decision about eligible participants, formats, process, reporting and retention. |

| ID | Condition | Business rule | Basis |
|---|---|---|---|
| AP-BR1 | Sage owns or hosts an AP asset | Do not describe it as certified or production-ready solely from possession | Stakeholder update plus OpenPeppol onboarding sequence |
| AP-BR2 | A route would use Sage as the sending or receiving AP | Require applicable legal authority, accepted conformance evidence, valid production trust material and operational approval | OpenPeppol guidance; proposed Sage activation policy |
| AP-BR3 | A country or participant is proposed | Country pack independently approves the document/process, participant identity, direction and local obligations | PRD-SEI-227/233 |
| AP-BR4 | Certificates or endpoint metadata change | Preserve original invoice route and message evidence; apply the new material prospectively after verification | PRD-SEI-233/242 |

## Scope and evidence

This PRD owns the **AP accreditation and production-readiness path** for Sage's reported asset: entity/agreement verification, test setup, conformance evidence, certificate issuance and custody, operational validation, pilot gate and expiry/incident controls. [PRD-SEI-241](PRD-SEI-241-ubl-validation-service.md) owns the shared validation handoff for invoice content; this PRD requires evidence that outbound documents are valid under the selected BIS before AP transport. [PRD-SEI-233](PRD-SEI-233-peppol-multi-address-and-endpoint-routing.md) owns participant and endpoint routing. [PRD-SEI-242](PRD-SEI-242-peppol-lifecycle-feedback.md) owns post-send feedback.

Out of scope: SMP operation or participant registration unless separately approved; a general assertion of certification across all service domains or countries; South Africa rollout without the discovery gates in PRD-SEI-240; replacing contracted APs by default; and any Confluence publication.

Official sources reviewed 2026-10-05:

| Evidence | What it establishes | Limit / next evidence |
|---|---|---|
| [OpenPeppol AP setup guide v2.1](https://peppol.org/wp-content/uploads/2024/04/how_to_set-up_a__post-award__peppol_access_point_v2.1.pdf) | Membership, authority agreement, test certificate, AS4 testbed, approved test report and production PKI certificate are distinct steps; AP PKI and HTTPS server certificates serve different purposes | Confirm current authority-specific requirements and Sage's completed steps |
| [OpenPeppol test and onboarding guide v1.4](https://peppol.org/wp-content/uploads/2024/03/Peppol_TestbedAndOnboarding_v1.4.pdf) and [testbed](https://www.testbed.peppol.org/) | AP test PKI and HTTPS AS4 endpoint are test prerequisites; successful acceptance is needed before production PKI issuance | Confirm exact current suite/version and retain accepted report |
| [OpenPeppol membership categories](https://peppol.org/join/) | Candidate AP and certified AP memberships are distinct; candidate status does not authorise production service | Verify Sage legal entity and category with official records |
| Stakeholder update, 2026-10-05 | Sage now has an AP; validation and certificates still need work | Asset type, evidence and completed onboarding stages are unverified |

## Required journey and gates

1. **Inventory without activation.** AP owner records product/vendor, hosting, environment, AS4 endpoint, legal entity, intended service domains and countries, signed agreements, and certificate state. Product exposes `not ready` for production routes.
2. **Establish authority.** Legal/network owner verifies OpenPeppol membership and the Peppol Service Provider Agreement with the relevant authority for the operating entity and intended domain. Resolve any local authority-specific requirements.
3. **Prepare test trust.** Security owner obtains or verifies the AP test PKI credential through the authorised process; configures an isolated test AP and a separately trusted HTTPS server certificate. Secrets stay in approved stores, with references and fingerprints in the evidence record.
4. **Run conformance.** Engineering executes the current required AS4/eDelivery suite, captures test configuration, versions, outcomes and defects, then submits the report through the prescribed process. Failed tests return to remediation and rerun; a local pass alone is not authority acceptance.
5. **Obtain production trust.** After report acceptance, authorised owner requests the production AP PKI certificate, verifies subject/entity/domain and validity, deploys it with dual control, tests connectivity and publishes only approved endpoint metadata.
6. **Prove service behaviour.** Before a pilot, test eligible outbound and inbound scenarios, valid/invalid BIS documents, participant discovery, technical acknowledgement, unknown outcomes, recovery, certificate expiry warning and rollback. Bind original route and message IDs to each exchange.
7. **Approve and pilot.** Product, country compliance, security and operations sign off a named cohort and route. Enable narrowly, monitor, reconcile incidents, and retain a kill switch that stops *new* sends without erasing historical evidence or losing inbound obligations.

## Functional and operational requirements

| ID | Requirement |
|---|---|
| APV-FR1 | The AP owner shall record the specific asset, hosting model, operating legal entity, authority, service domains, environments, vendor dependencies and accountable contacts before test or production activation. |
| APV-FR2 | The readiness record shall separately show membership/agreement, test PKI, AS4 endpoint/HTTPS certificate, test execution, authority acceptance, production PKI, operations approval and country-pack activation, each with owner, evidence reference and date. |
| APV-FR3 | Production routing shall remain disabled until the required agreement, accepted test report, valid production AP PKI credential, approved HTTPS endpoint, security/operations sign-off and country-specific eligibility are evidenced. |
| APV-FR4 | Test and production traffic, endpoints, discovery metadata, keys and credentials shall be isolated; an AP test credential shall never authorise a production exchange. |
| APV-FR5 | The AP shall validate or obtain trustworthy evidence of validation of the exact outbound Peppol BIS document and version before accepting it for transport; a validation pass shall not imply delivery. |
| APV-FR6 | A send/receive leg shall retain AP entity/role, participant, document/process, endpoint, certificate fingerprint/reference, configuration/version, message correlation and qualified acknowledgements. |
| APV-FR7 | A timeout after possible transmission shall produce an outcome-unknown case and block blind resend or provider/endpoint switch until the original message is reconciled. |
| APV-FR8 | Operations shall monitor certificate expiry, revocation, endpoint health, failed conformance checks and message failures, with named response owners and evidence-preserving recovery. |
| APV-FR9 | Certificate rotation and AP rollback shall verify new connectivity before cutover, retain access to historic evidence, and disable only affected new routes when trust fails. |
| APV-FR10 | Customer and internal availability views shall distinguish AP asset present, test-ready, conformance-submitted, certified/credentialed, pilot-ready and country-route-active without implying later states from earlier ones. |

Proposed readiness states are **asset recorded → authority verified → test ready → test submitted → test accepted → production trust ready → pilot approved → route active**. A rejection or expiry returns the affected gate to blocked; it does not delete its history. This is a conceptual workflow, not an approved API or persistence schema.

## Acceptance and release gate

| ID | Demonstration |
|---|---|
| APV-AC1 | Given Sage has an AP asset but lacks accepted test evidence or a production credential, a customer production send through Sage AP is blocked and the missing gate is visible. |
| APV-AC2 | Given a valid AP test PKI credential and isolated endpoint, the required test suite can run and produces versioned evidence; a failed case remains open until rerun and authority acceptance. |
| APV-AC3 | Given accepted conformance evidence, the production PKI request and deployment record identifies the same approved legal entity/domain and retains certificate metadata without exposing private keys. |
| APV-AC4 | Given a valid production AP credential but no approved country route or document/process capability, production dispatch remains blocked. |
| APV-AC5 | Given an ambiguous send and a changed endpoint or certificate, operations reconcile the original message before retry or switch; historical route evidence remains readable. |
| APV-AC6 | Given credential expiry or revocation, new affected sends stop, an alert names an owner, and in-flight/historic exchanges remain available for reconciliation. |

No production date or success target is asserted. The AP owner should baseline test pass rate and time to acceptance; operations should baseline delivery and reconciliation measures during the pilot. A production go/no-go record must include authority evidence, security sign-off, supported document/process matrix, country approval, support rota, incident path, capacity test and rollback owner.

## Risks, decisions and open questions

| Item | Owner / impact |
|---|---|
| What does “Sage has an AP” mean: owned implementation, hosted software, contracted service, or an already registered entity? | AP engineering and product; determines evidence and operating responsibility |
| Which legal entity, Peppol Authority, service domains and agreement are in scope? | Legal/network owner; blocks test/certificate and production claims |
| Are test PKI, HTTPS server and production PKI certificates all pending, or has any one been issued? | Security/AP owner; determines immediate critical path |
| Which current test suite and local authority checks apply, and who submits the report? | AP engineering and authority contact; blocks production PKI request |
| Which first country, ERP, direction, BIS document/process and pilot counterparties? | Country product and platform product; blocks pilot scope and country activation |
| Who operates the AP, on-call support, key renewal and certificate incidents? | Operations/security; blocks production readiness |
| Does Sage also intend to operate an SMP or use a contracted SMP? | Network product; separate authority and migration decision |

**Current decision:** proceed with validation planning for the reported Sage AP. **Open decision:** production activation requires named evidence at every gate above; this draft does not certify Sage or select a country route.

## Revision history

| Date | Change | Pull request |
|---|---|---|
| 2026-10-05 | Separate successor focused on validation, accreditation and certificates after stakeholder reported Sage has an AP | |
