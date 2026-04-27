---
atomic_guid: "6290f8a8-8ee9-4661-b9cf-390031bf6973"
title: "Truncate system log files via truncate utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "6290f8a8-8ee9-4661-b9cf-390031bf6973"
  - "Truncate system log files via truncate utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test truncates the system log files using the truncate utility with (-s 0) parameter which sets file size to zero, thus emptying the file content

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]

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
sudo truncate -s 0 #{system_log_path} #size parameter shorthand
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
