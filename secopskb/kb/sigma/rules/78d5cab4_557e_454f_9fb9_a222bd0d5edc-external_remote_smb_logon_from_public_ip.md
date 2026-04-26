---
sigma_id: "78d5cab4-557e-454f-9fb9-a222bd0d5edc"
title: "External Remote SMB Logon from Public IP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_successful_external_remote_smb_login.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_successful_external_remote_smb_login.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "78d5cab4-557e-454f-9fb9-a222bd0d5edc"
  - "External Remote SMB Logon from Public IP"
attack_technique_ids:
  - "T1133"
  - "T1078"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# External Remote SMB Logon from Public IP

Detects successful logon from public IP address via SMB. This can indicate a publicly-exposed SMB port.

## Metadata

- Rule ID: 78d5cab4-557e-454f-9fb9-a222bd0d5edc
- Status: test
- Level: high
- Author: Micah Babinski (@micahbabinski), Zach Mathis (@yamatosecurity)
- Date: 2023-01-19
- Modified: 2024-03-11
- Source Path: rules/windows/builtin/security/account_management/win_security_successful_external_remote_smb_login.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 3
filter_main_local_ranges:
  IpAddress|cidr:
  - ::1/128
  - 10.0.0.0/8
  - 127.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 169.254.0.0/16
  - fc00::/7
  - fe80::/10
filter_main_empty:
  IpAddress: '-'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate or intentional inbound connections from public IP addresses on the SMB port.

## References

- https://www.inversecos.com/2020/04/successful-4624-anonymous-logons-to.html
- https://twitter.com/Purp1eW0lf/status/1616144561965002752

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_successful_external_remote_smb_login.yml)
