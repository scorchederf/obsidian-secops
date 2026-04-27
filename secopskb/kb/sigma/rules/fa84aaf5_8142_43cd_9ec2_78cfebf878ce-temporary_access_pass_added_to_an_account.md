---
sigma_id: "fa84aaf5-8142-43cd-9ec2-78cfebf878ce"
title: "Temporary Access Pass Added To An Account"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_tap_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_tap_added.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "fa84aaf5-8142-43cd-9ec2-78cfebf878ce"
  - "Temporary Access Pass Added To An Account"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a temporary access pass (TAP) is added to an account. TAPs added to priv accounts should be investigated

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  properties.message: Admin registered security info
  Status: Admin registered temporary access pass method for user
condition: selection
```

## False Positives

- Administrator adding a legitimate temporary access pass

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-privileged-accounts#changes-to-privileged-accounts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_tap_added.yml)
