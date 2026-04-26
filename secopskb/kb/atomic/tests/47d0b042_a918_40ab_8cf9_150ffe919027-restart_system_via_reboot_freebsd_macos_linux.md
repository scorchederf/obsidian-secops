---
atomic_guid: "47d0b042-a918-40ab-8cf9-150ffe919027"
title: "Restart System via `reboot` - FreeBSD/macOS/Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "47d0b042-a918-40ab-8cf9-150ffe919027"
  - "Restart System via `reboot` - FreeBSD/macOS/Linux"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Restart System via `reboot` - FreeBSD/macOS/Linux

This test restarts a FreeBSD/macOS/Linux system via `reboot`.

## Metadata

- Atomic GUID: 47d0b042-a918-40ab-8cf9-150ffe919027
- Technique: T1529: System Shutdown/Reboot
- Platforms: linux, macos
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
reboot
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
