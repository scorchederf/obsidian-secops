---
sigma_id: "34746e8c-5fb8-415a-b135-0abc167e912a"
title: "WinSxS Executable File Creation By Non-System Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_winsxs_binary_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_winsxs_binary_creation.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "34746e8c-5fb8-415a-b135-0abc167e912a"
  - "WinSxS Executable File Creation By Non-System Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WinSxS Executable File Creation By Non-System Process

Detects the creation of binaries in the WinSxS folder by non-system processes

## Metadata

- Rule ID: 34746e8c-5fb8-415a-b135-0abc167e912a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-11
- Source Path: rules/windows/file/file_event/file_event_win_susp_winsxs_binary_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\WinSxS\
  TargetFilename|endswith: .exe
filter_main_system_location:
  Image|startswith:
  - C:\Windows\Systems32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://media.defense.gov/2023/May/09/2003218554/-1/-1/0/JOINT_CSA_HUNTING_RU_INTEL_SNAKE_MALWARE_20230509.PDF

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_winsxs_binary_creation.yml)
