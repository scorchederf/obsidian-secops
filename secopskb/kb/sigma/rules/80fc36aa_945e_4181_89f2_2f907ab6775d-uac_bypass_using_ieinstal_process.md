---
sigma_id: "80fc36aa-945e-4181-89f2-2f907ab6775d"
title: "UAC Bypass Using IEInstal - Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_ieinstal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_ieinstal.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "80fc36aa-945e-4181-89f2-2f907ab6775d"
  - "UAC Bypass Using IEInstal - Process"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the pattern of UAC Bypass using IEInstal.exe (UACMe 64)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection:
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
  ParentImage|endswith: \ieinstal.exe
  Image|contains: \AppData\Local\Temp\
  Image|endswith: consent.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_ieinstal.yml)
