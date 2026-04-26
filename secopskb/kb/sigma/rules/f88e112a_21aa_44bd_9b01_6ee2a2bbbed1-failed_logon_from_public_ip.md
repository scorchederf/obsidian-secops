---
sigma_id: "f88e112a-21aa-44bd-9b01-6ee2a2bbbed1"
title: "Failed Logon From Public IP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_susp_failed_logon_source.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_failed_logon_source.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "f88e112a-21aa-44bd-9b01-6ee2a2bbbed1"
  - "Failed Logon From Public IP"
attack_technique_ids:
  - "T1078"
  - "T1190"
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Failed Logon From Public IP

Detects a failed logon attempt from a public IP. A login from a public IP can indicate a misconfigured firewall or network boundary.

## Metadata

- Rule ID: f88e112a-21aa-44bd-9b01-6ee2a2bbbed1
- Status: test
- Level: medium
- Author: NVISO
- Date: 2020-05-06
- Modified: 2024-03-11
- Source Path: rules/windows/builtin/security/account_management/win_security_susp_failed_logon_source.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  EventID: 4625
filter_main_ip_unknown:
  IpAddress|contains: '-'
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
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate logon attempts over the internet
- IPv4-to-IPv6 mapped IPs

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_failed_logon_source.yml)
