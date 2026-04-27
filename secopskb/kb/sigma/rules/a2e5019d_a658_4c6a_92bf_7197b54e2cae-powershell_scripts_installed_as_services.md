---
sigma_id: "a2e5019d-a658-4c6a-92bf-7197b54e2cae"
title: "PowerShell Scripts Installed as Services"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_powershell_script_installed_as_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_powershell_script_installed_as_service.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "a2e5019d-a658-4c6a-92bf-7197b54e2cae"
  - "PowerShell Scripts Installed as Services"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Scripts Installed as Services

Detects powershell script installed as a Service

## Metadata

- Rule ID: a2e5019d-a658-4c6a-92bf-7197b54e2cae
- Status: test
- Level: high
- Author: oscd.community, Natalia Shornikova
- Date: 2020-10-06
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_powershell_script_installed_as_service.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains:
  - powershell
  - pwsh
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_powershell_script_installed_as_service.yml)
