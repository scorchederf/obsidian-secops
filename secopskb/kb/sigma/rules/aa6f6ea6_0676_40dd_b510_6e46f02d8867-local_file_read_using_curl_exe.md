---
sigma_id: "aa6f6ea6-0676-40dd-b510-6e46f02d8867"
title: "Local File Read Using Curl.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_local_file_read.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_local_file_read.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aa6f6ea6-0676-40dd-b510-6e46f02d8867"
  - "Local File Read Using Curl.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local File Read Using Curl.EXE

Detects execution of "curl.exe" with the "file://" protocol handler in order to read local files.

## Metadata

- Rule ID: aa6f6ea6-0676-40dd-b510-6e46f02d8867
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-27
- Source Path: rules/windows/process_creation/proc_creation_win_curl_local_file_read.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \curl.exe
- OriginalFileName: curl.exe
selection_cli:
  CommandLine|contains: file:///
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://curl.se/docs/manpage.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_local_file_read.yml)
