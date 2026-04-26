---
sigma_id: "14701da0-4b0f-4ee6-9c95-2ffb4e73bb9a"
title: "Okta User Account Locked Out"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_user_account_locked_out.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_user_account_locked_out.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "14701da0-4b0f-4ee6-9c95-2ffb4e73bb9a"
  - "Okta User Account Locked Out"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta User Account Locked Out

Detects when an user account is locked out.

## Metadata

- Rule ID: 14701da0-4b0f-4ee6-9c95-2ffb4e73bb9a
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_user_account_locked_out.yml

## Logsource

- product: okta
- service: okta

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  displaymessage: Max sign in attempts exceeded
condition: selection
```

## False Positives

- Unknown

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_user_account_locked_out.yml)
