---
sigma_id: "4cbef972-f347-4170-b62a-8253f6168e6d"
title: "UAC Bypass Using IDiagnostic Profile"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_idiagnostic_profile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_idiagnostic_profile.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4cbef972-f347-4170-b62a-8253f6168e6d"
  - "UAC Bypass Using IDiagnostic Profile"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Using IDiagnostic Profile

Detects the "IDiagnosticProfileUAC" UAC bypass technique

## Metadata

- Rule ID: 4cbef972-f347-4170-b62a-8253f6168e6d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-03
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_idiagnostic_profile.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ParentImage|endswith: \DllHost.exe
  ParentCommandLine|contains: ' /Processid:{12C21EA7-2EB8-4B55-9249-AC243DA8C666}'
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

- https://github.com/Wh04m1001/IDiagnosticProfileUAC

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_idiagnostic_profile.yml)
