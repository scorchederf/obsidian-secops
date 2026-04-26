---
sigma_id: "84972c80-251c-4c3a-9079-4f00aad93938"
title: "Sensitive File Recovery From Backup Via Wbadmin.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "84972c80-251c-4c3a-9079-4f00aad93938"
  - "Sensitive File Recovery From Backup Via Wbadmin.EXE"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sensitive File Recovery From Backup Via Wbadmin.EXE

Detects the dump of highly sensitive files such as "NTDS.DIT" and "SECURITY" hive.
Attackers can leverage the "wbadmin" utility in order to dump sensitive files that might contain credential or sensitive information.

## Metadata

- Rule ID: 84972c80-251c-4c3a-9079-4f00aad93938
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2024-05-10
- Source Path: rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \wbadmin.exe
- OriginalFileName: WBADMIN.EXE
selection_backup:
  CommandLine|contains|all:
  - ' recovery'
  - recoveryTarget
  - itemtype:File
  CommandLine|contains:
  - \config\SAM
  - \config\SECURITY
  - \config\SYSTEM
  - \Windows\NTDS\NTDS.dit
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/blob/2cc01b01132b5c304027a658c698ae09dd6a92bf/yml/OSBinaries/Wbadmin.yml
- https://lolbas-project.github.io/lolbas/Binaries/Wbadmin/
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-start-recovery
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-start-backup

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml)
