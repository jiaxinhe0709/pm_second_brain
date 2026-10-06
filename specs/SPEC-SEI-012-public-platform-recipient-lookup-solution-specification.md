---
id: SPEC-SEI-012
title: Public Platform Recipient Lookup Solution Specification
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-06
updated: 2026-10-06
reviewers: []
related:
  - PRD-SEI-101
  - PRD-SEI-105
  - PRD-SEI-214
  - PRD-SEI-223
  - PRD-SEI-226
  - PRD-SEI-231
  - PRD-SEI-233
  - SPEC-SEI-002
  - SPEC-SEI-007
  - SPEC-SEI-011
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Public Platform Recipient Lookup Solution Specification

## Part 1 Feature Solution Summary

### Reader guide and design status

This **proposed logical design** answers where a recipient should receive an invoice in Spain's public/private invoicing model. It supplies evidence to outbound preparation and final exchange planning. The title describes the intended public-platform lookup use; it does not assert that AEAT currently provides a central recipient-directory API.

**Confirmed** identifies source-supported requirements. **Proposed** identifies behaviour, states and logical contracts needing design approval. **Open** identifies missing sources, access or decisions. **Out of scope** identifies another owner's responsibility. [Part 2](#part-2-logical-feature-specification) defines behaviour; [Part 3](#part-3-logical-service-interactions-and-data-inventory) defines contracts/data; [Part 4](#part-4-assurance-and-traceability-view) defines acceptance and gates. No endpoint or numeric cache lifetime is approved here.

### 1 Purpose, source authority and boundary

[PRD-SEI-223](../prds/PRD-SEI-223-interoperability-routing-transformation.md), FR1/3/5/29, requires explainable recipient-route evidence and an eligible representation. [SPEC-SEI-007](SPEC-SEI-007-spain-invoice-preparation-and-outbound-solution-specification.md), OUT-03/09/10, consumes an early indication and fresh final route evidence. [PRD-SEI-214](../prds/PRD-SEI-214-connections-registration-routing-structured-review.md) separately governs the issuer's own connections and routes. The issuer's connection does not reveal the recipient's destination.

| Evidence | Confirmed basis | Limit and consequence |
|---|---|---|
| [RD 238/2026, Article 6.1/6.3/6.4](https://www.boe.es/eli/es/rd/2026/03/25/238), checked 6 October 2026 | Defines the public receipt model, publication of private entry points and open operator consultation systems. More than one private entry point is possible. | Does not establish a central AEAT directory, a universal identifier query, or a precedence rule for competing sources. |
| [Order HAC/1028/2026](https://www.boe.es/eli/es/o/2026/10/02/hac1028), checked 6 October 2026 | Describes public invoice access services and their technical-contract dependency. | Invoice consultation is not evidence of recipient-directory support. Its third-party invoice-access permission cannot simply be applied to public directory lookup. |
| [Identity/tenancy PRD](../prds/PRD-SEI-231-country-identifiers-tenancy-and-delegated-accountants.md), [addressing PRD](../prds/PRD-SEI-233-peppol-multi-address-and-endpoint-routing.md) | Separate legal identity, tenancy, delegated actor and network address. | Country-qualified identities and network-specific endpoint semantics still require selected-source qualification. |

The proposed public-route decision follows OUT-09's safety rule: failed, stale, partial or ambiguous lookup is not proof that no private point exists. “Proven absence” means evidence sufficient under an approved Spain source/coverage policy, not an assumption that all directories can be exhaustively searched. RLU-Q01/Q03 must define how this condition can actually be met.

| In scope | Owning boundary |
|---|---|
| Exact recipient identity, action scope and source selection | Lookup with Identity/Spain policy owners. |
| Lookup execution, source observations and freshness | Lookup; [SPEC-SEI-011 connector](SPEC-SEI-011-public-platform-connector-solution-specification.md) only for qualified public-platform operations. Other operator sources use their own approved adapters. |
| Published destination candidates, private operational eligibility and public/unresolved classification | Lookup supplies versioned evidence; route/exchange services own final selection and plan. |
| Cache/coalescing, evidence refresh, conflicting results and controlled manual evidence | Lookup/Operations under source and country rules. |
| Draft versus final usage and historical evidence | Early result is advisory; final dispatch requires evidence meeting the current planning policy. |

**Out of scope:** invoice discovery/download; NIF/name census verification; onboarding or publishing/changing a recipient's entry point; customer route transitions; invoice validation/mapping/signing; dispatch, public-copy duties and buyer status. Tax identity matching does not establish receiving capability. This initial feature handles exact scoped lookup, not an unrestricted recipient search or directory export.

### 2 Outcomes, terms and actors

| Proposed outcome | Required evidence | Consumer behaviour |
|---|---|---|
| PRIVATE_READY | Published scoped destination plus qualified receiving/interconnection evidence and approved selection policy. | Supply destination/evidence to final planning; outbound still checks its own authority/profile. |
| PUBLIC_ROUTE_SUPPORTED | Approved policy establishes sufficient absence of an applicable private point under the approved absence-based public-receipt policy. Includes source/coverage and policy evidence. | Corresponds to OUT-09 PROVEN_NONE for its approved absence path. Final public execution still needs a qualified connector. |
| PRIVATE_OBSERVED_NOT_READY | Private point is evidenced, but required interoperability/capability is unsupported or unavailable. | Hold; public fallback is not inferred from a private outage. |
| UNRESOLVED | Lookup FAILED, STALE, AMBIGUOUS, PARTIAL, UNSUPPORTED or EVIDENCE_INSUFFICIENT. | Hold final dispatch; provide safe reason, owner and next action. |
| DENIED / INVALID_REQUEST | Actor, scope or qualified identity is invalid. | No unauthorised external lookup or destination disclosure. |

A **recipient** is the invoice buyer/legal party. An **entry point** is the published receiving destination; it need not be a raw URL. A **candidate** is an observed point not yet approved for this operation. **Freshness** means whether evidence is current enough for a defined use. **Coverage** explains what a source's positive or negative answer actually covers. A **snapshot** preserves the source, time, scope and policy used for one decision. **Negative caching** means temporarily reusing a prior absence observation under the same coverage/freshness rules.

ERP/preparation requests the early indication; exchange requests final evidence. Identity validates qualified recipient keys. Lookup/source adapters collect observations. Routing/Interoperability qualifies destination capability. Compliance owns Spain public-default and source precedence rules. Operations resolves source/conflict incidents without overriding authority or forging absence evidence.

### Spain use and reuse boundaries

| Area | Intended Spain use | Reuse classification | Condition and owner |
|---|---|---|---|
| Observation, cache and decision evidence | Keep source scope, timestamp, freshness and conflict history. | Reusable proposed design pattern | Lookup/Architecture: qualify actual store, isolation, concurrency and invalidation. |
| Identity, source precedence and destination selection | Resolve exact party and document/receiving capability. | Shared capability requiring country/network binding | Identity/Routing: bind scheme, lookup key, agreements, profiles and interconnection evidence. |
| Public/private receipt policy | Apply Spain's approved publication/default and coverage rules. | Spain-specific | Compliance/Spain technical owner: evidence sufficient for public-route decision, multi-point selection and applicability. |
| Existing recipient discovery or AEAT directory | Assess available Sage/source implementation. | Coverage unknown | Record exact source/build/contract, gaps, owner and tests; no central directory is proven here. |
| DTS | No transformation performed by lookup. | Out of scope here | Exchange uses DTS as preferred qualified transformation candidate when needed. A mapper cannot establish directory or destination support. |

### 3 Process and lifecycle

![Recipient lookup process](../assets/diagrams/public-platform-recipient-lookup-process.svg)

[Editable Draw.io](../assets/diagrams/public-platform-recipient-lookup-process.drawio) · [PNG preview](../assets/diagrams/public-platform-recipient-lookup-process.png).

Text equivalent: RLU-01 accepts early/final intent → RLU-02 checks identity/authority → RLU-03 fixes source/coverage/freshness policy → RLU-04 reuses qualifying evidence or coalesces refresh → RLU-05 queries approved sources → RLU-06 saves candidates and conflicts → RLU-07 checks capability and approved selection → RLU-08 saves private/public-supported/unresolved decision → RLU-09 hands evidence to the consumer. Failure, incomplete negative evidence and competing points remain held; RLU-10 performs bounded recovery/version changes without rewriting earlier plans.

| Activity / trigger | Preconditions, operation and result | Owner/error recovery |
|---|---|---|
| RLU-01 Lookup request / ERP or exchange | Workload scope, request/operation identity and use EARLY or FINAL; save request digest/correlation. | Lookup: same key/digest returns result; changed request conflicts. |
| RLU-02 Identity/authority / accepted request | Qualified recipient key and permitted actor/purpose; separate recipient from issuer/delegate. | Identity/Security: invalid or cross-tenant context denied. |
| RLU-03 Source policy / valid scope | Activated country/environment/capability and approved source, precedence, coverage and freshness versions. | Spain/Routing: missing policy leaves unsupported. |
| RLU-04 Cache/refresh / source policy selected | Reuse exact compatible evidence or acquire generation-controlled refresh. | Lookup: stale/negative evidence cannot qualify by default. |
| RLU-05 Query / authorised refresh | Approved read contract, bounds and source access; save correlation/results or classified failure. | Adapter: timeout does not prove absence; side effects follow original-operation safety. |
| RLU-06 Interpret / source responses | Preserve all candidates, applicable scope, coverage and conflicts without arbitrary selection. | Lookup/Compliance: contradictory/incomplete evidence held. |
| RLU-07 Qualify destination / candidates | Check exact receiving/interconnection/format capability and approved multi-point selection. | Routing/provider owner: published but unsupported point held. |
| RLU-08 Decide / sufficient evidence | Commit immutable decision/ref/version or owned unresolved result. | Lookup: changed generation/policy prevents stale commit. |
| RLU-09 Consumer handoff / decision saved | Return reason/source/time/freshness, evidence limitations and expiry/recheck condition. | Exchange: final plan retains snapshot; early result cannot authorise send. |
| RLU-10 Recover/change / owner action or invalidation | Refresh same scope, attach authorised manual evidence, or change policy prospectively with audit. | Operations/Lookup: no silent historical reroute or forged success. |

### 4 Risks and decision surface

The largest risks are assuming a central directory exists, treating a local negative response as global absence, selecting an arbitrary point, confusing identity match with capability, or dispatching on stale evidence. RLU-Q01–Q08 name owners and gates for these matters in Part 4.

## Part 2 Logical Feature Specification

### 1 Model and invariants

Proposed request scope includes tenant, issuer legal entity, recipient identifier scheme/value, country, environment, invoice document/process capability, direction, decision time, use EARLY/FINAL and any evidenced agreement reference. Exact physical fields remain open. A country-qualified identifier is not a Sage tenant ID. The initial implementation needs only dimensions supported by the selected sources and use case; unsupported granularity must be explicit.

| ID | Rule that must always hold |
|---|---|
| RLU-I01 | Recipient party, issuer connection, delegated actor and receiving address are separate identities. |
| RLU-I02 | A positive source observation needs capability/selection qualification; an empty response needs coverage evidence before public-route use. |
| RLU-I03 | Failed, partial, denied, stale or unqualified negative results cannot become proven absence. |
| RLU-I04 | Evidence contains exact source, scope, observation time, effective interval/freshness, policy and version. |
| RLU-I05 | Early lookup is advisory; final dispatch references evidence qualified for the final use and time. |
| RLU-I06 | Multiple/conflicting entry points require an approved deterministic selection or remain ambiguous. |
| RLU-I07 | Public fallback is a Spain policy decision; private unavailability cannot trigger it automatically. |
| RLU-I08 | Later lookup/country-policy changes cannot overwrite historical plan snapshots or reroute an operation already sent. |
| RLU-I09 | Caller scope and cache partition prevent disclosure across tenant/entity/environment/country boundaries. |
| RLU-I10 | Lookup cannot mutate recipient registration, create a route or sign/submit an invoice. |

### 2 Detailed behaviour

**RLU-01 Accept early or final intent.** Authenticate caller and action. Save exact request scope, consumer operation, digest, use and idempotency identity. Same request identity/digest resumes current result; changed recipient/scope/use conflicts. EARLY requests support preparation and report limitations. FINAL requests must satisfy the current exchange planning policy; an old EARLY result cannot merely be relabelled FINAL. Cancellation ends unsent local work or suppresses the requested handoff while preserving observations; a network call already started cannot be assumed cancelled.

**RLU-02 Check identity and authority.** Resolve scheme-qualified party identity under the approved country rules, including normalisation that preserves meaning. Reject ambiguous/missing identifiers without inventing substitutions from names, user IDs or free text. PRD-SEI-101/231 own structural identity checks; a census match is not a destination lookup. Verify workload/tenant and actor purpose separately from external source access permission. Directory access may be open or authenticated under its confirmed source contract. Do not require a recipient's invoice-access power of attorney merely because invoice consultation uses one; RLU-Q02 establishes the correct lookup authority.

**RLU-03 Select source and coverage policy.** Resolve a versioned source registry by country/environment/use. It identifies approved source type, operation/schema, supported identifier and capability scope, freshness/invalidation, coverage/completeness meaning, precedence and evidence ownership. A public-platform lookup uses SPEC-SEI-011 only if that capability is qualified. The initial outbound public-route path is the approved absence path in OUT-09; any additional public-selection basis requires a recorded decision and aligned outbound contract before activation. Operator consultation or evidenced recipient publication uses its own approved access path. No scraping arbitrary sites or following caller-supplied URLs is introduced. A sanctioned manual source requires explicit provenance and reviewer controls.

The source policy must explain why a result is authoritative for this recipient and invoice scope. A single operator's “not registered here” normally establishes only that operator's result. Do not convert it to absence across the network. Policy must also account for express receiving arrangements; “no record found” cannot override an applicable evidenced private agreement by convenience.

**RLU-04 Reuse or refresh evidence.** Cache keys include trusted tenant/access scope, recipient scheme/key, country, environment, document/process capability, source/coverage policy and result version. The conservative proposed default keeps responses tenant-scoped. Any shared cache for genuinely public data requires separate Security/Privacy approval and cannot share private authority evidence or business relationships.

Check freshness for the requested use, source validity and invalidation before reuse. Expired negative evidence requires refresh; a failed refresh cannot extend its validity. Coalesce identical active queries with one scoped refresh generation while preserving consumer requests. Timeout for one waiter does not grant it permission to overwrite another worker's newer observation. Preserve prior successful evidence with its actual age and current degraded status. Numeric TTL, final-use freshness and invalidation mechanisms are RLU-Q04 decisions.

**RLU-05 Query selected sources.** Execute bounded reads using the approved contract and explicit scope. Save request/source correlation, observation time and continuation/completeness evidence. Apply access, transport, payload/resource and destination controls. Throttle or unavailable source returns classified failure; no false empty response. If result pages exist, incomplete pages cannot establish absence. A source call with possible side effects follows SPEC-SEI-011 or the source adapter's equivalent reconciliation rules before unsafe repeat.

Final lookup refresh uses fair bounded capacity; no unlimited fan-out over all platforms. RLU-Q01/Q03 defines selected sources and the sufficiency of their combined evidence. Physical request aggregation is unproven and not required.

**RLU-06 Preserve and interpret candidates.** Store each source observation and every returned entry point with its scheme/operator/reference, declared direction, supported document/process/profile scope, effective interval and source evidence. Where fields are absent, retain UNKNOWN rather than assume support. Duplicate observations may share an evidence link while retaining source history. An address is data, not authorisation to transmit or fetch from it.

Apply approved source precedence only within its proven scope. Two valid points may coexist; neither record order nor last response wins. Conflicting party ownership, publication/withdrawal or effective intervals remain AMBIGUOUS until approved evidence resolves them. Do not erase earlier conflicting observations. A partial positive result can identify a candidate, but must not claim a complete destination set or prove the absence of competing points.

**RLU-07 Qualify operational eligibility and selection.** Check the candidate's receiving direction/process, environment, format/profile compatibility and direct/interconnection or bridge capability using qualified provider/capability evidence. Published address, reachable website and TLS success are insufficient. Format conversion is owned by exchange; lookup may reference an activated conversion path but cannot infer that an existing mapper supports this route. Source facts and Sage capability decisions remain separately labelled.

For multiple eligible points, use a documented receiving arrangement or approved deterministic selection rule whose coverage matches the invoice. An invalid caller preference cannot override this rule. Missing precedence or unsupported required scope yields AMBIGUOUS/UNSUPPORTED. A private destination whose operation is temporarily unavailable is PRIVATE_OBSERVED_NOT_READY; no automatic public fallback is added.

**RLU-08 Commit decision evidence.** Persist request, candidate/absence observations, selected policy, eligibility/selection evidence, outcome/reason and immutable decisionRef/version. PRIVATE_READY requires the qualified point. PUBLIC_ROUTE_SUPPORTED requires the approved public-receipt basis; its absence path provides the PROVEN_NONE evidence expected by OUT-09. Otherwise persist UNRESOLVED with explicit reason and owner. No external destination query result is silently mapped to a universal boolean “is registered”.

Commit checks active refresh generation and policy version. A stale worker cannot overwrite a newer observation; a concurrent source/selection change is reevaluated or held. Failed commit recovers from saved source observations rather than treating an uncommitted result as authoritative. Country policy cannot change past evidence.

**RLU-09 Handoff to preparation/exchange.** Return decisionRef, outcome, qualified destination reference if any, exact scope, source/time, freshness/recheck condition, evidence limits, safe next action and owner. Include the version expected at plan creation. Exchange checks that final evidence still meets its applicability/freshness and execution policy immediately before freezing the plan; material change before the first external effect causes revalidation/replanning. Lookup cannot promise an atomic transaction with an external directory. The accepted final-use freshness window and residual change risk need RLU-Q04 approval.

After a leg is sent, any new lookup is additional evidence; it cannot change the original destination or reconciliation identity. Customer output says “destination unresolved” with a safe cause rather than “recipient cannot invoice”. Internal events carry evidence references without unrestricted endpoint URLs or full tax identifiers.

**RLU-10 Recover and evolve safely.** Refresh bounded scope after a transient outage, source invalidation or approved conflict resolution. Operations may inspect safe metadata or attach authorised manual evidence with provenance, verifier, applicability, expiry/recheck condition and audit. They cannot declare global absence from an unsupported source, overwrite source results or grant a missing business authority. Source withdrawal/revocation invalidates new use according to the agreed mechanism while preserving earlier observations.

Profile/source rollout is inactive-first and cohort-bound. Rollback restores a qualified source/policy for eligible new decisions, preserves operation identities and does not rewrite sent plans. Suspension stops new affected queries/handoffs where required; historical lookup evidence remains available to permitted support/reconciliation users under retention policy.

### 3 Requirements and operational controls

| ID | Requirement / source |
|---|---|
| RLU-R01 | Separate qualified recipient identity, issuer connection and action authority; PRD101/231/226. |
| RLU-R02 | Activate only evidenced source/coverage contracts; a central public directory is an open capability; PRD223 FR1/3 and source limits. |
| RLU-R03 | Preserve source observations, coverage, candidate scope, conflicts and effective time; PRD223 FR1/3, PRD214 FR23. |
| RLU-R04 | Reuse cached evidence only under approved scope/freshness; failures cannot renew positive or negative validity; PRD223 FR1 and OUT-09. |
| RLU-R05 | Require receiving/interconnection/profile qualification and deterministic multi-point selection; PRD223 FR5/29 and RD238 Article 6 model. |
| RLU-R06 | Distinguish private ready, public supported, private not-ready and unresolved; failed/partial lookup cannot select public by inference; OUT-09. |
| RLU-R07 | Make early result advisory and bind final evidence/version to immutable plan; OUT-03/09/10, PRD214 FR14/16. |
| RLU-R08 | Recover concurrent refresh/commit/query failures without stale overwrite, unsafe side effect or arbitrary selection; PRD223 resilience principles. |
| RLU-R09 | Protect access, audit manual evidence, bound queries and expose truthful freshness/ownership; PRD105/226, PRD214 FR23–27. |
| RLU-R10 | Isolate country rules and qualify reused source/build contracts before activation; PRD223/227 and repository reuse controls. |

Least privilege, encryption and data minimisation protect party keys, addresses and business relationships. Restrict exact-recipient queries; enumeration/rate controls, safe errors and purpose checks reduce directory abuse. Mask personal identifiers in ordinary logs and metrics. Track source availability, latency, cache reuse by use, aged negative evidence, ambiguous/multi-point results, unresolved final plans, invalidations and manual cases. Product/Operations agree volume/freshness/capacity and retry targets under RLU-Q04/Q08; no numeric objective is asserted here.

## Part 3 Logical Service Interactions and Data Inventory

### 1 Logical contracts

Logical commands use requestId, consumerOperationId, tenant/issuer scope, qualified recipient reference, country/environment, capability/direction, EARLY/FINAL use, decision time, policy version, digest, idempotency key and correlation. The approved source contract supplies exact fields. Responses retain operation safety separately from route outcome. DENIED, INVALID_REQUEST, CONFLICT, TEMPORARY_FAILURE and PENDING are operation states; UNRESOLVED reasons must not become private-absence evidence.

| ID / caller → owner | Contract, authority and result | Failure/correlation evidence | Activities |
|---|---|---|---|
| RLU-INT-01 Preparation/exchange → lookup | Submit/query/cancel local request; scoped EARLY/FINAL result with decisionRef and recheck condition. | Same key/digest returns operation; changed input conflicts; D01/D07. | RLU-01/09 |
| RLU-INT-02 Lookup → identity/authority | Resolve qualified party and purpose/source permission; effective decision refs. | Invalid/denied/undetermined before external access; D02. | RLU-02/05 |
| RLU-INT-03 Lookup → source policy/cache | Resolve activated source/coverage/freshness; read scoped evidence or claim refresh generation. | Stale/partial/negative checked explicitly; compare-and-set; D03/D04. | RLU-03/04/08/10 |
| RLU-INT-04 Lookup → approved source adapter | Exact recipient/capability read; public source via SPEC-SEI-011 only if qualified. | Save source correlation, candidates, coverage or failure; timeout not absence; D04/D05. | RLU-05/06 |
| RLU-INT-05 Lookup → routing/interoperability | Qualify candidate receiving scope and approved selection; source facts remain separate. | Ready/not-ready/ambiguous/unsupported with evidence/version; D05/D06. | RLU-07 |
| RLU-INT-06 Lookup → decision store/consumer | Commit immutable result and publish safe versioned evidence notification. | Stale generation/policy rejected; outbox recovery; D07/D08. | RLU-08/09 |
| RLU-INT-07 Operations → lookup/audit | Inspect/refresh/attach approved manual evidence/change source profile with reason/version. | Separate permissions; cannot forge absence/route change; D03/D09. | RLU-10 |

Proposed events: RECIPIENT_LOOKUP_DECISION_RECORDED, RECIPIENT_LOOKUP_EVIDENCE_INVALIDATED and RECIPIENT_LOOKUP_RECOVERY_REQUIRED. They contain scoped request/decision IDs, result version, reason, time and safe evidence references. Notifications follow durable commit and are at least once; consumers deduplicate and cannot regress to an older result. A latest invalidation prevents new use under policy but does not edit an existing sent plan.

### 2 Data inventory

| ID / record and owner | Essential fields and handling | Consumers |
|---|---|---|
| RLU-D01 Request / lookup | Scoped caller/consumer, exact recipient/capability/use/time, digest/key/correlation and cancellation; restricted, immutable request. | RLU-01–10 |
| RLU-D02 Identity/access decision / Identity | Scheme/key normalisation version, issuer/recipient distinction, action/source permissions and effective policy; sensitive, append-only references. | RLU-02–05/09/10 |
| RLU-D03 Source/country policy / registry | Source contracts, coverage/precedence, allowed scope/use, freshness/negative caching, selection/manual-evidence rules and activation/version; restricted/versioned. | RLU-03–10 |
| RLU-D04 Refresh/cache / lookup | Exact cache partition, generation/lease, source operation IDs, bounds/continuation, last observation/expiry/invalidation and safe failure; restricted/versioned. | RLU-04–06/08/10 |
| RLU-D05 Source/candidate observation / lookup + Records | Immutable response ref/hash, candidate scheme/operator/address reference, scope/effective interval, source/time, positive/negative/completeness meaning and conflict evidence; sensitive/append-only. | RLU-05–10 |
| RLU-D06 Eligibility/selection / Routing | Candidate refs, receiving/interconnection/profile evidence, agreement/selection policy/version and known/unknown reason; restricted/append-only. | RLU-07–10 |
| RLU-D07 Decision snapshot / lookup | Request/scope, candidate or approved public basis, source/coverage/time, policy/version, outcome, limitations/recheck, owner/next action; immutable. Exchange plan references it. | RLU-08–10 |
| RLU-D08 Result outbox / lookup | Event/decision/version, target consumer, delivery attempts/receipt and safe refs; restricted/replayable. | RLU-08–10 |
| RLU-D09 Recovery/manual/audit case / Operations + audit | Fault, actor/action/reason/version, source provenance/verifier and validity for manual evidence, owner/resolution/retention class; restricted/append-only evidence. | RLU-01/10 |

Sources are authoritative only within their approved coverage. Lookup owns its observations/decisions; Routing owns capability assessment; exchange owns the frozen plan. Cache expiry does not delete evidence used by historical invoices. Records/Privacy approve retention, holds, authorised historical access and deletion by data class under RLU-Q07.

### 3 Reuse qualification

Assess existing Sage recipient/discovery/cache services before creating a new physical service. Record actual build, supported country/key/capability, source contracts, retained shared behaviour, Spain changes, gaps, build/run owner and qualification evidence. A Peppol resolver, identity verifier or AEAT invoice-consultation adapter is not automatically a Spain B2B directory implementation. Any shared country engine needs separate policy packs; missing Spain source/absence policy blocks activation rather than inheriting another country's defaults. DTS remains a downstream transformation candidate, not recipient discovery.

## Part 4 Assurance and Traceability View

### Acceptance scenarios

| ID / scenario | Requirements → activities / interactions / data | Expected evidence and result |
|---|---|---|
| RLU-A01 Wrong identity/tenant/environment | R01/09 → RLU-01/02, INT-01/02, D01/D02/D09 | Denied before external lookup/disclosure; issuer/delegate identity not substituted for recipient. |
| RLU-A02 Source/capability unverified | R02/10 → RLU-03/05, INT-03/04, D03/D05 | Unsupported/held; invoice consultation or census success cannot invent directory support. |
| RLU-A03 One private candidate qualified | R03/05/06 → RLU-05–09, INT-04–06, D05–D08 | PRIVATE_READY with exact source/interval/capability and selected receiving point evidence. |
| RLU-A04 Sufficient absence/public basis | R02/03/06 → RLU-03/05/06/08, INT-03/04/06, D03/D05/D07 | PUBLIC_ROUTE_SUPPORTED only under approved coverage/policy; OUT-09 receives its PROVEN_NONE evidence for the absence path. |
| RLU-A05 One operator empty, other scope unknown | R02/03/06 → RLU-05/06/08, INT-04/06, D03/D05/D07 | Local absence retained; final result EVIDENCE_INSUFFICIENT, not global public-route inference. |
| RLU-A06 Timeout, throttle or incomplete pages | R03/06/08 → RLU-05/06/10, INT-04/07, D04/D05/D09 | Failed/partial result and bounded recovery; no false negative or renewed freshness. |
| RLU-A07 Expired positive/negative cache | R04/07 → RLU-04/05/09, INT-03/04/01, D03–D05/D07 | Refresh required by use; failed refresh leaves stale evidence explicit and final dispatch held. |
| RLU-A08 Multiple points/contradictory sources | R03/05/06 → RLU-06–08, INT-04–06, D05–D07 | Approved agreement/selection evidence or AMBIGUOUS; no first-row/latest-response selection. |
| RLU-A09 Published point lacks eligible capability | R05/06 → RLU-07/08, INT-05/06, D05–D07 | PRIVATE_OBSERVED_NOT_READY or unresolved; reachable URL/mapper alone insufficient; no public outage fallback. |
| RLU-A10 Early result differs before final plan | R04/07 → RLU-04/08/09, INT-01/03/06, D04/D07/D08 | Final-use policy reevaluated; stale EARLY result cannot authorise send; new plan references qualified snapshot. |
| RLU-A11 Concurrent refresh and stale worker | R04/08 → RLU-04/08/10, INT-03/06/07, D04/D05/D07 | One scoped refresh coalesced; old generation cannot overwrite new result; crash recovers saved observations. |
| RLU-A12 Source changes after sending | R07/09 → RLU-09/10, INT-06/07, D05–D09 | New evidence/invalidation recorded; original sent plan/destination and reconciliation identity unchanged. |
| RLU-A13 Cache isolation/enumeration/manual evidence | R01/09 → RLU-02/04/10, INT-02/03/07, D02/D04/D09 | Cross-tenant/private sharing and unauthorised enumeration/recovery denied; manual evidence retains verifier/provenance without forged absence. |
| RLU-A14 Country reuse and source rollback | R02/08/10 → RLU-03/08/10, INT-03/06/07, D03–D07/D09 | Actual source/build and country packs qualified; rollback preserves history; Spain public-default rules cannot apply to another country. |
| RLU-A15 Stateful query uncertainty and cancellation | R08/09 → RLU-01/05/10, INT-01/04/07, D01/D04/D05/D09 | Saved source operation reconciled before unsafe repeat; cancellation does not claim remote undo or absence. |
| RLU-A16 Duplicate intent and notification loss | R07/08 → RLU-01/08/09, INT-01/06, D01/D07/D08 | Same key returns saved operation; changed request conflicts; replayed/late notifications preserve newest decision. |

### Open decisions and release gates

| ID / question | Owner | Impact and evidence gate |
|---|---|---|
| RLU-Q01 Does an approved AEAT/SPFE recipient lookup exist, and which alternative sources cover the selected Spain scope? | Spain Technical/Integration owners | Blocks source adapter activation; obtain exact official/operator contracts, identifiers, query/completeness and environments. No asserted central directory. |
| RLU-Q02 What lookup purpose/access authority applies to each source? | Compliance/Identity/Security | Blocks live access; distinguish open directory consultation from represented invoice access, protect recipient personal/business data. |
| RLU-Q03 What evidence/precedence establishes private selection or sufficient public-receipt basis, including multiple entry points and receiving agreements? | Spain Compliance/Routing/Product | Blocks public-default and multi-point decision activation. Incomplete sources leave unresolved; agree relationship to OUT-09 PROVEN_NONE. |
| RLU-Q04 What freshness, negative-cache, invalidation and final-use window is acceptable? | Product/Routing/Operations/Compliance | Blocks automatic final planning on cached results; define limits from source guarantees and accepted change risk, not invented TTL. |
| RLU-Q05 What interconnection, receiving/process and profile capability makes a point eligible? | Interoperability/provider/Format owners | Blocks PRIVATE_READY; qualify exact evidence and selection scope, including required conversion paths outside lookup. |
| RLU-Q06 Which existing implementation and physical service boundary can be reused? | Architecture/Lookup owner | Blocks implementation readiness claim; record build, contracts, local changes, gaps, tenancy/generation safety and support owner. |
| RLU-Q07 What retention, shared-cache and manual-evidence controls apply? | Records/Privacy/Security/Operations | Blocks shared public-data cache/manual override/production evidence handling; approve purpose, provenance, holds and historic access. |
| RLU-Q08 What quotas, recovery limits, alert/service targets and on-call ownership apply? | Product/Operations/source owners | Blocks production capacity/support promise; baseline volumes, runbooks and source outage/conflict drills. |

**Design review:** establish Q01–Q06 and source/decision boundaries with outbound. **Pilot:** qualify selected sources and exercise A01–A16, especially incomplete absence, multiple points, stale negatives and final-use changes. **Production:** resolve Q07/Q08 and outstanding scope-specific contracts; require source/capability conformance, isolation, recovery/rollback evidence and named operations. The readiness is **reviewable logical proposal**; central-directory availability, production readiness and implementation tests are not claimed.
