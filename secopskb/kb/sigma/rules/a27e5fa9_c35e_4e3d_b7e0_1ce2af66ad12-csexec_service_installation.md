---
sigma_id: "a27e5fa9-c35e-4e3d-b7e0-1ce2af66ad12"
title: "CSExec Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_csexecsvc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_csexecsvc.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "a27e5fa9-c35e-4e3d-b7e0-1ce2af66ad12"
  - "CSExec Service Installation"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CSExec Service Installation

Detects CSExec service installation and execution events

## Metadata

- Rule ID: a27e5fa9-c35e-4e3d-b7e0-1ce2af66ad12
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-07
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_csexecsvc.yml

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
- ServiceName: csexecsvc
- ImagePath|endswith: \csexecsvc.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/malcomvetter/CSExec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_csexecsvc.yml)
