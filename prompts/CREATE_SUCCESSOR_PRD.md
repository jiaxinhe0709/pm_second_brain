# Create a separate PRD version

Use this prompt when you want a new, individually readable PRD without changing the
previous file:

> Create a new version of `[PRD ID]` as a separate file. Keep the previous file
> completely unchanged. Explain what changed in plain language.

The agent will:

1. Find the source PRD and the next available permanent ID.
2. Create a separate successor file using that new ID.
3. Keep the source file untouched.
4. Make the successor an unpublished draft.
5. Link the successor to the source PRD.
6. Add a visible `Revision overview` covering:
   - the previous document;
   - why the new version exists;
   - what changed;
   - what stayed unchanged; and
   - open decisions.
7. Report the old and new filenames and confirm that nothing was published.
8. If publication is later approved, update the existing stable Confluence page
   from the successor; do not create a second Confluence page for the new Git
   version.

You do not need to select a new ID, rename files, use Git, or understand Confluence
settings. If you want particular changes, add them after the two-sentence prompt.

Git keeps the readable predecessor and successor files. Confluence shows only the
latest explicitly selected source on the existing topic page.

Example:

> Create a new version of `PRD-SEI-201` as a separate file. Keep the previous file
> completely unchanged. Expand the business scenarios and failure journeys, and
> explain the differences in plain language.
