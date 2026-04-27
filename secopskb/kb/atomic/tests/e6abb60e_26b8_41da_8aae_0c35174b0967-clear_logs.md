---
atomic_guid: "e6abb60e-26b8-41da-8aae-0c35174b0967"
title: "Clear Logs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.001"
attack_technique_name: "Indicator Removal on Host: Clear Windows Event Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Upon execution this test will clear Windows Event Logs. Open the System.evtx logs at C:\Windows\System32\winevt\Logs and verify that it is now empty.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]

## Input Arguments

### log_name

- description: Windows Log Name, ex System
- type: string
- default: System

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
wevtutil cl #{log_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.001/T1070.001.yaml)
