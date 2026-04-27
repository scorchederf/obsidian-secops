---
sigma_id: "a10a2c40-2c4d-49f8-b557-1a946bc55d9d"
title: "Uncommon File Created In Office Startup Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_uncommon_file_startup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_uncommon_file_startup.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "a10a2c40-2c4d-49f8-b557-1a946bc55d9d"
  - "Uncommon File Created In Office Startup Folder"
attack_technique_ids:
  - "T1587.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a file with an uncommon extension in an Office application startup folder

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities#^t1587001-malware|T1587.001: Malware]]

## Detection

```yaml
selection_word_paths:
- TargetFilename|contains: \Microsoft\Word\STARTUP
- TargetFilename|contains|all:
  - \Office
  - \Program Files
  - \STARTUP
filter_exclude_word_ext:
  TargetFilename|endswith:
  - .docb
  - .docm
  - .docx
  - .dotm
  - .mdb
  - .mdw
  - .pdf
  - .wll
  - .wwl
selection_excel_paths:
- TargetFilename|contains: \Microsoft\Excel\XLSTART
- TargetFilename|contains|all:
  - \Office
  - \Program Files
  - \XLSTART
filter_exclude_excel_ext:
  TargetFilename|endswith:
  - .xll
  - .xls
  - .xlsm
  - .xlsx
  - .xlt
  - .xltm
  - .xlw
filter_main_office_click_to_run:
  Image|contains: :\Program Files\Common Files\Microsoft Shared\ClickToRun\
  Image|endswith: \OfficeClickToRun.exe
filter_main_office_apps:
  Image|contains:
  - :\Program Files\Microsoft Office\
  - :\Program Files (x86)\Microsoft Office\
  Image|endswith:
  - \winword.exe
  - \excel.exe
condition: ((selection_word_paths and not filter_exclude_word_ext) or (selection_excel_paths
  and not filter_exclude_excel_ext)) and not 1 of filter_main_*
```

## False Positives

- False positive might stem from rare extensions used by other Office utilities.

## References

- https://app.any.run/tasks/d6fe6624-6ef8-485d-aa75-3d1bdda2a08c/
- http://addbalance.com/word/startup.htm
- https://answers.microsoft.com/en-us/msoffice/forum/all/document-in-word-startup-folder-doesnt-open-when/44ab0932-2917-4150-8cdc-2f2cf39e86f3
- https://en.wikipedia.org/wiki/List_of_Microsoft_Office_filename_extensions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_uncommon_file_startup.yml)
