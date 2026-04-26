---
atomic_guid: "d0eb3597-a1b3-4d65-b33b-2cda8d397f20"
title: "Suspicious Execution via Windows Command Shell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.003"
attack_technique_name: "Command and Scripting Interpreter: Windows Command Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "d0eb3597-a1b3-4d65-b33b-2cda8d397f20"
  - "Suspicious Execution via Windows Command Shell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Execution via Windows Command Shell

Command line executed via suspicious invocation. Example is from the 2021 Threat Detection Report by Red Canary.

## Metadata

- Atomic GUID: d0eb3597-a1b3-4d65-b33b-2cda8d397f20
- Technique: T1059.003: Command and Scripting Interpreter: Windows Command Shell
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1059.003/T1059.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Input Arguments

### input_message

- description: Message to write to file
- type: string
- default: Hello, from CMD!

### output_file

- description: File to output to
- type: string
- default: hello.txt

## Executor

- name: command_prompt

### Command

```commandprompt
%LOCALAPPDATA:~-3,1%md /c echo #{input_message} > #{output_file} & type #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml)
