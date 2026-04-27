---
atomic_guid: "b0768a5e-0f32-4e75-ae5b-d036edcf96b6"
title: "Delete system log files using srm utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "b0768a5e-0f32-4e75-ae5b-d036edcf96b6"
  - "Delete system log files using srm utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test securely deletes the system log files individually and recursively using the srm utility.
Install srm using Homebrew with the command: brew install khell/homebrew-srm/srm
Refer: https://github.com/khell/homebrew-srm/issues/1 for installation

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]

## Input Arguments

### system_log_folder

- description: path to log parent folder
- type: string
- default: /var/log/

### system_log_path

- description: path to system.log
- type: string
- default: /var/log/system.log

## Dependencies

target files must exist

### Prerequisite Check

```bash
stat #{system_log_path} #{system_log_folder}
```

### Get Prerequisite

```bash
mkdir -p #{system_log_folder} && touch #{system_log_path} #{system_log_folder}/system.log
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo srm #{system_log_path} #system log file deletion
sudo srm -r #{system_log_folder} #recursive deletion of log files
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
