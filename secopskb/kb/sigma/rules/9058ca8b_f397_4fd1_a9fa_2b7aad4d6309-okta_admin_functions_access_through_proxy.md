---
sigma_id: "9058ca8b-f397-4fd1-a9fa-2b7aad4d6309"
title: "Okta Admin Functions Access Through Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_admin_activity_from_proxy_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_admin_activity_from_proxy_query.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "9058ca8b-f397-4fd1-a9fa-2b7aad4d6309"
  - "Okta Admin Functions Access Through Proxy"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Admin Functions Access Through Proxy

Detects access to Okta admin functions through proxy.

## Metadata

- Rule ID: 9058ca8b-f397-4fd1-a9fa-2b7aad4d6309
- Status: test
- Level: medium
- Author: Muhammad Faisal @faisalusuf
- Date: 2023-10-25
- Source Path: rules/identity/okta/okta_admin_activity_from_proxy_query.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  debugContext.debugData.requestUri|contains: admin
  securityContext.isProxy: 'true'
condition: selection
```

## False Positives

- False positives are expected if administrators access these function through proxy legitimatly. Apply additional filters if necessary

## References

- https://www.beyondtrust.com/blog/entry/okta-support-unit-breach
- https://dataconomy.com/2023/10/23/okta-data-breach/
- https://blog.cloudflare.com/how-cloudflare-mitigated-yet-another-okta-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_admin_activity_from_proxy_query.yml)
