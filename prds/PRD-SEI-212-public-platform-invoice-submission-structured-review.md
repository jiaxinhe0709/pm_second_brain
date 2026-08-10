---
id: PRD-SEI-212
title: Public Platform — Invoice Submission — Structured Review
type: prd
status: draft
version: 1
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers:
  - dianna.hindle@sage.com
related:
  - PRD-SEI-103
  - https://confluence.sage.com/spaces/DNBU/pages/837610648/Public+Platform+Onboard
  - https://confluence.sage.com/spaces/DNBU/pages/837610656/UBL+2.5+Invoice+Submission+Send
  - PRD-SEI-102
  - PRD-SEI-201
  - research/PRD-SEI-201-spain-use-case-evidence.md
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837610656"
  page_id: ""
  title: Public Platform — Invoice Submission — Structured Review
  layout: two_left_sidebar
  toc: true
---

# Public Platform — Invoice Submission — Structured Review

## Revision overview

| Area | Summary |
|---|---|
| Predecessor | Based on PRD-SEI-103, which remains unchanged as the predecessor document. |
| Reason for this successor | Provide an individually readable successor that publishes through a native Confluence two-column layout with a left-sidebar Table of Contents. |
| Material changes | Assigns permanent ID PRD-SEI-212, adds this revision overview, and adds Confluence layout and navigation metadata for publication as a new child page. |
| Unchanged areas | Business analysis, research evidence, scenarios, requirements, visuals, acceptance criteria, risks, decisions and open questions remain unchanged from PRD-SEI-103. |
| Decisions still open | All product, provider, regulatory and architecture decisions remain as recorded in PRD-SEI-103; this successor introduces no new product decision. |

## Overview

This Phase 1 feature defines how a Sage ERP submits an outbound electronic invoice to Spain's public e-invoicing solution through Sage's platform service.

It covers the product boundary from an ERP's request to send an invoice through:

- customer and outbound-route eligibility;
- mapping to the approved Spanish public UBL profile;
- syntax, semantic and public-profile validation;
- rejection of embedded or integrated attachments before transmission;
- idempotent web-service submission;
- interpretation of admitted, rejected, partial and outcome-unknown responses;
- preservation of public invoice identity and receipt evidence;
- safe retry and reconciliation; and
- visibility for the ERP, customer and operations.

The existing Confluence title refers to **UBL 2.5**. Current official evidence confirms EN 16931 using UBL syntax, but the referenced European syntax binding is UBL 2.1. UBL 2.5 was published by OASIS as a Committee Specification in April 2026; that does not establish it as the version accepted by Spain's public solution.

The product requirement is therefore a **versioned public invoice profile**, not an unverified hard-coded `UBL 2.5` label. The exact version, customization/profile identifiers, schemas, code lists and AEAT validation rules are production gates.

> **Validate before transmission, identify every submission once, and never convert an unknown external outcome into a duplicate invoice.**

### Delivery context

| Phase | Outbound capability | This PRD's responsibility |
|---|---|---|
| **Phase 1 — Public Platform Connection** | Public onboarding, outbound submission, inbound consultation and public lifecycle | **Deliver safe public invoice submission using the approved UBL/EN 16931 profile** |
| Phase 2 — Private Platform Connections | Public/private coexistence and independent route changes | Preserve the outbound route, connection and schema/profile used by each invoice |
| Phase 3 — Platform Expansion | Private-first and provider switching | Reuse canonical validation and submission orchestration while retaining provider-specific evidence |

## Product principles

1. **UBL version and Spanish public profile are related but not interchangeable.**
2. **An invoice that is valid XML may still fail UBL schema, EN 16931, Spanish profile or public-service rules.**
3. **Sage should reject known-invalid content before calling the public service.**
4. **Embedded attachments are a product validation error, not a retriable platform failure.**
5. **Submission acceptance is not the same as recipient delivery, commercial acceptance or payment.**
6. **A timed-out mutation has an unknown outcome until reconciled.**
7. **The exact document sent, validation-pack version and external evidence must remain historically explainable.**
8. **Current outbound route changes must not rewrite an invoice already bound to Public.**

## Submission and recovery visual

<!-- confluence-html-macro:start -->
<div class="ppis-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .ppis-visual *{box-sizing:border-box}
    .ppis-visual h2{margin:0;color:#172b4d;font-size:18px;font-weight:600}
    .ppis-visual .ppis-subtitle{margin:6px 0 18px;color:#6b778c;font-size:12px}
    .ppis-visual svg{display:block;width:1100px;height:520px;background:#fafbfc;border:1px solid #ebecf0;border-radius:8px}
    .ppis-visual .ppis-node{fill:#fff;stroke:#36b37e;stroke-width:2}
    .ppis-visual .ppis-public{fill:#deebff;stroke:#0052cc;stroke-width:2}
    .ppis-visual .ppis-success{fill:#e3fcef;stroke:#36b37e;stroke-width:2}
    .ppis-visual .ppis-alert{fill:#ffebe6;stroke:#de350b;stroke-width:2}
    .ppis-visual .ppis-retry{fill:#fff7d6;stroke:#ff991f;stroke-width:2}
    .ppis-visual .ppis-optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:2;stroke-dasharray:7 5}
    .ppis-visual .ppis-title{fill:#172b4d;font-size:12px;font-weight:700;text-anchor:middle}
    .ppis-visual .ppis-copy{fill:#42526e;font-size:10px;text-anchor:middle}
    .ppis-visual .ppis-label{fill:#6b778c;font-size:10px;font-weight:600;text-anchor:middle}
    .ppis-visual .ppis-path{fill:none;stroke:#36b37e;stroke-width:2.5}
    .ppis-visual .ppis-path-alert{fill:none;stroke:#de350b;stroke-width:2.5;stroke-dasharray:6 5}
    .ppis-visual .ppis-path-retry{fill:none;stroke:#ff991f;stroke-width:2.5;stroke-dasharray:7 5}
    .ppis-visual .ppis-path-optional{fill:none;stroke:#6b778c;stroke-width:2;stroke-dasharray:7 5}
    .ppis-visual .ppis-notes{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;width:1100px;margin-top:12px}
    .ppis-visual .ppis-note{padding:10px 12px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;background:#fff;font-size:11px;line-height:1.4}
    .ppis-visual .ppis-note strong{display:block;margin-bottom:3px;color:#172b4d}
  </style>
  <h2>Public Invoice Submission and Outcome Recovery</h2>
  <p class="ppis-subtitle">Sage validates the invoice against a controlled profile before submission and reconciles any response that is lost after transmission.</p>
  <svg viewBox="0 0 1100 520" role="img" aria-label="ERP invoice request flows through eligibility, UBL mapping and validation, public web-service submission and receipt persistence, with correction and unknown-outcome reconciliation loops">
    <rect class="ppis-node" x="25" y="185" width="155" height="90" rx="10"/>
    <text class="ppis-title" x="102" y="216">Accept send request</text>
    <text class="ppis-copy" x="102" y="237">Legal entity + invoice</text>
    <text class="ppis-copy" x="102" y="252">idempotency identity</text>

    <rect class="ppis-node" x="220" y="185" width="155" height="90" rx="10"/>
    <text class="ppis-title" x="297" y="216">Resolve Public route</text>
    <text class="ppis-copy" x="297" y="237">Outbound ready</text>
    <text class="ppis-copy" x="297" y="252">environment authorised</text>

    <rect class="ppis-node" x="415" y="185" width="155" height="90" rx="10"/>
    <text class="ppis-title" x="492" y="216">Map and validate</text>
    <text class="ppis-copy" x="492" y="237">UBL + EN 16931</text>
    <text class="ppis-copy" x="492" y="252">Spain/AEAT profile</text>

    <rect class="ppis-public" x="610" y="185" width="155" height="90" rx="10"/>
    <text class="ppis-title" x="687" y="216">Submit web service</text>
    <text class="ppis-copy" x="687" y="237">Exact versioned payload</text>
    <text class="ppis-copy" x="687" y="252">correlation evidence</text>

    <rect class="ppis-node" x="805" y="185" width="155" height="90" rx="10"/>
    <text class="ppis-title" x="882" y="216">Classify response</text>
    <text class="ppis-copy" x="882" y="237">Admitted / rejected</text>
    <text class="ppis-copy" x="882" y="252">partial / unknown</text>

    <rect class="ppis-success" x="985" y="185" width="95" height="90" rx="45"/>
    <text class="ppis-title" x="1032" y="216">Persist</text>
    <text class="ppis-copy" x="1032" y="237">Public ID</text>
    <text class="ppis-copy" x="1032" y="252">receipt</text>

    <path class="ppis-path" d="M180 230 L210 230"/>
    <polygon points="210,230 200,224 200,236" fill="#36b37e"/>
    <path class="ppis-path" d="M375 230 L405 230"/>
    <polygon points="405,230 395,224 395,236" fill="#36b37e"/>
    <path class="ppis-path" d="M570 230 L600 230"/>
    <polygon points="600,230 590,224 590,236" fill="#36b37e"/>
    <path class="ppis-path" d="M765 230 L795 230"/>
    <polygon points="795,230 785,224 785,236" fill="#36b37e"/>
    <path class="ppis-path" d="M960 230 L975 230"/>
    <polygon points="975,230 965,224 965,236" fill="#36b37e"/>

    <polygon class="ppis-alert" points="492,320 552,345 552,395 492,420 432,395 432,345"/>
    <text class="ppis-title" x="492" y="356">Correctable rejection</text>
    <text class="ppis-copy" x="492" y="375">field, profile or</text>
    <text class="ppis-copy" x="492" y="390">embedded attachment</text>
    <path class="ppis-path-alert" d="M492 275 L492 310"/>
    <polygon points="492,310 486,300 498,300" fill="#de350b"/>
    <path class="ppis-path-alert" d="M432 370 C330 370 300 315 298 285"/>
    <polygon points="298,285 292,295 304,295" fill="#de350b"/>
    <text class="ppis-label" x="345" y="345">return actionable errors</text>

    <polygon class="ppis-retry" points="687,320 747,345 747,395 687,420 627,395 627,345"/>
    <text class="ppis-title" x="687" y="354">Transient before send</text>
    <text class="ppis-copy" x="687" y="375">bounded retry</text>
    <path class="ppis-path-retry" d="M687 275 L687 310"/>
    <polygon points="687,310 681,300 693,300" fill="#ff991f"/>
    <path class="ppis-path-retry" d="M627 370 C585 340 585 295 610 250"/>
    <polygon points="610,250 600,256 612,262" fill="#ff991f"/>

    <rect class="ppis-optional" x="805" y="335" width="230" height="78" rx="10"/>
    <text class="ppis-title" x="920" y="365">Outcome reconciliation</text>
    <text class="ppis-copy" x="920" y="385">Timeout after possible send:</text>
    <text class="ppis-copy" x="920" y="400">find receipt/result before retry</text>
    <path class="ppis-path-optional" d="M882 275 L882 325"/>
    <polygon points="882,325 876,315 888,315" fill="#6b778c"/>
    <path class="ppis-path-optional" d="M1035 335 C1080 320 1070 290 1040 275"/>
    <polygon points="1040,275 1051,276 1046,287" fill="#6b778c"/>
  </svg>
  <div class="ppis-notes">
    <div class="ppis-note"><strong>Profile control</strong>The accepted UBL version, Spanish rules, AEAT schemas and code lists are one immutable validation-pack version attached to the submission.</div>
    <div class="ppis-note"><strong>Attachment rule</strong>Embedded or integrated files are rejected before transmission. An electronic signature is treated separately according to the final public specification.</div>
    <div class="ppis-note"><strong>Mutation safety</strong>A timeout after bytes may have reached the public service is not automatically retried. Sage first reconciles using its idempotency and public invoice identities.</div>
  </div>
</div>
<!-- confluence-html-macro:end -->

## Problem and business objective

The current Confluence page contains only:

> attachments not allowed — error

That is a useful constraint, but it does not define an invoice-submission product. It leaves unanswered:

- which actor may submit on behalf of which legal entity;
- whether Sage receives business data, an ERP-generated UBL document, or both;
- which exact UBL version and Spanish customization/profile apply;
- how schema validation differs from EN 16931 and AEAT validation;
- what counts as an attachment and whether a signature is exempt;
- whether invoices are sent individually or in batches;
- how admitted and rejected items are represented in a mixed response;
- when the invoice becomes legally/operationally submitted;
- which public identifier and receipt evidence must be retained;
- how repeated requests are deduplicated;
- what happens when the request times out after transmission;
- whether a rejected invoice may reuse the same number/identity after correction;
- how an improper submitted invoice is withdrawn or corrected; and
- how submission continues or catches up after a public-service outage.

Without a defined product boundary:

- different ERPs may generate incompatible UBL variants;
- a document may pass XSD but fail the Spanish business profile;
- customers may discover the attachment prohibition only after an external rejection;
- automatic retry may create a duplicate or collide with an existing original;
- an admitted invoice may be shown incorrectly as delivered or commercially accepted;
- a lost response may leave Sage and the public service in contradictory states;
- a route switch may send a Public-bound invoice to a private provider;
- an external profile change may alter historical validation behaviour; and
- operations may lack the exact payload, validation version and receipt needed to investigate.

The objective is to give every eligible Sage ERP one stable, asynchronous submission contract that produces one of four explainable outcomes:

1. **Correctable before transmission** — Sage identifies fields/profile/attachment issues.
2. **Rejected by the public service** — rejection and reason are preserved and mapped.
3. **Admitted by the public service** — public identity and receipt evidence are retained.
4. **Outcome unknown** — Sage reconciles before any resubmission.

## Business value

| Stakeholder | Value |
|---|---|
| Customer/accountant | Receives actionable errors before an invalid invoice is transmitted and can trust that retry will not duplicate it |
| Sage ERP | Uses one stable platform contract rather than implementing AEAT transport, profile validation and recovery |
| Platform engineering | Maintains one controlled validation pack and submission orchestrator for public outbound |
| Operations/support | Can identify the exact stage, error ownership, payload/profile version and receipt |
| Product/compliance | Can update the Spanish profile without pretending every UBL minor version is automatically accepted |

## Definitions and concept boundaries

| Term | Definition |
|---|---|
| UBL | OASIS Universal Business Language, an XML business-document family |
| UBL version | The version of the UBL schema/library used by the invoice document |
| EN 16931 | European semantic data model for core electronic invoice elements and associated syntax bindings |
| Spanish public profile | The final AEAT constraints, required/conditional fields, code lists, cardinalities and extensions applied to public invoices |
| Validation pack | Immutable versioned set of XSD, EN 16931 rules, Spanish/AEAT rules, code lists and implementation configuration |
| Schema validation | Checks XML structure, namespace, type and cardinality against the selected XSD |
| Semantic/profile validation | Checks cross-field, business-term, country and public-service rules not fully represented by XSD |
| Embedded/integrated attachment | Another file carried inside the invoice document, for example encoded binary content |
| Electronic signature | Cryptographic signature evidence; the draft order treats a signature accompanying interconnection separately from prohibited embedded files |
| Submission | Mutating request to make an invoice available through the public solution |
| Admission | Public-service validation outcome accepting the submitted item |
| Receipt | Public-service evidence after submission, expected in the draft to include a secure verification code |
| Delivery | Invoice becomes available to or reaches the recipient; not proven solely by submission admission |
| Commercial acceptance/rejection | Recipient's business response; separate from technical admission |
| Outcome unknown | Sage cannot prove whether the public service admitted/rejected the request, usually because the response was lost after possible transmission |
| Unique public invoice code | Draft identity derived from issuer NIF, invoice number/series and issue date |
| Faithful copy | UBL representation deposited when the original invoice was not emitted/interconnected using the public solution; not the Phase 1 primary submission in this PRD |
| Baja | Traceable withdrawal/removal message described by the draft for an improper invoice/copy; not automatically equivalent to correction or commercial cancellation |

### Submission stages must remain distinct

| Stage | Evidence | What Sage may say | What Sage must not infer |
|---|---|---|---|
| Locally valid | Validation-pack result | Ready to submit | Accepted by public solution |
| Transmitted | Transport/correlation evidence | Request sent/awaiting result | Admitted |
| Admitted | Public response for the item | Accepted by public solution | Delivered or commercially accepted |
| Receipt recorded | Secure verification/public receipt evidence | Submission evidence retained | Paid |
| Delivered/available | Confirmed lifecycle evidence | Available/delivered according to approved mapping | Commercially accepted |
| Commercially accepted/rejected | Recipient lifecycle event | Business response received | Payment |
| Paid | Payment-state evidence | Paid according to applicable lifecycle | — |

## Scope

### In scope for Phase 1

- outbound eligibility by legal entity, environment and effective public route;
- stable Sage ERP submission and operation-status contract;
- canonical-to-public UBL mapping or controlled acceptance of ERP-supplied UBL;
- versioned UBL/EN 16931/Spanish public validation;
- explicit rejection of embedded/integrated files;
- signature handling according to the final public contract;
- web-service submission to the public solution;
- per-item admitted/rejected result processing;
- public unique identity, provider references and receipt evidence;
- request idempotency, duplicate protection and concurrency;
- safe retry for known pre-transmission failure;
- reconciliation for post-transmission timeout/unknown result;
- status visibility, operations, audit and metrics;
- backlog/recovery behaviour during external technical outage; and
- preservation of route, profile, payload and submission history.

### Dependencies

- Public Platform Onboarding for legal entity, representation and credentials.
- Routing context for the effective Public outbound connection.
- Secure certificate/signature capability.
- Canonical invoice data and ERP field semantics.
- Public invoice lifecycle/status feature.
- PRD-SEI-102 for public consultation/reconciliation capabilities where they can resolve submission state.
- Final ministerial order, AEAT schemas, code lists, WSDL/OpenAPI, sandbox and volumetry.
- Correction/credit-note and baja product rules.

### Out of scope

- public invoice consultation/retrieval detailed behaviour;
- private-provider submission;
- Public ↔ Private transition orchestration;
- customer accounting approval before the ERP calls Sage;
- legal/tax advice or deciding whether an invoice should exist;
- embedding PDFs, images, spreadsheets or other files in the public invoice;
- inventing a separate attachment upload endpoint;
- committing to UBL 2.5 before AEAT confirms it;
- complete payment, rejection, correction or collection lifecycle;
- manual AEAT web-form submission by Sage; and
- detailed faithful-copy submission unless added as a separately approved Phase 1 capability.

## Actors and business scenarios

| Scenario | Primary actor | Expected outcome | Exception/continuity |
|---|---|---|---|
| Submit valid invoice | ERP/customer | One public submission is admitted and receipt evidence is available | Asynchronous operation remains distinct from later delivery |
| Correct invalid invoice | ERP/customer | Field-level actionable errors are returned before transmission | No public invoice identity is created by Sage |
| Submit invoice containing embedded PDF | ERP/customer | Sage rejects it as an unsupported embedded file | Guidance explains how supporting information may be represented/referenced if allowed |
| Retry same request | ERP | Existing operation/result is returned | No second public mutation |
| Public service rejects item | Platform | Rejection reason is mapped and retained | Correctability/reuse of identity follows confirmed public rules |
| Mixed batch response | Platform | Each item receives its own admitted/rejected outcome | Batch transport success does not hide item failure |
| Response is lost after send | Platform/operations | Operation becomes outcome-unknown and reconciles | No blind retry |
| Public service is unavailable before send | Platform | Bounded retry/backlog applies | Customer sees delayed, not rejected |
| Route changes after submission started | Routing/platform | Invoice retains its original Public routing snapshot | New invoices follow the new effective route |
| Improper invoice must be withdrawn/corrected | Customer/ERP | Approved baja/correction journey preserves traceability | Withdrawal is not silent deletion |

## Business rules

| ID | Condition | Rule | Rationale/evidence | Status |
|---|---|---|---|---|
| BR1 | Invoice uses the public solution | It must conform to EN 16931 under the approved UBL and AEAT profile | RD 238/2026 + draft order | Confirmed direction; final profile open |
| BR2 | A document contains an embedded/integrated file | It must not be submitted to the public solution | Draft order Articles 3.6 and 4.4 | Confirmed draft constraint; final order gate |
| BR3 | Electronic signature accompanies interconnection | It is evaluated under signature rules, not treated automatically as an embedded attachment | Draft order Article 3.6 | Confirmed draft distinction; format open |
| BR4 | ERP repeats the same logical submission | Sage returns/reuses the existing operation and does not send a second mutation | Duplicate protection | Proposed for approval |
| BR5 | Sage cannot prove whether transmission reached AEAT | Outcome must be reconciled before retry | Mutation safety | Proposed for approval |
| BR6 | Public response admits one item | Invoice may be shown as admitted, not delivered/accepted/paid | Lifecycle separation | Proposed for approval |
| BR7 | Public response contains multiple item outcomes | Each invoice result is processed independently | Draft response is a list of admitted/rejected items | Confirmed draft behaviour |
| BR8 | Public service already holds the same original unique code | Duplicate submission must not create another invoice | Draft duplicate rejection | Confirmed draft behaviour |
| BR9 | Invoice route is fixed for submission | Later route change does not rewrite its Public context | PRD-SEI-201 principle | Confirmed |
| BR10 | Validation pack changes | Existing submissions retain the pack/version used; new submissions use only an approved effective version | Audit and reproducibility | Proposed for approval |
| BR11 | Invoice is improper after admission | It follows approved baja/correction behaviour with retained traceability | Draft order | Confirmed direction; business sequence open |
| BR12 | Public service has a technical incident | Backlogged work is retained and sent under the final permitted recovery window | Draft four-day recovery provision | Draft constraint; final legal confirmation required |

## Research and evidence

### Evidence register

| Evidence | Confidence | What it confirms | Limitation/follow-up |
|---|---|---|---|
| [UBL 2.5 Invoice Submission (Send)](https://confluence.sage.com/spaces/DNBU/pages/837610656/UBL+2.5+Invoice+Submission+Send), revision 3 | Low/medium internal | Attachments are expected to be rejected; submission feature is Phase 1 | Does not define UBL contract, journeys, errors or evidence source |
| [Real Decreto 238/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295), Articles 2, 6, 7 and 11 | High official | Public solution requires UBL terms defined through EN 16931/EU syntax reference; NIFs and minimum invoice content matter; unique identity and public lifecycle are required | Detailed schemas, services and volumetry depend on implementing order/AEAT |
| [Commission Implementing Decision (EU) 2017/1870](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017D1870) | High official | Referenced UBL invoice/credit-note syntax is ISO/IEC 19845:2015 / UBL 2.1 | Later Spanish technical profile could explicitly evolve; final AEAT artefacts remain authoritative |
| [April 2026 Spanish draft ministerial order](https://www.hacienda.gob.es/sgt/normativadoctrina/proyectos/16042026-proyecto-pom-factura-electronica.pdf), Articles 3–6 | Medium-high official draft | EN 16931/UBL, AEAT-hosted specifications/volumetry, no embedded files, web-service validation, per-item admitted/rejected results, receipt/verification code, duplicate rules, unique code and technical-incident handling | Draft, not final; service artefacts/error catalogue are not included |
| [OASIS UBL 2.5 Committee Specification 01](https://docs.oasis-open.org/ubl/UBL-2.5.html) | High standards source | UBL 2.5 exists as an April 2026 Committee Specification; UBL minor versions are designed for backward compatibility | Existence/backward compatibility does not prove AEAT accepts `UBLVersionID=2.5` |
| Internal Spain use-case evidence, UC1/UC4/UC6/UC7 | Medium internal | Public UBL submission, transformation, parallel PDF and correction are important scenarios | Exact format, PDF transition obligation and correction rules need official/local confirmation |

### Confirmed findings

1. Public invoices must use the UBL syntax/profile required by Spain's implementing rules.
2. The Spanish draft requires the EN 16931 semantic model under UBL and delegates final technical specifications and volumetry to AEAT's electronic office.
3. The currently incorporated European syntax reference is UBL 2.1, not UBL 2.5.
4. UBL 2.5 is a real OASIS Committee Specification and is designed to remain compatible with earlier UBL 2.x documents; it is not yet evidence of the Spanish accepted submission version.
5. The draft prohibits other integrated or embedded files in public invoices and faithful copies.
6. The draft permits an electronic signature to accompany interconnection, subject to final signature mechanics.
7. Sage's likely system-to-system interconnection path is a web service, not the individual public web form.
8. The draft expects syntax/semantic/profile validation and an itemised admitted/rejected response.
9. The draft expects receipt evidence including a secure verification code.
10. The draft unique code uses issuer NIF, invoice number/series and issue date and applies duplicate/original-copy controls.

### Key contradiction: UBL 2.5 page title versus official syntax baseline

| Claim | Evidence | Product treatment |
|---|---|---|
| Phase 1 submission is “UBL 2.5” | Existing internal page title only | Unconfirmed |
| Spanish rule references EN 16931 UBL invoice/credit note through EU Decision 2017/1870 | BOE + EUR-Lex | Current official baseline points to UBL 2.1 |
| UBL 2.5 exists and later minor versions accept earlier conforming documents | OASIS UBL 2.5 | Useful future compatibility, not acceptance evidence |

**Decision required:** obtain the final AEAT schema/profile package and record its exact accepted UBL version(s). Until then, do not expose or hard-code `2.5` as a customer contract.

### Evidence gaps

- final ministerial order and effective date;
- AEAT service documentation, endpoint/WSDL/OpenAPI and environment details;
- exact UBL version(s), namespaces and allowed `UBLVersionID`;
- Spanish `CustomizationID`, `ProfileID`, extensions and code lists;
- published XSD/Schematron/other rule artefacts and versioning policy;
- authentication, representation and signature packaging;
- individual versus batch request contract and maximum items;
- synchronous/async behaviour, correlation and idempotency support;
- complete response/error catalogue and field pointers;
- rate, concurrency, payload and volumetry limits;
- receipt/secure-verification-code structure and retrieval;
- authoritative query/reconciliation operation after a lost response;
- correction, baja, credit-note and identity-reuse rules; and
- final technical-incident recovery timing.

## Current-state and option analysis

### ERP supplies ready-to-send UBL

| Aspect | Assessment |
|---|---|
| Benefit | Preserves ERP-specific invoice construction; less mapping in platform |
| Risk | Every ERP must track AEAT profile versions and errors; inconsistent support |
| Product treatment | May be supported as an advanced contract only if Sage still validates and records the exact profile |

### ERP supplies canonical/business invoice data

| Aspect | Assessment |
|---|---|
| Benefit | Stable ERP contract; central mapping/profile updates and error language |
| Risk | Platform owns a broad and evolving semantic mapping |
| Product treatment | Recommended default where Sage has a canonical invoice model |

### Hybrid contract

| Aspect | Assessment |
|---|---|
| Benefit | Supports mature ERPs and simpler consumers |
| Risk | Two input paths can diverge in validation and lifecycle behaviour |
| Product treatment | Candidate direction: one canonical validation/submission pipeline after input normalisation |

### Recommended direction

1. Define one provider-neutral Sage submission operation and immutable invoice correlation identity.
2. Accept canonical invoice data as the normal path; allow prebuilt UBL only through an explicit, validated capability.
3. Normalise both paths to one internal submission artefact.
4. Bind the artefact to an effective validation pack containing UBL XSD, EN 16931 and Spanish/AEAT rules.
5. Reject attachment/profile/business-rule issues before external transmission.
6. Persist the exact outbound XML fingerprint, pack version, route snapshot and intended public unique code.
7. Submit through the confirmed AEAT web service.
8. Classify each item response independently.
9. Persist public references and receipt evidence before reporting admitted.
10. Reconcile any post-transmission timeout before retry.

This is a proposed product model, not an approved architecture.

## Conceptual model and immutable context

| Concept | Required attributes | Purpose |
|---|---|---|
| Submission request | Sage request ID, idempotency identity, ERP/customer actor, legal entity, environment, invoice identity | Stable client operation |
| Public route snapshot | public connection, effective route/version, decision time | Preserves why Public was selected |
| Validation pack | pack ID/version, UBL version, XSD, EN 16931 rules, Spanish rules, code lists, effective dates | Reproducible validation |
| Submission artefact | exact XML or secure object reference, content hash, size, signature context, created time | Proves what Sage sent |
| Public identity | issuer NIF, invoice number/series, issue date, derived/returned unique code | Duplicate detection and lifecycle correlation |
| Submission attempt | attempt ID, send boundary, correlation, start/end, transport evidence, outcome | Safe retry/reconciliation |
| Item result | admitted/rejected/unknown, public error code/path/message, mapped Sage category | Item-level behaviour |
| Receipt | secure verification code/public receipt, response evidence, received time | Submission evidence |
| Lifecycle link | invoice ID, public identity/reference, current status/history | Later delivery/business/payment events |

Mutable customer configuration must not rewrite the public route, validation pack, exact payload fingerprint or public references of an existing attempt.

## Proposed state model

| State | Meaning | Permitted next behaviour |
|---|---|---|
| `RECEIVED` | Sage accepted the client operation identity | Eligibility and normalisation |
| `VALIDATING` | Route, document and profile validation in progress | Ready or correction-required |
| `CORRECTION_REQUIRED` | Known pre-transmission issue | Customer corrects and submits a new version under approved identity rule |
| `READY_TO_SUBMIT` | Exact artefact and pack are fixed | Send when capacity/service permits |
| `SUBMITTING` | External attempt has started | Await response |
| `RETRY_PENDING` | Failure proven before transmission or safely retriable | Bounded retry |
| `OUTCOME_UNKNOWN` | Public mutation may have occurred | Reconcile only |
| `REJECTED` | Public service rejected the item | Correct/escalate according to reason |
| `ADMITTED` | Public service admitted the item | Persist receipt and monitor lifecycle |
| `WITHDRAWAL_PENDING` | Approved baja requested | Reconcile withdrawal |
| `WITHDRAWN` | Public evidence confirms traceable baja | Historical record remains |

`ADMITTED`, `REJECTED` and `WITHDRAWN` are terminal for that submission attempt, not necessarily for the business invoice lifecycle.

## Validation model

Validation should run in increasing-cost order and return one coherent error contract.

| Layer | Examples | Result owner |
|---|---|---|
| Request/identity | missing legal entity, invoice identity, idempotency identity | ERP/client |
| Eligibility/route | onboarding incomplete, wrong environment, no effective Public outbound route | Customer/configuration |
| XML/security | malformed XML, disallowed constructs, unsafe size/encoding | ERP/client or security |
| UBL XSD | invalid namespace, element/type/cardinality | ERP/mapping |
| EN 16931 | required business term, totals/tax consistency, cross-field rules | ERP/customer |
| Spanish/AEAT profile | NIF, allowed codes, additional fields, original/copy, public extensions | ERP/customer/profile mapping |
| Attachment/signature | embedded file prohibited; signature packaging unsupported/invalid | ERP/customer or security |
| External validation | AEAT-only or changed rule | Provider/public solution |

### Attachment behaviour

The draft rule is specific: invoices cannot incorporate other integrated or embedded files. The product should therefore:

1. Detect binary/object attachment constructs and unsupported embedded content before submission.
2. Return an actionable error identifying the unsupported content and affected invoice.
3. Avoid stripping an attachment silently because doing so changes the submitted document.
4. Preserve the customer's original input according to approved retention/security policy.
5. Treat permitted invoice references as structured invoice data, not as binary attachments.
6. Treat electronic-signature packaging through a separately confirmed validation path.
7. Keep any temporary dual-channel PDF obligation outside the public UBL payload and correlate it only through an approved separate journey.

## Illustrative payload excerpt

The following is a **synthetic discussion aid**, not an AEAT-valid fixture. It deliberately uses the current official UBL 2.1 baseline and omits Spain-specific profile identifiers until AEAT publishes/confirms them.

```xml
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
         xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
         xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.1</cbc:UBLVersionID>
  <!-- CustomizationID/ProfileID must come from the final AEAT profile. -->
  <cbc:ID>SYNTH-2026-0001</cbc:ID>
  <cbc:CopyIndicator>false</cbc:CopyIndicator>
  <cbc:IssueDate>2026-07-29</cbc:IssueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>EUR</cbc:DocumentCurrencyCode>
  <!-- Supplier, customer, tax, monetary totals and invoice lines omitted. -->
  <!-- No embedded PDF/image/spreadsheet is included. -->
</Invoice>
```

Do not turn this excerpt into a test fixture. Production fixtures must be generated from the final AEAT schemas, profile identifiers, rule artefacts and approved synthetic identities.

## Detailed journeys

### Journey 1 — prepare public outbound without sending

1. Public onboarding establishes the legal entity, environment, authorisation and outbound capability.
2. Routing records Public as the effective outbound route.
3. Platform loads an approved validation pack for that environment/effective time.
4. A readiness test validates configuration and approved synthetic content without creating a real invoice.
5. Operations can see ready/not-ready evidence separately from customer invoice submission.

### Journey 2 — submit a valid invoice

1. ERP sends canonical invoice data or an explicitly supported prebuilt UBL document with an idempotency identity.
2. Sage authenticates the caller and resolves legal entity/environment.
3. Sage resolves and persists the effective outbound Public route.
4. Input is normalised and mapped to the approved public profile.
5. Sage validates request, XML, XSD, EN 16931, Spanish/AEAT rules and attachment/signature constraints.
6. Sage persists the exact artefact fingerprint, validation-pack version and intended public identity.
7. Submission attempt calls the public web service with correlation evidence.
8. Sage classifies the item response as admitted or rejected.
9. For admission, Sage persists public reference and receipt/verification evidence.
10. ERP sees admitted as a technical/public outcome, distinct from delivery and business lifecycle.

### Journey 3 — correct an invalid invoice before transmission

1. Validation identifies one or more correctable errors.
2. Sage does not call the public service.
3. ERP receives stable error category, field/business-term pointer where possible, message and validation-pack version.
4. Customer corrects the invoice.
5. Resubmission uses the approved operation/version semantics.
6. Audit preserves the rejected local version without presenting it as externally submitted.

### Journey 4 — reject embedded attachment

1. Invoice contains an encoded PDF, image, spreadsheet or other integrated file.
2. Sage identifies the attachment construct before external submission.
3. Operation becomes `CORRECTION_REQUIRED`.
4. ERP receives an attachment-prohibited error and guidance; Sage does not silently remove it.
5. Customer submits a corrected structured invoice without the embedded file.
6. If a separate transitional PDF channel is required, it follows its own approved correlated journey.

### Journey 5 — public service rejects the invoice

1. Sage validation passed under the local pack.
2. Public response rejects the item with error reason.
3. Sage persists raw sanitised response evidence and maps it to a stable category.
4. Result is `REJECTED`, not retried automatically as a transport error.
5. Correctable errors return to ERP; rule drift/unknown errors create operations and profile-maintenance signals.
6. Reuse of invoice identity after correction follows the confirmed AEAT rule.

### Journey 6 — mixed response for a batch

1. Confirmed service contract allows multiple invoices in one request.
2. AEAT returns a list containing admitted and rejected items.
3. Sage correlates every response item deterministically to one submission operation.
4. Each item receives its own terminal/intermediate result and evidence.
5. Uncorrelated or missing response items become outcome-unknown; batch transport success is not applied to all.

If the final service is individual-only, this journey becomes an adapter-level non-goal rather than product behaviour.

### Journey 7 — duplicate ERP request

1. ERP repeats the same request/idempotency identity because its response was lost.
2. Sage locates the existing operation.
3. If payload identity matches, Sage returns current/existing result.
4. If payload conflicts, Sage rejects the reuse and requires an approved new version/correction identity.
5. No additional public request is sent solely because the client repeated its call.

### Journey 8 — timeout after possible transmission

1. Sage starts a public submission and the connection times out after bytes may have been transmitted.
2. Attempt becomes `OUTCOME_UNKNOWN`.
3. Sage does not blindly resend.
4. Reconciliation searches/consults using public unique identity, correlation or receipt retrieval supported by the final API.
5. If an original exists, Sage records admission/receipt evidence.
6. If the public service proves no mutation occurred, a safe retry may start.
7. If the outcome cannot be resolved, operations receives an explicit case; the customer is not told to create a different invoice silently.

### Journey 9 — public service unavailable before transmission

1. Connection/service health prevents transmission before the mutating boundary.
2. Attempt becomes `RETRY_PENDING`.
3. Sage queues bounded retry/backoff and preserves original route/profile context.
4. Customer sees delayed/pending with last failure classification.
5. Recovery drains backlog fairly and within final regulatory/service timing.
6. An invoice that becomes invalid due to a profile change is not silently remapped after the original pack was fixed; approved migration/revalidation behaviour applies.

### Journey 10 — internal failure after external admission

1. Public service admits the invoice, but Sage fails before persisting the final result/receipt.
2. Operation remains or becomes `OUTCOME_UNKNOWN`.
3. Recovery reconciles public state using immutable attempt/public identity.
4. Sage persists the existing result rather than resubmitting.
5. Downstream status notification is idempotent.

### Journey 11 — route changes while invoice is in progress

1. Invoice route snapshot was fixed as Public before submission.
2. Customer activates a Private outbound route for new invoices.
3. Existing `READY_TO_SUBMIT`, `SUBMITTING`, `OUTCOME_UNKNOWN` and admitted Public invoices retain Public context.
4. New invoices after the effective cutover resolve Private.
5. Any cancellation/migration of queued Public work requires an explicit transition rule; it is not silently rerouted.

### Journey 12 — withdraw or correct an improper admitted invoice

1. Customer identifies an invoice that should not correspond to the documented operation or needs correction.
2. Sage determines whether approved baja, corrective invoice/credit note or other lifecycle action applies.
3. Any mutating action has its own idempotency, unknown-outcome and reconciliation path.
4. Public traceability and original payload remain retained.
5. Sage never deletes the admitted invoice record simply because a baja/correction succeeds.

## Functional requirements

### Identity, eligibility and routing

| ID | Requirement |
|---|---|
| FR1 | Every submission must identify Sage legal entity, environment, invoice identity and idempotency identity. |
| FR2 | Caller must be authorised to submit for the legal entity. |
| FR3 | Public onboarding and outbound capability must be ready before submission. |
| FR4 | Sage must resolve and persist one effective outbound route before external transmission. |
| FR5 | Test and production identities, routes, credentials, artefacts and receipts must remain isolated. |
| FR6 | A later route/configuration change must not rewrite an existing invoice's submission context. |

### Input, mapping and profile

| ID | Requirement |
|---|---|
| FR7 | The Sage contract must declare supported input modes: canonical data and/or validated prebuilt UBL. |
| FR8 | Both supported input modes must converge on the same eligibility, validation, submission and lifecycle behaviour. |
| FR9 | Each outbound artefact must bind to one immutable validation-pack ID/version. |
| FR10 | The pack must identify accepted UBL version, schemas, EN 16931 rules, Spanish/AEAT rules, extensions and code lists. |
| FR11 | New validation packs must have controlled effective dates, rollback and environment-specific approval. |
| FR12 | Historic invoice validation must remain explainable using the pack originally applied. |
| FR13 | Production must not label or emit UBL 2.5 unless it is explicitly accepted by the final AEAT specification and pack. |

### Validation and attachments

| ID | Requirement |
|---|---|
| FR14 | Sage must validate request identity, route, XML/security, UBL XSD, EN 16931, Spanish/AEAT profile and attachment/signature rules before transmission. |
| FR15 | Validation errors must use stable category, code, message, pack version and field/business-term pointer where available. |
| FR16 | Known-invalid invoices must not be transmitted. |
| FR17 | Embedded or integrated files must be rejected before public submission. |
| FR18 | Sage must not silently strip or alter an embedded attachment to make an invoice pass. |
| FR19 | Signature content/packaging must be distinguished from attachments and accepted only under the confirmed public contract. |
| FR20 | Validation must protect against unsafe XML, excessive size/complexity and unsupported encoding according to security limits. |

### Submission orchestration and idempotency

| ID | Requirement |
|---|---|
| FR21 | Submission must be asynchronous from the ERP perspective when external completion cannot be guaranteed within a bounded client call. |
| FR22 | Repeating the same idempotency identity with the same logical payload must return the existing operation/result. |
| FR23 | Reusing an idempotency identity with conflicting payload/context must be rejected. |
| FR24 | The exact outbound artefact or approved secure reference, content fingerprint, route snapshot and pack version must be durable before the mutating boundary. |
| FR25 | Each external attempt must record whether failure occurred before transmission, after possible transmission or after a confirmed response. |
| FR26 | Safe pre-transmission transient failures may retry with configured backoff. |
| FR27 | A post-transmission timeout must enter outcome-unknown and reconcile before retry. |
| FR28 | Concurrent mutations for the same invoice identity must be prevented or serialised under approved correction rules. |

### Response, receipt and lifecycle

| ID | Requirement |
|---|---|
| FR29 | Sage must classify each invoice item independently as admitted, rejected, partial/missing or outcome-unknown. |
| FR30 | A request-level success must not be applied to items without a correlated item outcome. |
| FR31 | Public error code/reason and sanitised evidence must be retained and mapped without losing the external value. |
| FR32 | Admission must persist public identity/reference and receipt/secure-verification evidence before customer notification. |
| FR33 | Admission must remain distinct from delivery, commercial acceptance/rejection, correction and payment. |
| FR34 | Downstream operation/lifecycle notifications must be idempotent and ordered or version-aware. |
| FR35 | Public invoice unique-code components and original/copy classification must be retained. |

### Recovery, correction and operations

| ID | Requirement |
|---|---|
| FR36 | Sage must provide a reconciliation path for outcome-unknown attempts using confirmed public query/reference capabilities. |
| FR37 | Internal failure after public admission must recover the existing outcome without creating a second invoice. |
| FR38 | External technical outage must preserve a backlog with age, reason, route/profile context and safe recovery policy. |
| FR39 | Operations must be able to inspect request, validation, artefact fingerprint, attempt boundary, response, receipt, lifecycle and audit relationships. |
| FR40 | Operations may retry only operations classified safe; cursor/reference/idempotency evidence must not be manually overwritten. |
| FR41 | Unknown or newly observed AEAT validation errors must create profile-maintenance/operational signals. |
| FR42 | Baja/correction requests must be separate idempotent operations and preserve original traceability. |
| FR43 | Submission and historical access must continue under the original Public context after a later route change. |
| FR44 | Every material state change must record actor/trigger, timestamp, reason, correlation and previous/new state. |

## Proposed Sage API and experience

| Capability | Product behaviour |
|---|---|
| Validate invoice | Returns the applicable pack and all safe actionable pre-transmission errors |
| Submit invoice | Accepts stable identity/idempotency context and returns an operation |
| Get submission | Returns state, admission/rejection category, freshness and safe corrective action |
| Get receipt | Returns authorised receipt evidence after admission |
| Request retry | Allowed only when current operation is classified safe |
| Request correction/baja | Separate lifecycle operation after product/legal rules are approved |
| Operations reconcile | Searches public evidence for outcome-unknown attempt |

Exact endpoint paths and request/response shapes require API design. Client responses should be provider-neutral while preserving the public error code and evidence for support.

## Failure and operation-safety matrix

| Failure/condition | Classification | Automatic action | Customer/operations outcome |
|---|---|---|---|
| Missing/invalid business field | Correctable before send | None | Field/business-term error |
| Embedded attachment | Correctable before send | None | Attachment-prohibited guidance |
| Invalid/expired credential before send | Action required | No repeated mutation | Re-authorise/renew |
| No effective Public route | Configuration conflict | None | Resolve route |
| AEAT validation rejection | External rejection | No blind retry | Correct/escalate with reason |
| Throttled before mutation | Transient safe | Backoff | Pending/delayed |
| Network failure proven before send | Transient safe | Backoff | Pending/delayed |
| Timeout after possible send | Outcome unknown | Reconcile | Pending investigation |
| Mixed response missing item | Outcome unknown for item | Reconcile item | Other items keep own results |
| Duplicate original exists | Duplicate/conflict | Reconcile existing identity | Return existing/conflict behaviour |
| Internal persistence failure after admission | Outcome unknown | Reconcile | No resubmission |
| Profile changes while queued | Version conflict | Apply approved migration policy | Do not silently alter payload |
| Concurrent correction/submission | Concurrency conflict | Serialise/reject | Refresh current state |
| Baja timeout after possible send | Outcome unknown | Reconcile baja | Preserve original |

## Non-functional requirements

### Security and privacy

- Credentials, private keys, certificates and signing material use approved secret/HSM/key-management controls.
- Invoice payloads and receipts are encrypted in transit and at rest according to policy.
- Raw XML access is least-privilege, audited and redacted from normal logs.
- XML processing must disable unsafe external entities and enforce size/depth/resource limits.
- Legal-entity isolation applies across ERP, accountant, support and operations access.
- Synthetic fixtures must not contain real customer/NIF/personal data.

### Reliability and consistency

- Client, external-attempt and downstream-notification idempotency are required independently.
- The durable submission artefact must exist before external mutation.
- State transitions must be concurrency/version controlled.
- Outbox/equivalent recovery must prevent admission evidence from being lost between persistence and notification.
- Reconciliation must be repeatable and auditable.

### Performance and capacity

- ERP submit call must have a bounded response and not wait indefinitely for AEAT.
- Validation latency, submission latency, maximum payload/batch size and throughput targets require sandbox baselines.
- Capacity must include peak invoice issuance, month/quarter/year-end spikes, retry amplification and outage backlog.
- Rate/concurrency controls must honour final AEAT volumetry and tenant fairness.

### Audit, retention and reproducibility

- Preserve invoice identity, payload fingerprint, route snapshot, pack version, attempts, external responses, receipt and lifecycle history for the approved retention period.
- A pack update must not prevent support from explaining earlier validation/outcomes.
- Withdrawal/correction must add history, not erase the original.

### Accessibility and messaging

- Error messages must explain whether the customer can correct, must re-authorise, should wait, or needs support.
- Customer-facing status must not use “sent successfully” where only local validation or transport success is known.
- Errors should be localisable without changing stable machine codes.

### Observability

Measure by environment, pack version, ERP/product, result class and sanitised external error. Protect invoice/NIF/customer information in telemetry.

Required signals include:

- received/validating/ready/submitting/backlog counts and age;
- validation failure rate by layer/business term;
- attachment-prohibition failure rate;
- admission, rejection and outcome-unknown rate;
- AEAT latency, throttling and availability;
- reconciliation age/outcome;
- duplicate/conflict rate;
- receipt-persistence and downstream-notification delay; and
- pack-version/error-regression indicators.

## Acceptance criteria

| ID | Given | When | Then |
|---|---|---|---|
| AC1 | Ready Public outbound legal entity and valid invoice | ERP submits once | One operation binds route, pack and artefact before external send |
| AC2 | Invoice fails EN 16931/Spanish rule | Validation runs | Actionable error is returned and AEAT is not called |
| AC3 | Invoice contains embedded PDF | Validation runs | Attachment-prohibited error is returned and document is not silently changed |
| AC4 | Signature uses approved packaging | Validation runs | It is evaluated by signature rules rather than rejected merely as an attachment |
| AC5 | ERP repeats same idempotency identity/payload | Existing operation exists | Same operation/result is returned with no new public submission |
| AC6 | ERP reuses idempotency identity with different payload | Request arrives | Conflict is rejected |
| AC7 | Public service admits invoice | Response arrives | Public identity and receipt evidence are persisted before admission is exposed |
| AC8 | Public service rejects invoice | Response arrives | External reason and stable mapped category are retained; no automatic transport retry occurs |
| AC9 | Batch response admits one and rejects one | Response arrives | Each invoice receives its own correct outcome |
| AC10 | Response omits an item | Batch processing completes | Missing item becomes outcome-unknown, not admitted |
| AC11 | Timeout occurs after possible send | Attempt is evaluated | Operation reconciles before retry |
| AC12 | Sage fails after AEAT admission | Recovery runs | Existing public result is recovered without duplicate invoice |
| AC13 | Public service is unavailable before send | Safe failure occurs | Backlog/retry preserves artefact, route and pack context |
| AC14 | UBL validation pack is upgraded | Historic submission is viewed | Original pack/version and payload fingerprint remain visible |
| AC15 | Outbound route switches to Private | Earlier Public submission remains active | Earlier invoice retains Public context; new invoice resolves the effective new route |
| AC16 | Improper admitted invoice requires action | Approved baja/correction is requested | Separate auditable operation runs and original history remains |
| AC17 | Production configuration has no confirmed AEAT UBL version/profile | Activation is attempted | Production entry is blocked rather than defaulting to UBL 2.5 |

## Metrics and success measures

| Metric | Target/direction | Status/owner |
|---|---|---|
| Submitted items with complete route/pack/payload/attempt audit | 100% | Proposed target |
| Admitted items with retained public identity and receipt | 100% | Proposed target |
| Duplicate public invoices caused by Sage retry | 0 | Proposed target |
| Known attachment/profile errors caught before AEAT | 100% | Proposed target after rule coverage |
| Outcome-unknown operations resolved within target | Target required | SRE/product |
| Avoidable invoice loss | 0 | Proposed target |
| Validation-to-admission conversion | Baseline by ERP/error category | Product/data |
| Public rejection caused by local pack drift | 0 direction | Engineering/compliance |
| Submission latency and backlog age | Targets required after sandbox | SRE/product |
| Customer/support cases described ambiguously as “sent” | 0 direction | Product/operations |

## Capacity model

Required inputs:

- active outbound legal entities;
- average/peak invoices per minute and peak-period distribution;
- average and maximum payload size;
- supported batch size and partial-response behaviour;
- AEAT rate/concurrency/volumetry limits;
- validation CPU/memory cost;
- signing latency/capacity;
- external response latency;
- maximum supported outage and recovery window; and
- reconciliation query capacity.

```text
peak submission demand
  = peak invoices per minute × average external requests per invoice

outage backlog
  = peak/average arrivals during outage + safe retries + unresolved outcomes

required recovery throughput
  = backlog ÷ approved catch-up duration + continuing live traffic
```

Production approval requires a model showing that live traffic, outcome reconciliation and backlog recovery can coexist without breaching AEAT limits or starving tenants.

## Risks and mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| UBL 2.5 is assumed from page title | External rejection and customer contract mismatch | Version-neutral title; final AEAT pack gate |
| XSD validation is treated as complete | Semantic/Spanish-rule rejection | Layered EN 16931 and AEAT validation |
| Attachment is stripped automatically | Submitted invoice differs from approved ERP document | Reject and require explicit correction |
| Signature is rejected as attachment | Valid interconnection path blocked | Separate confirmed signature handling |
| Admission is called delivery/acceptance | Misleading lifecycle and support | Explicit stage model |
| Timeout triggers immediate resend | Duplicate/original conflict | Outcome-unknown reconciliation |
| Batch result applied globally | Some rejected/missing items shown successful | Per-item correlation/state |
| AEAT pack changes without control | Historic results unreproducible; new rejects | Immutable pack version, effective date and rollback |
| Public outage backlog overwhelms recovery | Timing breaches and starvation | Capacity model, backoff and fair drain |
| Unique-code collision/correction rule unclear | Customer cannot correct or duplicates invoice | Confirmation gate and explicit correction identity |
| Route changes queued invoice silently | Wrong network or duplicate | Immutable route snapshot and transition rule |
| Raw invoice/error data leaks into logs | Privacy/security incident | Redaction, least privilege and audited payload access |

## Dependencies, rollout and production gates

### Discovery

1. Obtain final order and AEAT technical publication.
2. Record exact accepted UBL version/profile and validation artefacts.
3. Obtain service contract, sandbox, credentials and synthetic data process.
4. Confirm attachment, signature, batch, receipt, duplicate, correction and outage rules.
5. Agree canonical/prebuilt UBL input strategy with ERP product teams.
6. Agree status terminology and customer correction experience.

### Build and validation

1. Implement versioned validation pack and fixture suite.
2. Implement canonical mapping/prebuilt UBL normalisation.
3. Implement local error contract including embedded attachment.
4. Implement durable artefact, route snapshot, idempotency and attempt boundary.
5. Implement web-service adapter, per-item response and receipt persistence.
6. Implement outcome-unknown reconciliation and operations.
7. Test profile upgrade/rollback, duplicates, partial response, timeout and internal-failure recovery.
8. Load-test peak, signing, batch, outage and catch-up scenarios.

### Rollout

1. Synthetic schema/profile conformance suite.
2. AEAT sandbox/certification evidence.
3. Internal legal entities.
4. Limited pilot across representative ERP input modes and invoice complexity.
5. Measure validation, admission, rejection and reconciliation outcomes.
6. Expand behind pack/version and operational feature controls.

### Production entry gates

- final accepted UBL version and Spain/AEAT profile confirmed;
- final schemas, rules, code lists and change/versioning process stored or referenced with permission;
- service endpoints/contract, sandbox and authentication approved;
- signature packaging and attachment prohibition tested;
- canonical/prebuilt UBL contract approved;
- unique identity, duplicate and correction/baja behaviour confirmed;
- per-item result, receipt and reconciliation proven;
- rate, payload, batch, concurrency and volumetry limits enforced;
- outage/recovery window and capacity model approved;
- security/privacy/retention/architecture review complete;
- customer messages, operations runbook, dashboards and escalation ownership ready; and
- end-to-end synthetic and pilot acceptance criteria pass.

## Consultation and open decisions

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| Which UBL version(s) will AEAT accept? | Determines schema and customer contract | AEAT spec + Spain local team | Production pack | Current incorporated baseline is UBL 2.1; do not assume 2.5 |
| What are final `CustomizationID`, `ProfileID`, extensions and code lists? | Determines Spanish profile validation | AEAT spec | Mapping/build | Supplied by final AEAT artefacts |
| Does Sage accept canonical data, prebuilt UBL or both? | Determines ERP contract and ownership | Product + architecture + ERP teams | API/mapping | Canonical default; controlled UBL path may be useful |
| What exactly counts as prohibited integrated/embedded content? | Determines validation coverage | AEAT spec + architecture | Attachment validation | Binary/object content prohibited; structured references may remain |
| How is permitted electronic signature packaged and validated? | Determines security and payload | AEAT spec + security | Submission build | Separate from embedded attachment |
| Is submission individual, batch or both? | Determines orchestration/partial result | AEAT spec | Adapter/capacity | Product supports per-item outcomes regardless |
| What is the idempotency/correlation contract? | Prevents duplicate mutation | AEAT spec + architecture | Resilience | Sage idempotency plus public identity/reconciliation |
| How can Sage query an outcome after lost response? | Determines safe retry | AEAT spec | Production resilience | Use unique code/reference/receipt consultation |
| Can a rejected invoice reuse the same identity after correction? | Determines ERP correction journey | AEAT spec + local team | Error recovery | Must follow public duplicate/identity rules |
| When is baja valid versus a corrective/credit invoice? | Prevents improper deletion/correction | Spain local team/compliance | Post-admission lifecycle | Separate decisions; preserve original trace |
| Is the draft four-day post-incident window final and how is incident evidenced? | Determines backlog SLA/runbook | Legal/local team + AEAT | Operations readiness | Queue and audit now; final timing after order |
| Is parallel PDF delivery required during transition, and through what channel? | Determines dual delivery without embedding | Spain local team/compliance | Adjacent feature | Never embed it in public UBL under current draft |
| Who owns validation-pack updates and emergency rollback? | Determines operational governance | Product/compliance + engineering | Production operations | Named pack owner and two-person approval |

## Decisions

| Date | Decision | Evidence/status |
|---|---|---|
| 2026-07-29 | Submission is a separate Phase 1 PRD from onboarding, consultation and lifecycle | Scope decision |
| 2026-07-29 | Document title is version-neutral until AEAT confirms accepted UBL version | Evidence-led scope decision |
| 2026-07-29 | Current official baseline points to EN 16931 UBL 2.1, not a confirmed UBL 2.5 mandate | BOE + EU Decision 2017/1870 |
| 2026-07-29 | Embedded/integrated files are rejected before transmission | Draft order; final confirmation gate |
| 2026-07-29 | Signature handling is separate from attachment handling | Draft order distinction |
| 2026-07-29 | Admission, delivery, business acceptance and payment are distinct | Proposed lifecycle principle |
| 2026-07-29 | Outcome-unknown submission reconciles before retry | Proposed safety requirement |
| 2026-07-29 | Validation pack and outbound context remain immutable per attempt | Proposed audit/reproducibility requirement |

## Source notes

- The April 2026 ministerial order is a draft. Its attachment, response, duplicate, receipt and outage provisions are treated as strong discovery evidence, not final legal/API approval.
- The official EU syntax reference incorporated by the Spanish regulation identifies UBL 2.1. OASIS UBL 2.5 compatibility does not authorise Sage to label a Spanish public invoice as 2.5.
- This PRD restates all product-relevant evidence so Confluence readers do not need access to repository research files.
- This is a research/proposal/solution PRD and does not provide tax or legal advice.

## Revision history

| Date | Version/revision | Change | Evidence/decision source | Pull request |
|---|---|---|---|---|
| 2026-07-29 | Version 1 (Draft) | Initial evidence-led Phase 1 submission PRD with UBL-version correction, attachment rule, detailed journeys, requirements, visual, acceptance and production gates | Confluence revision 3, RD 238/2026, EU Decision 2017/1870, April 2026 draft order, OASIS UBL 2.5 | |

