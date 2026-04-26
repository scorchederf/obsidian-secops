---
sigma_id: "3268b746-88d8-4cd3-bffc-30077d02c787"
title: "HackTool - Empire PowerShell UAC Bypass"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_uac_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_uac_bypass.yml"
build_date: "2026-04-26 17:03:19"
status: "stable"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "3268b746-88d8-4cd3-bffc-30077d02c787"
  - "HackTool - Empire PowerShell UAC Bypass"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Empire PowerShell UAC Bypass

Detects some Empire PowerShell UAC bypass methods

## Metadata

- Rule ID: 3268b746-88d8-4cd3-bffc-30077d02c787
- Status: stable
- Level: critical
- Author: Ecco
- Date: 2019-08-30
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_uac_bypass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ' -NoP -NonI -w Hidden -c $x=$((gp HKCU:Software\Microsoft\Windows Update).Update)'
  - ' -NoP -NonI -c $x=$((gp HKCU:Software\Microsoft\Windows Update).Update);'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13055/data/module_source/privesc/Invoke-EventVwrBypass.ps1#L64
- https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13055/data/module_source/privesc/Invoke-FodHelperBypass.ps1#L64

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_uac_bypass.yml)
