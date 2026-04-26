---
sigma_id: "a0413867-daf3-43dd-9245-734b3a787942"
title: "Bitlocker Key Retrieval"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_bitlocker_key_retrieval.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_bitlocker_key_retrieval.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "azure / auditlogs"
aliases:
  - "a0413867-daf3-43dd-9245-734b3a787942"
  - "Bitlocker Key Retrieval"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitlocker Key Retrieval

Monitor and alert for Bitlocker key retrieval.

## Metadata

- Rule ID: a0413867-daf3-43dd-9245-734b3a787942
- Status: test
- Level: medium
- Author: Michael Epping, '@mepples21'
- Date: 2022-06-28
- Source Path: rules/cloud/azure/audit_logs/azure_ad_bitlocker_key_retrieval.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  Category: KeyManagement
  OperationName: Read BitLocker key
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#bitlocker-key-retrieval

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_bitlocker_key_retrieval.yml)
