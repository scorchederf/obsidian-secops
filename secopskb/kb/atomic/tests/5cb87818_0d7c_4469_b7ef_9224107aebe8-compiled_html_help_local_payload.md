---
atomic_guid: "5cb87818-0d7c-4469-b7ef-9224107aebe8"
title: "Compiled HTML Help Local Payload"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.001"
attack_technique_name: "Signed Binary Proxy Execution: Compiled HTML File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "5cb87818-0d7c-4469-b7ef-9224107aebe8"
  - "Compiled HTML Help Local Payload"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Compiled HTML Help Local Payload

Uses hh.exe to execute a local compiled HTML Help payload.
Upon execution calc.exe will open

## Metadata

- Atomic GUID: 5cb87818-0d7c-4469-b7ef-9224107aebe8
- Technique: T1218.001: Signed Binary Proxy Execution: Compiled HTML File
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.001/T1218.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Input Arguments

### local_chm_file

- description: Local .chm payload
- type: path
- default: PathToAtomicsFolder\T1218.001\src\T1218.001.chm

## Dependencies

The payload must exist on disk at specified location (#{local_chm_file})

### Prerequisite Check

```text
if (Test-Path "#{local_chm_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{local_chm_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.001/src/T1218.001.chm" -OutFile "#{local_chm_file}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
hh.exe "#{local_chm_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml)
