---
sigma_id: "8c3a6607-b7dc-4f0d-a646-ef38c00b76ee"
title: "Active Directory Group Enumeration With Get-AdGroup"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_get_adgroup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_adgroup.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "8c3a6607-b7dc-4f0d-a646-ef38c00b76ee"
  - "Active Directory Group Enumeration With Get-AdGroup"
attack_technique_ids:
  - "T1069.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Active Directory Group Enumeration With Get-AdGroup

Detects usage of the "Get-AdGroup" cmdlet to enumerate Groups within Active Directory

## Metadata

- Rule ID: 8c3a6607-b7dc-4f0d-a646-ef38c00b76ee
- Status: test
- Level: low
- Author: frack113
- Date: 2022-03-17
- Modified: 2022-11-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_get_adgroup.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Get-AdGroup '
  - -Filter
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_adgroup.yml)
