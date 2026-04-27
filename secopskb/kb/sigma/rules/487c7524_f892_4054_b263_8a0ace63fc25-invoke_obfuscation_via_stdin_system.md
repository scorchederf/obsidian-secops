---
sigma_id: "487c7524-f892-4054-b263-8a0ace63fc25"
title: "Invoke-Obfuscation Via Stdin - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_stdin_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_stdin_services.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "487c7524-f892-4054-b263-8a0ace63fc25"
  - "Invoke-Obfuscation Via Stdin - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Stdin - System

Detects Obfuscated Powershell via Stdin in Scripts

## Metadata

- Rule ID: 487c7524-f892-4054-b263-8a0ace63fc25
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-12
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_stdin_services.yml

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
  - set
  - '&&'
  ImagePath|contains:
  - environment
  - invoke
  - input
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_via_stdin_services.yml)
