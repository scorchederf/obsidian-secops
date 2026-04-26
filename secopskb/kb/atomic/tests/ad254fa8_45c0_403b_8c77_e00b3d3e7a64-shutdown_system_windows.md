---
atomic_guid: "ad254fa8-45c0-403b-8c77-e00b3d3e7a64"
title: "Shutdown System - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "ad254fa8-45c0-403b-8c77-e00b3d3e7a64"
  - "Shutdown System - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shutdown System - Windows

This test shuts down a Windows system.

## Metadata

- Atomic GUID: ad254fa8-45c0-403b-8c77-e00b3d3e7a64
- Technique: T1529: System Shutdown/Reboot
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Input Arguments

### timeout

- description: Timeout period before shutdown (seconds)
- type: integer
- default: 1

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
shutdown /s /t #{timeout}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
