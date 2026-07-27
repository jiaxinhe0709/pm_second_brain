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

## Required metadata

Managed documents require `id`, `title`, `type`, `status`, `owner`, `created`, and `updated`.

PRDs and feature proposals also require `product`, `reviewers`, `related`, and `confluence`.

## Review and publication

- Review substantive changes in pull requests.
- Publish only merged documents explicitly marked for publication.
- Confluence feedback should result in a GitHub issue or pull request.
- Publication must display the source document ID and Git revision.
- Credentials belong in repository or organisation secrets.

