---
sigma_id: "0058b9e5-bcd7-40d4-9205-95ca5a16d7b2"
title: "UAC Bypass Using Windows Media Player - Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_wmp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_wmp.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0058b9e5-bcd7-40d4-9205-95ca5a16d7b2"
  - "UAC Bypass Using Windows Media Player - Process"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using Windows Media Player - Process

Detects the pattern of UAC Bypass using Windows Media Player osksupport.dll (UACMe 32)

## Metadata

- Rule ID: 0058b9e5-bcd7-40d4-9205-95ca5a16d7b2
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_wmp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection_img_1:
  Image: C:\Program Files\Windows Media Player\osk.exe
selection_img_2:
  Image: C:\Windows\System32\cmd.exe
  ParentCommandLine: '"C:\Windows\system32\mmc.exe" "C:\Windows\system32\eventvwr.msc"
    /s'
selection_integrity:
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
condition: 1 of selection_img_* and selection_integrity
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_wmp.yml)
