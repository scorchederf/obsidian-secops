---
sigma_id: "00321fee-ca72-4cce-b011-5415af3b9960"
title: "MSSQL Destructive Query"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_destructive_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_destructive_query.yml"
build_date: "2026-04-26 14:14:28"
status: "experimental"
level: "medium"
logsource: "windows / application"
aliases:
  - "00321fee-ca72-4cce-b011-5415af3b9960"
  - "MSSQL Destructive Query"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL Destructive Query

Detects the invocation of MS SQL transactions that are destructive towards table or database data, such as "DROP TABLE" or "DROP DATABASE".

## Metadata

- Rule ID: 00321fee-ca72-4cce-b011-5415af3b9960
- Status: experimental
- Level: medium
- Author: Daniel Degasperi '@d4ns4n_'
- Date: 2025-06-04
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_destructive_query.yml

## Logsource

- definition: Requirements: MSSQL audit policy must be enabled in order to receive this event (event id 33205)
- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection:
  Provider_Name: MSSQLSERVER$AUDIT
  EventID: 33205
  Data|contains:
  - statement:TRUNCATE TABLE
  - statement:DROP TABLE
  - statement:DROP DATABASE
condition: selection
```

## False Positives

- Legitimate transaction from a sysadmin.

## References

- https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-table-transact-sql?view=sql-server-ver16
- https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-database-transact-sql?view=sql-server-ver16
- https://learn.microsoft.com/en-us/sql/t-sql/statements/truncate-table-transact-sql?view=sql-server-ver16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_destructive_query.yml)
