---
atomic_guid: "ca50dd85-81ff-48ca-92e1-61f119cb1dcf"
title: "Delete system journal logs via rm and journalctl utilities"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "ca50dd85-81ff-48ca-92e1-61f119cb1dcf"
  - "Delete system journal logs via rm and journalctl utilities"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete system journal logs via rm and journalctl utilities

The first sub-test deletes the journal files using rm utility in the "/var/log/journal/" directory and the second sub-test clears the journal by modifiying time period of logs that should be retained to zero.

## Metadata

- Atomic GUID: ca50dd85-81ff-48ca-92e1-61f119cb1dcf
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Input Arguments

### journal_folder

- description: path to journal logs
- type: string
- default: /var/log/journal

## Dependencies

target files must exist

### Prerequisite Check

```bash
stat #{journal_folder}
```

### Get Prerequisite

```bash
mkdir -p #{journal_folder} && touch #{journal_folder}/T1070_002.journal
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo rm #{journal_folder}/* #physically deletes the journal files, and not just their content
sudo journalctl --vacuum-time=0 #clears the journal while still keeping the journal files in place
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
