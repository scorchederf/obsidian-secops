---
sigma_id: "25b9c01c-350d-4b95-bed1-836d04a4f324"
title: "Moriya Rootkit - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_moriya_rootkit.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_moriya_rootkit.yml"
build_date: "2026-04-26 17:03:20"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Moriya Rootkit - System

Detects the use of Moriya rootkit as described in the securelist's Operation TunnelSnake report

## Metadata

- Rule ID: 25b9c01c-350d-4b95-bed1-836d04a4f324
- Status: test
- Level: critical
- Author: Bhabesh Raj
- Date: 2021-05-06
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_moriya_rootkit.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

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
