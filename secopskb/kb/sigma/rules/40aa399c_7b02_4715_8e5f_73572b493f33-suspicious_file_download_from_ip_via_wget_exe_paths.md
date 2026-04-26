---
sigma_id: "40aa399c-7b02-4715-8e5f-73572b493f33"
title: "Suspicious File Download From IP Via Wget.EXE - Paths"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wget_download_susp_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wget_download_susp_locations.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "40aa399c-7b02-4715-8e5f-73572b493f33"
  - "Suspicious File Download From IP Via Wget.EXE - Paths"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious File Download From IP Via Wget.EXE - Paths

Detects potentially suspicious file downloads directly from IP addresses and stored in suspicious locations using Wget.exe

## Metadata

- Rule ID: 40aa399c-7b02-4715-8e5f-73572b493f33
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-02-23
- Source Path: rules/windows/process_creation/proc_creation_win_wget_download_susp_locations.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \wget.exe
- OriginalFileName: wget.exe
selection_ip:
  CommandLine|re: ://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
selection_http:
  CommandLine|contains: http
selection_flag:
- CommandLine|re: \s-O\s
- CommandLine|contains: --output-document
selection_paths:
- CommandLine|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\Help\
  - :\Windows\Temp\
  - \Temporary Internet
- CommandLine|contains|all:
  - :\Users\
  - \Favorites\
- CommandLine|contains|all:
  - :\Users\
  - \Favourites\
- CommandLine|contains|all:
  - :\Users\
  - \Contacts\
- CommandLine|contains|all:
  - :\Users\
  - \Pictures\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.gnu.org/software/wget/manual/wget.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wget_download_susp_locations.yml)
