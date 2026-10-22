# Customer onboarding

Use this folder to review onboarding through three complementary views. All three specifications remain drafts. Publication of the review set is authorised; implementation readiness remains subject to the recorded gates.

| Read | Main audience | What the reader should understand |
|---|---|---|
| [SEI018 — Solution Summary](SPEC-SEI-018-customer-onboarding-solution-summary.md) | Local Product teams, directors and cross-functional stakeholders | Business outcome, scope, responsibilities and main decisions. Start here for a quick overview. |
| [SEI019 — Logical Feature Specification](SPEC-SEI-019-customer-onboarding-logical-feature-specification.md) | Product teams, business analysts and process reviewers | High-level journeys, actors, decisions, outcomes and safe exceptions. Diagrams explain the flow; acceptance checks support review. |
| [SEI021 — Sequence and Reuse Assessment](SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md) | Architects and engineers | Main engineering view: five sequences, eight scenarios, existing API capabilities, Spain public/private changes, product impact and owned gaps. New API design stays outside scope. |

**Retained supporting reference:** [SEI020](../archive/SPEC-SEI-020-customer-onboarding-api-design-and-reuse-assessment.md) is archived. Its detailed API-A01–16 checks, source conflicts and earlier analysis remain available through SEI021. Permanent IDs and publication settings are preserved. [Preview SEI021](../../work/onboarding-sequence-review/SPEC-SEI-021.html).

In SEI021, start with [product impact](SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md#1-engineering-direction), [public readiness](SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md#22-public-readiness), [private setup](SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md#23-private-setup) or the [API reuse table](SPEC-SEI-021-customer-onboarding-sequence-and-reuse-assessment.md#26-existing-api-and-capability-reuse). Detailed evidence links lead to the retained sources.

## Product requirements and original specification

The existing PRDs remain the product requirements sources. This landing page adds navigation; it does not replace or duplicate them.

| Source | Scope |
|---|---|
| [PRD-SEI-101 Public platform onboarding](../../prds/PRD-SEI-101-public-platform-onboarding.md) | Phase 1 public readiness. |
| [PRD-SEI-104 Accountant and single-client onboarding](../../prds/PRD-SEI-104-accountant-and-single-client-onboarding.md) | Direct and delegated access, client isolation and portfolio work. |
| [PRD-SEI-107 Onboarding failure recovery](../../prds/PRD-SEI-107-public-onboarding-failure-recovery.md) | Correction, safe retry, reconciliation and manual recovery. |
| [PRD-SEI-222 Customer onboarding and migration](../../prds/PRD-SEI-222-customer-onboarding-entry-point-migration.md) | Private setup, authorised route changes and historical continuity. |
| [Original SPEC-SEI-002](../SPEC-SEI-002-onboarding-solution-specification.md) | Unchanged combined specification. Retains detailed technical analysis, field inventories, decision records and original acceptance coverage. |

## Directory and publication boundary

This is the onboarding pilot for a feature-folder structure. Shared diagrams stay in [assets/diagrams](../../assets/diagrams/); shared terminology and source evidence stay in [context](../../context/). Other feature directories are unchanged.

SPEC-SEI-018, SPEC-SEI-019 and SPEC-SEI-021 are the primary review set. Archived SPEC-SEI-020 retains its permanent ID and detailed evidence. Existing ONB and OFR behaviour IDs retain their meanings. The [FR source contracts](<../../context/FR API/Onboarding/>) remain unchanged evidence inputs.

The stable onboarding Confluence page `923861390` selects **SPEC-SEI-018** in [the publication configuration](../../config/confluence.yml). SPEC-SEI-019 and SPEC-SEI-021 are authorised as sibling pages under `837610648`; their returned page IDs must be recorded after creation. SPEC-SEI-002 remains unchanged in Git.

## Confluence presentation

Present three sibling pages under the existing onboarding feature/PRD page (`837610648`). Keep the README as local navigation; do not create another Confluence page merely for the directory.

| Confluence view | Git source | Authorised page handling |
|---|---|---|
| Onboarding Solution Summary | SPEC-SEI-018 | Reuse the existing specification page `923861390`, preserving its URL/history. |
| Onboarding Logical Feature Specification | SPEC-SEI-019 | Create one sibling under the same parent; record its returned page ID. |
| Onboarding API Reuse Assessment | SPEC-SEI-021 | Use the same engineering topic; reconcile any existing sibling before creation. No separate page for archived SPEC020. |

Each view links to the other two. High-level business journeys and process diagrams stay in 019; engineering sequences, reuse and product impact stay in 021. Its detailed assurance and source-analysis links continue to archived 020. No API design is added.

The [local preview](../../work/onboarding-api-review/index.html) shows the review structure. The publication package uses the same three views with source revisions, editable diagrams and native companion links. Live targets were checked on 22 October 2026: page `923861390` exists under the parent; the two companion titles are absent. Sources must complete repository review and merge before the live update. Preserve SPEC-SEI-002 and the parent PRD content. Publication does not change lifecycle status.
