---
atomic_guid: "08ffca73-9a3d-471a-aeb0-68b4aa3ab37b"
title: "Regsvr32 local DLL execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.010"
attack_technique_name: "Signed Binary Proxy Execution: Regsvr32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "08ffca73-9a3d-471a-aeb0-68b4aa3ab37b"
  - "Regsvr32 local DLL execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regsvr32 local DLL execution

Regsvr32.exe is a command-line program used to register and unregister OLE controls. Upon execution, calc.exe will be launched.

## Metadata

- Atomic GUID: 08ffca73-9a3d-471a-aeb0-68b4aa3ab37b
- Technique: T1218.010: Signed Binary Proxy Execution: Regsvr32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.010/T1218.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Input Arguments

### dll_name

- description: Name of DLL to Execute, DLL Should export DllRegisterServer
- type: path
- default: PathToAtomicsFolder\T1218.010\bin\AllTheThingsx86.dll

### regsvr32name

- description: Default name of Regsvr32.exe
- type: string
- default: regsvr32.exe

### regsvr32path

- description: Default location of Regsvr32.exe
- type: path
- default: C:\Windows\system32

## Dependencies

AllTheThingsx86.dll must exist on disk at specified location (#{dll_name})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{dll_name}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.010/bin/AllTheThingsx86.dll" -OutFile "#{dll_name}"
```

## Executor

- name: command_prompt

### Command

```cmd
IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (C:\Windows\syswow64\regsvr32.exe /s #{dll_name}) ELSE ( #{regsvr32path}\#{regsvr32name} /s #{dll_name} )
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml)
