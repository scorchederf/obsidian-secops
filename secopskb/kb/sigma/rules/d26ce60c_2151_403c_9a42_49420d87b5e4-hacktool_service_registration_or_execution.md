---
sigma_id: "d26ce60c-2151-403c-9a42-49420d87b5e4"
title: "HackTool Service Registration or Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_hacktools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_hacktools.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "d26ce60c-2151-403c-9a42-49420d87b5e4"
  - "HackTool Service Registration or Execution"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool Service Registration or Execution

Detects installation or execution of services

## Metadata

- Rule ID: d26ce60c-2151-403c-9a42-49420d87b5e4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-21
- Modified: 2023-08-07
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_hacktools.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID:
  - 7045
  - 7036
selection_service_name:
  ServiceName|contains:
  - cachedump
  - DumpSvc
  - gsecdump
  - pwdump
  - UACBypassedService
  - WCE SERVICE
  - WCESERVICE
  - winexesvc
selection_service_image:
  ImagePath|contains: bypass
condition: selection_eid and 1 of selection_service_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_hacktools.yml)
