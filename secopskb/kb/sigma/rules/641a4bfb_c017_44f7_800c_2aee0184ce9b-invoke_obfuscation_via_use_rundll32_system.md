---
sigma_id: "641a4bfb-c017-44f7-800c-2aee0184ce9b"
title: "Invoke-Obfuscation Via Use Rundll32 - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_rundll32_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_rundll32_services.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "641a4bfb-c017-44f7-800c-2aee0184ce9b"
  - "Invoke-Obfuscation Via Use Rundll32 - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use Rundll32 - System

Detects Obfuscated Powershell via use Rundll32 in Scripts

## Metadata

- Rule ID: 641a4bfb-c017-44f7-800c-2aee0184ce9b
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-09
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_rundll32_services.yml

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
  - '&&'
  - rundll32
  - shell32.dll
  - shellexec_rundll
  ImagePath|contains:
  - value
  - invoke
  - comspec
  - iex
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_rundll32_services.yml)
