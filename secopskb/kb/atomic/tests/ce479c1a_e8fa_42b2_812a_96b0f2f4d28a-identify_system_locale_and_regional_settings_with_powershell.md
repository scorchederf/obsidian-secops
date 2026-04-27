---
atomic_guid: "ce479c1a-e8fa-42b2-812a-96b0f2f4d28a"
title: "Identify System Locale and Regional Settings with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "ce479c1a-e8fa-42b2-812a-96b0f2f4d28a"
  - "Identify System Locale and Regional Settings with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This action demonstrates how an attacker might gather a system's region and language settings using PowerShell, which could aid in profiling 
the machine's location and user language preferences. The command outputs system locale details to a temporary file for further analysis.

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
powershell.exe -c "Get-Culture | Format-List | Out-File -FilePath %TMP%\a.txt"
```

### Cleanup

```cmd
cmd.exe /c del "%TMP%\a.txt"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
