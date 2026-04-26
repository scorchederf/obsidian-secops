---
sigma_id: "36e037c4-c228-4866-b6a3-48eb292b9955"
title: "DNS Query Request By Regsvr32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_regsvr32_dns_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_regsvr32_dns_query.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "36e037c4-c228-4866-b6a3-48eb292b9955"
  - "DNS Query Request By Regsvr32.EXE"
attack_technique_ids:
  - "T1559.001"
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query Request By Regsvr32.EXE

Detects DNS queries initiated by "Regsvr32.exe"

## Metadata

- Rule ID: 36e037c4-c228-4866-b6a3-48eb292b9955
- Status: test
- Level: medium
- Author: Dmitriy Lifanov, oscd.community
- Date: 2019-10-25
- Modified: 2023-09-18
- Source Path: rules/windows/dns_query/dns_query_win_regsvr32_dns_query.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1559-inter-process_communication|T1559.001]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection:
  Image|endswith: \regsvr32.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://pentestlab.blog/2017/05/11/applocker-bypass-regsvr32/
- https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_regsvr32_dns_query.yml)
