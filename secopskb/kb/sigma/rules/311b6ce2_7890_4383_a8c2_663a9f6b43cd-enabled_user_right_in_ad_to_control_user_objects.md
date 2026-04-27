---
sigma_id: "311b6ce2-7890-4383-a8c2-663a9f6b43cd"
title: "Enabled User Right in AD to Control User Objects"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_alert_active_directory_user_control.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_active_directory_user_control.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "311b6ce2-7890-4383-a8c2-663a9f6b43cd"
  - "Enabled User Right in AD to Control User Objects"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enabled User Right in AD to Control User Objects

Detects scenario where if a user is assigned the SeEnableDelegationPrivilege right in Active Directory it would allow control of other AD user objects.

## Metadata

- Rule ID: 311b6ce2-7890-4383-a8c2-663a9f6b43cd
- Status: test
- Level: high
- Author: @neu5ron
- Date: 2017-07-30
- Modified: 2021-12-02
- Source Path: rules/windows/builtin/security/win_security_alert_active_directory_user_control.yml

## Logsource

- definition: Requirements: Audit Policy : Policy Change > Audit Authorization Policy Change, Group Policy : Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Policy Change\Audit Authorization Policy Change
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection_base:
  EventID: 4704
selection_keywords:
  PrivilegeList|contains: SeEnableDelegationPrivilege
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://blog.harmj0y.net/activedirectory/the-most-dangerous-user-right-you-probably-have-never-heard-of/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_active_directory_user_control.yml)
