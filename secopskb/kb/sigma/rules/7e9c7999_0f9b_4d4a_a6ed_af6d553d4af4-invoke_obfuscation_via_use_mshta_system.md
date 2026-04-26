---
sigma_id: "7e9c7999-0f9b-4d4a-a6ed-af6d553d4af4"
title: "Invoke-Obfuscation Via Use MSHTA - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_mshta_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_mshta_services.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "7e9c7999-0f9b-4d4a-a6ed-af6d553d4af4"
  - "Invoke-Obfuscation Via Use MSHTA - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use MSHTA - System

Detects Obfuscated Powershell via use MSHTA in Scripts

## Metadata

- Rule ID: 7e9c7999-0f9b-4d4a-a6ed-af6d553d4af4
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-09
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_mshta_services.yml

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
  - mshta
  - vbscript:createobject
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_use_mshta_services.yml)
