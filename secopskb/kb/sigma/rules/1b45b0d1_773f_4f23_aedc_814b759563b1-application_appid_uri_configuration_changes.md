---
sigma_id: "1b45b0d1-773f-4f23-aedc-814b759563b1"
title: "Application AppID Uri Configuration Changes"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_appid_uri_changes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_appid_uri_changes.yml"
build_date: "2026-04-26 14:14:20"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Application AppID Uri Configuration Changes

Detects when a configuration change is made to an applications AppID URI.

## Metadata

- Rule ID: 1b45b0d1-773f-4f23-aedc-814b759563b1
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
- Date: 2022-06-02
- Source Path: rules/cloud/azure/audit_logs/azure_app_appid_uri_changes.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

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
