# Invoice sending

Review sending through three complementary views, following [customer onboarding](../onboarding/README.md). All three are unpublished drafts based on SPEC-SEI-007 and the supplied FR sending guide.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-022](SPEC-SEI-022-invoice-sending-solution-summary.md) | Business outcome, scope, actors, workflow and material decisions. Start here. |
| [Logical Feature Specification — SPEC-SEI-023](SPEC-SEI-023-invoice-sending-logical-feature-specification.md) | Scenarios, OUT activities, rules, failures, recovery and functional acceptance. |
| [Sequence and Reuse Assessment — SPEC-SEI-024](SPEC-SEI-024-invoice-sending-sequence-and-reuse-assessment.md) | FR submission/upload/event/detail sequences, Spain public/private differences and engineering evidence gaps. |

[Local review preview](../../work/invoice-sending-review/index.html) · [FR guide evidence extract](<../../context/FR API/Sending/send-e-invoice-guide-extract.md>).

## Current sources

| Source | Scope |
|---|---|
| [SPEC-SEI-007 Invoice sending solution](../SPEC-SEI-007-invoice-sending-solution.md) | Unchanged combined predecessor. Retains detailed interaction/data inventories, field traceability and original acceptance links. |
| [PRD-SEI-246 Spain invoice preparation and outbound flow](../../prds/PRD-SEI-246-spain-invoice-preparation-and-outbound-flow.md) | Proposed end-to-end business flow. |
| [PRD-SEI-223 Interoperability, routing and transformation](../../prds/PRD-SEI-223-interoperability-routing-transformation.md) | Shared exchange requirements. |
| [PRD-SEI-212 Public platform invoice submission](../../prds/PRD-SEI-212-public-platform-invoice-submission-structured-review.md) | Public submission requirements. |

The folder name uses the business action. It covers the sending journey across public and private routes. Shared diagrams stay in [assets/diagrams](../../assets/diagrams/); terminology and source evidence stay in [context](../../context/).

SPEC-SEI-007 remains unchanged and selected for stable Confluence page `923861395` in [the publication configuration](../../config/confluence.yml). The companions retain existing OUT meanings and add separate engineering gap/check IDs. Their Revision overviews explain the split and open decisions.

This README is local navigation. Publication and companion page handling require separate approval; no second page is created solely to retain the predecessor as a separate Git document.
