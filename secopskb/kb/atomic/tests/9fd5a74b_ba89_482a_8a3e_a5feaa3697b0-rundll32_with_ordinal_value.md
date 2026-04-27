---
atomic_guid: "9fd5a74b-ba89-482a-8a3e-a5feaa3697b0"
title: "Rundll32 with Ordinal Value"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "9fd5a74b-ba89-482a-8a3e-a5feaa3697b0"
  - "Rundll32 with Ordinal Value"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Rundll32 with Ordinal Value

Rundll32.exe loading dll using ordinal value #2 to DLLRegisterServer. 
Upon successful execution, Calc.exe will spawn.

## Metadata

- Atomic GUID: 9fd5a74b-ba89-482a-8a3e-a5feaa3697b0
- Technique: T1218.011: Signed Binary Proxy Execution: Rundll32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.011/T1218.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Input Arguments

### input_file

- description: DLL File
- type: string
- default: PathToAtomicsFolder\T1218.010\bin\AllTheThingsx64.dll

### input_url

- description: Url to download the DLL
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/bin/AllTheThingsx64.dll

## Dependencies

DLL file must exist on disk at specified location

### Prerequisite Check

```powershell
if (Test-Path "#{input_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "#{input_url}" -OutFile "#{input_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
rundll32.exe "#{input_file}",#2
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
