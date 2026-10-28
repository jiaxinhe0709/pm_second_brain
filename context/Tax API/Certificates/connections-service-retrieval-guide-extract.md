# Connections Service credential retrieval — reviewed extract

Source: [2.1. Connection Service - Retrieve Credentials](https://confluence.sage.com/pages/viewpage.action?pageId=484738408), page 484738408, version 14; read 27 October 2026. Storage-body SHA-256: `def3a392e8ce6bc41bb10595405a074e12e3f950f43515601081dfa61edbe202`. This extract omits credential values, tokens, source identifiers and raw exports.

## Documented contract and scope

The page describes **ITSA Service retrieving HMRC access tokens**, following a Sage product request. It restricts this endpoint to **trusted services**.

**Request method: `GET`.** URL: `https://api.network.sage.com/datasets/{dataset_id}/connections/{connection_id}/credentials`. The page lists `traceparent`, `tracestate`, `Authorization` and `Accept` headers. It gives HTTP status `200` for success.

The response example includes `data.type`, `data.id`, `data.attributes.providerId`, `label`, `credentials` and audit metadata. Under `credentials` it includes `credentialType`, `authenticatedAt`, `expiresBy` and `credentialObject.accessToken` / `credentialObject.expiresBy`. The page discusses access-token expiry and Redis TTL; these are not validated certificate expiry.

## Reuse limits

This is an existing internal retrieval contract candidate. It does not establish:

- an AEAT certificate response or Spain B2B permission;
- a product-facing, non-secret credential list or readiness lookup;
- certificate validation, action suitability or authority to act;
- permission for an ERP to retrieve certificate/password material.

Tax/Connections and Security must confirm caller permissions, AEAT credential shape and a safe reference/readiness contract before B2B reuse. Do not add this secret-bearing endpoint to the ERP onboarding flow. Provider discovery and certificate provisioning are documented separately in the [AEAT upload extract](aeat-certificate-upload-guide-extract.md).
