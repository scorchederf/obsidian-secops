---
sigma_id: "218d2855-2bba-4f61-9c85-81d0ea63ac71"
title: "MSSQL Server Failed Logon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "windows / application"
aliases:
  - "218d2855-2bba-4f61-9c85-81d0ea63ac71"
  - "MSSQL Server Failed Logon"
attack_technique_ids:
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL Server Failed Logon

Detects failed logon attempts from clients to MSSQL server.

## Metadata

- Rule ID: 218d2855-2bba-4f61-9c85-81d0ea63ac71
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems), j4son
- Date: 2023-10-11
- Modified: 2024-06-26
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon.yml

## Logsource

- definition: Requirements: Must enable MSSQL authentication.
- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  Provider_Name|contains: MSSQL
  EventID: 18456
condition: selection
```

## False Positives

- This event could stem from users changing an account's password that's used to authenticate via a job or an automated process. Investigate the source of such events and mitigate them

## References

- https://cybersecthreat.com/2020/07/08/enable-mssql-authentication-log-to-eventlog/
- https://www.experts-exchange.com/questions/27800944/EventID-18456-Failed-to-open-the-explicitly-specified-database.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon.yml)
