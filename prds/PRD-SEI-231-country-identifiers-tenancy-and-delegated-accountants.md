---
id: PRD-SEI-231
title: E-Invoicing — Country Identifiers, Tenancy and Delegated Accountants
type: prd
status: discovery
owner: TBD
product: multi-country-e-invoicing
created: 2026-08-12
updated: 2026-08-18
reviewers: []
related:
  - PRD-SEI-227
  - PRD-SEI-223
  - PRD-SEI-226
  - PRD-SEI-232
  - PRD-SEI-233
  - PRD-SEI-234
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "866150169"
  page_id: "866152234"
  title: E-Invoicing — Country Identifiers, Tenancy and Delegated Accountants
  layout: two_left_sidebar
  toc: true
---

# E-Invoicing — Country Identifiers, Tenancy and Delegated Accountants

## Decision summary

Model Sage access context, legal identity, establishment identity, tax identity, network address, delegated authority and credentials as separate, related records. Do not attach country identifiers directly to `tenantId` or `datasetId`, and do not treat a credential as proof that an accountant may act for every client or operation.

Apply those identities through one immutable **compliance context** that produces three independently evidenced outcomes:

1. **Document compliance** — the invoice representation contains the correct legal, tax and establishment identities and satisfies the applicable semantic/profile rules.
2. **Delivery compliance** — the intended recipient was resolved using an eligible network address and the invoice reached the required destination through an approved route.
3. **Reporting compliance** — each required authority report used the correct taxpayer/reporting identity, met its timing/content rule and received or reconciled an authority outcome.

**Compliance delivery** is the overall product capability that determines, orchestrates and evidences the applicable set of obligations. It is not a fourth compliance result. **Delivery compliance** is only the recipient-delivery branch. Success in one branch must never imply success in another.

For France, the corrected cardinality is: an accountant portfolio may contain many client **SIRENs**; each legal unit has one SIREN and may have many establishment **SIRETs**. A SIRET contains the SIREN plus an establishment-specific NIC. [French official guidance](https://entreprendre.service-public.gouv.fr/vosdroits/F32135) gives the example `1 SIREN + 3 SIRETs` for one head office and two shops.

This is a discovery contract, not an approved physical schema or API.

## Outcome, phase and product principles

This discovery defines how Sage products, customers, accountants, platform services and operations can identify the correct legal subject, prove authority and explain each compliance outcome across France, Spain, Germany, Ireland and the UK. It does not activate a country, choose a provider or approve a physical architecture.

| Principle | Product consequence |
|---|---|
| One context, three outcomes | Document, recipient-delivery and authority-reporting states remain independently queryable, recoverable and evidenced. |
| Identity is role-specific | A legal-registration number, establishment number, VAT number and network address may share characters but are never interchangeable without an explicit scheme and role. |
| Authority is evaluated per operation | An accountant's login or certificate does not grant portfolio-wide submission, retrieval, correction or reporting rights. |
| Policy owns applicability | The effective country pack determines which identifiers and outcome branches are required for the transaction. |
| History is immutable | Later identifier, route, mandate or country-policy changes do not rewrite the context used for an existing invoice. |
| Country variation is configuration where possible | Shared records and workflow contracts hold country-owned catalogs, validators, directory rules and authority evidence without country-named tenant columns. |

## Definitions and boundaries

| Term | Meaning in this PRD | Must not be confused with |
|---|---|---|
| Compliance delivery | Overall capability that evaluates policy, binds identity/authority, executes required compliance legs and retains evidence | Recipient delivery alone |
| Document compliance | Validity of the structured invoice representation under the applicable semantic, syntax/profile and business rules | Proof the recipient received it |
| Delivery compliance | Successful and evidenced delivery to the intended recipient using an eligible address, route and provider/network context | Government reporting or commercial acceptance |
| Reporting compliance | Successful and evidenced submission of required invoice, transaction, payment or status data to the competent authority | Delivery to the buyer |
| Compliance context | Immutable record of actor, legal subjects, identifier snapshot, authority decision, policy version, obligations, direction and effective time used for one invoice/action | Mutable customer master data |
| Legal entity identity | Official identity of the person or organisation bearing rights and obligations | Establishment, VAT registration or network address |
| Establishment identity | Identity of a branch, site, fixed establishment or operational unit when the country supplies or requires one | The parent legal entity |
| Tax identity | Identifier issued for a tax purpose, including VAT where applicable | Universal proof of legal incorporation or delivery address |
| Network address | Scheme-qualified participant/directory/routing identity used to discover or address an electronic destination | Taxpayer identity or selected service provider |
| Delegated authority | Effective, evidenced permission for a delegate to perform named capabilities for a principal | Authentication, credential possession or a general product role |
| Delivery acknowledgement | Technical/network evidence about receipt by the next required destination | Buyer acceptance, tax acceptance or overall compliance |

## Capability model

| Layer | Shared capability | Country-owned decision or binding | Evidence state |
|---|---|---|---|
| Applicability | Evaluate seller, buyer, establishment, transaction, direction and effective time | Scope, exemptions, dates and required obligation branches | Proposed shared contract; country rules require approval |
| Identity | Store and version scheme-qualified identifiers against legal subjects | Official schemes, issuers, formats, cardinality and permitted roles | France partly confirmed; other catalogs expanded below |
| Authority | Evaluate principal, delegate, user, capability, direction and validity | Legally accepted mandate/agent evidence and operation scope | Country-specific confirmation required |
| Document | Bind invoice parties/establishments and validate representation | Required invoice identifiers, profiles, fields and validation rules | Country/profile evidence required |
| Delivery | Resolve recipient and execute an eligible route | Directory key, participant scheme, routing qualifier, network and acknowledgement | Country/network evidence required |
| Reporting | Create independent authority legs and reconcile outcomes | Reporter identity, authority schema, deadlines and acknowledgements | France/Spain examples; other country details gated |
| Evidence | Retain immutable decision, identity snapshot and outcome history | Retention, disclosure and legal-evidence requirements | Shared concept; policy and security approval required |

## Identity-driven compliance delivery

<!-- confluence-html-macro:start -->
<div class="eii-compliance-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eii-compliance-map *{box-sizing:border-box}.eii-compliance-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eii-compliance-map svg{display:block;width:1100px;height:700px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eii-compliance-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.7}.eii-compliance-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eii-compliance-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eii-compliance-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eii-compliance-map .title{fill:#172b4d;font-size:11px;font-weight:700}.eii-compliance-map .copy{fill:#42526e;font-size:8.8px}.eii-compliance-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eii-compliance-map .path{fill:none;stroke:#00875a;stroke-width:2}.eii-compliance-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eii-compliance-map .path-warn{fill:none;stroke:#ff991f;stroke-width:1.8;stroke-dasharray:6 4}.eii-compliance-map .arrow{fill:#00875a}.eii-compliance-map .arrow-g{fill:#6b778c}.eii-compliance-map .arrow-w{fill:#ff991f}.eii-compliance-map .notes{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;min-width:1100px;margin-top:10px}.eii-compliance-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eii-compliance-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">Compliance delivery binds one policy and identity snapshot, then manages document, recipient-delivery and authority-reporting obligations as separate outcome legs.</p>
  <svg viewBox="0 0 1100 700" role="img" aria-label="Invoice intent and actor enter a country-policy decision. Policy creates one immutable compliance context containing tenant, legal entities, establishments, identifier snapshots, delegated authority, policy version and effective time. The context activates three independent branches: document compliance using legal, establishment and tax identities; delivery compliance using participant, directory and routing identities; and optional reporting compliance using taxpayer, reporter, delegate and authority identifiers. Each branch has its own state, correlation, acknowledgement and evidence. A derived compliance summary never replaces the three outcomes. Identity or mandate changes apply only to eligible new actions while historical context remains unchanged.">
    <text x="32" y="30" class="label">REQUEST AND POLICY</text><text x="318" y="30" class="label">ONE IMMUTABLE CONTEXT</text><text x="692" y="30" class="label">THREE INDEPENDENT OUTCOMES</text>
    <rect x="32" y="66" width="220" height="92" rx="10" class="main"/><text x="52" y="96" class="title">Invoice intent + actor</text><text x="52" y="118" class="copy">tenant • product • direction • transaction</text><text x="52" y="138" class="copy">direct user or delegated accountant</text>
    <path d="M142 158 V198" class="path"/><polygon points="142,198 136,188 148,188" class="arrow"/>
    <rect x="32" y="200" width="220" height="112" rx="10" class="main"/><text x="52" y="230" class="title">Country policy decision</text><text x="52" y="252" class="copy">scope • exemption • effective date</text><text x="52" y="272" class="copy">required branches • identifier roles</text><text x="52" y="292" class="copy">policy and evidence versions</text>
    <path d="M252 256 H316" class="path"/><polygon points="316,256 306,250 306,262" class="arrow"/>
    <rect x="318" y="168" width="310" height="176" rx="12" class="warn"/><text x="340" y="198" class="title">ComplianceContext — proposed</text><text x="340" y="222" class="copy">workspace • tenant • legal entity • establishment</text><text x="340" y="244" class="copy">scheme-qualified identifier snapshots</text><text x="340" y="266" class="copy">actor • delegated-authority decision • credential ref</text><text x="340" y="288" class="copy">policy/obligation versions • effective time</text><text x="340" y="310" class="copy">invoice/action ID • idempotency • provenance</text><text x="340" y="332" class="copy">immutable after first external mutation</text>
    <path d="M628 220 H676 V104 H704" class="path"/><polygon points="704,104 694,98 694,110" class="arrow"/>
    <path d="M628 256 H704" class="path"/><polygon points="704,256 694,250 694,262" class="arrow"/>
    <path d="M628 292 H676 V410 H704" class="path-opt"/><polygon points="704,410 694,404 694,416" class="arrow-g"/>
    <rect x="706" y="56" width="344" height="116" rx="10" class="main"/><text x="728" y="86" class="title">Document compliance outcome</text><text x="728" y="108" class="copy">legal entity • establishment • tax identifiers</text><text x="728" y="128" class="copy">semantic/profile validation • representation evidence</text><text x="728" y="148" class="copy">state • rule results • mapper/profile version</text>
    <rect x="706" y="204" width="344" height="116" rx="10" class="main"/><text x="728" y="234" class="title">Delivery compliance outcome</text><text x="728" y="256" class="copy">sender/recipient participant • directory/routing key</text><text x="728" y="276" class="copy">network • provider role • endpoint capability</text><text x="728" y="296" class="copy">state • correlation • delivery acknowledgement</text>
    <rect x="706" y="352" width="344" height="116" rx="10" class="optional"/><text x="728" y="382" class="title">Reporting compliance outcome</text><text x="728" y="404" class="copy">taxpayer • reporter/delegate • authority account</text><text x="728" y="424" class="copy">report schema • deadline • authority destination</text><text x="728" y="444" class="copy">state • correlation • authority acknowledgement</text>
    <path d="M1050 114 H1070 V561 H1050" class="path"/><path d="M1050 262 H1070" class="path"/><path d="M1050 410 H1070" class="path-opt"/><polygon points="1050,561 1060,555 1060,567" class="arrow"/>
    <rect x="706" y="522" width="344" height="78" rx="39" class="finish"/><text x="750" y="552" class="title">Evidence + derived summary</text><text x="750" y="574" class="copy">complete • action required • reconciling • in progress</text><text x="750" y="592" class="copy">three outcomes retained under one context</text>
    <rect x="318" y="408" width="310" height="116" rx="10" class="optional"/><text x="340" y="438" class="title">Current identity and authority records</text><text x="340" y="460" class="copy">can change for eligible future actions</text><text x="340" y="480" class="copy">revocation/expiry blocks new protected operations</text><text x="340" y="500" class="copy">historical snapshots remain explainable</text>
    <path d="M473 408 V344" class="path-warn"/><polygon points="473,344 467,354 479,354" class="arrow-w"/>
    <rect x="226" y="620" width="648" height="42" rx="21" class="finish"/><text x="310" y="646" class="title">Compliance delivery = applicable obligations + independent outcomes + one retained context</text>
  </svg>
  <div class="notes"><div class="note"><strong>Different identifiers</strong>Invoice party identity, recipient address and authority-reporting identity can legitimately differ.</div><div class="note"><strong>No inherited success</strong>A valid document can still be undelivered; a delivered invoice can still have failed reporting.</div><div class="note"><strong>Delegation is per branch</strong>Submit, retrieve, correct, report and view evidence can require different grants.</div><div class="note"><strong>History stays fixed</strong>Current master-data corrections apply prospectively and never rewrite an executed context.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Identity and authority map

<!-- confluence-html-macro:start -->
<div class="eii-map" style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;padding:22px;background:#fff;border:1px solid #dfe1e6;border-radius:8px;box-sizing:border-box;max-width:1180px;margin:0 auto;overflow-x:auto;">
  <style>
    .eii-map *{box-sizing:border-box}.eii-map .sub{margin:0 0 14px;color:#6b778c;font-size:12px}.eii-map svg{display:block;width:100%;max-width:1100px;height:auto;min-width:760px;border:1px solid #dfe1e6;border-radius:8px;background:#fcfcfd}.eii-map .main{fill:#e3fcef;stroke:#36b37e;stroke-width:1.6}.eii-map .finish{fill:#abf5d1;stroke:#00875a;stroke-width:1.8}.eii-map .optional{fill:#f4f5f7;stroke:#6b778c;stroke-width:1.5;stroke-dasharray:7 5}.eii-map .warn{fill:#fff7d6;stroke:#ffab00;stroke-width:1.6}.eii-map .title{fill:#172b4d;font-size:10px;font-weight:700}.eii-map .copy{fill:#42526e;font-size:8.5px}.eii-map .label{fill:#6b778c;font-size:9px;font-weight:700;letter-spacing:.08em}.eii-map .path{fill:none;stroke:#00875a;stroke-width:2}.eii-map .path-opt{fill:none;stroke:#6b778c;stroke-width:1.7;stroke-dasharray:7 5}.eii-map .arrow{fill:#00875a}.eii-map .arrow-g{fill:#6b778c}.eii-map .notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;min-width:0;margin-top:10px}.eii-map .note{padding:9px;border:1px solid #dfe1e6;border-radius:6px;color:#42526e;font-size:10px;line-height:1.4}.eii-map .note strong{display:block;color:#172b4d;margin-bottom:2px}
  </style>
  <p class="sub">One internal access context can reference several legal entities; each legal entity can carry country identities, establishments and network addresses. Delegation is an explicit scoped edge.</p>
  <svg viewBox="0 0 1100 640" role="img" aria-label="Two onboarding paths lead to a common identity graph. A direct client enters a workspace directly. An accountant firm reaches the workspace only through a separate delegated authority grant. The workspace references a client legal entity without embedding official identifiers. The French example shows one SIREN and multiple SIRETs. Tax identities, Peppol participant addresses and credentials sit in separate non-overlapping lanes. Every connector uses a dedicated gutter and every action binds actor, authority, client entity, capability, direction and effective time.">
    <text x="32" y="30" class="label">ACCESS PATH</text><text x="350" y="30" class="label">SAGE CONTEXT AND AUTHORITY</text><text x="720" y="30" class="label">LEGAL / COUNTRY / NETWORK IDENTITY</text>
    <rect x="32" y="62" width="238" height="82" rx="10" class="main"/><text x="52" y="92" class="title">Direct client</text><text x="52" y="114" class="copy">Owner/admin acts for own business</text><text x="52" y="132" class="copy">interactive or bounded bulk operations</text>
    <rect x="32" y="194" width="238" height="104" rx="10" class="main"/><text x="52" y="224" class="title">Accountant firm + authorised user</text><text x="52" y="246" class="copy">Portfolio may contain many client SIRENs</text><text x="52" y="266" class="copy">batch is execution mode, not authority</text><text x="52" y="286" class="copy">no implicit access to another client</text>
    <rect x="350" y="62" width="270" height="104" rx="10" class="main"/><text x="370" y="92" class="title">Workspace / access context</text><text x="370" y="114" class="copy">tenantId • datasetId? • product/account</text><text x="370" y="134" class="copy">internal references and permissions</text><text x="370" y="154" class="copy">dataset meaning/cardinality is an open gate</text>
    <rect x="350" y="208" width="270" height="90" rx="10" class="optional"/><text x="370" y="238" class="title">Delegated authority grant</text><text x="370" y="260" class="copy">client • capability • direction • country</text><text x="370" y="280" class="copy">effective interval • evidence • revocation</text>
    <path d="M270 103 H350" class="path"/><polygon points="350,103 340,97 340,109" class="arrow"/>
    <path d="M270 246 H350" class="path-opt"/><polygon points="350,246 340,240 340,252" class="arrow-g"/>
    <path d="M485 208 V166" class="path-opt"/><polygon points="485,166 479,176 491,176" class="arrow-g"/>
    <path d="M620 114 H720" class="path"/><polygon points="720,114 710,108 710,120" class="arrow"/>
    <rect x="720" y="62" width="330" height="104" rx="10" class="main"/><text x="740" y="92" class="title">Client legal entity</text><text x="740" y="114" class="copy">stable Sage entity reference</text><text x="740" y="134" class="copy">country establishment and tax context</text><text x="740" y="154" class="copy">one workspace may reference 1..n by policy</text>
    <path d="M885 166 V206" class="path"/><polygon points="885,206 879,196 891,196" class="arrow"/>
    <rect x="720" y="208" width="330" height="142" rx="10" class="finish"/><text x="740" y="238" class="title">France identity example</text><text x="740" y="262" class="copy">Legal unit — one SIREN (9 digits)</text><text x="740" y="286" class="copy">├─ Head office — SIRET A (SIREN + NIC)</text><text x="740" y="310" class="copy">├─ Establishment — SIRET B</text><text x="740" y="334" class="copy">└─ Establishment — SIRET C</text>
    <rect x="350" y="378" width="270" height="82" rx="10" class="optional"/><text x="370" y="408" class="title">Tax identities</text><text x="370" y="430" class="copy">NIF / VAT / country registration</text><text x="370" y="450" class="copy">scheme + value + country + validity</text>
    <rect x="350" y="492" width="270" height="82" rx="10" class="optional"/><text x="370" y="522" class="title">Peppol participant addresses</text><text x="370" y="544" class="copy">scheme + value • 0..n per entity/context</text><text x="370" y="564" class="copy">discovery identity, not provider company</text>
    <rect x="720" y="408" width="330" height="82" rx="10" class="warn"/><text x="740" y="438" class="title">Credential / certificate reference</text><text x="740" y="460" class="copy">authentication evidence; authority remains separate</text><text x="740" y="480" class="copy">custody • purpose • environment • expiry • rotation</text>
    <path d="M720 134 H680 V419 H620" class="path-opt"/><polygon points="620,419 630,413 630,425" class="arrow-g"/>
    <path d="M680 419 V533 H620" class="path-opt"/><polygon points="620,533 630,527 630,539" class="arrow-g"/>
    <path d="M620 253 H660 V449 H720" class="path-opt"/><polygon points="720,449 710,443 710,455" class="arrow-g"/>
    <rect x="178" y="598" width="744" height="30" rx="15" class="finish"/><text x="274" y="618" class="title">Action context = actor + authority + client entity + identifier + capability + direction + effective time</text>
  </svg>
  <div class="notes"><div class="note"><strong>No identifier stuffing</strong>Internal IDs reference identity records; they do not become part of SIREN, SIRET, NIF or a Peppol address.</div><div class="note"><strong>Authority is narrower than access</strong>A login, API key or certificate never grants portfolio-wide rights by implication.</div><div class="note"><strong>Batch preserves isolation</strong>Every item is authorised, processed, evidenced and failed independently for its client entity.</div></div>
</div>
<!-- confluence-html-macro:end -->

## Actors, objectives and processing differences

| Actor | Need or responsibility |
|---|---|
| Business owner or administrator | Select the correct legal entity/establishment, approve routes and mandates, and understand which compliance outcome needs action. |
| Accountant firm and authorised user | Work across a portfolio without gaining transitive access; act only for approved clients, capabilities, directions and periods. |
| Sage product or API consumer | Submit stable business intent and receive separate document, delivery and reporting outcomes without encoding country identifier rules. |
| Identity/country-policy owner | Maintain official schemes, issuer evidence, validation rules, role eligibility, effective dates and deprecations. |
| Platform service | Bind tenant, legal subject, identity snapshot, authority decision and obligations before external mutation. |
| Provider/network/authority | Validate, route, receive or acknowledge one defined external leg; it is not the owner of the other outcomes by implication. |
| Operations/support | See intended and observed state, evidence freshness, fault domain and safe next action without exposing restricted identifiers. |
| Security/privacy/legal | Approve credential custody, identifier classification, delegated-authority evidence, retention and disclosure. |

| Objective | Evidence of success |
|---|---|
| O1 — Correct subject | Each invoice/action identifies the legally relevant seller, buyer, establishment and taxpayer with scheme-qualified evidence. |
| O2 — Explainable outcomes | Products and operations can distinguish document, delivery and reporting results, including not-applicable and outcome-unknown states. |
| O3 — Safe delegation | Every accountant action is evaluated against a current, client- and capability-specific authority grant. |
| O4 — Reusable contract | France, Spain, Germany, Ireland and UK use the same record and outcome contracts while country packs own legal bindings. |
| O5 — Historical continuity | Identity, mandate, route or policy changes do not corrupt evidence for earlier invoices/actions. |

| Concern | Direct client | Accountant / portfolio |
|---|---|---|
| Authority | Own-business role plus approved product permission | Explicit relationship to each client plus capability-specific representation evidence |
| Cardinality | One or more workspaces/legal entities according to product policy | Many client workspaces/legal entities; no transitive access |
| Processing | Interactive or bounded bulk | Async batch may improve scale, but each item has its own authority decision, context, outcomes and idempotency keys |
| Credential | Client, Sage or provider credential according to approved route | Firm/user credential may authenticate; authority must still be proven per client, branch and operation |
| Visibility | Own invoices, branch outcomes and evidence | Only authorised client, direction, period, operation and disclosure level; portfolio aggregates must not leak item data |
| Revocation | Product role or route change blocks eligible future actions | Revocation can affect one client/capability without invalidating other clients or rewriting prior evidence |

The earlier draft `POST /api/v1/es/onboarding/profile` and `/batch` paths remain scenario sketches only. Endpoint names, asynchronous response behaviour, physical schema and certificate ownership are not approved by this PRD.

## Business scenarios

| ID | Trigger and actor | Expected outcome | Exception or continuity rule |
|---|---|---|---|
| S1 | Direct client sends a domestic invoice | Policy resolves the correct legal subjects, creates one context and activates the required document/delivery/reporting branches | No branch reports success by inheriting another branch's result |
| S2 | Accountant submits for client A | Client A, the accountant user and the submission grant are bound before validation or mutation | Access to client B or retrieval/reporting for client A remains denied unless separately granted |
| S3 | Valid invoice uses a wrong recipient network address | Document outcome can succeed while delivery is blocked/correctable | Correct the route/address without rewriting validated invoice identity unless policy requires regeneration |
| S4 | Recipient delivery succeeds but authority reporting fails | Delivery remains succeeded; reporting becomes action-required or outcome-unknown and is recovered independently | Do not resend the invoice to the buyer solely because reporting failed |
| S5 | Authority accepts a report while recipient delivery is unknown | Reporting evidence is retained; delivery reconciles using its own correlation and operation-safety rule | Do not retract or duplicate authority reporting without a country rule and evidence |
| S6 | Identifier or mandate expires after dispatch | Historical context retains the previously valid evidence | New protected actions after expiry require a current identifier/authority decision; permitted follow-up is country/capability-specific |
| S7 | Accountant submits a mixed-client batch | Each item creates an isolated context and branch outcomes | Partial success is allowed; one client's failure or idempotency key cannot affect another client |
| S8 | Country scheme or directory version changes | New eligible actions use the newly approved version | Earlier invoice contexts retain the original scheme, policy, lookup evidence and route |

## Identifier roles by compliance outcome

The same character sequence can legitimately appear in more than one role. The platform must therefore bind **identifier reference + role + subject + scheme/version**, not copy a bare value into every boundary.

| Outcome or decision | Identifier roles consumed | Questions that must be answered | Evidence retained |
|---|---|---|---|
| Applicability | Seller/buyer legal entity, establishment, jurisdiction, VAT/tax status | Which country policy applies? Is the transaction in scope? Which branches are required? | Policy version, facts used, source identifiers, effective time and decision reasons |
| Document compliance | Supplier/buyer legal/tax IDs, establishment IDs, invoice/self-billing party IDs | Which identity belongs in each semantic/profile field? Is it valid for the issue date and role? | Identifier snapshots, field mapping/profile version, rule results and representation integrity reference |
| Delivery compliance | Sender/recipient participant ID, directory key, routing qualifier, endpoint/capability ID, provider account reference | Is the intended recipient discoverable and capable? Which eligible network/route and provider roles apply? | Lookup source/time, participant scheme/value, route plan, correlations and acknowledgements |
| Reporting compliance | Taxpayer ID, establishment/reporting-unit ID, reporter/delegate ID, authority account/registration ID | Who is legally obliged to report? Who may submit? Which authority destination/schema/deadline applies? | Authority decision, reporter identity, mandate evidence, payload/schema reference, correlation and acknowledgement |
| Support/reconciliation | Sage context IDs plus redacted external references | Can support correlate all legs without exposing unnecessary official identifiers or secrets? | Redacted diagnostic view, audit actor, fault domain, safe-next-action decision |

### Important asymmetries

- A document can be valid without a discoverable recipient route.
- A route can resolve while the invoice remains semantically invalid and therefore must not be dispatched.
- Reporting may be not applicable, synchronous, asynchronous, periodic or triggered by a later event; country policy owns that decision.
- A network acknowledgement proves only what the network/provider defines, not buyer commercial acceptance or tax acceptance.
- An accountant may be allowed to create or submit an invoice but not retrieve inbound invoices, report payment, correct, cancel or see restricted evidence.
- An outbound participant address does not automatically establish an inbound address, supported profile or active capability.

## Official identifier comparison

| Country | Legal/business identity | Establishment or unit identity | Tax/invoice identity | Delivery/network identity | Compliance-delivery consequence | Evidence confidence |
|---|---|---|---|---|---|---|
| France | SIREN: 9 digits for the legal unit | SIRET: 14 digits; SIREN + five-digit NIC for each establishment | VAT ID: `FR` + two-digit key + SIREN | French directory can use SIREN or SIRET plus a routing code. Peppol v9.7 includes `0002` FR:SIRENE and `0009` FR:SIRET | Document, directory and Peppol values may share a SIREN/SIRET value but must retain distinct scheme/role and routing evidence | Confirmed hierarchy and current official directory guidance; detailed field/route implementation remains country-owned |
| Spain | NIF for legal persons/entities; normally invariant unless legal form or nationality changes | No universal SIRET-equivalent e-invoice establishment hierarchy is confirmed by the reviewed evidence | Public B2B solution requires issuer and recipient NIF; the invoice unique code includes issuer NIF, series/number and issue date. NIF-IVA serves relevant intra-EU use | Peppol `9920` ES:VAT exists, but Spain's statutory public/private interconnection model must not be assumed to use Peppol universally | NIF is confirmed for document/public-solution identity; platform destination, provider interconnection and reporter authority remain separate bindings | NIF and Royal Decree confirmed; final technical-order details and operation-specific authority remain gates |
| Germany | W-IdNr: `DE` + nine digits, being rolled out as a nationwide business identifier | W-IdNr adds a five-digit distinguishing feature for activities, businesses or establishments, for example `-00001` | Supplier Steuernummer or USt-IdNr is required in the structured invoice; W-IdNr does not currently replace them | B2B does not require Leitweg-ID. B2G can use `0204:Leitweg-ID`; private Peppol participants may use `9930:VAT` or `0088:GLN` | W-IdNr and USt-IdNr may share the base pattern but remain different schemes. Leitweg-ID must never leak into a universal B2B rule | Current BMF and federal Peppol guidance confirmed; W-IdNr rollout and future uses require versioning |
| Ireland | CRO number identifies incorporated companies, not every economic actor | No general establishment identity for the future B2B route is confirmed | Revenue issues a Tax Reference Number; VAT invoices use the supplier registration number. A sole trader's TRN can equal the PPSN after tax registration | Ireland uses Peppol for B2G; `9935` IE:VAT is active. Future domestic B2B participant/routing detail remains open | CRO, TRN and VAT values cover different subjects/purposes. PPSN-derived values require restricted-data treatment | Current Revenue/CRO/B2G evidence confirmed; future B2B technical contract remains a gate |
| UK | Companies House CRN identifies registered companies, generally eight digits or two letters plus six characters; it does not cover all businesses | No universal establishment identifier is confirmed | UTR is a ten-digit tax-administration identifier; VAT registration number is nine digits and required on VAT invoices | Peppol `9932` GB:VAT is active, but final UK mandate participant/profile rules remain open | CRN, UTR and VAT number cannot be collapsed. UTR must not become a public routing key | Current HMRC/Peppol facts confirmed; future UK e-invoice implementation detail remains open |

Sources: [French SIREN/SIRET and VAT guidance](https://www.impots.gouv.fr/professionnel/les-numeros-didentification), [French directory guidance](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiches_reforme/fiche-1_f_v.pdf), [AEAT NIF guidance](https://sede.agenciatributaria.gob.es/Sede/censos-nif-domicilio-fiscal/solicitar-nif/nif-juridica.html), [Spain Royal Decree 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238), [German W-IdNr guidance](https://www.bundesfinanzministerium.de/Content/DE/FAQ/wirtschafts-identifikationsnummer.html), [German e-invoice FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html), [German federal Peppol guidance](https://e-rechnung-bund.de/en/faq/what-is-the-peppol-participant-id-and-how-can-it-be-requested/), [Irish Revenue TRN guidance](https://www.revenue.ie/en/starting-a-business/registering-for-tax/tax-reference-number.aspx), [Irish VAT invoice requirements](https://www.revenue.ie/en/vat/vat-records-invoices-credit-notes/invoices/information-required-vat-invoice.aspx), [Irish Peppol Authority](https://www.gov.ie/en/office-of-government-procurement/publications/irish-peppol-authority/), [UK VAT registration](https://www.gov.uk/register-for-vat/how-register-for-vat), [UK UTR guidance](https://www.gov.uk/find-utr-number), and [OpenPeppol Participant Identifier Schemes v9.7](https://docs.peppol.eu/edelivery/codelists/v9.7/Peppol%20Code%20Lists%20-%20Participant%20identifier%20schemes%20v9.7.html), accessed 2026-08-18.

The OpenPeppol list is dynamic. Store the scheme/version or verification time and support deprecation without reinterpreting historical participant addresses.

## Reusable conceptual records and fields

These are conceptual fields, not an approved physical schema. Country-named columns such as `siren`, `nif`, `utr` or `croNumber` should not be added to a shared tenant record.

| Record | Reusable fields | Country-owned content or rule |
|---|---|---|
| AccessContext | `contextId`, `tenantId`, `datasetId`, `productId`, `environment`, `legalEntityRefs`, validity | Product meaning/cardinality of tenant and dataset; who may attach legal entities |
| LegalEntity | `legalEntityId`, legal name, legal form, incorporation/subject jurisdiction, status, validity, predecessor/successor references | Which registry/identity proves existence; merger, legal-form and cessation effects |
| Establishment | `establishmentId`, `parentLegalEntityId`, establishment type, address, jurisdiction, official identifier references, validity | Whether a formal establishment identifier exists and when the establishment controls applicability/reporting |
| ExternalIdentifier | `identifierId`, `scheme`, raw value, normalized value, issuing country, issuing authority, subject type/reference, permitted roles, validity, status, verification source/time, sensitivity classification | Format/check digits, normalization, issuer, role eligibility, verification method, deprecation and masking |
| NetworkAddress | `addressId`, network, participant scheme/value, direction, document profiles/capabilities, directory/endpoint reference, provider/access-point role, validity, discovery source/time | Eligible schemes, registration/discovery rules, routing priority, capability lookup and acknowledgement meaning |
| DelegatedAuthorityGrant | `grantId`, principal entity, delegate organisation/user, capability, direction, country, network/route scope, validity, evidence reference, verification status, revocation reason/time | Legally accepted mandate/agent mechanism, sub-delegation, proof format and operation scope |
| CredentialReference | `credentialRef`, owner, custodian, purpose, provider/network, environment, validity, rotation/status, secret-store reference | Accepted certificate/credential, trust chain, legal use and custody model |
| ComplianceContext | `complianceContextId`, invoice/action ID, actor, legal subjects, identifier snapshot references, authority decision, policy/obligation versions, direction, effective time, idempotency identity, provenance | Facts required by applicability and when the context becomes immutable |
| ComplianceOutcome | outcome type, applicability, state, correlation/idempotency, request/representation reference, observed external result, evidence times, failure classification, safe next action | Country/provider status mapping, acknowledgement semantics, deadlines and recovery rules |

### Identifier normalization and uniqueness

- Preserve the received/display value and a separately normalized comparison value; never discard legally meaningful formatting or prefixes.
- Uniqueness is at least `scheme + normalized value + issuing authority/country + subject level`; a bare value is never a global key.
- Treat aliases and derivations as explicit relationships. For example, a French VAT number is derived partly from SIREN, but is not the SIREN record.
- A single value registered under different Peppol schemes remains distinct unless an approved reconciliation rule links it.
- Validation by length or regular expression is insufficient where an official registry/check service exists; record evidence source and time.
- Do not place secrets, private keys or unredacted restricted identifiers into logs, URLs, metrics labels or customer-safe error text.

## Delegated accountants and authority

The shared rule is: **authentication identifies the caller; delegated authority determines whether that caller may perform this operation for this client at this time**.

### Authority decision inputs

| Dimension | Required question |
|---|---|
| Principal | Which exact client legal entity or establishment bears the obligation? |
| Delegate | Which accountant firm and which authorised user/service is acting? |
| Capability | Onboard, maintain identity, issue, submit, retrieve, view, correct, cancel, report payment/status, reconcile or administer? |
| Outcome branch | Does the grant cover document creation/validation, recipient delivery, authority reporting, or evidence access? |
| Direction and document | Outbound/inbound; invoice, credit note, correction, status/payment report or another supported type? |
| Jurisdiction and route | Which country, authority, network/provider and environment are in scope? |
| Time | Is the grant active at decision time and, where required, at transaction/document/reporting time? |
| Evidence | What mandate/agent-link/power proves the grant, who verified it, and can it be disclosed? |
| Revocation/sub-delegation | Has it been revoked, replaced or narrowed? May firm users or service accounts act under it? |

### Country authority evidence

| Country | Confirmed authority pattern | Do not infer | Required follow-up |
|---|---|---|---|
| France | A business may use an explicit mandate when delegating relevant electronic-invoicing/platform actions | Selecting an accountant or platform grants every invoice, reporting and evidence capability | Confirm mandate fields, platform registration effect, revocation and per-operation scope |
| Spain | AEAT powers/social-collaboration arrangements are procedure-bounded; RD 238/2026 also permits specified recipient authorisation to a private platform for payment communication | VERI*FACTU authority, tax social collaboration and B2B invoice-platform authority are one universal grant | Obtain legal matrix for issue, submit, receive, status/payment report, correction and consultation |
| Germany | The Vollmachtsdatenbank can transmit official tax powers and allows limitations; tax numbers and data-access scopes matter | A tax-adviser power automatically authorises every e-invoice delivery/network action | Separate tax-representation evidence from customer-authorised invoice exchange and Peppol/provider permissions |
| Ireland | Revenue uses an explicit agent-client linking/approval process | A ROS agent link is automatically the future B2B e-invoice mandate | Confirm tax-head/service scope and future domestic e-invoice delegation design |
| UK | HMRC authorisation varies by tax service and mechanism; limited authorisation may permit one service/action only | One digital handshake, Agent Services Account or form authorises all tax and e-invoice actions | Confirm future UK e-invoice mandate, service scopes and evidence/revocation interfaces |

Sources: [France reform guidance](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiches_reforme/fiche-1_f_v.pdf), [Spain RD 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238), [AEAT VERI*FACTU delegation FAQ](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/cuestiones-generales-cumplimiento-delegacion.html), [German ELSTER Vollmachtsdatenbank](https://www.elster.de/elsterweb/infoseite/vollmachtsdatenbank), [Irish Revenue agent linking](https://www.revenue.ie/en/jobs-and-pensions/tax-agent-tax-service/inform-revenue-agent.aspx), and [UK HMRC agent authorisation](https://www.gov.uk/guidance/how-to-get-authorised-to-act-as-a-tax-agent-on-behalf-of-your-clients), accessed 2026-08-18.

## Scope and non-goals

### In scope for discovery

- Shared identity, establishment, network-address, authority and credential concepts.
- Identifier roles across applicability, document, delivery and reporting decisions.
- France, Spain, Germany, Ireland and UK evidence catalog at discovery depth.
- Direct-client and delegated-accountant actions, including batch isolation.
- Immutable compliance context and independent outcome/evidence contract.
- Lifecycle, failure, security, privacy, operations, reuse assessment and country decision gates.

### Non-goals

- Approving a database schema, endpoint names, provider, network or credential-custody design.
- Declaring every Peppol identifier to be an approved production address in a country.
- Treating tax-agent authority as e-invoicing authority without country confirmation.
- Defining all invoice-profile field mappings or authority payload schemas before official technical artefacts exist.
- Migrating or publishing production identity data.
- Setting unsupported latency, volume, retention, availability or code-reuse targets.
- Publishing this revision to Confluence without explicit approval.

## Business rules

| ID | Condition | Rule | Evidence/status |
|---|---|---|---|
| BR1 | Any external identifier is stored or used | Store scheme, value, issuer country/authority, subject level, permitted role, validity and verification evidence; never infer type from length alone | Confirmed product principle |
| BR2 | Product context is linked to compliance identity | `tenantId` and `datasetId` remain internal access/context identifiers and reference versioned legal subjects/identities | Proposed; product cardinality is open |
| BR3 | French legal identity is represented | One legal unit has one SIREN and may have many establishment SIRETs | Confirmed official evidence |
| BR4 | A national value is used as a Peppol/directory address | Preserve the participant/directory scheme and role separately from the legal/tax identity record | Confirmed network-model principle |
| BR5 | Country policy evaluates an invoice/action | It declares document, delivery and reporting obligations independently as required, not applicable, unsupported or unknown | Confirmed parent-PRD principle |
| BR6 | An outcome branch succeeds | Success applies only to that branch and its defined acknowledgement semantics | Confirmed product decision |
| BR7 | An aggregate compliance summary is shown | Derive it from required branch outcomes; never use it as the only source state | Proposed product behaviour |
| BR8 | A delegate acts for a client | Evaluate principal, delegate, capability, branch, direction, jurisdiction, route, validity, evidence and revocation before protected access/mutation | Confirmed product/security principle |
| BR9 | A credential authenticates a caller/service | Credential possession proves authentication only; execution still needs valid identity, policy and authority decisions | Confirmed security principle |
| BR10 | An accountant submits or views a batch | Authorise and isolate every item; batch acceptance is not item success | Confirmed product principle |
| BR11 | Identity, mandate, route or policy changes after external mutation | Apply current changes only to eligible future actions and retain the historical context/outcomes | Confirmed continuity principle |
| BR12 | A scheme, identifier or address expires/is deprecated | Block ineligible new use, retain history and require explicit replacement/reverification rather than silent conversion | Proposed lifecycle requirement |
| BR13 | Reporting is not required by applicable policy | Record reporting as `NOT_APPLICABLE` with policy evidence, not `SUCCEEDED` or omitted | Proposed outcome contract |
| BR14 | External mutation has an ambiguous result | Enter outcome-unknown and reconcile before resubmission unless end-to-end idempotency proves safety | Confirmed resilience principle |

## Proposed context and outcome lifecycle

### Compliance-context lifecycle

| Stage | Behaviour |
|---|---|
| Draft | Resolve current master data, policy and authority without external mutation; corrections may replace the draft decision. |
| Bound | Freeze selected legal subjects, identifier snapshots, authority decision, policy/obligation versions and idempotency identity for the planned action. |
| Executing | One or more required branches may mutate external systems; context is immutable except append-only evidence and outcome events. |
| Closed | All required branches reached terminal, explicitly waived or accepted exception states under policy; history remains queryable. |
| Historical | Current configuration may differ, but retrieval/follow-up uses the original context and country-approved continuity rules. |

### Independent branch states

State names are proposed; behavioural distinctions are required.

| State | Meaning | Safe next action |
|---|---|---|
| `NOT_APPLICABLE` | Policy confirms the branch is not required | Retain policy evidence; no execution |
| `PENDING` | Required branch is planned or awaiting execution/result | Execute or poll according to operation safety |
| `SUCCEEDED` | Defined branch outcome and evidence are complete | No mutation; continue other required branches |
| `CORRECTION_REQUIRED` | Customer/product-correctable identity, document or route issue | Correct eligible data, re-evaluate and create a new representation/attempt as policy permits |
| `FAILED` | Terminal failure under current plan | Escalate or create an approved alternative plan; never relabel as success |
| `OUTCOME_UNKNOWN` | External mutation may have succeeded but evidence is inconclusive | Reconcile by correlation/query before resend |
| `SUSPENDED` | Execution is blocked by revoked authority/credential, security control or kill switch | Restore/replace evidence and re-authorise before new mutation |

### Derived summary

The aggregate may show `IN_PROGRESS`, `ACTION_REQUIRED`, `RECONCILIATION_REQUIRED` or `COMPLETE`. `COMPLETE` requires every policy-required branch to be `SUCCEEDED` or an explicitly approved terminal exception; a not-applicable branch contributes evidence but no success. The aggregate does not replace invoice business status, payment status or the branch events.

## End-to-end journeys

### J1 — Configure identity and delegation without activation

1. Product/admin selects a workspace and proposed legal entity.
2. Platform creates or links legal entity, establishment and scheme-qualified identifier records.
3. Country catalog validates format and, where available, verifies against an approved source.
4. Admin/accountant relationship creates a proposed authority grant with evidence and explicit capabilities.
5. Security/provider credentials are referenced separately.
6. Readiness reports verified, missing, expired, unsupported and open-policy items without creating a route or mutating an external system.

Expected result: identity readiness is explainable; no route, participant registration or compliance success is implied.

### J2 — Primary outbound compliance delivery

1. Product submits invoice intent, tenant, actor and idempotency identity.
2. Platform resolves seller, buyer and relevant establishments and evaluates effective country policy.
3. If delegated, platform verifies the exact client/capability/direction/branch grant.
4. Platform binds one compliance context and activates required branches.
5. Document branch maps identifiers into the selected representation and validates it.
6. Delivery branch resolves participant/directory identity, binds network/provider/adapter and dispatches only after document readiness.
7. Reporting branch submits independently when policy requires it; sequencing may differ by country.
8. Product receives three outcome views plus a derived summary and customer-safe actions.

Expected result: each outcome has separate correlation and evidence; success is not inherited.

### J3 — Correctable identity or document failure

1. Validation identifies a missing/invalid identifier role or profile field before dispatch.
2. Product receives stable rule, subject, scheme/field, policy/profile version and correction guidance.
3. Authorised user corrects current master data or invoice intent.
4. Platform re-evaluates and creates a new bound context/representation where required; the failed attempt remains auditable.

Expected result: no external dispatch occurred before a compliant representation was available.

### J4 — Delivery unknown after reporting success

1. Recipient dispatch times out after transmission and becomes `OUTCOME_UNKNOWN`.
2. Independently required authority reporting succeeds and retains its acknowledgement.
3. Platform queries/reconciles the delivery correlation before any resend.
4. Delivery becomes succeeded if evidence is found, or an authorised safe retry creates a new attempt linked to the original.

Expected result: reporting is not duplicated and buyer delivery is not falsely marked successful.

### J5 — Mandate revoked after invoice issue

1. Client revokes the accountant's reporting and retrieval capabilities.
2. New protected actions are denied immediately after the effective revocation time.
3. Previously executed context retains the historical grant evidence and audit actor.
4. Policy determines whether Sage/client operations may complete reconciliation without the revoked delegate.

Expected result: revocation is prospective and scoped; historical evidence remains explainable.

### J6 — Mixed-client batch

1. Accountant submits items for clients A, B and C.
2. Every item resolves its client, grant, policy and idempotency namespace independently.
3. Client A succeeds; B requires correction; C is denied before protected processing.
4. Batch view reports per-item outcomes using masked identifiers and no cross-client data leakage.

Expected result: partial success is safe and no item inherits another client's authority or result.

## Functional requirements

### Identity and tenancy

| ID | Requirement |
|---|---|
| ID-FR1 | Before external mutation or protected retrieval, the platform must resolve `tenant/access context → Sage legal entity → applicable establishment → scheme-qualified identifiers` and record the resolution evidence. |
| ID-FR2 | The platform must support one legal entity to many establishments and many identifiers/network addresses with effective dates, explicit roles and no silent overwrite. |
| ID-FR3 | Identifier uniqueness and lookup must include scheme, normalized value, issuer country/authority and subject level; a bare value must not be a global key. |
| ID-FR4 | The platform must retain raw/display and normalized identifier values plus verification/deprecation evidence without placing restricted values in logs or metrics labels. |
| ID-FR5 | A country catalog must declare each scheme's issuer, subject level, format/check rules, allowed roles, verification method, sensitivity, validity and deprecation state. |

### Policy and compliance context

| ID | Requirement |
|---|---|
| ID-FR6 | Country policy must evaluate applicability and independently declare document, delivery and reporting branches as required, not applicable, unsupported or unknown. |
| ID-FR7 | Before the first external mutation, the platform must bind an immutable compliance context containing actor, subjects, identifier snapshots, authority decision, credential reference, policy/obligation versions, direction, effective time, provenance and idempotency identity. |
| ID-FR8 | Current identity, route, authority or policy changes must not mutate a bound historical context; eligible follow-up must retain or explicitly link to the original context. |

### Delegated authority

| ID | Requirement |
|---|---|
| ID-FR9 | Every delegated operation must evaluate principal, delegate organisation/user, capability, outcome branch, direction/document, country/route, effective interval, evidence and revocation. |
| ID-FR10 | Submission, retrieval, correction, cancellation, payment/status reporting, onboarding, evidence access and administration must be separately authorisable. |
| ID-FR11 | Revocation/expiry must block newly initiated protected operations at its effective time without erasing historical authority evidence. |
| ID-FR12 | Batch processing must authorise and isolate every item, support partial success and prevent cross-client idempotency, data and correlation collisions. |

### Document, delivery and reporting outcomes

| ID | Requirement |
|---|---|
| ID-FR13 | Document compliance must record selected party/establishment/tax identifiers, representation/profile/mapping versions, validation results and integrity reference before dispatch. |
| ID-FR14 | Delivery compliance must record intended recipient, participant/directory scheme/value, lookup evidence, network/channel, provider roles, route, correlation and acknowledgement semantics separately from document/reporting state. |
| ID-FR15 | Reporting compliance must create one independent leg per required authority obligation with taxpayer/reporter/delegate identity, schema/version, deadline, correlation, acknowledgement and recovery state. |
| ID-FR16 | A branch marked not applicable must retain the policy/version and reason; absence of a row or event must not mean not applicable. |
| ID-FR17 | A derived summary must be computed from required branch states and must expose which branch blocks completion; it must not overwrite branch events. |
| ID-FR18 | A timeout after possible mutation must enter outcome-unknown and reconcile before resend unless the end-to-end operation is proven idempotent. |

### Product and operations experience

| ID | Requirement |
|---|---|
| ID-FR19 | Product/API responses must expose separate document, delivery and reporting outcomes, applied policy/version, customer-safe reasons and allowed next actions. |
| ID-FR20 | Operations must see intended versus observed state, evidence freshness, fault domain and safe actions for each branch without direct database correction. |
| ID-FR21 | Support views and exports must mask or omit restricted identifiers and authority evidence according to actor, purpose and jurisdiction. |
| ID-FR22 | Scheme, directory, mandate and policy versions must be observable so deprecation/migration can be planned without reinterpreting historical invoices. |

## Failure and recovery matrix

| Failure | Affected outcome | Required behaviour | Prohibited behaviour |
|---|---|---|---|
| Unknown/invalid legal or tax identity | Applicability/document/reporting | Block affected branch, identify subject/scheme and correction owner | Guess identifier type or merge by value |
| Valid identifier in wrong role | Any | Reject role binding with explainable rule | Reuse VAT/registry/network value merely because strings match |
| Recipient address not found | Delivery | Return distinct discovery/readiness result; preserve valid document outcome | Claim document failure or invent email/PDF fallback |
| Profile validation fails | Document | No dispatch; return stable rule/field/version guidance | Mark delivery/reporting pending as if mutation occurred |
| Delegate lacks one capability | Requested branch | Deny that operation with audit; preserve unrelated valid grants | Deny all clients/capabilities or widen permission automatically |
| Grant revoked during batch | Per item/branch | Evaluate at each item's protected decision point; stop newly unauthorised work | Treat batch acceptance time as permanent authority |
| Provider timeout after send | Delivery/reporting leg | Mark that leg outcome-unknown and reconcile by correlation | Blind resend or change other successful legs |
| Authority rejects report after buyer delivery | Reporting | Preserve delivery success; correct/retry reporting under country rule | Resend invoice to buyer solely due to report rejection |
| Internal persistence fails after external success | Affected leg | Recover external evidence and append durable outcome before new mutation | Repeat external call without reconciliation |
| Duplicate/out-of-order acknowledgement | Affected leg | Deduplicate by source identity; retain raw evidence and deterministic derived view | Drop contradictory evidence or regress terminal state silently |
| Scheme/director/registry data changes | Future contexts | Reverify/replace current record; link predecessor/successor | Rewrite historical snapshot |
| Restricted identifier appears in diagnostic path | Security/privacy | Redact, alert and correct telemetry/control | Persist it in logs, URLs or metrics labels |

## Non-functional requirements

| ID | Requirement |
|---|---|
| ID-NFR1 | Tenant, legal entity, delegate client, country and environment boundaries must be enforced for identities, grants, credentials, contexts, outcomes and diagnostics. |
| ID-NFR2 | Secrets/private keys must remain in approved custody with rotation and environment isolation and must never be stored as identifier or mandate evidence. |
| ID-NFR3 | Official identifiers and authority evidence must be classified, minimised, masked and retained/deleted under approved country, legal, privacy and security rules. |
| ID-NFR4 | Every policy, identity, authority and external-mutation decision must have immutable actor/source/time, version, correlation and result evidence. |
| ID-NFR5 | Outcome processing must be idempotent or explicitly outcome-unknown/reconcilable; operation safety must be documented per provider/authority. |
| ID-NFR6 | Observability must distinguish product/customer data, identity/catalog, authority, policy, document, directory/route, provider/network and authority-reporting faults. |
| ID-NFR7 | Availability, lookup latency, batch throughput, payload, backlog and evidence-freshness targets require baselines and owners before delivery commitment. |
| ID-NFR8 | Customer-facing explanations must be accessible, localisable and safe to disclose without exposing another client, restricted identifier or confidential mandate. |

## Acceptance criteria

| ID | Given / when / then |
|---|---|
| ID-AC1 | Given one French SIREN with three active establishments, when identity is resolved, then all three SIRETs remain distinct, traceable to the legal unit and eligible only for their approved roles. |
| ID-AC2 | Given an accountant may submit for client A but may not retrieve for A or access client B, when all actions are attempted, then only A's submission proceeds and both denials identify the missing capability/client link with audit. |
| ID-AC3 | Given the same normalized value appears under two schemes or countries, when stored and resolved, then no automatic identity merge occurs. |
| ID-AC4 | Given a document is valid but the recipient is undiscoverable, when status is queried, then document is succeeded, delivery is correction-required and reporting retains its independently applicable state. |
| ID-AC5 | Given recipient delivery succeeds and authority reporting rejects, when status/retry is requested, then delivery remains succeeded and only reporting is corrected/retried. |
| ID-AC6 | Given reporting is not required by the effective country policy, when the context is created, then reporting is not-applicable with policy evidence rather than succeeded or absent. |
| ID-AC7 | Given a network send times out after possible transmission, when retry logic runs, then delivery is outcome-unknown and no resend occurs before reconciliation proves it safe. |
| ID-AC8 | Given a mandate is revoked after an invoice was sent, when historical evidence and a new reporting action are requested, then the old context retains the grant snapshot while the unauthorised new action is denied. |
| ID-AC9 | Given a mixed-client batch, when one client succeeds, one needs correction and one lacks authority, then per-item outcomes remain isolated and no client data appears in another item's response. |
| ID-AC10 | Given an identifier/directory scheme version is deprecated, when a new invoice and a historical invoice are viewed, then new ineligible use is blocked/replaced while the historical scheme/version remains intact. |
| ID-AC11 | Given restricted Irish sole-trader or UK tax identifiers, when operations/support views are used, then only authorised roles see permitted masked/full values and logs/metrics contain none. |
| ID-AC12 | Given three required branches have succeeded, when the aggregate is derived, then it is complete; if any required branch later receives contradictory evidence, the branch and summary expose reconciliation without deleting prior evidence. |

## Reuse assessment

This is a product-model estimate, not an implementation/code-reuse measurement. The denominator is 24 named capability slices reviewed in this PRD.

| Classification | Capability slices | Percentage | Included slices |
|---|---:|---:|---|
| Reusable unchanged core | 14 of 24 | 58% | Context separation, legal-entity graph, scheme-qualified storage, validity/versioning, evidence verification, sensitivity, network-address record, authority-grant model, credential separation, per-operation authorisation, batch isolation, outcome separation, audit and historical continuity |
| Reusable via country configuration | 6 of 24 | 25% | Identifier catalog, format/check validation, subject/cardinality binding, participant-scheme eligibility, directory resolution and invoice/report field mapping |
| Country-specific implementation | 4 of 24 | 17% | Legal applicability, official registry/onboarding integration, legally accepted delegated-authority evidence, and statutory delivery/reporting topology/lifecycle |
| Total reusable platform surface | 20 of 24 | **83%** | Shared core plus governed country configuration |

The 83% figure is a discovery hypothesis for reusable **design surface**. It must not be presented as proof that 83% of France/Spain code exists, is production-ready or can be reused unchanged. Architecture must inventory real services, rules, tests, operations and technical debt before setting a delivery target.

## Metrics

| Metric | Why it matters | Baseline/target status | Owner |
|---|---|---|---|
| Contexts with verified required identifier roles before mutation | Measures identity completeness | Baseline required; target not approved | Identity/platform product |
| Branch outcomes with policy, correlation and evidence completeness | Tests explainability and auditability | Baseline required | Platform operations |
| Cross-client authority denials and leakage incidents | Tests portfolio isolation | Security target must be approved; leakage tolerance expected to be zero but not formally set here | Security/product |
| Correctable identifier/document failure rate by country/rule | Identifies onboarding/data-quality friction | Baseline required | Country/product |
| Delivery/reporting outcome-unknown age and reconciliation completion | Tests safe recovery | Baseline and operational thresholds required | Operations |
| Identifier/directory verification freshness | Detects stale routing or legal identity | Country/provider freshness rules required | Identity/country owner |
| New-country capability reuse classification | Validates the 83% design hypothesis | Measure first reference pack against the 24-slice inventory | Architecture/platform product |

## Risks and mitigations

| Risk | Consequence | Mitigation/gate |
|---|---|---|
| One “compliant” status collapses three outcomes | False customer assurance and unsafe retry | Independent branch states/events plus derived-only summary |
| Bare identifier values are reused across roles | Misdelivery, false taxpayer association or audit failure | Scheme/subject/role-qualified records and country catalog |
| Tax-agent evidence is treated as invoice authority | Unauthorised submission/retrieval/reporting | Per-country/per-capability mandate matrix and runtime decision |
| France/Peppol design leaks into other countries | Country forks and incorrect routing | Germany/Ireland/UK counter-examples and country-owned bindings |
| Restricted identifiers leak through telemetry/support | Privacy/security incident | Classification, masking, purpose-based views and telemetry tests |
| Dynamic scheme/directory data becomes stale | Delivery failure or wrong recipient | Version/freshness evidence, reverification and deprecation workflow |
| Aggregate retry duplicates a successful branch | Duplicate invoice or report | Per-leg idempotency/correlation and outcome-unknown reconciliation |
| Reuse percentage becomes a delivery commitment | Underestimated country work | Keep design estimate labelled; require implementation inventory |

## Evidence register

| ID | Source | Finding | Confidence/limitation | Requirement impact |
|---|---|---|---|---|
| E1 | [French SIREN/SIRET guidance](https://entreprendre.service-public.gouv.fr/vosdroits/F32135) and [tax identifier guidance](https://www.impots.gouv.fr/professionnel/les-numeros-didentification) | SIREN identifies legal unit; SIRET identifies establishment; VAT number has a separate tax role | Confirmed official evidence | BR1–BR4; ID-FR1–5; ID-AC1 |
| E2 | [French e-invoice directory/reform guidance](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiches_reforme/fiche-1_f_v.pdf) | Directory and routing use SIREN/SIRET and routing information; explicit mandate is relevant when activity is delegated | Official, but detailed production specifications/versioning still require country ownership | ID-FR14; ID-FR9–12 |
| E3 | [AEAT NIF guidance](https://sede.agenciatributaria.gob.es/Sede/censos-nif-domicilio-fiscal/solicitar-nif/nif-juridica.html) and [RD 238/2026](https://www.boe.es/eli/es/rd/2026/03/25/238) | NIF identifies issuer/recipient in Spain public B2B solution; invoice unique code includes issuer NIF; public/private delivery and reporting are distinct | Confirmed primary/official evidence; technical order remains a gate | Compliance-branch separation and Spain catalog |
| E4 | [AEAT delegation FAQ](https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/cuestiones-generales-cumplimiento-delegacion.html) and [social collaboration FAQ](https://sede.agenciatributaria.gob.es/Sede/colaborar-agencia-tributaria/colaboracion-social-presentacion-declaraciones/preguntas-frecuentes-sobre-colaboracion-social.html) | Representation is procedure-bounded and does not confer universal rights | Official but VERI*FACTU/tax-procedure-specific | BR8–BR9; country authority gate |
| E5 | [German W-IdNr FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/wirtschafts-identifikationsnummer.html), [e-invoice FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) and [federal Peppol guidance](https://e-rechnung-bund.de/en/faq/what-is-the-peppol-participant-id-and-how-can-it-be-requested/) | W-IdNr, USt-IdNr/Steuernummer and Leitweg/Peppol identities have different roles; Leitweg-ID is B2G, not B2B | Confirmed current guidance; rollout/future uses are version-sensitive | Prevents universal identifier and route assumptions |
| E6 | [ELSTER Vollmachtsdatenbank](https://www.elster.de/elsterweb/infoseite/vollmachtsdatenbank) | German tax powers can be electronically transmitted and scoped | Official tax context, not proof of e-invoice network authority | Country authority separation |
| E7 | [Irish TRN](https://www.revenue.ie/en/starting-a-business/registering-for-tax/tax-reference-number.aspx), [VAT invoice](https://www.revenue.ie/en/vat/vat-records-invoices-credit-notes/invoices/information-required-vat-invoice.aspx), [agent link](https://www.revenue.ie/en/jobs-and-pensions/tax-agent-tax-service/inform-revenue-agent.aspx) and [Peppol Authority](https://www.gov.ie/en/office-of-government-procurement/publications/irish-peppol-authority/) | Legal/company, tax, agent and network identities are distinct; sole-trader TRN may derive from PPSN | Official current sources; future B2B route remains open | Privacy classification and Ireland gates |
| E8 | [UK VAT registration](https://www.gov.uk/register-for-vat/how-register-for-vat), [UTR](https://www.gov.uk/find-utr-number) and [agent authorisation](https://www.gov.uk/guidance/how-to-get-authorised-to-act-as-a-tax-agent-on-behalf-of-your-clients) | Company, UTR, VAT and agent-service identities/permissions are separate | Official current sources; future e-invoice implementation remains open | Privacy, identifier and authority separation |
| E9 | [OpenPeppol Participant Identifier Schemes v9.7](https://docs.peppol.eu/edelivery/codelists/v9.7/Peppol%20Code%20Lists%20-%20Participant%20identifier%20schemes%20v9.7.html) | Active scheme list includes relevant FR/ES/DE/IE/GB schemes and is versioned/dynamic | Official network source; presence does not mean country production approval | Scheme/version/deprecation requirements |
| E10 | [Accountant & Single Client — Domain Services Team](https://confluence.sage.com/spaces/DNBU/pages/848078252/Accountant+Single+Client) | Proposes direct/batch paths, asymmetric send/retrieve authority and client isolation | Internal discovery input; endpoint/certificate/SPFE assumptions unapproved | Batch and authority scenarios |

## Open questions and delivery gates

| Question | Why it matters | Decision owner | Blocks | Current hypothesis |
|---|---|---|---|---|
| What does `datasetId` represent and can one dataset contain several legal entities/establishments? | Determines tenancy and identity cardinality | Product/domain architecture | Approved conceptual model and API | Keep dataset as internal context until decided |
| Which facts make each country policy applicable? | Selects legal subject, establishment and branches | Country legal/compliance | Production scope | Country pack owns effective-dated applicability |
| Which identifier is required for each semantic/profile/directory/report field? | Prevents correct value in wrong role | Country product/technical owner | Country implementation | Use role-qualified mapping, never bare aliases |
| What official verification sources and freshness rules are available? | Determines identity trust and stale-route risk | Identity/country owner | Production onboarding | Format-only validation is insufficient where registry checks exist |
| Which accountant capabilities are legally delegable and how is evidence revoked? | Controls portfolio access and mutations | Country legal/security/product | Delegated launch | Grants are client/capability/branch specific |
| Who owns credential/certificate custody per provider/authority? | Authentication, rotation and support boundary | Security/architecture/operations | External integration | Credentials remain separate references |
| What are acknowledgement semantics and operation-safety rules per leg? | Determines success and retry | Provider/authority integration owner | Production resilience | No success without defined evidence; unknown reconciles first |
| What retention/masking rules apply to official IDs and mandates? | Privacy, tax evidence and support | Legal/privacy/security | Production data handling | Classify per scheme/evidence, not one universal period |
| Which real services/code are reusable against the 24 slices? | Converts design estimate into delivery evidence | Architecture/current France/Spain teams | Delivery estimate | 83% remains a hypothesis until inventory/tests |

## Decisions

| Decision | Status |
|---|---|
| Separate access context, legal entity, establishment, tax identity, network address, delegated authority and credential | Confirmed product direction |
| Use one immutable compliance context and three independent outcome branches | Confirmed by parent PRD and this detailed review |
| Treat compliance delivery as orchestration, not a fourth outcome | Confirmed clarification from user review, 2026-08-18 |
| Use shared conceptual records plus country-owned catalogs/bindings | Proposed; architecture and country consultation required |
| Use the 83% design-surface estimate only as a discovery hypothesis | Proposed measurement approach; implementation evidence required |

## Readiness

This document is **consultation-ready for identity, country-policy, delegation, architecture, security/privacy and operations workshops**. It is not delivery-ready. Production remains gated on country identifier/field catalogs, legal applicability, authority evidence, official technical artefacts, provider/directory behaviour, operation safety, retention and approved ownership.

## Revision history

| Date | Change | Evidence/decision |
|---|---|---|
| 2026-08-12 | Initial child discovery PRD; corrected SIREN/SIRET cardinality and combined identity, tenancy, Peppol address and accountant-delegation analysis | User feedback, supplied research and official French/Spanish sources |
| 2026-08-12 | Published as a child of commonality page `866150169` | User publication approval |
| 2026-08-12 | Relayout separated workspace, delegated authority, identifiers and credentials into collision-free lanes; made SVG and note cards responsive | Confluence visual review |
| 2026-08-18 | Deepened the discovery into an identity-driven compliance-delivery model; separated document, recipient-delivery and authority-reporting outcomes; added five-country identifier/authority evidence, reusable records, lifecycle, journeys, failures, requirements, acceptance, metrics, reuse method and delivery gates | User review and official sources accessed 2026-08-18 |
