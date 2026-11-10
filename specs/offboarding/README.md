# Customer offboarding

Review offboarding through three complementary views. All three are unpublished drafts. The analysis distinguishes platform switching from ending access or services, including Sage access to SPFE. SPEC-SEI-032 owns OFF-S01–10, partial/full scope, business closure and incident entry. The summary diagram provides the reading route; analysis coverage does not enable a switch or prove an external deregistration operation.

| Read | Purpose |
|---|---|
| [Solution Summary — SPEC-SEI-031](SPEC-SEI-031-customer-offboarding-solution-summary.md) | Business outcomes, platform responsibilities, proposed support periods and decisions. Start here. |
| [Logical Feature Specification — SPEC-SEI-032](SPEC-SEI-032-customer-offboarding-logical-feature-specification.md) | OFF activities, scenarios, cutoff rules, historical work, export, recovery and acceptance. |
| [Sequence and Reuse Assessment — SPEC-SEI-033](SPEC-SEI-033-customer-offboarding-sequence-and-reuse-assessment.md) | Existing disconnection evidence, shared capability reuse, provider differences and engineering gates. |

[Local review preview](../../work/offboarding-review/index.html).

The shared [settings overview lives in SPEC037](../onboarding-and-connectivity/SPEC-SEI-037-customer-onboarding-and-connectivity-solution-summary.md#e-invoicing-settings-overview). [SPEC038](../onboarding-and-connectivity/SPEC-SEI-038-customer-onboarding-and-connectivity-logical-feature-specification.md#switch-platform-one-customer-journey) owns the complete customer switch journey. This set supplies exit checks within that request, or a standalone disconnect; it does not own another settings or switch journey.

The combined predecessor is retained in [the archive](../archive/README.md). Its
linked detail remains part of this review set; its lifecycle and publication
settings are unchanged.

## Sources and publication

[SPEC-SEI-003](../archive/SPEC-SEI-003-offboarding-solution-specification.md) remains unchanged. Its OFF activity, invariant, requirement, interaction, data and acceptance IDs retain their meanings. [PRD-SEI-243](../../prds/PRD-SEI-243-customer-offboarding-and-provider-exit.md) remains the product source. New support periods and commercial choices are proposals for the PRD owner, not approved policy.

SPEC-SEI-003 remains the selected Git source for stable Confluence page `923861391` in [config/confluence.yml](../../config/confluence.yml). These drafts have no Confluence page IDs. This README adds local navigation. Publication requires explicit approval.

Shared diagrams stay in [assets/diagrams](../../assets/diagrams/). The [glossary](../../context/GLO-SEI-001-e-invoicing-terminology.md) defines shared terms. The [Spain evidence guide](../../context/RES-SEI-002-spain-public-platform-technical-evidence.md) supplies the original public-platform baseline; its earlier public-only review deferred offboarding. This set is a separate analysis and does not change that phase boundary.
