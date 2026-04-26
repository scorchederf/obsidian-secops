---
sigma_id: "d08dd86f-681e-4a00-a92c-1db218754417"
title: "MSSQL XPCmdshell Option Change"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_change.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "d08dd86f-681e-4a00-a92c-1db218754417"
  - "MSSQL XPCmdshell Option Change"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSSQL XPCmdshell Option Change

Detects when the MSSQL "xp_cmdshell" stored procedure setting is changed.

## Metadata

- Rule ID: d08dd86f-681e-4a00-a92c-1db218754417
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-12
- Modified: 2024-06-26
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_change.yml

## Logsource

- product: windows
- service: application

## Detection

```yaml
selection:
  Provider_Name|contains: MSSQL
  EventID: 15457
  Data|contains: xp_cmdshell
condition: selection
```

## False Positives

- Legitimate enable/disable of the setting
- Note that since the event contain the change for both values. This means that this will trigger on both enable and disable

## References

- https://www.netspi.com/blog/technical/network-penetration-testing/sql-server-persistence-part-1-startup-stored-procedures/
- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_xp_cmdshell_change.yml)
