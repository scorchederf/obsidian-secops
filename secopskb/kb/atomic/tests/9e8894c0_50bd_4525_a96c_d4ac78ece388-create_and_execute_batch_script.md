---
atomic_guid: "9e8894c0-50bd-4525-a96c-d4ac78ece388"
title: "Create and Execute Batch Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.003"
attack_technique_name: "Command and Scripting Interpreter: Windows Command Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "9e8894c0-50bd-4525-a96c-d4ac78ece388"
  - "Create and Execute Batch Script"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create and Execute Batch Script

Creates and executes a simple batch script. Upon execution, CMD will briefly launch to run the batch script then close again.

## Metadata

- Atomic GUID: 9e8894c0-50bd-4525-a96c-d4ac78ece388
- Technique: T1059.003: Command and Scripting Interpreter: Windows Command Shell
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059.003/T1059.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Input Arguments

### command_to_execute

- description: Command to execute within script.
- type: string
- default: dir

### script_path

- description: Script path.
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1059.003_script.bat

## Dependencies

Batch file must exist on disk at specified location (#{script_path})

### Prerequisite Check

```powershell
if (Test-Path "#{script_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item "#{script_path}" -Force | Out-Null
Set-Content -Path "#{script_path}" -Value "#{command_to_execute}"
```

## Executor

- name: powershell

### Command

```powershell
Start-Process "#{script_path}"
```

### Cleanup

```powershell
Remove-Item "#{script_path}" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml)
