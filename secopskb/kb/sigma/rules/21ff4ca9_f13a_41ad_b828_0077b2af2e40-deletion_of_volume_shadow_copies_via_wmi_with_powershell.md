---
sigma_id: "21ff4ca9-f13a-41ad-b828-0077b2af2e40"
title: "Deletion of Volume Shadow Copies via WMI with PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_shadowcopy_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_shadowcopy_deletion.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "21ff4ca9-f13a-41ad-b828-0077b2af2e40"
  - "Deletion of Volume Shadow Copies via WMI with PowerShell"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Deletion of Volume Shadow Copies via WMI with PowerShell

Detects deletion of Windows Volume Shadow Copies with PowerShell code and Get-WMIObject. This technique is used by numerous ransomware families such as Sodinokibi/REvil

## Metadata

- Rule ID: 21ff4ca9-f13a-41ad-b828-0077b2af2e40
- Status: test
- Level: high
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-20
- Modified: 2022-12-30
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_shadowcopy_deletion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection_get:
  CommandLine|contains:
  - Get-WmiObject
  - gwmi
  - Get-CimInstance
  - gcim
selection_shadowcopy:
  CommandLine|contains: Win32_ShadowCopy
selection_delete:
  CommandLine|contains:
  - .Delete()
  - Remove-WmiObject
  - rwmi
  - Remove-CimInstance
  - rcim
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1490/T1490.md#atomic-test-5---windows---delete-volume-shadow-copies-via-wmi-with-powershell
- https://www.elastic.co/guide/en/security/current/volume-shadow-copy-deletion-via-powershell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_shadowcopy_deletion.yml)
