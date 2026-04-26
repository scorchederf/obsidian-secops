---
atomic_guid: "5a282e50-86ff-438d-8cef-8ae01c9e62e1"
title: "Reboot System via `poweroff` - FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "5a282e50-86ff-438d-8cef-8ae01c9e62e1"
  - "Reboot System via `poweroff` - FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Reboot System via `poweroff` - FreeBSD

This test restarts a FreeBSD system using `poweroff`.

## Metadata

- Atomic GUID: 5a282e50-86ff-438d-8cef-8ae01c9e62e1
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

```sh
poweroff -r 3
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
