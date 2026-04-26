---
atomic_guid: "e129d73b-3e03-4ae9-bf1e-67fc8921e0fd"
title: "Detect Virtualization Environment (FreeBSD)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "e129d73b-3e03-4ae9-bf1e-67fc8921e0fd"
  - "Detect Virtualization Environment (FreeBSD)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Detect Virtualization Environment (FreeBSD)

Detects execution in a virtualized environment.
At boot, dmesg stores a log if a hypervisor is detected.

## Metadata

- Atomic GUID: e129d73b-3e03-4ae9-bf1e-67fc8921e0fd
- Technique: T1497.001: Virtualization/Sandbox Evasion: System Checks
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1497.001/T1497.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
if [ "$(sysctl -n hw.hv_vendor)" != "" ]; then echo "Virtualization Environment detected"; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
