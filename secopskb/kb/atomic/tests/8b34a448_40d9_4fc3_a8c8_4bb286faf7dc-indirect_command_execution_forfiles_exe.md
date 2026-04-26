---
atomic_guid: "8b34a448-40d9-4fc3-a8c8-4bb286faf7dc"
title: "Indirect Command Execution - forfiles.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1202"
attack_technique_name: "Indirect Command Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "8b34a448-40d9-4fc3-a8c8-4bb286faf7dc"
  - "Indirect Command Execution - forfiles.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Indirect Command Execution - forfiles.exe

forfiles.exe may invoke the execution of programs and commands from a Command-Line Interface.
[Reference](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Forfiles.yml)
"This is basically saying for each occurrence of notepad.exe in c:\windows\system32 run calc.exe"
Upon execution calc.exe will be opened.

## Metadata

- Atomic GUID: 8b34a448-40d9-4fc3-a8c8-4bb286faf7dc
- Technique: T1202: Indirect Command Execution
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1202/T1202.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Input Arguments

### process

- description: Process to execute
- type: string
- default: calc.exe

## Executor

- name: command_prompt

### Command

```commandprompt
forfiles /p c:\windows\system32 /m notepad.exe /c #{process}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml)
