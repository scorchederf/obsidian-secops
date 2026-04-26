---
sigma_id: "002bdb95-0cf1-46a6-9e08-d38c128a6127"
title: "WScript or CScript Dropper - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_cscript_wscript_dropper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_cscript_wscript_dropper.yml"
build_date: "2026-04-26 15:01:54"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "002bdb95-0cf1-46a6-9e08-d38c128a6127"
  - "WScript or CScript Dropper - File"
attack_technique_ids:
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WScript or CScript Dropper - File

Detects a file ending in jse, vbe, js, vba, vbs written by cscript.exe or wscript.exe

## Metadata

- Rule ID: 002bdb95-0cf1-46a6-9e08-d38c128a6127
- Status: test
- Level: high
- Author: Tim Shelton
- Date: 2022-01-10
- Modified: 2022-12-02
- Source Path: rules/windows/file/file_event/file_event_win_cscript_wscript_dropper.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection:
  Image|endswith:
  - \wscript.exe
  - \cscript.exe
  TargetFilename|startswith:
  - C:\Users\
  - C:\ProgramData
  TargetFilename|endswith:
  - .jse
  - .vbe
  - .js
  - .vba
  - .vbs
condition: selection
```

## False Positives

- Unknown

## References

- WScript or CScript Dropper (cea72823-df4d-4567-950c-0b579eaf0846)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_cscript_wscript_dropper.yml)
