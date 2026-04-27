---
atomic_guid: "73a90cd2-48a2-4ac5-8594-2af35fa909fa"
title: "Shutdown System via `poweroff` - FreeBSD/Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "73a90cd2-48a2-4ac5-8594-2af35fa909fa"
  - "Shutdown System via `poweroff` - FreeBSD/Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Shutdown System via `poweroff` - FreeBSD/Linux

This test shuts down a FreeBSD/Linux system using `poweroff`.

## Metadata

- Atomic GUID: 73a90cd2-48a2-4ac5-8594-2af35fa909fa
- Technique: T1529: System Shutdown/Reboot
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
poweroff
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
