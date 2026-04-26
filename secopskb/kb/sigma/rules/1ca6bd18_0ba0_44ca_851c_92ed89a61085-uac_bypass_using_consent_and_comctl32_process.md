---
sigma_id: "1ca6bd18-0ba0-44ca-851c-92ed89a61085"
title: "UAC Bypass Using Consent and Comctl32 - Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_consent_comctl32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_consent_comctl32.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1ca6bd18-0ba0-44ca-851c-92ed89a61085"
  - "UAC Bypass Using Consent and Comctl32 - Process"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using Consent and Comctl32 - Process

Detects the pattern of UAC Bypass using consent.exe and comctl32.dll (UACMe 22)

## Metadata

- Rule ID: 1ca6bd18-0ba0-44ca-851c-92ed89a61085
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_consent_comctl32.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ParentImage|endswith: \consent.exe
  Image|endswith: \werfault.exe
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_consent_comctl32.yml)
