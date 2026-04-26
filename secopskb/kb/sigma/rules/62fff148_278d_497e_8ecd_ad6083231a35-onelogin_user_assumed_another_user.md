---
sigma_id: "62fff148-278d-497e-8ecd-ad6083231a35"
title: "OneLogin User Assumed Another User"
framework: "sigma"
generated: "true"
source_path: "rules/identity/onelogin/onelogin_assumed_another_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/onelogin/onelogin_assumed_another_user.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "onelogin / onelogin.events"
aliases:
  - "62fff148-278d-497e-8ecd-ad6083231a35"
  - "OneLogin User Assumed Another User"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OneLogin User Assumed Another User

Detects when an user assumed another user account.

## Metadata

- Rule ID: 62fff148-278d-497e-8ecd-ad6083231a35
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-10-12
- Modified: 2022-12-25
- Source Path: rules/identity/onelogin/onelogin_assumed_another_user.yml

## Logsource

- product: onelogin
- service: onelogin.events

## Detection

```yaml
selection:
  event_type_id: 3
condition: selection
```

## False Positives

- Unknown

## References

- https://developers.onelogin.com/api-docs/1/events/event-resource

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/onelogin/onelogin_assumed_another_user.yml)
