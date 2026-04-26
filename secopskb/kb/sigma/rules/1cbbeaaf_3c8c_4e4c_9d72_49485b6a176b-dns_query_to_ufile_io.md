---
sigma_id: "1cbbeaaf-3c8c-4e4c-9d72-49485b6a176b"
title: "DNS Query To Ufile.io"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_ufile_io_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_ufile_io_query.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "windows / dns_query"
aliases:
  - "1cbbeaaf-3c8c-4e4c-9d72-49485b6a176b"
  - "DNS Query To Ufile.io"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To Ufile.io

Detects DNS queries to "ufile.io", which was seen abused by malware and threat actors as a method for data exfiltration

## Metadata

- Rule ID: 1cbbeaaf-3c8c-4e4c-9d72-49485b6a176b
- Status: test
- Level: low
- Author: yatinwad, TheDFIRReport
- Date: 2022-06-23
- Modified: 2023-09-18
- Source Path: rules/windows/dns_query/dns_query_win_ufile_io_query.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  QueryName|contains: ufile.io
condition: selection
```

## False Positives

- DNS queries for "ufile" are not malicious by nature necessarily. Investigate the source to determine the necessary actions to take

## References

- https://thedfirreport.com/2021/12/13/diavol-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_ufile_io_query.yml)
