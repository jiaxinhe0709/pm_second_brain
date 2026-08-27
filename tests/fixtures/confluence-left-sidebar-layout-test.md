---
id: TEST-CONFLUENCE-001
title: TEST — Confluence Change History and Layout
type: publication-test
status: draft
owner: Jiaxinhe He
product: spain-e-invoicing
created: 2026-08-10
updated: 2026-08-26
reviewers: []
related:
  - PRD-SEI-210
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: "880492320"
  title: TEST — Confluence Change History and Layout
  layout: two_left_sidebar
  toc: true
---

# Confluence Change History and Layout Test

> **Test page:** This page validates GitHub Markdown publishing and Confluence layout behaviour. It is not a product requirement or delivery commitment.

## Purpose

Confirm that a managed Markdown document can generate a native Confluence two-column section with a narrow left sidebar, a wide content column and an automatic page-version history.

### Expected sidebar behaviour

The left column should contain only Confluence's native Table of Contents macro. The contents should include heading levels 2 and 3 from this document.

### Expected content behaviour

The right column should contain the source banner, headings, paragraphs, lists and tables from this Markdown file, followed by Confluence's native Change History macro.

## Layout verification

Use this checklist after the page is published:

- The page uses a narrow left column and a wide right column.
- The Table of Contents appears in the left column.
- The **Confluence page history** section appears after this test content.
- The history table displays no more than the configured ten page versions.
- The newest published version includes the source document ID, Git revision and document update date in its version comment.
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

| Date | Page version | Result |
|---|---:|---|
| 2026-08-26 | 1 | Confluence rendered the native history table with Version, Published, Changed By and CURRENT fields. The stored page contains one Change History macro with a ten-version limit and one Table of Contents macro. |

This second publication verifies that the table displays more than one real page version and that the newest version carries the Git-backed publication comment.
