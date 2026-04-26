---
sigma_id: "0fc35fc3-efe6-4898-8a37-0b233339524f"
title: "Suspicious ScreenSave Change by Reg.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_screensaver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_screensaver.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0fc35fc3-efe6-4898-8a37-0b233339524f"
  - "Suspicious ScreenSave Change by Reg.exe"
attack_technique_ids:
  - "T1546.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious ScreenSave Change by Reg.exe

Adversaries may establish persistence by executing malicious content triggered by user inactivity.
Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension

## Metadata

- Rule ID: 0fc35fc3-efe6-4898-8a37-0b233339524f
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-08-19
- Modified: 2022-06-02
- Source Path: rules/windows/process_creation/proc_creation_win_reg_screensaver.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.002]]

## Detection

```yaml
selection_reg:
  Image|endswith: \reg.exe
  CommandLine|contains:
  - HKEY_CURRENT_USER\Control Panel\Desktop
  - HKCU\Control Panel\Desktop
selection_option_1:
  CommandLine|contains|all:
  - /v ScreenSaveActive
  - /t REG_SZ
  - /d 1
  - /f
selection_option_2:
  CommandLine|contains|all:
  - /v ScreenSaveTimeout
  - /t REG_SZ
  - '/d '
  - /f
selection_option_3:
  CommandLine|contains|all:
  - /v ScreenSaverIsSecure
  - /t REG_SZ
  - /d 0
  - /f
selection_option_4:
  CommandLine|contains|all:
  - /v SCRNSAVE.EXE
  - /t REG_SZ
  - '/d '
  - .scr
  - /f
condition: selection_reg and 1 of selection_option_*
```

## False Positives

- GPO

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.002/T1546.002.md
- https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_screensaver.yml)
