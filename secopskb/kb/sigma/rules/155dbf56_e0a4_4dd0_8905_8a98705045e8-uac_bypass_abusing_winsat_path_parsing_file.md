---
sigma_id: "155dbf56-e0a4-4dd0-8905-8a98705045e8"
title: "UAC Bypass Abusing Winsat Path Parsing - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_winsat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_winsat.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "155dbf56-e0a4-4dd0-8905-8a98705045e8"
  - "UAC Bypass Abusing Winsat Path Parsing - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UAC Bypass Abusing Winsat Path Parsing - File

Detects the pattern of UAC Bypass using a path parsing issue in winsat.exe (UACMe 52)

## Metadata

- Rule ID: 155dbf56-e0a4-4dd0-8905-8a98705045e8
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2022-10-09
- Source Path: rules/windows/file/file_event/file_event_win_uac_bypass_winsat.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Users\
  TargetFilename|endswith:
  - \AppData\Local\Temp\system32\winsat.exe
  - \AppData\Local\Temp\system32\winmm.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_winsat.yml)
