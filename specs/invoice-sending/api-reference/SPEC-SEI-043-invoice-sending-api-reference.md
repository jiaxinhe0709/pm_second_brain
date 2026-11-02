---
id: SPEC-SEI-043
title: Invoice Sending API Reference and Spain Changes
type: api-reference
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-30
updated: 2026-11-02
reviewers: []
related:
  - SPEC-SEI-024
  - SPEC-SEI-022
  - SPEC-SEI-023
  - GLO-SEI-001
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837610656"
  page_id: "937965432"
  title: Invoice Sending API Reference and Spain Changes
  layout: two_left_sidebar
  toc: true
---

# Invoice Sending API Reference and Spain Changes

[Sequence and Reuse Assessment](../SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md) · [Solution Summary](../SPEC-SEI-022-invoice-sending-solution-summary.md) · [Logical Feature Specification](../SPEC-SEI-023-invoice-sending-logical-feature-specification.md) · [Feature landing page](../README.md)

## Revision overview

This API view owns field-level detail, request/response examples and contract issues. This revision adds change types and text labels to Spain field proposals, records the six-case public-route decision, clarifies identity and platform terms, and links withdrawal assessment to FP-SEI-002. Sequences, scenarios, decisions and acceptance checks remain in SPEC-SEI-023/024. No new call or wire contract is approved.

## Summary

This page owns request/response examples, detailed API fields, field-level change types and contract issues. [SPEC-SEI-024](../SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md) owns sequences, scenarios, decisions and checks.

## How to read the examples

<span style="color:#666666;">Grey — Existing behaviour, calls and fields.</span> <span style="color:#1565C0;">Blue — Proposed Spain change.</span> <span style="color:#B42318;">Red — Open question, Assumption, Gap or Source conflict.</span> Always read the text label beside each colour. This follows [SPEC-SEI-039 §3](../../onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md#3-proposed-reuse-sequences-phases-13) and [SPEC-SEI-040 “How to read the examples”](../../onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#how-to-read-the-examples). Examples use the preserved France-oriented contract and proposed Spain values where explicitly labelled. Proposed values and response fields are not approved wire contracts or implementation evidence.

<a id="1-identity-routing-and-representation"></a>

## 1 Identity, routing and representation differences

| Evidence / exact fields | Required qualification and consequence |
|---|---|
| `sender`, `recipient`, `accessPointAddressType`, `accessPointAddress`, `accessPointId` | <span style="color:#666666;">Existing:</span> INT-SND01 defines sender and recipient as network-routing addresses, separate from seller/buyer in invoice content. The snapshot describes `recipient.accessPointAddress` as a Buyer key in the sender ERP; this is a confirmed wording defect. NIF is a legal tax identifier, not automatically a routing address. <span style="color:#1565C0;">Proposed:</span> `es.nif`, aligned with SPEC-SEI-040. <span style="color:#B42318;">Open:</span> NIF-as-routing-address equivalence and NIE handling. Do not replace France's `fr.siren`. Spain's sender-side `accessPointId` meaning is Proposed and needs API-owner qualification. SND-G02; OUT-R04/11; INT-SND01/02. |
| Submission's required values and correlation | <span style="color:#B42318;">Source conflict:</span> INT-SND01 says the guide requires `sender.accessPointAddressType`, `recipient.accessPointAddressType` and `eInvoiceTypeCode`; the OpenAPI schema omits `eInvoiceTypeCode` from its required list. <span style="color:#666666;">Existing:</span> Retain returned resource identity and optional `erpInvoiceId` linkage; the ERP reference is not an idempotency guarantee. INT-SND01/02; SND-G04/07. |
| Self-billing and extra recipients | <span style="color:#666666;">Existing guide:</span> buyer-to-seller route, one recipient per submission. <span style="color:#B42318;">Open:</span> Qualify material issuer, represented business, actual destination, public-copy responsibility and supported `eInvoiceTypeCode`; the guide does not resolve those Spain roles. Accountant distribution remains OUT-Q02. SND-G02/06. |
| `AR_Invoice`, `AR_CreditNote`, `AP_CreditNote` | <span style="color:#666666;">Existing:</span> Preserve FR codes and the guide's type `381` association. <span style="color:#B42318;">Open:</span> Supplied public formats use UBL 2.5 `InvoiceType`, including rectification, not `CreditNote`. Confirm any public mapping; never infer it from the FR label. SPFE-S08 p. 8; SND-G03. |
| `attachments[].mimetype` / `filename` | <span style="color:#666666;">Existing:</span> Guide names `ubl-2.1/xml` and `application/pdf`, filename 1–128 and address values 1–50. <span style="color:#B42318;">Open:</span> It supplies no Spain UBL 2.5 MIME value. Qualify selected schemas, file roles and limits without silently extending them. SND-G02/03/07. |
| FR UBL/PDF or Factur-X choice | <span style="color:#666666;">Existing:</span> Real France UBL can have an optional PDF; Factur-X needs one hybrid file. Demo's two-file requirement is local. <span style="color:#B42318;">Open:</span> Public restrictions on embedded files are distinct from MIME transport of UBL business documents; do not forward a hybrid or auxiliary PDF by default. SPFE-S02 Articles 3.5/4.4; SPFE-S03 p. 11; SND-G03. |
| Public batch, identity and results | <span style="color:#666666;">Existing source:</span> Catalogue states 1–100 invoices and authority evaluated per invoice. <span style="color:#B42318;">Source conflict:</span> preserve the disputed 5120-byte unit limit; do not silently use KB. Business `200`/`406`/`400` request codes are not HTTP codes. Example locator/response fields do not prove CSV mapping. SPFE-S03/S08/S06; SND-G02. |
| Existing DTS | <span style="color:#666666;">Existing candidate:</span> Preferred transformation implementation candidate under PRD-SEI-223 FR43–46 and SPEC-SEI-008. <span style="color:#B42318;">Gap:</span> Prove Spain field coverage, profile/version coexistence, rule isolation, final-byte validation, semantic preservation and operational ownership. FR UBL 2.1 or Factur-X support alone cannot establish this. SND-G03. |

The OpenAPI calls `recipient.accessPointAddress` a Buyer key in the sender's ERP. This is a confirmed wording defect. The guide defines sender and recipient values as routing addresses, separate from invoice seller and buyer identities. `es.nif` is a Proposed Spain address-type value, aligned with SPEC-SEI-040; whether a tax NIF can serve as the routing address and how NIE is handled remain Open. INT-SND01/02; SND-G02.

| Identity purpose | Meaning and boundary |
|---|---|
| Tax identity | Seller NIF and buyer NIF or NIE identify the invoice parties for tax purposes. NIE is a NIF class for a foreign natural person, not a separate scheme. [PRD-SEI-101, “Seller NIF vs Buyer NIF/NIE”](../../../prds/PRD-SEI-101-public-platform-onboarding.md). |
| Routing address | Identifies the network participant or destination. A NIF is a routing-address value only where the selected network contract defines a scheme such as `es.nif`. |
| Certificate or signature | Any certificate or signature required for the selected action is separate from tax identity, routing address and authenticated-caller identity. Possession alone does not establish authority. |

Apply the six-case Spain recipient-route decision in [SPEC-SEI-023 OUT-09](../SPEC-SEI-023-invoice-sending-logical-feature-specification.md#3-process-and-activity-order).

`PRIVATE_READY` and `PROVEN_NONE` retain their existing meanings; the public-route decision also considers whether the customer communicated a private address. The two addressing pages are user-supplied. Their content status is **Content not preserved in this repository**. Their reported wording does not replace final legal evidence. Product and Spain Compliance must resolve the source conflicts. Until then, OUT-09 holds if the route condition is unclear. USR-ADDR01/02; OUT-09.

<a id="1-1-accesspointid-selection-semantics"></a>

### 1.1 `accessPointId` selection semantics

| Condition | Proposed result |
|---|---|
| No explicit `accessPointId` or it is null | <span style="color:#1565C0;">Proposed:</span> For Spain, resolve the configured active sender route only where the country contract permits omission or null. This must not change France's required-field contract. |
| Explicit selection is valid, connected and eligible | <span style="color:#1565C0;">Proposed under SND-G09 (option B):</span> In Phase 2, select only the active route or a ready public connection, subject to recipient-destination eligibility, and bind the route and evidence to the invoice plan. Use of another connected private platform is <span style="color:#B42318;">Open</span>. |
| Explicit selection is unknown, disconnected or ineligible | <span style="color:#1565C0;">Proposed:</span> Return a clear error to the ERP. Do not replace it with the configured point or another route. |
| No valid configured sender access point exists | <span style="color:#1565C0;">Proposed:</span> Return a clear configuration error; do not choose a public sender point or recipient route silently. |
| Several sender access points are configured | <span style="color:#1565C0;">Proposed:</span> Select exactly one for the invoice. Configuration never means fan-out. |

The sender access point may be public or private. It is the sender-side connection. The public recipient route is the recipient's destination under Spain policy. These are separate choices. The onboarding snapshots document access-point and connection operations, but not per-invoice selection. SND-G02; INT-AP07.

## 2 Proposed Spain extension of the Send e-invoice API

This section proposes how Sending could reuse the France API for Spain. `Existing` marks behaviour documented by the France contract or guide. `Proposed` marks intent that needs API and Spain qualification. Assumptions, open points and source conflicts remain unresolved. The snapshot describes the France contract. It does not prove deployment or Spain support. INT-SND01/02.

### Field changes by element

| Element | Change type | Label and required treatment |
|---|---|---|
| `Idempotency-Key` | No change | <span style="color:#666666;">Existing.</span> Keep its current purpose. Lifetime, input binding and safe replay remain SND-G04. |
| `erpInvoiceId` | No change | <span style="color:#666666;">Existing.</span> Preserve its current ERP-reference meaning; it is not an idempotency guarantee. |
| `upload` / returned `uploadUrl` | No change | <span style="color:#666666;">Existing.</span> Keep the current upload interaction and qualify completion/retry separately. |
| Status event | No change | <span style="color:#666666;">Existing.</span> Keep the event as processing evidence; it does not independently prove delivery or copy completion. |
| `GET` invoice detail | No change | <span style="color:#666666;">Existing.</span> Keep the detail read and current field meanings. |
| `attachments[].mimetype` | New value | <span style="color:#B42318;">Open.</span> A Spain UBL 2.5 MIME value is not confirmed. Do not put an invented value in a request. |
| `sender.accessPointAddressType` | New value | <span style="color:#1565C0;">Proposed:</span> `es.nif`, aligned with [SPEC-SEI-040 API-03](../../onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-03). <span style="color:#B42318;">Open:</span> confirm when NIF is a routing-address value and how NIE is handled. |
| `recipient.accessPointAddressType` | New value | <span style="color:#1565C0;">Proposed:</span> `es.nif`, aligned with [SPEC-SEI-040 API-03](../../onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md#api-03). <span style="color:#B42318;">Open:</span> confirm when NIF is a routing-address value and how NIE is handled. |
| `accessPointId` | Changed meaning | <span style="color:#1565C0;">Proposed Spain-only change:</span> when null, use the active sender route. France remains unchanged and retains its current required-field contract. |
| `eInvoiceTypeCode` | New value | <span style="color:#B42318;">Open:</span> Spain document mapping is not confirmed. |
| Recipient delivery and SPFE-copy results using `history[]` / `statusAttributes` | New field, if needed | <span style="color:#1565C0;">Proposed:</span> reuse existing history/status structures where meanings stay intact; add a per-action result shape only if needed. <span style="color:#B42318;">Open:</span> the wire contract remains under SND-G05. |
| Withdrawal reference | New call (under assessment; not approved) | <span style="color:#B42318;">Open:</span> see [FP-SEI-002](../../../feature-proposals/FP-SEI-002-global-api-submission-withdrawal.md). This is an assessment of a possible separate command, not an approved call or wire contract. No equivalent Sage capability is documented in the preserved contracts (<span style="color:#B42318;">Gap</span>). |

**Engineering conclusion:** Spain sending needs new values and a Spain-only changed meaning, not a new send call. Withdrawal is a possible separate command under assessment in FP-SEI-002. SPFE, SERES, EDICOM, ZeroComa and B2Brouter are platforms selected through `accessPointId`; they are not values of `accessPointAddressType`.

SPFE withdrawal applies only to an invoice already submitted when no real transaction existed and no rectifying invoice is required. The SPFE reference uses issuer NIF, series and number, and issue date. A rectifying invoice is an ERP/Compliance correction; stopping work before an external effect is separate. A permitted withdrawal is a recorded outcome, after which the identifier may be reused. See [SPEC-SEI-023 OUT-SPFE-R02](../SPEC-SEI-023-invoice-sending-logical-feature-specification.md#4-shared-controls-and-spain-binding). Withdrawal remains Open and is not an approved call.

### Contract baseline and reuse assessment

| Capability | Evidence label | Spain proposal and limit |
|---|---|---|
| `POST /datasets/{datasetId}/e-invoices`, returned resource ID and attachment upload URLs | <span style="color:#666666;">Existing</span> | Reuse the one-invoice resource and upload pattern. The POST accepts prepared files; preparation and ERP issuance remain outside this contract. INT-SND02; SND-G01. |
| `PUT {uploadUrl}`, status event, detail read, `currentStatus`, `history[]` and `statusAttributes` | <span style="color:#666666;">Existing</span> | Reuse as the observation baseline. Confirm event authentication, history correlation, freshness and Spain support. A processing status is not a recipient or public-copy result. INT-SND01/02; INT-ERR01; SND-G05. |
| Spain document and routing values | <span style="color:#1565C0;">Proposed</span> / <span style="color:#B42318;">Open</span> | Propose `es.nif` for sender and recipient address types. Spain UBL 2.5 MIME and document mapping, routing-address equivalence and NIE handling remain open. Do not copy France enum values into Spain. SND-G02/03. |
| Configured sender access point and explicit selection | <span style="color:#1565C0;">Proposed</span> | Use `accessPointId` as the leading candidate for explicit sender-access-point selection. For Spain, null means use the active route; the current snapshot calls it a “route destination,” so confirm the changed meaning. Do not confuse `accessPointId` with dataset-specific `connectionId`. France remains unchanged. SND-G02. |
| Separate delivery and SPFE action results | <span style="color:#1565C0;">Proposed</span> / <span style="color:#B42318;">Open</span> | Keep the existing status/history model where possible, with an additive per-action representation only if needed to make both outcomes independently observable. The example below is illustrative, not a wire contract. Private-platform copy-result/error reporting and failed-copy retry ownership are <span style="color:#B42318;">Gaps</span>. SND-G05. |
| Onboarding route and activation | <span style="color:#B42318;">Open — SND-G09</span> | Onboarding must confirm the shared decision because onboarding specs are not edited here. <span style="color:#666666;">Existing:</span> a saved connection does not activate a route; Private A to Private B switching is disabled; SPFE has no enrolment API (“SPFE use TBD”). <span style="color:#1565C0;">Proposed:</span> the administrator chooses the initial route (public or one private platform) for the dataset and sender address; authorised route changes are onboarding operations with their own authority/effective date; Phase 2 per-invoice choice (option B) is limited to the active route or a ready public connection. Use of another connected private platform remains Open. |
| Recipient lookup, route eligibility, customer configuration and access-point setup | Outside Sending | Owned by routing and onboarding. Sending consumes qualified sender configuration and recipient evidence; it does not create a national directory or connection. |
| UBL mapping, signing, SPFE transport and later lifecycle reports | Outside Sending | DTS, trust, public connector and lifecycle own their contracts. Sending coordinates the required handoffs and results. |

### Invoice document and file handling

SPFE-S08 and the product specifications identify UBL 2.5 for the public route. The France snapshot lists `ubl-2.1/xml` and `application/pdf`. It does not establish Spain MIME, profile or provider support. No Spain MIME value is proposed. DTS remains the preferred transformation candidate, subject to qualification. SPFE-S08; SND-G03.

The transitional PDF goes to the recipient. Exclude it from every SPFE request, including attachments. Use a qualified private attachment path or a separate recipient channel. UBL 2.5 profile support and each provider's file rules remain open. RD238-T2; INT-SND02; SND-G08.

### Response, notification and error proposal

Reuse `currentStatus`, `history[]` and `statusAttributes` for their existing processing meanings. The snapshot defines `IN_PROGRESS`, `COMPLETED` and `ERROR` for `operationStatus`. `ERROR` is final for one attempt. These fields do not identify recipient delivery or the required SPFE action. Do not map France processing codes to Spain business statuses. INT-SND02; INT-ERR01.

**Proposed:** If the current resource cannot show both outcomes independently, add an action-result concept to the response and notification pattern. Each result identifies its purpose, outcome, reason when present and next owner. Keep an action unresolved until evidence confirms its result. Do not show full completion while a required action remains unresolved. The API owner must qualify this proposal under SND-G05.

This request example uses existing field names. Bracketed values are placeholders, not approved Spain values. Each JSON key and value stays intact; adjacent colored text labels are annotations outside the values. Null illustrates the proposed Spain selection only, where the country contract permits it. The France schema still requires `accessPointId`. INT-SND02; SND-G02.

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-Invoice" <span style="color:#666666;">Existing</span>,
    "attributes": {
      "attachments": [
        {
          "filename": "invoice-example.xml" <span style="color:#666666;">Existing</span>,
          "mimetype": "[Spain UBL 2.5 MIME: not confirmed]" <span style="color:#B42318;">Open</span>
        }
      ],
      "sender": {
        "accessPointAddressType": "es.nif" <span style="color:#1565C0;">Proposed</span>,
        "accessPointAddress": "[sender NIF; routing use open]" <span style="color:#B42318;">Open</span>
      },
      "recipient": {
        "accessPointAddressType": "es.nif" <span style="color:#1565C0;">Proposed</span>,
        "accessPointAddress": "[recipient NIF or NIE; routing use open]" <span style="color:#B42318;">Open</span>
      },
      "accessPointId": null <span style="color:#1565C0;">Proposed</span>,
      "eInvoiceTypeCode": "[Spain document mapping]" <span style="color:#B42318;">Open</span>,
      "erpInvoiceId": "erp-invoice-example-42" <span style="color:#666666;">Existing</span>
    }
  }
}</code></pre>
<!-- confluence-html-macro:end -->

This response fragment is **Proposed**. It is not the current OpenAPI schema. `proposedActionResults` and its labels are unapproved placeholders. Recipient delivery may be complete while the required SPFE action is unresolved. Overall completion remains pending until both results are known. Support takes ownership only if platform recovery cannot resolve the outcome. SND-G05.

The fragment omits history entries, `meta` and an aggregate completion field for brevity. It does not define an aggregate field.

<!-- confluence-html-macro:start -->
<pre style="color:#666666;background-color:#f5f5f5;padding:12px;overflow-x:auto;"><code>{
  "data": {
    "type": "e-Invoice" <span style="color:#666666;">Existing</span>,
    "id": "85f5d2c4-0ea3-4fca-9b71-12b507f4c201" <span style="color:#666666;">Existing</span>,
    "attributes": {
      "currentStatus": null <span style="color:#666666;">Existing</span>,
      "proposedActionResults": [ <span style="color:#1565C0;">Proposed</span>
        {"purpose": "recipient delivery" <span style="color:#1565C0;">Proposed</span>, "outcome": "completed" <span style="color:#1565C0;">Proposed</span>},
        {
          "purpose": "required SPFE action" <span style="color:#1565C0;">Proposed</span>,
          "outcome": "unresolved" <span style="color:#1565C0;">Proposed</span>,
          "errorReason": "external result awaiting reconciliation" <span style="color:#1565C0;">Proposed</span>,
          "nextOwner": "platform recovery" <span style="color:#1565C0;">Proposed</span>
        }
      ]
    }
  }
}
</code></pre>
<!-- confluence-html-macro:end -->

Reuse the France notification and detail pattern after API qualification. The ERP result must identify the action, reason and next owner. Separate transport errors, Sending errors, content errors and business lifecycle results. Return content errors to the ERP for correction. A correction creates a governed invoice revision. Retry eligible technical work only after reconciling the original result. Preserve completed actions. A failed invoice need not block later invoices. Sending cannot detect invoices the ERP never submitted without a separate capability. Keep accepted work visible and recoverable. SND-G04/05/07; OUT-A23/24.

### Scenario coverage

| Scenario | Proposed Sending behaviour | Boundary / open evidence |
|---|---|---|
| A. Public platform only | <span style="color:#1565C0;">Proposed:</span> Use the eligible public recipient route. No separate faithful copy is added after public issuance/interconnection. | Public eligibility and the six-case Spain recipient rule remain under OUT-09/SND-G02. |
| B. Private delivery plus required SPFE action | <span style="color:#1565C0;">Proposed:</span> Plan private recipient delivery and the required SPFE action as separate results. In Phase 2, the selected private platform sends the copy; this capability is an <span style="color:#B42318;">Assumption</span>, expected but unconfirmed. The user-supplied `PPIFE_competitor_analysis.xlsx` marks SPFE integration as pending and is not preserved in this repository. | Prove the boundary between issuance and copy, action correlation and partial/lost-result recovery. How the private platform reports copy results/errors to Sage and who retries a failed copy are <span style="color:#B42318;">Gaps</span> under SND-G05. |
| C. Several configured private providers | <span style="color:#1565C0;">Proposed (option B):</span> Phase 2 per-invoice choice is limited to the active route or the public platform when its connection is ready. It does not connect providers, change the active route or change configuration. Never fan out. | Per-invoice use of another connected private platform is <span style="color:#B42318;">Open</span> for onboarding confirmation under SND-G09. |
| D. Sage operates as a private platform | <span style="color:#1565C0;">Proposed:</span> When Sage operates as the private platform, Sage sends the required SPFE copy. Keep the sender-platform role and delivery/copy results separate. | Provider-facing APIs and operator service remain outside this Sending proposal. Copy result/error reporting and failed-copy retry ownership remain open under SND-G05. |

### Contract issues and compatibility

These are issues in the preserved snapshot and guide, not verified runtime defects. API owners must decide corrections against the selected contract.

#### Confirmed schema inconsistency

| Snapshot locator | Inconsistency | Consequence |
|---|---|---|
| `SendInvoiceResponse.required`; `SendInvoiceResponse.properties` | <span style="color:#B42318;">Gap:</span> `documents` is required, but the schema defines `attachments` and no `documents` property. | Correct the schema/example inconsistency in the owning API contract; do not assume which name runtime uses. |

#### Missing definition

| Snapshot locator | Missing definition | Consequence |
|---|---|---|
| `SendInvoiceRequest.required` and `.accessPointId` | <span style="color:#B42318;">Open:</span> the field is required but its type allows `null`; the meaning of null is undefined. | Spain proposes that null means use the active route. Keep France unchanged; qualify the country-specific contract. |
| `SendInvoiceRequest.sender` and `.recipient` | <span style="color:#B42318;">Open:</span> both parent properties are required, but neither nested object declares required child properties. | The schema does not enforce the address type/value required by the guide. |
| `SendInvoiceRequest.attachments` | <span style="color:#B42318;">Open:</span> the array schema has no `minItems`. | Empty attachment-list behaviour is not constrained by this schema. |

#### Guide and schema conflict

| Snapshot locator / guide | Conflict | Consequence |
|---|---|---|
| `traceparent` and `tracestate`; INT-SND01 step 2 | <span style="color:#B42318;">Source conflict:</span> both headers have `required: false` in the OpenAPI snapshot, but INT-SND01 says they are required. | Keep the conflict open and confirm the selected contract. Do not describe them as required based on the snapshot. |
| `SendInvoiceRequest.required` and `.eInvoiceTypeCode`; INT-SND01 | <span style="color:#B42318;">Source conflict:</span> the schema omits `eInvoiceTypeCode` from the required list, while INT-SND01 says it is required. | Resolve the source conflict and confirm Spain document mapping separately. |
| `SendInvoiceRequest.recipient.accessPointAddress`; INT-SND01 | <span style="color:#B42318;">Source conflict:</span> snapshot description identifies a Buyer key in the sender ERP, while the guide defines sender and recipient values as network-routing addresses. | Correct the contract description; do not treat NIF or ERP buyer ID as the network address without a qualified mapping. |

Other relevant preserved onboarding contract issues are: `GET /accesspoints` declares `datasetId` as a path parameter although the path has no placeholder; connection requests allow address `maxLength` 114, while connection responses and Sending allow 50; string length constraints use `maximum` in some request properties; and the create example uses invalid IPv4 `183.342.1.1`. The postal-code example is numeric although the schema type is string; this confirms a type/example mismatch, not that `12345` is an invalid postal code. Preserve these as onboarding/API-owner follow-ups, not new Sending requirements. INT-AP07.

Keep France behaviour compatible: Spain additions must be country-qualified, and must not make France `accessPointId` optional or change France file/profile values. Do not rewrite historical plans or action outcomes after route/configuration changes. The dataset's country binding and how Spain applies the new omission/null behaviour remain Open under SND-G02/07. No implementation or deployment claim follows from this proposal.

## REF Source references

| ID | Source / version and exact locator | Supports / limit |
|---|---|---|
| INT-SND01 | [FR sending guide extract](<../../../context/FR API/Sending/send-e-invoice-guide-extract.md>), received 22 October 2026; prerequisites, Submission design requirements and steps 1–5 | Guide field meanings, operations and required-header claims. Revision and deployed build are unknown. |
| INT-SND02 | [Preserved Send e-invoice OpenAPI snapshot](<../../../context/FR API/Sending/send-e-invoice-openapi.md>), OpenAPI 3.1.0, info version 1.0.0; POST request/response schemas, parameters and history item schema | Existing France-oriented fields and schema facts. `traceparent` and `tracestate` are optional in this snapshot. It does not establish deployment or Spain support. |
| REF-ONBOARDING | [SPEC-SEI-038](../../onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md), §§3.2/6.7; [SPEC-SEI-039](../../onboarding-and-connectivity/SPEC-SEI-039-customer-onboarding-and-connectivity-sequence-and-reuse-assessment.md), draft updated 29 October 2026, §3 colour convention and GAP-02; [SPEC-SEI-040](../../onboarding-and-connectivity/api-reference/SPEC-SEI-040-existing-e-invoice-onboarding-api-reference.md), API-03/04 and “How to read the examples” | Existing connection/activation/provider-switching boundaries, proposed `es.nif` value and label convention. GAP-02 and sending route choices remain open; onboarding proposals do not prove live Spain support. |
| PRD-SEI-101 | [Public Platform Onboarding PRD](<../../../prds/PRD-SEI-101-public-platform-onboarding.md>), linked product topic “Seller NIF vs Buyer NIF/NIE” | Tax identity distinction, including seller/buyer NIF/NIE purpose. The PRD topic does not establish that a NIF is a routing address. |
| SPFE-S02 | [Original BOE Order HAC/1028/2026](<../../../context/BOE-A-2026-20587.pdf>), published 5 October 2026; Articles 3.4–3.6, 4 and 5.5–5.6 | Legal copy, withdrawal and correction conditions. It does not define a Sage API contract. |
| SPFE-S03 | [Original public service catalogue](<../../../context/Descripción servicios web/Catálogo de servicios/20261013/CatalogoServicios.pdf>), draft 0.1.0, 9 October 2026; §6.3, pp. 11–12 | Withdrawal operation purpose and business conditions. It does not select a Sage endpoint or wire contract. |
| SPFE-S08 | [Original public formats](<../../../context/Descripción servicios web/Formatos entrada y salida/20261013/FormatosEntradaSalida.pdf>), draft 0.1.0, 9 October 2026; §5.1.1, p. 8 | Public UBL 2.5 format evidence. It does not establish a MIME value for the France Sending API. |
| USR-ADDR01/02 | User-supplied [Invoice addresses Spain](https://confluence.sage.com/spaces/DNBU/pages/837611067/Invoice+addresses+Spain), supplied 28 October 2026; “Spain - March 2026 e-invoice update”, Intra-Compliance page URL/content not preserved | The reported public-by-default wording conflicts with the proposed hold after a no-match when a private address was supplied. Content is not preserved and is not final legal evidence. |
| SPFE-S16 / SPFE-S10 | [SPEC-SEI-023](../SPEC-SEI-023-invoice-sending-logical-feature-specification.md#ref-source-references), existing combined `SPFE-S16 / SPFE-S10` row with original WSDL links; [SPEC-SEI-024](../SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md#ref-source-references), existing `SPFE-S16` row | PRE transport evidence for `SendInvoice` and `CancelInvoice`; does not establish a Sage withdrawal call or production readiness. The source rows are unchanged in this revision. |
| FP-SEI-002 | [Global API submission withdrawal review proposal](<../../../feature-proposals/FP-SEI-002-global-api-submission-withdrawal.md>), draft updated 29 October 2026; “Proposed direction and decisions” and “Review outcome and acceptance evidence” | Assesses a distinct withdrawal command but selects no endpoint, payload or wire status. It is not an approved call. |
