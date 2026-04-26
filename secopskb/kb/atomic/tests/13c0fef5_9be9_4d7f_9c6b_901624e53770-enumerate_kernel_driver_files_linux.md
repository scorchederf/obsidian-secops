---
atomic_guid: "13c0fef5-9be9-4d7f-9c6b-901624e53770"
title: "Enumerate Kernel Driver Files (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1652"
attack_technique_name: "Device Driver Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "13c0fef5-9be9-4d7f-9c6b-901624e53770"
  - "Enumerate Kernel Driver Files (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Kernel Driver Files (Linux)

Finds and lists all kernel driver files on a Linux system in order to provide a broader view of available drivers, not just loaded ones.

## Metadata

- Atomic GUID: 13c0fef5-9be9-4d7f-9c6b-901624e53770
- Technique: T1652: Device Driver Discovery
- Platforms: linux
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1652/T1652.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1652-device_driver_discovery|T1652]]

## Executor

- elevation_required: False
- name: bash

### Command

```bash
find /lib/modules/$(uname -r)/kernel/drivers -name "*.ko*"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml)
