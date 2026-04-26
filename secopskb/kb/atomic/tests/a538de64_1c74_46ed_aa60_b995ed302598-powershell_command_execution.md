---
atomic_guid: "a538de64-1c74-46ed-aa60-b995ed302598"
title: "PowerShell Command Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "a538de64-1c74-46ed-aa60-b995ed302598"
  - "PowerShell Command Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Command Execution

Use of obfuscated PowerShell to execute an arbitrary command; outputs "Hello, from PowerShell!". Example is from the 2021 Threat Detection Report by Red Canary.

## Metadata

- Atomic GUID: a538de64-1c74-46ed-aa60-b995ed302598
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Input Arguments

### obfuscated_code

- description: Defaults to: Invoke-Expression with a "Write-Host" line.
- type: string
- default: JgAgACgAZwBjAG0AIAAoACcAaQBlAHsAMAB9ACcAIAAtAGYAIAAnAHgAJwApACkAIAAoACIAVwByACIAKwAiAGkAdAAiACsAIgBlAC0ASAAiACsAIgBvAHMAdAAgACcASAAiACsAIgBlAGwAIgArACIAbABvACwAIABmAHIAIgArACIAbwBtACAAUAAiACsAIgBvAHcAIgArACIAZQByAFMAIgArACIAaAAiACsAIgBlAGwAbAAhACcAIgApAA==

## Executor

- name: command_prompt

### Command

```commandprompt
powershell.exe -e  #{obfuscated_code}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
