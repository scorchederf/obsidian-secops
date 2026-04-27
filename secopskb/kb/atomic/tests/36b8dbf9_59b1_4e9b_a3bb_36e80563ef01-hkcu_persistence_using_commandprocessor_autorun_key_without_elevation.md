---
atomic_guid: "36b8dbf9-59b1-4e9b-a3bb-36e80563ef01"
title: "HKCU - Persistence using CommandProcessor AutoRun key (Without Elevation)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "36b8dbf9-59b1-4e9b-a3bb-36e80563ef01"
  - "HKCU - Persistence using CommandProcessor AutoRun key (Without Elevation)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HKCU - Persistence using CommandProcessor AutoRun key (Without Elevation)

An adversary may abuse the CommandProcessor AutoRun registry key to persist. Every time cmd.exe is executed, the command defined in the AutoRun key also gets executed.
[reference](https://devblogs.microsoft.com/oldnewthing/20071121-00/?p=24433)

## Metadata

- Atomic GUID: 36b8dbf9-59b1-4e9b-a3bb-36e80563ef01
- Technique: T1546: Event Triggered Execution
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1546/T1546.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Input Arguments

### command

- description: Command to Execute
- type: string
- default: notepad.exe

## Executor

- name: powershell

### Command

```powershell
$path = "HKCU:\Software\Microsoft\Command Processor"
if (!(Test-Path -path $path)){
  New-Item -ItemType Key -Path $path
}
New-ItemProperty -Path $path -Name "AutoRun" -Value "#{command}" -PropertyType "String"
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Command Processor" -Name "AutoRun" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
