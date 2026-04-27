---
atomic_guid: "449aa403-6aba-47ce-8a37-247d21ef0306"
title: "Regsvr32 local COM scriptlet execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.010"
attack_technique_name: "Signed Binary Proxy Execution: Regsvr32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "449aa403-6aba-47ce-8a37-247d21ef0306"
  - "Regsvr32 local COM scriptlet execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regsvr32 local COM scriptlet execution

Regsvr32.exe is a command-line program used to register and unregister OLE controls. Upon execution, calc.exe will be launched.

## Metadata

- Atomic GUID: 449aa403-6aba-47ce-8a37-247d21ef0306
- Technique: T1218.010: Signed Binary Proxy Execution: Regsvr32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.010/T1218.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Input Arguments

### filename

- description: Name of the local file, include path.
- type: path
- default: PathToAtomicsFolder\T1218.010\src\RegSvr32.sct

### regsvr32name

- description: Default name of Regsvr32.exe
- type: string
- default: regsvr32.exe

### regsvr32path

- description: Default location of Regsvr32.exe
- type: path
- default: C:\Windows\system32

## Dependencies

Regsvr32.sct must exist on disk at specified location (#{filename})

### Prerequisite Check

```powershell
if (Test-Path "#{filename}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{filename}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.010/src/RegSvr32.sct" -OutFile "#{filename}"
```

## Executor

- name: command_prompt

### Command

```cmd
#{regsvr32path}\#{regsvr32name} /s /u /i:"#{filename}" scrobj.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml)
