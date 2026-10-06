---
id: PRD-SEI-226
title: Security — Trust, Identity, Data and Audit
type: prd
status: discovery
owner: TBD
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-10-06
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
  - PRD-SEI-101
  - PRD-SEI-236
  - PRD-SEI-237
  - PRD-SEI-238
  - PRD-SEI-239
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "876576918"
  page_id: "866148660"
  title: Security — Trust, Identity, Data and Audit
  layout: two_left_sidebar
  toc: true
---

# Security — Trust, Identity, Data and Audit

## Decision summary

Phase 3 must establish an explicit trust chain from an authorised customer and verified legal entity through Sage users/services, operator certificates, signed invoice representations, partner/public/counterparty transport and durable audit evidence.

Identity, authority, connection credentials, certificate custody, invoice signature, electronic seal, timestamp and long-term validation evidence are separate controls. A “Sage certificate” may authenticate a Sage workload or transport channel, support a Sage-operated delegated signing service, or identify Sage as a seal creator; those meanings are not interchangeable. No credential may be shared across tenants or environments; no partner assertion may replace Sage's evidence responsibilities; and no route, support or migration action may rewrite historical trust evidence.

PRD-SEI-226 owns certificate/key lifecycle and produces purpose-scoped readiness evidence. PRD-SEI-101 may invoke setup and display readiness during onboarding, while PRD-SEI-223 and its format children consume the approved policy at representation-signing and verification time. Neither consumer owns private-key storage, rotation or revocation.

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
- Customer, accountant/delegate, Sage and provider certificates, keys, secrets, signature/seal and secure transport lifecycle.
- Certificate inventory, protected storage, dependency mapping, expiry, renewal, rotation, revocation, compromise and destruction.
- Signature validation and preservation evidence sufficient to explain historic conclusions after certificate expiry or rotation.
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
| Electronic signature | Per-representation cryptographic result associated with an authorised natural-person signatory/direct or delegated signing model | The signer's certificate, a legal-person seal or a transport certificate |
| Electronic seal | Per-representation cryptographic result associated with a legal-person seal creator and origin/integrity | Proof that a customer authorised Sage to sign, or an electronic signature by the issuer |
| Certificate | Electronic attestation binding validation data to an identified subject and purpose | A signature, seal, private key, authority grant or organisational certification |
| Private key/signature-creation data | Secret cryptographic material used to create a signature, seal or channel proof | The public certificate or safe certificate metadata |
| Sage-managed signing | Sage invokes an approved protected signing capability for an identified issuer/delegate under explicit authority | Sage becoming the invoice issuer or using a generic Sage service certificate |
| Sage operator seal | Seal created by the named Sage legal person/operator under an approved policy | Customer/delegate signature unless Legal approves that exact substitution |
| Long-term validation evidence | Signed bytes/hash, signature, chain, revocation evidence, trusted time, policy/trust-list versions and validation conclusion retained for later proof | Keeping an expired private key available for new signing |
| Organisational certification | Assurance such as ISO/IEC 27001 over a defined management-system scope | An electronic certificate or invoice signature |
| Trust evidence | Certificate chain, validation, hash, timestamp, authority and action history | Raw secret/key material |
| Data controller/processor role | Approved legal responsibility for processing | System ownership by itself |
| Audit event | Immutable security/business action evidence | Debug log containing uncontrolled content |

### Certificate, signature, seal and certification taxonomy

| Item | Principal/subject | Primary purpose | Typical custodian | Stored by product? | Expiry effect |
|---|---|---|---|---|---|
| Customer/issuer signing certificate | Issuer or authorised natural-person signatory | Create an invoice signature directly | Customer device, approved trust service or protected Sage/provider boundary | Reference and safe metadata only | Stop new signing when not currently valid; preserve historic evidence |
| Accountant/delegate signing certificate | Authorised accountant/delegate | Create a delegated invoice signature for named clients/capabilities | Accountant or approved remote signing service | Reference and safe metadata only | Stop only affected delegated use; re-evaluate every client authority |
| Sage-managed remote-signing credential | Issuer/delegate identity operated through a Sage-controlled or contracted signing service | Apply a signature without exposing key material to the ERP | Approved HSM/remote signing/trust-service boundary | Operation/reference only | Rotate or suspend affected signing policy; never fall back to another signer silently |
| Sage operator seal certificate | Named Sage legal person/operator | Create an electronic seal where the approved route/policy permits it | Sage-controlled or contracted HSM/trust service | Operation/reference only | Stop new sealing on expiry/revocation; does not erase historic seals |
| External private-platform signing/seal certificate | Provider legal person or delegated signer | Provider-owned signing/sealing under an evidenced authority model | Provider/trust service | External reference and returned evidence only | Provider readiness becomes limited/blocked until revalidated |
| Sage workload/service certificate | Sage service identity | Authenticate service-to-service calls | Sage workload identity/secret platform | Reference only | Stop/rotate affected workload; never sign an invoice with it by implication |
| AS2/AS4/mTLS transport certificate | Sage/operator/counterparty endpoint | Authenticate/encrypt transport | Relevant operator/network boundary | Reference and public metadata only | Channel becomes unavailable/untrusted; invoice signature remains a separate decision |
| Public/counterparty validation certificate | External platform/authority | Verify received responses, channels, signatures or seals | External subject; Sage stores trust evidence | Public certificate/chain and evidence as approved | Refresh trust and quarantine unsafe traffic; preserve earlier observed evidence |
| Timestamp/validation-service certificate | Trust service | Bind evidence to time or validate status | Qualified/approved trust service | Returned token/evidence, not signing key | Historical verification follows preservation policy; current expiry alone must not rewrite past conclusion |
| ISO/IEC 27001 or equivalent certification | Organisation and defined ISMS scope | Demonstrate management-system assurance | Certification body/organisation | Certificate/report reference and scope evidence | Operator readiness may lapse; it is unrelated to invoice cryptography |

### Signing and sealing modes

| Mode | Who is represented | Required authority evidence | What Sage may do | Prohibited inference |
|---|---|---|---|---|
| Direct issuer signature | Invoice issuer/signatory | Issuer identity, signing role and effective authority | Validate readiness and invoke/import the approved signature operation | A Sage login or certificate upload proves signing authority |
| Authorised delegated signature | Issuer represented by accountant, provider or Sage-operated delegate | Principal, delegate, capability/route, effective interval and delegation evidence | Invoke the delegate's protected signing operation and retain the authority snapshot | One accountant certificate covers every client or capability |
| Sage-managed remote signing for issuer/delegate | Issuer or approved delegate; Sage is service operator/custodian | Same direct/delegated authority plus approved custody and service contract | Execute a non-exportable signing operation and return evidence | The Sage workload/service identity becomes the signatory |
| Sage operator seal | Named Sage legal person/operator | Approved seal policy and legal basis for the route/document | Apply the operator seal with its own identity and evidence | A seal is equivalent to Article 7.3 delegated signature without Legal approval |
| Provider signature/seal | Provider signatory or legal person | Provider contract, authority model and verified response evidence | Request/verify the operation through the provider adapter | Provider success proves customer authority or correct signing policy |
| Transport authentication | Sage/operator/counterparty endpoint | Network/service trust policy | Establish channel and retain channel evidence | Channel authentication proves invoice origin/integrity or business authority |

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
| Sage Business Identity / trust-service owner | Operate or govern protected signing, sealing, certificate inventory, lifecycle, validation and evidence APIs without redefining customer authority |
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
| S10 | Sage performs delegated signing for a customer | The exchange plan names the customer principal, approved delegate/signing service, authority snapshot, trust policy and protected key operation | Sage workload or operator identity is never substituted silently as invoice signer |
| S11 | Sage applies an operator seal | Seal creator is the named Sage legal person and the route/policy explicitly permits that seal | Do not report it as the issuer's or accountant's signature |
| S12 | Certificate expires after an invoice was signed | New use stops; historic validation uses the retained signed object, chain, status/time and policy evidence | Do not erase evidence or mark every historic invoice invalid solely from current expiry |
| S13 | Certificate is compromised or revoked | Suspend narrow dependencies, assess signing-time and post-compromise evidence, rotate and follow incident/legal process | Do not destroy forensic/historic evidence or silently re-sign prior invoices |

## Security and data rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Actor is authenticated | Still require legal-entity authority, action and scope before privileged operation | Proposed access-control rule |
| BR2 | Credential/key is used | Bind use to owner, purpose, environment, tenant/operator scope and lifecycle | Proposed control |
| BR3 | Private-platform exchange occurs | Use approved secure transport meeting applicable AS2/AS4 requirements | RD 238/2026 Article 13; exact profile open |
| BR4 | Private-platform invoice is emitted | Apply the approved direct or authorised-delegated advanced signature after required transformation; use an operator seal only where Legal has approved that exact route/policy against the applicable duty | RD 238/2026 Articles 7 and 13; seal substitution remains open |
| BR5 | Data crosses Sage/partner/public boundary | Apply approved purpose, role, minimisation, encryption, residency and retention | Regulatory/security/privacy control |
| BR6 | Support/audit evidence is generated | Exclude secrets/private keys and minimise invoice/payment/personal content | Confirmed repository/security principle |
| BR7 | Trust/authority is revoked or expires | Stop affected new use and enter controlled recovery without deleting historical evidence | Proposed lifecycle control |
| BR8 | Route/operator changes | Preserve original signature, certificate validation, actor, representation hash and network evidence | Confirmed continuity principle |
| BR9 | Partner operates a control | Sage requires scoped evidence, incident access, audit rights, subprocessor/change control and exit obligations | ADR/PRD-SEI-221 principle |
| BR10 | Retention/deletion conflict exists | Legal hold/approved obligation wins; record decision and delete only at authorised gate | Open legal/privacy policy |
| BR11 | A “Sage certificate” is proposed | Classify it as workload, transport, delegated-signing, operator-seal, validation or timestamp material before design/activation | Proposed terminology/control rule |
| BR12 | Sage signs for an issuer/delegate | The signed evidence must name the represented principal, actual signer/delegate, authority snapshot and Sage signing-service role separately | RD 238/2026 Article 7.3; exact service model open |
| BR13 | Sage applies its own operator seal | Record Sage as seal creator and require explicit legal/route approval; never label it as the customer's signature | eIDAS distinction; Spanish applicability open |
| BR14 | Certificate validity ends or status becomes unsafe | Stop new dependent use, invalidate current readiness and rotate/recover without rewriting the evidence of completed operations | Lifecycle/continuity rule |
| BR15 | Historic signature is inspected after certificate expiry/rotation | Evaluate the preserved signing-time evidence and approved validation policy; do not decide from current certificate dates alone | ETSI preservation principle; retention profile open |

## Research and evidence register

### Final public-order evidence

Article 11 of the final order distinguishes authentication from representation. Third-party Article 9 recovery and Article 10 consultation, including web-service/automated access, require registered power of attorney. Check action and represented legal entity separately from certificate validity. The AEAT procedure/code, verification, revocation and accepted certificate contract remain implementation gates; do not infer these from SII or VERI*FACTU. See the [source snapshot and impact review](../research/spain-public-platform-order-evidence.md).


| Source | Finding | Confidence/limitation | Security impact |
|---|---|---|---|
| RD 238/2026 Article 7 | Transformation must preserve authenticity/integrity; private-platform invoices require advanced signature under the defined model | Primary regulation; implementation/trust profile approval required | Transform/sign order, evidence and validation |
| [RD 238/2026 Article 7.3–7.4](https://www.boe.es/eli/es/rd/2026/03/25/238) | Every invoice issued through a private platform requires an advanced electronic signature, directly by the issuer or through authorised delegated signing; required transformation occurs before signing | Primary regulation; exact signature container/profile and accepted delegated-service model remain to be approved | Direct/delegated signing modes, authority snapshot and transform-before-sign control |
| [Amended invoicing-regulation Article 10.1(a)](https://www.boe.es/eli/es/rd/2026/03/25/238) | Origin/integrity may use an advanced signature based on a qualified signature certificate or an advanced seal based on a qualified seal certificate | Primary regulation; this does not by itself prove a Sage operator seal satisfies the narrower Article 7.3 private-platform signature duty | Keep signature and seal policies separate pending Legal decision |
| RD 238/2026 Article 13 | Operator requires ISO/IEC 27001 or equivalent, AS2/AS4, advanced signature/seal capability, data governance/confidentiality and breach prevention | Primary regulation; certification scope/equivalence and technical profiles require evidence | Certification, protocol, PKI, data and incident controls |
| RD 238/2026 Article 13.2 | UNE data-governance maturity is one described way to meet the stated governance requirement | Primary regulation; applicability/route requires compliance approval | Data-control assessment option |
| RD 238/2026 Article 11 | Public authentication/representation and integrity procedures depend on official specifications | Primary regulation with ministerial-order dependency | Public trust adapter and readiness gate |
| PRD-SEI-202/203 | Connection-aware credential lifecycle, tenancy, audit and resilience | Product intent; implementation fitness unassessed | Reuse assessment input |
| ADR-SEI-001/PRD-SEI-221 | Named operator, accountability, supplier evidence and ongoing readiness | Proposed governance | Control ownership and partner boundary |
| [eIDAS Regulation (EU) 910/2014, consolidated](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02014R0910-20240520) | Separates electronic signatures, electronic seals, their qualified certificates, trust-service providers, remote creation devices, validation, timestamps and preservation services | Primary EU framework; selected qualified/non-qualified service and Spanish application require Legal/Security approval | Trust taxonomy, signer/seal-creator identity, remote signing and provider due diligence |
| [ETSI EN 319 102-1](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/01.04.00_20/en_31910201v010400a.pdf) | Long-term signature availability depends on retaining/augmenting validation material and time evidence before algorithms or supporting certificates become unsuitable | Technical standard; exact baseline/profile must be selected by architecture/security | Historic validation package, crypto agility and preservation events |
| [Spanish electronic signature and certificate policy catalogue](https://administracionelectronica.gob.es/ctt/politicafirma/descargas) | Publishes Spanish administration signature/certificate policies, including Facturae material | Public-sector/profile evidence; does not define every B2B private-platform profile | PRD-SEI-239 and route-specific policy registry |

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
| Identity | Trust-material ID/reference, class, owner/legal subject, custodian, issuer, certificate subject/SANs, serial/fingerprint and environment |
| Purpose | Transport authentication, workload authentication, direct signing, delegated signing, sealing, validation or timestamping; never a generic `SIGNING` purpose |
| Scope | Tenant, principal, delegate, operator/service, capability, direction, route/profile and environment permitted; never raw key material |
| Authority | Direct/delegated/seal policy, principal/delegate, authority reference, effective interval and revocation status |
| Validity | `notBefore`, `notAfter`, issuer/chain status, status source, checked time and next mandatory recheck |
| Lifecycle | Requested, approved, provisioned, active, expiring, rotation-pending, suspended, expired, revoked, compromised and destroyed timestamps/reasons |
| Custody | Customer device, provider, Sage vault/HSM/KMS or remote trust service; exportability, access policy, dual control and backup/recovery rules |
| Cryptography | Key type/size, algorithm constraints, signature/profile identifiers and crypto-policy version without exposing key data |
| Evidence | Public certificate/chain, fingerprint, validation conclusion, revocation response, trusted timestamp and audit references as approved |
| Dependency | Connections, routes, workloads, sign/seal policies, queued/in-flight operations and historical obligations using it |
| Operations | Owner, renewal/rotation owner, expiry horizon, alert state, last test, incident state and customer/operator remediation |

### Trust-policy record

| Area | Required information |
|---|---|
| Applicability | Country, route, direction, document/format profile, environment and effective interval |
| Required trust result | No certificate, transport authentication, direct advanced signature, authorised delegated signature, seal, or combined requirements |
| Actor | Principal, permitted signer/delegate or seal creator and authority policy |
| Certificate policy | Permitted certificate class/issuer/trust list, key usage, algorithms and validation rules |
| Custody policy | Customer, accountant, Sage, provider or qualified/approved remote service; export and recovery restrictions |
| Ordering | Required transform, validate, sign/seal, timestamp and transmit sequence |
| Runtime checks | Current authority, validity, revocation/status freshness, environment, purpose and dependency readiness |
| Preservation | Signed object, validation package, trusted time/augmentation, retention and revalidation/renewal rules |
| Versioning | Policy ID/version, approval, evidence source, activation/retirement and rollback |

### Signed-representation evidence record

| Area | Required information |
|---|---|
| Signed object | Exact signed bytes or immutable object reference, content hash, format/profile and representation ID |
| Signature/seal | Signature value/container/profile, claimed signing time, signer/seal-creator identity and role |
| Certificate evidence | Signer certificate and chain, fingerprints, issuer, serial, validity interval and qualified-status evidence where required |
| Authority evidence | Direct/delegated/seal policy, principal/delegate and immutable authority snapshot used at signing time |
| Validation evidence | Validation policy/version, conclusion, time, trust-list/chain, OCSP/CRL/status evidence and warnings |
| Trusted time/preservation | Timestamp/evidence-record references, augmentation/preservation events and algorithm-policy version |
| Provenance | Transformation/mapping/validation pack, signing service/provider, environment, correlation and audit references |

### Certificate lifecycle and readiness states

`REQUESTED → APPROVED → PROVISIONED → ACTIVE → EXPIRING → ROTATION_PENDING → RETIRED → DESTROYED`

Exception states: `SUSPENDED`, `EXPIRED`, `REVOKED`, `COMPROMISED`, `VALIDATION_UNKNOWN`.

- `ACTIVE` is purpose-, scope-, environment- and authority-specific; it is not a universal certificate status.
- `EXPIRING` and alert horizons are policy-configured by certificate class and owner rather than hard-coded in this PRD.
- Rotation may permit a controlled overlap only where the protocol/signature policy allows it; the exact certificate used is frozen per operation.
- `EXPIRED`, `REVOKED`, `COMPROMISED` or `VALIDATION_UNKNOWN` prevents new dependent operations unless an approved, explicit exception exists.
- Current expiry must not rewrite a historic signature conclusion solely because the certificate later expired. Historic verification uses the signed representation and preserved evidence under the approved validation/preservation policy.
- Private-key destruction and signed-evidence retention are separate decisions: the private key may be retired/destroyed while signed bytes, public certificate chain and validation/preservation evidence remain retained.

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
5. Old private-key material is revoked/retired/destroyed after active-dependency and incident gates; the public certificate and historic validation/preservation evidence remain for the approved retention period.

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

### J7 — Onboard customer or accountant certificate

1. Onboarding resolves the exact capability, route, format/signature profile, environment and signer model.
2. The user selects direct issuer, authorised delegate, Sage-managed signing, provider signing or another approved mode; `Sage certificate` is not accepted as an undifferentiated answer.
3. The approved custody service provisions/imports or references the certificate without returning private-key material to the product.
4. Sage verifies owner, custodian, principal, delegate, authority, purpose/key usage, environment, chain/trust, validity and current revocation/status evidence.
5. Readiness becomes effective only for the proven scope and records its next recheck/expiry dependency.

### J8 — Sage-managed delegated signature

1. Exchange planning selects a policy that explicitly permits Sage-operated remote signing for the identified customer/delegate.
2. Sage rechecks customer authority, delegated-signing authority, certificate readiness and final representation hash immediately before use.
3. A protected signing operation occurs in the approved HSM/remote-signing/trust-service boundary; the ERP, logs and support surfaces never receive the private key.
4. Sage binds returned signature evidence to the exact representation, principal, delegate, service role, policy and signing time.
5. Any ambiguous signing outcome is reconciled by immutable operation/reference before another signing request is attempted.

### J9 — Expiry, renewal and historic validation

1. Inventory monitoring identifies an approaching policy horizon and every active dependency/owner.
2. Renewal or new material is provisioned and validated in the correct environment; overlap is used only when the applicable protocol/policy permits it.
3. New operations switch through an effective-dated, auditable policy change; in-flight operations keep their frozen trust plan unless safely restarted.
4. Expired/retired material is blocked from new use and later revoked/destroyed according to approved dependency and incident checks.
5. Historic invoices retain exact signed bytes, public certificate chain, validation result, revocation/time evidence, trust/policy versions and preservation events required for later verification.

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
| FR27 | Expose a non-secret certificate-readiness contract covering reference, owner/legal subject, purpose, environment, authority link, issuer/chain, validity, revocation/status evidence, checked time and remediation. |
| FR28 | Notify or invalidate dependent onboarding/runtime readiness when a certificate expires, rotates, is revoked, changes purpose/scope or loses its authority link. |
| FR29 | Preserve historic certificate/signature attribution across rotation and route/provider changes without permitting obsolete material for new operations. |

### Certificate, signing, sealing and preservation

| ID | Requirement |
|---|---|
| FR30 | Classify every trust item as customer/delegate signing, Sage-managed signing, Sage operator seal, provider signing/seal, workload identity, transport, validation or timestamp material before provisioning or use. |
| FR31 | Maintain an inventory and dependency graph linking each trust-material version to its owner, custodian, scope, environment, workloads, connections, routes, policies, queued/in-flight operations and historical evidence obligations. |
| FR32 | Support direct issuer, authorised delegated, Sage-managed remote-signing, provider and operator-seal modes as separate policies; a product must not select one as a silent fallback for another. |
| FR33 | Where Sage manages signing for an issuer/delegate, the trust service must verify the represented principal, actual signer/delegate, authority snapshot, certificate purpose/scope and final representation hash before the protected key operation. |
| FR34 | A Sage workload or transport certificate must never create an invoice signature or seal unless a separately approved policy explicitly provisions that material for the required legal purpose. |
| FR35 | A Sage operator seal must identify the Sage seal creator and must not be represented as the customer's/direct or delegated signature; use for a Spanish private-platform invoice requires explicit Legal approval against the applicable duty. |
| FR36 | Store private keys/signature-creation data only in the approved customer device, provider, vault/HSM/KMS or remote trust-service boundary; application databases, products, logs, support tools and PRDs may store only references and approved public metadata/evidence. |
| FR37 | Enforce non-exportability where required, least privilege, dual control for high-risk lifecycle actions, attributable key use, environment separation and tested backup/recovery without uncontrolled key copies. |
| FR38 | Monitor `notBefore`, `notAfter`, status/revocation freshness, trust-chain changes, algorithm policy and authority validity using certificate-class-specific horizons and named renewal/rotation owners. |
| FR39 | Prevent new dependent operations when trust material is not yet valid, expired, revoked, compromised, suspended, wrong-purpose, wrong-owner, wrong-environment or validation-unknown; expose the affected scope and remediation. |
| FR40 | Perform renewal/rotation using effective-dated versions, tested counterpart compatibility and controlled overlap only where policy permits; freeze the exact trust-material and policy versions per operation. |
| FR41 | Treat certificate compromise separately from routine expiry: contain affected dependencies, preserve forensic evidence, assess signing-time impact and invoke security/legal notification and recovery processes. |
| FR42 | Persist the exact signed/sealed representation plus signature/seal, public certificate chain, authority snapshot, validation policy/conclusion, revocation/status evidence, trusted time and provenance required by the approved retention/preservation profile. |
| FR43 | Support revalidation and preservation/augmentation events without altering the original signed bytes or presenting a new preservation timestamp as the original signing time. |
| FR44 | Keep private-key retention/destruction independent from signed-evidence retention; destruction of retired key material must not delete public certificate, signature or validation evidence needed for historic proof. |
| FR45 | Return purpose-specific readiness and health (`TRANSPORT_READY`, `DIRECT_SIGN_READY`, `DELEGATED_SIGN_READY`, `SEAL_READY`, `VALIDATION_READY`) rather than one generic certificate status. |

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
| NFR9 | Signing/sealing operations and lifecycle mutations must be attributable, tamper-evident and correlated to the requesting actor, principal, representation and policy version. |
| NFR10 | Certificate inventory and dependency monitoring must detect expiry, revocation/status, algorithm-policy and trust-chain risk early enough for the approved rotation process; exact horizons require owner approval. |
| NFR11 | Protected signing/sealing service availability, capacity, throttling and disaster recovery must be measured against the invoice-volume and deadline model; no signing target is invented here. |
| NFR12 | Historic validation/preservation evidence must remain readable and verifiable across certificate, provider, route, system and algorithm migrations for the approved retention period. |
| NFR13 | Cryptographic erasure, key destruction and evidence deletion must require independent dependency, retention/legal-hold and audit gates. |

## Threat and failure matrix

| Threat/failure | Required control/response |
|---|---|
| User authenticated but not authorised for entity | Deny, audit and alert based on risk |
| Cross-tenant identifier manipulation | Enforce server-side tenancy and negative tests |
| Secret appears in log/support export | Prevent/redact; security incident and rotation assessment |
| Certificate expired/revoked/wrong environment | Stop affected operation; rotate/revalidate |
| Certificate approaches expiry with active dependencies | Alert named owner, provision/test replacement and expose at-risk capabilities; do not wait for failure |
| Certificate expires after historic signing | Block new use; validate history from retained signing-time evidence and approved policy rather than current date alone |
| Certificate compromised | Suspend narrow dependencies, preserve evidence, assess affected signatures/transactions and invoke incident/legal response |
| Sage workload certificate selected for invoice signing | Reject policy resolution; require an approved direct/delegated/seal trust policy and purpose-specific material |
| Sage operator seal proposed as delegated customer signature | Block until Legal approves the exact route/policy; preserve the distinction in UX and evidence |
| Signing operation times out after possible key use | Mark outcome unknown and query/reconcile by immutable signing-operation reference before retry |
| Private key exported to product/log/support path | Prevent where possible; treat as security incident, rotate/contain and investigate exposure |
| Validation evidence unavailable after provider exit | Use contracted export/preservation path; block exit completion until approved evidence continuity is proven |
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
- Given a Sage workload certificate is valid, when an invoice-signing operation requests it, then the request is rejected unless an independently approved signing/seal policy and purpose-specific trust-material version authorise that use.
- Given Sage performs delegated signing, when the signature is created, then evidence distinguishes the customer principal, authorised delegate/signatory, Sage signing-service role, authority snapshot, certificate and exact signed representation.
- Given Sage applies an operator seal, when evidence is displayed, then Sage is named as seal creator and the result is never labelled as the customer's/direct or delegated signature.
- Given a certificate enters the configured expiry horizon, when monitoring evaluates dependencies, then the named owner, affected capabilities and required renewal/rotation action are visible without exposing key material.
- Given an active certificate expires or is revoked, when a new dependent operation starts, then it is blocked while unaffected certificate purposes/routes continue where safe.
- Given an invoice was validly signed before its certificate later expired, when historic verification occurs, then the result uses the retained signed bytes, chain, signing-time/status/time and policy evidence rather than failing solely because the certificate is now expired.
- Given a protected signing request times out after possible execution, when recovery runs, then Sage reconciles the original signing-operation reference and does not create a second signature blindly.
- Given retired private-key material is destroyed, when an authorised historic invoice is inspected, then the signed representation, public certificate chain and approved validation/preservation evidence remain available.

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
| Trust material by class, purpose, owner and lifecycle state | Finds unowned or misclassified Sage/customer/provider certificates | Security/trust owner |
| Certificates inside each approved expiry horizon with unresolved replacement | Measures continuity risk without inventing a universal warning period | Security/operations |
| New operations blocked by expired/revoked/wrong-purpose material | Detects policy and renewal failures | Security/product |
| Direct, delegated, Sage-managed, provider and seal operations by policy/version | Makes the actual signing model observable | Product/legal/security |
| Historic signatures with complete validation/preservation package | Measures evidence durability | Security/audit/legal |
| Signing outcome-unknown cases and reconciliation age | Measures duplicate-signature/recovery risk | Trust-service operations |

## Rollout and security gates

| Gate | Required evidence |
|---|---|
| Discovery | Named security/privacy/legal owners, operator identity, data roles/classes and regulatory interpretation |
| Design | Threat model, trust/authority/data model, certificate taxonomy, signer/seal modes, custody/storage, expiry/rotation, historic-preservation, audit, retention and partner boundary approved |
| Build/test | Secure implementation review, negative tenancy/auth tests, direct/delegated/Sage-managed/seal policy tests, signing/transport conformance, replay, outcome-unknown, expiry, rotation, compromise and historic-revalidation tests pass |
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
| “Sage certificate” becomes an ambiguous catch-all | Mandatory trust-material classification and purpose-specific readiness/API contracts |
| Sage operator seal is mistaken for customer/delegated signature | Separate policies, legal gate, explicit signer/seal-creator evidence and UX labels |
| Certificate expires without a known dependency owner | Inventory/dependency graph, class-specific horizons and named renewal/rotation ownership |
| Historic signatures become unverifiable after expiry/provider exit | Preserve signed bytes, chain, status/time, validation/policy and portability evidence |
| Keys are copied into product databases for convenience | Non-exportable protected operation boundary and reference-only product contracts |
| Rotation creates duplicate or differently signed invoice attempts | Freeze trust plan per operation and reconcile ambiguous signing outcomes before retry |

## Open questions and owners

| Question | Why it matters | Owner | Blocks | Hypothesis |
|---|---|---|---|---|
| Which legal entity is operator and certificate/signature actor? | Defines trust/accountability | Legal/security/ADR owner | Design | Open via ADR-SEI-001 |
| Is the operator ISMS certification scope/equivalent acceptable? | Statutory/readiness evidence | Security/local legal | Pilot | Require scoped evidence, not logo/certificate alone |
| What AS2/AS4 profiles and certificate authorities are required? | Interoperability/trust | Local technical/security | Build/external test | Official/counterparty evidence required |
| Who signs—issuer, delegated operator or platform seal—and under what authority? | Non-repudiation and transform order | Legal/security/operator | Design | Support only approved explicit modes |
| Does RD 238/2026 Article 7.3 permit a Sage operator seal for any private-platform issuance scenario, or only direct/authorised delegated electronic signature? | Prevents treating signature and seal as interchangeable | Spain Legal/compliance | Trust policy and production signing | Block seal substitution until explicitly approved |
| When Sage provides “Sage signature”, is Sage a remote-signing service for the customer/delegate, the legal signer/delegate, or the operator seal creator? | Determines identity, authority, liability, certificate subject and UX wording | Business Identity owner, Legal, Security, Product | Architecture/contract | Model all separately; choose per approved service |
| Which Sage Business Identity/trust capability owns certificate inventory, remote signing/sealing, validation and preservation evidence? | Avoids duplicate key stores and incomplete lifecycle ownership | Business Identity owner (Sam Reid) / architecture | Build | PRD-SEI-226 owns contract; service ownership must be named |
| Which certificate classes may be customer-held, accountant-held, Sage-held or provider-held, and may private keys ever be imported/exported? | Determines custody UX, HSM/remote-service design and support boundary | Security/Legal/Product | Design | Prefer non-exportable protected operations and references |
| What expiry warning and rotation-overlap policies apply to each certificate class/protocol? | Prevents outage without inventing one universal threshold | Security/operations/provider owners | Operations readiness | Configure per class with named owner and tested lead time |
| Which timestamp, OCSP/CRL/status, trust-list, signature level and preservation/augmentation evidence must be retained per route/profile? | Determines historic verification after expiry or algorithm change | Legal/security/local technical team | Retention and validation design | Retain a complete versioned validation package until approved profile says otherwise |
| What happens to queued/in-flight invoices when a signing certificate rotates, expires or is revoked? | Prevents silent re-signing, duplicate attempts and unexplained representation change | Product/architecture/operations | Runtime design | Freeze trust version per attempt; restart only under explicit audited policy |
| Which AEAT certificate and registered-authority procedures implement Article 11? | Public trust boundary | Local technical team | External validation | Track official specification |
| What are controller/processor roles across Sage and partner? | Contract/privacy/control | Privacy/legal | Contract/pilot | Map per data flow/purpose |
| Where may invoice/payment/evidence data be stored and processed? | Residency/subprocessor architecture | Privacy/security/legal | Design/contract | Approved locations only |
| What retention/deletion periods apply by data class? | Storage, audit and exit | Legal/privacy | Production | Configurable until approved |
| What security evidence can support/customer roles see? | Diagnosis versus minimisation | Security/operations | Design | Role-specific redacted views |
| Which controls must continue for historical invoices after switch? | Credential/access lifecycle | Legal/security/product | Production/exit | Restrict to required historical operations |

## Change log

| Date | Version | Change | Evidence/decision |
|---|---|---|---|
| 2026-08-10 | Version 1 | Initial Phase 3 trust, identity, data and audit PRD | PRD-SEI-210/221–225 and RD 238/2026 |
| 2026-09-21 | Version 2 | Clarified lifecycle ownership and added the certificate-readiness contract consumed by onboarding and format-specific exchange | PRD-SEI-101/223/236–239; RD 238/2026 Article 7.3 |
| 2026-09-22 | Version 3 | Separated customer/delegate, Sage-managed, provider, operator-seal, workload and transport certificate models; added protected storage, inventory, expiry/rotation/compromise, outcome-unknown signing and long-term validation/preservation requirements | Stakeholder direction; RD 238/2026 Articles 7/10/13; eIDAS; ETSI EN 319 102-1; Spanish signature-policy catalogue |
