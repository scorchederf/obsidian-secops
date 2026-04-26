---
sigma_id: "696bfb54-227e-4602-ac5b-30d9d2053312"
title: "Veeam Backup Database Suspicious Query"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_db_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_db_recon.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "696bfb54-227e-4602-ac5b-30d9d2053312"
  - "Veeam Backup Database Suspicious Query"
attack_technique_ids:
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Veeam Backup Database Suspicious Query

Detects potentially suspicious SQL queries using SQLCmd targeting the Veeam backup databases in order to steal information.

## Metadata

- Rule ID: 696bfb54-227e-4602-ac5b-30d9d2053312
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-04
- Source Path: rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_db_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
selection_sql:
  Image|endswith: \sqlcmd.exe
  CommandLine|contains|all:
  - VeeamBackup
  - 'From '
selection_db:
  CommandLine|contains:
  - BackupRepositories
  - Backups
  - Credentials
  - HostCreds
  - SmbFileShares
  - Ssh_creds
  - VSphereInfo
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlcmd_veeam_db_recon.yml)
