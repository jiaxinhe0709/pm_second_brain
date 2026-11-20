---
id: NOTE-SEI-003
title: Receiving questions and decisions
type: note
status: draft
owner: Jiaxin He
created: 2026-11-20
updated: 2026-11-20
related:
  - NOTE-SEI-002
  - SPEC-SEI-008
  - SPEC-SEI-026
  - SPEC-SEI-027
confluence:
  publish: false
  page_id: ""
---

# Receiving questions and decisions

The user supplied these receiving requirements on 20 November 2026: avoid duplicate invoices in the ERP, and keep the original file before conversion. ERP means the customer's business software. We still need to agree the detailed rules and confirm what the software supports. [SPEC027 technical questions](SPEC-SEI-027-invoice-retrieval-sequence-and-reuse-assessment.md#4-open-engineering-decisions) lists the engineering checks still needed.

## Questions and decisions

The entries add detail to [Q14 retrieval](../../work/spain-solution-review-questions.html#q14) and [Q16 original files](../../work/spain-solution-review-questions.html#q16). Those questions keep their IDs and answers.

<!-- receiving-log-table:start -->
| ID and area | Current understanding | Question or decision needed | State | Decision or evidence | Suggested owner and next action | Affected specs or diagrams |
|---|---|---|---|---|---|---|
| <a id="q14-1"></a>Q14.1 — Avoid sending the same invoice to the ERP twice | ERP requirement supplied by the user: the Domain Service must check for duplicates before passing retrieved invoices to the ERP. Keep a record of each arrival and its source. | How do we recognise the same invoice arriving again, including a public copy and a private original? How do we distinguish a correction or changed file? What if two copies arrive together, or delivery to the ERP must be retried? | Open | Requirement and Domain Service responsibility supplied on 20 November. SPEC026 proposes related checks. Exact matching rules, reliable delivery and software support still need confirmation. [R1](#r1) | Receiving, API and ERP teams: agree matching, handling of conflicts and delivery rules. Test that retries do not create duplicate ERP records. | SPEC026 RCV-07/08 and RSD-A05/06; SPEC027 RET-G04/07/09; deduplication/ERP handoff sequence. |
| <a id="q16-1"></a>Q16.1 — Keep the original file before converting it | User requirement: save the exact original before converting it. Link each converted file to its original. Do not replace the original with the converted file. | Who stores the files, who can access them, and how long are they kept? How do we trace each converted file back to its original? Apply this to sending and receiving. What conversion or delivery work must wait if saving the original fails? | Open | SPEC026 and SPEC008 already propose related controls. We still need to confirm working storage, approved retention rules and recovery from backups. [R1](#r1) [R2](#r2) | Records, Receiving, DTS, Sending and Security teams: confirm who saves the original, which rules apply and how files can be recovered. | SPEC026 source capture/conversion; SPEC008; sending preparation; archive-before-transformation sequence. |
<!-- receiving-log-table:end -->

## Related decisions and diagram follow-up

[NOTE-SEI-002 Q20.2](../invoice-sending/NOTE-SEI-002-sending-questions-and-decisions.md#q20-2) records the Sage Active notification and X3 response questions. Confirm whether they apply to receiving, sending or both. In the next diagram revision, show that the original is saved before conversion. Show the duplicate and conflict checks before passing an invoice to the ERP. If a public faithful copy and a private original relate to one invoice, keep both records and their sources.

Use the decision states in [NOTE-SEI-001](../onboarding-and-connectivity/NOTE-SEI-001-onboarding-questions-and-decisions.md#evidence-and-decision-handling). Owners and due dates still need agreement. Recording the requirements does not approve the detailed design or change a document's status. Update this table, then run `python3 tools/render_question_logs.py` to update the HTML.

## Source references

<a id="r1"></a>
**R1 — Current receiving draft:** [SPEC026 customer scenarios](SPEC-SEI-026-invoice-retrieval-logical-feature-specification.md#2-scenarios-and-observable-outcomes) and activities RCV-01, RCV-06/07/08. These describe saving originals, conversion, duplicate checks and passing invoices to the ERP. SPEC027 lists the checks needed to prove the software supports them. A label saying “copy” or “original” does not prove two files represent the same invoice.

<a id="r2"></a>
**R2 — File conversion proposal:** [SPEC008 field-preservation controls](../SPEC-SEI-008-spain-ubl-mapper-migration-to-dts-solution-specification.md#spfe-source-contract-binding), draft. Assess DTS, Sage's Document Transformation Service, first. Check its software version, field mappings, country rules, links between original and converted files, and operating support for the selected Spain use. A proposed design does not prove that this is built and working.
