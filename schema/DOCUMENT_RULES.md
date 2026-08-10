# Document Rules

## Source of truth

GitHub is canonical. Confluence pages are published representations.

## Files

- One PRD or feature proposal per Markdown file.
- Use a permanent ID plus a readable slug.
- Never encode status or version in a filename.
- Store supporting assets in `assets/`.

## Lifecycle

`idea → discovery → draft → in-review → approved → implemented → superseded`

## Separate successor versions

Git remains the detailed edit history. When a user explicitly wants an individually
readable version and does not want the existing file changed, create a successor
document instead of editing the predecessor.

- The successor must have a new permanent document ID and readable filename.
- Do not encode `v2`, dates, or lifecycle status in the filename.
- Keep the predecessor file unchanged unless a separate change is explicitly
  approved.
- Create the successor with `status: draft`, `confluence.publish: false`, and an
  empty `confluence.page_id`.
- Keep one stable Confluence page per product topic. A successor does not create a
  new Confluence page merely because it is a separate Git document.
- After explicit publication approval, map the successor to the topic's stable
  Confluence page ID and select it in `config/confluence.yml` under
  `publication.current_sources`.
- The publisher must refuse an older document when another document is selected as
  the current source for that page ID.
- Include the predecessor ID in `related`.
- Put a `Revision overview` near the start of the successor stating what it is based
  on, why it exists, what changed, what did not change, and which decisions remain
  open.
- A successor is not automatically approved, publishable, or a reason to mark its
  predecessor as superseded.

This is a new related Git document, not a duplicate identity: permanent IDs must
never be reused across separate files. Confluence remains a latest-version
publication layer rather than a version archive.

## Required metadata

Managed documents require `id`, `title`, `type`, `status`, `owner`, `created`, and `updated`.

PRDs and feature proposals also require `product`, `reviewers`, `related`, and `confluence`.

## Review and publication

- Review substantive changes in pull requests.
- Publish only merged documents explicitly marked for publication.
- Confluence feedback should result in a GitHub issue or pull request.
- Publication must display the source document ID and Git revision.
- Credentials belong in repository or organisation secrets.
