---
atomic_guid: "c63bbe52-6f17-4832-b221-f07ba8b1736f"
title: "Find Kernel Extensions (macOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1652"
attack_technique_name: "Device Driver Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "c63bbe52-6f17-4832-b221-f07ba8b1736f"
  - "Find Kernel Extensions (macOS)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Find Kernel Extensions (macOS)

Searches for kernel extension (kext) files on a macOS system.

## Metadata

- Atomic GUID: c63bbe52-6f17-4832-b221-f07ba8b1736f
- Technique: T1652: Device Driver Discovery
- Platforms: macos
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
kextfind
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml)
