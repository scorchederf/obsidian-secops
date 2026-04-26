---
sigma_id: "0f16d9cf-0616-45c8-8fad-becc11b5a41c"
title: "Renamed AutoHotkey.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_autohotkey.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_autohotkey.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0f16d9cf-0616-45c8-8fad-becc11b5a41c"
  - "Renamed AutoHotkey.EXE Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed AutoHotkey.EXE Execution

Detects execution of a renamed autohotkey.exe binary based on PE metadata fields

## Metadata

- Rule ID: 0f16d9cf-0616-45c8-8fad-becc11b5a41c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali
- Date: 2023-02-07
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_autohotkey.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Product|contains: AutoHotkey
- Description|contains: AutoHotkey
- OriginalFileName:
  - AutoHotkey.exe
  - AutoHotkey.rc
filter:
- Image|endswith:
  - \AutoHotkey.exe
  - \AutoHotkey32.exe
  - \AutoHotkey32_UIA.exe
  - \AutoHotkey64.exe
  - \AutoHotkey64_UIA.exe
  - \AutoHotkeyA32.exe
  - \AutoHotkeyA32_UIA.exe
  - \AutoHotkeyU32.exe
  - \AutoHotkeyU32_UIA.exe
  - \AutoHotkeyU64.exe
  - \AutoHotkeyU64_UIA.exe
- Image|contains: \AutoHotkey
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.autohotkey.com/download/
- https://thedfirreport.com/2023/02/06/collect-exfiltrate-sleep-repeat/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_autohotkey.yml)
