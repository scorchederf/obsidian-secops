---
atomic_guid: "d2a1f4bc-a064-4223-8281-a086dce5423c"
title: "Abuse of Linux Magic System Request Key for Reboot"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "d2a1f4bc-a064-4223-8281-a086dce5423c"
  - "Abuse of Linux Magic System Request Key for Reboot"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Abuse of Linux Magic System Request Key for Reboot

adversaries with root or sufficient privileges to silently manipulate or destabilize a system. By writing to /proc/sysrq-trigger, they can forced to reboot.

## Metadata

- Atomic GUID: d2a1f4bc-a064-4223-8281-a086dce5423c
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
echo "b" > /proc/sysrq-trigger
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
