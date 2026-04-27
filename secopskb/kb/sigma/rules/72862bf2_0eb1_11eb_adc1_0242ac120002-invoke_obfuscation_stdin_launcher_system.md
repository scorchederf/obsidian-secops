---
sigma_id: "72862bf2-0eb1-11eb-adc1-0242ac120002"
title: "Invoke-Obfuscation STDIN+ Launcher - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_stdin_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_stdin_services.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "72862bf2-0eb1-11eb-adc1-0242ac120002"
  - "Invoke-Obfuscation STDIN+ Launcher - System"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Obfuscated use of stdin to execute PowerShell

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_main:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains|all:
  - cmd
  - powershell
  ImagePath|contains:
  - /c
  - /r
selection_other:
- ImagePath|contains: noexit
- ImagePath|contains|all:
  - input
  - $
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_invoke_obfuscation_stdin_services.yml)
