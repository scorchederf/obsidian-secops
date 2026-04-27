---
sigma_id: "065cceea-77ec-4030-9052-fc0affea7110"
title: "DNS Query for Anonfiles.com Domain - Sysmon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_anonymfiles_com.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_anonymfiles_com.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / dns_query"
aliases:
  - "065cceea-77ec-4030-9052-fc0affea7110"
  - "DNS Query for Anonfiles.com Domain - Sysmon"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DNS Query for Anonfiles.com Domain - Sysmon

Detects DNS queries for "anonfiles.com", which is an anonymous file upload platform often used for malicious purposes

## Metadata

- Rule ID: 065cceea-77ec-4030-9052-fc0affea7110
- Status: test
- Level: high
- Author: pH-T (Nextron Systems)
- Date: 2022-07-15
- Modified: 2023-01-16
- Source Path: rules/windows/dns_query/dns_query_win_anonymfiles_com.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  QueryName|contains: .anonfiles.com
condition: selection
```

## False Positives

- Rare legitimate access to anonfiles.com

## References

- https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbyte

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_anonymfiles_com.yml)
