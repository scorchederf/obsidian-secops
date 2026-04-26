---
sigma_id: "4bb79b62-ef12-4861-981d-2aab43fab642"
title: "TacticalRMM Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_tacticalrmm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_tacticalrmm.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "4bb79b62-ef12-4861-981d-2aab43fab642"
  - "TacticalRMM Service Installation"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# TacticalRMM Service Installation

Detects a TacticalRMM service installation. Tactical RMM is a remote monitoring & management tool.

## Metadata

- Rule ID: 4bb79b62-ef12-4861-981d-2aab43fab642
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-28
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_tacticalrmm.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection_root:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ImagePath|contains: tacticalrmm.exe
- ServiceName|contains: TacticalRMM Agent Service
condition: all of selection_*
```

## False Positives

- Legitimate use of the tool

## References

- https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_tacticalrmm.yml)
