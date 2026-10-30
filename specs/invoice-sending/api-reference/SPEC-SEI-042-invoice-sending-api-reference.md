---
id: SPEC-SEI-042
title: Invoice Sending API Reference and Spain Changes
type: api-reference
status: draft
owner: Jiaxin He
product: spain-e-invoicing
created: 2026-10-30
updated: 2026-10-30
reviewers: []
related:
  - SPEC-SEI-024
  - SPEC-SEI-022
  - SPEC-SEI-023
  - GLO-SEI-001
confluence:
  publish: false
  space_key: DNBU
  parent_page_id: "837610656"
  page_id: ""
  title: Invoice Sending API Reference and Spain Changes
  layout: two_left_sidebar
  toc: true
---

# Invoice Sending API Reference and Spain Changes

[Sequence and Reuse Assessment](../SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md) · [Solution Summary](../SPEC-SEI-022-invoice-sending-solution-summary.md) · [Logical Feature Specification](../SPEC-SEI-023-invoice-sending-logical-feature-specification.md) · [Feature landing page](../README.md)

## Summary

This page owns request/response examples, detailed API fields, the field-level reuse map and confirmed contract defects. [SPEC-SEI-024](../SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md) owns sequences, gaps and decisions.

## How to read the examples

Examples use the preserved France-oriented contract and proposed Spain values where explicitly labelled. Proposed values and response fields are not approved wire contracts or implementation evidence.

<a id="1-identity-routing-and-representation"></a>

## 1 Identity, routing and representation differences

| Evidence / exact fields | Required qualification and consequence |
|---|---|
| `sender`, `recipient`, `accessPointAddressType`, `accessPointAddress`, `accessPointId` | INT-SND01 defines sender and recipient as network-routing addresses, separate from seller/buyer in invoice content. The snapshot describes `recipient.accessPointAddress` as a Buyer key in the sender ERP; this is a confirmed wording defect. NIF is a legal tax identifier, not automatically a routing address. Spain schemes and values remain Open; do not replace `fr.siren` with an invented Spain enum. The snapshot calls `accessPointId` a route destination; using it to select the sender's access point is Proposed and needs API-owner qualification. SND-G02; OUT-R04/11; INT-SND01/02. |
| Submission's required values and correlation | INT-SND01 says the guide requires `sender.accessPointAddressType`, `recipient.accessPointAddressType` and `eInvoiceTypeCode`; the OpenAPI schema omits `eInvoiceTypeCode` from its required list. Preserve this source conflict. Retain returned resource identity and optional `erpInvoiceId` linkage; the ERP reference is not an idempotency guarantee. INT-SND01/02; SND-G04/07. |
| Self-billing and extra recipients | Guide routes buyer to seller, one recipient per submission. Qualify material issuer, represented business, actual destination, public-copy responsibility and supported `eInvoiceTypeCode`; the guide does not resolve those Spain roles. Accountant distribution remains OUT-Q02. SND-G02/06. |
| `AR_Invoice`, `AR_CreditNote`, `AP_CreditNote` | Preserve FR codes and the guide's type `381` association. Supplied public formats use UBL 2.5 `InvoiceType`, including rectification, not `CreditNote`. Confirm any public mapping; never infer it from the FR label. SPFE-S08 p. 8; SND-G03. |
| `attachments[].mimetype` / `filename` | Guide names `ubl-2.1/xml` and `application/pdf`, filename 1–128 and address values 1–50. It supplies no Spain UBL 2.5 MIME value. Qualify selected schemas, file roles and limits without silently extending them. SND-G02/03/07. |
| FR UBL/PDF or Factur-X choice | Real France UBL can have an optional PDF; Factur-X needs one hybrid file. Demo's two-file requirement is local. Public restrictions on embedded files are distinct from MIME transport of UBL business documents; do not forward a hybrid or auxiliary PDF by default. SPFE-S02 Articles 3.5/4.4; SPFE-S03 p. 11; SND-G03. |
| Public batch, identity and results | Catalogue states 1–100 invoices, authority evaluated per invoice and a disputed 5120-byte unit limit. Preserve the conflict with supplied examples; do not silently use KB. Business `200`/`406`/`400` request codes are not HTTP codes. Example locator/response fields do not prove CSV mapping. SPFE-S03/S08/S06; SND-G02. |
| Existing DTS | Preferred transformation implementation candidate under PRD-SEI-223 FR43–46 and SPEC-SEI-008. Prove Spain field coverage, profile/version coexistence, rule isolation, final-byte validation, semantic preservation and operational ownership. FR UBL 2.1 or Factur-X support alone cannot establish this. SND-G03. |

The OpenAPI calls `recipient.accessPointAddress` a Buyer key in the sender's ERP. This is a confirmed wording defect. The guide defines sender and recipient values as routing addresses, separate from invoice seller and buyer identities. Spain address schemes and mappings remain open. No Spain address-type value is proposed. INT-SND01/02.

The Spain route distinction is:

| Evidence condition | Proposed handling | Status |
|---|---|---|
| `PRIVATE_READY` | A published private destination is eligible under the confirmed interconnection or bridge rule. Use that destination. | Existing outcome meaning; qualify for Spain |
| `PROVEN_NONE` | A successful authoritative lookup confirms no private receiving entry point. Under Spain policy, use the public recipient route. PRD-SEI-231 ID-AC14; PRD-SEI-223 BR3. | Existing outcome meaning; Spain rule source |
| No private address has been communicated to the sender by the recipient | Use the public route only if the approved Spain rule accepts this evidence and it is retained. | Proposed separate condition; evidence and rule open |
| Private entry point is published and matches the invoice scope | Select it only after route eligibility and interconnection/bridge conditions are confirmed. | Proposed; route qualification Open |
| Lookup fails, is stale, unsupported or ambiguous | Hold dispatch. These outcomes prove neither that no private address has been communicated to the sender by the recipient nor that no private route exists. | Proposed control |
| No central authoritative directory can return the required evidence | Do not convert the missing directory or failed query into proof of absence or lack of recipient communication. Product and Spain Compliance must define acceptable alternate evidence and release conditions. | Source conflict/Open |

The two addressing pages are user-supplied. Their content status is **Content not preserved in this repository**. Their reported wording does not replace final legal evidence. Product and Spain Compliance must resolve the source conflict. Until then, OUT-09 holds if the route condition is unclear. USR-ADDR01/02; OUT-09.

<a id="1-1-accesspointid-selection-semantics"></a>

### 1.1 `accessPointId` selection semantics

| Condition | Proposed result |
|---|---|
| No explicit `accessPointId` or it is null | For Spain, resolve the configured sender access point only where the country contract permits omission or null. This must not change France's required-field contract. |
| Explicit selection is valid, connected and eligible | Use that sender access point for this invoice, subject to recipient-destination eligibility. Bind the selected route and evidence to the invoice plan. |
| Explicit selection is unknown, disconnected or ineligible | Return a clear error to the ERP. Do not replace it with the configured point or another route. |
| No valid configured sender access point exists | Return a clear configuration error; do not choose a public sender point or recipient route silently. |
| Several sender access points are configured | Select exactly one for the invoice. Configuration never means fan-out. |

The sender access point may be public or private. It is the sender-side connection. The public recipient route is the recipient's destination under Spain policy. These are separate choices. The onboarding snapshots document access-point and connection operations, but not per-invoice selection. SND-G02; INT-AP07.

## 2 Proposed Spain extension of the Send e-invoice API

This section proposes how Sending could reuse the France API for Spain. `Existing` marks behaviour documented by the France contract or guide. `Proposed` marks intent that needs API and Spain qualification. Assumptions, open points and source conflicts remain unresolved. The snapshot describes the France contract. It does not prove deployment or Spain support. INT-SND01/02.

### Contract baseline and reuse assessment

| Capability | Evidence label | Spain proposal and limit |
|---|---|---|
| `POST /datasets/{datasetId}/e-invoices`, returned resource ID and attachment upload URLs | Existing | Reuse the one-invoice resource and upload pattern. The POST accepts prepared files; preparation and ERP issuance remain outside this contract. INT-SND02; SND-G01. |
| `PUT {uploadUrl}`, status event, detail read, `currentStatus`, `history[]` and `statusAttributes` | Existing | Reuse as the observation baseline. Confirm event authentication, history correlation, freshness and Spain support. A processing status is not a recipient or public-copy result. INT-SND01/02; INT-ERR01; SND-G05. |
| Spain document and routing values | Extend | Preserve field names only where the selected Spain contract supports their meaning. Spain UBL 2.5, address schemes, recipient scope and MIME remain open. Do not copy France enum values into Spain. SND-G02/03. |
| Configured sender access point and explicit selection | Proposed | Use `accessPointId` as the leading candidate for explicit sender-access-point selection. The current snapshot calls it a “route destination”; its sender-side meaning is unconfirmed. Do not confuse `accessPointId` with dataset-specific `connectionId`. SND-G02. |
| Separate delivery and SPFE action results | Proposed | Keep the existing status/history model where possible, with an additive per-action representation only if needed to make both outcomes independently observable. The example below is illustrative, not a wire contract. SND-G05. |
| Recipient lookup, route eligibility, customer configuration and access-point setup | Outside Sending | Owned by routing and onboarding. Sending consumes qualified sender configuration and recipient evidence; it does not create a national directory or connection. |
| UBL mapping, signing, SPFE transport and later lifecycle reports | Outside Sending | DTS, trust, public connector and lifecycle own their contracts. Sending coordinates the required handoffs and results. |

### Invoice document and file handling

SPFE-S08 and the product specifications identify UBL 2.5 for the public route. The France snapshot lists `ubl-2.1/xml` and `application/pdf`. It does not establish Spain MIME, profile or provider support. No Spain MIME value is proposed. DTS remains the preferred transformation candidate, subject to qualification. SPFE-S08; SND-G03.

The transitional PDF goes to the recipient. Exclude it from every SPFE request, including attachments. Use a qualified private attachment path or a separate recipient channel. UBL 2.5 profile support and each provider's file rules remain open. RD238-T2; INT-SND02; SND-G08.

### Response, notification and error proposal

Reuse `currentStatus`, `history[]` and `statusAttributes` for their existing processing meanings. The snapshot defines `IN_PROGRESS`, `COMPLETED` and `ERROR` for `operationStatus`. `ERROR` is final for one attempt. These fields do not identify recipient delivery or the required SPFE action. Do not map France processing codes to Spain business statuses. INT-SND02; INT-ERR01.

**Proposed:** If the current resource cannot show both outcomes independently, add an action-result concept to the response and notification pattern. Each result identifies its purpose, outcome, reason when present and next owner. Keep an action unresolved until evidence confirms its result. Do not show full completion while a required action remains unresolved. The API owner must qualify this proposal under SND-G05.

This request example uses existing field names. Bracketed values are placeholders, not approved Spain values or a valid payload. Null illustrates the proposed Spain selection only, where the country contract permits it. The France schema still requires `accessPointId`. INT-SND02; SND-G02.

```json
{
  "data": {
    "type": "e-Invoice",
    "attributes": {
      "attachments": [
        {"filename": "invoice-example.xml", "mimetype": "[Spain UBL 2.5 MIME: open]"}
      ],
      "sender": {
        "accessPointAddressType": "[Spain routing scheme: open]",
        "accessPointAddress": "[sender routing address]"
      },
      "recipient": {
        "accessPointAddressType": "[Spain routing scheme: open]",
        "accessPointAddress": "[recipient routing address]"
      },
      "accessPointId": null,
      "eInvoiceTypeCode": "[Spain document mapping: open]",
      "erpInvoiceId": "erp-invoice-example-42"
    }
  }
}
```

This response fragment is **Proposed**. It is not the current OpenAPI schema. `proposedActionResults` and its labels are unapproved placeholders. Recipient delivery may be complete while the required SPFE action is unresolved. Overall completion remains pending until both results are known. Support takes ownership only if platform recovery cannot resolve the outcome. SND-G05.

The fragment omits history entries, `meta` and an aggregate completion field for brevity. It does not define an aggregate field.

```json
{
  "data": {
    "type": "e-Invoice",
    "id": "85f5d2c4-0ea3-4fca-9b71-12b507f4c201",
    "attributes": {
      "currentStatus": null,
      "proposedActionResults": [
        {"purpose": "recipient delivery", "outcome": "completed"},
        {
          "purpose": "required SPFE action",
          "outcome": "unresolved",
          "errorReason": "external result awaiting reconciliation",
          "nextOwner": "platform recovery"
        }
      ]
    }
  }
}
```

Reuse the France notification and detail pattern after API qualification. The ERP result must identify the action, reason and next owner. Separate transport errors, Sending errors, content errors and business lifecycle results. Return content errors to the ERP for correction. A correction creates a governed invoice revision. Retry eligible technical work only after reconciling the original result. Preserve completed actions. A failed invoice need not block later invoices. Sending cannot detect invoices the ERP never submitted without a separate capability. Keep accepted work visible and recoverable. SND-G04/05/07; OUT-A23/24.

### Scenario coverage

| Scenario | Proposed Sending behaviour | Boundary / open evidence |
|---|---|---|
| A. Public platform only | Use the eligible public recipient route. No separate faithful copy is added after public issuance/interconnection. | Public eligibility and the Spain recipient-default evidence rule remain under OUT-09/SND-G02. |
| B. Private delivery plus required SPFE action | Plan private recipient delivery and the required SPFE action as separate results. One ERP-facing request coordinated by Sage is an Assumption under OUT-Q03. | Prove the boundary between issuance and copy, action correlation and recovery from partial or lost results. |
| C. Several configured private providers | Use one configured sender access point or one valid explicit selection. Never fan out. Keep recipient destination separate and require recipient-routing eligibility. | `accessPointId` sender-side semantics and provider contracts need API-owner confirmation. |
| D. Sage operates as a private platform | **Proposed:** Sage may share the ERP-facing connection model with other private platforms. Keep the sender-platform role and required public-copy responsibility visible. | Limited outline only. Provider-facing APIs and operator service remain outside this Sending proposal. |

### Confirmed contract defects and compatibility

The following are defects in the preserved snapshot, not verified runtime defects. Record only these confirmed schema/documentation issues; API owners must decide corrections.

| Snapshot locator | Confirmed defect | Consequence for proposal |
|---|---|---|
| `SendInvoiceResponse.required`; `SendInvoiceResponse.properties` | `documents` is required, but the schema defines `attachments` and no `documents` property. | Fix the schema/example inconsistency in the owning API contract; do not assume which name runtime uses. |
| `SendInvoiceRequest.sender` and `.recipient` | Both parent properties are required, but neither nested object declares required child properties. | The schema does not enforce the address type/value that the guide says to supply. |
| `SendInvoiceRequest.required` and `.eInvoiceTypeCode` | `eInvoiceTypeCode` is absent from the required list, while INT-SND01 says it is required. | Resolve as a source conflict and align the selected contract. |
| `SendInvoiceRequest.attachments` | Array schema has no `minItems`. | Empty attachment-list behaviour is not constrained by this schema. |
| `SendInvoiceRequest.required` and `.accessPointId` | Field is required but its type allows `null`; null behaviour is undocumented. | The proposed Spain configured-point fallback is additive and requires an explicit country/compatibility contract. |
| `SendInvoiceRequest.recipient.accessPointAddress` | Description identifies a Buyer key in the sender ERP, conflicting with the guide's routing-address meaning. | Correct the contract description; do not treat NIF or ERP buyer ID as the network address without a qualified mapping. |

Other relevant preserved onboarding contract issues are: `GET /accesspoints` declares `datasetId` as a path parameter although the path has no placeholder; connection requests allow address `maxLength` 114, while connection responses and Sending allow 50; string length constraints use `maximum` in some request properties; and the create example uses invalid IPv4 `183.342.1.1`. The postal-code example is numeric although the schema type is string; this confirms a type/example mismatch, not that `12345` is an invalid postal code. Preserve these as onboarding/API-owner follow-ups, not new Sending requirements. INT-AP07.

Keep France behaviour compatible: Spain additions must be country-qualified, and must not make France `accessPointId` optional or change France file/profile values. Do not rewrite historical plans or action outcomes after route/configuration changes. The dataset's country binding and how Spain applies the new omission/null behaviour remain Open under SND-G02/07. No implementation or deployment claim follows from this proposal.
