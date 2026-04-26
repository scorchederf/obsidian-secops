---
sigma_id: "4b60e6f2-bf39-47b4-b4ea-398e33cfe253"
title: "CMSTP UAC Bypass via COM Object Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp_com_object_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp_com_object_access.yml"
build_date: "2026-04-26 14:14:21"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4b60e6f2-bf39-47b4-b4ea-398e33cfe253"
  - "CMSTP UAC Bypass via COM Object Access"
attack_technique_ids:
  - "T1548.002"
  - "T1218.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CMSTP UAC Bypass via COM Object Access

Detects UAC Bypass Attempt Using Microsoft Connection Manager Profile Installer Autoelevate-capable COM Objects (e.g. UACMe ID of 41, 43, 58 or 65)

## Metadata

- Rule ID: 4b60e6f2-bf39-47b4-b4ea-398e33cfe253
- Status: stable
- Level: high
- Author: Nik Seetharaman, Christian Burkard (Nextron Systems)
- Date: 2019-07-31
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp_com_object_access.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Detection

```yaml
selection:
  ParentImage|endswith: \DllHost.exe
  ParentCommandLine|contains:
  - ' /Processid:{3E5FC7F9-9A51-4367-9063-A120244FBEC7}'
  - ' /Processid:{3E000D72-A845-4CD9-BD83-80C07C3B881F}'
  - ' /Processid:{BD54C901-076B-434E-B6C7-17C531F4AB41}'
  - ' /Processid:{D2E7041B-2927-42FB-8E9F-7CE93B6DC937}'
  - ' /Processid:{E9495B87-D950-4AB5-87A5-FF6D70BF3E90}'
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
condition: selection
```

## False Positives

- Legitimate CMSTP use (unlikely in modern enterprise environments)

## References

- https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/
- https://twitter.com/hFireF0X/status/897640081053364225
- https://medium.com/falconforce/falconfriday-detecting-uac-bypasses-0xff16-86c2a9107abf
- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp_com_object_access.yml)
