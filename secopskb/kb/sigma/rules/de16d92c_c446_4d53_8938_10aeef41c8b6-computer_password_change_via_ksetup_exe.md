---
sigma_id: "de16d92c-c446-4d53-8938-10aeef41c8b6"
title: "Computer Password Change Via Ksetup.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ksetup_password_change_computer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ksetup_password_change_computer.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "de16d92c-c446-4d53-8938-10aeef41c8b6"
  - "Computer Password Change Via Ksetup.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Computer Password Change Via Ksetup.EXE

Detects password change for the computer's domain account or host principal via "ksetup.exe"

## Metadata

- Rule ID: de16d92c-c446-4d53-8938-10aeef41c8b6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_ksetup_password_change_computer.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \ksetup.exe
- OriginalFileName: ksetup.exe
selection_cli:
  CommandLine|contains: ' /setcomputerpassword '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/Oddvarmoe/status/1641712700605513729
- https://learn.microsoft.com/en-gb/windows-server/administration/windows-commands/ksetup

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ksetup_password_change_computer.yml)
