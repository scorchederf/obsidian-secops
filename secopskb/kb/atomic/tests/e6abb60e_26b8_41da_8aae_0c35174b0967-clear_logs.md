---
atomic_guid: "e6abb60e-26b8-41da-8aae-0c35174b0967"
title: "Clear Logs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.001"
attack_technique_name: "Indicator Removal on Host: Clear Windows Event Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "e6abb60e-26b8-41da-8aae-0c35174b0967"
  - "Clear Logs"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear Logs

Upon execution this test will clear Windows Event Logs. Open the System.evtx logs at C:\Windows\System32\winevt\Logs and verify that it is now empty.

## Metadata

- Atomic GUID: e6abb60e-26b8-41da-8aae-0c35174b0967
- Technique: T1070.001: Indicator Removal on Host: Clear Windows Event Logs
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1070.001/T1070.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Input Arguments

### log_name

- description: Windows Log Name, ex System
- type: string
- default: System

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
wevtutil cl #{log_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml)
