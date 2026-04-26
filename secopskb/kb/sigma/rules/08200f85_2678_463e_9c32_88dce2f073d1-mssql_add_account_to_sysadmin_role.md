---
sigma_id: "08200f85-2678-463e-9c32-88dce2f073d1"
title: "MSSQL Add Account To Sysadmin Role"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_add_sysadmin_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_add_sysadmin_account.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "08200f85-2678-463e-9c32-88dce2f073d1"
  - "MSSQL Add Account To Sysadmin Role"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL Add Account To Sysadmin Role

Detects when an attacker tries to backdoor the MSSQL server by adding a backdoor account to the sysadmin fixed server role

## Metadata

- Rule ID: 08200f85-2678-463e-9c32-88dce2f073d1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-13
- Modified: 2024-06-26
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_add_sysadmin_account.yml

## Logsource

- definition: Requirements: MSSQL audit policy must be enabled in order to receive this event in the application log
- product: windows
- service: application

## Detection

```yaml
selection:
  Provider_Name|contains: MSSQL
  EventID: 33205
  Data|contains|all:
  - object_name:sysadmin
  - 'statement:alter server role [sysadmin] add member '
condition: selection
```

## False Positives

- Rare legitimate administrative activity

## References

- https://www.netspi.com/blog/technical/network-penetration-testing/sql-server-persistence-part-1-startup-stored-procedures/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_add_sysadmin_account.yml)
