---
sigma_id: "a4b25073-8947-489c-a8dd-93b41c23f26d"
title: "Windows LAPS Credential Dump From Entra ID"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_auditlogs_laps_credential_dumping.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_auditlogs_laps_credential_dumping.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "a4b25073-8947-489c-a8dd-93b41c23f26d"
  - "Windows LAPS Credential Dump From Entra ID"
attack_technique_ids:
  - "T1098.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows LAPS Credential Dump From Entra ID

Detects when an account dumps the LAPS password from Entra ID.

## Metadata

- Rule ID: a4b25073-8947-489c-a8dd-93b41c23f26d
- Status: test
- Level: high
- Author: andrewdanis
- Date: 2024-06-26
- Source Path: rules/cloud/azure/audit_logs/azure_auditlogs_laps_credential_dumping.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098.005]]

## Detection

```yaml
selection:
  category: Device
  activityType|contains: Recover device local administrator password
  additionalDetails.additionalInfo|contains: Successfully recovered local credential
    by device id
condition: selection
```

## False Positives

- Approved activity performed by an Administrator.

## References

- https://twitter.com/NathanMcNulty/status/1785051227568632263
- https://www.cloudcoffee.ch/microsoft-365/configure-windows-laps-in-microsoft-intune/
- https://techcommunity.microsoft.com/t5/microsoft-entra-blog/introducing-windows-local-administrator-password-solution-with/ba-p/1942487

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_auditlogs_laps_credential_dumping.yml)
