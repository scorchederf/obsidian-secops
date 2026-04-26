---
atomic_guid: "1620de42-160a-4fe5-bbaf-d3fef0181ce9"
title: "Visual Basic script execution to gather local computer information"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.005"
attack_technique_name: "Command and Scripting Interpreter: Visual Basic"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.005/T1059.005.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "1620de42-160a-4fe5-bbaf-d3fef0181ce9"
  - "Visual Basic script execution to gather local computer information"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Visual Basic script execution to gather local computer information

Visual Basic execution test, execute vbscript via PowerShell.

When successful, system information will be written to $env:TEMP\T1059.005.out.txt.

## Metadata

- Atomic GUID: 1620de42-160a-4fe5-bbaf-d3fef0181ce9
- Technique: T1059.005: Command and Scripting Interpreter: Visual Basic
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059.005/T1059.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Input Arguments

### vbscript

- description: Path to sample script
- type: string
- default: PathToAtomicsFolder\T1059.005\src\sys_info.vbs

## Dependencies

Sample script must exist on disk at specified location (#{vbscript})

### Prerequisite Check

```text
if (Test-Path "#{vbscript}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -ItemType Directory (Split-Path "#{vbscript}") -Force | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.005/src/sys_info.vbs" -OutFile "#{vbscript}"
```

## Executor

- name: powershell

### Command

```powershell
cscript "#{vbscript}" > $env:TEMP\T1059.005.out.txt
```

### Cleanup

```powershell
Remove-Item $env:TEMP\T1059.005.out.txt -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.005/T1059.005.yaml)
