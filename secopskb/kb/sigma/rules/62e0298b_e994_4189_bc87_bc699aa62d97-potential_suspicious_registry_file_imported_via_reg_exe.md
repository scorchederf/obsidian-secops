---
sigma_id: "62e0298b-e994-4189-bc87-bc699aa62d97"
title: "Potential Suspicious Registry File Imported Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_import_from_suspicious_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_import_from_suspicious_paths.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "62e0298b-e994-4189-bc87-bc699aa62d97"
  - "Potential Suspicious Registry File Imported Via Reg.EXE"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious Registry File Imported Via Reg.EXE

Detects the import of '.reg' files from suspicious paths using the 'reg.exe' utility

## Metadata

- Rule ID: 62e0298b-e994-4189-bc87-bc699aa62d97
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali
- Date: 2022-08-01
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_reg_import_from_suspicious_paths.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_cli:
  CommandLine|contains: ' import '
selection_paths:
  CommandLine|contains:
  - C:\Users\
  - '%temp%'
  - '%tmp%'
  - '%appdata%'
  - \AppData\Local\Temp\
  - C:\Windows\Temp\
  - C:\ProgramData\
condition: all of selection_*
```

## False Positives

- Legitimate import of keys

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_import_from_suspicious_paths.yml)
