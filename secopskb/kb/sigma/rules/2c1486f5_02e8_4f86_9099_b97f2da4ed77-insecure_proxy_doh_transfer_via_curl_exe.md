---
sigma_id: "2c1486f5-02e8-4f86-9099-b97f2da4ed77"
title: "Insecure Proxy/DOH Transfer Via Curl.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_insecure_proxy_or_doh.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_insecure_proxy_or_doh.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2c1486f5-02e8-4f86-9099-b97f2da4ed77"
  - "Insecure Proxy/DOH Transfer Via Curl.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Insecure Proxy/DOH Transfer Via Curl.EXE

Detects execution of "curl.exe" with the "insecure" flag over proxy or DOH.

## Metadata

- Rule ID: 2c1486f5-02e8-4f86-9099-b97f2da4ed77
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-27
- Source Path: rules/windows/process_creation/proc_creation_win_curl_insecure_proxy_or_doh.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \curl.exe
- OriginalFileName: curl.exe
selection_cli:
  CommandLine|contains:
  - --doh-insecure
  - --proxy-insecure
condition: all of selection_*
```

## False Positives

- Access to badly maintained internal or development systems

## References

- https://curl.se/docs/manpage.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_insecure_proxy_or_doh.yml)
