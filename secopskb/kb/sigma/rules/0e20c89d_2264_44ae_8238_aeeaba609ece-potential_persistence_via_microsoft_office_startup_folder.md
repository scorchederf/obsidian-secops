---
sigma_id: "0e20c89d-2264-44ae-8238-aeeaba609ece"
title: "Potential Persistence Via Microsoft Office Startup Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_startup_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_startup_persistence.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "0e20c89d-2264-44ae-8238-aeeaba609ece"
  - "Potential Persistence Via Microsoft Office Startup Folder"
attack_technique_ids:
  - "T1137"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Microsoft Office Startup Folder

Detects creation of Microsoft Office files inside of one of the default startup folders in order to achieve persistence.

## Metadata

- Rule ID: 0e20c89d-2264-44ae-8238-aeeaba609ece
- Status: test
- Level: high
- Author: Max Altgelt (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-02
- Modified: 2023-06-22
- Source Path: rules/windows/file/file_event/file_event_win_office_startup_persistence.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]

## Detection

```yaml
selection_word_paths:
- TargetFilename|contains: \Microsoft\Word\STARTUP
- TargetFilename|contains|all:
  - \Office
  - \Program Files
  - \STARTUP
selection_word_extension:
  TargetFilename|endswith:
  - .doc
  - .docm
  - .docx
  - .dot
  - .dotm
  - .rtf
selection_excel_paths:
- TargetFilename|contains: \Microsoft\Excel\XLSTART
- TargetFilename|contains|all:
  - \Office
  - \Program Files
  - \XLSTART
selection_excel_extension:
  TargetFilename|endswith:
  - .xls
  - .xlsm
  - .xlsx
  - .xlt
  - .xltm
filter_main_office:
  Image|endswith:
  - \WINWORD.exe
  - \EXCEL.exe
condition: (all of selection_word_* or all of selection_excel_*) and not filter_main_office
```

## False Positives

- Loading a user environment from a backup or a domain controller
- Synchronization of templates

## References

- https://insight-jp.nttsecurity.com/post/102hojk/operation-restylink-apt-campaign-targeting-japanese-companies
- https://learn.microsoft.com/en-us/office/troubleshoot/excel/use-startup-folders

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_startup_persistence.yml)
