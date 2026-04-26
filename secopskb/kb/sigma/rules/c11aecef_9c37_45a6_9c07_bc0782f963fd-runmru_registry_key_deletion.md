---
sigma_id: "c11aecef-9c37-45a6-9c07-bc0782f963fd"
title: "RunMRU Registry Key Deletion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_delete_runmru.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_delete_runmru.yml"
build_date: "2026-04-26 14:14:35"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c11aecef-9c37-45a6-9c07-bc0782f963fd"
  - "RunMRU Registry Key Deletion"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RunMRU Registry Key Deletion

Detects deletion of the RunMRU registry key, which stores the history of commands executed via the Run dialog.
In the clickfix techniques, the phishing lures instruct users to open a run dialog through (Win + R) and execute malicious commands.
Adversaries may delete this key to cover their tracks after executing commands.

## Metadata

- Rule ID: c11aecef-9c37-45a6-9c07-bc0782f963fd
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-09-25
- Source Path: rules/windows/process_creation/proc_creation_win_reg_delete_runmru.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_cli:
  CommandLine|contains|all:
  - ' del'
  - \Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.zscaler.com/blogs/security-research/coldriver-updates-arsenal-baitswitch-and-simplefix

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_delete_runmru.yml)
