---
sigma_id: "9494bff8-959f-4440-bbce-fb87a208d517"
title: "Changes to Device Registration Policy"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/audit_logs/azure_ad_device_registration_policy_changes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_device_registration_policy_changes.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "azure / auditlogs"
aliases:
  - "9494bff8-959f-4440-bbce-fb87a208d517"
  - "Changes to Device Registration Policy"
attack_technique_ids:
  - "T1484"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Changes to Device Registration Policy

Monitor and alert for changes to the device registration policy.

## Metadata

- Rule ID: 9494bff8-959f-4440-bbce-fb87a208d517
- Status: test
- Level: high
- Author: Michael Epping, '@mepples21'
- Date: 2022-06-28
- Source Path: rules/cloud/azure/audit_logs/azure_ad_device_registration_policy_changes.yml

## Logsource

- product: azure
- service: auditlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484]]

## Detection

```yaml
selection:
  Category: Policy
  ActivityDisplayName: Set device registration policies
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/entra/architecture/security-operations-devices#device-registrations-and-joins-outside-policy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/audit_logs/azure_ad_device_registration_policy_changes.yml)
