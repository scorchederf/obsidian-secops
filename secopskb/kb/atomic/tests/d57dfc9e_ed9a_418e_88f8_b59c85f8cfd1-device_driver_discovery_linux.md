---
atomic_guid: "d57dfc9e-ed9a-418e-88f8-b59c85f8cfd1"
title: "Device Driver Discovery (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1652"
attack_technique_name: "Device Driver Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "d57dfc9e-ed9a-418e-88f8-b59c85f8cfd1"
  - "Device Driver Discovery (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Device Driver Discovery (Linux)

Displays a list of loaded kernel modules on a Linux system, which is used to enumerate drivers.

## Metadata

- Atomic GUID: d57dfc9e-ed9a-418e-88f8-b59c85f8cfd1
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
lsmod
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml)
