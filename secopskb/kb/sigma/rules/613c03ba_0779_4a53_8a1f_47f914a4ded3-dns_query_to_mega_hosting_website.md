---
sigma_id: "613c03ba-0779-4a53-8a1f-47f914a4ded3"
title: "DNS Query To MEGA Hosting Website"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_mega_nz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_mega_nz.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "613c03ba-0779-4a53-8a1f-47f914a4ded3"
  - "DNS Query To MEGA Hosting Website"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To MEGA Hosting Website

Detects DNS queries for subdomains related to MEGA sharing website

## Metadata

- Rule ID: 613c03ba-0779-4a53-8a1f-47f914a4ded3
- Status: test
- Level: medium
- Author: Aaron Greetham (@beardofbinary) - NCC Group
- Date: 2021-05-26
- Modified: 2023-09-18
- Source Path: rules/windows/dns_query/dns_query_win_mega_nz.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  QueryName|contains: userstorage.mega.co.nz
condition: selection
```

## False Positives

- Legitimate DNS queries and usage of Mega

## References

- https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_mega_nz.yml)
