---
sigma_id: "7fff6773-2baa-46de-a24a-b6eec1aba2d1"
title: "UAC Bypass Using NTFS Reparse Point - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_ntfs_reparse_point.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_ntfs_reparse_point.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "7fff6773-2baa-46de-a24a-b6eec1aba2d1"
  - "UAC Bypass Using NTFS Reparse Point - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Using NTFS Reparse Point - File

Detects the pattern of UAC Bypass using NTFS reparse point and wusa.exe DLL hijacking (UACMe 36)

## Metadata

- Rule ID: 7fff6773-2baa-46de-a24a-b6eec1aba2d1
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2022-10-09
- Source Path: rules/windows/file/file_event/file_event_win_uac_bypass_ntfs_reparse_point.yml

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
  TargetFilename|endswith: \AppData\Local\Temp\api-ms-win-core-kernel32-legacy-l1.DLL
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_ntfs_reparse_point.yml)
