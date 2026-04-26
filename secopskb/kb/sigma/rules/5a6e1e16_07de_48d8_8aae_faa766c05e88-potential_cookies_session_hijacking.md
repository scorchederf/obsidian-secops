---
sigma_id: "5a6e1e16-07de-48d8-8aae-faa766c05e88"
title: "Potential Cookies Session Hijacking"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_cookie_hijacking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_cookie_hijacking.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5a6e1e16-07de-48d8-8aae-faa766c05e88"
  - "Potential Cookies Session Hijacking"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Cookies Session Hijacking

Detects execution of "curl.exe" with the "-c" flag in order to save cookie data.

## Metadata

- Rule ID: 5a6e1e16-07de-48d8-8aae-faa766c05e88
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-27
- Source Path: rules/windows/process_creation/proc_creation_win_curl_cookie_hijacking.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \curl.exe
- OriginalFileName: curl.exe
selection_cli:
- CommandLine|re: \s-c\s
- CommandLine|contains: --cookie-jar
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://curl.se/docs/manpage.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_cookie_hijacking.yml)
