---
atomic_guid: "6326dbc4-444b-4c04-88f4-27e94d0327cb"
title: "Restart System via `shutdown` - FreeBSD/macOS/Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "6326dbc4-444b-4c04-88f4-27e94d0327cb"
  - "Restart System via `shutdown` - FreeBSD/macOS/Linux"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test restarts a FreeBSD/macOS/Linux system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529: System Shutdown/Reboot]]

## Input Arguments

### timeout

- description: Time to restart (can be minutes or specific time)
- type: string
- default: now

## Executor

- elevation_required: True
- name: sh

### Command

```bash
shutdown -r #{timeout}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
