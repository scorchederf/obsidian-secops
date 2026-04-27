---
sigma_id: "c4ff1eac-84ad-44dd-a6fb-d56a92fc43a9"
title: "ProcessHacker Privilege Elevation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_pua_proceshacker.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_pua_proceshacker.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "c4ff1eac-84ad-44dd-a6fb-d56a92fc43a9"
  - "ProcessHacker Privilege Elevation"
attack_technique_ids:
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a ProcessHacker tool that elevated privileges to a very high level

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ServiceName|startswith: ProcessHacker
  AccountName: LocalSystem
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/1kwpeter/status/1397816101455765504

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_pua_proceshacker.yml)
