---
id: NAV-SEI-001
title: Routing and Transmission
type: navigation
status: discovery
owner: TBD
created: 2026-08-10
updated: 2026-08-10
confluence:
  publish: true
  space_key: DNBU
  parent_page_id: "837588803"
  page_id: "876576916"
  title: Routing and Transmission
  layout: two_left_sidebar
  toc: true
---

# Routing and Transmission

## Purpose

This section groups the Phase 3 capabilities that determine where an invoice is sent, how it is exchanged, and how its commercial lifecycle continues across the public solution and private platforms.

The detailed PRDs remain authoritative. This page is a navigation and scope view, not a replacement requirements document.

## Capability coverage

| Capability from the Phase 3 assessment | Authoritative document | Current treatment |
|---|---|---|
| Send and receive through public or private routes | [Exchange — Interoperability, Routing and Transformation](https://confluence.sage.com/pages/viewpage.action?pageId=866148656) | Covered |
| Private-to-private exchange | [Exchange — Interoperability, Routing and Transformation](https://confluence.sage.com/pages/viewpage.action?pageId=866148656) | Covered; external specifications remain evidence gates |
| Mandatory and optional lifecycle statuses | [Lifecycle — Status, Rejection and Payment Reporting](https://confluence.sage.com/pages/viewpage.action?pageId=866148657) | Covered |
| Rejection and total-payment reporting | [Lifecycle — Status, Rejection and Payment Reporting](https://confluence.sage.com/pages/viewpage.action?pageId=866148657) | Covered; legal deadlines remain confirmation gates where applicable |
| Single and batch processing | [Exchange — Interoperability, Routing and Transformation](https://confluence.sage.com/pages/viewpage.action?pageId=866148656) | Exchange behaviour covered; batch product experience requires scope confirmation |
| Invoice generation, presentation and attachments | Phase 3 roadmap decision | Not assumed in the regulated exchange baseline |

## Detailed documents

- [Exchange — Interoperability, Routing and Transformation](https://confluence.sage.com/pages/viewpage.action?pageId=866148656)
- [Lifecycle — Status, Rejection and Payment Reporting](https://confluence.sage.com/pages/viewpage.action?pageId=866148657)

## Boundary and open decisions

- Routing, transformation, signature or seal, delivery, public-copy submission and status reporting are related but separately auditable actions.
- A route change must apply prospectively and must not rewrite the original route or lifecycle evidence of existing invoices.
- Invoice creation, pretty-PDF presentation and attachment management should become a separate product outcome only if they are accepted into Phase 3 scope.
