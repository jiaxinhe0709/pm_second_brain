---
id: SPEC-SEI-048
title: Shared Error Handling and Operational Support
type: solution-spec
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-11-23
updated: 2026-11-23
reviewers: []
related:
  - PRD-SEI-107
  - PRD-SEI-215
  - PRD-SEI-225
  - SPEC-SEI-004
  - SPEC-SEI-011
  - GLO-SEI-001
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Shared Error Handling and Operational Support

## 1 Purpose and authority

Support, Enablement and Engineering need to find failed work, explain the evidenced cause and complete permitted recovery without routine engineering intervention. Customers need an accurate result and a safe next action. This document owns the proposed operational requirements common to the [stage documents](README.md#stage-documents). The stage and functional specifications own their business decisions and recovery boundaries.

PRD107 already covers onboarding errors and recovery. PRD215 covers shared resilience. PRD225 covers observability, cases, safe actions and audit across the phases. The stakeholder note adds explicit search, historical investigation, version visibility and portal/bulk recovery needs. These are draft requirements for qualification, not evidence that a portal or action is implemented. OPS-S01–04 below identify their authority. Use the [shared glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md).

## 2 Common operational requirements

| ID | Actor, condition, required behaviour and result | Basis |
|---|---|---|
| OPS-R01 Find affected work | An authorised investigator can search by dataset, customer/business, e-invoicing address, region/country and environment. Invoice searches also support date range, invoice number, sender, recipient, invoice ID, invoice type, business status and error status. Search by a known ERP or external reference without first knowing an internal connection ID. List permitted matches and show ambiguity. A failed search is not an empty result. | OPS-S01/02 FR1–4; OPS-S03 visibility/search |
| OPS-R02 Inspect scope and versions | For each result, show the applicable ERP integrations and regional connections, enabled functions, intended and observed state, evidence time/freshness and configuration history. Show API, integration and deployed version references where recorded. Mark unavailable version evidence explicitly. A version change is a possible cause until the evidence confirms it. Cross-region views include only authorised scope. | OPS-S01/02 FR1/2/21; OPS-S03 connections/versioning |
| OPS-R03 Explain every error | Preserve each error's operation/attempt, stage, exact source code and source version, response level/field where supplied, occurrence time and safe diagnostic reference. Distinguish customer data, authority, authentication/certificate, configuration, Sage product/platform, connector, external platform and unknown causes. Mark the cause confirmed or suspected. Show clear wording, impact, next action and accountable owner; do not invent a root cause or collapse multiple errors into one. | OPS-S01/02 FR4/21; OPS-S03 diagnosis; OPS-S04 |
| OPS-R04 Read historical activity | Show a time-ordered, correlated record of requests, attempts, configuration/region changes, user and operational actions, outcomes and evidence. Keep event time and observation time distinct. Record gaps rather than implying complete history. Historical search must cover the approved investigation period and remain usable after temporary files or runtime logs expire. | OPS-S01/02 FR25, NFR6; OPS-S03 history |
| OPS-R05 Assess recovery eligibility | Before offering or executing an action, check current role/authority, business, country, environment, original operation, prior effects, current version, source contract and runbook. Show the failed checkpoint, permitted action, expected impact and blocking reason. Enforce the owning stage's rules for both automatic and manual actions. Existing failure rules remain authoritative; portal access adds no override. | OPS-S01/02 FR8–12; OPS-S03 portal recovery |
| OPS-R06 Recover through the portal | An authorised operator can execute each enabled routine recovery action through the operational portal and inspect its progress/result. Preserve the original operation and attempt history; corrections create linked revisions under the stage rule. Prevent concurrent conflicting actions. Unqualified or unsafe actions stay unavailable with a reason and owner. Record actor, reason, time, runbook/policy version, affected identities, preconditions, attempts and resulting evidence. | OPS-S01/02 FR11/12/25; OPS-S03 self-service |
| OPS-R07 Recover several items | Before a bulk action, show the selected scope, eligible items, exclusions and intended effects. Recheck permission and eligibility for each item at execution. Return separate results and preserve completed work when another item fails, changes or loses authority. Stopping queued bulk work cannot declare an in-flight external effect absent. Bulk execution is a proposed extension; limits and approval thresholds remain open. | OPS-S01/02 FR10–12; OPS-S03 bulk recovery |
| OPS-R08 Own and close the case | Show the Sage case owner, technical/dependency owner, next action, escalation and applicable deadline exposure. Monitor failed/stuck work, age, backlog, unknown outcomes and recovery failures using approved thresholds. Close only after the customer outcome and remaining obligations are evidenced or explicitly handed over. | OPS-S01/02 FR3/5–7/13/17; OPS-S03 troubleshooting |
| OPS-R09 Protect investigation evidence | Apply least privilege, tenant/client and environment isolation to search, detail, audit and recovery. Mask tax identifiers and invoice content for the viewer's role. Keep secrets, private keys and raw sensitive payloads out of logs, messages and ordinary support exports. Preserve safe correlation and protected evidence references. | OPS-S02 NFR3/4/6; OPS-S03 correlation |

Operation safety classes and reconciliation-first recovery remain in [PRD225 — Operation safety classes](../../prds/PRD-SEI-225-operations-resilience-support-reconciliation.md#operation-safety-classes). Retry budgets, numerical limits and escalation periods must be qualified per operation. The stakeholder's reported **six-day retention** is an unverified implementation concern. INT-ERR01's **six-day support guidance** is a different, code-specific source statement. Neither defines the required retention period, retry window or Spain reporting allowance. OPS-S03/04.

## 3 Stakeholder request coverage

| Note topic | Requirement / stage owner |
|---|---|
| Connections across regions, configuration and API versions | OPS-R01/02; SPEC004 onboarding operations |
| Complete history and successful/failed attempts beyond temporary retention | OPS-R04/09; every stage |
| Dataset/file transformation search, stuck work, mapper/ruleset/DTS versions | OPS-R01–04/08; SPEC049 |
| Customer readiness, prerequisites, Sage/external identifier relationships | SPEC004 onboarding operations; OPS-R01–04 |
| Invoice journey, submission evidence, status and filters | OPS-R01–04; SPEC050–052 |
| Distinguish Sage, connector and external errors; end-to-end correlation | OPS-R02–04/09; SPEC011 retains SPFE code bindings |
| Portal and bulk retries/replays with history | OPS-R05–08; each stage qualifies its permitted actions |
| Regional registration or “Registered for the Public Platform” | SPEC004 must show only evidenced external records. No SPFE registration operation or state is introduced by this note. |

## 4 Spain use, reuse and implementation evidence

Intended Spain use covers Phase 1 SPFE, enabled Phase 2 providers and the proposed Phase 3 Sage operator scope. These phase labels do not confirm delivery. Search, case history and guarded recovery are reusable design patterns. Existing support/case/search capabilities are implementation reuse candidates; Operations and Engineering must identify their actual builds, coverage, gaps and evidence. Actual implementation coverage is unknown.

Country and provider bindings select authority, regional configuration, exact codes, retry safety, deadlines and historical-route access. Spain identity, public-copy and reporting rules remain in the owning Spain specs. They must not become defaults for another country. Existing DTS is the preferred transformation candidate; [SPEC049](SPEC-SEI-049-transformation-and-validation-error-handling.md) qualifies its local mappings and recovery support. This document selects no new service, store or API.

## 5 Acceptance and open gates

| Check | Required evidence |
|---|---|
| OPS-A01 Search and explain | Demonstrate OPS-R01–04 with dataset-only, legal invoice number and external-reference searches, ambiguous matches, several errors, missing version evidence and unavailable search. |
| OPS-A02 Historical investigation | Demonstrate OPS-R04 after temporary artefact expiry; show retained successful/failed attempts, version lineage and explicit historical gaps. |
| OPS-A03 Guarded portal and bulk actions | Demonstrate OPS-R05–07 with mixed eligible/blocked/completed items, revoked permission, concurrent action and uncertain external result. No item bypasses its stage rule. |
| OPS-A04 Country and access isolation | Demonstrate OPS-R02/09 with another tenant/client, region, country and test/live context. A Spain code or runbook cannot enable another country's action. |
| OPS-A05 Case closure | Demonstrate OPS-R08 with a completed retry but unresolved external outcome, retained deadline exposure and named handover. |

Operations/Product own retention/search periods and portal/bulk release scope. Security owns recovery roles and bulk approval thresholds. API/Integration owners qualify identifiers, per-operation semantics and version evidence. Engineering/Operations own existing-tool coverage, alert thresholds and case ownership. Missing decisions block the dependent capability; they do not justify fabricated history or unsafe recovery. The checks above are required evidence, not executed product tests.

## REF Source references

| ID | Source/version and locator | Supported claim and limit |
|---|---|---|
| OPS-S01 | [PRD107](../../prds/PRD-SEI-107-public-onboarding-failure-recovery.md), Functional requirements FR1–20; [PRD215](../../prds/PRD-SEI-215-resilience-recovery-reconciliation-structured-review.md), Overview and operational recovery sections; repository drafts read 23 November 2026. | Canonical product scope for error classification, safe recovery and operational access; no proof of build coverage. |
| OPS-S02 | [PRD225](../../prds/PRD-SEI-225-operations-resilience-support-reconciliation.md), Phase and outcome, FR1–25, NFR1–8 and Acceptance criteria; repository draft read 23 November 2026. | Shared operations, evidence, ownership and audit. Does not approve this portal's interface, bulk limits or retention duration. |
| OPS-S03 | Stakeholder operational/troubleshooting note supplied by the user, received 23 November 2026; source date/authoritative version not supplied. Synthesised in §3. Earlier ERP use-case table received in the same chat. | Support, Enablement and Engineering requests. Reported six-day retention and existing limitations are unverified. Draft analysis input; not an approved external contract or production finding. No raw export is copied here. |
| OPS-S04 / INT-ERR01 | [Supplied FR invoice-flow error guide extract](<../../context/FR API/Shared/invoice-flow-error-handling-guide-extract.md>), received 22 October 2026, Processing and error fields, code dictionary and interpretation limits. | Exact FR attempt fields and source-specific guidance. Does not establish AEAT codes, retention or Spain support. |
| OPS-S05 | [SPEC011 — SPFE response and error matrix](../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix); [reviewed local release](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026), 23 November 2026. | Authoritative project binding and source limits for SPFE errors. Stage documents reference it rather than copying the catalogue. |
