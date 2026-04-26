---
sigma_id: "976d6e6f-a04b-4900-9713-0134a353e38b"
title: "Veeam Backup Servers Credential Dumping Script Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_veeam_credential_dumping_script.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_veeam_credential_dumping_script.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "976d6e6f-a04b-4900-9713-0134a353e38b"
  - "Veeam Backup Servers Credential Dumping Script Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Veeam Backup Servers Credential Dumping Script Execution

Detects execution of a PowerShell script that contains calls to the "Veeam.Backup" class, in order to dump stored credentials.

## Metadata

- Rule ID: 976d6e6f-a04b-4900-9713-0134a353e38b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_veeam_credential_dumping_script.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - '[Credentials]'
  - '[Veeam.Backup.Common.ProtectedStorage]::GetLocalString'
  - Invoke-Sqlcmd
  - Veeam Backup and Replication
condition: selection
```

## False Positives

- Administrators backup scripts (must be investigated)

## References

- https://www.pwndefend.com/2021/02/15/retrieving-passwords-from-veeam-backup-servers/
- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_veeam_credential_dumping_script.yml)
