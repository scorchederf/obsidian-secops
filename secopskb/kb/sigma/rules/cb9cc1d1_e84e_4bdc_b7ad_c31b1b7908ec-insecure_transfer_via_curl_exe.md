---
sigma_id: "cb9cc1d1-e84e-4bdc-b7ad-c31b1b7908ec"
title: "Insecure Transfer Via Curl.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_insecure_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_insecure_connection.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cb9cc1d1-e84e-4bdc-b7ad-c31b1b7908ec"
  - "Insecure Transfer Via Curl.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Insecure Transfer Via Curl.EXE

Detects execution of "curl.exe" with the "--insecure" flag.

## Metadata

- Rule ID: cb9cc1d1-e84e-4bdc-b7ad-c31b1b7908ec
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-30
- Source Path: rules/windows/process_creation/proc_creation_win_curl_insecure_connection.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \curl.exe
- OriginalFileName: curl.exe
selection_cli:
- CommandLine|re: \s-k\s
- CommandLine|contains: --insecure
condition: all of selection_*
```

## False Positives

- Access to badly maintained internal or development systems

## References

- https://curl.se/docs/manpage.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_insecure_connection.yml)
