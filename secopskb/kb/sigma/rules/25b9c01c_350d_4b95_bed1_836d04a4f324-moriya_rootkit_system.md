---
sigma_id: "25b9c01c-350d-4b95-bed1-836d04a4f324"
title: "Moriya Rootkit - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_moriya_rootkit.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_moriya_rootkit.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "critical"
logsource: "windows / system"
aliases:
  - "25b9c01c-350d-4b95-bed1-836d04a4f324"
  - "Moriya Rootkit - System"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of Moriya rootkit as described in the securelist's Operation TunnelSnake report

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ServiceName: ZzNetSvc
condition: selection
```

## False Positives

- Unknown

## References

- https://securelist.com/operation-tunnelsnake-and-moriya-rootkit/101831

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_moriya_rootkit.yml)
