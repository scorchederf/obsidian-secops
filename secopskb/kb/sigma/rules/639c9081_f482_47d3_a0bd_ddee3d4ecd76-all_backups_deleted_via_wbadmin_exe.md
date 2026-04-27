---
sigma_id: "639c9081-f482-47d3-a0bd-ddee3d4ecd76"
title: "All Backups Deleted Via Wbadmin.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wbadmin_delete_all_backups.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wbadmin_delete_all_backups.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "639c9081-f482-47d3-a0bd-ddee3d4ecd76"
  - "All Backups Deleted Via Wbadmin.EXE"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# All Backups Deleted Via Wbadmin.EXE

Detects the deletion of all backups or system state backups via "wbadmin.exe".
This technique is used by numerous ransomware families and actors.
This may only be successful on server platforms that have Windows Backup enabled.

## Metadata

- Rule ID: 639c9081-f482-47d3-a0bd-ddee3d4ecd76
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-13
- Modified: 2024-05-10
- Source Path: rules/windows/process_creation/proc_creation_win_wbadmin_delete_all_backups.yml

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
  - delete
  - backup
  CommandLine|contains: keepVersions:0
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#atomic-test-5---windows---delete-volume-shadow-copies-via-wmi-with-powershell
- https://github.com/albertzsigovits/malware-notes/blob/558898932c1579ff589290092a2c8febefc3a4c9/Ransomware/Lockbit.md
- https://www.sentinelone.com/labs/ranzy-ransomware-better-encryption-among-new-features-of-thunderx-derivative/
- https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/ransomware-report-avaddon-and-new-techniques-emerge-industrial-sector-targeted
- https://www.trendmicro.com/content/dam/trendmicro/global/en/research/24/b/lockbit-attempts-to-stay-afloat-with-a-new-version/technical-appendix-lockbit-ng-dev-analysis.pdf
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-delete-systemstatebackup

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wbadmin_delete_all_backups.yml)
