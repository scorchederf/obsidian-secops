---
atomic_guid: "86f0e4d5-3ca7-45fb-829d-4eda32b232bb"
title: "Delete system log files using shred utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "86f0e4d5-3ca7-45fb-829d-4eda32b232bb"
  - "Delete system log files using shred utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete system log files using shred utility

This test overwrites the contents of the log file with zero bytes(-z) using three passes(-n 3) of data, and then delete the file(-u) securely

## Metadata

- Atomic GUID: 86f0e4d5-3ca7-45fb-829d-4eda32b232bb
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
sudo shred -u -z -n 3 #{system_log_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
