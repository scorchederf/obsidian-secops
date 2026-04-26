---
sigma_id: "350dfb37-3706-4cdc-9e2e-5e24bc3a46df"
title: "MSSQL Disable Audit Settings"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_disable_audit_settings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_disable_audit_settings.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "350dfb37-3706-4cdc-9e2e-5e24bc3a46df"
  - "MSSQL Disable Audit Settings"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL Disable Audit Settings

Detects when an attacker calls the "ALTER SERVER AUDIT" or "DROP SERVER AUDIT" transaction in order to delete or disable audit logs on the server

## Metadata

- Rule ID: 350dfb37-3706-4cdc-9e2e-5e24bc3a46df
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-13
- Modified: 2024-06-26
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_disable_audit_settings.yml

## Logsource

- definition: Requirements: MSSQL audit policy must be enabled in order to receive this event in the application log
- product: windows
- service: application

## Detection

```yaml
selection:
  Provider_Name|contains: MSSQL
  EventID: 33205
  Data|contains:
  - statement:ALTER SERVER AUDIT
  - statement:DROP SERVER AUDIT
condition: selection
```

## False Positives

- This event should only fire when an administrator is modifying the audit policy. Which should be a rare occurrence once it's set up

## References

- https://www.netspi.com/blog/technical/network-penetration-testing/sql-server-persistence-part-1-startup-stored-procedures/
- https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-server-audit-transact-sql?view=sql-server-ver16
- https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-server-audit-transact-sql?view=sql-server-ver16

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_disable_audit_settings.yml)
