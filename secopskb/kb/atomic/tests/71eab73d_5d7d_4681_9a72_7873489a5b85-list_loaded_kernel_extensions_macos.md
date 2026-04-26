---
atomic_guid: "71eab73d-5d7d-4681-9a72-7873489a5b85"
title: "List loaded kernel extensions (macOS)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1652"
attack_technique_name: "Device Driver Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "71eab73d-5d7d-4681-9a72-7873489a5b85"
  - "List loaded kernel extensions (macOS)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List loaded kernel extensions (macOS)

Displays a list of loaded kernel extensions (kexts) on a macOS system.

## Metadata

- Atomic GUID: 71eab73d-5d7d-4681-9a72-7873489a5b85
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
kextstat
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1652/T1652.yaml)
