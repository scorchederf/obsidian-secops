---
sigma_id: "cbb67ecc-fb70-4467-9350-c910bdf7c628"
title: "Added Credentials to Existing Application"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_app_credential_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_credential_added.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "cbb67ecc-fb70-4467-9350-c910bdf7c628"
  - "Added Credentials to Existing Application"
attack_technique_ids:
  - "T1098.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Added Credentials to Existing Application

Detects when a new credential is added to an existing application. Any additional credentials added outside of expected processes could be a malicious actor using those credentials.

## Metadata

- Rule ID: cbb67ecc-fb70-4467-9350-c910bdf7c628
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', Bailey Bercik '@baileybercik'
- Date: 2022-05-26
- Modified: 2025-07-18
- Source Path: rules/cloud/azure/audit_logs/azure_app_credential_added.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.001]]

## Detection

```yaml
selection:
  properties.message:
  - Update application – Certificates and secrets management
  - Update Service principal/Update Application
condition: selection
```

## False Positives

- When credentials are added/removed as part of the normal working hours/workflows

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications#application-credentials

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_app_credential_added.yml)
