---
sigma_id: "d042284c-a296-4988-9be5-f424fadcc28c"
title: "Suspicious Execution of InstallUtil Without Log"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d042284c-a296-4988-9be5-f424fadcc28c"
  - "Suspicious Execution of InstallUtil Without Log"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution of InstallUtil Without Log

Uses the .NET InstallUtil.exe application in order to execute image without log

## Metadata

- Rule ID: d042284c-a296-4988-9be5-f424fadcc28c
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-23
- Modified: 2022-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \InstallUtil.exe
  Image|contains: Microsoft.NET\Framework
  CommandLine|contains|all:
  - '/logfile= '
  - /LogToConsole=false
condition: selection
```

## False Positives

- Unknown

## References

- https://securelist.com/moonbounce-the-dark-side-of-uefi-firmware/105468/
- https://learn.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml)
