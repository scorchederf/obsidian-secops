---
atomic_guid: "20aba24b-e61f-4b26-b4ce-4784f763ca20"
title: "System Time Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1124"
attack_technique_name: "System Time Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "20aba24b-e61f-4b26-b4ce-4784f763ca20"
  - "System Time Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Time Discovery

Identify the system time. Upon execution, the local computer system time and timezone will be displayed.

## Metadata

- Atomic GUID: 20aba24b-e61f-4b26-b4ce-4784f763ca20
- Technique: T1124: System Time Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1124/T1124.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1124-system_time_discovery|T1124]]

## Input Arguments

### computer_name

- description: computer name to query
- type: string
- default: localhost

## Executor

- name: command_prompt

### Command

```cmd
net time \\#{computer_name}
w32tm /tz
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1124/T1124.yaml)
