---
sigma_id: "f7375e28-5c14-432f-b8d1-1db26c832df3"
title: "Potential Arbitrary DLL Load Using Winword"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_winword_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_winword_dll_load.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f7375e28-5c14-432f-b8d1-1db26c832df3"
  - "Potential Arbitrary DLL Load Using Winword"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Arbitrary DLL Load Using Winword

Detects potential DLL sideloading using the Microsoft Office winword process via the '/l' flag.

## Metadata

- Rule ID: f7375e28-5c14-432f-b8d1-1db26c832df3
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2020-10-09
- Modified: 2023-03-29
- Source Path: rules/windows/process_creation/proc_creation_win_office_winword_dll_load.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img:
- Image|endswith: \WINWORD.exe
- OriginalFileName: WinWord.exe
selection_dll:
  CommandLine|contains|all:
  - '/l '
  - .dll
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/D4Vinci/One-Lin3r/blob/9fdfa5f0b9c698dfbd4cdfe7d2473192777ae1c6/one_lin3r/core/liners/windows/cmd/dll_loader_word.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_winword_dll_load.yml)
