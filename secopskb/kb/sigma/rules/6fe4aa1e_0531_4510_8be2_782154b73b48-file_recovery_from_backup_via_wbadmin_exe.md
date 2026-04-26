---
sigma_id: "6fe4aa1e-0531-4510-8be2-782154b73b48"
title: "File Recovery From Backup Via Wbadmin.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6fe4aa1e-0531-4510-8be2-782154b73b48"
  - "File Recovery From Backup Via Wbadmin.EXE"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Recovery From Backup Via Wbadmin.EXE

Detects the recovery of files from backups via "wbadmin.exe".
Attackers can restore sensitive files such as NTDS.DIT or Registry Hives from backups in order to potentially extract credentials.

## Metadata

- Rule ID: 6fe4aa1e-0531-4510-8be2-782154b73b48
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2024-05-10
- Source Path: rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection_img:
- Image|endswith: \wbadmin.exe
- OriginalFileName: WBADMIN.EXE
selection_cli:
  CommandLine|contains|all:
  - ' recovery'
  - recoveryTarget
  - itemtype:File
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-start-recovery
- https://lolbas-project.github.io/lolbas/Binaries/Wbadmin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml)
