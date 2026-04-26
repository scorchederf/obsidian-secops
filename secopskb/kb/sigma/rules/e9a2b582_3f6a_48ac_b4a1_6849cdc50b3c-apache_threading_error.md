---
sigma_id: "e9a2b582-3f6a-48ac-b4a1-6849cdc50b3c"
title: "Apache Threading Error"
framework: "sigma"
generated: "true"
source_path: "rules/web/product/apache/web_apache_threading_error.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/product/apache/web_apache_threading_error.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "apache"
aliases:
  - "e9a2b582-3f6a-48ac-b4a1-6849cdc50b3c"
  - "Apache Threading Error"
attack_technique_ids:
  - "T1190"
  - "T1210"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Apache Threading Error

Detects an issue in apache logs that reports threading related errors

## Metadata

- Rule ID: e9a2b582-3f6a-48ac-b4a1-6849cdc50b3c
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-01-22
- Modified: 2021-11-27
- Source Path: rules/web/product/apache/web_apache_threading_error.yml

## Logsource

- definition: Requirements: Must be able to collect the error.log file
- service: apache

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1210-exploitation_of_remote_services|T1210]]

## Detection

```yaml
keywords:
- '__pthread_tpp_change_priority: Assertion `new_prio == -1 || (new_prio >= fifo_min_prio
  && new_prio <= fifo_max_prio)'
condition: keywords
```

## False Positives

- 3rd party apache modules - https://bz.apache.org/bugzilla/show_bug.cgi?id=46185

## References

- https://github.com/hannob/apache-uaf/blob/da40f2be3684c8095ec6066fa68eb5c07a086233/README.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/product/apache/web_apache_threading_error.yml)
