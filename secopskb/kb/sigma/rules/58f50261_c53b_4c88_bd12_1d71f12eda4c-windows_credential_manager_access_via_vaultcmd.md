---
sigma_id: "58f50261-c53b-4c88-bd12-1d71f12eda4c"
title: "Windows Credential Manager Access via VaultCmd"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vaultcmd_list_creds.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vaultcmd_list_creds.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "58f50261-c53b-4c88-bd12-1d71f12eda4c"
  - "Windows Credential Manager Access via VaultCmd"
attack_technique_ids:
  - "T1555.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Credential Manager Access via VaultCmd

List credentials currently stored in Windows Credential Manager via the native Windows utility vaultcmd.exe

## Metadata

- Rule ID: 58f50261-c53b-4c88-bd12-1d71f12eda4c
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-08
- Modified: 2022-05-13
- Source Path: rules/windows/process_creation/proc_creation_win_vaultcmd_list_creds.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \VaultCmd.exe
- OriginalFileName: VAULTCMD.EXE
selection_cli:
  CommandLine|contains: '/listcreds:'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555.004/T1555.004.md#atomic-test-1---access-saved-credentials-via-vaultcmd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vaultcmd_list_creds.yml)
