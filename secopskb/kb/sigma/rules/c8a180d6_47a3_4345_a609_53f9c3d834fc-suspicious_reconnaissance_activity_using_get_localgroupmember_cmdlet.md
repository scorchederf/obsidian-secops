---
sigma_id: "c8a180d6-47a3-4345-a609-53f9c3d834fc"
title: "Suspicious Reconnaissance Activity Using Get-LocalGroupMember Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_get_localgroup_member_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_get_localgroup_member_recon.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c8a180d6-47a3-4345-a609-53f9c3d834fc"
  - "Suspicious Reconnaissance Activity Using Get-LocalGroupMember Cmdlet"
attack_technique_ids:
  - "T1087.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Reconnaissance Activity Using Get-LocalGroupMember Cmdlet

Detects suspicious reconnaissance command line activity on Windows systems using the PowerShell Get-LocalGroupMember Cmdlet

## Metadata

- Rule ID: c8a180d6-47a3-4345-a609-53f9c3d834fc
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-10
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_get_localgroup_member_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Detection

```yaml
selection_cmdlet:
  CommandLine|contains: 'Get-LocalGroupMember '
selection_group:
  CommandLine|contains:
  - domain admins
  - ' administrator'
  - ' administrateur'
  - enterprise admins
  - Exchange Trusted Subsystem
  - Remote Desktop Users
  - Utilisateurs du Bureau à distance
  - Usuarios de escritorio remoto
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_get_localgroup_member_recon.yml)
