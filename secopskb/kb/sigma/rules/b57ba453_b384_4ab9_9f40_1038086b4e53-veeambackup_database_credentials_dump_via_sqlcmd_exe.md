---
sigma_id: "b57ba453-b384-4ab9-9f40-1038086b4e53"
title: "VeeamBackup Database Credentials Dump Via Sqlcmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_dump.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b57ba453-b384-4ab9-9f40-1038086b4e53"
  - "VeeamBackup Database Credentials Dump Via Sqlcmd.EXE"
attack_technique_ids:
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VeeamBackup Database Credentials Dump Via Sqlcmd.EXE

Detects dump of credentials in VeeamBackup dbo

## Metadata

- Rule ID: b57ba453-b384-4ab9-9f40-1038086b4e53
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-20
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_dump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
selection_tools:
  Image|endswith: \sqlcmd.exe
selection_query:
  CommandLine|contains|all:
  - SELECT
  - TOP
  - '[VeeamBackup].[dbo].[Credentials]'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/12/13/diavol-ransomware/
- https://forums.veeam.com/veeam-backup-replication-f2/recover-esxi-password-in-veeam-t34630.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_dump.yml)
