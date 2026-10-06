---
id: PRD-SEI-246
title: Spain Invoice Preparation and Outbound Flow
type: prd
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-05
updated: 2026-10-05
reviewers: []
related:
  - PRD-SEI-244
  - PRD-SEI-223
  - PRD-SEI-241
confluence:
  publish: false
  page_id: ""
---

# Spain Invoice Preparation and Outbound Flow

## Revision overview

This separate review draft combines the ERP preparation journey in the supplied process-flow screenshot with the outbound exchange controls in [PRD-SEI-244](PRD-SEI-244-e-invoicing-process-flow-specification.md). It exists so the combined diagram can be validated before the user copies it into the appropriate PRD.

The changes are complete draft-data submission before issuance, service-assisted preparation and validation, ERP-owned issuance, final-data submission, and an explicit Spain public-platform default when recipient lookup successfully establishes that no private receipt entry point exists. Authorisation, final representation checks, correlated dispatch, separate delivery/copy evidence and reconciliation remain part of the exchange flow.

The original process-flow specification and its diagrams remain unchanged. PRD-SEI-244 remains the selected Git source for its stable Confluence page. This draft is not selected for publication. Open decisions are listed below; the diagram is a business-flow proposal rather than an approved API or regulatory specification.

## Combined process flow

![Spain invoice preparation and outbound exchange](../assets/diagrams/spain-invoice-preparation-and-outbound-flow.svg)

**Editable source:** [Draw.io diagram](../assets/diagrams/spain-invoice-preparation-and-outbound-flow.drawio). **Display preview:** [PNG](../assets/diagrams/spain-invoice-preparation-and-outbound-flow.png).

**Presentation:** Grey and white, horizontal responsibility lanes and four phase bands, following the existing outbound pilot. Shapes distinguish ERP input/output, service tasks, decisions, rule/plan documents, retained evidence, external parties and hold/recovery actions. Short exception branches identify correction or recovery; they do not imply automatic reissuance.


The recipient branches are alternatives. The public-copy branch is a separate conditional obligation, not another recipient delivery. Observation arrows into the result step do not represent a synchronous join: each leg may produce an acknowledgement or later outcome independently. A known result remains visible while another leg is pending or uncertain.

## Agreed business boundaries

| Area | Working agreement |
|---|---|
| Country | This diagram is specific to Spain; public fallback is not a universal country rule. |
| ERP input | ERP submits complete invoice data rather than being required to supply a finished electronic invoice file. |
| Complete invoice data | Includes issuer, recipient, type, dates, lines, quantities, prices, taxes, totals and applicable references or attachments. It excludes unrelated ERP records. The exact API field contract remains to be defined. |
| Before issuance | Service helps prepare and validate the draft. Issues return to ERP for correction. |
| Issuance | ERP owns the issuance action and submits the final issued identity and exact revision. A successful draft check does not prove the final revision is valid. |
| Recipient lookup | Check during preparation and confirm before dispatch. A successful lookup showing no private receipt entry point selects public-platform delivery automatically. |
| Lookup failure | Failed, stale or ambiguous evidence does not establish absence of a destination. Recover or refresh before selecting the route. |
| Public delivery versus copy | Public recipient delivery and a faithful public copy are distinct purposes. The exchange plan determines the required legs and tracks them independently. |
| Completion | Draft validation, ERP issuance, dispatch, platform acknowledgement, recipient delivery and buyer acceptance remain distinct states. |
| Recovery | Reconcile an uncertain external operation against its original route and leg before retry. Do not repeat a completed leg. |

## Decisions still to validate

1. **Draft-to-final contract:** define required data, final identifiers, revision binding and how an ERP change invalidates earlier preparation results.
2. **Preparation ownership:** the diagram places final electronic representation preparation in the service. Confirm the draft artefact returned to ERP and ownership/timing of the human-readable version; that version is not assumed to be a prerequisite for sending.
3. **Early lookup failure:** the diagram reports route status during preparation. Decide whether unresolved early lookup prevents issuance; the final dispatch gate blocks sending while the route is unknown.
4. **Issued-invoice correction:** define which failures can be resolved without changing invoice content and which require the ERP's applicable correction process. There is no automatic return from an issued invoice to a draft.
5. **Route eligibility and bridging:** a discovered private entry point still needs an eligible operational route. Apply the existing Spain interconnection/bridge rules; do not treat finding an address as proof of readiness.
6. **Public-copy sequence and outcome vocabulary:** confirm the required copy conditions, dispatch timing and available platform evidence against the approved Spain technical specifications. This business diagram does not define a sequential delivery-then-copy dependency.

## Validation scenarios

- Invalid draft: issues return to ERP; no issuance or external invoice transmission occurs through this flow.
- Final issued data differs from the validated draft: the service checks the actual submitted final revision before dispatch.
- Valid final data and an eligible private recipient route: deliver on that route and execute any independently required faithful-copy obligation.
- Successful authoritative lookup finds no private receipt entry point: automatically plan recipient delivery through the Spain public platform.
- Recipient lookup times out: recover lookup; do not select public fallback solely because of the timeout.
- Recipient delivery succeeds but public-copy outcome is unknown: retain delivery success and reconcile the copy leg only.
- Public platform acknowledges submission: display the supported evidence level; do not infer recipient retrieval or buyer acceptance.

## Repository references

- [Existing process-flow specification — PRD-SEI-244](PRD-SEI-244-e-invoicing-process-flow-specification.md)
- [Spain exchange, routing and transformation — PRD-SEI-223](PRD-SEI-223-interoperability-routing-transformation.md), especially business rules BR3, BR7 and BR8, journeys J1/J2 and the no-private-entry-point acceptance scenario.
- [UBL validation service — PRD-SEI-241](PRD-SEI-241-ubl-validation-service.md)

These are repository references for review, not a new verification of current legal or external API requirements.
