---
sigma_id: "16905e21-66ee-42fe-b256-1318ada2d770"
title: "Start of NT Virtual DOS Machine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_16bit_application.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_16bit_application.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "16905e21-66ee-42fe-b256-1318ada2d770"
  - "Start of NT Virtual DOS Machine"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Start of NT Virtual DOS Machine

Ntvdm.exe allows the execution of 16-bit Windows applications on 32-bit Windows operating systems, as well as the execution of both 16-bit and 32-bit DOS applications

## Metadata

- Rule ID: 16905e21-66ee-42fe-b256-1318ada2d770
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-07-16
- Source Path: rules/windows/process_creation/proc_creation_win_susp_16bit_application.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \ntvdm.exe
  - \csrstub.exe
condition: selection
```

## False Positives

- Legitimate use

## References

- https://learn.microsoft.com/en-us/windows/compatibility/ntvdm-and-16-bit-app-support
- https://support.microsoft.com/fr-fr/topic/an-ms-dos-based-program-that-uses-the-ms-dos-protected-mode-interface-crashes-on-a-computer-that-is-running-windows-7-5dc739ea-987b-b458-15e4-d28d5cca63c7
- https://app.any.run/tasks/93fe92fa-8b2b-4d92-8c09-a841aed2e793/
- https://app.any.run/tasks/214094a7-0abc-4a7b-a564-1b757faed79d/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_16bit_application.yml)
