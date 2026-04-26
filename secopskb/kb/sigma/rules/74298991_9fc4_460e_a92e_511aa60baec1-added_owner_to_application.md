---
sigma_id: "74298991-9fc4-460e-a92e-511aa60baec1"
title: "Added Owner To Application"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_owner_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_owner_added.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "74298991-9fc4-460e-a92e-511aa60baec1"
  - "Added Owner To Application"
attack_technique_ids:
  - "T1552"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Added Owner To Application

Detects when a new owner is added to an application. This gives that account privileges to make modifications and configuration changes to the application.

## Metadata

- Rule ID: 74298991-9fc4-460e-a92e-511aa60baec1
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
- Date: 2022-06-02
- Source Path: rules/cloud/azure/audit_logs/azure_app_owner_added.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]

## Detection

```yaml
selection:
  properties.message: Add owner to application
condition: selection
```

## False Positives

- When a new application owner is added by an administrator

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#new-owner

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_owner_added.yml)
