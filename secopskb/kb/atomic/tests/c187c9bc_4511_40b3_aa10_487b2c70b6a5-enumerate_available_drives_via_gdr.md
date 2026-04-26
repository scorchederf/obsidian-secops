---
atomic_guid: "c187c9bc-4511-40b3-aa10-487b2c70b6a5"
title: "Enumerate Available Drives via gdr"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "c187c9bc-4511-40b3-aa10-487b2c70b6a5"
  - "Enumerate Available Drives via gdr"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Available Drives via gdr

This test simulates an attacker attempting to list the available drives on the system to gather data about file storage locations.

## Metadata

- Atomic GUID: c187c9bc-4511-40b3-aa10-487b2c70b6a5
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
powershell.exe -c "gdr -PSProvider 'FileSystem'"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
