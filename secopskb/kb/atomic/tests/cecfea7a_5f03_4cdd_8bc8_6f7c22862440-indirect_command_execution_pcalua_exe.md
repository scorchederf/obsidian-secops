---
atomic_guid: "cecfea7a-5f03-4cdd-8bc8-6f7c22862440"
title: "Indirect Command Execution - pcalua.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1202"
attack_technique_name: "Indirect Command Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "cecfea7a-5f03-4cdd-8bc8-6f7c22862440"
  - "Indirect Command Execution - pcalua.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Indirect Command Execution - pcalua.exe

The Program Compatibility Assistant (pcalua.exe) may invoke the execution of programs and commands from a Command-Line Interface.
[Reference](https://twitter.com/KyleHanslovan/status/912659279806640128)
Upon execution, calc.exe should open

## Metadata

- Atomic GUID: cecfea7a-5f03-4cdd-8bc8-6f7c22862440
- Technique: T1202: Indirect Command Execution
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1202/T1202.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Input Arguments

### payload_path

- description: Path to payload
- type: path
- default: C:\Windows\System32\calc.exe

### process

- description: Process to execute
- type: string
- default: calc.exe

## Executor

- name: command_prompt

### Command

```cmd
pcalua.exe -a #{process}
pcalua.exe -a #{payload_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml)
