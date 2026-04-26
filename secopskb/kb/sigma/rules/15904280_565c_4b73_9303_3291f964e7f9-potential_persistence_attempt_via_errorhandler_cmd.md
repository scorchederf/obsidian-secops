---
sigma_id: "15904280-565c-4b73-9303-3291f964e7f9"
title: "Potential Persistence Attempt Via ErrorHandler.Cmd"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_errorhandler_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_errorhandler_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "15904280-565c-4b73-9303-3291f964e7f9"
  - "Potential Persistence Attempt Via ErrorHandler.Cmd"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Attempt Via ErrorHandler.Cmd

Detects creation of a file named "ErrorHandler.cmd" in the "C:\WINDOWS\Setup\Scripts\" directory which could be used as a method of persistence
The content of C:\WINDOWS\Setup\Scripts\ErrorHandler.cmd is read whenever some tools under C:\WINDOWS\System32\oobe\ (e.g. Setup.exe) fail to run for any reason.

## Metadata

- Rule ID: 15904280-565c-4b73-9303-3291f964e7f9
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-09
- Modified: 2022-12-19
- Source Path: rules/windows/file/file_event/file_event_win_errorhandler_persistence.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith: \WINDOWS\Setup\Scripts\ErrorHandler.cmd
condition: selection
```

## False Positives

- Unknown

## References

- https://www.hexacorn.com/blog/2022/01/16/beyond-good-ol-run-key-part-135/
- https://github.com/last-byte/PersistenceSniper

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_errorhandler_persistence.yml)
