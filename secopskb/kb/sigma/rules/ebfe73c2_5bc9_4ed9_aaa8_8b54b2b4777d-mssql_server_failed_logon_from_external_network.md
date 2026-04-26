---
sigma_id: "ebfe73c2-5bc9-4ed9-aaa8-8b54b2b4777d"
title: "MSSQL Server Failed Logon From External Network"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon_from_external_network.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon_from_external_network.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / application"
aliases:
  - "ebfe73c2-5bc9-4ed9-aaa8-8b54b2b4777d"
  - "MSSQL Server Failed Logon From External Network"
attack_technique_ids:
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MSSQL Server Failed Logon From External Network

Detects failed logon attempts from clients with external network IP to an MSSQL server. This can be a sign of a bruteforce attack.

## Metadata

- Rule ID: ebfe73c2-5bc9-4ed9-aaa8-8b54b2b4777d
- Status: test
- Level: medium
- Author: j4son
- Date: 2023-10-11
- Modified: 2025-05-28
- Source Path: rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon_from_external_network.yml

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
filter_main_local_ips:
  Data|contains:
  - 'CLIENT: 10.'
  - 'CLIENT: 172.16.'
  - 'CLIENT: 172.17.'
  - 'CLIENT: 172.18.'
  - 'CLIENT: 172.19.'
  - 'CLIENT: 172.20.'
  - 'CLIENT: 172.21.'
  - 'CLIENT: 172.22.'
  - 'CLIENT: 172.23.'
  - 'CLIENT: 172.24.'
  - 'CLIENT: 172.25.'
  - 'CLIENT: 172.26.'
  - 'CLIENT: 172.27.'
  - 'CLIENT: 172.28.'
  - 'CLIENT: 172.29.'
  - 'CLIENT: 172.30.'
  - 'CLIENT: 172.31.'
  - 'CLIENT: 192.168.'
  - 'CLIENT: 127.'
  - 'CLIENT: 169.254.'
  - 'CLIENT: <local machine>'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://cybersecthreat.com/2020/07/08/enable-mssql-authentication-log-to-eventlog/
- https://www.experts-exchange.com/questions/27800944/EventID-18456-Failed-to-open-the-explicitly-specified-database.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/mssqlserver/win_mssql_failed_logon_from_external_network.yml)
