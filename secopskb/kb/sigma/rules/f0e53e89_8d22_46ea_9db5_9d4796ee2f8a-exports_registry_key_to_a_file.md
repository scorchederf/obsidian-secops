---
sigma_id: "f0e53e89-8d22-46ea-9db5-9d4796ee2f8a"
title: "Exports Registry Key To a File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regedit_export_keys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_export_keys.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "f0e53e89-8d22-46ea-9db5-9d4796ee2f8a"
  - "Exports Registry Key To a File"
attack_technique_ids:
  - "T1012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Exports Registry Key To a File

Detects the export of the target Registry key to a file.

## Metadata

- Rule ID: f0e53e89-8d22-46ea-9db5-9d4796ee2f8a
- Status: test
- Level: low
- Author: Oddvar Moe, Sander Wiebing, oscd.community
- Date: 2020-10-07
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_regedit_export_keys.yml

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
selection_cli:
  CommandLine|contains|windash: ' -E '
filter_1:
  CommandLine|contains:
  - hklm
  - hkey_local_machine
filter_2:
  CommandLine|endswith:
  - \system
  - \sam
  - \security
condition: all of selection_* and not all of filter_*
```

## False Positives

- Legitimate export of keys

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regedit/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_export_keys.yml)
