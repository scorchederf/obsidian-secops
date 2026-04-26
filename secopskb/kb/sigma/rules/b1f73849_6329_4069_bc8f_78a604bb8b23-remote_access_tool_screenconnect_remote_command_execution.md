---
sigma_id: "b1f73849-6329-4069-bc8f-78a604bb8b23"
title: "Remote Access Tool - ScreenConnect Remote Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "b1f73849-6329-4069-bc8f-78a604bb8b23"
  - "Remote Access Tool - ScreenConnect Remote Command Execution"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect Remote Command Execution

Detects the execution of a system command via the ScreenConnect RMM service.

## Metadata

- Rule ID: b1f73849-6329-4069-bc8f-78a604bb8b23
- Status: test
- Level: low
- Author: Ali Alwashali
- Date: 2023-10-10
- Modified: 2024-02-26
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \ScreenConnect.ClientService.exe
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains: \TEMP\ScreenConnect\
condition: all of selection_*
```

## False Positives

- Legitimate use of ScreenConnect. Disable this rule if ScreenConnect is heavily used.

## References

- https://github.com/SigmaHQ/sigma/pull/4467

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution.yml)
