---
sigma_id: "0b0cd537-fc77-4e6e-a973-e53495c1083d"
title: "Renamed Office Binary Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_office_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_office_processes.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0b0cd537-fc77-4e6e-a973-e53495c1083d"
  - "Renamed Office Binary Execution"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of a renamed office binary

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

## Detection

```yaml
selection:
- OriginalFileName:
  - Excel.exe
  - MSACCESS.EXE
  - MSPUB.EXE
  - OneNote.exe
  - OneNoteM.exe
  - OUTLOOK.EXE
  - POWERPNT.EXE
  - WinWord.exe
  - Olk.exe
- Description:
  - Microsoft Access
  - Microsoft Excel
  - Microsoft OneNote
  - Microsoft Outlook
  - Microsoft PowerPoint
  - Microsoft Publisher
  - Microsoft Word
  - Sent to OneNote Tool
filter_main_legit_names:
  Image|endswith:
  - \EXCEL.exe
  - \excelcnv.exe
  - \MSACCESS.exe
  - \MSPUB.EXE
  - \ONENOTE.EXE
  - \ONENOTEM.EXE
  - \OUTLOOK.EXE
  - \POWERPNT.EXE
  - \WINWORD.exe
  - \OLK.EXE
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://infosec.exchange/@sbousseaden/109542254124022664

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_office_processes.yml)
