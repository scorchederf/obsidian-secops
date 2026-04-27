---
atomic_guid: "e62f8694-cbc7-468f-862c-b10cd07e1757"
title: "Delete system log files using Applescript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "e62f8694-cbc7-468f-862c-b10cd07e1757"
  - "Delete system log files using Applescript"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete system log files using Applescript

This test deletes the system log file using applescript using osascript via Finder application
Note: The user may be prompted to grant access to the Finder application before the command can be executed successfully as part of TCC(Transparency, Consent, and Control) Framework.
Refer: https://www.rainforestqa.com/blog/macos-tcc-db-deep-dive

## Metadata

- Atomic GUID: e62f8694-cbc7-468f-862c-b10cd07e1757
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
osascript -e 'tell application "Finder" to delete POSIX file "#{system_log_path}"'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
