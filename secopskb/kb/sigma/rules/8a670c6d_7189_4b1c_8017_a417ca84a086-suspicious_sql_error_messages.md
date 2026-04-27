---
sigma_id: "8a670c6d-7189-4b1c-8017-a417ca84a086"
title: "Suspicious SQL Error Messages"
framework: "sigma"
generated: "true"
source_path: "rules/application/sql/app_sqlinjection_errors.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/sql/app_sqlinjection_errors.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "sql / application"
aliases:
  - "8a670c6d-7189-4b1c-8017-a417ca84a086"
  - "Suspicious SQL Error Messages"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious SQL Error Messages

Detects SQL error messages that indicate probing for an injection attack

## Metadata

- Rule ID: 8a670c6d-7189-4b1c-8017-a417ca84a086
- Status: test
- Level: high
- Author: Bjoern Kimminich
- Date: 2017-11-27
- Modified: 2023-02-12
- Source Path: rules/application/sql/app_sqlinjection_errors.yml

## Logsource

- category: application
- definition: Requirements: application error logs must be collected (with LOG_LEVEL ERROR and above)
- product: sql

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- quoted string not properly terminated
- You have an error in your SQL syntax
- Unclosed quotation mark
- 'near "*": syntax error'
- SELECTs to the left and right of UNION do not have the same number of result columns
condition: keywords
```

## False Positives

- A syntax error in MySQL also occurs in non-dynamic (safe) queries if there is an empty in() clause, that may often be the case.

## References

- http://www.sqlinjection.net/errors

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/sql/app_sqlinjection_errors.yml)
