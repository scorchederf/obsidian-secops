---
sigma_id: "b6c718dd-8f53-4b9f-98d8-93fdca966969"
title: "New Okta User Created"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_user_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_user_created.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "informational"
logsource: "okta / okta"
aliases:
  - "b6c718dd-8f53-4b9f-98d8-93fdca966969"
  - "New Okta User Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Okta User Created

Detects new user account creation

## Metadata

- Rule ID: b6c718dd-8f53-4b9f-98d8-93fdca966969
- Status: test
- Level: informational
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-10-25
- Source Path: rules/identity/okta/okta_user_created.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype: user.lifecycle.create
condition: selection
```

## False Positives

- Legitimate and authorized user creation

## References

- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_user_created.yml)
