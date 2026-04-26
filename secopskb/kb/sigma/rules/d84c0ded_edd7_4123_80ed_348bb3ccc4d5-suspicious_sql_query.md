---
sigma_id: "d84c0ded-edd7-4123-80ed-348bb3ccc4d5"
title: "Suspicious SQL Query"
framework: "sigma"
generated: "true"
source_path: "rules/category/database/db_anomalous_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/category/database/db_anomalous_query.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "database"
aliases:
  - "d84c0ded-edd7-4123-80ed-348bb3ccc4d5"
  - "Suspicious SQL Query"
attack_technique_ids:
  - "T1190"
  - "T1505.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious SQL Query

Detects suspicious SQL query keywrods that are often used during recon, exfiltration or destructive activities. Such as dropping tables and selecting wildcard fields

## Metadata

- Rule ID: d84c0ded-edd7-4123-80ed-348bb3ccc4d5
- Status: test
- Level: medium
- Author: @juju4
- Date: 2022-12-27
- Source Path: rules/category/database/db_anomalous_query.yml

## Logsource

- category: database
- definition: Requirements: Must be able to log the SQL queries

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1505-server_software_component|T1505.001]]

## Detection

```yaml
keywords:
- drop
- truncate
- dump
- select \*
condition: keywords
```

## False Positives

- Inventory and monitoring activity
- Vulnerability scanners
- Legitimate applications

## References

- https://github.com/sqlmapproject/sqlmap

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/category/database/db_anomalous_query.yml)
