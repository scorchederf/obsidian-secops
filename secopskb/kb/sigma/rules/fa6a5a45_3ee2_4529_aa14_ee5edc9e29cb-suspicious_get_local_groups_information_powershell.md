---
sigma_id: "fa6a5a45-3ee2-4529-aa14-ee5edc9e29cb"
title: "Suspicious Get Local Groups Information - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_local_group_reco.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_local_group_reco.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "fa6a5a45-3ee2-4529-aa14-ee5edc9e29cb"
  - "Suspicious Get Local Groups Information - PowerShell"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Get Local Groups Information - PowerShell

Detects the use of PowerShell modules and cmdlets to gather local group information.
Adversaries may use local system permission groups to determine which groups exist and which users belong to a particular group such as the local administrators group.

## Metadata

- Rule ID: fa6a5a45-3ee2-4529-aa14-ee5edc9e29cb
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-12
- Modified: 2025-08-22
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_local_group_reco.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_localgroup:
  ScriptBlockText|contains:
  - 'get-localgroup '
  - 'get-localgroupmember '
selection_wmi_module:
  ScriptBlockText|contains:
  - 'get-wmiobject '
  - 'gwmi '
  - 'get-ciminstance '
  - 'gcim '
selection_wmi_class:
  ScriptBlockText|contains: win32_group
condition: selection_localgroup or all of selection_wmi_*
```

## False Positives

- Inventory scripts or admin tasks

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.001/T1069.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_local_group_reco.yml)
