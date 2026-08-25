---
id: TEST-CONFLUENCE-001
title: TEST — Confluence Left Sidebar and Table of Contents
type: publication-test
status: draft
owner: Jiaxinhe He
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-10
reviewers: []
related:
  - PRD-SEI-210
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: "876576843"
  title: TEST — Markdown Sidebar and Table of Contents
  layout: two_left_sidebar
  toc: true
---

# Confluence Left Sidebar and Table of Contents Test

> **Test page:** This page validates GitHub Markdown publishing and Confluence layout behaviour. It is not a product requirement or delivery commitment.

## Purpose

Confirm that a managed Markdown document can generate a native Confluence two-column section with a narrow left sidebar and a wide content column.

### Expected sidebar behaviour

The left column should contain only Confluence's native Table of Contents macro. The contents should include heading levels 2 and 3 from this document.

### Expected content behaviour

The right column should contain the source banner, native Change History macro, headings, paragraphs, lists and tables from this Markdown file.

## Layout verification

Use this checklist after the page is published:

- The page uses a narrow left column and a wide right column.
- The Table of Contents appears in the left column.
- The Publication history section displays no more than the configured ten page versions.
- Published versions include the source document ID, Git revision and document update date in their version comment.
- Selecting a Table of Contents entry navigates to the corresponding heading.
- Heading level 2 and heading level 3 entries are visible.
- The document remains readable without horizontal clipping.

### Narrow sidebar check

This heading should appear nested beneath **Layout verification** in the Table of Contents.

## Markdown component check

| Component | Expected result |
|---|---|
| Paragraph | Rendered in the wide right column |
| Bulleted list | Preserved as a native Confluence list |
| Table | Preserved as a native Confluence table |
| Heading 2 | Displayed as a top-level TOC entry |
| Heading 3 | Nested beneath its nearest heading 2 |

### Final nested heading

If this entry appears in the left sidebar and links to this section, the heading-depth configuration is working.

## Test outcome

Record the visual result and any required adjustment before applying this layout convention to additional published PRDs.
