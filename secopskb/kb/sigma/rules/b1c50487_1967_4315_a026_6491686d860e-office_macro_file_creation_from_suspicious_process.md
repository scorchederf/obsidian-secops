---
sigma_id: "b1c50487-1967-4315-a026-6491686d860e"
title: "Office Macro File Creation From Suspicious Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_macro_files_from_susp_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_macro_files_from_susp_process.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "b1c50487-1967-4315-a026-6491686d860e"
  - "Office Macro File Creation From Suspicious Process"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Office Macro File Creation From Suspicious Process

Detects the creation of a office macro file from a a suspicious process

## Metadata

- Rule ID: b1c50487-1967-4315-a026-6491686d860e
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-23
- Modified: 2023-02-22
- Source Path: rules/windows/file/file_event/file_event_win_office_macro_files_from_susp_process.yml

## Logsource

- category: file_event
- definition: Requirements: The "ParentImage" field is not available by default on EID 11 of Sysmon logs. To be able to use this rule to the full extent you need to enriche the log with additional ParentImage data
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection_cmd:
- Image|endswith:
  - \cscript.exe
  - \mshta.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- ParentImage|endswith:
  - \cscript.exe
  - \mshta.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
selection_ext:
  TargetFilename|endswith:
  - .docm
  - .dotm
  - .xlsm
  - .xltm
  - .potm
  - .pptm
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1566.001/T1566.001.md
- https://learn.microsoft.com/en-us/deployoffice/compat/office-file-format-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_macro_files_from_susp_process.yml)
