---
sigma_id: "cf1dbc6b-6205-41b4-9b88-a83980d2255b"
title: "Okta API Token Revoked"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_api_token_revoked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_api_token_revoked.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "cf1dbc6b-6205-41b4-9b88-a83980d2255b"
  - "Okta API Token Revoked"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta API Token Revoked

Detects when a API Token is revoked.

## Metadata

- Rule ID: cf1dbc6b-6205-41b4-9b88-a83980d2255b
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_api_token_revoked.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype: system.api_token.revoke
condition: selection
```

## False Positives

- Unknown

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_api_token_revoked.yml)
