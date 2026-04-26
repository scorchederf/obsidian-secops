---
atomic_guid: "369878c6-fb04-48d6-8fc2-da9d97b3e054"
title: "Delete log files via cat utility by appending /dev/null or /dev/zero (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "369878c6-fb04-48d6-8fc2-da9d97b3e054"
  - "Delete log files via cat utility by appending /dev/null or /dev/zero (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete log files via cat utility by appending /dev/null or /dev/zero (freebsd)

The first sub-test truncates the log file to zero bytes via /dev/null and the second sub-test fills the log file with null bytes(zeroes) via /dev/zero, using cat utility

## Metadata

- Atomic GUID: 369878c6-fb04-48d6-8fc2-da9d97b3e054
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
cat /dev/null > /var/log/messages #truncating the file to zero bytes
cat /dev/zero > /var/log/messages #log file filled with null bytes(zeros)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
