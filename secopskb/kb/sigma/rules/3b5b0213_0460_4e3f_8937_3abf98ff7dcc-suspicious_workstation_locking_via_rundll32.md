---
sigma_id: "3b5b0213-0460-4e3f-8937-3abf98ff7dcc"
title: "Suspicious Workstation Locking via Rundll32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_user32_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_user32_dll.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3b5b0213-0460-4e3f-8937-3abf98ff7dcc"
  - "Suspicious Workstation Locking via Rundll32"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Workstation Locking via Rundll32

Detects a suspicious call to the user32.dll function that locks the user workstation

## Metadata

- Rule ID: 3b5b0213-0460-4e3f-8937-3abf98ff7dcc
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-06-04
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_user32_dll.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_call_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_call_parent:
  ParentImage|endswith: \cmd.exe
selection_call_cli:
  CommandLine|contains: user32.dll,
selection_function:
  CommandLine|contains: LockWorkStation
condition: all of selection_*
```

## False Positives

- Scripts or links on the user desktop used to lock the workstation instead of Windows+L or the menu option

## References

- https://app.any.run/tasks/2aef9c63-f944-4763-b3ef-81eee209d128/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_user32_dll.yml)
