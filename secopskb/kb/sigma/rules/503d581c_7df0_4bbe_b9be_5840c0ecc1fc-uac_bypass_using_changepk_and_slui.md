---
sigma_id: "503d581c-7df0-4bbe-b9be-5840c0ecc1fc"
title: "UAC Bypass Using ChangePK and SLUI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_changepk_slui.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_changepk_slui.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "503d581c-7df0-4bbe-b9be-5840c0ecc1fc"
  - "UAC Bypass Using ChangePK and SLUI"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using ChangePK and SLUI

Detects an UAC bypass that uses changepk.exe and slui.exe (UACMe 61)

## Metadata

- Rule ID: 503d581c-7df0-4bbe-b9be-5840c0ecc1fc
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_changepk_slui.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  Image|endswith: \changepk.exe
  ParentImage|endswith: \slui.exe
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
condition: selection
```

## False Positives

- Unknown

## References

- https://mattharr0ey.medium.com/privilege-escalation-uac-bypass-in-changepk-c40b92818d1b
- https://github.com/hfiref0x/UACME
- https://medium.com/falconforce/falconfriday-detecting-uac-bypasses-0xff16-86c2a9107abf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_changepk_slui.yml)
