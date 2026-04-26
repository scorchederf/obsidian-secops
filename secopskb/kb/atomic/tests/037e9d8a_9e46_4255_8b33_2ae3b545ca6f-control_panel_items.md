---
atomic_guid: "037e9d8a-9e46-4255-8b33-2ae3b545ca6f"
title: "Control Panel Items"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.002"
attack_technique_name: "Signed Binary Proxy Execution: Control Panel"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.002/T1218.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "037e9d8a-9e46-4255-8b33-2ae3b545ca6f"
  - "Control Panel Items"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Control Panel Items

This test simulates an adversary leveraging control.exe
Upon execution calc.exe will be launched

## Metadata

- Atomic GUID: 037e9d8a-9e46-4255-8b33-2ae3b545ca6f
- Technique: T1218.002: Signed Binary Proxy Execution: Control Panel
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.002/T1218.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.002]]

## Input Arguments

### cpl_file_path

- description: path to cpl file
- type: path
- default: PathToAtomicsFolder\T1218.002\bin\calc.cpl

## Dependencies

Cpl file must exist on disk at specified location (#{cpl_file_path})

### Prerequisite Check

```text
if (Test-Path "#{cpl_file_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{cpl_file_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.002/bin/calc.cpl" -OutFile "#{cpl_file_path}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
control.exe "#{cpl_file_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.002/T1218.002.yaml)
