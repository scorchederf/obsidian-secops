---
sigma_id: "4ae3e30b-b03f-43aa-87e3-b622f4048eed"
title: "Potential Arbitrary File Download Using Office Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_arbitrary_cli_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_arbitrary_cli_download.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4ae3e30b-b03f-43aa-87e3-b622f4048eed"
  - "Potential Arbitrary File Download Using Office Application"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential arbitrary file download using a Microsoft Office application

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \EXCEL.EXE
  - \POWERPNT.EXE
  - \WINWORD.exe
- OriginalFileName:
  - Excel.exe
  - POWERPNT.EXE
  - WinWord.exe
selection_http:
  CommandLine|contains:
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Winword/
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Powerpnt/
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Excel/
- https://medium.com/@reegun/unsanitized-file-validation-leads-to-malicious-payload-download-via-office-binaries-202d02db7191

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_arbitrary_cli_download.yml)
