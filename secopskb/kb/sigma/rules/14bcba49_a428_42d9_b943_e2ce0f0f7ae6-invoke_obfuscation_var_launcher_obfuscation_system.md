---
sigma_id: "14bcba49-a428-42d9-b943-e2ce0f0f7ae6"
title: "Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_var_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_var_services.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "14bcba49-a428-42d9-b943-e2ce0f0f7ae6"
  - "Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation VAR++ LAUNCHER OBFUSCATION - System

Detects Obfuscated Powershell via VAR++ LAUNCHER

## Metadata

- Rule ID: 14bcba49-a428-42d9-b943-e2ce0f0f7ae6
- Status: test
- Level: high
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-13
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_var_services.yml

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
  - '&&set'
  - cmd
  - /c
  - -f
  ImagePath|contains:
  - '{0}'
  - '{1}'
  - '{2}'
  - '{3}'
  - '{4}'
  - '{5}'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_var_services.yml)
