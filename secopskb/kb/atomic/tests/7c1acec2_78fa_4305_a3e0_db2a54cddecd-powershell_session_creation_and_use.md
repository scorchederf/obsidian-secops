---
atomic_guid: "7c1acec2-78fa-4305-a3e0-db2a54cddecd"
title: "PowerShell Session Creation and Use"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7c1acec2-78fa-4305-a3e0-db2a54cddecd"
  - "PowerShell Session Creation and Use"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Session Creation and Use

Connect to a remote powershell session and interact with the host.
Upon execution, network test info and 'T1086 PowerShell Session Creation and Use' will be displayed.

## Metadata

- Atomic GUID: 7c1acec2-78fa-4305-a3e0-db2a54cddecd
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Input Arguments

### hostname_to_connect

- description: The host to connect to, by default it will connect to the local machine
- type: string
- default: $env:COMPUTERNAME

## Dependencies

PSRemoting must be enabled

### Prerequisite Check

```untitled
Try {
    New-PSSession -ComputerName #{hostname_to_connect} -ErrorAction Stop | Out-Null
    exit 0
} 
Catch {
    exit 1
}
```

### Get Prerequisite

```untitled
Enable-PSRemoting
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-PSSession -ComputerName #{hostname_to_connect}
Test-Connection $env:COMPUTERNAME
Set-Content -Path $env:TEMP\T1086_PowerShell_Session_Creation_and_Use -Value "T1086 PowerShell Session Creation and Use"
Get-Content -Path $env:TEMP\T1086_PowerShell_Session_Creation_and_Use
Remove-Item -Force $env:TEMP\T1086_PowerShell_Session_Creation_and_Use
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
