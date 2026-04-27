---
sigma_id: "5513deaf-f49a-46c2-a6c8-3f111b5cb453"
title: "SQL Injection Strings In URI"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_sql_injection_in_access_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_sql_injection_in_access_logs.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "5513deaf-f49a-46c2-a6c8-3f111b5cb453"
  - "SQL Injection Strings In URI"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# SQL Injection Strings In URI

Detects potential SQL injection attempts via GET requests in access logs.

## Metadata

- Rule ID: 5513deaf-f49a-46c2-a6c8-3f111b5cb453
- Status: test
- Level: high
- Author: Saw Win Naung, Nasreddine Bencherchali (Nextron Systems), Thurein Oo (Yoma Bank)
- Date: 2020-02-22
- Modified: 2023-09-04
- Source Path: rules/web/webserver_generic/web_sql_injection_in_access_logs.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  cs-method: GET
keywords:
- '@@version'
- '%271%27%3D%271'
- '=select '
- =select(
- =select%20
- concat_ws(
- CONCAT(0x
- from mysql.innodb_table_stats
- from%20mysql.innodb_table_stats
- group_concat(
- information_schema.tables
- json_arrayagg(
- or 1=1#
- or%201=1#
- 'order by '
- order%20by%20
- 'select * '
- select database()
- select version()
- select%20*%20
- select%20database()
- select%20version()
- select%28sleep%2810%29
- SELECTCHAR(
- table_schema
- UNION ALL SELECT
- UNION SELECT
- UNION%20ALL%20SELECT
- UNION%20SELECT
- '''1''=''1'
filter_main_status:
  sc-status: 404
condition: selection and keywords and not 1 of filter_main_*
```

## False Positives

- Java scripts and CSS Files
- User searches in search boxes of the respective website
- Internal vulnerability scanners can cause some serious FPs when used, if you experience a lot of FPs due to this think of adding more filters such as "User Agent" strings and more response codes

## References

- https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/
- https://www.acunetix.com/blog/articles/using-logs-to-investigate-a-web-application-attack/
- https://brightsec.com/blog/sql-injection-payloads/
- https://github.com/payloadbox/sql-injection-payload-list
- https://book.hacktricks.xyz/pentesting-web/sql-injection/mysql-injection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_sql_injection_in_access_logs.yml)
