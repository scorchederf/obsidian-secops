---
sigma_id: "0f63e1ef-1eb9-4226-9d54-8927ca08520a"
title: "Admin User Remote Logon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_admin_rdp_login.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_admin_rdp_login.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "0f63e1ef-1eb9-4226-9d54-8927ca08520a"
  - "Admin User Remote Logon"
attack_technique_ids:
  - "T1078.001"
  - "T1078.002"
  - "T1078.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Admin User Remote Logon

Detect remote login by Administrator user (depending on internal pattern).

## Metadata

- Rule ID: 0f63e1ef-1eb9-4226-9d54-8927ca08520a
- Status: test
- Level: low
- Author: juju4
- Date: 2017-10-29
- Modified: 2022-10-09
- Source Path: rules/windows/builtin/security/account_management/win_security_admin_rdp_login.yml

## Logsource

- definition: Requirements: Identifiable administrators usernames (pattern or special unique character. ex: "Admin-*"), internal policy mandating use only as secondary account
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.001]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 10
  AuthenticationPackageName: Negotiate
  TargetUserName|startswith: Admin
condition: selection
```

## False Positives

- Legitimate administrative activity.

## References

- https://car.mitre.org/wiki/CAR-2016-04-005

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_admin_rdp_login.yml)
