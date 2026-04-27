---
atomic_guid: "c8d40da9-31bd-47da-a497-11ea55d1ef6c"
title: "sysctl to gather macOS hardware info"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "c8d40da9-31bd-47da-a497-11ea55d1ef6c"
  - "sysctl to gather macOS hardware info"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# sysctl to gather macOS hardware info

Gets the macOS hardware information, which can be used to determine whether the target macOS host is running on a physical or virtual machine. sysctl can be used to gather interesting macOS host data, including hardware information, memory size, logical cpu information, etc.

## Metadata

- Atomic GUID: c8d40da9-31bd-47da-a497-11ea55d1ef6c
- Technique: T1082: System Information Discovery
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
sysctl -n hw.model
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
