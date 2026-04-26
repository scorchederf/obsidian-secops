---
atomic_guid: "0208ea60-98f1-4e8c-8052-930dce8f742c"
title: "Overwrite macOS system log via echo utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "0208ea60-98f1-4e8c-8052-930dce8f742c"
  - "Overwrite macOS system log via echo utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Overwrite macOS system log via echo utility

This test overwrites the contents of system log file with an empty string using echo utility

## Metadata

- Atomic GUID: 0208ea60-98f1-4e8c-8052-930dce8f742c
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Input Arguments

### system_log_path

- description: path to system.log
- type: string
- default: /var/log/system.log

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo echo '' > #{system_log_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
