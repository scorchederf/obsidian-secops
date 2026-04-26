---
sigma_id: "62ed5b55-f991-406a-85d9-e8e8fdf18789"
title: "UAC Bypass Using Consent and Comctl32 - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_consent_comctl32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_consent_comctl32.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "62ed5b55-f991-406a-85d9-e8e8fdf18789"
  - "UAC Bypass Using Consent and Comctl32 - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using Consent and Comctl32 - File

Detects the pattern of UAC Bypass using consent.exe and comctl32.dll (UACMe 22)

## Metadata

- Rule ID: 62ed5b55-f991-406a-85d9-e8e8fdf18789
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/windows/file/file_event/file_event_win_uac_bypass_consent_comctl32.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\System32\consent.exe.@
  TargetFilename|endswith: \comctl32.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_consent_comctl32.yml)
