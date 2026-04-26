---
sigma_id: "28a452f3-786c-4fd8-b8f2-bddbe9d616d1"
title: "Creation of WerFault.exe/Wer.dll in Unusual Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_werfault_dll_hijacking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_werfault_dll_hijacking.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "28a452f3-786c-4fd8-b8f2-bddbe9d616d1"
  - "Creation of WerFault.exe/Wer.dll in Unusual Folder"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Creation of WerFault.exe/Wer.dll in Unusual Folder

Detects the creation of a file named "WerFault.exe" or "wer.dll" in an uncommon folder, which could be a sign of WerFault DLL hijacking.

## Metadata

- Rule ID: 28a452f3-786c-4fd8-b8f2-bddbe9d616d1
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-05-09
- Modified: 2025-12-03
- Source Path: rules/windows/file/file_event/file_event_win_werfault_dll_hijacking.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \WerFault.exe
  - \wer.dll
filter_main_known_locations:
  TargetFilename|startswith:
  - C:\Windows\SoftwareDistribution\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
  - C:\Windows\UUS\arm64\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/hackers-are-now-hiding-malware-in-windows-event-logs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_werfault_dll_hijacking.yml)
