---
sigma_id: "f7385ee2-0e0c-11eb-adc1-0242ac120002"
title: "Invoke-Obfuscation CLIP+ Launcher - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_clip_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_clip_services.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "f7385ee2-0e0c-11eb-adc1-0242ac120002"
  - "Invoke-Obfuscation CLIP+ Launcher - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation CLIP+ Launcher - System

Detects Obfuscated use of Clip.exe to execute PowerShell

## Metadata

- Rule ID: f7385ee2-0e0c-11eb-adc1-0242ac120002
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-13
- Modified: 2023-02-20
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_clip_services.yml

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
  - cmd
  - '&&'
  - 'clipboard]::'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_clip_services.yml)
