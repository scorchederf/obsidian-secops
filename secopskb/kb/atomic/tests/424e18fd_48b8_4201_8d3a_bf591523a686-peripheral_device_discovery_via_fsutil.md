---
atomic_guid: "424e18fd-48b8-4201-8d3a-bf591523a686"
title: "Peripheral Device Discovery via fsutil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1120"
attack_technique_name: "Peripheral Device Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "424e18fd-48b8-4201-8d3a-bf591523a686"
  - "Peripheral Device Discovery via fsutil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Peripheral Device Discovery via fsutil

Performs pheripheral device discovery utilizing fsutil to list all drives.

## Metadata

- Atomic GUID: 424e18fd-48b8-4201-8d3a-bf591523a686
- Technique: T1120: Peripheral Device Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1120/T1120.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1120-peripheral_device_discovery|T1120]]

## Executor

- name: command_prompt

### Command

```cmd
fsutil fsinfo drives
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml)
