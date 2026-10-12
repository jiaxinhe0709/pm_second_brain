---
id: SPEC-SEI-002
title: Customer Onboarding Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-12
reviewers: []
related:
  - GLO-SEI-001
  - PRD-SEI-101
  - PRD-SEI-104
  - PRD-SEI-107
  - PRD-SEI-202
  - PRD-SEI-222
  - PRD-SEI-225
  - PRD-SEI-226
  - PRD-SEI-231
  - SPEC-SEI-001
  - SPEC-SEI-004
  - ADR-SEI-001
  - SPEC-SEI-014
  - SPEC-SEI-013
  - SPEC-SEI-011
  - SPEC-SEI-006
  - SPEC-SEI-007
  - SPEC-SEI-009
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610648"
  page_id: "923861390"
  layout: two_left_sidebar
  toc: true
---

# Customer Onboarding Solution Specification

Use the [shared e-invoicing glossary](../context/GLO-SEI-001-e-invoicing-terminology.md). Local definitions explain this feature. Technical IDs, fields and source codes retain their stated meanings.

## Part 1 Feature Solution Summary

### Reader guide

Part 1 explains the scope, people involved, workflow and open decisions. Start here for a stakeholder review. Part 2 gives the detailed behaviour and rules. Part 3 describes service interactions and data. Part 4 links requirements to the checks and evidence needed before release.

The design remains a draft. **Proposed** choices need review. **Open** decisions need an owner's recorded answer. Technical IDs and state names give all readers the same references.

### 1 Purpose, authority and boundaries

This **proposed logical design** helps a Spanish business set up, connect, confirm or extend e-invoicing through a Sage ERP or product. It covers new customers and customers who already use public services, private services or both. It also covers customers already connected through Sage. The E-Invoice Service checks the current setup and requested outcome first. External registration or a platform change is required only where the selected journey needs it.

The intended outcome is access to selected, supported functions from the Sage ERP through the **E-Invoicing Global API**. Connection, readiness and activation are separate results. The API contract, adapters and implemented capabilities still need qualification. **Phase 1** checks readiness for supported public functions. **Later phases** may configure private connections and activate or change a qualified route. Each scenario retains these phase gates.

**Required checks before readiness:** certificate-based readiness needs **both a verified business NIF and a valid, suitable certificate**. The E-Invoice Service records evidence for both checks. The NIF identifies the represented business. The certificate must support the selected actor, purpose and environment. Effective action authority is also required. Neither a NIF nor a certificate alone establishes permission or readiness.

The certificate can already be held by the qualified Tax/certificate capability or an authorised representative. A new customer upload is not a default requirement. If approved policy records NOT_REQUIRED, retain that evidenced certificate exception. Business NIF verification and action authority still apply. Use the approved NIF/NIE mapping for an individual legal subject; do not substitute the caller's identity for the business. Identity verification follows the approved policy and does not decide applicability for every invoice.

**Setup stages:** ONB-01 opens a case from an authenticated Sage request, an authorised business reference and selected functions. NIF or certificate verification can still be pending. ONB-02/03/06 establish identity, authority and the access/trust requirements for each function. Complete required credential checks before the first dependent platform operation. Any route activation still needs ONB-07. Later use must recheck validity, expiry, revocation and authority under the owning feature's policy. Opening a case is not a readiness or activation result.

Public readiness alone does not prove external registration, private-route activation or invoice exchange. Requirements come from [public onboarding](../prds/PRD-SEI-101-public-platform-onboarding.md), [direct and accountant onboarding](../prds/PRD-SEI-104-accountant-and-single-client-onboarding.md), [recovery](../prds/PRD-SEI-107-public-onboarding-failure-recovery.md), and [private onboarding and migration](../prds/PRD-SEI-222-customer-onboarding-entry-point-migration.md). The [certificate spec](SPEC-SEI-001-certificate-management-solution-specification.md) defines trust-readiness checks where policy requires them.

The services, state names, interactions and records below are **proposed**. The PRDs define customer outcomes and safety constraints. Applying official Spain rules to each selected interface remains **open**. Representation and signing need qualification for each action. The provider entry-point sequence, operator model, measurable service targets and actual dependency implementation ownership also remain **open**. The E-Invoice Service owns the workflow as stated below. This file is the canonical Markdown source for onboarding.

### Customer entry journeys and scope

Scenario IDs identify entry journeys. They do not define a technical state for the whole customer. A direct customer or validated accountant can use each supported journey. For a portfolio, the E-Invoice Service checks each business separately. It compares the existing setup with the requested Sage functions. Customer statements inform this check but do not prove Sage's authority or integration.

| Scenario | Current situation and desired outcome | Work required | Result and boundary |
|---|---|---|---|
| ONB-S01 First-time setup | Customer has no e-invoicing setup and wants to start through Sage. | Establish the business and authority. Present supported options. Configure missing prerequisites and check each selected function. | Return public readiness under ONB-04 or later-phase private activation under ONB-05–07. Do not select a platform without customer choice. |
| ONB-S02 Connect existing public service | Customer uses the public B2B service outside Sage and wants supported functions in the ERP. | Identify the service and environment. Check Sage access, represented-party authority and required trust. Reuse valid evidence and complete missing checks. | Return evidenced public readiness through the Global API. ONB-04 alone cannot establish active invoice exchange or publish a receiving destination. |
| ONB-S03 Connect existing private provider | Customer wants to keep the current private provider and use it from the ERP. | Qualify the integration. Bind the existing account with permission. Configure the Sage connection. Check sending and receiving separately. | Retain the provider. Establish the Sage route explicitly if required. Duplicate commercial enrolment or receiving-point publication requires a contract requirement. |
| ONB-S04 Connect public and private services | Customer uses both services and wants Sage to support the selected combination. | Record each function, direction and execution owner. Qualify public and private connections separately. Record unchanged and changed setup. | Return a result for each function. Public reporting or copy capability is not a second delivery route. Prevent duplicate delivery and unsupported overlapping selection. |
| ONB-S05 Confirm or extend Sage setup | Customer already connects through Sage and wants confirmation or an additional function. | Read authoritative configuration. Check current permissions and evidence. Recheck stale dependencies. Set up only missing functions. | Confirm valid unchanged setup without external mutation, or add only the requested supported function. Failed checks cannot renew readiness. |
| ONB-S06 Change platform | Customer wants to move an authorised future sending or receiving scope to another supported platform. | Record the current route and earlier obligations. Qualify the new connection. Obtain change authority. Observe required external changes and commit the boundary. | Change new traffic only through ONB-07. Keep earlier invoice context. Private A → Private B remains gated by SPEC-SEI-014 and its source product decision. |
| ONB-S07 Add B2B after B2G use | Customer uses government invoicing, such as FACe, and now needs supported B2B functions. | Record the existing B2G service. Assess B2B identity, authority, connection and capability requirements separately. | Set up B2B without changing B2G. B2G support through this API needs a separate scope and adapter decision. |
| ONB-S08 Unsupported or uncertain setup | Requested provider, function or combination is unsupported, or current setup is unknown. | Explain the missing integration or evidence. Name the owner. Offer only qualified options. Reconcile any possible external effect. | Return a limitation, action required or unresolved case. Do not force migration, substitute a platform or report connected. |

**Confirmed source context, checked 9 October 2026:** [FACe](https://www.facturae.gob.es/face) is a B2G submission service. [Order HAC/1028/2026](https://www.boe.es/eli/es/o/2026/10/02/hac1028) governs the B2B public solution. These are separate services. The published rules do not prove an implemented Sage connector or customer production access. The [AEAT scope guidance](https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/cuestiones-generales/quienes-estan-obligados-que-operaciones-incluyen.html) excludes B2C and international B2B with a business not established in Spain. A transaction addressed to a Spanish permanent establishment can fall within scope. The E-Invoice Service records business context. The owning invoice feature checks applicability for each transaction. B2G use or an international invoice does not establish readiness or exemption for the whole business.

### ERP and API responsibility boundary

The proposed handoff is **Sage ERP / product → Global API → E-Invoice Service → shared identity, trust and connection services → qualified public connector or provider integration**. Responses use the same product-facing contract. This flow identifies responsibilities. It does not approve endpoints or deployment boundaries. The [Global API spec](SPEC-SEI-013-provider-api-through-the-e-invoicing-global-api-solution-specification.md) owns common API exposure. The [public connector](SPEC-SEI-011-public-platform-connector-solution-specification.md) owns public execution. [Shared connectivity](SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns connection and route records.

**Confirmed ownership direction:** the E-Invoice Service owns the onboarding journey and its recovery coordination. There is no separate onboarding service. In this spec, **onboarding** names the setup workflow. **Proposed:** an internal onboarding component could implement that workflow within the E-Invoice Service. Its need, code boundary and implementation remain open under ONB-Q05. It does not introduce a separate product API or deployment.

The E-Invoice Service assesses current setup, coordinates missing checks, tracks work items and returns results. The ERP displays results and customer actions. Identity, certificate, connection and routing capabilities retain their own controls. Operations handles assigned manual cases. SPEC-SEI-004 defines the recovery behaviour inside this ownership model.

**Certificate reuse direction:** use the existing Tax/certificate capability where its actual contract supports the requested function. The E-Invoice Service requests readiness and a protected reference under SPEC-SEI-001. It does not hold private keys, issue certificates or create another credential store. Tax Service, Connections Service and AFL owners must confirm the actual source and supported operations. Do not assume that the proposed Tax Vault and the described Connections Service/AFL path are the same implementation.

Reuse a suitable existing certificate by reference. Confirm its business or authorised representative, purpose, environment, version, validity and effective authority. Return missing actions to the ERP. A certificate lookup or validation result alone does not prove that the existing service can authenticate a request or sign invoice data. Qualify those operations separately before use. Certificate custody, validation, protected use, renewal and revocation remain in SPEC-SEI-001.

Keep three facts separate: **represented business identity**, **authenticated caller identity**, and **authority for the requested action**. The verified business NIF establishes the first. The accepted authentication method identifies the caller for that service. A Sage login does not itself authenticate a public-platform request. The scoped grant establishes authority. A customer's, accountant's, Sage's or provider's credential can support only its approved actor and purpose. ONB-Q06 must establish the credential owner, custodian, execution owner and effective grant for each function.

**Confirmed operation context, checked 12 October 2026:** [Order HAC/1028/2026, Article 11](https://www.boe.es/eli/es/o/2026/10/02/hac1028) requires accepted electronic certificates for public-platform authentication. Specified generation, status/payment and consultation web forms also allow Cl@ve. Third-party retrieval and consultation require registered representation, including automated access. The web-form option does not establish Cl@ve support for the automated ERP/API connection; qualify that contract separately.

For covered B2B invoices issued through private platforms, [RD 238/2026, Article 7(3)](https://www.boe.es/eli/es/rd/2026/03/25/238/con) requires an advanced electronic signature by the issuer or an authorised delegate. This is separate from connection authentication. For receiving, assess access and retrieval requirements separately from signing. Receiving a signed invoice is not a request to sign it. Private-provider access follows its qualified contract. None of these rules establishes a universal customer certificate-upload step.

This spec owns current-setup assessment, customer intent, journey selection and setup results. [Sending](SPEC-SEI-007-invoice-sending-solution.md), [receiving](SPEC-SEI-006-invoice-receiving-solution.md) and [lifecycle status](SPEC-SEI-009-invoice-lifecycle-status-solution-specification.md) own invoice operations and outcomes. The E-Invoice Service does not issue an invoice or treat a test as delivery. Platforms can support different functions. The API must not promise every provider or function.

Customer-facing actions are **Set up e-invoicing**, **Connect your existing service**, **Review or extend your setup**, and **Change your e-invoicing platform**. All use one work-item model and shared controls. A completed assessment can still return required actions. Report sending or receiving as active only when the owning feature and required route evidence confirm activation.

### Setup result and changing the e-invoicing platform

In **Check public setup requirements** and **Configure and check private setup**, the E-Invoice Service checks business identity, authority, required certificates and trust, and the selected connection. ONB-02–04/06 coordinate these checks and record limitations. Use **readiness** in technical states, evidence and contracts. The diagram explains the work in plain language. Passed checks do not activate sending or receiving.

In **Return results and required actions**, the E-Invoice Service returns passed, failed and unknown checks, limitations, next actions and action owners. ONB-04/06 supply the check results. ONB-11 returns them through the Global API. Passed checks alone do not confirm sending or receiving activation. Activation results need evidence from the owning feature. The product shows plain-language results and retains exact technical states and evidence internally.

**Change e-invoicing platform** changes the selected platform for future sending or receiving within an authorised scope and boundary. Show the customer the current and proposed platform, affected direction, remaining steps and result. Use **route** as the technical term. Earlier invoices retain their history and permitted follow-up channels.

This spec coordinates customer intent, setup and migration. The [shared connectivity and routing spec](SPEC-SEI-014-shared-platform-connectivity-and-routing-solution-specification.md) owns connection and profile qualification, route-version commit and historical context (SPC-01–08). ONB-06/07 use that foundation. They do not create another route engine. The Sage operator role needs separate qualification. Adding that role does not migrate customers or change their active platforms.

### Spain use and reuse boundaries

This is a **Spain reference design**. Reuse classifications describe proposed behaviour. They do not prove that existing code is ready. **Reusable unchanged** keeps the design pattern. **Reusable with country binding** needs approved local policies or adapters. **Country-specific** rules stay in the country pack. **Unknown** needs implementation evidence.

The design follows the [shared platform and country-pack direction](../prds/PRD-SEI-227-e-invoicing-as-a-service.md). Spain pilot and production use require this spec's approval and evidence gates. Another country needs its own reuse assessment.

| Area | Intended use in Spain | Reuse classification | Condition and owner |
|---|---|---|---|
| Work items and portfolio isolation | Track each Spanish business separately. Recognise repeated requests and show partial portfolio results. | Reusable unchanged | The E-Invoice Service and Product validate the work-item and version patterns. They verify tenant and client isolation. |
| Current setup, readiness and route transition | Assess existing public and private use. Reuse qualified evidence. Configure or activate missing supported functions separately. | Reusable with country binding | Product, Identity and the route owner bind local identity, authority, entitlement, provider and entry-point policies. They preserve phase gates. |
| Spain onboarding rules | Apply Spain identity and representation checks. Use the confirmed public and private entry-point and migration sequence. | Country-specific | The Spain technical owner and Compliance keep NIF/NIE rules and platform sequences separate from other countries' defaults. |
| Existing onboarding implementation | Assess identity, trust, work-item, connection and routing services for Spain. | Unknown | Architecture and service owners must identify the existing owners, contracts and gaps. This spec does not establish a deployed end-to-end implementation. |
| Internal onboarding component | Coordinate setup and recovery within the E-Invoice Service. | Proposed design pattern; implementation unknown | The E-Invoice Service owner and Architecture assess existing workflow, record and recovery capabilities. Record retained behaviour, local changes, gaps and evidence before deciding what to build under ONB-Q05. |
| Existing Tax/certificate capability | Reuse suitable protected credentials and readiness results for selected Spain functions. | Existing implementation reuse candidate; B2B coverage unknown | Tax Service, Connections Service and AFL owners confirm the source, build, contracts, purpose checks and operations under SPEC-SEI-001. Record local changes and gaps. ONB-Q06 blocks unqualified authentication or signing. |
| Existing customer setup evidence | Reuse checks only for their proven business, purpose, role, environment and validity. This includes identity, mandate, trust and connection checks. | Reusable with country/provider binding | Identity, Trust and Integration record the source, versions, retained checks, gaps, owner and recheck conditions. External use does not prove Sage access. |
| ERP/API integration and representation checks | Return consistent scenario results. The owning exchange features qualify required formats. | Unknown implementation coverage | The API owner qualifies the actual contract and build. Existing DTS is the preferred transformation reuse candidate where relevant. Qualify its selected contracts, mappings, rule packs and operations under SPEC-SEI-008. Setup alone does not prove DTS readiness. |

### Plain-language terms

| Term | Meaning |
|---|---|
| Legal entity / legal subject | The business to which the invoice or action belongs. Technical fields use `legalSubject` for this business. |
| Authority | Permission to perform a specific action for that business. Logging in or holding a certificate does not by itself give this permission. |
| Capability | A supported function, such as receiving invoices or signing them. |
| Onboarding | Establish or confirm the setup for selected functions through Sage. This can connect an existing service, add a function or coordinate an authorised platform change. |
| Onboarding component | A proposed internal component of the E-Invoice Service that could implement setup and recovery coordination. Its implementation remains open. |
| Global API | The proposed common e-invoicing API contract used by Sage products and authorised partners. It does not establish that an integration is implemented or active. |
| B2B / B2G / B2C | Business to business; business to government; business to consumer. Each transaction and service has its own scope and controls. |
| Route | The time-bound selection of platform and connection for a defined invoice scope and direction. A ready connection does not activate a route or rewrite earlier invoice plans. |
| Idempotency | Repeating the same logical request adds no effect within the contract’s defined scope and retention window. The contract binds request identity and input and defines conflict handling. |
| Reconciliation | Check the original operation against a reliable source to establish what actually happened before deciding the next action. |
| Gate | A condition, decision or evidence check that must pass before the next step can proceed. |
| Tenant | The customer account boundary used to keep one customer’s data and access separate from another’s. |
| Immutable / append-only | Immutable means a saved record cannot be changed. Append-only means later information is added as another record. Neither means indefinite retention. |
| Provenance | The record of where data came from and which versions, checks and changes produced the result. |
| Contract | The agreed inputs, outputs, behaviour and responsibilities between services or parties. |
| Durable | Saved through the agreed recovery boundary so the record survives a process restart or worker failure. Long-term retention is a separate policy. |
| Readiness | The current capability-check result for a stated legal entity, actor, environment and route/profile. It includes evidence, limitations and a recheck condition. It is separate from authority, route activation and invoice outcomes. |
| Entry point | The published receiving destination for a legal entity. It need not be a raw URL. Publication does not by itself prove operational eligibility for a particular invoice. |
| Cutover / rollback | Cutover changes future work to a qualified route at an agreed boundary. Rollback is a controlled change back, with its own checks and evidence. Earlier invoices keep their actual route history. |
| Portfolio | An accountant’s set of client businesses. Each client is checked separately. |
| Input digest / hash | A calculated fingerprint used to detect a change in the submitted data. |

### 2 Outcomes and handoffs

| Outcome | Observable result | Boundary |
|---|---|---|
| Public capability ready | Return readiness for the entity and capability. Include limitations, evidence, expiry or recheck, and next action. | Do not claim external registration, invoice compliance, delivery or private-route activation. |
| Private route active | Intended and observed readiness match for the authorised direction and scope. Record the effective boundary for new traffic. | Earlier invoices retain their original route and operator. |
| Existing setup confirmed | Requested functions have current evidence. Return unchanged route and configuration through the API without new external work. | Do not renew stale evidence or grant missing permission. |
| Setup extended | Requested additional functions pass their own gates. Unchanged functions retain their context. | Do not report all functions active from new readiness alone. |
| Unsupported connection or function | Tell the ERP which provider, function or combination is unsupported. Return the available next action. | Do not substitute a provider, force migration or report connected. |
| Action required / blocked | Hold the affected entity, capability or direction. Return a stable reason and owner. | Other portfolio items and unaffected directions continue. |
| Cancelled before activation | Close pending work under policy. Keep live routing unchanged. | Reconcile completed external actions. Reverse them separately where required. |
| Recovery or rollback case | Preserve actual external and invoice state. Restoration is a new transition with evidence. | Do not reset state silently or rewrite history. |

Actors include the customer administrator or validated delegate, Sage product/API, E-Invoice Service, and legal-subject and authority services. Supporting actors include trust, operator, connection and route services, the external platform or provider, the evidence store, and operations. Each actor performs only authorised actions for the stated tenant, legal entity, environment, capability, direction and route scope. Each accountant client has an isolated work item. Portfolio membership does not share a mandate or credential.

### 3 Process diagrams and text equivalent

Start with the process overview. Use the two process details to review public checks or private setup and activation. Use the matching sequence diagrams for requests, responses and evidence. Both views describe the same behaviour. The [entry-journey table](#customer-entry-journeys-and-scope) defines each scenario's scope.

The overview shows **work paths**, not service responsibility lanes. The detail diagrams use the shared responsibility lane names and omit groups with no activity. All three use the same activity IDs. The common sequence is **request → identity and authority → current setup → only required work → results and actions**. ONB-01–11 retain their meanings.

In the detail diagrams, the **Domain Service - E-Invoice Service** lane owns workflow coordination. A future internal onboarding component stays within that lane. The **Domain Service - Other Services** lane includes the qualified Tax/certificate dependency. The overview's work paths and the detail lanes do not create separate onboarding or recovery services.

**Common behaviour:** capture intent, check identity and authority, assess current setup, request required access/trust checks and return each function's result. **Scenario-specific work:** establish first setup, bind an existing provider, coordinate a public/private combination, confirm or extend setup, or change a supported route. **Conditional work:** certificate setup, external mutation, activation, historical release and recovery run only when required. Country and provider contracts determine the checks; scenario labels do not determine certificate need.

Use the same labels in both diagram types. A common check can confirm that no further work is needed. The labels describe behaviour, not proven reuse of code. Country and provider bindings select the rules and contracts; they are separate from the scenario labels.

| Label | Meaning | Example |
|---|---|---|
| Common | Shared behaviour for supported setup journeys. Return a limitation when scope or required evidence cannot be established. | Capture intent, establish identity and authority, assess current setup and return results. |
| Scenario-specific | Work selected for the customer's current setup and requested outcome. | Public checks, existing private-account binding or a requested platform change. |
| Conditional | Work performed only when the assessed plan and approved contract require or permit it. | Certificate correction, external observation or mutation, activation and recovery. |

Shapes and arrows retain their existing meanings. Process arrows show work and conditional paths. Sequence arrows distinguish requests, responses and notifications. In a sequence, **opt** means an optional group; **alt** means alternative outcomes. These terms do not define new service states.

| Shared action wording | Activity | Process and sequence correlation |
|---|---|---|
| Capture requested functions | ONB-01 | Open the scoped work item. A saved request receipt is not readiness. |
| Check business identity and authority | ONB-02 | Verify the represented business NIF and scoped grant. Keep caller identity separate. ONB-03/06 recheck affected evidence where needed. |
| Assess current setup | ONB-10 | Read current versions and evidence. Reuse only matching, valid decisions. |
| Check access and trust requirements | ONB-03/06 | Resolve the requirements for each function. Check required certificate readiness through SPEC-SEI-001 CERT-05. |
| Return results and required actions | ONB-11 | Return each function's setup, readiness, activation evidence, limitation and action owner through the Global API. |

**Onboarding overview:** ![Set up, connect or review e-invoicing through Sage](../assets/diagrams/onboarding-scenario-selection-process.svg)

[Editable Draw.io](../assets/diagrams/onboarding-scenario-selection-process.drawio) · [PNG](../assets/diagrams/onboarding-scenario-selection-process.png).

ONB-01 captures the requested functions and outcome. ONB-02 checks the caller, represented business and action authority. ONB-10 compares the request with current setup and valid evidence. For each function, confirm valid unchanged setup or run the required public or private work. Both branches can apply to the same business. They do not require a platform change.

Public work uses ONB-03/04 to check prerequisites and record readiness. Private work uses ONB-05/06 to configure only missing settings and check each selected function. Activate or change a private route through ONB-07 only when required, supported and explicitly authorised. Keep earlier invoice context under ONB-09. A requested change still requires qualified setup before activation. If the route is valid and unchanged, return its current evidence without a route commit.

ONB-11 returns setup, readiness and activation separately for each function through the Global API. Include failed and unknown checks, limitations, required actions and their owners. A completed request or passed setup check does not prove active sending or receiving. Unsupported work returns a limitation. A possible external effect uses ONB-08 and the shared recovery spec before an unsafe repeat or an activation claim. Return partial results and preserve independently valid functions.

| Work path | Entry journeys | How to read it |
|---|---|---|
| Public checks | Public functions in ONB-S01/02/04/05/07 | Use the public detail. Existing public or B2G use does not prove Sage B2B authority or access. |
| Private setup | Private functions in ONB-S01/03/04/05/06/07 | Use the private detail. Bind an existing account where selected. Keep the provider unless the customer requests a supported change. |
| Confirm unchanged setup | ONB-S05 and valid unchanged functions in other journeys | Use the overview shortcut. Return current evidence without external mutation or a new route version. |
| Activate or change a route | ONB-S06 or required initial activation for a selected private function | Use the private detail after qualification. Change only authorised future traffic and keep earlier invoice context. |
| Limitation or recovery | ONB-S08 or affected work in any journey | Return a precise limitation or owned action. Preserve independently valid functions. |

ONB-S01 requires explicit customer choice. ONB-S04 can use both setup paths. ONB-S05 adds only requested supported functions and rechecks affected stale evidence. ONB-S07 keeps existing B2G use separate from B2B setup; B2G support through this API remains a separate scope and adapter decision.

The following matrix identifies the differences without creating eight duplicate sequences. All supported paths use the shared actions above. Sequence examples show a selected business and function; they do not promise every provider or capability.

| Scenario | Scenario-specific work | Conditional work or shortcut | Diagram coverage |
|---|---|---|---|
| ONB-S01 First-time setup | Record the customer's supported public/private choice and establish missing setup. | Required certificate process, enrolment and later-phase activation only under the selected policy and contract. | Overview plus selected public/private process and sequence. |
| ONB-S02 Existing public service | Check Sage access to the selected public function. | Reuse matching evidence; run only missing or stale checks. No route activation in this public path. | Public process and public sequence example. |
| ONB-S03 Existing private provider | Bind the authorised existing account and configure missing Sage settings. | Reuse qualified credentials; activate the Sage route only if required. No duplicate enrolment by default. | Private process and private sequence example. |
| ONB-S04 Public and private | Assess each selected function and its execution owner independently. | Both detail paths can apply. Hold only affected work, subject to invoice dependencies. | Overview plus both process details and sequences; no implied order between paths. |
| ONB-S05 Confirm or extend | Confirm current setup or add the requested supported function. | Valid unchanged evidence skips setup changes and route commit. Recheck affected stale evidence. | Overview confirmation shortcut; shared sequence groups and selected detail for an extension. |
| ONB-S06 Change platform | Qualify the proposed connection and preserve earlier invoice context. | Required external change, current authority and version checks precede authorised activation. Gated migration modes stay blocked. | Private process and its conditional activation sequence group, with SPEC-SEI-014. |
| ONB-S07 Add B2B after B2G | Check B2B identity, authority, access and trust separately. | Reuse only evidence qualified for B2B. Keep existing B2G unchanged. | Selected public/private detail; shared checks in its sequence. |
| ONB-S08 Unsupported or uncertain | Return the precise scope or evidence limitation. | No unsupported mutation. Failed safe reads use owned retry/escalation; possible effects use original-operation reconciliation. | Overview limitation path, sequence action branches and SPEC-SEI-004 recovery. |

For ONB-S04, public and private checks remain independent. A public failure does not revoke an unaffected private capability. The owning invoice feature still enforces required public-copy and reporting dependencies before dependent invoice actions. Unsupported overlapping selections remain blocked. The branches do not create two delivery routes for the same action.

**Public setup checks — detail:** ![Check public setup and return the readiness result](../assets/diagrams/onboarding-public-readiness-process.svg)

[Editable Draw.io](../assets/diagrams/onboarding-public-readiness-process.drawio) · [PNG](../assets/diagrams/onboarding-public-readiness-process.png).

This Phase 1 path starts after ONB-01/02/10 establish the request, authority and assessed plan. ONB-03 checks only missing or stale identity and representation evidence, the public connection and required trust. The selected policy determines whether certificates are required. Record NOT_REQUIRED only with policy evidence; UNDETERMINED blocks affected progress. Use only qualified public operations and the correct business, capability and environment.

**Check access and trust requirements** includes two decisions: determine whether a certificate is required, then establish its readiness for the selected purpose. ONB-INT-03 consumes the qualified SPEC-SEI-001 CERT-05 result. Reuse a suitable existing protected reference without another upload. A confirmed missing, expired, revoked or unsuitable certificate returns a correction owner. Unavailable or ambiguous evidence leaves readiness unconfirmed; it does not prove missing material.

ONB-04 records each check, readiness result, evidence and recheck condition. Missing authority or uncertain policy returns an action owner. A possible external mutation uses ONB-08. ONB-11 returns the result through the Global API. Public readiness does not establish external registration, route activation or active exchange. Portfolio clients retain independent results, including failures.

**Public setup — sequence:** ![Connect an existing public service: shared checks and certificate readiness](../assets/diagrams/spain-onboarding-public-setup-sequence.svg)

[Editable Draw.io](../assets/diagrams/spain-onboarding-public-setup-sequence.drawio) · [PNG](../assets/diagrams/spain-onboarding-public-setup-sequence.png).

The ONB-S02 example expands the public process into logical requests and responses. Common groups capture the request, check business identity and authority, assess current setup and return results. The access/trust group resolves policy and shows the qualified Tax/certificate readiness handoff. Its alternatives distinguish valid reuse, confirmed correction and unavailable evidence. The public group performs only required qualified reads and records ONB-04 results. The main path continues only after its prerequisite gates pass; failures return actions instead.

Receipt and notification are separate from the authoritative result. The ERP can query the saved work item after a missed notification. The example uses a saved asynchronous request; wholly local checks can finish synchronously. Participant labels identify responsibilities, not approved deployment boundaries or endpoints.

**Private connection and activation — detail:** ![Connect a private provider and activate or change only when required](../assets/diagrams/onboarding-private-route-process.svg)

[Editable Draw.io](../assets/diagrams/onboarding-private-route-process.drawio) · [PNG](../assets/diagrams/onboarding-private-route-process.png).

This later-phase path starts after ONB-01/02/10 establish the request, authority and assessed plan. ONB-05 records the explicit provider choice, business, direction, scope, commercial terms and authority. Bind the existing account where selected. Configure only missing settings. Create an enrolment or subscription only where the contract requires it. Keep connection configuration separate from active route state.

ONB-06 checks sending, receiving and status functions separately. It observes required external state. Publish or change a receiving point only where the selected plan and contract require it. A configured connection does not prove readiness. Missing or unknown evidence returns an owned action; a possible external effect uses ONB-08. Recovered external success does not itself activate a route.

Use **Check access and trust requirements** here as in the public path. ONB-06 consumes purpose-specific certificate readiness through ONB-INT-03 where required. Private-provider access, public authentication and invoice signing remain separate purposes. Provider-held or delegated credentials need their approved actor and grant; do not assume a customer upload.

After qualification, decide whether a route change is required. A valid unchanged route returns its current evidence without a commit. An initial Sage activation or supported platform change uses ONB-07 only after current readiness, action authority, the expected route version and the effective boundary are confirmed. ONB-09 preserves earlier and in-flight invoice context. Release old dependencies at separate approved gates. ONB-11 returns the observed result for each function.

Before an external change, failure leaves the old route. A possible external effect can require a hold on affected traffic until reachability is established. After cutover, failure opens a controlled restoration case. Each invoice retains its actual origin. Private A → Private B and unsupported coexistence remain disabled until their decisions and contracts are approved.

**Private setup and activation — sequence:** ![Connect a private provider: shared trust checks and conditional activation](../assets/diagrams/spain-onboarding-private-setup-sequence.svg)

[Editable Draw.io](../assets/diagrams/spain-onboarding-private-setup-sequence.drawio) · [PNG](../assets/diagrams/spain-onboarding-private-setup-sequence.png).

The ONB-S03 example uses the same common groups and certificate outcomes as the public sequence. ONB-05 binds existing account context and configures only missing settings. ONB-06 checks selected private functions after required access/trust gates pass. Required external mutations remain separate qualified operations with saved intent and recovery controls.

The route alternatives distinguish unchanged confirmation, required authorised activation and blocked or uncertain work. An unchanged route needs no commit. ONB-07 rechecks authority, current readiness, observations, the expected version and boundary before activation. ONB-09 preserves earlier invoice context. Failure or uncertainty returns to SPEC-SEI-004 and the exact affected parent gate. Runtime authentication, invoice signing and use-time rechecks remain with their owning features.

**Shared failure and recovery:** all journeys use [SPEC-SEI-004](SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md#3-process-diagrams). It owns classification, safe retry and uncertain-effect reconciliation. Resume the exact parent check after resolution. Preserve unaffected services and hold only unsafe dependent work. These steps do not add another retry engine or an activation shortcut.

### 4 Ordered lifecycle

| Activity | Trigger and required result | Owner / consumer |
|---|---|---|
| ONB-01 Capture requested functions | Create one scoped, versioned item from an authenticated request. For a duplicate key, return the same result. | Product → E-Invoice Service |
| ONB-02 Check business identity and authority | Verify the business NIF for the legal subject. Check the represented party or delegate, action and authority validity. Show any missing grant. | Identity/authority → E-Invoice Service |
| ONB-10 Assess current setup | Read public, private and Sage setup evidence. Compare requested functions. Preserve unchanged selections without mutation. | E-Invoice Service → connection/route/adapters |
| ONB-03 Assess prerequisites | Assess applicability, environment and external checks. Require a valid, suitable certificate where policy requires one. Keep NIF, certificate and authority results separate. | E-Invoice Service → identity / qualified certificate capability / external adapter |
| ONB-04 Publish public readiness | Return each capability's result, evidence and recheck condition. Do not change a route. | E-Invoice Service → product |
| ONB-05 Configure private choice | Save the explicit option, subscription and connection intent, and scope. Do not activate new traffic. | Customer/product → E-Invoice Service / Routing |
| ONB-06 Prove private readiness | Establish observed readiness for the operator, transport, profile and required external entry point. | Connection/adapter → E-Invoice Service |
| ONB-07 Cut over new traffic | Process overlapping scope changes one at a time. Record the authorised effective boundary. | Route service → exchange/product |
| ONB-08 Reconcile/recover | Assign an owner to each unknown or inconsistent result. Record observed state and a safe next action. | Operations/external adapter |
| ONB-09 Preserve and release | Preserve original invoice context. Release previous dependencies only after approved gates pass. | Route/records/operations |
| ONB-11 Return results and required actions | Return setup, readiness and activation separately for each selected function through the Global API. Include limitations, evidence and required actions. | E-Invoice Service → Global API → ERP/product |

### 5 Key decisions and risks

| Decision | Design impact | Owner and gate |
|---|---|---|
| Official public-solution identity, representation, certificate and API contract | Establish which ONB-03 checks and mutations the contract supports. | Spain regulatory/technical owner; public pilot |
| Private operator, supported directions/scope granularity and activation mechanism | Define the ONB-05–07 command and lock key. | Product, architecture, operator; design |
| Entry-point publish/observe/withdraw order and propagation evidence | Establish safe inbound cutover and rollback. | Local technical/regulatory owner, provider; pilot |
| Post-switch historical status/reporting actor and route | Define retained access to the previous provider. | Compliance/Tax, provider; migration pilot |
| Provider idempotency, state query and correction support | Establish whether automated or manual reconciliation is safe. | Provider owner, operations; integration |
| Trust/signature and retention policies | Define required readiness, expiry checks and record schedules. | Security, Legal/Tax; design |
| ONB-Q01 Provider/account discovery and existing-evidence reuse | Define permitted observations, account binding and evidence freshness. Do not inherit evidence from another role or environment. | Integration, Identity and Trust owners; selected provider pilot |
| ONB-Q02 Public/private combinations and executor ownership | Define supported functions, directions and dependencies. Prevent overlapping routes and duplicate delivery. | Product, Connection/Routing and Exchange owners; design and pilot |
| ONB-Q03 B2G, B2C and international product coverage | Decide coverage beyond this B2B onboarding scope. Qualify the separate service and adapter before expanding scope. | Spain Product and Compliance, API/Integration owners; before enabling that capability |
| ONB-Q04 ERP result and public-operation enablement | Qualify actual Global API fields and evidence for each function. Keep Phase 1 readiness separate from later activation. | API, E-Invoice Service, Sending/Receiving and public connector owners; API design and public pilot |
| ONB-Q05 Internal onboarding component and implementation reuse | Decide which existing E-Invoice Service capabilities can implement setup, saved work items and recovery. Identify remaining component work without introducing a separate service. | E-Invoice Service owner and Architecture; component design before build |
| ONB-Q06 Existing Tax/certificate contract and execution owner | Confirm the actual protected source, lookup/readiness contract, safe metadata and supported authentication/signing operations. Status feedback alone cannot qualify protected execution. | Tax Service, Connections Service, AFL, E-Invoice Service and Security owners; selected-function pilot under SPEC-SEI-001 |

An accountant could act without client permission. A service could treat public readiness as activation or repeat an external change after a timeout. A transition could lose inbound reachability or access needed for earlier invoices. These are the main risks.

The controls below pause affected work, show intended and observed states, and preserve unaffected routes. Continue the previous route only while evidence confirms its safety and reachability. A possible external change can require a hold before local activation.

## Part 2 Logical Feature Specification

This part explains the proposed behaviour step by step. An invariant is a rule that must always hold, including during failures and recovery.

### 1 Scope model and invariants

The proposed work-item key is (tenant, legalSubject, environment, capability, direction, scope, onboardingIntent). Each request includes an idempotency key and a fingerprint of the input in its agreed standard form.

Changes affecting the same business, direction and scope run one at a time. Independent clients and directions that do not overlap can proceed separately. TEST and production use separate identities, evidence, credentials, route state and keys.

| ID | Rule that must always hold |
|---|---|
| ONB-I01 | Authentication, legal-subject identity, representation authority, credential possession, commercial entitlement, external registration and active route are independent facts. |
| ONB-I02 | Public readiness is per entity and capability, with limitations and evidence. It cannot activate a private route or prove invoice compliance. |
| ONB-I03 | Check the accountant grant for each client, capability, action and effective time. Portfolio success must not hide a failed item. |
| ONB-I04 | Change the route for new eligible traffic only after an explicitly authorised cutover. Each invoice retains its actual origin route, operator and identifiers. |
| ONB-I05 | An unknown external mutation is not success or permission to retry. Observe and reconcile the original operation before repeating it. |
| ONB-I06 | Subscription, connection, entry-point registration, route, transition and historical access have separate state and separate release gates. |
| ONB-I07 | No private key or reusable secret enters a product response, work item, audit event or support view. |
| ONB-I08 | Reuse evidence only for its proven subject, authority, purpose, role, provider/profile, country and environment. Check versions and validity. Record the source and missing checks. |
| ONB-I09 | An entry scenario or customer statement cannot prove external registration, Sage access, B2B readiness or active exchange. Unknown current setup is visible. |
| ONB-I10 | Setup failure affects only dependent functions and scopes. Preserve unaffected selections. The owning invoice feature enforces dependencies between functions. |
| ONB-I11 | No-change confirmation performs no external enrolment, publication, subscription creation or route commit. Extending setup changes only explicitly requested supported functions. |
| ONB-I12 | Before certificate-based readiness, both business NIF verification and required-certificate checks must pass. Action authority remains separate. A policy-backed NOT_REQUIRED result removes only the certificate requirement; unknown certificate need does not. |

### 2 Activities and state transitions

**ONB-01 Capture requested functions.** The product submits the business reference, requested capabilities and directions, actor, environment and any portfolio batch reference. The E-Invoice Service checks the request format, tenant access and capability support. It then saves a work item.

The case can open before NIF or certificate verification is complete. Retain the authorised business scope and show pending checks. Do not require a new certificate upload as an intake condition. This does not permit a platform operation or readiness result before its prerequisites pass.

For the same key and input fingerprint, the E-Invoice Service returns the existing item. For the same key with different content, it returns a conflict. Cancellation stops pending steps. It does not erase a possible completed external change. The portfolio parent shows overall progress. Each client item retains its own permission, state and error.

Record the desired outcome: first setup, connection of an existing service, setup confirmation or extension, or platform change. These descriptions are proposed intent labels. They are not approved API enum values. ONB-10 derives the scenario without replacing the requested capability, direction or scope. For an unsupported request, return a precise limitation without an external operation.

**ONB-02 Check business identity and authority.** The legal-subject service resolves Spanish identity and its product and tenant mapping. It does not treat a user login as the legal entity. The authority service checks the direct administrator or delegate mandate for the exact capability, direction, action and time. Missing, expired, revoked or ambiguous authority blocks the affected child item. Grant correction creates a new decision snapshot. An in-flight external operation retains the snapshot used at submission. Reconcile that operation before replacement. Recheck authority immediately before ONB-07 and other external mutations.

Obtain the business NIF verification result and evidence under the approved identity policy. Bind that result to the represented legal subject and environment. For an individual business, retain the approved NIF/NIE mapping. Keep the caller or delegate identity separate. An unverified NIF blocks readiness even when a certificate is valid; NIF verification alone does not prove action authority.

**ONB-10 Assess current setup.** After access to the tenant and entity is established, the E-Invoice Service reads authoritative connection, route and readiness records. If a qualified external read exists, it inspects the named provider, account or service without changing it. Record customer-declared facts separately from observed evidence. Include the source, time, environment and version. Do not assume a universal platform directory or query an unrelated business. A failed or empty lookup does not prove that the business has no setup.

Compare selected functions with current public and private connections, routes and obligations for earlier invoices. Record a plan for each function. The plan confirms unchanged setup, refreshes a stale check, configures a missing connection, requests supported activation, or returns an unsupported or unknown result. ONB-S04 can contain several plans. Create a new subscription for an existing account only if the commercial contract requires it. Keep B2G and B2B service contexts separate. Scenario correction creates a new plan revision. Do not repeat completed or uncertain operations.

Reuse a passed check only when all qualification conditions hold. The original subject, authority, purpose, role, provider/profile, country and environment must match. Relevant input, policy and credential versions must remain valid. Expiry and recheck conditions must be satisfied. Record retained evidence, omitted work, missing checks and the responsible owner. If evidence is stale, changed, revoked or unproven, recheck affected dependencies. Never copy protected secrets or transfer TEST evidence into production. If the plan becomes stale before mutation, refresh it and require the expected route version. ONB-08 owns the original uncertain effect.

**ONB-03 Prerequisites.** The E-Invoice Service resolves a versioned capability policy for the phase, operator, environment, route, direction and effective date. It checks required legal identity and representation evidence, and product entitlement. It performs external verification only under an approved contract. Check certificate readiness only where policy requires it. Record NOT_REQUIRED with policy evidence. UNDETERMINED blocks progress under that policy. The qualified certificate capability returns purpose-specific readiness and an evidence reference under [SPEC-SEI-001](SPEC-SEI-001-certificate-management-solution-specification.md). It does not expose key material.

Where a certificate is required, the E-Invoice Service asks the qualified Tax/certificate capability for an existing protected reference and readiness decision. Resolve the business and source binding from authorised context. Reuse only matching, current evidence for the selected purpose and environment. Do not request another upload because setup was reopened. The existing capability retains certificate material; ONB-D04 records references and safe results only.

If no suitable certificate is confirmed, return the required action and its owner. Missing, expired, revoked or unsuitable credentials need correction through the approved certificate process. Missing authority is a separate permission issue. If lookup is unavailable, stale or ambiguous, record the unknown result and use ONB-08. Do not infer absence or prompt another upload from a failed lookup. The ERP shows readiness, limitations, recheck conditions and next actions; exact source reasons need an approved mapping under ONB-Q06.

Establish the credential and authority needed for access before the first dependent platform operation. A certificate can support authentication as well as invoice signing. NIF/NIE identifies the subject but does not replace authentication or authority. Do not assume that every customer must upload a personal certificate. The selected actor, purpose and contract determine the required credential. Validate actual authentication/signing support with the execution owner; a readiness result does not perform either operation.

**Check access and trust requirements** names this common check in ONB-03/06. Reuse an existing qualified credential, request the approved process for a missing credential, or retain an evidenced NOT_REQUIRED result. If the requirement is unknown, keep the policy block. Record the credential owner and actor separately from the represented business. Authentication readiness cannot satisfy invoice-signing readiness, and signing readiness cannot grant retrieval or reporting authority.

External reads may retry under a bounded policy. An external mutation requires a safety classification and reconciliation support. The E-Invoice Service must not create a registration call without a confirmed official interface.

For public functions, use the qualified public connector and required shared connection and profile checks. An existing public login or FACe use does not establish Sage access. Run only missing or invalidated checks identified by ONB-10. The country and effective policy determine required capabilities. The E-Invoice Service must not make a permanent B2B/B2C or international applicability decision for every invoice.

**ONB-04 Public readiness.** The E-Invoice Service saves each required check's result and evidence source before it calculates the capability result. Proposed states are NOT_STARTED, CHECKING, ACTION_REQUIRED, READY_WITH_LIMITATIONS, READY, SUSPENDED and OUTCOME_UNKNOWN.

READY means the approved Phase 1 checks passed for that capability at the recorded time. Expired or revoked dependencies can change the result. Show the reason and recheck time. Remove sensitive values from product and support results. Show the user who must act next. A public-readiness event cannot activate a route.

**ONB-05 Private choice/configuration.** The product presents supported public, current-provider and Sage options. Show the operator, direction, supported scope, price and support boundary. The E-Invoice Service records explicit customer or delegate choice and action authority. It creates missing proposed subscription and connection configurations separately from active route state. For an existing provider or public route, record current directions and historical obligations. Before any external change, configuration failure or cancellation leaves the old route. A possible external effect requires ONB-08. Block unsupported mixed-scope combinations and explain the limitation. Do not widen scope silently.

For ONB-S03, bind the existing provider account and create only missing Sage configuration. Reuse a matching connection under its current version. Reopening ERP setup must not cause re-enrolment, credential replacement or receiving-destination publication. A required external change needs separate authority and a durable operation record. For ONB-S05, retain unchanged functions and configure only the requested addition. Before external mutation, return a limitation for unsupported provider interfaces or gated platform changes.

**ONB-06 Private readiness.** The E-Invoice Service validates approval for the operator, contract and customer group. It checks credentials, required trust, transport and profile conformance, and provider capabilities. For inbound functions, check required entry-point publication and discoverability. Store the intended value, external operation ID, independently observed value, source, observation time and freshness. A configured connection does not prove external readiness. If publication times out, record OUTCOME_UNKNOWN and invoke ONB-08. If reliable provider observation is unavailable, require a documented manual gate with named evidence and approver. The existing route remains selected.

Use the same SPEC-SEI-001 certificate dependency as ONB-03 where the selected provider requires it. Public authentication, private connection access and invoice signing remain separate purposes. Existing tax-use validity alone cannot satisfy all three. Reuse only a qualified reference and decision; return a precise unsupported-purpose result when the source contract cannot provide the required operation.

Inspect current receiving-point evidence and reuse it where valid. Publish or change the receiving point only when the selected plan and contract require it. Qualify sending, receiving and status functions independently. ONB-S04 keeps public and private results separate and records each execution owner. Successful private transport does not prove readiness for public copies or reporting. A possible external change can invalidate reachability before local route commit. Hold that scope under ONB-08. Do not assume the old route remains safe.

**ONB-07 Activation/cutover.** The E-Invoice Service rechecks the actor's permission and current readiness evidence. The route service locks the affected scope and records the expected route version. The cutover plan records the approved time and sequence, entry-point publication evidence, rollback trigger and customer notice.

The route service changes the route only if its current version matches the expected version. This check is **compare-and-set**. The change applies only to the authorised direction and scope, for invoices accepted after the agreed boundary. If external and internal states differ, do not report ACTIVE. Open ONB-08.

When the exchange service accepts an invoice, it saves that invoice's route version. The selected provider cannot change during processing of that invoice. After successful cutover, save the actual cutover time and return status for each direction. A single ONBOARDED flag must not hide different route states.

If ONB-10 proves the selected Sage route is valid and unchanged, omit route commit. Connecting an existing external provider can still require an explicitly selected initial Sage route. The provider can remain unchanged. Route activation requires separate customer authority. Phase 1 still prohibits route mutation. Private A → Private B remains disabled until the shared-foundation gate is approved.

**ONB-08 Recovery.** The E-Invoice Service owns the affected capability and route outcome. [SPEC-SEI-004](SPEC-SEI-004-onboarding-failure-and-reconciliation-solution-specification.md) defines failure classification, retry, correction, cancellation and reconciliation. Before repeating a mutation or claiming readiness, reconcile unknown effects with the original correlation or operation ID. If states differ, keep the transition blocked and assign a recovery case owner. After cutover, restoration is a new authorised transition. It requires current external-state and inbound-discoverability checks. Invoice origins remain unchanged.

**ONB-09 Continuity and release.** The E-Invoice Service retains old-route access for in-flight delivery, statuses, rejection and payment reporting, corrections, and audit. Apply confirmed actor and channel rules. Release the old entry point, registration, credentials and commercial relationship at separate approved gates. [Offboarding SPEC-SEI-003](SPEC-SEI-003-offboarding-solution-specification.md) governs a later full exit. If the historical execution path is unconfirmed, block release. This does not block a new-traffic cutover already supported by evidence.

**ONB-11 Return results and required actions.** After decisions are durable, the E-Invoice Service returns the authoritative work-item version through the Global API. For each requested function, include the business, environment, platform or service, and integration role. Include the connection reference and version, readiness and recheck evidence. Where applicable, include the selected route, version and effective boundary. Return activation evidence from the owning feature, limitations, next action and action owner. Keep request completion separate from setup and activation. Exact API fields require ONB-Q04. Do not introduce a state for the whole customer or rename readiness values.

The ERP can show **ready for supported public operations**, **sending active**, **receiving pending**, **existing setup confirmed**, or **connection unavailable**, as evidence permits. These are illustrative messages, not new technical states. If activation evidence is missing, report pending or unknown even when connection checks passed. Keep public-copy and reporting results separate from delivery and receiving. A setup result must not claim invoice acceptance, payment or completion of a legal report.

For unchanged setup, return valid existing references. Do not create a subscription, publish an entry point or commit a route. Notify the product and owning runtime feature when readiness changes. A failed recheck must not leave a misleading ready result. After a lost notification, read the authoritative version.

Before a dependent runtime action, its owner applies the required authority and credential-validity checks under SPEC-SEI-001 and the selected contract. Expiry, revocation or changed authority can block new use. Preserve prior evidence and invoice history. Setup completion is not indefinite permission to use a credential.

### 3 Logical requirements and quality controls

| ID | Requirement and PRD source |
|---|---|
| ONB-R01 | Before mutation, resolve the legal subject, tenant, environment and exact capability. Source: PRD-SEI-101/222. |
| ONB-R02 | Verify direct or per-client delegate authority for each action. Recheck before activation. Source: PRD-SEI-104/231. |
| ONB-R03 | Maintain separate readiness dimensions with evidence. Check certificates only where policy requires them. Source: PRD-SEI-101/226. |
| ONB-R04 | Return partial portfolio results. Isolate correction, cancellation and failure for each client. Source: PRD-SEI-104/107. |
| ONB-R05 | Allow private configuration and tests without changing the live route. Source: PRD-SEI-222. |
| ONB-R06 | Before cutover, require observed external inbound readiness and explicit authority for the scope. Source: PRD-SEI-222. |
| ONB-R07 | Process overlapping cutovers one at a time. Preserve the origin route for each invoice. Source: PRD-SEI-222/202. |
| ONB-R08 | Before retry or success, reconcile external mutations whose outcome is unknown. Source: PRD-SEI-107/222/225. |
| ONB-R09 | Preserve the historical actor, route and evidence. Release previous dependencies separately. Source: PRD-SEI-222/224. |
| ONB-R10 | Audit intent, decisions, mutations, observations, corrections and overrides. Include actor, scope, time and source. Source: PRD-SEI-225/226. |
| ONB-R11 | Assess existing services and requested outcome before planning missing work. Separate declared and observed facts. Use ONB-S01–08. Proposed refinement of PRD-SEI-101/222. |
| ONB-R12 | Reuse only qualified evidence. Confirm unchanged setup without external mutation. Extend only requested functions. Sources: PRD-SEI-101 readiness/recheck and PRD-SEI-222 continuity. This scenario refinement remains proposed. |
| ONB-R13 | Return setup, readiness and evidenced activation for each function through the common API. Do not use a global ONBOARDED flag. Sources: SPEC-SEI-013/014 and PRD-SEI-101/222. |
| ONB-R14 | Keep B2G/B2B service contexts, phase gates, unsupported providers and gated platform changes explicit. The owning invoice feature checks transaction applicability. Sources: scope boundaries and ONB-Q02–04. |
| ONB-R15 | The E-Invoice Service owns setup and recovery coordination. Any internal onboarding component remains proposed. Use existing API and dependency owners. Source: user ownership direction and ONB-Q05. |
| ONB-R16 | Reuse suitable Tax/certificate references under SPEC-SEI-001. Return safe readiness and customer actions. Failed lookup cannot imply absence or trigger repeat upload. Qualify authentication and signing separately. Sources: SPEC-SEI-001 CERT-03–06, CM-AC17/19 and ONB-Q06. |
| ONB-R17 | Require a verified business NIF before readiness. For certificate-based functions, also require a valid, suitable certificate and effective action authority. Record each result independently. Only approved NOT_REQUIRED policy permits the certificate exception. Sources: PRD-SEI-101 identity/readiness, SPEC-SEI-001 and user setup direction. |
| ONB-R18 | Separate case intake, per-function readiness, activation and later use. Qualify authentication, signing, retrieval and reporting for the actual actor and contract. Web-form access does not establish automated API access. Sources: SPEC-SEI-001, Article 11 and Article 7(3) cited in Part 1. |

Grant only the permissions needed for the approved purpose. Limit delegation to that purpose. Record who makes each support override. Overrides must not bypass external-observation or legal-policy gates. Encrypt sensitive evidence. Isolate tenants, entities and environments. Redact diagnostics and store credentials by reference only.

Define service objectives after measuring volumes, external propagation and recovery baselines. Monitor the age and count of pending, blocked, unknown and inconsistent items. Also monitor expiring grants and trust, stale entry points and failed cutovers. Assign an operations owner to each alert.

## Part 3 Logical Service Interactions and Data Inventory

This part describes what each service asks for, returns and stores. The technical field names support design review; they do not by themselves define an approved API.

### Spain and reuse boundary in contracts

Reuse one work-item and readiness contract while resolving country rules through versioned policies and provider adapters. The Spain public-readiness result must remain separate from private-route activation. Another country needs its own identity, representation, certificate and receiving-address evidence; it cannot inherit Spain’s readiness or transition sequence.

The relevant country and policy context may be resolved from trusted context or versioned references. Exact field names, service placement and physical APIs remain proposed. Reuse assessment must record the source implementation or design pattern, retained behaviour, local changes, missing functions, owner and qualification evidence before its dependent release gate passes.

### 1 Interaction contracts

These are logical contracts, not approved endpoints or physical service allocations. Every command carries requestId, correlationId, actor, tenant, legalSubject, environment, action, scope, expectedVersion and inputDigest as applicable. An error includes stable category, affected scope, safe retry class and responsible action; never a credential.

The E-Invoice Service owns the ONB workflow interactions and results. These contracts describe internal work and calls to dependency owners. They do not define a separately hosted onboarding API. The proposed internal component uses the same fields, authority checks and work-item versions.

| ID | Caller → logical owner | Input / output and safety |
|---|---|---|
| ONB-INT-01 | Product → E-Invoice Service | Open/get/cancel work item; idempotency key and digest; returns item/version and child outcomes; conflict on changed duplicate. |
| ONB-INT-02 | E-Invoice Service → identity/authority | Resolve legal subject and scoped decision snapshot; returns grant evidence, validity and reason; fail closed on unknown. |
| ONB-INT-03 | E-Invoice Service → capability policy and qualified Tax/certificate capability | Evaluate policy and required trust. Resolve an existing protected reference/version where supported. Return READY, limited, action, not-required or undetermined with evidence, source, recheck and action owner. Never return key material. Failed lookup remains unknown. ONB-03/06 consume the SPEC-SEI-001 readiness result; exact contract requires ONB-Q06. |
| ONB-INT-04 | E-Invoice Service → external verification adapter | Perform approved read/check or mutation only under a versioned contract; record operation ID, safety class, external reference and observed result. |
| ONB-INT-05 | E-Invoice Service → subscription/connection | Store proposed commercial and technical context; returns independent states; cannot select active route. |
| ONB-INT-06 | E-Invoice Service → entry-point/provider adapter | Publish or inspect supported entry point; intent and observed state remain distinct; unknown result invokes ONB-INT-08. |
| ONB-INT-07 | E-Invoice Service → route/exchange | Compare-and-set cutover for exact direction/scope and effective boundary; route version returned and bound to new invoices. |
| ONB-INT-08 | Operations / E-Invoice Service → adapter | Query/reconcile original external operation; returns confirmed, absent-safe-to-retry or unresolved with evidence; no duplicate mutation. |
| ONB-INT-09 | E-Invoice Service → product/operations | Emit state-changed/case-opened notification after durable commit; consumers deduplicate by eventId and version. |
| ONB-INT-10 | E-Invoice Service → connection/route and qualified adapters | Read current setup for an authorised business/environment and requested functions; return versioned configuration, observations, source/freshness and limitations; no external mutation or universal directory assumption. Consumed by ONB-10. |
| ONB-INT-11 | E-Invoice Service → Global API → ERP/product | Return per-function setup/readiness and independently evidenced activation, selected references, limitations and owned actions; query by item/version after a lost notification. Consumed by ONB-11; exact field mapping requires ONB-Q04. |

Events are proposed ONBOARDING_ITEM_CHANGED, PUBLIC_READINESS_CHANGED, PRIVATE_READINESS_CHANGED, ROUTE_CUTOVER_OBSERVED and ONBOARDING_RECOVERY_OPENED. Delivery is at least once, so the same event may arrive again; consumers recognise repeats and read the authoritative work-item version. A notification is never the sole proof of an external side effect. External adapter capabilities (query, idempotency, publication, revocation, acknowledgement) are registered per provider and environment; unsupported operations become explicit manual gates.

### 2 Data inventory

| ID | Record / owner | Essential fields and handling | Consumers |
|---|---|---|---|
| ONB-D01 | Onboarding work item / E-Invoice Service | Immutable request scope/digest; mutable state/version, phase, owner, deadline, child links, reason; restricted | Product, operations |
| ONB-D02 | Legal subject and authority snapshot / identity | Tenant/entity key, verified identity reference, actor, mandate, action, scope, valid interval, evidence reference; versioned/restricted | ONB-02, ONB-07 |
| ONB-D03 | Capability policy and readiness / policy and E-Invoice Service | Policy version, phase, dimension, result, source, observedAt, validUntil, next action; append decision history | ONB-03/04/06 |
| ONB-D04 | Trust reference / certificate capability under SPEC-SEI-001 | Purpose, protected material reference/version, readiness, evidence/source, next recheck and action owner. The E-Invoice Service retains safe references and results. The confirmed custodian retains credential material. Never store key bytes here. | ONB-03/06, ONB-11 |
| ONB-D05 | Subscription and connection / respective owner | Operator, terms/entitlement, environment, transport/profile, independent state, credential reference | ONB-05/06 |
| ONB-D06 | Entry-point intent/observation / operator adapter | Direction/scope, intended value, external reference, observed value/source/time, safety class, operation ID | ONB-06/08 |
| ONB-D07 | Route transition / route | From/to route, expected version, effective boundary, approval, observed state, rollback case and outcome | ONB-07/09 |
| ONB-D08 | Invoice origin / exchange/records | Invoice ID, original operator/route/profile, route version, accepted time and external correlations; immutable | ONB-07/09, offboarding |
| ONB-D09 | Recovery/evidence case / operations | Fault class, original operation, intended/observed state, owner, safe action, evidence with sensitive values removed and audit timeline | ONB-08 |
| ONB-D10 | Current-setup assessment and plan / E-Invoice Service | Scenario/intent, requested functions, declared versus observed facts, source/time, configuration versions, retained evidence, missing checks and per-function plan; restricted/versioned; authoritative connection/route records stay with their owners | ONB-10, ONB-03–08/11 |
| ONB-D11 | ERP capability result / E-Invoice Service | Work-item version, per-function connection/readiness/activation references, effective boundary, limitations, next action and owner; derived from committed evidence, access controlled and rebuildable | ONB-11, Global API, ERP/product, support |

Retention and deletion periods are set by approved legal, privacy, contract and evidence policy per data class; none are inferred here. D02/D04/D05 references are access controlled. D08 remains available to explain later statuses and reports after route change. All records include tenant/entity/environment partition keys and audit attribution.

## Part 4 Assurance and Traceability View

This part shows how requirements connect to activities, interfaces, data and acceptance checks. The scenarios describe evidence still needed; they are not a claim that implementation tests have passed.

### 1 Verification matrix

| Scenario | Requirement → activities / contracts | Evidence and expected result |
|---|---|---|
| ONB-A01 Direct public readiness | R01–03 → ONB-01–04 / INT-01–04, D01–04 | One entity/capability returns evidenced readiness or precise limitation; no private route changes. |
| ONB-A02 Accountant partial portfolio | R01–04 → ONB-01–04 / INT-01–03, D01–03 | One invalid client remains blocked; authorised clients continue; no shared grant or credential inference. |
| ONB-A03 Corrected NIF or grant | R01–03, R10 → ONB-02/03 / INT-02–04 | New evidence revision is checked; earlier decision and external operation remain auditable. |
| ONB-A04 Configure private without activation | R05 → ONB-05/06 / INT-05/06, D05–07 | Existing inbound/outbound routing is unchanged through tests and failure. |
| ONB-A05 Scoped cutover | R06/07/09 → ONB-06/07/09 / INT-06/07, D06–08 | Only authorised direction changes after evidenced boundary; earlier invoices retain origin. |
| ONB-A06 Publication timeout | R08/10 → ONB-08 / INT-08, D06/09 | Outcome unknown is visible; no second mutation until observed or manually resolved. |
| ONB-A07 Overlapping transitions | R07 → ONB-07 / INT-07, D07 | Only one transition passes the expected-version check. The other receives a conflict or waits in the queue; both cannot activate overlapping routes. |
| ONB-A08 Rollback after live invoices | R07–10 → ONB-08/09 / INT-07–09, D07–09 | Restoration has new evidence; invoices on each side keep actual route. |
| ONB-A09 Country-bound onboarding reuse | R01–03/06/10 → ONB-02/03/06, INT-02–04/06, D02/03/06 | The same workflow selects separate approved country policies. Spain identity and entry-point rules do not run for another country; missing local policy blocks readiness or activation. Existing Spain evidence remains unchanged. |
| ONB-A10 Shared foundation and understandable results | R03/05–09 → ONB-04/06/07/09; SPEC-SEI-014 SPC-03/04/08, SPC-A01/03/05/09 | Setup returns passed/failed/unknown checks and named required actions without activating a route. Platform change states direction and boundary, uses one Routing owner, and preserves existing provider connections and historical context when an operator role is added. |
| ONB-A11 First-time public/private choices, S01 | R01–03/05/06/11/13 → ONB-01–07/10/11, INT-01–07/10/11, D01–07/10/11 | Supported public choice returns readiness without route mutation; private choice uses separate activation gates. ERP can distinguish ready from active; no silent selection. |
| ONB-A12 Existing public service, S02 | R02/03/11–14 → ONB-02–04/10/11, INT-02–04/10/11, D02–04/10/11 | External public use without Sage authority returns the missing action. With valid matching evidence, omit repeated work; do not infer registration or active exchange. |
| ONB-A13 Existing private provider, S03 | R05/06/11–13 → ONB-05–07/10/11, INT-05–07/10/11, D05–07/10/11 | Retain the current provider, bind its account and check functions; no duplicate enrolment/subscription/publication. Initial Sage route requires explicit authority even when provider is unchanged. |
| ONB-A14 Public/private combination, S04 | R03/06/08/11/13/14 → ONB-03–08/10/11, INT-03–08/10/11, D03/05–07/09–11 | Independently qualify public and private functions; partial failure preserves unaffected selection but dependent invoice actions remain gated. Reject overlapping unsupported routes and prove one executor per delivery action. |
| ONB-A15 Confirm/extend Sage setup, S05 | R03/11–13 → ONB-03–07/10/11, INT-03/05–07/10/11, D03–07/10/11 | Valid unchanged setup returns existing references with zero external mutation and no new route version. Extension adds only requested supported functions; stale evidence is rechecked. |
| ONB-A16 Gated or supported migration, S06 | R06–09/11/14 → ONB-05–11, INT-05–11, D05–11 | Supported change preserves actual historical context. Private A → Private B remains blocked before approval; a diagram cannot enable it. |
| ONB-A17 B2G and transaction boundaries, S07 | R11/14 → ONB-03/10/11, INT-03/10/11, D03/10/11 | FACe/B2G use cannot satisfy B2B service readiness. B2C/international context is retained without a business-wide exemption or blanket applicability decision; owning invoice features evaluate individual transactions. |
| ONB-A18 Unsupported/unknown setup, S08 | R08/11/13/14 → ONB-01/08/10/11, INT-01/08/10/11, D01/09–11 | Unsupported provider/function returns a precise limitation without substitution or mutation. Failed lookup is unknown, not absent; a possible effect uses SPEC-SEI-004. |
| ONB-A19 Evidence and implementation reuse | R03/11/12/14 → ONB-03/06/10, INT-03/04/10, D03–05/10 | Changed country, role, purpose, environment, policy or credential version prevents unsupported evidence reuse. Record source build/contracts, local changes, gaps and owner before activating reused components; qualify relevant DTS coverage in its owning spec. |
| ONB-A20 ERP result and concurrent setup | R07/08/10–13 → ONB-07/08/10/11, INT-07–11, D07/09–11 | Stale setup/route versions cannot overwrite a concurrent change. Repeated result reads and lost/duplicate notifications return the authoritative version; readiness or a recovered external operation alone never claims active exchange. |
| ONB-A21 E-Invoice Service ownership | R15 → ONB-01–11, INT-01–11, D01/03/09–11; SPEC-SEI-004 | ERP requests use the existing Global API and E-Invoice Service. Internal workflow calls do not require a separate onboarding service. Record component reuse candidates, gaps and owners before build; no proposed component is treated as deployed. |
| ONB-A22 Existing suitable certificate | R03/12/16 → ONB-03/06/11, INT-03/11, D03/04/11; SPEC-SEI-001 CM-AC17 | Reuse the protected reference only when subject, authority, purpose, role, country, environment and versions match. Verify current validity. No duplicate upload or credential copy enters the E-Invoice Service or ERP. |
| ONB-A23 Certificate correction or unknown lookup | R08/13/16 → ONB-03/06/08/11, INT-03/08/11, D03/04/09/11; SPEC-SEI-004 | Confirmed missing, expired, revoked or unsuitable credentials return owned actions. Missing authority remains separate. Unavailable, stale or ambiguous lookup cannot prove absence, trigger repeat upload or renew readiness. Preserve independent valid functions. |
| ONB-A24 Certificate feedback and protected execution | R03/14–16 → ONB-03/06/11, INT-03/11, D03/04/11; SPEC-SEI-001 CERT-05/06 | ERP receives safe readiness and next actions. Readiness or tax-only certificate validity cannot enable unqualified public authentication, private access or invoice signing. Qualify the actual execution contract and owner for each selected purpose before use. |
| ONB-A25 Both NIF and required certificate | R01–03/13/17 → ONB-02–04/06/11, INT-02/03/11, D02–04/11 | Valid NIF with an unsuitable required certificate cannot produce READY. A valid certificate with unverified business NIF cannot produce READY. Both passing still require action authority. Approved NOT_REQUIRED retains NIF and authority checks. The delegate's identity cannot replace the business NIF. |
| ONB-A26 Intake before readiness | R01/03/13/17/18 → ONB-01–04/06/11, INT-01–03/11, D01–04/11 | An authorised Sage request can open a scoped case while NIF or certificate checks are pending. No default upload is required. The case cannot claim readiness, activate a route or start a dependent platform operation before its gates pass. |
| ONB-A27 Operation, actor and runtime boundaries | R02/03/16/18 → ONB-02/03/06/11, INT-02/03/11, D02–04/11; SPEC-SEI-001 | A Cl@ve web-form option cannot qualify an unproven automated API path. Authentication cannot substitute for signing or grant retrieval/reporting authority. Record the approved credential owner and actor per function. Required runtime rechecks block expired, revoked or unauthorised new use without rewriting prior evidence. |
| ONB-A28 Scenario and diagram correlation | R03/08/11–18 → ONB-01–11, INT-01–11, D01–11; SPEC-SEI-001/004 | Map ONB-S01–08 to the process and sequence groups. Shared action names and IDs agree. Both views distinguish certificate requirement from readiness, valid reuse from correction/unknown evidence, and readiness from activation. Confirmation creates no mutation; mixed results preserve valid independent functions. Recovered work resumes its exact gate. |

### 2 Review and release gates

**Reviewable now:** logical separation, lifecycle, failure model and proposed contracts. **Public pilot gate:** approved capability/representation and external API policy; authority and conditional trust policy; per-client isolation, cancellation and unknown-outcome drills. **Private pilot gate:** selected operator and provider capability matrix; verified entry-point mechanism/sequence; observed readiness and scoped route granularity; historical obligations decision table; rollback and concurrent-cutover drills. **Production gate:** approved legal/operator terms, threat review, conformance evidence, support runbooks and ownership, measured service objectives and monitoring, retention policy, and passed end-to-end pilot evidence.

Open decisions in Part 1 must be recorded with owner, source, date and accepted outcome before their dependent paths are enabled. Where the official interface or legal actor is unknown, the product exposes a blocked/manual gate and does not assert that onboarding is complete.

**Component and certificate reuse gate:** resolve ONB-Q05/06 with actual service-owner evidence. Prove saved workflow and recovery behaviour in the E-Invoice Service. Qualify Tax/certificate lookup, safe feedback, source/version binding and each required protected operation. Confirm implementation gaps before build and customer actions before pilot. SPEC-SEI-001 retains the certificate lifecycle gates; this spec does not approve a new custodian or signer.

**Scenario/API pilot evidence:** exercise ONB-S01–08 against qualified contracts and actual API/result mappings, including existing account binding, zero-mutation confirmation, stale-evidence refresh, mixed public/private partial results and scenario correction. Reconcile failures under SPEC-SEI-004 before resuming the precise parent gate. ONB-Q01–04 remain release gates; this scenario expansion does not establish broader B2G/B2C/international support, a deployed API or a newly approved migration mode.
