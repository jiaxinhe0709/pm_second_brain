---
id: RES-SEI-010
title: UK Peppol customer and product scenarios
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-005
  - RES-SEI-009
  - PRD-SEI-230
  - PRD-SEI-231
  - PRD-SEI-242
confluence:
  publish: false
  page_id: ""
---

# UK Peppol customer and product scenarios

UK businesses need to know whether they can exchange a particular invoice, what happened and what they can safely do next. Accountants need the same clarity for each represented client. Products and support need to distinguish a customer data problem, an unavailable route, uncertain delivery and a buyer decision.

The baseline journeys already exist in [PRD-SEI-230](../../../prds/PRD-SEI-230-uk-e-invoicing-compliance-pack.md#business-scenarios), UK-S1–UK-S12. Global lifecycle qualification is defined by PG-01–PG-07 in [RES-SEI-005](../global/RES-SEI-005-network-and-participant-lifecycle.md#scenario-evidence-to-obtain). The cases below add UK research variants and consultation questions. They do not restate those requirements or approve a UK technical contract.

## Actors and research outcomes

| Actor | Outcome to understand | Evidence to collect |
|---|---|---|
| Small business owner | Prepare or correct data without learning network internals | Product walkthroughs and synthetic invoices showing real data gaps |
| Finance team | Send, receive and reconcile without duplicate work | Current issue/import/reconciliation flows and exception handling |
| Accountant | Act for the correct client and capability | Firm/client access, authority and handover journeys |
| Product/API consumer | Present actionable results and recover missed events | Data contracts, current product fields and status wording |
| Support/operations | Locate the failure and identify the next responsible actor | Trace and runbook examples across provider boundaries |

Use synthetic data or permitted summaries. Do not add raw customer exports or personal data to the research folder.

## Proposed UK scenario extensions

| ID | Actor, condition and trigger | Outcome to investigate | Exception and safe next action | Baseline relationship |
|---|---|---|---|---|
| UKR-01 | UK business already exchanges public-sector invoices and prepares for the VAT mandate | Identify which current identity, profile, registration and product evidence can be reused | Existing NHS/B2G setup is not treated as universal 2029 readiness; assess the missing country gates | UK-S1/9; PG-02; UK04/UK06 |
| UKR-02 | Small business currently creates unstructured invoices and seeks a transition route | Show missing business data, product capability and supported assistance | No final exemption or compliant fallback is invented; retain the policy question with an owner | UK-S1/6; UK01/UK03 |
| UKR-03 | Accountant prepares one client already registered elsewhere and another new client | Resolve authority and registration separately for each client | A valid firm login does not permit registration takeover or actions for all clients | UK-S8/10; PG-01/02/06 |
| UKR-04 | Business uses separate sales and purchase systems | Establish sending, receiving and evidence-access arrangements independently | Sending readiness does not imply receiving/import readiness; name the missing capability | UK-S2/3/9; PG-01/05 |
| UKR-05 | A group or multi-entity customer uses a shared Sage workspace | Associate each invoice and participant with the correct legal subject under the qualified policy | Do not infer legal entity or participant ownership from workspace membership or a shared tax fact | UK-S8/9; PRD-SEI-231 |
| UKR-06 | Seller trades across borders or has GB/Northern Ireland transaction context | Determine applicable scope, identifier, profile and any separate obligations | Return a specific unresolved applicability/profile decision; no guessed UK result or silent remapping | UK-S12; RES-SEI-007 cross-border assessment |
| UKR-07 | Product exposes a credit or self-billing feature | Establish final UK coverage and the selected document/process before claiming support | Standard invoice support is not reused as proof of every document variant | UK-S2/7; P06/P08 |
| UKR-08 | Seller uses a process with a business-response expectation | Explain which feedback is expected and which customer action follows | Missing optional feedback does not become rejection; timeout after possible send uses PG-04 | UK-S2/5; P07; PRD-SEI-242 |
| UKR-09 | Buyer product rejects an imported invoice after network delivery | Show network evidence separately from the local import or buyer-processing result | Do not resend merely because a local accounting task failed; recover the failed handoff | UK-S3/5; PG-05; PRD-SEI-242 |
| UKR-10 | Customer changes accountant, product or provider with invoices in flight | Preserve effective authority and evidence access through the change | Revoked access stops new unauthorised action; registration and in-flight work follow the qualified transfer plan | UK-S8/10; PG-06/07 |

Source IDs refer to [RES-SEI-003](../RES-SEI-003-peppol-source-register.md). UK policy facts are authoritative in RES-SEI-009; external message meanings remain in PRD-SEI-242. The desired research outcomes in this table are proposed product analysis, not statutory requirements.

## Product evidence to inspect

| Product surface | Specific questions |
|---|---|
| Customer/business setup | Can the product distinguish tenant, legal entity, VAT facts, participant and authorised delegate? |
| Invoice creation | Which fields needed by the selected candidate profile are absent, derived or held as free text? |
| Invoice correction | Can a user understand a field/rule issue, correct it and preserve the invoice's lineage? |
| Sending and receiving | Are directions independently enabled? What happens when one product or provider is unavailable? |
| Result presentation | Does “sent”, “delivered”, “accepted” or “paid” identify its evidence and meaning? |
| Accounting handoff | Can an import fail and recover without repeating network delivery? |
| Evidence access | Can eligible users retrieve the source, rendering, history and support reference after a change? |
| Operations | Can support identify the missing owner/evidence without asking the customer to resend first? |

## Consultation output and readiness checks

For each selected product, record the scenario, current behaviour, observed gap, owner and evidence link. Prioritise blocked business outcomes over a feature-count score. Do not mark a capability implemented because it appears in a PRD.

Demonstrate UKR-03 with isolated synthetic clients; UKR-04 with one direction unavailable; UKR-08 with supported and unsupported response processes; and UKR-09 with a delivered document whose local import fails. UKR-06 remains an evidence gate until country scope and profile are qualified. Capture gaps as proposed changes for the owning PRD, with acceptance checks linked to these IDs.
