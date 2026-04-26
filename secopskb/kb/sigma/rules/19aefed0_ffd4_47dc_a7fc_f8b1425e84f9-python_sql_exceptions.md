---
sigma_id: "19aefed0-ffd4-47dc-a7fc-f8b1425e84f9"
title: "Python SQL Exceptions"
framework: "sigma"
generated: "true"
source_path: "rules/application/python/app_python_sql_exceptions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/python/app_python_sql_exceptions.yml"
build_date: "2026-04-26 14:14:34"
status: "stable"
level: "medium"
logsource: "python / application"
aliases:
  - "19aefed0-ffd4-47dc-a7fc-f8b1425e84f9"
  - "Python SQL Exceptions"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Python SQL Exceptions

Generic rule for SQL exceptions in Python according to PEP 249

## Metadata

- Rule ID: 19aefed0-ffd4-47dc-a7fc-f8b1425e84f9
- Status: stable
- Level: medium
- Author: Thomas Patzke
- Date: 2017-08-12
- Modified: 2020-09-01
- Source Path: rules/application/python/app_python_sql_exceptions.yml

## Logsource

- category: application
- product: python

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- DataError
- IntegrityError
- ProgrammingError
- OperationalError
condition: keywords
```

## False Positives

- Application bugs

## References

- https://www.python.org/dev/peps/pep-0249/#exceptions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/python/app_python_sql_exceptions.yml)
