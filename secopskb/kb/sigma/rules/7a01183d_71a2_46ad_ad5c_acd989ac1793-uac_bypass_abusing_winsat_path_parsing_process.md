---
sigma_id: "7a01183d-71a2-46ad-ad5c-acd989ac1793"
title: "UAC Bypass Abusing Winsat Path Parsing - Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_winsat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_winsat.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7a01183d-71a2-46ad-ad5c-acd989ac1793"
  - "UAC Bypass Abusing Winsat Path Parsing - Process"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UAC Bypass Abusing Winsat Path Parsing - Process

Detects the pattern of UAC Bypass using a path parsing issue in winsat.exe (UACMe 52)

## Metadata

- Rule ID: 7a01183d-71a2-46ad-ad5c-acd989ac1793
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_winsat.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
  ParentImage|endswith: \AppData\Local\Temp\system32\winsat.exe
  ParentCommandLine|contains: C:\Windows \system32\winsat.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_winsat.yml)
