---
atomic_guid: "65526037-7079-44a9-bda1-2cb624838040"
title: "DLL Side-Loading using the Notepad++ GUP.exe binary"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.001"
attack_technique_name: "Hijack Execution Flow: DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "65526037-7079-44a9-bda1-2cb624838040"
  - "DLL Side-Loading using the Notepad++ GUP.exe binary"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DLL Side-Loading using the Notepad++ GUP.exe binary

GUP is an open source signed binary used by Notepad++ for software updates, and is vulnerable to DLL Side-Loading, thus enabling the libcurl dll to be loaded.
Upon execution, calc.exe will be opened.

## Metadata

- Atomic GUID: 65526037-7079-44a9-bda1-2cb624838040
- Technique: T1574.001: Hijack Execution Flow: DLL
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1574.001/T1574.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Input Arguments

### gup_executable

- description: GUP is an open source signed binary used by Notepad++ for software updates
- type: path
- default: PathToAtomicsFolder\T1574.002\bin\GUP.exe

### process_name

- description: Name of the created process
- type: string
- default: calculator.exe

## Dependencies

Gup.exe binary must exist on disk at specified location (#{gup_executable})

### Prerequisite Check

```text
if (Test-Path "#{gup_executable}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{gup_executable}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/bin/GUP.exe?raw=true" -OutFile "#{gup_executable}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
"#{gup_executable}"
```

### Cleanup

```commandprompt
taskkill /F /IM #{process_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml)
