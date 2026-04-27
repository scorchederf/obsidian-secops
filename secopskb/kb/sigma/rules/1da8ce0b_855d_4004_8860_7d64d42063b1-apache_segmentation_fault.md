---
sigma_id: "1da8ce0b-855d-4004-8860-7d64d42063b1"
title: "Apache Segmentation Fault"
framework: "sigma"
generated: "true"
source_path: "rules/web/product/apache/web_apache_segfault.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/product/apache/web_apache_segfault.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "apache"
aliases:
  - "1da8ce0b-855d-4004-8860-7d64d42063b1"
  - "Apache Segmentation Fault"
attack_technique_ids:
  - "T1499.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a segmentation fault error message caused by a crashing apache worker process

## Logsource

- definition: Requirements: Must be able to collect the error.log file
- service: apache

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1499-endpoint_denial_of_service#^t1499004-application-or-system-exploitation|T1499.004: Application or System Exploitation]]

## Detection

```yaml
keywords:
- exit signal Segmentation Fault
condition: keywords
```

## False Positives

- Unknown

## References

- http://www.securityfocus.com/infocus/1633

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/product/apache/web_apache_segfault.yml)
