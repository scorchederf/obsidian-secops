---
sigma_id: "82880171-b475-4201-b811-e9c826cd5eaa"
title: "Exports Critical Registry Keys To a File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regedit_export_critical_keys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_export_critical_keys.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "82880171-b475-4201-b811-e9c826cd5eaa"
  - "Exports Critical Registry Keys To a File"
attack_technique_ids:
  - "T1012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exports Critical Registry Keys To a File

Detects the export of a crital Registry key to a file.

## Metadata

- Rule ID: 82880171-b475-4201-b811-e9c826cd5eaa
- Status: test
- Level: high
- Author: Oddvar Moe, Sander Wiebing, oscd.community
- Date: 2020-10-12
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_regedit_export_critical_keys.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1012-query_registry|T1012]]

## Detection

```yaml
selection_img:
- Image|endswith: \regedit.exe
- OriginalFileName: REGEDIT.EXE
selection_cli_1:
  CommandLine|contains|windash: ' -E '
selection_cli_2:
  CommandLine|contains:
  - hklm
  - hkey_local_machine
selection_cli_3:
  CommandLine|endswith:
  - \system
  - \sam
  - \security
condition: all of selection_*
```

## False Positives

- Dumping hives for legitimate purpouse i.e. backup or forensic investigation

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regedit/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_export_critical_keys.yml)
