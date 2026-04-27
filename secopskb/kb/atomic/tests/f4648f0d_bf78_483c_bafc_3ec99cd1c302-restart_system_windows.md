---
atomic_guid: "f4648f0d-bf78-483c-bafc-3ec99cd1c302"
title: "Restart System - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "f4648f0d-bf78-483c-bafc-3ec99cd1c302"
  - "Restart System - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test restarts a Windows system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529: System Shutdown/Reboot]]

## Input Arguments

### timeout

- description: Timeout period before restart (seconds)
- type: integer
- default: 1

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
shutdown /r /t #{timeout}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
