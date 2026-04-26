---
sigma_id: "0afecb6e-6223-4a82-99fb-bf5b981e92a5"
title: "Remote Access Tool - ScreenConnect Temporary File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_remote_access_tools_screenconnect_remote_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_remote_access_tools_screenconnect_remote_file.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "0afecb6e-6223-4a82-99fb-bf5b981e92a5"
  - "Remote Access Tool - ScreenConnect Temporary File"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect Temporary File

Detects the creation of files in a specific location by ScreenConnect RMM.
ScreenConnect has feature to remotely execute binaries on a target machine. These binaries will be dropped to ":\Users\<username>\Documents\ConnectWiseControl\Temp\" before execution.

## Metadata

- Rule ID: 0afecb6e-6223-4a82-99fb-bf5b981e92a5
- Status: test
- Level: low
- Author: Ali Alwashali
- Date: 2023-10-10
- Source Path: rules/windows/file/file_event/file_event_win_remote_access_tools_screenconnect_remote_file.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection:
  Image|endswith: \ScreenConnect.WindowsClient.exe
  TargetFilename|contains: \Documents\ConnectWiseControl\Temp\
condition: selection
```

## False Positives

- Legitimate use of ScreenConnect

## References

- https://github.com/SigmaHQ/sigma/pull/4467

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_remote_access_tools_screenconnect_remote_file.yml)
