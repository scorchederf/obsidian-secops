---
sigma_id: "f346bbd5-2c4e-4789-a221-72de7685090d"
title: "Google Cloud SQL Database Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_sql_database_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_sql_database_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "f346bbd5-2c4e-4789-a221-72de7685090d"
  - "Google Cloud SQL Database Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud SQL Database Modified or Deleted

Detect when a Cloud SQL DB has been modified or deleted.

## Metadata

- Rule ID: f346bbd5-2c4e-4789-a221-72de7685090d
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-10-15
- Modified: 2022-12-25
- Source Path: rules/cloud/gcp/audit/gcp_sql_database_modified_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - cloudsql.instances.create
  - cloudsql.instances.delete
  - cloudsql.users.update
  - cloudsql.users.delete
condition: selection
```

## False Positives

- SQL Database being modified or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- SQL Database modified or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/update

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_sql_database_modified_or_deleted.yml)
