---
sigma_id: "19951c21-229d-4ccb-8774-b993c3ff3c5c"
title: "Okta API Token Created"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_api_token_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_api_token_created.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "19951c21-229d-4ccb-8774-b993c3ff3c5c"
  - "Okta API Token Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta API Token Created

Detects when a API token is created

## Metadata

- Rule ID: 19951c21-229d-4ccb-8774-b993c3ff3c5c
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_api_token_created.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype: system.api_token.create
condition: selection
```

## False Positives

- Legitimate creation of an API token by authorized users

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_api_token_created.yml)
