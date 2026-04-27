---
atomic_guid: "7b1cee42-320f-4890-b056-d65c8b884ba5"
title: "Reboot System via `halt` - FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "7b1cee42-320f-4890-b056-d65c8b884ba5"
  - "Reboot System via `halt` - FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Reboot System via `halt` - FreeBSD

This test restarts a FreeBSD system using `halt`.

## Metadata

- Atomic GUID: 7b1cee42-320f-4890-b056-d65c8b884ba5
- Technique: T1529: System Shutdown/Reboot
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
halt -r
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
