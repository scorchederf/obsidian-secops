---
sigma_id: "853e74f9-9392-4935-ad3b-2e8c040dae86"
title: "UAC Bypass Using DismHost"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_dismhost.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_dismhost.yml"
build_date: "2026-04-26 15:01:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "853e74f9-9392-4935-ad3b-2e8c040dae86"
  - "UAC Bypass Using DismHost"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Using DismHost

Detects the pattern of UAC Bypass using DismHost DLL hijacking (UACMe 63)

## Metadata

- Rule ID: 853e74f9-9392-4935-ad3b-2e8c040dae86
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_dismhost.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ParentImage|contains|all:
  - C:\Users\
  - \AppData\Local\Temp\
  - \DismHost.exe
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_dismhost.yml)
