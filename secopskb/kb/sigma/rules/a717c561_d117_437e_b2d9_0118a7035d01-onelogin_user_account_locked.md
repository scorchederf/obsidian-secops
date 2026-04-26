---
sigma_id: "a717c561-d117-437e-b2d9-0118a7035d01"
title: "OneLogin User Account Locked"
framework: "sigma"
generated: "true"
source_path: "rules/identity/onelogin/onelogin_user_account_locked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/onelogin/onelogin_user_account_locked.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "onelogin / onelogin.events"
aliases:
  - "a717c561-d117-437e-b2d9-0118a7035d01"
  - "OneLogin User Account Locked"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OneLogin User Account Locked

Detects when an user account is locked or suspended.

## Metadata

- Rule ID: a717c561-d117-437e-b2d9-0118a7035d01
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-10-12
- Modified: 2022-12-25
- Source Path: rules/identity/onelogin/onelogin_user_account_locked.yml

## Logsource

- product: onelogin
- service: onelogin.events

## Detection

```yaml
selection1:
  event_type_id: 532
selection2:
  event_type_id: 553
selection3:
  event_type_id: 551
condition: 1 of selection*
```

## False Positives

- System may lock or suspend user accounts.

## References

- https://developers.onelogin.com/api-docs/1/events/event-resource/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/onelogin/onelogin_user_account_locked.yml)
