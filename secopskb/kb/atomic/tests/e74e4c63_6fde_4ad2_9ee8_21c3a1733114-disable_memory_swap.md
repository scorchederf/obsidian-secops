---
atomic_guid: "e74e4c63-6fde-4ad2-9ee8-21c3a1733114"
title: "Disable Memory Swap"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "e74e4c63-6fde-4ad2-9ee8-21c3a1733114"
  - "Disable Memory Swap"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Memory Swap

disable swapping of device paging that impaire the compromised host to swap data if the RAM is full. Awfulshred wiper used this technique as an additional 
payload to the compromised host and to make sure that there will be no recoverable data due to swap feature of FreeBSD/linux.

## Metadata

- Atomic GUID: e74e4c63-6fde-4ad2-9ee8-21c3a1733114
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
swapon -a 
sleep 2
swapoff -a
sync
```

### Cleanup

```bash
swapon -a
sleep 2
sync
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
