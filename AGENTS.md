# Agent Instructions

Read `schema/DOCUMENT_RULES.md` before creating or changing managed documents.

- GitHub content is canonical; Confluence is a generated publishing layer.
- Keep one PRD or feature proposal per Markdown file.
- Preserve permanent document IDs.
- Check for an existing document before creating another.
- Update links when moving or renaming files.
- Never add secrets, tokens, customer personal data, or confidential raw exports.
- Do not publish to Confluence or change document status without explicit user approval.

## Separate-version requests

When a user asks for a new version, a separate version, or says not to overwrite a
managed document:

- Leave the source file completely unchanged.
- Create a successor document with the next available permanent ID and a readable
  filename; do not add `v2`, a date, or a lifecycle status to the filename.
- Start the successor as `status: draft` with `confluence.publish: false` and no
  Confluence page ID. Never reuse the predecessor's Confluence page ID.
- Add the predecessor ID to `related` and add a plain-language `Revision overview`
  near the top covering the predecessor, reason, changes, unchanged areas, and open
  decisions.
- Do not mark the predecessor as superseded or otherwise edit it unless the user
  separately approves that change.
- In the handoff, name both files and explicitly confirm whether the source changed
  and whether the successor is eligible for publication.

The user does not need to choose an ID or understand Git. The instruction "Create
a new version and keep the previous file unchanged" is sufficient.
