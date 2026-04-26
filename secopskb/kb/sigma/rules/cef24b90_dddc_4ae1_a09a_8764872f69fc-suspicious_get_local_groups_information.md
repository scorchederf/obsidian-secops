---
sigma_id: "cef24b90-dddc-4ae1-a09a-8764872f69fc"
title: "Suspicious Get Local Groups Information"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_local_group_reco.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_local_group_reco.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / ps_module"
aliases:
  - "cef24b90-dddc-4ae1-a09a-8764872f69fc"
  - "Suspicious Get Local Groups Information"
attack_technique_ids:
  - "T1069.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Get Local Groups Information

Detects the use of PowerShell modules and cmdlets to gather local group information.
Adversaries may use local system permission groups to determine which groups exist and which users belong to a particular group such as the local administrators group.

## Metadata

- Rule ID: cef24b90-dddc-4ae1-a09a-8764872f69fc
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-12
- Modified: 2025-08-22
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_local_group_reco.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]

## Detection

```yaml
selection_localgroup:
- Payload|contains:
  - 'get-localgroup '
  - 'get-localgroupmember '
- ContextInfo|contains:
  - 'get-localgroup '
  - 'get-localgroupmember '
selection_wmi_module:
- Payload|contains:
  - 'get-wmiobject '
  - 'gwmi '
  - 'get-ciminstance '
  - 'gcim '
- ContextInfo|contains|all:
  - 'get-wmiobject '
  - 'gwmi '
  - 'get-ciminstance '
  - 'gcim '
selection_wmi_class:
- Payload|contains: win32_group
- ContextInfo|contains: win32_group
condition: selection_localgroup or all of selection_wmi_*
```

## False Positives

- Administrator script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.001/T1069.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_local_group_reco.yml)
