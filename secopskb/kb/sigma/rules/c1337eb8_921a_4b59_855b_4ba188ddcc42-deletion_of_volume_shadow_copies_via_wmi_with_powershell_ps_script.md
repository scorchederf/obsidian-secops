---
sigma_id: "c1337eb8-921a-4b59-855b-4ba188ddcc42"
title: "Deletion of Volume Shadow Copies via WMI with PowerShell - PS Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_win32_shadowcopy_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_win32_shadowcopy_deletion.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "c1337eb8-921a-4b59-855b-4ba188ddcc42"
  - "Deletion of Volume Shadow Copies via WMI with PowerShell - PS Script"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects deletion of Windows Volume Shadow Copies with PowerShell code and Get-WMIObject. This technique is used by numerous ransomware families such as Sodinokibi/REvil

## Logsource

- category: ps_script
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

## Detection

```yaml
selection_get:
  ScriptBlockText|contains:
  - Get-WmiObject
  - gwmi
  - Get-CimInstance
  - gcim
selection_shadowcopy:
  ScriptBlockText|contains: Win32_ShadowCopy
selection_delete:
  ScriptBlockText|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_win32_shadowcopy_deletion.yml)
