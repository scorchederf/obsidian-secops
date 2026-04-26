---
sigma_id: "164eda96-11b2-430b-85ff-6a265c15bf32"
title: "Local Groups Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_group.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "164eda96-11b2-430b-85ff-6a265c15bf32"
  - "Local Groups Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local Groups Reconnaissance Via Wmic.EXE

Detects the execution of "wmic" with the "group" flag.
Adversaries may attempt to find local system groups and permission settings.
The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group.
Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

## Metadata

- Rule ID: 164eda96-11b2-430b-85ff-6a265c15bf32
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-12
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_group.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains: ' group'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.001/T1069.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_group.yml)
