---
sigma_id: "6cc2b61b-d97e-42ef-a9dd-8aa8dc951657"
title: "Okta Unauthorized Access to App"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_unauthorized_access_to_app.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_unauthorized_access_to_app.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "6cc2b61b-d97e-42ef-a9dd-8aa8dc951657"
  - "Okta Unauthorized Access to App"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Unauthorized Access to App

Detects when unauthorized access to app occurs.

## Metadata

- Rule ID: 6cc2b61b-d97e-42ef-a9dd-8aa8dc951657
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_unauthorized_access_to_app.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  displaymessage: User attempted unauthorized access to app
condition: selection
```

## False Positives

- User might of believe that they had access.

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_unauthorized_access_to_app.yml)
