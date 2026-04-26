---
sigma_id: "87df9ee1-5416-453a-8a08-e8d4a51e9ce1"
title: "Delete Volume Shadow Copies Via WMI With PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_delete_volume_shadow_copies.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_delete_volume_shadow_copies.yml"
build_date: "2026-04-26 14:14:23"
status: "stable"
level: "high"
logsource: "windows / ps_classic_start"
aliases:
  - "87df9ee1-5416-453a-8a08-e8d4a51e9ce1"
  - "Delete Volume Shadow Copies Via WMI With PowerShell"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Delete Volume Shadow Copies Via WMI With PowerShell

Shadow Copies deletion using operating systems utilities via PowerShell

## Metadata

- Rule ID: 87df9ee1-5416-453a-8a08-e8d4a51e9ce1
- Status: stable
- Level: high
- Author: frack113
- Date: 2021-06-03
- Modified: 2023-10-27
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_delete_volume_shadow_copies.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  Data|contains|all:
  - Get-WmiObject
  - Win32_ShadowCopy
  Data|contains:
  - Delete()
  - Remove-WmiObject
condition: selection
```

## False Positives

- Legitimate Administrator deletes Shadow Copies using operating systems utilities for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md
- https://www.fortinet.com/blog/threat-research/stomping-shadow-copies-a-second-look-into-deletion-methods

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_delete_volume_shadow_copies.yml)
