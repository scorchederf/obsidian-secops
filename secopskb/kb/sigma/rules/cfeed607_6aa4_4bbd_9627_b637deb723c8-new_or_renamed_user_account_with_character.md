---
sigma_id: "cfeed607-6aa4-4bbd-9627-b637deb723c8"
title: "New or Renamed User Account with '$' Character"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_new_or_renamed_user_account_with_dollar_sign.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_new_or_renamed_user_account_with_dollar_sign.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "cfeed607-6aa4-4bbd-9627-b637deb723c8"
  - "New or Renamed User Account with '$' Character"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New or Renamed User Account with '$' Character

Detects the creation of a user with the "$" character. This can be used by attackers to hide a user or trick detection systems that lack the parsing mechanisms.

## Metadata

- Rule ID: cfeed607-6aa4-4bbd-9627-b637deb723c8
- Status: test
- Level: medium
- Author: Ilyas Ochkov, oscd.community
- Date: 2019-10-25
- Modified: 2024-01-16
- Source Path: rules/windows/builtin/security/win_security_new_or_renamed_user_account_with_dollar_sign.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_create:
  EventID: 4720
  SamAccountName|contains: $
selection_rename:
  EventID: 4781
  NewTargetUserName|contains: $
filter_main_homegroup:
  EventID: 4720
  TargetUserName: HomeGroupUser$
condition: 1 of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1387743867663958021

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_new_or_renamed_user_account_with_dollar_sign.yml)
