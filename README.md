# PM Second Brain

Git is the system of record for product documents. Confluence is the publishing and discovery layer.

## Working model

1. Create or update one Markdown file per PRD or feature proposal.
2. Open a pull request early and review substantive changes in GitHub.
3. Merge approved documents to `main`.
4. Publish eligible documents to Confluence after merge.

## Repository map

- `prds/` — one file per product requirements document
- `feature-proposals/` — one file per feature proposal
- `decisions/` — durable product and architecture decisions
- `research/` — customer and market evidence
- `context/` — personas, metrics, principles, glossary, and product context
- `inbox/` — ideas and feedback awaiting triage
- `assets/` — diagrams, screenshots, and attachments
- `templates/` — document starters
- `prompts/` — reusable PM assistant workflows
- `config/` — products, document types, and non-secret publishing configuration
- `schema/` — document rules and metadata schema
- `tools/` — validation and publishing utilities

## Document identity

Use a stable ID and readable filename:

```text
PRD-BILL-001-e-invoice-pipeline.md
FP-BILL-001-validation-rules.md
ADR-001-retry-policy.md
```

Do not put versions or statuses in filenames. Git records detailed versions; front matter records lifecycle status.

If an individually readable version is needed, ask for a separate successor PRD.
The existing file stays unchanged, while the successor receives a new permanent ID,
links back to its predecessor, and starts as an unpublished draft. A non-technical
contributor can use the copy-ready instructions in
`prompts/CREATE_SUCCESSOR_PRD.md`.

## Confluence

Only documents with `confluence.publish: true` are eligible for publication. Git
may contain multiple readable successor documents, while Confluence keeps one
stable page per topic and displays the latest selected source. The selected source
for each stable page is recorded under `publication.current_sources` in
`config/confluence.yml`. Keep credentials in GitHub Actions secrets, never in this
repository.

Generated pages include Confluence's native Change History macro when
`publication.change_history.enabled` is true. The configured `limit` controls how
many Confluence page versions are displayed. The macro appears after the managed
document's content, and live updates add a version comment containing the managed
document ID, Git revision and document update date.

The native macro records publication history; it does not replace a PRD's curated
Markdown `Revision history` or `Change log`, which remains the canonical explanation
of material product and requirement changes.
