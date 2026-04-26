---
sigma_id: "91174a41-dc8f-401b-be89-7bfc140612a0"
title: "Office Macro File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_macro_files_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_macro_files_created.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "91174a41-dc8f-401b-be89-7bfc140612a0"
  - "Office Macro File Creation"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Office Macro File Creation

Detects the creation of a new office macro files on the systems

## Metadata

- Rule ID: 91174a41-dc8f-401b-be89-7bfc140612a0
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-23
- Source Path: rules/windows/file/file_event/file_event_win_office_macro_files_created.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - .docm
  - .dotm
  - .xlsm
  - .xltm
  - .potm
  - .pptm
condition: selection
```

## False Positives

- Very common in environments that rely heavily on macro documents

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1566.001/T1566.001.md
- https://learn.microsoft.com/en-us/deployoffice/compat/office-file-format-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_macro_files_created.yml)
