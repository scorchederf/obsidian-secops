---
sigma_id: "11b52f18-aaec-4d60-9143-5dd8cc4706b9"
title: "Invoke-Obfuscation RUNDLL LAUNCHER - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_rundll_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_rundll_services.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "11b52f18-aaec-4d60-9143-5dd8cc4706b9"
  - "Invoke-Obfuscation RUNDLL LAUNCHER - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation RUNDLL LAUNCHER - System

Detects Obfuscated Powershell via RUNDLL LAUNCHER

## Metadata

- Rule ID: 11b52f18-aaec-4d60-9143-5dd8cc4706b9
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-18
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_rundll_services.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains|all:
  - rundll32.exe
  - shell32.dll
  - shellexec_rundll
  - powershell
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_rundll_services.yml)
