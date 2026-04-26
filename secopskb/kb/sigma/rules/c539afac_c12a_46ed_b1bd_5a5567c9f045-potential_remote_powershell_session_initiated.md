---
sigma_id: "c539afac-c12a-46ed-b1bd-5a5567c9f045"
title: "Potential Remote PowerShell Session Initiated"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_remote_powershell_session.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_remote_powershell_session.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "c539afac-c12a-46ed-b1bd-5a5567c9f045"
  - "Potential Remote PowerShell Session Initiated"
attack_technique_ids:
  - "T1059.001"
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Remote PowerShell Session Initiated

Detects a process that initiated a network connection over ports 5985 or 5986 from a non-network service account.
This could potentially indicates a remote PowerShell connection.

## Metadata

- Rule ID: c539afac-c12a-46ed-b1bd-5a5567c9f045
- Status: test
- Level: high
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-09-12
- Modified: 2024-02-02
- Source Path: rules/windows/network_connection/net_connection_win_susp_remote_powershell_session.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection:
  DestinationPort:
  - 5985
  - 5986
  Initiated: 'true'
  SourceIsIpv6: 'false'
filter_main_service_users:
- User|contains:
  - NETWORK SERVICE
  - NETZWERKDIENST
  - SERVICIO DE RED
  - SERVIZIO DI RETE
- User|contains|all:
  - SERVICE R
  - SEAU
filter_main_localhost:
  SourceIp:
  - ::1
  - 127.0.0.1
  DestinationIp:
  - ::1
  - 127.0.0.1
filter_optional_avast:
  Image:
  - C:\Program Files\Avast Software\Avast\AvastSvc.exe
  - C:\Program Files (x86)\Avast Software\Avast\AvastSvc.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate usage of remote PowerShell, e.g. remote administration and monitoring.
- Network Service user name of a not-covered localization

## References

- https://threathunterplaybook.com/hunts/windows/190511-RemotePwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_remote_powershell_session.yml)
