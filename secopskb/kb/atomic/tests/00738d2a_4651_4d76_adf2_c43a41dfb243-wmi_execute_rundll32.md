---
atomic_guid: "00738d2a-4651-4d76-adf2-c43a41dfb243"
title: "WMI Execute rundll32"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "00738d2a-4651-4d76-adf2-c43a41dfb243"
  - "WMI Execute rundll32"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses wmic.exe to execute a DLL function using rundll32. Specify a valid value for remote IP using the node parameter.

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Input Arguments

### dll_to_execute

- description: Path to DLL.
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\calc.dll

### function_to_execute

- description: Name of DLL function to call
- type: string
- default: StartW

### node

- description: Ip Address
- type: string
- default: 127.0.0.1

## Dependencies

DLL with function to execute must exist on disk at specified location (#{dll_to_execute})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_to_execute}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/bin/calc.dll?raw=true" -OutFile "#{dll_to_execute}"
```

## Executor

- name: command_prompt

### Command

```cmd
wmic /node:#{node} process call create "rundll32.exe \"#{dll_to_execute}\" #{function_to_execute}"
```

### Cleanup

```cmd
taskkill /f /im calculator.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
