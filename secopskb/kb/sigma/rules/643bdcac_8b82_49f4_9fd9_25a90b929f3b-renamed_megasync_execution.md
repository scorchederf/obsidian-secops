---
sigma_id: "643bdcac-8b82-49f4-9fd9-25a90b929f3b"
title: "Renamed MegaSync Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_megasync.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_megasync.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "643bdcac-8b82-49f4-9fd9-25a90b929f3b"
  - "Renamed MegaSync Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Renamed MegaSync Execution

Detects the execution of a renamed MegaSync.exe as seen used by ransomware families like Nefilim, Sodinokibi, Pysa, and Conti.

## Metadata

- Rule ID: 643bdcac-8b82-49f4-9fd9-25a90b929f3b
- Status: test
- Level: high
- Author: Sittikorn S
- Date: 2021-06-22
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_megasync.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  OriginalFileName: megasync.exe
filter:
  Image|endswith: \megasync.exe
condition: selection and not filter
```

## False Positives

- Software that illegally integrates MegaSync in a renamed form
- Administrators that have renamed MegaSync

## References

- https://redcanary.com/blog/rclone-mega-extortion/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_megasync.yml)
