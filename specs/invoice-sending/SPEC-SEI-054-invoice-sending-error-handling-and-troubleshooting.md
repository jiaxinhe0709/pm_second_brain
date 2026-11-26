---
id: SPEC-SEI-054
title: Spain Invoice Sending Error Handling and Troubleshooting
type: solution-spec
status: draft
owner: Jiaxin He
author: Samu Coco
product: spain-e-invoicing
created: 2026-11-25
updated: 2026-11-26
reviewers: [Jiaxin He]
related:
  - SPEC-SEI-048
  - SPEC-SEI-011
  - PRD-SEI-215
  - PRD-SEI-225
  - SPEC-SEI-022
  - SPEC-SEI-023
  - SPEC-SEI-024
  - SPEC-SEI-043
  - SPEC-SEI-049
  - SPEC-SEI-050
  - NOTE-SEI-002
  - GLO-SEI-001
  - RES-SEI-002
confluence:
  publish: false
  space_key: DNBU
  page_id: ""
---

# Spain Invoice Sending Error Handling and Troubleshooting

## Summary for review

- **PROPOSAL:** This draft defines ERP feedback and support troubleshooting for invoice sending.
- Scope: single, multiple and automatic sending, cancellation and correction; Phase 1/2.
- No new codes, fields or endpoints are defined. No troubleshooting mechanism is selected.

**Classification — §2**

- Success — the named action succeeded; other work stays separate.
- In progress — the request was accepted and its result is not final.
- Partial result — the selection has mixed results; show each invoice separately.
- Prerequisite not met — a required condition is missing; complete it or wait for it.
- Business rule — the state or input does not permit the requested action.
- Validation error — fix request data; use SPEC049 for generation/UBL issues and hold sending.
- Authentication-configuration error — fix caller access, credentials, certificate or settings.
- Platform rejection — show the platform's refusal and permitted next action.
- Technical-transient error — a service failed; do not assume resending is safe.
- Unknown outcome — an action may have happened; reconcile before conflicting work.

**Minimum information for Ops Tooling team — §3**

- Search
- Company and invoice
- Request and route
- Stopped step
- Times
- Platform answer
- Attempts
- Current results
- Next action

**Examples — §4**

- SS09: Accepted send still running → In progress → check the existing request.
- SS12: No sending platform → Prerequisite not met → finish setup or choose a permitted platform.
- SS15: Timeout after possible sending → Unknown outcome → reconcile the original action.
- MS08: Mixed batch → Partial result → show each invoice; recover only eligible failed actions.
- CN07: Already cancelled → Business rule → return the existing result; do not cancel again.

**PROPOSAL:** Draft for Jiaxin's review. Publication is disabled. The whole catalogue is a PROPOSAL unless the Source column marks a statement as FACT.

## 1. Purpose and scope

**PROPOSAL:** Tell the local Sage ERP what happened, what remains unresolved and who must act next. Give authorised support staff the same explanation without asking them to join several routine API responses.

**FACT:** [SPEC023 OUT-13–15][S023] (lines 119–121) separates action results, earlier successes and next steps. [SPEC050 ERR-SND-01–06][S050] (lines 36–41) covers investigation and recovery. Both are drafts, not proof of deployed behaviour.

**PROPOSAL:** Apply [SPEC048 OPS-R01–09 — common operational requirements][S048OPS] alongside the sending cases below. These shared requirements are referenced here, not copied.

### Revision overview

**PROPOSAL:** This companion adds ERP feedback, support information and Nestor references to SPEC050's sending view. SPEC023 keeps the functional rules. SPEC043 keeps the API contract. SPEC049 keeps generation and validation. Existing documents and publication choices stay unchanged.

**PROPOSAL:** The scope is:

| Scope | Treatment and reason |
| --- | --- |
| Included | Single, multiple and automatic pending sends; cancellation, including the sending consequence of TBAI/VERIFACTU voiding; correction. Cover public/private routes and external-provider forwarding. Keep Nestor's phase labels as noted below. |
| Generation and validation | Refer to SPEC049 ERR-TRF-02–05 (lines 37–40). Keep its result and responsible team visible. Hold dependent sending. Do not redefine UBL rules, issue formats or transformation recovery. |
| Phase 3, templates and Sage as private operator | Exclude CII.3, CII.6 and CII.9 in full in this version; they can follow once the Phase 1/2 pattern is reviewed. |
| Onboarding, receiving and lifecycle-status queries | Keep these workflows separate. Sending may report missing setup, use saved cancellation evidence or inspect its own result/history. It does not define those workflows or acceptance-by-silence timers. |
| Fiscal void and rectifying-invoice content | Cover their sending/cancellation consequences and separate results. Do not define legal applicability, tax-submission contracts or fiscal correction rules. Missing support is a prerequisite. |
| Operational mechanism | Architecture, Engineering and Ops Tooling must choose between safe New Relic logs, a tailored API, existing tools or another mechanism. No mechanism is selected here. |

**FACT:** The [sending README][README] lists the existing specification views and metadata.

**FACT:** [Nestor e-invoicing use cases (SharePoint)][N], `Sheet1!A1:F1`, lists epic, phase, use case, description, next step and required services. The selected ranges contain 64 use cases, including 47 error rows. They do not define an ERP API contract.

**FACT:** Nestor marks CII.2.1 (`Sheet1!B54:E54`), CIL.8 (`B186:E187`) and CIL.10 (`B190:E191`) as Phase 1. The catalogue keeps those labels.

**FACT:** Nestor's error next steps often say “not sent” (`Sheet1!E49:E53`, `E185`, `E189`). [SPEC023 recovery][S023REC] (lines 138, 148–157) and [SPEC050 ERR-SND-02][S050] (line 37) require evidence that sending did not happen. **PROPOSAL:** Keep this distinction when the result is unknown. The disagreement stays open in §5.

### REF Source references

| Source | Exact locator | Supported claims and limits |
| --- | --- | --- |
| **FACT:** N — reviewed copy, 25 November 2026; author version/date unknown | [Nestor e-invoicing use cases (SharePoint)][N], Sheet1 rows 46–60, 68–89, 104–122 and 184–191. Scenario sources retain exact use cases/cells. | Business cases and next steps. Their phase labels and blanket failure wording are inputs, not approved design or implementation. |
| **FACT:** Sending drafts, updated 23 November 2026 | [SPEC022 §§1–4][S022]; [SPEC023 OUT-08–15 and cancellation rules][S023]; [SPEC024 §§2.3–2.4, SND-G04/05/07][S024]; [SPEC043][S043]; [NOTE002 Q30.3–8/Q20.1–2][NOTE] | Draft behaviour, source disagreements and open decisions. Cancellation/correction eligibility remains proposed. |
| **FACT:** Shared operations and SPFE error sources | [SPEC048 OPS-R01–09][S048OPS]; [SPEC011 response and error matrix][S011M] and [business/technical mapping][S011ERR]; [business messages, SPFE-S28][SBUS] and [technical messages, SPFE-S29][STECH], received 23 November 2026; [SPEC050 REF ERR-S04][S050REF] | Common operational requirements and exact source-code/operation/version references. Message keys/templates do not prove wire-code bindings or safe retries. |
| **FACT:** Stage boundaries | [SPEC049 §2][S049]; [SPEC050 §2][S050] | Generation/validation and sending investigation/recovery boundaries. |
| **FACT:** SPFE-S16/S10, reviewed local PRE release 23 November 2026 | [SendInvoice WSDL][WSEND]; [CancelInvoice WSDL][WCANCEL], documentation lines 13–25 and operation lines 63–72; [manifest][BASE], `current_wsdl_baseline`; [release review][RELEASE], lines 79–92 | SOAP/ebMS transport and responses. WSDL bytes match 29 October. They do not define ERP responses, universal resend permission, fiscal voiding or working software. |
| **FACT:** INT-SND01/02 and INT-ERR01, supplied FR evidence | [Sending guide][GUIDE], prerequisites/steps 2–5; [OpenAPI snapshot][OPENAPI], version 1.0.0, POST schemas; [error guide][ERRGUIDE], lines 9–12, 83–96 | FR intake/history meanings. These sources do not prove Spain support or deployment. Code-to-operation mappings remain open under SPEC050 REF ERR-S04. |
| **FACT (user-supplied; not independently checked):** Ops Tooling use cases | [Admin Portal Use Cases (SharePoint)][OPSUSE], Ops Tooling team; version/section not supplied | Reported production/staging users and customer-provided search identifiers. |
| **FACT:** Terminology | [Glossary][GLOSSARY], original/copy and proposed cancellation/correction terms, lines 169, 188–196 | Use the existing terms and their source rules. |
| **FACT:** CPOST | `network-eInvoicing: src/Api/PostInvoicesHandler/Handler/PostInvoices.cs` | Static invoice POST code. |
| **FACT:** CCREATE | `network-eInvoicing: src/Common/Common.Api.PostInvoice.Services/InvoiceCreation.cs` | Static invoice-creation code. |
| **FACT:** CUPLOAD | `network-eInvoicing: src/Common/Common.Api.PostInvoice.Services/InvoiceUploadUrlGenerator.cs` | Static upload-URL code. |
| **FACT:** CGET | `network-eInvoicing: src/Api/GetInvoiceHandler/Handler/GetInvoice.cs` | Static invoice-detail code. |
| **FACT:** CCONN | `network-eInvoicing: src/Api/GetDatasetAccesspointsHandler/UseCases/RetrieveAccesspoints.cs` | Static dataset/platform code. |

**FACT:** Code references use Git `5684196c93e9a28a6c0dc3189fb6dae8eb64eb78`. They describe inspected files, not executed APIs or deployment.

### Existing code responses

| Condition | Existing response and limit | Source |
| --- | --- | --- |
| Intake accepted | Creates/reuses an invoice, generates upload URLs and returns `201 Created`. Records completed New and pending FileUploaded processing. This does not prove delivery. | **FACT:** CPOST:86–115; CCREATE:120–142. |
| Request/caller access fails | Returns `400` for invalid request/validation and `401` for missing/invalid caller token. These checks do not cover all Spain UBL/certificate rules. | **FACT:** CPOST:50–79, 190–208. |
| Creation/upload-link stage fails | Returns `503` for creation failure. A conditional `403` branch checks the existing dataset-onboarding message; other failures use the upload result's status. The inspected upload generator does not produce that onboarding message. | **FACT:** CPOST:86–109; CUPLOAD:26–57. |
| Same request | Invoice creation uses `[Idempotent]`. Input binding, key lifetime and concurrency still need confirmation. This does not prove safe downstream resend/cancellation. | **FACT:** CPOST:212–221; [S024]:171. |
| Result/history | Returns history outcomes/errors, attempt metadata and settings. Also places attempt fields in current status, conflicting with INT-ERR01 (§5). | **FACT:** CGET:155–174, 190–199. |

**FACT:** New Spain status codes, reason codes, result fields and cancellation endpoints are **not defined** here. [SPEC043][S043], lines 133–149, 176–180, leaves per-action results proposed and cancellation contracts open. **PROPOSAL:** Architecture/Engineering decide how to return the business information below.

## 2. Classification model

**PROPOSAL:** These are business meanings, not API values or codes. Classify each action and keep earlier successes visible. Show uncertain causes as uncertain. SS23 uses the existing Validation error category for request checks; the SPEC049 reference in UBL rows applies only to generation/UBL validation.

**PROPOSAL:** The retry column concerns the action named in that row. “No” still allows checking the existing request. “After fixing…” also requires permission to act, unchanged request identity/input and confirmation that repetition cannot create another effect. If an external action may have happened, reconcile first. A corrected invoice or rectifying invoice is a new linked action. Retry intervals and limits remain undefined. Basis: [SPEC023 recovery][S023REC], lines 138–159; [SPEC024][S024], lines 169–184.

**PROPOSAL:** Return all relevant blockers. A later credential failure cannot turn an earlier unknown send result into a confirmed failure. A missing notification does not prove rejection. Ordinary waiting and missing prerequisites are not technical failures.

**PROPOSAL — Phase 1 SPFE feedback:** For Platform rejection and Technical-transient error, ERP feedback must keep the exact SPFE code returned, its operation and source/contract version. Use the [SPEC011 response and error matrix][S011M] and [business/technical mapping][S011ERR], with the [SPFE business messages][SBUS] and [technical messages][STECH] cited in [SPEC050 REF ERR-S04][S050REF]. Mark an absent code or unconfirmed binding “not defined”. A message-list key is not automatically a returned code. A code or HTTP status alone does not permit a retry.

| Classification | What it means for the ERP |
| --- | --- |
| Success | The named action has a confirmed successful result. Continue remaining work. This does not mean buyer acceptance or success of another action. |
| In progress | The request was accepted and its result is not final yet. |
| Partial result | The selection has mixed results. Show each invoice's own classification and next action. |
| Prerequisite not met | Required setup, permission, approval, trigger or platform support is missing. Complete or wait for that condition before sending. |
| Business rule | The state or input does not permit the action, or requires a different business action. Explain the alternative. |
| Validation error | Request validation found malformed or missing API data, or generation/UBL validation found an issue. The ERP/API owner fixes request data. Use SPEC049 only for generation/UBL issues. Hold sending. |
| Authentication-configuration error | Caller access, credentials, certificate or connection settings are invalid for this action. Name who must fix them. |
| Platform rejection | The platform explicitly refused the action/document. Keep its exact reason and show the permitted next action. For Phase 1 SPFE, apply the code/operation/version rule above. |
| Technical-transient error | A service or dependency failed. Do not infer that resending is safe. For Phase 1 SPFE, apply the code/operation/version rule above. |
| Unknown outcome | Sending/cancellation may have happened, but the result is not confirmed. Reconcile the original action before conflicting work. |

## 3. Minimum troubleshooting information

**PROPOSAL:** The Ops Tooling team must see these nine items together. Scenario columns list only additional information.

**FACT (user-supplied source; not independently checked):** Ops Tooling users are customer-service agents and Enablement in production, and ERP developers and Enablement in staging. Source: [Admin Portal Use Cases, Ops Tooling team][OPSUSE].

**FACT (same user-supplied source; not independently checked):** A user talking to a customer should be able to start from an identifier the customer can give, such as the invoice number, and reach the internal IDs. Source: [Admin Portal Use Cases][OPSUSE].

**PROPOSAL:** Search and Company and invoice must work from the ERP invoice number plus the company, without the user knowing internal IDs.

- Search: find cases by dataset/company, route, time, invoice/error status and external reference.
- Company and invoice: known ERP reference, represented company, environment, invoice type/revision and original/copy role.
- Request and route: action, requester, single/multiple/automatic context, sender platform, destination and saved cancellation route.
- Stopped step: preparation, files, access checks, sending, platform response or result publication; whether it started, waited or failed.
- Times: request, attempts, last progress, platform response and last observation; keep event time separate from observation time.
- Platform answer: exact safe code/reason, source/version, whole-request or invoice-level result, and confirmed versus suspected cause.
- Attempts: original request, retries, duplicates, trace references and whether an external action may have happened.
- Current results: each invoice and each delivery/copy/PDF/cancellation/fiscal-void result, with earlier successes and unknown results visible.
- Next action: responsible person/team, missing condition, retry restriction and escalation owner.

**FACT:** These needs come from [SPEC050 §2, including ERR-SND-06 search][S050], [SPEC048 OPS-R01–09][S048OPS], [SPEC023][S023]:43–45, 115–121, 167 and [SPEC024][S024]:130, 140–144, 169–171. CGET:155–169 returns attempt metadata; CCONN:54–66 derives platform labels from connection-record presence. Neither proves this complete view exists.

**PROPOSAL:** Mark missing information “not available” or “not defined”. Restrict access by company/environment and mask sensitive data. Do not log secrets, private keys, token-bearing URLs or raw sensitive invoice/provider content. Agree how long investigation evidence must remain available. Inspect current Ops Tooling before choosing new interfaces; see [SPEC023][S023]:167 and [SPEC024][S024]:169.

## 4. Scenario catalogue

**PROPOSAL:** The catalogue has 67 scenarios. The catalogue count is separate from the 64 selected Nestor rows. Each row uses §3's minimum list. The Ops Tooling team column contains only additions; “Minimum list only” means none. Source facts identify existing use cases or code, not approval of the proposed handling. `NEW` means added coverage, not an external code.

**PROPOSAL:** `1/2` covers the relevant public/private routes. Rows tied to CII.2.1, CIL.8 and CIL.10 keep Nestor's Phase 1 labels. Other private-platform rows use Phase 2. Platform support and cancellation rules still need confirmation; follow SPEC023.

### 4.1 Send single

| ID | Nestor ref (or NEW) | Scenario | Phase | Classification | ERP feedback: what the ERP must know + expected next action | Retry safe? | Troubleshooting info for Ops Tooling team | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SS01 | CII.1.3; CII.2.2 | The selected sending action succeeds. | 1 public / 2 private | Success | Identify what completed and what remains. Continue any outstanding copy or PDF work. Platform admission does not mean buyer acceptance. | No | Minimum list only | **FACT:** N, Sheet1!C48:E48, C55:E55; [S023], OUT-13–15. |
| SS02 | NEW | The API accepted the request; upload or platform processing has no final result yet. | 1/2 | In progress | Keep the returned reference. Complete the existing upload steps and check that request. Do not show it as delivered. | No | Upload and scan result for each required file. | **FACT:** CPOST:86–115; CCREATE:120–142. |
| SS03 | CII.1.1; CII.1.2; CII.2.1 | Generation or validation blocks the prepared invoice. | Nestor phase: 1; routes: public (CII.1), private (CII.2.1) | Validation error → SPEC049 | Refer to SPEC049's issues and responsible team. Hold sending until its correction steps are complete. | After fixing validation issues | Transformation result and related validation issues. | **FACT:** N, Sheet1!C46:E47, C54:E54; [S049], ERR-TRF-02–05. |
| SS04 | CII.1.4; CII.2.3 | A required certificate is invalid, expired or unsuitable. | 1/2 | Authentication-configuration error | Identify the platform and certificate purpose. Ask the responsible team to fix certificate access or signing. Do not ask for invoice-data changes. | After fixing the certificate | Protected certificate/version reference and its purpose. | **FACT:** N, Sheet1!C49:E49, C56:E56; [S023]:85, 113. |
| SS05 | CII.1.5; CII.2.4 | Saved platform credentials are invalid. | 1/2 where applicable | Authentication-configuration error | Identify the platform access problem and who must fix it. Preserve the invoice and earlier results. Use the platform's actual login method. | After fixing platform credentials | Platform account and login method, without credentials. | **FACT:** N, Sheet1!C50:E50, C57:E57. |
| SS06 | CII.1.6; CII.2.5 | The platform explicitly rejects invalid UBL. | 1/2 | Platform rejection | Keep the rejection reason. Refer UBL issues to SPEC049. Use CR02/CR03 to choose representation repair or fiscal correction. For Phase 1 SPFE, apply §2's code/operation/version rule. | After fixing the rejected UBL | Rejected file revision and linked validation result. | **FACT:** N, Sheet1!C51:E51, C58:E58; [S050], ERR-SND-01/04; [S023]:223. **FACT:** [SPEC011 matrix][S011M]; [SPEC050 ERR-S04][S050REF]. |
| SS07 | CII.1.7; CII.2.6 | A platform outage blocks sending; evidence proves this attempt had no external effect. | 1/2 | Technical-transient error | Explain the outage and recovery owner. Preserve completed work. If sending may have happened, use SS15. For Phase 1 SPFE, apply §2's code/operation/version rule. | After fixing the platform outage | Platform outage evidence and proof this attempt sent nothing. | **FACT:** N, Sheet1!C52:E52, C59:E59; [S023]:157. **FACT:** [SPEC011 matrix][S011M]; [SPEC050 ERR-S04][S050REF]. |
| SS08 | CII.1.8; CII.2.7 | A Sage service fails before any possible external effect. | 1/2 | Technical-transient error | Identify the failed step and recovery owner. Keep accepted invoice references. If earlier sending is uncertain, use SS15. | After fixing the Sage service outage | Last saved checkpoint and proof this attempt sent nothing. | **FACT:** N, Sheet1!C53:E53, C60:E60; [S050], ERR-SND-02. |
| SS09 | NEW | A send request was accepted and is still running. | 1/2 | In progress | Return the existing request and its progress. Wait or check that request. Do not report it as failed. | No | Minimum list only | **FACT:** [S023REC]:146; [S050], ERR-SND-04. |
| SS10 | NEW | The same invoice/action and unchanged input are submitted again. | 1/2 | In progress if still running; otherwise existing final result | If the first send is still running, return In progress. If it finished, return its existing result: Success or the original final state. Do not send again. | No | Input comparison between duplicate and original request. | **FACT:** [S023REC]:146; CPOST:212–221. **PROPOSAL:** return the original request's pending or final result. |
| SS11 | NEW | The same request identity carries changed input or a different revision. | 1/2 | Business rule | Explain the conflict. Ask for a revision or correction decision. Do not replace an issued invoice silently. | No | Both input revisions and the conflict reason. | **FACT:** [S023]:108, 112; [S023REC]:146. |
| SS12 | NEW | The customer has no permitted sending platform, or the selected platform is not configured. | 1/2 | Prerequisite not met | Explain the missing setup. Offer the setup owner or another permitted platform. Do not start onboarding within this flow. | After fixing sending-platform setup | Minimum list only | **FACT:** [S023], OUT-00/10, lines 106, 115. **FACT:** CPOST:86–109 includes the conditional dataset-onboarding `403` branch. CUPLOAD:26–57 does not produce that onboarding message in the inspected path; this does not prove setup checks work end to end. |
| SS13 | NEW | The selected platform was offboarded, disconnected or is no longer permitted. | 1/2 | Prerequisite not met | Hold new sends. Identify who can restore access. Do not reconnect or change route automatically. Keep earlier actions tied to their original route. | After fixing platform access | Platform change and effective date. | **FACT:** [S023REC]:143; [S023]:115. |
| SS14 | NEW | The recipient destination or route is missing, ambiguous, conflicting or not confirmed as supported. | 1/2 | Prerequisite not met | Explain what destination information or decision is missing. Ask the customer or Integration team to resolve it. A lookup failure must not select the public route. | After fixing destination details | Supplied/resolved destinations and lookup coverage. | **FACT:** [S023], OUT-09/10, lines 91–115; recovery lines 144–145. |
| SS15 | NEW | A timeout or lost result follows possible sending. | 1/2 | Unknown outcome | Say sending may have happened. Keep the original request and reconciliation owner. Do not ask for a new invoice or key. | Reconcile first | Original payload/file reference and evidence of possible transmission. | **FACT:** [S023REC]:148; [S024]:130; [S050], ERR-SND-02. |
| SS16 | NEW | Some uploads succeed; another expires or fails before completion is confirmed. | 1/2 | Technical-transient error | Keep the invoice and successful uploads. Recover only the failed upload. Use SS03 for validation issues and SS15 if external sending may have happened. | After fixing the upload failure | Completed/failed uploads, file roles and access expiry. | **FACT:** [S023REC]:147; [S049], ERR-TRF-04. |
| SS17 | NEW | Caller authentication fails. | 1/2 | Authentication-configuration error | Restore caller access. Then check permission to act for the company separately. A renewed token does not restore withdrawn permission; use SS13 for platform access. | After fixing caller authentication | Minimum list only | **FACT:** CPOST:67–79; [S023REC]:143, 157. |
| SS18 | NEW | One delivery, copy or PDF action fails while another succeeds. | 1/2 as applicable | Technical-transient error | Show each result separately. Recover only failed work. Use Platform rejection for an explicit refusal and SS15 for an unknown effect. | After fixing the failed action | Minimum list only | **FACT:** [S023REC]:150–152; [S050], ERR-SND-03. **ASSUMPTION:** Phase 2 provider-copy capability remains unconfirmed. |
| SS19 | NEW | Progress or notification is missing; the current result cannot be confirmed. | 1/2 | Unknown outcome | Show the last confirmed result and when it was checked. Investigate the original request. Keep any final attempt error and its recovery owner. Do not infer failure or resend from silence. | Reconcile first | Notification delivery history and gaps. | **FACT:** [S023REC]:154–155; [S050], ERR-SND-04; [ERRGUIDE]:9–12. |
| SS20 | Related: MCS.8.1; ON.7.1 | E-invoice sending is disabled for the customer, or company automatic submission is not activated for an automatic send. | Nestor labels: ON.7.1 = 1; MCS.8.1 = 2. Route: not stated in those rows. | Prerequisite not met | Show that the invoice is not sent by setting, not as a failure. Name who can change the setting. Do not start onboarding in this flow. | After fixing the relevant sending setting | Customer sending setting or company automatic-submission setting that blocked this action. | **FACT:** N, customer-settings MCS.8.1, worksheet row 357 (C357:E357); onboarding ON.7.1, row 24 (C24:E24). **PROPOSAL:** blocked-setting feedback and next action. |
| SS21 | Related: MCS.1.3; MCS.3.1 | The customer's e-invoice format is missing or unsupported for the private route. | 2 private | Prerequisite not met | Identify the missing or unsupported format and who can change the customer setting. Hold sending until a supported format is selected. Use SPEC049 for generation/validation errors. | After fixing the customer format setting | Customer format setting and the format supported by the selected private route. | **FACT:** N, customer-settings MCS.1.3, worksheet row 348 (C348:E348), and MCS.3.1, row 352 (C352:E352). **PROPOSAL:** missing/unsupported-format feedback; the setting rows do not define this error response. |
| SS22 | Related: MCS.1–MCS.6 | The customer's sending or destination platform changes while the invoice waits to be sent. | 2 | Business rule | Show which route was used or blocked and why. Do not choose the pending invoice's route rule in this draft. Architecture and the specification owner must define it. | No | Earlier/current customer sending and destination settings, change time, and route used or blocked. | **FACT:** N, customer-settings MCS.1–MCS.6, worksheet rows 346–355 (C346:E355); row 356 is MCS.7.1 (C356:E356). **PROPOSAL:** Which route applies is not defined and needs Architecture and the specification owner. |
| SS23 | NEW | The request is malformed or missing required API request data. | Phases: 1/2; routes: public/private | Validation error | Explain which request data is malformed, missing or invalid. The ERP/API owner corrects the request before sending. Do not treat this as a platform rejection or route API request errors to SPEC049. | After fixing request data | Safe request-validation findings or missing-data list; no raw sensitive request body. | **FACT:** CPOST:50–79, 190–208 returns `400` for malformed request/validation failure. **PROPOSAL:** use the existing Validation error category; SPEC049 remains the generation/UBL boundary. |
| SS24 | NEW | The ERP asks for an existing sending result through a read-only check, and that read fails. | Phases: 1/2; routes: public/private | Technical-transient error | Say that the result could not be read. Keep the last confirmed invoice result and its observation time. Do not show “invoice does not exist” or start a new send. Retry only the read. | Yes | Failed result-read reference and service failure, linked to the last successful observation. | **FACT:** CGET:78–88 reports repository failure and absent invoice as `404`; see §5. **PROPOSAL:** separate failed read from absence; Yes applies only to this read-only check. |
| SS25 | NEW | A send is requested for an invoice already confirmed cancelled. Same invoice and number: not a rectifying invoice (see CR03/CR06) and not a correction request (see CR07). | Phases: 1/2; routes: public/private | Business rule | Return the existing cancellation result. Do not send again, reactivate the invoice or reuse its number. | No | Cancellation result and time. | **FACT:** [S023]:193, 211; [S024]:144 restrict reactivation and do not describe a new Send request. **PROPOSAL:** this Send-request handling. |
| SS26 | NEW | A manual send is requested but required approval or the final revision is missing. | Phases: 1/2; routes: public/private | Prerequisite not met | Say which approval or final revision is missing and who must provide it. Hold sending. Do not show this as an outage. | After fixing missing approval or final revision | Approval state and revision used. | **FACT:** [S023]:111–113, 142; [S024]:55, 224, 229 require approval and the final revision. **PROPOSAL:** ERP feedback and next action. |
| SS27 | NEW | The platform answered, but Sage could not record or publish the result. | Phases: 1/2; routes: public/private | Unknown outcome | Show the last confirmed result and when it was checked. Say a platform answer may exist but is not recorded. Do not resend or infer failure. Follow SS15 and SS19. | Reconcile first | Platform-answer reference versus the recorded status, and the time they diverged. | **FACT:** [S023]:119, 121, 148, 154 covers lost local results, result reporting and missing events; [S024]:130 prevents resending after an uncertain result. **PROPOSAL:** this recording/publication failure handling and ERP feedback. |

**PROPOSAL:** For multiple/automatic recovery, apply [SPEC048 OPS-R07][S048OPS]: select only eligible failed actions. Keep completed invoices/actions out of recovery selections. Recheck permission and eligibility for each action at execution. Keep unknown outcomes on the reconciliation path.

### 4.2 Send multiple

**FACT:** [NOTE002 Q30.4/Q30.8][NOTE] (lines 38, 42) separates ERP selection, API requests and SPFE packages. Bulk API and package results are not agreed. **PROPOSAL:** Return results per invoice without assuming a bulk endpoint or package format.

| ID | Nestor ref (or NEW) | Scenario | Phase | Classification | ERP feedback: what the ERP must know + expected next action | Retry safe? | Troubleshooting info for Ops Tooling team | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MS01 | CII.4.1; CII.4.3; CII.5.1; CII.5.3; CII.5.9 | Selected invoices are sent through their public/private routes; individual actions complete. | 1 public / 2 mixed | Success | Apply SS01 per invoice. Show unfinished items. Report the selection as complete only when all required item/action results are confirmed. | No | Selection-to-invoice links. | **FACT:** N, Sheet1!C68:E68, C70:E70, C76:E76, C78:E78, C84:E84. |
| MS02 | CII.4.2; CII.5.2 | One or more selected invoices fail pre-send UBL validation. | 1/2 | Validation error → SPEC049 | Apply SS03 to affected invoices. Keep other valid invoices and explain which can continue. | After fixing validation issues | Validation result for each blocked invoice. | **FACT:** N, Sheet1!C69:E69, C77:E77; [S049], ERR-TRF-02/06. |
| MS03 | CII.4.4; CII.5.4; CII.5.10 | A certificate check blocks selected actions. | 1/2 | Authentication-configuration error | Apply SS04 to the affected invoices. Do not mark unrelated companies or platforms as failed. | After fixing the certificate | Certificate shared by affected invoices or companies. | **FACT:** N, Sheet1!C71:E71, C79:E79, C85:E85. |
| MS04 | CII.4.5; CII.5.5; CII.5.11 | Saved credentials block selected actions. | 1/2 where applicable | Authentication-configuration error | Apply SS05 only to the affected platform accounts. Keep other results. | After fixing platform credentials | Platform account shared by affected invoices. | **FACT:** N, Sheet1!C72:E72, C80:E80, C86:E86. |
| MS05 | CII.4.6; CII.5.6; CII.5.12 | The platform rejects UBL for selected invoices. | 1/2 | Platform rejection | Apply SS06 per invoice. Keep both the whole-request response and each invoice result. One rejection must not fail the whole selection. For Phase 1 SPFE, apply §2's code/operation/version rule. | After fixing the rejected UBL | Minimum list only | **FACT:** N, Sheet1!C73:E73, C81:E81, C87:E87; [S050], ERR-SND-06. **FACT:** [SPEC011 matrix][S011M]; [SPEC050 ERR-S04][S050REF]. |
| MS06 | CII.4.7; CII.5.7; CII.5.13 | A platform outage affects part or all of the selection. | 1/2 | Technical-transient error | Apply SS07 where sending did not happen. Use SS15 for uncertain items. Other routes may continue if their checks pass. | After fixing the platform outage | Routes and invoices affected by the outage. | **FACT:** N, Sheet1!C74:E74, C82:E82, C88:E88. |
| MS07 | CII.4.8; CII.5.8; CII.5.14 | A Sage service fails during multiple-invoice processing. | 1/2 | Technical-transient error | Apply SS08 to each failed step. Keep accepted/completed items and use SS15 for uncertain items. | After fixing the Sage service outage | Last saved checkpoint for each invoice. | **FACT:** N, Sheet1!C75:E75, C83:E83, C89:E89. |
| MS08 | NEW | The selection has mixed successful, blocked, rejected, pending or unknown results. | 1/2 | Partial result | Show each invoice's own classification and next action. Keep completed items visible. Do not retry the whole selection; follow each item's retry rule. | No | Counts by result and missing item results. | **FACT:** [S023]:58, 119–121; [NOTE]:42. |
| MS09 | NEW | The selection response is lost and the customer selects all invoices again. | 1/2 | Unknown outcome | Find the original per-invoice requests. Use SS10 for duplicates. Do not send the whole selection again. | Reconcile first | Original selection and links to existing invoice requests. | **FACT:** [S050], ERR-SND-02/06; [NOTE], Q30.8. |
| MS10 | NEW | One customer's setup or permission is missing, withdrawn or changes during execution. | 1/2 | Prerequisite not met | Apply SS12/SS13 and recheck permission per item. One company must not use another's permissions or platform setup. | After fixing missing setup or permission | Setup/permission changes and excluded invoices. | **FACT:** [S023]:61–62, 113, 118; [NOTE], Q30.7. |

### 4.3 Automatic pending sending

**FACT:** [NOTE002 Q30.3][NOTE] (line 37) leaves triggers and certificate choice open. **PROPOSAL:** These cases apply if automatic sending is enabled. They do not set a schedule, retry interval or duration.

| ID | Nestor ref (or NEW) | Scenario | Phase | Classification | ERP feedback: what the ERP must know + expected next action | Retry safe? | Troubleshooting info for Ops Tooling team | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AS01 | CII.7.1; CII.8.1; CII.8.2; CII.8.8 | Pending invoices complete sending through the selected public/private routes. | 1 public / 2 mixed | Success | Apply SS01 per completed action. Show which pending invoices remain and why. | No | Trigger/rule used and invoices selected. | **FACT:** N, Sheet1!C104:E104, C110:E111, C117:E117. |
| AS02 | CII.7.2; CII.8.3; CII.8.9 | A certificate is invalid or expired when queued work is ready to run. | 1/2 | Authentication-configuration error | Apply SS04. Show the action required and its owner. Keep other pending work and earlier successes. | After fixing the certificate | Certificate choice at selection and execution. | **FACT:** N, Sheet1!C105:E105, C112:E112, C118:E118. |
| AS03 | CII.7.3; CII.8.4; CII.8.10 | Saved platform credentials are invalid during automatic sending. | 1/2 where applicable | Authentication-configuration error | Apply SS05. Name the person or team that must act. Do not leave unexplained pending work. | After fixing platform credentials | Platform account affected across the automatic run. | **FACT:** N, Sheet1!C106:E106, C113:E113, C119:E119. |
| AS04 | CII.7.4; CII.8.5; CII.8.11 | The platform rejects invalid UBL from automatic sending. | 1/2 | Platform rejection | Apply SS06 and the related SPEC049/correction decision. Stop resubmitting unchanged input. For Phase 1 SPFE, apply §2's code/operation/version rule. | After fixing the rejected UBL | Queued file revision and rejected file. | **FACT:** N, Sheet1!C107:E107, C114:E114, C120:E120. **FACT:** [SPEC011 matrix][S011M]; [SPEC050 ERR-S04][S050REF]. |
| AS05 | CII.7.5; CII.8.6; CII.8.12 | A platform outage blocks automatic sending. | 1/2 | Technical-transient error | Apply SS07. Explain who will recover the work and when progress can next be checked. Use SS15 if sending may have happened. | After fixing the platform outage | Outage incident and affected queued items. | **FACT:** N, Sheet1!C108:E108, C115:E115, C121:E121. |
| AS06 | CII.7.6; CII.8.7; CII.8.13 | A Sage service fails during automatic sending. | 1/2 | Technical-transient error | Apply SS08. Show saved work and the recovery owner. A failed run does not prove that every invoice failed. | After fixing the Sage service outage | Automatic run and last saved work per invoice. | **FACT:** N, Sheet1!C109:E109, C116:E116, C122:E122. |
| AS07 | NEW | Approved work waits for the sending trigger; no send request has been accepted. | 1/2 | Prerequisite not met | Explain which trigger must occur. Wait without calling this an outage. If approval expires or is withdrawn, use AS09. | No | Sending trigger and approval state. | **FACT:** [S023]:111; [NOTE], Q30.3. **PROPOSAL:** waiting for a trigger is a prerequisite, not an accepted send. |
| AS08 | NEW | A send request was accepted and is still running when manual or automatic work targets it again. | 1/2 | In progress | Apply SS09/SS10. Link to the existing request and prevent another send. | No | Overlapping automatic runs and manual request. | **FACT:** [S023REC]:146, 156. |
| AS09 | NEW | Platform access, permission or approval becomes invalid while work is queued. | 1/2 | Prerequisite not met | Recheck the affected condition and name who can fix it. Use SS13 for platform access and CR05 for changed invoice data. Do not use newer bytes silently. | After fixing invalid access or approval | Queued versus current access/approval and change time. | **FACT:** [S023]:111–118; [S023REC]:143. |
| AS10 | NEW | Automatic sending stops progressing or loses its result after a possible send. | 1/2 | Unknown outcome | Apply SS15/SS19. Show an owner and last observation. Do not restart all pending sends to clear the backlog. | Reconcile first | Automatic run and last saved checkpoint. | **FACT:** [S050], ERR-SND-02/04/06; [S024], SND-G07. |

### 4.4 Cancellation, including TBAI/VERIFACTU voiding

**FACT:** [SPEC023 cancellation eligibility][ELIG] (lines 197–231) proposes state and reason checks. Buyer rejection is not required for sent/pending invoices. Technical rejection and full customer rejection differ. **PROPOSAL:** Follow those checks without approving them here. Keep original/copy targets separate and do not infer buyer acceptance from elapsed time.

| ID | Nestor ref (or NEW) | Scenario | Phase | Classification | ERP feedback: what the ERP must know + expected next action | Retry safe? | Troubleshooting info for Ops Tooling team | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CN01 | CIL.7.1; CIL.8.1 | An eligible cancellation request was accepted; its final result is pending. This includes sent invoices without buyer acceptance. | Nestor phase: 1; routes: public (CIL.7.1), private (CIL.8.1) | In progress | Keep cancellation separate from sending. Retain the original destination and original/copy purpose. Wait for confirmation before showing cancelled. | No | Eligibility/reason check and exact original/copy target. | **FACT:** N, Sheet1!C184:E184, C186:E186; [ELIG]:199–207; [S024]:140–143. |
| CN02 | NEW | Cancellation is confirmed. | 1/2 | Success | Show what was cancelled and what remains unresolved. Follow the existing cancelled-state/numbering proposal. Cancelling a public copy does not prove cancellation of the private original. | No | Minimum list only | **FACT:** [S023]:193, 227; [S024]:143–144. |
| CN03 | CIL.7.2; CIL.8.2 | Cancellation transmission fails; evidence proves no external effect. | Nestor phase: 1; routes: public (CIL.7.2), private (CIL.8.2) | Technical-transient error | Say this attempt did not execute and name the recovery owner. Keep earlier invoice/delivery results. Use CN05 if execution is uncertain. | After fixing the cancellation transmission failure | Proof cancellation did not reach the platform. | **FACT:** N, Sheet1!C185:E185, C187:E187; [S050], ERR-SND-05. |
| CN04 | NEW | The platform explicitly rejects cancellation. | 1/2 | Platform rejection | Show the refusal and permitted alternative or owner. Do not show cancelled or treat this as buyer rejection of the invoice. For Phase 1 SPFE, apply §2's code/operation/version rule. | No | Cancellation eligibility and target-existence checks. | **FACT:** [S050], ERR-SND-05; [S024]:141–144. **FACT:** [SPEC011 matrix][S011M]; [SPEC050 ERR-S04][S050REF]. |
| CN05 | NEW | Cancellation times out, or its result is lost after possible execution. | 1/2 | Unknown outcome | Say cancellation is unresolved. Reconcile the original attempt. Do not repeat sending/cancellation or create a replacement to hide uncertainty. | Reconcile first | Reconciliation observations. | **FACT:** [S050], ERR-SND-05; [S024]:143–144. |
| CN06 | NEW | The invoice never reached platform admission and evidence proves no earlier send effect. | 1/2 | Business rule | Explain that there is no platform submission to cancel. Offer only a safe stop or correction of pending work. If admission is unknown, use CN05/SS15. | No | Proof of no platform admission; pending work that can still be stopped. | **FACT:** [S023]:117; [S023REC]:156. |
| CN07 | NEW | The exact invoice/action is already confirmed cancelled. | 1/2 | Business rule | Return the existing result. Explain that another cancellation is unnecessary. Do not reactivate it, reuse its number or cancel again. | No | Minimum list only | **FACT:** [ELIG]:211; [S024]:144. |
| CN08 | NEW | The existing state/reason rule does not permit cancellation. | 1/2 | Business rule | Explain the rule and permitted correction path. Buyer rejection alone does not permit cancellation. Keep the existing treatment of technical rejection, accepted, paid and partially rejected states. SPEC023:201 treats acceptance by silence after four days as workshop input pending verification. Cancellation eligibility follows the state and reason rules above. | No | State and reason used for the eligibility check. | **FACT:** [ELIG]:199–211, 223; [S023]:201. |
| CN09 | NEW | A cancellation request was accepted and remains pending; it may overlap the original send. | 1/2 | In progress | Show the existing request. If the original send may have executed, reconcile before conflicting work. If cancellation was not accepted and the send effect is unknown, use CN05/SS15. Do not say safely stopped. | No | Link between competing send and cancellation requests. | **FACT:** [S023REC]:156; [S024]:141–144. |
| CN10 | CIL.9.1; CIL.10.1 | A TBAI/VERIFACTU void leads to a cancellation request, but cancellation checks are not complete. | Nestor phase: 1; routes: public (CIL.9.1), private (CIL.10.1) | Prerequisite not met | Keep fiscal void and platform cancellation separate. Confirm eligibility, exact target and regime/provider support first. Name the review owner. Once the request is accepted with no final result, use CN01. | After fixing missing cancellation checks | Fiscal regime and protected void reference. | **FACT:** N, Sheet1!C188:E188, C190:E190; [S023]:231 retains separate VERI*FACTU treatment as open. **PROPOSAL:** complete cancellation checks before treating the request as accepted. |
| CN11 | CIL.9.2; CIL.10.2 | Sending cancellation for a voided invoice fails before any external effect. | Nestor phase: 1; routes: public (CIL.9.2), private (CIL.10.2) | Technical-transient error | Keep the fiscal-void result. Recover only e-invoice cancellation under CN03. Use CN04 for refusal and CN05 for possible execution. Do not repeat or reverse fiscal void automatically. | After fixing the cancellation transmission failure | Minimum list only | **FACT:** N, Sheet1!C189:E189, C191:E191. |
| CN12 | NEW | E-invoice cancellation is known, but a possible fiscal void has no reliable completion result. | 1/2 | Unknown outcome | Keep known cancellation and name the owner of the unresolved fiscal result. Do not claim the tax system is updated or repeat platform cancellation to repair it. | Reconcile first | Fiscal regime and reference used to investigate the void. | **FACT:** N, Sheet1!C188:E191 names fiscal void and sending cancellation as connected steps. |
| CN13 | NEW | The original platform was offboarded or changed before historical cancellation. | 1/2 | Prerequisite not met | Identify the missing access or support for the earlier action. Keep the original target. Do not use the new-send platform to retarget cancellation. Offer the support/provider path. | After fixing historical platform access | Permitted purpose for retaining historical access. | **FACT:** [S023]:75; [S024]:140–146. |

### 4.5 Correction

**FACT:** [SPEC023 Correct][S023ENTRY] (line 74) sends rectifying-invoice creation to SPEC015 IC-12, then uses normal Send. [The technical-rejection rule][ELIG] (line 223) separates representation/routing repair from fiscal-content correction. **PROPOSAL:** Keep that distinction; correction does not automatically mean cancellation or editing issued data.

| ID | Nestor ref (or NEW) | Scenario | Phase | Classification | ERP feedback: what the ERP must know + expected next action | Retry safe? | Troubleshooting info for Ops Tooling team | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR01 | NEW | Unissued input needs generation or validation correction. | 1/2 | Validation error → SPEC049 | Use SS03 and the SPEC049 result. After correction, recheck affected preparation. Keep sending blocked until those checks pass. | After fixing validation issues | Input and validation revisions. | **FACT:** [S049], ERR-TRF-02/03; [S023]:110–113. |
| CR02 | NEW | The platform technically rejects routing or UBL representation; issued fiscal data is correct. | 1/2 | Platform rejection | Follow the existing same-number repair proposal. Refer UBL work to SPEC049 and preserve issued fiscal data. Check the earlier result before sending. Do not cancel or create a rectifying invoice automatically. | After fixing the representation or routing issue | Rejected/repaired representations and unchanged fiscal content. | **FACT:** [ELIG]:205, 223; [S049], ERR-TRF-02/03. |
| CR03 | NEW | A technically rejected issued invoice has incorrect amounts, NIF or tax. | 1/2 | Business rule | Use the rectifying-invoice process. Do not edit and resend issued fiscal data as a representation fix. Send the new invoice through the normal flow. | No | Link between original and separately numbered rectifying invoice. | **FACT:** [ELIG]:205, 223; [S023ENTRY]:74. |
| CR04 | NEW | Customer rejection prompts a correction request. | 1/2 | Business rule | Separate buyer rejection from technical rejection. Follow the fiscal correction decision. Partial rejection need not cause rectification; full rejection does not automatically permit cancellation. | No | Customer rejection reason and correction decision. | **FACT:** [ELIG]:199–211; [GLOSSARY]:192–196. |
| CR05 | NEW | The final revision changes after approval/preparation or while queued. | 1/2 | Business rule | Explain which earlier decision no longer applies. Obtain the new revision/approval and repeat affected preparation checks. Keep earlier possible/completed sends visible. | No | Old/new revisions and affected approval or file. | **FACT:** [S023]:111–116; [S023REC]:142, 146. |
| CR06 | NEW | A separately issued rectifying invoice enters normal sending. | 1/2 | Follows the scenario that applies (SS01–SS27) | Sending checks, results and retries follow the SS01–SS27 scenario that applies. Use MS/AS rules where applicable. Keep the rectifying invoice separate from the original. Do not repeat the original invoice. | No | Link between original and rectifying invoices. | **FACT:** [S023ENTRY]:74; [S022]:82. |
| CR07 | NEW | The customer requests correction or reactivation of a cancelled invoice. | 1/2 | Business rule | Explain the existing cancelled-state restriction and refer to the permitted business action or owner. Do not reopen the invoice or release its number. | No | Minimum list only | **FACT:** [ELIG]:211; [GLOSSARY]:193–194. |

### Nestor coverage check

**FACT:** Row counts and use-case ranges below refer to N, Sheet1. **PROPOSAL:** The catalogue column shows how the rows are covered.

| Selected group | Workbook rows / use cases | Catalogue coverage | Error rows |
| --- | --- | --- | --- |
| CII.1 | Sheet1 rows 46–53; CII.1.1–1.8 | SS01, SS03–SS08 | 6; one local-validation row delegated to SPEC049 through SS03. |
| CII.2 | Rows 54–60; CII.2.1–2.7 | SS01, SS03–SS08 | 5. |
| CII.4 | Rows 68–75; CII.4.1–4.8 | MS01–MS07 | 6; one local-validation row delegated through MS02. |
| CII.5 | Rows 76–89; CII.5.1–5.14 | MS01–MS07 | 11; one local-validation row delegated through MS02. |
| CII.7 | Rows 104–109; CII.7.1–7.6 | AS01–AS06 | 5. |
| CII.8 | Rows 110–122; CII.8.1–8.13 | AS01–AS06 | 10. |
| CIL.7–CIL.10 | Rows 184–191; each group's .1/.2 | CN01, CN03, CN10–CN11; CN04/CN05 split explicit rejection/uncertainty. | 4. |

**FACT:** This trace covers all 64 selected workbook rows and all 47 selected error rows. Three local-validation error rows are covered by an explicit SPEC049 handoff, not redefined: CII.1.2, CII.4.2 and CII.5.2. No selected row is omitted. **PROPOSAL:** Coverage means a proposed response for review, not proof of working software or approved TBAI/VERIFACTU behaviour.

### Related rows outside the 64 selected

**FACT:** The references below support SS20–SS22. They are related settings/onboarding rows, not additions to the original 64 selected sending/cancellation rows. Source: [Nestor e-invoicing use cases][N], Sheet1, worksheet rows 24 and 346–357.

| Scenario | Related use cases and worksheet rows | Relationship to the original selection | Source |
| --- | --- | --- | --- |
| `SS20` | Customer-settings MCS.8.1, row 357; onboarding ON.7.1, row 24 | Settings that can prevent customer sending or automatic submission. Outside the 64 selected. | **FACT:** N, C357:E357 and C24:E24. **PROPOSAL:** SS20 treatment. |
| `SS21` | Customer-settings MCS.1.3, row 348; MCS.3.1, row 352 | Private-route format settings. Outside the 64 selected. CII.2.2 remains in the original selection. | **FACT:** N, C348:E348, C352:E352 and C55:E55. **PROPOSAL:** SS21 treatment. |
| `SS22` | Customer-settings MCS.1–MCS.6, rows 346–355; neighbouring row 356 is MCS.7.1 | Sending/destination changes. Outside the 64 selected; they do not define which route applies to a waiting invoice. | **FACT:** N, C346:E356. **PROPOSAL:** SS22 route rule remains for Architecture and the specification owner. |

**FACT:** In the reviewed workbook, column A is `EPIC`, not `Row` (Sheet1!A1). The references above use worksheet row numbers and name the epic because MCS IDs repeat in company/customer settings. Row 356 is MCS.7.1, not MCS.6. Source: [Nestor e-invoicing use cases][N], A31:E40 and A346:E356.

**FACT:** CII.2.2 (worksheet row 55) says to send through the customer's configured platforms; it does not state the required format. The customer-required-format wording is in MCS.1.3 and MCS.3.1 (rows 348 and 352). Source: [Nestor e-invoicing use cases][N], C55:E55, C348:E348 and C352:E352.

### Acceptance scenarios

**PROPOSAL:** These are required review scenarios, not executed tests. They reuse [SPEC050 §4 acceptance scenarios][S050AC] and map them to the catalogue.

| Required review case | Catalogue cases | Result to check | Source |
| --- | --- | --- | --- |
| Private delivery accepted; public-copy evidence lost | SS18, SS15, MS08, AS10 | Keep delivery success. Reconcile only the unresolved copy action. Do not send recipient delivery again. | **FACT:** SPEC050 §4, ERR-SND-02/03. |
| History attempt has `ERROR`; invoice snapshot remains `Submitted` | SS19, SS02 | Keep the failed attempt separate from the invoice's current status. Show the error owner and next action. Do not start a fresh send because of the attempt error or missing notification. | **FACT:** SPEC050 §4, ERR-SND-04. |
| Uncertain cancellation, completed invoice and revoked permission in one bulk selection | CN05, CN09, MS08, MS10, AS09 | Reconcile uncertain cancellation. Exclude completed actions and actions without current permission. Preserve separate item results. | **FACT:** SPEC050 §4, ERR-SND-05/06; SPEC048 OPS-R07. |
| Common operational checks | SS12, SS13, SS15, MS08, MS10, AS08, CN05 | Apply [SPEC048 OPS-A01–05][S048AC] to search, history, guarded recovery, access/country isolation and case closure. Demonstrate the checks against the selected implementation. | **FACT:** SPEC050 §4; SPEC048 §5, OPS-A01–05. |

## 5. Spec vs code conflicts

**FACT:** These are differences between inspected sources and code. The deployed contract is not confirmed. This section covers sending/result diagnosis, not receiving or lifecycle-query contracts.

| Conflict | Spec/source position | Code position | Source |
| --- | --- | --- | --- |
| Failed read versus absence | A failed read does not prove absence. | Returns `404` for repository failure and for an absent invoice. | **FACT:** [S023REC]:148; [S024]:130; CGET:78–88. |
| Current-status versus attempt fields | INT-ERR01 puts `operationStatus`/`errorCode` in history, not current status. | Sets those fields in both history and current status. | **FACT:** [ERRGUIDE]:10–11; [S050], ERR-SND-04; CGET:155–162, 190–199. |
| Intake response property | Saved SendInvoiceResponse requires `documents`, but defines `attachments` and no `documents` property. | Returns attachment upload descriptions, not a `documents` property. | **FACT:** [S043]:258; CPOST:123–164. |

**FACT:** Some support remains unconfirmed. The onboarding rejection branch does not prove setup checks work end to end (CPOST:106–109; CUPLOAD:26–57). Connection labels do not prove sending is available (CCONN:54–66). Private-copy results/retries and cancellation contracts remain open ([S024], SND-G04/05/07). No Spain cancellation/fiscal-void handler was found in the inspected `network-eInvoicing: src/Api`/`src/Lambdas` tree. Absence here does not prove absence elsewhere.

**FACT:** Nestor's phase labels and blanket “not sent” wording differ from the phase/effect distinctions noted in §1. [SPEC023][S023], lines 191–193, also keeps the conflict between catalogue identifier reuse and the proposed permanently consumed fiscal number.

[README]: README.md
[N]: https://sage365-my.sharepoint.com/:x:/g/personal/nestor_zarzoso_sage_com/IQDRGN4ug5hhRpa7DqLzA__JAY0OEoqdBZ7_znRmAFUPAA0
[S022]: SPEC-SEI-022-invoice-sending-solution-summary.md
[S023]: SPEC-SEI-023-invoice-sending-logical-feature-specification.md
[S023ENTRY]: SPEC-SEI-023-invoice-sending-logical-feature-specification.md#entry-actions
[S023REC]: SPEC-SEI-023-invoice-sending-logical-feature-specification.md#exceptions-errors-and-recovery
[ELIG]: SPEC-SEI-023-invoice-sending-logical-feature-specification.md#proposed-cancel-eligibility
[S024]: SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md
[S043]: api-reference/SPEC-SEI-043-invoice-sending-api-reference.md
[S049]: ../error-handling/SPEC-SEI-049-transformation-and-validation-error-handling.md
[S050]: ../error-handling/SPEC-SEI-050-invoice-sending-error-handling.md
[NOTE]: NOTE-SEI-002-sending-questions-and-decisions.md
[GLOSSARY]: ../../context/GLO-SEI-001-e-invoicing-terminology.md
[BASE]: ../../assets/regulatory/spain/spfe/source-manifest.json
[RELEASE]: ../../context/RES-SEI-002-spain-public-platform-technical-evidence.md#pre-wsdl-and-supporting-evidence-reviewed-23-november-2026
[WSEND]: <../../context/WSDL%20servicios%20web%20-%20PRE_23_11_26/SendInvoice.wsdl>
[WCANCEL]: <../../context/WSDL%20servicios%20web%20-%20PRE_23_11_26/CancelInvoice.wsdl>
[GUIDE]: <../../context/FR%20API/Sending/send-e-invoice-guide-extract.md>
[OPENAPI]: <../../context/FR%20API/Sending/send-e-invoice-openapi.md>
[ERRGUIDE]: <../../context/FR%20API/Shared/invoice-flow-error-handling-guide-extract.md>

[S048OPS]: ../error-handling/SPEC-SEI-048-shared-error-handling-and-operational-support.md#2-common-operational-requirements
[S048AC]: ../error-handling/SPEC-SEI-048-shared-error-handling-and-operational-support.md#5-acceptance-and-open-gates
[S011M]: ../SPEC-SEI-011-public-platform-connector-solution-specification.md#spfe-response-and-error-matrix
[S011ERR]: ../SPEC-SEI-011-public-platform-connector-solution-specification.md#business-and-technical-error-mapping
[S050REF]: ../error-handling/SPEC-SEI-050-invoice-sending-error-handling.md#ref-source-references
[S050AC]: ../error-handling/SPEC-SEI-050-invoice-sending-error-handling.md#4-acceptance-and-open-decisions
[SBUS]: <../../context/Listados%20códigos%20de%20error/errores_negocio.properties>
[STECH]: <../../context/Listados%20códigos%20de%20error/errores_tecnicos.properties>

[OPSUSE]: https://sage365.sharepoint.com/sites/sf-et-adminportals/_layouts/15/Doc.aspx?sourcedoc=%7B4665C6E9-20CB-47DB-AAFF-E55EE46DF75E%7D&file=Admin%20Portal%20Use%20Cases.docx&action=default
