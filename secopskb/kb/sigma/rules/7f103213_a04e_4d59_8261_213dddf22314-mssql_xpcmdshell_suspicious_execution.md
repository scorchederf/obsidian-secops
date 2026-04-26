---
sigma_id: "7f103213-a04e-4d59-8261-213dddf22314"
title: "MSSQL XPCmdshell Suspicious Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_audit_log.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_audit_log.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "7f103213-a04e-4d59-8261-213dddf22314"
  - "MSSQL XPCmdshell Suspicious Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL XPCmdshell Suspicious Execution

Detects when the MSSQL "xp_cmdshell" stored procedure is used to execute commands

## Metadata

- Rule ID: 7f103213-a04e-4d59-8261-213dddf22314
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-12
- Modified: 2024-06-26
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_audit_log.yml

## Logsource

- definition: Requirements: MSSQL audit policy to monitor for "xp_cmdshell" must be enabled in order to receive this event in the application log (Follow this tutorial https://dba.stackexchange.com/questions/103183/is-there-any-way-to-monitor-execution-of-xp-cmdshell-in-sql-server-2012)
- product: windows
- service: application

## Detection

```yaml
selection:
  Provider_Name|contains: MSSQL
  EventID: 33205
  Data|contains|all:
  - object_name:xp_cmdshell
  - statement:EXEC
condition: selection
```

## False Positives

- Unknown

## References

- https://www.netspi.com/blog/technical/network-penetration-testing/sql-server-persistence-part-1-startup-stored-procedures/
- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_audit_log.yml)
