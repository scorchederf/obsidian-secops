---
atomic_guid: "c23bdb88-928d-493e-b46d-df2906a50941"
title: "Delete log files via cat utility by appending /dev/null or /dev/zero"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "c23bdb88-928d-493e-b46d-df2906a50941"
  - "Delete log files via cat utility by appending /dev/null or /dev/zero"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete log files via cat utility by appending /dev/null or /dev/zero

The first sub-test truncates the log file to zero bytes via /dev/null and the second sub-test fills the log file with null bytes(zeroes) via /dev/zero, using cat utility

## Metadata

- Atomic GUID: c23bdb88-928d-493e-b46d-df2906a50941
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

- description: path of system log to delete.
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
sudo cat /dev/null > #{system_log_path} #truncating the file to zero bytes
sudo dd if=/dev/zero bs=1000 count=5 of=#{system_log_path} #log file filled with null bytes(zeros)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
