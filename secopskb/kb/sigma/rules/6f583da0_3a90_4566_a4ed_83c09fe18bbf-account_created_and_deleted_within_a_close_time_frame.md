---
sigma_id: "6f583da0-3a90-4566-a4ed-83c09fe18bbf"
title: "Account Created And Deleted Within A Close Time Frame"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_account_created_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_account_created_deleted.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "6f583da0-3a90-4566-a4ed-83c09fe18bbf"
  - "Account Created And Deleted Within A Close Time Frame"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Account Created And Deleted Within A Close Time Frame

Detects when an account was created and deleted in a short period of time.

## Metadata

- Rule ID: 6f583da0-3a90-4566-a4ed-83c09fe18bbf
- Status: test
- Level: high
- Author: Mark Morowczynski '@markmorow', MikeDuddington, '@dudders1', Tim Shelton
- Date: 2022-08-11
- Modified: 2022-08-18
- Source Path: rules/cloud/azure/audit_logs/azure_ad_account_created_deleted.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  properties.message:
  - Add user
  - Delete user
  Status: Success
condition: selection
```

## False Positives

- Legit administrative action

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-user-accounts#short-lived-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_account_created_deleted.yml)
