---
atomic_guid: "a574dafe-a903-4cce-9701-14040f4f3532"
title: "HKLM - Persistence using CommandProcessor AutoRun key (With Elevation)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "a574dafe-a903-4cce-9701-14040f4f3532"
  - "HKLM - Persistence using CommandProcessor AutoRun key (With Elevation)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may abuse the CommandProcessor AutoRun registry key to persist. Every time cmd.exe is executed, the command defined in the AutoRun key also gets executed.
[reference](https://devblogs.microsoft.com/oldnewthing/20071121-00/?p=24433)

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]

## Input Arguments

### command

- description: Command to Execute
- type: string
- default: notepad.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path "HKLM:\Software\Microsoft\Command Processor" -Name "AutoRun" -Value "#{command}" -PropertyType "String"
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKLM:\Software\Microsoft\Command Processor" -Name "AutoRun" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
