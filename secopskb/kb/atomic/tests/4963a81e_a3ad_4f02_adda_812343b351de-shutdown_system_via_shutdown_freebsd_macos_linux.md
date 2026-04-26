---
atomic_guid: "4963a81e-a3ad-4f02-adda-812343b351de"
title: "Shutdown System via `shutdown` - FreeBSD/macOS/Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "4963a81e-a3ad-4f02-adda-812343b351de"
  - "Shutdown System via `shutdown` - FreeBSD/macOS/Linux"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shutdown System via `shutdown` - FreeBSD/macOS/Linux

This test shuts down a FreeBSD/macOS/Linux system using a halt.

## Metadata

- Atomic GUID: 4963a81e-a3ad-4f02-adda-812343b351de
- Technique: T1529: System Shutdown/Reboot
- Platforms: linux, macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Input Arguments

### timeout

- description: Time to shutdown (can be minutes or specific time)
- type: string
- default: now

## Executor

- elevation_required: True
- name: sh

### Command

```sh
shutdown -h #{timeout}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
