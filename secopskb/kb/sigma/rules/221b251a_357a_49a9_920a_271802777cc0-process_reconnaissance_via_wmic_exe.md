---
sigma_id: "221b251a-357a-49a9-920a-271802777cc0"
title: "Process Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_process.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "221b251a-357a-49a9-920a-271802777cc0"
  - "Process Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Reconnaissance Via Wmic.EXE

Detects the execution of "wmic" with the "process" flag, which adversary might use to list processes running on the compromised host or list installed software hotfixes and patches.

## Metadata

- Rule ID: 221b251a-357a-49a9-920a-271802777cc0
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-01
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_process.yml

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
  CommandLine|contains: process
filter_main_creation:
  CommandLine|contains|all:
  - call
  - create
condition: all of selection* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1047/T1047.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wmic

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_process.yml)
