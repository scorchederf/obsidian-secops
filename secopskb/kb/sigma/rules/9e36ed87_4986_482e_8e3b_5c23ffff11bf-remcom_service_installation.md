---
sigma_id: "9e36ed87-4986-482e-8e3b-5c23ffff11bf"
title: "RemCom Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_remcom.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_remcom.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "9e36ed87-4986-482e-8e3b-5c23ffff11bf"
  - "RemCom Service Installation"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RemCom Service Installation

Detects RemCom service installation and execution events

## Metadata

- Rule ID: 9e36ed87-4986-482e-8e3b-5c23ffff11bf
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-07
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_remcom.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ServiceName: RemComSvc
- ImagePath|endswith: \RemComSvc.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/kavika13/RemCom/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_remcom.yml)
