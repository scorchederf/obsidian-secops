---
sigma_id: "c9783e20-4793-4164-ba96-d9ee483992c4"
title: "Logged-On User Password Change Via Ksetup.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ksetup_password_change_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ksetup_password_change_user.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c9783e20-4793-4164-ba96-d9ee483992c4"
  - "Logged-On User Password Change Via Ksetup.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Logged-On User Password Change Via Ksetup.EXE

Detects password change for the logged-on user's via "ksetup.exe"

## Metadata

- Rule ID: c9783e20-4793-4164-ba96-d9ee483992c4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_ksetup_password_change_user.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \ksetup.exe
- OriginalFileName: ksetup.exe
selection_cli:
  CommandLine|contains: ' /ChangePassword '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-gb/windows-server/administration/windows-commands/ksetup

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ksetup_password_change_user.yml)
