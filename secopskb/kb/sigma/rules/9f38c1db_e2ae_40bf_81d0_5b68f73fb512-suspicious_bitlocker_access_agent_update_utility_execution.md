---
sigma_id: "9f38c1db-e2ae-40bf-81d0-5b68f73fb512"
title: "Suspicious BitLocker Access Agent Update Utility Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_baaupdate_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_baaupdate_susp_child_process.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9f38c1db-e2ae-40bf-81d0-5b68f73fb512"
  - "Suspicious BitLocker Access Agent Update Utility Execution"
attack_technique_ids:
  - "T1218"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious BitLocker Access Agent Update Utility Execution

Detects the execution of the BitLocker Access Agent Update Utility (baaupdate.exe) which is not a common parent process for other processes.
Suspicious child processes spawned by baaupdate.exe could indicate an attempt at lateral movement via BitLocker DCOM & COM Hijacking.

## Metadata

- Rule ID: 9f38c1db-e2ae-40bf-81d0-5b68f73fb512
- Status: experimental
- Level: high
- Author: andrewdanis, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_baaupdate_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
selection:
  ParentImage|endswith: \baaupdate.exe
  Image|endswith:
  - \bitsadmin.exe
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \schtasks.exe
  - \wmic.exe
  - \wscript.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/rtecCyberSec/BitlockMove

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_baaupdate_susp_child_process.yml)
