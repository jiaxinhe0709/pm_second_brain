# Provider API artefacts

This folder is reserved for provider-supplied machine-readable specifications and supporting technical assets.

Before adding an artefact, confirm that Sage is permitted to retain it and add a neighbouring manifest containing:

```yaml
provider: ""
artifact: ""
source_url: ""
retrieved: 2026-07-27
version: ""
environment: ""
access: public
storage_permission: confirmed
contains_secrets: false
contains_customer_data: false
used_by: []
```

Permitted examples include OpenAPI specifications, JSON schemas, WSDL/XSD files, Postman collections, and provider-supplied diagrams.

Never add credentials, tokens, passwords, certificates, customer data, confidential raw exports, or an unauthorised mirror of a documentation website.

