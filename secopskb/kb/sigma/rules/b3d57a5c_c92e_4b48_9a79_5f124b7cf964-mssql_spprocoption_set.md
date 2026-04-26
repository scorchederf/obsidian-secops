---
sigma_id: "b3d57a5c-c92e-4b48-9a79-5f124b7cf964"
title: "MSSQL SPProcoption Set"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_sp_procoption_set.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_sp_procoption_set.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "b3d57a5c-c92e-4b48-9a79-5f124b7cf964"
  - "MSSQL SPProcoption Set"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL SPProcoption Set

Detects when the a stored procedure is set or cleared for automatic execution in MSSQL. A stored procedure that is set to automatic execution runs every time an instance of SQL Server is started

## Metadata

- Rule ID: b3d57a5c-c92e-4b48-9a79-5f124b7cf964
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-13
- Modified: 2024-06-26
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_sp_procoption_set.yml

## Logsource

- definition: Requirements: MSSQL audit policy to monitor for "sp_procoption" must be enabled in order to receive this event in the application log
- product: windows
- service: application

## Detection

```yaml
selection:
  Provider_Name|contains: MSSQL
  EventID: 33205
  Data|contains|all:
  - object_name:sp_procoption
  - statement:EXEC
condition: selection
```

## False Positives

- Legitimate use of the feature by administrators (rare)

## References

- https://www.netspi.com/blog/technical/network-penetration-testing/sql-server-persistence-part-1-startup-stored-procedures/
- https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-procoption-transact-sql?view=sql-server-ver16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_sp_procoption_set.yml)
