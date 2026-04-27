---
atomic_guid: "810a465f-cd4f-47bc-b43e-d2de3b033ecc"
title: "Delete system log files using OSAScript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "810a465f-cd4f-47bc-b43e-d2de3b033ecc"
  - "Delete system log files using OSAScript"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete system log files using OSAScript

This test deletes the system log file using osascript via "do shell script"(sh/bash by default) which in-turn spawns rm utility, requires admin privileges

## Metadata

- Atomic GUID: 810a465f-cd4f-47bc-b43e-d2de3b033ecc
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Input Arguments

### system_log_path

- description: path to system.log
- type: string
- default: /var/log/system.log

## Dependencies

target files must exist

### Prerequisite Check

```bash
stat #{system_log_path}
```

### Get Prerequisite

```bash
touch #{system_log_path}
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
osascript -e 'do shell script "rm #{system_log_path}" with administrator privileges'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
