---
sigma_id: "1b45b0d1-773f-4f23-aedc-814b759563b1"
title: "Application AppID Uri Configuration Changes"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_appid_uri_changes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_appid_uri_changes.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "1b45b0d1-773f-4f23-aedc-814b759563b1"
  - "Application AppID Uri Configuration Changes"
attack_technique_ids:
  - "T1552"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a configuration change is made to an applications AppID URI.

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  properties.message:
  - Update Application
  - Update Service principal
condition: selection
```

## False Positives

- When and administrator is making legitimate AppID URI configuration changes to an application. This should be a planned event.

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#appid-uri-added-modified-or-removed

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_appid_uri_changes.yml)
