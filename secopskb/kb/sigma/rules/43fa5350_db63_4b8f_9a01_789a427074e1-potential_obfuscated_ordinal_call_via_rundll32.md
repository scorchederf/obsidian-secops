---
sigma_id: "43fa5350-db63-4b8f-9a01-789a427074e1"
title: "Potential Obfuscated Ordinal Call Via Rundll32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_obfuscated_ordinal_call.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_obfuscated_ordinal_call.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "43fa5350-db63-4b8f-9a01-789a427074e1"
  - "Potential Obfuscated Ordinal Call Via Rundll32"
attack_technique_ids:
  - "T1027.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Obfuscated Ordinal Call Via Rundll32

Detects execution of "rundll32" with potential obfuscated ordinal calls

## Metadata

- Rule ID: 43fa5350-db63-4b8f-9a01-789a427074e1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2023-05-17
- Modified: 2025-02-23
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_obfuscated_ordinal_call.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.010]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
- CommandLine|contains: rundll32
selection_cli:
  CommandLine|contains:
  - '#+'
  - '#-'
  - '#0'
  - '#655'
  - '#656'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://www.youtube.com/watch?v=52tAmVLg1KM&t=2070s

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_obfuscated_ordinal_call.yml)
