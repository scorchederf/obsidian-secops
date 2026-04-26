---
sigma_id: "b53317a0-8acf-4fd1-8de8-a5401e776b96"
title: "Application Removed Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_uninstall_application.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_uninstall_application.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b53317a0-8acf-4fd1-8de8-a5401e776b96"
  - "Application Removed Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Application Removed Via Wmic.EXE

Detects the removal or uninstallation of an application via "Wmic.EXE".

## Metadata

- Rule ID: b53317a0-8acf-4fd1-8de8-a5401e776b96
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-28
- Modified: 2024-07-02
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_uninstall_application.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \WMIC.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains|all:
  - call
  - uninstall
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1047/T1047.md#atomic-test-10---application-uninstall-using-wmic

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_uninstall_application.yml)
