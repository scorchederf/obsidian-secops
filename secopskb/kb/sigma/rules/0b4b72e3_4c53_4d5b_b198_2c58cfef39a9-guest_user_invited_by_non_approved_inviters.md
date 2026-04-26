---
sigma_id: "0b4b72e3-4c53-4d5b-b198-2c58cfef39a9"
title: "Guest User Invited By Non Approved Inviters"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_guest_invite_failure.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_guest_invite_failure.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "0b4b72e3-4c53-4d5b-b198-2c58cfef39a9"
  - "Guest User Invited By Non Approved Inviters"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Guest User Invited By Non Approved Inviters

Detects when a user that doesn't have permissions to invite a guest user attempts to invite one.

## Metadata

- Rule ID: 0b4b72e3-4c53-4d5b-b198-2c58cfef39a9
- Status: test
- Level: medium
- Author: Mark Morowczynski '@markmorow', Yochana Henderson, '@Yochana-H'
- Date: 2022-08-10
- Source Path: rules/cloud/azure/audit_logs/azure_guest_invite_failure.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  properties.message: Invite external user
  Status: failure
condition: selection
```

## False Positives

- A non malicious user is unaware of the proper process

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts#things-to-monitor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_guest_invite_failure.yml)
