---
id: PRD-SEI-226
title: Security — Trust, Identity, Data and Audit
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-210
  - PRD-SEI-221
  - PRD-SEI-222
  - PRD-SEI-223
  - PRD-SEI-224
  - PRD-SEI-225
  - FP-SEI-001
  - ADR-SEI-001
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: ""
  title: Security — Trust, Identity, Data and Audit
  layout: two_left_sidebar
  toc: true
---

# Security — Trust, Identity, Data and Audit

## Decision summary

Phase 3 must establish an explicit trust chain from an authorised customer and verified legal entity through Sage users/services, operator certificates, signed invoice representations, partner/public/counterparty transport and durable audit evidence.

Identity, authority, connection credentials and invoice signature/seal are separate controls. No credential may be shared across tenants or environments; no partner assertion may replace Sage's evidence responsibilities; and no route, support or migration action may rewrite historical trust evidence.

> **Product principle:** Every privileged action and exchanged representation must answer who acted, for which legal entity, under what authority, using which trust material, on what data, and with what independently verifiable evidence.

## Phase and security outcome

| Phase | Security boundary | Phase 3 consequence |
|---|---|---|
| Phase 1 | Sage-to-public authentication, customer authority and invoice protection | Reuse only where control scope and implementation are proven |
| Phase 2 | Multiple provider credentials, adapters, tenants and route audit | Reuse connection isolation, secret lifecycle and historical context |
| **Phase 3** | Sage or partner operates a public-facing private platform | Add operator certification, external platform trust, AS2/AS4, advanced signature/seal, data governance and operator-wide incident/audit controls |

## Problem and objective

### Problem

The Phase 3 proposition combines customer identity, Sage product tenancy, legal-entity authority, operator/platform identity, transport certificates, invoice signature/seal, public authorisation, partner access and support actions. These are different trust relationships with different owners and lifecycles.

If represented as one generic “credential” or “authenticated connection”:

- a Sage user could act for the wrong legal entity;
- one tenant/environment could use another's certificate or data;
- an operator seal could be confused with issuer authorisation;
- transformation might invalidate signature/integrity evidence;
- expired/revoked certificates could continue processing;
- support staff could access invoice/payment data without necessity;
- partner subcontractors or data locations could change without review;
- audit evidence could become unavailable after route/partner termination;
- data deletion could remove evidence still needed for lifecycle, dispute or compliance.

### Objective

Define security and data requirements for identity, authority, trust material, secure transport, representation integrity, tenant/environment isolation, data governance, privacy, audit, incident response, retention and partner assurance across the complete Phase 3 lifecycle.

## Scope and non-goals

### In scope

- Human, customer/legal-entity, service, operator/platform and counterparty identity.
- Customer authority/consent and privileged operational permissions.
- Certificates, keys, secrets, signature/seal and secure transport lifecycle.
- Data classification, minimisation, residency, retention, deletion, export and purpose.
- Tenant/environment isolation and secure product/operator boundaries.
- Audit, non-repudiation evidence, security monitoring and incident handling.
- Partner/supplier/subprocessor controls and operating-model exit.
- Security readiness and recurring assurance.

### Non-goals

- Choosing a specific identity, PKI, HSM, SIEM or cloud product.
- Claiming ISO/IEC 27001/equivalent scope without certification evidence.
- Providing legal/privacy advice or setting unapproved retention periods.
- Defining detailed AS2/AS4/public endpoint configuration before official/architecture approval.
- Replacing corporate security, privacy, cryptography or supplier-assurance standards.
- Treating payment information as authority to initiate payment.

## Trust concepts and distinctions

| Concept | Meaning | Must not be confused with |
|---|---|---|
| User identity | Authenticated person/service accessing Sage | Legal entity represented |
| Legal-entity identity | Verified business/NIF and tenancy context | User account or provider tenant |
| Authority | Evidence that an actor may perform an action for a legal entity/scope | Authentication alone |
| Service identity | Workload/platform identity used for internal/external calls | Customer consent |
| Operator identity | Legal/technical identity of the private-platform operator | Sage brand or underlying partner UI |
| Transport credential | Key/certificate/secret securing and authenticating a channel | Invoice signature or seal |
| Invoice signature/seal | Evidence protecting origin/integrity of a representation | Transport encryption or platform acknowledgement |
| Trust evidence | Certificate chain, validation, hash, timestamp, authority and action history | Raw secret/key material |
| Data controller/processor role | Approved legal responsibility for processing | System ownership by itself |
| Audit event | Immutable security/business action evidence | Debug log containing uncontrolled content |

## Trust-boundary visual

<!-- confluence-html-macro:start -->
<div class="p3sec-visual" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:24px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1140px;margin:0 auto;overflow-x:auto;">
  <style>
    .p3sec-visual *{box-sizing:border-box}.p3sec-visual h2{margin:0;color:#172b4d;font-size:18px}.p3sec-visual .sub{margin:6px 0 16px;color:#6b778c;font-size:12px}.p3sec-visual svg{display:block;width:1080px;height:520px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.p3sec-visual .customer{fill:#e3fcef;stroke:#36b37e;stroke-width:1.5}.p3sec-visual .sage{fill:#deebff;stroke:#4c9aff;stroke-width:1.5}.p3sec-visual .trust{fill:#fff7d6;stroke:#ffab00;stroke-width:1.5}.p3sec-visual .external{fill:#eae6ff;stroke:#6554c0;stroke-width:1.5}.p3sec-visual .audit{fill:#fff;stroke:#7a869a;stroke-width:1.5;stroke-dasharray:6 4}.p3sec-visual .title{fill:#172b4d;font-size:11px;font-weight:700}.p3sec-visual .copy{fill:#42526e;font-size:9px}.p3sec-visual .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.p3sec-visual .path{fill:none;stroke:#00875a;stroke-width:2}.p3sec-visual .boundary{fill:none;stroke:#6554c0;stroke-width:1.6;stroke-dasharray:6 4}.p3sec-visual .audit-path{fill:none;stroke:#7a869a;stroke-width:1.4;stroke-dasharray:5 4}.p3sec-visual .arrow{fill:#00875a}.p3sec-visual .arrow-p{fill:#6554c0}.p3sec-visual .arrow-g{fill:#7a869a}.p3sec-visual .notes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-width:1080px;margin-top:12px}.p3sec-visual .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.p3sec-visual .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <h2>Separate authority, service trust, transport and invoice evidence</h2>
  <p class="sub">Every boundary validates a different claim. The audit chain records the result and provenance—not reusable secrets or unrestricted invoice content.</p>
  <svg viewBox="0 0 1080 520" role="img" aria-label="An authorised customer user acts for a verified legal entity. Sage validates identity, authority and tenant scope before shared services create an exchange plan. The operator trust service applies approved transport credentials and invoice signature or seal before exchanging with the public solution, private platforms or a partner. Each boundary records redacted immutable audit evidence, while keys and secrets remain in controlled custody. Revocation or incident can suspend the affected scope without deleting historical evidence.">
    <text x="34" y="34" class="label">CUSTOMER AUTHORITY</text><text x="315" y="34" class="label">SAGE CONTROLLED TRUST</text><text x="815" y="34" class="label">EXTERNAL TRUST</text>
    <rect x="34" y="74" width="210" height="82" rx="9" class="customer"/><text x="52" y="101" class="title">Authenticated actor</text><text x="52" y="122" class="copy">User/service identity • role • session</text><text x="52" y="139" class="copy">least privilege and step-up as required</text>
    <rect x="34" y="202" width="210" height="92" rx="9" class="customer"/><text x="52" y="229" class="title">Verified legal entity and authority</text><text x="52" y="250" class="copy">NIF • tenancy • action • direction/scope</text><text x="52" y="268" class="copy">consent/representation evidence and expiry</text>
    <path d="M139 156 V194" class="path"/><polygon points="139,194 133,184 145,184" class="arrow"/>
    <path d="M244 248 H300" class="path"/><polygon points="300,248 290,242 290,254" class="arrow"/>
    <rect x="302" y="184" width="210" height="128" rx="9" class="sage"/><text x="320" y="211" class="title">Sage policy and tenancy boundary</text><text x="320" y="232" class="copy">Authorise operation • isolate tenant/environment</text><text x="320" y="250" class="copy">classify/minimise data • select operator</text><text x="320" y="268" class="copy">persist intent before external mutation</text><text x="320" y="290" class="copy">deny by default when context is incomplete</text>
    <path d="M512 248 H550" class="path"/><polygon points="550,248 540,242 540,254" class="arrow"/>
    <rect x="552" y="158" width="224" height="180" rx="9" class="trust"/><text x="570" y="185" class="title">Operator trust and key boundary</text><text x="570" y="207" class="copy">Service/platform identity</text><text x="570" y="225" class="copy">AS2/AS4 or approved public transport</text><text x="570" y="243" class="copy">certificate/key custody and rotation</text><text x="570" y="261" class="copy">transform, validate, sign/seal</text><text x="570" y="279" class="copy">verify inbound origin/integrity</text><text x="570" y="301" class="copy">secrets never enter product/audit payloads</text><text x="570" y="319" class="copy">revoke/suspend affected scope safely</text>
    <path d="M776 218 H812 V112" class="boundary"/><polygon points="812,112 806,122 818,122" class="arrow-p"/>
    <path d="M776 278 H812 V382" class="boundary"/><polygon points="812,382 806,372 818,372" class="arrow-p"/>
    <rect x="814" y="72" width="232" height="80" rx="9" class="external"/><text x="832" y="99" class="title">Public solution / authority</text><text x="832" y="120" class="copy">Approved authentication, UBL and evidence</text><text x="832" y="137" class="copy">independent external state</text>
    <rect x="814" y="342" width="232" height="80" rx="9" class="external"/><text x="832" y="369" class="title">Private platform / partner</text><text x="832" y="390" class="copy">Platform identity • secure channel • trust chain</text><text x="832" y="407" class="copy">contracted evidence and incident duty</text>
    <rect x="302" y="404" width="474" height="74" rx="9" class="audit"/><text x="320" y="431" class="title">Immutable, redacted security and business audit</text><text x="320" y="452" class="copy">Actor • legal entity • authority • policy • certificate/hash • action • result • source/time • retention class</text><text x="320" y="469" class="copy">No private keys, reusable secrets or uncontrolled invoice/payment content</text>
    <path d="M407 312 V396" class="audit-path"/><polygon points="407,396 401,386 413,386" class="arrow-g"/><path d="M664 338 V396" class="audit-path"/><polygon points="664,396 658,386 670,386" class="arrow-g"/>
  </svg>
  <div class="notes"><div class="note"><strong>Authentication is not authority</strong>The actor, legal entity, action and scope must all be proven.</div><div class="note"><strong>Transport is not invoice trust</strong>Channel security and representation signature/seal have separate evidence.</div><div class="note"><strong>Evidence survives change</strong>Route, credential or partner termination does not rewrite historical trust facts.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors and security responsibilities

| Actor | Security responsibility |
|---|---|
| Customer legal representative/admin | Authorise entity, users, routes and permitted platform actions |
| Sage user/service identity owner | Maintain authentication, role and lifecycle controls |
| Sage product/platform teams | Enforce tenancy, permissions, secure contracts and audit |
| Legal private-platform operator | Maintain certified ISMS scope, platform trust, secure protocol, signature/seal and data governance |
| Trust/certificate owner | Approve issuance, custody, use, rotation, revocation and evidence |
| Partner/subprocessor | Meet contracted controls, boundaries, incident/evidence and deletion/exit duties |
| Security/privacy/legal | Approve threat/privacy analysis, data roles, controls, exceptions and incidents |
| Operations/support | Use restricted diagnostic evidence and authorised recovery actions |
| Counterparty/public solution | Present/validate external identity and provide evidence through approved contracts |

## Security scenarios

| ID | Scenario | Expected control outcome | Failure/continuity rule |
|---|---|---|---|
| S1 | Customer admin authorises Sage for a legal entity/scope | Authority evidence is verified, scoped, effective-dated and auditable | No route/action if authority incomplete or expired |
| S2 | Sage sends through operator AS2/AS4 boundary | Correct service identity, transport certificate and environment policy are used | Invalid/expired/revoked trust stops affected mutation |
| S3 | Invoice requires transformation and signature | Approved representation is transformed/validated before signing/sealing | Original and transform/trust provenance remain immutable |
| S4 | Inbound platform submits signed invoice | Platform/channel, certificate chain, signature/integrity, recipient and replay are validated | Invalid/untrusted content is quarantined, not delivered |
| S5 | Support investigates failure | Least-privileged redacted evidence is available | Raw secrets/full content require separately approved access |
| S6 | Certificate approaches expiry | Rotation completes and both old/new trust windows are controlled/tested | Alert/suspend before unsafe expiry |
| S7 | Partner changes subprocessor/data location/control | Change is assessed and approved before affected processing | Restrict/suspend if approval/evidence absent |
| S8 | Customer switches route/operator | New trust activates after readiness; old credential retained only for approved historical operations | Historical signature/audit remains unchanged |
| S9 | Security incident affects one operator/environment | Contain/revoke/suspend affected scope, preserve evidence and coordinate notice | Unaffected routes remain separated where safe |

## Security and data rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Actor is authenticated | Still require legal-entity authority, action and scope before privileged operation | Proposed access-control rule |
| BR2 | Credential/key is used | Bind use to owner, purpose, environment, tenant/operator scope and lifecycle | Proposed control |
| BR3 | Private-platform exchange occurs | Use approved secure transport meeting applicable AS2/AS4 requirements | RD 238/2026 Article 13; exact profile open |
| BR4 | Private-platform invoice is emitted | Apply approved advanced signature/delegated-signature or seal model after required transformation | RD 238/2026 Articles 7 and 13; legal design open |
| BR5 | Data crosses Sage/partner/public boundary | Apply approved purpose, role, minimisation, encryption, residency and retention | Regulatory/security/privacy control |
| BR6 | Support/audit evidence is generated | Exclude secrets/private keys and minimise invoice/payment/personal content | Confirmed repository/security principle |
| BR7 | Trust/authority is revoked or expires | Stop affected new use and enter controlled recovery without deleting historical evidence | Proposed lifecycle control |
| BR8 | Route/operator changes | Preserve original signature, certificate validation, actor, representation hash and network evidence | Confirmed continuity principle |
| BR9 | Partner operates a control | Sage requires scoped evidence, incident access, audit rights, subprocessor/change control and exit obligations | ADR/PRD-SEI-221 principle |
| BR10 | Retention/deletion conflict exists | Legal hold/approved obligation wins; record decision and delete only at authorised gate | Open legal/privacy policy |

## Research and evidence register

| Source | Finding | Confidence/limitation | Security impact |
|---|---|---|---|
| RD 238/2026 Article 7 | Transformation must preserve authenticity/integrity; private-platform invoices require advanced signature under the defined model | Primary regulation; implementation/trust profile approval required | Transform/sign order, evidence and validation |
| RD 238/2026 Article 13 | Operator requires ISO/IEC 27001 or equivalent, AS2/AS4, advanced signature/seal capability, data governance/confidentiality and breach prevention | Primary regulation; certification scope/equivalence and technical profiles require evidence | Certification, protocol, PKI, data and incident controls |
| RD 238/2026 Article 13.2 | UNE data-governance maturity is one described way to meet the stated governance requirement | Primary regulation; applicability/route requires compliance approval | Data-control assessment option |
| RD 238/2026 Article 11 | Public authentication/representation and integrity procedures depend on official specifications | Primary regulation with ministerial-order dependency | Public trust adapter and readiness gate |
| PRD-SEI-202/203 | Connection-aware credential lifecycle, tenancy, audit and resilience | Product intent; implementation fitness unassessed | Reuse assessment input |
| ADR-SEI-001/PRD-SEI-221 | Named operator, accountability, supplier evidence and ongoing readiness | Proposed governance | Control ownership and partner boundary |

## Proposed trust model

### Identity and authority dimensions

| Dimension | Required evidence/lifecycle |
|---|---|
| Human user | Authentication strength, Sage account, role, session/risk, joiner/mover/leaver |
| Customer legal entity | Verified NIF/identity, tenant mapping, evidence source, review/expiry |
| Customer authority | Authoriser, represented entity, action/direction/scope, effective interval, revocation |
| Sage service | Workload identity, environment, service owner, least privilege and rotation |
| Operator/platform | Legal operator, technical platform identity, qualification/control scope and environment |
| Counterparty/public | Trusted endpoint/platform identity, certificate/contract version and observed validation |

### Trust-material record

| Area | Required information |
|---|---|
| Identity | Credential/certificate reference, owner, issuer, subject, environment and purpose |
| Scope | Tenant/operator/service/direction/profile permitted; never raw key material |
| Lifecycle | Requested, issued, activated, rotated, expiring, revoked and destroyed timestamps |
| Custody | Approved store/HSM boundary, access policy, dual control and backup/recovery rules |
| Evidence | Fingerprint/chain/algorithm/profile, validation result, timestamp and audit reference |
| Dependency | Connections, routes, sign/seal operations and historical obligations using it |

### Data classification and context

At minimum distinguish: customer/legal-entity identity, user/authority evidence, invoice content, payment/status data, credentials/private keys, certificate/public trust evidence, operational telemetry, audit/security events and support exports. Each class needs purpose, access, residency, retention, deletion and disclosure rules.

## Detailed journeys

### J1 — Establish customer authority without activating route

1. Sage authenticates the actor and resolves the intended legal entity.
2. Product captures the action, direction/scope, operator and authority basis.
3. Independent verification/approval occurs under the selected policy.
4. Authority record becomes effective without changing connection/route state.
5. Every subsequent privileged operation rechecks current authority and scope.

### J2 — Provision and rotate operator trust material

1. Named owner requests trust material for a specific operator/environment/purpose.
2. Security approval, issuance and controlled custody occur without exposing raw key material to products/support.
3. Connection validation proves trust with non-production/test counterpart where required.
4. Rotation creates an overlap/transition under approved protocol and rollback controls.
5. Old material is revoked/destroyed only after no active/historical dependency requires it.

### J3 — Sign/seal an outbound representation

1. Exchange plan fixes input/output syntax, transformation and approved signing actor.
2. Transformation and semantic validation complete before signing where required.
3. Trust service verifies legal-entity/operator authority and key purpose.
4. Signature/seal is applied; representation hash, certificate evidence and timestamp are persisted.
5. Transport uses separate channel credentials; products receive references, not keys.

### J4 — Validate inbound platform and invoice trust

1. External platform establishes approved secure channel and platform identity.
2. Sage validates certificate/identity, environment, replay controls and allowed capability.
3. Invoice signature/seal, representation integrity, recipient and schema/profile are validated.
4. Valid content is durably persisted/delivered with original trust evidence.
5. Invalid/untrusted content is quarantined with redacted evidence and no trusted acknowledgement.

### J5 — Investigate and contain a security incident

1. Security/operational signal identifies affected credential, tenant, operator, route, representation or data set.
2. Incident command contains/revokes/suspends the narrowest safe scope and preserves forensic evidence.
3. Required Sage, partner, customer, legal/privacy and authority processes are invoked.
4. In-flight/external state is reconciled; restored credentials/controls are independently validated.
5. Readiness re-approval precedes resumption; historical evidence remains immutable.

### J6 — Route/partner exit and data disposition

1. Exit inventory identifies customer data, trust material, audit, historical invoices and open obligations across parties.
2. Destination trust/readiness and required data/evidence export are verified.
3. New use of old credentials stops; historical use is explicitly restricted and monitored.
4. Partner certifies return/deletion when authorised, while Sage retains approved evidence.
5. Final revocation/deletion follows separate legal, continuity, security and audit gates.

## Functional requirements

### Identity, authority and access

| ID | Requirement |
|---|---|
| FR1 | Authenticate every human/service actor using approved controls appropriate to action risk. |
| FR2 | Resolve verified legal entity and tenant independently of user identity. |
| FR3 | Authorise privileged actions by legal entity, direction/scope, operation, effective interval and environment. |
| FR4 | Enforce least privilege, separation of duties and step-up/dual approval where approved policy requires. |
| FR5 | Revoke/expire authority and access promptly without deleting historical audit. |
| FR6 | Prevent cross-tenant, cross-environment and cross-operator credential/data use. |

### Credentials, transport and representation trust

| ID | Requirement |
|---|---|
| FR7 | Maintain an owned lifecycle for every secret/key/certificate from request through destruction. |
| FR8 | Store private keys/secrets only in approved custody and expose references/operations rather than raw material. |
| FR9 | Bind every credential to permitted purpose, environment, service/operator and scope. |
| FR10 | Monitor expiry/revocation and complete tested rotation before unsafe loss of service. |
| FR11 | Authenticate private-platform transport through approved AS2/AS4 profile and the public route through its approved contract. |
| FR12 | Apply/validate advanced signature or seal according to approved legal actor, transformation order and profile. |
| FR13 | Persist representation hash, signature/seal/certificate validation, timestamp and provenance sufficient for historical verification. |
| FR14 | Detect/prevent replay and reject/quarantine invalid, expired, revoked, mis-scoped or untrusted traffic. |

### Data, privacy and audit

| ID | Requirement |
|---|---|
| FR15 | Classify data and enforce approved purpose, minimisation, access, residency, retention, deletion and disclosure by class. |
| FR16 | Encrypt sensitive data in transit and at rest and manage encryption keys separately from protected content. |
| FR17 | Maintain immutable audit of actor, legal entity, authority, policy/rule, action, representation/trust reference, result and time. |
| FR18 | Keep raw secrets/private keys out of application logs, repositories, PRDs, tests and support exports. |
| FR19 | Provide redacted evidence views appropriate to product, support, operations, audit and regulatory roles. |
| FR20 | Preserve legal hold, historical lifecycle and dispute evidence while enforcing deletion when no approved purpose remains. |

### Partner, incident and exit

| ID | Requirement |
|---|---|
| FR21 | Record controller/processor/subprocessor roles and approved data/trust boundaries for every operating-model party. |
| FR22 | Require partner evidence for certification scope, access, vulnerability/incident, subprocessors, residency, retention and deletion. |
| FR23 | Assess/approve material partner control, subprocessor, data-location or ownership changes before affected processing. |
| FR24 | Support credential/route/tenant-scoped containment, revocation and suspension during security incidents. |
| FR25 | Preserve forensic and business evidence and reconcile external state before service resumption. |
| FR26 | Test data/evidence portability, credential revocation and partner deletion/transition assistance before production. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR1 | The named operator must provide evidence that its applicable ISMS scope holds ISO/IEC 27001 or approved equivalent before production. |
| NFR2 | Cryptographic algorithms, certificates, keys and profiles must follow approved Sage/regulatory standards and crypto-agility controls. |
| NFR3 | Security/audit evidence must be tamper-evident, time-correlated and available for the approved retention period. |
| NFR4 | Privileged access and key use must be monitored, attributable and reviewed at an approved frequency. |
| NFR5 | Security controls must remain effective under peak/load, failover, backlog and partner outage scenarios. |
| NFR6 | Environment/tenant isolation must be tested through negative and adversarial scenarios, not only configuration review. |
| NFR7 | Vulnerability, dependency, penetration and threat-model testing must meet approved service risk criteria before pilot/production. |
| NFR8 | Incident detection, evidence, notification and recovery objectives must be approved by security/privacy/legal; no targets are invented here. |

## Threat and failure matrix

| Threat/failure | Required control/response |
|---|---|
| User authenticated but not authorised for entity | Deny, audit and alert based on risk |
| Cross-tenant identifier manipulation | Enforce server-side tenancy and negative tests |
| Secret appears in log/support export | Prevent/redact; security incident and rotation assessment |
| Certificate expired/revoked/wrong environment | Stop affected operation; rotate/revalidate |
| Stolen/replayed external message | Channel/signature/replay validation and quarantine |
| Transformation after signature | Reject workflow; enforce exchange-plan order |
| Signature validates but business authority absent | Do not infer customer authority; apply approved actor model |
| Partner subprocessor changes silently | Contract monitoring and suspend/review affected processing |
| Audit system unavailable | Preserve durable local evidence/queue; restrict high-risk actions if audit cannot be guaranteed |
| Deletion requested with open legal/lifecycle need | Place approved hold; record purpose/owner/review |
| DR restores stale credential/configuration | Reconcile trust lifecycle and external state before resumption |
| Security incident during route transition | Freeze conflicting actions; preserve both route/trust histories |

## Acceptance criteria

- Given an authenticated user without authority for the selected legal entity, when route activation is requested, then the operation is denied and audited without external mutation.
- Given a production private-platform exchange, when transport is established, then the correct operator/environment identity and approved AS2/AS4 profile are validated independently of invoice signature evidence.
- Given transformation is required, when signing occurs, then the approved transformation and semantic validation complete first and their provenance is bound to the signed representation.
- Given an inbound invoice with invalid/revoked trust, when processed, then it is quarantined, no trusted product delivery occurs and redacted evidence is available to authorised operations.
- Given a certificate approaches expiry, when rotation runs, then the new material is validated, dependencies transition under audit and the old material is revoked only after safe checks.
- Given support investigates a case, when evidence is displayed, then it contains correlation and trust results but no raw secrets/private keys or unnecessary invoice/payment content.
- Given a partner/model exit, when the exit test completes, then required data/evidence is portable, credentials are revoked at approved gates and partner deletion/retention evidence is available.
- Given a security incident affects one operator/environment, when containment occurs, then affected traffic is suspended narrowly while immutable historical evidence and unaffected isolated routes are preserved.

## Measures

| Measure | Purpose | Owner |
|---|---|---|
| Authorities/credentials with owner, scope and expiry | Control completeness | Security/product |
| Certificate rotation completed before risk threshold | Trust continuity | Security/operations |
| Invalid/replay/cross-tenant attempts prevented | Boundary effectiveness | Security |
| Privileged/key-use audit completeness | Accountability | Security/audit |
| Secrets or excessive data found in logs/exports | Data minimisation | Security/privacy |
| Partner/certification evidence current | Supplier/operator assurance | Supplier assurance |
| Security tests/findings closed by gate | Readiness | Engineering/security |
| Exit/deletion/portability exercises passed | Continuity and data governance | Product/legal/security |

## Rollout and security gates

| Gate | Required evidence |
|---|---|
| Discovery | Named security/privacy/legal owners, operator identity, data roles/classes and regulatory interpretation |
| Design | Threat model, trust/authority/data model, key/certificate design, audit, retention and partner boundary approved |
| Build/test | Secure implementation review, negative tenancy/auth tests, signing/transport conformance, replay and rotation tests pass |
| External validation | Public/counterparty trust, certificate and protocol interoperability evidenced |
| Pilot | Operator certification scope, privacy/security/supplier approvals, monitoring, incident and support controls pass PRD-SEI-221 |
| Production | Penetration/risk acceptance, key/DR/exit exercises, retention and operational readiness approved |
| Ongoing | Certification, access, key, partner, vulnerability, incident and regulatory changes trigger reassessment |

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Authentication treated as business authority | Separate identity, entity and scoped authority records |
| Transport certificate confused with invoice signature | Separate trust dimensions/evidence |
| Partner certification assumed to cover Sage flow | Verify scope, environments, subprocessors and full service chain |
| Keys exposed through products/support | Controlled custody and operation/reference interface |
| Route change destroys trust history | Immutable representation, certificate and authority evidence |
| Retention defaults conflict with privacy/continuity | Data-class policy, holds and separate deletion gates |
| Partner/model exit strands data/evidence | Contracted portability/deletion and tested exit |
| Security containment causes unnecessary outage | Tenant/operator/environment/capability-scoped controls |

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Hypothesis |
|---|---|---|---|---|
| Which legal entity is operator and certificate/signature actor? | Defines trust/accountability | Legal/security/ADR owner | Design | Open via ADR-SEI-001 |
| Is the operator ISMS certification scope/equivalent acceptable? | Statutory/readiness evidence | Security/local legal | Pilot | Require scoped evidence, not logo/certificate alone |
| What AS2/AS4 profiles and certificate authorities are required? | Interoperability/trust | Local technical/security | Build/external test | Official/counterparty evidence required |
| Who signs—issuer, delegated operator or platform seal—and under what authority? | Non-repudiation and transform order | Legal/security/operator | Design | Support only approved explicit modes |
| What public authentication/representation process will the ministerial order define? | Public trust boundary | Local technical team | External validation | Track official specification |
| What are controller/processor roles across Sage and partner? | Contract/privacy/control | Privacy/legal | Contract/pilot | Map per data flow/purpose |
| Where may invoice/payment/evidence data be stored and processed? | Residency/subprocessor architecture | Privacy/security/legal | Design/contract | Approved locations only |
| What retention/deletion periods apply by data class? | Storage, audit and exit | Legal/privacy | Production | Configurable until approved |
| What security evidence can support/customer roles see? | Diagnosis versus minimisation | Security/operations | Design | Role-specific redacted views |
| Which controls must continue for historical invoices after switch? | Credential/access lifecycle | Legal/security/product | Production/exit | Restrict to required historical operations |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 trust, identity, data and audit PRD | PRD-SEI-210/221–225 and RD 238/2026 |
