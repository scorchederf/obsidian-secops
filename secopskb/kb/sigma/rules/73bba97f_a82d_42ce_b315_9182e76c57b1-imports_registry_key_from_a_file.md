---
sigma_id: "73bba97f-a82d-42ce-b315-9182e76c57b1"
title: "Imports Registry Key From a File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "73bba97f-a82d-42ce-b315-9182e76c57b1"
  - "Imports Registry Key From a File"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Imports Registry Key From a File

Detects the import of the specified file to the registry with regedit.exe.

## Metadata

- Rule ID: 73bba97f-a82d-42ce-b315-9182e76c57b1
- Status: test
- Level: medium
- Author: Oddvar Moe, Sander Wiebing, oscd.community
- Date: 2020-10-07
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_img:
- Image|endswith: \regedit.exe
- OriginalFileName: REGEDIT.EXE
selection_cli:
  CommandLine|contains:
  - ' /i '
  - ' /s '
  - .reg
filter_1:
  CommandLine|contains|windash:
  - ' -e '
  - ' -a '
  - ' -c '
filter_2:
  CommandLine|re: :[^ \\]
condition: all of selection_* and not all of filter_*
```

## False Positives

- Legitimate import of keys
- Evernote

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regedit/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_import_keys.yml)
