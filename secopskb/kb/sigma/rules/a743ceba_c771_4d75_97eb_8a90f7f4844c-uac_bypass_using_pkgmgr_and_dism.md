---
sigma_id: "a743ceba-c771-4d75-97eb-8a90f7f4844c"
title: "UAC Bypass Using PkgMgr and DISM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_pkgmgr_dism.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_pkgmgr_dism.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a743ceba-c771-4d75-97eb-8a90f7f4844c"
  - "UAC Bypass Using PkgMgr and DISM"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Using PkgMgr and DISM

Detects the pattern of UAC Bypass using pkgmgr.exe and dism.exe (UACMe 23)

## Metadata

- Rule ID: a743ceba-c771-4d75-97eb-8a90f7f4844c
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_pkgmgr_dism.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ParentImage|endswith: \pkgmgr.exe
  Image|endswith: \dism.exe
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

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_pkgmgr_dism.yml)
