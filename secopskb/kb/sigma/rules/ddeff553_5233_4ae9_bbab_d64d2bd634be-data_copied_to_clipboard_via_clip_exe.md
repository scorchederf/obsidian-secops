---
sigma_id: "ddeff553-5233-4ae9-bbab-d64d2bd634be"
title: "Data Copied To Clipboard Via Clip.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_clip_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_clip_execution.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "ddeff553-5233-4ae9-bbab-d64d2bd634be"
  - "Data Copied To Clipboard Via Clip.EXE"
attack_technique_ids:
  - "T1115"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Data Copied To Clipboard Via Clip.EXE

Detects the execution of clip.exe in order to copy data to the clipboard. Adversaries may collect data stored in the clipboard from users copying information within or between applications.

## Metadata

- Rule ID: ddeff553-5233-4ae9-bbab-d64d2bd634be
- Status: test
- Level: low
- Author: frack113
- Date: 2021-07-27
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_clip_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1115-clipboard_data|T1115]]

## Detection

```yaml
selection:
- Image|endswith: \clip.exe
- OriginalFileName: clip.exe
condition: selection
```

## False Positives

- Unknown

## Simulation

### Utilize Clipboard to store or execute commands from

- atomic_guid: 0cd14633-58d4-4422-9ede-daa2c9474ae7
- name: Utilize Clipboard to store or execute commands from
- technique: T1115
- type: atomic-red-team

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/clip
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1115/T1115.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_clip_execution.yml)
