---
sigma_id: "06125661-3814-4e03-bfa2-1e4411c60ac3"
title: "Backup Files Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_backup_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_backup_file.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "06125661-3814-4e03-bfa2-1e4411c60ac3"
  - "Backup Files Deleted"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Backup Files Deleted

Detects deletion of files with extensions often used for backup files. Adversaries may delete or remove built-in operating system data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.

## Metadata

- Rule ID: 06125661-3814-4e03-bfa2-1e4411c60ac3
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-02
- Modified: 2023-02-15
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_backup_file.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \wt.exe
  - \rundll32.exe
  - \regsvr32.exe
  TargetFilename|endswith:
  - .VHD
  - .bac
  - .bak
  - .wbcat
  - .bkf
  - .set
  - .win
  - .dsk
condition: selection
```

## False Positives

- Legitimate usage

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#atomic-test-6---windows---delete-backup-files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_backup_file.yml)
