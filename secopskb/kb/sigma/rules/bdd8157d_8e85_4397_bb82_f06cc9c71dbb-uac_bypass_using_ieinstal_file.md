---
sigma_id: "bdd8157d-8e85-4397-bb82-f06cc9c71dbb"
title: "UAC Bypass Using IEInstal - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_ieinstal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_ieinstal.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "bdd8157d-8e85-4397-bb82-f06cc9c71dbb"
  - "UAC Bypass Using IEInstal - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using IEInstal - File

Detects the pattern of UAC Bypass using IEInstal.exe (UACMe 64)

## Metadata

- Rule ID: bdd8157d-8e85-4397-bb82-f06cc9c71dbb
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2022-10-09
- Source Path: rules/windows/file/file_event/file_event_win_uac_bypass_ieinstal.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  Image: C:\Program Files\Internet Explorer\IEInstal.exe
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains: \AppData\Local\Temp\
  TargetFilename|endswith: consent.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_ieinstal.yml)
