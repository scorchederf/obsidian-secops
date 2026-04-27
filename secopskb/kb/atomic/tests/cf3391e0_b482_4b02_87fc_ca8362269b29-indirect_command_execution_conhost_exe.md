---
atomic_guid: "cf3391e0-b482-4b02-87fc-ca8362269b29"
title: "Indirect Command Execution - conhost.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1202"
attack_technique_name: "Indirect Command Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "cf3391e0-b482-4b02-87fc-ca8362269b29"
  - "Indirect Command Execution - conhost.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

conhost.exe refers to a host process for the console window. It provide an interface between command prompt and Windows explorer.
Executing it through command line can create process ancestry anomalies
[Reference] (http://www.hexacorn.com/blog/2020/05/25/how-to-con-your-host/)

## ATT&CK Mapping

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Input Arguments

### process

- description: Process to execute
- type: string
- default: notepad.exe

## Executor

- name: command_prompt

### Command

```cmd
conhost.exe "#{process}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml)
