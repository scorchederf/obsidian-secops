---
atomic_guid: "848e43b3-4c0a-4e4c-b4c9-d1e8cea9651c"
title: "Real-time system log clearance/deletion"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "848e43b3-4c0a-4e4c-b4c9-d1e8cea9651c"
  - "Real-time system log clearance/deletion"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Real-time system log clearance/deletion

This test reads real-time system log file and writes empty string to it, thus clearing the log file without tampering with the logging process

## Metadata

- Atomic GUID: 848e43b3-4c0a-4e4c-b4c9-d1e8cea9651c
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo log -f /var/log/system.log | : > /var/log/system.log
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
