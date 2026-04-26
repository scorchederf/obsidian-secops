---
atomic_guid: "78f92e14-f1e9-4446-b3e9-f1b921f2459e"
title: "Reboot System via `halt` - Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "78f92e14-f1e9-4446-b3e9-f1b921f2459e"
  - "Reboot System via `halt` - Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Reboot System via `halt` - Linux

This test restarts a Linux system using `halt`.

## Metadata

- Atomic GUID: 78f92e14-f1e9-4446-b3e9-f1b921f2459e
- Technique: T1529: System Shutdown/Reboot
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
halt --reboot
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
