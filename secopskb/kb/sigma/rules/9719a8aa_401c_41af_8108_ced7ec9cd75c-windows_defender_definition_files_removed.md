---
sigma_id: "9719a8aa-401c-41af-8108-ced7ec9cd75c"
title: "Windows Defender Definition Files Removed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mpcmdrun_remove_windows_defender_definition.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mpcmdrun_remove_windows_defender_definition.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9719a8aa-401c-41af-8108-ced7ec9cd75c"
  - "Windows Defender Definition Files Removed"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Defender Definition Files Removed

Adversaries may disable security tools to avoid possible detection of their tools and activities by removing Windows Defender Definition Files

## Metadata

- Rule ID: 9719a8aa-401c-41af-8108-ced7ec9cd75c
- Status: test
- Level: high
- Author: frack113
- Date: 2021-07-07
- Modified: 2023-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_mpcmdrun_remove_windows_defender_definition.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \MpCmdRun.exe
- OriginalFileName: MpCmdRun.exe
selection_cli:
  CommandLine|contains|all:
  - ' -RemoveDefinitions'
  - ' -All'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mpcmdrun_remove_windows_defender_definition.yml)
