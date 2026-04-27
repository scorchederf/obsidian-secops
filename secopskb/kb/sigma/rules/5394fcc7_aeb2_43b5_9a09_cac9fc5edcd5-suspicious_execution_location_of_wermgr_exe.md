---
sigma_id: "5394fcc7-aeb2-43b5-9a09-cac9fc5edcd5"
title: "Suspicious Execution Location Of Wermgr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wermgr_susp_exec_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wermgr_susp_exec_location.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5394fcc7-aeb2-43b5-9a09-cac9fc5edcd5"
  - "Suspicious Execution Location Of Wermgr.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious Windows Error Reporting manager (wermgr.exe) execution location.

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \wermgr.exe
filter_main_legit_location:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html
- https://www.echotrail.io/insights/search/wermgr.exe
- https://github.com/binderlabs/DirCreate2System

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wermgr_susp_exec_location.yml)
