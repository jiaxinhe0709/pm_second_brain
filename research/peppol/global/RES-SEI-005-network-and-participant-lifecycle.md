---
id: RES-SEI-005
title: Peppol network and participant lifecycle
type: research
status: draft
owner: TBD
product: multi-country-e-invoicing
created: 2026-10-15
updated: 2026-10-15
related:
  - RES-SEI-003
  - PRD-SEI-231
  - PRD-SEI-233
  - PRD-SEI-242
  - PRD-SEI-243
confluence:
  publish: false
  page_id: ""
---

# Peppol network and participant lifecycle

Customers need reliable registration, invoice exchange and provider change without losing authority or invoice history. [PRD-SEI-233](../../../prds/PRD-SEI-233-peppol-multi-address-and-endpoint-routing.md) owns participant and route requirements. This analysis identifies the evidence and scenario coverage needed to qualify that design for real providers and countries.

## Identity and discovery evidence

Use [RES-SEI-003](../RES-SEI-003-peppol-source-register.md#global-network-sources) for source versions.

| Concept | External finding | Product consequence |
|---|---|---|
| Participant identifier | Scheme and value identify the network participant. Invoice party identifiers do not have a universal one-to-one relationship with the envelope participant. P04, pp. 10–11 | Preserve the association and the rule that established it |
| SML | The Service Metadata Locator identifies where recipient metadata is published. P03 §2 | A directory search is not sufficient dispatch evidence |
| SMP | The Service Metadata Publisher supplies capability and endpoint metadata for the selected document/process. P03 §2 | “Participant found” does not mean every invoice type is supported |
| Endpoint | `ServiceEndpointList` supports one or more endpoints for a process. P03 §4.3 | A raw URL is not a business identity; endpoint choice needs a qualified policy |
| Scheme state | Scheme lists distinguish active, deprecated and removed entries. P05 | Retain the source release and apply changes prospectively |

An invoice `EndpointID`, tax identifier, Sage tenant and AP address answer different questions. Do not collapse them into one customer identifier. A syntactically valid identifier is not proof that a participant exists, that a caller may manage it or that a route is legally eligible.

The public Peppol Directory can omit registered receivers because publication is not complete. **P11, Directory section.** A failed directory search therefore needs authoritative capability lookup before a product claims that the recipient is absent from the network.

## Scenario evidence to obtain

These are proposed qualification scenarios, not replacements for the owning PRD requirements. UK-specific additions reference these IDs in RES-SEI-010.

| ID | Actor and condition | Outcome to demonstrate | Failure or recovery evidence |
|---|---|---|---|
| PG-01 | An authorised business requests its first receiving registration | Correct participant, documents/processes and environment become discoverable; customer sees send and receive readiness separately | Incorrect identity is corrected before publication; uncertain registration is queried before a second creation |
| PG-02 | A customer is already registered with another provider | Existing registration and operator are identified; transfer or association follows the applicable contract | No silent overwrite; conflicting ownership is resolved with evidence |
| PG-03 | A seller sends to a discoverable participant | The selected process/profile and recipient endpoint match; the retained route explains the choice | Missing participant, unsupported process, unavailable metadata and untrusted metadata produce distinct actions |
| PG-04 | Transmission may have occurred but no final result is available | Original message can be reconciled and shown as outcome unknown | No blind resend or alternate endpoint attempt; operator resolves the original exchange first |
| PG-05 | Buyer product receives the document again | The same delivery is recognised while a genuinely different invoice remains distinguishable | Replayed messages do not create duplicate bookkeeping; conflicting content is investigated |
| PG-06 | Customer changes AP or metadata provider | New work uses the qualified destination after an evidenced cutover; earlier work remains traceable | Registration ownership, overlap, rollback and in-flight messages have explicit handling |
| PG-07 | Business withdraws, closes or loses authority | Future affected activity stops at the approved boundary; retained evidence remains accessible to eligible users | Inbound obligations and unfinished exchanges are resolved before deletion or deregistration |

For PG-01/02, obtain provider management contracts rather than inventing a common registration API. SMP's public lookup contract does not define the customer-administration workflow. For PG-06, distinguish a sending-provider connection change from receiving-participant metadata migration; the effects need not be the same.

## Feedback must retain its source meaning

MLS concerns processing/delivery from C3 towards C4; Invoice Response concerns the buyer's processing decision. MLS `AP` confirms delivery towards C4, while Invoice Response `AP` means buyer approval. MLS `AB` reports forwarding without confirmation. Evidence: P09 §§2.1–2.2 and P10 response-code table.

[PRD-SEI-242](../../../prds/PRD-SEI-242-peppol-lifecycle-feedback.md#peppol-signal-vocabulary) owns the full signal vocabulary, exact codes and mapping rules. Link to that statement rather than copying the code list here. Missing feedback needs the selected process's expectation and timer; it cannot automatically mean failure or payment.

## Proposed evidence record

This is information needed for qualification and diagnosis, not a storage schema or API design.

| Evidence group | Record for the selected exchange |
|---|---|
| Business and authority | Represented legal entity, authenticated caller, authority scope, tenant and environment |
| Capability | Participant scheme/value, document type, process, profile/version and direction |
| Discovery | Source operator, retrieval time, signature/trust outcome, relevant validity and selected endpoint |
| Execution | Sending and receiving AP roles, immutable message correlation and exact document reference |
| Observation | Original response, source namespace/version, producer, receipt time and interpreted outcome |
| Recovery | Unresolved question, owner, evidence sought and permitted next action |

## Open provider-contract questions

- Which operations create, inspect, transfer and delete a registration? What proves authority for each?
- How are existing registrations and conflicting claims detected without mutating customer state?
- Which discovery cache, signature and validity rules apply? How are redirects qualified?
- Which IDs survive callback loss, provider change and support escalation?
- What acknowledgement proves the C3-to-C4 handoff for each receiving integration?
- How can operations reconcile an uncertain send when the original provider is unavailable?
- Which retention and export rights survive customer exit?

Proposed owners: network product for registration and migration; AP engineering for exchange contracts; security for trust; operations for reconciliation. Named accountable owners remain to be assigned in RES-SEI-011.
