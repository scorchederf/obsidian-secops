---
atomic_guid: "f6ecb109-df24-4303-8d85-1987dbae6160"
title: "Check OS version via \"ver\" command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "f6ecb109-df24-4303-8d85-1987dbae6160"
  - "Check OS version via \"ver\" command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Check OS version via "ver" command

Ver command shows information about os version.

## Metadata

- Atomic GUID: f6ecb109-df24-4303-8d85-1987dbae6160
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: command_prompt

### Command

```commandprompt
ver
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
