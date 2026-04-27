---
atomic_guid: "61303105-ff60-427b-999e-efb90b314e41"
title: "Reboot System via `poweroff` - Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "61303105-ff60-427b-999e-efb90b314e41"
  - "Reboot System via `poweroff` - Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Reboot System via `poweroff` - Linux

This test restarts a Linux system using `poweroff`.

## Metadata

- Atomic GUID: 61303105-ff60-427b-999e-efb90b314e41
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
poweroff --reboot
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
