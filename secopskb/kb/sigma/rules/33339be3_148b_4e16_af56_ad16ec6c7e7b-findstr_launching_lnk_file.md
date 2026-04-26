---
sigma_id: "33339be3-148b-4e16-af56-ad16ec6c7e7b"
title: "Findstr Launching .lnk File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_lnk.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_lnk.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "33339be3-148b-4e16-af56-ad16ec6c7e7b"
  - "Findstr Launching .lnk File"
attack_technique_ids:
  - "T1036"
  - "T1202"
  - "T1027.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Findstr Launching .lnk File

Detects usage of findstr to identify and execute a lnk file as seen within the HHS redirect attack

## Metadata

- Rule ID: 33339be3-148b-4e16-af56-ad16ec6c7e7b
- Status: test
- Level: medium
- Author: Trent Liffick
- Date: 2020-05-01
- Modified: 2024-01-15
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_lnk.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.003]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \find.exe
  - \findstr.exe
- OriginalFileName:
  - FIND.EXE
  - FINDSTR.EXE
selection_cli:
  CommandLine|endswith:
  - .lnk
  - .lnk"
  - .lnk'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/hhsgov-open-redirect-used-by-coronavirus-phishing-to-spread-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_lnk.yml)
