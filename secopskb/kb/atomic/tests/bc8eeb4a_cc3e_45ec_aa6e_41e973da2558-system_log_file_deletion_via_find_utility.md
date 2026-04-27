---
atomic_guid: "bc8eeb4a-cc3e-45ec-aa6e-41e973da2558"
title: "System log file deletion via find utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "bc8eeb4a-cc3e-45ec-aa6e-41e973da2558"
  - "System log file deletion via find utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# System log file deletion via find utility

This test finds and deletes the system log files within /var/log/ directory using various executions(rm, shred, unlink)

## Metadata

- Atomic GUID: bc8eeb4a-cc3e-45ec-aa6e-41e973da2558
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Input Arguments

### system_log_name1

- description: name or prefix of system log to delete.
- type: string
- default: system.log

### system_log_name2

- description: name or prefix of system log to delete.
- type: string
- default: system.log.97.gz

### system_log_name3

- description: name or prefix of system log to delete.
- type: string
- default: system.log.98.gz

## Dependencies

target files must exist

### Prerequisite Check

```bash
stat /var/log/#{system_log_name1} /var/log/#{system_log_name2} /var/log/#{system_log_name3}
```

### Get Prerequisite

```bash
touch /var/log/#{system_log_name1} /var/log/#{system_log_name2} /var/log/#{system_log_name3}
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo find /var/log -name '#{system_log_name1}*' -exec rm {} \; #using "rm" execution
sudo find /var/log -name "#{system_log_name2}*" -exec shred -u -z -n 3 {} \; #using "shred" execution
sudo find /var/log -name "#{system_log_name3}*" -exec unlink {} \; #using "unlink" execution
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
