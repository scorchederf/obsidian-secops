---
sigma_id: "39ed3c80-e6a1-431b-9df3-911ac53d08a7"
title: "UAC Bypass Using NTFS Reparse Point - Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_ntfs_reparse_point.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_ntfs_reparse_point.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "39ed3c80-e6a1-431b-9df3-911ac53d08a7"
  - "UAC Bypass Using NTFS Reparse Point - Process"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using NTFS Reparse Point - Process

Detects the pattern of UAC Bypass using NTFS reparse point and wusa.exe DLL hijacking (UACMe 36)

## Metadata

- Rule ID: 39ed3c80-e6a1-431b-9df3-911ac53d08a7
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_ntfs_reparse_point.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection1:
  CommandLine|startswith: '"C:\Windows\system32\wusa.exe"  /quiet C:\Users\'
  CommandLine|endswith: \AppData\Local\Temp\update.msu
  IntegrityLevel:
  - High
  - System
  - S-1-16-16384
  - S-1-16-12288
selection2:
  ParentCommandLine: '"C:\Windows\system32\dism.exe" /online /quiet /norestart /add-package
    /packagepath:"C:\Windows\system32\pe386" /ignorecheck'
  IntegrityLevel:
  - High
  - System
  CommandLine|contains|all:
  - C:\Users\
  - \AppData\Local\Temp\
  - \dismhost.exe {
  Image|endswith: \DismHost.exe
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_ntfs_reparse_point.yml)
