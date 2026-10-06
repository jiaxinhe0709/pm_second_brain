# Agent Instructions

Read `schema/DOCUMENT_RULES.md` before creating or changing managed documents.

- GitHub content is canonical; Confluence is a generated publishing layer.
- Keep one PRD or feature proposal per Markdown file.
- Preserve permanent document IDs.
- Check for an existing document before creating another.
- Update links when moving or renaming files.
- Never add secrets, tokens, customer personal data, or confidential raw exports.
- Do not publish to Confluence or change document status without explicit user approval.

## Solution spec language and reuse

- Write specs for engineering and stakeholders who use English as a second
  language. Use plain language, explain necessary technical terms, and preserve
  precise behaviour, technical IDs, controls and open decisions.
- For each Spain spec, explicitly identify intended Spain use, reusable design
  patterns, shared capabilities needing country rules or adapters, Spain-specific
  behaviour, and unknown implementation coverage.
- Distinguish reuse of an existing implementation from reuse of a proposed design
  pattern. Record the source capability, local changes, gaps, owner and evidence
  needed before activation; a reuse candidate is not proof of production readiness.
- Assess existing DTS as the preferred transformation reuse candidate where
  relevant. Qualify its actual build, contracts, mappings, rule packs and operations
  for the selected Spain scope.
- Keep country rules separate from shared behaviour. Spain identity, routing,
  public-copy and reporting rules must not become defaults for another country.
  Include acceptance coverage for country-rule isolation and reuse qualification.

## Shared specification terminology

- Use [the e-invoicing glossary](context/GLO-SEI-001-e-invoicing-terminology.md)
  when creating or reviewing e-invoicing specs. Keep local definitions aligned.
- Qualify represented-party identity, authenticated-caller identity and outcome
  meanings. Preserve exact contract fields, state values and source codes.
- Add or clarify shared terms in the glossary when a spec introduces a new meaning.

## Context and chat lifecycle

- Treat each chat as one primary outcome. Continue in the same chat while refining
  that outcome or its directly related files.
- A change of deliverable, country, or lifecycle phase (for example research to
  mockup, mockup to PRD, or PRD to publication) is a natural boundary for a fresh
  chat.
- At such a boundary, finish the current safe work, then recommend a fresh chat and
  provide a concise handoff containing: objective, canonical files, agreed
  decisions, completed work, open questions, and a ready-to-paste next prompt.
- If the objective is unchanged but the chat has become long, recommend `/compact`
  once at a natural pause. Do not repeatedly interrupt the work with context advice.
- Use `/side` for a quick explanatory question when available. Use a fresh chat for
  maximum context savings; use `/fork` only when inherited conversation history is
  materially useful.
- Prefer current repository files and Git state over raw chat history. Read only the
  files needed for the task; do not reload every related PRD by default.
- Keep handoffs under 300 words and omit command history, failed attempts,
  superseded ideas, and routine verification output.
- Do not create permanent handoff files unless the user asks. Never refuse to
  continue solely because a chat is long.

## Separate-version requests

When a user asks for a new version, a separate version, or says not to overwrite a
managed document:

- Leave the source file completely unchanged.
- Create a successor document with the next available permanent ID and a readable
  filename; do not add `v2`, a date, or a lifecycle status to the filename.
- Start the successor as `status: draft` with `confluence.publish: false` and no
  Confluence page ID.
- Keep one stable Confluence page per product topic. After explicit publication
  approval, the successor may become the selected source for the predecessor's
  stable page ID; update `config/confluence.yml` at the same time.
- Never create a second Confluence page solely because Git contains a separately
  readable successor version.
- Add the predecessor ID to `related` and add a plain-language `Revision overview`
  near the top covering the predecessor, reason, changes, unchanged areas, and open
  decisions.
- Do not mark the predecessor as superseded or otherwise edit it unless the user
  separately approves that change.
- In the handoff, name both files, confirm whether the source changed, and identify
  which Git document is the current source for the stable Confluence page.

The user does not need to choose an ID or understand Git. The instruction "Create
a new version and keep the previous file unchanged" is sufficient.
